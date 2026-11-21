"""Check that tokens.json still matches the public readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())


def rgb_hex(value):
    parts = value.replace("rgb(", "").replace(")", "").split(",")
    return "#{:02x}{:02x}{:02x}".format(*(int(p.strip()) for p in parts))


assert tokens["core"]["color"]["page"]["$value"] == "#ffffff"
assert tokens["core"]["color"]["ink"]["$value"] == rgb_hex(readings["home"]["body"]["color"])
assert tokens["core"]["color"]["sale"]["$value"] == rgb_hex(readings["home"]["nav"]["saleColor"])
assert tokens["core"]["color"]["promo"]["$value"] == readings["home"]["promo"]["cssVar"]
assert tokens["core"]["color"]["sand"]["$value"] == rgb_hex(readings["login"]["pageBackground"])
assert tokens["core"]["color"]["shop"]["$value"] == rgb_hex(readings["login"]["shop"]["backgroundColor"])
assert tokens["core"]["fontSize"]["body"]["$value"] == readings["home"]["body"]["fontSize"]
assert tokens["core"]["fontSize"]["display"]["$value"] == readings["home"]["hero"]["fontSize"]
assert tokens["core"]["fontSize"]["title"]["$value"] == readings["product"]["h1"]["fontSize"]
assert tokens["core"]["size"]["add-to-cart"]["$value"] == readings["product"]["addToCart"]["height"]
assert tokens["core"]["size"]["promo"]["$value"] == readings["home"]["promo"]["height"]
assert tokens["core"]["radius"]["button"]["$value"] == readings["home"]["shopNow"]["borderRadius"]
assert tokens["core"]["radius"]["button"]["$value"] == readings["product"]["addToCart"]["borderRadius"]
assert readings["product"]["addToCart"]["clicked"] is False
assert readings["home"]["shopNow"]["clicked"] is False
assert readings["login"]["providersClicked"] is False
assert readings["login"]["email"]["empty"] is True
assert readings["footer"]["subscribe"]["clicked"] is False
print("away tokens match readings")
