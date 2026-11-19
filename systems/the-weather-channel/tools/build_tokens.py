#!/usr/bin/env python3
"""Check tokens.json for The Weather Channel.

Values were read from the live public page and written by hand into tokens.json.
This script does not invent tokens. It refuses a token with no evidence label,
a colour that is not a hex or rgba value, and a dimension that is not a px length.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = HERE / "tokens.json"
COLOR = re.compile(r"^(#[0-9a-fA-F]{6}|rgba?\([^)]+\))$")
DIM = re.compile(r"^\d+(\.\d+)?px$")
EVIDENCE = {"Measured", "Derived", "Sampled", "Observed", "Reconstruction", "Not captured"}


def walk(node, path, errors):
    if not isinstance(node, dict):
        return
    if "$value" in node:
        if "$extensions" not in node or "source" not in node.get("$extensions", {}):
            errors.append(f"{path}: missing $extensions.source")
        else:
            label = node["$extensions"]["source"].get("evidence")
            if label not in EVIDENCE:
                errors.append(f"{path}: evidence {label!r} is not a known label")
            if not node["$extensions"]["source"].get("where"):
                errors.append(f"{path}: source has no where")
        kind = node.get("$type")
        value = node["$value"]
        if kind == "color" and not (isinstance(value, str) and COLOR.match(value)):
            errors.append(f"{path}: colour {value!r} is not hex or rgb")
        if kind == "dimension" and not (isinstance(value, str) and DIM.match(value)):
            errors.append(f"{path}: dimension {value!r} is not a px length")
        if kind == "cubicBezier":
            if not (isinstance(value, list) and len(value) == 4):
                errors.append(f"{path}: easing is not four numbers")
        return
    for key, child in node.items():
        if key.startswith("$"):
            continue
        walk(child, f"{path}.{key}" if path else key, errors)


def check(data):
    errors = []
    for group in ("core", "light"):
        if group not in data:
            errors.append(f"missing {group} set")
        else:
            walk(data[group], group, errors)
    if "dark" in data:
        errors.append("dark set is present; the public page had no dark theme")
    return errors


def main():
    data = json.loads(TOKENS.read_text())
    errors = check(data)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"{TOKENS.name}: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
