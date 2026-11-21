#!/usr/bin/env python3
"""Cofounder tokens are written from the capture readings, not generated.

The marketing site publishes no named colour scale. tokens.json was filled
from computed styles in raw/components-computed.json and declared Tailwind
variables in raw/css-vars.json. This script checks that those source files
still exist and that every token has $extensions.source. It does not rewrite
tokens.json, because a second mapping would invent values the site does not
declare.

Run from the package: python3 tools/build_tokens.py
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
TOKENS = HERE / "tokens.json"


def walk(node, path=""):
    if not isinstance(node, dict):
        return
    if "$value" in node:
        src = (node.get("$extensions") or {}).get("source")
        if not src:
            raise SystemExit(f"missing source: {path}")
        return
    for k, v in node.items():
        if k.startswith("$"):
            continue
        walk(v, f"{path}.{k}" if path else k)


def main():
    missing = [name for name in ("components-computed.json", "css-vars.json") if not (RAW / name).exists()]
    if missing:
        raise SystemExit("missing readings: " + ", ".join(missing))
    data = json.loads(TOKENS.read_text())
    walk(data)
    print("tokens.json sources present; readings present; not rewritten")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
