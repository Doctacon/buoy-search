Status: done
Created: 2026-07-14
Updated: 2026-07-14
Parent: None
Depends-On: None

# Namespace Discovery and Explicit Multi-Namespace Retrieval Plan

## Aggregate outcome

Remove the unsafe demo namespace retrieval fallback, let operators list/filter visible namespace IDs, and retrieve across explicitly selected namespaces with deterministic rank fusion.

## Child sequence

1. `.10x/tickets/done/2026-07-14-add-namespace-discovery-command.md` adds the read-only discovery surface.
2. `.10x/tickets/done/2026-07-14-add-explicit-multi-namespace-retrieval.md` removes the fallback and adds repeatable explicit retrieval plus fusion. It depends on the discovery command so failure guidance points to an available workflow.

## Integration expectations

Both children use the existing region/API-key configuration, preserve dry-run/live safety, add tests and focused docs, and make no namespace mutations. The parent is a plan and is not executable.

## Acceptance criteria

- Both child tickets pass independent review and close.
- README/details-on-demand documentation presents discover → select → retrieve without a demo fallback.
- Existing single-namespace retrieval compatibility remains verified.

## Progress and closure

- 2026-07-14: Namespace discovery child completed and independently passed review.
- 2026-07-14: Explicit multi-namespace retrieval child completed after review repairs and independently passed re-review.
- 2026-07-14: Aggregate review passed: `.10x/reviews/2026-07-14-namespace-discovery-and-retrieval-parent-review.md`.

All acceptance criteria are supported by child evidence/reviews and `docs/retrieval.md`. Single-namespace compatibility remains tested; no live API operation occurred.

## Retrospective

The smallest coherent workflow is discover IDs, explicitly select targets, embed once, and fuse namespace-qualified ranks. Avoiding automatic fan-out and metadata inference keeps cost and semantics legible. Initial review exposed two important boundary cases—single-target error attribution and duplicate namespace identity—which are now durable regressions. No additional skill or knowledge record is needed.

## Blockers

- None.
