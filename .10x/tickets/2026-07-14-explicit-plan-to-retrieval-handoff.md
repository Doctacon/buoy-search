Status: blocked
Created: 2026-07-14
Updated: 2026-07-14
Parent: None
Depends-On: None

# Make the Plan-to-Retrieval Handoff Explicit

## Scope

Shape and implement one coherent operator handoff: decision-complete apply preflight text, copy-ready retrieval commands after plan/apply, and fail-fast live retrieval when namespace is neither explicitly supplied nor environment-sourced.

## Candidate acceptance

- Human preflight shows selected source/plan, artifact/model, first-apply state, embed/upsert/unchanged/stale counts, and retain/delete intent.
- Live retrieval without operator-sourced namespace fails before model, credentials, or API work.
- Plan/apply output provides a copy-ready command using the actual namespace.
- JSON remains the automation contract and schema changes are additive only when ratified.

## References

- `.10x/reviews/2026-07-14-buoy-performance-ux-codebase-review.md`

## Blockers

- Requires user ratification of the live-namespace compatibility break and exact output contract before specification/implementation.
