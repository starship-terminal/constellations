#!/usr/bin/env python3
"""Check tokens.json against the readings in raw/.

The token file is the capture record. This script does not invent values.
It fails when a semantic colour in tokens.json is absent from raw/css-vars.json.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
CSS = json.loads((HERE / "raw" / "css-vars.json").read_text())
RESOLVED = CSS["home"]["resolved"]

EXPECTED = {
    "dark.accent": ("#ff5e3e", "--semantic-primary"),
    "dark.surface": ("#171717", "--semantic-background"),
    "dark.text-muted": ("#ffffff80", "--semantic-muted-foreground"),
    "dark.focus": ("#3773f5", "--semantic-focus-ring"),
    "dark.success": ("#17f455", "--semantic-success"),
    "dark.destructive": ("#ef4444", "--semantic-destructive"),
    "dark.muted": ("#ffffff1a", "--semantic-muted"),
    "dark.surface-card": ("#1b1b1b", "--semantic-surface-card"),
}


def value(path):
    node = TOKENS
    for part in path.split("."):
        node = node[part]
    return node["$value"]


def main():
    failed = False
    for path, (want, var) in EXPECTED.items():
        got = value(path)
        declared = RESOLVED.get(var, "")
        if got != want or declared.lower() != want:
            print(f"{path}: token {got} reading {var}={declared} expected {want}", file=sys.stderr)
            failed = True
    if "--font-tertiary" not in RESOLVED or "Phonic" not in RESOLVED["--font-tertiary"]:
        print("missing Phonic in --font-tertiary", file=sys.stderr)
        failed = True
    if failed:
        return 1
    print("tokens match raw/css-vars.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
