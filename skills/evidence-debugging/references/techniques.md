# Choose a probe that reaches the symptom

| Failure | Useful starting loop | What prevents a false pass |
|---|---|---|
| Wrong output | Focused test or CLI with a minimal fixture | Assert the exact output/invariant, then fail it on known-bad behavior |
| API integration | Replay a sanitized request through the real adapter seam | Distinguish provider error, fallback response and actual provider success |
| UI defect | Browser steps plus DOM, console or screenshot evidence | Confirm the server/build and reproduce the user's visible symptom |
| Parser/input space | Hypothesis strategies plus explicit edge examples | Independent expected values, shrunk regressions and mutation controls |
| Intermittent failure | Repeated trigger with controlled clock/state where possible | Record denominator and observed rate before/after; avoid invented confidence |
| Performance | Timing harness or profiler over the original operation | Keep workload and output checks equivalent; report hardware and conditions |
| Several components | Targeted observations at input/output boundaries | Find the first changed value; log presence/types instead of secrets |

Prefer a disposable fixture directory per experiment. A known-bad mutation belongs in an isolated copy, never a live checkout used by another agent. Git bisection, branch changes and history operations must respect the user's explicit authorization. Without it, compare preserved copies or inspect history read-only.

For a hard bug, a short experiment table keeps the investigation recoverable: cause, predicted observation, command, actual observation, status. Do not accumulate logs that do not distinguish causes.
