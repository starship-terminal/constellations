#!/usr/bin/env python3
"""Check that systems/amazon/tokens.json cites a capture source for every token."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = ROOT / "tokens.json"
READINGS = ROOT / "raw" / "measured-hex.json"


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        source = (node.get("$extensions") or {}).get("source") or {}
        if not source.get("evidence") or not source.get("capture"):
            raise SystemExit(f"missing source at {path}")
        if "amazon.com" not in source["capture"]:
            raise SystemExit(f"capture missing amazon.com at {path}")
        return
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("$"):
                continue
            walk(value, f"{path}.{key}" if path else key)


def main():
    data = json.loads(TOKENS.read_text())
    walk(data)
    readings = json.loads(READINGS.read_text())
    brand = readings["customProperties"]["--nav-desktop-header-tbg"]
    if data["light"]["color"]["brand"]["$value"] != brand:
        raise SystemExit("brand token does not match --nav-desktop-header-tbg")
    page = readings["computed"]["body"]["backgroundColor"]
    if page != "rgb(255, 255, 255)":
        raise SystemExit(f"unexpected page background {page}")
    print("tokens ok")


if __name__ == "__main__":
    main()
