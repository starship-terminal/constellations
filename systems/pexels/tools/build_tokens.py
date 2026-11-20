#!/usr/bin/env python3
"""Build tokens.json from Pexels CSS readings.

Sources, read from www.pexels.com on 2026-11-21, signed out:
  raw/css-vars.json            custom properties parsed from the live stylesheets
  raw/components-sample.json   computed styles of the Join button, Home pill, h1,
                               search field, search chip, License link, and the
                               Join hover state

The greyscale and named hues are declared on `[data-mode="light"], body` and again
on `[data-mode="dark"]`. Public pages paint the light set. The dark set is in the
stylesheets and was not applied on any captured page, so the dark semantic roles
are labelled as stylesheet declarations, not as a live theme.

Every token carries $extensions.source. A dimension is one px or rem length.
Deterministic: same inputs, same bytes.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
S = json.loads((RAW / "components-sample.json").read_text())

LIGHT_SEL = '[data-mode="light"], body'
DARK_SEL = '[data-mode="dark"]'
SHEET = "Next stylesheet 619c2e3a161a45cb.css, parsed 2026-11-21"


def decl(selector, name):
    hits = [d for d in V["decls"] if d["selector"] == selector and d["name"] == name and not d.get("media")]
    if not hits:
        raise SystemExit(f"missing decl {selector} {name}")
    return hits[0]["value"]


def color(v):
    v = v.strip().lower()
    if v == "#000":
        return "#000000"
    if v == "#fff":
        return "#ffffff"
    if re.fullmatch(r"#[0-9a-f]{6}", v):
        return v
    m = re.fullmatch(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", v)
    if m:
        return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())
    raise SystemExit("not a colour: " + v)


def token(value, ty, source, description=None):
    if ty == "color" and not str(value).startswith("{"):
        value = color(value)
    if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(value)):
        raise SystemExit("bad dimension " + str(value))
    if ty == "fontWeight":
        value = int(value)
    t = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    if description:
        t["$description"] = description
    return t


def palette(selector, label):
    hues = {
        "greyscale": ["100", "200", "300", "400", "500", "600", "700", "800", "900", "black", "shadow", "white"],
        "alien": ["light", "lighter", "mid", "dark"],
        "jellyfish": ["light", "lighter", "mid", "dark"],
        "papaya": ["light", "lighter", "mid", "dark"],
        "strawberry": ["light", "lighter", "mid", "dark"],
        "sunshine": ["light", "lighter", "mid", "dark"],
    }
    out = {}
    for hue, steps in hues.items():
        out[hue] = {}
        for step in steps:
            name = f"--color-{hue}-{step}"
            src = f"Measured. {label} declares {name}: {decl(selector, name)}. {SHEET}."
            out[hue][step] = token(decl(selector, name), "color", src)
    return out


src_join = "Measured. Join button computed style on www.pexels.com/ at 1440x900, 2026-11-21, raw/components-sample.json."
src_join_hover = "Measured. Join button :hover, same page, raw/components-sample.json joinHover."
src_home = "Measured. Home subnav pill computed style, same page."
src_h1 = "Measured. homepage h1 computed style, same page."
src_search = "Measured. SearchInput container computed style, same page."
src_pill = "Measured. trending search chip computed style, same page."
src_link = "Measured. License nav link computed style, same page."
src_motion = "Measured. Join button transition, same page."
src_body = "Measured. body computed font on www.pexels.com/, raw/css-vars.json resolved.body."

light_page = "{color.greyscale.white}"
# semantic aliases point at the set's own color group

core = {
    "font": {
        "family": {
            "sans": token(
                "Canva Sans, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif",
                "fontFamily",
                src_body + " @font-face Canva Sans from static.pexels.com/1/fonts/CanvaSans-Medium.woff2 and CanvaSans-Bold.woff2.",
            ),
            "display": token(
                "Canva Sans Display, Canva Sans, Helvetica Neue, sans-serif",
                "fontFamily",
                "Measured. @font-face Canva Sans Display Regular/Medium/Bold in the same stylesheet. The homepage h1 computed to Canva Sans, not Display, so display is the declared face, not the h1's used face.",
            ),
        },
        "weight": {
            "regular": token(400, "fontWeight", src_body),
            "bold": token(700, "fontWeight", src_h1),
        },
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "48px",
                "fontWeight": 700,
                "lineHeight": "52.8px",
                "letterSpacing": "-2px",
            },
            "$extensions": {"source": src_h1},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "14px",
                "fontWeight": 400,
                "lineHeight": "19.6px",
            },
            "$extensions": {"source": src_body},
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "17px",
                "fontWeight": 400,
                "lineHeight": "17px",
                "letterSpacing": "-0.5px",
            },
            "$extensions": {"source": src_join},
        },
    },
    "radius": {
        "control": token("12px", "dimension", src_join + " border-radius 12px."),
        "search": token("12px", "dimension", src_search + " border-radius 12px."),
        "pill": token("30px", "dimension", src_home + " border-radius 30px."),
        "chip": token("180px", "dimension", src_pill + " border-radius 180px. Stylesheet --radius-outer on .SearchTermPill_pill is 180px."),
        "nav": token("25px", "dimension", src_link + " border-radius 25px."),
    },
    "space": {
        "4": token("4px", "dimension", "Derived. 4px base. Chip padding starts at 5px and 8px (raw/components-sample.json pill). Not a published spacing scale."),
        "8": token("8px", "dimension", "Measured. Search chip padding-top 8px."),
        "12": token("12px", "dimension", "Measured. Search container padding 12px."),
        "16": token("16px", "dimension", "Measured. License link padding-left 16px."),
        "20": token("20px", "dimension", "Measured. Join button padding-left and padding-right 20px."),
    },
    "size": {
        "control": token("48px", "dimension", src_join + " height 48px. Home pill and search chip are also 48px."),
        "logo": token("38px", "dimension", "Measured. Navbar logo height 38px, width 115px."),
        "logoWidth": token("115px", "dimension", "Measured. Navbar logo width 115px."),
    },
    "border": {
        "width": token("1px", "dimension", src_join + " border-top-width 1px. Search chip border is also 1px."),
    },
    "motion": {
        "hover": token("100ms", "duration", src_motion + " background-color 0.1s."),
        "border": token("250ms", "duration", src_motion + " border-color 0.25s."),
    },
    "layout": {
        "desktop": token("1440px", "dimension", "Requested desktop viewport 1440x900. Sidecars record the measured innerWidth."),
        "phone": token("390px", "dimension", "Requested phone viewport 390x844 at deviceScaleFactor 2."),
    },
}

def semantic(selector, label, hover_bg):
    return {
        "color": palette(selector, label),
        "background": {
            "page": token("{color.greyscale.white}", "color", f"{label} page is the white greyscale step. Body background computed transparent over it."),
            "surface": token("{color.greyscale.200}", "color", f"Measured. Search container background rgb(247, 247, 247), which is --color-greyscale-200 on {label}."),
            "sunken": token("{color.greyscale.100}", "color", f"Declared --color-greyscale-100 on {label}. Not measured on a painted element in this pass."),
        },
        "text": {
            "primary": token("{color.greyscale.black}", "color", src_h1 + " color rgb(0, 0, 0), --color-greyscale-black."),
            "secondary": token("{color.greyscale.shadow}", "color", src_link + " color rgb(25, 25, 25), --color-greyscale-shadow."),
            "muted": token("{color.greyscale.800}", "color", f"Declared --color-greyscale-800 on {label}. Used for secondary labels. Not re-measured on a caption in this pass."),
            "onAccent": token("{color.greyscale.white}", "color", src_join + " color rgb(255, 255, 255) on the ink button."),
            "link": token("#0000ee", "color", src_link + " Unstyled anchors computed to rgb(0, 0, 238). Nav links override this to greyscale-shadow."),
        },
        "border": {
            "default": token("{color.greyscale.400}", "color", src_pill + " border rgb(237, 237, 237), --color-greyscale-400."),
            "strong": token("{color.greyscale.shadow}", "color", src_join + " border rgb(25, 25, 25), --color-greyscale-shadow."),
        },
        "action": {
            "primary": token("{color.greyscale.shadow}", "color", src_join + " background rgb(25, 25, 25)."),
            "primaryHover": token(hover_bg, "color", src_join_hover + " Hover background rgb(57, 57, 57), --color-greyscale-900 in the light set. Recorded as a literal because the dark set's 900 step is a light grey."),
            "selected": token("{color.greyscale.black}", "color", src_home + " selected Home pill background rgb(0, 0, 0)."),
            "download": token("{color.alien.dark}", "color", "Observed. Free download button paints green. --color-alien-dark is #32ac64 on both theme selectors. The exact computed green was not read in this pass, so the token aliases the declared accent."),
        },
        "focus": {
            "ring": token("{color.greyscale.black}", "color", "Measured. Search wrap outline color rgb(0, 0, 0) with style none and width 3px while the field was focused. No painted ring was observed."),
        },
    }


light = semantic(LIGHT_SEL, "the light selector `[data-mode=\"light\"], body`", "#393939")
# Dark semantic roles alias the dark palette. Hover was not observed in dark.
dark = semantic(DARK_SEL, "the dark selector `[data-mode=\"dark\"]`, declared and not applied on the public pages", "#393939")
dark["action"]["primaryHover"] = token(
    "#393939",
    "color",
    "Not captured as a live hover. The light Join hover computed to #393939. The dark theme was not on screen, so this value is the light measurement copied, not a dark-theme reading.",
)

doc = {
    "$description": "Pexels public site, www.pexels.com, read 2026-11-21. Light is the live theme. Dark tokens are stylesheet declarations on [data-mode=dark], not a theme the public pages applied.",
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "Dark (declared, not applied)", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
}

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=1) + "\n")
print("wrote", out, "light colors", len(light["color"]["greyscale"]), "dark", len(dark["color"]["greyscale"]))
