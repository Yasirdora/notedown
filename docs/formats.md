# Formats and Markdown support

Notedown stores documents as Markdown. Its custom parser supports the syntax below, including several GitHub-flavored features, but does not fully conform to CommonMark or GFM.

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

Supported fenced-code languages receive syntax highlighting; other languages display as plain code. Raw HTML displays as text. Math notation and Mermaid diagrams are not rendered.

Enable **Footnotes** in the command palette to number references by first appearance and collect definitions at the end with return links. When disabled, footnote syntax displays as text. See the [research-note example](../examples/research-note.md).

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

PDF output depends on the browser's print settings. Rich clipboard output depends on browser permissions and the receiving application. Copy options format content for pasting; they do not connect to or send content through Slack, Docs, or email services.

## Images and portability

Pasted or dropped files can be PNG, JPEG, GIF, or WebP. Their bytes are stored in IndexedDB, while the Markdown contains an `asset:<id>` reference.

A Markdown export retains the reference but **does not include the image file**. Local image references will not resolve on another device or after their browser storage is cleared. Exporting `.md` alone does not back up these images.

HTML export embeds available stored images as data URLs. It cannot recover missing images. Remote image URLs remain remote and may require a connection. Relative image paths require the referenced files.

## Page editing and source fidelity

Page editing converts the formatted document back to Markdown. This can change heading styles, emphasis markers, spacing, or list markers while retaining equivalent formatting.

Versions compares the result with a trusted Markdown baseline for review or restoration. Use Markdown view when exact source structure matters, and check exports in the application where you intend to use them.

See [sample documents](../examples/README.md), [privacy and storage](privacy-and-storage.md), and the [product overview](product-overview.md).
