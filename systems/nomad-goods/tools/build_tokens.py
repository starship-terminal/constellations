#!/usr/bin/env python3
"""Build tokens.json from systems/nomad-goods/raw/readings.json.

Values are the ones read on nomadgoods.com/sg on 2026-11-19. A value labelled
Measured is taken from a computed style in raw/readings.json by R(), which
fails when the reading is missing. The class rules that were read from the
Shopify CSS files the page linked are not saved in raw/ (the file holds their
names only), so each value that came only from those files is labelled
Reconstruction: typed in by hand at capture time. Dark theme was not on the
public pages.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RAW = json.loads((ROOT / "raw" / "readings.json").read_text())

M = "Measured"
D = "Derived"
X = "Reconstruction"
HAND = "Entered by hand at capture time from {}; the stylesheet is not saved in raw/, so no file holds this reading."


def R(path):
    """A reading from raw/readings.json `computed`, by dotted path; a missing one stops the build."""
    node = RAW["computed"]
    for key in path.split("."):
        if not isinstance(node, dict) or key not in node:
            raise SystemExit(f"raw/readings.json has no computed.{path}")
        node = node[key]
    return node


def hexes(text):
    """Every rgb()/rgba() colour in a computed value, as #rrggbb or #rrggbbaa."""
    out = []
    for m in re.finditer(r"rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)", text):
        rgb = "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
        a = m.group(4)
        out.append(rgb if a is None or float(a) >= 1 else rgb + "%02x" % round(float(a) * 255))
    if not out:
        raise SystemExit(f"no colour in {text!r}")
    return out


def lengths(text):
    """The px lengths in a computed value, in order ("0px 24px" -> ["0px", "24px"])."""
    return re.findall(r"-?\d+(?:\.\d+)?px", text)


def shadow_lengths(text):
    """offset-x, offset-y, blur and spread of a one-layer computed box-shadow, colour removed."""
    rest = re.sub(r"rgba?\([^)]*\)", "", text)
    found = lengths(rest)
    if len(found) != 4:
        raise SystemExit(f"expected four lengths in the shadow {text!r}")
    return found


def hand(token, stylesheet):
    """Relabel a token whose value was typed in from a stylesheet that raw/ does not hold."""
    token["$extensions"]["evidence"] = X
    token["$extensions"]["source"] += ". " + HAND.format(stylesheet)
    return token


def color(value, source, evidence=M):
    return {
        "$type": "color",
        "$value": value,
        "$extensions": {"source": source, "evidence": evidence},
    }


def duration(value, source, evidence=M):
    return {
        "$type": "duration",
        "$value": value,
        "$extensions": {"source": source, "evidence": evidence},
    }


def dim(value, source, evidence=M):
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": source, "evidence": evidence},
    }


def font(value, source):
    return {
        "$type": "fontFamily",
        "$value": value,
        "$extensions": {"source": source, "evidence": M},
    }


def number(value, source, evidence=M):
    return {
        "$type": "number",
        "$value": value,
        "$extensions": {"source": source, "evidence": evidence},
    }


def shadow(value, source):
    return {
        "$type": "shadow",
        "$value": value,
        "$extensions": {"source": source, "evidence": M},
    }


def typography(family, size, weight, line_height, tracking, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line_height,
            "letterSpacing": tracking,
        },
        "$extensions": {"source": source, "evidence": M},
    }


def typo(family, reading, source, weight=None, tracking=None):
    """A type style from one computed reading: size, line height and tracking as the browser computed them.
    `weight` / `tracking` fill a field the reading lacks, and the source says so."""
    r = R(reading)
    fills = []
    if weight is None:
        weight = int(r["fontWeight"])
    else:
        fills.append(f"font-weight {weight} is the class's weight on the other readings, not read here")
    if tracking is None:
        ls = r.get("letterSpacing")
        if ls is None:
            tracking = "0px"
            fills.append("letter-spacing not read, written 0px")
        elif ls == "normal":
            tracking = "0px"
            fills.append("letter-spacing computed normal, written 0px")
        else:
            tracking = ls
    else:
        fills.append(f"letter-spacing not read, written {tracking}")
    note = f"{source}: computed {r['fontSize']} / {r['lineHeight']} ({reading})"
    if fills:
        note += "; " + "; ".join(fills)
    return typography(family, r["fontSize"], weight, r["lineHeight"], tracking, note)


def typo_hand(family, size, weight, line_height, tracking, source, stylesheet):
    return hand(typography(family, size, weight, line_height, tracking, source), stylesheet)


def build():
    """The token document, built in memory from raw/readings.json; main() writes it."""
    page = "getComputedStyle on https://nomadgoods.com/sg/ at 1440x900, 2026-11-19"
    light_btn = hexes(R("buttonLightMd.backgroundImage"))
    dark_btn = hexes(R("buttonDarkMd.backgroundImage"))
    dark_shadow = hexes(R("buttonDarkMd.boxShadow"))
    core = {
        "font": {
            "family": {
                "display": font(R("h1Home.fontFamily"), "computed font-family on h1.type-title-lg (h1Home)"),
                "ui": font(R("fieldMd.fontFamily"), "computed font-family on input.field (fieldMd)"),
                "body": font(R("body.fontFamily").replace('"', ""), "computed font-family on body"),
            }
        },
        "color": {
            "black": color(hexes(R("body.color"))[0], f"body color; {page}"),
            "white": color(hexes(R("fieldMd.backgroundColor"))[0], ".field computed background (fieldMd)"),
            "page": color(hexes(R("body.backgroundColor"))[0], "body computed background-color"),
            "ink-soft": color(light_btn[-1], "button-light gradient end (buttonLightMd.backgroundImage)"),
            "charcoal": color(dark_btn[0], "button-dark background-image (buttonDarkMd)"),
            "inset": color(dark_shadow[0], "button-dark inset shadow (buttonDarkMd.boxShadow)"),
            "hairline": color(dark_shadow[1], "button-dark inset ring (buttonDarkMd.boxShadow)"),
            "disabled": hand(color("#adadad", "buttons.css .button-dark:disabled background #adadad"), "buttons.css"),
            "muted": hand(color("#6b6b6b", "fields.css placeholder and .field-muted-text #6b6b6b"), "fields.css"),
            "danger": hand(color("#e3163b", "fields.css .field-error and .field-error-text #e3163b"), "fields.css"),
            "info": color(hexes(R("pillNew.backgroundColor"))[0], "computed .type-pill NEW background (pillNew)"),
            "sale": color(hexes(R("pillSale.backgroundColor"))[0], "computed .type-pill Black Friday and HOT background (pillSale)"),
            "link-blue": hand(color("#007aff", "css-bundle.css uses #007aff five times; not seen on the measured controls"), "css-bundle.css"),
            "near-black": color(hexes(R("klaviyoModal.buttonBackground"))[0], "Klaviyo Sign Up button background (klaviyoModal)"),
            "scrim": color(hexes(R("phoneMenu.scrim"))[0], "phone menu scrim (phoneMenu.scrim); the Klaviyo scrim was rgba(0, 0, 0, 0.5)"),
        },
        "typography": {
            "display": typo("{core.font.family.display}", "h1Home", "h1.type-title-lg at 1440"),
            "display-mobile": typo("{core.font.family.display}", "h1AboutPhone", "h1.type-title-lg on about at 390", weight=700),
            "title-section": typo("{core.font.family.display}", "h2Section", "h2.type-title-section at 1440"),
            "title-md": typo_hand("{core.font.family.display}", "50px", 700, "0.95", "-0.04em",
                                  "h2.type-title-md computed 50px / 47.5px / -2px on about at 1440; type.css 3.125rem from 768px", "type.css"),
            "page-title": typo("{core.font.family.display}", "pageTitle", "product h1.type-page-title at 1440"),
            "heading-md": typo_hand("{core.font.family.display}", "24px", 700, "1.11", "-0.04em",
                                    "p.type-heading-md computed 24px / 26.64px / -0.96px on the collection page; type.css 1.5rem from 768px", "type.css"),
            "heading-sm": typo("{core.font.family.display}", "headingSm", "footer h3.type-heading-sm"),
            "price": typo("{core.font.family.display}", "price", ".type-price on the product page"),
            "body-lg": typo("{core.font.family.body}", "bodyLg", "about paragraph .type-body-lg at 1440"),
            "body": typo("{core.font.family.body}", "body", "body"),
            "body-sm": typo_hand("{core.font.family.body}", "14px", 400, "1.5", "0em",
                                 "type.css .type-body-sm 0.875rem, line-height 1.5; footer signup copy uses that class", "type.css"),
            "fine-print": typo_hand("{core.font.family.body}", "12px", 400, "1.5", "0em",
                                    "type.css .type-fine-print 0.75rem, line-height 1.5", "type.css"),
            "button-md": typo("{core.font.family.display}", "buttonLightMd", "Shop Now, button-md"),
            "button-sm": typo("{core.font.family.display}", "buttonSm", "footer Submit, button-sm", weight=700),
            "field": typo("{core.font.family.ui}", "fieldMd", "input.field", weight=400),
            "detail-sm": typo("{core.font.family.ui}", "detailSm", "collection card caption .type-detail-sm"),
            "pill": typo("{core.font.family.display}", "pillNew", ".type-pill, uppercase", weight=700),
        },
        "space": {
            "2": hand(dim("2px", "tab-bar padding in buttons.css"), "buttons.css"),
            "4": hand(dim("4px", "drawer row padding 4px"), "the drawer's computed padding, which raw/readings.json does not hold"),
            "8": dim(R("rootVars.frameWidth"), ":root --frame-width (rootVars.frameWidth)"),
            "10": dim(R("rootVars.gridEdge"), ":root --grid-edge (rootVars.gridEdge)"),
            "12": dim(R("rootVars.frameWidth768"), "--frame-width from 768px (rootVars.frameWidth768)"),
            "16": dim(lengths(R("fieldSm.padding"))[1], "field-sm padding-inline (fieldSm.padding)"),
            "20": dim(lengths(R("buttonSm.padding"))[1], "button-sm padding-inline (buttonSm.padding); --grid-edge from 1200px is the same 20px"),
            "24": dim(lengths(R("buttonLightMd.padding"))[1], "button-md padding-inline (buttonLightMd.padding)"),
            "25": dim(R("rootVars.gridGutter"), ":root --grid-gutter (rootVars.gridGutter); .surface-card radius is 25px too"),
            "30": dim(lengths(R("navLink.padding"))[1], "nav link padding-inline (navLink.padding); product card padding-top is 30px too"),
            "40": dim(R("rootVars.gridGutter480"), "--grid-gutter from 480px (rootVars.gridGutter480); product card padding-inline is 40px too"),
            "50": dim(R("footer.borderTopWidth"), "footer border-top-width (footer.borderTopWidth)"),
            "70": dim(lengths(R("footer.padding"))[0], "footer padding-block (footer.padding)"),
            "100": dim(R("rootVars.textCardEdge1024"), "--text-card-edge from 1024px (rootVars.textCardEdge1024)"),
        },
        "radius": {
            "none": hand(dim("0px", "body and announcement radius"), "the computed radius of body and the announcement bar, which raw/readings.json does not hold"),
            "checkbox": hand(dim("6px", "fields.css .field-checkbox border-radius:6px"), "fields.css"),
            "tab-selected": hand(dim("13px", "buttons.css .tab-bar-selected border-radius:13px"), "buttons.css"),
            "status": hand(dim("15px", "labels.css .status-box border-radius:15px"), "labels.css"),
            "tab-bar": hand(dim("16px", "buttons.css .tab-bar border-radius:16px"), "buttons.css"),
            "popover": dim(R("surfacePopover.borderRadius"), ".surface-popover computed radius (surfacePopover)"),
            "textarea": hand(dim("24px", "fields.css .field-textarea border-radius:24px"), "fields.css"),
            "card": dim(R("surfaceCard.borderRadius"), ".surface-card computed radius (surfaceCard)"),
            "dialog": dim(R("klaviyoModal.borderRadius"), "Klaviyo form computed radius (klaviyoModal)"),
            "pill": dim(R("buttonLightMd.borderRadius"), "button-md computed radius (buttonLightMd); .field-md is the same 100px"),
            "round": dim(R("colorSwatch.borderRadius"), "colour swatch computed radius (colorSwatch)"),
        },
        "border": {
            "none": hand(dim("0px", "button-light border 0, buttons.css"), "buttons.css"),
            "hairline": dim(lengths(R("buttonDarkMd.border"))[0], "button-dark border 1px solid #000 (buttonDarkMd.border)"),
            "control": dim(lengths(R("focusVisible.outline"))[0], "focus-visible outline width (focusVisible.outline); fields.css checkbox and radio borders are 2px too"),
        },
        "size": {
            "icon-sm": dim(R("iconButtonSm.height"), "button-icon-sm computed 28px (iconButtonSm)"),
            "icon-md": hand(dim("40px", "buttons.css .button-icon-md 2.5rem. Not seen painted on the measured pages."), "buttons.css"),
            "control-sm": dim(R("buttonSm.height"), "button-sm computed height (buttonSm); field-sm is the same 40px"),
            "control-compact": dim(R("buttonCompact.height"), "button-compact computed height (buttonCompact)"),
            "control-md": dim(R("buttonLightMd.height"), "button-md computed height (buttonLightMd); field-md is the same 48px"),
            "swatch": dim(R("colorSwatch.height"), "product colour link computed size (colorSwatch)"),
            "close": dim(R("klaviyoModal.closeSize"), "Klaviyo close button computed size (klaviyoModal.closeSize)"),
            "logo-height": dim(R("logo.desktop.height"), "header wordmark svg computed height at 1440 and 390 (logo)"),
            "announcement": dim(R("announcement.height"), "announcement bar computed height (announcement)"),
            "nav-item": dim(R("navLink.height"), "desktop nav link computed height (navLink)"),
            "checkbox": hand(dim("24px", "fields.css .field-checkbox 1.5rem"), "fields.css"),
        },
        "layout": {
            "max-width": dim(R("rootVars.universalMaxWidth"), "app.css --universalMaxWidth (rootVars.universalMaxWidth)"),
            "container-height": dim(R("rootVars.desktopContainerHeight"), "app.css --desktopContainerHeight (rootVars.desktopContainerHeight)"),
            "breakpoint-480": dim("480px", "the min-width that raises --grid-gutter (rootVars.gridGutter480)", D),
            "breakpoint-768": dim("768px", "the min-width that raises --frame-width (rootVars.frameWidth768)", D),
            "breakpoint-1024": dim("1024px", "the min-width that raises --text-card-edge (rootVars.textCardEdge1024)", D),
            "breakpoint-1200": dim("1200px", "the min-width that raises --grid-edge (rootVars.gridEdge1200)", D),
            "content-desktop": dim("%dpx" % RAW["viewportDesktop"]["innerWidth"], "measured innerWidth of the desktop capture"),
            "content-phone": dim("%dpx" % RAW["viewportPhone"]["innerWidth"], "measured innerWidth of the phone capture"),
        },
        "shadow": {
            "card": hand(shadow(
                {
                    "color": "#0000000f",
                    "offsetX": "0px",
                    "offsetY": "1px",
                    "blur": "1px",
                    "spread": "-0.5px",
                },
                "first elevation step of .surface-card, surfaces.css, rgba(0,0,0,.06)",
            ), "surfaces.css"),
            "field-ring": shadow(
                {
                    "color": hexes(R("fieldMd.boxShadow"))[0],
                    **dict(zip(("offsetX", "offsetY", "blur", "spread"), shadow_lengths(R("fieldMd.boxShadow")))),
                    "inset": "inset" in R("fieldMd.boxShadow"),
                },
                ".field inset ring, computed on the search field (fieldMd.boxShadow)",
            ),
        },
        "motion": {
            "duration": {
                "press": hand(duration("150ms", "buttons.css .button-dark transition .15s"), "buttons.css"),
                "light-press": hand(duration("200ms", "buttons.css .button-light transition .2s"), "buttons.css"),
                "underline": hand(duration("500ms", "links.css .link-underline:after transition width .5s ease"), "links.css"),
            },
            "easing": {
                "ease": hand({
                    "$type": "cubicBezier",
                    "$value": [0.25, 0.1, 0.25, 1],
                    "$extensions": {
                        "source": "links.css transition width .5s ease. Keyword expanded.",
                        "evidence": D,
                    },
                }, "links.css"),
                "drawer": hand({
                    "$type": "cubicBezier",
                    "$value": [0.165, 0.84, 0.44, 1],
                    "$extensions": {
                        "source": "css-bundle.css transition transform .3s cubic-bezier(.165,.84,.44,1)",
                        "evidence": M,
                    },
                }, "css-bundle.css"),
            },
        },
    }
    light = {
        "background": {
            "page": color("{core.color.page}", "body background"),
            "surface": color("{core.color.white}", ".surface-card and .field background"),
            "raised": color("{core.color.white}", ".surface-popover background #fff"),
            "overlay": color("{core.color.white}", "Klaviyo form background rgb(255, 255, 255)"),
            "scrim": color("{core.color.scrim}", "phone menu overlay rgba(0, 0, 0, 0.6)"),
            "announcement": color("{core.color.black}", "announcement text sits on a black fade; the bar itself is a gradient to rgba(0,0,0,.6)"),
            "inverse": color("{core.color.charcoal}", "button-dark face rgb(47, 47, 47)"),
        },
        "text": {
            "primary": color("{core.color.black}", "body color"),
            "secondary": hand(color("{core.color.muted}", "fields.css placeholder #6b6b6b"), "fields.css"),
            "disabled": hand(color("{core.color.white}", "disabled buttons paint #fff on #adadad, buttons.css"), "buttons.css"),
            "on-accent": color("{core.color.white}", ".type-pill and button-dark color rgb(255, 255, 255)"),
            "link": color("{core.color.black}", "a{color:inherit} in app.css; nav links computed rgb(0, 0, 0)"),
            "inverse": color("{core.color.white}", "hero h1 and announcement computed rgb(255, 255, 255)"),
        },
        "border": {
            "default": color(hexes(R("fieldMd.boxShadow"))[0], "field inset ring (fieldMd.boxShadow)"),
            "strong": color("{core.color.black}", "button-dark border #000"),
            "focus": color("{core.color.black}", "focus-visible outline 2px solid #000"),
            "error": hand(color("{core.color.danger}", "fields.css .field-error #e3163b"), "fields.css"),
        },
        "accent": {
            "default": color("{core.color.black}", "primary action is the black button-dark face, not a brand hue"),
            "hover": hand(color("{core.color.charcoal}", "button-dark has no :hover rule; the face stays #2f2f2f. Hover was not forced"), "buttons.css"),
            "pressed": hand(color("{core.color.inset}", "button-dark:active inset shadow uses #0e0e0e. Pressed state was not held."), "buttons.css"),
            "info": color("{core.color.info}", "NEW pill rgb(0, 91, 211)"),
            "sale": color("{core.color.sale}", "Black Friday and HOT pill rgb(203, 121, 76)"),
        },
        "status": {
            "warning": color("{core.color.sale}", "no warning colour was read; the sale pill is the only warm colour measured and stands in", X),
            "danger": hand(color("{core.color.danger}", "fields.css error colour, not seen painted"), "fields.css"),
            "info": color("{core.color.info}", "NEW pill"),
        },
        "component": {
            "button-primary": {
                "background": color("{core.color.charcoal}", "button-dark computed gradient"),
                "text": color("{core.color.white}", "button-dark color"),
                "radius": dim("{core.radius.pill}", "button-md computed 100px"),
                "height": dim("{core.size.control-md}", "button-md computed 48px"),
                "padding": dim(lengths(R("buttonDarkMd.padding"))[1], "button-md computed padding-inline (buttonDarkMd.padding)"),
            },
            "button-secondary": {
                "background": color("{core.color.white}", "button-light gradient starts rgb(255, 255, 255)"),
                "text": color("{core.color.black}", "Shop Now computed color"),
                "radius": dim("{core.radius.pill}", "button-light computed 100px"),
                "height": dim("{core.size.control-md}", "Shop Now computed 48px"),
            },
            "field": {
                "background": color("{core.color.white}", "input.field computed background"),
                "text": color("{core.color.black}", "input.field computed color"),
                "radius": dim("{core.radius.pill}", "field-md computed 100px"),
                "height": dim("{core.size.control-md}", "field-md computed 48px"),
            },
            "card": {
                "background": color("{core.color.white}", ".surface-card computed background"),
                "radius": dim("{core.radius.card}", ".surface-card computed 25px"),
            },
            "badge": {
                "background": color("{core.color.info}", "NEW pill computed background"),
                "text": color("{core.color.white}", "NEW pill computed color"),
                "radius": dim("{core.radius.pill}", "pill computed 100px"),
            },
        },
    }
    doc = {
        "$schema": "https://www.designtokens.org/schemas/2025.10/format.json",
        "core": core,
        "light": light,
        "$themes": [{"name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
        "$extensions": {
            "nomad": {
                "captured": RAW["captured"],
                "pages": RAW["pages"],
                "dark": "Not captured. Public pages had no theme switch and color-scheme was normal.",
                "screenshots": "Not captured. Preview snapshot failed: The browser is not producing screenshot frames.",
            },
            "notTokenised": [
                "No success colour was on the measured pages, so there is no light.status.success token.",
            ],
        },
    }
    check(doc)
    return doc


def check(doc):
    """Refuse a token with no source or evidence, an alias that resolves to nothing, and a duration or
    dimension that is not one length of the right unit. Raises SystemExit, so it also runs under -O."""
    flat = {}

    def walk(node, path):
        if isinstance(node, dict) and "$value" in node:
            flat[path] = node
        elif isinstance(node, dict):
            for k, v in node.items():
                if not k.startswith("$"):
                    walk(v, f"{path}.{k}" if path else k)

    walk({k: doc[k] for k in ("core", "light")}, "")
    for path, t in flat.items():
        ext = t.get("$extensions", {})
        if not ext.get("source") or ext.get("evidence") not in (M, D, X):
            raise SystemExit(f"{path}: no source or evidence")
        values = t["$value"].values() if isinstance(t["$value"], dict) else [t["$value"]]
        for v in values:
            for ref in re.findall(r"\{([^{}]+)\}", v) if isinstance(v, str) else []:
                if ref not in flat:
                    raise SystemExit(f"{path}: alias {{{ref}}} resolves to nothing")
        v = t["$value"]
        if isinstance(v, str) and "{" in v and t["$type"] in ("color", "dimension", "duration"):
            # an alias must be the whole value and point at a token of the same type
            m = re.fullmatch(r"\{([^{}]+)\}", v)
            if not m:
                raise SystemExit(f"{path}: {v!r} is not one whole alias")
            if flat[m.group(1)]["$type"] != t["$type"]:
                raise SystemExit(f"{path}: alias {v} points at a {flat[m.group(1)]['$type']}, not a {t['$type']}")
            v = flat[m.group(1)]["$value"]
        if t["$type"] == "duration" and not re.fullmatch(r"\d+(\.\d+)?(ms|s)", v):
            raise SystemExit(f"{path}: duration {v!r} is not a time")
        if t["$type"] == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?px", v):
            raise SystemExit(f"{path}: dimension {v!r} is not one px length")
    return len(flat)


def main():
    doc = build()
    out = ROOT / "tokens.json"
    out.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
