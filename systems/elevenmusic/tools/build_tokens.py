#!/usr/bin/env python3
"""ElevenMusic tokens are written from raw/readings.json by the capture, not regenerated here.

The readings are CSS lab() values. tokens.json already holds the sRGB conversion and the
source string for each token. This script checks that every token has a source.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((HERE / "tokens.json").read_text())
missing = []

def walk(node, path):
    if not isinstance(node, dict):
        return
    if "$value" in node:
        if not (node.get("$extensions") or {}).get("source"):
            missing.append(path)
        return
    for key, child in node.items():
        if key.startswith("$"):
            continue
        walk(child, f"{path}.{key}" if path else key)

walk(tokens, "")
if missing:
    print("tokens missing a source:", ", ".join(missing))
    sys.exit(1)
print("elevenmusic tokens: every value has a source")
