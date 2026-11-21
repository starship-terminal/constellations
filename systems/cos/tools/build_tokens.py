#!/usr/bin/env python3
"""Check measured COS tokens against raw/readings.json.

Does not recapture the site. Does not write tokens.json.
"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
readings = json.loads((ROOT / "raw" / "readings.json").read_text())
tokens = json.loads((ROOT / "tokens.json").read_text())["core"]


def hex_of(rgb):
    if rgb.startswith("#"):
        return rgb.lower()
    parts = rgb.replace("rgb(", "").replace(")", "").split(",")
    r, g, b = (int(p.strip()) for p in parts[:3])
    return f"#{r:02x}{g:02x}{b:02x}"


checks = [
    ("ink", tokens["color"]["ink"]["$value"], readings["body"]["color"]),
    ("notice", tokens["color"]["notice"]["$value"], readings["notice"]["background"]),
    ("wordmark", tokens["color"]["wordmark"]["$value"], readings["logo"]["fill"]),
    ("footer", tokens["color"]["footer"]["$value"], readings["footer"]["background"]),
    ("add to bag", tokens["color"]["ink"]["$value"], readings["addToBag"]["background"]),
    ("control radius", tokens["radius"]["control"]["$value"], readings["addToBag"]["radius"]),
    ("add to bag height", tokens["size"]["add-to-bag"]["$value"], f"{readings['addToBag']['height']}px"),
    ("notice height", tokens["size"]["notice"]["$value"], f"{readings['notice']['height']}px"),
]

failed = 0
for name, token, raw in checks:
    left = token.lower()
    right = raw if raw.endswith("px") else hex_of(raw)
    if left != right:
        print(f"mismatch {name}: token {left} readings {right}", file=sys.stderr)
        failed += 1
    else:
        print(f"ok {name} {left}")

sys.exit(failed)
