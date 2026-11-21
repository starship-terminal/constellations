#!/usr/bin/env python3
"""Build tokens.json from the Ripple public-site readings.

Sources, read from ripple.com on 2026-11-21 in headless Chromium at 1440x900:
  raw/css-vars.json            custom properties declared on the homepage
                               stylesheets. Ripple stores palette channels as
                               space-separated RGB triples (--bds-primary-500
                               is "0 106 255"). This builder converts those
                               triples to hex. Tailwind internals (--tw-*) and
                               the Osano cookie banner (--osano-*) are not
                               product tokens.
  raw/components-computed.json computed styles of the painted controls.

The public site paints one light theme. There is no dark theme switch.
Unread values stay out of the file.

Deterministic: same inputs, byte-identical output.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())

DECL = V["resolved"]["light"]


def rgb_triple(raw):
    m = re.fullmatch(r"(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})", raw.strip())
    if not m:
        return None
    return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())


def color(name, seen=None):
    seen = seen or set()
    if name in seen:
        raise ValueError(f"alias cycle at {name}")
    seen.add(name)
    raw = DECL[name]["raw"].strip()
    alias = re.fullmatch(r"var\((--[a-z0-9-]+)\)", raw)
    if alias:
        return color(alias.group(1), seen)
    hexed = rgb_triple(raw)
    if not hexed:
        raise ValueError(f"{name} is not an RGB triple: {raw!r}")
    return {
        "$value": hexed,
        "$type": "color",
        "$extensions": {"source": f"css-var {name} ({raw}) on ripple.com :root, 2026-11-21"},
    }


def dim(value, source):
    if isinstance(value, (int, float)):
        value = "%gpx" % value
    if not re.fullmatch(r"-?\d+(\.\d+)?px", str(value)):
        raise ValueError(f"dimension {value!r} from {source}")
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def font_stack(name):
    raw = DECL[name]["raw"]
    return {
        "$value": raw,
        "$type": "fontFamily",
        "$extensions": {"source": f"css-var {name} on ripple.com :root, 2026-11-21"},
    }


def typography(role, reading, family_token):
    return {
        "$value": {
            "fontFamily": family_token,
            "fontSize": reading["fontSize"],
            "fontWeight": int(reading["fontWeight"]),
            "lineHeight": reading["lineHeight"],
            "letterSpacing": reading["letterSpacing"] if reading["letterSpacing"] != "normal" else "0px",
        },
        "$type": "typography",
        "$extensions": {"source": f"measured getComputedStyle {reading['where']}"},
    }


def measured_color(value, where):
    return {
        "$value": value,
        "$type": "color",
        "$extensions": {"source": f"measured getComputedStyle {where}"},
    }


# BDS is the named brand system (button classes are bds-*). The marketing
# --color-* scale is a second declared ramp used by page sections.
bds_stops = {
    "primary": [100, 200, 300, 400, 500, 600, 700, 800, 900],
    "neutral": [25, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900],
    "blue": [100, 200, 300, 400, 500, 600, 700, 800, 900],
    "gray": [25, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900],
    "green": [100, 200, 300, 400, 500],
    "orange": [100, 200, 300, 400, 500],
    "pink": [100, 200, 300, 400, 500],
    "purple": [100, 200, 300, 400, 500],
}

core_color = {
    "white": color("--bds-color-white"),
    "black": color("--bds-color-black"),
}
for family, stops in bds_stops.items():
    prefix = "--bds-primary-" if family == "primary" else (
        "--bds-neutral-" if family == "neutral" else f"--bds-color-{family}-"
    )
    core_color[family] = {str(stop): color(f"{prefix}{stop}") for stop in stops}

# Marketing gray/blue steps that the homepage sections actually reference
# (bg-gray-90, text-gray-2.5, bg-blue-50). Kept beside BDS, not merged into it.
marketing = {}
for name in (
    "--color-gray-2-5", "--color-gray-5", "--color-gray-10", "--color-gray-20",
    "--color-gray-40", "--color-gray-50", "--color-gray-70", "--color-gray-90",
    "--color-blue-50", "--color-blue-55", "--color-blue-60", "--color-blue-70",
    "--color-white", "--color-black",
):
    key = name.removeprefix("--color-").replace(".", "")
    marketing[key] = color(name)

hero = C["hero-title"]
body = C["body-copy"]
nav = C["nav-trigger"]
cta = C["hero-cta"]
footer_link = C["footer-link"]
search = C["search-field"]

core = {
    "color": core_color,
    "marketing": marketing,
    "font": {
        "display": font_stack("--font-ripple"),
        "ui": font_stack("--font-ripple-bds"),
    },
    "typography": {
        "display": typography("display", hero, "{font.display}"),
        "body": typography("body", body, "{font.display}"),
        "nav": typography("nav", nav, "{font.ui}"),
        "button": typography("button", cta, "{font.display}"),
        "footer-link": typography("footer-link", footer_link, "{font.display}"),
    },
    "radius": {
        "button": dim(cta["borderRadius"], "measured button.button-dark border-radius, homepage"),
        "pill": dim("9999px", "measured Contact Sales and icon buttons, border-radius 9999px"),
        "search": dim(search["borderRadius"], "measured input[type=search] border-radius"),
        "logo": dim("2px", "measured header logo link border-radius"),
        "nav": dim(nav["borderRadius"], "measured nav trigger border-radius"),
    },
    "size": {
        "header": dim("80px", "measured header height at 1440"),
        "button": dim(cta["height"], "measured Explore Our Solutions button height"),
        "icon-button": dim("40px", "measured Open search button width and height"),
        "search-field": dim(search["height"], "measured search input height"),
    },
}

light = {
    "page": {"$value": "{marketing.white}", "$type": "color", "$extensions": {"source": "alias of marketing white; header computes rgb(255, 255, 255)"}},
    "surface": {"$value": "{marketing.gray-2-5}", "$type": "color", "$extensions": {"source": "alias; section bands compute rgb(250, 250, 250), which is --color-gray-2-5"}},
    "text": {"$value": "{marketing.gray-90}", "$type": "color", "$extensions": {"source": "alias; h1 computes rgb(20, 26, 31), which is --color-gray-90"}},
    "muted": {"$value": "{marketing.gray-40}", "$type": "color", "$extensions": {"source": "alias; footer link hover computes rgb(147, 154, 159), which is --color-gray-40"}},
    "accent": {"$value": "{color.primary.500}", "$type": "color", "$extensions": {"source": "alias; focus ring computes rgb(0, 106, 255), which is --bds-primary-500"}},
    "on-accent": {"$value": "{marketing.gray-5}", "$type": "color", "$extensions": {"source": "alias; primary button text computes rgb(241, 242, 243), which is --color-gray-5"}},
    "border": {"$value": "{color.neutral.100}", "$type": "color", "$extensions": {"source": "alias; search field background computes rgb(228, 229, 231), which is --bds-neutral-100"}},
    "footer": {"$value": "{marketing.gray-90}", "$type": "color", "$extensions": {"source": "alias; footer background computes rgb(20, 26, 31)"}},
    "footer-text": {"$value": "{marketing.gray-2-5}", "$type": "color", "$extensions": {"source": "alias; footer text computes rgb(250, 250, 250)"}},
    "focus": {
        "ring": measured_color(
            "#006aff",
            "search input and icon button box-shadow second layer rgb(0, 106, 255) 0 0 0 3px",
        ),
    },
    "component": {
        "button": {
            "radius": dim(cta["borderRadius"], "measured primary button"),
            "height": dim(cta["height"], "measured primary button"),
            "text": measured_color("#f1f2f3", "primary button color"),
            "fill-inner": measured_color("#005bcc", "primary button radial-gradient inner stop rgb(0, 91, 204)"),
            "fill-outer": measured_color("#008cff", "primary button radial-gradient outer stop rgb(0, 140, 255) at 80%"),
            "hover-fill": measured_color("#0067e5", "primary button hover radial-gradient rgb(0, 103, 229)"),
        },
        "search": {
            "background": measured_color("#e4e5e7", "search input backgroundColor"),
            "text": measured_color("#586074", "search input color"),
            "radius": dim(search["borderRadius"], "measured search input"),
            "height": dim(search["height"], "measured search input"),
        },
        "menu": {
            "background": measured_color("#ffffff", "Products mega menu panel background"),
            "shadow": {
                "$value": "0px 10px 20px 0px rgba(0, 0, 0, 0.05)",
                "$type": "shadow",
                "$extensions": {"source": "measured Products menu panel box-shadow"},
            },
        },
    },
}

# shadow type in this repo's builder expects a list of layers. Use a string
# only if the style guide accepts it. The kit check wants a list.
light["component"]["menu"]["shadow"] = {
    "$value": [{
        "color": "rgba(0, 0, 0, 0.05)",
        "offsetX": "0px",
        "offsetY": "10px",
        "blur": "20px",
        "spread": "0px",
    }],
    "$type": "shadow",
    "$extensions": {"source": "measured Products mega menu panel box-shadow rgba(0, 0, 0, 0.05) 0px 10px 20px 0px"},
}

doc = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
    }],
}

(HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", HERE / "tokens.json")
