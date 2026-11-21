#!/usr/bin/env python3
"""Check measured Banana Republic tokens against raw/readings.json.

Does not recapture the site. Does not write tokens.json.
"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
readings = json.loads((ROOT / "raw" / "readings.json").read_text())
tokens = json.loads((ROOT / "tokens.json").read_text())

checks = [
    (tokens["color"]["universal"]["$value"], "#e9e8e3", "universal bar"),
    (tokens["color"]["promo"]["$value"], "#000000", "promo bar"),
    (tokens["color"]["wordmark"]["$value"], "#ad280a", "wordmark"),
    (tokens["color"]["footer"]["$value"], "#f2f1ee", "footer"),
    (tokens["color"]["add-to-bag"]["$value"], "#000000", "add to bag"),
    (tokens["radius"]["control"]["$value"], "0px", "control radius"),
    (tokens["size"]["add-to-bag"]["$value"], "56px", "add to bag height"),
]

expected = {
    "universal bar": readings["universalBar"]["background"],
    "promo bar": readings["promoBar"]["background"],
    "wordmark": readings["wordmark"]["fill"],
    "footer": readings["footer"]["background"],
    "add to bag": readings["addToBag"]["background"],
    "control radius": readings["addToBag"]["radius"],
    "add to bag height": f"{readings['addToBag']['height']}px",
}


def hex_of(rgb):
    if rgb.startswith("#"):
        return rgb.lower()
    parts = rgb.replace("rgb(", "").replace(")", "").split(",")
    r, g, b = (int(p.strip()) for p in parts[:3])
    return f"#{r:02x}{g:02x}{b:02x}"


failed = 0
for got, want, name in checks:
    source = expected[name]
    if source.endswith("px"):
        ok = got == source
    else:
        ok = got.lower() == hex_of(source)
    print(("ok" if ok else "FAIL"), name, got, "from", source)
    failed += not ok

if readings["addToBag"]["clicked"] or readings["signUp"]["submitted"]:
    print("FAIL a stopped control was marked as submitted")
    failed += 1

sys.exit(1 if failed else 0)
