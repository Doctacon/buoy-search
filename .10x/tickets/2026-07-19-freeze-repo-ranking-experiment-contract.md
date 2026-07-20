Status: open
Created: 2026-07-19
Updated: 2026-07-20
Parent: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md
Depends-On: None

# C1: Freeze Repo Ranking Experiment Contract

## Scope

Create the immutable local evaluation contract shared by C3-C8. Inventory the 13 checked-in repo-search datasets and their 90 unique composite `repo_key:case_id` identities; preserve each dataset-local `case_id` and every existing label; pin source snapshot/manifests; verify every judgment path; freeze dataset hashes, repository-grouped folds, namespace/source-commit mapping, metrics, experiment-escalation/full-policy gates, deterministic tolerances, and a hash-addressed artifact schema.

The 13-repo basket is:

- 10 cases each: Buoy, Requests, Click, pytest, Typer;
- 5 cases each: Black, Ruff, Flask, Django, Pydantic, HTTPX, MkDocs, Rich;
- 90 total unique composite `repo_key:case_id` identities. Dataset-local `case_id` values remain local and MUST NOT be renamed merely because the same value appears in another repository.

The paired baseline for an index-changing experiment MUST be the current promoted default on the same source commit and selected corpus as its candidate. The historical routed result `80.316` / P@5 `0.517` is a secondary reference only.

## Acceptance criteria

- Exactly 13 expected dataset files and 90 unique composite `repo_key:case_id` identities load under the active eval schema. The contract records `repo_key`, unchanged dataset-local `case_id`, and the derived composite identity separately; it does not require dataset-local IDs to be globally unique.
- Every nonzero and explicit-zero judgment path is checked against a pinned repository source manifest; dataset and manifest hashes are recorded, and no local ID, judgment, grade, reason, or other label content is changed.
- Exact stable `repo_key`, repository, source commit, baseline namespace, experiment namespace pattern, model contract, and corpus-selection mapping fields are defined without creating a namespace.
- Repository-grouped folds are frozen before tuning; no case from a held-out repository may enter that fold's training or selection data.
- Primary metrics are repo composite score and Precision@5; NDCG@10, Recall@10, MRR@10, and per-case deltas remain reported diagnostics.
- Full-basket default candidates reuse the active `.10x/decisions/repo-ranking-promotion-policy.md`: no repo score regression, no repo P@5 regression, positive score on at least 3 repos, largest gain share at most 70%, and improved all-repo average score. Separately, three-repo pilots use no score/P@5 regression, positive average score, and at least two improving repos only as an experiment escalation gate for deciding whether to request a separately approved full-basket run; that pilot rule is not active promotion policy or promotion authority.
- The immutable raw-candidate schema needed by C3/C7/C8 is defined, including `repo_key`, unchanged dataset-local `case_id`, derived composite `repo_key:case_id`, namespace-qualified hit identity, path/content/section fields, ANN rank, BM25 rank, fused rank/score, retrieval options, source commit, namespace, model compatibility, and dataset hash. Cache keys and joins MUST use the composite identity rather than assuming local `case_id` is globally unique.
- Determinism/tolerance rules, artifact hash procedure, credential/provider redaction, request-count accounting, and missing-repo handling are explicit.
- C1 MUST NOT define or infer C7 material-weight/sign/order thresholds or C8 oracle-gap measures/thresholds. It may reserve schema fields for later pre-registered values, but completing C1 does not make C7 or C8 executable; each remains blocked until its thresholds are user-ratified.
- No label-quality or human-ground-truth claim is made.

## Stop conditions

- If a checked-in judgment path cannot be reproduced from the pinned source manifest, mark only that repository insufficient and exclude it explicitly; do not rewrite, replace, or silently reinterpret labels.
- If all 90 composite `repo_key:case_id` identities, source snapshot, namespace/source compatibility, or held-out grouping cannot be frozen, dependent comparison work remains blocked. Duplicate dataset-local `case_id` values across different repositories are not an error.
- Do not read credentials, load/download a model, call live retrieval, generate embeddings, write/delete a namespace, change a catalog, or modify datasets.

## Evidence expectations

A durable contract/evidence record containing the dataset/manifest inventory and hashes, all 90 composite identities plus preserved local IDs, 13-repo mapping, folds, correctly attributed experiment-escalation and promotion gates, artifact/cache schema, validation commands/output, explicit insufficient repositories if any, explicit unresolved C7/C8 thresholds, and confirmation that all work was local/read-only.

## Blockers

Independent review is pending. Click is repaired against its commit/corpus-compatible existing v4 manifest. Buoy remains insufficient because its selected post-rebrand public corpus intentionally excludes the judged `.10x/specs/repo-search-eval-autoresearch.md` path. Its same-source baseline also requires a separately approved 903-row write to the exact proposed namespace `github-doctacon-buoy-search-v1`; no approval or write occurred. The full 13-repo contract cannot authorize C3 or any dependent comparison while those Buoy conditions remain unresolved.

## Explicit exclusions

Label edits or review; candidate retrieval; model research or selection; generated experiment code; source/tests; namespace/catalog/default changes; experiment execution; promotion.

## References

- `.10x/research/2026-07-19-repo-search-heavy-ranking-experiment-decomposition.md`
- `.10x/specs/repo-search-eval-autoresearch.md`
- `.10x/decisions/repo-ranking-promotion-policy.md`
- `.10x/evidence/2026-06-28-expanded-repo-ranking-basket-validation.md`

## Progress and notes

- 2026-07-19: Opened as the executable contract-freeze prerequisite. No freeze work was performed during decomposition.
- 2026-07-20: Clarified composite case identity, label preservation, pilot-gate attribution, and the boundary that C1 cannot ratify or unblock C7/C8 experiment thresholds.
- 2026-07-20: Executed the local/read-only freeze. All 13 datasets load as 90 unique composite identities with unchanged local IDs and 370 judgments; hashes, mappings, folds, metrics, gates, and raw artifact/cache rules are frozen in `.10x/evidence/2026-07-20-repo-ranking-experiment-contract-freeze.md` and its storage inventory. Manifest validation resolved 341 paths but found 22 Buoy and 7 Click paths absent, marking only those repositories insufficient and blocking C3+. No credentials, models, live calls, namespace operations, or label edits occurred. Ticket remains active pending independent review.
- 2026-07-20: Repaired PR #59 review blockers. Checked in a 1.3 MB deterministic source-path bundle instead of 347 MB crawl artifacts; added a standard-library validator, focused tests, and CI invocation; reconciled the exact namespace pattern and `selected_corpus_artifact_hash` field; re-pinned Click only after verifying its existing v4 commit/corpus covers 36/36 judgments; and generated a current public-source post-rebrand Buoy plan at `fcb7abb` selecting 64 paths/903 rows. Buoy still misses the intentionally excluded internal `.10x` judgment and its exact proposed `github-doctacon-buoy-search-v1` 903-row baseline write remains pending separate approval. No labels, credentials, models, retrieval calls, namespaces, or catalogs changed; C1 remains active.
