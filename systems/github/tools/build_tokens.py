#!/usr/bin/env python3
"""Check named Primer roles against raw/measured.json. Does not rewrite tokens.json."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
measured = json.loads((ROOT / "raw" / "measured.json").read_text())
tokens = json.loads((ROOT / "tokens.json").read_text())
home = measured["home-light-full"]["resolved"]
dark = measured["login-dark-desktop"]["resolved"]

checks = {
    "light.color.fg.default": home["--fgColor-default"],
    "light.color.bg.default": home["--bgColor-default"],
    "light.color.accent.emphasis": home["--bgColor-accent-emphasis"],
    "light.color.success.emphasis": home["--bgColor-success-emphasis"],
    "dark.color.fg.default": dark["--fgColor-default"],
    "dark.color.bg.default": dark["--bgColor-default"],
    "dark.color.accent.emphasis": dark["--bgColor-accent-emphasis"],
}

def get(path):
    node = tokens
    for part in path.split("."):
        node = node[part]
    return node["$value"]

def norm(color):
    value = color.strip().lower()
    if value.startswith("#") and len(value) == 4:
        value = "#" + "".join(ch * 2 for ch in value[1:])
    return value

failed = 0
for path, expected in checks.items():
    got = norm(get(path))
    want = norm(expected)
    if got != want:
        print(f"mismatch {path}: tokens {got} measured {want}")
        failed += 1
    else:
        print(f"ok {path} {got}")
sys.exit(failed)
