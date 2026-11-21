#!/usr/bin/env python3
"""The token file names the public Reflect capture and keeps a source on every token."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((HERE / "tokens.json").read_text())


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        source = node.get("$extensions", {}).get("source", {})
        assert source.get("label") == "Measured", path
        assert source.get("file", "").startswith("raw/"), path
        assert source.get("where"), path
        return
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("$"):
                continue
            walk(value, path + "." + key)


walk(tokens["core"])
walk(tokens["light"])
assert tokens["light"]["color"]["bg"]["page"]["$value"] == "#030014"
assert "dark" not in tokens
print("ok")
