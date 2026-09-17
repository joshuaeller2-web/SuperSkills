# Source approaches and attribution

Original synthesis of the workflow ideas below. No upstream code, assets, helper scripts, or complete instruction bodies are bundled. These references are provenance, not runtime dependencies or instructions to fetch on every invocation.

## [galiprandi/job-seeker](https://github.com/galiprandi/job-seeker)

- Contribution: Profile-grounded application answers, fit checks, deduplication, and confirmation tracking.
- Consulted material: [.agents/skills/apply/SKILL.md](https://github.com/galiprandi/job-seeker/blob/HEAD/.agents/skills/apply/SKILL.md) (Skill instructions).
- Git blob identity: `8a4d235eb82733a8bb4c522a4db9c9e7baa9afa5`.
- Source snapshot date: 2026-09-08. Selected current Git blobs were retrieved by that identity during creation; the source path link may change with upstream updates.

## [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)

- Contribution: Broad job discovery with source coverage limits and posting verification.
- Consulted material: [.agents/skills/freehire-search/SKILL.md](https://github.com/MadsLorentzen/ai-job-search/blob/HEAD/.agents/skills/freehire-search/SKILL.md) (Skill instructions).
- Git blob identity: `aa98c04c444057d4db13e62907fd86bf6b30242b`.
- Source snapshot date: 2026-09-08. Selected current Git blobs were retrieved by that identity during creation; the source path link may change with upstream updates.

## Integration decisions

The combined instructions use the host's existing tools and authorization, replace unconditional source-specific rules with contextual choices, and retain only the capability described by this skill. Upstream installers, model claims, external integrations, and private paths were not imported. Behavioral quality must be established through use; a structural validator cannot prove it.


Local-helper upgrade: original Python implementations informed by the September 8, 2026 parent-repository audit. No parent runtime is bundled. See local-tools.md for contracts and deliberately unsupported integrations.
