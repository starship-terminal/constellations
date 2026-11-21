#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

Column publishes one light theme. Palette and role names are custom properties
read from column.com on 2026-11-21. A name whose computed value is a colour,
length, or number becomes a token. Unresolved var() and animation leftovers
stay out. No dark set: the marketing site declares none.

Deterministic: same inputs, same bytes. Edit the raw file, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
RES = RAW["resolved"]["light"]

ROLE = {
    "page": "--color-0",
    "surface": "--color-gray-50",
    "surface-muted": "--bg-color-muted",
    "text": "--text-color-heading",
    "text-body": "--text-color-body",
    "muted": "--color-gray-500",
    "accent": "--color-blue-800",
    "accent-bright": "--color-blue-500",
    "on-accent": "--color-0",
    "border": "--color-gray-200",
    "link": "--text-color-heading",
    "focus": "--btn-focus-ring-primary",
    "field-focus": "--form-input-border-focus",
}


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{6})", v)
    if m:
        return "#" + m.group(1)
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", v)
    if not m:
        raise ValueError("not a colour: " + v)
    r, g, b, a = m.groups()
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def token_name(css_name):
    return css_name.lstrip("-").replace("-", ".")


def leaf(css_name, value, ty):
    return {
        "$type": ty,
        "$value": value,
        "$extensions": {"source": f"Measured css-var {css_name} on column.com :root, raw/css-vars.json resolved.light"},
    }


def add(tree, path, node):
    cur = tree
    parts = path.split(".")
    for p in parts[:-1]:
        cur = cur.setdefault(p, {})
    cur[parts[-1]] = node


core = {}
skipped = []
for name, rec in sorted(RES.items()):
    kind = rec.get("kind")
    if kind == "color" and "value" in rec:
        try:
            val = norm_color(rec["value"])
        except ValueError:
            skipped.append(name)
            continue
        add(core, "color." + token_name(name), leaf(name, val, "color"))
    elif kind == "dimension" and isinstance(rec.get("value"), str) and rec["value"].endswith("px"):
        if name.startswith("--text-"):
            add(core, "typography.size." + token_name(name), leaf(name, rec["value"], "dimension"))
        elif name.startswith("--space-") and not name.startswith("--space-n") and name != "--space-auto":
            add(core, "spacing." + token_name(name), leaf(name, rec["value"], "dimension"))
    elif kind == "number" and name.startswith("--font-"):
        add(core, "typography.weight." + token_name(name), leaf(name, int(rec["value"]) if float(rec["value"]).is_integer() else rec["value"], "fontWeight"))

# font families are strings, not DTCG fontFamily objects with a measured stack only
for name in ("--font-sans", "--font-mono", "--font-ui"):
    rec = RES.get(name)
    if rec and rec.get("raw"):
        add(core, "typography.family." + token_name(name), {
            "$type": "fontFamily",
            "$value": rec["raw"].split(",")[0].strip().strip('"'),
            "$extensions": {
                "source": f"Measured css-var {name} on column.com, raw/css-vars.json",
                "stack": rec["raw"][:180],
            },
        })

light = {}
for role, css_name in ROLE.items():
    rec = RES.get(css_name)
    if not rec or rec.get("kind") != "color":
        skipped.append("role:" + role)
        continue
    light[role] = leaf(css_name, norm_color(rec["value"]), "color")

# button recipe from declared role vars, resolved
for role, css_name in {
    "button-bg": "--btn-bg-primary",
    "button-bg-hover": "--btn-bg-primary-hover",
    "button-text": "--btn-text-color-primary",
    "button-bg-secondary": "--btn-bg-secondary",
    "button-text-secondary": "--btn-text-color-secondary",
}.items():
    rec = RES.get(css_name)
    if rec and rec.get("kind") == "color":
        light[role] = leaf(css_name, norm_color(rec["value"]), "color")

doc = {
    "$description": "Column public marketing tokens, read from column.com custom properties on 2026-11-21. One light theme. Signed-out. Dashboard behind the login wall was not measured.",
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}],
    "$extensions": {
        "notCaptured": [
            "Dark theme: marketing site declares no dark variant. docs.column.com has a Toggle theme control; its dark values were not read into this set.",
            "Status roles (success, warning, danger, info): no semantic status custom properties on the public marketing surface. Colour ramps exist and are in core.color.",
            "Radius scale: no shared radius custom properties resolved on :root. Component radii are measured per element in raw/components-computed.json.",
            "Motion: durations and easings were not read as tokens.",
            "Signed-in dashboard: stopped at the login wall. No email, password, or OAuth control was used.",
        ]
    },
}
(HERE / "tokens.json").write_text(json.dumps(doc, indent=1) + "\n")
print("core groups", list(core))
print("light roles", list(light))
print("skipped", len(skipped))
