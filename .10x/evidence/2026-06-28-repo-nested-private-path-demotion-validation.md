Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Relates-To: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md, .10x/decisions/namespace-ranking-defaults.md, .10x/knowledge/repo-search-ranking-defaults.md

# Repo Nested Private Path Demotion Validation

## What was observed

A third ranking-only hypothesis passed the five-repo no-regression policy after the documentation path demotion baseline: demote nested private package/topic directories when their private segment is absent from the query.

Promoted behavior in the `repo_code` profile:

- A nested private path segment is a non-package-root directory segment beginning with `_`, such as `typer/_click/core.py`'s `_click` segment.
- Package roots are exempt: `src/_pytest/logging.py` treats `_pytest` as the package root, not as a nested private topic.
- If the query contains tokens related to the private segment, there is no demotion. For example, `Click command conversion` does not demote `typer/_click/core.py`.
- If the query does not mention the private segment, the file receives a `0.80` multiplier.

This is retrieval/ranking-only. It does not change indexing, namespaces, row schema, embeddings, or live writes.

## Procedure

Exploration before the passing result:

- Continued ranking-profile hypotheses against cached live retrieval candidates from the baseline repo namespaces.
- Tested root package source boosts, top-level source-like boosts, filename/path overlap boosts, test-query boosts, docs-query boosts, dunder/internal file demotions, and nested-private path demotion.
- Root package source boosts passed but were smaller; path/filename boosts regressed turbo-search/pytest; dunder demotion regressed Typer; nested-private path demotion had the best no-regression result.
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

- `autoresearch/runs/repo-nested-private-path-demotion-20260628/nested-private-path-demotion-summary.json`
- `autoresearch/runs/repo-nested-private-path-demotion-20260628/nested-private-path-demotion-report.md`
- per-repo eval JSON files under `autoresearch/runs/repo-nested-private-path-demotion-20260628/`

No plan/apply, row writes, stale deletion, or namespace deletion was run for this validation.

## Result

Baseline is the immediately previous promoted documentation path demotion result from `autoresearch/runs/repo-doc-path-demotion-20260628/doc-path-demotion-summary.json`.

| Repo | Baseline score | New score | Δ score | Baseline P@5 | New P@5 | Δ P@5 |
|---|---:|---:|---:|---:|---:|---:|
| turbo-search | 87.760 | 87.760 | +0.000 | 0.540 | 0.540 | +0.000 |
| Requests | 84.426 | 84.426 | +0.000 | 0.420 | 0.420 | +0.000 |
| Click | 72.816 | 72.816 | +0.000 | 0.420 | 0.420 | +0.000 |
| pytest | 89.191 | 89.191 | +0.000 | 0.720 | 0.720 | +0.000 |
| Typer | 62.787 | 64.411 | +1.624 | 0.420 | 0.440 | +0.020 |

Averages across the five-repo basket:

- Score: `79.396 -> 79.721` (`+0.325`)
- P@5: `0.504 -> 0.508` (`+0.004`)

## What this supports or challenges

Supports:

- Nested private implementation/vendor-topic directories can be distractors when the query does not name that topic.
- Query-aware demotion is safer than universally demoting all private directories or all private files.
- The package-root exemption avoids demoting projects whose import package itself starts with `_`, such as pytest's `src/_pytest/`.

Challenges/limits:

- The eval labels are still assistant-drafted.
- The improvement is concentrated in Typer; the other validation repos are unchanged.
- This does not make metadata preambles, file cards, oversize indexing, or broad path/filename overlap boosts default-safe.

## Conclusion

Promote nested private path-segment demotion inside the default `repo_code` ranking profile. It is the next valid no-regression improvement after the query-aware documentation path demotion.
