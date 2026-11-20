#!/usr/bin/env python3
"""Check tokens.json against raw/computed-root.json for Meta AI.

The token file was written from live computed styles on 2026-11-19. This script
does not browse. It fails if a semantic colour in tokens.json disagrees with the
saved computed custom property.

    python3 tools/build_tokens.py
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
RAW = json.loads((HERE / "raw" / "computed-root.json").read_text())["vars"]

CHECKS = {
    "dark.surface.page": "--background-primary",
    "dark.surface.raised": "--fill-primary",
    "dark.text.primary": "--text-primary",
    "dark.text.secondary": "--text-secondary",
    "dark.text.tertiary": "--text-tertiary",
    "dark.accent": "--accent-dark",
    "dark.accentPressed": "--accent",
    "dark.border.subtle": "--color-fill-divider",
    "dark.text.link": "--text-primary-link",
    "dark.text.destructive": "--color-text-destructive",
}


def dig(node, path):
    cur = node
    for part in path.split("."):
        cur = cur[part]
    return cur["$value"]


def main():
    bad = []
    for token_path, var in CHECKS.items():
        got = dig(TOKENS, token_path)
        expect = RAW[var]
        if got != expect:
            bad.append(f"{token_path} is {got}, {var} is {expect}")
    if "core" not in TOKENS or "dark" not in TOKENS or "light" not in TOKENS:
        bad.append("tokens.json needs core, dark and light sets")
    if bad:
        print("\n".join(bad))
        return 1
    print("tokens.json matches raw/computed-root.json on", len(CHECKS), "semantic colours")
    return 0


if __name__ == "__main__":
    sys.exit(main())
