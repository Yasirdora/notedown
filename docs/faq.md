# Frequently asked questions

## What is Notedown?

A browser-based Markdown writing app in development by Yasir Dora. It offers a formatted Page view and direct access to Markdown source, with a local document library and export tools. See the [product overview](product-overview.md).

## Is this the application source repository?

No. This repository publishes documentation and sample documents. Application source is maintained privately. Repository activity does not itself indicate a public app release.

## Where do my notes live?

In storage belonging to the browser profile and site address you use. Note text and preferences use localStorage; pasted or dropped images use IndexedDB. There is no built-in cross-device sync. Read [privacy and storage](privacy-and-storage.md) before relying on the browser as your only copy.

## Can I write offline?

The implementation caches application resources after an initial visit to support subsequent offline use. Caching must finish successfully. External images and links may still require a connection.

## Does the app send my writing to a server?

The current implementation has no document-upload service or analytics integration. Remote images can contact their hosts when displayed, and opening a link visits its destination. “Stored locally” should not be understood to mean “no network activity under any circumstances.”

## Will my documents stay saved forever?

Browser storage cannot guarantee that. Clearing site data, deleting a profile, storage limits, device loss, and private browsing restrictions can affect saved work. Export important notes and verify the copies. A visible save error means the browser has not accepted the latest write.

## How should I export a note with images?

HTML export embeds available images stored by the app. Markdown exports retain browser-local `asset:` references and do not include the image bytes. Remote image URLs remain remote in either format. See [images and portability](formats.md#images-and-portability).

## Is Versions a complete edit history?

No. It compares the document with a trusted Markdown baseline to help review Page editing changes. Keeping a new baseline or intentionally editing the source updates that reference. It is not a chronological backup archive.

## How do I use footnotes?

Open the command palette with `⌘ K` on macOS or `Ctrl K` on Windows and Linux, then choose the footnotes toggle. The syntax stays literal when the pack is off. The [research note](../examples/research-note.md) provides a small example.

## Does Notedown support every Markdown extension?

No. It supports common Markdown and selected extensions, including tables, task lists, strikethrough, highlight, and optional footnotes. Raw HTML is escaped. Math and Mermaid do not have dedicated rendering. See the [format guide](formats.md).

## Are native apps, collaboration, or sync available?

The current implementation is a browser app. It does not include native desktop/mobile apps, shared editing, or cloud sync. The [roadmap](roadmap.md) distinguishes implemented features from ideas under evaluation.

## Does Copy for Slack send a message?

No. It puts adapted text on the clipboard for you to paste. Copy for Docs / Email likewise prepares clipboard content without connecting to those services.

Return to the [repository overview](../README.md).
