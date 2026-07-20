Status: open
Created: 2026-07-19
Updated: 2026-07-19
Parent: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md
Depends-On: None

# C1: Freeze Repo Ranking Experiment Contract

## Scope

Create the immutable local evaluation contract shared by C3-C8. Inventory the 13 checked-in repo-search datasets and their 90 unique cases; pin source snapshot/manifests; verify every judgment path; freeze dataset hashes, repository-grouped folds, namespace/source-commit mapping, metrics, pilot/full gates, deterministic tolerances, and a hash-addressed artifact schema.

The 13-repo basket is:

- 10 cases each: Buoy, Requests, Click, pytest, Typer;
- 5 cases each: Black, Ruff, Flask, Django, Pydantic, HTTPX, MkDocs, Rich;
- 90 total known cases.

The paired baseline for an index-changing experiment MUST be the current promoted default on the same source commit and selected corpus as its candidate. The historical routed result `80.316` / P@5 `0.517` is a secondary reference only.

## Acceptance criteria

- Exactly 13 expected dataset files and 90 unique case IDs load under the active eval schema.
- Every nonzero and explicit-zero judgment path is checked against a pinned repository source manifest; dataset and manifest hashes are recorded.
- Exact repo, source commit, baseline namespace, experiment namespace pattern, model contract, and corpus-selection mapping fields are defined without creating a namespace.
- Repository-grouped folds are frozen before tuning; no case from a held-out repository may enter that fold's training or selection data.
- Primary metrics are repo composite score and Precision@5; NDCG@10, Recall@10, MRR@10, and per-case deltas remain reported diagnostics.
- Pilot/full gates reuse the active `.10x/decisions/repo-ranking-promotion-policy.md`: no repo score regression, no repo P@5 regression, positive score on at least 3 repos for a full basket, largest gain share at most 70%, and improved all-repo average score. Three-repo pilots require no score/P@5 regression, positive average score, and at least two improving repos.
- The immutable raw-candidate schema needed by C3/C7/C8 is defined, including namespace-qualified hit identity, path/content/section fields, ANN rank, BM25 rank, fused rank/score, query ID, retrieval options, source commit, namespace, model compatibility, and dataset hash.
- Determinism/tolerance rules, artifact hash procedure, credential/provider redaction, request-count accounting, and missing-repo handling are explicit.
- No label-quality or human-ground-truth claim is made.

## Stop conditions

- If a checked-in judgment path cannot be reproduced from the pinned source manifest, mark only that repository insufficient and exclude it explicitly; do not rewrite, replace, or silently reinterpret labels.
- If unique case identity, source snapshot, namespace/source compatibility, or held-out grouping cannot be frozen, dependent comparison work remains blocked.
- Do not read credentials, load/download a model, call live retrieval, generate embeddings, write/delete a namespace, change a catalog, or modify datasets.

## Evidence expectations

A durable contract/evidence record containing the dataset/manifest inventory and hashes, 13-repo mapping, folds, gates, artifact schema, validation commands/output, explicit insufficient repositories if any, and confirmation that all work was local/read-only.

## Blockers

None. This is the first executable child and is record/local-inspection only.

## Explicit exclusions

Label edits or review; candidate retrieval; model research or selection; generated experiment code; source/tests; namespace/catalog/default changes; experiment execution; promotion.

## References

- `.10x/research/2026-07-19-repo-search-heavy-ranking-experiment-decomposition.md`
- `.10x/specs/repo-search-eval-autoresearch.md`
- `.10x/decisions/repo-ranking-promotion-policy.md`
- `.10x/evidence/2026-06-28-expanded-repo-ranking-basket-validation.md`

## Progress and notes

- 2026-07-19: Opened as the executable contract-freeze prerequisite. No freeze work was performed during decomposition.
