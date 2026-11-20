#!/usr/bin/env python3
"""Check systems/play/tokens.json against the readings in raw/.

Play's tokens were written from computed styles on Internet Archive replays,
because createwithplay.com did not resolve on the capture date. Those readings
were not saved to raw/, so every token is labelled Reconstruction. This script
does not invent values. It refuses a token whose source has no evidence label, a
Measured, Declared or Derived value that appears in no file in raw/, a dimension
that is not one px length, and a colour that is not hex.

    python3 tools/build_tokens.py
"""
from __future__ import annotations

import json
import math
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


LABELS = ("Measured", "Declared", "Derived")


def raw_strings() -> set:
    """Every string and number in raw/*.json, lower-cased, with rgb() colours also as hex."""
    acc = set()

    def walk(node):
        if isinstance(node, dict):
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
        else:
            low = str(node).strip().lower()
            acc.add(low)
            for m in re.finditer(r"rgba?\(\s*([\d.]+)[ ,]+([\d.]+)[ ,]+([\d.]+)(?:\s*[,/]\s*([\d.]+))?\s*\)", low):
                r, g, b, a = m.groups()
                h = "#" + "".join(f"{math.floor(float(x) + 0.5):02x}" for x in (r, g, b))
                if a is not None and float(a) < 1:
                    h += f"{math.floor(float(a) * 255 + 0.5):02x}"  # keep the alpha: rgba(255, 255, 255, 0.07) is #ffffff12
                acc.add(h)
            acc.update(m.group(0) for m in re.finditer(r"#[0-9a-f]{3,8}\b|-?[\d.]+px\b", low))

    for path in sorted((HERE / "raw").glob("*.json")):
        walk(json.loads(path.read_text()))
    return acc


def check(data: dict, seen: set) -> tuple[list, int]:
    """(problems, token count) for a token document against the raw readings in `seen`."""
    problems = []
    count = 0
    for path, token in list(walk(data.get("core", {}))) + list(walk(data.get("dark", {}))):
        count += 1
        source = (token.get("$extensions") or {}).get("source") or ""
        if source.startswith("Reconstruction"):
            pass
        elif any(source.startswith(word) for word in LABELS):
            value = token.get("$value")
            parts = [str(v) for v in value.values()] if isinstance(value, dict) else [str(value)]
            missing = [v for v in parts if not v.startswith("{") and v.lower() not in seen]
            if missing:
                problems.append(f"{path}: labelled {source.split()[0]} but raw/ holds no reading of {missing}")
        else:
            problems.append(f"{path}: source does not start with Measured, Declared, Derived or Reconstruction")
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
    return problems, count


def main() -> int:
    problems, count = check(json.loads(TOKENS.read_text()), raw_strings())
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print(f"play tokens ok: {count} tokens, dark only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
