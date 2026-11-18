#!/usr/bin/env python3
"""Write components.md from the Maze measurement file.

Reads raw/components-computed.json and tokens.json. Every colour is the
computed value, followed by the core colour token when one matches. A state
row shows only what differs from the first state.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.loads((ROOT / "raw" / "components-computed.json").read_text())
T = json.loads((ROOT / "tokens.json").read_text())
C = J["components"]


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


BY = {}
for name, tok in flat(T["core"]["color"]):
    if tok["$type"] == "color" and isinstance(tok["$value"], str) and tok["$value"].startswith("#"):
        BY.setdefault(tok["$value"].lower(), name)


def hex_of(c):
    m = re.fullmatch(r"rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*[\d.]+)?\)", c or "")
    if not m:
        return None
    return "#%02x%02x%02x" % tuple(int(x) for x in m.group(1, 2, 3))


def colour(c):
    h = hex_of(c)
    if not h:
        return c or ""
    tok = BY.get(h)
    return f"{h} `{tok}`" if tok else h


def row(state, s, base):
    style = s.get("style") or {}
    bits = []
    for key, label in (("backgroundColor", "fill"), ("color", "ink"), ("fontSize", "size"), ("fontWeight", "weight"), ("borderTopLeftRadius", "radius"), ("fontFamily", "font")):
        val = style.get(key)
        if not val or (base and base.get(key) == val):
            continue
        shown = colour(val) if "olor" in key else val
        if key == "fontFamily":
            shown = shown.split(",")[0].strip('"')
        bits.append(f"{label} {shown}")
    rect = s.get("rect") or {}
    size = f"{round(rect.get('w', 0))}×{round(rect.get('h', 0))}"
    crop = s.get("crop") or ""
    link = f"[crop]({crop})" if crop else ""
    return f"| {state} | {size} | {', '.join(bits) or 'same'} | {s.get('via', '')} | {link} |"


lines = [
    "# Components",
    "",
    "Measured on the live signed-out DOM, 2026-11-18, light, 1440 (phone menu at 390). Nothing was submitted. Login email was filled with `sample@example.com` and cleared. The password field was focused and never filled.",
    "",
]
groups = {}
for key, comp in C.items():
    groups.setdefault(comp.get("group") or "Other", []).append((key, comp))

for group, items in groups.items():
    lines.append(f"## {group}")
    lines.append("")
    for key, comp in items:
        lines.append(f"### {comp.get('title') or key}")
        lines.append("")
        lines.append(f"Selector: `{comp.get('sel', '')}`.")
        if comp.get("missing"):
            lines.append("")
            lines.append("Not found on the page at measure time.")
            lines.append("")
            continue
        lines.append("")
        lines.append("| State | Size | What changed | How | Crop |")
        lines.append("|---|---|---|---|---|")
        states = comp.get("states") or {}
        base = None
        for name, s in states.items():
            if s.get("error"):
                lines.append(f"| {name} |  | {s['error']} | {s.get('via', '')} | |")
                continue
            lines.append(row(name, s, base))
            base = base or (s.get("style") or {})
        lines.append("")

(ROOT / "components.md").write_text("\n".join(lines) + "\n")
print("components", len(C))
