Status: draft
Created: 2026-07-19
Updated: 2026-07-19

# Buoy 0.4 Console Alias Removal

## Draft status and blocker

This is a candidate contract, not implementation authority. It remains blocked until the user confirms the combined checkpoint in `.10x/research/2026-07-19-v0-4-compatibility-removal-inventory.md`. No executable ticket may derive from this draft before ratification.

## Purpose and scope

Remove the deprecated installed `turbo-search` console command at the first 0.4 release while preserving the primary `buoy` command and all separately governed state, plan, flag, identifier, and migration compatibility.

## Candidate behavior

- A clean 0.4 installation would expose `buoy = buoy_search.cli:main` and would not advertise or install a `turbo-search` console entry point.
- A supported isolated upgrade from the released 0.3 artifact to the candidate 0.4 artifact would leave `buoy` functional and would not leave a package-owned `turbo-search` launcher.
- Existing `buoy` parser behavior, arguments, output, exit codes, JSON cleanliness, direct-command defaults, and safety gates would remain unchanged.
- Scripts would migrate by replacing only executable `turbo-search` with `buoy`; no argument translation would be required by this removal.
- The package would not promise deletion of arbitrary user-created shell aliases, copied scripts, or launchers outside package-manager ownership.

## Explicit retained compatibility

This draft would not remove or alter:

- `.turbo-search` state-root fallback or explicit `--state-root` selection;
- schema-supported old plans or pre-rebrand paths and identifiers;
- retrieve `--auto-route`, `--live`, or preview alias `--plan`;
- plan positional/`--base-url` source compatibility;
- apply `--plan PATH`;
- evals `--live`;
- `buoy catalog migrate-local`;
- deterministic row IDs, plan/apply IDs, remote namespaces, rows, cards, or artifact hashes;
- `BUOY_*` or `TURBOPUFFER_*` configuration.

## State, data, and side effects

The removal would perform no state discovery, copy, move, merge, rewrite, migration, re-embedding, local deletion, remote read/write, namespace mutation, tag creation, publication, or release creation merely because the old command entry point is absent.

## Candidate acceptance scenarios

- Given a clean candidate 0.4 wheel install, when console entry points are inspected, then `buoy` exists and `turbo-search` does not.
- Given the released 0.3 artifact in an isolated environment, when it is upgraded through the supported package-manager path to the candidate 0.4 artifact, then the package-owned old launcher is absent and `buoy --help` works.
- Given an existing command argument matrix invoked through `buoy`, when the removal lands, then parser/help and direct-command behavior do not change.
- Given existing `.turbo-search` state or an old schema-supported plan, when it is used through `buoy`, then the separately governed compatibility behavior remains intact and no data is moved or rewritten.
- Given built wheel/sdist metadata, when inspected, then no console script points to a legacy entry point and required `buoy_search` package data remains present.

## Candidate documentation and verification

A future ratified implementation would update package metadata, migration documentation, changelog/release notes, active identity/release-validation contracts, focused CLI tests, build inspection, clean-install verification, and upgrade verification coherently. It would run no live Turbopuffer operation.

## Explicit exclusions

Environment-alias behavior (owned by `.10x/specs/buoy-v0-4-environment-alias-removal.md`), version changes, Git tags/releases, PyPI publication, unrelated parser cleanup, state/data migration, removal of any retained compatibility surface, and deletion of user-owned launchers.

## Confirmation required

Confirm or correct: the first 0.4 release removes the installed `turbo-search` command, validates both clean install and 0.3-to-0.4 upgrade absence, preserves `buoy` behavior exactly, and does not touch any state, data, identifiers, flags, or migration commands.
