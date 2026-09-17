# Source approaches and attribution

Original synthesis of the workflow ideas below. No upstream code, assets, helper scripts, or complete instruction bodies are bundled. These references are provenance, not runtime dependencies or instructions to fetch on every invocation.

## [bradautomates/claude-video](https://github.com/bradautomates/claude-video)

- Contribution: Captions-first research with optional visual sampling.
- Consulted material: [skills/watch/SKILL.md](https://github.com/bradautomates/claude-video/blob/HEAD/skills/watch/SKILL.md) (Skill instructions).
- Git blob identity: `7cd78b6aac3a4c66f4e8b0b57830070b2cf3e71d`.
- Source snapshot date: 2026-09-08. Selected current Git blobs were retrieved by that identity during creation; the source path link may change with upstream updates.

## [taoufik123-collab/claude-watch](https://github.com/taoufik123-collab/claude-watch)

- Contribution: Scene-aware editorial analysis and close inspection of the opening hook.
- Consulted material: [SKILL.md](https://github.com/taoufik123-collab/claude-watch/blob/HEAD/SKILL.md) (Skill instructions).
- Git blob identity: `698e952c27ceb0207aecff1f27dd635219fd6201`.
- Source snapshot date: 2026-09-08. Selected current Git blobs were retrieved by that identity during creation; the source path link may change with upstream updates.

## [JCodesMore/youtube-for-ai-agents](https://github.com/JCodesMore/youtube-for-ai-agents)

- Contribution: Video discovery and cross-video research using explicit metadata and timestamps.
- Consulted material: [skills/youtube/SKILL.md](https://github.com/JCodesMore/youtube-for-ai-agents/blob/HEAD/skills/youtube/SKILL.md) (Skill instructions).
- Git blob identity: `a748682ee73bca3b7d607ff1e7cf46068068c73e`.
- Source snapshot date: 2026-09-08. Selected current Git blobs were retrieved by that identity during creation; the source path link may change with upstream updates.

## Integration decisions

The combined instructions use the host's existing tools and authorization, replace unconditional source-specific rules with contextual choices, and retain only the capability described by this skill. Upstream installers, model claims, external integrations, and private paths were not imported. Behavioral quality must be established through use; a structural validator cannot prove it.


Local-helper upgrade: original Python implementations informed by the September 8, 2026 parent-repository audit. No parent runtime is bundled. See local-tools.md for contracts and deliberately unsupported integrations.
