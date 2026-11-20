#!/usr/bin/env python3
"""Build systems/nudea/tokens.json from raw/readings.json.

Values are the computed styles and :root custom properties read on nudea.com
on 2026-11-19. Nothing here is guessed. A token that could not be read is
absent, and the gap is listed in raw/readings.json and components.md.

    python3 tools/build_tokens.py
"""
import json
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent
READINGS = PKG / "raw" / "readings.json"
RAW_ROOT = json.loads(READINGS.read_text())["customProperties"]
OUT = PKG / "tokens.json"

HEX = re.compile(r"^#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$")
PX = re.compile(r"^-?\d+(\.\d+)?px$")


class CheckError(Exception):
    pass


def src(evidence, capture, note):
    return {
        "$description": note,
        "$extensions": {"source": {"evidence": evidence, "capture": capture}},
    }


def color(value, note, evidence="Measured", capture=":root custom property, nudea.com 2026-11-19"):
    return {"$value": value, "$type": "color", **src(evidence, capture, note)}


def dim(value, note, capture="computed style, nudea.com 2026-11-19"):
    return {"$value": value, "$type": "dimension", **src("Measured", capture, note)}


def num(value, typ, note, capture="computed style or custom property, nudea.com 2026-11-19"):
    return {"$value": value, "$type": typ, **src("Measured", capture, note)}


def bezier(text):
    """cubic-bezier(0, 0, 0.3, 1) as the DTCG list [0, 0, 0.3, 1]."""
    m = re.fullmatch(r"cubic-bezier\(([^)]*)\)", text.strip())
    if not m:
        raise CheckError(f"not a cubic-bezier: {text!r}")
    nums = [float(x) for x in m.group(1).split(",")]
    return [int(x) if x == int(x) else x for x in nums]


def alias(path, typ, note):
    return {"$value": "{" + path + "}", "$type": typ, **src("Derived", "alias of a measured token", note)}


def build():
    page = "https://www.nudea.com/ 2026-11-19, computed"
    product = "https://www.nudea.com/products/the-classic-flannel-pj-set-mulberry_gingham 2026-11-19"
    about = "https://www.nudea.com/pages/about 2026-11-19"
    collection = "https://www.nudea.com/collections/bras 2026-11-19"
    root = ":root custom property, nudea.css / Dawn base.css, 2026-11-19"

    core = {
        "color": {
            "cotton": color("#fbfaf2", "Page ground. --cotton, and body background-color rgb(251, 250, 242).", capture=root),
            "dark-cotton": color("#efeee7", "--dark-cotton. Declared, not used as the header fill on the pages read.", capture=root),
            "raven": color("#333333", "Text and primary button fill. --raven, and body color rgb(51, 51, 51).", capture=root),
            "grid": color("#d3d2cc", "Hairline. --grid. Size pills use it as a 1px border.", capture=root),
            "brick": color("#a04b2d", "--brick. Declared on :root. Not seen as a fill on the pages read.", capture=root),
            "nude": color("#f2d3bc", "--nude. Declared on :root. Not seen as a fill on the pages read.", capture=root),
            "olive": color("#8a8b5b", "--olive. Declared on :root. Not seen as a fill on the pages read.", capture=root),
            "lilac": color("#e2e4ed", "--lilac. Declared on :root. Not seen as a fill on the pages read.", capture=root),
            "peach-fuzz": color("#ffbe98", "--peach-fuzz. Declared on :root. Not seen as a fill on the pages read.", capture=root),
            "red": color("#ad2c2c", "Sale and promo. --red. Sale tag background and .nav-item--promo colour are rgb(173, 44, 44).", capture=root),
            "white": color("#ffffff", "--white. Declared. Cotton text on raven is the cream --cotton, not this white.", capture=root),
        },
        "font": {
            "family": {
                "display": num("abril-text, serif", "fontFamily", "--font-heading-family and --font-body-family. Adobe Fonts kit wxz8tft.", capture=root),
                "ui": num("neue-haas-grotesk-display, sans-serif", "fontFamily", "--font-second-family. Buttons, prices, eyebrows, footer links.", capture=root),
            },
            "weight": {
                "body": num(300, "fontWeight", "--font-body-weight. Body, nav, product title.", capture=root),
                "heading": num(400, "fontWeight", "--font-heading-weight declared. Buttons and prices compute to 400.", capture=root),
            },
        },
        "typography": {
            "display": num({
                "fontFamily": "{font.family.display}",
                "fontWeight": "{font.weight.body}",
                "fontSize": "36px",
                "lineHeight": "46px",
                "letterSpacing": "0.72px",
            }, "typography", "About page h1, computed.", capture=about),
            "product-title": num({
                "fontFamily": "{font.family.display}",
                "fontWeight": "{font.weight.body}",
                "fontSize": "24px",
                "lineHeight": "34px",
                "letterSpacing": "0.48px",
            }, "typography", "Product page h1, computed.", capture=product),
            "nav": num({
                "fontFamily": "{font.family.display}",
                "fontWeight": "{font.weight.body}",
                "fontSize": "16px",
                "lineHeight": "34px",
                "letterSpacing": "0.32px",
            }, "typography", "Desktop header nav item, computed.", capture=page),
            "quote": num({
                "fontFamily": "{font.family.display}",
                "fontWeight": "{font.weight.body}",
                "fontSize": "20px",
                "lineHeight": "30px",
                "letterSpacing": "0.4px",
            }, "typography", "About pull quote is 20px/30px. Drawer h4 computes to the same size with 0.4px tracking.", capture=about),
            "body": num({
                "fontFamily": "{font.family.display}",
                "fontWeight": "{font.weight.body}",
                "fontSize": "14px",
                "lineHeight": "20px",
                "letterSpacing": "0.28px",
            }, "typography", "Body and product description, computed.", capture=page),
            "card-title": num({
                "fontFamily": "{font.family.display}",
                "fontWeight": "{font.weight.body}",
                "fontSize": "14px",
                "lineHeight": "20px",
                "letterSpacing": "0.28px",
            }, "typography", "Collection card title, computed.", capture=collection),
            "price": num({
                "fontFamily": "{font.family.ui}",
                "fontWeight": "{font.weight.heading}",
                "fontSize": "13px",
                "lineHeight": "22px",
                "letterSpacing": "0.26px",
            }, "typography", "Price and announcement link size. Price is 13px/400; announcement link is 13px/300.", capture=product),
            "eyebrow": num({
                "fontFamily": "{font.family.ui}",
                "fontWeight": "{font.weight.heading}",
                "fontSize": "12px",
                "lineHeight": "22px",
                "letterSpacing": "0.96px",
            }, "typography", "Collection h1, featured-link eyebrow, footer link, accordion title. Uppercase.", capture=collection),
            "button": num({
                "fontFamily": "{font.family.ui}",
                "fontWeight": "{font.weight.heading}",
                "fontSize": "12px",
                "lineHeight": "22px",
                "letterSpacing": "0.96px",
            }, "typography", ".button computed. Uppercase.", capture=product),
            "search": num({
                "fontFamily": "{font.family.display}",
                "fontWeight": "{font.weight.body}",
                "fontSize": "20px",
                "lineHeight": "30px",
                "letterSpacing": "0.4px",
            }, "typography", ".search__input computed.", capture=product),
            "badge": num({
                "fontFamily": "{font.family.ui}",
                "fontWeight": "{font.weight.heading}",
                "fontSize": "10px",
                "lineHeight": "20px",
                "letterSpacing": "0.2px",
            }, "typography", ".product-tag--sale computed.", capture=product),
        },
        "radius": {
            "none": dim("0px", "Product cards, inputs and the Dawn --buttons-radius custom property are 0. The drawn button is not.", capture=root),
            "badge": dim("5px", ".product-tag--sale border-radius.", capture=product),
            "size-end": dim("10px", "Outer corners of the size row. Selected XS is 10px 0 0 10px; XL is 0 10px 10px 0.", capture=product),
            "image": dim("10px", "Collection card image border-radius.", capture=collection),
            "pill": dim("100px", ".button and .product-form__submit border-radius. The stylesheet sets 10rem, which computes to 100px.", capture=product),
            "swatch": {
                "$value": "18.5px",
                "$type": "dimension",
                **src("Derived", "37px swatch with border-radius 100%, product page",
                      "Half of the measured 37px swatch. The computed value is 100%, which DESIGN.md cannot export."),
            },
        },
        "spacing": {
            "2": dim("2px", "Header icon button vertical padding is 4px 2px. The 2px is the horizontal step.", capture=page),
            "4": dim("4px", "Mobile grid vertical spacing custom property is 4px.", capture=root),
            "7": dim("7px", "Sale tag horizontal padding is 0 7px.", capture=product),
            "8": dim("8px", "Desktop grid vertical spacing custom property.", capture=root),
            "14": dim("14px", "Mobile grid horizontal spacing custom property. Mobile menu label padding is 14px 0.", capture=root),
            "20": dim("20px", "Button horizontal padding, and the phone header padding.", capture=product),
            "28": dim("28px", "Desktop grid horizontal spacing custom property.", capture=root),
            "40": dim("40px", "Desktop header horizontal padding.", capture=page),
            "50": dim("50px", "Footer padding-top.", capture=page),
        },
        "size": {
            "announcement": dim("30px", "Announcement bar inner height.", capture=page),
            "button": dim("40px", ".button height.", capture=page),
            "button-primary": dim("50px", ".product-form__submit height.", capture=product),
            "size-pill": dim("55px", "Size label height.", capture=product),
            "swatch": dim("37px", "Colour swatch width and height.", capture=product),
            "header": dim("88px", "header-component height at 1440.", capture=page),
            "header-phone": dim("57px", "header-component height at 390.", capture=page),
            "search": dim("83px", ".search__input height.", capture=product),
            "logo": dim("20px", "Wordmark SVG height. Width computed at 141px.", capture=page),
            "border": dim("1px", "Button, size pill and search underline width.", capture=product),
        },
        "motion": {
            "duration": {
                "short": num("100ms", "duration", "--duration-short is 0.1s.", capture=root),
                "default": num("200ms", "duration", "--duration-default is 0.2s.", capture=root),
                "announcement": num("250ms", "duration", "--duration-announcement-bar is 0.25s.", capture=root),
                "medium": num("300ms", "duration", "--duration-medium is 0.3s. .button transition-duration computes to 0.3s.", capture=root),
                "long": num("500ms", "duration", "--duration-long is 0.5s.", capture=root),
                "extra-long": num("600ms", "duration", "--duration-extra-long is 0.6s. --animation-fade-in uses 0.6s.", capture=root),
            },
            "easing": {
                "in-out": {"$value": [0.42, 0, 0.58, 1], "$type": "cubicBezier",
                           **src("Derived", product, ".button transition-timing-function computes to ease-in-out; the CSS keyword is cubic-bezier(0.42, 0, 0.58, 1).")},
                "out-slow": num(bezier(RAW_ROOT["--ease-out-slow"]), "cubicBezier", "--ease-out-slow is cubic-bezier(0, 0, 0.3, 1). Used by --animation-fade-in and --animation-slide-in.", capture=root),
            },
        },
    }
    light = {
        "color": {
            "page": alias("color.cotton", "color", "Body background."),
            "surface": alias("color.cotton", "color", "Cards and the product column sit on the page ground. No raised surface colour was computed."),
            "header": {
                "$value": "#fbfaf2cc",
                "$type": "color",
                **src("Measured", "header-component:hover::after",
                      "The header element itself is transparent. On hover the stylesheet paints rgba(251, 250, 242, 0.8), which is cotton at 80%."),
            },
            "announcement": alias("color.raven", "color", "Announcement inner background."),
            "text": alias("color.raven", "color", "Body and nav text."),
            "text-on-raven": alias("color.cotton", "color", "Announcement link, primary button label, selected size, sale tag."),
            "muted": {
                "$value": "#333333",
                "$type": "color",
                **src("Measured", product,
                      "Compare-at price is the same raven, with text-decoration line-through. No separate muted grey was computed."),
            },
            "accent": alias("color.raven", "color", "Primary action fill."),
            "accent-text": alias("color.cotton", "color", "Primary action label."),
            "promo": alias("color.red", "color", "Black Friday nav item and the sale tag."),
            "border": alias("color.grid", "color", "Size pills and the search underline."),
            "hero-scrim": {
                "$value": "#333333",
                "$type": "color",
                **src("Not captured", page,
                      "The homepage hero is a photograph. Its dark field was not a flat computed background, so this is the raven token as the nearest declared dark, not a sampled pixel."),
            },
        },
        "component": {
            "button-primary": {
                "background": alias("color.raven", "color", "Primary button fill."),
                "text": alias("color.cotton", "color", "Primary button label."),
                "radius": alias("radius.pill", "dimension", "Primary button radius."),
                "height": alias("size.button-primary", "dimension", "Add to bag / pre-order height."),
                "padding": dim("0px", "Vertical padding is 0. Horizontal padding is 20px, recorded as spacing.20.", capture=product),
            },
            "button-secondary": {
                "background": {
                    "$value": "#00000000",
                    "$type": "color",
                    **src("Measured", page, "Outline button background computes to transparent."),
                },
                "text": alias("color.raven", "color", "Outline button label on cotton."),
                "radius": alias("radius.pill", "dimension", "Outline button radius."),
                "height": alias("size.button", "dimension", "Outline button height."),
            },
            "badge-sale": {
                "background": alias("color.red", "color", "Sale tag fill."),
                "text": alias("color.cotton", "color", "Sale tag label."),
                "radius": alias("radius.badge", "dimension", "Sale tag radius."),
            },
        },
    }
    # hero-scrim was labelled Not captured but still given a value. Remove the invented value.
    del light["color"]["hero-scrim"]

    doc = {
        "core": core,
        "light": light,
        "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
        "$extensions": {
            "source": {
                "evidence": "Measured",
                "capture": "nudea.com public signed-out pages, 2026-11-19",
            },
            "notTokenised": [
                "Hero photograph background. It is an image, not a flat colour.",
                "Klarna badge fill. Visible on the product screenshot, not read from computed style.",
                "Pressed and disabled button colours. Not held.",
                "Dark theme. The signed-out store does not switch theme.",
                "Swatch border-radius 100% is stored as 18.5px so the radius scale can export.",
            ],
        },
    }
    return doc


def check(doc):
    def walk(node, path, found):
        if isinstance(node, dict) and "$value" in node:
            found.append((path, node))
            return
        if isinstance(node, dict):
            for k, v in node.items():
                if k.startswith("$"):
                    continue
                walk(v, f"{path}.{k}" if path else k, found)

    found = []
    walk(doc.get("core", {}), "", found)
    walk(doc.get("light", {}), "", found)
    flat = {}
    for path, node in found:
        if "source" not in node.get("$extensions", {}):
            raise CheckError(f"no source on {path}")
        flat[path] = node
    for path, node in found:
        val = node["$value"]
        if isinstance(val, str) and val.startswith("{") and val.endswith("}"):
            target = val[1:-1]
            if target not in flat and f"core.{target}" not in flat and target not in {p.split(".", 1)[-1] if p.startswith("core.") else p for p in []}:
                # aliases are written without the set prefix and resolve inside core or light
                candidates = [p for p in flat if p == target or p.endswith("." + target) or p.split(".", 1)[-1] == target]
                # prefer exact tail match from the start of a group
                exact = [p for p in flat if p == target or p[p.find(".") + 1:] == target or p.endswith(target) and (p[: -len(target)] in ("",) or p[-len(target) - 1] == ".")]
                # simpler: strip set prefix
                tails = {p.split(".", 1)[-1] if "." in p else p: p for p in flat}
                # The alias omits the set. Match the suffix.
                if not any(p.endswith(target) and (len(p) == len(target) or p[-len(target) - 1] == ".") for p in flat):
                    raise CheckError(f"alias {path} points at nothing: {target}")
        elif node.get("$type") == "color" and isinstance(val, str):
            if not HEX.match(val):
                raise CheckError(f"bad colour {path}: {val}")
        elif node.get("$type") == "dimension" and isinstance(val, str):
            if not PX.match(val):
                raise CheckError(f"bad dimension {path}: {val}")
        elif node.get("$type") == "cubicBezier":
            if not (isinstance(val, list) and len(val) == 4
                    and all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in val)):
                raise CheckError(f"cubicBezier {path} is not four numbers: {val!r}")
    return flat


def main():
    doc = build()
    check(doc)
    text = json.dumps(doc, indent=2) + "\n"
    OUT.write_text(text)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
