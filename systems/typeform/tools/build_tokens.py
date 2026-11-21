#!/usr/bin/env python3
"""Build tokens.json from Typeform's public Webflow stylesheets.

Sources, read from www.typeform.com on 2026-11-21, signed out, 1440x900:
  raw/css-vars.json            every custom property the shared Webflow sheet
                               declares, resolved on a probe element
  raw/components-computed.json computed styles of public controls

The site paints one light theme. Semantic roles live in `light` and alias
`core` primitives. There is no dark set: no theme switch was found.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never
tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V["resolved"]["light"]


def raw(name):
    item = RES.get(name) or {}
    return (item.get("value") or item.get("raw") or "").strip()


def norm_color(v):
    v = v.strip().lower()
    if v == "transparent":
        return "rgba(0, 0, 0, 0)"
    if v == "white":
        return "#ffffff"
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % a))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return "#%02x%02x%02x" % (int(r), int(g), int(b)) if a == 1 else "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    raise ValueError("not a colour: " + v)


def color(name):
    return norm_color(raw(name))


def dim_rem(name):
    v = raw(name).strip()
    if v.startswith("."):
        v = "0" + v
    if not re.fullmatch(r"-?\d+(\.\d+)?rem", v):
        raise ValueError(f"{name}: not a rem length: {v!r}")
    return v


def token(value, ty, source):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def alias(path, source):
    return {"$value": "{" + path + "}", "$type": "color", "$extensions": {"source": source}}


# Primitive ramps declared as --_colour-primitives---primitives--<hue>--<step>
HUES = ("neutral", "purple", "lavender", "blue", "green", "red", "yellow")
core_color = {}
for hue in HUES:
    group = {}
    for step in ("25", "50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "1000"):
        name = f"--_colour-primitives---primitives--{hue}--{step}"
        if name not in RES:
            continue
        group[step] = token(color(name), "color", f"css-var {name}")
    core_color[hue] = group

# Brand purple used as eyebrow / highlight, declared beside the ramp.
for step, name in (("400", "--_colour-primitives---get-real--400"), ("700", "--_colour-primitives---get-real--700"), ("800", "--_colour-primitives---get-real--800")):
    if name in RES:
        core_color.setdefault("brand", {})[step] = token(color(name), "color", f"css-var {name}")

def space_group():
    out = {}
    prefix = "--_size-and-spacing---primitives--spacers--"
    for key, item in RES.items():
        if not key.startswith(prefix):
            continue
        step = key[len(prefix):]
        out[step] = token(dim_rem(key), "dimension", f"css-var {key}")
    return out


def radius_group():
    out = {}
    prefix = "--_size-and-spacing---tokens--corner-radius--"
    for key in RES:
        if not key.startswith(prefix):
            continue
        step = key[len(prefix):]
        out[step] = token(dim_rem(key), "dimension", f"css-var {key}")
    return out


def type_role(slug, size_var, lh_var, ls_var, font_var, weight):
    return token({
        "fontFamily": "{" + "font.family." + ("display" if "Tobias" in raw(font_var) else "sans") + "}",
        "fontSize": dim_rem(size_var) if raw(size_var).endswith("rem") or raw(size_var).startswith(".") else raw(size_var),
        "fontWeight": weight,
        "lineHeight": raw(lh_var),
        "letterSpacing": raw(ls_var) if raw(ls_var) not in ("0px", "0") else "0px",
    }, "typography", f"css-var {size_var}")


# Webflow stores the face name with the weight baked in ("Twklausanne 500").
# The numeric weight is not a separate computed font-weight (buttons read 400),
# so the role weight is Derived from the family token name.
ROLES = {
    "display": ("--_typography---heading-display-size", "--_typography---heading-display-line-height", "--_typography---heading-display-letter-spacing", "--_typography---heading-display-font", 400),
    "heading-1": ("--_typography---heading-one-size", "--_typography---heading-one-line-height", "--_typography---heading-one-letter-spacing", "--_typography---heading-one-font", 400),
    "heading-2": ("--_typography---heading-two-size", "--_typography---heading-two-line-height", "--_typography---heading-two-letter-spacing", "--_typography---heading-two-font", 400),
    "heading-3": ("--_typography---heading-three-size", "--_typography---heading-three-line-height", "--_typography---heading-three-letter-spacing", "--_typography---heading-three-font", 350),
    "heading-4": ("--_typography---heading-four-size", "--_typography---heading-four-line-height", "--_typography---heading-four-letter-spacing", "--_typography---heading-four-font", 400),
    "heading-5": ("--_typography---heading-five-size", "--_typography---heading-five-line-height", "--_typography---heading-five-letter-spacing", "--_typography---heading-five-font", 500),
    "heading-6": ("--_typography---heading-six-size", "--_typography---heading-six-line-height", "--_typography---heading-six-letter-spacing", "--_typography---heading-six-font", 500),
    "body-lg": ("--_typography---paragraph-lg-size", "--_typography---paragraph-lg-line-height", "--_typography---paragraph-lg-letter-spacing", "--_typography---paragraph-lg-font", 350),
    "body": ("--_typography---paragraph-md-size", "--_typography---paragraph-md-line-height", "--_typography---paragraph-md-letter-spacing", "--_typography---paragraph-md-font", 400),
    "body-sm": ("--_typography---paragraph-sm-size", "--_typography---paragraph-sm-line-height", "--_typography---paragraph-sm-letter-spacing", "--_typography---paragraph-sm-font", 400),
    "caption": ("--_typography---paragraph-xs-size", "--_typography---paragraph-xs-line-height", "--_typography---paragraph-xs-letter-spacing", "--_typography---paragraph-xs-font", 400),
    "label": ("--_typography---eyebrow-size", "--_typography---eyebrow-line-height", "--_typography---eyebrow-letter-spacing", "--_typography---eyebrow-font", 600),
    "action": ("--_typography---action-text-sm-size", "--_typography---action-text-sm-line-height", "--_typography---action-text-sm-letter-spacing", "--_typography---action-text-sm-font", 500),
}

typography = {}
for slug, spec in ROLES.items():
    size = raw(spec[0])
    if size.startswith("."):
        # dim_rem accepts a leading dot after normalisation inside the helper
        pass
    typography[slug] = type_role(slug, *spec)
    # fix fontSize that starts with a dot
    fs = typography[slug]["$value"]["fontSize"]
    if isinstance(fs, str) and fs.startswith("."):
        typography[slug]["$value"]["fontSize"] = "0" + fs
    typography[slug]["$extensions"]["source"] = f"css-var {spec[0]}; weight Derived from the family token name {raw(spec[3])}"

layout = {
    "content-large": token(dim_rem("--_size-and-spacing---max-width--large"), "dimension", "css-var --_size-and-spacing---max-width--large"),
    "content-medium": token(dim_rem("--_size-and-spacing---max-width--medium"), "dimension", "css-var --_size-and-spacing---max-width--medium"),
    "gutter": token(dim_rem("--_size-and-spacing---primitives--section-spacing--gutter"), "dimension", "css-var --_size-and-spacing---primitives--section-spacing--gutter"),
    "margin": token(dim_rem("--_size-and-spacing---primitives--section-spacing--margin"), "dimension", "css-var --_size-and-spacing---primitives--section-spacing--margin"),
    "section-small": token(dim_rem("--_size-and-spacing---primitives--section-spacing--section-padding-small"), "dimension", "css-var --_size-and-spacing---primitives--section-spacing--section-padding-small"),
    "section-medium": token(dim_rem("--_size-and-spacing---primitives--section-spacing--section-padding-medium"), "dimension", "css-var --_size-and-spacing---primitives--section-spacing--section-padding-medium"),
    "section-large": token(dim_rem("--_size-and-spacing---primitives--section-spacing--section-padding-large"), "dimension", "css-var --_size-and-spacing---primitives--section-spacing--section-padding-large"),
}

# Measured control geometry. These are computed styles, not declared tokens.
measured = {
    "button-height": token("40px", "dimension", "measured a.Sign up on https://www.typeform.com/ 1440x900, components-computed.json button-primary.default.height"),
    "button-radius": token("12px", "dimension", "measured a.Sign up border-radius, components-computed.json button-primary.default.borderRadius"),
    "button-padding-x": token("20px", "dimension", "measured a.Sign up padding-left, components-computed.json button-primary.default.paddingLeft"),
    "nav-item-height": token("88px", "dimension", "measured Platform trigger height, components-computed.json nav-platform.default.rect.h"),
    "menu-shadow": token([{
        "color": "rgba(0, 0, 0, 0.04)",
        "offsetX": "0px",
        "offsetY": "4px",
        "blur": "4px",
        "spread": "0px",
    }], "shadow", "measured #w-dropdown-list-0 box-shadow, components-computed.json nav-menu.default.boxShadow"),
    "hero-size": token("80px", "dimension", "measured homepage h2 font-size, components-computed.json hero-heading.default.fontSize"),
    "focus-outline-width": token("0px", "dimension", "measured Sign up keyboard focus outline width, components-computed.json button-primary.focus.outline (rgb(42, 34, 43) none 0px). Focus landed; no ring was painted."),
}

core = {
    "color": core_color,
    "font": {
        "family": {
            "sans": token("Twklausanne, Arial, sans-serif", "fontFamily", "css-var --_typography---paragraph-md-font (declared \"Twklausanne 400\"; weight suffix stripped, fallbacks kept)"),
            "display": token("Tobias, \"Times New Roman\", sans-serif", "fontFamily", "css-var --_typography---heading-display-font"),
            "mono": token("Apercu Mono, ui-monospace, monospace", "fontFamily", "Not captured as a computed stack; @font-face family Apercumonopro is in raw/css-vars.json fonts. The public UI samples did not paint a code face."),
        }
    },
    "typography": typography,
    "spacing": space_group(),
    "radius": radius_group(),
    "layout": layout,
    "measured": measured,
}

# Semantic light roles. Each aliases a primitive that resolves to the same hex
# the semantic custom property computed to.
light = {
    "page": alias("color.neutral.25", "css-var --tokens--surfaces--background-idle = #faf9fb, alias of color.neutral.25"),
    "surface": alias("color.neutral.25", "css-var --tokens--surfaces--foreground-idle computed white is a card fill; page ground is --tokens--surfaces--background-idle"),
    "raised": alias("color.neutral.50", "css-var --tokens--surfaces--background-hover = #f5f3f6"),
    "invert": alias("color.neutral.1000", "css-var --tokens--surfaces--invert-idle = #2a222b"),
    "text": {
        "primary": alias("color.neutral.1000", "css-var --tokens--text-colour--text-colour-primary = #2a222b"),
        "secondary": alias("color.neutral.700", "css-var --tokens--text-colour--text-colour-secondary = #655d67"),
        "on-accent": alias("color.neutral.25", "css-var --tokens--button--primary-text = #faf9fb"),
        "invert": alias("color.neutral.25", "css-var --tokens--text-colour--text-colour-invert = #faf9fb"),
        "highlight": alias("color.purple.700", "css-var --tokens--text-colour--text-colour-highlight = #9454ab"),
        "eyebrow": alias("color.purple.600", "css-var --tokens--text-colour--eyebrow-colour = #a25fba"),
    },
    "border": {
        "default": alias("color.neutral.200", "css-var --tokens--border--border-primary = #e5e1e5"),
        "strong": alias("color.neutral.1000", "css-var --tokens--button--secondary-border = #2a222b"),
    },
    "accent": {
        "default": alias("color.neutral.1000", "css-var --tokens--button--primary-bg-idle = #2a222b"),
        "hover": alias("color.neutral.800", "css-var --tokens--button--primary-bg-hover = #564b58"),
        "pressed": token("#3e3040", "color", "measured Contact sales hover background rgb(62, 48, 64), color.neutral.900. Pressed was not held; this is the hover reading."),
    },
    "button": {
        "secondary-bg": alias("color.neutral.25", "css-var --tokens--button--secondary-bg-idle = #faf9fb"),
        "secondary-hover": alias("color.neutral.100", "css-var --tokens--button--secondary-bg-hover = #eeecee"),
        "tertiary-hover": alias("color.purple.600", "css-var --tokens--button--tertiary-hover = #a25fba"),
    },
}

# Focus colour is Not captured: keyboard focus landed and outline computed to
# none. The width is core.measured.focus-outline-width. No colour token is invented.

doc = {
    "$description": "Typeform public marketing site, measured 2026-11-21 from www.typeform.com stylesheets and computed styles. One light theme. Signed-in product not captured.",
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    "$extensions": {
        "notTokenised": [
            "Dark theme: not present on the public marketing site.",
            "Focus ring colour: keyboard focus landed and outline computed to none.",
            "Motion durations and easings: not declared as custom properties in the harvested sheet.",
            "Pressed state of the primary button: not held. accent.pressed is the measured hover of Contact sales.",
            "Disabled, loading, error, checkbox, radio, switch, toast, table, avatar: not present on the captured public pages.",
            "Deleted Webflow variable aliases (names containing <deleted|) were ignored.",
        ]
    },
}

# Fix fontSize values that the helper stored with a leading dot before dim_rem.
def walk_fix(node):
    if isinstance(node, dict) and "$value" in node and node.get("$type") == "dimension":
        v = node["$value"]
        if isinstance(v, str) and v.startswith("."):
            node["$value"] = "0" + v
    elif isinstance(node, dict) and "$value" in node and node.get("$type") == "typography":
        fs = node["$value"].get("fontSize")
        if isinstance(fs, str) and fs.startswith("."):
            node["$value"]["fontSize"] = "0" + fs
        lh = node["$value"].get("lineHeight")
        if isinstance(lh, str) and lh.endswith("em"):
            pass
    elif isinstance(node, dict):
        for v in node.values():
            walk_fix(v)

walk_fix(doc)

# Validate dimensions and colours.
DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")

def check(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        ty, val = node["$type"], node["$value"]
        if isinstance(val, str) and val.startswith("{"):
            return
        if ty == "color":
            if val == "Not captured":
                raise SystemExit("colour token left as Not captured: " + path)
            norm_color(val)
        if ty == "dimension" and not DIM.fullmatch(str(val)):
            raise SystemExit(f"{path}: bad dimension {val!r}")
        if ty == "typography":
            if not DIM.fullmatch(val["fontSize"]):
                raise SystemExit(f"{path}: bad fontSize {val['fontSize']!r}")
        if "source" not in node.get("$extensions", {}):
            raise SystemExit("missing source " + path)
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            check(v, path + "." + k)

check(doc)
(HERE / "tokens.json").write_text(json.dumps(doc, indent=1) + "\n")
print("wrote tokens.json", "core colours", sum(len(g) for g in core_color.values()), "spacing", len(core["spacing"]), "radius", len(core["radius"]))
