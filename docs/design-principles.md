# Design principles

Notedown combines visual document editing, Markdown access, and document organization in a browser-based word processor. These principles guide its editing controls, storage behavior, and development priorities.

## Keep Markdown accessible

Documents use Markdown. Writers should be able to inspect, edit, and export the source. Export guidance must explain which files and images are included and which still depend on browser storage or external hosts.

## Make formatting and structure intuitive

Headings, paragraphs, lists, and tables should be readable while editing. Insertion and formatting controls should identify the action and the content it affects. Document navigation and section reordering should help writers revise longer documents.

## Explain changes to Markdown

Editing a formatted document can change its Markdown representation. Notedown should explain those changes and provide a way to review them. Versions compares the current source with a trusted baseline; it does not guarantee identical source or provide a complete edit history.

## Report save results accurately

A save indicator should confirm a successful write. Storage failures must remain visible, with instructions for preserving unsaved work. Browser storage can become unavailable, so writers need exports for independent copies.

## Describe storage and network behavior

The current app stores documents in the browser without an account or a content-upload service. External images can contact their hosts. Documentation should explain where data is stored, when network requests occur, and what can cause data loss.

## Provide clear controls and keyboard commands

Menus, the command palette, keyboard shortcuts, and direct manipulation should make document actions easy to find and use. Optional extensions should explain their syntax and how to enable them. Footnotes, for example, are opt-in.

## Prioritize documented writing tasks

Feature proposals should identify the writing task, the problem, and the expected improvement. The [roadmap](roadmap.md) separates current capabilities from proposals still under evaluation.

See the [product overview](product-overview.md) and [privacy and storage](privacy-and-storage.md) for how these principles apply today.
