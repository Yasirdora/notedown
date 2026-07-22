# Design principles

Notedown is built around a simple aim: make writing feel direct while keeping the document understandable outside the app. These principles guide the development implementation and future decisions.

## Keep the words accessible

Markdown is the document's working form. Writers can inspect the source, edit it directly, and export it. A clear explanation of image portability matters as much as the export button itself.

## Let the page do the work

The writing surface should be readable before it is decorated. Structure belongs in headings, paragraphs, lists, and tables. Controls should appear where they help a writer act without competing with the document.

## Make transformations visible

Editing a formatted page can change how Markdown is written. Notedown should explain those changes and offer a way to review them. Versions compares the current source with a trusted baseline; it should never be described as a guarantee of identical source or a complete history.

## Treat saving as a responsibility

A save indicator should reflect a successful write. Storage failures must stay visible, and recovery advice must be practical. Browser persistence is useful, but exports remain necessary for independent copies.

## Keep privacy claims precise

The current app stores notes in the browser without an account or a content-upload service. External images can still contact their hosts. Documentation should describe what happens to a writer's data in concrete terms rather than rely on an absolute slogan.

## Make power discoverable

Menus, a command palette, keyboard shortcuts, and direct manipulation should provide understandable routes to the same work. Additional syntax should be deliberate and identified; footnotes, for example, are opt-in.

## Build from observed needs

A feature earns its place when it improves a real writing task. Future ideas belong in the roadmap with a clear distinction between current behavior and work still under evaluation.

See the [product overview](product-overview.md) and privacy and storage for how these principles apply today.
