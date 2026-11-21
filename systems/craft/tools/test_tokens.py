"""Checks that named Craft tokens match the captured readings."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
raw = json.loads((ROOT / "raw" / "css-vars.json").read_text())
vars_ = raw["vars"]

assert vars_["--background"] == "#fcf9f7"
assert vars_["--foreground"] == "#030302"
assert vars_["--primary"] == "#030302"
assert vars_["--accent"] == "#427e8a"
assert vars_["--destructive"] == "#bb433a"
assert tokens["light"]["color"]["background"]["page"]["$value"] == "#fcf9f7"
assert tokens["light"]["color"]["action"]["primary"]["$value"] == "#030302"
assert tokens["core"]["font"]["size"]["hero"]["$value"] == "66px"
assert tokens["light"]["color"]["background"]["auth-button"]["$value"] == "#2e6de9"
print("craft tokens ok")
