#!/usr/bin/env python3
"""Write systems/stocktwits/tokens.json from the 2026-11-19 live readings.

Values are the custom properties resolved on stocktwits.com while the T3
preview tab was on the public signed-out pages. Light and dark come from
[data-theme="light"] and [data-theme="dark"] on the same document. A value
that was not on the page is not invented here.
"""

from __future__ import annotations

import json
from pathlib import Path

PKG = Path(__file__).resolve().parent.parent
OUT = PKG / "tokens.json"

SRC = "stocktwits.com computed custom properties, T3 preview, 2026-11-19"


def color(value: str, note: str) -> dict:
    return {
        "$value": value,
        "$type": "color",
        "$extensions": {"source": f"{SRC}: {note}"},
    }


# Custom properties the page declared that no file in raw/ holds: raw/ has computed styles of
# controls (components-computed.json) and motion rules, but no custom-property dump. These values
# were typed in from the T3 preview at capture time, so they carry the hand-entered label.
HAND = {
    "black2", "white2", "blue", "blueAdaDark", "greenDark", "redDark", "orange", "sentimentOrange",
    "edgeBlue", "edgePurple", "stLightGrey3", "stLightGrey7", "stDarkGrey3", "stDarkGrey4",
    "stDarkGrey5", "stDarkGrey6", "charcoalDarker3", "pageDark",
}


def hand(token: dict) -> dict:
    """Relabel a token whose reading is not in raw/: Reconstruction, entered by hand."""
    note = token["$extensions"]["source"][len(SRC) + 2:]
    token["$extensions"]["source"] = (
        f"Reconstruction: entered by hand at capture time from {note} on stocktwits.com "
        "(T3 preview, 2026-11-19); no raw/ file holds this reading"
    )
    return token


def dim(value: str, note: str) -> dict:
    return {
        "$value": value,
        "$type": "dimension",
        "$extensions": {"source": f"{SRC}: {note}"},
    }


def font_family(value: str, note: str) -> dict:
    return {
        "$value": value,
        "$type": "fontFamily",
        "$extensions": {"source": f"{SRC}: {note}"},
    }


def font_weight(value: str, note: str) -> dict:
    return {
        "$value": value,
        "$type": "fontWeight",
        "$extensions": {"source": f"{SRC}: {note}"},
    }


def duration(value: str, note: str) -> dict:
    return {
        "$value": value,
        "$type": "duration",
        "$extensions": {"source": f"{SRC}: {note}"},
    }


def bezier_points(value: str) -> list:
    """"0.25, 0.1, 0.25, 1" as the four numbers DTCG's cubicBezier holds. A string would
    export as a bare number list, which is not a CSS easing."""
    points = [float(p) for p in value.split(",")]
    assert len(points) == 4, value
    return [int(p) if p.is_integer() else p for p in points]


def cubic(value: str, note: str) -> dict:
    return {
        "$value": bezier_points(value),
        "$type": "cubicBezier",
        "$extensions": {"source": f"{SRC}: {note}"},
    }


def text(value: str, note: str) -> dict:
    return {
        "$value": value,
        "$type": "other",
        "$extensions": {"source": f"{SRC}: {note}"},
    }


def core() -> dict:
    doc = {
        "color": {
            "black": color("#000000", "--black"),
            "black2": color("#101010", "--black-2"),
            "white": color("#ffffff", "--white"),
            "white2": color("#f8f8fb", "--white-2"),
            "blue": color("#008fff", "--blue, also --primary-button-hover"),
            "blue5": color("#1b66e7", "--blue-5, also --primary-button-background and --legal-blue"),
            "blueAdaLight": color("#1b66e7", "--blue-ada on [data-theme=light]"),
            "blueAdaDark": color("#008fff", "--blue-ada on [data-theme=dark]"),
            "greenLight": color("#128760", "--green and --price-positive on [data-theme=light]"),
            "greenDark": color("#19b682", "--green and --price-positive on [data-theme=dark]"),
            "redLight": color("#dd331d", "--red and --price-negative on [data-theme=light]"),
            "redDark": color("#fe433d", "--red and --price-negative on [data-theme=dark]"),
            "purpleLight": color("#8146ff", "--purple on [data-theme=light]"),
            "purpleDark": color("#9666ff", "--purple on [data-theme=dark]"),
            "orange": color("#ff8125", "--orange"),
            "sentimentOrange": color("#ba5d1a", "--sentiment-orange"),
            "edgeBlue": color("#1b8dff", "--edge-blue"),
            "edgePurple": color("#9369ee", "--edge-purple"),
            "stLightGrey1": color("#8e8e93", "--st-light-grey-1, also --st-tertiary-text"),
            "stLightGrey2": color("#aeaeb2", "--st-light-grey-2"),
            "stLightGrey3": color("#c7c7cc", "--st-light-grey-3"),
            "stLightGrey4": color("#d1d1d6", "--st-light-grey-4, also --primary-button-disabled in light"),
            "stLightGrey5": color("#e5e5ea", "--st-light-grey-5, also --primary-border in light"),
            "stLightGrey6": color("#f2f2f7", "--st-light-grey-6, also --secondary-background in light"),
            "stLightGrey7": color("#f9f9fb", "--st-light-grey-7"),
            "stDarkGrey2": color("#636366", "--st-dark-grey-2, also --st-secondary-text in light"),
            "stDarkGrey3": color("#48484a", "--st-dark-grey-3"),
            "stDarkGrey4": color("#3a3a3c", "--st-dark-grey-4"),
            "stDarkGrey5": color("#2c2c2e", "--st-dark-grey-5"),
            "stDarkGrey6": color("#1c1c1e", "--st-dark-grey-6, also --primary-background in dark"),
            "charcoalDarker3": color("#151516", "--charcoal-darker-3"),
            "pageDark": color("#0e0e0f", "--tertiary-background on [data-theme=dark]"),
            "placeholder": color("#9ca3af", "computed ::placeholder on the sign-in email field, rgb(156, 163, 175)"),
            "onetrust": color("#1d68d7", "computed background of the OneTrust I Accept button, rgb(29, 104, 215)"),
            "strike": color("#aeaeb2", "computed colour of the struck list price on /subscriptions, rgb(174, 174, 178)"),
        },
        "font": {
            "family": {
                "sans": font_family(
                    "Source Sans 3, Source Sans 3 Fallback, Arial, sans-serif",
                    "computed font-family on body: \"Source Sans 3\", \"Source Sans 3 Fallback\"; fallback @font-face is local(\"Arial\")",
                ),
            },
            "weight": {
                "regular": font_weight("400", "computed weight of body, links, and the sign-in field"),
                "semibold": font_weight("600", "computed weight of STButton and the symbol price"),
                "bold": font_weight("700", "computed weight of the sign-in h1, plan name, and about hero"),
                "black": font_weight("900", "computed weight of the sign-in welcome line"),
            },
        },
        "space": {
            "1": dim("4px", "computed gap on the xs button and stream avatar spacing, --stream-message-timeline-avatar-spacing"),
            "2": dim("8px", "computed gap on the md button and live-calls badge padding-block"),
            "3": dim("12px", "computed padding-inline on the xs button and search field gap"),
            "4": dim("16px", "computed search padding-inline and --stream-message-outer-spacing"),
            "5": dim("20px", "computed padding-inline on the md button"),
            "6": dim("24px", "computed padding-inline on the lg button"),
            "7": dim("28px", "computed padding-inline on the xl button"),
            "8": dim("32px", "computed gap of the about top nav, gap-x-[32px]"),
            "10": dim("40px", "computed height of the md button and the sign-in field"),
        },
        "radius": {
            "none": dim("0px", "computed radius of the header and the For You tab"),
            "sm": dim("6px", "computed radius of the enterprise sales field"),
            "md": dim("8px", "computed radius of the sign-in and signup field"),
            "lg": dim("12px", "computed radius of the subscription card"),
            "xl": dim("40px", "computed radius of the about content card"),
            "full": dim("9999px", "computed radius of STButton, the search pill, and the live-calls badge"),
        },
        "size": {
            "buttonXs": dim("24px", "computed height of the Use App button at 390px"),
            "buttonMd": dim("40px", "computed height of STButton_md and the sign-in field"),
            "buttonLg": dim("48px", "computed height of STButton_lg, Enter Stocktwits"),
            "buttonXl": dim("56px", "computed height of STButton_xl, Get Started"),
            "header": dim("90px", "resolved --header on the desktop shell"),
            "mobileHeader": dim("52px", "computed height of MobileHeader at 390px"),
            "sidebar": dim("300px", "resolved --sidebar, computed width of the watchlist column"),
            "search": dim("36px", "computed height of the search pill"),
            "avatar": dim("40px", "computed width and height of the stream avatar image"),
            "maxLayout": dim("1280px", "resolved --max-layout-width"),
        },
        "shadow": {
            "plan": text(
                "0px 10px 20px 0px rgba(0, 0, 0, 0.05)",
                "computed box-shadow of .Chargebee_card on /subscriptions",
            ),
        },
        "motion": {
            "duration": {
                "hamburger": duration("300ms", "declared transition-duration 0.3s on .HomeLandingPageMobileMenu_hamburgerLine"),
                "float": duration("3000ms", "declared animation-duration 3s on .HomeLandingPage_floatingHeroImage"),
                "gradient": duration("4000ms", "declared animation-duration 4s on .HomeLandingPage_gradientText"),
                "count": duration("0ms", "under prefers-reduced-motion: reduce, AnimatedCount enter and exit animations are set to 0s"),
            },
            "easing": {
                "ease": cubic("0.25, 0.1, 0.25, 1", "declared timing-function ease on the hamburger line, expanded from the CSS keyword"),
                "progress": cubic("0, 0, 0.2, 1", "computed transition-timing-function of the top progress bar, cubic-bezier(0, 0, 0.2, 1), duration 0.25s"),
            },
        },
    }
    for key in HAND:
        hand(doc["color"][key])
    return doc


def semantic(theme: str) -> dict:
    page = "{color.white}" if theme == "light" else "{color.stDarkGrey6}"
    text = "{color.black}" if theme == "light" else "{color.white}"
    muted = "{color.stDarkGrey2}" if theme == "light" else "{color.stLightGrey2}"
    accent = "{color.blue5}" if theme == "light" else "{color.blueAdaDark}"
    border = "{color.stLightGrey5}" if theme == "light" else "{color.stDarkGrey4}"
    surface = "{color.stLightGrey6}" if theme == "light" else "{color.black}"
    positive = "{color.greenLight}" if theme == "light" else "{color.greenDark}"
    negative = "{color.redLight}" if theme == "light" else "{color.redDark}"
    note = f"[data-theme={theme}]"
    return {
        "page": color(page, f"--primary-background on {note}"),
        "surface": color(surface, f"--secondary-background on {note}"),
        "text": color(text, f"--st-primary-text on {note}"),
        "muted": color(muted, f"--st-secondary-text on {note}"),
        "accent": color(accent, f"--blue-ada on {note}; the filled primary button stays --primary-button-background #1b66e7 in both themes"),
        "border": color(border, f"--primary-border on {note}"),
        "positive": color(positive, f"--price-positive on {note}"),
        "negative": color(negative, f"--price-negative on {note}"),
        "button": {
            "primary": color(
                "{color.blue5}",
                "--primary-button-background, unchanged between themes; the filled shell control Sign up or log in was computed rgb(0, 0, 0), not this token",
            ),
            "primaryText": color("{color.white}", "--primary-button-text"),
            "primaryHover": color("{color.blue}", "--primary-button-hover"),
            "secondary": color(
                "{color.white}" if theme == "light" else "{color.stDarkGrey6}",
                f"--secondary-button-background on {note}",
            ),
            "secondaryText": color(text, f"--secondary-button-text on {note}"),
            "secondaryBorder": color(border, f"--secondary-button-border on {note}"),
            "disabled": color(
                "{color.stLightGrey4}" if theme == "light" else "{color.stDarkGrey3}",
                f"--primary-button-disabled on {note}; the empty Log In submit computed rgb(209, 209, 214)",
            ),
            "disabledText": color(
                "{color.white}" if theme == "light" else "{color.black}",
                f"--primary-button-disabled-text on {note}",
            ),
        },
        "field": {
            "background": color(
                "{color.stLightGrey6}" if theme == "light" else "{color.stDarkGrey5}",
                f"--st-input-background on {note}; the sign-in field computed rgb(242, 242, 247)",
            ),
        },
        "focus": hand(color(
            "#86b7fe" if theme == "light" else "#000000",
            f"--select-focused on {note}. The focused sign-in field computed outline none and box-shadow none, so this token is declared and not painted on that control",
        )),
    }


def build() -> dict:
    """The token document; nothing is written (main() writes it)."""
    return {
        "core": core(),
        "light": semantic("light"),
        "dark": semantic("dark"),
        "$themes": [
            {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
    }


def render() -> str:
    """tokens.json's exact text."""
    return json.dumps(build(), indent=2) + "\n"


def main() -> None:
    OUT.write_text(render())
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
