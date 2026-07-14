Status: done
Created: 2026-07-12
Updated: 2026-07-12
Parent: None
Depends-On: None

# Measure and Tune Approved Apply Throughput

## Scope

Implement the measured, independently configurable embedding/write batch controls in `.10x/specs/approved-apply-throughput-measurement.md`.

## Acceptance criteria

- Satisfy every scenario and constraint in the governing specification.
- Add deterministic timing tests using a controlled clock; do not make timing assertions dependent on real model or network latency.
- Preserve the existing approved-apply progress safety guarantees and JSON compatibility except for the specified additive diagnostic fields.
- Run focused and full tests; record evidence and independent review.

## Explicit exclusions

- Live benchmarking, live apply, service-write concurrency, retries, embedding-model changes, and automatic batch-size selection.

## References

- `.10x/specs/approved-apply-throughput-measurement.md`
- `.10x/research/2026-07-12-approved-apply-throughput-options.md`
- `.10x/tickets/done/2026-07-12-approved-apply-progress.md`

## Evidence expectations

Focused CLI/apply unit tests and complete test-suite output. Any later live benchmark requires a separate ticket and explicit approval for the target namespace.

## Progress and notes

- 2026-07-12: User selected the measure-and-tune path: independent embedding/write batch controls and per-stage measurement before considering write concurrency.
- 2026-07-12: Implementation authorized; assigned to a single worker.
- 2026-07-12: Independent review found two blockers: timing calls can interrupt an apply after remote success, and stale deletes are absent from write timing/progress. Repair must preserve ordering while making timing observation best-effort and accounting for successful deletes.
- 2026-07-12: Added independent `--embedding-batch-size` (default 32), preserved 64-row `--batch-size`, added injectible monotonic elapsed/embedding/write measurements, and surfaced additive approved text/JSON diagnostics. Focused tests: 60 passed; full suite: 204 passed. Evidence: `.10x/evidence/2026-07-12-approved-apply-throughput-measurement.md`.
- 2026-07-12: Repaired review blockers: all timing observation is best-effort, including post-upsert and final-summary paths; successful stale deletes now contribute to write timing and emit post-success timing progress. Added controlled-clock regressions. Focused tests: 62 passed; full suite: 206 passed.
- 2026-07-12: Final independent review passed. Parent re-ran the full suite: 206 passed. Closure evidence: `.10x/evidence/2026-07-12-approved-apply-throughput-measurement.md`; review: `.10x/reviews/2026-07-12-approved-apply-throughput-measurement-review.md`.

## Blockers

- None.
