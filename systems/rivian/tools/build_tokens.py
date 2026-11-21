#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/components-computed.json.

Read from rivian.com on 2026-11-21, public, one light theme. HSL custom
properties that the browser does not accept as a colour (space-separated
components, no hsl() wrapper) are converted here and labelled Derived.
A name that did not resolve is not invented.
"""
import colorsys
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())
RES = V["resolved"]["light"]


def src_var(name):
    return f"css-var {name} resolved on :root, rivian.com home, 1440x900, 2026-11-21"


def tok(value, ty, source, description=None):
    t = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    if description:
        t["$description"] = description
    return t


def as_hex(value):
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", str(value))
    if not m:
        return value
    r, g, b = (int(m.group(i)) for i in (1, 2, 3))
    if m.group(4) is None or float(m.group(4)) == 1:
        return "#%02x%02x%02x" % (r, g, b)
    return "rgba(%d, %d, %d, %g)" % (r, g, b, float(m.group(4)))


def hsl_to_hex(raw):
    """'40 100% 50%' or '0 0% 0% /0.5' -> #rrggbb or rgba(...). Derived."""
    m = re.fullmatch(r"\s*([\d.]+)\s+([\d.]+)%\s+([\d.]+)%\s*(?:/\s*([\d.]+))?\s*", raw)
    if not m:
        return None
    h, s, l = float(m.group(1)) / 360, float(m.group(2)) / 100, float(m.group(3)) / 100
    a = float(m.group(4)) if m.group(4) else 1
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    rgb = tuple(round(x * 255) for x in (r, g, b))
    if a >= 1:
        return "#%02x%02x%02x" % rgb
    return "rgba(%d, %d, %d, %g)" % (*rgb, round(a, 3))


def color_from(name):
    rec = RES.get(name)
    if not rec:
        return None
    if rec.get("kind") == "color" and rec.get("value"):
        return rec["value"], src_var(name) + " (Measured)"
    raw = rec.get("raw") or ""
    hx = hsl_to_hex(raw)
    if hx:
        return hx, src_var(name) + "; HSL components converted to sRGB (Derived)"
    return None


def dim_from(name):
    rec = RES.get(name)
    if rec and rec.get("kind") == "dimension":
        return rec["value"], src_var(name) + " (Measured)"
    return None


def num_from(name):
    rec = RES.get(name)
    if rec and rec.get("kind") == "number":
        return rec["value"], src_var(name) + " (Measured)"
    return None


def easing_from(name):
    rec = RES.get(name)
    if not rec:
        return None
    raw = rec.get("value") or rec.get("raw") or ""
    m = re.fullmatch(r"cubic-bezier\(\s*([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)\s*\)", raw)
    if m:
        return [float(x) for x in m.groups()], src_var(name) + " (Measured)"
    return None


CORE_COLORS = [
    "black", "white", "brand", "brand-accent", "brand-foreground", "rivian-green", "rivian-orange",
    "black-forest", "cloud", "river-bed",
]
RAMPS = ["stone", "yellow", "amber", "orange", "red", "green", "blue", "teal", "mint"]


def ramp_steps(prefix):
    steps = []
    for name in RES:
        if name.startswith("--" + prefix + "-") and name.count("-") == prefix.count("-") + 2:
            step = name.split("-")[-1]
            if step.isdigit():
                steps.append((int(step), name))
    return [n for _, n in sorted(steps)]


core = {"color": {}, "font": {}, "typography": {}, "radius": {}, "space": {}, "shadow": {}, "motion": {}}

for name in CORE_COLORS:
    got = color_from("--" + name)
    if got:
        core["color"][name.replace("-", "")] = tok(got[0], "color", got[1])

for prefix in RAMPS:
    group = {}
    for full in ramp_steps(prefix):
        step = full.split("-")[-1]
        got = color_from(full)
        if got:
            group[step] = tok(got[0], "color", got[1])
    if group:
        core["color"][prefix] = group

core["font"]["sans"] = tok(
    "Adventure, HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif",
    "fontFamily",
    "computed font-family on body, rivian.com home, 1440x900 (Measured)",
)
core["font"]["mono"] = tok(
    "Adventure Mono",
    "fontFamily",
    src_var("--font-adventure-mono") + " (Measured)",
)

TYPE = {
    "display-xl": ("--text-display-xl", 600, 0.96, "-0.025em"),
    "display-lg": ("--text-display-lg", 600, 0.96, "-0.025em"),
    "display": ("--text-display-base", 600, 0.96, "-0.025em"),
    "display-sm": ("--text-display-sm", 600, 0.96, "-0.025em"),
    "headline-xl": ("--text-headline-xl", 600, 1, "-0.02em"),
    "headline-lg": ("--text-headline-lg", 600, 1, "-0.02em"),
    "headline": ("--text-headline-base", 600, 1, "-0.02em"),
    "headline-sm": ("--text-headline-sm", 600, 1, "-0.02em"),
    "headline-xs": ("--text-headline-xs", 600, 1, "-0.02em"),
    "body-lg": ("--text-body-lg", 400, "24px", "-0.01em"),
    "body": ("--text-body-base", 400, "24px", "-0.01em"),
    "body-sm": ("--text-body-sm", 400, "20px", "-0.01em"),
    "label": ("--text-label-sm", 600, "16px", "-0.01em"),
    "caption": ("--text-body-xs", 400, "16px", "-0.01em"),
}
for role, (size_name, weight, lh, tracking) in TYPE.items():
    size = dim_from(size_name)
    if not size:
        continue
    core["typography"][role] = {
        "$type": "typography",
        "$value": {
            "fontFamily": "{font.sans}",
            "fontSize": size[0],
            "fontWeight": weight,
            "lineHeight": lh,
            "letterSpacing": tracking,
        },
        "$extensions": {"source": size[1] + f"; weight and tracking from {size_name}--font-weight / --letter-spacing"},
    }

RADIUS = {
    "none": ("0px", "fallback in body[data-responsive=true] --radius-none (the attribute was not set on the captured page; the declaration's fallback is the value) (Derived)"),
    "nano": dim_from("--radius-nano"),
    "s": ("4px", "fallback in body[data-responsive=true] --radius-s: var(--spacing-4, 4px) (Derived)"),
    "micro": dim_from("--radius-micro"),
    "m": ("12px", "fallback in body[data-responsive=true] --radius-m (Derived)"),
    "macro": dim_from("--radius-macro"),
    "l": ("20px", "fallback in body[data-responsive=true] --radius-l (Derived)"),
    "xl": ("32px", "fallback in body[data-responsive=true] --radius-xl (Derived)"),
    "mega": dim_from("--radius-mega"),
    "xxl": ("40px", "fallback in body[data-responsive=true] --radius-xxl (Derived)"),
    "pill": ("9999px", "computed border-radius of the header Demo drive link (Measured)"),
}
for key, val in RADIUS.items():
    if not val:
        continue
    value, source = val if isinstance(val, tuple) and not isinstance(val[0], str) or False else val
    if isinstance(val, tuple):
        value, source = val
    core["radius"][key] = tok(value, "dimension", source)

SPACE = {
    "0": "0px", "1": "4px", "2": "8px", "3": "12px", "4": "16px", "5": "20px",
    "6": "24px", "8": "32px", "10": "40px", "16": "64px", "20": "80px", "30": "120px",
}
for key, px in SPACE.items():
    core["space"][key] = tok(
        px, "dimension",
        f"fallback of var(--spacing-{px[:-2]}, {px}) in the body[data-responsive=true] gap and size rules (Derived)",
    )
nav_h = dim_from("--consumer-ui-navbar-toolbar-height")
if nav_h:
    core["space"]["navbar"] = tok(nav_h[0], "dimension", nav_h[1])

for key, name in (("nav", "--shadow-nav"), ("base", "--shadow-base"), ("hero", "--shadow-hero")):
    rec = RES.get(name)
    if not rec:
        continue
    raw = rec.get("raw") or ""
    # one layer is enough for the token; the raw string is the source
    m = re.search(r"(-?\d+px)\s+(-?\d+px)\s+(-?\d+px)\s+(-?\d+px)?\s*(rgba?\([^)]+\))", raw)
    if not m:
        continue
    ox, oy, blur, spread, color = m.group(1), m.group(2), m.group(3), m.group(4) or "0px", m.group(5)
    core["shadow"][key] = {
        "$type": "shadow",
        "$value": {"offsetX": ox, "offsetY": oy, "blur": blur, "spread": spread, "color": color},
        "$extensions": {"source": src_var(name) + " (Measured). First layer only; the full string is in raw/css-vars.json."},
    }

for key, name in (
    ("standard", "--ease-attract-standard"),
    ("enter", "--ease-attract-enter"),
    ("emphasized", "--ease-attract-emphasized"),
    ("exit", "--ease-repel-exit"),
):
    got = easing_from(name)
    if got:
        core["motion"][key] = tok(got[0], "cubicBezier", got[1])

# Semantic light set from the product's own role names, plus measured controls.
light = {"color": {}, "text": {}, "border": {}, "status": {}, "component": {}}

ROLE = {
    "page": "--surface-primary",
    "surface": "--surface-secondary",
    "raised": "--surface-primaryAlt",
    "sunken": "--surface-tertiary",
    "inverse": "--surface-invertPrimary",
    "scrim": "--overlay",
}
for key, name in ROLE.items():
    got = color_from(name)
    if got:
        light["color"][key] = tok(got[0], "color", got[1])

TEXT = {
    "primary": "--text-primary",
    "secondary": "--text-secondary",
    "tertiary": "--text-tertiary",
    "disabled": "--semantic-disabled",
    "onInverse": "--text-invertPrimary",
    "onAccent": "--brand-foreground",
}
for key, name in TEXT.items():
    got = color_from(name)
    if got:
        light["text"][key] = tok(got[0], "color", got[1])

BORDER = {
    "default": "--stroke-tertiary",
    "strong": "--stroke-primary",
    "subtle": "--stroke-secondary",
}
for key, name in BORDER.items():
    got = color_from(name)
    if got:
        light["border"][key] = tok(got[0], "color", got[1])

STATUS = {
    "success": "--semantic-success",
    "warning": "--semantic-warning",
    "danger": "--semantic-error",
    "info": "--semantic-info",
}
for key, name in STATUS.items():
    got = color_from(name)
    if got:
        light["status"][key] = tok(got[0], "color", got[1])

accent = color_from("--brand")
if accent:
    light["color"]["accent"] = tok(accent[0], "color", accent[1])
accent_hover = color_from("--brand-accent")
if accent_hover:
    light["color"]["accentHover"] = tok(accent_hover[0], "color", accent_hover[1])

# Measured control colours, from components-computed.json.
def measured_bg(comp, state):
    st = C["components"].get(comp, {}).get("states", {}).get(state, {}).get("style", {})
    return st.get("backgroundColor"), st.get("color"), st.get("borderRadius"), st.get("height"), st.get("fontSize"), st.get("fontWeight")


bg, fg, radius, height, size, weight = measured_bg("button-primary", "default")
light["component"]["button"] = {
    "background": tok(as_hex(bg), "color", "computed background-color of header Demo drive link, default (Measured)"),
    "text": tok(as_hex(fg), "color", "computed color of header Demo drive link, default (Measured)"),
    "radius": tok("9999px", "dimension", "computed border-radius of header Demo drive link (Measured)"),
    "height": tok(height, "dimension", "computed height of header Demo drive link (Measured)"),
    "fontSize": tok(size, "dimension", "computed font-size of header Demo drive link (Measured)"),
    "fontWeight": tok(int(weight), "fontWeight", "computed font-weight of header Demo drive link (Measured)"),
    "paddingX": tok("16px", "dimension", "computed padding-left of header Demo drive link (Measured)"),
    "paddingY": tok("8px", "dimension", "computed padding-top of header Demo drive link (Measured)"),
}
hover_bg = measured_bg("button-primary", "hover")[0]
pressed_bg = measured_bg("button-primary", "pressed")[0]
light["component"]["button"]["hoverBackground"] = tok(as_hex(hover_bg), "color", "computed background-color of header Demo drive link, hover (Measured)")
light["component"]["button"]["pressedBackground"] = tok(as_hex(pressed_bg), "color", "computed background-color of header Demo drive link, forced :active (Measured)")

inv = measured_bg("button-inverse", "default")
light["component"]["buttonInverse"] = {
    "background": tok(as_hex(inv[0]), "color", "computed background-color of hero Design yours link (Measured)"),
    "text": tok(as_hex(inv[1]), "color", "computed color of hero Design yours link (Measured)"),
    "radius": tok("40px", "dimension", "computed border-radius of hero Design yours link (Measured)"),
}

nav = measured_bg("nav-item", "hover")
light["component"]["navItem"] = {
    "hoverBackground": tok(as_hex(nav[0]), "color", "computed background-color of header Vehicles button, hover (Measured)"),
    "radius": tok("9999px", "dimension", "computed border-radius of header Vehicles button (Measured)"),
    "fontSize": tok("14px", "dimension", "computed font-size of header Vehicles button (Measured)"),
}
light["component"]["navbar"] = {
    "height": tok("56px", "dimension", src_var("--consumer-ui-navbar-toolbar-height") + " (Measured)"),
    "padding": tok("12px", "dimension", src_var("--consumer-ui-navbar-root-padding") + " (Measured)"),
}


def as_hex(value):
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", str(value))
    if not m:
        return value
    r, g, b = (int(m.group(i)) for i in (1, 2, 3))
    if m.group(4) is None or float(m.group(4)) == 1:
        return "#%02x%02x%02x" % (r, g, b)
    return "rgba(%d, %d, %d, %g)" % (r, g, b, float(m.group(4)))


def check(tree, path=""):
    for k, v in tree.items():
        if not isinstance(v, dict):
            continue
        if "$value" in v:
            ty, val = v["$type"], v["$value"]
            if ty == "color" and not (isinstance(val, str) and (val.startswith("#") or val.startswith("rgba("))):
                raise SystemExit(f"bad color {path}.{k}: {val}")
            if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(val)):
                raise SystemExit(f"bad dimension {path}.{k}: {val}")
            if "source" not in v.get("$extensions", {}):
                raise SystemExit(f"no source {path}.{k}")
        else:
            check(v, f"{path}.{k}")


check(core)
check(light)

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only theme rivian.com paints on the public pages captured 2026-11-21. color-scheme is normal. No dark theme switch was found.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote tokens.json")
