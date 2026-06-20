Status: blocked
Created: 2026-06-20
Updated: 2026-06-20
Parent: .loom/tickets/2026-06-20-turbopuffer-jellyfish-rag-plan.md
Depends-On: .loom/tickets/2026-06-20-turbopuffer-hybrid-retrieval-client.md, .loom/specs/turbopuffer-jellyfish-rag.md, .loom/knowledge/turbopuffer-rag-vocabulary.md

# Define agent answering workflow over retrieved chunks

## Scope

Make it clear how the agent should answer future user questions using turbopuffer retrieval over the Jellyfish docs.

In scope:

- Document the command the agent should run for retrieval.
- Define expected retrieval output format.
- Define citation behavior for answers.
- Optionally add a convenience command that formats retrieved context into a prompt-friendly bundle.
- Add guardrails: answer only from retrieved context, say when retrieval is insufficient, and cite URLs/titles.

Out of scope:

- Building a separate chat UI.
- Adding a proprietary LLM service.
- Replacing the agent's normal answer generation logic.

## Acceptance criteria

- A future agent can read the docs/procedure and know exactly how to retrieve before answering.
- Answers should cite source `url` and `title` for material claims.
- The workflow distinguishes retrieval failure, weak retrieval, and answerable questions.
- The project includes at least one example question showing retrieval output and an answer sketch.

## Progress and notes

- 2026-06-20: Ticket created only.

## Blockers

- User approval to implement.
- Retrieval client output shape must be stable.
