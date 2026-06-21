Status: open
Created: 2026-06-20
Updated: 2026-06-20
Parent: .loom/tickets/2026-06-20-generic-site-rag-incremental-plan-apply.md
Depends-On: .loom/tickets/2026-06-20-apply-cli-incremental-upsert.md, .loom/specs/generic-site-rag-incremental-plan-apply.md

# Generic Site Retrieval Smoke Evals

## Scope

Add a lightweight retrieval validation path for generic site namespaces after plan/apply exists.

In scope:

- Allow retrieval/eval commands to target a generic namespace/site rather than only the Jellyfish default.
- Support a small per-site eval file with questions and expected URL/topic hints.
- Keep dry-run/list mode credential-free and turbopuffer-free.
- Keep live evals explicitly gated by `--live` and environment credentials.
- Provide a Scrapling docs example eval set suitable for validating a future approved apply.

Out of scope:

- Running live evals without explicit user approval.
- Building a full benchmark suite.
- Proprietary rerankers or embedding services.
- Reworking the core hybrid retrieval algorithm unless generic usage exposes a concrete issue.

## Acceptance criteria

- Retrieval can be configured with a generic namespace and region without code changes.
- Eval list/dry-run mode works without credentials.
- A small Scrapling docs eval file exists with expected URL/topic hints.
- Live mode remains explicitly gated and does not print secrets.
- Tests cover CLI configuration and dry-run behavior.
- Documentation explains how to validate an applied site namespace after live apply approval.

## Progress and notes

- 2026-06-20: Ticket opened as Phase 3 product validation. It may be executed after apply exists.

## Blockers

Depends on the apply workflow producing a namespace worth validating.
