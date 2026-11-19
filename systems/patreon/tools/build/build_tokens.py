#!/usr/bin/env python3
"""Check systems/patreon/tokens.json against raw/computed.json.

The marketing values were read live from https://www.patreon.com/ on 2026-11-19.
This script does not invent tokens. It checks that the colours and sizes written
in tokens.json still match the readings in raw/computed.json.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
RAW = json.loads((HERE / "raw" / "computed.json").read_text())


def check():
    resolved = RAW["resolved"]
    problems = []
    expect = {
        ("core", "color", "primary"): resolved["--color-primary"],
        ("core", "color", "highlight"): resolved["--color-highlight"],
        ("core", "color", "red"): resolved["--color-red"],
        ("core", "color", "green"): resolved["--color-green"],
        ("core", "color", "yellow"): resolved["--color-yellow"],
    }
    for path, raw in expect.items():
        node = TOKENS
        for part in path:
            node = node[part]
        got = node["$value"].lower()
        if got != raw.lower():
            problems.append(f"{'.'.join(path)} is {got}, reading is {raw}")
    desktop = RAW["computed"]["desktop1440"]
    button = TOKENS["core"]["size"]["button"]["$value"]
    if button != desktop["getStarted"]["height"]:
        problems.append(f"button height {button} != {desktop['getStarted']['height']}")
    if TOKENS["core"]["radius"]["pill"]["$value"] != desktop["getStarted"]["radius"]:
        problems.append("pill radius drifted from the Get Started reading")
    login = RAW["computed"]["login"]
    if TOKENS["core"]["size"]["login-control"]["$value"] != login["continue"]["height"]:
        problems.append("login control height drifted")
    return problems


def main():
    problems = check()
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print("tokens.json matches raw/computed.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
