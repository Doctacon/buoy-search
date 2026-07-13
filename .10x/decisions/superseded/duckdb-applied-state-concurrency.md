Status: active
Created: 2026-07-12
Updated: 2026-07-12

# DuckDB Applied-State Concurrency

## Context

The current applied-state backend writes a full JSON row ledger plus an additional full JSON snapshot for every approved apply under `.turbo-search/state/...`. The local state is 495 MB, while plan artifacts are 4.5 GB. The renewed Turbopuffer account has no namespaces, so existing JSON state claims remote rows that no longer exist and must not suppress the next approved apply.

The operator wants independent `turbo-search` processes to apply different namespaces concurrently. They do not require simultaneous applies to one namespace.

## Decision

Use embedded DuckDB, not Quack, for applied state. Each `(site_id, namespace)` pair owns an independent database at:

```text
.turbo-search/state/<site-id>/<namespace>/state.duckdb
```

The backend will retain one current row ledger and lightweight `apply_runs` summaries indefinitely. It will not retain full row snapshots.

An approved apply must acquire a non-blocking exclusive lock scoped to its own `(site_id, namespace)`. A contending apply must fail clearly before remote mutation. Applies to different namespaces may run concurrently because they use different databases and locks.

Migration will archive the current JSON state but reset the DuckDB ledger empty. This is intentional: the current remote account has no matching namespaces, so importing old rows would incorrectly classify the next apply as unchanged.

## Alternatives considered

- **One shared DuckDB file:** rejected because independent processes would contend on one local writer boundary.
- **DuckDB Quack server:** rejected for this scope. It adds a service, network endpoint, token lifecycle, and beta protocol without helping the required different-namespace parallelism. It also would not make remote Turbopuffer writes and local state updates one transaction.
- **Keep JSON plus bounded history:** rejected because duplicate snapshot storage is the current bloat source and does not improve concurrent writer handling.
- **Allow same-namespace writers:** rejected. A local transaction cannot atomically cover Turbopuffer writes; a namespace-scoped lock is required for coherent remote/local state.

## Consequences

- The project adds the open-source `duckdb` Python dependency and a one-time local migration path.
- Old JSON state remains recoverable as archived local evidence but is not used as active state.
- A failed process after remote writes but before the local transaction leaves state stale; a later approved apply must safely re-upsert, matching the existing recovery model.
- Quack may be reconsidered only for cross-machine shared state or a deliberate centralized state service.
