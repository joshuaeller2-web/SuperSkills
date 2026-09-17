---
name: maker-3d
description: "Design parametric printable parts, review model geometry and plan fit checks using real dimensions and printer constraints. Use for brackets, mounts, holders and enclosures; no physical strength certification."
---

# maker-3d

Establish the part's purpose, mating geometry, critical dimensions, loads, printer, material and manufacturing constraints. Record supplied dimensions and established mounting or mating interfaces as protected requirements before filling gaps. Use supplied measurements and verified specifications; label estimates. Do not silently assume printer size or tolerance.

Reuse an available modeling workflow such as CadQuery or OpenSCAD. Keep dimensions as named parameters, units explicit and orientation deliberate. Preserve requested geometry when reducing material. Check continuous support, connections between parts, wall thickness and assembly access before cosmetic details.

Execute the model when tools are available. Inspect dimensions, bounding box, volume, manifold or watertight status, intersections and disconnected components. A plausible render does not establish printability. Use a fit coupon for critical mating geometry. Test physical assumptions rather than treating source-table clearances or temperatures as universal constants.

Deliver source and requested export files with a print orientation and assembly explanation. Use real slicer results for mass, support and print-time claims. State separately what geometry, slicing and physical testing establish. Update spool records only when requested and from measured weights.

Read [draft provenance and incorporated methods](references/draft-methods.md) when revising these methods.
