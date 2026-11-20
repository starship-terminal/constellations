#!/usr/bin/env python3
"""Write components.md from the Melius measurement file.

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


def cell(text):
    """A table cell: a pipe would split it and a newline would end the row."""
    return " ".join(str(text).split()).replace("|", "\\|")


BY = {}
for name, tok in flat(T["core"]["color"]):
    if tok["$type"] == "color" and isinstance(tok["$value"], str) and tok["$value"].startswith("#"):
        BY.setdefault(tok["$value"].lower(), name)


def colour(c):
    if not c:
        return ""
    m = re.fullmatch(r"rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)", c)
    if not m:
        return c
    alpha = m.group(4)
    if alpha is not None and float(alpha) == 0:
        return "transparent"
    h = "#%02x%02x%02x" % tuple(int(x) for x in m.group(1, 2, 3))
    shown = h
    if alpha is not None and float(alpha) < 1:
        shown = f"{h} / {alpha}"
    tok = BY.get(h) if shown == h else None
    return f"{shown} `{tok}`" if tok else shown


TEXT_KEYS = ("color", "fontSize", "fontWeight", "fontFamily")
PAINT_KEYS = (
    ("backgroundColor", "fill"),
    ("color", "ink"),
    ("fontSize", "size"),
    ("fontWeight", "weight"),
    ("fontFamily", "font"),
    ("borderTopLeftRadius", "radius"),
    ("outlineWidth", "outline"),
    ("outlineColor", "outline colour"),
    ("boxShadow", "shadow"),
)


def paint(s):
    style = dict(s.get("style") or {})
    text = s.get("textStyle") or {}
    for key in TEXT_KEYS:
        if text.get(key):
            style[key] = text[key]
    return style


def row(state, s, base):
    style = paint(s)
    bits = []
    for key, label in PAINT_KEYS:
        val = style.get(key)
        if not val or val in ("none", "0px") or (base and base.get(key) == val):
            continue
        if key == "outlineColor" and (style.get("outlineWidth") or "0px") in ("0px", "0", "none"):
            continue
        shown = colour(val) if "olor" in key or key == "boxShadow" else val
        if key == "fontFamily":
            shown = shown.split(",")[0].strip('"')
        if key == "boxShadow" and len(shown) > 80:
            shown = shown[:77] + "..."
        bits.append(f"{label} {shown}")
    rect = s.get("rect") or {}
    size = f"{round(rect.get('w', 0))}×{round(rect.get('h', 0))}"
    crop = s.get("crop") or ""
    link = f"[crop]({crop})" if crop else ""
    return f"| {cell(state)} | {size} | {cell(', '.join(bits) or 'same')} | {cell(s.get('via', ''))} | {link} |"


lines = [
    "# Components",
    "",
    "Measured on the live signed-out DOM, 2026-11-19, light, 1440 (phone menu at 390). Nothing was submitted. Login email was filled with `sample@example.com` and cleared. Password, billing, Google and the newsletter were never submitted.",
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
                lines.append(f"| {cell(name)} |  | {cell(s['error'])} | {cell(s.get('via', ''))} | |")
                continue
            if s.get("skipped") or s.get("via") == "focus failed":
                # The element at rest, not the state: listed as not captured and never used as a base.
                lines.append(f"| {cell(name)} |  | not captured: keyboard focus did not reach the element | {cell(s.get('via', ''))} | |")
                continue
            lines.append(row(name, s, base))
            base = base or paint(s)
        lines.append("")

# The coverage checklist. It was typed into components.md by hand, so a rebuild deleted it; it is
# written here now, with links from the package root, where components.md sits.
GAPS = [
    ("Button, link, text field, card, menu", "Captured. Nav focus-visible is a 2px orange outline."),
    ("Icon button", "The phone hamburger measured 0×0. The click did not open a drawer."),
    ("Text area, select, checkbox, radio", "Not on the captured routes."),
    ("Switch", "The pricing Monthly/Annual control is in [pricing-light-default](screenshots/pricing-light-default.png). It was not flipped, so its states are not in the tables."),
    ("Tabs", "Docs tabs are in [docs-light-default](screenshots/docs-light-default.png). Not toggled."),
    ("Tooltip, toast", "Not opened."),
    ("Dialog", "The login card is a dialog over the product. [login-light-default](screenshots/login-light-default.png)."),
    ("Table, avatar, list row", "Not on these routes."),
    ("Badge", "The Ditto New chip is in the product menu shot. Not cropped on its own."),
    ("Empty, loading, error, destructive confirmation", "Login was not submitted, so no error. Not on the public routes."),
    ("Disabled, loading, selected", "Not shown."),
]
lines += ["## Gaps", "", "| Checklist item | Status |", "|---|---|"]
lines += [f"| {item} | {status} |" for item, status in GAPS]
lines.append("")

TEXT = "\n".join(lines) + "\n"

if __name__ == "__main__":
    (ROOT / "components.md").write_text(TEXT)
    print("components", len(C))
