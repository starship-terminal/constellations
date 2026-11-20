#!/usr/bin/env python3
"""Check systems/contra/tokens.json against the readings in raw/.

Contra's tokens were written from computed styles on public signed-out pages.
This script does not invent values. It refuses a token whose source string is
empty, a dimension that is not one px length, and a colour that is not hex.

    python3 tools/check_tokens.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOKENS = HERE / "tokens.json"
HEX = re.compile(r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
PX = re.compile(r"^-?\d+(\.\d+)?px$")


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
    for path, token in list(walk(data.get("core", {}))) + list(walk(data.get("light", {}))):
        count += 1
        source = (token.get("$extensions") or {}).get("source") or ""
        if not any(word in source for word in ("Measured", "Declared", "Derived")):
            problems.append(f"{path}: source does not say Measured, Declared, or Derived")
        kind = token.get("$type")
        value = token.get("$value")
        if kind == "color" and not (isinstance(value, str) and HEX.match(value)):
            problems.append(f"{path}: colour is not hex: {value!r}")
        if kind == "dimension" and not (isinstance(value, str) and PX.match(value)):
            problems.append(f"{path}: dimension is not one px length: {value!r}")
        if kind == "typography":
            if not isinstance(value, dict):
                problems.append(f"{path}: typography is not an object")
            elif not str(value.get("fontSize", "")).endswith("px"):
                problems.append(f"{path}: fontSize is not px")
    if "dark" in data:
        problems.append("dark set is present; the live marketing pages stayed light under prefers-color-scheme: dark")
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print(f"contra tokens ok: {count} tokens, light only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
