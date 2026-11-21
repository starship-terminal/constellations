#!/usr/bin/env python3
"""Check that tokens.json still matches the homepage readings in raw/."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
raw = json.loads((ROOT / "raw" / "homepage-computed.json").read_text())
readings = raw["readings"]

expect = {
    "core.color.promo": readings["primaryButton"]["backgroundColor"],
    "core.color.cream": readings["mainBar"]["backgroundColor"],
    "core.color.charcoal": readings["utilityBar"]["backgroundColor"],
    "core.color.paper": readings["body"]["backgroundColor"],
    "core.radius.control": readings["primaryButton"]["borderRadius"],
}

def rgb_to_hex(value):
    nums = value[value.find("(") + 1:value.find(")")].split(",")
    return "#{:02x}{:02x}{:02x}".format(*(int(n.strip()) for n in nums[:3]))

def as_hex(value):
    return rgb_to_hex(value) if value.startswith("rgb") else value

got = {
    "core.color.promo": as_hex(tokens["core"]["color"]["promo"]["$value"]),
    "core.color.cream": as_hex(tokens["core"]["color"]["cream"]["$value"]),
    "core.color.charcoal": as_hex(tokens["core"]["color"]["charcoal"]["$value"]),
    "core.color.paper": as_hex(tokens["core"]["color"]["paper"]["$value"]),
    "core.radius.control": tokens["core"]["radius"]["control"]["$value"],
}
want = {k: rgb_to_hex(v) if v.startswith("rgb") else v for k, v in expect.items()}
bad = [k for k in want if got[k].lower() != want[k].lower()]
if bad:
    print("mismatch", {k: (got[k], want[k]) for k in bad})
    sys.exit(1)
print("tokens match homepage readings")
