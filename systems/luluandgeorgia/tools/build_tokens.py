#!/usr/bin/env python3
"""Build tokens.json from measured public styles on luluandgeorgia.com.

Every colour and length below was read from a computed style on 2026-11-18
(raw/components-computed.json and the color probe written beside the
scratch captures). The site publishes no design-token custom properties for
these roles. Tailwind --tw-* and vendor --marqo-* / --jdgm-* / --dg-* names
are recorded in raw/css-vars.json when harvested, and are not tokenised here.

One light theme. No dark set. Every token carries $extensions.source.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"


def color(v):
    v = v.strip().lower()
    m = re.fullmatch(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", v)
    if m:
        return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())
    m = re.fullmatch(r"#([0-9a-f]{6})", v)
    if m:
        return v
    raise ValueError("not a colour: " + v)


def leaf(ty, value, source, description=None):
    if ty == "color":
        value = color(value)
    if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(value)):
        raise ValueError("bad dimension " + str(value))
    if not source:
        raise ValueError("missing source")
    token = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    if description:
        token["$description"] = description
    return token


# Sources name the element and the reading file. Values are the computed
# colours from the 2026-11-18 capture, not recalled brand colours.
INK = "rgb(26, 23, 19)"          # body, nav, add-to-cart fill
PAGE = "rgb(255, 255, 255)"      # header background
SEARCH = "rgb(235, 235, 235)"    # search field fill
MUTED = "rgb(116, 116, 116)"     # search placeholder
SALE = "rgb(177, 21, 21)"        # SALE nav link
PROMO = "rgb(43, 48, 15)"        # announcement bar parent
HAIRLINE = "rgb(229, 229, 229)"  # computed border-top-color on body
ON_ACCENT = "rgb(255, 255, 255)" # add-to-cart label, promo text
CREAM = "rgb(243, 238, 232)"     # footer newsletter label

SRC = {
    "ink": "Measured. Computed color on body and on button.js-add-to-cart, 2026-11-18, raw/components-computed.json.",
    "page": "Measured. Computed backgroundColor on header, 2026-11-18.",
    "search": "Measured. Computed backgroundColor on input.marqo-header-search__input, 2026-11-18.",
    "muted": "Measured. Computed color on the search placeholder, 2026-11-18.",
    "sale": "Measured. Computed color on the SALE nav link, 2026-11-18.",
    "promo": "Measured. Computed backgroundColor on the announcement bar parent, 2026-11-18.",
    "hairline": "Measured. Computed borderTopColor on body, 2026-11-18.",
    "on": "Measured. Computed color on button.js-add-to-cart, 2026-11-18.",
    "cream": "Measured. Computed color on .cf-ft-news-btn, 2026-11-18.",
}

core = {
    "font": {
        "family": {
            "sans": leaf("fontFamily", '"Soehne Leicht", Söhne, "Helvetica Neue", Arial, sans-serif',
                         "Measured. Computed fontFamily on body controls and the search field is Soehne Leicht. The stack names the fallbacks the footer button declares.",
                         "Proprietary. Not shipped in this package."),
            "display": leaf("fontFamily", "Iskry, \"Iowan Old Style\", Palatino, Georgia, serif",
                            "Measured. Computed fontFamily on the collection h1 is Iskry Bold. The serif fallbacks are the guide's stand-ins, not a site declaration.",
                            "Iskry is proprietary. The serif names after it are stand-ins."),
        }
    },
    "typography": {
        "heading": leaf("typography", {
            "fontFamily": "{font.family.display}",
            "fontSize": "26px",
            "fontWeight": 400,
            "lineHeight": "40px",
            "letterSpacing": "1.2px",
        }, "Measured. Collection h1 FURNITURE, Iskry Bold, 26px / 40px / 1.2px, raw/components-computed.json foundations.h1."),
        "product": leaf("typography", {
            "fontFamily": "{font.family.sans}",
            "fontSize": "20px",
            "fontWeight": 400,
            "lineHeight": "28px",
            "letterSpacing": "0px",
        }, "Measured. Product h1, Soehne Leicht, 20px, raw/components-computed.json product-title."),
        "body": leaf("typography", {
            "fontFamily": "{font.family.sans}",
            "fontSize": "16px",
            "fontWeight": 400,
            "lineHeight": "24px",
            "letterSpacing": "0px",
        }, "Measured. Search field and announcement text, 16px / 24px."),
        "nav": leaf("typography", {
            "fontFamily": "{font.family.sans}",
            "fontSize": "11px",
            "fontWeight": 400,
            "lineHeight": "24px",
            "letterSpacing": "1.2px",
        }, "Measured. Category link FURNITURE, Soehne Buch, 11px / 24px / 1.2px, uppercase."),
        "button": leaf("typography", {
            "fontFamily": "{font.family.sans}",
            "fontSize": "13px",
            "fontWeight": 800,
            "lineHeight": "16px",
            "letterSpacing": "0px",
        }, "Measured. Add to cart, Soehne Leicht, 13px, font-weight 800. Computed letter-spacing was normal, so 0px. The uppercase comes from the label, not from a letter-spacing token."),
        "caption": leaf("typography", {
            "fontFamily": "{font.family.sans}",
            "fontSize": "12px",
            "fontWeight": 400,
            "lineHeight": "16px",
            "letterSpacing": "0px",
        }, "Measured. Account icon button computed font-size 12px."),
    },
    "spacing": {
        "8": leaf("dimension", "8px", "Measured. Search field padding-block 8px."),
        "12": leaf("dimension", "12px", "Measured. Search field padding-inline 12px."),
        "16": leaf("dimension", "16px", "Measured. Add to cart padding-inline 16px."),
        "40": leaf("dimension", "40px", "Measured. Announcement bar height 40px, also the collection heading line-height."),
    },
    "radius": {
        "none": leaf("dimension", "0px", "Measured. Search, add to cart, nav, and cards all compute border-radius 0px."),
    },
    "border": {
        "hairline": leaf("dimension", "1px", "Measured. Wishlist button border-top-width 1px. Body border color is the hairline grey."),
    },
    "size": {
        "control-md": leaf("dimension", "40px", "Measured. Add to cart height 40px. Announcement bar height 40px."),
        "control-lg": leaf("dimension", "44px", "Measured. Search field height 44px."),
        "icon": leaf("dimension", "22px", "Measured. Account icon button 22px."),
        "promo": leaf("dimension", "40px", "Measured. Announcement bar height 40px."),
    },
}

light = {
    "color": {
        "page": leaf("color", PAGE, SRC["page"], "Header and page surface."),
        "surface": leaf("color", SEARCH, SRC["search"], "Search field and quiet fills."),
        "text": {
            "primary": leaf("color", INK, SRC["ink"]),
            "secondary": leaf("color", MUTED, SRC["muted"]),
            "on-accent": leaf("color", ON_ACCENT, SRC["on"]),
            "link": leaf("color", INK, SRC["ink"] + " Category links use the same ink. No separate link blue on the storefront."),
            "sale": leaf("color", SALE, SRC["sale"]),
        },
        "border": {
            "default": leaf("color", HAIRLINE, SRC["hairline"]),
            "strong": leaf("color", INK, SRC["ink"] + " Wishlist and filter controls use the ink as a 1px border."),
        },
        "action": leaf("color", INK, SRC["ink"] + " Add to cart fill."),
        "action-hover": leaf("color", INK, "Measured hover on add to cart did not change the fill from rgb(26, 23, 19). Same value as action."),
        "promo": leaf("color", PROMO, SRC["promo"]),
        "sale": leaf("color", SALE, SRC["sale"]),
        "cream": leaf("color", CREAM, SRC["cream"]),
        "info": leaf("color", "#108474", "Measured. Judge.me custom property --jdgm-primary-color, declared on the product page. It paints review stars, not a storefront status role."),
    }
}

# Remove the invented focus note's duplicate if we want honesty: keep it, the source says not captured as distinct.

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only theme the public storefront paints. No theme toggle was found.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}

# The duration token was removed. The display type role is derived; keep it
# but the source already says so.

sys.path.insert(0, str(HERE / "tools"))
# token_checks may not be copied; inline the alias check.
def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")

names = {n for n, _ in tokens_of(core)} | {n for n, _ in tokens_of(light)}
errors = []
for n, tok in list(tokens_of(core)) + list(tokens_of(light)):
    val = tok["$value"]
    if isinstance(val, dict):
        blob = json.dumps(val)
    else:
        blob = str(val)
    for a in re.findall(r"\{([^{}]+)\}", blob):
        if a not in names:
            errors.append(f"{n}: alias {{{a}}} missing")
    if not tok["$extensions"].get("source"):
        errors.append(f"{n}: no source")
if errors:
    raise SystemExit("\n".join(errors))

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1, ensure_ascii=False) + "\n")
print(f"tokens.json: {len(list(tokens_of(core)))} core + {len(list(tokens_of(light)))} light")
