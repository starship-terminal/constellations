#!/usr/bin/env python3
"""Refresh the capture inventory from accepted images and sanitized readings."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


def build():
    path = HERE / "raw/capture-inventory.json"
    inventory = json.loads(path.read_text())
    ingest = json.loads((HERE / "raw/readings/_ingest.json").read_text())
    inventory["screenshots"] = [image["file"] for image in ingest["images"]]
    inventory["readings"] = []
    for item in ingest["measurements"]:
        reading_path = HERE / "raw/readings" / item["file"]
        data = json.loads(reading_path.read_text())
        inventory["readings"].append({
            "file": reading_path.relative_to(HERE).as_posix(),
            "width": data["width"], "height": data["height"],
            "theme": data["theme"], "elements": len(data["elements"]),
        })
    inventory["exclusions"] = [
        "Clipped mobile create-user dialog",
        "API key pages and test credential settings",
        "Light mobile and light dashboard states beyond the five retained light readings",
        "Paid activation, financial details, user profile detail pages",
        "Hover/pressed, post-submit validation, successful mutation feedback",
        "Other nested tabs not listed in screenshots",
    ]
    inventory["appearanceApproval"] = {
        "approved": True,
        "scope": "Temporary account appearance change for the five retained light states",
        "lightReadings": [item["file"] for item in inventory["readings"] if "-light-" in item["file"]],
        "restored": "Original dark appearance restored and verified after capture",
    }
    path.write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n")
    print(f"capture-inventory.json: {len(inventory['readings'])} readings, {len(inventory['screenshots'])} screenshots")


if __name__ == "__main__":
    build()
