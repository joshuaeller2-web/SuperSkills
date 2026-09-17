# Phaser effects and tweens

Use only for a Phaser project after inspecting its installed version and renderer. The reviewed filter procedure targets Phaser 4 and WebGL; do not transplant its APIs into Phaser 3 or Canvas.

Distinguish local/internal effects from screen-space/external passes. Bound costly passes and test with the actual scene. For animation, separate repetition of an individual tween from loops of a whole chain. Stop or destroy tweens and effect resources with their owning object's lifecycle. Respect reduced-motion needs where relevant. Check the installed API and run scene-level tests; this reference does not install Phaser or establish that Phaser is the user's universal default.

## Provenance

Round 2, phaserjs/phaser, commit `02d8931b626d9764c133cbb3fbf99966c03c757c`.

- https://github.com/phaserjs/phaser/blob/02d8931b626d9764c133cbb3fbf99966c03c757c/skills/filters-and-postfx/SKILL.md
- https://github.com/phaserjs/phaser/blob/02d8931b626d9764c133cbb3fbf99966c03c757c/skills/tweens/SKILL.md

Original scoped synthesis from inspected primary source. Upstream software and runtime dependencies are not installed by this reference. Behavioral effectiveness remains unverified until task trials.
