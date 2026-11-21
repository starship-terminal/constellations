#!/usr/bin/env python3
"""Confirm tokens.json colour values match the readings in raw/readings.json."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

def rgb_to_hex(value):
    parts = value.replace("rgb(", "").replace(")", "").split(",")
    nums = [int(p.strip()) for p in parts]
    return "#{:02x}{:02x}{:02x}".format(*nums)

expected = {
    "light.color.page": rgb_to_hex(readings["home"]["body"]["background"]),
    "light.color.ink": rgb_to_hex(readings["home"]["body"]["color"]),
    "light.color.header": rgb_to_hex(readings["home"]["header"]["background"]),
    "light.color.accent": rgb_to_hex(readings["home"]["signUp"]["background"]),
    "light.color.trial": rgb_to_hex(readings["home"]["trialButton"]["background"]),
    "light.color.desktop": rgb_to_hex(readings["home"]["desktopButton"]["background"]),
    "light.color.muted": rgb_to_hex(readings["home"]["otherPlatforms"]["color"]),
    "light.color.auth-button": rgb_to_hex(readings["signin"]["button"]["background"]),
}

found = {
    "light.color.page": tokens["light"]["color"]["page"]["$value"],
    "light.color.ink": tokens["light"]["color"]["ink"]["$value"],
    "light.color.header": tokens["light"]["color"]["header"]["$value"],
    "light.color.accent": tokens["light"]["color"]["accent"]["$value"],
    "light.color.trial": tokens["light"]["color"]["trial"]["$value"],
    "light.color.desktop": tokens["light"]["color"]["desktop"]["$value"],
    "light.color.muted": tokens["light"]["color"]["muted"]["$value"],
    "light.color.auth-button": tokens["light"]["color"]["auth-button"]["$value"],
}

bad = [f"{k}: token {found[k]} readings {expected[k]}" for k in expected if found[k] != expected[k]]
if bad:
    print("\n".join(bad))
    sys.exit(1)
print(f"ok {len(expected)} colours match raw/readings.json")
