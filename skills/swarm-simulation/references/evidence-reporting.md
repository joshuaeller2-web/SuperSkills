# Evidence and reporting

Report each run as a reproducible observation with its configuration. Compare runs only when the intended control variables match.

Use this result structure:

- **Question:** the decision the simulation informs.
- **Source facts:** claims directly supported by the seed material.
- **Added assumptions:** rules or values needed to complete the world.
- **Configuration:** model, revision, population, rounds, seeds, intervention, and stopping rule.
- **Distribution:** counts or ranges across replications, including failures.
- **Mechanisms:** event chains observed in logs, with run and round identifiers.
- **Sensitivity:** which conclusions change when assumptions or seeds change.
- **Limits:** missing actors, invalid abstractions, calibration gaps, and tool failures.
- **Decision use:** what the simulation suggests testing in reality.

Do not hide failed or incomplete runs. A surprising story from one run is a hypothesis generator, not a supported forecast.
