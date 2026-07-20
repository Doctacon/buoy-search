Status: blocked
Created: 2026-07-19
Updated: 2026-07-20
Parent: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md
Depends-On: .10x/tickets/done/2026-07-19-freeze-repo-ranking-experiment-contract.md

# C5: Implement Opt-In Python Syntax Chunking

## Scope

Own a local-only, experiment-only Python syntax chunking implementation after an active focused specification defines exact behavior. Preserve fixed 80-line chunking as the default and preserve existing `--repo-search-metadata` output/behavior.

Existing records support evaluating syntax-aware chunks and lightweight Python breadcrumbs without Tree-sitter. They do not fully settle the exact AST boundary ownership, ancestor breadcrumbs, long-symbol subdivision, line coverage/citation rules, fallback behavior, or experiment arm names. This ticket is therefore not executable yet.

`.10x/specs/repo-python-syntax-chunking-experiment.md` now contains one exact draft recommendation based on the current source boundary and standard-library AST capabilities. Its `draft` status does not ratify the proposed semantics.

## Required syntax-contract checkpoint

Before implementation, ask the user to confirm all seven numbered items in the draft spec or correct the affected item explicitly:

1. the three arm identifiers and metadata/file-card isolation;
2. AST grammar/node/decorator and fixed-window breadcrumb semantics;
3. innermost-symbol/module/nesting/trivia ownership;
4. an 80-source-line maximum, deterministic subdivision, zero overlap, and fail-closed oversize handling;
5. exact source reconstruction and `Lines S-E`/unchanged-blob citation behavior;
6. whole-file syntax-error and non-Python fallback;
7. default compatibility, supported-runtime parity, standard-library-only locality, and zero side effects.

Only explicit confirmation or corrections may activate the spec and unblock this ticket.

## Acceptance criteria after ratification

- An active focused syntax experiment spec exists and this ticket contains no unresolved behavior.
- Implementation is explicit opt-in, local-plan-capable, standard-library-only unless a later decision says otherwise, and unchanged by default.
- Existing metadata mode remains compatible and is not silently combined with isolated breadcrumb arms.
- Tests cover every ratified boundary/fallback/coverage scenario and prove complete source-order coverage with no unintended omission or duplication.
- Local paired plans record commit, selected files, chunks/rows, multipliers, and zero remote calls/writes.
- No namespace, catalog, applied state, dataset, label, or default changes occur.

## Stop conditions

- Do not implement or create an active spec while the exact syntax behavior remains unratified.
- Stop if deterministic complete source coverage and citation-line preservation cannot be specified and tested.
- Do not add Tree-sitter or multilingual parser dependencies without a later explicit need and decision.
- Do not live-apply from this child.

## Evidence expectations

Ratification provenance, active focused spec, focused/full local tests, paired local plan/preflight summaries, diff review, and no-live-call proof.

## Blockers

- The seven-item exact checkpoint in `.10x/specs/repo-python-syntax-chunking-experiment.md` is recommended but not user-ratified.
- The focused spec remains `draft`; C5 cannot become executable until confirmed/corrected semantics are reflected in an `active` spec.

## Explicit exclusions

Live retrieval or writes; namespace/catalog/default mutation; Tree-sitter; multilingual product support; repeating the completed global metadata experiment; public product promotion.

## References

- `.10x/specs/repo-python-syntax-chunking-experiment.md`
- `.10x/research/2026-07-19-repo-search-heavy-ranking-experiment-decomposition.md`
- `.10x/research/2026-06-28-repo-search-precision-state-of-art.md`
- `.10x/research/2026-06-28-expanded-validation-ranking-hypotheses.md`
- `.10x/tickets/done/2026-06-28-repo-searchable-path-symbol-metadata.md`

## Progress and notes

- 2026-07-19: Opened blocked. Inspection found the hypothesis record-backed but the exact behavior insufficient for an active spec; no spec, source, tests, plans, or live operations were created.
- 2026-07-20: C1 closed. C5 remains blocked only on its separately required exact syntax-contract ratification and active focused spec; C1 closure authorized no implementation.
- 2026-07-20: Inspected the current 80-line repository renderer, regex metadata breadcrumbs, downstream token/overlap chunking, manifest citation fields, and CPython 3.11 AST spans. Drafted the exact seven-item recommended contract in `.10x/specs/repo-python-syntax-chunking-experiment.md`. No source, tests, plans, dependencies, model loads, live calls, writes, deletes, state, datasets, defaults, or parent-ticket content changed; C5 remains blocked.
