Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Relates-To: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md, .10x/decisions/namespace-ranking-defaults.md

# Repo Capped Aggregation Default Promotion

Note: this promotion was later superseded by cross-repo validation on `psf/requests`; `capped_sum_3` remains opt-in and the universal repo default returned to `max`. See `.10x/evidence/2026-06-28-cross-repo-requests-validation.md`.

## What was observed

Hypothesis: repository file-level ranking should reward repeated evidence from multiple chunks in the same file, not only the best single chunk.

Implementation changed the repository/general aggregation default from `max` to `capped_sum_3` while preserving website defaults:

```text
site-* default: page / none / pool20 / max
repo default:  file / repo_code / pool100 / capped_sum_3
```

Safety:

- live turbopuffer retrieval calls only;
- no live writes;
- no stale deletes;
- no namespace deletion/replacement/management;
- no state mutation;
- no re-indexing.

Artifacts:

- `autoresearch/runs/repo-score-hypotheses-20260628/summary.json`
- `autoresearch/runs/repo-score-hypotheses-20260628/results.json`
- `autoresearch/runs/repo-score-hypotheses-20260628/report.md`
- `autoresearch/runs/repo-capped-aggregation-default-promotion-20260628/summary.json`
- `autoresearch/runs/repo-capped-aggregation-default-promotion-20260628/report.md`

## Procedure

First ran a live retrieval-only + offline post-processing grid against the existing repo namespace:

```bash
uv run python - <<'PY'
# Fetch raw live retrieval pools from github-doctacon-turbo-search-v1.
# Score file ranking variants across profile, pool, and aggregation choices.
PY
```

Then validated the selected variant through the production CLI path:

```bash
uv run turbo-search evals \
  --live \
  --dataset src/turbo_search/data/turbo_search_repo_search_seed_evals.json \
  --namespace github-doctacon-turbo-search-v1 \
  --top-k 10 \
  --candidates 200 \
  --json

uv run turbo-search evals \
  --live \
  --dataset src/turbo_search/data/turbo_search_repo_search_seed_evals.json \
  --namespace github-doctacon-turbo-search-v1 \
  --top-k 10 \
  --candidates 200 \
  --ranking-aggregation max \
  --json
```

After implementation, omitted ranking flags resolved to the promoted repo default:

```text
ranking_mode = file
ranking_profile = repo_code
ranking_pool = 100
ranking_aggregation = capped_sum_3
```

Validation commands:

```bash
uv run python -m unittest tests.test_retriever tests.test_cli tests.test_autoresearch tests.test_evals
uv run python -m unittest discover tests
git diff --check
```

Observed before this evidence record was written:

```text
56 tests OK
133 tests OK
git diff --check: no whitespace errors
```

## Results

Official live retrieval-only validation through the CLI:

| Variant | Mode | Pool | Aggregation | P@5 | ΔP@5 | Score | ΔScore | NDCG | ΔNDCG | Recall | ΔRecall | MRR |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| legacy-max | file | 100 | max | 0.500 | +0.000 | 87.251 | +0.000 | 0.920 | +0.000 | 0.833 | +0.000 | 1.000 |
| default-after-promotion | file | 100 | capped_sum_3 | 0.520 | +0.020 | 89.629 | +2.378 | 0.935 | +0.015 | 0.900 | +0.067 | 1.000 |

The offline grid selected the same winner family:

```text
file / repo_code / pool100 / capped_sum_3
Precision@5 = 0.520
repo_search_score = 89.617 in offline post-processing, 89.629 through official CLI validation
```

## What this supports or challenges

Supports:

- Repeated same-file evidence improves repository retrieval when capped at three chunks.
- `pool=100` remains the best default pool among tested values; larger pools did not improve the selected default.
- The change improves Precision@5, Recall@10, NDCG@10, and composite score without re-indexing or changing embeddings.

Challenges / limits:

- The eval remains a 10-case seed dataset for `turbo-search` repository search.
- The experiment validates one repository namespace, not a broad multi-repo benchmark.
- MRR@10 was already saturated at 1.0, so future gains must come from Recall@10, NDCG@10, and Precision@5.

## Conclusion

Promoting repository aggregation from `max` to `capped_sum_3` was validated for the then-current `turbo-search` namespace, but later cross-repo validation showed it should remain opt-in rather than the universal repo default.
