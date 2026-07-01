Status: open
Created: 2026-06-28
Updated: 2026-06-28
Depends-On: .10x/evidence/2026-06-28-cross-corpus-live-retrieval-evals.md, .10x/evidence/2026-06-28-website-page-aggregation-experiments.md, .10x/evidence/2026-06-28-cross-site-page-aggregation-sqlmesh-validation.md, .10x/evidence/2026-06-28-repo-role-diversification-validation.md

# Website Capped Aggregation Default Review

## Scope

Review whether website namespaces should promote page-level `capped_sum_3` aggregation instead of the current `max` aggregation.

Expanded Ruff and Typer site evals improved with `page / none / pool20 / capped_sum_3`, but prior Pi-site evidence showed a tiny score regression at pool 20 while P@5 was unchanged. The user-selected promotion policy is no meaningful regressions, so default promotion requires resolving whether that prior regression is meaningful, stale, or acceptable.

## Acceptance criteria

- Compare `page/max/pool20` vs `page/capped_sum_3/pool20` across all current website validation namespaces: turbopuffer, SQLMesh, Pi, Ruff docs, and Typer docs.
- Use live retrieval-only evals; no writes, deletes, apply, stale cleanup, or namespace deletion.
- Record per-site P@5, composite score, recall, NDCG, MRR, and deltas.
- Apply the selected no-regression policy before any default change.
- If promotion is justified, update the namespace-ranking decision, docs, tests, and evidence in a separate implementation slice.

## Explicit exclusions

- No repo ranking changes.
- No website reindexing or live apply.
- No stale deletion or namespace deletion.

## Blockers

- Live retrieval-only evals still require explicit approval at execution time.

## References

- `.10x/evidence/2026-06-28-cross-corpus-live-retrieval-evals.md`
- `.10x/decisions/namespace-ranking-defaults.md`

## Progress and notes

- 2026-06-28: Opened after expanded Ruff/Typer docs evals improved with capped aggregation while existing Pi-site evidence prevents automatic promotion under no-regression policy.
