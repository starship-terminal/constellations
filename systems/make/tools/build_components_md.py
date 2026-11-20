#!/usr/bin/env python3
"""Write components.md from the Make public measurements.

The kit's public builder expects a Gauth-shaped palette. This writer reads
raw/components-computed.json and names the token whose value matches.
"""
import json
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
for n, t in flat(T):
    if t.get("$type") == "color" and isinstance(t.get("$value"), str) and t["$value"].startswith("#"):
        BY.setdefault(t["$value"].lower(), n)


def parse(rgb):
    """(hex, alpha) for a computed colour, or None. Alpha is 1 for #rrggbb and rgb()."""
    if not isinstance(rgb, str):
        return None
    if rgb.startswith("#"):
        return rgb.lower(), 1.0
    if not rgb.startswith(("rgb(", "rgba(")):
        return None
    parts = rgb.replace("rgba(", "").replace("rgb(", "").replace(")", "").replace("/", ",").replace(" ", ",").split(",")
    parts = [x for x in parts if x]
    if len(parts) < 3:
        return None
    try:
        r, g, b = [int(float(x)) for x in parts[:3]]
        a = float(parts[3]) if len(parts) > 3 else 1.0
    except ValueError:
        return None
    return "#%02x%02x%02x" % (r, g, b), a


def colour(rgb):
    """A colour cell. A transparent fill says so, a translucent one keeps its rgba(); only an opaque
    colour is written as hex and named by the token that holds it."""
    p = parse(rgb)
    if not p:
        return cell(rgb or "")
    h, a = p
    if a == 0:
        return "transparent"
    if a < 1:
        return cell(rgb)
    tok = BY.get(h)
    return f"{h} `{tok}`" if tok else h


def cell(text):
    """A table cell: a pipe would split it and a newline would end the row."""
    return " ".join(str(text).split()).replace("|", "\\|")


lines = ["# Make components", "", "Measured on public pages, 2026-11-18, light, 1440. Nothing was submitted.", ""]
order = [
    "cta-primary", "cta-secondary", "nav-get-started", "signin-submit",
    "text-link", "display", "pricing-heading", "search-field", "email-field",
    "password-field", "template-card", "faq-summary",
]
for key in order:
    comp = C.get(key)
    if not comp:
        continue
    lines.append(f"## {comp.get('title', key)}")
    lines.append("")
    lines.append(cell(f"{comp.get('group', '')}. {comp.get('url', '')}"))
    lines.append("")
    if comp.get("missing"):
        lines.append("Not found on the page.")
        lines.append("")
        continue
    lines.append("| State | Size | Fill | Ink | Type | Via |")
    lines.append("|---|---|---|---|---|---|")
    for state, s in comp.get("states", {}).items():
        if s.get("skipped"):
            lines.append(f"| {cell(state)} | | | | | not captured: {cell(s['skipped'])} |")
            continue
        if s.get("error"):
            lines.append(f"| {cell(state)} | | | | | {cell(s['error'][:80])} |")
            continue
        st = s.get("style") or {}
        lines.append(
            f"| {state} | {s.get('rect', {}).get('w')}×{s.get('rect', {}).get('h')} | {colour(st.get('backgroundColor'))} | {colour(st.get('color'))} | {st.get('fontSize')} / {st.get('fontWeight')} | {cell(s.get('via', ''))} |"
        )
    crop = next((s.get("crop") for s in comp.get("states", {}).values() if s.get("crop")), None)
    if crop:
        lines.append("")
        lines.append(f"![{key}]({crop})")
    lines.append("")

lines.append("## Gaps")
lines.append("")
lines.append("- The scenario editor, dashboard and billing portal sit behind sign-in and were not entered.")
lines.append("- Register shows a CAPTCHA and was not submitted.")
lines.append("- Continue with Google and Continue with SSO start OAuth and were not pressed.")
lines.append("- Talk to sales and checkout were not submitted.")
lines.append("- Checkbox and radio were not painted as product controls on the captured pages. OneTrust checkboxes were hidden with the consent banner.")
lines.append("- Toast, tooltip, table, avatar, switch and tabs were not present on the captured public pages.")
lines.append("")
(ROOT / "components.md").write_text("\n".join(lines))
print("components", len(C))
