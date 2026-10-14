# Frequently asked questions

## What is Notedown?

An advanced word processor for intuitive writing, in development by Yasir Dora. It runs in the browser and combines visual editing, document formatting, Markdown access, a document library, and export tools. See the [product overview](product-overview.md).

## Is this the application source repository?

No. This repository publishes documentation and sample documents. Application source is maintained privately. Repository activity does not itself indicate a public app release.

## Where are my documents stored?

In storage belonging to the browser profile and site address you use. Document text and preferences use localStorage; pasted or dropped images use IndexedDB. There is no built-in cross-device sync. Read [privacy and storage](privacy-and-storage.md) for storage limits and backup options.

## Can I write offline?

Yes, after the app has loaded and successfully cached its files. External images and links may still require a connection.

## Does the app send my writing to a server?

The current implementation has no document-upload service or analytics integration. Displaying a remote image can contact its host, and opening a link visits its destination.

## Do I need to back up my documents?

Yes. Clearing site data, deleting a profile, storage limits, device loss, and private browsing restrictions can affect saved work. Export important documents and verify the copies. A visible save error means the browser has not accepted the latest write.

## How should I export a document with images?

HTML export embeds available images stored by the app. Markdown exports retain browser-local `asset:` references and do not include the image bytes. Remote image URLs remain remote in either format. See [images and portability](formats.md#images-and-portability).

## Is Versions a complete edit history?

No. It compares the document with a trusted Markdown baseline to help review Page editing changes. Keeping a new baseline or intentionally editing the source updates that reference. It is not a chronological backup archive.

## How do I use footnotes?

Open the command palette with `⌘ K` on macOS or `Ctrl K` on Windows and Linux, then choose the footnotes toggle. The syntax stays literal when the pack is off. The [research note](../examples/research-note.md) provides a small example.

## Which Markdown features are supported?

Notedown supports common Markdown and selected extensions, including tables, task lists, strikethrough, highlight, and optional footnotes. Raw HTML is displayed as text. Math and Mermaid do not have dedicated rendering. See the [format guide](formats.md) for supported syntax and limits.

## Are native apps, collaboration, or sync available?

The current implementation is a browser app. It does not include native desktop/mobile apps, shared editing, or cloud sync. The [roadmap](roadmap.md) distinguishes implemented features from ideas under evaluation.

## Does Copy for Slack send a message?

No. It puts adapted text on the clipboard for you to paste. Copy for Docs / Email likewise prepares clipboard content without connecting to those services.

Return to the [repository overview](../README.md).
