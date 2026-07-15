Status: recorded
Created: 2026-07-14
Updated: 2026-07-14
Relates-To: .10x/tickets/done/2026-07-14-explicit-plan-to-retrieval-handoff.md, .10x/specs/apply-to-retrieval-handoff.md

# Apply-to-Retrieval Handoff Validation

## What was observed

Apply preflight and successful approved apply summaries now add the effective Turbopuffer region and two POSIX-shell-safe retrieval commands. The preview and live commands use the verified plan namespace, embedding model, and embedding precision plus runtime region; live differs only by a final `--live`. The primary `buoy` executable and quoted `<query>` placeholder are used.

Human output now identifies source, selected plan path, plan ID, artifact hash, namespace/region, verified model/precision, first-apply state, upsert/unchanged/embedding/stale counts, state path, and an explicit stale intent (`retain N` or `delete N`). Preflight labels commands for use after successful apply; approved output labels them as the next retrieval step. Existing failed-apply paths still emit empty stdout and therefore no success handoff.

## Procedure and validation

Deterministic tests cover:

- JSON additive region and live command tokens;
- POSIX `shlex.join`/`shlex.split` recovery for spaces and shell metacharacters in every dynamic command value;
- automatically selected-plan text with exact plan/source/artifact and decision counters;
- successful approved apply preserving the pre-rebrand namespace `github-doctacon-turbo-search-v1` and verified float16/model settings;
- nonzero stale retain and delete text intent;
- existing failure, state, cleanup, timing, and apply safety regressions.

```text
PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest tests.test_apply_cli -q
Ran 41 tests; OK

PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest discover -s tests -p 'test_*.py' -q
Ran 274 tests; OK

uv lock --check
Resolved 130 packages

uv build --out-dir /tmp/buoy-apply-retrieval-handoff-build
Built buoy_search-0.2.1 wheel and sdist

git diff --check
OK

git diff --cached --name-only
empty
```

The full suite emitted one expected existing cleanup-warning line from a failure-path test; the suite passed.

## What this supports

The implementation satisfies `.10x/specs/apply-to-retrieval-handoff.md` without changing plan verification, latest-plan discovery, namespace identity, credential timing, embedding/writes, deletion, state commit, artifact cleanup, or retrieval execution.

No Turbopuffer API call, live namespace query, embedding model load, or remote mutation was performed for this validation.

## Limits

Shell safety is validated through token round-trip rather than executing generated commands. Real installed-shell rendering and a live retrieval following an approved apply were not exercised and are not required for this ticket. Independent review remains required before closure.
