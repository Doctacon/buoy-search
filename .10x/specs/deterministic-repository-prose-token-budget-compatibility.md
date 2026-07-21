Status: draft
Created: 2026-07-20
Updated: 2026-07-20

# Deterministic Repository-Prose Token-Budget Compatibility

## Draft authority and purpose

This inactive focused draft shapes the unresolved repository Markdown/prose compatibility surface exposed by C6. It does not authorize implementation, tests, generic pipeline changes, plan/artifact regeneration, tokenizer execution beyond read-only shaping, model construction/inference, provider/live operations, C6 execution, or namespace writes.

The active source-only contract `.10x/specs/deterministic-treatment-token-budget-subdivision.md` MUST NOT be reused for prose. Repository prose has heading-based sections and generic sentence overlap, not physical `SourceRange` ownership, breadcrumbs, exact `Lines S-E` citations, or source-line reconstruction.

The exact preserved treatment checkpoint contains 366 incompatible prose plan rows: 183 unique `(repository,row_id)` parents across 57 paths, duplicated in `fixed-80-python-breadcrumbs` and `python-ast`. Read-only plan inspection found the same 183 parents unchanged in `current-default`. Exact decomposition, the 57-path inventory, cause analysis, and exploratory option deltas are recorded in `.10x/evidence/2026-07-20-prose-token-budget-compatibility-shaping.md`.

## Provenance map

| Semantic or observation | Current provenance |
|---|---|
| Pinned BGE tokenizer revision/files/class/lock, maximum 512, special tokens on, no truncation; preserved checkpoint identities | Active-record-backed by C6 records and the active source-only specification |
| 366 treatment occurrences = 183 unique parents across 57 paths; 9 pytest / 174 Ruff unique parents; exact 513–689 range | Source-observed from the preserved gzip report |
| The same 183 title/section/content/index/URL/row signatures occur in `current-default` | Source-observed from the preserved external plan roots |
| Approximate content accounting, heading sections, two-sentence overlap, complete embedding rendering, and semantic row identity behavior | Source-observed in `chunker.py`, `github_repo.py`, and `plan_artifacts.py` |
| No-action preserves parity but leaves C6 blocked | Record-backed consequence |
| Treatment-only splitting breaks prose parity with current-default | Source-observed consequence |
| All-three-arm splitting preserves cross-arm parity but breaks ordinary/current-default byte parity unless the ordinary generic pipeline changes too | Source-observed and active-contract-backed consequence |
| Scope, exact boundary hierarchy, overlap, coverage contract, atomic fallback, failure scope, and parity policy | **Blocked pending explicit user ratification** |
| Final row/plan/artifact/namespace/storage identities after any implementation | Blocked on ratified behavior, implementation, and complete regeneration |

## Current behavior that a decision must preserve or explicitly supersede

1. `.md/.markdown/.mdx` repository files enter the generic Markdown pipeline as source Markdown. `.txt/.rst/.adoc` files receive a synthetic `# <repo_path>` heading before generic parsing.
2. Generic parsing normalizes body whitespace/chrome, removes headings from content, and uses the heading stack as `section_path`.
3. Generic splitting uses a 300-token `TOKEN_RE` approximation over Markdown units, sentences, words, and token spans, with two-sentence overlap capped at 80 approximate tokens.
4. Final embedding text is nonempty `Title:`, nonempty `Section:`, and content joined by double LF. The canonical URL and source metadata are stored but not embedded.
5. Prose sections have no physical-line citation. A compatibility child can retain the parent's heading path but MUST NOT fabricate `Lines S-E` or source breadcrumbs.
6. Plan row identity derives from site, canonical URL, section path, and exact content hash, with deterministic duplicate ordinals. `chunk_index` records order but is not an ordinary unique row's semantic identity.
7. Current C6 requires ordinary no-arm and explicit `current-default` equality and requires unchanged prose across all three arms.

## Exact compatibility accounting common to any split option

If splitting is ratified, every compatibility decision SHOULD use only the same pinned offline tokenizer contract as the active source specification:

- model `BAAI/bge-small-en-v1.5`;
- revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`;
- tokenizer-files identity `9c7beccadaa552c323907a895ad9ab188d8b75763022403f72c5d91085334f3b`;
- locked `transformers==5.12.1` slow `BertTokenizer` implementation;
- exact `model_max_length=512`; and
- special tokens enabled, truncation and padding disabled, offline with no alternate tokenizer or model construction.

For a candidate child, accounting MUST use the production-rendered final payload:

```text
Title: <unchanged parent title>

[Section: <unchanged parent heading path>\n\n]
<exact candidate content>
```

The Section block is absent only when the parent's section path is empty. Title, Section, double-LF separators, candidate content, and tokenizer special tokens are charged. URL and stored metadata remain outside embedding text and are validated unchanged, not charged. A separately reconstructed approximate counter MUST NOT authorize a boundary.

The candidate MUST be rendered through the same production `MarkdownChunk.embedding_text` path used for emission. Missing/mismatched tokenizer identity or an emitted payload above 512 fails planning.

The remainder of this draft is intentionally option-shaped. RFC 2119 terms become binding only for the option and exact checkpoint values the user ratifies after review.

## Option A — no action / preserve exact generic prose

- Keep all prose chunks byte-for-byte identical across ordinary no-arm, `current-default`, and both treatment arms.
- Keep all section paths, overlap, identities, indexes, counts, and plan artifacts unchanged.
- Do not reinterpret the exact maximum, truncate silently, or claim tokenizer readiness.
- Keep all 366 preserved incompatible treatment occurrences as an independent C6 fail-closed stop.

This is the only option that preserves every current parity invariant without widening generic behavior. It does not advance C6 readiness.

## Option B — treatment-only final-row compatibility pass

This option would process only generic prose rows inside `fixed-80-python-breadcrumbs` and `python-ast` after current generic chunking and before final plan emission.

### Common minimal behavior

- A complete final parent payload at or below 512 remains byte-identical with the same semantic row ID.
- An over-limit parent is replaced at its current position by ordered children.
- Every child retains exact parent title, heading `section_path`, canonical URL, path, document kind, tags, source hash, and source metadata.
- Children MUST NOT receive line citations, source breadcrumbs, code headers, or invented headings.
- Child contents are nonempty, ordered, non-overlapping, and concatenate byte-for-byte to the already-normalized parent content. This preserves the overlap already present between generic parents but adds no overlap between compatibility children.
- Children receive exact content hashes and semantic row IDs under the existing identity algorithm. Final chunk indexes are reassigned consecutively; unchanged compatible row IDs remain stable even when a preceding split shifts indexes.
- A split parent and its children necessarily have different row IDs. All plan/artifact/report/count/storage/namespace identities require regeneration.

### Boundary option B1 — farthest whitespace

From each character cursor, exhaustively count every later existing whitespace-run end plus end-of-content and select the farthest complete rendered candidate at or below 512. If none fits, the blocked atomic policy below applies.

The exact C6 probe split every 183 unique parent into 2 children with no scalar fallback. Per treatment arm this would replace 183 parents with 366 children (+183: pytest +9, Ruff +174). Across both treatments, the isolated preserved-envelope delta is +366 rows and +6 estimated 64-row requests before source subdivision.

Tradeoff: smallest observed row increase, but it can split Markdown constructs or code spans at whitespace.

### Boundary option B2 — structure-preferred hierarchy

At each cursor, search boundary tiers in this order:

1. existing paragraph ends;
2. existing generic sentence ends;
3. whitespace-run ends; and
4. Unicode-scalar ends only if scalar fallback is ratified.

Use the first tier containing any exactly feasible candidate and exhaustively select that tier's farthest feasible end. Do not assume token-count monotonicity. End-of-content participates at every tier where it is naturally present.

The exact C6 probe produced 392 children: 157 parents split in 2 and 26 split in 3. It used 366 paragraph ends and 26 whitespace ends, with no sentence or scalar fallback. Per treatment arm this is +209 rows (pytest +10, Ruff +199); across both treatments, +418 isolated rows and +6 estimated 64-row requests before source subdivision.

Tradeoff: preserves paragraph structure more strongly but adds 26 more rows per affected arm than B1. Tier priority is a retrieval semantic, not merely an implementation detail.

### Parity consequence

Either B1 or B2 clears the 366 preserved treatment-prose occurrences in the local probe while deliberately breaking treatment/current-default prose equality for the affected parents. The identical 183 current-default parents remain above 512. Ratifying this option therefore requires explicit supersession of C6's unchanged-prose treatment-isolation invariant and an explicit decision that exact compatibility is treatment-only.

## Option C — all-arm or global final-row compatibility pass

Apply B1 or B2 identically to `current-default` and both treatment arms. This preserves prospective cross-arm prose parity.

- B1's isolated all-three-arm delta is +549 rows and +9 estimated 64-row requests.
- B2's isolated all-three-arm delta is +627 rows and +9 estimated 64-row requests.

If applied only inside C6 arm routing, explicit `current-default` ceases to equal the ordinary no-arm path. If applied to the shared generic pipeline, ordinary/current-default equality can remain prospective, but every generic caller gains an exact pinned-tokenizer dependency and changed behavior for over-limit final rows. The project-wide affected population is unknown. This is broader than treatment-prose compatibility and requires a separate global compatibility contract and impact review; it MUST NOT be smuggled into a C6-local implementation ticket.

## Option D — integrate exact accounting into the generic splitter

Replace approximate accumulation decisions inside the generic unit/sentence/word splitter with complete-payload exact accounting while retaining a separate 300 retrieval target and/or 512 hard maximum.

This could preserve generic structural intent more directly but leaves several independent choices:

- whether 300 remains an approximate soft target or becomes an exact content/full-payload target;
- whether Title/Section overhead is charged against 300, only against 512, or both;
- whether two-sentence overlap is retried, shortened, dropped, or allowed to force an earlier boundary;
- whether compatible existing chunks may be rechunked;
- whether a long sentence/word/code block is split by whitespace, token-like spans, Unicode scalars, or fails; and
- whether the behavior is treatment-only, all C6 arms, repository prose globally, or every generic corpus.

No projection is authoritative until those semantics are ratified. This option has the widest regression surface and is not the minimal C6-local change.

## Blocked atomic-content and failure semantics

The exact 183-parent probes needed no Unicode-scalar fallback, so the preserved checkpoint does not force a choice between these policies:

1. **Structure hard stop:** if no paragraph/sentence/whitespace candidate fits, fail the complete repository/arm plan.
2. **Scalar safety fallback:** allow exact Unicode-scalar prefixes and fail only if no non-whitespace scalar plus unchanged Title/Section fits.
3. **Context/content weakening:** drop or rewrite title/section, truncate, omit, or accept oversize content.

Option 3 is not recommended: it changes coverage/citation meaning or silently loses content. If failure occurs under option 1 or 2, a candidate complete-plan diagnostic is repository, arm, repo path, unchanged section path, exact observed token count, tokenizer checkpoint, and `max=512`, with no content or token IDs. Prose has no truthful source line number.

Failure scope remains blocked: abort complete repository/arm plan (recommended for parity with the active source contract), omit only the file, omit only the row, or fall back to current/truncating behavior. No partial successful artifact should be called complete under a fail-closed option.

## Isolation and downstream gates common to any ratified split

A later implementation ticket would have to prove:

1. exact tokenizer identity/options/offline behavior and full final payload accounting;
2. deterministic boundary selection without monotonicity assumptions;
3. every final affected payload is at most 512;
4. exact normalized-parent content reconstruction under no-new-overlap behavior, plus preservation of existing inter-parent generic overlap;
5. unchanged Title/Section/canonical URL/metadata and absence of invented line citations/breadcrumbs/headers;
6. selected unsplittable/failure behavior with sanitized diagnostics and no partial artifact;
7. deterministic child identities/order/indexes and unchanged compatible-row identities;
8. exact selected parity scope: treatment-only divergence, all-arm parity, or global ordinary/current-default parity;
9. no source-range/generic-code/header/metadata-card behavior drift beyond the ratified scope; and
10. no model construction/inference, network fallback, credentials/provider calls, namespaces, retrieval, catalog/applied-state/default operations, deletes, evaluation, or promotion.

After separately reviewed implementation, a separately authorized complete forecast must regenerate source and prose together, validate every final row with the exact tokenizer, recompute all plan/artifact/JSONL/report/count/request/storage/namespace identities, and receive independent review. C6 stays blocked on zero incompatible rows and its still-separate exact nine-namespace write approval. No option in this draft unblocks C6 or carries prior approval forward.

## Exact confirm-or-correct user checkpoint

> Confirm or correct the repository-prose policy before this draft can become active. Choose **A, B, C, or D** and correct every parenthesized value:
>
> - **A — no action:** preserve ordinary/current-default/treatment prose byte-for-byte and keep the exact 366 treatment occurrences fail-closed, so C6 remains blocked; **or**
> - **B — treatment-only final-row cap:** process only the two treatment arms, accepting deliberate divergence from the 183 identical current-default parents; choose **B1 farthest-whitespace** (observed +183 rows/arm; +366 across treatments) or **B2 paragraph→sentence→whitespace hierarchy** (observed +209 rows/arm; +418 across treatments); **or**
> - **C — parity-preserving prospective cap:** choose B1 or B2 and apply it to **[all three C6 arms only / the shared ordinary generic pipeline]**, acknowledging that the first breaks ordinary/current-default parity and the second widens behavior beyond C6; **or**
> - **D — integrated generic rewrite:** separately shape the 300-target, 512-cap, overlap, compatible-row, and global-scope semantics before activation.
>
> For B or C, confirm: count only the exact pinned complete `Title + optional Section + content + separators + special tokens` payload; retain unchanged Title/heading Section/URL/metadata with no invented `Lines` citations or code headers; preserve each already-normalized parent content exactly and its existing inter-parent overlap; add **no new child overlap**; keep compatible parents byte-identical; order children at the parent position and use existing content-based row identity; choose atomic policy **[fail at an unsplittable paragraph/sentence/whitespace atom / permit Unicode-scalar fallback]**; on failure **[abort the complete repository/arm plan]** with sanitized repository/arm/path/section/token-count/checkpoint/max only and no partial artifact, omission, truncation, or context dropping. Confirm that all reported row/request deltas are shaping projections only, that source subdivision still changes later totals, and that implementation, complete regeneration, independent review, zero-incompatible preflight, and separate exact namespace-write approval remain mandatory. No choice here itself unblocks C6.

Until the user confirms one exact branch and every bracketed value after independent draft review, this specification remains `draft`, the shaping ticket remains blocked, and no executable implementation ticket may be opened from it.

## References

- `.10x/tickets/2026-07-20-shape-prose-token-budget-compatibility.md`
- `.10x/evidence/2026-07-20-prose-token-budget-compatibility-shaping.md`
- `.10x/tickets/2026-07-19-evaluate-python-syntax-chunking.md`
- `.10x/specs/deterministic-treatment-token-budget-subdivision.md`
- `.10x/evidence/.storage/2026-07-20-c6-python-syntax-tokenizer-preflight.json.gz`
- `.10x/evidence/2026-07-20-c6-python-syntax-pilot-forecast.md`
- `src/buoy_search/chunker.py`
- `src/buoy_search/github_repo.py`
- `src/buoy_search/plan_artifacts.py`
