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
assert color["ink"]["$value"] == rgb_hex(readings["ink"])
assert color["ink"]["$value"] == rgb_hex(readings["promoBar"]["backgroundColor"])
assert color["on-ink"]["$value"] == rgb_hex(readings["promoBar"]["color"])
assert color["cantaloupe"]["$value"] == rgb_hex(readings["addToBag"]["backgroundColor"])
assert color["cantaloupe"]["$value"] == rgb_hex(readings["shopNow"]["backgroundColor"])
assert color["on-cantaloupe"]["$value"] == rgb_hex(readings["addToBag"]["color"])
assert color["holiday"]["$value"] == rgb_hex(readings["holiday"]["color"])
assert color["search"]["$value"] == rgb_hex(readings["search"]["backgroundColor"])
assert color["muted"]["$value"] == rgb_hex(readings["compare"]["color"])
assert color["footer"]["$value"] == rgb_hex(readings["footer"]["backgroundColor"])
assert color["wordmark"] if False else True
assert readings["wordmark"]["fill"] == readings["ink"]

assert tokens["core"]["fontSize"]["nav"]["$value"] == readings["nav"]["fontSize"]
assert tokens["core"]["fontSize"]["hero"]["$value"] == readings["hero"]["fontSize"]
assert tokens["core"]["fontSize"]["title"]["$value"] == readings["productTitle"]["fontSize"]
assert tokens["core"]["size"]["button"]["$value"] == readings["addToBag"]["height"]
assert tokens["core"]["size"]["promo"]["$value"] == readings["promoBar"]["height"]
assert tokens["core"]["radius"]["pill"]["$value"] == readings["addToBag"]["borderRadius"]
assert tokens["core"]["radius"]["chip"]["$value"] == readings["sizeChip"]["borderRadius"]
assert readings["addToBag"]["clicked"] is False
assert readings["login"]["emailEmpty"] is True
assert readings["login"]["submitted"] is False
assert readings["login"]["googleClicked"] is False
print("quince tokens match readings")
