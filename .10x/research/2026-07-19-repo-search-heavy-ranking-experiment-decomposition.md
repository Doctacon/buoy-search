Status: active
Created: 2026-07-19
Updated: 2026-07-19

# Repo Search Heavy Ranking Experiment Decomposition

## Question

How should `.10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md` be decomposed so unfinished ranking hypotheses can be evaluated without reopening completed work, inventing product semantics, duplicating live retrieval, or authorizing models and remote mutations?

## Sources and methods

Inspected the active owner and governing records:

- `.10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md`
- `.10x/reviews/2026-07-19-stale-ticket-status-closure-review.md`
- `.10x/research/2026-06-28-repo-search-precision-state-of-art.md`
- `.10x/research/2026-06-28-expanded-validation-ranking-hypotheses.md`
- `.10x/decisions/repo-ranking-promotion-policy.md`
- `.10x/decisions/namespace-ranking-defaults.md`
- `.10x/specs/repo-search-eval-autoresearch.md`
- `.10x/evidence/2026-06-28-cross-corpus-seed-eval-datasets.md`
- `.10x/evidence/2026-06-28-expanded-repo-ranking-basket-validation.md`
- `.10x/evidence/2026-07-01-repo-portfolio-routing-validation.md`
- `.10x/evidence/2026-07-02-repo-routed-profile-portfolio-validation.md`
- `.10x/tickets/done/2026-06-28-repo-searchable-path-symbol-metadata.md`
- `.10x/evidence/2026-06-28-repo-oversize-metadata-local-validation.md`

Inspected current implementation boundaries in `src/buoy_search/chunker.py`, `apply.py`, `cli.py`, `catalog.py`, `retriever.py`, `github_repo.py`, `crawler.py`, `plan_artifacts.py`, `config.py`, and `remote_catalog.py`. Current source fixes content/catalog vectors at 384 dimensions, exposes only `none` and `repo_code` ranking profiles, renders repository code into fixed 80-line Markdown sections, and already has an opt-in regex-based Python symbol/path metadata mode.

Enumerated the 13 checked-in `src/buoy_search/data/*_repo_search_seed_evals.json` files. The known basket is 90 cases: 10 each for Buoy, Requests, Click, pytest, and Typer; 5 each for Black, Ruff, Flask, Django, Pydantic, HTTPX, MkDocs, and Rich.

Also inspected the user-designated planner artifact at `/Users/crlough/Code/personal/turbo-search/.pi-subagents/artifacts/outputs/ede1dca0-7084-420f-a122-b9568444f19f/parallel-0/1-planner/plan.md`. The requested worktree-local `context.md` and `plan.md` were absent; no authority is inferred from them.

No source, tests, datasets, model files, generated plans, namespaces, catalogs, credentials, or live services were changed or called.

## Findings

### Completed history that remains terminal evidence

The umbrella already contains evidence for local rerankers, file/page aggregation, current `repo_code` scoring, opt-in searchable path/symbol metadata and regex breadcrumbs, metadata/file-card/oversize ablations, 13-repo scoring grids, and promoted distribution-safe ranking changes. The decomposition must not reopen those outcomes.

### Unfinished outcomes

Four outcome families remain genuinely unfinished:

1. select and evaluate a feasible open-source/local code-aware embedding candidate;
2. isolate syntax-aware chunk boundaries from the already-completed global metadata/breadcrumb treatment;
3. fit and evaluate a transparent lightweight ranker with repository-held-out validation;
4. reproduce the `80.316` routed result and distinguish an oracle/static map from a selector that can generalize without repository identity.

The `80.316` / P@5 `0.517` result is a secondary best-known routed-portfolio reference. It is not a universal baseline, an automatic selector, or a product contract. Every index-changing comparison still needs a paired current-default baseline on the same source commit and corpus.

### Authority boundaries

Record-backed now:

- open-source/local-only model use and no proprietary model APIs;
- new namespaces for indexing experiments, no baseline namespace mutation, and zero namespace/stale deletion;
- unchanged product defaults during experiments;
- the 13-repo/90-case basket as calibration evidence;
- the active distribution-aware promotion policy: no repo score regression, no repo P@5 regression, positive score gains on at least 3 repos, largest gain share at most 70%, and improved all-repo average score;
- assistant-drafted labels may support experiment-only calibration, not a production-ground-truth claim;
- C7 and C8 can and should share one immutable raw candidate cache.

Not ratified now:

- code-model identity, revision, license conclusion, dimension exception, prefix/pooling contract, download size, RAM/device need, or compute budget;
- numeric latency, storage, request, billing, or write budgets;
- new namespace writes, model downloads, or live retrieval calls;
- learned labels as production ground truth or any default promotion;
- an automatic selector, static per-repo product map, public profile/CLI surface, catalog mutation, or promotion path;
- exact Python syntax chunk semantics. Existing records support the hypothesis and a no-Tree-sitter direction, but do not fully define AST ownership, source-coverage rules, fallback behavior, long-symbol subdivision, or arm names. An active focused syntax spec therefore is not justified yet.

### Graph and call-sharing boundary

The safe graph is C1-C9:

- C1 freezes datasets, source snapshots, folds, metrics, mappings, gates, and artifact schema.
- C2 performs read-only model feasibility research without downloading or naming a candidate in advance.
- C3 makes one separately approved raw-candidate retrieval pass and freezes a hash-addressed cache.
- C4 is blocked on C1/C2 plus exact download and new-namespace write approval.
- C5 is local-only but blocked until exact syntax behavior is ratified and captured in an active focused spec.
- C6 is blocked on C5 plus exact new-namespace row/write approval.
- C7 and C8 are offline consumers of the same frozen C3 cache; they must not issue retrieval calls.
- C9 remains blocked until C8 and a product checkpoint; no active product spec exists now.

C3 owns the only retrieval capture for C7/C8. Any inability to export separate ANN and BM25 candidates, namespace-qualified identities, or deterministic default replay stops both children rather than triggering duplicate calls.

## Exact checkpoints

1. **C3 retrieval checkpoint:** after C1 reports the exact namespace/commit map and predicted request count, ask: “Approve one retrieval-only raw-candidate pass for the 90 frozen cases, with separate ANN and BM25 lists, zero writes/deletes/catalog changes, and the reported request/cost bound?”
2. **C4 model/write checkpoint:** after C2 and local planning report exact values, ask: “Approve download of pinned open-source model `<model>@<revision>` (`<bytes>`, `<RAM/device estimate>`) and up to `<rows>/<new namespaces>/<estimated writes>` for the three-repo paired pilot, with zero deletes and no catalog/default change?”
3. **C5 syntax-contract checkpoint:** recommend the smallest local standard-library Python experiment, then ask the user to confirm or correct exact arms, AST boundary/ancestor semantics, long-symbol subdivision, source-line coverage/citation behavior, and syntax-error/non-Python fallback before activating a spec or implementation ticket.
4. **C6 syntax-write checkpoint:** after approved local C5 plans report exact per-arm rows and storage multiplier, ask approval for only those new namespaces/writes, with zero deletes and no catalog/default change.
5. **C9 product checkpoint:** only after C8, ask: “I recommend a versioned explicit opt-in profile with `repo_code` unchanged; confirm that surface, or explicitly authorize shaping an automatic selector from the held-out C8 result.” Never offer the static benchmark-repo map as automatic generalization.
6. **Promotion label-confidence checkpoint:** only if an embedding or learned candidate is proposed for default promotion, ask whether the source-backed assistant labels are sufficient for that decision or whether to fund bounded independent review of the 90 cases. This is not a prerequisite for experiment-only work.

## Stop conditions

- Stop affected C1 repositories if their checked-in judgment paths cannot be reproduced from pinned source manifests; do not rewrite labels silently.
- Stop C4 if no credible 384-dimensional candidate works through the installed local path without remote code, unless a separate dynamic-dimension decision is ratified.
- Stop C3/C7/C8 if separate raw lists cannot be captured or current default replay mismatches the live ordering outside C1's declared tolerance.
- Stop C4/C6 on failed pilot gates, unapproved or exceeded resource bounds, incompatible models/chunks, or any need to mutate/delete baseline namespaces.
- Stop C5 if deterministic complete source coverage and citation line behavior cannot be specified and tested.
- Stop C7 on leakage, repo identity, incomplete held-out folds, unstable material weights, or active-policy failure.
- Stop automatic C8/C9 productization if only oracle/static mapping can be reproduced.
- A passing experiment creates promotion-candidate evidence only. It does not authorize a default, catalog write, public selector, or product promotion.

## Conclusion

Convert the umbrella to a non-executable parent and create only the nine bounded child owners. C1 and C2 are executable now within record/local-read boundaries. C3/C4/C5/C6/C9 remain blocked at named gates. C7/C8 remain offline and dependency-gated on one frozen C3 cache. No syntax or product spec should be activated during decomposition because the exact semantics are not fully record-backed yet.
