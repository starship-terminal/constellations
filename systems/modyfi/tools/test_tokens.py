#!/usr/bin/env python3
"""Package contract: measured Modyfi colours stay the colours the site declared."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((HERE / "tokens.json").read_text())
core = tokens["core"]["color"]

assert core["accent"]["$value"].lower() == "#ff0357", core["accent"]
assert core["paragraph"]["$value"].lower() == "#c9c9c9"
assert core["background"]["$value"].lower() in ("#000000", "#000")
assert core["heading"]["$value"].lower() in ("#ffffff", "#fff")
assert "dark" in tokens["$themes"][0]["selectedTokenSets"]
assert tokens["dark"]["color"]["accent"]["$value"] == "{core.color.accent}"
print("modyfi token contract ok")
