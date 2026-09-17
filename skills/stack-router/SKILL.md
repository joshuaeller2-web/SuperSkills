---
name: stack-router
description: "Apply a lightweight route decision to each request, choose one primary installed skill when needed, route authorized Company OS work to the narrowest responsible agent, and explain master, super, sub-master and minor placement during skill audits."
---

# stack-router

Apply only this small routing contract on each request. Do not load every skill body.

1. Preserve the user's current task and presentation preferences.
2. Clarify intent only when different readings would materially change the work.
3. Prefer an explicitly selected skill. Otherwise choose one primary skill by requested outcome, artifact or path, then semantic trigger.
4. Load a sub-master or minor reference only when its distinct situation matches.
5. Load `super-long-task` for substantial work, context cleanup or explicit token optimization. Recall prior context only when the request depends on earlier work or decisions.

## Route to agents when Company OS is active

Agent routing is an additional decision after skill routing, not a replacement for it. Apply it only when the user invokes Company OS, requests an agent or department, or authorizes delegated company work.

1. Choose the primary shared skill for the work.
2. Read `F:/AI/Company OS/organization.json` and route to the narrowest role whose purpose owns the deliverable. Use `company-chief-of-staff` for unclear, cross-department, or intake-heavy assignments.
3. Load `company-agent-runtime`, then use the selected role's entry in `F:/AI/Company OS/agent-skills/role-skill-map.json` to select one applicable sub-master and the minor method needed now.
4. State the route as `request -> primary skill -> agent role -> agent sub-master/minor -> next owner`.
5. Default to one responsible agent. Add a second specialist only for an independent bounded unit or independent verification. Never activate the whole organization.

An agent title does not expand authority, tools, data access, budget, or the user's scope. Ordinary non-Company OS requests remain on the existing skill route and do not activate an agent.

Follow-ups stay on the current route. An explicit “new task” resets it. Scale verification to the changed artifact and record why a required selected-workflow step was skipped.

For catalog audits, enumerate named host/project discovery scopes and show name collisions before reading full bodies. Distinguish identical shared junctions from conflicting implementations. Do not silently choose a same-name source based on enumeration order.

Use the actual installed skill paths and current host invocation mechanism. Do not assume a universal Skill tool or claim a missing skill exists. If no installed skill fits, handle a one-off directly or use super-skill-builder to review the capability gap. Routing must not end an authorized task before the work is done.

Read [draft provenance and incorporated methods](references/draft-methods.md) when revising these methods.

For catalog discovery, read [catalog discovery](references/round-2-catalog-discovery.md).

For the agent-routing decision table and examples, read [agent routing](references/agent-routing.md).
