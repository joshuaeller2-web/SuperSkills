# Independent validation

Use independent validation when a simulation report will guide a consequential decision or be published as evidence.

Give two reviewers the same original question, configuration, output, and objective rubric. Keep their review contexts separate. Require structured criterion-level PASS or FAIL findings. Agreement is required for release; disagreement becomes an unresolved finding rather than majority approval.

Fix only supported findings, then rerun both reviewers fresh. Stop after the declared repair ceiling and escalate remaining failures. Prefer deterministic checks for schema, arithmetic, reproducibility, and invariant enforcement; reviewer agreement does not replace them.

Keep synthetic agreement distinct from external validation. Two reviewers can check whether the report follows its evidence, but they cannot prove the simulated world predicts reality.

Sources reviewed as data:

- `affaan-m/everything-claude-code`, `skills/santa-method/SKILL.md`, commit `8321021`
- `sickn33/antigravity-awesome-skills`, `skills/multi-agent-brainstorming/SKILL.md`, commit `69906dd`

