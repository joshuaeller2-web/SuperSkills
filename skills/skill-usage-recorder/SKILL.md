---
name: skill-usage-recorder
description: Record which installed skills were used for a request and give one short reason for each. This is an always-run reporting control; it records routing and support skills without replacing the task's primary skill.
---

# Skill Usage Recorder

At the end of every user request, report the skills actually used. Keep the record short and distinguish use from mere availability.

## Record

- Name one **primary skill** that owned the task.
- Name only **supporting skills** whose instructions materially changed the work.
- Give one sentence or short clause explaining why each was used.
- Report only controls actually applied through active house rules: `adhd-focus`, `intent`, `stack-router`, `lean-context`, and `memory-recall`. Do not automatically claim all five. A relevant-context decision is distinct from an actual memory lookup; name only what occurred.
- Do not list a skill merely because it was installed, discovered, mentioned, or available.
- Mark uncertain activation `UNVERIFIED`; never infer automatic activation from file presence.

Use this final-answer shape:

```text
Skills used
- Primary: skill-name — reason.
- Supporting: skill-name — reason.
- Controls observed: applicable controls only — short explanation; otherwise UNVERIFIED.
```

When `F:\Ai Skill Library` is available, also append a compact JSON record with [record_usage.py](scripts/record_usage.py). Record the task label and reasons, not private prompts, credentials, source-document contents, or full conversation text. If the library or script is unavailable, show the final-answer record and state that persistent logging was unavailable.

This skill records usage after the work. It does not become the primary task skill and does not authorize any external action.

## Evidence and script contract

The script appends agent self-report, not host instrumentation. Use `--controls-json '["intent"]'` only for controls actually observed; omitted controls default to an empty list. Use `--supporting-json '[{"skill":"name","reason":"material contribution"}]'` for supporting skills. Status defaults to UNVERIFIED; pass `--status` explicitly for the task's supported outcome. A successful append is not proof of task success, skill effectiveness, or automatic activation.

Schema version 2 adds `usage_evidence: agent_self_report`. The legacy key `always_run_controls` is retained for compatibility but contains only explicitly supplied controls. Older unversioned entries populated all five controls automatically and defaulted status to PASS; do not use those fields as observed activation or outcome evidence. Preserve historical rows; qualify them rather than rewriting history.

Actual usage frequency helps prioritize evaluation. Demonstrating benefit requires comparable task outcomes with and without the skill, including verification quality, corrections, and costs. Avoid logging raw prompts, private documents, or credentials.
