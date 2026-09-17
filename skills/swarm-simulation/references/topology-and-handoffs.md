# Topology and handoffs

Choose the smallest architecture that preserves the interaction being tested.

| Shape | Use when | Main failure |
|---|---|---|
| Single agent | One bounded task and few tools | No population interaction |
| Supervisor | Central decomposition and synthesis matter | Bottleneck and lossy paraphrase |
| Pipeline | Stages have strict dependencies | Slowest stage gates the run |
| Hierarchy | Strategy, planning, and execution require distinct authority | Alignment loss between layers |
| Peer swarm | Agents must negotiate, transfer control, or adapt locally | Divergence and hard-to-debug state |

For every edge, name the sender, receiver, trigger, allowed fields, evidence pointer, timeout, retry limit, and failure destination. Pass bounded artifacts rather than complete histories. Preserve an agent's complete result when supervisor paraphrase would lose required detail.

Do not confuse workforce parallelism with population simulation. Parallel coding agents divide work; simulated actors interact inside a modeled environment. Route ordinary work delegation to Company OS or the host's agent tools.

Sources reviewed as data:

- `alirezarezvani/claude-skills`, `engineering/skills/agent-designer/SKILL.md`, commit `19392f7`
- `alirezarezvani/claude-skills`, `engineering/skills/agent-workflow-designer/SKILL.md`, commit `19392f7`
- `sickn33/antigravity-awesome-skills`, `skills/multi-agent-patterns/SKILL.md`, commit `69906dd`
- `tripolskypetr/agent-swarm-kit`, `README.md`, commit `f21a19e`

