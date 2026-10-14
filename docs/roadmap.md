# Roadmap

Notedown is in development. This roadmap lists implemented features and areas under evaluation. Release dates have not been set.

## Implemented features

- Page, Markdown, Split, and Read views.
- Local document library with search, rename, and brief delete undo.
- Automatic browser saving, visible save failures, and offline application caching.
- Headings, lists, quotes, code, tables, task lists, strikethrough, highlight, and optional footnotes.
- Slash insertion, a command palette, find, outline navigation and reordering, and table editing.
- Local image paste/drop for supported formats.
- Focus mode, reading counts, and light/dark/system appearance.
- Versions review against a trusted Markdown baseline.
- Markdown and HTML exports, browser printing to PDF, and destination-specific clipboard formats.

These features are present in the development build. Browser support has not been fully tested. See the [format guide](formats.md) for syntax and export limitations.

## Under evaluation

| Area | What needs to be established |
| --- | --- |
| Browser and accessibility support | Testing across browsers, input methods, assistive technology, and smaller screens |
| Backup and image portability | Exporting documents and their local images together |
| Markdown fidelity | More compatibility tests and improved review of source changes |
| Recovery and storage guidance | Handling storage failures and documenting recovery steps |
| Performance | Measuring limits for long documents, large libraries, and documents with many images |
| Additional syntax | Evaluating useful extensions and their compatibility with other editors |

## Undecided features

Folder-based storage, synchronization, collaboration, and native packaging are not available. No implementation commitments have been made for these features.

See the [design principles](design-principles.md) and [FAQ](faq.md) for more detail.
