# Source approaches and attribution

Original synthesis of the workflow ideas below. No upstream code, assets, helper scripts, or complete instruction bodies are bundled. These references are provenance, not runtime dependencies or instructions to fetch on every invocation.

## [staskh/trading_skills](https://github.com/staskh/trading_skills)

- Contribution: Explicit risk metrics, measurement periods, and position context.
- Consulted material: [.claude/skills/risk-assessment/SKILL.md](https://github.com/staskh/trading_skills/blob/HEAD/.claude/skills/risk-assessment/SKILL.md) (Skill instructions).
- Git blob identity: `e52cc9e0d600ce4ecf953a0d0194505fd9b8c224`.
- Source snapshot date: 2026-09-08. Selected current Git blobs were retrieved by that identity during creation; the source path link may change with upstream updates.

## [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills)

- Contribution: Rule-based backtests, realistic friction, and robustness checks.
- Consulted material: [skills/backtest-expert/SKILL.md](https://github.com/tradermonty/claude-trading-skills/blob/HEAD/skills/backtest-expert/SKILL.md) (Skill instructions).
- Git blob identity: `df6ecfb11c2cbf1d1192d87a7deec3b3aeb5c503`.
- Source snapshot date: 2026-09-08. Selected current Git blobs were retrieved by that identity during creation; the source path link may change with upstream updates.

## [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire)

- Contribution: Business quality, valuation, incentives, counterarguments, and evidence uncertainty.
- Consulted material: [codex-skills/investment-research/SKILL.md](https://github.com/xbtlin/ai-berkshire/blob/HEAD/codex-skills/investment-research/SKILL.md) (Skill instructions).
- Git blob identity: `5ae8c2370d31077f12cb9abcf4dee788eee52206`.
- Source snapshot date: 2026-09-08. Selected current Git blobs were retrieved by that identity during creation; the source path link may change with upstream updates.

## Integration decisions

The combined instructions use the host's existing tools and authorization, replace unconditional source-specific rules with contextual choices, and retain only the capability described by this skill. Upstream installers, model claims, external integrations, and private paths were not imported. Behavioral quality must be established through use; a structural validator cannot prove it.


Local-helper upgrade: original Python implementations informed by the September 8, 2026 parent-repository audit. No parent runtime is bundled. See local-tools.md for contracts and deliberately unsupported integrations.
