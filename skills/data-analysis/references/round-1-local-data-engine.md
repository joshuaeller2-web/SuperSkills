# Local data engine

Inspect input format, size, available memory and expected repeated queries. When installed and appropriate, consider DuckDB for SQL-shaped aggregation/joins and Polars for expression pipelines or reshaping. Reuse a resident connection for repeated exploration, or batch questions in a single process. Query in place or stream when loading everything risks memory exhaustion.

For remote data, request only needed rows and columns when authorized access supports it. Record row counts, transformations, elapsed time and correctness checks. Benchmark engines on representative data rather than claiming universal speed. Do not ban pandas, auto-install dependencies or treat a fraction-of-RAM heuristic as a memory-safety guarantee. This method does not create a resident data kernel automatically.

## Provenance

Round 1, code-yeongyu/oh-my-openagent, commit `db06fbe7a796216cc7d0d725401592be98ac134b`.

- https://github.com/code-yeongyu/oh-my-openagent/blob/db06fbe7a796216cc7d0d725401592be98ac134b/packages/shared-skills/skills/data-scientist/SKILL.md

Original scoped synthesis from inspected primary source. Upstream software and runtime dependencies are not installed by this reference. Behavioral effectiveness remains unverified until task trials.
