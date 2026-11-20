#!/usr/bin/env python3
"""Build tokens.json from Loom's public capture.

Loom marketing declares the Lens scale on the html style attribute
(--lns-color-*, --lns-themeLight-*, --lns-themeDark-*, type, space, radius,
shadow). The live pages paint light. Dark tokens are declared and were not
painted: adding class dark did not rebind --lns-color-*. They are a dark set
labelled as declared, not as a captured theme.

hsla() literals are converted to sRGB hex. That conversion is Derived. A
computed style that matches the hex is named in the source. calc() sizes are
resolved from --lns-unit (0.5rem = 8px at the measured 16px root).
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))
import motion as motion_mod

VARS = json.loads((RAW / "css-vars.json").read_text())
HOME = VARS["pages"]["/"]
INLINE = HOME["inline"]
RESOLVED = HOME["resolved"]
MOTION = json.loads((RAW / "motion.json").read_text()) if (RAW / "motion.json").exists() else None
COMP = json.loads((RAW / "components-computed.json").read_text())["components"]

DATE = "2026-11-18"
M = f"Declared on html style, loom.com, {DATE}, light, 1440"
C = f"Measured computed style, public Loom pages, {DATE}, light, 1440"
D = "Derived: hsla() or calc() on the declared token, resolved at a 16px root"


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def shadow(value, source):
    return {"$value": value, "$type": "shadow", "$extensions": {"source": source}}


def hsla_to_css(s):
    m = re.fullmatch(
        r"hsla?\(\s*([\d.]+)\s*,\s*([\d.]+)%\s*,\s*([\d.]+)%\s*(?:,\s*([\d.]+)\s*)?\)",
        str(s).strip(),
    )
    if not m:
        return None
    import colorsys
    h, sat, light, a = float(m.group(1)), float(m.group(2)) / 100, float(m.group(3)) / 100, float(m.group(4) or 1)
    r, g, b = colorsys.hls_to_rgb(h / 360, light, sat)
    rgb = tuple(round(x * 255) for x in (r, g, b))
    if a >= 0.999:
        return "#%02x%02x%02x" % rgb
    return "rgba(%d, %d, %d, %g)" % (rgb[0], rgb[1], rgb[2], round(a, 3))


def raw_color(name):
    raw = (INLINE.get(name) or RESOLVED.get(name) or "").strip()
    if not raw:
        raise SystemExit("missing " + name)
    if raw.startswith("var("):
        inner = re.search(r"hsla?\([^)]+\)", raw)
        if inner:
            return inner.group(0), raw
    return raw, raw


def declared_color(name, note=""):
    literal, raw = raw_color(name)
    css = hsla_to_css(literal)
    if not css:
        raise SystemExit("not hsla: %s = %r" % (name, raw))
    src = f"{D}. {M}: {name} = {raw}."
    if note:
        src += " " + note
    return color(css, src)


def declared(name):
    """A declared --lns-* value from the html style attribute. Raises when it is missing."""
    raw = (INLINE.get(name) or RESOLVED.get(name) or "").strip()
    if not raw:
        raise SystemExit("missing " + name)
    return raw


def decl_num(name):
    raw = declared(name)
    n = float(raw)
    return int(n) if n == int(n) else n


def decl_len(name):
    raw = declared(name)
    if raw == "0":
        return "0px"
    if not re.fullmatch(r"-?[\d.]+px", raw):
        raise SystemExit("not a px length: %s = %r" % (name, raw))
    return raw


def measured(key, prop, state="default"):
    """A computed style of a measured component. Raises when the reading is missing."""
    try:
        v = COMP[key]["states"][state]["style"][prop]
    except KeyError:
        raise SystemExit("no reading for %s %s %s in raw/components-computed.json" % (key, state, prop))
    if v in (None, "", "auto"):
        raise SystemExit("no usable reading for %s %s %s: %r" % (key, state, prop, v))
    return v


def measured_px(key, prop, state="default"):
    v = measured(key, prop, state)
    m = re.fullmatch(r"(-?[\d.]+)px", v)
    if not m:
        raise SystemExit("not px: %s %s = %r" % (key, prop, v))
    return "%gpx" % round(float(m.group(1)), 3)


HAND = "Reconstruction: entered by hand at capture time; no raw reading holds this value"


def unit_px():
    # --lns-unit is 0.5rem; body font-size measured 16px
    if declared("--lns-unit") != "0.5rem":
        raise SystemExit("--lns-unit is no longer 0.5rem")
    return 8


def calc_len(term):
    """One shadow length: 0, Npx, or calc(N * 0.5rem) / calc(N * var(--lns-unit, 8px))."""
    if term == "0":
        return "0"
    if re.fullmatch(r"-?[\d.]+px", term):
        return term
    px = calc_px(term)
    if not px:
        raise SystemExit("shadow length not understood: %r" % term)
    return px


def declared_shadow(name):
    """--lns-shadow-* is one layer: x y blur colour, the lengths as calc() of --lns-unit."""
    raw = declared(name)
    parts = re.findall(r"calc\([^)]*\)\)?|hsla?\([^)]*\)|\S+", raw)
    *lengths, colour = parts
    css = hsla_to_css(colour)
    if not css or len(lengths) != 3:
        raise SystemExit("shadow not understood: %s = %r" % (name, raw))
    return " ".join(calc_len(t) for t in lengths) + " " + css


def calc_px(expr):
    text = str(expr).strip()
    m = re.fullmatch(r"calc\(([\d.]+)\s*\*\s*0\.5rem\)", text)
    if not m:
        m = re.fullmatch(r"calc\(([\d.]+)\s*\*\s*var\(--lns-unit,\s*8px\)\)", text)
    if not m:
        return None
    return "%gpx" % (float(m.group(1)) * unit_px())


def declared_dim(name, note=""):
    raw = (INLINE.get(name) or RESOLVED.get(name) or "").strip()
    px = calc_px(raw)
    if not px:
        if re.fullmatch(r"-?[\d.]+px", raw):
            px = raw
        else:
            raise SystemExit("not a length: %s = %r" % (name, raw))
    src = f"{D}. {M}: {name} = {raw}."
    if note:
        src += " " + note
    return dim(px, src)


PALETTE = [
    "red", "redDark", "blurpleLight", "blurpleMedium", "blurple", "blurpleDark", "blurpleStrong",
    "offWhite", "blueLight", "blue", "blueDark", "magentaLight", "magenta", "magentaDark",
    "orangeLight", "orange", "orangeDark", "tealLight", "teal", "tealDark",
    "yellowLight", "yellow", "yellowDark", "grey8", "grey7", "grey6", "grey5", "grey4", "grey3",
    "grey2", "grey1", "white",
]

core = {
    "color": {name: declared_color("--lns-color-" + name) for name in PALETTE},
    "font": {
        "family": {
            "display": font(
                measured("hero-title", "fontFamily"),
                f"{C}: hero-title (home h1) font-family. Charlie Display is proprietary and not shipped.",
            ),
            "text": font(
                measured("primary-cta", "fontFamily"),
                f"{C}: primary-cta font-family; body and buttons. Charlie Text is proprietary and not shipped.",
            ),
        },
        "weight": {
            "book": num(decl_num("--lns-fontWeight-book"), f"{M}: --lns-fontWeight-book", "fontWeight"),
            "regular": num(decl_num("--lns-fontWeight-regular"), f"{M}: --lns-fontWeight-regular", "fontWeight"),
            "medium": num(decl_num("--lns-fontWeight-medium"), f"{M}: --lns-fontWeight-medium", "fontWeight"),
            "bold": num(decl_num("--lns-fontWeight-bold"), f"{M}: --lns-fontWeight-bold. Computed h1 weight was {measured('hero-title', 'fontWeight')}.", "fontWeight"),
        },
        "size": {
            "small": declared_dim("--lns-fontSize-small", "Also --lns-fontSize-body-sm."),
            "body": declared_dim("--lns-fontSize-body-md", "Also --lns-fontSize-medium."),
            "large": declared_dim("--lns-fontSize-body-lg", "Also --lns-fontSize-large."),
            "heading-sm": declared_dim("--lns-fontSize-heading-sm"),
            "heading-md": declared_dim("--lns-fontSize-heading-md"),
            "heading-lg": declared_dim("--lns-fontSize-heading-lg"),
            "display": dim(measured_px("hero-title", "fontSize"), f"{C}: hero-title (home h1) font-size, rounded to 3 decimals. The declared heading-lg is 48px; the hero is larger than that step."),
        },
        "lineHeight": {
            "small": num(decl_num("--lns-lineHeight-small"), f"{M}: --lns-lineHeight-small"),
            "body": num(decl_num("--lns-lineHeight-body-md"), f"{M}: --lns-lineHeight-body-md"),
            "large": num(decl_num("--lns-lineHeight-body-lg"), f"{M}: --lns-lineHeight-body-lg"),
            "heading-sm": num(decl_num("--lns-lineHeight-heading-sm"), f"{M}: --lns-lineHeight-heading-sm"),
            "heading-md": num(decl_num("--lns-lineHeight-heading-md"), f"{M}: --lns-lineHeight-heading-md"),
            "heading-lg": num(decl_num("--lns-lineHeight-heading-lg"), f"{M}: --lns-lineHeight-heading-lg"),
            "display": dim(measured_px("hero-title", "lineHeight"), f"{C}: hero-title (home h1) line-height"),
        },
        "tracking": {
            "large": dim(decl_len("--lns-letterSpacing-body-lg"), f"{M}: --lns-letterSpacing-body-lg"),
            "heading-md": dim(decl_len("--lns-letterSpacing-heading-md"), f"{M}: --lns-letterSpacing-heading-md"),
            "heading-lg": dim(decl_len("--lns-letterSpacing-heading-lg"), f"{M}: --lns-letterSpacing-heading-lg"),
        },
    },
    "space": {
        "unit": dim("%dpx" % unit_px(), f"{D}. {M}: --lns-unit = {declared('--lns-unit')}, root font-size 16px."),
        "xsmall": declared_dim("--lns-space-xsmall"),
        "small": declared_dim("--lns-space-small"),
        "medium": declared_dim("--lns-space-medium"),
        "large": declared_dim("--lns-space-large"),
        "xlarge": declared_dim("--lns-space-xlarge"),
        "xxlarge": declared_dim("--lns-space-xxlarge"),
    },
    "radius": {
        "none": dim(decl_len("--lns-radius-none"), f"{M}: --lns-radius-none"),
        "50": declared_dim("--lns-radius-50"),
        "100": declared_dim("--lns-radius-100", "Also --lns-radius-medium."),
        "150": declared_dim("--lns-radius-150"),
        "175": declared_dim("--lns-radius-175", "Also --lns-formFieldRadius."),
        "200": declared_dim("--lns-radius-200", "Also --lns-radius-large."),
        "250": declared_dim("--lns-radius-250"),
        "300": declared_dim("--lns-radius-300", "Also --lns-radius-xlarge."),
        "full": declared_dim("--lns-radius-full", f"The painted CTA uses {measured('primary-cta', 'borderTopLeftRadius')}, which is the same pill."),
    },
    "shadow": {
        "small": shadow(declared_shadow("--lns-shadow-small"), f"{D}. {M}: --lns-shadow-small = {declared('--lns-shadow-small')}."),
        "medium": shadow(declared_shadow("--lns-shadow-medium"), f"{D}. {M}: --lns-shadow-medium = {declared('--lns-shadow-medium')}."),
        "large": shadow(declared_shadow("--lns-shadow-large"), f"{D}. {M}: --lns-shadow-large = {declared('--lns-shadow-large')}."),
    },
    "sizing": {
        "formFieldHeight": declared_dim("--lns-formFieldHeight"),
        "formFieldBorder": dim(decl_len("--lns-formFieldBorderWidth"), f"{M}: --lns-formFieldBorderWidth"),
        "formFieldBorderFocus": dim(decl_len("--lns-formFieldBorderWidthFocus"), f"{M}: --lns-formFieldBorderWidthFocus"),
        "ctaHeight": dim(measured_px("primary-cta", "height"), f"{C}: primary-cta height (Get Loom for free, header)"),
        "loginButtonHeight": dim(measured_px("sso-google", "height"), f"{C}: sso-google height (Log in with Google)"),
        "emailFieldHeight": dim(measured_px("email-field", "height"), f"{C}: email-field height (#email on /login). Taller than --lns-formFieldHeight (36px)."),
        "iconButton": dim(measured_px("copy-link", "height"), f"{C}: copy-link height (Copy link on the public share page)"),
    },
    "layout": {
        "desktop": dim("1440px", f"{HAND}; the desktop viewport the capture scripts request"),
        "phone": dim("390px", f"{HAND}; the phone viewport the capture scripts request (PNG is 780px at devicePixelRatio 2)"),
        "desktopHeight": dim("900px", f"{HAND}; the desktop viewport height the capture scripts request"),
        "phoneHeight": dim("844px", f"{HAND}; the phone viewport height the capture scripts request"),
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.display}",
                "fontSize": "{font.size.display}",
                "fontWeight": measured("hero-title", "fontWeight"),
                "lineHeight": "{font.lineHeight.display}",
            },
            "$extensions": {"source": f"{C}: hero-title (home h1)"},
        },
        "heading-lg": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.display}",
                "fontSize": "{font.size.heading-lg}",
                "fontWeight": "{font.weight.bold}",
                "lineHeight": declared("--lns-lineHeight-heading-lg"),
                "letterSpacing": "{font.tracking.heading-lg}",
            },
            "$extensions": {"source": f"{M}: --lns-fontSize-heading-lg and companions"},
        },
        "heading-md": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.display}",
                "fontSize": "{font.size.heading-md}",
                "fontWeight": "{font.weight.bold}",
                "lineHeight": declared("--lns-lineHeight-heading-md"),
                "letterSpacing": "{font.tracking.heading-md}",
            },
            "$extensions": {"source": f"{M}: --lns-fontSize-heading-md"},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.text}",
                "fontSize": "{font.size.body}",
                "fontWeight": "{font.weight.regular}",
                "lineHeight": declared("--lns-lineHeight-body-md"),
            },
            "$extensions": {"source": f"{M}: --lns-fontSize-body-md. Body computed size was 16px."},
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.text}",
                "fontSize": "{font.size.small}",
                "fontWeight": "{font.weight.medium}",
                "lineHeight": declared("--lns-lineHeight-small"),
            },
            "$extensions": {"source": f"{M}: --lns-fontSize-small. Nav CTA computed {measured('primary-cta', 'fontSize')}."},
        },
    },
}

LIGHT_ROLES = {
    "page": ("--lns-themeLight-color-background", f"{C}: marketing page paints white."),
    "surface": ("--lns-themeLight-color-overlay", f"{C}: login card and share pane sit on white."),
    "surfaceMuted": ("--lns-themeLight-color-backgroundSecondary", ""),
    "text": ("--lns-themeLight-color-body", f"{C}: body color rgb(41, 42, 46) matches grey8."),
    "textMuted": ("--lns-themeLight-color-bodyDimmed", ""),
    "textOnAccent": ("--lns-color-white", f"{C}: primary CTA color rgb(255, 255, 255)."),
    "accent": ("--lns-themeLight-color-primary", f"{C}: primary CTA background rgb(24, 104, 219) matches blurple."),
    "accentHover": ("--lns-themeLight-color-primaryHover", ""),
    "accentPressed": ("--lns-themeLight-color-primaryActive", ""),
    "border": ("--lns-themeLight-color-border", ""),
    "focus": ("--lns-themeLight-color-focusRing", ""),
    "record": ("--lns-themeLight-color-record", "Declared record orange. The record button itself sits behind sign-in."),
    "success": ("--lns-themeLight-color-success", ""),
    "warning": ("--lns-themeLight-color-warning", ""),
    "danger": ("--lns-themeLight-color-danger", ""),
    "info": ("--lns-themeLight-color-info", ""),
    "disabled": ("--lns-themeLight-color-disabledContent", f"{C}: Continue on an empty email is a disabled fill."),
    "scrim": ("--lns-themeLight-color-backdrop", ""),
    "fieldBorder": ("--lns-themeLight-color-formFieldBorder", f"{C}: #email border."),
    "fieldBackground": ("--lns-themeLight-color-formFieldBackground", ""),
}

DARK_ROLES = {
    "page": "--lns-themeDark-color-background",
    "surface": "--lns-themeDark-color-overlay",
    "surfaceMuted": "--lns-themeDark-color-backgroundSecondary",
    "text": "--lns-themeDark-color-body",
    "textMuted": "--lns-themeDark-color-bodyDimmed",
    "textOnAccent": "--lns-color-white",
    "accent": "--lns-themeDark-color-primary",
    "accentHover": "--lns-themeDark-color-primaryHover",
    "accentPressed": "--lns-themeDark-color-primaryActive",
    "border": "--lns-themeDark-color-border",
    "focus": "--lns-themeDark-color-focusRing",
    "record": "--lns-themeDark-color-record",
    "success": "--lns-themeDark-color-success",
    "warning": "--lns-themeDark-color-warning",
    "danger": "--lns-themeDark-color-danger",
    "info": "--lns-themeDark-color-info",
    "disabled": "--lns-themeDark-color-disabledContent",
    "scrim": "--lns-themeDark-color-backdrop",
    "fieldBorder": "--lns-themeDark-color-formFieldBorder",
    "fieldBackground": "--lns-themeDark-color-formFieldBackground",
}

light = {}
for role, (name, note) in LIGHT_ROLES.items():
    tok = declared_color(name, note)
    light[role] = tok

dark = {}
for role, name in DARK_ROLES.items():
    dark[role] = declared_color(
        name,
        "Declared --lns-themeDark token. Not painted on the captured pages. Adding class dark did not rebind --lns-color-*.",
    )

if MOTION:
    core["motion"], motion_extra = motion_mod.build(MOTION)
    if motion_extra:
        # Values DTCG cannot hold (linear()/steps() easings, transitions past the 60 kept), as the kit stores them.
        core["$extensions"] = {"notTokenised": motion_extra}

doc = {
    "$description": "Loom public signed-out capture, 2026-11-18. Lens tokens from html style. Dark set is declared, not painted.",
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "Dark (declared, not painted)", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
}

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out, "core groups", list(core), "light", len(light), "dark", len(dark))
