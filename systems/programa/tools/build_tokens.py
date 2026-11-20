#!/usr/bin/env python3
"""Check systems/programa/tokens.json against the readings in raw/.

Programa's tokens were written from computed styles on the live marketing
site and the signed-out login and register pages. This script does not
invent values or write tokens.json. It refuses a token whose source has no
evidence label, a Measured, Declared or Derived value that no file in raw/
holds (raw_check.py normalises both sides), a dimension that is not one px
length, and a colour that is not hex or rgba(). A value no reading holds is
labelled Reconstruction, entered by hand at capture time.

    python3 tools/build_tokens.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import raw_check

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
    seen = raw_check.reading_forms(HERE / "raw")
    for set_name in ("core", "light", "app"):
        if set_name not in data:
            problems.append(f"missing set {set_name}")
            continue
        for path, token in walk(data[set_name]):
            count += 1
            source = (token.get("$extensions") or {}).get("source") or ""
            if source.startswith("Reconstruction"):
                pass
            elif any(source.startswith(word) for word in ("Measured", "Declared", "Derived")):
                gone = raw_check.missing(token, seen)
                if gone:
                    problems.append(f"{set_name}.{path}: labelled {source.split()[0]} but raw/ holds no reading of {gone}")
            else:
                problems.append(f"{set_name}.{path}: source does not start with Measured, Declared, Derived or Reconstruction")
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
