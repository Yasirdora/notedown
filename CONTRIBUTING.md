# Contributing to Notedown

This repository holds product documentation, examples, and images. Application
source is private, so application code changes cannot be submitted here.

## Report a problem

Use the [bug report form](https://github.com/yasirdora/notedown/issues/new?template=bug_report.yml).
Include the browser and operating system, the view you were using, the steps
that reproduce the problem, and what you expected to happen. A short, invented
Markdown example is usually more useful than a screenshot alone.

For export or storage problems, say which format or action was involved and
whether Notedown showed a warning. Preserve your own backup before experimenting.
Never attach private notes, browser-storage dumps, tokens, or personal data.

Security reports belong in the [private reporting process](SECURITY.md).

## Suggest an improvement

Use the [feature request form](https://github.com/yasirdora/notedown/issues/new?template=feature_request.yml).
Describe the writing task, where the current workflow gets in the way, and an
example of a useful outcome. Check the [roadmap](docs/roadmap.md) and existing
issues first. Feature requests are considered without a delivery commitment.

## Improve these materials

For a correction, open a focused pull request that explains the error and the
evidence for the replacement. Keep prose plain, distinguish current behavior
from future ideas, and preserve relative links. Use original example text and
include useful alternative text with images.

The licence permits proposed changes submitted to this repository; it does not
grant rights in the application. Submit only material you are entitled to share.
By submitting it, you permit the maintainer to use, edit, and publish your
contribution as part of these materials under this repository's licence.

## Check a documentation change

With Python 3.9 or later installed, run:

```sh
python3 scripts/check_repository.py
```

The check validates local document links and fragments, required public files,
example checksums, image files, and the publication file boundary. The included
GitHub workflow runs the same check on pushes and pull requests once published.
It does not test the private app.
If you intentionally edit an example, update its SHA-256 entry in
`examples/checksums.json` as part of the same change.

Keep discussion respectful, specific, and focused on the work. Reports and
contributions are reviewed as time allows; this repository offers no response
time guarantee.
