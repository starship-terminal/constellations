#!/usr/bin/env python3
"""Check systems/fiverr/tokens.json. This capture has no CSS dump to rebuild from.

The homepage painted once and was not measured. The login wall painted once.
A human-check then blocked every later load. tokens.json is the evidence file:
sampled fills are labelled Sampled, and unread roles are the string "Not captured".
Do not invent values here. A future capture that reads CSS should replace this
checker with a builder that reads raw/css-vars.json.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = HERE / "tokens.json"
data = json.loads(TOKENS.read_text())

missing = []


def walk(node, path):
    if not isinstance(node, dict):
        return
    if "$value" in node:
        source = (node.get("$extensions") or {}).get("source", "")
        if not source:
            missing.append(path + " has no $extensions.source")
        if node["$value"] == "Not captured" and "Not captured" not in source:
            missing.append(path + " is Not captured but its source does not say so")
        return
    for key, child in node.items():
        if key.startswith("$"):
            continue
        walk(child, path + key + ".")


walk(data, "")
if "light" not in data:
    missing.append("light set missing")
if missing:
    print("\n".join(missing), file=sys.stderr)
    sys.exit(1)
print("tokens.json sources ok")
