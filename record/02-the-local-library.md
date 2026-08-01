# The local library

**Observed phase: 1–6 August 2026**

The early desk became a workspace for multiple documents on 1 August. A library sidebar let writers create notes, search their titles and contents, rename them, and switch between them. Importing a Markdown file created a document in the library. A short undo window supported recovery from a recent deletion.

The product decision was to keep this organization in the browser. A writer did not need an account or a synchronization service to maintain a collection of notes. Titles could follow the first heading or opening line, while an explicit rename gave the writer control over the name.

Image handling expanded on 6 August. Pasted and dropped image data moved into a separate browser database, while the document body retained references to those local assets. This matters because text and image data have different storage needs. It also means that a Markdown file containing browser-local image references is not, by itself, a complete image backup.

Local storage offers a useful privacy boundary, but it is not the same as a backup. Browser profiles, private browsing, storage limits, and clearing site data can affect access to saved work. Exporting important notes remains part of using a browser-based library responsibly. Later work added more explicit handling of storage and recovery conditions.

See the [development record](README.md) for dates and provenance.
