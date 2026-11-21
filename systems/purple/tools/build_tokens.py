#!/usr/bin/env python3
"""Check measured Purple tokens against raw/readings.json. Does not recapture."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
readings = json.loads((ROOT / "raw" / "readings.json").read_text())
tokens = json.loads((ROOT / "tokens.json").read_text())

expected = {
    "core.color.ink.$value": "#181831",
    "core.color.promo.$value": "#ca2b16",
    "core.color.page.$value": "#f8f5ef",
    "core.color.wordmark.$value": "#1f1a5e",
    "core.radius.pill.$value": "48px",
}


def get(obj, path):
    cur = obj
    for part in path.split("."):
        cur = cur[part]
    return cur


failed = []
for path, want in expected.items():
    got = str(get(tokens, path)).lower()
    if got != want:
        failed.append(f"{path}: {got} != {want}")

ink = readings["colors"]["ink"]
if ink != "rgb(24, 24, 49)":
    failed.append(f"readings ink drifted: {ink}")

if failed:
    raise SystemExit("\n".join(failed))
print("purple tokens match readings")
