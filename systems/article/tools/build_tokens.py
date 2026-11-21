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
assert tokens["core"]["color"]["ink"]["$value"] == rgb_hex(readings["body"]["color"])
assert tokens["core"]["color"]["banner"]["$value"] == rgb_hex(readings["banner"]["backgroundColor"])
assert tokens["core"]["color"]["coral"]["$value"] == rgb_hex(readings["shopSale"]["backgroundColor"])
assert tokens["core"]["color"]["coral"]["$value"] == rgb_hex(readings["addToCart"]["backgroundColor"])
assert tokens["core"]["color"]["coral"]["$value"] == readings["tokensDeclared"]["coral"]
assert tokens["core"]["color"]["field"]["$value"] == rgb_hex(readings["search"]["borderColor"])
assert tokens["core"]["color"]["footer"]["$value"] == rgb_hex(readings["footer"]["backgroundColor"])
assert tokens["core"]["fontSize"]["body"]["$value"] == readings["body"]["fontSize"]
assert tokens["core"]["fontSize"]["display"]["$value"] == readings["hero"]["displayFontSize"]
assert tokens["core"]["fontSize"]["title"]["$value"] == readings["product"]["titleFontSize"]
assert tokens["core"]["size"]["banner"]["$value"] == readings["banner"]["height"]
assert tokens["core"]["size"]["cart"]["$value"] == readings["addToCart"]["height"]
assert tokens["core"]["radius"]["pill"]["$value"] == readings["addToCart"]["borderRadius"]
assert readings["addToCart"]["clicked"] is False
assert readings["shopSale"]["clicked"] is False
assert readings["subscribe"]["clicked"] is False
assert readings["login"]["submitted"] is False
assert readings["login"]["providersClicked"] is False
assert readings["login"]["emailValueLength"] == 0
assert readings["signup"]["submitted"] is False
assert readings["search"]["typed"] is False
print("article tokens match readings")
