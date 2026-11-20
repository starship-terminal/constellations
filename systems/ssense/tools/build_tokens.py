#!/usr/bin/env python3
"""Build systems/ssense/tokens.json from raw/readings.json.

Every value is copied from a computed style or a declared rule recorded on
2026-11-19. The builder does not invent a dark theme, a phone scale, or a
colour that was not on the page. A missing reading stays out of the file.
"""
import json
import re
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
RAW = json.loads((ROOT / "raw" / "readings.json").read_text())
CAPTURE = "raw/readings.json, live computed styles on ssense.com/en-sg, 2026-11-19, viewport 1169x731, dpr 2, signed out"


def src(where):
    return {"evidence": "Measured", "capture": CAPTURE, "where": where}


def hexcolor(value):
    """rgb()/rgba() as the computed style reports it -> lower-case #rrggbb, or #rrggbbaa when the
    alpha is below 1. A value that is already hex is lower-cased; anything else is refused."""
    v = value.strip().lower()
    if re.fullmatch(r"#[0-9a-f]{6}([0-9a-f]{2})?", v):
        return v
    m = re.fullmatch(r"rgba?\(\s*(\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\s*\)", v)
    if not m:
        raise ValueError(f"not a colour: {value!r}")
    out = "#%02x%02x%02x" % tuple(int(x) for x in m.groups()[:3])
    if m.group(4) is not None and float(m.group(4)) < 1:
        out += "%02x" % int(float(m.group(4)) * 255 + 0.5)
    return out


def color(value, where):
    """The value is normalised to hex; raw/readings.json keeps the reading as the browser wrote it."""
    return {"$type": "color", "$value": hexcolor(value), "$extensions": {"source": src(where)}}


def dim(value, where):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": src(where)}}


def font(value, where):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": src(where)}}


def number(value, where):
    return {"$type": "number", "$value": value, "$extensions": {"source": src(where)}}


def text(value, where):
    return {"$type": "other", "$value": value, "$extensions": {"source": src(where)}}


C = RAW["colors"]
T = RAW["type"]
P = RAW["components"]
S = RAW["spacing"]
R = RAW["radius"]

core = {
    "font": {
        "family": {
            "favorit": font(T["chrome"]["font"], T["chrome"]["where"]),
            "favorit-inter1": font(T["tileHeadline"]["font"], T["tileHeadline"]["where"]),
            "favorit-regular": font(
                '"Favorit SSENSE Regular", "Helvetica Neue", Helvetica, Arial, sans-serif',
                P["loginButton"]["font"] + "; " + RAW["fonts"]["favoritRegular"]["where"],
            ),
            "times-now": font(T["editorialDeck"]["font"], T["editorialDeck"]["where"]),
            "inter": font(T["storefront"]["font"], T["storefront"]["where"]),
        }
    },
    "typography": {
        "chrome": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.favorit}",
                "fontSize": T["chrome"]["size"],
                "fontWeight": int(T["chrome"]["weight"]),
                "lineHeight": T["chrome"]["lineHeight"],
                "letterSpacing": "0px",
            },
            "$extensions": {"source": src(T["chrome"]["where"] + "; letter-spacing computed as normal, recorded as 0px")},
        },
        "storefront": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.inter}",
                "fontSize": T["storefront"]["size"],
                "fontWeight": int(T["storefront"]["weight"]),
                "lineHeight": T["storefront"]["lineHeight"],
                "letterSpacing": "0px",
            },
            "$extensions": {"source": src(T["storefront"]["where"])},
        },
        "login-heading": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.favorit}",
                "fontSize": T["loginHeading"]["size"],
                "fontWeight": int(T["loginHeading"]["weight"]),
                "lineHeight": T["loginHeading"]["lineHeight"],
                "letterSpacing": T["loginHeading"]["letterSpacing"],
            },
            "$extensions": {"source": src(T["loginHeading"]["where"])},
        },
        "faq-title": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.favorit}",
                "fontSize": T["faqTitle"]["size"],
                "fontWeight": int(T["faqTitle"]["weight"]),
                "lineHeight": T["faqTitle"]["lineHeight"],
                "letterSpacing": "0px",
            },
            "$extensions": {"source": src(T["faqTitle"]["where"])},
        },
        "faq-group": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.favorit}",
                "fontSize": T["faqGroup"]["size"],
                "fontWeight": int(T["faqGroup"]["weight"]),
                "lineHeight": T["faqGroup"]["lineHeight"],
                "letterSpacing": "0px",
            },
            "$extensions": {"source": src(T["faqGroup"]["where"])},
        },
        "tile-headline": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.favorit-inter1}",
                "fontSize": T["tileHeadline"]["size"],
                "fontWeight": int(T["tileHeadline"]["weight"]),
                "lineHeight": T["tileHeadline"]["lineHeight"],
                "letterSpacing": T["tileHeadline"]["letterSpacing"],
            },
            "$extensions": {"source": src(T["tileHeadline"]["where"])},
        },
        "tile-label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.favorit-inter1}",
                "fontSize": T["tileLabelSans"]["size"],
                "fontWeight": int(T["tileLabelSans"]["weight"]),
                "lineHeight": T["tileLabelSans"]["lineHeight"],
                "letterSpacing": T["tileLabelSans"]["letterSpacing"],
            },
            "$extensions": {"source": src(T["tileLabelSans"]["where"])},
        },
        "row-title": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.favorit-inter1}",
                "fontSize": T["rowTitle"]["size"],
                "fontWeight": int(T["rowTitle"]["weight"]),
                "lineHeight": T["rowTitle"]["lineHeight"],
                "letterSpacing": T["rowTitle"]["letterSpacing"],
            },
            "$extensions": {"source": src(T["rowTitle"]["where"])},
        },
        "editorial-hero": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.favorit-inter1}",
                "fontSize": T["editorialHero"]["size"],
                "fontWeight": int(T["editorialHero"]["weight"]),
                "lineHeight": T["editorialHero"]["lineHeight"],
                "letterSpacing": T["editorialHero"]["letterSpacing"],
            },
            "$extensions": {"source": src(T["editorialHero"]["where"])},
        },
        "editorial-deck": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.times-now}",
                "fontSize": T["editorialDeck"]["size"],
                "fontWeight": int(T["editorialDeck"]["weight"]),
                "lineHeight": T["editorialDeck"]["lineHeight"],
                "letterSpacing": T["editorialDeck"]["letterSpacing"],
            },
            "$extensions": {"source": src(T["editorialDeck"]["where"])},
        },
        "editorial-body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.times-now}",
                "fontSize": T["editorialBody"]["size"],
                "fontWeight": int(T["editorialBody"]["weight"]),
                "lineHeight": T["editorialBody"]["lineHeight"],
                "letterSpacing": T["editorialBody"]["letterSpacing"],
            },
            "$extensions": {"source": src(T["editorialBody"]["where"])},
        },
        "category-serif": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.times-now}",
                "fontSize": T["tileLabelSerif"]["size"],
                "fontWeight": int(T["tileLabelSerif"]["weight"]),
                "lineHeight": T["tileLabelSerif"]["lineHeight"],
                "letterSpacing": "0px",
            },
            "$extensions": {"source": src(T["tileLabelSerif"]["where"])},
        },
    },
    "radius": {
        "none": dim(R["square"], "header, product card, Add to bag, login field, search dialog"),
        "cta": dim(R["editorialCta"], P["editorialCta"]["radius"] + " on .ed-ButtonCTA"),
    },
    "spacing": {
        "5": dim(S["loginLabelGap"], "login label margin-bottom and listing price gap"),
        "9": dim(S["searchFieldPaddingLeft"], "search field padding-left"),
        "10": dim(S["cardImageGap"], "product image margin-bottom and FAQ answer margin-bottom"),
        "12": dim(S["sizeSelectMarginTop"], "size select parent margin-top (mt-3, computed as 12px)"),
        "18": dim(S["ctaPaddingX"], "editorial CTA and wishlist horizontal padding"),
        "20": dim(S["navGap"], "header nav gap and search dialog padding and page inset"),
        "25": dim(S["loginFieldToButton"], "gap from the login email field to Continue"),
        "55": dim(S["headerHeight"], "fixed header height"),
        "68": dim(S["tileLabelOffset"], "editorial tile label column, width and negative margin"),
    },
    "motion": {
        "drawer": dim("0.2s", RAW["motion"]["drawer"]),
        "main": dim("0.35s", RAW["motion"]["mainTransform"]),
        "dot": dim("0.1s", RAW["motion"]["carouselDot"]),
    },
}

light = {
    "background": {
        "page": color(C["white"]["value"], C["white"]["where"]),
        "surface": color(C["white"]["value"], "search dialog and header, same white as the page"),
        "action": color(C["black"]["value"], P["addToBag"]["background"] + " on Add to bag and Continue"),
        "muted": color(C["designerSearchFill"]["value"], C["designerSearchFill"]["where"]),
        "disabled": color(C["grey1"]["value"], P["disabledButtonDeclared"]["where"]),
    },
    "text": {
        "primary": color(C["black"]["value"], C["black"]["where"]),
        "secondary": color(C["editorialInk"]["value"], C["editorialInk"]["where"]),
        "muted": color(C["grey2"]["value"], C["grey2"]["where"]),
        "on-action": color(C["whiteOnBlack"]["value"], C["whiteOnBlack"]["where"]),
        "placeholder": color(C["grey1"]["value"], C["grey1"]["where"]),
    },
    "border": {
        "stroke": color(C["grey1"]["value"], "search dialog border, 1px solid"),
        "strong": color(C["black"]["value"], "login email field and search field, 1px solid"),
        "field": color(C["fieldBorder"]["value"], C["fieldBorder"]["where"]),
        "editorial": color(C["editorialCtaBorder"]["value"], C["editorialCtaBorder"]["where"]),
    },
    "focus": {
        "outline": color(C["focusOutline"]["value"], C["focusOutline"]["where"]),
    },
    "component": {
        "header": {
            "bg": color(P["header"]["background"], "header.opaque-header"),
            "height": dim(P["header"]["height"], "header getBoundingClientRect height"),
        },
        "button": {
            "bg": color(P["addToBag"]["background"], "Add to bag"),
            "text": color(P["addToBag"]["color"], "Add to bag label"),
            "radius": dim(P["addToBag"]["radius"], "Add to bag border-radius"),
            "height": dim(P["addToBag"]["height"], "Add to bag height"),
        },
        "field": {
            "bg": color("rgba(0, 0, 0, 0)", "login #email background"),
            "text": color(C["black"]["value"], "login #email color"),
            "radius": dim(P["loginField"]["radius"], "login #email border-radius"),
            "height": dim(P["loginField"]["height"], "login #email height"),
        },
        "cta": {
            "bg": color("rgba(0, 0, 0, 0)", ".ed-ButtonCTA background"),
            "text": color(C["editorialInk"]["value"], ".ed-ButtonCTA color"),
            "radius": dim(P["editorialCta"]["radius"], ".ed-ButtonCTA border-radius"),
            "height": dim(P["editorialCta"]["height"], ".ed-ButtonCTA height"),
        },
    },
}

doc = {
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}],
    "$extensions": {
        "source": src("package root"),
        "gaps": [
            "No dark theme painted on the signed-out pages.",
            "Phone width (390) was not measured. Desktop plan width 1440 was not reached; the pane was 1169px.",
            "Screenshots were not produced: preview_snapshot returned 'The browser is not producing screenshot frames'.",
            "Hover, pressed, loading, and error states were not forced. Focus on the size select set an orange outline-color with outline-style none.",
            "prefers-reduced-motion was false, and no authored reduce rule was found on the editorial page. A motion-probe pass was not run.",
            "Sale red was not present. The sale price is black, and the previous price is grey and struck through.",
            "Disabled Add to bag was not painted. .s-button--disabled is a declared rule only.",
        ],
    },
}

out = ROOT / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print(f"wrote {out}")
