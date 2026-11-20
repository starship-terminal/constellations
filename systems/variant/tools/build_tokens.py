#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/components-computed.json.

Variant's signed-out surfaces were read live on 2026-11-19. This script does
not invent values: every colour, length and font string is copied from those
two files. A role that was not painted is listed under $extensions.notTokenised.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())["declared"]
COMP = json.loads((RAW / "components-computed.json").read_text())

SRC_VAR = "raw/css-vars.json declared custom property, variant.com 2026-11-19"
SRC_HOME = "raw/components-computed.json home, getComputedStyle, variant.com 2026-11-19"
SRC_AUTH = "raw/components-computed.json authentication, getComputedStyle, variant.com/authentication 2026-11-19"
SRC_TERMS = "raw/components-computed.json terms, getComputedStyle, variant.com/terms-and-privacy 2026-11-19"
SRC_MOTION = "raw/components-computed.json motion, computed style or authored rule, 2026-11-19"


def color(value: str, source: str) -> dict:
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value: str, source: str) -> dict:
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font(value: str, source: str) -> dict:
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def text_style(family: str, size: str, weight: str, line: str, tracking: str, source: str) -> dict:
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
            "letterSpacing": tracking,
        },
        "$extensions": {"source": source},
    }


def shadow(value: str, source: str) -> dict:
    return {"$type": "shadow", "$value": value, "$extensions": {"source": source}}


def bezier_points(value: str) -> list:
    """"0.25, 0.1, 0.25, 1" as the four numbers DTCG's cubicBezier holds. A string would
    export as a bare number list, which is not a CSS easing."""
    points = [float(p) for p in value.split(",")]
    assert len(points) == 4, value
    return [int(p) if p.is_integer() else p for p in points]


def cubic(value: str, source: str) -> dict:
    return {"$type": "cubicBezier", "$value": bezier_points(value), "$extensions": {"source": source}}


def duration(value: str, source: str) -> dict:
    return {"$type": "duration", "$value": value, "$extensions": {"source": source}}


def number(value: str, source: str) -> dict:
    return {"$type": "number", "$value": value, "$extensions": {"source": source}}


def other(value: str, source: str) -> dict:
    return {"$value": value, "$extensions": {"source": source}}


def build() -> dict:
    """The token document; nothing is written (main() writes it)."""
    home = COMP["home"]
    auth = COMP["authentication"]
    terms = COMP["terms"]
    motion = COMP["motion"]

    core = {
        "font": {
            "family": {
                "display": font(
                    "Variant Neue Display, Variant Neue Text, Inter, Inter Fallback, system-ui, sans-serif",
                    SRC_HOME + " h1 fontFamily",
                ),
                "text": font(
                    "Variant Neue Text, Inter, Inter Fallback, system-ui, sans-serif",
                    SRC_HOME + " subtitle fontFamily",
                ),
                "inter": font(
                    "Inter, Inter Fallback, system-ui, sans-serif",
                    SRC_HOME + " body fontFamily",
                ),
                "mono": font(VARS["--font-mono"], SRC_VAR + " --font-mono"),
                "advercase": font(VARS["--font-advercase"], SRC_VAR + " --font-advercase (declared, not used on signed-out surfaces)"),
            }
        },
        "typography": {
            "display": text_style(
                "{font.family.display}", "32px", "400", "36px", "0.32px",
                SRC_HOME + " h1",
            ),
            "subtitle": text_style(
                "{font.family.text}", "14px", "400", "24px", "0.28px",
                SRC_HOME + " subtitlePrimary",
            ),
            "composer": text_style(
                "{font.family.text}", "14px", "400", "22px", "0.28px",
                SRC_HOME + " editor",
            ),
            "chip": text_style(
                "{font.family.text}", "11px", "400", "11px", "0.22px",
                SRC_HOME + " suggestionButton",
            ),
            "auth-title": text_style(
                "{font.family.inter}", "21px", "500", "32px", "-0.21px",
                SRC_AUTH + " title",
            ),
            "control-size": dim("13px", SRC_AUTH + " googleButton and emailInput fontSize"),
            "control-weight": other("400", SRC_AUTH + " googleButton fontWeight"),
            "control-tracking": dim("0.13px", SRC_AUTH + " googleButton letterSpacing"),
            "legal-title": text_style(
                "{font.family.inter}", "21px", "500", "32px", "-0.21px",
                SRC_TERMS + " h1",
            ),
            "legal-body": text_style(
                "{font.family.inter}", "13px", "400", "20px", "0.13px",
                SRC_TERMS + " body",
            ),
            "legal-heading": text_style(
                "{font.family.inter}", "13px", "500", "20px", "0.13px",
                SRC_TERMS + " h2",
            ),
            "fine-print": text_style(
                "{font.family.inter}", "12px", "400", "20px", "0.12px",
                SRC_AUTH + " terms",
            ),
        },
        "radius": {
            "chip": dim("6px", SRC_HOME + " suggestionButton borderRadius"),
            "control": dim("6px", SRC_AUTH + " emailInput and buttons borderRadius"),
            "card": dim("8px", SRC_HOME + " grid cardRadius"),
            "composer": dim("10px", SRC_HOME + " composer borderRadius"),
            "token": dim(VARS["--border-radius"], SRC_VAR + " --border-radius (resolved 12px on homepage root; signed-out controls measured 6, 8 and 10)"),
        },
        "space": {
            "chip-pad-y": dim("0px", SRC_HOME + " suggestionButton padding top"),
            "chip-pad-end": dim("8px", SRC_HOME + " suggestionButton padding"),
            "chip-pad-start": dim("7px", SRC_HOME + " suggestionButton padding and --action-padding-expanded"),
            "chip-gap": dim("7px", SRC_HOME + " suggestionButton gap; matches --action-gap-expanded"),
            "control-height": dim("40px", SRC_AUTH + " button and input height"),
            "icon-button": dim("24px", SRC_HOME + " iconButton width and height"),
            "chip-height": dim("26px", SRC_HOME + " suggestionButton height"),
            "column": dim("408px", SRC_HOME + " left width at 1440"),
            "auth-control": dim("400px", SRC_AUTH + " button and input width"),
            "auth-card": dim("520px", SRC_AUTH + " card maxWidth"),
            "legal": dim("920px", SRC_TERMS + " articleWidth"),
            "page-max": dim(VARS["--max-width"], SRC_VAR + " --max-width"),
            "hero-inset": dim("24px", SRC_HOME + " h1 x offset"),
        },
        "border": {
            "hairline": dim("0.5px", SRC_HOME + " suggestionButton and composer ring"),
        },
        "motion": {
            "card-fade": duration("500ms", SRC_MOTION + " widget card transition opacity 0.5s"),
            "card-delay": duration("300ms", SRC_MOTION + " widget card transition delay 0.3s"),
            "ease": cubic("0.25, 0.1, 0.25, 1", SRC_MOTION + " keyword ease on the widget card, expanded to the CSS ease control points"),
            "shimmer": duration(VARS["--widget-entry-shimmer-duration"], SRC_VAR + " --widget-entry-shimmer-duration"),
            "shimmer-ease": cubic("0, 0, 0.2, 1", SRC_VAR + " --widget-entry-shimmer-ease"),
            "load": duration("582ms", SRC_VAR + " --widget-load-duration 581.71ms, rounded to a whole millisecond"),
            "chip": duration("200ms", SRC_MOTION + " authored .input-container__style-chip transition 0.2s"),
            "shared": duration("300ms", SRC_MOTION + " authored .shared_container transition 0.3s"),
            "shared-ease": cubic("0.19, 1, 0.22, 1", SRC_MOTION + " authored .shared_container cubic-bezier"),
            "hover-indicator": duration("100ms", SRC_MOTION + " authored sidebar and menu hover indicator 0.1s"),
            "hover-ease": cubic("0.175, 0.885, 0.32, 1", SRC_MOTION + " authored hover indicator cubic-bezier"),
        },
        "palette": {
            "gray-dark": color(VARS["--color-gray-dark"], SRC_VAR + " --color-gray-dark"),
            "gray-light": color(VARS["--color-gray-light"], SRC_VAR + " --color-gray-light"),
            "gray-lighter": color(VARS["--color-gray-lighter"], SRC_VAR + " --color-gray-lighter"),
            "gray-medium": color(VARS["--color-gray-medium"], SRC_VAR + " --color-gray-medium"),
            "offwhite": color(VARS["--homepage-offwhite"], SRC_VAR + " --homepage-offwhite"),
            "primary-blue": color(VARS["--color-primary-blue"], SRC_VAR + " --color-primary-blue"),
            "secondary-blue": color(VARS["--color-secondary-blue"], SRC_VAR + " --color-secondary-blue"),
            "tertiary-blue": color(VARS["--color-tertiary-blue"], SRC_VAR + " --color-tertiary-blue"),
            "brand-blue": color(VARS["--color-brand-blue"], SRC_VAR + " --color-brand-blue"),
            "accent-blue": color(VARS["--color-accent-blue"], SRC_VAR + " --color-accent-blue"),
            "accent-coral": color(VARS["--color-accent-coral"], SRC_VAR + " --color-accent-coral"),
            "accent-purple": color(VARS["--color-accent-purple"], SRC_VAR + " --color-accent-purple"),
            "warning-red": color(VARS["--color-warning-red"], SRC_VAR + " --color-warning-red"),
            "white-03": color(VARS["--color-white-03"], SRC_VAR + " --color-white-03"),
            "white-05": color(VARS["--color-white-05"], SRC_VAR + " --color-white-05"),
            "white-10": color(VARS["--color-white-10"], SRC_VAR + " --color-white-10"),
            "white-15": color(VARS["--color-white-15"], SRC_VAR + " --color-white-15"),
            "white-50": color(VARS["--color-white-50"], SRC_VAR + " --color-white-50"),
            "white-85": color(VARS["--color-white-85"], SRC_VAR + " --color-white-85"),
        },
    }

    # The product paints one dark surface on every signed-out page. The set is
    # named dark because that is what was on screen. There is no light set.
    dark = {
        "page": color(home["body"]["backgroundColor"], SRC_HOME + " body backgroundColor"),
        "column": color(home["left"]["backgroundColor"], SRC_HOME + " left and right column backgroundColor"),
        "auth-page": color(auth["page"]["backgroundColor"], SRC_AUTH + " page backgroundColor"),
        "composer": color(home["composer"]["backgroundColor"], SRC_HOME + " composer backgroundColor"),
        "text": color(home["h1"]["color"], SRC_HOME + " h1 color, matches --homepage-offwhite"),
        "muted": color(home["subtitlePrimary"]["color"], SRC_HOME + " subtitle color"),
        "text-soft": color(home["editor"]["color"], SRC_HOME + " editor color"),
        "placeholder": color(home["placeholder"]["color"], SRC_HOME + " placeholder color"),
        "icon": color(home["iconButton"]["color"], SRC_HOME + " icon button color"),
        "border": color("rgba(255, 255, 255, 0.1)", SRC_HOME + " suggestionButton border and composer box-shadow colour"),
        "composer-ring": shadow(home["composer"]["boxShadow"], SRC_HOME + " composer boxShadow"),
        "control-fill": color(auth["googleButton"]["backgroundColor"], SRC_AUTH + " Google button and email button background"),
        "control-fill-hover": color(auth["emailButton"]["filled"]["hover"]["backgroundColor"], SRC_AUTH + " enabled email button hover"),
        "control-text": color(auth["googleButton"]["color"], SRC_AUTH + " Google button color"),
        "control-text-disabled": color(auth["emailButton"]["empty"]["color"], SRC_AUTH + " empty email button color"),
        "field": color(auth["emailInput"]["backgroundColor"], SRC_AUTH + " email input background"),
        "field-border": color("rgba(255, 255, 255, 0.1)", SRC_AUTH + " email input border colour"),
        "divider": color(auth["divider"]["color"], SRC_AUTH + " divider label color"),
        "legal-title": color(terms["h1"]["color"], SRC_TERMS + " h1 color"),
        "legal-body": color(terms["body"]["color"], SRC_TERMS + " article color"),
        "tab-inactive": color(terms["tab"]["inactiveColor"], SRC_TERMS + " inactive tab color"),
        "focus-ring": color(
            auth["emailButton"]["focusVisible"]["outline"].split(" auto ")[0],
            SRC_AUTH + " user-agent focus outline on buttons and links. Not a product custom property.",
        ),
        "component": {
            "chip": {
                "bg": color("{column}", SRC_HOME + " suggestionButton background, same as the column"),
                "text": color("{text}", SRC_HOME + " suggestionButton color"),
                "radius": dim("{radius.chip}", SRC_HOME + " suggestionButton"),
                "height": dim("{space.chip-height}", SRC_HOME + " suggestionButton"),
            },
            "button": {
                "bg": color("{control-fill}", SRC_AUTH + " primary and Google buttons"),
                "text": color("{control-text}", SRC_AUTH + " enabled button text"),
                "radius": dim("{radius.control}", SRC_AUTH + " button radius"),
                "height": dim("{space.control-height}", SRC_AUTH + " button height"),
            },
            "field": {
                "bg": color("{field}", SRC_AUTH + " email input"),
                "text": color("{control-text}", SRC_AUTH + " input color"),
                "radius": dim("{radius.control}", SRC_AUTH + " input radius"),
                "height": dim("{space.control-height}", SRC_AUTH + " input height"),
            },
            "composer": {
                "bg": color("{composer}", SRC_HOME + " composer"),
                "radius": dim("{radius.composer}", SRC_HOME + " composer"),
            },
            "card": {
                "radius": dim("{radius.card}", SRC_HOME + " widget card"),
            },
        },
    }

    doc = {
        "core": core,
        "dark": dark,
        "$themes": [
            {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}}
        ],
        "$extensions": {
            "notTokenised": [
                "No light theme. prefers-color-scheme: light left body at rgb(34, 34, 34).",
                "Pressed state of Continue with Email: a click would submit the form.",
                "Homepage Submit, Add image and Select style hover and pressed: not opened.",
                "Signed-in sidebar, chat, billing modal, style modal and toasts: CSS is in the bundle, screens were not opened.",
                "Keyword colours red, blue, green, yellow (--color-error-red and siblings): declared, not painted on a signed-out element.",
                "Sonner toast layout variables and billing past-due colours: declared, not on screen.",
                "--widget-load-ease is a linear() spring and is not a cubicBezier token.",
                "Screenshots: preview_snapshot failed with 'The browser is not producing screenshot frames'. None were invented.",
            ],
            "source": "Built by tools/build_tokens.py from raw/css-vars.json and raw/components-computed.json.",
        },
    }
    return doc


def render() -> str:
    """tokens.json's exact text."""
    return json.dumps(build(), indent=2) + "\n"


def main() -> None:
    out = HERE / "tokens.json"
    out.write_text(render())
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
