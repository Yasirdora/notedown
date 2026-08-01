# Product overview

Notedown is a browser-based Markdown writing app in development by Yasir Dora. It pairs an editable, typeset page with the plain text underneath, so a note can move from first draft to a readable document in the same workspace.

These capabilities describe Notedown’s current development version. This repository contains product documentation and examples; the application source remains private.

## One document, several views

**Page** offers a formatted writing surface. **Markdown** exposes the source. **Split** puts both alongside each other, and **Read** presents the document without editing controls. Light, dark, and system themes adjust the workspace.

Headings, lists, quotes, tables, tasks, links, images, and code blocks give everyday notes enough structure. Footnotes are an optional extension. The [format guide](formats.md) explains the supported syntax and its limits.

## Tools close to the writing

The slash menu inserts structure, while the command palette brings document actions and settings into a searchable list. Find locates text in the active document. The outline helps navigate and reorder sections.

Focus mode dims surrounding paragraphs and keeps the active line near reading height. Word and character counts and an estimated reading time remain available in the status area.

**Versions** lets writers inspect Page-to-Markdown changes against a trusted source baseline, then keep or restore changes. It is a source-review tool, not a complete revision archive.

## A library in the browser

The document library supports multiple notes, title and body search, renaming, and deletion with a brief undo opportunity. Edits are saved automatically to browser storage, and save failures remain visible.

There is no account or built-in cloud sync. Browser storage has limits, so exporting important work is part of a dependable workflow. See [privacy and storage](privacy-and-storage.md).

## Portable output

Import Markdown or plain-text files. Export Markdown, an HTML document, or use the browser's print dialog to save a PDF. Copy options adapt content for Slack, rich-text destinations such as Docs or email, Markdown, or plain text.

Stored images need particular care: Markdown exports retain browser-local image references, while HTML export embeds available stored images. The [format guide](formats.md#images-and-portability) explains the distinction.

Start with the sample documents, read the [design principles](design-principles.md), or return to the [repository overview](../README.md).
