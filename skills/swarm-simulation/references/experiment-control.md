# Experiment control

Before a run, record the question, baseline, number of agents, number of rounds, evaluation criteria, metric direction, seed digest, random seed, model, topology, cost ceiling, time ceiling, and stop conditions. A baseline failure does not become a successful experiment because later agents agree.

Use a fixed maximum round count and an explicit completion condition. Detect repeated state, stalled progress, excessive disagreement, budget exhaustion, and tool failure. Stop and report the condition instead of extending the run silently.

Keep agent-local instructions and tools isolated. Share only the state necessary for interaction. Record transfers of control and preserve the originating agent's evidence reference. Run a small pilot before increasing population or round count.

Sources reviewed as data:

- `alirezarezvani/claude-skills`, `engineering/agenthub/skills/hub-init/SKILL.md`, commit `19392f7`
- `affaan-m/everything-claude-code`, `skills/autonomous-loops/SKILL.md`, commit `8321021`
- `davila7/claude-code-templates`, `cli-tool/components/skills/ai-research/langgraph/SKILL.md`, commit `41afe2d`

