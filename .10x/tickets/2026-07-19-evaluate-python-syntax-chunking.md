Status: blocked
Created: 2026-07-19
Updated: 2026-07-20
Parent: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md
Depends-On: .10x/tickets/done/2026-07-19-implement-opt-in-python-syntax-chunking.md

# C6: Evaluate Python Syntax Chunking

## Scope

After C5 has an active ratified spec, passing required CI, and exact paired plan counts, evaluate only the specified `current-default`, fixed/breadcrumb, and syntax arms on Buoy, pytest, and Ruff. `current-default` MUST be the actual unchanged 80-entry repository renderer followed by current generic Markdown token split/overlap; pair each isolated Python-aware treatment against it on identical source commits/corpora. Use new namespaces and zero deletes.

## Acceptance criteria

- C5 is complete, focused/full CPython 3.11/3.13 CI is passing, and exact per-arm namespace names, commits, header/source row counts, storage multipliers, and write counts are reported before approval.
- The `current-default` control is proven identical to the ordinary pre-C5 no-arm pipeline; each Python-aware treatment is isolated from generic split/overlap and metadata/card treatments and paired against that control on the same selected corpus.
- Every apply targets a new namespace; no stale or namespace delete occurs; baseline namespaces, catalog, defaults, and local applied state outside the new namespaces remain unchanged.
- Live eval after approved applies is retrieval-only.
- Primary metrics match C4. Also report chunk-count multiplier, mean/p95 chunk tokens, symbol-boundary coverage, and fallback rate by language.
- The three-repo no-regression/positive-average/two-improving-repo rule is only an experiment escalation gate. Stop an arm at the pilot if it fails that gate, exceeds an approved chunk/storage bound, or gains only from the already-completed global metadata preamble. Passing permits only a request for separately approved full-basket experimentation; it is not promotion authority.
- Full-basket expansion requires a separate exact ten-repo forecast and approval; only the full-basket keep gate is governed by the active distribution policy.
- Passing means promotion-candidate evidence only; fixed-line behavior remains the default.

## Approval gate

Blocked until C5 local plans can fill this exact checkpoint:

> Approve up to `<rows>/<new namespaces>/<estimated writes and storage multiplier>` for the ratified Buoy/pytest/Ruff `current-default` control and its paired isolated Python-aware arms on the reported identical commits/corpora, with zero deletes and no catalog/default change?

Past namespace approvals do not authorize these writes. Approval covers only the exact planned commits/arms/counts.

## Stop conditions

- Stop before any live operation without exact approval.
- Stop on commit/corpus mismatch, unapproved/exceeded rows or storage, a failed pilot gate, fallback/coverage behavior that violates the active spec, or any need to delete/mutate a baseline namespace.
- Do not add Tree-sitter unless the Python experiment first passes and a later multilingual need is explicitly ratified.
- Stop before full expansion until its exact incremental forecast is separately approved.

## Evidence expectations

Approval provenance; required CPython 3.11/3.13 CI; paired control/treatment plan and apply summaries; exact header/source rows and writes/deletes; per-arm metrics/resources/fallbacks; retrieval-only proof; review; explicit no-promotion conclusion.

## Blockers

- **C5 dependency satisfied:** C5 is complete at independently reviewed PR #69 head `360c6b9c666ccf432c082ac44d0a1400955ce3e9`, with required focused/full CPython 3.11/3.13 validation.
- **Exact local forecast recorded but not approval-ready:** `.10x/evidence/2026-07-20-c6-python-syntax-pilot-forecast.md` and its compact checkpoint bind the three arms to C1-pinned Buoy `fcb7abbe1652d2eab4ee23816b6d992d893603ac` (57 selected source files after seven card-incompatible oversize paths), pytest `1aa747de62dd9e9f395513c25298ba604f1724d0` (572 files), and Ruff `e6856de97d72225196444b7d969b8fe084140503` (9,758 files). The exact envelope is 151,990 final rows/row writes across nine new deterministic namespaces, 2,378 estimated 64-row upsert requests, zero deletes, and 547,388,704 serialized-plan-row-plus-raw-vector estimate bytes (`2.607014766x` the three-control subtotal; provider overhead excluded).
- **Control citation-contract drift requires resolution:** Ruff's exactly ordinary-equivalent `current-default` contains 2,722 code source final rows across 170 files with no parseable `Lines S-E` component after generic Markdown processing. This conflicts with the active spec's originating-section citation statement. The local-only task did not repair source or narrow the corpus; independent review must resolve this before the counts can be treated as a passing approval checkpoint.
- **Chunk/model resource interpretation remains unapproved:** the treatments contain 15,187 rows above 512 approximate tokens (8,065 fixed/breadcrumb; 7,122 AST), with maxima of 6,524. Approximate counts are not exact model-tokenizer counts, no model was loaded, and no acceptable chunk/storage/provider bound has been approved. Ruff additionally records 559/2,875 Python parse fallbacks (19.4434783%) per treatment; Buoy and pytest record zero Python parse fallbacks.
- **Independent review and write approval remain absent:** this record-only/artifact forecast requires independent review. No exact approval exists for any of the nine namespace writes, and the blocking findings above prevent requesting the unchanged write-approval checkpoint as passing. C6 remains `blocked`; no apply, retrieval, catalog/state/default change, delete, or promotion is authorized.

## Explicit exclusions

Source implementation; behavior shaping; Tree-sitter; baseline mutation/deletion; catalog/default changes; automatic promotion.

## References

- `.10x/specs/repo-python-syntax-chunking-experiment.md`
- `.10x/research/2026-07-19-repo-search-heavy-ranking-experiment-decomposition.md`
- `.10x/tickets/done/2026-07-19-implement-opt-in-python-syntax-chunking.md`
- `.10x/decisions/repo-ranking-promotion-policy.md`

## Progress and notes

- 2026-07-19: Opened blocked. No namespace names/counts, write budget, live call, or promotion was ratified.
- 2026-07-20: Clarified that the three-repo rule is an experiment escalation gate only, not active promotion policy.
- 2026-07-20: Reconciled C6 with the parent paired-default rule: the required control is the actual unchanged current renderer plus generic split/overlap, and each isolated Python-aware arm must be paired against it on the same corpus. C6 remains blocked on C5 and exact write approval.
- 2026-07-20: The exact seven-item C5 contract is now independently reviewed, user-ratified unchanged, and active. C6 remains blocked on C5 completion, passing exact paired local plans with namespace/row/storage/write counts, and separate exact write approval; no plan, namespace, live operation, or write was authorized.
- 2026-07-20: C5 closed after independent PASS at PR #69 head `360c6b9c666ccf432c082ac44d0a1400955ce3e9`; its dependency is satisfied. The existing bounded three-file Buoy plans do not fill this ticket's exact Buoy/pytest/Ruff pilot forecast. Exact pilot namespace names, commits/corpora, selected-file and header/source/total row counts, storage multipliers, and write counts remain required before the unchanged separate write-approval checkpoint. No C6 plan, live operation, namespace write, retrieval, or promotion was authorized.
- 2026-07-20: Executed only the authorized local forecast/preflight. Nine exact plans over the C1-pinned, arm-identical Buoy/pytest/Ruff source corpora forecast 151,990 rows/writes in nine deterministic namespaces, 2,378 default 64-row upsert requests, zero deletes, and 547,388,704 estimated serialized-row-plus-raw-vector bytes. Ordinary no-arm and explicit `current-default` signatures match exactly; headers/corpora match across arms; no model, credential, provider, namespace, retrieval, catalog, applied-state, dataset, label, default, or promotion operation occurred. Preflight nevertheless found 2,722 Ruff control source rows across 170 files without the active spec's `Lines S-E` component, 15,187 treatment rows above 512 approximate tokens, and 559/2,875 Ruff Python parse fallbacks per treatment. Recorded `.10x/evidence/2026-07-20-c6-python-syntax-pilot-forecast.md` plus compact checkpoint; C6 remains blocked on those findings, independent review, and separate exact write approval. The counts are not a write request and C6 was not made executable.
