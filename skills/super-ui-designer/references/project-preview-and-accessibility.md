# Project previews and rendered accessibility

Use only the applicable branch. These are original summaries of reviewed source methods, not installed upstream tools.

## shadcn projects
Identify the project's configured CLI/version and component conventions. If the shadcn CLI is available, inspect its project information with `info` before choosing component changes. Consult that version's help for `add --dry-run` and `--diff [path]`; inspect the proposed files and differences before applying the change. A missing CLI is not permission to run an unpinned latest installer. Use repository inspection and a normal reviewable diff if the CLI is unavailable. An ordinary `add` or `init` can change files and dependencies.

## Tabs and accessibility
Inspect the rendered tab interface: tablist, tab and tabpanel roles, selected state, accessible names, panel associations, focus and arrow-key navigation. Exercise keyboard interactions and report exact failing elements with observed behavior. A source-code check alone does not prove browser accessibility. Apply current accessibility standards only after verifying the relevant criterion; do not claim a fixed checklist count or overall conformance from these checks.

## Provenance and limits
- shadcn-ui/ui, commit `2b3e6d4f8d9161fe5c19340dc383aade392012dd`, `apps/v4/content/docs/(root)/cli.mdx`: https://github.com/shadcn-ui/ui/blob/2b3e6d4f8d9161fe5c19340dc383aade392012dd/apps/v4/content/docs/%28root%29/cli.mdx
- thedaviddias/Front-End-Checklist, commit `30756a79b2f7d4363ac592710146c8e28fa9f1b5`, `skills/tabs-accessibility/SKILL.md`: https://github.com/thedaviddias/Front-End-Checklist/blob/30756a79b2f7d4363ac592710146c8e28fa9f1b5/skills/tabs-accessibility/SKILL.md

Round 1, reviewed 2026-09-14. Source text was inspected; upstream CLI execution and model-driven behavioral improvement remain UNAVAILABLE. No upstream bodies or assets copied. Front-End-Checklist license not established by the review.
