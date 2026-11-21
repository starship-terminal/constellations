#!/usr/bin/env python3
"""Check girlfriend tokens against the saved readings. Does not recapture the site."""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
readings = json.loads((ROOT / "raw" / "readings.json").read_text())
tokens = json.loads((ROOT / "tokens.json").read_text())
core = tokens["girlfriend"]["core"]

checks = [
    (core["color"]["page"]["$value"], "#ffffff", "page"),
    (core["color"]["ink"]["$value"], "#000000", "ink"),
    (core["color"]["promo"]["$value"], "#0b0b0b", "promo"),
    (core["color"]["button"]["$value"], "#000000", "button"),
    (core["color"]["button-text"]["$value"], "#ffffff", "button text"),
    (core["color"]["wordmark"]["$value"], "#0d0d29", "wordmark"),
    (core["font"]["ui"]["$value"], "Neue Haas Grotesk Text Roman, sans-serif", "ui font"),
    (core["font"]["display"]["$value"], "Canela Thin, sans-serif", "display font"),
    (core["font"]["promo"]["$value"], "Space Mono, monospace", "promo font"),
    (core["size"]["button-height"]["$value"], "41px", "button height"),
    (core["radius"]["button"]["$value"], "30px", "button radius"),
]

failed = False
for got, want, name in checks:
    if got != want:
        print(f"mismatch {name}: {got} != {want}", file=sys.stderr)
        failed = True

if readings["primaryButton"]["background"] != "rgb(0, 0, 0)":
    print("readings primary button background drifted", file=sys.stderr)
    failed = True
if readings["page"]["background"] != "rgb(255, 255, 255)":
    print("readings page background drifted", file=sys.stderr)
    failed = True

if failed:
    sys.exit(1)
print("girlfriend tokens match readings")
