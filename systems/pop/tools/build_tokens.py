#!/usr/bin/env python3
"""Build tokens.json from Pop's public readings.

Sources, read from https://pop.site/ on 2026-11-21, signed out, 1440x900:
  raw/css-vars.json            Framer --token-* colours declared on body, plus @font-face families
  raw/components-computed.json computed styles of the public controls
  raw/extra-readings.json      the claim button's gradient (backgroundImage) and the hero sub colour

Framer names its colours as --token-<uuid>. Those names are not a semantic system,
so core.color records the distinct declared values and light.* aliases the ones
a captured control actually paints. The site paints one light theme. The dark set
is empty and is not listed in $themes.

Every token carries $extensions.source. Unread roles stay out of the file and are
listed as Not captured in the README. Deterministic: same inputs, same bytes.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components-computed.json").read_text())["components"]
EXTRA = json.loads((RAW / "extra-readings.json").read_text())

# Declared Framer colours, from the body rule the CSSOM returned. The uuid names
# are Framer's; the values are what the stylesheet writes.
DECLARED = {
    "#3b82f6": "--token-0b12ad74-9094-410e-935d-51b5c5537668",
    "#ffffff": "--token-15ca1af0-2da4-4bbd-9f08-3fc0f29b6d8b",
    "#fafafc": "--token-fa705767-5e35-486a-bb40-ab4d203a212e",
    "#e3e3e3": "--token-a1f53698-a178-4eb8-9899-2999dea13655",
    "#d2d2d7": "--token-29dd526f-4234-4459-9db5-a1733fe58a26",
    "#6e6e73": "--token-66acd1d2-52d6-4a61-bf7e-f53145f51819",
    "#171717": "--token-4da5a6b8-0988-4de4-b536-2545a7e0ca93",
    "#478eff": "--token-51154332-dea8-4968-a246-7ef834ce1e02",
    "#2222221a": "--token-27624316-603b-43f0-8d23-774029505797",
    "#ffed90": "--token-a8970b24-0404-4f8d-b99b-2f43e1b745c0",
    "#00276b": "--token-57da7360-b622-4a78-9f9e-6ac7cf96d64f",
    "#fdfdfd": "--token-6c8d10ba-463b-4990-b64f-32918ca2d4f2",
    "#dedede": "--token-7e7d9213-6afe-4309-afa8-7dccf478cb0d",
    "#000000": "--token-6e6e337d-28cc-44d1-a0da-bb7b5b6c59e1",
    "#545454": "--token-66b6d7ff-ba33-4d69-8906-b2633b6d4a86",
    "#bdbdbd": "--token-95a8f7e0-de26-4a21-abd8-7324f048c094",
    "#474d50": "--token-778dc32c-fa91-4f86-8154-267d5648c0d5",
    "#00a8f5": "--token-271ffd78-22b3-4fe7-958b-4f72926745f7",
}


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def font_w(value, source):
    return {"$value": value, "$type": "fontWeight", "$extensions": {"source": source}}


def text_style(family, size, weight, line, tracking, source):
    return {
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
            "letterSpacing": tracking,
        },
        "$type": "typography",
        "$extensions": {"source": source},
    }


def alias(path, source):
    return {"$value": "{" + path + "}", "$type": "color", "$extensions": {"source": source}}


def st(name, state="default"):
    return COMP[name]["states"][state]


INK = "Satoshi, sans-serif"
SANS = "Inter, sans-serif"
MONO = '"Fragment Mono", ui-monospace, monospace'

doc = {
    "core": {
        "color": {
            "blue": {
                "500": color("#3b82f6", "declared " + DECLARED["#3b82f6"] + " on body (raw/css-vars.json); also the end stop of claim-button backgroundImage"),
                "400": color("#478eff", "declared " + DECLARED["#478eff"] + " on body (raw/css-vars.json). Not painted on a captured control"),
                "sky": color("#00a8f5", "declared " + DECLARED["#00a8f5"] + " on body; start stop of claim-button backgroundImage (raw/extra-readings.json)"),
                "ink": color("#00276b", "declared " + DECLARED["#00276b"] + " on body (raw/css-vars.json). Not painted on a captured control"),
            },
            "ink": {
                "900": color("#171717", "declared " + DECLARED["#171717"] + " on body; computed color of nav-link default"),
                "700": color("#545454", "declared " + DECLARED["#545454"] + " on body; computed color of the hero sub line (raw/extra-readings.json)"),
                "500": color("#6e6e73", "declared " + DECLARED["#6e6e73"] + " on body; computed color of nav-link hover"),
                "400": color("#474d50", "declared " + DECLARED["#474d50"] + " on body; computed ::placeholder color of claim-field"),
            },
            "neutral": {
                "0": color("#ffffff", "declared " + DECLARED["#ffffff"] + " on body; computed backgroundColor of page-ground"),
                "50": color("#fdfdfd", "declared " + DECLARED["#fdfdfd"] + " on body (raw/css-vars.json). Not painted on a captured control"),
                "100": color("#fafafc", "declared " + DECLARED["#fafafc"] + " on body; computed backgroundColor of claim-suffix"),
                "200": color("#e3e3e3", "declared " + DECLARED["#e3e3e3"] + " on body (raw/css-vars.json). Not painted on a captured control"),
                "300": color("#dedede", "declared " + DECLARED["#dedede"] + " on body (raw/css-vars.json). Not painted on a captured control"),
                "400": color("#d2d2d7", "declared " + DECLARED["#d2d2d7"] + " on body (raw/css-vars.json). Not painted on a captured control"),
                "500": color("#bdbdbd", "declared " + DECLARED["#bdbdbd"] + " on body (raw/css-vars.json). Not painted on a captured control"),
            },
            "yellow": color("#ffed90", "declared " + DECLARED["#ffed90"] + " on body (raw/css-vars.json). Not painted on a captured control"),
            "black": color("#000000", "declared " + DECLARED["#000000"] + " on body; computed color of page-ground"),
            "scrim": color("rgba(34, 34, 34, 0.102)", "declared " + DECLARED["#2222221a"] + " on body as #2222221a. Not painted on a captured control"),
            "focus": color("#005fcc", "computed outlineColor of nav-link focus-visible. Chromium's auto outline, not a declared token"),
            "go-home": color("#3b82f6", "computed backgroundColor of the 404 Go home link on /enterprise. Flat fill, not the claim gradient"),
            "on-accent": color("#ffffff", "computed color of the claim-button text node (raw/components-computed.json textStyle)"),
        },
        "font": {
            "sans": {"$value": INK, "$type": "fontFamily", "$extensions": {"source": "computed fontFamily of nav-link default, Satoshi Placeholder dropped"}},
            "text": {"$value": SANS, "$type": "fontFamily", "$extensions": {"source": "computed fontFamily of the article-card title text node, Inter Placeholder dropped"}},
            "mono": {"$value": MONO, "$type": "fontFamily", "$extensions": {"source": "@font-face Fragment Mono in raw/css-vars.json. Not used by a captured control"}},
        },
        "typography": {
            "display": text_style(INK, "69px", 500, "62.1px", "-3.92px", "computed style of display-heading default (pricing h1; home h1 matches)"),
            "body": text_style(INK, "21px", 500, "29.4px", "-0.63px", "computed style of the hero sub line (raw/extra-readings.json)"),
            "label": text_style(INK, "15px", 500, "19.5px", "-0.45px", "computed style of nav-link default"),
            "button": text_style(INK, "15px", 500, "19.5px", "-0.45px", "computed textStyle of claim-button default"),
            "caption": text_style(INK, "13px", 400, "15.6px", "-0.39px", "computed style of footer-link default"),
            "question": text_style(SANS, "18px", 500, "25.2px", "-0.72px", "computed textStyle of faq-question default"),
            "card-title": text_style(SANS, "16px", 600, "22.4px", "-0.32px", "computed textStyle of article-card default"),
            "field": text_style(INK, "15px", 500, "18px", "-0.15px", "computed style of claim-field default"),
        },
        "radius": {
            "sm": dim("4px", "computed borderRadius of privacy-checkbox default"),
            "md": dim("10px", "computed borderRadius of privacy-submit default"),
            "pill": dim("26px", "computed borderRadius of claim-button default"),
            "go-home": dim("16px", "computed borderRadius of the 404 Go home link"),
            "full": dim("9999px", "computed borderRadius of claim-suffix default (the right-hand pill end)"),
        },
        "space": {
            "3": dim("12px", "computed paddingLeft of claim-suffix default"),
            "4": dim("16px", "computed paddingTop of claim-button default"),
            "5": dim("20px", "computed paddingRight of claim-suffix default"),
            "6": dim("24px", "computed paddingLeft of claim-button default"),
        },
        "size": {
            "control": dim("40px", "computed height of claim-button default"),
            "checkbox": dim("16px", "computed width of privacy-checkbox default"),
            "logo": dim("24px", "computed height of logo default"),
        },
    },
    "light": {
        "page": alias("color.neutral.0", "computed backgroundColor of page-ground default"),
        "surface": alias("color.neutral.100", "computed backgroundColor of claim-suffix default"),
        "text": alias("color.ink.900", "computed color of nav-link default"),
        "muted": alias("color.ink.700", "computed color of the hero sub line"),
        "accent": alias("color.blue.500", "end stop of claim-button backgroundImage; declared body token"),
        "border": alias("color.ink.500", "computed color of nav-link hover, the only border-like shift the public controls show"),
        "focus": alias("color.focus", "computed outlineColor of nav-link focus-visible"),
        "component": {
            "button": {
                "radius": dim("26px", "computed borderRadius of claim-button default"),
                "height": dim("40px", "computed height of claim-button default"),
                "pad-x": dim("24px", "computed paddingLeft of claim-button default"),
                "pad-y": dim("16px", "computed paddingTop of claim-button default"),
            },
            "field": {
                "height": dim("40px", "computed height of claim-field default"),
            },
        },
    },
    "dark": {},
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
}

# The claim gradient is not a single colour. Record it beside the accent so a
# reader can see both stops without inventing a gradient token type the checks reject.
doc["light"]["$extensions"] = {
    "notTokenised": [
        {
            "name": "claim-button.backgroundImage",
            "value": EXTRA["claimBgImage"],
            "reason": "A two-stop gradient. The stops are core.color.blue.sky and core.color.blue.500. DTCG colour tokens here stay flat.",
        }
    ]
}

(HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
print("wrote tokens.json")
