#!/usr/bin/env python3
"""Build tokens.json from systems/nomad-goods/raw/readings.json.

Values are the ones read on nomadgoods.com/sg on 2026-11-19: computed styles
on live elements, plus the class rules in the Shopify CSS files the page
linked. A rem in those files is recorded as the px the browser computed at
the default 16px root. Dark theme was not on the public pages.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RAW = json.loads((ROOT / "raw" / "readings.json").read_text())

M = "Measured"
D = "Derived"


def color(value, source):
    return {
        "$type": "color",
        "$value": value,
        "$extensions": {"source": source, "evidence": M},
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


def main():
    page = "getComputedStyle on https://nomadgoods.com/sg/ at 1440x900, 2026-11-19"
    css = "Shopify stylesheet linked by that page, confirmed by computed style"
    core = {
        "font": {
            "family": {
                "display": font(
                    "Gotham-Bold, sans-serif",
                    "computed font-family on h1.type-title-lg and .button-dark",
                ),
                "ui": font(
                    "Gotham-Book, sans-serif",
                    "computed font-family on input.field and input in app.css",
                ),
                "body": font(
                    "Aleo, HelveticaNeue, Helvetica Neue, sans-serif",
                    "computed font-family on body",
                ),
            }
        },
        "color": {
            "black": color("#000000", f"body color rgb(0, 0, 0); {page}"),
            "white": color("#ffffff", "button-light text and .field background rgb(255, 255, 255)"),
            "page": color("#f3f3f3", "body background-color rgb(243, 243, 243); app.css body{background-color:#f3f3f3}"),
            "ink-soft": color("#f1f1f1", "button-light gradient end rgb(241, 241, 241)"),
            "charcoal": color("#2f2f2f", "button-dark background-image rgb(47, 47, 47)"),
            "inset": color("#0e0e0e", "button-dark inset shadow rgb(14, 14, 14)"),
            "hairline": color("#676767", "button-dark inset ring rgb(103, 103, 103)"),
            "disabled": color("#adadad", "buttons.css .button-dark:disabled background #adadad"),
            "muted": color("#6b6b6b", "fields.css placeholder and .field-muted-text #6b6b6b"),
            "danger": color("#e3163b", "fields.css .field-error and .field-error-text #e3163b"),
            "info": color("#005bd3", "computed .type-pill NEW background rgb(0, 91, 211)"),
            "sale": color("#cb794c", "computed .type-pill Black Friday and HOT rgb(203, 121, 76)"),
            "link-blue": color("#007aff", "css-bundle.css uses #007aff five times; not seen on the measured controls"),
            "near-black": color("#050505", "Klaviyo Sign Up button background rgb(5, 5, 5)"),
            "scrim": color("#00000099", "phone menu scrim rgba(0, 0, 0, 0.6); Klaviyo scrim was rgba(0, 0, 0, 0.5)"),
        },
        "typography": {
            "display": typography(
                "{core.font.family.display}", "77px", "700", "0.95", "-0.04em",
                "h1.type-title-lg computed 77px / 73.15px / -3.08px at 1440; type.css desktop 4.8125rem, line-height .95, letter-spacing -.04em",
            ),
            "display-mobile": typography(
                "{core.font.family.display}", "47px", "700", "0.95", "-0.04em",
                "h1.type-title-lg computed 47px / 44.65px / -1.88px at 390; type.css base 2.9375rem",
            ),
            "title-section": typography(
                "{core.font.family.display}", "56px", "700", "0.95", "-0.04em",
                "h2.type-title-section computed 56px / 53.2px / -2.24px at 1440; type.css 3.5rem from 768px",
            ),
            "title-md": typography(
                "{core.font.family.display}", "50px", "700", "0.95", "-0.04em",
                "h2.type-title-md computed 50px / 47.5px / -2px on about at 1440; type.css 3.125rem from 768px",
            ),
            "page-title": typography(
                "{core.font.family.display}", "36px", "700", "1.11", "-0.04em",
                "product h1.type-page-title computed 36px / 39.96px / -1.44px; type.css 2.25rem, line-height 1.11",
            ),
            "heading-md": typography(
                "{core.font.family.display}", "24px", "700", "1.11", "-0.04em",
                "p.type-heading-md computed 24px / 26.64px / -0.96px on the collection page; type.css 1.5rem from 768px",
            ),
            "heading-sm": typography(
                "{core.font.family.display}", "16px", "700", "1.11", "-0.04em",
                "footer h3.type-heading-sm computed 16px / 17.76px / -0.64px",
            ),
            "price": typography(
                "{core.font.family.display}", "32px", "700", "1", "-0.04em",
                ".type-price computed 32px / 32px / -1.28px on the product page; type.css 2rem from 768px",
            ),
            "body-lg": typography(
                "{core.font.family.body}", "23px", "400", "1.5", "0em",
                "about paragraph computed 23px / 34.5px; type.css .type-body-lg 1.4375rem, line-height 1.5",
            ),
            "body": typography(
                "{core.font.family.body}", "16px", "400", "1.5", "0em",
                "body computed 16px / 24px; type.css .type-body-md",
            ),
            "body-sm": typography(
                "{core.font.family.body}", "14px", "400", "1.5", "0em",
                "type.css .type-body-sm 0.875rem; footer signup copy uses that class",
            ),
            "fine-print": typography(
                "{core.font.family.body}", "12px", "400", "1.5", "0em",
                "type.css .type-fine-print 0.75rem",
            ),
            "button-md": typography(
                "{core.font.family.display}", "16px", "700", "1.11", "-0.04em",
                "Shop Now computed 16px / 17.76px / -0.64px",
            ),
            "button-sm": typography(
                "{core.font.family.display}", "14px", "700", "1.11", "-0.04em",
                "announcement and footer Submit computed 14px / 15.54px / -0.56px",
            ),
            "field": typography(
                "{core.font.family.ui}", "16px", "400", "1.5", "-0.02em",
                "input.field computed 16px / 24px / -0.32px; type.css letter-spacing -.02em",
            ),
            "detail-sm": typography(
                "{core.font.family.ui}", "12px", "400", "1.25", "-0.02em",
                "collection caption computed 12px / 15px / -0.24px; type.css .type-detail-sm",
            ),
            "pill": typography(
                "{core.font.family.display}", "11px", "700", "1", "-0.04em",
                ".type-pill computed 11px / 11px / -0.44px, uppercase",
            ),
        },
        "space": {
            "2": dim("2px", "tab-bar padding in buttons.css"),
            "4": dim("4px", "drawer row padding 4px, computed"),
            "8": dim("8px", "frame-width at the root, app.css --frame-width:8px"),
            "10": dim("10px", ":root --grid-edge:10px, app.css"),
            "12": dim("12px", "--frame-width:12px from 768px, app.css"),
            "16": dim("16px", "field-sm padding 0 1rem, computed 16px"),
            "20": dim("20px", "button-sm horizontal padding, computed 20px; --grid-edge:20px from 1200px"),
            "24": dim("24px", "button-md horizontal padding, computed 24px"),
            "25": dim("25px", ":root --grid-gutter:25px and .surface-card radius 25px"),
            "30": dim("30px", "nav link padding 0 30px and product card padding-top 30px"),
            "40": dim("40px", "--grid-gutter:40px from 480px; product card padding-inline 40px"),
            "50": dim("50px", "footer border-top-width 50px, computed"),
            "70": dim("70px", "footer padding-block 70px, computed"),
            "100": dim("100px", "--text-card-edge:100px from 1024px, app.css"),
        },
        "radius": {
            "none": dim("0px", "body and announcement radius, computed"),
            "checkbox": dim("6px", "fields.css .field-checkbox border-radius:6px"),
            "tab-selected": dim("13px", "buttons.css .tab-bar-selected border-radius:13px"),
            "status": dim("15px", "labels.css .status-box border-radius:15px"),
            "tab-bar": dim("16px", "buttons.css .tab-bar border-radius:16px"),
            "popover": dim("20px", ".surface-popover computed 20px"),
            "textarea": dim("24px", "fields.css .field-textarea border-radius:24px"),
            "card": dim("25px", ".surface-card computed 25px"),
            "dialog": dim("40px", "Klaviyo form computed border-radius 40px"),
            "pill": dim("100px", "button-md and .field-md computed 100px"),
            "round": dim("1000px", "colour swatch computed border-radius 1000px"),
        },
        "border": {
            "none": dim("0px", "button-light border 0, buttons.css"),
            "hairline": dim("1px", "button-dark border 1px solid #000, computed"),
            "control": dim("2px", "fields.css checkbox and radio border 2px; focus outline 2px"),
        },
        "size": {
            "icon-sm": dim("28px", "button-icon-sm computed 28px; buttons.css 1.75rem"),
            "icon-md": dim("40px", "buttons.css .button-icon-md 2.5rem. Not seen painted on the measured pages."),
            "control-sm": dim("40px", "button-sm and field-sm computed 40px"),
            "control-compact": dim("44px", "button-compact computed 44px"),
            "control-md": dim("48px", "button-md and field-md computed 48px"),
            "swatch": dim("30px", "product colour link computed 30px"),
            "close": dim("35px", "Klaviyo close button computed 35px"),
            "logo-height": dim("25px", "header wordmark svg computed height 25px at 1440 and 390"),
            "announcement": dim("50px", "announcement bar computed height 50px"),
            "nav-item": dim("70px", "desktop nav link computed height 70px"),
            "checkbox": dim("24px", "fields.css .field-checkbox 1.5rem"),
        },
        "layout": {
            "max-width": dim("1600px", "app.css --universalMaxWidth:1600px"),
            "container-height": dim("700px", "app.css --desktopContainerHeight:700px"),
            "breakpoint-480": dim("480px", "app.css min-width 480px raises --grid-gutter"),
            "breakpoint-768": dim("768px", "type.css and app.css min-width 768px"),
            "breakpoint-1024": dim("1024px", "app.css min-width 1024px raises --text-card-edge"),
            "breakpoint-1200": dim("1200px", "app.css min-width 1200px raises --grid-edge"),
            "content-desktop": dim("1440px", "measured innerWidth of the desktop capture"),
            "content-phone": dim("390px", "measured innerWidth of the phone capture"),
        },
        "shadow": {
            "card": shadow(
                {
                    "color": "#0000000f",
                    "offsetX": "0px",
                    "offsetY": "1px",
                    "blur": "1px",
                    "spread": "-0.5px",
                },
                "first elevation step of .surface-card, surfaces.css, rgba(0,0,0,.06)",
            ),
            "field-ring": shadow(
                {
                    "color": "#0000001a",
                    "offsetX": "0px",
                    "offsetY": "0px",
                    "blur": "0px",
                    "spread": "1px",
                    "inset": True,
                },
                "fields.css .field inset ring rgba(0,0,0,.1), computed on the search field",
            ),
        },
        "motion": {
            "duration": {
                "press": dim("150ms", "buttons.css .button-dark transition .15s", D),
                "light-press": dim("200ms", "buttons.css .button-light transition .2s", D),
                "underline": dim("500ms", "links.css .link-underline:after transition width .5s ease", D),
            },
            "easing": {
                "ease": {
                    "$type": "cubicBezier",
                    "$value": [0.25, 0.1, 0.25, 1],
                    "$extensions": {
                        "source": "links.css transition width .5s ease. Keyword expanded.",
                        "evidence": D,
                    },
                },
                "drawer": {
                    "$type": "cubicBezier",
                    "$value": [0.165, 0.84, 0.44, 1],
                    "$extensions": {
                        "source": "css-bundle.css transition transform .3s cubic-bezier(.165,.84,.44,1)",
                        "evidence": M,
                    },
                },
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
            "secondary": color("{core.color.muted}", "fields.css placeholder #6b6b6b"),
            "disabled": color("{core.color.white}", "disabled buttons paint #fff on #adadad, buttons.css"),
            "on-accent": color("{core.color.white}", ".type-pill and button-dark color rgb(255, 255, 255)"),
            "link": color("{core.color.black}", "a{color:inherit} in app.css; nav links computed rgb(0, 0, 0)"),
            "inverse": color("{core.color.white}", "hero h1 and announcement computed rgb(255, 255, 255)"),
        },
        "border": {
            "default": color("#0000001a", "field inset ring #0000001a"),
            "strong": color("{core.color.black}", "button-dark border #000"),
            "focus": color("{core.color.black}", "focus-visible outline 2px solid #000"),
            "error": color("{core.color.danger}", "fields.css .field-error #e3163b"),
        },
        "accent": {
            "default": color("{core.color.black}", "primary action is the black button-dark face, not a brand hue"),
            "hover": color("{core.color.charcoal}", "button-dark has no :hover rule; the face stays #2f2f2f"),
            "pressed": color("{core.color.inset}", "button-dark:active inset shadow uses #0e0e0e. Pressed state was not held."),
            "info": color("{core.color.info}", "NEW pill rgb(0, 91, 211)"),
            "sale": color("{core.color.sale}", "Black Friday and HOT pill rgb(203, 121, 76)"),
        },
        "status": {
            "success": color("{core.color.black}", "no success colour was on the measured pages"),
            "warning": color("{core.color.sale}", "sale pill is the only warm status colour measured"),
            "danger": color("{core.color.danger}", "fields.css error colour, not seen painted"),
            "info": color("{core.color.info}", "NEW pill"),
        },
        "component": {
            "button-primary": {
                "background": color("{core.color.charcoal}", "button-dark computed gradient"),
                "text": color("{core.color.white}", "button-dark color"),
                "radius": dim("{core.radius.pill}", "button-md computed 100px"),
                "height": dim("{core.size.control-md}", "button-md computed 48px"),
                "padding": dim("24px", "button-md computed padding-inline 24px"),
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
            }
        },
    }
    out = ROOT / "tokens.json"
    out.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
