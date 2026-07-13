Status: recorded
Created: 2026-07-12
Updated: 2026-07-12
Relates-To: .10x/tickets/done/2026-07-12-purge-legacy-json-during-duckdb-migration.md, .10x/specs/compact-duckdb-applied-state.md

# Legacy JSON Delete-and-Reset Validation

## What was observed

- First access to a namespace with legacy `last-applied.json` first initializes and atomically installs an empty valid `state.duckdb`, then deletes the JSON; legacy rows are not imported.
- If temporary DuckDB initialization fails, the legacy JSON remains intact, no active database is installed, and the temporary database path is removed.
- Existing `legacy-json/` state artifacts are removed when the matching namespace state is accessed. No new archive directory is created.
- The repository-local cleanup pass found no existing `legacy-json/` directories to remove: `legacy_json_paths_deleted=0`.
- Documentation and the project skill now describe delete-and-reset migration.

## Procedure

1. Ran targeted state tests, including a mocked DuckDB schema-initialization failure proving the JSON survives and no temporary or active database remains, then ran the complete test suite.
2. Ran this local-only cleanup under `.turbo-search/state`, which deletes only entries named `legacy-json` without reading their contents:

```bash
uv run python - <<'PY'
from pathlib import Path
import shutil

root = Path('.turbo-search/state')
deleted = []
if root.is_dir():
    for path in sorted(root.rglob('legacy-json')):
        if path.is_symlink():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)
        else:
            continue
        deleted.append(path.relative_to(Path('.turbo-search')))
print(f'legacy_json_paths_deleted={len(deleted)}')
for path in deleted:
    print(f'deleted={path}')
PY
```

3. Verified no `legacy-json` directories remain under `.turbo-search/state`.

## Results

```text
PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest tests.test_applied_state -q
Ran 13 tests in 1.847s
OK

PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest discover -s tests -p 'test_*.py' -q
Ran 187 tests in 6.295s
OK

legacy_json_paths_deleted=0
find .turbo-search/state -type d -name legacy-json
0

git diff --check
OK
```

## Limits

No Turbopuffer operation, embeddings, or credential read occurred. The cleanup pass is limited to existing `legacy-json` state directories; historic `history/` snapshots and plan artifacts are outside this ticket.
