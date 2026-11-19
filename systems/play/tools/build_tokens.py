#!/usr/bin/env python3
"""Check systems/play/tokens.json against the readings in raw/.

Play's tokens were written from computed styles on Internet Archive replays,
because createwithplay.com did not resolve on the capture date. This script
does not invent values. It refuses a token whose source string is empty, a
dimension that is not one px length, and a colour that is not hex.

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
    if "light" in data:
        problems.append("light set is present; the captured marketing pages had no light theme")
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print(f"play tokens ok: {count} tokens, dark only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
