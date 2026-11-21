#!/usr/bin/env python3
"""Build systems/netflix/tokens.json from raw/computed.json.

Every value was read with getComputedStyle on a live public page on 2026-11-21.
Netflix declared no custom properties on :root. Unread roles stay Not captured.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "computed.json").read_text())


def tok(value, ty, source):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def color(name, note):
    return tok(name, "color", "Measured " + note)


def dim(value, note):
    return tok(value, "dimension", "Measured " + note)


core = {
    "color": {
        "black": color("#000000", "body background on the marketing homepage"),
        "white": color("#ffffff", "h1 color on the marketing homepage"),
        "red": color("#e50914", "Sign In and Get Started backgroundColor"),
        "red-hover": color("#c11119", "Get Started backgroundColor while hovered"),
        "field": color("rgba(22, 22, 22, 0.7)", "email field painted shell backgroundColor"),
        "grey-border": color("rgba(128, 128, 128, 0.7)", "email field painted shell border-top-color"),
        "faq": color("#2d2d2d", "FAQ question row backgroundColor"),
        "card": color("#232323", "trending title button backgroundColor"),
        "dialog": color("#161616", "title-modal backgroundColor"),
        "scrim": color("rgba(0, 0, 0, 0.7)", "title-modal background scrim"),
        "text-muted": color("rgba(255, 255, 255, 0.7)", "footer link color"),
        "help-ink": color("#221f1f", "help.netflix.com body color"),
        "cookie-ink": color("#333333", "OneTrust preference heading color"),
    },
    "font": {
        "family": tok(
            'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
            "fontFamily",
            "Measured h1 fontFamily on the marketing homepage. Netflix Sans is proprietary and is not committed.",
        )
    },
    "typography": {
        "display": {
            "fontFamily": "{core.font.family}",
            "fontSize": dim("56px", "marketing h1 fontSize"),
            "fontWeight": tok("700", "fontWeight", "Measured marketing h1 fontWeight"),
            "lineHeight": dim("70px", "marketing h1 lineHeight"),
        },
        "heading": {
            "fontFamily": "{core.font.family}",
            "fontSize": dim("32px", "login h1 fontSize"),
            "fontWeight": tok("700", "fontWeight", "Measured login h1 fontWeight"),
            "lineHeight": dim("32px", "login h1 fontSize used as line height; computed line-height was not a separate length"),
        },
        "section": {
            "fontFamily": "{core.font.family}",
            "fontSize": dim("24px", "h2 Trending now fontSize"),
            "fontWeight": tok("500", "fontWeight", "Measured h2 fontWeight"),
            "lineHeight": dim("24px", "h2 fontSize; computed line-height was normal, Not captured as a separate length"),
        },
        "body": {
            "fontFamily": "{core.font.family}",
            "fontSize": dim("16px", "email input fontSize"),
            "fontWeight": tok("400", "fontWeight", "Measured email input fontWeight"),
            "lineHeight": dim("24px", "email input lineHeight"),
        },
        "label": {
            "fontFamily": "{core.font.family}",
            "fontSize": dim("14px", "Sign In fontSize"),
            "fontWeight": tok("500", "fontWeight", "Measured Sign In fontWeight"),
            "lineHeight": dim("14px", "Sign In lineHeight"),
        },
        "caption": {
            "fontFamily": "{core.font.family}",
            "fontSize": dim("14px", "footer link fontSize"),
            "fontWeight": tok("400", "fontWeight", "Measured footer link fontWeight"),
            "lineHeight": dim("21px", "footer link lineHeight"),
        },
    },
    "radius": {
        "button": dim("4px", "Sign In and Get Started borderRadius"),
        "field": dim("4px", "email field painted shell borderRadius"),
        "card": dim("8px", "trending title button borderRadius"),
        "dialog": dim("8px", "title-modal borderRadius"),
        "help-field": dim("2px", "help search input borderRadius"),
    },
    "spacing": {
        "4": dim("4px", "Sign In padding-top"),
        "8": dim("8px", "email input padding-bottom"),
        "12": dim("12px", "Get Started padding-top"),
        "16": dim("16px", "Sign In padding-left and email padding-left"),
        "24": dim("24px", "Get Started padding-left and FAQ padding"),
    },
    "size": {
        "button-sm": dim("32px", "Sign In height"),
        "button-md": dim("48px", "login Continue height"),
        "button-lg": dim("56px", "Get Started height"),
        "field": dim("56px", "email field painted shell height"),
        "focus": dim("2px", "Get Started focus outline-width"),
    },
    "border": {
        "field": dim("1px", "email field painted shell border-top-width"),
    },
    "shadow": {
        "dialog": tok(
            {
                "color": "rgba(0, 0, 0, 0.8)",
                "offsetX": "0px",
                "offsetY": "4px",
                "blur": "8px",
                "spread": "0px",
            },
            "shadow",
            "Measured title-modal boxShadow",
        )
    },
    "motion": {
        "button": tok("250ms", "duration", "Measured Get Started transitionDuration 0.25s"),
        "button-ease": tok(
            [0.4, 0, 0.68, 0.06],
            "cubicBezier",
            "Measured Get Started transitionTimingFunction",
        ),
    },
}

dark = {
    "color": {
        "bg": {
            "page": tok("{core.color.black}", "color", "Derived alias of measured body background"),
            "surface": tok("{core.color.faq}", "color", "Derived alias of measured FAQ row"),
            "raised": tok("{core.color.card}", "color", "Derived alias of measured title card"),
            "overlay": tok("{core.color.dialog}", "color", "Derived alias of measured title-modal"),
            "scrim": tok("{core.color.scrim}", "color", "Derived alias of measured title-modal scrim"),
        },
        "text": {
            "primary": tok("{core.color.white}", "color", "Derived alias of measured h1"),
            "secondary": tok("{core.color.text-muted}", "color", "Derived alias of measured footer link"),
            "on-accent": tok("{core.color.white}", "color", "Derived alias of measured button label"),
        },
        "border": {
            "default": tok("{core.color.grey-border}", "color", "Derived alias of measured field border"),
            "focus": tok("{core.color.white}", "color", "Derived alias of measured focus outline"),
        },
        "accent": {
            "default": tok("{core.color.red}", "color", "Derived alias of measured button fill"),
            "hover": tok("{core.color.red-hover}", "color", "Derived alias of measured hover fill"),
        },
    },
    "component": {
        "button": {
            "background": tok("{core.color.red}", "color", "Derived alias of measured Get Started"),
            "text": tok("{core.color.white}", "color", "Derived alias of measured button label"),
            "radius": tok("{core.radius.button}", "dimension", "Derived alias of measured button radius"),
            "height": tok("{core.size.button-lg}", "dimension", "Derived alias of measured Get Started height"),
        },
        "field": {
            "background": tok("{core.color.field}", "color", "Derived alias of measured field shell"),
            "text": tok("{core.color.white}", "color", "Derived alias of measured field color"),
            "radius": tok("{core.radius.field}", "dimension", "Derived alias of measured field radius"),
            "height": tok("{core.size.field}", "dimension", "Derived alias of measured field height"),
        },
    },
}

light = {
    "color": {
        "bg": {
            "page": color("#ffffff", "help.netflix.com body backgroundColor"),
            "surface": color("#ffffff", "help search input backgroundColor"),
        },
        "text": {
            "primary": color("#221f1f", "help.netflix.com body color"),
            "secondary": color("rgba(0, 0, 0, 0.7)", "help Plans and Pricing link color"),
        },
        "accent": {
            "default": tok("{core.color.red}", "color", "Derived. Help pages reuse the same red brand; the help home did not paint a red control in the sampled nodes"),
        },
        "border": {
            "default": color("#000000", "help search input border-top-color; width was 0px"),
        },
    }
}

doc = {
    "$schema": "https://www.w3.org/community/design-tokens/",
    "core": core,
    "dark": dark,
    "light": light,
    "$themes": [
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
    "$metadata": {
        "tokenSetOrder": ["core", "dark", "light"],
    },
    "$extensions": {
        "notTokenised": [
            "Accent pressed, disabled, loading, and error fills: not shown on the public pages.",
            "Status success, warning, danger, and info: not shown.",
            "Text disabled and a distinct link colour on the marketing page: footer links use text.secondary.",
            "Border strong: not a separate computed colour.",
            "Reduced motion: not read.",
            "Breakpoints: captures were taken at 1440 and 390; the CSS breakpoint values were not read.",
            "Code type role: not present on the public marketing pages.",
        ]
    },
}

(HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", HERE / "tokens.json")
