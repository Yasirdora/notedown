# Privacy and storage

This page describes storage and network behavior in the current development build.

## Where work is stored

| Data | Storage |
| --- | --- |
| Note text, titles, and library state | Browser localStorage |
| Appearance and editing preferences | Browser localStorage |
| Trusted Markdown baselines used by Versions | Browser localStorage |
| Pasted or dropped image files | Browser IndexedDB |
| Application files needed for offline use | Browser cache, managed by a service worker |

Storage is specific to the browser profile and site address. The library does not transfer to another browser, profile, device, or site address.

The app has no account system, built-in cloud sync, analytics integration, or endpoint for uploading document content. Local storage does not provide encryption or prevent access through the same browser profile.

## Network activity

The app downloads its files on the first visit. A service worker caches them for later offline use. Offline use requires successful caching; externally hosted images and linked pages may still need a connection.

Displaying an externally hosted image can send a request to its host, including from an exported HTML document. Opening a link visits its destination. See [images and portability](formats.md#images-and-portability) for local image and export behavior.

## Saving and backups

Notedown automatically saves edits to browser storage and displays failures if storage is full or blocked. It requests persistent storage where supported; the browser decides whether to grant it.

Clearing site data, deleting a browser profile, storage eviction, device loss, and private-browsing restrictions can remove or prevent access to saved documents. Persistent storage does not replace a backup. Keep exported copies of important documents outside the browser.

## Recovery limits

Deleting a note provides a single undo opportunity for about one minute. Deleting another note replaces that undo slot. There is no permanent trash archive.

Versions stores a trusted Markdown baseline for each note to review changes made through Page editing. It does not keep a chronological edit history. Editing in Markdown or accepting a new baseline updates the trusted source.

Editing the same library in multiple tabs can produce conflicts. The app detects incoming writes and warns when a tab has unsaved work. It does not merge conflicts or support collaborative editing.

## Exporting a backup

- Export `.md` for portable text that opens in another editor.
- Use HTML export to include available images stored by the app; external image URLs remain external.
- Use Print / save as PDF for a fixed reading copy.
- Check that the exported document opens and contains the material you need before clearing browser data.

See [formats](formats.md) for export details and the [FAQ](faq.md) for common questions.
