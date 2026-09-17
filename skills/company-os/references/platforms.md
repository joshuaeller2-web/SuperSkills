# Platform access

Canonical organization: `F:/AI/Company OS/organization.json`.
Human help: `QUICK-REFERENCE.md`, `USER-MANUAL.md`, `COMPANY-GUIDE.html` under that folder.
Agent workflow: `OPERATING-MANUAL.md` and `POLICY.md` under that folder.

## Codex

In a fresh task, request: `Use $company-os to act as Chief of Staff for [goal]. Scope: [folder or project]. Return: [deliverable]. Use the relevant specialists and a separate verifier.`

Custom definitions live in `C:/Users/joshu/.codex/agents/company-<role-id>.toml`. Inspect available delegation tools before invoking an agent; never claim a role was instantiated just because you adopted its charter. Use subagents for bounded work when authorized; do not create new sidebar tasks without a request for new tasks.

## Claude Code

Ask Claude Code to use the `company-os` skill, or start its executive agent with `claude --agent company-chief-of-staff` from the intended workspace. Definitions live in `C:/Users/joshu/.claude/agents/company-<role-id>.md`. Ordinary Claude web chat does not automatically load these local definitions. For web chat, supply the relevant manual/charter text and task packet yourself.

## Hermes

Start intake with `hermes -p company-chief-of-staff chat` or `F:/AI/Company OS/Open Chief of Staff.cmd`. Ask it to load the `company-os` skill. Profiles live in `C:/Users/joshu/AppData/Local/hermes/profiles`.

Check `F:/AI/Company OS/evidence/hermes-setup.json` and actual profile folders for the installed executive mapping. Do not assume every catalog specialist has a Hermes profile. Route specialist work through the Chief of Staff, using a charter or a file handoff to Codex/Claude Code as appropriate. Native Bot Chat visibility and bot-to-bot messaging require separate live verification; a working CLI profile is not proof of either.

## Discovery and routine status

The canonical skill lives in `F:/Ai Skill Library/Skills/Combined/company-os`; host discovery links point there. A fresh session may be needed after installation. Installed files do not prove a model has loaded them.

For routine questions, inspect the current Codex automation and Company OS workflow evidence. Do not reuse an old schedule as confirmed current, extend its review boundary, or trigger paid model calls merely to demonstrate this help skill.
