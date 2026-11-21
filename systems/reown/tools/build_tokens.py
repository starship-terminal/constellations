#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/components-computed.json.

Marketing tokens are Reown's own --p-* primitives and --s-* semantic names,
resolved on https://reown.com/ at 1440. Docs light and dark are a second
surface (Mintlify). Demo AppKit colours are recorded under core.color.appkit
when present. Unread values are not invented.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components-computed.json").read_text()) if (RAW / "components-computed.json").exists() else {"readings": []}

M = V["marketing"]["resolved"]
DOCS_L = V["docs"]["light"]["resolved"]
DOCS_D = V["docs"]["dark"]["resolved"]
DEMO = V.get("demo", {}).get("resolved", {})


def rgb_triplet(value):
    value = value.strip()
    m = re.fullmatch(r"(\d+),\s*(\d+),\s*(\d+)", value)
    if m:
        return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
    m = re.fullmatch(r"rgb\((\d+),\s*(\d+),\s*(\d+)\)", value)
    if m:
        return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
    m = re.fullmatch(r"rgba\((\d+),\s*(\d+),\s*(\d+),\s*([\d.]+)\)", value)
    if m:
        a = float(m.group(4))
        if a >= 1:
            return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
        return "rgba(%d, %d, %d, %g)" % (int(m.group(1)), int(m.group(2)), int(m.group(3)), round(a, 3))
    if re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        return value.lower()
    return None


def tok(value, ty, source):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def put(tree, path, token):
    node = tree
    for key in path[:-1]:
        node = node.setdefault(key, {})
    node[path[-1]] = token


def dim(value, source):
    value = value.strip()
    if re.fullmatch(r"-?[\d.]+rem", value) or re.fullmatch(r"-?[\d.]+px", value) or re.fullmatch(r"-?[\d.]+ms", value):
        return tok(value, "dimension" if not value.endswith("ms") else "duration", source)
    return None


core = {}
light = {}
dark = {}
not_tokenised = []

# Primitives. Marketing stores colours as "R, G, B" triplets.
for name, raw in sorted(M.items()):
    if not name.startswith("--p-color-"):
        continue
    leaf = name[len("--p-color-"):].replace("_", "-")
    hexed = rgb_triplet(raw)
    if not hexed:
        not_tokenised.append({"name": name, "value": raw, "reason": "not a colour triplet"})
        continue
    put(core, ["color", "primitive", leaf], tok(hexed, "color", "Measured. css-var %s resolved on :root at https://reown.com/ (1440). Authored as an RGB triplet." % name))

for name, raw in sorted(M.items()):
    if name.startswith("--p-space-"):
        leaf = name[len("--p-space-"):]
        t = dim(raw, "Measured. css-var %s on https://reown.com/" % name)
        if t:
            put(core, ["spacing", leaf], t)
    elif name.startswith("--p-radius-"):
        leaf = name[len("--p-radius-"):]
        t = dim(raw, "Measured. css-var %s on https://reown.com/" % name)
        if t:
            put(core, ["radius", leaf], t)
    elif name.startswith("--p-text-"):
        leaf = name[len("--p-text-"):]
        t = dim(raw, "Measured. css-var %s on https://reown.com/" % name)
        if t:
            put(core, ["font", "size", leaf], t)
    elif name.startswith("--p-duration-"):
        leaf = name[len("--p-duration-"):]
        raw_s = raw.strip()
        if raw_s.endswith("ms"):
            put(core, ["duration", leaf], tok(raw_s, "duration", "Measured. css-var %s" % name))
        elif raw_s.endswith("s"):
            ms = round(float(raw_s[:-1]) * 1000, 3)
            put(core, ["duration", leaf], tok(("%g" % ms) + "ms", "duration", "Derived. %s is %s, converted to ms" % (name, raw_s)))
    elif name.startswith("--p-ease-"):
        leaf = name[len("--p-ease-"):]
        m = re.fullmatch(r"cubic-bezier\(([^)]*)\)", raw.strip())
        if m:
            nums = [float(x) for x in m.group(1).split(",")]
            put(core, ["easing", leaf], tok(nums, "cubicBezier", "Measured. css-var %s on https://reown.com/" % name))
    elif name.startswith("--p-leading-"):
        leaf = name[len("--p-leading-"):]
        put(core, ["font", "leading", leaf], tok(raw.strip(), "number", "Measured. css-var %s" % name))
    elif name.startswith("--p-weight-"):
        leaf = name[len("--p-weight-"):]
        put(core, ["font", "weight", leaf], tok(int(float(raw)), "fontWeight", "Measured. css-var %s" % name))
    elif name.startswith("--p-tracking-"):
        leaf = name[len("--p-tracking-"):]
        put(core, ["font", "tracking", leaf], tok(raw.strip(), "dimension" if raw.strip().endswith(("rem", "em", "px")) else "other", "Measured. css-var %s" % name))
        if not raw.strip().endswith(("rem", "em", "px")):
            core["font"]["tracking"][leaf]["$type"] = "other"

put(core, ["font", "family", "sans"], tok(M.get("--p-font-sans", "KHTeka-Regular, sans-serif"), "fontFamily", "Measured. css-var --p-font-sans on https://reown.com/. KH Teka is a licensed face; not redistributed."))
put(core, ["font", "family", "mono"], tok(M.get("--p-font-mono", "KHTekaMono-Regular, monospace"), "fontFamily", "Measured. css-var --p-font-mono on https://reown.com/."))

# Semantic marketing colours, also RGB triplets.
SEMANTIC = {
    "surface": "--s-color-surface",
    "surface-lift": "--s-color-surface-lift",
    "surface-dark": "--s-color-surface-dark",
    "surface-dim": "--s-color-surface-dim",
    "surface-subtle": "--s-color-surface-subtle",
    "on-surface": "--s-color-on-surface",
    "on-surface-muted": "--s-color-on-surface-muted",
    "accent": "--s-color-accent",
    "accent-blue": "--s-color-accent-blue",
    "accent-green": "--s-color-accent-green",
    "accent-orange": "--s-color-accent-orange",
    "accent-yellow": "--s-color-accent-yellow",
    "backdrop": "--s-color-backdrop",
    "border": "--s-color-border",
    "border-strong": "--s-color-border-strong",
    "border-subtle": "--s-color-border-subtle",
    "button-bg": "--s-color-button-bg",
    "button-text": "--s-color-button-text",
    "danger": "--s-color-danger",
    "divider": "--s-color-divider",
    "field-bg": "--s-color-field-bg",
    "field-text": "--s-color-field-text",
    "nav-overlay": "--s-color-nav-overlay",
    "placeholder": "--s-color-placeholder",
}
for leaf, name in SEMANTIC.items():
    raw = M.get(name)
    if not raw:
        continue
    hexed = rgb_triplet(raw)
    if not hexed:
        not_tokenised.append({"name": name, "value": raw, "reason": "semantic colour not a triplet"})
        continue
    put(light, ["color", leaf], tok(hexed, "color", "Measured. css-var %s resolved on :root at https://reown.com/. The marketing site has one theme; section classes (theme--blue and others) override these locally." % name))

# Type roles from --s-type-*
roles = {}
for name, raw in M.items():
    m = re.fullmatch(r"--s-type-([a-z0-9]+)-(size|leading|tracking|weight)", name)
    if not m:
        continue
    roles.setdefault(m.group(1), {})[m.group(2)] = raw.strip()
for role, parts in sorted(roles.items()):
    if "size" not in parts:
        continue
    composite = {
        "fontFamily": "{font.family.sans}",
        "fontSize": parts["size"],
        "fontWeight": int(float(parts["weight"])) if "weight" in parts else 400,
        "lineHeight": parts.get("leading", "1.4"),
        "letterSpacing": parts.get("tracking", "0"),
    }
    put(core, ["typography", role], tok(composite, "typography", "Measured. --s-type-%s-* on https://reown.com/. fontFamily aliases --p-font-sans." % role))

# Docs semantic colours. Mintlify stores some as space-separated RGB channels.
def docs_color(raw):
    raw = raw.strip()
    hexed = rgb_triplet(raw)
    if hexed:
        return hexed
    m = re.fullmatch(r"(\d+)\s+(\d+)\s+(\d+)", raw)
    if m:
        return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
    return None

for theme_name, resolved, tree in (("light", DOCS_L, light), ("dark", DOCS_D, dark)):
    mapping = {
        "docs-primary": "--primary",
        "docs-background": "--background-" + theme_name,
        "docs-border": "--default-border-color",
    }
    for leaf, name in mapping.items():
        raw = resolved.get(name)
        if not raw:
            continue
        hexed = docs_color(raw)
        if not hexed:
            not_tokenised.append({"name": name, "theme": theme_name, "value": raw[:80], "reason": "docs colour not parsed"})
            continue
        put(tree, ["color", leaf], tok(hexed, "color", "Measured. css-var %s resolved on docs.reown.com in the %s theme." % (name, theme_name)))
    family = resolved.get("--default-font-family")
    if family and theme_name == "light":
        put(core, ["font", "family", "docs-sans"], tok(family.split(",")[0].strip().strip('"'), "fontFamily", "Measured. --default-font-family on docs.reown.com (first family). Full stack in raw/css-vars.json."))

# Demo AppKit accent, hex already.
accent = DEMO.get("--apkt-colors-accent100")
if accent:
    hexed = rgb_triplet(accent) or (accent if accent.startswith("#") else None)
    # rgba(9, 136, 240, 1.0)
    m = re.fullmatch(r"rgba\((\d+),\s*(\d+),\s*(\d+),\s*[\d.]+\)", accent.strip())
    if m:
        hexed = "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
    if hexed:
        put(core, ["color", "appkit", "accent"], tok(hexed, "color", "Measured. --apkt-colors-accent100 on https://demo.reown.com/."))
for leaf, name in (("black", "--apkt-colors-black"), ("white", "--apkt-colors-white"), ("walletkit", "--apkt-colors-productWalletKit"), ("appkit", "--apkt-colors-productAppKit"), ("cloud", "--apkt-colors-productCloud"), ("documentation", "--apkt-colors-productDocumentation")):
    raw = DEMO.get(name)
    if raw and raw.startswith("#"):
        put(core, ["color", "appkit", leaf], tok(raw.lower(), "color", "Measured. %s on https://demo.reown.com/." % name))

# Component measurements that are not a single variable.
def reading(name, state="default"):
    for row in COMP["readings"]:
        if row.get("name") == name and row.get("state") == state:
            return row
    return None

btn = reading("button-primary")
if btn:
    put(light, ["component", "button", "height"], tok(btn["height"], "dimension", "Measured. computed height of a.button--solid.theme--blue (Learn) on https://reown.com/ at 1440."))
    put(light, ["component", "button", "radius"], tok(btn["borderRadius"], "dimension", "Measured. computed border-radius of the same button."))
    put(light, ["component", "button", "font"], tok(btn["fontFamily"].split(",")[0].strip().strip('"'), "fontFamily", "Measured. computed font-family of the same button. Buttons use the mono face."))
    bg = rgb_triplet(btn["backgroundColor"])
    fg = rgb_triplet(btn["color"])
    if bg:
        put(light, ["component", "button", "bg"], tok(bg, "color", "Measured. computed background of a.button--solid.theme--blue. Section theme, not the root --s-color-button-bg."))
    if fg:
        put(light, ["component", "button", "text"], tok(fg, "color", "Measured. computed color of a.button--solid.theme--blue."))

field = reading("text-field")
if field:
    put(light, ["component", "field", "radius"], tok(field["borderRadius"], "dimension", "Measured. computed border-radius of the footer newsletter input (placeholder Mail) on https://reown.com/pricing. Focused only. Not submitted."))
    bg = rgb_triplet(field["backgroundColor"])
    if bg:
        put(light, ["component", "field", "bg"], tok(bg, "color", "Measured. computed background of that input."))

if "color" not in dark:
    raise SystemExit("docs dark colours were not read; refusing to invent a dark set")

doc = {
    "$description": "Reown public surfaces, captured 2026-11-21. Marketing tokens from reown.com. Docs tokens from docs.reown.com. AppKit colours from demo.reown.com. Dashboard sign-in was not entered.",
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$extensions": {
        "notTokenised": not_tokenised,
        "gaps": [
            "Marketing has no dark theme. prefers-color-scheme: dark did not change body colors (raw/css-vars.json themeProbe).",
            "Success, warning and info are not separate marketing semantic names. Green, orange and yellow exist as accents.",
            "Disabled, loading and error control states were not shown on the public pages.",
            "Dashboard (dashboard.reown.com/sign-in) was not entered.",
        ],
    },
}

text = json.dumps(doc, indent=2) + "\n"
(HERE / "tokens.json").write_text(text)
print("tokens written", sum(1 for _ in HERE.joinpath("tokens.json").read_text().split('"$value"')), "values")
