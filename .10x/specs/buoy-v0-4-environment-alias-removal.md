Status: draft
Created: 2026-07-19
Updated: 2026-07-19

# Buoy 0.4 Environment Alias Removal

## Draft status and blocker

This is a candidate contract, not implementation authority. It remains blocked until the user confirms the combined checkpoint in `.10x/research/2026-07-19-v0-4-compatibility-removal-inventory.md`, especially the old-variable failure behavior. No executable ticket or test may encode that behavior before ratification.

## Purpose and scope

Remove fallback acceptance of exactly two deprecated branded embedding variables at the first 0.4 release:

- `TURBO_SEARCH_EMBEDDING_MODEL` → `BUOY_EMBEDDING_MODEL`;
- `TURBO_SEARCH_EMBEDDING_PRECISION` → `BUOY_EMBEDDING_PRECISION`.

No other `TURBO_SEARCH_*` variable is implemented, and this draft grants no authority over `TURBOPUFFER_*` variables.

## Candidate behavior

Recommended, pending confirmation:

- If either removed variable is present, configuration would fail with exit 2 before model loading, credential use, local mutation, or remote calls.
- The error would name each present old variable and its exact `BUOY_*` replacement without printing variable values.
- Old-only, old+new-equal, and old+new-different input would all fail under this candidate. The old value would never supply an effective model or precision.
- With no old variable present, `BUOY_EMBEDDING_MODEL`, `BUOY_EMBEDDING_PRECISION`, their current defaults, CLI overrides, and validation would remain unchanged.
- Approved apply would continue deriving the effective embedding model and precision from its verified plan; removed ambient aliases would not override or silently alter that contract.

This recommendation intentionally detects removed names for a migration error. The alternative—stop reading them entirely—would make old-only configuration silently select the default model/precision and can cause routing exclusion or explicit-retrieval embedding mismatch. The user must choose; neither behavior is ratified by the existing removal schedule alone.

## Explicit retained compatibility

This draft would not alter:

- `TURBOPUFFER_API_KEY`, `TURBOPUFFER_REGION`, or command-specific `TURBOPUFFER_NAMESPACE` behavior;
- current `BUOY_EMBEDDING_MODEL` / `BUOY_EMBEDDING_PRECISION` semantics;
- CLI model/precision overrides;
- old plans missing `embedding_precision`, which remain interpreted as `float32` under their active contract;
- `.turbo-search` state-root fallback, old plan paths, command flags, source aliases, `catalog migrate-local`, IDs, namespaces, rows, cards, or artifact hashes.

## State, data, and side effects

Configuration rejection would occur before side effects. The removal would not migrate configuration files automatically, rewrite plans or DuckDB ledgers, re-embed content, change deterministic IDs, mutate remote cards/rows/namespaces, or delete local/remote data.

## Candidate acceptance scenarios

- Given only `TURBO_SEARCH_EMBEDDING_MODEL`, when a configuration-consuming command starts, then it fails with the exact replacement name, does not expose the value, and performs no model/credential/state/API work.
- Given only `TURBO_SEARCH_EMBEDDING_PRECISION`, the same fail-before-side-effect behavior occurs.
- Given old and new forms together with equal or different values, the candidate rejects removed-variable presence rather than retaining the 0.3 fallback/conflict matrix.
- Given only current `BUOY_*` variables, current selection, validation, CLI precedence, JSON cleanliness, and command behavior remain unchanged.
- Given approved apply, the verified plan remains authoritative for effective model/precision and no ambient old alias changes the plan contract.
- Given retrieve/evals/autoresearch/config consumers, focused tests prove the same chosen boundary without live Turbopuffer calls.

## Candidate documentation and verification

A future ratified implementation would update `src/buoy_search/config.py`, focused config/CLI tests, migration documentation, changelog/release notes, and active local-compatibility/precision contracts coherently. Secret or configuration values would never be persisted in records or diagnostics.

## Explicit exclusions

Console alias removal (owned by `.10x/specs/buoy-v0-4-console-alias-removal.md`), changes to current variables/defaults, plan-schema changes, state/data migration, remote operations, version/tag/publication work, or removal of any unrelated compatibility.

## Confirmation required

Confirm or correct: 0.4 rejects either removed environment variable—even when the corresponding new variable is also present—with a value-redacting, pre-side-effect migration error. If instead 0.4 should ignore removed variables, explicitly accept the silent-default/mismatch risk described above.
