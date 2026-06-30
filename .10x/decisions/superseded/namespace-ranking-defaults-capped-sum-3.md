Status: superseded
Created: 2026-06-28
Updated: 2026-06-28

# Namespace Ranking Defaults

Superseded-By: `.10x/decisions/namespace-ranking-defaults.md`

## Context

`turbo-search` now supports namespace-aware final ranking after hybrid ANN + BM25 + RRF. Website and repository indexes have different duplicate patterns:

- website rows need page-level deduplication by canonical URL;
- GitHub repository rows need file-level grouping by `repo_path`;
- repository files can have multiple independently relevant chunks, so single-best-chunk `max` aggregation can under-rank files with repeated evidence.

The prior website default decision preserved repository aggregation as `max` while promoting website page ranking. A later repo-specific experiment tested file-level `capped_sum_3` aggregation on the existing `github-doctacon-turbo-search-v1` namespace and improved the repo eval:

```text
legacy repo max default:      Precision@5 = 0.500, Recall@10 = 0.833, NDCG@10 = 0.920, Score = 87.251
repo capped_sum_3 default:   Precision@5 = 0.520, Recall@10 = 0.900, NDCG@10 = 0.935, Score = 89.629
```

Website evidence still supports keeping website aggregation as `max` at pool 20 because capped aggregation was not uniformly better for the precision-oriented website default.

This decision supersedes `.10x/decisions/superseded/website-ranking-defaults.md` by preserving its website default and updating repository aggregation.

## Decision

Use namespace-aware defaults:

Website namespaces (`site-*`):

```text
candidates = 200
ranking_mode = page
ranking_profile = none
ranking_pool = 20
ranking_aggregation = max
```

Repository/general namespaces, including GitHub namespaces:

```text
candidates = 200
ranking_mode = file
ranking_profile = repo_code
ranking_pool = 100
ranking_aggregation = capped_sum_3
```

User-supplied CLI/config ranking options continue to override namespace defaults.

## Alternatives considered

- Keep repository aggregation at `max`: rejected because live retrieval-only validation showed lower Precision@5, Recall@10, NDCG@10, and composite score on the repo seed eval.
- Promote larger repository ranking pools: rejected for now because `pool=100` matched or beat larger pools in the current grid while keeping less post-processing work.
- Promote `capped_sum_3` for website namespaces too: rejected for now because website experiments showed mixed site/pool behavior and max remained the safer precision-oriented website default.
- Re-index with path/symbol metadata before changing defaults: deferred because capped aggregation improves score without live writes or schema changes.

## Consequences

- Repository retrieval/evals without explicit ranking flags now reward up to three matching chunks from the same file.
- Website defaults remain page/none/pool20/max.
- `--ranking-aggregation max` remains available to inspect legacy single-best-chunk file/page ranking.
- Raw chunk order remains available through `--ranking-mode chunk --ranking-profile none`.
- Further repo score improvements should target remaining Recall@10/NDCG gaps after the capped aggregation baseline and the repository index hygiene/profile baseline in `.10x/decisions/repo-index-hygiene-defaults.md`.

## Evidence

- `.10x/evidence/2026-06-28-repo-search-file-ranking-promotion-validation.md`
- `.10x/evidence/2026-06-28-repo-capped-aggregation-default-promotion.md`
- `.10x/evidence/2026-06-28-repo-index-hygiene-and-profile-validation.md`
- `.10x/evidence/2026-06-28-website-ranking-evidence-hardening.md`
