# Methods and participant records

Replace `<skill-dir>` with the absolute directory containing this skill's SKILL.md. Keep the script path quoted; input paths refer to your task workspace. Use an available Python 3.10+ interpreter.

Select reasoning methods before seeing their conclusions: causal tracing for mechanisms, constraint analysis for feasibility, incentives for behavior, counterexamples for a favored claim, and opportunity cost for prioritization. A domain triad is a useful optional prompt structure, not three independent experts by itself.

`python "<skill-dir>/scripts/collect_views.py" views.json` accepts:

```json
{"seats":[{"id":"risk","status":"completed","source":"actual agent run or supplied report identifier","position":"Try a bounded pilot","strongest_objection":"The pilot may not represent full scale","reversing_evidence":"Measured unit costs exceed the ceiling"},{"id":"operations","status":"failed","reason":"timeout"}]}
```

The helper rejects duplicate IDs and incomplete completed views, preserves failed seats and does not compute votes or consensus. Supplied labels cannot prove independence. All unavailable views give exit 1; invalid input exits 2. It does not start agents or external CLIs.

When actual independent analysis is authorized, gather first views before sharing them. A second round can anonymize arguments; require a specific evidential reason for changed positions. Preserve dissent and name a measurable reversing condition. If only one agent is available, label the output as its perspectives. A failed independent seat stays unavailable.
