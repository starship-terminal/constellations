#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the live readings.

Sources, read from https://wiza.co/ on 2026-11-19 in the T3 preview browser
(CSS viewport 1440x900 and 390x844, devicePixelRatio 2). The marketing site is
Webflow. Its stylesheet declares a real token layer on :root (154 custom
properties). Those declarations are in raw/css-vars.json. Component colours,
radii, padding and type that the page paints are in raw/components.json.

Wiza's public marketing site paints one theme. There is no theme control on
any signed-out surface, so there is a light set and no dark set. The login
app (wiza.co/auth/login) is a separate PrimeVue/Tailwind surface. Its values
are recorded under light.auth as measured app tokens, not as a second theme.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never
tokens.json.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))

V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components.json").read_text())

DECL = V["declared"]


def norm_color(v):
    v = v.strip().lower()
    if v in ("white",):
        return "#ffffff"
    if v in ("transparent",):
        return "#00000000"
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        # Translucent colours stay #rrggbbaa: tools/catalog.py and the contrast check read only hex.
        if len(h) == 8 and h[6:8] != "ff":
            return "#" + h
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        hexed = "#%02x%02x%02x" % (int(r), int(g), int(b))
        return hexed if a >= 1 else hexed + "%02x" % round(a * 255)
    raise ValueError("not a colour: " + v)


# One px or rem length. em tracking is relative to a font size, so it is not a dimension token.
DIM = re.compile(r"-?(\d+(\.\d+)?|\.\d+)(px|rem)")


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension must be one px or rem length, got {val!r}")
    if ty == "color" and not str(val).startswith("{") and not re.fullmatch(r"#[0-9a-f]{6}([0-9a-f]{2})?", str(val)):
        raise ValueError(f"{path}: colour {val!r} is not #rrggbb(aa)")
    if ty == "number" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: number {val!r}")
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")


def leaf(path, ty, val, source, description=None):
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty == "fontWeight" and isinstance(val, str) and val.isdigit():
        val = int(val)
    if ty == "number" and isinstance(val, str):
        val = float(val) if "." in val else int(val)
    check(path, ty, val)
    token = {"$value": val, "$type": ty, "$extensions": {"source": source}}
    if description:
        token["$description"] = description
    return token


def put(tree, path, token):
    node = tree
    parts = path.split(".")
    for part in parts[:-1]:
        node = node.setdefault(part, {})
    node[parts[-1]] = token


def css_name(token_name):
    return "--" + token_name.replace(".", "--")


# core: the declared scales. Fluid clamps stay in raw/css-vars.json because
# DTCG dimension tokens are a single length. The desktop computed length is
# recorded beside the step as a description, not as a second invented value.
CORE = {}

SWATCHES = {
    "brand.0": ("#f5f0ff", "--swatch--brand-0"),
    "brand.25": ("#e4d8fd", "--swatch--brand-25"),
    "brand.50": ("#9371f0", "--swatch--brand-50"),
    "brand.100": ("#7e43ff", "--swatch--brand-100"),
    "brand.200": ("#4c24a3", "--swatch--brand-200"),
    "brand.300": ("#361d6d", "--swatch--brand-300"),
    "brand.500": ("#26114a", "--swatch--brand-500"),
    "light.0": ("#ffffff", "--swatch--light-0"),
    "light.25": ("#f6f8fa", "--swatch--light-25"),
    "light.50": ("#eceff3", "--swatch--light-50"),
    "light.100": ("#dfe1e6", "--swatch--light-100"),
    "light.200": ("#c1c7cf", "--swatch--light-200"),
    "light.300": ("#a4abb8", "--swatch--light-300"),
    "light.400": ("#808897", "--swatch--light-400"),
    "light.500": ("#666d80", "--swatch--light-500"),
    "light.600": ("#353849", "--swatch--light-600"),
    "light.700": ("#272835", "--swatch--light-700"),
    "light.800": ("#1a1b25", "--swatch--light-800"),
    "light.900": ("#0d0d12", "--swatch--light-900"),
    "dark.800": ("#2f2b2d", "--swatch--dark-800"),
    "dark.900": ("#1f1d1e", "--swatch--dark-900"),
    "mutedText": ("#615e6e", "--swatch--muted-text"),
    "subText": ("#9491a1", "--swatch--sub-text"),
    "problemText": ("#312749", "--swatch--the-problem-colors-text"),
    "verification": ("#11244a", "--swatch--verification"),
    "neutralLight.50": ("#ecedf3", "--swatch--neutral-light-50"),
}
for name, (value, key) in SWATCHES.items():
    put(CORE, "color." + name, leaf(
        "core.color." + name, "color", value,
        f"css-var {key} declared {DECL[key]}",
    ))

# 8-digit hex neutrals, kept as the declared value converted to rgba.
NEUTRALS = {
    "25": "#1d4f810a",
    "50": "#12376914",
    "100": "#09194821",
    "200": "#07204540",
    "300": "#02173b5c",
    "400": "#03103080",
    "500": "#666880",
    "600": "#010419c9",
    "700": "#010213d9",
    "800": "#01020ee6",
    "900": "#000005f2",
}
for step, value in NEUTRALS.items():
    css = f"--swatch--neutral-{step}"
    put(CORE, f"color.neutral.{step}", leaf(
        f"core.color.neutral.{step}", "color", value,
        f"css-var {css} declared {DECL[css]}",
    ))

RADII = {
    "xsmall": "--radius--xsmall",
    "small": "--radius--small",
    "midsize": "--radius--midsize",
    "xmidsize": "--radius--xmidsize",
    "xxmidsize": "--radius--xxmidsize",
    "main": "--radius--main",
    "large": "--radius--large",
    "xlarge": "--radius--xlarge",
    "xxlarge": "--radius--xxlarge",
    "huge": "--radius--huge",
    "section": "--radius--section",
}
for name, css in RADII.items():
    put(CORE, "radius." + name, leaf(
        "core.radius." + name, "dimension", DECL[css],
        f"css-var {css}",
    ))

# Fluid space steps. The token value is the desktop end of the clamp
# (viewport-max 75rem), which is what 1440 CSS px resolves toward.
# The phone end is recorded in the description from the same declaration.
SPACE = {
    "1": ("0.5rem", "6px at 20rem, 8px at 75rem"),
    "2": ("0.75rem", "10px at 20rem, 12px at 75rem"),
    "3": ("1rem", "14px at 20rem, 16px at 75rem"),
    "4": ("1.5rem", "20px at 20rem, 24px at 75rem"),
    "5": ("2rem", "28px at 20rem, 32px at 75rem"),
    "6": ("2.5rem", "32px at 20rem, 40px at 75rem"),
    "7": ("3rem", "36px at 20rem, 48px at 75rem"),
    "8": ("4rem", "40px at 20rem, 64px at 75rem"),
}
for step, (desktop, note) in SPACE.items():
    css = f"--_spacing---space--{step}"
    put(CORE, "spacing." + step, leaf(
        "core.spacing." + step, "dimension", desktop,
        f"css-var {css} desktop end of the clamp; {note}. Full clamp in raw/css-vars.json",
    ))

put(CORE, "spacing.gutter", leaf(
    "core.spacing.gutter", "dimension", "1.5rem",
    "css-var --site--gutter declared 1.5rem",
))
put(CORE, "spacing.marginDesktop", leaf(
    "core.spacing.marginDesktop", "dimension", "3rem",
    "css-var --site--margin desktop end of the clamp (1rem at 20rem, 3rem at 75rem). At 390px the computed width was 18.5391px",
))
put(CORE, "spacing.sectionSmall", leaf("core.spacing.sectionSmall", "dimension", "3rem",
    "css-var --_spacing---section-space--small desktop end (2rem at 20rem, 3rem at 75rem)"))
put(CORE, "spacing.sectionMain", leaf("core.spacing.sectionMain", "dimension", "6rem",
    "css-var --_spacing---section-space--main desktop end (3.5rem at 20rem, 6rem at 75rem)"))
put(CORE, "spacing.sectionLarge", leaf("core.spacing.sectionLarge", "dimension", "7.5rem",
    "css-var --_spacing---section-space--large desktop end (5.5rem at 20rem, 7.5rem at 75rem)"))
put(CORE, "spacing.pageTop", leaf("core.spacing.pageTop", "dimension", "9.5rem",
    "css-var --_spacing---section-space--page-top desktop end (7rem at 20rem, 9.5rem at 75rem)"))

put(CORE, "border.width", leaf(
    "core.border.width", "dimension", "0.094rem",
    "css-var --border-width--main declared .094rem",
))
put(CORE, "focus.width", leaf("core.focus.width", "dimension", "0.125rem", "css-var --focus--width"))
put(CORE, "focus.offsetInner", leaf("core.focus.offsetInner", "dimension", "-0.125rem", "css-var --focus--offset-inner"))
put(CORE, "focus.offsetOuter", leaf("core.focus.offsetOuter", "dimension", "0.1875rem", "css-var --focus--offset-outer"))

put(CORE, "font.family.display", leaf(
    "core.font.family.display", "fontFamily", "Britti Sans, Arial, sans-serif",
    "css-var --_typography---font--primary-family. Britti Sans 500 woff2 is served by the site and is not shipped",
))
put(CORE, "font.family.body", leaf(
    "core.font.family.body", "fontFamily", "Inter, Arial, sans-serif",
    "css-var --_typography---font--secondary-font. Inter 400 and 500 woff2 loaded on the marketing pages",
))
put(CORE, "font.family.auth", leaf(
    "core.font.family.auth", "fontFamily", "Inter var, ui-sans-serif, system-ui, sans-serif",
    "Reconstruction: entered by hand at capture time from the computed font-family on wiza.co/auth/login body. Inter var is a separate face from the marketing Inter",
))
put(CORE, "font.weight.regular", leaf("core.font.weight.regular", "fontWeight", 400, "css-var --_typography---font--primary-regular"))
put(CORE, "font.weight.medium", leaf("core.font.weight.medium", "fontWeight", 500, "css-var --_typography---font--primary-medium"))
put(CORE, "font.weight.bold", leaf("core.font.weight.bold", "fontWeight", 700, "css-var --_typography---font--primary-bold"))
put(CORE, "font.lineHeight.tight", leaf("core.font.lineHeight.tight", "number", 1, "css-var --_typography---line-height--1"))
put(CORE, "font.lineHeight.snug", leaf("core.font.lineHeight.snug", "number", 1.1, "css-var --_typography---line-height--1-1"))
put(CORE, "font.lineHeight.body", leaf("core.font.lineHeight.body", "number", 1.5, "css-var --_typography---line-height--1-5"))
# --_typography---letter-spacing--0-03em (-.03em) is relative to the font size, so it is listed
# under core.$extensions.notTokenised below rather than as a dimension token.

# Desktop computed sizes at 1440 CSS px (16px root). The clamp is in raw/css-vars.json.
TYPE = {
    "display": ("80px", "80px", "5rem desktop end of --_typography---font-size--display; computed h1 on / was 64px because the heading uses the h1 step"),
    "h1": ("64px", "64px", "computed font-size of h1 on https://wiza.co/ at 1440px. Declared clamp ends at 4rem"),
    "h2": ("56px", "56px", "computed font-size of h2 on https://wiza.co/ at 1440px. Declared clamp ends at 3.5rem"),
    "h3": ("48px", "48px", "declared --_typography---font-size--h3 desktop end 3rem. Not used as a visible heading size on the measured pages"),
    "h4": ("40px", "40px", "computed font-size of the Team Plan h2 on /pricing"),
    "h5": ("32px", "32px", "computed font-size of .pricing_card_price_text (u-text-style-h5) on /pricing"),
    "h6": ("24px", "24px", "computed font-size of pricing card titles (h2) on /pricing"),
    "textXlarge": ("22px", "28.6px", "declared --_typography---font-size--text-xlarge desktop end 1.375rem"),
    "textLarge": ("18px", "27px", "declared --_typography---font-size--text-large desktop end 1.125rem"),
    "textMain": ("16px", "24px", "computed body copy on /privacy and the home paragraph role. Declared text-main desktop end is 1rem"),
    "textSmall": ("14px", "21px", "computed .nav_link1 and the work-email field on the home page"),
    "textXsmall": ("12px", "16px", "computed .pricing_tag_text and .pricing_card_price_desc"),
}
for name, (size, line, note) in TYPE.items():
    put(CORE, "typography." + name, {
        "$value": {
            "fontFamily": "{font.family.display}" if name in ("display", "h1", "h2", "h3", "h4", "h5", "h6") else "{font.family.body}",
            "fontSize": size,
            "fontWeight": 500 if name in ("display", "h1", "h2", "h3", "h4", "h5", "h6") else 400,
            "lineHeight": line,
        },
        "$type": "typography",
        "$extensions": {"source": (
            # 12px at the declared 1.3 or 1.5 would be 15.6px or 18px, so textXsmall's 16px is the
            # computed line height of the elements it was read from, not a declared step.
            "Reconstruction: lineHeight 16px entered by hand at capture time from the computed line height "
            "of .pricing_tag_text and .pricing_card_price_desc; it is not a declared step (1.3 or 1.5 of 12px "
            "give 15.6px or 18px), and raw/ does not hold the computed value. fontSize: " + note
            if name == "textXsmall" else
            "Reconstruction: lineHeight entered by hand at capture time (headings at the declared "
            "--_typography---line-height--1, text steps at the declared 1.3 or 1.5); no style's computed "
            "line height or tracking was saved in raw/. fontSize: " + note
        )},
    })

put(CORE, "layout.columnCount", leaf("core.layout.columnCount", "number", 12, "css-var --site--column-count"))
put(CORE, "layout.viewportMax", leaf("core.layout.viewportMax", "dimension", "75rem", "css-var --site--viewport-max (unitless 75, times 1rem)"))
put(CORE, "layout.viewportMin", leaf("core.layout.viewportMin", "dimension", "20rem", "css-var --site--viewport-min (unitless 20, times 1rem)"))
put(CORE, "layout.contentMax", leaf("core.layout.contentMax", "dimension", "1200px", "Reconstruction: entered by hand at capture time from the measured content width of the home h1 and hero video at 1440px"))

# Semantic light set: declared theme roles, resolved, plus painted components.
LIGHT = {}

THEME = {
    "text": ("#26114a", "--_theme---text", "resolved from --swatch--brand-500"),
    "headingAccent": ("#4c24a3", "--_theme---heading-accent", "resolved from --swatch--brand-200"),
    "background2": ("#c1c7cf", "--_theme---background-2", "resolved from --swatch--light-200"),
    "selectionBackground": ("#e4d8fd", "--_theme---selection--background", "resolved from --swatch--brand-25"),
    "selectionText": ("#26114a", "--_theme---selection--text", "resolved from --swatch--brand-text"),
    "buttonPrimaryBackground": ("#7e43ff", "--_theme---button-primary--background", "resolved from --swatch--brand-100. The painted primary button on the home page is brand-500, not this token"),
    "buttonPrimaryText": ("#26114a", "--_theme---button-primary--text", "resolved from --swatch--brand-text"),
    "buttonSecondaryBackground": ("#26114a", "--_theme---button-secondary--background", "resolved from --swatch--brand-500"),
    "buttonSecondaryText": ("#ffffff", "--_theme---button-secondary--text", "resolved from --swatch--light-0"),
}
for name, (value, css, note) in THEME.items():
    put(LIGHT, "color." + name, leaf("light.color." + name, "color", value, f"css-var {css}; {note}"))

put(LIGHT, "color.page", leaf("light.color.page", "color", "#ffffff", "painted button and pricing-card surface; html and body background are transparent over the hero gradient"))
put(LIGHT, "color.ink", leaf("light.color.ink", "color", "#26114a", "computed color of body, h2 and nav links on https://wiza.co/ (rgb(38, 17, 74))"))
put(LIGHT, "color.muted", leaf("light.color.muted", "color", "#615e6e", "computed color of footer links and pricing price descriptions (rgb(97, 94, 110)), matching --swatch--muted-text"))
put(LIGHT, "color.footerInk", leaf("light.color.footerInk", "color", "#312749", "computed color of the footer on https://wiza.co/ (rgb(49, 39, 73)), matching --swatch--the-problem-colors-text"))
put(LIGHT, "color.accent", leaf("light.color.accent", "color", "#7e43ff", "computed color of prose links on /privacy and the login submit (rgb(126, 67, 255)), matching --swatch--brand-100"))
put(LIGHT, "color.onAccent", leaf("light.color.onAccent", "color", "#ffffff", "computed color of the filled primary button label"))
put(LIGHT, "color.heroGround", leaf("light.color.heroGround", "color", "#231645", "Reconstruction: entered by hand at capture time from the computed background of the animated heading wrap on the home hero (rgb(35, 22, 69))"))
put(LIGHT, "color.enterpriseHeroInk", leaf("light.color.enterpriseHeroInk", "color", "#ffffff", "computed color of the h1 on /enterprise"))

# Painted components. Values are computed styles, not guesses.
COMPONENTS = C["components"]
for name, spec in COMPONENTS.items():
    for prop, value in spec["values"].items():
        ty = spec["types"][prop]
        put(LIGHT, f"component.{name}.{prop}", leaf(
            f"light.component.{name}.{prop}", ty, value, spec["source"],
        ))


CORE.setdefault("$extensions", {})["notTokenised"] = [
    "--_typography---letter-spacing--0-03em: -.03em, declared (raw/css-vars.json). em tracking scales "
    "with the font size and is not one px or rem length. No measured style was seen using it.",
    "Type steps carry no letterSpacing: no style's computed tracking was saved in raw/.",
]

import token_checks  # noqa: E402  (tools/ is on sys.path above)

_errors = token_checks.alias_errors(CORE, LIGHT)
if _errors:
    raise SystemExit("\n".join(_errors))

doc = {
    "core": CORE,
    "light": LIGHT,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}



def render():
    """tokens.json's exact text; importing this module writes nothing."""
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


if __name__ == "__main__":
    out = render()
    (HERE / "tokens.json").write_text(out)
    print(f"tokens.json: {out.count(chr(10))} lines")
