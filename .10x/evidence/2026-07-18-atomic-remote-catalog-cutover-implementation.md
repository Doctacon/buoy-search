Status: recorded
Created: 2026-07-18
Updated: 2026-07-18
Relates-To: .10x/tickets/2026-07-18-atomic-remote-catalog-cutover.md

# Atomic Remote Catalog Cutover Implementation

## What was implemented

The reviewed inert backend is now wired as one public authority transition in code:

- `buoy catalog` reads and mutates exact `buoy-routing-catalog-v1`; local path authority/options are removed;
- `migrate-local` validates and holds the exact source descriptor/inode through approved writes and reports truthful initial/final state, intended/affected IDs, counts, revisions, requests, and available billing;
- approved apply precomputes and persists remote-bound intent before content writes, conditionally registers after local state commit, and retains truthful pending recovery across conflicts, snapshot failures, and cleanup failures;
- reconcile supports ordinary commit, safe rebase, first-apply manual race, and exact two-independent-read operator acceptance without content replay;
- no CLI namespace defaults to authenticated live namespace/card intersection and deterministic routing; explicit repeatable namespaces bypass the remote catalog; `TURBOPUFFER_NAMESPACE` is ignored for retrieval and `--auto-route` is a compatibility no-op;
- preview/live outputs distinguish read-only routing from content retrieval, and provider payloads remain redacted from messages and tracebacks;
- public documentation/help/changelog describe remote authority and permission boundaries.

## Validation

Credential-free local commands on reviewed HEAD `1ff74c8`:

```text
Python 3.11: 392 tests passed
Python 3.13: 392 tests passed
uv build: wheel and sdist passed
git diff --check: passed
```

Focused checkpoints covered 36 catalog CLI/backend tests, 22 pending/recovery tests, 62 routing/CLI tests, and 74 apply/pending/catalog tests. All newly introduced temporary skips were removed. Hard client sentinels and process environments without `TURBOPUFFER_API_KEY`/`TURBOPUFFER_NAMESPACE` prevented real provider calls.

## Side-effect boundary

No implementation or test command created a provider client against live state, wrote/read credentials, mutated Turbopuffer, queried content namespaces, or changed canonical `.buoy/catalog.json`. One earlier incomplete test-harness run attempted namespace listing with inherited dummy credentials and failed at authentication before any query result or write; the harness was replaced with injected fakes and hard sentinels before validation.

## What this supports

This supports implementation readiness for hosted PR checks and the subsequent fail-closed live seed/branch verification phase. It does not prove live provider normalization or authorize local catalog deletion before integration and post-merge verification.
