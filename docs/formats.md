# Formats and Markdown support

Notedown uses a custom Markdown implementation. It supports common Markdown structures and several GitHub-flavored features; this is not a claim of complete CommonMark or GFM conformance.

## Supported syntax

| Structure | Support |
| --- | --- |
| Headings | `#` through `######`, plus underlined first- and second-level headings |
| Emphasis | Italic, bold, and `~~strikethrough~~` |
| Highlight | `==highlight==`, a Notedown extension that may display literally elsewhere |
| Lists | Bulleted, numbered, nested, and task lists |
| Quotes | Blockquotes, including nested content |
| Code | Inline code, fenced blocks, and indented blocks |
| Tables | Pipe tables with column alignment |
| Links | Inline, reference-style, and angle-bracket autolinks |
| Images | Markdown image syntax; local image handling is described below |
| Breaks | Thematic dividers and explicit line breaks |
| Footnotes | Optional pack using `[^name]` and `[^name]: definition` |

Recognized fenced-code languages receive syntax coloring. Other languages remain plain code. Raw HTML is displayed as text rather than executed. Math notation and Mermaid diagrams do not have dedicated rendering in the current implementation.

Footnotes must be enabled from the command palette. When enabled, references are numbered by first appearance, collected at the end, and linked back to their references. With the pack off, footnote syntax remains literal text. Try the [research-note example](../examples/research-note.md).

## Import and export

| Action | Format and behavior |
| --- | --- |
| Open a file | `.md`, `.markdown`, or `.txt`, read as text into a new library document |
| Export Markdown | A `.md` file containing the current source |
| Export HTML | An HTML document with styling and available stored images embedded |
| Print / save as PDF | Uses the browser's print dialog and available PDF destination |
| Copy Markdown | Current Markdown source |
| Copy plain text | Text adapted from the rendered document |
| Copy for Slack | Text adapted to Slack's formatting conventions |
| Copy for Docs / Email | Rich HTML with a plain-text fallback where rich clipboard access is unavailable |

PDF output depends on the browser's print settings. Rich clipboard results also depend on browser permissions and the receiving application. These copy options prepare content for pasting; they do not connect to or send content through those services.

## Images and portability

Pasted or dropped files can be PNG, JPEG, GIF, or WebP. Their bytes are stored in IndexedDB, while the Markdown contains an `asset:<id>` reference.

A Markdown export retains that reference. It does **not** bundle the image file, so a `.md` export containing stored images is not a complete image backup or a portable image document. Do not expect those references to resolve on another device or after clearing browser storage.

HTML export embeds available stored images as data URLs. Missing stored images cannot be reconstructed by exporting. Images already linked to remote URLs remain remote and may require a network connection; relative image paths still depend on the files they point to.

## Page editing and source fidelity

Page edits serialize the formatted document back into Markdown. Equivalent formatting may be rewritten: heading style, emphasis markers, spacing, or list markers can change.

Versions compares the result with a trusted source baseline and allows review or restoration. Use Markdown view when exact source structure matters, and check exports in the destination where they will be used.

See [sample documents](../examples/README.md), [privacy and storage](privacy-and-storage.md), and the [product overview](product-overview.md).
