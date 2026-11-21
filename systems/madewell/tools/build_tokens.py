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
assert color["on-ink"]["$value"] == rgb_hex(readings["addToBag"]["color"])
assert color["brand"]["$value"] == rgb_hex(readings["announcement"]["backgroundColor"])
assert color["nav-accent"]["$value"] == rgb_hex(readings["navAccent"]["color"])
assert color["field"]["$value"] == rgb_hex(readings["search"]["backgroundColor"])
assert color["field-muted"]["$value"] == rgb_hex(readings["newsletter"]["backgroundColor"])
assert color["footer"]["$value"] == rgb_hex(readings["footer"]["backgroundColor"])

assert tokens["core"]["fontSize"]["nav"]["$value"] == readings["nav"]["fontSize"]
assert tokens["core"]["fontSize"]["body"]["$value"] == readings["body"]["fontSize"]
assert tokens["core"]["size"]["announcement"]["$value"] == readings["announcement"]["height"]
assert tokens["core"]["size"]["header"]["$value"] == readings["header"]["height"]
assert tokens["core"]["size"]["add-to-bag"]["$value"] == readings["addToBag"]["height"]
assert tokens["core"]["radius"]["control"]["$value"] == readings["addToBag"]["borderRadius"]
assert readings["addToBag"]["clicked"] is False
assert readings["newsletter"]["submitted"] is False
assert readings["login"]["emailEmpty"] is True
assert readings["login"]["submitted"] is False
assert readings["login"]["screenshotDiscarded"] is True
print("madewell tokens match readings")
