# Optional review and test-first modes

For a requested review, assess both specification compliance and implementation quality. A stylistically clean patch can still miss its requirement; a behaviorally complete patch can still introduce a security or maintenance defect. Record the axes separately and prioritize actual impact with source or test evidence.

For review feedback, record an accept, reject or unverified disposition with code/test evidence. Verify the claim against the current revision before fixing it. Do not automatically publish the response.

For requested TDD, choose an observable public seam and an independent expected result. Reproduce a meaningful failing behavior, check that it fails for the intended reason, implement the smallest appropriate change, then refactor while retaining the regression check. Do not delete existing working code or force TDD onto every change merely because this optional method exists.

A reviewer handoff names authoritative requirements, exact diff/revision scope, changed behavior, test commands and unresolved risks. The reviewer should not treat an implementer's success claim as evidence.

## Preserved source provenance

- `F:\Ai Skill Library\Quarantine\Claude-consolidated\executing-plans\SKILL.md`
- `F:\Ai Skill Library\Quarantine\Claude-consolidated\requesting-code-review\SKILL.md`
- `F:\Ai Skill Library\Quarantine\Claude-consolidated\receiving-code-review\SKILL.md`
- `F:\Ai Skill Library\Quarantine\Claude-consolidated\code-review\SKILL.md`
- `F:\Ai Skill Library\Quarantine\Claude-consolidated\tdd\SKILL.md`
- `F:\Ai Skill Library\Quarantine\Claude-consolidated\test-driven-development\SKILL.md`

Original scoped synthesis; behavioral equivalence not established.
