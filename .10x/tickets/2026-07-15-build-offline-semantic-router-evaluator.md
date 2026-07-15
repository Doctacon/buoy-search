Status: blocked
Created: 2026-07-15
Updated: 2026-07-15
Parent: .10x/tickets/2026-07-15-semantic-routing-offline-pilot-plan.md
Depends-On: .10x/tickets/2026-07-15-build-offline-namespace-catalog-fixture.md

# Build Offline Semantic Router Evaluator

## Scope

Implement deterministic validation, eligibility-first oracle/exact/semantic/hybrid routing, route-level RRF, exact downstream namespace-qualified RRF, metric formulas, canonical serialization, and tests governed by `.10x/specs/offline-semantic-routing-evaluation.md`.

Execute on `work/build-offline-semantic-router-evaluator` after catalog integration.

## Acceptance criteria

- Reuse integrated catalog/taxonomy models.
- Validate complete cases/config/vectors before evaluation.
- Implement oracle, exact, semantic, and route-hybrid algorithms exactly.
- Directly reuse or exactly reproduce `cross_namespace_rrf` ordering.
- Implement every metric/formula/edge case and canonical JSON contract.
- Keep unauthorized metadata out of route output and internal safety details redacted.
- Install no-network/credential/model/Turbopuffer/persistence sentinels.
- Add focused tests for every evaluator acceptance scenario; run full suite and diff check.

## Assumption provenance

Strategy comparison is user-ratified. Eligibility-before-score, RRF constant/formula, namespace-qualified identity, and oracle control are record/source-backed. Fixture vectors, formulas, labels, limits, and serialization are pilot-only. Real quality/thresholds remain unresolved and excluded.

## Explicit exclusions

Fixture conclusions, CLI/API, live services, answer generation, learned routing, decomposition, evidence tag filters/boosts, concepts, ontology, or graphs.

## References

- `.10x/specs/offline-semantic-routing-evaluation.md`
- `.10x/tickets/2026-07-15-semantic-routing-offline-pilot-plan.md`

## Evidence expectations

Changed files, formula examples, safety and repeatability tests, full-suite result, no-network proof, and limits.

## Blockers

Blocked pending shaping pass and integrated catalog dependency.

## Progress and notes

- 2026-07-15: Initial evaluator semantics were incomplete; repaired spec now defines validation, formulas, metrics, oracle, serialization, and exact RRF compatibility. No implementation started.
