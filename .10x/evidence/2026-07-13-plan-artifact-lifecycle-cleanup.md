Status: recorded
Created: 2026-07-13
Updated: 2026-07-13
Relates-To: .10x/tickets/done/2026-07-12-local-artifact-retention-and-legacy-state-gc.md, .10x/specs/plan-artifact-lifecycle-cleanup.md

# Plan Artifact Lifecycle Cleanup Validation

## What was observed

- A successful mocked approved apply removes exactly its verified plan directory after the local state commit.
- Failed approved apply retains its plan directory and existing state/history.
- A newly written plan removes only older verified sibling plans with the same namespace; other namespaces and malformed directories remain.
- Candidate directories containing symlinks are retained, and cleanup warnings include the retained path. A cleanup warning does not turn an otherwise successful approved apply into a failure.
- No live Turbopuffer operation or historical-backlog cleanup was run.
- Cleanup rejects any plan target or supersession candidate within the configured state-root tree, even when it has valid plan and manifest files.

## Procedure

1. Ran focused plan-cleanup, apply, and CLI tests.
2. Ran the complete unit suite.
3. Checked whitespace and the staged index.
4. Added state-root boundary regression cases using valid injected plan artifacts under both the default-style `.turbo-search` root and a custom configured state root.

## Results

```text
PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest tests.test_plan_cleanup tests.test_apply_cli tests.test_cli -q
Ran 55 tests in 1.321s
OK

PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest discover -s tests -p 'test_*.py' -q
Ran 194 tests in 4.880s
OK

git diff --check
OK

git diff --cached --quiet
no staged files
```

## What this supports or challenges

Supports the prospective lifecycle contract: pending/preflight/failed plans remain, while successful approved applies and verified same-namespace supersession remove only the plan directories no longer needed. It also supports the deletion boundary: state-root paths are retained even when they contain valid plan artifacts.

## Limits

This evidence uses temporary test artifacts and mocked approved writers. It does not validate live remote writes, retroactive artifact reconciliation, or plan-artifact format compaction.
