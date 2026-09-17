# MiroFish boundary

Source reviewed: `666ghj/MiroFish` at commit `39d849138ef254f6c737ab4c4705e5545dbe31d4`.

The reviewed repository describes this pipeline:

1. Extract seed information and build a graph with individual and collective memory.
2. Extract entities and relationships, generate personas, and configure agents.
3. Run parallel social simulations with temporal memory updates.
4. Generate a report from the post-simulation environment.
5. Allow follow-up interaction with agents and the report agent.

The repository requires an OpenAI-compatible LLM API and Zep Cloud. Its README warns that consumption is high and recommends fewer than 40 rounds for initial trials. The code defaults to 10 rounds when not overridden. MiroFish uses OASIS for social simulation and is AGPL-3.0 licensed.

Do not claim this skill installs or replaces MiroFish. An actual MiroFish run requires separate dependency, credential, privacy, license, and cost review. Do not upload seed documents or call Zep Cloud without explicit authorization.
