Status: done
Created: 2026-07-14
Updated: 2026-07-14
Parent: None
Depends-On: None

# Review Buoy for Performance and User-Experience Leverage

## Scope

Perform a read-only whole-codebase review and identify exactly three highest-leverage next tasks for runtime performance or ease of user experience. Rank by observed pain, expected impact, implementation/risk cost, and evidence strength.

## Acceptance criteria

- Inspect active records, current source/tests/docs/workflows, prior live benchmark evidence, and current CLI behavior.
- Independently review runtime/data-path performance, first-run/operator UX, and reliability/maintainability constraints that materially affect either.
- Avoid speculative architecture and duplicate/owned work; account for the already-open float16 ticket.
- Return exactly three bounded task recommendations with rationale, expected outcome, dependencies, risks, and verification approach.
- Record an adversarial review artifact; do not implement recommendations.

## Explicit exclusions

Code changes, live crawls/applies/retrieval, package/release mutation, and broad refactoring without demonstrated user/performance value.

## Evidence expectations

Concrete paths/behavior, prior benchmark measurements, safe local command/test observations, active-ticket search, and independent reviewer reports.

## Progress and notes

- 2026-07-14: Three independent reviews completed and parent synthesis recorded at `.10x/reviews/2026-07-14-buoy-performance-ux-codebase-review.md`; exactly three recommendations have durable owners.

## Blockers

- None.
