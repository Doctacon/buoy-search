Status: open
Created: 2026-07-19
Updated: 2026-07-19
Parent: .10x/tickets/2026-07-19-buoy-v0-4-compatibility-removal-plan.md
Depends-On: None

# Remove Buoy 0.4 Environment Aliases

## Scope

Implement `.10x/specs/buoy-v0-4-environment-alias-removal.md`:

- replace fallback/warning/conflict selection for exactly `TURBO_SEARCH_EMBEDDING_MODEL` and `TURBO_SEARCH_EMBEDDING_PRECISION` with the ratified presence-rejection gate;
- invoke the gate after successful parsing and before every actual primary CLI or autoresearch handler/experiment dispatch;
- preserve help/version, parser failures, parsed no-handler help, current variables/defaults/overrides, plan-derived apply configuration, and every unrelated compatibility surface;
- update focused config/CLI/autoresearch tests and only environment-migration/changelog/spec references affected by this removal.

## Acceptance criteria

- Each old name rejects on presence, including an empty value and old+new equal/different combinations; no old value becomes effective.
- Actual `crawl`, `plan`, `apply`, `namespaces`, `retrieve`, `evals`, every catalog subcommand, and autoresearch invocation return 2 before sentinel handler dispatch or any read/write/model/credential/remote side effect.
- Model-only, precision-only, and both-present diagnostics match the active specification byte-for-byte; both-present order is model then precision under either environment insertion order; no value is printed.
- Rejection emits no stdout, including with `--json`, and emits exactly one newline-terminated stderr diagnostic.
- `buoy --help`, `buoy --version`, each top-level and catalog-subcommand help path, bare `buoy`, bare `buoy catalog`, `python -m buoy_search --help`, and autoresearch help remain available with old names present. Malformed arguments retain argparse behavior.
- With old names absent, all existing `BUOY_*`, `TURBOPUFFER_*`, defaults, CLI overrides, plan authority, parser/output, direct-command, state/data, catalog, identifier, and remote behavior remain unchanged.
- Focused config/CLI/autoresearch and no-side-effect tests, complete Python 3.11/3.13 suites, distribution checks, migration-reference checks, independent review, and hosted checks pass.

## Validation and evidence expectations

Record exact changed files; table-driven command/help/version coverage; old/new/empty/insertion-order matrix; exit/stdout/stderr bytes; sentinel call traces; checks proving autoresearch rejects before experiment reads and commands reject before local/remote effects; focused/full commands and results; hosted identities; and explicit no-state/no-data/no-remote attestation. Redact all environment values from evidence.

## Dependencies and parallelism

No child execution dependency. Work may proceed in parallel with `.10x/tickets/2026-07-19-remove-buoy-v0-4-console-alias.md`, but both reviewed diffs must be assembled into one aggregate 0.4.0 candidate before integration to `develop`.

## Blockers

None.

## Explicit exclusions

Console-script/`legacy_main` changes; version/tag/publication work; changes to current variables/defaults or `TURBOPUFFER_*`; plan schemas; state/data migration; remote operations; any unrelated compatibility removal; stale skill-reference correction.

## References

- `.10x/tickets/2026-07-19-buoy-v0-4-compatibility-removal-plan.md`
- `.10x/specs/buoy-v0-4-environment-alias-removal.md`
- `.10x/specs/buoy-v0-4-console-alias-removal.md`
- `.10x/specs/buoy-local-compatibility.md`
- `.10x/specs/embedding-inference-precision.md`

## Progress and notes

- 2026-07-19: Opened from the ratified active environment-removal specification. No implementation performed.
