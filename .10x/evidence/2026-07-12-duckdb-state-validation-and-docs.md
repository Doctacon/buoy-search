Status: recorded
Created: 2026-07-12
Updated: 2026-07-12
Relates-To: .10x/tickets/done/2026-07-12-duckdb-state-validation-and-docs.md, .10x/specs/compact-duckdb-applied-state.md

# DuckDB State Validation and Documentation

## What was observed

- User-facing documentation now describes per-namespace `.turbo-search/state/<site-id>/<namespace>/state.duckdb` state, archive-and-reset legacy migration, compact apply summaries, and namespace-scoped fail-fast applies.
- No Quack dependency, configuration, source, or test reference exists in `pyproject.toml`, `uv.lock`, `src`, or `tests`.
- The stable ignored source identifier for the measurement is `.turbo-search/state/github-duckdb-duckdb/github-duckdb-duckdb-v1/last-applied.json`. At measurement time it contained 82,813 rows, occupied 47,917,691 bytes, and had SHA-256 `7bd22371eda3b4fcf389a5699707ffdab98fbf3dfa37353cedddb143e859d969`.
- The equivalent temporary DuckDB current ledger occupied 19,673,088 bytes (about 58.9% smaller). No source content, credential, or row value was printed.

## Procedure

Run this from the repository root. It reads the identified ignored legacy JSON ledger, parses it through the existing domain boundary, writes an equivalent active ledger only under an automatically removed temporary state root, and prints only the stable identifier, counts, byte sizes, and hash:

```bash
SOURCE_PATH='.turbo-search/state/github-duckdb-duckdb/github-duckdb-duckdb-v1/last-applied.json' \
uv run python - <<'PY'
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory

from turbo_search.applied_state import applied_state_from_json, save_applied_state

source = Path(os.environ["SOURCE_PATH"])
source_bytes = source.read_bytes()
state = applied_state_from_json(json.loads(source_bytes))
with TemporaryDirectory(prefix="turbo-search-state-measure-") as temp_dir:
    state_root = Path(temp_dir)
    paths = save_applied_state(state, state_root=state_root)
    print(f"source_path={source}")
    print(f"source_bytes={len(source_bytes)}")
    print(f"source_sha256={hashlib.sha256(source_bytes).hexdigest()}")
    print(f"rows={len(state.rows)}")
    print(f"duckdb_path={paths.database_path.name}")
    print(f"duckdb_bytes={paths.database_path.stat().st_size}")
PY
```

Observed output:

```text
source_path=.turbo-search/state/github-duckdb-duckdb/github-duckdb-duckdb-v1/last-applied.json
source_bytes=47917691
source_sha256=7bd22371eda3b4fcf389a5699707ffdab98fbf3dfa37353cedddb143e859d969
rows=82813
duckdb_path=state.duckdb
duckdb_bytes=19673088
```

The temporary directory is removed on exit. The command does not touch `.turbo-search/`, load embeddings, or call Turbopuffer.

Additional validation:

1. Searched dependency/config/source/test paths for Quack.
2. Ran targeted migration, locking, and diff tests plus the complete unit suite.
3. Inspected documentation changes and ran `git diff --check` with no staged files.

## Results

```text
PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest tests.test_applied_state tests.test_apply_cli tests.test_plan_diff -q
Ran 39 tests in 1.664s
OK

PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest discover -s tests -p 'test_*.py' -q
Ran 186 tests in 5.027s
OK

git diff --check
OK

git diff --cached --quiet
no staged files
```

## What this supports or challenges

Supports that the compact DuckDB current-state format substantially reduces storage for a representative existing ledger and that documentation matches the active embedded, no-Quack concurrency contract.

## Limits

The measurement is reproducible only while the identified ignored source file still exists with the recorded SHA-256; a changed source must be remeasured and recorded. It isolates one legacy ledger and one current-row DuckDB representation; it does not estimate plan-artifact storage, future DuckDB file growth, or reclaimable space from legacy archives. No live Turbopuffer operation was run.
