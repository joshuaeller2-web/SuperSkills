# Optional runtime adapters

No adapter is installed by this skill. Select one only when the requested run needs it and the user has authorized its dependencies, credentials, model calls, and network boundary.

- **MiroFish:** preferred candidate for document-seeded society simulation and multi-round outcome reporting. Follow `mirofish.md`.
- **agent-swarm-kit:** TypeScript option for explicit tool-call handoffs, per-client sessions, agent-scoped tools, and bounded shared chat history. It is an orchestration runtime, not a forecasting validator.
- **LangGraph:** Python option for typed shared state, conditional branches, cycles, checkpointers, and human interruption. Every cycle needs an iteration and timeout exit.
- **Ruflo:** large external orchestration, memory, MCP, and federation system. Treat it as a separate platform evaluation. Do not load or install it merely to run this skill.

When an agent proposes a real action, pass it through deterministic policy and state validation before any approval request. An approval must be explicit, expirable, single-use, and bound to the exact proposal and decision. Simulation output itself never grants execution authority.

Sources reviewed as data:

- `666ghj/MiroFish`, commit `39d8491`
- `tripolskypetr/agent-swarm-kit`, `README.md`, commit `f21a19e`
- `davila7/claude-code-templates`, LangGraph skill, commit `41afe2d`
- `ruvnet/ruflo`, `README.md`, commit `2602b64`
- `NVIDIA-AI-Blueprints/Multi-Agent-Intelligent-Warehouse`, `README.md`, commit `a371b4c`
