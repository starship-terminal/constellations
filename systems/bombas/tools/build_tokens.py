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
assert color["page"]["$value"] == rgb_hex(readings["header"]["backgroundColor"])
assert color["navy"]["$value"] == rgb_hex(readings["promoBar"]["backgroundColor"])
assert color["navy"]["$value"] == rgb_hex(readings["addToBag"]["backgroundColor"])
assert color["ink"]["$value"] == rgb_hex(readings["nav"]["color"])
assert color["on-navy"]["$value"] == rgb_hex(readings["addToBag"]["color"])
assert color["cream"]["$value"] == rgb_hex(readings["sizeChip"]["backgroundColor"])
assert color["muted"]["$value"] == rgb_hex(readings["product"]["compareColor"])
assert color["sale"]["$value"] == rgb_hex(readings["product"]["saleColor"])
assert color["soft-blue"]["$value"] == rgb_hex(readings["footer"]["signupBackground"])
assert color["footer"]["$value"] == rgb_hex(readings["footer"]["backgroundColor"])
assert color["brand-blue"]["$value"] == readings["cssVars"]["--brand-bombas-blue"]

assert tokens["core"]["fontSize"]["nav"]["$value"] == readings["nav"]["fontSize"]
assert tokens["core"]["fontSize"]["display"]["$value"] == readings["hero"]["fontSize"]
assert tokens["core"]["fontSize"]["title"]["$value"] == readings["product"]["titleFontSize"]
assert tokens["core"]["size"]["button"]["$value"] == readings["addToBag"]["height"]
assert tokens["core"]["size"]["promo"]["$value"] == readings["promoBar"]["height"]
assert tokens["core"]["size"]["header"]["$value"] == readings["header"]["height"]
assert tokens["core"]["radius"]["button"]["$value"] == readings["addToBag"]["borderRadius"]
assert tokens["core"]["radius"]["chip"]["$value"] == readings["sizeChip"]["borderRadius"]
assert tokens["core"]["radius"]["pill"]["$value"] == readings["shopWomen"]["borderRadius"]
assert readings["addToBag"]["clicked"] is False
assert readings["login"]["emailEmpty"] is True
assert readings["login"]["submitted"] is False
assert readings["login"]["identityProviderClicked"] is False
print("bombas tokens match readings")
