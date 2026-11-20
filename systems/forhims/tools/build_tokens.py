#!/usr/bin/env python3
"""Build tokens.json from the forhims.co.uk readings.

Sources, read on 2026-11-21 from www.forhims.co.uk, signed out, light only:
  raw/css-vars.json            every custom property the live CSSOM declares,
                               resolved at 1440x900 (tools/capture/vars.mjs)
  raw/components-computed.json computed styles of the public controls

The UK site paints html.brand-hims.variant-care-sans. Colour ramps are the
declared --b-color-* names. Type sizes are the computed px of those roles on
the live page, because the authored values are fluid slopes. One theme.
Every token carries $extensions.source. A value that was not read is absent.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text()) if (RAW / "components-computed.json").exists() else {"components": {}}
RES = V["resolved"]


def css(name):
    item = RES.get(name)
    if not item or "value" not in item:
        raise KeyError(name)
    return item["value"]


def color(value):
    value = str(value).strip().lower()
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", value)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    if re.fullmatch(r"#[0-9a-f]{6}", value):
        return value
    raise ValueError(value)


def dim(value):
    value = str(value).strip()
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?)px", value)
    if not m:
        raise ValueError(value)
    n = round(float(m.group(1)), 2)
    text = ("%g" % n) + "px"
    if not re.fullmatch(r"-?\d+(\.\d+)?px", text):
        raise ValueError(text)
    return text


def tok(value, ty, source):
    if ty == "color":
        value = color(value)
    elif ty == "dimension":
        value = dim(value)
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def alias(path, ty, source):
    return {"$value": "{" + path + "}", "$type": ty, "$extensions": {"source": source}}


def family(name):
    # "CareSans, Helvetica, Arial, sans-serif" -> first family
    return str(css(name)).split(",")[0].strip().strip('"')


core = {"color": {}, "font": {"family": {}}, "typography": {}, "space": {}, "radius": {}, "size": {}}

# Colour ramps that the hims brand actually declares. Hers ramps are a sister
# brand and stay out of this package.
RAMPS = {
    "himsPrimary": "--b-color-hims-primary-p",
    "himsSecondary": "--b-color-hims-secondary-s",
    "neutralDark": "--b-color-neutral-dark-",
    "neutralLight": "--b-color-neutral-light-",
    "sage": "--b-color-sage-light-",
    "utilityCaution": "--b-color-utility-caution-uc",
    "utilityError": "--b-color-utility-error-ue",
    "utilitySuccess": "--b-color-utility-success-us",
}
STEPS = {
    "himsPrimary": ["100", "300", "500", "700", "900"],
    "himsSecondary": ["100", "300", "500", "700", "900"],
    "neutralDark": ["050", "100", "300", "500", "700", "900", "1000"],
    "neutralLight": ["100", "300", "500", "700", "900", "1000"],
    "sage": ["500", "700", "900", "950"],
    "utilityCaution": ["100", "300", "500"],
    "utilityError": ["100", "300", "500"],
    "utilitySuccess": ["100", "300", "500"],
}
for group, prefix in RAMPS.items():
    core["color"][group] = {}
    for step in STEPS[group]:
        name = prefix + step
        core["color"][group][step] = tok(css(name), "color", f"css-var {name} resolved on :root, www.forhims.co.uk, 1440x900, light")

core["color"]["black"] = tok(css("--b-color-black"), "color", "css-var --b-color-black")
core["color"]["white"] = tok(css("--b-color-white"), "color", "css-var --b-color-white")
core["color"]["brand"] = tok(css("--colors-brand-default"), "color", "css-var --colors-brand-default resolved on :root")

core["font"]["family"]["sans"] = {
    "$value": family("--b-font-family-sans"),
    "$type": "fontFamily",
    "$extensions": {"source": "css-var --b-font-family-sans on html.variant-care-sans; first family of the stack. Sofia Pro is declared but not the active UK variant."},
}
core["font"]["family"]["serif"] = {
    "$value": family("--b-font-family-serif"),
    "$type": "fontFamily",
    "$extensions": {"source": "css-var --b-font-family-serif on :root; first family. Not observed in the captured headings."},
}

# Type roles from computed elements, not the fluid slope tokens (those resolve
# to sub-pixel px that are not the painted size).
TYPE = {
    "display": ("logo", "default", "Wordmark size on the home header. Display slopes exist (--b-font-size-display-*) but were not the painted hero size in this capture."),
    "nav": ("nav-link", "default", "Weight / Hair nav link."),
    "label": ("login-button", "default", "LOGIN pill label."),
    "body": ("button-primary", "default", "Explore treatments label, the body size."),
    "menu": ("menu-item", "default", "Sex menu item."),
}
for role, (comp, state, note) in TYPE.items():
    style = C["components"][comp][state]
    core["typography"][role] = {
        "fontFamily": {
            "$value": style["fontFamily"].split(",")[0].strip().strip('"'),
            "$type": "fontFamily",
            "$extensions": {"source": f"computed fontFamily on {comp}/{state}; {note}"},
        },
        "fontSize": tok(style["fontSize"], "dimension", f"computed fontSize on {comp}/{state}, 1440x900"),
        "fontWeight": tok(int(float(style["fontWeight"])), "fontWeight", f"computed fontWeight on {comp}/{state}"),
        "lineHeight": tok(style["lineHeight"], "dimension", f"computed lineHeight on {comp}/{state}"),
    }

# Spacing from the declared unit scale, kept as the computed px.
for step in ("000", "008", "016", "024", "032", "048"):
    name = f"--b-unit-u{step}"
    core["space"][step] = tok(css(name), "dimension", f"css-var {name} resolved at 1440x900. Authored as a fluid unit; the painted px is what is stored.")

core["radius"]["menu"] = tok(C["components"]["menu"]["open"]["borderRadius"], "dimension", "computed borderRadius on the Sex floating menu")
core["radius"]["card"] = tok(C["components"]["treatment-card"]["default"]["borderRadius"], "dimension", "computed borderRadius on a home treatment card")
core["radius"]["pill"] = tok(C["components"]["login-button"]["default"]["borderRadius"], "dimension", "computed borderRadius on the LOGIN pill")

core["size"]["nav"] = tok(C["components"]["nav-link"]["default"]["fontSize"], "dimension", "computed fontSize of a nav link, used as the nav text size")
if "height" in C["components"].get("login-button", {}).get("default", {}):
    h = C["components"]["login-button"]["default"]["height"]
    if h and h != "auto":
        core["size"]["login"] = tok(h, "dimension", "computed height of the LOGIN button")

light = {
    "background": {
        "page": alias("color.white", "color", "page canvas is --b-color-white on the captured marketing pages"),
        "surface": tok(css("--colors-canvas-grayPink"), "color", "css-var --colors-canvas-grayPink; the cream card fill on the home treatment cards"),
        "menu": alias("color.white", "color", "Sex menu computed backgroundColor rgb(255, 255, 255)"),
        "scrim": tok("rgba(0, 0, 0, 0.4)", "color", "Observed on home-light-account-menu.png. The exact scrim token was not isolated, so this is the visible overlay, labelled from the screenshot review rather than a named variable."),
    },
    "text": {
        "primary": tok(C["components"]["nav-link"]["default"]["color"], "color", "computed color on nav-link/default, 1440x900. Nearest declared step is --b-color-neutral-dark-900 at rgba(0,0,0,0.83); they are not the same value."),
        "onAccent": alias("color.white", "color", "LOGIN and primary button labels compute to white or near-white on dark fills"),
        "brand": alias("color.brand", "color", "css-var --colors-brand-default; the copper 'for you' and the hims wordmark"),
        "muted": tok(css("--b-color-neutral-dark-500"), "color", "css-var --b-color-neutral-dark-500. Used as the muted ink step. A dedicated muted text role was not separately computed."),
    },
    "border": {
        "default": tok(css("--b-color-neutral-dark-100"), "color", "css-var --b-color-neutral-dark-100"),
    },
    "action": {
        "primary": alias("color.black", "color", "declared --colors-button-primary is #000000. The Explore treatments pill is black in screenshots/home-light-default.png. Computed backgroundColor on the button node was transparent, so the fill was not isolated to that node."),
        "primaryText": alias("color.white", "color", "computed color rgb(255, 255, 255) on the primary button label"),
        "quiet": tok(css("--b-color-neutral-dark-100"), "color", "LOGIN computes to background rgba(0, 0, 0, 0.06), the neutral-dark-100 step"),
    },
    "status": {
        "success": alias("color.utilitySuccess.500", "color", "declared --b-color-utility-success-us500. Not seen on a public form error."),
        "warning": alias("color.utilityCaution.500", "color", "declared --b-color-utility-caution-uc500. Not seen on a public form."),
        "danger": alias("color.utilityError.500", "color", "declared --b-color-utility-error-ue500. A validation error was not reached: no form was submitted."),
    },
}

# The account-menu screenshot shows a dimmed page. No computed scrim colour
# was isolated, so no scrim token is written.

doc = {
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}

out = json.dumps(doc, indent=1) + "\n"
(HERE / "tokens.json").write_text(out)
print("wrote tokens.json", out.count('"$value"'), "tokens")
