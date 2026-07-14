Status: active
Created: 2026-07-14
Updated: 2026-07-14
Parent: None
Depends-On: None

# Make Planning Single-Pass and Stage-Timed

## Scope

Measure sitemap-policy, crawl, corpus write, chunking, diff, artifact construction, and publication durations; reuse each source's existing `IndexingPlan`; construct/serialize complete artifacts once while preserving outputs, hashes, progress, and source behavior.

## Acceptance criteria

- Website, repository, and local-document plan paths call corpus processing once.
- Complete chunk serialization/artifact construction occurs once per plan.
- Diagnostic timing is best-effort and cannot fail planning.
- Existing manifests/chunks/diffs/hash compatibility remain stable.
- Focused call-count/equivalence tests, full suite, retained-corpus benchmark, and review pass.

## Exclusions

Live crawl benchmarking without approval, chunk semantic changes, crawler rewrite, and concurrency changes.

## References

- `.10x/reviews/2026-07-14-buoy-performance-ux-codebase-review.md`

## Progress and notes

- 2026-07-14: Reused source-built `IndexingPlan` across website/repository/local-document plans, reduced complete artifact construction to one call, added best-effort stage timing, and added focused coverage. Full 247-test suite/build/lock/diff checks pass. Retained 8,749-chunk corpus benchmark reduced duplicate post-fetch work from median 6.350s to 3.195s (49.7%). Evidence: `.10x/evidence/2026-07-14-single-pass-plan-and-stage-timing.md`.
- 2026-07-14: Repaired closure-test gap with exact one-process/one-artifact assertions for website, repository, and local-document plan paths plus old-pattern/full-rebuild equivalence coverage (only `created_at` treated as volatile). Focused 145 and full 248 tests, build, lock, and diff checks pass.

## Blockers

- Required independent review before closure.
