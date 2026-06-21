Status: open
Created: 2026-06-20
Updated: 2026-06-20
Parent: .loom/tickets/2026-06-20-generic-site-rag-incremental-plan-apply.md
Depends-On: .loom/tickets/2026-06-20-apply-cli-incremental-upsert.md, .loom/specs/generic-site-rag-incremental-plan-apply.md, .loom/decisions/generic-site-rag-incremental-state.md

# Apply Stale Delete Guardrail

## Scope

Add explicit stale-row delete behavior to generic site apply.

In scope:

- Ensure plans report stale rows from local applied state.
- Ensure apply without `--delete-stale` never deletes rows.
- Preserve stale rows in local state as retained stale rows when not deleted.
- Add `--delete-stale` for approved apply.
- Delete exact stale row IDs only after artifact verification, namespace verification, and explicit approval.
- Update local state to remove or mark deleted rows after successful delete.
- Tests with a fake turbopuffer writer/deleter.

Out of scope:

- Namespace deletion.
- Automatic deletes by default.
- Live delete execution without explicit user approval.
- Remote state reconciliation.

## Command sketch

Approved upsert while retaining stale rows:

```bash
turbo-search apply --plan <plan.json> --namespace <namespace> --approve
```

Approved upsert and delete stale rows:

```bash
turbo-search apply --plan <plan.json> --namespace <namespace> --approve --delete-stale
```

## Acceptance criteria

- Plans show stale row count and row IDs/details needed for deletion.
- Apply preflight shows whether stale rows would be retained or deleted depending on flags.
- Apply without `--delete-stale` performs zero delete calls.
- Apply without `--delete-stale` keeps stale rows visible in local state as retained stale rows.
- Apply with `--delete-stale` deletes only stale row IDs from the plan.
- If delete fails, local state is not updated as if the delete succeeded.
- Tests cover retained stale rows, explicit delete, delete failure, and no accidental deletes in preflight.

## Progress and notes

- 2026-06-20: Ticket opened because user explicitly chose delete-by-flag behavior.

## Blockers

- Exact turbopuffer delete API/SDK shape must be verified before live usage.
