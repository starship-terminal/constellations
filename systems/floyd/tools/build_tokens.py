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
assert color["page"]["$value"] == rgb_hex(readings["body"]["backgroundColor"])
assert color["ink"]["$value"] == rgb_hex(readings["body"]["color"])
assert color["ink"]["$value"] == rgb_hex(readings["addToCart"]["backgroundColor"])
assert color["on-ink"]["$value"] == rgb_hex(readings["addToCart"]["color"])
assert color["announcement"]["$value"] == rgb_hex(readings["announcement"]["backgroundColor"])
assert color["nav"]["$value"] == rgb_hex(readings["nav"]["color"])
assert color["muted"]["$value"] == rgb_hex(readings["product"]["regularColor"])
assert color["ink"]["$value"] == readings["wordmark"]["fill"].lower()

assert tokens["core"]["fontSize"]["body"]["$value"] == readings["nav"]["fontSize"]
assert tokens["core"]["fontSize"]["title"]["$value"] == readings["product"]["titleFontSize"]
assert tokens["core"]["size"]["button"]["$value"] == readings["addToCart"]["height"]
assert tokens["core"]["size"]["announcement"]["$value"] == readings["announcement"]["height"]
assert tokens["core"]["radius"]["button"]["$value"] == readings["addToCart"]["borderRadius"]
assert readings["addToCart"]["clicked"] is False
assert readings["newsletter"]["submitted"] is False
assert readings["login"]["emailEmpty"] is True
assert readings["login"]["submitted"] is False
assert readings["login"]["screenshotDiscarded"] is True
print("floyd tokens match readings")
