Status: active
Created: 2026-06-28
Updated: 2026-06-28
Depends-On: .10x/research/2026-06-28-expanded-validation-ranking-hypotheses.md, .10x/tickets/2026-06-28-cross-corpus-validation-basket.md

# Repo Searchable Path and Symbol Metadata

## Scope

Test whether repository indexing improves when generated code pages include searchable path, file-stem, and symbol metadata/breadcrumbs.

This owns the local implementation and validation slice for expanded-validation hypotheses H4 and H5:

- H4: exact path/title/identifier tokens should become searchable text;
- H5: symbol breadcrumbs should be added to code chunks.

## Acceptance criteria

- Add an explicit opt-in plan/crawl option so existing repo planning defaults remain unchanged.
- Include searchable metadata only in generated repository Markdown, not website crawls.
- Keep local-only plan behavior: no credentials, embeddings, turbopuffer calls, writes, deletes, or namespace mutation during local validation.
- Validate with unit tests and local plan/preflight artifacts.
- Do not promote as a default or live-apply new namespaces without separate approval.

## Explicit exclusions

- No Tree-sitter dependency.
- No proprietary model APIs.
- No live apply/reindex in this slice unless separately approved.
- No stale deletion or namespace deletion.

## Blockers

- Live namespace evaluation requires explicit approval after local plan/preflight review.

## References

- `.10x/research/2026-06-28-expanded-validation-ranking-hypotheses.md`
- `.10x/tickets/2026-06-28-repo-oversize-source-indexing.md`

## Progress and notes

- 2026-06-28: Activated after user requested execution of the next three recommended hypotheses.
- 2026-06-28: Added opt-in `--repo-search-metadata`, which includes path tokens, file stem, Python symbol names/tokens, and per-line-window symbol breadcrumbs in generated repository code pages. Local pytest/Typer plans and preflights passed without live writes. Evidence: `.10x/evidence/2026-06-28-repo-oversize-metadata-local-validation.md`.
- 2026-06-28: After explicit user approval for writes/evals to new namespaces, live-applied metadata-only ablations for pytest/Typer. Metadata-only improved both existing seed datasets (`pytest 84.742 -> 85.971`, `Typer 59.423 -> 62.062`) without changing the file-size cap. Metadata-only is now the strongest promotion candidate from this slice, pending validation on the older repo basket. Evidence: `.10x/evidence/2026-06-28-repo-oversize-metadata-live-eval.md`.
