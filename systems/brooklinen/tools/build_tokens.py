"""Check that tokens.json still matches the public readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())


def rgb_hex(value):
    parts = value.replace("rgb(", "").replace(")", "").split(",")
    return "#{:02x}{:02x}{:02x}".format(*(int(p.strip()) for p in parts))


color = tokens["core"]["color"]
assert color["page"]["$value"] == rgb_hex(readings["body"]["backgroundColor"])
assert color["navy"]["$value"] == rgb_hex(readings["nav"]["color"])
assert color["navy"]["$value"] == rgb_hex(readings["addToCart"]["backgroundColor"])
assert color["on-navy"]["$value"] == rgb_hex(readings["addToCart"]["color"])
assert color["maroon"]["$value"] == rgb_hex(readings["mystery"]["backgroundColor"])
assert color["compare"]["$value"] == rgb_hex(readings["product"]["compareColor"])
assert color["nudge"]["$value"] == rgb_hex(readings["nudge"]["backgroundColor"])
assert color["shop"]["$value"] == rgb_hex(readings["login"]["shopButtonBackground"])
assert color["ink"]["$value"] == rgb_hex(readings["login"]["headingColor"])
assert color["wordmark"]["$value"] == "#253455"

assert tokens["core"]["fontSize"]["nav"]["$value"] == readings["nav"]["fontSize"]
assert tokens["core"]["fontSize"]["display"]["$value"] == readings["hero"]["fontSize"]
assert tokens["core"]["fontSize"]["title"]["$value"] == readings["product"]["titleFontSize"]
assert tokens["core"]["size"]["button"]["$value"] == readings["addToCart"]["height"]
assert tokens["core"]["size"]["promo"]["$value"] == readings["promoBar"]["height"]
assert tokens["core"]["radius"]["button"]["$value"] == readings["addToCart"]["borderRadius"]
assert tokens["core"]["radius"]["chip"]["$value"] == readings["sizeChip"]["borderRadius"]
assert readings["addToCart"]["clicked"] is False
assert readings["login"]["emailEmpty"] is True
assert readings["login"]["submitted"] is False
print("brooklinen tokens match readings")
