from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_LOG = Path(r"F:\Ai Skill Library\Reports\Usage\skill-usage.jsonl")


def main() -> None:
    parser = argparse.ArgumentParser(description="Append a compact skill-usage record.")
    parser.add_argument("--host", required=True)
    parser.add_argument("--task", required=True)
    parser.add_argument("--primary", required=True)
    parser.add_argument("--primary-reason", required=True)
    parser.add_argument("--supporting-json", default="[]")
    parser.add_argument("--controls-json", default="[]", help="Explicitly observed controls only; not proof of automatic activation")
    parser.add_argument("--status", choices=("PASS", "PARTIAL", "BLOCKED", "UNVERIFIED", "WITHHELD"), default="UNVERIFIED")
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG)
    args = parser.parse_args()

    try:
        supporting = json.loads(args.supporting_json)
        controls = json.loads(args.controls_json)
    except json.JSONDecodeError as exc:
        parser.error(f"Invalid JSON argument: {exc.msg}")
    if not isinstance(supporting, list) or any(
        not isinstance(x, dict) or any(not isinstance(x.get(k), str) or not x[k].strip() for k in ('skill', 'reason'))
        for x in supporting
    ):
        parser.error("--supporting-json must be a list of objects with nonempty skill and reason strings")
    allowed_controls = {'adhd-focus', 'intent', 'stack-router', 'lean-context', 'memory-recall'}
    if not isinstance(controls, list) or any(not isinstance(x, str) or x not in allowed_controls for x in controls):
        parser.error("--controls-json must be a list of known control names")
    if any(not value.strip() for value in (args.host, args.task, args.primary, args.primary_reason)):
        parser.error("Host, task, primary and primary reason must not be empty")
    record = {
        "schema_version": 2,
        "usage_evidence": "agent_self_report",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "host": args.host,
        "task": args.task,
        "primary": {"skill": args.primary, "reason": args.primary_reason},
        "supporting": supporting,
        "always_run_controls": list(dict.fromkeys(controls)),
        "status": args.status,
    }
    args.log.parent.mkdir(parents=True, exist_ok=True)
    with args.log.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(json.dumps({"status": "PASS", "log": str(args.log), "primary": args.primary}))


if __name__ == "__main__":
    main()
