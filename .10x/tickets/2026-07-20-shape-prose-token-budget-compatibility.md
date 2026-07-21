Status: blocked
Created: 2026-07-20
Updated: 2026-07-20
Parent: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md
Depends-On: None

# Shape Prose Token-Budget Compatibility

## Outcome

Own the unresolved behavior for exactly 366 incompatible unchanged prose plan rows in the preserved C6 checkpoint. This is a blocked shaping owner only. It prevents the source-only contract or implementation ticket from inventing prose semantics and grants no implementation, test, plan regeneration, model, live-operation, or write authority.

## Known boundary

The preserved tokenizer checkpoint contains 366 incompatible prose plan rows: 183 unique `(repository,row_id)` identities across 57 paths, duplicated across the two treatment arms because their prose path is unchanged. The rows comprise 9 pytest rows per treatment arm and 174 Ruff rows per treatment arm. They are disjoint from the 20,926 incompatible source plan rows and remain an independent fail-closed C6 stop.

The active source-only specification `.10x/specs/deterministic-treatment-token-budget-subdivision.md` MUST NOT process these rows. Physical-source-line subdivision, inherited treatment breadcrumbs/ownership, and `SourceRange` reconstruction do not define prose behavior.

## Scope after separate shaping authorization

- Inspect the active generic Markdown/prose renderer and exact incompatible prose entries without mutating preserved artifacts.
- Present user-legible options for exact tokenizer-compatible prose behavior, including coverage/citations, overlap or no-overlap, structure preservation, identity/order, individually unsplittable content, and fail-closed handling.
- Map every semantic to active-record-backed, source-observed, user-ratified, or blocked provenance.
- Draft a focused prose specification only after execution-critical behavior is explicitly ratified; do not fold prose rules into the active source contract.
- Preserve C6’s separate complete-regeneration, independent-review, and exact namespace-write approval gates.

## Acceptance criteria

- All 366 preserved prose plan rows and their exact class/repository/path counts remain accounted for without treating duplication across arms as distinct prose semantics.
- A confirm-or-correct checkpoint settles exact rendered-payload accounting, deterministic boundaries, coverage/citations, structure/overlap behavior, identity/order, unsplittable content, failure scope, treatment/control parity, and isolation.
- Options and tradeoffs distinguish preserving current generic prose behavior from any new tokenizer-compatible behavior; no source-range semantics are silently reused.
- Required source/test, full-plan regeneration, artifact identity/count, review, and separate write-approval consequences remain downstream-only.
- C6 remains blocked until a separately reviewed and ratified prose contract is implemented and a complete regenerated exact preflight has zero incompatible rows.

## Blockers

The user ratified only the reviewed source-only subdivision contract. No exact prose behavior or authorization to shape it was supplied. This ticket remains blocked until the user separately authorizes prose shaping; any later draft would still require independent review and explicit ratification before implementation.

## Explicit exclusions

Source subdivision implementation; prose source/tests before a separately reviewed active prose spec and executable ticket; mutation/regeneration of the preserved C6 forecast, compact authority, tokenizer report, or validator; model construction/inference/download; credentials/provider access; namespace/catalog/applied-state/default operations; retrieval; deletes; evaluation; promotion; write approval.

## Evidence expectations

If shaping is later authorized: exact provenance-classified prose decomposition, renderer/source citations, options/tradeoffs, user-legible checkpoint, preserved-artifact attestation, independent review, and explicit no-implementation/no-live-operation evidence.

## References

- `.10x/tickets/2026-07-19-evaluate-python-syntax-chunking.md`
- `.10x/specs/deterministic-treatment-token-budget-subdivision.md`
- `.10x/evidence/2026-07-20-deterministic-token-budget-subdivision-shaping.md`
- `.10x/evidence/.storage/2026-07-20-c6-python-syntax-tokenizer-preflight.json.gz`
- `.10x/tickets/2026-07-20-implement-deterministic-token-budget-source-subdivision.md`

## Progress and notes

- 2026-07-20: Opened blocked when the user ratified only the reviewed source-only subdivision contract. The exact 366 incompatible prose plan rows remain unchanged and fail closed. No prose semantics, specification, implementation/test, artifact regeneration, model/live operation, or write was authorized or performed.
