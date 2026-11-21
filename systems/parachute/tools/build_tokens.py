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
assert color["ink"]["$value"] == rgb_hex(readings["body"]["color"])
assert color["ink"]["$value"] == rgb_hex(readings["addToBag"]["backgroundColor"])
assert color["on-ink"]["$value"] == rgb_hex(readings["addToBag"]["color"])
assert color["cream"]["$value"] == rgb_hex(readings["footer"]["backgroundColor"])
assert color["cream"]["$value"] == rgb_hex(readings["shopTheSale"]["backgroundColor"])
assert color["muted"]["$value"] == rgb_hex(readings["tokens"]["muted"])
assert color["accent"]["$value"] == rgb_hex(readings["tokens"]["accent"])
assert color["promo"]["$value"] == rgb_hex(readings["promoBar"]["backgroundColor"])
assert color["wordmark"]["$value"] == readings["tokens"]["wordmark"]

assert tokens["core"]["fontSize"]["nav"]["$value"] == readings["header"]["navFontSize"]
assert tokens["core"]["fontSize"]["display"]["$value"] == readings["hero"]["fontSize"]
assert tokens["core"]["fontSize"]["title"]["$value"] == readings["product"]["titleFontSize"]
assert tokens["core"]["size"]["button"]["$value"] == readings["addToBag"]["height"]
assert tokens["core"]["size"]["promo"]["$value"] == readings["promoBar"]["height"]
assert tokens["core"]["radius"]["button"]["$value"] == readings["addToBag"]["borderRadius"]
assert tokens["core"]["radius"]["sale"]["$value"] == readings["shopTheSale"]["borderRadius"]
assert readings["addToBag"]["clicked"] is False
assert readings["login"]["emailEmpty"] is True
assert readings["login"]["submitted"] is False
assert readings["login"]["screenshotKept"] is False
print("parachute tokens match readings")
