#!/usr/bin/env python3
"""Build tokens.json from the live readings in raw/.

Every colour and length below was read from computed style or a custom
property on https://navan.com/ (and the public pricing, expense and sign-in
boundary pages) on 2026-11-19. Nothing here is sampled from a screenshot.
A type style whose line height raw/components.json does not hold is labelled
Reconstruction: that line height was typed in by hand at capture time.
build() returns the document; running the file writes it.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
OUT = HERE / "tokens.json"

VARS = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components.json").read_text())


def color(value, source):
    return {
        "$type": "color",
        "$value": value,
        "$extensions": {"source": source},
    }


def dim(value, source):
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": source},
    }


def font(value, source):
    return {
        "$type": "fontFamily",
        "$value": value,
        "$extensions": {"source": source},
    }


def text_style(family, size, weight, line_height, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line_height,
        },
        "$extensions": {"source": source},
    }


def by_hand(token, what):
    """Relabel a token one of whose values no file in raw/ holds."""
    token["$extensions"]["source"] = ("Reconstruction: " + what + " was entered by hand at capture time; "
                                      "raw/components.json holds no reading of it. "
                                      + token["$extensions"]["source"].removeprefix("Measured "))
    return token


def ramp(name, steps, source):
    return {
        step: color(value, f"{source} --{name}-{step}")
        for step, value in steps.items()
    }


SRC = "Measured computed custom property on :root, https://navan.com/, 1440x900, 2026-11-19"
HOME = "Measured computed style, https://navan.com/, 1440x900, dpr 2, 2026-11-19"
PRICE = "Measured computed style, https://navan.com/pricing, 1440x900, 2026-11-19"
LOGIN = "Measured computed style, https://login.navan.com/ identifier page, 1440x900, 2026-11-19. Email field was not filled."

def build():
    """The token document, built in memory from raw/; main() writes it."""
    return {
        "$description": "Navan public marketing site, measured 2026-11-19. Light only: the signed-out marketing pages ship no dark theme switch.",
        "core": core(),
        "light": light(),
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}
        ],
    }


def core():
    return {
    "color": {
        "blurple": ramp("blurple", VARS["color"]["blurple"], SRC),
        "gray": ramp("gray", VARS["color"]["gray"], SRC),
        "aqua": ramp("aqua", VARS["color"]["aqua"], SRC),
        "lilac": ramp("lilac", VARS["color"]["lilac"], SRC),
        "red": ramp("red", VARS["color"]["red"], SRC),
        "yellow": ramp("yellow", VARS["color"]["yellow"], SRC),
        "tan": ramp("tan", VARS["color"]["tan"], SRC),
        "black": ramp("black", VARS["color"]["black"], SRC),
        "white": ramp("white", VARS["color"]["white"], SRC),
    },
    "font": {
        "family": {
            "sans": font("Inter, Inter Fallback, ui-sans-serif, system-ui", HOME + " body"),
            "serif": font("Sanomat, ui-serif", HOME + " h1"),
            "login": font("nvn-regular, Helvetica", LOGIN + " label"),
            "login-heading": font("nvn-heading, serif", LOGIN + " h1"),
        }
    },
    "typography": {
        "display": text_style("Sanomat, ui-serif", "45px", "600", "54px", HOME + " h1"),
        "display-phone": text_style("Sanomat, ui-serif", "25px", "600", "30px", "Measured computed style, expense page at innerWidth 390, 2026-11-19"),
        "heading": text_style(COMP["h2"]["fontFamily"], COMP["h2"]["fontSize"], COMP["h2"]["fontWeight"], COMP["h2"]["lineHeight"], HOME + " h2 (raw/components.json h2)"),
        "title": by_hand(text_style("Inter, Inter Fallback, ui-sans-serif, system-ui", "21px", "300", "30px", HOME + " hero prompt"), "the hero prompt style"),
        "body": text_style("Inter, Inter Fallback, ui-sans-serif, system-ui", "16px", "300", "24px", HOME + " body. letter-spacing computed -2%, not tokenised"),
        "nav": text_style("Inter, Inter Fallback, ui-sans-serif, system-ui", "14px", "400", "19px", HOME + " nav item"),
        "button": text_style("Inter, Inter Fallback, ui-sans-serif, system-ui", "14px", "400", "20px", HOME + " primary link"),
        "price": by_hand(text_style("Inter, Inter Fallback, ui-sans-serif, system-ui", "30px", "700", "36px", PRICE + " Free"), "the 36px line height"),
        "feature": by_hand(text_style("Inter, Inter Fallback, ui-sans-serif, system-ui", "15px", "300", "26px", PRICE + " feature row"), "the 26px line height"),
        "faq": by_hand(text_style("Inter, Inter Fallback, ui-sans-serif, system-ui", "19px", "300", "25px", PRICE + " FAQ button"), "the 25px line height"),
        "footer": by_hand(text_style("Inter, Inter Fallback, ui-sans-serif, system-ui", "13px", "300", "19px", PRICE + " footer Privacy link"), "the 19px line height"),
        "login-heading": by_hand(text_style("nvn-heading, serif", "40px", "600", "40px", LOGIN + " h1. line-height was not read; the 40px size is repeated as the line height"), "the 40px line height"),
        "login-label": by_hand(text_style(COMP["login"]["label"]["fontFamily"], COMP["login"]["label"]["fontSize"], COMP["login"]["label"]["fontWeight"], "20px", LOGIN + " Email address label, computed 13.92px"), "the 20px line height"),
    },
    "radius": {
        "none": dim("0px", HOME + " body"),
        "control": dim("8px", HOME + " hidden checkbox, unused as a painted field"),
        "input": dim("10px", LOGIN + " email input"),
        "tile": dim("12px", HOME + " choice tile and cookie sheet top"),
        "card": dim("14px", HOME + " flip-card-inner"),
        "sheet": dim("12px", PRICE + " cookie sheet top corners"),
        "plan": dim("20px", PRICE + " plan card"),
        "login-card": dim("12px", LOGIN + " widget outer"),
        "pill": dim("9999px", HOME + " Get started"),
        "login-button": dim("100px", LOGIN + " Continue"),
    },
    "spacing": {
        "2": dim("8px", HOME + " checkbox padding-block, the 8px step on the page"),
        "3": dim("10px", HOME + " button padding-block"),
        "4": dim("16px", HOME + " announcement text block"),
        "5": dim("20px", HOME + " h1 margin-bottom"),
        "6": dim("28px", HOME + " button padding-inline and nav gap"),
        "7": dim("40px", PRICE + " cookie sheet padding-block"),
        "8": dim("48px", PRICE + " footer padding-top"),
        "9": dim("64px", PRICE + " cookie sheet padding-inline"),
        "nav": dim("77px", HOME + " --global-nav-height and measured nav"),
        "announce": dim("50px", HOME + " measured announcement bar; token --global-announcement-bar-height is 55px"),
    },
    "size": {
        "button": dim("44px", HOME + " Get started height"),
        "button-compact": dim("40px", PRICE + " cookie buttons"),
        "login-control": dim("52px", LOGIN + " email input and Continue"),
        "tile": dim("80px", HOME + " choice tile"),
        "screen-xs": dim("380px", SRC + " --screen-xs"),
        "screen-sm": dim("576px", SRC + " --screen-sm"),
        "screen-md": dim("768px", SRC + " --screen-md"),
        "screen-lg": dim("1025px", SRC + " --screen-lg"),
        "screen-xl": dim("1230px", SRC + " --screen-xl"),
        "screen-xxl": dim("1440px", SRC + " --screen-xxl"),
    },
    "motion": {
        "duration": {
            "fast": {"$type": "duration", "$value": "150ms", "$extensions": {"source": HOME + " button transition-duration 0.15s"}},
            "tile": {"$type": "duration", "$value": "200ms", "$extensions": {"source": HOME + " choice tile transition 0.2s"}},
        },
        "easing": {
            "standard": {"$type": "cubicBezier", "$value": [0.4, 0, 0.2, 1], "$extensions": {"source": HOME + " button and tile transition-timing-function cubic-bezier(0.4, 0, 0.2, 1)"}},
        },
    },
    }


def light():
    return {
    "background": {
        "page": color("#ffffff", HOME + " nav and plan cards paint white; body itself is transparent"),
        "surface": color("#ffffff", HOME + " flip-card and plan card"),
        "muted": color("#f1f1f9", HOME + " section background #F1F1F9, matches --gray-250"),
        "tint": color("#f0f0ff", HOME + " choice tile default and expense hero, --blue-50"),
        "tint-selected": color("#e1e2fe", HOME + " selected choice tile, --blurple-100"),
        "action": color("#6307f8", HOME + " Get started, --blurple-500"),
        "action-dark": color("#15002c", HOME + " Request a demo and footer, --blurple-900"),
        "inverse": color("#15002c", PRICE + " footer"),
        "login": color("#f5f5f8", LOGIN + " body"),
        "login-action": color("#131316", LOGIN + " Continue"),
    },
    "text": {
        "primary": color("#15002c", HOME + " h1, --blue-900"),
        "secondary": color("#5a5a72", PRICE + " feature rows, --gray-600"),
        "muted": color("#70708f", HOME + " review 'out of', --gray-550"),
        "inverse": color("#ffffff", HOME + " button label"),
        "link": color("#6307f8", HOME + " Log In at the wide nav, --blurple-500"),
        "login": color("#1e212a", LOGIN + " heading and label"),
        "login-link": color("#7300cd", LOGIN + " Can't log in link"),
        "on-announce": color("#ffffff", HOME + " announcement text"),
    },
    "border": {
        "stroke": color("#c6c6d2", HOME + " body border-top-color, --gray-400"),
        "action": color("#6307f8", HOME + " primary button border"),
        "strong": color("#15002c", PRICE + " secondary cookie button"),
        "plan": color("#6307f8", PRICE + " plan card"),
        "login": color("#a14be3", LOGIN + " focused email input"),
        "login-social": color("#0f1419", LOGIN + " social buttons"),
    },
    "focus": {
        "ring": color("#6307f8", HOME + " primary control colour; outline-offset 4px, outline-width 3px"),
    },
    "component": {
        "button-primary-bg": color("#6307f8", HOME),
        "button-primary-text": color("#ffffff", HOME),
        "button-primary-radius": dim("9999px", HOME),
        "button-primary-height": dim("44px", HOME),
        "nav-height": dim("77px", HOME),
        "input-radius": dim("10px", LOGIN),
        "input-height": dim("52px", LOGIN),
        "card-radius": dim("14px", HOME),
        "plan-radius": dim("20px", PRICE),
    },
    }


def main():
    OUT.write_text(json.dumps(build(), indent=2) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
