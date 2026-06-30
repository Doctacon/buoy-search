Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Relates-To: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md, .10x/decisions/namespace-ranking-defaults.md

# Repo Path/Symbol Ranking Validation

## What was observed

Implemented a conservative scoring-only path/symbol enhancement inside the existing `repo_code` ranking profile. It uses retrieval fields already returned from turbopuffer and does not require schema changes, reindexing, namespace cleanup, or stale deletion.

Signals added:

- exact-ish query token match against source file stems, e.g. `hooks` -> `src/requests/hooks.py`;
- exact-ish query token match against documentation file stems, e.g. `API` -> `docs/api.rst`, partially recovering the docs demotion without making docs outrank neutral source files;
- Python `def`/`class` declaration tokens from candidate chunk content, aggregated across all chunks in a file group;
- the strongest path/symbol signal across the grouped file is used so a later chunk containing the relevant symbol can help the file-level representative.

No live writes, deletes, reindexing, or state mutation were performed for this validation.

## Procedure

Regression tests:

```bash
uv run python -m unittest tests.test_retriever
uv run python -m unittest discover tests
git diff --check
```

Observed:

```text
15 tests OK
137 tests OK
git diff --check: no whitespace errors
```

Live retrieval-only evals:

```bash
uv run turbo-search evals \
  --live \
  --dataset src/turbo_search/data/turbo_search_repo_search_seed_evals.json \
  --namespace github-doctacon-turbo-search-v2-clean \
  --top-k 10 \
  --candidates 200 \
  --json

uv run turbo-search evals \
  --live \
  --dataset src/turbo_search/data/requests_repo_search_seed_evals.json \
  --namespace github-psf-requests-v1 \
  --top-k 10 \
  --candidates 200 \
  --json
```

Artifacts:

- `autoresearch/runs/repo-path-symbol-ranking-20260628/turbo-default-path-symbol.json`
- `autoresearch/runs/repo-path-symbol-ranking-20260628/requests-default-path-symbol.json`
- `autoresearch/runs/repo-path-symbol-ranking-20260628/summary.json`
- `autoresearch/runs/repo-path-symbol-ranking-20260628/report.md`

## Results

Baseline is the previous cross-repo-safe repo default: `file / repo_code / pool100 / max` before the path/symbol scorer.

| Corpus | Namespace | Score before | Score after | Δ score | P@5 before | P@5 after | Δ P@5 | NDCG@10 | Recall@10 | MRR@10 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| turbo-search | `github-doctacon-turbo-search-v2-clean` | 86.697 | 87.126 | +0.430 | 0.520 | 0.520 | +0.000 | 0.914 | 0.833 | 1.000 |
| psf/requests | `github-psf-requests-v1` | 81.809 | 82.547 | +0.738 | 0.360 | 0.400 | +0.040 | 0.877 | 0.767 | 1.000 |

## What this supports or challenges

Supports:

- Scoring-only path/symbol ranking is a safe universal-default improvement across the two current repo validation corpora.
- Using the strongest signal across a file group matters because a symbol-bearing chunk may not be the representative chunk selected by best fused rank.
- Exact documentation filename recovery can improve precision on public library repos while still leaving docs below neutral source files after the base docs demotion.

Challenges / limits:

- The improvement is modest; it does not solve low Requests Precision@5 by itself.
- Symbol extraction is currently Python-only and regex-based over retrieved chunk content. It does not parse full files and does not create durable symbol metadata.
- Recall@10 is unchanged. Broader gains likely require schema/index metadata for path tokens and symbols, or more labeled repos before a learned/adaptive scorer.

## Conclusion

Promote the conservative scoring-only path/symbol scorer as part of the existing universal `repo_code` default. It improves both validation repos without changing the namespace default shape:

```text
file / repo_code / pool100 / max
```
