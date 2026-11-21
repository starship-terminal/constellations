#!/usr/bin/env python3
"""Check measured & Other Stories tokens against raw/readings.json.

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
    r, g, b = (int(float(p.strip())) for p in parts[:3])
    return f"#{r:02x}{g:02x}{b:02x}"


checks = [
    ("promo", tokens["color"]["promo"]["$value"], readings["promo"]["background"]),
    ("text", tokens["color"]["text"]["$value"], readings["body"]["color"]),
    ("header", tokens["color"]["header"]["$value"], readings["header"]["background"]),
    ("last chance", tokens["color"]["last-chance"]["$value"], readings["lastChance"]["color"]),
    ("footer heading", tokens["color"]["footer-heading"]["$value"], readings["footerHeading"]["color"]),
    ("disabled", tokens["color"]["disabled"]["$value"], readings["product"]["chooseSize"]["background"]),
    ("hero size", tokens["fontSize"]["hero"]["$value"], readings["hero"]["fontSize"]),
    ("control radius", tokens["radius"]["control"]["$value"], readings["shopNow"]["radius"]),
    ("control height", tokens["size"]["control"]["$value"], f"{readings['shopNow']['height']}px"),
]

failed = 0
for name, got, source in checks:
    if str(source).endswith("px"):
        ok = got == source
    else:
        ok = got.lower() == hex_of(source)
    print(("ok" if ok else "FAIL"), name, got, "from", source)
    failed += not ok

if readings["shopNow"]["clicked"] or readings["signUp"]["submitted"] or readings["bag"]["opened"]:
    print("FAIL a stopped control was marked as used")
    failed += 1

sys.exit(1 if failed else 0)
