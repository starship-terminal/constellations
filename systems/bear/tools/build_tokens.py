#!/usr/bin/env python3
"""Build systems/bear/tokens.json from raw/elements.json.

Every colour is the computed rgb from that file, written as hex or rgba.
Lengths are the computed px strings. The script does not keep a second copy
of the numbers.

    python3 tools/build_tokens.py
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw" / "elements.json"
CAPTURE = "raw/elements.json getComputedStyle https://bear.app/ 2026-11-22 signed out"


def rgb_to_value(rgb):
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)(?:\s*,\s*([\d.]+))?\s*\)", rgb.strip())
    if not m:
        raise SystemExit(f"not a computed rgb: {rgb!r}")
    parts = [int(round(float(m.group(i)))) for i in (1, 2, 3)]
    alpha = m.group(4)
    if alpha is None or float(alpha) == 1:
        return "#" + "".join(f"{n:02x}" for n in parts)
    if float(alpha) == 0:
        return "transparent"
    return f"rgba({parts[0]}, {parts[1]}, {parts[2]}, {float(alpha)})"


def tok(value, typ, desc, capture=CAPTURE):
    return {
        "$value": value,
        "$type": typ,
        "$description": desc,
        "$extensions": {"source": {"evidence": "Measured", "capture": capture}},
    }


def alias(path, typ, desc):
    return {
        "$value": "{" + path + "}",
        "$type": typ,
        "$description": desc,
        "$extensions": {"source": {"evidence": "Derived", "capture": CAPTURE}},
    }


def color_from(rgb, desc):
    return tok(rgb_to_value(rgb), "color", desc)


def main():
    data = json.loads(RAW.read_text())
    home = data["home"]
    els = home["elements"]
    vars_ = home["vars"]
    states = data["states"]
    features = {row["text"]: row for row in home["featureH2"]}
    tags = home["proTags"]
    gold = next(t for t in tags if t["parent"] == "list")
    sky = next(t for t in tags if "more-info" in t["parent"])
    red = next(t for t in tags if t["backgroundColor"] == vars_["--accent-color"]["computedColor"])

    def var_color(name, desc):
        row = vars_[name]
        value = rgb_to_value(row["computedColor"])
        return tok(value, "color", f"{desc} Declared {row['raw']}, computed {row['computedColor']}.")

    core = {
        "color": {
            "paper": var_color("--background-color", "Page white. Nav background computed the same rgb."),
            "mist": var_color("--background-secondary-color", "Secondary surface. Feature cards and faq code paint this rgb."),
            "fog": var_color("--background-tertiary-color", "Tertiary surface. Community active row paints this rgb."),
            "ink": var_color("--text-color", "Body, headings, nav links, and the price."),
            "muted": var_color("--text-secondary-color", "Subtitle, price period, and footer copyright."),
            "hairline": var_color("--stroke-color", "Declared stroke. No homepage control painted a 1px border in this colour."),
            "accent": var_color("--accent-color", "Subscribe fill, inline links, community ribbon, default PRO tag."),
            "on-accent": color_from(els["button"]["color"], "Computed text on a.link-button."),
            "markdown": color_from(features["Seamless Markdown"]["color"], "Computed colour on the Seamless Markdown heading."),
            "organize": color_from(features["Organize easily"]["color"], "Computed colour on the Organize easily heading."),
            "beauty": color_from(features["Universal beauty"]["color"], "Computed colour on the Universal beauty heading."),
            "gold": color_from(gold["backgroundColor"], "Computed background on the feature-list PRO tag."),
            "sky": color_from(sky["backgroundColor"], "Computed background on the more-info PRO tag."),
            "offer": color_from(els["offer"]["backgroundColor"], "Computed background on the yearly offer badge."),
            "focus": color_from(states["link"]["focus"]["outlineColor"], "Computed outline colour on a focused nav link. Browser default."),
        },
        "font": {
            "family": {
                "body": tok(els["body"]["fontFamily"] + ", sans-serif", "fontFamily", "Computed font-family on body, plus a generic fallback."),
                "heading": tok(els["h1"]["fontFamily"] + ", sans-serif", "fontFamily", "Computed font-family on h1, plus a generic fallback."),
                "code": tok(data["code"]["fontFamily"] + ", ui-monospace, monospace", "fontFamily", "Computed font-family on faq code, plus generic fallbacks."),
            },
            "weight": {
                "regular": tok(els["body"]["fontWeight"], "fontWeight", "Computed font-weight on body."),
                "bold": tok(els["storyTitle"]["fontWeight"], "fontWeight", "Computed font-weight on .community-story-title and .pro-tag."),
            },
            "size": {
                "body": tok(els["body"]["fontSize"], "dimension", "Computed font-size on body."),
                "nav": tok(els["navLink"]["fontSize"], "dimension", "Computed font-size on a nav link."),
                "button": tok(els["button"]["fontSize"], "dimension", "Computed font-size on a.link-button."),
                "subtitle": tok(els["subtitle"]["fontSize"], "dimension", "Computed font-size on .subtitle."),
                "feature": tok(features["Seamless Markdown"]["fontSize"], "dimension", "Computed font-size on a feature h2."),
                "display": tok(els["h1"]["fontSize"], "dimension", "Computed font-size on h1 at 1440."),
                "display-narrow": tok(data["phone"]["h1FontSize"], "dimension", "Computed font-size on h1 at 390 CSS px."),
                "price": tok(els["price"]["fontSize"], "dimension", "Computed font-size on .price-tier-price."),
                "period": tok(els["period"]["fontSize"], "dimension", "Computed font-size on .price-tier-period."),
                "offer": tok(els["offer"]["fontSize"], "dimension", "Computed font-size on .price-tier-offer."),
                "story": tok(els["storyTitle"]["fontSize"], "dimension", "Computed font-size on .community-story-title."),
                "code": tok(data["code"]["fontSize"], "dimension", "Computed font-size on faq code."),
            },
            "line-height": {
                "body": tok(els["body"]["lineHeight"], "dimension", "Computed line-height on body."),
                "heading": tok(els["h1"]["lineHeight"], "dimension", "Computed line-height on h1."),
                "subtitle": tok(els["subtitle"]["lineHeight"], "dimension", "Computed line-height on .subtitle."),
            },
            "letter-spacing": {
                "button": tok(els["button"]["letterSpacing"], "dimension", "Computed letter-spacing on a.link-button."),
            },
        },
        "radius": {
            "none": tok(els["navLink"]["borderRadius"], "dimension", "Computed border-radius on a nav link."),
            "tag": tok(gold["borderRadius"], "dimension", "Computed border-radius on the 16px PRO tag."),
            "offer": tok(els["offer"]["borderRadius"], "dimension", "Computed border-radius on the offer badge."),
            "button": tok(els["button"]["borderRadius"], "dimension", "Computed border-radius on a.link-button."),
            "ribbon": tok(els["ribbon"]["borderRadius"], "dimension", "Computed border-radius on .community-story-ribbon."),
            "card": tok(els["card"]["borderRadius"], "dimension", "Computed border-radius on .more-info-block."),
            "code": tok(data["code"]["borderRadius"], "dimension", "Computed border-radius on faq code."),
        },
        "space": {
            "nav": tok(els["nav"]["height"], "dimension", "Computed height of nav.navigation."),
            "button-y": tok(els["button"]["padding"].split()[0], "dimension", "Computed block padding on a.link-button."),
            "button-x": tok(els["button"]["padding"].split()[1], "dimension", "Computed inline padding on a.link-button."),
            "wrapper": tok(els["wrapper"]["padding"].split()[1], "dimension", "Computed inline padding on .wrapper."),
            "column": tok(els["wrapper"]["maxWidth"], "dimension", "Computed max-width on .wrapper."),
        },
        "shadow": {
            "none": tok(els["button"]["boxShadow"], "shadow", "Computed box-shadow on a.link-button, the nav, and cards."),
        },
    }
    # The nav's measured background must match the paper token, or the page role is wrong.
    paper = core["color"]["paper"]["$value"]
    nav_bg = rgb_to_value(els["nav"]["backgroundColor"])
    if nav_bg != paper:
        raise SystemExit(f"nav background {nav_bg} does not match --background-color {paper}")
    if data["dark"]["body"] != els["body"]["color"] or data["dark"]["button"] != els["button"]["backgroundColor"]:
        raise SystemExit("dark emulation changed paints; a dark set is required")

    light = {
        "page": alias("color.paper", "color", "Nav paints this white. Body and html backgrounds computed transparent."),
        "surface": alias("color.mist", "color", "Feature cards and code chips."),
        "surface-selected": alias("color.fog", "color", "Declared tertiary background."),
        "text": alias("color.ink", "color", "Body and headings."),
        "muted": alias("color.muted", "color", "Subtitle and copyright."),
        "accent": alias("color.accent", "color", "Subscribe button and inline links."),
        "on-accent": alias("color.on-accent", "color", "Text on the accent button."),
        "border": alias("color.hairline", "color", "Declared stroke."),
        "focus": alias("color.focus", "color", "Focus outline."),
        "link": alias("color.accent", "color", "Inline link colour matches the accent."),
        "component": {
            "button": {
                "background": alias("color.accent", "color", "Subscribe."),
                "text": alias("color.on-accent", "color", "Subscribe."),
                "radius": alias("radius.button", "dimension", "Subscribe."),
                "padding-y": alias("space.button-y", "dimension", "Subscribe."),
                "padding-x": alias("space.button-x", "dimension", "Subscribe."),
            },
            "nav": {
                "background": alias("color.paper", "color", "Fixed nav."),
                "text": alias("color.ink", "color", "Nav links."),
                "height": alias("space.nav", "dimension", "Nav."),
            },
            "card": {
                "background": alias("color.mist", "color", "More-info card."),
                "radius": alias("radius.card", "dimension", "More-info card."),
                "text": alias("color.ink", "color", "Card title."),
            },
            "tag": {
                "background": alias("color.gold", "color", "Feature-list PRO tag. Other PRO tags paint sky or accent."),
                "text": alias("color.on-accent", "color", "PRO tag."),
                "radius": alias("radius.tag", "dimension", "PRO tag."),
            },
        },
    }
    doc = {
        "core": core,
        "light": light,
        "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
        "$metadata": {
            "tokenSetOrder": ["core", "light"],
            "product": "Bear",
            "captured": data["capturedAt"],
            "source": "https://bear.app/ signed out. No dark set: prefers-color-scheme dark did not change computed paints.",
        },
    }
    text = json.dumps(doc, indent=2) + "\n"
    (HERE / "tokens.json").write_text(text)
    print(f"wrote tokens.json ({text.count(chr(10))} lines)")


if __name__ == "__main__":
    main()
