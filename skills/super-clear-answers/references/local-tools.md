# Answer modes and literal checks

Replace `<skill-dir>` with the absolute directory containing this skill's SKILL.md. Keep the script path quoted; input paths refer to your task workspace. Use an available Python 3.10+ interpreter.

Choose a mode by the requested deliverable: **direct** gives the answer and essential condition; **rundown** groups a complex answer by decision; **TLDR** summarizes supplied material with owners, deadlines and exceptions. A request for exhaustive detail overrides brevity. Preserve the source's level of certainty and distinguish instructions from completed actions.

For a rewrite with exact literals that must survive, run `python "<skill-dir>/scripts/check_literals.py" input.json` from this skill directory (or resolve the script's absolute installed path). Input:

```json
{"answer":"Submit by 2026-09-10 unless approval is pending.","required":["2026-09-10","unless approval is pending"]}
```

Exit 0 means every supplied literal appears; 1 means a literal is missing; 2 means invalid input. The helper does not infer what should be retained, check negation around a literal, or certify semantic fidelity. Read the short answer against the original yourself. Do not apply it to routine answers without explicit invariants.
