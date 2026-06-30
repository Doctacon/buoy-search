Status: active
Created: 2026-06-28
Updated: 2026-06-28

# Repository Index Hygiene Defaults

## Context

After shipping the repo-search/autoresearch work, the public `Doctacon/turbo-search` repository contained many project-memory and evaluation artifacts in addition to source code and docs. Re-indexing current `main` into the existing repo namespace without additional filtering introduced answer-key-like files such as `src/turbo_search/data/*eval*.json`, `.10x/` records, and `autoresearch/` artifacts into retrieval results.

Observed effect on `github-doctacon-turbo-search-v1` after applying current `main` without stale deletion:

```text
polluted current-main index, max aggregation:        Score = 57.875
polluted current-main index, capped_sum_3 default:  Score = 71.346
```

The strongest pollution came from eval seed JSON and project-memory/run artifacts outranking implementation files for implementation-oriented queries.

A clean namespace excluding memory/run/eval artifacts and using the repo ranking default recovered score:

```text
github-doctacon-turbo-search-v2-clean: Score = 88.125
```

## Decision

Default GitHub repository planning excludes repository-local artifacts that are not normally useful implementation search targets:

```text
.10x/
.claude/
.cursor/
.loom/
.pi/
.turbo-search/
artifacts/
autoresearch/
```

Default GitHub repository planning also excludes eval/fixture/dataset JSON under `/data/` when the path contains one of:

```text
eval
fixture
seed
dataset
```

The `repo_code` ranking profile also strongly demotes these artifact/eval paths when they are already present in an existing namespace, and lightly boosts `tests/` files because repository search questions often ask where behavior is validated.

## Alternatives considered

- Keep indexing all git-tracked text files: rejected because shipped project-memory/eval artifacts materially degraded repo search score.
- Require users to pass `--exclude-path` manually: rejected because the noisy categories are common generated/project-memory surfaces and safe to exclude by default.
- Delete stale rows from the existing namespace: deferred because stale deletion requires separate explicit approval and was not needed to validate a clean namespace.
- Exclude all JSON or all data files: rejected as too broad; some repositories legitimately store source/config data in JSON. The default only excludes eval/fixture/dataset-like JSON under `/data/`.
- Exclude `tests/`: rejected because tests are frequently relevant validation sources and are part of the eval judgments.

## Consequences

- New GitHub repo indexes are more focused on source, tests, configuration, README/docs, and other user-facing material.
- Existing polluted namespaces can improve through the `repo_code` profile demotions without requiring deletion, but the cleanest result comes from a new filtered namespace or explicit stale cleanup.
- Users can still override with `--include-path` when they intentionally want to index a normally excluded artifact path.

## Evidence

- `.10x/evidence/2026-06-28-repo-index-hygiene-and-profile-validation.md`
