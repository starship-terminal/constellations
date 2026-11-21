#!/usr/bin/env python3
"""The public Capy token file names the product and keeps a source on every token."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("$"):
                continue
            yield from walk(value, f"{path}.{key}" if path else key)


def main():
    subprocess.check_call([sys.executable, str(HERE / "tools" / "build_tokens.py")])
    doc = json.loads((HERE / "tokens.json").read_text())
    assert doc["$description"].startswith("Public Capy")
    assert "light" in doc and "dark" in doc and "core" in doc
    missing = [path for path, token in walk(doc) if "source" not in token.get("$extensions", {})]
    assert not missing, missing
    assert doc["light"]["color"]["page"]["$value"] == "#ffffff"
    assert doc["core"]["typography"]["display"]["$value"]["fontSize"] == "64px"
    print("ok", sum(1 for _ in walk(doc)), "tokens")


if __name__ == "__main__":
    main()
