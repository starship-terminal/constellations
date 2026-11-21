#!/usr/bin/env python3
"""Check Dermstore tokens against the live readings. Does not recapture the site."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expect = {
    "core.color.ink": readings["body"]["color"],
    "core.color.page": readings["body"]["backgroundColor"],
    "core.color.promo": readings["promo"]["backgroundColor"],
    "core.color.ink-soft": readings["promo"]["color"],
    "core.color.nav": readings["nav"]["backgroundColor"],
    "core.color.on-ink": readings["nav"]["color"],
    "core.color.trust": readings["trust"]["backgroundColor"],
    "core.color.search-border": readings["search"]["wrapBorder"],
    "core.color.bag": readings["product"]["bag"]["backgroundColor"],
    "core.color.muted": readings["product"]["brandColor"],
    "core.color.title": readings["product"]["titleColor"],
}

want_hex = {
    "core.color.ink": "#121212",
    "core.color.page": "#ffffff",
    "core.color.promo": "#cccccc",
    "core.color.ink-soft": "#000000",
    "core.color.nav": "#222222",
    "core.color.on-ink": "#ffffff",
    "core.color.trust": "#f2f2f2",
    "core.color.search-border": "#8c8c8c",
    "core.color.bag": "#000000",
    "core.color.muted": "#6b7280",
    "core.color.title": "#111827",
}

hexes = {key: tokens["core"]["color"][key.split(".")[-1]]["$value"] for key in want_hex}

failed = False
for key, rgb in expect.items():
    if hexes[key] != want_hex[key]:
        print(f"mismatch {key}: reading {rgb} token {hexes[key]}")
        failed = True

if "Manrope" not in readings["body"]["fontFamily"]:
    print("mismatch font", readings["body"]["fontFamily"])
    failed = True
if "Manrope" not in tokens["core"]["font"]["body"]["$value"]:
    print("mismatch token font")
    failed = True
if "Libre Bodoni" not in tokens["core"]["font"]["display"]["$value"]:
    print("mismatch display font")
    failed = True
if readings["product"]["bag"]["borderRadius"] != "0px":
    print("mismatch bag radius", readings["product"]["bag"]["borderRadius"])
    failed = True
if tokens["core"]["radius"]["none"]["$value"] != "0px":
    print("mismatch radius token")
    failed = True
if readings["search"]["borderRadius"] != "0px":
    print("mismatch search radius")
    failed = True
if tokens["core"]["color"]["hero"]["$value"] != readings["hero"]["sampled"]:
    print("mismatch hero sample")
    failed = True

if failed:
    sys.exit(1)
print("dermstore tokens match raw/readings.json")
