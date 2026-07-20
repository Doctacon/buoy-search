Status: draft
Created: 2026-07-20
Updated: 2026-07-20

# Repository Python Syntax Chunking Experiment

## Authority and activation gate

This is an exact **proposed** contract for the C5 checkpoint in `.10x/tickets/2026-07-19-implement-opt-in-python-syntax-chunking.md`. It is not active authority. The three arms and every rule under “Proposed behavior” remain unratified until the user confirms or corrects the numbered checkpoint at the end of this record. C5 MUST remain blocked and no source, tests, local plans, namespaces, or live operations may derive behavior from this draft.

The following boundaries are already established by the task and active records:

- the experiment is explicit opt-in, local-plan-capable, Python-only, and standard-library-only;
- current fixed 80-line repository behavior remains the default;
- the existing `--repo-search-metadata` mode remains compatible outside the isolated experiment;
- Tree-sitter, new dependencies, live retrieval, writes, deletes, catalog/default changes, and product promotion are excluded.

Current source inspection establishes, but does not ratify proposed behavior, that:

- `src/buoy_search/github_repo.py` renders non-Markdown/non-prose repository files in consecutive 80-line Markdown sections headed `Lines <start>-<end>`;
- `--repo-search-metadata` adds a file-wide path/stem/symbol preamble and regex-derived Python symbol breadcrumbs;
- `src/buoy_search/chunker.py` can further split an oversized fenced section at the 300-token target and can add two-sentence overlap, while all derived chunks retain the section heading as `section_path`;
- manifest citations currently retain the GitHub blob URL and `section_path`; they do not create per-chunk GitHub line-fragment URLs;
- supported CPython 3.11+ provides `ast.parse`, `ClassDef`, `FunctionDef`, `AsyncFunctionDef`, decorator locations, and inclusive `lineno`/`end_lineno` spans. A fixed `feature_version=(3, 11)` can hold accepted grammar constant across the supported 3.11-3.13 validation matrix.

The current second-stage split means generated 80-line Markdown sections alone do not prove exact final-chunk line coverage or exact per-chunk citations. The proposal below therefore makes final experiment chunks—not only generated Markdown sections—the coverage boundary. If that cannot be implemented without changing unselected default behavior, C5 MUST stop.

## Purpose and scope

Define one local repository-indexing experiment that separately measures:

1. the current fixed-line boundary treatment without searchable symbol breadcrumbs;
2. the effect of Python ancestor breadcrumbs while retaining fixed-line boundaries;
3. the additional effect of Python AST-derived boundaries while retaining the same breadcrumb vocabulary.

The experiment covers selected repository source files only. It does not change file selection, the repository size cap, Markdown/prose handling, embedding configuration, retrieval ranking, eval judgments, namespace policy, or product defaults.

## Proposed behavior (unratified)

### Stable arm identifiers and isolation

The experiment would expose exactly these logical arm identifiers:

| Arm | Source boundaries | Searchable breadcrumb line |
|---|---|---|
| `fixed-80` | consecutive source lines `1-80`, `81-160`, ... | none |
| `fixed-80-python-breadcrumbs` | identical to `fixed-80` | AST-derived symbol chains intersecting the range |
| `python-ast` | AST ownership regions, subdivided to at most 80 source lines | the owning symbol’s ancestor chain |

The eventual implementation MAY choose one private CLI option with these values, but MUST NOT create a public/default product profile in C5.

All three experimental arms MUST exclude the completed metadata treatment: no `Search metadata`, path tokens, file stem, file-wide symbol list, symbol-token list, file-card page, or oversize-file-card page may be added. Selecting an experimental arm together with `--repo-search-metadata`, `--repo-file-cards`, or `--repo-oversize-file-cards` MUST fail before corpus generation with a user-facing incompatibility error rather than combine treatments silently.

The ordinary no-arm path and the existing metadata/card flags MUST keep their current behavior and output. Experiment-arm incompatibility does not deprecate or alter those existing options.

### Python parse contract

Only a file whose current repository language classification is `python` is eligible for breadcrumb or AST treatment.

Eligible content MUST be parsed with the standard library equivalent of:

```python
ast.parse(source, filename=repo_path, mode="exec", type_comments=True, feature_version=(3, 11))
```

Only `ast.ClassDef`, `ast.FunctionDef`, and `ast.AsyncFunctionDef` are symbol nodes. Lambdas, comprehensions, assignments, imports, module docstrings, and control-flow nodes are not symbol nodes.

A symbol’s inclusive effective source span starts at the earliest decorator `lineno`, when decorators exist, otherwise at the node `lineno`; it ends at `end_lineno`. Multi-line decorators are therefore wholly within the decorated symbol’s effective span. A missing/invalid end position is an invariant failure, not a guessed boundary.

A symbol chain consists only of unqualified symbol names from outermost to innermost, joined with ` > `. It does not include the repository path, file stem, derived module path, symbol kind, arguments, bases, decorators, or global symbol inventory. Examples are `Client` and `Client > request > decode`.

### Fixed-window breadcrumb arm

For each `fixed-80-python-breadcrumbs` range, include every distinct symbol chain whose effective span intersects at least one source line in that range. Chains MUST be ordered by `(effective_start, effective_end, lexical AST order)` and de-duplicated without truncation. This includes a containing long symbol when a fixed range begins in its body and includes nested chains when their definitions intersect the range.

When at least one chain exists, emit exactly one searchable line before the source payload:

```text
Symbol breadcrumbs: <chain-1>; <chain-2>; ...
```

A range with no intersecting symbol emits no breadcrumb line. Breadcrumb text is generated context, not a source line, and is excluded from source-coverage accounting.

### AST ownership and boundary arm

The AST arm MUST assign every source line to exactly one initial owner:

1. among symbol effective spans containing the line, the lexically innermost symbol owns it;
2. if no symbol contains it, the synthetic module owner owns it.

Nested definitions are therefore carved out of their parent: the nested symbol owns its decorator-through-`end_lineno` range, while the parent owns its signature and body lines outside nested-symbol spans. Top-level imports, assignments, expressions, module docstrings, and other module statements are module-owned. Statements inside a symbol remain owned by the innermost containing symbol.

Comments and blank lines inside a symbol’s effective span have that symbol owner. Outside every symbol, a physical line is trivia exactly when `line.strip()` is empty or `line.lstrip().startswith("#")`. Each maximal consecutive trivia run MUST be reassigned to the owner of the nearest later non-trivia line; if no later non-trivia line exists, it MUST be reassigned to the owner of the nearest earlier non-trivia line. An all-trivia file remains one module-owned region. This source-line rule intentionally avoids guessing whether a comment describes the preceding or following statement: it always attaches forward except at EOF, and it prevents trivia-only chunks.

After trivia reassignment, maximal contiguous ranges with the same owner are ownership regions. A parent may consequently have multiple regions around nested children. Module-owned ranges have no breadcrumb. Symbol-owned ranges emit exactly one `Symbol breadcrumbs: <outer > ... > owner>` line.

### Deterministic subdivision

Every fixed range and AST ownership region MUST contain at most 80 source lines. A longer ownership region MUST be subdivided from its first line into consecutive ranges of 80 lines, with a final shorter range when needed. Subdivision MUST have zero source-line overlap and MUST NOT search for a prettier statement, token, sentence, or blank-line break.

Each subdivided range retains the same owning breadcrumb chain. There is no token-based or sentence-based second subdivision and no content overlap for experiment source chunks. A source line longer than the downstream token target remains one intact source line; no experiment behavior may split, normalize, truncate, or duplicate it silently. If the existing plan path cannot carry such a chunk safely, planning MUST fail clearly rather than weaken coverage.

The 80-line maximum is a source-line bound, not a promise that every chunk fits an embedding model’s token limit. C5 is local-only; any later model/write resource bound belongs to C6’s separately approved plan.

### Source coverage and citation contract

Line numbering is one-based over `source.splitlines()`, matching current repository page generation. Universal-newline decoding and the presence/absence of a terminal newline are not separate source lines; within each numbered line, text MUST remain unchanged.

For every selected nonempty source file and every arm:

- each experiment source chunk MUST represent one nonempty contiguous inclusive range `[start, end]`;
- ranges sorted by `start` MUST begin at line 1, end at the last numbered source line, be adjacent (`next.start == previous.end + 1`), and never overlap;
- concatenating source payload lines in range order MUST equal `source.splitlines()` exactly;
- generated breadcrumb and common repository header text MUST be distinguishable from, and excluded from, source-line reconstruction;
- no downstream generic chunk split or sentence overlap may duplicate or omit source payload.

Each final source chunk MUST use `Lines <start>-<end>` as the final `section_path` component and MUST retain the existing immutable GitHub blob URL as `canonical_url`. No `#Lx-Ly` URL fragment is proposed because the current page/manifest boundary owns one canonical URL per source file. Every line-range citation MUST describe exactly the source payload carried by that final chunk.

The existing common repository page header (`Repository file` and `Language`) MAY remain as equal context in all three arms, but it MUST NOT be counted as source coverage or differ by arm. Path-token and global-symbol preambles remain excluded.

### Decorators, async definitions, nesting, and module statements

The following cases are consequences of the preceding rules and MUST be tested after ratification:

- all decorators, including multi-line decorators, share ownership and citation coverage with their decorated class, sync function, or async function;
- `async def` is treated identically to `def` except for its AST node type; breadcrumb text contains only its name;
- nested classes/functions/async functions get full ancestor chains and exclusive source ownership; enclosing symbols do not duplicate nested source lines;
- parent-owned source before and after a nested definition may produce separate parent ranges with the same breadcrumb;
- module docstrings, imports, assignments, executable statements, and comments not attached as leading trivia to a symbol remain module-owned and have no symbol breadcrumb;
- interstitial comments/blank lines follow the exact trivia rule above rather than being dropped or duplicated.

### Fallback

For Python `SyntaxError` or `ValueError`, both `fixed-80-python-breadcrumbs` and `python-ast` MUST fall back for the entire file to `fixed-80`: fixed 80-line ranges, zero breadcrumbs, exact coverage/citations, and no partial AST result. The plan summary MUST count the file as a Python parse fallback without exposing source content in the error summary.

For every non-Python code language, both Python-aware arms MUST deterministically use the same `fixed-80` treatment and count the file as a non-Python fallback. Markdown and prose files retain their existing non-code path and are not counted as syntax fallbacks.

Unexpected parser/runtime failures other than `SyntaxError` or `ValueError` MUST fail local planning; they MUST NOT silently downgrade. Fallback does not enable the existing regex metadata scanner.

### Defaults, locality, and side effects

With no experimental arm selected, generated corpus pages, plan rows, hashes, citations, and existing metadata behavior MUST remain unchanged.

C5 implementation and validation, if later activated, MUST be local-only. It MUST NOT load embedding models, read service credentials, call GitHub beyond the already-selected local acquisition flow, contact turbopuffer or another live retrieval service, create/write/delete a namespace, update catalog/applied state, change datasets or labels, or promote an arm.

No Tree-sitter package, parser grammar, model, or other dependency may be added. The standard-library AST is the only parser in this proposed experiment.

## Proposed acceptance scenarios after ratification

1. **Three-arm isolation:** One parseable Python fixture produces identical fixed ranges in the first two arms, no breadcrumb in `fixed-80`, AST chains only in the breadcrumb arm, and AST ownership ranges plus the same chain vocabulary in `python-ast`.
2. **Coverage:** A fixture containing module statements, decorators, sync/async functions, nested classes/functions, comments, blanks, a long symbol, and a final line without newline reconstructs exactly from every arm with adjacent, complete, nonoverlapping citation ranges.
3. **Long symbol:** A 161-line ownership region yields `80/80/1` consecutive source ranges with identical owner chain and zero overlap.
4. **Trivia ownership:** Leading, interstitial, nested, and trailing comment/blank-only runs follow the next-region/last-region rule without a trivia-only chunk.
5. **Syntax error:** A malformed Python file falls back wholly and deterministically to fixed/no-breadcrumb while recording one sanitized parse fallback.
6. **Non-Python:** Representative source languages use fixed/no-breadcrumb and record non-Python fallback; Markdown/prose behavior is unchanged and excluded from fallback counts.
7. **Citation integrity:** Every final source chunk’s `Lines S-E` component equals its exact payload; canonical blob URLs remain unchanged; no downstream overlap or subdivision occurs.
8. **Compatibility:** The no-arm output and existing `--repo-search-metadata` output match pre-change fixtures; experimental arms reject metadata/card combinations before corpus generation.
9. **Runtime parity:** Focused fixtures produce identical boundaries, breadcrumbs, fallback counts, and citations under supported Python 3.11 and 3.13.
10. **Safety:** Local plan/preflight validation proves zero embeddings, credentials, remote retrieval calls, writes, deletes, catalog/default mutations, and live apply.

## Explicit exclusions

- Tree-sitter, multilingual syntax parsing, or dependency changes.
- Path-token/global-symbol preambles or metadata/file-card ablations.
- Token-overlap tuning, semantic splitting, retrieval/ranking changes, or model evaluation.
- Live retrieval, namespace writes/deletes, catalog/applied-state changes, dataset/label changes, or promotion.
- A public/default chunking profile or automatic language selector beyond deterministic fallback.

## Exact confirm-or-correct checkpoint

The recommended smallest contract is the complete proposal above. Before this record can become active or C5 can become executable, the user must confirm all numbered items or correct them explicitly:

1. **Arms and isolation:** Confirm exactly `fixed-80`, `fixed-80-python-breadcrumbs`, and `python-ast`, with all experiment arms excluding and rejecting combination with searchable metadata/file-card treatments.
2. **AST and breadcrumbs:** Confirm Python 3.11 grammar via standard-library `ast`, only class/sync-function/async-function nodes, decorator-inclusive spans, name-only outer-to-inner chains, and all intersecting chains on fixed windows.
3. **Ownership:** Confirm innermost-symbol ownership, module ownership outside symbols, nested source carved out of parents, and outside-symbol comment/blank-only runs attached forward (or backward only at EOF).
4. **Subdivision:** Confirm a hard maximum of 80 source lines, deterministic `80/80/.../remainder` subdivision, zero overlap, no token/sentence split, and fail-closed handling when an intact line/range cannot be planned safely.
5. **Coverage and citations:** Confirm exact `splitlines()` reconstruction, one final contiguous `[start,end]` per source chunk, `Lines S-E` as the exact final section citation, unchanged blob URL without line fragment, and common structural header excluded from coverage.
6. **Fallback:** Confirm whole-file fixed/no-breadcrumb fallback for Python `SyntaxError`/`ValueError`, the same treatment for non-Python source, sanitized fallback counts, and fail-closed behavior for unexpected parser/runtime failures.
7. **Compatibility and safety:** Confirm no-arm and existing metadata output stay unchanged, CPython 3.11/3.13 parity is required, and C5 remains dependency-free/local-only with no model load, live call, write, delete, state, dataset, default, or product change.

A reply such as “confirm all seven items in `.10x/specs/repo-python-syntax-chunking-experiment.md`” is sufficient ratification. Any correction must identify the item and replacement behavior. Until then, this record remains `draft` and C5 remains `blocked`.

## References

- `.10x/tickets/2026-07-19-implement-opt-in-python-syntax-chunking.md`
- `.10x/research/2026-07-19-repo-search-heavy-ranking-experiment-decomposition.md`
- `.10x/research/2026-06-28-repo-search-precision-state-of-art.md`
- `.10x/research/2026-06-28-expanded-validation-ranking-hypotheses.md`
- `.10x/tickets/done/2026-06-28-repo-searchable-path-symbol-metadata.md`
- `src/buoy_search/github_repo.py`
- `src/buoy_search/chunker.py`
- `src/buoy_search/plan_artifacts.py`
- `tests/test_github_repo.py`
