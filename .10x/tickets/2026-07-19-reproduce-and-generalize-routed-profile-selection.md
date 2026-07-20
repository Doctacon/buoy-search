Status: open
Created: 2026-07-19
Updated: 2026-07-19
Parent: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md
Depends-On: .10x/tickets/2026-07-19-freeze-repo-ranking-experiment-contract.md, .10x/tickets/2026-07-19-capture-current-repo-candidates-and-baselines.md

# C8: Reproduce and Generalize Routed Profile Selection

## Scope

Using only C3's immutable shared raw-candidate cache, first reproduce the documented July routed-profile formulas, then distinguish oracle/static per-repo assignment from a selector that uses only runtime-observable non-identity features and is evaluated repository-held-out.

## Acceptance criteria

- Consume the exact frozen C3 cache/hash; do not issue retrieval, embedding, namespace, catalog, credential, or write calls.
- Encode the exact durable profile primitives from `.10x/evidence/2026-07-02-repo-routed-profile-portfolio-validation.md` and either reproduce them independently or declare the historical result unreproducible.
- Report separate rows for current default, oracle per-repo assignment, and a pre-registered held-out selector. Never label the historical benchmark namespace/profile map as an automatic/general selector.
- Freeze/hash selector inputs, training/selection rule, folds, seed, fallback, and tie-breaking before scoring. Repository/namespace identity and benchmark-repo hard-coding are forbidden.
- Report all 13 held-out repo score/P@5 deltas, component metrics, oracle gap, no-op rate, chosen-profile explanations, and mis-selection regressions.
- Keep gate: held-out selections pass the active distribution policy and materially close the oracle gap under a pre-registered C1 measure. Otherwise record no action for automatic selection and retain profiles as experiment-only evidence.
- No source default, product selector/profile, CLI/config surface, namespace, or catalog is changed.

## Stop conditions

- Stop if historical formulas cannot be reconstructed from durable evidence; do not claim `80.316` by copying the result table.
- Stop on C3 replay mismatch, cache/schema drift, identity leakage, held-out policy failure, or evidence showing only oracle/static assignment.
- Do not recapture candidates, productize a benchmark map, or invent a selector surface/fallback.

## Evidence expectations

Cache/hash provenance, exact formula reconstruction, frozen selector experiment definition, leakage checks, held-out results/oracle gap, deterministic rerun, policy mapping, review, and explicit productization disposition.

## Blockers

Dependency-gated: C1 and C3 are incomplete. Product semantics are intentionally deferred to C9 and do not block offline reproduction/generalization evidence.

## Explicit exclusions

Live calls/writes; source/product implementation; static benchmark map as generalization; public selector/profile surface; catalog/default changes; promotion.

## References

- `.10x/research/2026-07-19-repo-search-heavy-ranking-experiment-decomposition.md`
- `.10x/tickets/2026-07-19-capture-current-repo-candidates-and-baselines.md`
- `.10x/evidence/2026-07-01-repo-portfolio-routing-validation.md`
- `.10x/evidence/2026-07-02-repo-routed-profile-portfolio-validation.md`
- `.10x/decisions/repo-ranking-promotion-policy.md`

## Progress and notes

- 2026-07-19: Opened as an offline dependency-gated child. No selector semantics, profile surface, cache, source, tests, live operations, or promotion were created.
