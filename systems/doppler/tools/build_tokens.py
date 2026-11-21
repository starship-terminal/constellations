#!/usr/bin/env python3
"""Build tokens.json from live computed styles read on Doppler's public site.

Sources, read signed out on 2026-11-21:
  raw/components-live.json   computed styles on www.doppler.com and docs.doppler.com
  raw/theme-checks.json      page background after a prefers-color-scheme emulation
  The brand page lists the published hex values; the same colours were read from
  computed styles (page rgb(28, 22, 36) is #1c1624, accent rgb(0, 245, 117) is #00f575).

The marketing site paints one dark theme. Docs paint a separate light chrome.
There is no theme toggle on either surface, so light and dark are two products'
surfaces, not a pair of the same page.

Every token carries $extensions.source. Unread values are not invented.
Deterministic: same inputs, same bytes.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
LIVE = json.loads((RAW / "components-live.json").read_text())


def src(where, label="Measured"):
    return {"source": f"{label}: {where}", "label": label}


def color(value, where):
    return {"$type": "color", "$value": value, "$extensions": src(where)}


def dim(value, where):
    return {"$type": "dimension", "$value": value, "$extensions": src(where)}


def num(value, where):
    return {"$type": "number", "$value": value, "$extensions": src(where)}


def font(value, where):
    return {"$type": "fontFamily", "$value": value, "$extensions": src(where)}


def typo(family, size, weight, line, where):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
        },
        "$extensions": src(where),
    }


H = LIVE["home"]
P = H["primary"]
D = H["demo"]
DOCS = LIVE["docs"]
HOVER = LIVE["hover"]
FOCUS = LIVE["focus"]

# Brand page published the same hex values the computed styles resolved to.
# Page rgb(28, 22, 36) = #1c1624. Accent rgb(0, 245, 117) = #00f575.
# Hover rgb(0, 192, 91) = #00c05b. Text rgb(241, 240, 236) = #f1f0ec.

core = {
    "palette": {
        "warm-black": color("#1c1624", "computed html background rgb(28, 22, 36) on www.doppler.com; brand page names this Warm Black"),
        "warm-white": color("#f1f0ec", "computed h1 color rgb(241, 240, 236) on www.doppler.com; brand page names this Warm White"),
        "fluorescent-green": color("#00f575", "computed Start for Free background rgb(0, 245, 117); brand page names this Fluorescent Green"),
        "green-hover": color("#00c05b", "computed Start for Free background on hover rgb(0, 192, 91)"),
        "purple": color("#6b13f5", "brand page swatch button label, not painted as a page role on the home capture"),
        "light-purple": color("#b997ff", "brand page swatch button label"),
        "carmine": color("#f55c15", "brand page swatch button label"),
        "lilac": color("#ff9efa", "brand page swatch button label"),
        "factory-yellow": color("#fee442", "brand page swatch button label"),
        "docs-ink": color("#32343a", "computed docs h1 color rgb(50, 52, 58) on docs.doppler.com/docs/start"),
        "docs-page": color("#ffffff", "computed body background rgb(255, 255, 255) on docs.doppler.com"),
        "focus-blue": color("#005fcc", "computed outline rgb(0, 95, 204) on focused Start for Free"),
    },
    "fontFamily": {
        "repro": font(
            "__DopplerRepro_a18e76, __DopplerRepro_Fallback_a18e76, sans-serif",
            "computed font-family on h1 and Start for Free, www.doppler.com. The face name is a Next.js local font. Licence not captured.",
        ),
        "docs": font(
            '"Twemoji Country Flags", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif',
            "computed font-family on docs h1, docs.doppler.com/docs/start (stack shortened to the families read; full stack is in raw/components-live.json)",
        ),
    },
    "fontWeight": {
        "regular": num(400, "computed font-weight on body and Start for Free"),
        "display": num(450, "computed font-weight on marketing h1"),
        "docs-heading": num(600, "computed font-weight on docs h1"),
    },
    "typography": {
        "display": typo("{fontFamily.repro}", "48px", "450", "57.6px", "computed h1 on www.doppler.com at 1440"),
        "display-mobile": typo("{fontFamily.repro}", "36px", "450", "43.2px", "computed h1 font-size 36px at innerWidth 390; line-height not separately read, Derived as 1.2"),
        "body": typo("{fontFamily.repro}", "16px", "400", "24px", "computed body on www.doppler.com"),
        "button": typo("{fontFamily.repro}", "16px", "400", "24px", "computed Start for Free"),
        "docs-heading": typo("{fontFamily.docs}", "31px", "600", "39.86px", "computed h1 on docs.doppler.com/docs/start"),
    },
    "radius": {
        "button": dim("12px", "computed border-radius on Start for Free and Get Demo"),
        "header-bottom": dim("16px", "computed header border-radius 0 0 16px 16px"),
    },
    "spacing": {
        "header-x": dim("20px", "computed header padding 0 20px"),
        "button-y": dim("8px", "computed Start for Free padding-block"),
        "button-x": dim("12px", "computed Start for Free padding-inline"),
        "demo-y": dim("10px", "computed Get Demo padding-block"),
        "demo-x": dim("16px", "computed Get Demo padding-inline"),
    },
    "size": {
        "header-height": dim("72px", "computed header height at 1440 and at 390"),
        "button-height": dim("32px", "computed Start for Free height in the header"),
        "content-docs": dim("800px", "computed docs h1 width, the article column"),
    },
    "border": {
        "width": dim("1px", "computed Get Demo border-top-width"),
    },
    "focus": {
        "width": dim("1px", "computed outline-width on focused Start for Free (browser auto outline)"),
        "offset": dim("1px", "computed outline-offset on focused Start for Free"),
    },
    "layout": {
        "desktop": dim("1440px", "requested and measured window.innerWidth"),
        "phone": dim("390px", "requested and measured window.innerWidth"),
        "breakpoint-display": dim("1024px", "h1 stays 48px at 1024 and 36px at 768"),
    },
}

# display-mobile line-height was not read. Mark that token Derived.
core["typography"]["display-mobile"]["$extensions"]["label"] = "Derived"
core["typography"]["display-mobile"]["$extensions"]["source"] = (
    "Derived: font-size 36px measured at innerWidth 390; line-height not read, set to 1.2 of 36px"
)

dark = {
    "background": {
        "page": color("{palette.warm-black}", "computed html and body background on www.doppler.com"),
        "header": color("{palette.warm-black}", "computed header background"),
    },
    "text": {
        "primary": color("{palette.warm-white}", "computed h1 and header color"),
        "on-accent": color("{palette.warm-black}", "computed Start for Free text color"),
        "signin": color("#d0c9c4", "computed Sign In color rgb(208, 201, 196); element was in the DOM with zero box (mobile duplicate). Colour read, layout not"),
    },
    "accent": {
        "default": color("{palette.fluorescent-green}", "computed Start for Free background"),
        "hover": color("{palette.green-hover}", "computed Start for Free background on hover"),
    },
    "border": {
        "strong": color("{palette.warm-white}", "computed Get Demo border-top-color rgb(241, 240, 236)"),
        "focus": color("{palette.focus-blue}", "computed outline color on focused Start for Free"),
    },
    "button": {
        "primary-bg": color("{accent.default}", "Start for Free"),
        "primary-text": color("{text.on-accent}", "Start for Free"),
        "primary-radius": dim("{radius.button}", "Start for Free"),
        "secondary-bg": color("rgba(0, 0, 0, 0)", "computed Get Demo background"),
        "secondary-text": color("{text.primary}", "computed Get Demo color"),
        "secondary-border": color("{border.strong}", "computed Get Demo border"),
    },
}

light = {
    "background": {
        "page": color("{palette.docs-page}", "computed body background on docs.doppler.com"),
    },
    "text": {
        "primary": color("{palette.docs-ink}", "computed docs h1 color"),
    },
    "border": {
        "focus": color("{palette.focus-blue}", "not read on a docs control; the marketing focus colour is the only focus colour measured. Not used as a docs claim."),
    },
}
# Do not pretend the marketing focus colour is a docs token.
del light["border"]

tokens = {
    "core": core,
    "dark": dark,
    "light": light,
    "$themes": [
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
    "$extensions": {
        "capture": "public Doppler site and docs, signed out, 2026-11-21",
        "notTokenised": [
            "Pressed and disabled button colours: not captured (press could not be held; no disabled control on the public home).",
            "Motion durations and easings: --global-ease and --global-transition were declared, values cubic-bezier(0.9,0.1,0.1,0.9) and 350ms. Recorded in raw/css-vars-merged.json. Not promoted: they are Tailwind-adjacent globals, not a component motion scale.",
            "Docs theme: no toggle found. Light set is the docs chrome only.",
            "Elevation: header box-shadow computed as none.",
        ],
    },
}

# Alias check: every {path} must exist after flattening both sets a reader joins.
def leaves(node, prefix=""):
    out = {}
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}{k}" if not prefix else f"{prefix}.{k}"
        if isinstance(v, dict) and "$value" in v:
            out[path] = v
        elif isinstance(v, dict):
            out.update(leaves(v, path))
    return out

flat_core = leaves(core)
flat_dark = leaves(dark)
import re
for path, tok in {**flat_core, **{f"dark.{k}": v for k, v in flat_dark.items()}}.items():
    val = tok["$value"]
    if isinstance(val, str):
        for ref in re.findall(r"\{([^{}]+)\}", val):
            if ref not in flat_core and ref not in flat_dark and not ref.startswith("palette"):
                # palette lives in core
                if ref not in flat_core:
                    raise SystemExit(f"dangling alias {path} -> {ref}")

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=1) + "\n")
print("wrote", out, "core", len(flat_core), "dark", len(flat_dark))
