#!/usr/bin/env python3
"""Check systems/mymind/tokens.json.

The public site does not publish a token file. tokens.json was written from
computed styles in raw/computed.json, read on 2026-11-19. This script does
not rebuild those values. It refuses a token with no source, an alias that
points at nothing, and a dimension that is not one px length.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
TOKENS = HERE.parent / "tokens.json"
LENGTH = re.compile(r"^-?\d+(\.\d+)?px$")


def walk(node, path, found):
    if isinstance(node, dict) and "$value" in node:
        found.append((path, node))
        return
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            walk(child, f"{path}.{key}" if path else key, found)


def resolve(value, by_path, seen):
    if isinstance(value, dict):
        return {key: resolve(child, by_path, seen) for key, child in value.items()}
    if isinstance(value, list):
        return [resolve(child, by_path, seen) for child in value]
    if not isinstance(value, str) or not (value.startswith("{") and value.endswith("}")):
        return value
    ref = value[1:-1]
    # A Tokens Studio alias is a path inside the set, not a path that already
    # includes the set name. color.page must not match the token core.color.page.
    matches = [path for path in by_path if path == ref or path.endswith("." + ref)]
    matches = [path for path in matches if path.count(".") == ref.count(".") + 1 or path == ref]
    if ref in seen or any(path in seen for path in matches):
        raise ValueError(f"alias cycle at {ref}")
    if not matches:
        raise ValueError(f"alias {value} points at nothing")
    path = matches[0]
    return resolve(by_path[path]["$value"], by_path, seen | {ref, path})


def check(data):
    found = []
    core = []
    for group in ("core", "light"):
        if group not in data:
            raise ValueError(f"missing {group} set")
        walk(data[group], group, found)
        if group == "core":
            walk(data[group], "", core)
    by_path = {path: node for path, node in core}
    problems = []
    for path, node in found:
        source = (node.get("$extensions") or {}).get("source") or {}
        if source.get("evidence") not in ("Measured", "Derived"):
            problems.append(f"{path}: missing evidence")
        if not source.get("capture"):
            problems.append(f"{path}: missing capture")
        value = resolve(node["$value"], by_path, set())
        if node.get("$type") == "dimension" and not LENGTH.match(str(value)):
            problems.append(f"{path}: dimension {value!r} is not one px length")
        if node.get("$type") == "color" and not re.fullmatch(r"#[0-9a-fA-F]{6,8}", str(value)):
            problems.append(f"{path}: colour {value!r} is not hex")
    if problems:
        raise ValueError("\n".join(problems))
    return len(found)


def main():
    data = json.loads(TOKENS.read_text())
    count = check(data)
    print(f"tokens.json: {count} tokens, sources resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
