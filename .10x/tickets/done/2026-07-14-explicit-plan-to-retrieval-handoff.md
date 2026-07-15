Status: done
Created: 2026-07-14
Updated: 2026-07-14
Parent: None
Depends-On: None

# Make the Plan-to-Retrieval Handoff Explicit

## Scope

Implement `.10x/specs/apply-to-retrieval-handoff.md`: decision-complete apply preflight/approved text plus shell-safe preview/live retrieval commands. Namespace fallback removal and explicit selection are owned by `.10x/tickets/done/2026-07-14-add-explicit-multi-namespace-retrieval.md`.

## Acceptance criteria

- Human preflight and approved output show selected plan path/source/artifact, namespace/region/model/precision, first-apply state, embed/upsert/unchanged/stale counts, and explicit retain/delete intent.
- JSON additively includes region plus shell-safe `retrieval_commands.preview` and `.live` using the actual applied contract.
- Text labels commands as post-success during preflight and as the next step after successful apply.
- Shell-token tests cover spaces/metacharacters; automatic plan selection and pre-rebrand namespace identity remain exact.
- Focused/full tests, build, docs, evidence, and independent review pass; no live operation is required.

## References

- `.10x/reviews/2026-07-14-buoy-performance-ux-codebase-review.md`
- `.10x/specs/apply-to-retrieval-handoff.md`

## Progress and notes

- 2026-07-14: User explicitly authorized the recommended handoff. Exact text/JSON and shell-safety behavior is ratified in `.10x/specs/apply-to-retrieval-handoff.md`.
- 2026-07-14: Implemented additive region/retrieval commands, decision-complete text, exact stale intent, shell-token/automatic-plan/pre-rebrand regressions, and indexing docs. Focused 41 and full 274 tests pass; build, lock, diff, and no-staged-file checks pass. Evidence: `.10x/evidence/2026-07-14-apply-to-retrieval-handoff.md`. No live operation was run.
- 2026-07-14: Independent review passed with no blockers: `.10x/reviews/2026-07-14-apply-to-retrieval-handoff-review.md`.

## Closure

Every acceptance criterion maps to evidence, focused regressions, and a passing independent review. The active specification matches implementation.

## Retrospective

A command handoff is only trustworthy when it carries the exact verified embedding identity and runtime region and is shell-token safe. Explicit stale intent removes counter interpretation from the operator. Keeping fields additive preserved automation compatibility. These rules are focused in the specification/tests; no additional skill or knowledge record is needed.

## Blockers

- None.
