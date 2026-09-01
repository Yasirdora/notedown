# Privacy and storage

This page describes the current Notedown browser implementation in development. It is a product behavior guide, not a claim about a future hosted service. The application source is maintained privately.

## Where work is stored

| Data | Storage |
| --- | --- |
| Note text, titles, and library state | Browser localStorage |
| Appearance and editing preferences | Browser localStorage |
| Trusted Markdown baselines used by Versions | Browser localStorage |
| Pasted or dropped image files | Browser IndexedDB |
| Application files needed for offline use | Browser cache, managed by a service worker |

These stores belong to the browser profile and site address being used. Opening another browser, profile, or device does not transfer the library. A change of site address can also give the app a separate storage area.

The current app has no account system, built-in cloud sync, analytics integration, or document-content upload endpoint. Local storage does not imply encryption or protection from someone with access to the same browser profile.

## Network activity

Loading the app initially requires its files. A service worker caches application resources to support later offline use once caching succeeds.

An image linked to an external address can make a request to that host when displayed, including from an exported HTML document. Opening a link visits its destination. For a document that should remain independent of external image hosts, use supported local images and review the [export options](formats.md#images-and-portability).

Offline support depends on the app having loaded and cached successfully. It does not guarantee that every external image or link will be available without a connection.

## What “saved” means

Notedown automatically writes edits to browser storage and displays failures if storage is full or blocked. It also requests persistent storage where the browser provides that capability. The browser decides whether to grant it.

Saved work is still vulnerable to clearing site data, deleting a browser profile, storage eviction, device loss, or restrictions in private browsing. Keep exported copies of important documents outside the browser. A persistent-storage grant does not replace a backup.

## Recovery limits

Deleting a note provides a single undo opportunity for about one minute. Deleting another note replaces that undo slot. There is no permanent trash archive.

Versions retains a trusted source baseline for each note and helps review changes caused by Page editing. It does not keep a chronological archive of every edit. Intentional edits in Markdown and accepting a new baseline update what is trusted.

Editing the same library in multiple tabs can produce conflicting changes. The app detects incoming writes and warns when a tab has unsaved work; this is not shared editing or a conflict-merging system.

## Keeping an independent copy

- Export `.md` for portable text that opens in another editor.
- Use HTML export to include available images stored by the app; external image URLs remain external.
- Use Print / save as PDF for a fixed reading copy.
- Check that the exported document opens and contains the material you need before clearing browser data.

See [formats](formats.md) for export details and the [FAQ](faq.md) for common questions.
