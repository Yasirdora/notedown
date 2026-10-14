# Product overview

Notedown is an advanced word processor for intuitive writing, in development by Yasir Dora. It combines visual editing, document formatting, and organization in a browser application. Write and revise a formatted document, arrange its sections, and inspect or edit its Markdown source.

These capabilities describe Notedown’s current development version. This repository contains product documentation and examples; the application source remains private.

## Edit and format documents

**Page** lets you edit a formatted document. **Markdown** lets you edit its source. **Split** displays both, and **Read** presents the document without editing controls. Light, dark, and system themes control the interface appearance.

Use headings, lists, quotes, tables, tasks, links, images, and code blocks to structure a document. Enable the optional Footnotes pack to add references. The [format guide](formats.md) explains the supported syntax and its limits.

## Insert, navigate, and reorganize

The slash menu inserts document elements, and the command palette provides a searchable list of actions and settings. Find locates text in the active document. Use the outline to navigate and reorder sections.

Focus mode dims surrounding paragraphs and keeps the active line near reading height. Word and character counts and an estimated reading time remain available in the status area.

## Review Markdown changes

Editing in Page view can change the Markdown used to represent the document. **Versions** compares the current Markdown with a trusted baseline and lets you restore that baseline. It does not keep a complete revision history.

## Organize a document library

Create, rename, and switch between documents in the library. Search titles and document text, or delete a document with a brief opportunity to undo. Edits are saved automatically to browser storage, and save failures remain visible.

There is no account or built-in cloud sync. Keep exports of important documents because browser storage can be cleared or become unavailable. See [privacy and storage](privacy-and-storage.md).

## Import, export, and copy

Import Markdown or plain-text files. Export Markdown, an HTML document, or use the browser's print dialog to save a PDF. Copy options adapt content for Slack, rich-text destinations such as Docs or email, Markdown, or plain text.

Markdown exports retain browser-local image references without including the image files. HTML export embeds available stored images. The [format guide](formats.md#images-and-portability) explains how to export documents containing images.

Start with the [sample documents](../examples/README.md), read the [design principles](design-principles.md), or return to the [repository overview](../README.md).
