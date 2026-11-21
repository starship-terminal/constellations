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
assert color["ink"]["$value"] == rgb_hex(readings["body"]["color"])
assert color["ink"]["$value"] == rgb_hex(readings["addToCart"]["backgroundColor"])
assert color["ink"]["$value"] == readings["wordmark"]["fill"]
assert color["on-ink"]["$value"] == rgb_hex(readings["addToCart"]["color"])
assert color["sage"]["$value"] == rgb_hex(readings["promoBar"]["backgroundColor"])
assert color["rust"]["$value"] == rgb_hex(readings["product"]["saleColor"])
assert color["compare"]["$value"] == rgb_hex(readings["product"]["compareColor"])
assert color["bronze"]["$value"] == rgb_hex(readings["bronze"])
assert color["stone"]["$value"] == rgb_hex(readings["stone"])
assert color["wall"]["$value"] == rgb_hex(readings["login"]["pageBackground"])
assert color["field-border"]["$value"] == "#dedede"

assert tokens["core"]["fontSize"]["nav"]["$value"] == readings["nav"]["fontSize"]
assert tokens["core"]["fontSize"]["title"]["$value"] == readings["product"]["titleFontSize"]
assert tokens["core"]["fontSize"]["sale"]["$value"] == readings["product"]["saleFontSize"]
assert tokens["core"]["size"]["promo"]["$value"] == readings["promoBar"]["height"]
assert tokens["core"]["size"]["cart"]["$value"] == readings["addToCart"]["height"]
assert tokens["core"]["size"]["chip"]["$value"] == readings["sizeChip"]["height"]
assert tokens["core"]["radius"]["button"]["$value"] == readings["addToCart"]["borderRadius"]
assert tokens["core"]["radius"]["field"]["$value"] == readings["login"]["fieldRadius"]
assert readings["addToCart"]["clicked"] is False
assert readings["login"]["emailEmpty"] is True
assert readings["login"]["submitted"] is False
assert readings["login"]["screenshotKept"] is False
print("coyuchi tokens match readings")
