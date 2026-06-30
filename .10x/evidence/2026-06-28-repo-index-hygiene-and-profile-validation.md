Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Relates-To: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md, .10x/decisions/repo-index-hygiene-defaults.md, .10x/decisions/namespace-ranking-defaults.md

# Repo Index Hygiene and Profile Validation

## What was observed

After the repo-search/autoresearch work shipped, the public `Doctacon/turbo-search` repo had moved to commit:

```text
fd7f20cdc14f8d7769bf5305e2dd67eae415a8d2
```

Planning current `main` into the existing namespace without extra filters selected many project-memory and eval artifacts:

```text
files_discovered = 80
files_selected = 78
chunks_generated = 889
rows_to_upsert = 538
stale_rows = 81
```

Applying those changes to `github-doctacon-turbo-search-v1` was approved under the repo workflow live-write authority. No stale deletion was run.

Observed approved apply:

```text
rows_upserted = 538
embeddings_generated = 538
stale_rows_retained = 81
rows_deleted = 0
state_updated = true
```

The unfiltered current-main index degraded repo-search score because answer-key-like eval JSON and project-memory/run artifacts could outrank implementation files.

Profile and index-hygiene hypotheses were then tested:

1. Promote repo `capped_sum_3` aggregation: already improved old namespace score from `87.251` to `89.629` before reindexing current main.
2. Demote repository artifact/eval paths in `repo_code` ranking profile and lightly boost `tests/` files.
3. Exclude repository-local memory/run/eval artifacts by default during GitHub repo planning.
4. Apply a clean new namespace, `github-doctacon-turbo-search-v2-clean`, with equivalent filters and no deletes.

## Procedure

Unfiltered current-main plan:

```bash
uv run turbo-search plan https://github.com/Doctacon/turbo-search \
  --out-dir artifacts/site-crawls/github-doctacon-turbo-search-reindex-20260628 \
  --namespace github-doctacon-turbo-search-v1 \
  --json
```

Preflight and approved apply, no stale deletion:

```bash
uv run turbo-search apply \
  --plan artifacts/site-crawls/github-doctacon-turbo-search-reindex-20260628/plan.json \
  --namespace github-doctacon-turbo-search-v1 \
  --json

uv run turbo-search apply \
  --plan artifacts/site-crawls/github-doctacon-turbo-search-reindex-20260628/plan.json \
  --namespace github-doctacon-turbo-search-v1 \
  --approve \
  --json
```

Clean namespace plan used artifact/eval excludes:

```bash
uv run turbo-search plan https://github.com/Doctacon/turbo-search \
  --out-dir artifacts/site-crawls/github-doctacon-turbo-search-clean-20260628 \
  --namespace github-doctacon-turbo-search-v2-clean \
  --exclude-path '.10x/**' \
  --exclude-path '.loom/**' \
  --exclude-path '.pi/**' \
  --exclude-path '.claude/**' \
  --exclude-path '.cursor/**' \
  --exclude-path '.turbo-search/**' \
  --exclude-path 'autoresearch/**' \
  --exclude-path 'artifacts/**' \
  --exclude-path 'src/turbo_search/data/*eval*.json' \
  --json
```

Clean namespace apply:

```bash
uv run turbo-search apply \
  --plan artifacts/site-crawls/github-doctacon-turbo-search-clean-20260628/plan.json \
  --namespace github-doctacon-turbo-search-v2-clean \
  --approve \
  --json
```

Default-exclusion source validation, local only:

```bash
uv run turbo-search plan https://github.com/Doctacon/turbo-search \
  --out-dir artifacts/site-crawls/github-doctacon-turbo-search-default-excludes-20260628 \
  --namespace github-doctacon-turbo-search-v2-default-excludes \
  --json
```

Observed default-exclusion plan without explicit `--exclude-path`:

```text
files_discovered = 80
files_selected = 29
files_skipped_filtered = 50
chunks_generated = 497
rows_to_upsert = 497
first_apply = true
turbopuffer_api_calls = false
```

Validation commands:

```bash
uv run python -m unittest tests.test_github_repo tests.test_retriever tests.test_cli tests.test_autoresearch tests.test_evals
uv run python -m unittest discover tests
git diff --check
```

Observed:

```text
69 tests OK
134 tests OK
git diff --check: no whitespace errors
```

## Results

### Current main, unfiltered existing namespace

| Namespace | Variant | P@5 | Score | NDCG | Recall | MRR |
|---|---|---:|---:|---:|---:|---:|
| `github-doctacon-turbo-search-v1` | unfiltered current-main, max | 0.420 | 57.875 | 0.564 | 0.808 | 0.431 |
| `github-doctacon-turbo-search-v1` | unfiltered current-main, capped_sum_3 | 0.460 | 71.346 | 0.714 | 0.833 | 0.720 |
| `github-doctacon-turbo-search-v1` | after artifact/profile demotion | 0.480 | 84.321 | 0.872 | 0.867 | 0.950 |

### Clean current-main namespace

| Namespace | Variant | P@5 | Score | NDCG | Recall | MRR |
|---|---|---:|---:|---:|---:|---:|
| `github-doctacon-turbo-search-v2-clean` | max | 0.500 | 84.091 | 0.885 | 0.808 | 0.950 |
| `github-doctacon-turbo-search-v2-clean` | capped_sum_3 before profile update | 0.520 | 87.035 | 0.902 | 0.900 | 0.950 |
| `github-doctacon-turbo-search-v2-clean` | capped_sum_3 after artifact/profile update | 0.520 | 88.125 | 0.908 | 0.900 | 1.000 |

## What this supports or challenges

Supports:

- Index hygiene matters more than another reranker on the shipped repo: indexing `.10x`, `autoresearch`, and eval seed JSON materially hurt score.
- `capped_sum_3` remains better than `max` on clean current-main indexing for `turbo-search`; later cross-repo validation kept it opt-in rather than universal default.
- The `repo_code` profile should demote process/run/eval artifacts and lightly boost `tests/` files.
- Default GitHub repo planning should exclude project-memory/run/eval artifacts so future namespaces do not need manual excludes.

Challenges / limits:

- The current `github-doctacon-turbo-search-v1` namespace now contains unfiltered current-main rows plus retained stale rows; no deletion was run.
- The clean namespace improves over the polluted current-main namespace but does not exceed the old pre-reindex score of `89.629`; current-main source content changed, and the eval now retrieves new adjacent `autoresearch` implementation in some eval-related queries.
- Results remain based on one repository seed eval, not a broad multi-repo benchmark.

## Conclusion

For `turbo-search` specifically, the best line from this evidence was:

```text
namespace = github-doctacon-turbo-search-v2-clean
ranking = file / repo_code / pool100 / capped_sum_3
score = 88.125
```

Later query-intent work improved the opt-in capped `turbo-search` score further, while cross-repo Requests validation kept the universal repo default at `max`. Default repo planning and `repo_code` ranking were updated so future GitHub repo indexes avoid the artifact pollution found in the shipped repository.
