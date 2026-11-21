#!/usr/bin/env python3
"""Check that tokens.json still matches raw/readings.json. Does not rewrite tokens."""
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[1]
readings = json.loads((root / "raw" / "readings.json").read_text())
tokens = json.loads((root / "tokens.json").read_text())


def hex_of(rgb):
    parts = rgb.replace("rgb(", "").replace(")", "").split(",")
    return "#{:02x}{:02x}{:02x}".format(*(int(p.strip()) for p in parts))


def reading(role):
    return next(item for item in readings["readings"] if item["role"] == role)


checks = [
    ("ink", tokens["core"]["color"]["ink"]["$value"], "#4d4d4d"),
    ("body", tokens["core"]["color"]["body"]["$value"], hex_of(reading("body")["color"])),
    ("page", tokens["core"]["color"]["page"]["$value"], hex_of(reading("body")["background"])),
    ("promo", tokens["core"]["color"]["promo"]["$value"], hex_of(reading("promo bar")["background"])),
    ("on-promo", tokens["core"]["color"]["on-promo"]["$value"], hex_of(reading("promo bar")["color"])),
    ("muted", tokens["core"]["color"]["muted"]["$value"], hex_of(reading("footer")["color"])),
    ("intro", tokens["core"]["color"]["intro"]["$value"], hex_of(reading("collection intro")["color"])),
    ("price", tokens["core"]["color"]["price"]["$value"], hex_of(reading("card price")["color"])),
    ("accent", tokens["light"]["color"]["accent"]["$value"], "{core.color.promo}"),
    ("button-height", tokens["light"]["component"]["button"]["primary"]["height"]["$value"], "{core.spacing.button}"),
    ("add-to-cart", tokens["core"]["spacing"]["button"]["$value"], reading("add to cart")["height"]),
    ("hero-size", tokens["core"]["typography"]["hero"]["$value"]["fontSize"], reading("hero title")["fontSize"]),
    ("title-size", tokens["core"]["typography"]["title"]["$value"]["fontSize"], reading("product title")["fontSize"]),
    ("nav-size", tokens["core"]["typography"]["nav"]["$value"]["fontSize"], reading("nav link")["fontSize"]),
]

errors = [name for name, got, want in checks if got.lower() != want.lower()]
if errors:
    print("mismatch:", ", ".join(errors))
    sys.exit(1)
print("tokens match readings for color, type size, and button height")
