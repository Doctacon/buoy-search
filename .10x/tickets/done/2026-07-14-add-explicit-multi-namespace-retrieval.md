Status: done
Created: 2026-07-14
Updated: 2026-07-14
Parent: .10x/tickets/done/2026-07-14-namespace-discovery-and-retrieval-plan.md
Depends-On: .10x/tickets/done/2026-07-14-add-namespace-discovery-command.md

# Add Explicit Multi-Namespace Retrieval

## Scope

Implement `.10x/specs/explicit-multi-namespace-retrieval.md`: remove the demo fallback, resolve repeatable explicit namespaces, embed once, run existing retrieval per namespace, and merge multi-namespace results with deterministic RRF.

## Acceptance criteria

- Dry/live retrieval without CLI/environment namespace fails before model, credentials, or API work.
- Repeated `--namespace` preserves order and one namespace retains the existing contract.
- Multi-namespace retrieval embeds once, queries sequentially, fails whole with namespace attribution, and returns global top-k deterministic RRF hits with namespace citations.
- Existing within-namespace ranking/schema behavior remains unchanged.
- Text/JSON docs and copy-ready examples cover discover → select → retrieve.
- Focused/full tests, build, evidence, and independent review pass.

## Exclusions

Automatic fan-out, metadata registration, mixed model settings, concurrency, partial results, and multi-namespace evals.

## References

- `.10x/specs/explicit-multi-namespace-retrieval.md`

## Evidence expectations

Deterministic fake-namespace/embedder tests proving call order, one embedding, fusion, attribution, and failure behavior. No live query is required for closure.

## Progress and notes

- 2026-07-14: Implemented explicit namespace resolution without demo fallback, repeatable CLI selection, single query embedding, sequential existing namespace retrieval, deterministic cross-namespace RRF, namespace-attributed multi output, focused docs, and deterministic tests. Evidence: `.10x/evidence/2026-07-14-explicit-multi-namespace-retrieval.md`.
- 2026-07-14: Focused 67 tests and full 268 tests pass; lock, wheel/sdist build, diff, and no-staged-file checks pass. No live operation was run.
- 2026-07-14: Independent review found two closure blockers: single-namespace live failures lacked namespace attribution, and repeated identical namespace selections could duplicate `(namespace, row ID)`. Repaired by wrapping single failures and rejecting duplicate selections before config/model/API work. Added duplicate, single-failure, multi-text-attribution, and exact-RRF regressions. Focused 70 and full 271 tests, build, lock, diff, and no-staged-file checks pass. Evidence refreshed.
- 2026-07-14: Independent re-review passed with no blockers: `.10x/reviews/2026-07-14-explicit-multi-namespace-retrieval-review.md`.

## Closure

Every acceptance criterion maps to `.10x/evidence/2026-07-14-explicit-multi-namespace-retrieval.md`, deterministic tests, and a passing independent re-review. The active specification remains coherent.

## Retrospective

Separating identifier discovery from explicit content selection avoided automatic broad fan-out and metadata machinery. Reusing one query vector preserves latency while namespace-qualified identity and deterministic RRF prevent score-scale and collision errors. Early duplicate rejection is simpler than merging repeated namespace inputs. No additional skill or knowledge record is warranted.

## Blockers

- None.
