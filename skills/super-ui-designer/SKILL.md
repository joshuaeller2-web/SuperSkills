---
name: super-ui-designer
description: "Design, refine, audit, or redesign websites and application interfaces using real references, coherent visual decisions, accessible interactions, and responsive verification. Use for UI work and visual critique, not backend-only changes."
---

# Super UI Designer

Make the interface fit its users, content, and task. Distinctive design is a result of coherent decisions, not a compulsory decorative style.

## Route by intent

| Request | Work |
| --- | --- |
| Audit or critique | Inspect and report ranked findings; do not edit unless asked |
| Study a reference | Extract visual principles and observed tokens; distinguish measurements from estimates |
| Refine | Preserve the existing identity, behavior, and content while fixing the named weaknesses |
| Redesign or build | Change the visual structure within the authorized scope while preserving product requirements |

Inspect existing screens, components, tokens, and the supplied references before deciding the visual direction. A missing design document does not mean the project has no design. Use the host's required authoring tools when applicable.

## Choose a coherent direction

- Determine the audience, main task, content hierarchy, existing brand, and desired density. Ask only about a consequential uncertainty.
- Read actual reference images or rendered pages. Record useful relationships: hierarchy, spacing, type scale, color roles, layout rhythm, materials, and motion. Do not claim exact fonts or color values from an uncertain image estimate.
- Reuse the project's established tokens. When needed, define a small set for typography, spacing, color, radii, and interactive states; apply them consistently.
- Marketing pages can prioritize narrative and expressive composition. Product screens prioritize task completion, information density, feedback, and navigation. Do not transfer a dramatic landing-page layout blindly to a data-heavy dashboard.
- Choose section structure from the content. Avoid mechanically repeating a hero and equal-card grid, but honor an explicitly requested aesthetic even if it is common.

## Implement and inspect

Use real content or clearly labeled placeholders. Preserve factual claims, routes, component boundaries, and working behavior outside the requested change. New typography or assets must be available and suitable for the project; do not assume an upstream asset library was installed with this skill.

Check the relevant viewport sizes, readable contrast, keyboard navigation, visible focus, semantic labels, loading and empty states, errors, and reduced-motion behavior. Keep motion purposeful and avoid making it necessary to access content.

For conformance claims, verify the applicable standard's current criterion, number, and level. Distinguish a poor visible-label pattern from a confirmed missing computed accessible name; inspect the actual accessibility mapping before declaring a naming failure. When the evidence is only a description, qualify findings that depend on browser behavior or unobserved styles.

Render the changed interface, inspect it, fix concrete defects in a batch, then repeat the exact failing interaction and verify the resulting focus, selection, state, and visible feedback. Stop polishing when the requested outcome and checks are satisfied; continue if an important defect remains. If rendering is unavailable, report the visual result as unverified rather than implying a screenshot was inspected.

Read [sources](references/sources.md) only for provenance or to revise the combined approach.

## Local tools and extended methods

For the matching task, read [local tools and methods](references/local-tools.md). Use only the relevant helper; resolve script paths from this installed skill directory. The guide gives exact input formats, exit meanings and limits. Successful helper output does not establish facts outside its declared checks.

## Reviewed optional method

For shadcn component changes or rendered tab accessibility reviews, Read [project-preview-and-accessibility](references/project-preview-and-accessibility.md).

## Consolidated draft methods

For ui-design, read [incorporated draft methods](references/draft-methods.md).

For motion and component polish, read [motion and component polish](references/round-2-motion-and-component-polish.md).

For overlay titles, read [overlay titles](references/round-1-overlay-titles.md).
