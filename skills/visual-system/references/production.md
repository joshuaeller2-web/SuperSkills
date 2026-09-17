# Production and acceptance by medium

These are local operating rules. Load the relevant lane; do not demand irrelevant outputs.

| Lane | Authoritative work | Preview/export | Acceptance evidence |
| --- | --- | --- | --- |
| UI | Components, actual text, styles/tokens, state logic | Rendered page and assets | Primary action and relevant states exercised in the real application; keyboard/focus and narrow layout inspected |
| Diagram | Nodes, relationships, labels, source IDs and meaning | SVG/HTML or requested image | Required entities and edges reconciled to source; direction/legend checked; readable layout and requested export inspected |
| Scene/game 3D | Native scene or reproducible script, meshes, materials, rig where needed | Renders and destination-compatible asset | Scale/orientation/materials/animation and intended interactions checked after import; actual runtime observations |
| Fabricated 3D | Parametric source, measured dimensions and protected interfaces | Mesh/3MF and assembly view | Geometry checks, real slicer output, and separate fit/physical observations; unresolved physical claims remain unverified |

## UI

Preserve the product's existing identity for narrow fixes. Keep semantic copy in actual UI text rather than baked into generated imagery. Define the primary flow and relevant loading, empty, error, and disabled states. Inspect the actual rendering at a normal and a narrow viewport; check containment, hierarchy, text readability, focus, keyboard operation, and the main action. Check reduced motion if motion exists. Record the tested browser and sizes.

An interactive 3D hero needs a stated purpose. Keep a readable still fallback, avoid obstructing content, and check asset transfer size and runtime behavior on the intended devices when performance claims matter. Stop offscreen rendering if appropriate and verify it, rather than assuming implementation is effective. Do not report a fast page from a screenshot.

## Diagrams

Establish diagram purpose and authoritative facts before styling. Reconcile entities, labels, edge directions, branches, cycles, and state transitions with the supplied source. Do not invent missing relationships to make the composition symmetrical. Retain readable semantic labels; use color plus text or shape for meaning. Inspect crossings, label collisions, grouping, legend, and the requested exported file. An attractive image alone cannot establish semantic correctness. Use Archify's own supported format and validator when available rather than inventing its schema.

## Scene/game 3D

Set units, axes, intended scale, camera/distance, target engine/viewer, and required export before construction. Build distinct functional parts when they need separate animation, materials, variants, or semantics. Keep stable object names and record material/texture dependencies. For informational scenes, carry semantic data alongside the geometry (for example object ID to room name and supplied area). Do not present a modeled area as a surveyed fact.

Inspect silhouettes, topology, normals, intersections, UVs/materials, and dimensions relevant to the brief. Complexity follows camera distance and target constraints, not a universal polygon count. For rigged assets, inspect weights, deformation and each required clip, then test them in the target viewer/game. A still frame cannot establish motion quality; a rendered video cannot establish interactive behavior. Watch the integrated scene for clipping, object disappearance, collision/selection problems, and camera issues. Preserve native source plus compatible exports and their mappings.

## Fabricated 3D

Collect payload/mating dimensions, load use, material, printer volume, nozzle and intended fabrication method when they affect the design. Keep known interfaces protected and units explicit. Mark estimated values instead of silently choosing tolerances. Inspect bounding dimensions, disconnected components, wall thickness, assembly access, watertight/manifold properties as appropriate, and continuity of support. Use a fit coupon for uncertain critical interfaces.

Render the full assembly when requested. Slice the actual delivered geometry before claiming mass, supports, plates or print time. Record slicer version/profile, material and settings behind such claims. Physical fit and strength remain unverified until observed; a successful mesh check or attractive render does not prove them. Cosmetic consistency must not compromise geometry or mounting requirements.

## Shared handoff

Use the smallest useful asset manifest: stable ID, authoritative source path, export path, units where applicable, dependencies, provenance/license, revision, and tested destination. An optional browser showcase is a view of these assets, not their sole editable source. Preserve existing files and keep new experiments separate when the direction is uncertain.
