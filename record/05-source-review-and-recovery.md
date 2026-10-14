# Source review and recovery

**Observed phase: 14 October 2026, building on August source-review work**

Source review began in early August. The source seal, enabled by default on 10 August, compared the current Markdown with a trusted baseline for reviewing changes.

Work on 14 October addressed unintended Markdown rewrites during Page editing and updated shared document-parsing rules. Source review was separated from the main interface to support direct testing.

Saving and recovery changes covered pending edits at session end, storage failures, export integrity, and conflicting writes from multiple tabs. The app added persistent-storage requests and offline-loading improvements. Keyboard and screen-reader interactions received targeted fixes.

Versions stores a source baseline rather than a full edit history. Persistent storage remains subject to browser approval and does not prevent site data from being cleared. See [privacy and storage](../docs/privacy-and-storage.md) for recovery limits and backup instructions.

See the [development record](README.md) for dates and provenance.
