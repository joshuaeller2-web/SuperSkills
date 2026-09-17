# Task briefs and reconciliation

Replace `<skill-dir>` with the absolute directory containing this skill's SKILL.md. Keep the script path quoted; input paths refer to your task workspace. Use an available Python 3.10+ interpreter.

For a plan with numbered ATX headings, `python "<skill-dir>/scripts/task_brief.py" plan.md 2` prints Task 2 through the next heading of equal or higher level. It ignores Markdown fences, rejects missing/duplicate task numbers, and writes only stdout. Preserve output explicitly in the task workspace when a brief is useful; do not overwrite an unrelated file.

Before implementation, connect each acceptance criterion to a user-observable input/action/result and compare it with explicit non-goals. Before completion, map each criterion to the actual artifact and fresh check. A passing test runner can still omit a requirement. A test-discovery error, syntax failure or fixture crash is not evidence that a product assertion failed.

For debugging, trace the observed failure backward through input, state and ownership; test the cheapest distinguishing hypothesis. Replace fixed sleeps with checks for the actual readiness condition where supported. Discover local standards from repeated examples and retain exceptions; do not import every parent framework.

If independent review is authorized, bind its result to the exact reviewed revision. A changed revision invalidates the old review. Tracker writes and Git operations retain the current session's authorization boundary.

Task numbers must identify a single heading across all levels. Use a heading such as Details for a task subsection; repeating Task 1 in a nested heading is treated as an ambiguous duplicate and rejected.
