Status: open
Created: 2026-07-15
Updated: 2026-07-15
Parent: None
Depends-On: None

# Semantic Routing Offline Pilot Plan

## Plan outcome

Build and run the smallest deterministic local plumbing pilot for a semantic namespace catalog, controlled taxonomy, and exact/semantic/hybrid routing without Turbopuffer calls, hosted APIs, production infrastructure, or a graph.

This is a parent plan, not an executable ticket.

## Governing records

- `.10x/decisions/data-vault-is-analogy-not-architecture.md`
- `.10x/specs/controlled-taxonomy-pilot.md`
- `.10x/specs/semantic-namespace-catalog-pilot.md`
- `.10x/specs/offline-semantic-routing-evaluation.md`
- `.10x/reviews/2026-07-15-semantic-routing-offline-pilot-shaping-review.md`
- focused 2026-07-15 namespace, tagging, multi-hop, and concept-graph research records

## Assumption provenance

### User-ratified direction

Namespace cards, controlled taxonomy, exact/semantic/hybrid offline comparison, current RRF downstream control, ACL/false-exclusion measurement, and evidence before graph work.

### Record/source-backed invariants

No Data Vault or graph; eligibility before score; governed/derived/ACL separation; `RRF_K = 60`; namespace-qualified evidence identity; offline/no-live boundary.

### Synthetic pilot-only mechanics

All fixture schemas, normalization, ACL groups, compatibility fields, vectors, labels, limits, and metric formulas are deterministic plumbing mechanics only.

### Unresolved outside the pilot

Production semantics, real quality, ACLs, taxonomy, public behavior, storage, models, thresholds, and architecture promotion.

## Child sequence

1. `.10x/tickets/2026-07-15-build-controlled-taxonomy-fixture.md`
2. `.10x/tickets/2026-07-15-build-offline-namespace-catalog-fixture.md`
3. `.10x/tickets/2026-07-15-build-offline-semantic-router-evaluator.md`
4. `.10x/tickets/2026-07-15-freeze-offline-semantic-routing-fixture.md`
5. `.10x/tickets/2026-07-15-run-offline-semantic-routing-pilot.md`

Each child executes in its own `work/*` branch/worktree based on current `develop`.

The catalog child depends on the integrated taxonomy model. The evaluator depends on catalog. The freeze child depends on the evaluator and owns fixed fixtures/preregistration. The run child may not edit frozen inputs.

## Aggregate acceptance criteria

- All active specs pass independent shaping review before children become executable.
- Each child passes focused/full tests, independent review, and protected integration.
- Freeze manifest/review precedes held-out execution.
- Oracle, exact, semantic, and hybrid use identical eligibility, limits, cached evidence, and metric definitions.
- Results are deterministic plumbing evidence only.
- No network, credentials, model download, Turbopuffer construction/call, persistent production store, Data Vault, concept extraction, ontology, or graph occurs.

## Blockers

All children are blocked pending pass re-review of the repaired shaping records. Production and architecture work remain blocked on pilot evidence and later user ratification.

## Progress and notes

- 2026-07-15: User approved the offline pilot direction.
- 2026-07-15: Initial shaping review failed due to underdefined taxonomy, compatibility, vector, routing, RRF, metric, freeze, dependency, and synthetic ACL mechanics. Child execution blocked.
- 2026-07-15: Repaired the specifications and ticket graph; added provenance classifications and a separate fixture-freeze child. Awaiting independent re-review before opening execution.
