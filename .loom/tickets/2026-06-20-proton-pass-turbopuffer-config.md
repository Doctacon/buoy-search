Status: blocked
Created: 2026-06-20
Updated: 2026-06-20
Parent: .loom/tickets/2026-06-20-turbopuffer-jellyfish-rag-plan.md
Depends-On: .loom/specs/turbopuffer-jellyfish-rag.md

# Configure turbopuffer credentials and runtime settings

## Scope

Prepare runtime configuration for turbopuffer without persisting secrets in the repository.

In scope:

- Identify the Proton Pass item containing the turbopuffer API key.
- Retrieve the key only after user approval and only into the active shell/session environment.
- Establish environment variables:
  - `TURBOPUFFER_API_KEY`
  - `TURBOPUFFER_REGION`
  - `TURBOPUFFER_NAMESPACE`
- Document the chosen region/namespace in non-secret project docs if useful.

Out of scope:

- Committing API keys or generated `.env` files containing secrets.
- Calling turbopuffer write/query APIs beyond a minimal auth/config smoke check if explicitly approved.

## Acceptance criteria

- The implementation can read turbopuffer config from environment variables.
- No secret value is written to project files, Loom records, logs, or committed output.
- If Proton Pass is used, access is justified with `PROTON_PASS_AGENT_REASON` and follows the `proton-pass-agent` skill.
- The ticket progress log records only non-secret facts: item title/vault if acceptable, region, namespace, and whether config was verified.

## Progress and notes

- 2026-06-20: Ticket created only. API key was not accessed.
- Future executor should read `/Users/crlough/.pi/agent/skills/proton-pass-agent/SKILL.md` before any Proton Pass commands.

## Blockers

- User approval to access Proton Pass.
- Need either the Proton Pass vault/item title or explicit permission to search accessible Proton Pass items for the turbopuffer credential.
- Need region confirmation or approval to default `TURBOPUFFER_REGION=gcp-us-central1`.
- Need namespace confirmation or approval to default `TURBOPUFFER_NAMESPACE=jellyfish-site-docs-v1`.
