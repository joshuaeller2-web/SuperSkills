# SuperSkills

A private snapshot of Josh's reusable AI skill collection for Codex, Claude Code, and Hermes.

Browse the [skill catalog](CATALOG.md). Each package has a `SKILL.md` entry point and any supporting references, scripts, assets, and attribution.

## Contents

- 26 skill packages under `skills/`, including the Super Skills, shared domain workflows, routing controls, Company OS entry points, Archify, Visual System, and watch-youtube.
- `manifest.json` records SHA-256 hashes and sizes for the exported skill files.
- `scripts/validate_snapshot.py` checks file integrity and rejects unexpected files in the skill tree.

This is a versioned snapshot, not a live sync. Editing this repository does not update the installed skills. Existing installed packages were preserved.

## Use a skill

Choose a package from the catalog and read its `SKILL.md`. To install it, copy that entire package directory into your host's configured skill discovery directory. Preserve existing directories and resolve name collisions first. Restart or refresh the host as required by its installed version.

For Josh's current setup, Codex uses `~/.codex/skills` and Claude Code uses `~/.claude/skills`. Hermes uses its configured skill root, which can vary by profile. These locations describe the source setup; discovery in a different installation must be checked there.

For example, copy `skills/super-skill-builder/` into your host's skill directory, then ask: "Use super-skill-builder to audit this skill package."

## Dependencies and limits

The skill files are preserved as exported, including machine-specific paths. These packages are not all standalone:

- `company-os`, `company-agent-runtime`, and Company OS routing refer to the external `F:/AI/Company OS` manuals, roles, and method library. Those resources are not bundled here.
- Some reference documents cite local archive, draft, report, and evidence paths. These are historical provenance or external dependencies, not files promised by this repository.
- `skill-usage-recorder` defaults to a local `F:/Ai Skill Library` log. Its helper accepts `--log` for an explicit alternate destination.
- Skills may require separately installed tools, plugins, accounts, interpreters, or services. A package does not install or authorize those integrations.
- System and plugin-managed skills, host credentials/configuration, usage logs, personal documents, candidate archives, and the full Company OS organization are outside this snapshot.

Packaging checks establish file integrity and basic structure. They do not establish automatic activation or successful execution of every workflow on every host.

## Verify

Run with Python 3:

```console
python scripts/validate_snapshot.py
```

## Attribution

Existing provenance references, licenses, and third-party notices remain with their packages. Archify identifies its upstream repository and includes its MIT license and third-party notices. Local curation does not imply original authorship of every method. No blanket repository license overrides package-specific terms; review those terms before redistribution.
