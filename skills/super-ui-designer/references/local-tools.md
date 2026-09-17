# Contrast and design records

Replace `<skill-dir>` with the absolute directory containing this skill's SKILL.md. Keep the script path quoted; input paths refer to your task workspace. Use an available Python 3.10+ interpreter.

Use `python "<skill-dir>/scripts/contrast.py" input.json` for opaque sRGB colors. Input:

```json
{"colors":{"ink":"#000000","paper":"#FFFFFF","accent":"#888888"},"pairs":[{"fg":"ink","bg":"paper","use":"text"},{"fg":"accent","bg":"paper","use":"text"}]}
```

`text` requires 4.5:1; `large_text` and `ui` require 3:1. The caller must establish which use applies. Do not label ordinary hyperlinks as non-text UI. Compare unrounded ratios. Exit 1 reports a failed specified pair; 2 is invalid input. Omitting `pairs` returns every color combination as a report, with conformance UNVERIFIED; matrix exit 0 never means accessibility passed. Alpha, gradients, photos and computed browser styles need rendered/computed evidence. Verify the applicable current criterion before asserting conformance.

Record only useful project decisions: existing token names, color roles and allowed pairings, type/spacing scales, content-to-layout choice and source references. For component work, preview relevant default/focus/disabled/loading/error states without forcing irrelevant states. For page work, choose structure from the content and task. Audit, refine, reference study and rebuild remain distinct modes. The helper does not install a design database or render a page.
