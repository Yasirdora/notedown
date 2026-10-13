# Source review and recovery

**Observed phase: 14 October 2026, building on August source-review work**

A readable editing surface creates a difficult obligation: changes to presentation should not quietly obscure changes to the underlying document. Source review began in early August, and the source seal became enabled by default on 10 August. It compares the current Markdown with a trusted baseline and supports reviewing differences.

Work recorded on 14 October returned to that boundary. It addressed cases where page handling could rewrite Markdown, strengthened shared rules for interpreting document structure, and separated source-review behavior from the main interface so its rules could be exercised more directly.

Saving and recovery received parallel attention. The recorded changes covered pending text at the end of a session, storage failures, export integrity, and coordination between two tabs using the same local library. Other work requested persistent browser storage and improved the offline application path. Keyboard and screen-reader interactions also received targeted corrections.

These efforts serve different safeguards. Source review helps a writer inspect document changes. Save feedback helps reveal a failed write. Coordination between tabs reduces conflicting updates. Export gives the writer a separate copy outside the site's storage. None replaces the others, and a trusted source baseline is not a complete backup system.

Browser persistence can be unavailable or denied, and site data can still be removed. Important work should therefore have an exported copy whose contents the writer has checked.

See the [development record](README.md) for dates and provenance.
