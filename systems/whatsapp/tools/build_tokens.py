#!/usr/bin/env python3
"""Check tokens.json for the WhatsApp public marketing capture.

whatsapp.com declares no custom properties on :root. tokens.json was written
from computed styles (raw/readings.json notes the pages). This script does not
invent tokens. It checks the file still has the measured roles and exits 0
when it does.

    python3 tools/build_tokens.py
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = HERE / "tokens.json"

REQUIRED = [
    "core.color.green",
    "core.color.ink",
    "core.color.ink-deep",
    "core.color.cream",
    "core.font.family.sans",
    "core.typography.display",
    "core.radius.pill",
    "light.background.page",
    "light.background.field",
    "light.text.primary",
    "light.text.muted",
    "light.action.primary",
    "light.border.default",
]


def lookup(node, path):
    cur = node
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def main() -> int:
    data = json.loads(TOKENS.read_text())
    missing = [p for p in REQUIRED if lookup(data, p) is None]
    if missing:
        print("missing measured tokens:", ", ".join(missing), file=sys.stderr)
        return 1
    if data.get("dark"):
        print("dark set must stay empty: no dark theme was painted", file=sys.stderr)
        return 1
    green = lookup(data, "core.color.green")["$value"]
    if green != "#25d366":
        print("green drifted from the measured #25d366", file=sys.stderr)
        return 1
    print("tokens.json: measured roles present, dark set empty")
    return 0


if __name__ == "__main__":
    sys.exit(main())
