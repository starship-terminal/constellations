#!/usr/bin/env python3
"""Zapier tokens are written from live readings, not rebuilt by this kit copy.

The committed tokens.json is the source. This file stays so the kit layout is
present. It checks that tokens.json exists and that every token has a source.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = HERE / "tokens.json"


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            yield from walk(child, f"{path}.{key}" if path else key)


def check():
    data = json.loads(TOKENS.read_text())
    missing = [path for path, token in walk(data) if "source" not in token.get("$extensions", {})]
    if missing:
        raise SystemExit("tokens missing $extensions.source: " + ", ".join(missing))
    print(f"{len(list(walk(data)))} tokens, each with a source")


if __name__ == "__main__":
    check()
    sys.exit(0)
