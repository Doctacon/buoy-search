Status: blocked
Created: 2026-07-15
Updated: 2026-07-15
Parent: .10x/tickets/2026-07-15-semantic-routing-offline-pilot-plan.md
Depends-On: None

# Build Controlled Taxonomy Fixture

## Scope

Implement the flat taxonomy model, canonical normalization, global validation, and deterministic exact phrase matcher governed by `.10x/specs/controlled-taxonomy-pilot.md`.

Execute on `work/build-controlled-taxonomy-fixture` in its own worktree based on current `develop` after shaping passes.

## Acceptance criteria

- Implement minimum typed taxonomy/term model and JSON loader.
- Enforce global descriptor uniqueness and exact normalization/matching/output rules.
- Ensure matching never mutates assignments or authorization.
- Add focused tests for every taxonomy acceptance scenario.
- Run focused tests, full suite, and `git diff --check`.

## Assumption provenance

Broad taxonomy/exact-routing direction is user-ratified. Detailed normalization and fixture mechanics are synthetic pilot-only. Governed/derived/ACL separation and no public behavior are record-backed. Production taxonomy semantics remain unresolved and excluded.

## Explicit exclusions

Catalog authorization, routing fusion, evidence filters/boosts, hierarchy, ontology, LLM tags, public behavior, live services, or graphs.

## References

- `.10x/specs/controlled-taxonomy-pilot.md`
- `.10x/tickets/2026-07-15-semantic-routing-offline-pilot-plan.md`

## Evidence expectations

Changed files, exact normalization examples, scenario tests, full-suite result, no-network/external mutation proof, and limits.

## Blockers

Blocked pending pass re-review of the repaired shaping records.

## Progress and notes

- 2026-07-15: Opened from initial spec set, then blocked after shaping review found execution-critical ambiguity. Repaired governing spec; no implementation started.
