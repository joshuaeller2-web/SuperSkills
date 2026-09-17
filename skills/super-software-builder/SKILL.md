---
name: super-software-builder
description: "Build and verify software applications or games, including browser games, Canvas, Phaser, platformers, sprites and game loops. Use for substantive software delivery and game development with requirements and integrated checks; a planning-only request remains planning-only."
---

# Super Software Builder

Turn the user's requirements into working software with a traceable definition of done. Adapt the process to the size of the change.

## Establish the contract

Read the request, applicable repository instructions, existing implementation, and relevant tests. Confirm the working directory, repository, branch, and changed files before editing. Preserve concurrent changes; isolate conflicting edits only through actions allowed in the current session.

For a bounded change, keep the plan brief. For a new subsystem, capture the intended behavior, interfaces, constraints, and acceptance examples in the project's existing planning location. Reuse its conventions instead of installing a new project-management system.

Describe acceptance through an observable scenario: starting condition, user action or input, expected result. Include the meaningful failure case. Distinguish requested outcomes from implementation ideas and explicit non-goals.

Resolve routine reversible details from context. Ask when missing information would materially change the product or an authorization boundary. Existing authorization is sufficient for the work it covers; do not add an approval gate for every step.

## Build in useful units

1. Follow the codebase's patterns for interfaces, error handling, data ownership, and testing. Treat examples as evidence of conventions, not automatically universal rules.
2. Order units by dependency and deliver usable vertical slices. Keep each change connected to its acceptance criteria.
3. Fix relevant review findings before extending the same work. Verify the feedback still applies to the current files.
4. Implement actual behavior, including integration and error paths. Do not substitute disconnected UI, constant-returning stubs, or fixtures for a required live integration.
5. Use independent agents only when authorized, available, and useful. Give each a bounded deliverable and clear file ownership; reconcile their integration yourself. Sequential execution is a complete supported mode.

## Verify and reconcile

For a bug, reproduce the failure before fixing it when feasible. For new logic, test meaningful behavior and boundaries. Run the repository's required checks and the affected end-to-end path. Tests should be capable of rejecting an incorrect implementation.

If checks fail, use their evidence to identify the cause rather than repeatedly broadening the patch. Retest after a relevant fix. Do not keep rerunning unchanged successful checks without a reason.

Compare the actual delivered behavior with the original request, not only the derived plan. Capture unresolved failures or unavailable integrations honestly. A passing build alone does not prove the feature works.

Close with the result, relevant verification, and any material remaining limitation. Commit, push, merge, deploy, or change external tracker state only within current authorization; the skill does not grant those permissions.

## Subagent integration pitfalls

After delegating to subagents, always inspect their source files (read_file) for actual class names, method signatures, and attribute names **before** writing integration tests. Subagents rarely export exact names the caller expects — mismatches in `get_bet()`, `calculate()`, `payout()`, and `__init__` parameters are common. Write the integration test against the real API, not the assumed one.

When subagents build numeric modules (bet sizing, payouts, probability), verify three things on first run:

- **Return value semantics**: Does a method return net profit (winnings only) or total returned (stake + winnings)? Using the wrong semantics on a double-subtraction path (`net = payout - stake` when payout already includes stake) drains the bankroll.
- **Argument order**: Functions with multiple positional parameters (e.g., `payout(side, amount)` vs `payout(amount, side)`) silently swap meaning. Call with named arguments or verify the first call's output against expected values.
- **Shared state contamination**: When running multiple independent simulations in one process, shared mutable objects (statistics engines, random seeds) corrupt results. Spin each simulation in a fresh subprocess or pass a brand-new instance to each.

For betting systems using Kelly criterion: full Kelly on negative-expectation games (e.g., Baccarat ~1.06% house edge) causes rapid ruin from volatility. Use fractional Kelly (0.25x–0.5x) for negative-EV games; full Kelly is suitable only for positive-EV games (e.g., poker against weaker opponents).

For work spanning sessions, retain the contract, evidence, and next step in an existing task record. Do not impose multiple ledgers on a small change.

Read [sources](references/sources.md) only for provenance or a revision of this workflow.

## Local tools and extended methods

For the matching task, read [local tools and methods](references/local-tools.md). Use only the relevant helper; resolve script paths from this installed skill directory. The guide gives exact input formats, exit meanings and limits. Successful helper output does not establish facts outside its declared checks.

## Reviewed optional method

When building SQL execution paths or production error handling, Read [sql-and-error-boundaries](references/sql-and-error-boundaries.md).

## Consolidated draft methods

For build-loop, read [incorporated draft methods](references/draft-methods.md).

For phaser effects and tweens, read [phaser effects and tweens](references/round-2-phaser-effects-and-tweens.md).

For game development, including requests to make a game, platformer, sprite system or game loop, read [game-dev: game development](references/game-dev.md). This is an optional minor inside this skill, not a separate always-running agent.

For compact specification, read [compact specification](references/round-2-compact-specification.md).

For observed api client, read [observed api client](references/round-2-observed-api-client.md).

For contextual code review, read [contextual code review](references/round-1-contextual-code-review.md).

For the optional review, handoff or test-first mode, read [legacy methods](references/legacy-review-methods.md).
