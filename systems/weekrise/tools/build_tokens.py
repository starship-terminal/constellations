#!/usr/bin/env python3
"""Check Weekrise tokens.json against the custom properties read from the live page.

The tokens file was written from those readings. This script does not regenerate
it. It fails if a --vapor-* colour or radius from raw/css-vars.json is missing
from tokens.json, so a later edit cannot drop a measured value quietly. Values are
compared whole after normalising case and short hex, so #000 does not match #000000xx.

    python3 tools/build_tokens.py
"""
from __future__ import annotations

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
TOKENS = json.loads((HERE / "tokens.json").read_text())


def norm(value: str) -> str:
    """Lower-case; a 3- or 4-digit hex is spelt out (#e00 -> #ee0000). Compared whole, never as a substring."""
    v = value.strip().lower()
    if v.startswith("#") and len(v) in (4, 5):
        v = "#" + "".join(c * 2 for c in v[1:])
    return v


def walk(node, found: set[str]) -> None:
    if isinstance(node, dict):
        if "$value" in node and isinstance(node["$value"], str):
            found.add(norm(node["$value"]))
        for child in node.values():
            walk(child, found)
    elif isinstance(node, list):
        for child in node:
            walk(child, found)


def main() -> int:
    found: set[str] = set()
    walk(TOKENS, found)
    missing = []
    for name, value in RAW["properties"].items():
        if not (name.startswith("--vapor-accent-") or name.startswith("--vapor-radius-")
                or name in {
                    "--vapor-primary", "--vapor-primary-text", "--vapor-primary-light",
                    "--vapor-primary-dark", "--vapor-background", "--vapor-foreground",
                    "--vapor-error", "--vapor-error-text", "--vapor-black", "--vapor-white",
                }):
            continue
        needle = norm(value)
        if needle not in found:
            missing.append(f"{name} {value}")
    if missing:
        print("missing measured values:", file=sys.stderr)
        for line in missing:
            print(" ", line, file=sys.stderr)
        return 1
    print(f"weekrise: {len(RAW['properties'])} custom properties, checked colours and radii are in tokens.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
