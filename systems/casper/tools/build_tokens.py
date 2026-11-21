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
assert tokens["core"]["color"]["ink"]["$value"] == rgb_hex(readings["body"]["color"])
assert tokens["core"]["color"]["ink"]["$value"] == rgb_hex(readings["announcement"]["backgroundColor"])
assert tokens["core"]["color"]["nav"]["$value"] == rgb_hex(readings["nav"]["color"])
assert tokens["core"]["color"]["sale"]["$value"] == rgb_hex(readings["sale"]["color"])
assert tokens["core"]["color"]["lime"]["$value"] == rgb_hex(readings["hero"]["accent"])
assert tokens["core"]["color"]["lime"]["$value"] == rgb_hex(readings["shopSale"]["backgroundColor"])
assert tokens["core"]["color"]["button"]["$value"] == rgb_hex(readings["login"]["buttonBackground"])
assert tokens["core"]["color"]["cart"]["$value"] == rgb_hex(readings["addToCart"]["backgroundColor"])
assert tokens["core"]["color"]["field"]["$value"] == rgb_hex(readings["login"]["fieldBorder"])
assert tokens["core"]["fontSize"]["body"]["$value"] == readings["body"]["fontSize"]
assert tokens["core"]["fontSize"]["title"]["$value"] == readings["product"]["titleFontSize"]
assert tokens["core"]["fontSize"]["display"]["$value"] == readings["hero"]["fontSize"]
assert tokens["core"]["size"]["field"]["$value"] == readings["login"]["fieldHeight"]
assert tokens["core"]["radius"]["pill"]["$value"] == readings["addToCart"]["borderRadius"]
assert readings["addToCart"]["clicked"] is False
assert readings["login"]["submitted"] is False
assert readings["login"]["providersClicked"] is False
assert readings["signup"]["submitted"] is False
assert readings["login"]["emailValueLength"] == 0
assert readings["login"]["passwordValueLength"] == 0
print("casper tokens match readings")
