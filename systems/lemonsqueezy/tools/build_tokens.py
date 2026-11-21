#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/readings.json.

The marketing site declares its palette as Webflow custom properties on :root
(raw/css-vars.json, resolved on https://www.lemonsqueezy.com/ on 2026-11-21).
Component sizes come from computed styles in raw/readings.json. There is no
dark theme on the public site, so this file has core and light only.

Unread values stay out. A token that could not be read is not invented.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())["out"]
READ = json.loads((RAW / "readings.json").read_text())
SRC = "raw/css-vars.json, resolved on :root at https://www.lemonsqueezy.com/ on 2026-11-21"
COMP = "raw/readings.json computed style, 2026-11-21"


def color(value, source, description=None):
    token = {
        "$type": "color",
        "$value": value,
        "$extensions": {"source": source},
    }
    if description:
        token["$description"] = description
    return token


def dim(value, source, description=None):
    token = {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": source},
    }
    if description:
        token["$description"] = description
    return token


def font(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def num(value, source):
    return {"$type": "number", "$value": value, "$extensions": {"source": source}}


def typography(family, size, weight, line, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
        },
        "$extensions": {"source": source},
    }


def duration(value, source):
    return {"$type": "duration", "$value": value, "$extensions": {"source": source}}


def cubic(value, source):
    return {"$type": "cubicBezier", "$value": value, "$extensions": {"source": source}}


# Palette names that resolved to a hex or a keyword colour. Keyword "black"
# and "white" are recorded as the hex the browser paints, from the census.
PALETTE = {
    "black": "#000000",
    "black-2": VARS["--black-2"],
    "blue": VARS["--blue"],
    "blue-50": VARS["--blue-50-501"],
    "blue-100": VARS["--blue-100"],
    "blue-200": VARS["--blue-200"],
    "blue-300": VARS["--blue-300"],
    "blue-400": VARS["--blue-400"],
    "blue-500": VARS["--blue-500"],
    "blue-600": VARS["--blue-600"],
    "blue-700": VARS["--blue-700"],
    "blue-violet": VARS["--blue-violet"],
    "border": VARS["--border-color"],
    "gray-300": VARS["--gray-300"],
    "gray-500": VARS["--gray-500"],
    "green-50": VARS["--green-50-501"],
    "green-100": VARS["--green-100"],
    "green-200": VARS["--green-200"],
    "green-300": VARS["--green-300"],
    "green-400": VARS["--green-400"],
    "green-500": VARS["--green-500"],
    "green-600": VARS["--green-600"],
    "green-700": VARS["--green-700"],
    "grey-50": VARS["--grey-50"],
    "grey-100": VARS["--grey-100"],
    "grey-200": VARS["--grey-200"],
    "grey-700": VARS["--grey-700"],
    "ink": VARS["--dark-grey"],
    "yellow": VARS["--ls-color-yellow"],
    "yellow-lighter": VARS["--ls-color-yellow-lighter"],
    "yellow-50": VARS["--yellow-50-501"],
    "yellow-100": VARS["--yellow-100"],
    "yellow-200": VARS["--yellow-200"],
    "yellow-300": VARS["--yellow-300"],
    "yellow-400": VARS["--yellow-400"],
    "yellow-500": VARS["--yellow-500"],
    "yellow-700": VARS["--yellow-700"],
    "orange-50": VARS["--orange-50"],
    "orange-100": VARS["--orange-100"],
    "orange-200": VARS["--orange-200"],
    "orange-300": VARS["--orange-300"],
    "orange-400": VARS["--orange-400"],
    "orange-500": VARS["--orange-500"],
    "orange-600": VARS["--orange-600"],
    "orange-700": VARS["--orange-700"],
    "pink-50": VARS["--pink-50"],
    "pink-100": VARS["--pink-100"],
    "pink-200": VARS["--pink-200"],
    "pink-300": VARS["--pink-300"],
    "pink-400": VARS["--pink-400"],
    "pink-500": VARS["--pink-500"],
    "pink-600": VARS["--pink-600"],
    "pink-700": VARS["--pink-700"],
    "pink-800": VARS["--pink-800"],
    "purple-50": VARS["--purple-50-501"],
    "purple-100": VARS["--purple-100"],
    "purple-200": VARS["--purple-200"],
    "purple-300": VARS["--purple-300"],
    "purple-400": VARS["--purple-400"],
    "purple-500": VARS["--purple-500"],
    "purple-600": VARS["--purple-600"],
    "purple-700": VARS["--purple-700"],
    "purple-900": VARS["--purple-900"],
    "red-50": VARS["--red-50-501"],
    "red-100": VARS["--red-100"],
    "red-200": VARS["--red-200"],
    "red-400": VARS["--red-400"],
    "red-500": VARS["--red-500"],
    "red-700": VARS["--red-700"],
    "white": "#ffffff",
    "white-10": VARS["--white-901"],
}

core_palette = {k: color(v, SRC) for k, v in PALETTE.items()}

# Computed roles. These are the colours that actually paint the public pages.
C = READ["components"]

def comp_color(key, prop, note):
    raw = C[key][prop]
    # rgb() already converted in the builder from the reading's rgb string.
    return color(rgb_hex(raw), f"{COMP}; {key} {prop}. {note}")


def rgb_hex(value):
    value = value.strip()
    if value.startswith("#"):
        return value
    if value in ("transparent", "rgba(0, 0, 0, 0)"):
        return "#00000000"
    import re
    m = re.fullmatch(r"rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)", value)
    if not m:
        raise SystemExit(f"not a colour: {value}")
    hex_ = "".join(f"{int(n):02x}" for n in m.group(1, 2, 3))
    if m.group(4) is None or float(m.group(4)) == 1:
        return f"#{hex_}"
    a = float(m.group(4))
    return f"#{hex_}{round(a * 255):02x}"


light = {
    "page": color("#5423e7", f"{SRC}; --purple-600 paints .section-hero-header and .nav_component. meta theme-color is the same hex."),
    "surface": color("#ffffff", f"{SRC}; --white-900. Login card and help dialog sit on white."),
    "surface-muted": color(PALETTE["grey-50"], f"{SRC}; --grey-50. Pricing FAQ band is the pink-100 fill, recorded separately."),
    "text": color(PALETTE["black-2"], f"{SRC}; --black-2. Hero buttons and fee figures use this ink."),
    "text-on-accent": color("#ffffff", f"{COMP}; hero-title color on the purple page."),
    "muted": color("#ffffff99", f"{COMP}; nav-link and hero-body color, rgba(255,255,255,0.6) on the purple page."),
    "muted-ink": color(PALETTE["gray-500"], f"{SRC}; --gray-500. Secondary ink on light surfaces."),
    "accent": color(PALETTE["purple-600"], f"{SRC}; --ls-purple and --purple-600. Also the meta theme-color."),
    "accent-auth": color("#7047eb", f"{COMP}; login-submit background. Matches --purple-500 / --blue-violet."),
    "banner": color(PALETTE["yellow"], f"{SRC}; --ls-color-yellow. Shutdown banner background."),
    "link": color(PALETTE["purple-500"], f"{SRC}; --blue-violet. Docs links on the docs host use this violet."),
    "border": color(PALETTE["border"], f"{SRC}; --border-color."),
    "focus": color("#3889ec", f"Declared focus ring rgb(56, 152, 236) in the marketing stylesheet, 2026-11-21. Not observed on the primary button: its computed outline did not change on focus."),
    "success": color(PALETTE["green-500"], f"{SRC}; --green-500. Present as a ramp. A success state was not shown on the public pages."),
    "warning": color(PALETTE["yellow-500"], f"{SRC}; --yellow-500."),
    "danger": color(PALETTE["red-500"], f"{SRC}; --red-500. The help dialog marks a required email with a red asterisk. The asterisk colour was not measured on its own."),
    "info": color(PALETTE["blue-500"], f"{SRC}; --blue-500. Present as a ramp. An info toast was not shown."),
    "overlay": color("#12121799", "Not captured as a computed scrim. The help dialog dims the page. The scrim hex was not read, so this token is omitted from use."),
}

# Do not ship the overlay guess.
del light["overlay"]

core = {
    "palette": core_palette,
    "font": {
        "family": {
            "display": font("Circularpro book, sans-serif", f"{COMP}; hero-title fontFamily."),
            "body": font("Inter, sans-serif", f"{COMP}; banner, nav-link, button-primary fontFamily. @font-face Inter 400/500/600/700."),
            "auth": font("Inter, ui-sans-serif, system-ui, sans-serif", f"{COMP}; login-title fontFamily."),
            "mono": font("Jetbrainsmono, ui-monospace, monospace", "raw/readings.json @font-face Jetbrainsmono 400. Not observed on a public text node, so treat as available, not as a measured role."),
        },
        "weight": {
            "regular": num(400, f"{COMP}; hero-title and body."),
            "medium": num(500, f"{COMP}; button-primary and login-title."),
            "bold": num(700, "@font-face Inter 700. The pricing switch computed font-weight 700."),
        },
        "size": {
            "display": dim("80px", f"{COMP}; hero-title and pricing-title."),
            "title": dim("56px", f"{COMP}; pricing-fee."),
            "auth-title": dim("24px", f"{COMP}; login-title."),
            "body": dim("18px", f"{COMP}; banner and hero-body. Most frequent size on the homepage census (125 of 182 sampled)."),
            "nav": dim("15px", f"{COMP}; nav-link and button-primary."),
            "caption": dim("14px", f"{COMP}; footer-link and login-field."),
            "auth-button": dim("16px", f"{COMP}; login-submit."),
        },
    },
    "radius": {
        "control": dim("8px", f"{COMP}; login-field, login-submit, login-oauth, faq-open. Homepage census counted 8px nine times."),
        "pill": dim("40px", f"{COMP}; button-primary and button-white. Homepage census counted 40px three times."),
        "none": dim("0px", f"{COMP}; banner, hero-title."),
    },
    "space": {
        "4": dim("4px", "Not captured as its own step. Padding readings are 8, 10, 12, 16, 18, 20, 32, 40."),
        "8": dim("8px", f"{COMP}; button-primary padding-top, login-field padding-top."),
        "10": dim("10px", f"{COMP}; login-submit padding-top."),
        "12": dim("12px", f"{COMP}; login-oauth padding-top."),
        "16": dim("16px", f"{COMP}; nav-link padding-right, login-field padding-right."),
        "18": dim("18px", f"{COMP}; login-oauth padding-right."),
        "20": dim("20px", f"{COMP}; button-primary padding-right."),
        "32": dim("32px", f"{COMP}; nav-link padding-top. That padding is the nav bar's vertical inset, not a text pad."),
        "40": dim("40px", f"{COMP}; faq-open padding-right."),
    },
    "size": {
        "nav-height": dim("88px", f"{COMP}; nav-link height, which fills the nav bar."),
        "banner-height": dim("70px", f"{COMP}; banner height."),
        "button-height": dim("40px", f"{COMP}; button-primary height."),
        "auth-button-height": dim("48px", f"{COMP}; login-submit height."),
        "field-height": dim("40px", f"{COMP}; login-field height."),
        "oauth-height": dim("50px", f"{COMP}; login-oauth height."),
        "logo": dim("40px", f"{COMP}; logo link height."),
    },
    "typography": {
        "display": typography("{font.family.display}", "{font.size.display}", "{font.weight.regular}", "80px", f"{COMP}; hero-title 80/80."),
        "title": typography("{font.family.display}", "{font.size.title}", "{font.weight.regular}", "63.84px", f"{COMP}; pricing-fee 56/63.84."),
        "body": typography("{font.family.body}", "{font.size.body}", "{font.weight.regular}", "28.8px", f"{COMP}; banner 18/28.8. Hero body line-height was 30.6px."),
        "nav": typography("{font.family.body}", "{font.size.nav}", "{font.weight.medium}", "24px", f"{COMP}; button-primary 15/24 weight 500. Nav links computed weight 400."),
        "caption": typography("{font.family.body}", "{font.size.caption}", "{font.weight.regular}", "22.4px", f"{COMP}; footer-link 14/22.4."),
        "auth-title": typography("{font.family.auth}", "{font.size.auth-title}", "{font.weight.medium}", "32px", f"{COMP}; login-title 24/32 weight 500."),
    },
    "motion": {
        "duration-fast": duration("100ms", "Marketing stylesheet transition-duration 0.1s, 2026-11-21."),
        "duration-nav": duration("400ms", "Nav data-duration attribute read as 400 on .nav_component, 2026-11-21."),
        "easing": cubic([0.25, 0.46, 0.45, 0.94], "Marketing stylesheet cubic-bezier(0.25, 0.46, 0.45, 0.94), 2026-11-21."),
    },
    "shadow": {
        "card": {
            "$type": "shadow",
            "$value": "rgba(17, 17, 46, 0.06) 0px 2px 4px, rgba(17, 17, 46, 0.09) 0px 8px 13px",
            "$extensions": {"source": "Declared box-shadow in the marketing stylesheet, 2026-11-21. Not tied to one measured component."},
        },
    },
}

# Drop the space.4 placeholder. It was not measured.
del core["space"]["4"]

doc = {
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
}

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out, "palette", len(core_palette), "light", len(light))
