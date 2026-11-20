#!/usr/bin/env python3
"""Build tokens.json from the Quizlet custom properties read on the signed-in page.

Source: raw/css-vars.json, computed on documentElement while body had theme-night.
Cross-origin stylesheets on assets.quizlet.com were CSSOM-blocked, so these are
resolved custom properties, not parsed declarations. Semantic roles in the night
set are aliases into those ramps, matched to computed styles in
raw/components-computed.json. Light mode was offered and not switched, so there
is no light set.

PRODUCT (adapt): the kit copy of this file still described Claude. This rewrite
reads Quizlet's ramps. Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
COMPUTED = RAW["computed"]

HUES = ("gray", "error", "lemon", "lilac", "mint", "sherbert", "sky", "sunset", "twilight")


def color(value):
    value = value.strip()
    if not re.fullmatch(r"#[0-9A-Fa-f]{6}", value):
        raise ValueError("not a 6-digit hex colour: %r" % value)
    return value.upper()


def token(value, ty, source, description=None):
    out = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    if description:
        out["$description"] = description
    return out


def core_colors():
    group = {}
    for name, value in COMPUTED.items():
        if not name.startswith("--"):
            continue
        body = name[2:]
        hue, _, step = body.partition("-")
        if hue not in HUES or not step.isdigit():
            continue
        group.setdefault(hue, {})[step] = token(
            color(value),
            "color",
            "css-var %s, computed on :root (theme-night)" % name,
        )
    return group


def alias(path, source, description=None):
    return token("{%s}" % path, "color", source, description)


def main():
    src = "computed style on the signed-in night theme, matched to a core ramp"
    night = {
        "page": alias("color.twilight.900", src, "Body background rgb(10, 9, 45)."),
        "text": alias("color.gray.200", src, "Body text rgb(246, 247, 251)."),
        "text-strong": alias("color.gray.100", src, "Primary button label and menu text."),
        "text-muted": alias("color.gray.400", src, "Section label rgb(217, 221, 232)."),
        "accent": alias("color.twilight.500", src, "Primary button rgb(66, 85, 255)."),
        "accent-text": alias("color.twilight.300", src, "Edit link rgb(168, 177, 255)."),
        "selected": alias("color.twilight.400", src, "Selected nav rgb(117, 131, 255)."),
        "surface": alias("color.gray.700", src, "Search field rgb(46, 56, 86)."),
        "trial": alias("color.sunset.400", src, "Trial button rgb(255, 205, 31)."),
        "on-trial": alias("color.gray.800", src, "Trial label rgb(40, 46, 62)."),
        "danger": alias("color.error.300", src, "Error ramp step used as the danger role."),
    }
    doc = {
        "core": {
            "color": core_colors(),
            "font": {
                "family": {
                    "body": token(
                        "hurme_no2-webfont, -apple-system, system-ui, sans-serif",
                        "fontFamily",
                        "computed fontFamily of body on quizlet.com/latest",
                    )
                },
                "weight": {
                    "body": token(400, "fontWeight", "css-var --typography-body-weight"),
                    "section": token(600, "fontWeight", "css-var --typography-section-weight"),
                    "heading": token(700, "fontWeight", "css-var --typography-heading-weight"),
                },
                "size": {
                    "body": token("16px", "dimension", "computed fontSize of body"),
                    "label": token("14px", "dimension", "computed fontSize of a section label"),
                    "heading": token("20px", "dimension", "computed fontSize of an h2"),
                    "page": token("32px", "dimension", "computed fontSize of the settings h1 at phone width"),
                },
                "line-height": {
                    "body": token("26px", "dimension", "computed lineHeight of body"),
                    "label": token("20px", "dimension", "computed lineHeight of a section label"),
                    "heading": token("28px", "dimension", "computed lineHeight of an h2"),
                    "page": token("40px", "dimension", "computed lineHeight of the settings h1 at phone width"),
                },
            },
            "radius": {
                "field": token("8px", "dimension", "computed borderRadius of the search field"),
                "pill": token("200px", "dimension", "computed borderRadius of the primary button"),
            },
            "space": {
                "button-y": token("10px", "dimension", "computed padding-block of the primary button"),
                "button-x": token("16px", "dimension", "computed padding-inline of the primary button"),
            },
        },
        "night": night,
        "$themes": [
            {"id": "night", "name": "Night", "selectedTokenSets": {"core": "source", "night": "enabled"}}
        ],
    }
    text = json.dumps(doc, indent=1) + "\n"
    (HERE / "tokens.json").write_text(text)
    print("wrote", HERE / "tokens.json")


if __name__ == "__main__":
    main()
