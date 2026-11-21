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
assert color["page"]["$value"] == rgb_hex(readings["page"])
assert color["ink"]["$value"] == rgb_hex(readings["ink"])
assert color["ink"]["$value"] == rgb_hex(readings["signIn"]["backgroundColor"])
assert color["on-ink"]["$value"] == rgb_hex(readings["promoText"]["color"])
assert color["promo"]["$value"] == rgb_hex(readings["promoBar"]["backgroundColor"])
assert color["gold"]["$value"] == rgb_hex(readings["joinNow"]["backgroundColor"])
assert color["black"]["$value"] == rgb_hex(readings["selectSize"]["backgroundColor"])
assert color["muted"]["$value"] == rgb_hex(readings["compare"]["color"])
assert color["chip"]["$value"] == rgb_hex(readings["sizeChip"]["color"])
assert color["field-border"]["$value"] == "#cccccc"

assert tokens["core"]["fontSize"]["nav"]["$value"] == readings["nav"]["fontSize"]
assert tokens["core"]["fontSize"]["hero"]["$value"] == readings["hero"]["fontSize"]
assert tokens["core"]["fontSize"]["price"]["$value"] == readings["price"]["fontSize"]
assert tokens["core"]["size"]["promo"]["$value"] == readings["promoBar"]["height"]
assert tokens["core"]["size"]["select"]["$value"] == readings["selectSize"]["height"]
assert tokens["core"]["size"]["chip"]["$value"] == readings["sizeChip"]["height"]
assert tokens["core"]["radius"]["pill"]["$value"] == readings["selectSize"]["borderRadius"]
assert tokens["core"]["radius"]["chip"]["$value"] == readings["sizeChip"]["borderRadius"]
assert readings["selectSize"]["clicked"] is False
assert readings["joinNow"]["clicked"] is False
assert readings["login"]["emailEmpty"] is True
assert readings["login"]["passwordEmpty"] is True
assert readings["login"]["submitted"] is False
assert readings["login"]["googleClicked"] is False
assert readings["addToBagClicked"] is False
print("thirdlove tokens match readings")
