Status: blocked
Created: 2026-07-19
Updated: 2026-07-20
Parent: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md
Depends-On: .10x/tickets/done/2026-07-19-freeze-repo-ranking-experiment-contract.md

# C5: Implement Opt-In Python Syntax Chunking

## Scope

Own a local-only, experiment-only Python syntax chunking implementation after an active focused specification defines exact behavior. Preserve the actual current default—fixed 80-entry repository sections followed by generic Markdown token splitting/overlap—and preserve existing `--repo-search-metadata` output/behavior.

Existing records support evaluating syntax-aware chunks and lightweight Python breadcrumbs without Tree-sitter. They do not fully settle the exact LF-coordinate/AST ownership, tokenizer-owned decorator spans, ancestor breadcrumbs, long-symbol subdivision, final-chunk coverage/citation rules, fallback behavior, common header treatment, or experiment arm names. This ticket is therefore not executable yet.

`.10x/specs/repo-python-syntax-chunking-experiment.md` now contains one exact draft recommendation based on the current source boundary and standard-library AST capabilities. Its `draft` status does not ratify the proposed semantics.

## Required syntax-contract checkpoint

Before implementation, ask the user to confirm all seven numbered items in the draft spec or correct the affected item explicitly:

1. the three arm identifiers, actual current-default generic split/overlap control, parent-required pairing, and metadata/file-card isolation;
2. LF-only physical coordinates, AST grammar/nodes, and `tokenize` `@` ownership of full physical decorator spans;
3. fixed-window breadcrumb and innermost-symbol/module/nesting/trivia ownership;
4. an 80-physical-line maximum for treatment final chunks, deterministic subdivision, zero overlap, no downstream generic split, and fail-closed oversize handling;
5. one mandatory identical non-source `Repository file`/`Language` header final chunk plus the distinct treatment/control coverage and citation contracts;
6. whole-file isolated LF fixed/no-breadcrumb syntax-error and non-Python fallback plus fail-closed tokenizer/coordinate failures;
7. no-arm/metadata/card compatibility, focused/full CPython 3.11/3.13 CI validation, standard-library-only locality, and zero side effects.

Only explicit confirmation or corrections may activate the spec and unblock this ticket.

## Acceptance criteria after ratification

- An active focused syntax experiment spec exists and this ticket contains no unresolved behavior.
- Implementation is explicit opt-in, local-plan-capable, standard-library-only unless a later decision says otherwise, and unchanged by default; `current-default` exactly reproduces the pre-C5 80-entry renderer plus generic token split/overlap.
- Each Python-aware arm is isolated from generic split/overlap and metadata/card treatments and is paired against `current-default` on the same commit/corpus.
- Tests cover every ratified LF/AST/tokenizer/header/boundary/fallback/coverage scenario, distinguish control originating-section citations from exact treatment final-chunk citations, and prove complete treatment source-order coverage with no unintended omission or duplication.
- Focused and full tests pass in the required CI matrix on CPython 3.11 and 3.13; one local runtime is not sufficient closure evidence.
- Local paired plans record commit, selected files, header/source chunks and rows, multipliers, and zero remote calls/writes.
- No namespace, catalog, applied state, dataset, label, or default changes occur.

## Stop conditions

- Do not implement or create an active spec while the exact syntax behavior remains unratified.
- Stop if exact current-default parity, LF-coordinate treatment coverage, tokenizer-owned decorator spans, mandatory common-header parity, or the distinct control/treatment citation contracts cannot be specified and tested.
- Do not add Tree-sitter or multilingual parser dependencies without a later explicit need and decision.
- Do not live-apply from this child.

## Evidence expectations

Ratification provenance, active focused spec, focused/full CPython 3.11/3.13 CI results, golden current-default parity, LF/AST/tokenizer/header coverage assertions, paired local plan/preflight summaries, diff review, and no-live-call proof.

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
- 2026-07-20: Repaired PR #64's record-contract blockers: the paired control is now the actual current renderer plus generic split/overlap; treatment coordinates are LF-only with standard-library tokenizer-owned decorator introducers/spans; treatment final-chunk coverage is separated from control originating-section citations; the identical non-source repository header is mandatory and counted explicitly; and validation requires focused/full CPython 3.11/3.13 CI. The spec remains draft and C5 remains blocked; no implementation, tests, dependencies, plans, live operations, defaults, or product behavior changed.
