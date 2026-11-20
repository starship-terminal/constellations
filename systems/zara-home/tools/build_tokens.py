#!/usr/bin/env python3
"""Build tokens.json from raw/readings.json.

Every leaf is a value read on zarahome.com on 2026-11-19 (computed style or a
declared custom property). The builder refuses a leaf with no source. The
public pages showed one light theme, so there is no dark set.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw" / "readings.json"
OUT = HERE / "tokens.json"

DIM = re.compile(r"-?\d+(\.\d+)?(px|rem|em)")


def color(value):
    value = value.strip().lower()
    match = re.fullmatch(r"#([0-9a-f]{3}|[0-9a-f]{6})", value)
    if match:
        hexes = match.group(1)
        if len(hexes) == 3:
            hexes = "".join(ch * 2 for ch in hexes)
        return "#" + hexes
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


def check(doc):
    """Refuse a leaf with no source, a dimension that is not one length, a colour that is not
    #rrggbb(aa), a malformed alias, an alias (at any depth of a value) that resolves neither in its
    own set nor in core, and an alias chain that loops."""
    def leaves(node, path=""):
        if not isinstance(node, dict):
            return
        if "$value" in node:
            yield path, node
            return
        for key, child in node.items():
            if not key.startswith("$"):
                yield from leaves(child, f"{path}.{key}" if path else key)

    def strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for v in value.values():
                yield from strings(v)
        elif isinstance(value, list):
            for v in value:
                yield from strings(v)

    def alias_refs(value, where):
        """Every alias inside a value, at any depth. A string holding a brace must be one whole alias."""
        refs = []
        for text in strings(value):
            if "{" in text or "}" in text:
                m = re.fullmatch(r"\{([A-Za-z0-9_.-]+)\}", text)
                if not m:
                    raise ValueError(f"{where} malformed alias {text!r}")
                refs.append(m.group(1))
        return refs

    def follow(ref, own, core, where, chain):
        """Resolve ref in its own set, then core, then follow the target's aliases; refuse a cycle."""
        if ref in chain:
            raise ValueError(f"{where} alias cycle through {{{ref}}}")
        target = own.get(ref) or core.get(ref)
        if target is None:
            raise ValueError(f"{where} alias {{{ref}}} points at nothing")
        for nxt in alias_refs(target["$value"], where):
            follow(nxt, own if ref in own else core, core, where, chain + [ref])

    sets = [k for k in doc if not k.startswith("$")]
    core = {p: t for p, t in leaves(doc.get("core", {}))}
    for name in sets:
        own = {p: t for p, t in leaves(doc[name])}
        for path, node in own.items():
            where = f"{name}.{path}"
            if "$extensions" not in node or "source" not in node.get("$extensions", {}):
                raise ValueError(f"{where} has no source")
            value = node["$value"]
            refs = alias_refs(value, where)
            for ref in refs:
                follow(ref, own, core, where, [path])
            if isinstance(value, str) and refs:
                continue
            if node.get("$type") == "dimension" and isinstance(value, str) and not DIM.fullmatch(value):
                raise ValueError(f"{where} dimension {value!r}")
            if node.get("$type") == "color" and not re.fullmatch(r"#[0-9a-f]{6}([0-9a-f]{2})?", str(value)):
                raise ValueError(f"{where} colour {value!r}")


S = "raw/readings.json"


def main():
    readings = json.loads(RAW.read_text())
    computed = readings["computed"]
    props = readings["customProperties"]
    assert computed["worldwideGo"]["backgroundColor"] == "rgb(30, 30, 30)"
    assert props["--primary-color"] == "#1e1e1e"

    core = {
        "$description": "Scales read from zarahome.com public pages on 2026-11-19. One light theme.",
        "color": {
            "ink": leaf("color", "#1e1e1e", f"{S} computed.worldwideGo.backgroundColor and --primary-color", "House ink. Buttons, prices, footer headings."),
            "ink87": leaf("color", "rgba(0, 0, 0, 0.87)", f"{S} computed.productTitle.color and --mat-app-text-color", "Material body ink on product titles and the search field."),
            "black": leaf("color", "#000000", f"{S} body.color and computed.marketButton.color", "Body and the market switch. Not the filled-button ink."),
            "white": leaf("color", "#ffffff", f"{S} body.backgroundColor and computed.headerCategory.backgroundColor", "Page and category header."),
            "white80": leaf("color", "rgba(255, 255, 255, 0.8)", f"{S} computed.addOnCard.backgroundColor", "Add control sitting on a product photo."),
            "muted": leaf("color", "#8e8e93", f"{S} computed.sku.color and --primary-darker-color", "SKU and product description."),
            "mutedLight": leaf("color", "#d1d1d6", f"{S} customProperties.--primary-lighter-color", "Declared lighter primary. Not seen as a fill."),
            "rule": leaf("color", "#d8d8dc", f"{S} customProperties.--footer-v2-rule", "Footer rule, declared, not a computed border on a measured element."),
            "focus": leaf("color", "#2684ff", f"{S} computed.focusVisible.outline and --footer-v2-focus", "Focus outline. Stylesheet rule, not a live focus."),
            "accentBlue": leaf("color", "#007aff", f"{S} customProperties.--accent-darker-color", "Declared accent darker. Swiper theme uses the same hex. Not a button fill."),
            "sale": leaf("color", "#cf0a2c", f"{S} customProperties.--accent-lighter-color", "Declared accent lighter. No sale price used it on the captured pages."),
            "warn": leaf("color", "#b32624", f"{S} customProperties.--warn-color", "Material warn and filled-button token. Zara Home buttons on these pages used ink."),
            "warnWash": leaf("color", "#ffd8d6", f"{S} customProperties.--warn-lighter-color", "Declared warn wash. Not seen as a fill."),
            "hover": leaf("color", "#3a3a3c", f"{S} computed.buttonHover.backgroundColor", "button.mdc-button:hover. Stylesheet, not a live hover."),
            "hairline": leaf("color", "rgba(0, 0, 0, 0.12)", f"{S} computed.chooseSize.border", "Choose a size outline."),
        },
        "fontFamily": {
            "sans": leaf(
                "fontFamily",
                'ZH-Sans, Arial, "Lucida Sans Unicode", sans-serif',
                f"{S} body.fontFamily and fonts.stack",
                "ZH-Sans is ZaraAPPSans, served as woff2. Proprietary. Not committed.",
            )
        },
        "fontWeight": {
            "thin": leaf("fontWeight", 100, f"{S} fonts.weights"),
            "extraLight": leaf("fontWeight", 200, f"{S} fonts.weights"),
            "light": leaf("fontWeight", 300, f"{S} computed.footerLink.fontWeight and dialogHello.fontWeight"),
            "regular": leaf("fontWeight", 400, f"{S} body.fontWeight"),
            "medium": leaf("fontWeight", 500, f"{S} computed.footerHeading.fontWeight and priceGrid.fontWeight"),
            "semibold": leaf("fontWeight", 600, f"{S} computed.worldwideGo.fontWeight and productTitle.fontWeight"),
            "bold": leaf("fontWeight", 700, f"{S} computed.worldwideTitle.fontWeight and fonts.weights"),
        },
        "fontSize": {
            "micro": leaf("dimension", "10px", f"{S} computed.lookName.fontSize and dialogFooter.fontSize"),
            "caption": leaf("dimension", "11px", f"{S} computed.filters.fontSize and sku.fontSize"),
            "button": leaf("dimension", "12px", f"{S} computed.worldwideGo.fontSize and footerHeading.fontSize"),
            "body": leaf("dimension", "14px", f"{S} body.fontSize"),
            "header": leaf("dimension", "18px", f"{S} computed.headerSearch.fontSize and productPrice.fontSize"),
            "product": leaf("dimension", "22px", f"{S} computed.productTitle.fontSize"),
            "search": leaf("dimension", "30px", f"{S} computed.searchInput.fontSize"),
        },
        "lineHeight": {
            "micro": leaf("dimension", "14px", f"{S} computed.lookName.lineHeight and dialogFooter.lineHeight"),
            "caption": leaf("dimension", "15px", f"{S} computed.filters.lineHeight"),
            "footer": leaf("dimension", "16px", f"{S} computed.footerHeading.lineHeight and worldwideGo.lineHeight"),
            "body": leaf("dimension", "18px", f"{S} body.lineHeight"),
            "description": leaf("dimension", "20px", f"{S} computed.description.lineHeight"),
            "header": leaf("dimension", "22px", f"{S} computed.headerSearch.lineHeight and productPrice.lineHeight"),
            "product": leaf("dimension", "24px", f"{S} computed.productTitle.lineHeight"),
        },
        "letterSpacing": {
            "body": leaf("dimension", "0.2px", f"{S} body.letterSpacing"),
        },
        "radius": {
            "none": leaf("dimension", "0px", f"{S} computed.worldwideGo.borderRadius and searchInput.borderRadius", "Buttons, fields, dialog, swatches."),
            "cookie": leaf("dimension", "2px", f"{S} computed.cookieAllow.borderRadius", "OneTrust Allow All. Not a storefront control."),
        },
        "space": {
            "iconGap": leaf("dimension", "5px", f"{S} customProperties.--footer-v2-icon-gap"),
            "small": leaf("dimension", "8px", f"{S} customProperties.--footer-space-small and footerLink.marginBottom"),
            "headerPad": leaf("dimension", "10px", f"{S} computed.headerHome.padding"),
            "gutter": leaf("dimension", "14px", f"{S} customProperties.--footer-gutter"),
            "inset": leaf("dimension", "15px", f"{S} customProperties.--footer-page-inset and worldwideField.marginBottom"),
            "buttonPad": leaf("dimension", "16px", f"{S} computed.worldwideGo.padding and --footer-space-medium"),
            "goGap": leaf("dimension", "25px", f"{S} computed.worldwideGo.marginTop"),
            "block": leaf("dimension", "40px", f"{S} customProperties.--footer-block-padding and worldwideTitle.marginBottom"),
            "section": leaf("dimension", "60px", f"{S} customProperties.--footer-space-section"),
            "logoLeft": leaf("dimension", "60px", f"{S} worldwide gate logo margin-left, measured 60px"),
        },
        "size": {
            "swatch": leaf("dimension", "20px", f"{S} computed.swatch.width"),
            "header": leaf("dimension", "50px", f"{S} computed.headerHome.height"),
            "button": leaf("dimension", "36px", f"{S} computed.worldwideGo.height and chooseSize.height"),
            "dialogButton": leaf("dimension", "40px", f"{S} computed.dialogPrimary.height and --footer-cta-height"),
            "touch": leaf("dimension", "44px", f"{S} customProperties.--footer-touch-target and subscribe.height"),
            "field": leaf("dimension", "75px", f"{S} computed.worldwideField.height"),
            "subscribe": leaf("dimension", "310px", f"{S} computed.subscribe.width"),
            "dialog": leaf("dimension", "512px", f"{S} computed.dialogSurface.paneWidth"),
            "logo": leaf("dimension", "150px", f"{S} computed.logo.width"),
        },
        "typography": {
            "body": leaf("typography", {
                "fontFamily": "{fontFamily.sans}",
                "fontWeight": "{fontWeight.regular}",
                "fontSize": "{fontSize.body}",
                "lineHeight": "{lineHeight.body}",
                "letterSpacing": "{letterSpacing.body}",
            }, f"{S} body"),
            "footerLink": leaf("typography", {
                "fontFamily": "{fontFamily.sans}",
                "fontWeight": "{fontWeight.light}",
                "fontSize": "{fontSize.button}",
                "lineHeight": "{lineHeight.footer}",
                "letterSpacing": "{letterSpacing.body}",
            }, f"{S} computed.footerLink"),
            "footerHeading": leaf("typography", {
                "fontFamily": "{fontFamily.sans}",
                "fontWeight": "{fontWeight.medium}",
                "fontSize": "{fontSize.button}",
                "lineHeight": "{lineHeight.footer}",
                "letterSpacing": "{letterSpacing.body}",
            }, f"{S} computed.footerHeading"),
            "button": leaf("typography", {
                "fontFamily": "{fontFamily.sans}",
                "fontWeight": "{fontWeight.semibold}",
                "fontSize": "{fontSize.button}",
                "lineHeight": "{lineHeight.footer}",
                "letterSpacing": "{letterSpacing.body}",
            }, f"{S} computed.worldwideGo"),
            "productTitle": leaf("typography", {
                "fontFamily": "{fontFamily.sans}",
                "fontWeight": "{fontWeight.semibold}",
                "fontSize": "{fontSize.product}",
                "lineHeight": "{lineHeight.product}",
                "letterSpacing": "{letterSpacing.body}",
            }, f"{S} computed.productTitle"),
            "productPrice": leaf("typography", {
                "fontFamily": "{fontFamily.sans}",
                "fontWeight": "{fontWeight.semibold}",
                "fontSize": "{fontSize.header}",
                "lineHeight": "{lineHeight.header}",
                "letterSpacing": "{letterSpacing.body}",
            }, f"{S} computed.productPrice"),
            "search": leaf("typography", {
                "fontFamily": "{fontFamily.sans}",
                "fontWeight": "{fontWeight.medium}",
                "fontSize": "{fontSize.search}",
                "lineHeight": "{lineHeight.body}",
                "letterSpacing": "{letterSpacing.body}",
            }, f"{S} computed.searchInput"),
            "caption": leaf("typography", {
                "fontFamily": "{fontFamily.sans}",
                "fontWeight": "{fontWeight.regular}",
                "fontSize": "{fontSize.caption}",
                "lineHeight": "{lineHeight.caption}",
                "letterSpacing": "{letterSpacing.body}",
            }, f"{S} computed.filters"),
            "dialogHello": leaf("typography", {
                "fontFamily": "{fontFamily.sans}",
                "fontWeight": "{fontWeight.light}",
                "fontSize": "{fontSize.header}",
                "lineHeight": "{lineHeight.header}",
                "letterSpacing": "{letterSpacing.body}",
            }, f"{S} computed.dialogHello"),
            "micro": leaf("typography", {
                "fontFamily": "{fontFamily.sans}",
                "fontWeight": "{fontWeight.light}",
                "fontSize": "{fontSize.micro}",
                "lineHeight": "{lineHeight.micro}",
                "letterSpacing": "{letterSpacing.body}",
            }, f"{S} computed.dialogFooter"),
        },
        "shadow": {
            "none": leaf("shadow", "none", f"{S} computed.headerHome.boxShadow and dialogSurface.boxShadow"),
            "fab": leaf(
                "shadow",
                "0px 3px 5px -1px rgba(0, 0, 0, 0.2), 0px 6px 10px 0px rgba(0, 0, 0, 0.14), 0px 1px 18px 0px rgba(0, 0, 0, 0.12)",
                f"{S} computed.chatFab.boxShadow",
                "The only measured elevation. A round white control on the product page.",
            ),
        },
    }
    light = {
        "$description": "The one theme the public pages showed.",
        "background": {
            "page": alias("color.white", f"{S} body.backgroundColor"),
            "surface": alias("color.white", f"{S} computed.dialogSurface.backgroundColor"),
            "header": alias("color.white", f"{S} computed.headerCategory.backgroundColor", "Solid on category and product. Transparent over the homepage hero."),
            "add": alias("color.white80", f"{S} computed.addOnCard.backgroundColor"),
        },
        "text": {
            "primary": alias("color.ink", f"{S} computed.footerHeading.color"),
            "body": alias("color.ink87", f"{S} computed.productTitle.color"),
            "muted": alias("color.muted", f"{S} computed.description.color"),
            "inverse": alias("color.white", f"{S} computed.worldwideGo.color"),
            "black": alias("color.black", f"{S} body.color"),
        },
        "action": {
            "primary": alias("color.ink", f"{S} computed.worldwideGo.backgroundColor"),
            "primaryText": alias("color.white", f"{S} computed.worldwideGo.color"),
            "hover": alias("color.hover", f"{S} computed.buttonHover.backgroundColor"),
        },
        "border": {
            "default": alias("color.ink", f"{S} computed.worldwideGo.border and dialogSecondary.border"),
            "hairline": alias("color.hairline", f"{S} computed.chooseSize.border"),
            "rule": alias("color.rule", f"{S} customProperties.--footer-v2-rule"),
            "focus": alias("color.focus", f"{S} computed.focusVisible.outline"),
        },
        "component": {
            "button": {
                "background": alias("color.ink", f"{S} computed.worldwideGo.backgroundColor"),
                "text": alias("color.white", f"{S} computed.worldwideGo.color"),
                "radius": leaf("dimension", "0px", f"{S} computed.worldwideGo.borderRadius"),
                "height": leaf("dimension", "36px", f"{S} computed.worldwideGo.height"),
                "padding": leaf("dimension", "16px", f"{S} computed.worldwideGo.padding horizontal"),
            },
            "field": {
                "text": alias("color.ink87", f"{S} computed.searchInput.color"),
                "radius": leaf("dimension", "0px", f"{S} computed.searchInput.borderRadius"),
                "height": leaf("dimension", "35px", f"{S} computed.searchInput.height"),
            },
        },
    }

    doc = {
        "core": core,
        "light": light,
        "$themes": [
            {
                "id": "light",
                "name": "Light",
                "selectedTokenSets": {"core": "source", "light": "enabled"},
                "$extensions": {"source": f"{S} theme light, the only theme shown"},
            }
        ],
    }
    check(doc)
    return doc


def render():
    """tokens.json's exact text; nothing is written."""
    return json.dumps(main(), indent=1) + "\n"


def write():
    OUT.write_text(render())
    print(f"wrote {OUT}")


if __name__ == "__main__":
    write()
