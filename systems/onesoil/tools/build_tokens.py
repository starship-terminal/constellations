#!/usr/bin/env python3
"""Check systems/onesoil/tokens.json.

The marketing tokens were written from live computed styles on 2026-11-19.
This script does not invent values. It checks the committed file and exits
0 when every token has a source and every alias resolves.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent
TOKENS = PKG / "tokens.json"


class CheckError(Exception):
    pass


def walk(node, prefix=()):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = prefix + (key,)
        if isinstance(value, dict) and "$value" in value:
            yield path, value
        elif isinstance(value, dict):
            yield from walk(value, path)


def aliases(value):
    if isinstance(value, str):
        return re.findall(r"\{([^{}]+)\}", value)
    if isinstance(value, dict):
        found = []
        for item in value.values():
            found.extend(aliases(item))
        return found
    if isinstance(value, list):
        found = []
        for item in value:
            found.extend(aliases(item))
        return found
    return []


def check(doc):
    sets = [name for name in ("core", "light", "dark") if name in doc]
    paths = {".".join(path) for name in sets for path, _ in walk(doc[name])}
    for name in sets:
        for path, token in walk(doc[name]):
            where = name + "." + ".".join(path)
            src = token.get("$extensions", {}).get("source", {})
            if not src.get("evidence") or not src.get("capture"):
                raise CheckError(f"{where}: no source")
            for alias in aliases(token["$value"]):
                if alias not in paths:
                    raise CheckError(f"{where}: alias {{{alias}}} points at nothing")
            value = token["$value"]
            if isinstance(value, str) and value.startswith("{"):
                continue
            if token["$type"] == "color" and not re.fullmatch(r"#[0-9A-Fa-f]{6}([0-9A-Fa-f]{2})?", value):
                raise CheckError(f"{where}: bad colour {value}")
            if token["$type"] == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?px", value):
                raise CheckError(f"{where}: bad dimension {value}")
    if "light" in doc and "dark" in doc:
        light = sorted(".".join(path) for path, _ in walk(doc["light"]))
        dark = sorted(".".join(path) for path, _ in walk(doc["dark"]))
        if light != dark:
            raise CheckError("light and dark keys differ")


def main():
    doc = json.loads(TOKENS.read_text())
    check(doc)
    count = sum(1 for name in ("core", "light", "dark") if name in doc for _ in walk(doc[name]))
    print(f"tokens.json: {count} tokens ok")


if __name__ == "__main__":
    try:
        main()
    except CheckError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
