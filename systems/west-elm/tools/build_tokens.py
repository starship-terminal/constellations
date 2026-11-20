#!/usr/bin/env python3
"""Build tokens.json from raw/readings.json.

Every leaf is a value read on westelm.com on 2026-11-19 (computed style or a
same-origin stylesheet rule). The builder refuses a leaf with no source.
West Elm's public pages showed one light theme, so there is no dark set.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw" / "readings.json"
OUT = HERE / "tokens.json"

DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def color(value):
    value = value.strip().lower()
    match = re.fullmatch(r"#([0-9a-f]{6}|[0-9a-f]{8})", value)
    if match:
        return "#" + match.group(1)
    match = re.fullmatch(
        r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)",
        value,
    )
    if not match:
        raise ValueError("not a colour: " + value)
    red, green, blue, alpha = match.groups()
    alpha = float(alpha) if alpha is not None else 1
    hexed = "#%02x%02x%02x" % (int(red), int(green), int(blue))
    # Translucent colours as #rrggbbaa: tools/catalog.py and the contrast check read only hex.
    return hexed if alpha >= 1 else hexed + "%02x" % round(alpha * 255)


def leaf(type_, value, source, description=None):
    if not source:
        raise ValueError("leaf without a source")
    if type_ == "color" and not str(value).startswith("{"):
        value = color(value)
    if type_ == "dimension" and not (str(value).startswith("{") or DIM.fullmatch(str(value))):
        raise ValueError(f"dimension {value!r}")
    if type_ == "fontWeight" and not isinstance(value, int):
        raise ValueError(f"fontWeight {value!r}")
    token = {
        "$type": type_,
        "$value": value,
        "$extensions": {"source": source},
    }
    if description:
        token["$description"] = description
    return token


def alias(path, source, description=None):
    return leaf("color", "{" + path + "}", source, description)


S = "raw/readings.json"


def main():
    readings = json.loads(RAW.read_text())
    computed = readings["computed"]
    assert readings["body"]["color"] == "rgb(33, 33, 33)"

    core = {
        "$description": "Scales read from westelm.com public pages on 2026-11-19. One light theme.",
        "color": {
            "ink": leaf("color", "#212121", f"{S} body.color and nearly every text role", "House ink. Not pure black."),
            "inkBlack": leaf("color", "#000000", f"{S} computed.emailOverlay.body.color and filter button color", "Pure black appears on the email overlay body and the filter button label."),
            "white": leaf("color", "#ffffff", f"{S} computed.heroCta.backgroundColor and dialog background", "Surface and inverse text."),
            "gray100": leaf("color", "#f4f4f4", f"{S} computed.brandBar.backgroundColor and footer.backgroundColor", "Brand strip and footer ground."),
            "gray200": leaf("color", "#d9d9d9", f"{S} computed.categoryNavRule.borderTop and swatchThumb.border", "Hairline under the category nav and around swatch thumbs."),
            "gray300": leaf("color", "#c8c8c8", f"{S} computed.searchInput.border and quantityButton.border", "Field and stepper border."),
            "gray400": leaf("color", "#a6a6a6", f"{S} computed.quantityButton.color", "Disabled stepper glyph."),
            "gray500": leaf("color", "#767676", f"{S} computed.select.border", "Native select border."),
            "gray600": leaf("color", "#666666", f"{S} computed.loginLabel.color", "Floating field label."),
            "gray700": leaf("color", "#646464", f"{S} computed.sisterBrand.color and footerLink.color", "Sister-brand and footer link ink."),
            "gray800": leaf("color", "#4d4d4d", f"{S} computed.searchSubmit.backgroundColor", "Search submit fill."),
            "gray900": leaf("color", "#363636", f"{S} computed.emailOverlay.emailField.color", "Placeholder ink on the overlay email field."),
            "sale": leaf("color", "#af1a31", f"{S} computed.addToCart.backgroundColor and salePrice.color; stylesheet .btn-conversion", "Conversion red. Add to cart fill and sale price."),
            "saleHover": leaf("color", "#7a0000", f"{S} stylesheetRules.btnConversion hover #7a0000", "Add to cart hover fill, from the stylesheet, not a live hover."),
            "saleDisabled": leaf("color", "#d48c8c", f"{S} stylesheetRules.btnConversion disabled #d48c8c", "Add to cart disabled fill, from the stylesheet."),
            "promo": leaf("color", "#5b0819", f"{S} computed.promoBar.backgroundColor and .bg-bloedworst-5b0819", "Marketing banner burgundy."),
            "primaryHover": leaf("color", "#858585", f"{S} stylesheetRules.btnPrimaryHover", "Primary button hover fill on .design-platform .btn-primary:hover."),
            "focus": leaf("color", "#2563eb", f"{S} stylesheetRules.focusVisible outline solid 2px #2563eb", "One of several focus outlines in the global stylesheet."),
            "scrim": leaf("color", "rgba(0, 0, 0, 0.4)", f"{S} computed.emailOverlay.scrim", "Email overlay shader."),
        },
        "fontFamily": {
            "sans": leaf(
                "fontFamily",
                "GT Eesti Text, Helvetica, Arial, sans-serif",
                f"{S} body.fontFamily",
                "UI face. Proprietary, served from westelm.netstorage.",
            ),
            "serif": leaf(
                "fontFamily",
                "Sanomat, Georgia, Times, serif",
                f"{S} computed.heroTitle.fontFamily",
                "Display face for headlines.",
            ),
        },
        "fontWeight": {
            "light": leaf("fontWeight", 300, f"{S} body.fontWeight and hero titles"),
            "book": leaf("fontWeight", 375, f"{S} computed.utilityLink.fontWeight and heroCta.fontWeight", "GT Eesti Text Book."),
            "regular": leaf("fontWeight", 400, f"{S} computed.brandSelected.fontWeight and flagNew.fontWeight"),
        },
        "fontSize": {
            "utility": leaf("dimension", "9px", f"{S} computed.utilityLink.fontSize"),
            "micro": leaf("dimension", "10px", f"{S} computed.categoryNav.fontSize and promoBar.linkFontSize"),
            "caption": leaf("dimension", "12px", f"{S} body.fontSize, footer, secondary nav"),
            "body": leaf("dimension", "14px", f"{S} computed.searchInput.fontSize and heroCta.fontSize"),
            "product": leaf("dimension", "16px", f"{S} computed.productName.fontSize and loginEmail.fontSize"),
            "attribute": leaf("dimension", "18px", f"{S} computed.attributeLabel.fontSize"),
            "service": leaf("dimension", "20px", f"{S} computed.serviceTitle.fontSize"),
            "price": leaf("dimension", "24px", f"{S} computed.salePrice.fontSize"),
            "section": leaf("dimension", "28px", f"{S} computed.sectionTitle.fontSize"),
            "productTitle": leaf("dimension", "32px", f"{S} computed.productTitle.fontSize"),
            "overlay": leaf("dimension", "36px", f"{S} computed.emailOverlay.title.fontSize and familyTitle.fontSize"),
            "hero": leaf("dimension", "48px", f"{S} computed.heroTitle.fontSize"),
        },
        "lineHeight": {
            "utility": leaf("dimension", "11.7px", f"{S} computed.utilityLink.lineHeight"),
            "sister": leaf("dimension", "13px", f"{S} computed.sisterBrand.lineHeight"),
            "saleLabel": leaf("dimension", "14px", f"{S} computed.saleLabel.lineHeight"),
            "button": leaf("dimension", "16.8px", f"{S} computed.heroCta.lineHeight"),
            "search": leaf("dimension", "18.2px", f"{S} computed.searchInput.lineHeight"),
            "footer": leaf("dimension", "18px", f"{S} computed.footer.lineHeight"),
            "product": leaf("dimension", "20.8px", f"{S} computed.productName.lineHeight"),
            "brand": leaf("dimension", "20px", f"{S} computed.brandSelected.lineHeight"),
            "overlayBody": leaf("dimension", "23.4px", f"{S} computed.emailOverlay.body.lineHeight"),
            "price": leaf("dimension", "28px", f"{S} computed.salePrice.lineHeight"),
            "productTitle": leaf("dimension", "40px", f"{S} computed.productTitle.lineHeight and categoryNav.lineHeight"),
            "overlayTitle": leaf("dimension", "45px", f"{S} computed.emailOverlay.title.lineHeight"),
            "hero": leaf("dimension", "60px", f"{S} computed.heroTitle.lineHeight"),
        },
        "letterSpacing": {
            "brand": leaf("dimension", "0.24px", f"{S} computed.brandSelected.letterSpacing"),
            "sister": leaf("dimension", "0.3px", f"{S} computed.sisterBrand.letterSpacing"),
            "secondary": leaf("dimension", "0.36px", f"{S} computed.secondaryNavLink.letterSpacing"),
            "nav": leaf("dimension", "0.4px", f"{S} computed.categoryNav.letterSpacing"),
            "field": leaf("dimension", "0.42px", f"{S} computed.searchInput.letterSpacing"),
            "product": leaf("dimension", "0.48px", f"{S} computed.productName.letterSpacing"),
            "filter": leaf("dimension", "0.5px", f"{S} computed.filterButton.letterSpacing"),
            "overlayBody": leaf("dimension", "0.54px", f"{S} computed.emailOverlay.body.letterSpacing"),
            "productTitle": leaf("dimension", "0.64px", f"{S} computed.productTitle.letterSpacing"),
            "price": leaf("dimension", "0.72px", f"{S} computed.salePrice.letterSpacing"),
            "overlayTitle": leaf("dimension", "0.72px", f"{S} computed.emailOverlay.title.letterSpacing"),
            "hero": leaf("dimension", "0.96px", f"{S} computed.heroTitle.letterSpacing"),
            "saleLabel": leaf("dimension", "1px", f"{S} computed.saleLabel.letterSpacing"),
            "button": leaf("dimension", "1.4px", f"{S} computed.heroCta.letterSpacing"),
            "footerHeading": leaf("dimension", "1.2px", f"{S} computed.footerHeading.letterSpacing"),
            "flag": leaf("dimension", "1.2px", f"{S} computed.flagNew.letterSpacing"),
        },
        "radius": {
            "none": leaf("dimension", "0px", f"{S} computed.heroCta.borderRadius, search, buttons, dialog, swatches", "Square corners are the house shape."),
            "stepper": leaf("dimension", "2px", f"{S} computed.quantityButton.borderRadius left corners", "The only non-zero radius measured on a control."),
        },
        "space": {
            "1": leaf("dimension", "4px", f"{S} computed.saleLabel.padding bottom"),
            "2": leaf("dimension", "5px", f"{S} computed.gridItem.padding"),
            "3": leaf("dimension", "6px", f"{S} computed.brandSelected.padding horizontal and search padding vertical"),
            "4": leaf("dimension", "8px", f"{S} computed.addToCart.padding and productName padding bottom"),
            "5": leaf("dimension", "12px", f"{S} computed.heroCta.padding vertical and filterButton padding horizontal"),
            "6": leaf("dimension", "16px", f"{S} computed.searchInput.padding left and email field padding"),
            "7": leaf("dimension", "20px", f"{S} computed.brandSelected.padding left and footer horizontal padding"),
            "8": leaf("dimension", "24px", f"{S} computed.heroCta.padding horizontal"),
            "9": leaf("dimension", "60px", f"{S} computed.emailOverlay.padding top"),
            "10": leaf("dimension", "83px", f"{S} computed.emailOverlay.padding horizontal"),
        },
        "size": {
            "brandBar": leaf("dimension", "32px", f"{S} computed.brandBar.height"),
            "search": leaf("dimension", "36px", f"{S} computed.searchInput.height"),
            "navItem": leaf("dimension", "40px", f"{S} computed.categoryNav.height"),
            "button": leaf("dimension", "42px", f"{S} computed.loginSubmit.height"),
            "stepper": leaf("dimension", "44px", f"{S} computed.quantityButton.height"),
            "field": leaf("dimension", "56px", f"{S} computed.emailOverlay.emailField.height"),
            "loginField": leaf("dimension", "59px", f"{S} computed.loginEmail.height"),
            "addToCart": leaf("dimension", "52px", f"{S} computed.addToCart.height"),
            "promo": leaf("dimension", "54px", f"{S} computed.promoBar.height"),
            "accordion": leaf("dimension", "69px", f"{S} computed.accordion.height"),
            "searchWidth": leaf("dimension", "300px", f"{S} computed.searchInput.width"),
            "swatch": leaf("dimension", "132px", f"{S} computed.swatchThumb.width"),
            "cardImage": leaf("dimension", "360px", f"{S} computed.gridItem.image.width"),
            "dialog": leaf("dimension", "726px", f"{S} computed.emailOverlay.width"),
        },
        "shadow": {
            "dialog": leaf(
                "shadow",
                "0px 0px 11px 0px rgba(0, 0, 0, 0.16)",
                f"{S} computed.emailOverlay.boxShadow",
            ),
        },
        "duration": {
            "color": leaf("duration", "500ms", f"{S} stylesheetRules.transition background-color .5s"),
        },
        "easing": {
            "color": leaf(
                "cubicBezier",
                [0.4, 0.8, 0.4, 0.8],
                f"{S} stylesheetRules.transition cubic-bezier(0.4, 0.8, 0.4, 0.8)",
            ),
        },
        "typography": {
            "hero": leaf("typography", {
                "fontFamily": "{fontFamily.serif}",
                "fontWeight": "{fontWeight.light}",
                "fontSize": "{fontSize.hero}",
                "lineHeight": "{lineHeight.hero}",
                "letterSpacing": "{letterSpacing.hero}",
            }, f"{S} computed.heroTitle"),
            "productTitle": leaf("typography", {
                "fontFamily": "{fontFamily.serif}",
                "fontWeight": "{fontWeight.light}",
                "fontSize": "{fontSize.productTitle}",
                "lineHeight": "{lineHeight.productTitle}",
                "letterSpacing": "{letterSpacing.productTitle}",
            }, f"{S} computed.productTitle"),
            "overlayTitle": leaf("typography", {
                "fontFamily": "{fontFamily.serif}",
                "fontWeight": "{fontWeight.light}",
                "fontSize": "{fontSize.overlay}",
                "lineHeight": "{lineHeight.overlayTitle}",
                "letterSpacing": "{letterSpacing.overlayTitle}",
            }, f"{S} computed.emailOverlay.title"),
            "section": leaf("typography", {
                "fontFamily": "{fontFamily.serif}",
                "fontWeight": "{fontWeight.light}",
                "fontSize": "{fontSize.section}",
            }, f"{S} computed.sectionTitle"),
            "productName": leaf("typography", {
                "fontFamily": "{fontFamily.sans}",
                "fontWeight": "{fontWeight.light}",
                "fontSize": "{fontSize.product}",
                "lineHeight": "{lineHeight.product}",
                "letterSpacing": "{letterSpacing.product}",
            }, f"{S} computed.productName"),
            "body": leaf("typography", {
                "fontFamily": "{fontFamily.sans}",
                "fontWeight": "{fontWeight.light}",
                "fontSize": "{fontSize.body}",
                "lineHeight": "{lineHeight.search}",
                "letterSpacing": "{letterSpacing.field}",
            }, f"{S} computed.searchInput"),
            "nav": leaf("typography", {
                "fontFamily": "{fontFamily.sans}",
                "fontWeight": "{fontWeight.light}",
                "fontSize": "{fontSize.micro}",
                "lineHeight": "{lineHeight.productTitle}",
                "letterSpacing": "{letterSpacing.nav}",
            }, f"{S} computed.categoryNav"),
            "button": leaf("typography", {
                "fontFamily": "{fontFamily.sans}",
                "fontWeight": "{fontWeight.light}",
                "fontSize": "{fontSize.body}",
                "letterSpacing": "{letterSpacing.button}",
            }, f"{S} computed.loginSubmit and heroCta"),
            "utility": leaf("typography", {
                "fontFamily": "{fontFamily.sans}",
                "fontWeight": "{fontWeight.book}",
                "fontSize": "{fontSize.utility}",
                "lineHeight": "{lineHeight.utility}",
                "letterSpacing": "{letterSpacing.price}",
            }, f"{S} computed.utilityLink"),
            "footer": leaf("typography", {
                "fontFamily": "{fontFamily.sans}",
                "fontWeight": "{fontWeight.light}",
                "fontSize": "{fontSize.caption}",
                "lineHeight": "{lineHeight.footer}",
                "letterSpacing": "{letterSpacing.secondary}",
            }, f"{S} computed.footer"),
        },
    }

    light = {
        "$description": "Semantic roles from the one theme the public pages showed.",
        "background": {
            "page": alias("color.white", f"{S} dialog, fields and hero CTA sit on white; body itself is transparent"),
            "sunken": alias("color.gray100", f"{S} computed.brandBar and footer"),
            "surface": alias("color.white", f"{S} computed.emailOverlay.backgroundColor"),
            "scrim": alias("color.scrim", f"{S} computed.emailOverlay.scrim"),
            "promo": alias("color.promo", f"{S} computed.promoBar.backgroundColor"),
            "inverse": alias("color.ink", f"{S} computed.loginSubmit.backgroundColor"),
        },
        "text": {
            "primary": alias("color.ink", f"{S} body.color"),
            "muted": alias("color.gray700", f"{S} computed.footerLink.color"),
            "label": alias("color.gray600", f"{S} computed.loginLabel.color"),
            "inverse": alias("color.white", f"{S} computed.addToCart.color"),
            "sale": alias("color.sale", f"{S} computed.salePrice.color"),
            "disabled": alias("color.gray400", f"{S} computed.quantityButton.color"),
        },
        "border": {
            "default": alias("color.gray200", f"{S} computed.categoryNavRule and swatchThumb"),
            "field": alias("color.gray300", f"{S} computed.searchInput.border"),
            "strong": alias("color.ink", f"{S} computed.loginEmail.border and filterButton.border"),
            "select": alias("color.gray500", f"{S} computed.select.border"),
        },
        "action": {
            "primary": alias("color.ink", f"{S} computed.loginSubmit.backgroundColor", "Filled square button."),
            "conversion": alias("color.sale", f"{S} computed.addToCart.backgroundColor", "Add to cart only."),
            "conversionHover": alias("color.saleHover", f"{S} stylesheet hover, not a live hover"),
        },
        "focus": {
            "ring": alias("color.focus", f"{S} stylesheet :focus-visible outline #2563eb"),
        },
        "component": {
            "button": {
                "background": alias("color.ink", f"{S} computed.loginSubmit.backgroundColor"),
                "text": alias("color.white", f"{S} computed.loginSubmit.color"),
                "radius": leaf("dimension", "{radius.none}", f"{S} computed.loginSubmit.borderRadius"),
                "padding": leaf("dimension", "8px", f"{S} computed.loginSubmit.padding"),
                "height": leaf("dimension", "{size.button}", f"{S} computed.loginSubmit.height"),
            },
            "field": {
                "background": alias("color.white", f"{S} computed.loginEmail.backgroundColor"),
                "text": alias("color.ink", f"{S} computed.loginEmail.color"),
                "radius": leaf("dimension", "{radius.none}", f"{S} computed.loginEmail.borderRadius"),
                "padding": leaf("dimension", "16px", f"{S} computed.loginEmail.padding horizontal"),
                "height": leaf("dimension", "{size.loginField}", f"{S} computed.loginEmail.height"),
            },
        },
    }

    tokens = {
        "core": core,
        "light": light,
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}
        ],
    }
    check(tokens)
    OUT.write_text(json.dumps(tokens, indent=1) + "\n")
    print(f"wrote {OUT}")


def check(tokens):
    """Refuse a leaf with no source, a bad colour, or a dimension that is not one length."""
    def walk(node, path):
        if not isinstance(node, dict):
            return
        if "$value" in node:
            if not node.get("$extensions", {}).get("source"):
                raise ValueError(f"{path}: no source")
            type_ = node.get("$type")
            value = node["$value"]
            if isinstance(value, str) and value.startswith("{"):
                return
            if type_ == "color" and color(value) != value:
                raise ValueError(f"{path}: colour {value!r} is not lower-case #rrggbb(aa)")
            if type_ == "dimension" and not DIM.fullmatch(str(value)):
                raise ValueError(f"{path}: dimension {value!r}")
            return
        for key, child in node.items():
            if key.startswith("$"):
                continue
            walk(child, f"{path}.{key}" if path else key)
    walk(tokens, "")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
