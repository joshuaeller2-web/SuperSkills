---
name: super-long-task
description: "Keep substantial tasks aligned across steps and sessions, and reduce total token use with targeted context, selective command filtering, externalized output and compact checkpoints. Use for long-running work, context cleanup or token-efficiency requests; skip routine one-step tasks unless context cleanup is requested."
---

# Super Long Task

Maintain the original objective while executing a long task. Passing a self-written plan is not the same as satisfying the user's request.

## Route token use by workload

Use targeted context by default: search for the relevant symbol or path first, read only the sections needed to understand the change, and reread changed files plus final verification evidence. Do not force a repository-wide read to create an artificial baseline.

Add one conditional method only when its trigger is present:

- For a supported command expected to emit substantial repetitive output, use RTK when it is installed and previously approved. Set `RTK_TELEMETRY_DISABLED=1`. Preserve the command, exit status, failures and access to raw evidence. Fall back to the original command when RTK is unavailable or its filtered result is insufficient.
- For substantial output RTK does not cover, save the complete output in the authorized task workspace and return the relevant failures, totals and evidence paths. Do not summarize output already filtered adequately by RTK.
- For repeated searches over large accumulated tool results, use Context Mode only when its MCP integration is available and approved. Small or one-step work does not justify its startup and retrieval overhead.
- At a real phase boundary in a long session, replace superseded working history with one compact checkpoint. Preserve the objective, exact requirements, decisions, failed approaches, evidence, changed artifacts and next action. Adding progress messages without retiring old context is not token optimization.
- For repeated exploration of a large repository, use the bounded repository index below only after targeted search is insufficient. Check revision and changed paths before reuse.

Do not stack brevity personas by default. Caveman, Ponytail and Chisle increased total tokens in the recorded small-task comparison, so they remain opt-in experiments rather than components of this master. Never remove required safety, accessibility, validation, verification or user instructions to save tokens.

Judge optimization by total tokens per accepted task, including retries, retrieval, compression and verification. Keep model, reasoning effort, task inputs and quality checks fixed when comparing methods. Cached-token discounts and cheaper-model routing are cost measurements, not proof of fewer logical tokens. Read [adaptive token optimization](references/adaptive-token-optimization.md) when changing this routing policy or running a benchmark.

## Keep one useful record

Reuse the project's existing task record. If none exists and persistence is needed, create one compact task-local record containing:

- Original objective and links to authoritative specifications or supplied files.
- Required outcomes, exact invariants, exclusions, and user amendments.
- Current work, dependencies, changed artifacts, and verification evidence.
- Unresolved items and the next executable step.

Preserve exact acceptance-critical conditions in the record; do not replace them with weaker summaries. Do not create a hierarchy of ledgers for a task that fits one record.

## Execute with coverage

Split the task at meaningful deliverable boundaries. Map each independently omittable outcome to a check or explicit unresolved item. Keep source requirements distinguishable from inferred implementation choices.

Use observable checks appropriate to the outcome: calculations, source-to-output comparison, integration behavior, rendered inspection, or executable tests. A title saying a requirement is satisfied is not evidence. An absence check needs a known-bad control when a false negative could create a false completion claim.

Work the current unit, verify it, and integrate it with completed units. Continue authorized work without asking for routine permission. Use agents only when authorized and useful; a returned success message still needs the relevant integration evidence.

## Recover from interruptions or drift

After a handoff, context loss, user amendment, unexpected failure, or major milestone, reread the original requirement sources and the current record. Inspect the actual artifacts before trusting an old progress report. Preserve completed work that still meets the request.

If work has drifted, correct the plan and implementation to match the user's intent. Do not weaken acceptance to fit an easier result. If a requirement changes legitimately, record what changed and why, then recheck affected outcomes.

On repeated failure, stop the ineffective tactic, identify the assumption under test, and choose a different evidence-based probe. Persistence does not mean infinite retries, unauthorized actions, or polishing without a finish condition.

## Finish against the original goal

Reconcile each required outcome directly with the delivered artifacts and fresh evidence. Distinguish passed, unverified, blocked, and explicitly abandoned work according to the host's status vocabulary. Abandoned or unmet required work is not successful completion.

Recheck affected evidence after material edits. Once the required outcomes and appropriate checks pass, finish; do not invent more work to remain busy. Report the result briefly and keep detailed evidence in the task record when useful.

Read [sources](references/sources.md) only for provenance or revision.

## Local tools and extended methods

For the matching task, read [local tools and methods](references/local-tools.md). Use only the relevant helper; resolve script paths from this installed skill directory. The guide gives exact input formats, exit meanings and limits. Successful helper output does not establish facts outside its declared checks.

## Consolidated draft methods

For lean-context, read [incorporated draft methods](references/draft-methods.md).

For repository context index, read [repository context index](references/round-1-repository-context-index.md).

For the optional review, handoff or test-first mode, read [legacy methods](references/legacy-review-methods.md).
