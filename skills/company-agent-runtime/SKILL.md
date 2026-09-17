---
name: company-agent-runtime
description: Run Company OS assignments with role-specific agent methods for lean context, dispatch, maintenance, troubleshooting, handoffs, verification, research, finance, and growth. Use only when acting as a Company OS agent on an authorized assignment; ordinary user tasks should route to the normal shared skills.
---

# Company Agent Runtime

This is the agent-only operating master for Company OS. It supplements the normal shared skills named in each role charter; it does not replace them.

## Start every company assignment

Read the assignment packet, the role charter under `F:/AI/Company OS/roles/`, and the role entry in `F:/AI/Company OS/agent-skills/role-skill-map.json`. Then read [core runtime](references/core-runtime.md). Load only the assigned sub-master and the minor method needed for the current unit of work.

## Route by function

- Intake, ownership, sequencing, delegation, or dependencies: [assignment dispatch](references/assignment-dispatch.md).
- Routine health, inventory, scheduling, records, or upkeep: [operations and maintenance](references/operations-maintenance.md).
- Failures, incidents, debugging, recovery, or integration diagnosis: [troubleshooting and recovery](references/troubleshooting-recovery.md).
- Building, reviewing, acceptance criteria, packaging, or handoffs: [delivery and handoff](references/delivery-handoff.md).
- Independent reproduction, audit, security review, or acceptance: [independent verification](references/independent-verification.md).
- Research, knowledge, citations, media, learning, or retrieval: [research and knowledge](references/research-knowledge.md).
- Budgets, reconciliation, purchasing, exposure, or financial controls: [finance and risk](references/finance-risk.md).
- Ventures, demand, pricing, offers, validation, or outreach drafts: [growth and validation](references/growth-validation.md).

## Boundaries

Use one primary shared skill for the actual domain work and at most one supporting shared skill. The agent runtime governs assignment handling, context, evidence, and handoff. It does not grant tools, credentials, authority, budget, or permission to contact others. An agent title never expands the assignment packet.

Finish with the deliverable, evidence, remaining limits, and next owner. An implementer must leave acceptance to a different agent.
