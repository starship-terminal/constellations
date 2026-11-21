#!/usr/bin/env python3
"""Build tokens.json from the FoodNoms public-site readings.

Sources, read from foodnoms.com on 2026-11-21 in headless Chromium:
  raw/type.json     painted text roles and surface fills, light and dark
  raw/spans.json    the Get the App label (the <a> itself is unstyled link chrome)
  raw/measure.json  radii, paddings, motion, focus outline, search scrim

Framer paints in display-p3. A canvas sRGB conversion clips the brand orange
to #ff5407. Tokens keep the P3 channels as #rrggbb (0.972549*255 = 248).
That conversion is Derived. Computed radii, sizes and font stacks are Measured.

One light set and one dark set. The site switches with prefers-color-scheme,
not a class. Deterministic: same inputs, same bytes. Edit the readings, never
tokens.json by hand.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"


def tok(value, ty, source, description=""):
    out = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    if description:
        out["$description"] = description
    return out


def color(value, source, description=""):
    return tok(value, "color", source, description)


def dim(value, source, description=""):
    return tok(value, "dimension", source, description)


# P3 channel * 255, rounded. Recorded so the hex is not a recalled brand colour.
# accent 0.972549, 0.384314, 0.180392 -> #f8622e
SRC_P3 = "derived from computed display-p3 on foodnoms.com 2026-11-21 (raw/type.json); channel*255, not canvas sRGB"
SRC_MEASURED = "computed style on foodnoms.com 2026-11-21 (raw/measure.json, raw/spans.json)"

core = {
    "color": {
        "brand": {
            "accent": color("#f8622e", SRC_P3, "Header wordmark and Get the App fill. display-p3 0.972549 0.384314 0.180392."),
            "yellow": color("#ffbf02", SRC_P3, "Rotating headline 'Lose Weight'. display-p3 1 0.74902 0.007843."),
            "green": color("#4db04f", SRC_P3, "Rotating headline 'Eat Healthy'. display-p3 0.301961 0.690196 0.309804."),
            "red": color("#f13030", SRC_P3, "Rotating headline 'Monitor Sugars'. display-p3 0.945098 0.188235 0.188235."),
            "cyan": color("#1ba6d8", SRC_P3, "Rotating headline 'Stay Hydrated'. display-p3 0.105882 0.65098 0.847059."),
            "slate": color("#7ca1c2", SRC_P3, "Rotating headline 'Reduce Sodium'. display-p3 0.486275 0.631373 0.760784."),
            "orange": color("#f67724", SRC_P3, "Rotating headline 'Build Muscle'. display-p3 0.964706 0.466667 0.141176."),
            "purple": color("#af52de", SRC_P3, "Rotating headline 'Limit Alcohol'. display-p3 0.686275 0.321569 0.870588."),
            "brown": color("#8b561b", SRC_P3, "Rotating headline 'Limit Caffeine'. display-p3 0.545098 0.337255 0.105882."),
        },
        "neutral": {
            "white": color("#ffffff", SRC_P3, "Light page and on-accent text. display-p3 1 1 1."),
            "ink": color("#0d0d0d", SRC_P3, "Light headline remainder. display-p3 0.05098 0.05098 0.05098."),
            "body": color("#333333", SRC_P3, "Light feature body. display-p3 0.2 0.2 0.2."),
            "muted": color("#666666", SRC_P3, "Light nav and lede. display-p3 0.4 0.4 0.4."),
            "muted-dark": color("#999999", SRC_P3, "Dark nav and lede. display-p3 0.6 0.6 0.6."),
            "raised": color("#f2f2f2", SRC_P3, "Light feature card. display-p3 0.94902 0.94902 0.94902."),
            "raised-dark": color("#1a1a1a", SRC_P3, "Dark feature card. display-p3 0.101 0.101 0.101."),
            "black": color("#000000", SRC_P3, "Dark page. display-p3 0 0 0."),
        },
    },
    "font": {
        "family": {
            "display": tok("Aquawax Pro Bold, sans-serif", "fontFamily", SRC_MEASURED, "Headlines. Framer hosts the woff2; not bundled."),
            "label": tok("Aquawax Pro DemiBold, sans-serif", "fontFamily", SRC_MEASURED, "Get the App label."),
            "body": tok("Aquawax Pro Medium, sans-serif", "fontFamily", SRC_MEASURED, "Nav, lede, feature body."),
            "mono": tok("Fragment Mono, ui-monospace, monospace", "fontFamily", "declared @font-face Fragment Mono from fonts.gstatic.com (raw/measure.json fonts)"),
        },
        "weight": {
            "medium": tok(500, "number", SRC_MEASURED),
            "semibold": tok(600, "number", SRC_MEASURED),
            "bold": tok(700, "number", SRC_MEASURED),
        },
    },
    "fontSize": {
        "nav": dim("15px", SRC_MEASURED, "Desktop nav link."),
        "cta": dim("16px", SRC_MEASURED, "Get the App label."),
        "lede": dim("18px", SRC_MEASURED, "Hero lede."),
        "wordmark": dim("24px", SRC_MEASURED, "Header wordmark."),
        "section": dim("28px", SRC_MEASURED, "Feature heading."),
        "display": dim("56px", SRC_MEASURED, "Hero rotating line, desktop 1440."),
    },
    "lineHeight": {
        "nav": dim("15px", SRC_MEASURED),
        "cta": dim("16px", SRC_MEASURED),
    },
    "radius": {
        "pill": dim("20px", SRC_MEASURED, "Get the App, 40px tall so the ends are full pills."),
        "card": dim("25px", "computed border-radius of the feature card and the orange footer (raw/type.json blocks)"),
        "field": dim("40px", SRC_MEASURED, "Newsletter email field, fully rounded at 42px height."),
    },
    "space": {
        "cta-y": dim("12px", SRC_MEASURED, "Get the App padding-block."),
        "cta-x": dim("18px", SRC_MEASURED, "Get the App padding-inline."),
    },
    "size": {
        "control": dim("40px", SRC_MEASURED, "Get the App height."),
        "field": dim("42px", SRC_MEASURED, "Newsletter email field height."),
    },
    "motion": {
        "link": dim("0.4s", SRC_MEASURED, "Nav and footer link color transition."),
    },
    "focus": {
        "width": dim("1px", "computed outline on a focused Get the App link (raw/measure.json): rgb(0, 95, 204) auto 1px"),
    },
}

light = {
    "page": color("{color.neutral.white}", "alias of the light page fill"),
    "surface": color("{color.neutral.raised}", "alias of the light feature card"),
    "text": color("{color.neutral.ink}", "alias of the light headline remainder"),
    "muted": color("{color.neutral.muted}", "alias of the light nav colour"),
    "accent": color("{color.brand.accent}", "alias of the brand orange"),
    "border": color("{color.neutral.muted}", "no dedicated border token; hairlines read as the muted grey"),
    "on-accent": color("{color.neutral.white}", "Get the App label"),
    "footer": color("{color.brand.accent}", "footer band fill, same orange as the accent"),
    "scrim": color("rgba(46, 46, 46, 0.6)", "computed background of the help search overlay (raw/measure.json extra.scrim)"),
    "focus": color("#005fcc", "computed outline-color on a focused link (raw/measure.json)"),
    "component": {
        "button": {
            "bg": color("{color.brand.accent}", "Get the App fill"),
            "text": color("{color.neutral.white}", "Get the App label colour"),
            "radius": dim("{radius.pill}", "Get the App radius"),
            "height": dim("{size.control}", "Get the App height"),
        },
        "field": {
            "bg": color("{color.neutral.raised}", "newsletter email background"),
            "radius": dim("{radius.field}", "newsletter email radius"),
            "height": dim("{size.field}", "newsletter email height"),
        },
    },
}

dark = {
    "page": color("{color.neutral.black}", "alias of the dark page fill, prefers-color-scheme: dark"),
    "surface": color("{color.neutral.raised-dark}", "alias of the dark feature card"),
    "text": color("{color.neutral.raised}", "dark headline remainder, display-p3 0.94902"),
    "muted": color("{color.neutral.muted-dark}", "dark nav colour"),
    "accent": color("{color.brand.accent}", "accent does not change in dark"),
    "border": color("{color.neutral.muted-dark}", "no dedicated dark border; muted grey stands in"),
    "on-accent": color("{color.neutral.white}", "Get the App label stays white"),
    "footer": color("{color.brand.accent}", "footer band stays orange in dark"),
    "scrim": color("rgba(46, 46, 46, 0.6)", "search overlay measured in light; dark overlay not separately sampled"),
    "focus": color("#005fcc", "same UA focus outline as light"),
    "component": {
        "button": {
            "bg": color("{color.brand.accent}", "Get the App fill, unchanged in dark"),
            "text": color("{color.neutral.white}", "Get the App label"),
            "radius": dim("{radius.pill}", "Get the App radius"),
            "height": dim("{size.control}", "Get the App height"),
        },
    },
}

doc = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
    ],
    "$extensions": {
        "source": "foodnoms.com public site, 2026-11-21, headless Chromium, prefers-color-scheme light and dark",
    },
}

(HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", HERE / "tokens.json")
