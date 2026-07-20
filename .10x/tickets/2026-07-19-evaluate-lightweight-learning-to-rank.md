Status: open
Created: 2026-07-19
Updated: 2026-07-19
Parent: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md
Depends-On: .10x/tickets/2026-07-19-freeze-repo-ranking-experiment-contract.md, .10x/tickets/2026-07-19-capture-current-repo-candidates-and-baselines.md

# C7: Evaluate Lightweight Learning to Rank

## Scope

Fit and evaluate one transparent lightweight ranker entirely offline from C3's immutable shared raw-candidate cache and the existing assistant-drafted graded paths. Use repository-held-out validation; do not query or write namespaces again.

## Acceptance criteria

- Consume the exact frozen C3 cache/hash and C1 folds. No retrieval, embedding, namespace, catalog, or credential call occurs.
- Before fitting, freeze/hash the feature definitions, label transformation, splits, normalization/scales, seed, model form, and tie-breaking.
- Candidate features are limited to retrieval-time-observable signals from the cache/current scorer, such as ANN/BM25/RRF rank/score, file hit count, path role, filename/query overlap, path-token overlap, available Python symbol overlap, and current `repo_code` multiplier components.
- Repository/namespace identity, eval-case ID, answer text, hand-selected per-repo weights, and any held-out repo outcomes are forbidden features.
- Each repository is scored only by a model trained on the other 12 repositories; report fold membership and prove no leakage.
- Replay the current default from the same candidates. Publish fold weights, feature scales, all 13 held-out repo score/P@5 deltas, component metrics, and material-weight sign/order stability.
- Keep gate is the active distribution policy plus stable sign/order for material weights across folds. Otherwise classify the result as insufficient/overfit.
- A pass is experiment evidence only. Default promotion remains blocked pending the later label-confidence checkpoint and a separate product owner.

## Stop conditions

- Stop on C3 replay mismatch, cache/schema drift, label leakage, fewer than 12 training repos in a fold, repository identity dependence, any repo score/P@5 regression, or unstable material weights.
- Do not recapture candidates or issue live calls to repair an offline result.
- Do not add a runtime dependency or production ranking surface under this ticket.

## Evidence expectations

Cache/hash provenance, frozen experiment definition, leakage checks, fold results/weights/scales, deterministic rerun, active-policy mapping, review, and explicit experiment-only conclusion.

## Blockers

Dependency-gated: C1 and C3 are incomplete. No separate semantic blocker exists for offline experiment-only use of the labels; they remain assistant-drafted and non-product-ratifying.

## Explicit exclusions

Live calls/writes; label review/editing; repository identity features; production ranker implementation; selector/catalog/default changes; promotion.

## References

- `.10x/research/2026-07-19-repo-search-heavy-ranking-experiment-decomposition.md`
- `.10x/tickets/2026-07-19-freeze-repo-ranking-experiment-contract.md`
- `.10x/tickets/2026-07-19-capture-current-repo-candidates-and-baselines.md`
- `.10x/decisions/repo-ranking-promotion-policy.md`

## Progress and notes

- 2026-07-19: Opened as an offline dependency-gated child. No features, labels, model weights, cache, source, tests, or product behavior were created.
