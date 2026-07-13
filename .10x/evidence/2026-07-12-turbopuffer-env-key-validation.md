Status: recorded
Created: 2026-07-12
Updated: 2026-07-12
Relates-To: .pi/skills/turbopuffer-site-rag/SKILL.md, /Users/crlough/.pi/agent/skills/turbo-search-retrieve/SKILL.md

# Turbopuffer `.env` Credential Validation

## What was observed

- The repository `.env` contains a non-empty `TURBOPUFFER_API_KEY` and is ignored by Git.
- The inherited process `TURBOPUFFER_API_KEY` did not match the `.env` value. Validation therefore sourced `.env` in a subprocess rather than relying on the inherited environment.
- `uv run python -m unittest discover -s tests -p 'test_*.py' -q` passed: 179 tests in 3.122 seconds.
- With the `.env` key, the installed `turbopuffer` 2.4.0 SDK successfully listed namespaces in `gcp-us-central1` without mutation. The first page was empty and had no next page.
- A live `turbo-search retrieve` request using the same `.env` key reached Turbopuffer but received a 404 for the formerly recorded `github-doctacon-turbo-search-v1` namespace. No writes, deletes, or exports occurred.

## Procedure

1. Compared the inherited and `.env` key values only by one-way digest; no value was printed or recorded.
2. Ran the complete local unit suite.
3. Loaded `.env` only in a command subshell with `set -a; . ./.env; set +a`.
4. Called `Turbopuffer(...).namespaces(page_size=100)` and recorded only count/pagination facts.
5. Attempted one read-only `turbo-search retrieve --live` request against the historical namespace recorded in `.10x/evidence/2026-06-28-live-turbo-search-repo-index-and-eval.md`.

## What this supports or challenges

Supports that the renewed `.env` credential authenticates successfully with the installed Turbopuffer SDK and that the current repository code passes its complete local test suite.

Challenges the assumption that the June 2026 repository corpus is still available: the account has no namespaces in the first (and only) page, and the historical namespace returned 404. A new plan plus explicitly approved apply would be required before live repository retrieval can succeed.

## Limits

Listing namespaces validates authentication but does not prove indexing, write permission, or retrieval against an existing corpus. The failed read-only retrieval does not create a namespace or test approved apply, which remain outside this validation scope.
