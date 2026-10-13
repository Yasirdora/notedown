#!/usr/bin/env python3
"""Check the public documentation repository using Python 3.9+ only."""

import hashlib
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import struct
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parent.parent
DIRECTORIES = {"docs", "examples", "media", "record", ".github", "scripts"}
ROOT_FILES = {
    "README.md", "LICENSE", "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md",
    ".editorconfig", ".gitattributes", ".gitignore",
}
REQUIRED = {
    "README.md", "LICENSE", "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md",
    "media/logo.svg", "examples/checksums.json",
}
TEXT_SUFFIXES = {".md", ".txt", ".json", ".yml", ".yaml", ".html", ".svg"}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg"}
PRIVATE_NAMES = {".aws", ".ssh", ".codex", ".codedirector", "credentials", "secrets"}
ERRORS = []
TEXT = {}


def error(path, message):
    ERRORS.append("{}: {}".format(path, message))


def public_files():
    files = []
    for directory, children, names in os.walk(ROOT, followlinks=False):
        parent = Path(directory)
        children[:] = sorted(name for name in children if name not in {".git", "__pycache__"})
        for name in children[:]:
            candidate = parent / name
            if candidate.is_symlink():
                error(candidate.relative_to(ROOT), "symlink directories are not permitted")
                children.remove(name)
        for name in sorted(names):
            path = parent / name
            relative = path.relative_to(ROOT)
            if path.is_symlink():
                error(relative, "symlink files are not permitted")
                continue
            files.append(path)
            if len(relative.parts) == 1:
                if name not in ROOT_FILES:
                    error(relative, "unexpected root file")
            elif relative.parts[0] not in DIRECTORIES:
                error(relative, "outside the public directory allowlist")
            if any(part.lower() in PRIVATE_NAMES or part.lower().startswith(".env")
                   for part in relative.parts):
                error(relative, "private configuration or credential filename")
            if name.lower().startswith(("id_rsa", "id_ed25519", "credentials.", "secrets.")):
                error(relative, "private credential filename")
            allowed = path.suffix.lower() in TEXT_SUFFIXES | IMAGE_SUFFIXES
            allowed = allowed or str(relative) == "scripts/check_repository.py"
            allowed = allowed or (len(relative.parts) == 1 and name in ROOT_FILES)
            if not allowed:
                error(relative, "unsupported file type; application source is not public material")
    return files


def without_fences(text):
    result, fence = [], None
    for line in text.splitlines(keepends=True):
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
            result.append("\n")
        elif match:
            fence = match[1]
            result.append("\n")
        else:
            result.append(line)
    return "".join(result)


class Attributes(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links, self.ids = [], set()
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        for key, value in attributes:
            if value is not None and key in {"href", "src"}:
                self.links.append(value)
            if value is not None and (key == "id" or (tag == "a" and key == "name")):
                self.ids.add(value)


def fragments(text):
    clean = without_fences(text)
    identifiers = Attributes(clean).ids
    headings = []
    for match in re.finditer(r"^ {0,3}#{1,6}[ \t]+(.+?)\s*#*\s*$", clean, re.M):
        headings.append((match.start(), match[1]))
    for match in re.finditer(r"^([^\n]+)\n {0,3}(?:=+|-+)[ \t]*$", clean, re.M):
        headings.append((match.start(), match[1]))
    for match in re.finditer(r"<h[1-6]\b[^>]*>(.*?)</h[1-6]>", clean, re.I | re.S):
        headings.append((match.start(), match[1]))
    used = set()
    for _, heading in sorted(headings):
        heading = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", heading)
        heading = html.unescape(re.sub(r"<[^>]+>", "", heading)).lower().strip()
        slug = re.sub(r"[^\w\- ]", "", heading).replace(" ", "-")
        unique, count = slug, 0
        while unique in used:
            count += 1
            unique = "{}-{}".format(slug, count)
        used.add(unique)
        identifiers.add(unique)
    return identifiers


def links(text):
    clean = without_fences(text)
    clean = re.sub(r"(`+).*?\1", "", clean)
    found = Attributes(clean).links
    pattern = r"!?\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s)]+))(?:\s+[^)\n]*)?\)"
    for match in re.finditer(pattern, clean):
        found.append(match[1] or match[2])
    for match in re.finditer(r"^ {0,3}\[(?!\^)[^\]\n]+\]:\s*(?:<([^>\n]+)>|(\S+))", clean, re.M):
        found.append(match[1] or match[2])
    return found


def check_link(source, destination):
    relative = source.relative_to(ROOT)
    try:
        url = urlsplit(html.unescape(destination))
    except ValueError:
        error(relative, "invalid link: " + destination)
        return
    if url.scheme or url.netloc:
        return
    name = unquote(url.path)
    target = (ROOT / name.lstrip("/") if name.startswith("/") else source.parent / name) if name else source
    target = target.resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        error(relative, "link escapes the repository: " + destination)
        return
    if not target.exists():
        error(relative, "missing local link target: " + destination)
        return
    if target.is_dir():
        target = next((target / name for name in ("README.md", "index.md", "index.html")
                       if (target / name).is_file()), target)
    if url.fragment and target in TEXT:
        fragment = unquote(url.fragment)
        anchors = fragments(TEXT[target])
        if fragment not in anchors and not (fragment.startswith("user-content-") and fragment[13:] in anchors):
            error(relative, "missing heading or anchor: " + destination)


def jpeg_dimensions(data):
    if not data.startswith(b"\xff\xd8") or not data.endswith(b"\xff\xd9"):
        raise ValueError("invalid JPEG start or end marker")
    position = 2
    while position + 4 <= len(data):
        if data[position] != 255:
            raise ValueError("invalid JPEG segment")
        while position < len(data) and data[position] == 255:
            position += 1
        if position >= len(data):
            break
        marker = data[position]
        position += 1
        if marker == 0xDA:
            break
        if marker in {0x01, 0xD8, 0xD9} or 0xD0 <= marker <= 0xD7:
            continue
        length = int.from_bytes(data[position:position + 2], "big")
        if length < 2 or position + length > len(data):
            raise ValueError("invalid JPEG segment length")
        if marker in {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}:
            if length < 8:
                raise ValueError("truncated JPEG dimensions")
            height, width = struct.unpack(">HH", data[position + 3:position + 7])
            return width, height
        position += length
    raise ValueError("JPEG dimensions not found")


def check_image(path, data):
    relative = path.relative_to(ROOT)
    try:
        if path.suffix.lower() == ".svg":
            root = ET.fromstring(data)
            if root.tag not in {"svg", "{http://www.w3.org/2000/svg}svg"}:
                raise ValueError("SVG root element must be svg")
            return
        if path.suffix.lower() == ".png":
            if len(data) < 33 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
                raise ValueError("invalid PNG signature or header")
            if struct.unpack(">I", data[8:12])[0] != 13:
                raise ValueError("invalid PNG dimension header")
            width, height = struct.unpack(">II", data[16:24])
        else:
            width, height = jpeg_dimensions(data)
        if not (0 < width <= 32768 and 0 < height <= 32768):
            raise ValueError("invalid image dimensions {}x{}".format(width, height))
    except (ValueError, ET.ParseError, struct.error) as exception:
        error(relative, str(exception))


def check_examples(files):
    manifest = ROOT / "examples/checksums.json"
    if manifest not in TEXT:
        return
    try:
        checksums = json.loads(TEXT[manifest])
        if not isinstance(checksums, dict):
            raise ValueError("expected a JSON object of filename: SHA-256 pairs")
    except (ValueError, json.JSONDecodeError) as exception:
        error("examples/checksums.json", str(exception))
        return
    examples = {str(path.relative_to(ROOT / "examples")): path for path in files
                if path.relative_to(ROOT).parts[0] == "examples" and path.name not in {"README.md", "checksums.json"}}
    for name in sorted(examples.keys() - checksums.keys()):
        error("examples/checksums.json", "missing example checksum: " + name)
    for name in sorted(checksums.keys() - examples.keys()):
        error("examples/checksums.json", "checksum has no matching example: " + name)
    for name in examples.keys() & checksums.keys():
        digest = checksums[name]
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            error("examples/checksums.json", "invalid SHA-256 for " + name)
        elif hashlib.sha256(examples[name].read_bytes()).hexdigest() != digest:
            error("examples/checksums.json", "SHA-256 mismatch for " + name)


def main():
    files = public_files()
    for name in sorted(REQUIRED):
        if not (ROOT / name).is_file():
            error(name, "required public file is missing")
    for path in files:
        data = path.read_bytes()
        suffix = path.suffix.lower()
        if suffix in IMAGE_SUFFIXES | {".svg"}:
            check_image(path, data)
        if suffix in IMAGE_SUFFIXES:
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            error(path.relative_to(ROOT), "text must be UTF-8")
            continue
        TEXT[path] = text
        if b"\r" in data:
            error(path.relative_to(ROOT), "use LF line endings")
        if text.startswith("\ufeff"):
            error(path.relative_to(ROOT), "remove UTF-8 byte-order mark")
        if data and not data.endswith(b"\n"):
            error(path.relative_to(ROOT), "text must end with a newline")
    for path, text in TEXT.items():
        if path.suffix.lower() in {".md", ".html"}:
            for destination in links(text):
                check_link(path, destination)
    check_examples(files)
    if ERRORS:
        for message in sorted(set(ERRORS)):
            print("ERROR: " + message, file=sys.stderr)
        print("Repository checks failed.", file=sys.stderr)
        return 1
    print("Repository checks passed ({} files).".format(len(files)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
