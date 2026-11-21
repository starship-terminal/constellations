#!/usr/bin/env python3
"""Check that systems/booking/tokens.json cites a capture source for every token."""

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
    accent = readings["sampledHex"]["accent"]
    if data["light"]["color"]["accent"]["$value"] != accent:
        raise SystemExit("accent token does not match sampled #006ce4")
    page = readings["computed"]["body"]["backgroundColor"]
    if page != "rgb(255, 255, 255)":
        raise SystemExit(f"unexpected page background {page}")
    header = readings["computed"]["header"]["backgroundColor"]
    if header != "rgb(0, 59, 149)":
        raise SystemExit(f"unexpected header {header}")
    print("tokens ok")


if __name__ == "__main__":
    main()
