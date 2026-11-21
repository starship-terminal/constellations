"""Check that tokens.json still matches the public readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())

def rgb_hex(value):
    parts = value.replace("rgb(", "").replace(")", "").split(",")
    return "#{:02x}{:02x}{:02x}".format(*(int(p.strip()) for p in parts))

assert tokens["core"]["color"]["page"]["$value"] == rgb_hex(readings["body"]["backgroundColor"])
assert tokens["core"]["color"]["text"]["$value"] == rgb_hex(readings["body"]["color"])
assert tokens["core"]["color"]["ink"]["$value"] == readings["nav"]["linkColor"].replace("rgb(0, 0, 0)", "#000000")
assert tokens["core"]["color"]["product"]["$value"] == rgb_hex(readings["product"]["titleColor"])
assert tokens["core"]["color"]["product"]["$value"] == rgb_hex(readings["addToCart"]["color"])
assert tokens["core"]["fontSize"]["body"]["$value"] == readings["body"]["fontSize"]
assert tokens["core"]["fontSize"]["title"]["$value"] == readings["product"]["titleFontSize"]
assert tokens["core"]["fontSize"]["display"]["$value"] == readings["hero"]["fontSize"]
assert tokens["core"]["size"]["add-to-cart"]["$value"] == readings["addToCart"]["height"]
assert tokens["core"]["size"]["add-to-cart"]["$value"] == readings["signup"]["joinNow"]["height"]
assert tokens["core"]["size"]["field"]["$value"] == readings["login"]["email"]["height"]
assert tokens["core"]["radius"]["button"]["$value"] == readings["addToCart"]["borderRadius"]
assert tokens["core"]["radius"]["explore"]["$value"] == readings["explore"]["borderRadius"]
assert readings["addToCart"]["clicked"] is False
assert readings["login"]["providersClicked"] is False
assert readings["signup"]["providersClicked"] is False
print("the-ordinary tokens match readings")
