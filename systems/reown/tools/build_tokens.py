#!/usr/bin/env python3
"""Write tokens.json from raw/foundations.json. Measured values only."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = "getComputedStyle on reown.com and docs.reown.com, 2026-11-19, T3 preview tab, viewport 1169x731 at devicePixelRatio 2"


def color(value: str, source: str) -> dict:
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value: str, source: str) -> dict:
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def num(value: str, source: str) -> dict:
    return {"$type": "number", "$value": value, "$extensions": {"source": source}}


def font(value: str, source: str) -> dict:
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def cubic(value: str, source: str) -> dict:
    return {"$type": "cubicBezier", "$value": value, "$extensions": {"source": source}}


def duration(value: str, source: str) -> dict:
    return {"$type": "duration", "$value": value, "$extensions": {"source": source}}


def typography(family: str, size: str, weight: str, line_height: str, letter_spacing: str, source: str) -> dict:
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line_height,
            "letterSpacing": letter_spacing,
        },
        "$extensions": {"source": source},
    }


def build() -> dict:
    raw = json.loads((ROOT / "raw" / "foundations.json").read_text())
    tokens = raw["rootTokens"]
    s = f"{SRC}. Declared on :root as comma-separated RGB channels."

    def rgb(name: str) -> str:
        channels = tokens[name]
        r, g, b = [int(part.strip()) for part in channels.split(",")]
        return f"#{r:02x}{g:02x}{b:02x}"

    core = {
        "color": {
            "black": color("#000000", s + " --p-color-black"),
            "white": color("#ffffff", s + " --p-color-white"),
            "blue": color(rgb("--p-color-blue"), s + " --p-color-blue"),
            "blue-surface": color(rgb("--p-color-blue-surface"), s + " --p-color-blue-surface"),
            "blue-strong": color(rgb("--p-color-blue-strong"), s + " --p-color-blue-strong"),
            "green": color(rgb("--p-color-green"), s + " --p-color-green"),
            "orange": color(rgb("--p-color-orange"), s + " --p-color-orange"),
            "yellow": color(rgb("--p-color-yellow"), s + " --p-color-yellow"),
            "grey": {
                "1": color(rgb("--p-color-grey-1"), s + " --p-color-grey-1"),
                "1-5": color(rgb("--p-color-grey-1_5"), s + " --p-color-grey-1_5"),
                "1-7": color(rgb("--p-color-grey-1_7"), s + " --p-color-grey-1_7"),
                "2": color(rgb("--p-color-grey-2"), s + " --p-color-grey-2"),
                "3": color(rgb("--p-color-grey-3"), s + " --p-color-grey-3"),
                "3-5": color(rgb("--p-color-grey-3_5"), s + " --p-color-grey-3_5"),
                "4": color(rgb("--p-color-grey-4"), s + " --p-color-grey-4"),
                "5": color(rgb("--p-color-grey-5"), s + " --p-color-grey-5"),
                "6": color(rgb("--p-color-grey-6"), s + " --p-color-grey-6"),
                "7": color(rgb("--p-color-grey-7"), s + " --p-color-grey-7"),
                "8": color(rgb("--p-color-grey-8"), s + " --p-color-grey-8"),
            },
        },
        "font": {
            "family": {
                "sans": font("KHTeka-Regular, sans-serif", s + " --p-font-sans"),
                "mono": font("KHTekaMono-Regular, monospace", s + " --p-font-mono"),
                "docs": font(
                    'Inter, -apple-system, system-ui, "Segoe UI", sans-serif',
                    SRC + ". docs body fontFamily",
                ),
                "docs-mono": font(
                    '"Paper Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace',
                    SRC + ". docs code fontFamily",
                ),
            }
        },
        "typography": {
            "h1": typography("KHTeka-Regular, sans-serif", "36px", "400", "1.1", "-0.02em", SRC + ". hero h1 computed, matching --s-type-h1 at this width"),
            "h2": typography("KHTeka-Regular, sans-serif", "30px", "400", "1.1", "-0.02em", SRC + ". pricing title computed 32px; blog h2 computed 30px; token --s-type-h2-size resolved 1.875rem"),
            "lead": typography("KHTeka-Regular, sans-serif", "18px", "400", "1.4", "-0.01em", SRC + ". hero lead computed 18px"),
            "body": typography("KHTeka-Regular, sans-serif", "16px", "400", "1.5", "-0.01em", SRC + ". body and --s-type-body"),
            "small": typography("KHTeka-Regular, sans-serif", "14px", "400", "1.4", "0", SRC + ". --s-type-small-size 0.875rem; footer link computed 14px"),
            "caption": typography("KHTekaMono-Regular, monospace", "12px", "400", "1.5", "0", SRC + ". blog eyebrow computed 12px; --p-text-xs 0.75rem"),
            "button": typography("KHTekaMono-Regular, monospace", "16px", "400", "1", "-0.05rem", SRC + ". Start building computed"),
            "button-large": typography("KHTekaMono-Regular, monospace", "22px", "400", "22px", "-1.1px", SRC + ". nav Learn and Log in computed"),
            "docs-h1": typography("Inter, sans-serif", "36px", "600", "40px", "0", SRC + ". docs h1 computed, dark and light"),
            "docs-body": typography("Inter, sans-serif", "16px", "400", "24px", "0", SRC + ". docs body computed"),
            "docs-small": typography("Inter, sans-serif", "14px", "400", "20px", "0", SRC + ". docs sidebar and muted computed"),
            "price": typography("KHTeka-Regular, sans-serif", "40px", "400", "40px", "0", SRC + ". pricing $0 computed"),
        },
        "radius": {
            "button": dim("16px", SRC + ". --s-radius-button 1rem and Start building borderRadius"),
            "nav-pill": dim("14px", SRC + ". Learn and Log in computed borderRadius"),
            "input": dim("32px", SRC + ". --c-input-radius resolved 2rem; newsletter field borderRadius 32px"),
            "card": dim("16px", SRC + ". content card computed borderRadius"),
            "card-2": dim("40px", SRC + ". announcement and FAQ title computed 40px; --p-radius-40 2.5rem"),
            "card-3": dim("64px", SRC + ". blue content card and blog info card computed 64px"),
            "card-4": dim("88px", SRC + ". blog content card computed 88px; --p-radius-88 5.5rem"),
            "hero": dim("160px", SRC + ". hero computed borderRadius 160px; --s-radius-hero 10rem"),
            "plan": dim("32px", SRC + ". pricing plan card computed 32px"),
            "plan-ring": dim("40px", SRC + ". pricing featured wrapper computed 40px"),
            "docs-code": dim("16px", SRC + ". docs code block computed borderRadius"),
        },
        "spacing": {
            "2": dim("2px", s + " --p-space-2 0.125rem"),
            "4": dim("4px", s + " --p-space-4 0.25rem"),
            "8": dim("8px", s + " --p-space-8 0.5rem"),
            "12": dim("12px", s + " --p-space-12 0.75rem"),
            "16": dim("16px", s + " --p-space-16 1rem"),
            "20": dim("20px", s + " --p-space-20 1.25rem"),
            "24": dim("24px", s + " --p-space-24 1.5rem"),
            "32": dim("32px", s + " --p-space-32 2rem"),
            "40": dim("40px", s + " --p-space-40 2.5rem"),
            "48": dim("48px", s + " --p-space-48 3rem"),
            "64": dim("64px", s + " --p-space-64 4rem"),
            "button-x": dim("15px", SRC + ". Start building padding 13px 15px"),
            "button-y": dim("13px", SRC + ". Start building padding 13px 15px"),
            "page-gutter": dim("8px", SRC + ". header padding 0px 8px; --s-space-page-gutter 0.5rem"),
            "blog-pad": dim("40px", SRC + ". blog content padding 40px 40px 120px"),
        },
        "motion": {
            "duration": {
                "50": duration("50ms", s + " --p-duration-50"),
                "150": duration("150ms", s + " --p-duration-150 0.15s"),
                "250": duration("250ms", s + " --p-duration-250 0.25s"),
                "300": duration("300ms", s + " --p-duration-300 0.3s"),
                "600": duration("600ms", s + " --p-duration-600 0.6s"),
            },
            "easing": {
                "standard": cubic([0.45, 0, 0.55, 1], s + " --p-ease-standard"),
                "out": cubic([0.5, 1, 0.89, 1], s + " --p-ease-out"),
                "in": cubic([0.11, 0, 0.5, 0], s + " --p-ease-in"),
            },
        },
    }

    marketing = {
        "background": {
            "page": color("#9a9a9a", SRC + ". body backgroundColor rgb(154, 154, 154); --s-color-surface"),
            "surface": color("#202020", SRC + ". hero and card backgroundColor rgb(32, 32, 32); --p-color-grey-8"),
            "surface-subtle": color("#e9e9e9", SRC + ". blog card and footer nav rgb(233, 233, 233)"),
            "surface-dim": color("#d0d0d0", SRC + ". feature callout rgb(208, 208, 208)"),
            "pricing": color("#363636", SRC + ". pricing body backgroundColor rgb(54, 54, 54)"),
            "action": color("#379def", SRC + ". Start building backgroundColor rgb(55, 157, 239); --p-color-blue-surface"),
            "action-ink": color("#0988f0", SRC + ". FAQ link and --p-color-blue rgb(9, 136, 240)"),
            "announcement": color("#f4624a", SRC + ". announcement rgb(244, 98, 74)"),
            "positive": color("#18ac65", SRC + ". green card and Growth button rgb(24, 172, 101)"),
            "field": color("#363636", SRC + ". newsletter field rgb(54, 54, 54)"),
        },
        "text": {
            "primary": color("#ffffff", SRC + ". hero h1 color rgb(255, 255, 255)"),
            "secondary": color("#e4e4e4", SRC + ". hero lead rgb(228, 228, 228)"),
            "muted": color("#6c6c6c", SRC + ". body color rgb(108, 108, 108); --s-color-on-surface"),
            "ink": color("#202020", SRC + ". button label and blog heading rgb(32, 32, 32)"),
            "prose": color("#383838", SRC + ". blog paragraph rgb(56, 56, 56)"),
            "on-action": color("#202020", SRC + ". Start building color rgb(32, 32, 32)"),
        },
        "border": {
            "stroke": color("#ffffff", SRC + ". Explore Plans border 1px solid rgb(255, 255, 255)"),
            "subtle": color("#4f4f4f", SRC + ". --s-color-border resolved grey-6 rgb(79, 79, 79)"),
            "divider": color("#bbbbbb", SRC + ". --s-color-divider grey-2 rgb(187, 187, 187)"),
        },
        "focus": {
            "ring": color("#e59700", "Observed. Chromium's default focus ring (-webkit-focus-ring-color), not a Reown colour: the Start building outline after focus() reads rgb(229, 151, 0) and the marketing site styles no ring of its own. " + SRC),
        },
    }

    docs_dark = {
        "background": {
            "page": color("#202020", SRC + ". docs header bar rgb(32, 32, 32); --background-dark 32 32 32"),
            "surface": color("#202020", SRC + ". docs header bar"),
            "code": color("#0b0c0e", SRC + ". docs code block rgb(11, 12, 14)"),
            "action": color("#008847", SRC + ". docs --primary and active nav rgb(0, 136, 71)"),
        },
        "text": {
            "primary": color("#dee2e0", SRC + ". docs h1 rgb(222, 226, 224)"),
            "secondary": color("#ffffff", SRC + ". docs body color rgb(255, 255, 255)"),
            "muted": color("#9ea2a0", SRC + ". docs muted rgb(158, 162, 160)"),
            "code": color("#d4d4d4", SRC + ". docs code rgb(212, 212, 212)"),
            "on-action": color("#008847", SRC + ". active docs link rgb(0, 136, 71)"),
        },
        "border": {
            "stroke": color("#252927", SRC + ". docs --default-border-color 37 41 39"),
        },
    }

    docs_light = {
        "background": {
            "page": color("#ffffff", SRC + ". docs light header bar rgb(255, 255, 255); --background-light"),
            "surface": color("#ffffff", SRC + ". docs light header bar"),
            "action": color("#008847", SRC + ". docs --primary stays rgb(0, 136, 71) in light"),
        },
        "text": {
            "primary": color("#161a18", SRC + ". docs light h1 rgb(22, 26, 24)"),
            "secondary": color("#000000", SRC + ". docs light body color rgb(0, 0, 0)"),
            "muted": color("#4f5452", SRC + ". docs light muted paragraph rgb(79, 84, 82)"),
            "ink": color("#252927", SRC + ". docs light sidebar link rgb(37, 41, 39)"),
        },
        "border": {
            "stroke": color("#eef2f0", SRC + ". docs light --default-border-color 238 242 240"),
        },
    }

    sign_in = {
        "background": {
            "page": color("#202020", SRC + ". sign-in body rgb(32, 32, 32). Not submitted."),
            "surface": color("#252525", SRC + ". sign-in field wrap rgb(37, 37, 37)"),
            "action": color("#0989f1", SRC + ". Sign In button rgb(9, 137, 241)"),
        },
        "text": {
            "primary": color("#ffffff", SRC + ". sign-in body and field text"),
            "muted": color("#9a9a9a", SRC + ". Forgot password link rgb(154, 154, 154)"),
            "on-action": color("#202020", SRC + ". Sign In label rgb(32, 32, 32)"),
        },
        "border": {
            "stroke": color("#363636", SRC + ". sign-in field border 1px solid rgb(54, 54, 54)"),
        },
    }

    doc = {
        "$schema": "https://www.designtokens.org/schemas/2025.10/format/",
        "core": core,
        "marketing": marketing,
        "docs-dark": docs_dark,
        "docs-light": docs_light,
        "sign-in": sign_in,
        "$themes": [
            {"name": "marketing", "selectedTokenSets": {"core": "source", "marketing": "enabled"}},
            {"name": "docs-dark", "selectedTokenSets": {"core": "source", "docs-dark": "enabled"}},
            {"name": "docs-light", "selectedTokenSets": {"core": "source", "docs-light": "enabled"}},
            {"name": "sign-in", "selectedTokenSets": {"core": "source", "sign-in": "enabled"}},
        ],
    }
    return doc


def main() -> None:
    (ROOT / "tokens.json").write_text(json.dumps(build(), indent=2) + "\n")
    print("wrote", ROOT / "tokens.json")


if __name__ == "__main__":
    main()
