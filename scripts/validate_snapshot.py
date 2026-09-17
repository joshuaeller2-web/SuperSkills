"""Verify the exported skill file set against manifest.json (Python 3 stdlib)."""
import argparse
import hashlib
import json
from pathlib import Path


def validate(root):
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    entries = manifest["files"]
    expected = {entry["path"] for entry in entries}
    errors = []
    if len(expected) != len(entries):
        errors.append("Duplicate manifest paths")
    actual = {
        path.relative_to(root).as_posix()
        for path in (root / "skills").rglob("*")
        if path.is_file()
    }
    errors.extend("Missing: " + path for path in sorted(expected - actual))
    errors.extend("Unexpected: " + path for path in sorted(actual - expected))
    for entry in entries:
        relative = Path(entry["path"])
        path = (root / relative).resolve()
        if relative.is_absolute() or not path.is_relative_to((root / "skills").resolve()):
            errors.append("Invalid manifest path: " + entry["path"])
            continue
        if not path.is_file():
            continue
        data = path.read_bytes()
        if len(data) != entry["bytes"] or hashlib.sha256(data).hexdigest() != entry["sha256"]:
            errors.append("Content mismatch: " + entry["path"])
    return errors, len(entries)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors, count = validate(args.root.resolve())
    print(json.dumps({"status": "FAIL" if errors else "PASS", "manifest_files": count, "errors": errors}, indent=2))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
