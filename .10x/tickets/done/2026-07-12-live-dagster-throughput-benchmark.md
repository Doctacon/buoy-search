Status: done
Created: 2026-07-12
Updated: 2026-07-13
Parent: None
Depends-On: .10x/tickets/done/2026-07-12-approved-apply-throughput-measurement.md

# Live Dagster Approved-Apply Throughput Benchmark

## Scope

Run one fresh Dagster plan and one full approved apply to the explicitly authorized new namespace `site-dagster-io-benchmark-v1`, using a 128-row Turbopuffer write batch and 64-item local embedding computation batch. Record observed stage timings.

## Acceptance criteria

- Crawl and plan only `https://dagster.io/` with existing conservative/default crawl behavior; inspect the generated plan and preflight before embedding or remote writes.
- Apply only the inspected plan to `site-dagster-io-benchmark-v1` with `--batch-size 128 --embedding-batch-size 64 --approve`.
- Do not use `--delete-stale`, delete a namespace, modify the existing `site-dagster-io-v1`, or run a second live apply.
- Record rows, effective batch settings, elapsed/embedding/write timing, apply summary, and artifact cleanup outcome without exposing credentials.

## Explicit exclusions

- Retrieval smoke test, concurrency, retries, model changes, automatic tuning, and reuse/mutation of prior namespaces.

## References

- `.10x/specs/approved-apply-throughput-measurement.md`
- `.10x/research/2026-07-12-approved-apply-throughput-options.md`
- `.10x/tickets/done/2026-07-12-approved-apply-throughput-measurement.md`

## Evidence expectations

Plan/preflight/apply summaries, timing observations, namespace identity, and final local state/artifact status.

## Progress and notes

- 2026-07-12: User explicitly authorized the named new namespace and settings through the live-benchmark checkpoint.
- 2026-07-12: Execution authorized; assigned to a single worker.
- 2026-07-13: Fresh plan completed in 241.34 seconds: 1,164 pages and 25,322 chunks, no errors or reached limits. Exact-plan preflight was local-only and projected 25,322 first-apply upserts with no stale rows/deletes.
- 2026-07-13: One approved apply to `site-dagster-io-benchmark-v1` completed with `--batch-size 128 --embedding-batch-size 64`; 25,322 rows upserted, zero deleted. Instrumented elapsed/embedding/write durations: 707.575/521.829/165.997 seconds. The plan directory was removed and the new DuckDB ledger contains 25,322 applied rows. Evidence: `.10x/evidence/2026-07-13-live-dagster-throughput-benchmark.md`.
- 2026-07-13: Review identified a date mismatch, unsupported percentage wording, and insufficient retained raw output. Corrected the evidence date to match the ledger, retained sanitized raw plan/preflight/apply JSON, and corrected timing percentages.
- 2026-07-13: Final independent review passed. Closure evidence: `.10x/evidence/2026-07-13-live-dagster-throughput-benchmark.md`; review: `.10x/reviews/2026-07-13-live-dagster-throughput-benchmark-review.md`.

## Blockers

- None.
