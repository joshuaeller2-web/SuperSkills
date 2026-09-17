# Contextual code review

Establish intended behavior, architecture and constraints before judging changed lines. Inspect adjacent implementations and existing review discussion to avoid inconsistent or repeated findings. Review ownership, layering, complexity, regression triggers, security boundaries and missing behavioral tests.

Rank actual findings by severity: a review-category sequence must not demote a serious security defect. Each finding names the triggering condition, practical consequence, precise location and concrete correction. Save Markdown findings in an appropriate local artifact when useful. Do not assume tmp is ignored, require Linear, impose arbitrary function lengths or publish automatically.

## Provenance

Round 1, n8n-io/n8n, commit `8123c2ca468d80458555626a01ae74521c4c7d3d`.

- https://github.com/n8n-io/n8n/blob/8123c2ca468d80458555626a01ae74521c4c7d3d/.agents/skills/human-like-code-review/SKILL.md

Original scoped synthesis from inspected primary source. Upstream software and runtime dependencies are not installed by this reference. Behavioral effectiveness remains unverified until task trials.
