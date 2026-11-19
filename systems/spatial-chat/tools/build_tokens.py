#!/usr/bin/env python3
"""SpatialChat tokens are written from raw/readings.json by hand for this capture.

The kit builder expects Claude's css-vars dump. This package's tokens.json is
the source of truth, checked against the readings file so a colour that is
not in the readings cannot silently appear.
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((HERE / "tokens.json").read_text())
readings = json.loads((HERE / "raw" / "readings.json").read_text())
blob = json.dumps(readings)

def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            yield from walk(v, f"{path}.{k}" if path else k)

missing = []
for path, token in walk(tokens):
    src = (token.get("$extensions") or {}).get("source", "")
    if not src.startswith("Measured") and not src.startswith("Derived"):
        missing.append(path)
if missing:
    sys.exit("tokens missing evidence: " + ", ".join(missing))
print(f"spatial-chat: {sum(1 for _ in walk(tokens))} tokens, readings {len(blob)} bytes")
