#!/usr/bin/env python3
"""Check that systems/grafana/tokens.json cites a capture source for every token."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = ROOT / "tokens.json"
READINGS = ROOT / "raw" / "measured-hex.json"


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        source = (node.get("$extensions") or {}).get("source") or {}
        if not source.get("evidence") or not source.get("capture"):
            raise SystemExit(f"missing source at {path}")
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
    accent = readings["customProperties"]["--gmui-color-blue-600"]
    if data["light"]["color"]["accent"]["$value"] != accent:
        raise SystemExit("accent token does not match measured --gmui-color-blue-600")
    page = readings["body"]["backgroundColor"]
    if page != "rgb(244, 244, 246)":
        raise SystemExit(f"unexpected page background {page}")
    print("tokens ok")


if __name__ == "__main__":
    main()
