#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/components-computed.json.

The Org's public site declares a real custom-property layer (primary, neutral,
fg, bg, type, spacing). Those values are Measured. Component colours that are
not a declared variable are also Measured, from computed styles. The public
site paints one light theme. Dark is not emitted as a theme.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())["components"]
RES = V["resolved"]["light"]


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    raise ValueError("not a colour: " + v)


def css_color(name):
    item = RES[name]
    return norm_color(item.get("value") or item["raw"])


def css_dim(name):
    item = RES[name]
    val = item.get("value") or item["raw"]
    if not re.fullmatch(r"-?\d+(\.\d+)?px", val):
        raise ValueError(f"{name} is not a px length: {val}")
    return val


def token(value, ty, source, description=""):
    t = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    if description:
        t["$description"] = description
    return t


def color_var(name, description=""):
    return token(css_color(name), "color", f"css-var {name} resolved on https://theorg.com/ (light)", description)


def dim_var(name, description=""):
    return token(css_dim(name), "dimension", f"css-var {name} resolved on https://theorg.com/ (light)", description)


def measured_color(comp, state, prop="backgroundColor"):
    style = C[comp]["states"][state]["style"]
    return token(norm_color(style[prop]), "color", f"computed {prop} of {comp} {state} (raw/components-computed.json)")


def measured_dim(comp, state, prop):
    style = C[comp]["states"][state]["style"]
    val = style[prop]
    if prop == "height" and not re.fullmatch(r"-?\d+(\.\d+)?px", val):
        val = str(C[comp]["states"][state]["rect"]["h"]) + "px"
    if not re.fullmatch(r"-?\d+(\.\d+)?px", val):
        # keep one decimal from a computed px string
        m = re.fullmatch(r"(-?\d+(?:\.\d+)?)px", val)
        if not m:
            raise ValueError(f"{comp} {prop} {val}")
        val = ("%g" % round(float(m.group(1)), 2)) + "px"
    else:
        val = ("%g" % round(float(val[:-2]), 2)) + "px"
    return token(val, "dimension", f"computed {prop} of {comp} {state} (raw/components-computed.json)")


core = {
    "color": {
        "brand": color_var("--brand", "Navy brand ink."),
        "primary": {
            "10": color_var("--primary-10"),
            "20": color_var("--primary-20"),
            "40": color_var("--primary-40"),
            "100": color_var("--primary-100", "Declared link blue."),
            "100-hover": color_var("--primary-100-hover"),
        },
        "neutral": {k: color_var(f"--neutral-{k}") for k in ("0", "10", "20", "30", "40", "60", "70", "80", "90", "100")},
        "fg": {k: color_var(f"--fg-fg{k}") for k in ("1", "2", "3", "4", "5")},
        "bg": {k: color_var(f"--bg-bg{k}") for k in ("1", "2", "3", "4", "5", "6")},
        "status": {
            "success": color_var("--success"),
            "warning": color_var("--warning"),
            "error": color_var("--error"),
            "accent": color_var("--accent-100", "Pale teal accent declared beside the landing colours."),
        },
    },
    "font": {
        "family": {
            "primary": token(RES["--font-primary"]["value"], "fontFamily", "css-var --font-primary"),
            "secondary": token(RES["--font-secondary"]["value"], "fontFamily", "css-var --font-secondary"),
        },
        "size": {k.replace("--fs-", "fs-"): dim_var(k) for k in sorted(RES) if k.startswith("--fs-")},
        "line-height": {
            "tight": token(1, "number", "css-var --lh-1"),
            "snug": token(1.25, "number", "css-var --lh-2"),
            "body": token(1.5, "number", "css-var --lh-3"),
        },
    },
    "spacing": {k.replace("--sp-", "sp-"): dim_var(k) for k in sorted(RES) if k.startswith("--sp-")},
    "radius": {
        "icon": dim_var("--icon-radius"),
        "card": dim_var("--border-radius"),
        "popover": dim_var("--popover-rounding"),
    },
    "layout": {
        "content": dim_var("--max-content-width"),
        "compact": dim_var("--max-width-compact"),
        "screen-xs": dim_var("--screen-xs-min"),
        "screen-sm": dim_var("--screen-sm-min"),
        "screen-md": dim_var("--screen-md-min"),
        "screen-lg": dim_var("--screen-lg-min"),
        "icon": dim_var("--icon-size"),
    },
    "motion": {
        "card-hover": token("80ms", "duration", "css-var --transition-card-hover-duration"),
        "ease-out": token([0.19, 1, 0.22, 1], "cubicBezier", "css-var --transition-01"),
        "ease-enter": token([0.075, 0.82, 0.165, 1], "cubicBezier", "css-var --transition-timing-function"),
    },
}

light = {
    "page": color_var("--background", "Page background."),
    "surface": color_var("--bg-bg1", "Card and menu surface."),
    "surface-muted": color_var("--bg-bg2"),
    "text": color_var("--fg-fg1"),
    "muted": color_var("--fg-fg2"),
    "disabled": color_var("--fg-fg3"),
    "accent": measured_color("nav-signup", "default", "backgroundColor"),
    "accent-hover": measured_color("nav-signup", "hover", "backgroundColor"),
    "accent-pressed": measured_color("nav-signup", "pressed", "backgroundColor"),
    "on-accent": measured_color("nav-signup", "default", "color"),
    "ink": measured_color("hero-cta", "default", "backgroundColor"),
    "link": color_var("--primary-100"),
    "border": color_var("--neutral-20"),
    "success": color_var("--success"),
    "warning": color_var("--warning"),
    "danger": color_var("--error"),
    "info": token("Not captured", "color", "Not captured. --info-bg and --info-text resolve empty on the public home page."),
    "focus": token("Not captured", "color", "Not captured. Keyboard focus on the measured controls did not paint a distinct outline colour."),
    "component": {
        "signup": {
            "height": measured_dim("nav-signup", "default", "height"),
            "radius": token("999px", "dimension", "computed borderRadius of nav-signup default is a pill; recorded as 999px because the computed string is a percentage-like pill radius"),
        },
        "hero-cta": {
            "height": measured_dim("hero-cta", "default", "height"),
        },
        "search": {
            "height": measured_dim("search-field", "default", "height"),
        },
    },
}

# Pill radius: read the real computed value if it is a px length, else leave a note.
radius = C["nav-signup"]["states"]["default"]["style"].get("borderRadius", "")
if re.fullmatch(r"\d+(\.\d+)?px", radius):
    light["component"]["signup"]["radius"] = token(radius, "dimension", "computed borderRadius of nav-signup default")
else:
    # A fully rounded control. DTCG dimension must be one px or rem length.
    # Half the measured height is the pill radius.
    h = C["nav-signup"]["states"]["default"]["rect"]["h"]
    light["component"]["signup"]["radius"] = token(
        ("%g" % round(h / 2, 2)) + "px",
        "dimension",
        f"Derived from measured height {h}px / 2; computed borderRadius was {radius!r}",
    )

# Drop Not captured colour tokens: DTCG color type cannot hold that string.
# Record them under $extensions instead.
not_captured = {
    "info": light.pop("info"),
    "focus": light.pop("focus"),
}

doc = {
    "$description": "The Org public site, captured 2026-11-21 from https://theorg.com/. One light theme.",
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    "$extensions": {
        "notCaptured": {
            "info": "Status info colours (--info-bg, --info-text, --info-border) are declared empty on the public home page.",
            "focus": "Focus-visible on the measured nav and hero controls did not change outline colour. Not captured.",
            "dark": "No dark theme control on the public site. A dark class probe resolved the same custom properties.",
            "pressed-hold": "Pressed colours on buttons were forced with CDP :active, not a held pointer.",
        },
        "sources": not_captured,
    },
}

# Validate colours and dimensions.
def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        ty = node["$type"]
        val = node["$value"]
        if ty == "color":
            norm_color(val)
        if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(val)):
            raise SystemExit(f"bad dimension {path}: {val}")
        if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
            raise SystemExit(f"bad duration {path}: {val}")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, path + "." + k)

walk(doc)
(HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
print("wrote tokens.json")
