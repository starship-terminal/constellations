#!/usr/bin/env python3
"""Check that systems/disneyplus/tokens.json cites a capture source for every token."""

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
    accent = data["light"]["color"]["accent"]["$value"]
    if accent != readings["accent"]:
        raise SystemExit(f"accent {accent} does not match measured {readings['accent']}")
    page = data["light"]["color"]["page"]["$value"]
    if page != readings["page"]:
        raise SystemExit(f"page {page} does not match measured {readings['page']}")
    print("tokens ok")


if __name__ == "__main__":
    main()
