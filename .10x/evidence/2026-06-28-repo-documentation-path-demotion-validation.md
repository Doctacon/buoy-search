Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Relates-To: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md, .10x/decisions/namespace-ranking-defaults.md, .10x/knowledge/repo-search-ranking-defaults.md

# Repo Documentation Path Demotion Validation

## What was observed

A second ranking-only hypothesis passed the five-repo no-regression policy after the example/demo path demotion baseline: demote documentation roots that commonly outrank implementation files for implementation-oriented repository queries.

Promoted behavior in the `repo_code` profile:

- `doc/` paths receive a `0.80` multiplier when the query is not documentation/example oriented.
- `docs/tutorial/` paths receive an additional `0.80` multiplier when the query is not documentation/tutorial/example oriented.
- Documentation/example intent tokens exempt the added demotions so explicit documentation/tutorial/example queries can still surface those files.

This is retrieval/ranking-only. It does not change indexing, namespaces, row schema, embeddings, or live writes.

## Procedure

Exploration before the passing result:

- Continued ranking-profile hypotheses against cached live retrieval candidates from the baseline repo namespaces.
- Tested top-level source-like boosts, `testing/` boosts, singular `doc/` root demotion, `docs/tutorial/` demotion, docs-extra demotion, dunder/internal typing demotions, and combinations.
- The best no-regression candidate was singular `doc/` demotion plus non-documentation `docs/tutorial/` extra demotion.
- Implemented the demotion in `src/turbo_search/retriever.py` and added unit coverage in `tests/test_retriever.py`.

Live validation command shape:

```bash
uv run turbo-search evals --live --dataset <repo-seed-dataset> \
  --namespace <existing-baseline-namespace> \
  --top-k 10 --candidates 200 --json
```

Namespaces:

- `github-doctacon-turbo-search-v2-clean`
- `github-psf-requests-v1`
- `github-pallets-click-v1`
- `github-pytest-dev-pytest-v1`
- `github-fastapi-typer-v1`

Artifacts:

- `autoresearch/runs/repo-doc-path-demotion-20260628/doc-path-demotion-summary.json`
- `autoresearch/runs/repo-doc-path-demotion-20260628/doc-path-demotion-report.md`
- per-repo eval JSON files under `autoresearch/runs/repo-doc-path-demotion-20260628/`

No plan/apply, row writes, stale deletion, or namespace deletion was run for this validation.

## Result

Baseline is the immediately previous promoted example/demo path demotion result from `autoresearch/runs/repo-example-path-demotion-20260628/example-path-demotion-summary.json`.

| Repo | Baseline score | New score | Δ score | Baseline P@5 | New P@5 | Δ P@5 |
|---|---:|---:|---:|---:|---:|---:|
| turbo-search | 87.760 | 87.760 | +0.000 | 0.540 | 0.540 | +0.000 |
| Requests | 84.426 | 84.426 | +0.000 | 0.420 | 0.420 | +0.000 |
| Click | 72.816 | 72.816 | +0.000 | 0.420 | 0.420 | +0.000 |
| pytest | 86.042 | 89.191 | +3.150 | 0.660 | 0.720 | +0.060 |
| Typer | 59.710 | 62.787 | +3.076 | 0.400 | 0.420 | +0.020 |

Averages across the five-repo basket:

- Score: `78.151 -> 79.396` (`+1.245`)
- P@5: `0.488 -> 0.504` (`+0.016`)

## What this supports or challenges

Supports:

- Singular `doc/` documentation roots, especially pytest documentation, can crowd out source/test files for implementation-oriented queries.
- `docs/tutorial/` paths, especially in Typer, are useful but often too high for implementation-oriented repository search.
- Documentation demotion should be query-aware; explicit documentation/tutorial/example queries should not receive the added demotions.

Challenges/limits:

- The eval labels are still assistant-drafted.
- The no-regression claim is at the repository validation-target level. Some individual query cases move down while the repo aggregate improves; future human labels should decide whether per-query no-regression is required before learned ranking work.
- This does not make metadata preambles, file cards, or oversize indexing default-safe.

## Conclusion

Promote query-aware `doc/` and `docs/tutorial/` demotion inside the default `repo_code` ranking profile. It is the next valid no-regression improvement after the conditional example/demo path demotion.
