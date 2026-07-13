Status: recorded
Created: 2026-07-12
Updated: 2026-07-12
Target: .pi/skills/turbopuffer-site-rag/SKILL.md, /Users/crlough/.pi/agent/skills/turbo-search-retrieve/SKILL.md, .10x/evidence/2026-07-12-turbopuffer-env-key-validation.md
Verdict: pass

# Turbopuffer `.env` Skill Review

## Findings

No blocking findings.

- Both skills now match the current Turbopuffer code path: `src/turbo_search/retriever.py` and `src/turbo_search/apply.py` read `TURBOPUFFER_API_KEY` from the process environment, while `src/turbo_search/config.py` reads only non-secret runtime values.
- Both `.env` snippets use a subshell plus `set -a; . ./.env; set +a`, which was validated against the repository `.env` without printing a secret. The global-skill form using `uv run --directory` also exited successfully.
- The retrieval skill no longer describes the deleted Qdrant runtime, Compose service, or Qdrant result fields. Its live-result fields match `RetrievalResult.to_dict()`.
- The evidence record distinguishes authentication and local unit-test success from the missing remote namespace and does not treat a 404 as successful retrieval.

## Residual risk

The current Turbopuffer account has no existing namespace to retrieve. Restoring an indexed corpus requires a separately approved plan and live apply; this review does not authorize or perform that mutation.
