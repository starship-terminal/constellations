#!/usr/bin/env python3
"""Pass through tokens.json. The readings live in raw/. This builder checks the file parses."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((HERE / "tokens.json").read_text())
assert "core" in tokens and "light" in tokens
assert tokens["light"]["accent"]["$value"] == "#f35820"
print("tokens.json ok", HERE / "tokens.json")
