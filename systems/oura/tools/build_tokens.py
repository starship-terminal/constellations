#!/usr/bin/env python3
"""Check Oura tokens against the live readings. Does not recapture the site."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expect = {
    "core.color.page": ("home.hero.bg", "rgb(247, 241, 232)", "#f7f1e8"),
    "core.color.ink": ("home.h1.color", "rgb(74, 71, 65)", "#4a4741"),
    "core.color.action": ("home.shopSale.bg", "rgb(42, 114, 222)", "#2a72de"),
    "core.color.on-action": ("home.shopSale.color", "rgb(255, 255, 255)", "#ffffff"),
    "core.color.badge": ("extra.badge.bg", "rgb(28, 27, 26)", "#1c1b1a"),
    "core.color.muted": ("extra.footerHeads.0.color", "rgb(168, 165, 160)", "#a8a5a0"),
}


def dig(obj, path):
    cur = obj
    for part in path.split("."):
        cur = cur[int(part)] if part.isdigit() else cur[part]
    return cur


failed = False
for key, (path, rgb, hex_value) in expect.items():
    parts = key.split(".")
    token = tokens
    for part in parts:
        token = token[part]
    got = dig(readings, path)
    if got != rgb or token["$value"] != hex_value:
        print(f"mismatch {key}: reading {got} token {token['$value']}")
        failed = True

if "Editorial New" not in readings["home"]["h1"]["font"]:
    print("mismatch display font", readings["home"]["h1"]["font"])
    failed = True
if "AkkuratLL" not in readings["home"]["body"]["font"]:
    print("mismatch body font", readings["home"]["body"]["font"])
    failed = True
if readings["home"]["shopSale"]["h"] != 48:
    print("mismatch shop sale height", readings["home"]["shopSale"]["h"])
    failed = True
if readings["extra"]["badge"]["radius"] != "8px":
    print("mismatch badge radius", readings["extra"]["badge"]["radius"])
    failed = True

if failed:
    sys.exit(1)
print("oura tokens match raw/readings.json")
