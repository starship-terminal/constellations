#!/usr/bin/env python3
"""Build tokens.json from measured public styles on luluandgeorgia.com.

Every colour and length below is read from raw/components-computed.json, the
computed styles of 2026-11-18. Three colours came from a colour probe written
beside the scratch captures, which is not committed; they are typed in and
labelled Reconstruction. The site publishes no design-token custom properties for
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


# Every measured value is read from raw/components-computed.json: `components` holds the per-element
# readings, `foundations` the page-level ones. A missing reading fails the build. The colours the
# capture took from a separate colour probe that is not committed (the announcement bar parent, the
# footer newsletter button, the Judge.me star colour) are typed in below and labelled Reconstruction.
J = json.loads((RAW / "components-computed.json").read_text())
COMP, FOUND = J["components"], J["foundations"]
FILE = "raw/components-computed.json"


def reading(key, prop, state="default"):
    """A computed property of one measured component, or a foundations reading (key 'f:<name>')."""
    if key.startswith("f:"):
        v = (FOUND.get(key[2:]) or {}).get(prop)
    else:
        v = ((COMP.get(key) or {}).get("states", {}).get(state) or {}).get(prop)
    if v in (None, ""):
        raise SystemExit(f"{key} {state} {prop} missing from {FILE}")
    return v


def px(v):
    return f"{v:g}px" if isinstance(v, (int, float)) else v


def tracking(v):
    return "0px" if v == "normal" else v


def pad(key, i):
    """One side of a computed padding shorthand: 0 block, 1 inline."""
    parts = reading(key, "padding").split()
    return parts[min(i, len(parts) - 1)]


def first_family(key):
    return reading(key, "fontFamily").split(",")[0].strip().strip('"')


def by_hand(what):
    return f"Reconstruction: entered by hand at capture time from {what}. No committed reading in raw/ holds it."


INK = reading("f:body", "color")
PAGE = reading("f:header", "backgroundColor")
SEARCH = reading("search", "backgroundColor")
MUTED = reading("search", "color")
SALE = reading("f:sale", "color")
HAIRLINE = reading("f:body", "borderTop").split(" ", 2)[2]
ON_ACCENT = reading("atc", "color")
# The announcement bar itself now paints this fill. The 2026-11-18 olive
# #2b300f was a colour probe of a parent that is no longer on the page.
PROMO = reading("promo-bar", "backgroundColor")
CREAM = "rgb(243, 238, 232)"    # colour probe, not committed
if reading("atc", "backgroundColor") != INK or reading("atc", "backgroundColor", "hover") != INK:
    raise SystemExit("add to cart no longer paints the body ink; revisit action and action-hover")

SRC = {
    "ink": f"Measured. Computed color on body ({FILE} foundations.body) and backgroundColor of the add-to-cart button (atc), 2026-11-21.",
    "page": f"Measured. Computed backgroundColor on header ({FILE} foundations.header), 2026-11-21.",
    "search": f"Measured. Computed backgroundColor on the header search field ({FILE} search), 2026-11-21.",
    "muted": f"Measured. Computed color on the header search field placeholder ({FILE} search), 2026-11-21.",
    "sale": f"Measured. Computed color on the SALE nav link ({FILE} foundations.sale), 2026-11-21.",
    "promo": f"Measured. Computed backgroundColor on the announcement bar ({FILE} promo-bar), 2026-11-21. The bar is the red early-access sale strip, the same red as the SALE link.",
    "hairline": f"Measured. Computed borderTopColor on body ({FILE} foundations.body), 2026-11-21.",
    "on": f"Measured. Computed color on the add-to-cart button ({FILE} atc), 2026-11-21.",
    "cream": by_hand("a colour probe of the footer newsletter button .cf-ft-news-btn"),
}


def type_style(key, family, source):
    return leaf("typography", {
        "fontFamily": family,
        "fontSize": reading(key, "fontSize"),
        "fontWeight": int(reading(key, "fontWeight")),
        "lineHeight": reading(key, "lineHeight"),
        "letterSpacing": tracking(reading(key, "letterSpacing")),
    }, source)


core = {
    "font": {
        "family": {
            "sans": leaf("fontFamily", f'"{first_family("search")}", Söhne, "Helvetica Neue", Arial, sans-serif',
                         f"Measured: {first_family('search')} is the computed fontFamily on the search field and the body controls ({FILE}). "
                         "The fallbacks after it were entered by hand at capture time from a footer button reading that is not in raw/.",
                         "Proprietary. Not shipped in this package."),
            "display": leaf("fontFamily", f'{first_family("f:h1").split()[0]}, "Iowan Old Style", Palatino, Georgia, serif',
                            f"Measured. Computed fontFamily on the collection h1 is {first_family('f:h1')} ({FILE} foundations.h1). The serif fallbacks are the guide's stand-ins, not a site declaration.",
                            "Iskry is proprietary. The serif names after it are stand-ins."),
        }
    },
    "typography": {
        "heading": type_style("f:h1", "{font.family.display}", f"Measured. Collection h1 FURNITURE, {first_family('f:h1')}, {FILE} foundations.h1."),
        "product": type_style("product-title", "{font.family.sans}", f"Measured. Product h1, {first_family('product-title')}, {FILE} product-title."),
        "body": type_style("search", "{font.family.sans}", f"Measured. Header search field, {first_family('search')}, {FILE} search."),
        "nav": type_style("nav-link", "{font.family.sans}", f"Measured. Category link FURNITURE, {first_family('nav-link')}, uppercase, {FILE} nav-link."),
        "button": type_style("atc", "{font.family.sans}", f"Measured. Add to cart, {first_family('atc')}, uppercase label, {FILE} atc."),
        "caption": type_style("icon-account", "{font.family.sans}", f"Measured. Account icon button, {FILE} icon-account."),
    },
    "spacing": {
        "8": leaf("dimension", pad("search", 0), f"Measured. Search field padding-block, {FILE} search."),
        "12": leaf("dimension", pad("search", 1), f"Measured. Search field padding-inline, {FILE} search."),
        "16": leaf("dimension", pad("atc", 1), f"Measured. Add to cart padding-inline, {FILE} atc."),
        "40": leaf("dimension", px(reading("promo-bar", "rect")["h"]), f"Measured. Announcement bar height, {FILE} promo-bar; also the collection heading line-height."),
    },
    "radius": {
        "none": leaf("dimension", reading("search", "borderRadius"), f"Measured. Search, add to cart, nav and cards all compute border-radius 0px ({FILE})."),
    },
    "border": {
        "hairline": leaf("dimension", reading("filter-btn", "borderTopWidth"), f"Measured. Filter button border-top-width, {FILE} filter-btn."),
    },
    "size": {
        "control-md": leaf("dimension", px(reading("atc", "rect")["h"]), f"Measured. Add to cart height, {FILE} atc."),
        "control-lg": leaf("dimension", px(reading("search", "rect")["h"]), f"Measured. Search field height, {FILE} search."),
        "icon": leaf("dimension", px(reading("icon-account", "rect")["h"]), f"Measured. Account icon button height, {FILE} icon-account."),
        "promo": leaf("dimension", px(reading("promo-bar", "rect")["h"]), f"Measured. Announcement bar height, {FILE} promo-bar."),
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
            "strong": leaf("color", INK, by_hand("the wishlist and filter controls' 1px ink border; the wishlist button was not found by the measure pass and the filter button's reading is #ebebeb")),
        },
        "action": leaf("color", INK, SRC["ink"] + " Add to cart fill."),
        "action-hover": leaf("color", INK, f"Measured. Add to cart hover computes the same backgroundColor ({FILE} atc hover). Same value as action."),
        "promo": leaf("color", PROMO, SRC["promo"]),
        "sale": leaf("color", SALE, SRC["sale"]),
        "cream": leaf("color", CREAM, SRC["cream"]),
        "info": leaf("color", "#108474", by_hand("the Judge.me custom property --jdgm-primary-color declared on the product page; it paints review stars, not a storefront status role")),
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
