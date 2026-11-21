#!/usr/bin/env python3
"""Check that tokens.json matches the readings kept in raw/readings.json."""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())
props = readings["customProperties"]

expected = {
    "color.page": props["--background-base"],
    "color.text": props["--text-primary-base"],
    "color.brand": props["--primitive-brand-depop-red"],
    "color.search": props["--surface-primary-weak"],
    "color.border": props["--border-primary-base"],
    "color.divider": props["--border-divider-weak"],
    "font.family": props["--font-aktiv-grotesk"],
    "font.size-body": props["--size-sm"],
    "font.size-display": props["--size-2xl"],
    "radius.pill": props["--radius-fully-rounded"],
    "radius.small": props["--radius-small"],
    "space.16": props["--primitive-spacing-400"],
    "space.24": props["--primitive-spacing-600"],
    "space.32": props["--primitive-spacing-800"],
    "space.48": props["--primitive-spacing-1200"],
}


def walk(node, prefix=""):
    found = {}
    if isinstance(node, dict) and "$value" in node:
        found[prefix] = node["$value"]
        return found
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("$"):
                continue
            nxt = f"{prefix}.{key}" if prefix else key
            found.update(walk(value, nxt))
    return found


flat = walk(tokens["core"])
missing = [path for path, value in expected.items() if flat.get(path) != value]
if missing:
    for path in missing:
        print(f"{path}: token {flat.get(path)!r} != reading {expected[path]!r}")
    sys.exit(1)
print(f"tokens match {len(expected)} readings")
