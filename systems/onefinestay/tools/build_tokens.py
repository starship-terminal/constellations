#!/usr/bin/env python3
"""Build tokens.json from the Onefinestay readings in raw/.

Values were read on 2026-11-19 from the public marketing site in the T3 preview
browser. Custom properties come from raw/css-vars.json. Painted controls come
from raw/components-computed.json. There is no dark theme on the pages reached.

Every token carries $extensions.source. Deterministic: same inputs, same bytes.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components-computed.json").read_text())
RES = VARS["resolved"]
EL = COMP["elements"]

SRC = "www.onefinestay.com, resolved on :root, 2026-11-19, T3 preview, inner 1440x900"
SRC_EL = "www.onefinestay.com, computed style, 2026-11-19, T3 preview, inner 1440x900"


def tok(value, typ, source, **ext):
    out = {"$value": value, "$type": typ, "$extensions": {"source": source}}
    out["$extensions"].update(ext)
    return out


def color(name):
    return tok(RES[name], "color", f"{SRC}; {name}")


def dim_px(value, source):
    return tok(value, "dimension", source)


def build():
    """The token document, built in memory from raw/; main() writes it."""
    # Silence unused binding if a future reader expects COMP keys to be walked.
    assert EL["searchButton"]["background"] == "rgb(255, 128, 101)"
    return {
    "$schema": "https://www.w3.org/TR/design-tokens/",
    "core": {
        "font": {
            "family": {
                "display": tok(
                    "tiempos, tiempos Fallback, serif",
                    "fontFamily",
                    SRC_EL + "; home h1 computed font-family. Klim Tiempos Text, proprietary, not committed",
                ),
                "ui": tok(
                    "akkurat, akkurat Fallback, serif",
                    "fontFamily",
                    SRC_EL + "; body and nav computed font-family. Lineto Akkurat, proprietary, not committed",
                ),
            }
        },
        "fontWeight": {
            "regular": tok(400, "fontWeight", SRC + "; --font-weight-normal"),
            "medium": tok(500, "fontWeight", SRC + "; --font-weight-medium. Declared. Headings on the captured pages computed to 400"),
            "bold": tok(700, "fontWeight", SRC + "; --font-weight-bold"),
        },
        "typography": {
            "display": tok(
                {
                    "fontFamily": "{core.font.family.display}",
                    "fontSize": "64px",
                    "fontWeight": "{core.fontWeight.regular}",
                    "lineHeight": "72px",
                    "letterSpacing": "0px",
                },
                "typography",
                SRC_EL + "; home hero h2 at innerWidth 1440",
            ),
            "heading": tok(
                {
                    "fontFamily": "{core.font.family.display}",
                    "fontSize": "40px",
                    "fontWeight": "{core.fontWeight.regular}",
                    "lineHeight": "48px",
                    "letterSpacing": "0px",
                },
                "typography",
                SRC_EL + "; home h1 at innerWidth 1440",
            ),
            "heading-phone": tok(
                {
                    "fontFamily": "{core.font.family.display}",
                    "fontSize": "32px",
                    "fontWeight": "{core.fontWeight.regular}",
                    "lineHeight": "40px",
                    "letterSpacing": "0px",
                },
                "typography",
                "www.onefinestay.com home h1, computed style, 2026-11-19, T3 preview, inner 390x844",
            ),
            "card-title": tok(
                {
                    "fontFamily": "{core.font.family.display}",
                    "fontSize": "20px",
                    "fontWeight": "{core.fontWeight.regular}",
                    "lineHeight": "28px",
                    "letterSpacing": "0px",
                },
                "typography",
                SRC_EL + "; home listing card title, italic",
            ),
            "body": tok(
                {
                    "fontFamily": "{core.font.family.ui}",
                    "fontSize": "16px",
                    "fontWeight": "{core.fontWeight.regular}",
                    "lineHeight": "24px",
                    "letterSpacing": "0px",
                },
                "typography",
                SRC_EL + "; home paragraph",
            ),
            "nav": tok(
                {
                    "fontFamily": "{core.font.family.ui}",
                    "fontSize": "14px",
                    "fontWeight": "{core.fontWeight.regular}",
                    "lineHeight": "20px",
                    "letterSpacing": "0px",
                },
                "typography",
                SRC_EL + "; header Destinations link",
            ),
            "label": tok(
                {
                    "fontFamily": "{core.font.family.ui}",
                    "fontSize": "12px",
                    "fontWeight": "{core.fontWeight.bold}",
                    "lineHeight": "16px",
                    "letterSpacing": "0px",
                },
                "typography",
                SRC_EL + "; enquire field label FIRST NAME",
            ),
            "eyebrow": tok(
                {
                    "fontFamily": "{core.font.family.ui}",
                    "fontSize": "14px",
                    "fontWeight": "{core.fontWeight.bold}",
                    "lineHeight": "24px",
                    "letterSpacing": "0.35px",
                },
                "typography",
                SRC_EL + "; destination/london eyebrow, uppercase",
            ),
        },
        "radius": {
            "none": dim_px("0px", SRC_EL + "; search button border-radius"),
            "xs": dim_px("2px", SRC_EL + "; search bar, buttons and field shells computed border-radius 2px. --radius-xs declared 0.125rem, which is the same 2px"),
            "sm": dim_px("6px", SRC + "; --radius-sm is calc(0.625rem - 4px) = 6px. Not seen on a painted control this pass"),
            "md": dim_px("8px", SRC_EL + "; enquire input computed border-radius 8px from rounded-md. The painted shell around it is 2px"),
            "control": dim_px("10px", SRC + "; --radius 0.625rem. Declared. The painted buttons used 2px"),
            "chip": dim_px("24px", SRC_EL + "; search filter chip rounded-3xl computed 24px"),
            "3xl": dim_px("24px", SRC + "; --radius-3xl 1.5rem"),
        },
        "spacing": {
            "1": dim_px("4px", SRC + "; --spacing 0.25rem"),
            "2": dim_px("8px", SRC_EL + "; search bar padding and filter chip vertical padding"),
            "3": dim_px("12px", SRC_EL + "; field shell padding-block and inquire frame padding-inline"),
            "4": dim_px("16px", SRC_EL + "; button padding-inline and field shell padding-inline"),
            "6": dim_px("24px", SRC_EL + "; phone header padding-inline, and home paragraph padding-top"),
            "12": dim_px("48px", SRC_EL + "; desktop header padding-inline"),
            "16": dim_px("64px", SRC_EL + "; footer padding-block"),
            "header": dim_px("80px", SRC + "; --header-height 5rem, header computed height 80px"),
            "narrow": dim_px("890px", SRC + "; --container-narrow"),
        },
        "motion": {
            "duration": {
                "default": tok("200ms", "duration", SRC + "; --default-transition-duration 0.2s, also the computed link transition"),
            },
            "easing": {
                "standard": tok(
                    [0.4, 0, 0.2, 1],
                    "cubicBezier",
                    SRC + "; --default-transition-timing-function",
                ),
                "out": tok([0, 0, 0.2, 1], "cubicBezier", SRC + "; --ease-out"),
            },
        },
    },
    "light": {
        "surface": {
            "page": color("--background"),
            "card": color("--card"),
            "beige": color("--beige"),
            "board": color("--board-bg"),
            "footer": color("--neutral-700"),
            "header-solid": tok("#ffffff", "color", SRC_EL + "; listing header computed background"),
        },
        "text": {
            "primary": color("--neutral-900"),
            "ink": color("--foreground"),
            "muted": color("--neutral-600"),
            "placeholder": color("--neutral-400"),
            "on-footer": tok("#ffffff", "color", SRC_EL + "; footer social link computed color"),
            "on-hero": tok("#ffffff", "color", SRC_EL + "; home hero h2 computed color"),
        },
        "accent": color("--brand-500"),
        "brand": {
            "100": color("--brand-100"),
            "400": color("--brand-400"),
            "500": color("--brand-500"),
            "600": color("--brand-600"),
            "700": color("--brand-700"),
            "900": color("--brand-900"),
        },
        "neutral": {
            "100": color("--neutral-100"),
            "200": color("--neutral-200"),
            "300": color("--neutral-300"),
            "400": color("--neutral-400"),
            "500": color("--neutral-500"),
            "550": color("--neutral-550"),
            "600": color("--neutral-600"),
            "700": color("--neutral-700"),
            "800": color("--neutral-800"),
            "900": color("--neutral-900"),
        },
        "status": {
            "green-200": color("--green-200"),
            "green-500": color("--green-500"),
            "green-800": color("--green-800"),
            "red-500": color("--red-500"),
            "red-700": color("--red-700"),
            "destructive": color("--destructive"),
            "blue-500": color("--blue-500"),
        },
        "border": {
            "subtle": color("--border"),
            "field": color("--neutral-300"),
            "on-hero": tok("#ffffff", "color", SRC_EL + "; Inquire Now frame border"),
        },
        "focus": tok("#0066cc", "color", SRC_EL + "; Garden filter chip focus box-shadow, matches --blue-500"),
        "shadow": {
            "search": tok(
                {
                    "color": "rgba(0, 0, 0, 0.05)",
                    "offsetX": "0px",
                    "offsetY": "6px",
                    "blur": "24px",
                    "spread": "0px",
                },
                "shadow",
                SRC_EL + "; home search bar computed box-shadow",
            )
        },
        "component": {
            "button-primary": {
                "bg": color("--neutral-900"),
                "text": tok("#ffffff", "color", SRC_EL + "; enquire Submit computed color"),
                "radius": dim_px("2px", SRC_EL + "; enquire Submit computed border-radius"),
                "height": dim_px("48px", SRC_EL + "; enquire Submit computed height"),
            },
            "button-brand": {
                "bg": color("--brand-900"),
                "text": tok("#ffffff", "color", SRC_EL + "; Check Availability computed color"),
                "radius": dim_px("2px", SRC_EL + "; Check Availability computed border-radius"),
                "height": dim_px("40px", SRC_EL + "; Check Availability computed height"),
            },
            "button-search": {
                "bg": color("--brand-500"),
                "radius": dim_px("0px", SRC_EL + "; home search button computed border-radius"),
                "size": dim_px("40px", SRC_EL + "; home search button computed width and height"),
            },
            "field": {
                "bg": tok("rgba(0, 0, 0, 0)", "color", SRC_EL + "; enquire field shell computed background"),
                "text": color("--neutral-900"),
                "radius": dim_px("2px", SRC_EL + "; enquire field shell computed border-radius"),
            },
        },
    },
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}
    ],
}



def main():
    out = HERE / "tokens.json"
    text = json.dumps(build(), indent=2, ensure_ascii=False) + "\n"
    out.write_text(text)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
