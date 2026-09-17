# Adaptive token optimization

## Current routing decision

Targeted context is the default method. RTK, external output storage, Context Mode, checkpoints and repository indexing are conditional additions. Use the smallest combination whose trigger is observable. Avoid double compression and overlapping brevity personas.

| Trigger | Method | Required evidence |
|---|---|---|
| Relevant code or evidence is not yet located | Search first, then bounded reads | Paths and sections actually used |
| Supported command will produce repetitive output | RTK | Actual wrapped command, exit status, retained failure evidence |
| Large unsupported command or tool output | Externalize complete output, return a compact evidence summary | Artifact path, byte size, exit status and decisive excerpts |
| Repeated retrieval over accumulated tool output | Context Mode | Successful MCP calls and access to required raw details |
| Long session crosses a meaningful phase boundary | Replacement checkpoint | Old working history is superseded; exact requirements and evidence remain |
| Repeated exploration of a large stable repository | Revision-bound repository index | Revision, changed-path check and index scope |

## Measured evidence

The September 14, 2026 small-task comparison ran five matched tasks per condition. RTK was the only active individual condition with a lower mean, 2.91%. Context Mode, Caveman, Ponytail, Chisle, targeted-context instructions, local summarization, patch-only and repository-map instructions did not reduce the mean in that workload. Checkpoints were not exercised. Source artifacts: `F:\AI Sandbox\Candidates\Article-video-token-tests\REPORT.md` and `independent-review\FINAL-REVIEW.md`.

A later five-task pilot combined RTK with targeted context. The full result showed 20.76% fewer normalized tokens, but one combination run also loaded evidence-debugging. Excluding that matched task from every arm left four tasks and 17.03% fewer tokens. This is exploratory evidence from small fixes in synthetic repositories, not a general guarantee. Source artifacts: `F:\AI Sandbox\Candidates\Combined-token-test\REPORT.md`, `sensitivity.json` and `independent-review\FINAL-REVIEW.md`.

Claude's repository-exploration pilot found targeted context 12.8% below its baseline. RTK was 35.8% above baseline, but that RTK run also loaded evidence-debugging and emitted large repeated hash listings, so it does not isolate RTK. The checkpoint condition emitted five progress messages without showing replacement of old context. Source artifacts: `F:\AI Sandbox\Candidates\Token-scaled-pilot-1\METHOD.md`, `final-summary.json`, raw event logs and `independent-review\REVIEW.md`.

These results establish workload dependence and support conditional routing. They do not establish a 50% reduction, general intelligence improvement or production-scale effectiveness.

## Evaluation contract

Use matched tasks and retain unsuccessful runs. Keep the baseline free to work efficiently. Hold the model, reasoning effort, available tools, inputs and quality checks fixed. Confirm known-bad inputs fail before accepting positive checks. Verify actual tool or skill activation from traces. Report provider input and output once; cached input is a subset when the provider reports it that way. Report normalized results only with the actual totals and formula.

Test a combination against baseline, each component alone and the combination. A component belongs in the default route only when it improves accepted-task usage on representative workloads without weakening quality. Mark a conditional method `NOT EXERCISED` when its trigger does not occur.

## Sources

- DataCamp, "How to Reduce Token Usage in AI Coding Agents": differentiation among Caveman, Ponytail, RTK and Context Mode.
- WeAreDevelopers, "6 Open-Source Tools to Reduce Your Token Usage": repository maps, filtered command output and deferred tool descriptions.
- MindStudio, "Token Reduction Strategies for AI Agents": external state, retrieval, rolling summaries and structured output.
- Pluralsight, "11 ways to cut token usage in AI-assisted development": targeted reads, requirements, patches and local processing.
- YouTube `xXS83RALMtc`: startup-context audit, batching, concise communication and code maps; transcript-only review.
- YouTube `Ua0APTMVcb8`: Chisle and Caliper descriptions; transcript-only review.
- The Prompt Index, "AI Loop Engineering & Gauntlet Loops": inspect real artifacts, use independent review and explicit stopping limits.

Article and video performance claims are source claims, not local benchmark results. No source installer or additional runtime is authorized by this reference.
