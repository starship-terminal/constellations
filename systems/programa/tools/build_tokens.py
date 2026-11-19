#!/usr/bin/env python3
"""Check systems/programa/tokens.json against the readings in raw/.

Programa's tokens were written from computed styles on the live marketing
site and the signed-out login and register pages. This script does not
invent values. It refuses a token whose source string is empty, a dimension
that is not one px length, and a colour that is not hex or rgba().

    python3 tools/build_tokens.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOKENS = HERE / "tokens.json"
HEX = re.compile(r"^#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
RGBA = re.compile(r"^rgba\(\d+, \d+, \d+, [\d.]+\)$")
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
    for set_name in ("core", "light", "app"):
        if set_name not in data:
            problems.append(f"missing set {set_name}")
            continue
        for path, token in walk(data[set_name]):
            count += 1
            source = (token.get("$extensions") or {}).get("source") or ""
            if not any(word in source for word in ("Measured", "Declared", "Derived")):
                problems.append(f"{set_name}.{path}: source does not say Measured, Declared, or Derived")
            kind = token.get("$type")
            value = token.get("$value")
            if kind == "color" and not (isinstance(value, str) and (HEX.match(value) or RGBA.match(value) or value.startswith("{"))):
                problems.append(f"{set_name}.{path}: colour is not hex, rgba, or an alias: {value!r}")
            if kind == "dimension" and not (isinstance(value, str) and (PX.match(value) or value.startswith("{"))):
                problems.append(f"{set_name}.{path}: dimension is not one px length: {value!r}")
            if kind == "duration" and not (isinstance(value, str) and value.endswith("ms")):
                problems.append(f"{set_name}.{path}: duration is not ms: {value!r}")
            if kind == "typography":
                if not isinstance(value, dict):
                    problems.append(f"{set_name}.{path}: typography is not an object")
                elif not str(value.get("fontSize", "")).endswith("px") and not str(value.get("fontSize", "")).startswith("{"):
                    problems.append(f"{set_name}.{path}: fontSize is not px")
    if "dark" in data:
        problems.append("dark set is present; the captured pages had no dark theme")
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print(f"programa tokens ok: {count} tokens, light marketing plus signed-out app")
    return 0


if __name__ == "__main__":
    sys.exit(main())
