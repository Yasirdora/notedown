# Roadmap

Notedown is in development. This page separates capabilities present in the current browser implementation from areas still being evaluated. It is not a release schedule, and no delivery dates are promised.

## Implemented in development

- Page, Markdown, Split, and Read views.
- Local document library with search, rename, and brief delete undo.
- Automatic browser saving, visible save failures, and offline application caching.
- Common Markdown structures, tables, task lists, strikethrough, highlight, and optional footnotes.
- Slash insertion, a command palette, find, outline navigation and reordering, and table editing.
- Local image paste/drop for supported formats.
- Focus mode, reading counts, and light/dark/system appearance.
- Versions review against a trusted Markdown baseline.
- Markdown and HTML exports, browser printing to PDF, and destination-specific clipboard formats.

“Implemented” refers to the development code. It does not establish a public release, a tested browser support matrix, or universal format compatibility. The [format guide](formats.md) records current boundaries.

## Under evaluation

| Area | What needs to be established |
| --- | --- |
| Browser and accessibility coverage | Repeatable checks across browsers, input methods, assistive technology, and smaller screens |
| Backup and image portability | Clearer ways to move documents and their local images together |
| Markdown fidelity | Broader compatibility fixtures and clearer review of source changes |
| Recovery and storage guidance | Better support for storage failures and understandable recovery paths |
| Performance at document scale | Practical limits for long notes, large libraries, and image-heavy work |
| Additional syntax | Whether an extension serves a real writing need while keeping files understandable elsewhere |

## Longer-term questions

Folder-based storage, optional synchronization, collaboration, and native packaging require separate product decisions. None is available or committed through this roadmap.

The [design principles](design-principles.md) explain how future work will be judged. The [FAQ](faq.md) answers questions about the current implementation.
