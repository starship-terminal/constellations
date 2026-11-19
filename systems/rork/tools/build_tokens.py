#!/usr/bin/env python3
"""Check systems/rork/tokens.json against the readings in raw/.

Values were read with getComputedStyle on https://rork.com/ on 2026-11-19.
This script does not invent values. It refuses a token whose source string is
empty, a dimension that is not one px length, and a colour that is not hex.

    python3 tools/build_tokens.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOKENS = HERE / "tokens.json"
HEX = re.compile(r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
PX = re.compile(r"^-?\d+(\.\d+)?px$")
MS = re.compile(r"^\d+ms$")


def walk(node, path=""):
    if not isinstance(node, dict):
        return
    if "$value" in node:
        yield path, node
        return
    for key, child in node.items():
        if key.startswith("$"):
            continue
        yield from walk(child, f"{path}.{key}" if path else key)


def main() -> int:
    data = json.loads(TOKENS.read_text())
    problems = []
    count = 0
    for path, token in list(walk(data.get("core", {}))) + list(walk(data.get("dark", {}))):
        count += 1
        source = (token.get("$extensions") or {}).get("source", "")
        if not source.startswith("Measured"):
            problems.append(f"{path}: source does not start with Measured")
        kind = token.get("$type")
        value = token.get("$value")
        if kind == "color" and not (isinstance(value, str) and HEX.match(value)):
            problems.append(f"{path}: colour {value!r} is not hex")
        if kind == "dimension" and not (isinstance(value, str) and PX.match(value)):
            problems.append(f"{path}: dimension {value!r} is not one px length")
        if kind == "duration" and not (isinstance(value, str) and MS.match(value)):
            problems.append(f"{path}: duration {value!r} is not ms")
        if kind == "fontFamily" and not (isinstance(value, list) and value):
            problems.append(f"{path}: font family is empty")
    page = data["dark"]["surface"]["page"]["$value"]
    text = data["dark"]["text"]["primary"]["$value"]
    if page != "#171717":
        problems.append(f"page colour drifted from the body reading: {page}")
    if text != "#ffffff":
        problems.append(f"text colour drifted from the body reading: {text}")
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print(f"ok {count} tokens")
    return 0


if __name__ == "__main__":
    sys.exit(main())
