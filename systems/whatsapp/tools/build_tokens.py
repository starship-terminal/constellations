#!/usr/bin/env python3
"""Check tokens.json for the WhatsApp public marketing capture.

whatsapp.com declares no custom properties on :root. tokens.json was written
from computed styles (raw/readings.json notes the pages). This script does not
invent tokens. It checks the file still has the measured roles, that every
token has a source, and that every colour labelled Measured is held by a file
in raw/, and exits 0 when it does.

    python3 tools/build_tokens.py
"""
import json
import pathlib
import re
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


def walk(node, path=""):
    for key, value in node.items():
        if key.startswith("$") or not isinstance(value, dict):
            continue
        if "$value" in value:
            yield path + key, value
        else:
            yield from walk(value, path + key + ".")


def raw_colours():
    """Every colour raw/ holds: hex as written, rgb()/rgba() as #rrggbb."""
    seen = set()
    for f in sorted((HERE / "raw").iterdir()):
        text = f.read_text()
        seen.update(h.lower() for h in re.findall(r"#[0-9a-fA-F]{6}\b", text))
        for body in re.findall(r"rgba?\((\d+), (\d+), (\d+)", text):
            seen.add("#%02x%02x%02x" % tuple(int(c) for c in body))
    return seen


def resolve(data, setname, value, depth=0):
    """The literal an alias chain ends at (own set, then core, then root), or None if it breaks."""
    m = re.fullmatch(r"\{([^{}]+)\}", value) if isinstance(value, str) else None
    if not m:
        return value
    if depth > 20:
        return None
    for scope in (data.get(setname, {}), data.get("core", {}), data):
        target = lookup(scope, m.group(1))
        if isinstance(target, dict) and "$value" in target:
            return resolve(data, setname, target["$value"], depth + 1)
    return None


def problems(data, seen):
    """Tokens with no source, and Measured colours, direct or through an alias, no raw/ file holds."""
    out = []
    for name in ("core", "light", "dark"):
        for path, token in walk(data.get(name, {})):
            source = token.get("$extensions", {}).get("source")
            if not source:
                out.append(f"{name}.{path}: no source")
            if token["$type"] != "color" or not str(source).startswith("Measured"):
                continue
            value = resolve(data, name, token["$value"])
            if value is None:
                out.append(f"{name}.{path}: alias {token['$value']} does not resolve")
            elif isinstance(value, str) and value.startswith("#") and value.lower()[:7] not in seen:
                via = f" (through {token['$value']})" if value != token["$value"] else ""
                out.append(f"{name}.{path}: Measured {value}{via} is in no raw/ reading")
    return out


def main() -> int:
    data = json.loads(TOKENS.read_text())
    bad = problems(data, raw_colours())
    if bad:
        print("\n".join(bad), file=sys.stderr)
        return 1
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
