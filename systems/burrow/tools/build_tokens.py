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
assert color["ink"]["$value"] == rgb_hex(readings["nav"]["color"])
assert color["heading"]["$value"] == rgb_hex(readings["h1"]["color"])
assert color["promo"]["$value"] == rgb_hex(readings["promoBar"]["backgroundColor"])
assert color["promo-ink"]["$value"] == rgb_hex(readings["promoBar"]["linkColor"])
assert color["sale"]["$value"] == rgb_hex(readings["saleNav"]["color"])
assert color["coral"]["$value"] == rgb_hex(readings["product"]["saleColor"])
assert color["compare"]["$value"] == rgb_hex(readings["product"]["compareColor"])
assert color["quick"]["$value"] == rgb_hex(readings["quickShip"]["backgroundColor"])
assert color["button"]["$value"] == rgb_hex(readings["addToCart"]["backgroundColor"])
assert color["on-button"]["$value"] == rgb_hex(readings["addToCart"]["color"])
assert color["hero"]["$value"] == rgb_hex(readings["hero"]["titleColor"])
assert color["wordmark"]["$value"] == readings["wordmark"]["fill"]
assert color["cream"]["$value"] == "#f7eee3"

assert tokens["core"]["fontSize"]["nav"]["$value"] == readings["nav"]["fontSize"]
assert tokens["core"]["fontSize"]["display"]["$value"] == readings["hero"]["titleFontSize"]
assert tokens["core"]["fontSize"]["heading"]["$value"] == readings["h1"]["fontSize"]
assert tokens["core"]["size"]["button"]["$value"] == readings["shopSale"]["height"]
assert tokens["core"]["size"]["promo"]["$value"] == readings["promoBar"]["height"]
assert tokens["core"]["size"]["header"]["$value"] == readings["header"]["height"]
assert tokens["core"]["radius"]["button"]["$value"] == readings["shopSale"]["borderRadius"]
assert tokens["core"]["radius"]["cart"]["$value"] == readings["addToCart"]["borderRadius"]
assert readings["addToCart"]["clicked"] is False
assert readings["shopSale"]["clicked"] is False
assert readings["login"]["opened"] is False
assert readings["subscribe"]["submitted"] is False
print("burrow tokens match readings")
