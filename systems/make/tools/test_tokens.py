#!/usr/bin/env python3
"""tokens.json is rebuilt from raw/css-vars.json and every token has a source."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent
TOKENS = PKG / "tokens.json"
before = TOKENS.read_text()
subprocess.check_call([sys.executable, str(HERE / "build_tokens.py")])
after = TOKENS.read_text()
assert before == after, "build_tokens.py changed tokens.json"


def walk(node):
    if isinstance(node, dict) and "$value" in node:
        yield node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v)


doc = json.loads(after)
for node in walk(doc):
    assert node["$extensions"]["source"], node
print("ok", sum(1 for _ in walk(doc)), "tokens")
