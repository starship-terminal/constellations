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
assert color["page"]["$value"] == rgb_hex(readings["main"]["backgroundColor"])
assert color["ink"]["$value"] == rgb_hex(readings["ink"])
assert color["ink"]["$value"] == rgb_hex(readings["loginButton"]["backgroundColor"])
assert color["on-ink"]["$value"] == rgb_hex(readings["loginButton"]["color"])
assert color["lime"]["$value"] == rgb_hex(readings["promoBar"]["backgroundColor"])
assert color["lime"]["$value"] == rgb_hex(readings["badge"]["backgroundColor"])
assert color["nav"]["$value"] == rgb_hex(readings["navRow"]["backgroundColor"])
assert color["footer"]["$value"] == rgb_hex(readings["footer"]["backgroundColor"])
assert color["sale"]["$value"] == rgb_hex(readings["salePrice"]["color"])
assert color["bronze"]["$value"] == rgb_hex(readings["membershipKicker"]["color"])
assert color["panel"]["$value"] == rgb_hex(readings["loginPanel"]["backgroundColor"])

assert tokens["core"]["fontSize"]["nav"]["$value"] == readings["nav"]["fontSize"]
assert tokens["core"]["fontSize"]["button"]["$value"] == readings["loginButton"]["fontSize"]
assert tokens["core"]["fontSize"]["title"]["$value"] == readings["loginTitle"]["fontSize"]
assert tokens["core"]["size"]["button"]["$value"] == readings["loginButton"]["height"]
assert tokens["core"]["size"]["promo"]["$value"] == readings["promoBar"]["height"]
assert tokens["core"]["radius"]["chip"]["$value"] == readings["badge"]["borderRadius"]
assert readings["loginButton"]["clicked"] is False
assert readings["selectASize"]["clicked"] is False
assert readings["login"]["emailEmpty"] is True
assert readings["login"]["passwordEmpty"] is True
assert readings["login"]["submitted"] is False
assert readings["login"]["googleClicked"] is False
assert readings["login"]["facebookClicked"] is False
assert readings["signup"]["submitted"] is False
assert readings["signup"]["value"] == ""
assert readings["cartOpened"] is False
assert readings["getStartedClicked"] is False
assert readings["google"]["clicked"] is False
print("meundies tokens match readings")
