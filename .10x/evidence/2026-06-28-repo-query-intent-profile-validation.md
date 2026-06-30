Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Relates-To: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md, .10x/decisions/namespace-ranking-defaults.md

# Repo Query-Intent Profile Validation

## What was observed

Implemented query-aware `repo_code` profile behavior to address implementation-vs-experiment intent confusion.

The failure mode was: implementation/eval queries could rank experiment/autoresearch files above the direct implementation file because the lexical match was plausible. Example before the fix on the clean `turbo-search` namespace:

```text
evals-composite-metrics top hits included:
1. tests/test_evals.py
2. src/turbo_search/autoresearch.py
3. tests/test_autoresearch.py
4. src/turbo_search/evals.py
```

The fix:

- tokenize the user query and repo path;
- demote experiment-like paths (`autoresearch`, `experiment`, `fixture`, `hypothesis`, `benchmark`) when the query does not explicitly ask for experiment/autoresearch material;
- lightly boost `src/` files for implementation-intent queries using terms such as `implemented`, `implementation`, `source`, `function`, or `logic`;
- preserve experiment/autoresearch files when the query explicitly mentions them.

## Procedure

Validation commands:

```bash
uv run python -m unittest tests.test_retriever tests.test_cli tests.test_autoresearch tests.test_evals tests.test_github_repo
uv run python -m unittest discover tests
git diff --check
```

Observed:

```text
70 tests OK
135 tests OK
git diff --check: no whitespace errors
```

Live retrieval-only validation on the clean `turbo-search` namespace:

```bash
uv run turbo-search evals \
  --live \
  --dataset src/turbo_search/data/turbo_search_repo_search_seed_evals.json \
  --namespace github-doctacon-turbo-search-v2-clean \
  --top-k 10 \
  --candidates 200
```

Artifacts:

- `autoresearch/runs/repo-query-intent-profile-20260628/eval-clean-query-intent-default.json`
- `autoresearch/runs/repo-query-intent-profile-20260628/eval-clean-query-intent-max.json`
- `autoresearch/runs/repo-query-intent-profile-20260628/summary.json`
- `autoresearch/runs/repo-query-intent-profile-20260628/report.md`

## Results

Using opt-in capped aggregation on the clean `turbo-search` namespace after the query-intent profile fix:

```text
Precision@5 = 0.540
NDCG@10 = 0.924
Recall@10 = 0.900
MRR@10 = 1.000
repo_search_score = 89.197
passed = 10/10
```

Using the cross-repo-safe max aggregation default after the same profile fix:

```text
Precision@5 = 0.520
NDCG@10 = 0.906
Recall@10 = 0.833
MRR@10 = 1.000
repo_search_score = 86.697
passed = 10/10
```

The implementation-vs-experiment fix improved the targeted behavior and made `src/turbo_search/evals.py` more competitive for implementation-intent eval metric queries while preserving explicit autoresearch queries.

## Limits

- This is a heuristic profile, not learned reranking.
- It is intentionally conservative and only affects `repo_code` profile ranking.
- Capped aggregation remains opt-in after `psf/requests` showed it does not generalize as a default.
