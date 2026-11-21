"""Check that tokens.json still matches the public readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())


def rgb_hex(value):
    if value.startswith("#"):
        return value.lower()
    parts = value.replace("rgb(", "").replace(")", "").split(",")
    return "#{:02x}{:02x}{:02x}".format(*(int(p.strip()) for p in parts))


color = tokens["core"]["color"]
assert color["page"]["$value"] == "#ffffff"
assert color["ink"]["$value"] == rgb_hex(readings["tokens"]["primary"])
assert color["ink"]["$value"] == rgb_hex(readings["promoBar"]["color"])
assert color["on-ink"]["$value"] == rgb_hex(readings["tokens"]["onPrimary"])
assert color["hero"]["$value"] == rgb_hex(readings["hero"]["color"])
assert color["wordmark"]["$value"] == readings["tokens"]["wordmark"]
assert color["muted"]["$value"] == rgb_hex(readings["tokens"]["tertiary"])
assert color["field"]["$value"] == rgb_hex(readings["tokens"]["fieldBorder"])
assert color["accent"]["$value"] == rgb_hex(readings["tokens"]["accent"])
assert color["sale"]["$value"] == rgb_hex(readings["product"]["saleColor"])

assert tokens["core"]["fontSize"]["nav"]["$value"] == readings["header"]["navFontSize"]
assert tokens["core"]["fontSize"]["display"]["$value"] == readings["hero"]["fontSize"]
assert tokens["core"]["fontSize"]["collection"]["$value"] == readings["collection"]["titleFontSize"]
assert tokens["core"]["fontSize"]["title"]["$value"] == readings["product"]["titleFontSize"]
assert tokens["core"]["size"]["promo"]["$value"] == readings["promoBar"]["height"]
assert tokens["core"]["size"]["button"]["$value"] == readings["product"]["addToCart"]["height"]
assert tokens["core"]["radius"]["button"]["$value"] == readings["product"]["addToCart"]["borderRadius"]
assert tokens["core"]["radius"]["search"]["$value"] == readings["search"]["borderRadius"]
assert readings["product"]["addToCart"]["clicked"] is False
assert readings["email"]["filled"] is False
assert readings["email"]["submitted"] is False
assert readings["login"]["emailEmpty"] is True
assert readings["login"]["submitted"] is False
assert readings["login"]["screenshotKept"] is False
print("skims tokens match readings")
