#!/usr/bin/env python3
"""Write tokens.json from raw/foundations.json.

Values were read with getComputedStyle on shuttle.zip on 2026-11-19. This
script does not invent colours. Re-run only after updating the raw file.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "foundations.json").read_text())
OUT = HERE / "tokens.json"


def tok(type_, value, source):
    return {"$type": type_, "$value": value, "$extensions": {"source": source}}


def color(value, source):
    return tok("color", value, source)


def rgba_hex(value):
    """A computed rgba(r, g, b, a) as #rrggbbaa, so a translucent reading keeps its alpha."""
    r, g, b, a = (float(x) for x in value[value.index("(") + 1:-1].split(","))
    return "#%02x%02x%02x%02x" % (round(r), round(g), round(b), round(a * 255))


def dim(value, source):
    return tok("dimension", value, source)


def build():
    src = RAW["source"]
    c = RAW["colors"]
    t = RAW["type"]
    fonts = RAW["fonts"]
    core = {
        "color": {
            "black": color(c["black"], src + " body background"),
            "white": color(c["white"], src + " body color and --color-label"),
            "tint": color(c["tint"], src + " computed rgb(0, 119, 255) from --color-tint #0077ffff"),
            "link": color("#0984ff", src + " declared --color-link #0984ffff, not painted on a measured link"),
            "grouped": color(c["grouped"], src + " --color-grouped #2c2c2eff"),
            "grouped2": color(c["grouped2"], src + " --color-grouped2 and switch thumb"),
            "grouped3": color(c["grouped3"], src + " --color-grouped3"),
            "background2": color(c["background2"], src + " --color-background2 menu"),
            "panel": color(c["panelHex"], src + " demo panel dark:bg-neutral-800/90 painted #262626 at 0.9"),
            "lede": color(c["lede"], src + " about lede and updates prose"),
            "neutral400": color(c["neutral400"], src + " demo panel header text-neutral-400"),
            "neutral500": color(c["neutral500"], src + " FAQ question text-neutral-500"),
            "label2": color(c["label2Hex"], src + " --color-label2 #ebebf599, alpha recorded in components.md"),
        },
        "font": {
            "family": {
                "sans": tok("fontFamily", fonts["sans"], src + " body font-family, InterVariable from rsms.me/inter"),
            },
            "weight": {
                "regular": tok("fontWeight", 400, src + " body"),
                "medium": tok("fontWeight", 500, src + " display, nav, pill, auth title"),
                "semibold": tok("fontWeight", 600, src + " wordmark and app button"),
                "bold": tok("fontWeight", 700, src + " pricing Contact us"),
                "extrabold": tok("fontWeight", 800, src + " updates article h1"),
            },
            "size": {
                "xs": dim("12px", src + " app button and legal links"),
                "sm": dim("14px", src + " nav, pill, field, FAQ"),
                "md": dim("15px", src + " about Upload File text-[15px]"),
                "base": dim("16px", src + " body and field text"),
                "lede": dim("24px", src + " about lede"),
                "auth": dim("30px", src + " signup and login h3"),
                "prose": dim("36px", src + " updates article h1"),
                "display": dim("62px", src + " marketing h2 at 1169px"),
            },
        },
        "typography": {
            "display": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["sans"],
                    "fontSize": "62px",
                    "fontWeight": 500,
                    "lineHeight": "72px",
                    "letterSpacing": "-1.55px",
                },
                "$extensions": {"source": src + " about h2 New simple in file sharing"},
            },
            "authTitle": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["sans"],
                    "fontSize": "30px",
                    "fontWeight": 500,
                    "lineHeight": "36px",
                    "letterSpacing": "-0.75px",
                },
                "$extensions": {"source": src + " signup h3 Welcome!"},
            },
            "lede": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["sans"],
                    "fontSize": "24px",
                    "fontWeight": 400,
                    "lineHeight": "33px",
                },
                "$extensions": {"source": src + " about header p"},
            },
            "body": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["sans"],
                    "fontSize": "16px",
                    "fontWeight": 400,
                    "lineHeight": "24px",
                },
                "$extensions": {"source": src + " body"},
            },
            "nav": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["sans"],
                    "fontSize": "14px",
                    "fontWeight": 500,
                    "lineHeight": "20px",
                },
                "$extensions": {"source": src + " about nav link"},
            },
            "button": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["sans"],
                    "fontSize": "12px",
                    "fontWeight": 600,
                    "lineHeight": "16px",
                },
                "$extensions": {"source": src + " space Log In and Share"},
            },
        },
        "radius": {
            "sm": dim("6px", src + " suggestions field rounded-menuItem"),
            "md": dim("8px", src + " app button and Next"),
            "lg": dim("12px", src + " field rounded-xl and menu rounded-menu"),
            "xl": dim("16px", src + " demo panel rounded-2xl"),
            "2xl": dim("24px", src + " pricing card rounded-3xl"),
            "full": dim("9999px", src + " Sign up pill and switch"),
        },
        "spacing": {
            "1": dim("4px", src + " header gap-1"),
            "2": dim("8px", src + " nav py-2 and button gap"),
            "3": dim("12px", src + " app button horizontal padding and field py-3"),
            "4": dim("16px", src + " nav px-4, field px-4, card padding"),
            "5": dim("20px", src + " Contact us px-5"),
        },
        "motion": {
            "duration": {
                "fast": tok("duration", "150ms", src + " button transition 0.15s"),
            },
            "easing": {
                "standard": tok(
                    "cubicBezier",
                    [0.4, 0, 0.2, 1],
                    src + " button and switch cubic-bezier(0.4, 0, 0.2, 1)",
                ),
            },
        },
    }
    dark = {
        "surface": {
            "page": color(c["page"], src + " body background and --color-background"),
            "raised": color(c["grouped"], src + " field bg-group and secondary button"),
            "menu": color(c["background2"], src + " suggestions menu --color-background2"),
            "panel": color(c["panelHex"], src + " demo panel #262626 at 0.9 alpha"),
        },
        "text": {
            "primary": color(c["text"], src + " body color --color-label"),
            "secondary": color(c["lede"], src + " about lede #d4d4d4"),
            "muted": color(rgba_hex(c["label2"]), src + " --color-label2 painted rgba(235, 235, 245, 0.6)"),
            "faint": color(c["neutral500"], src + " FAQ text-neutral-500"),
            "onAccent": color(c["white"], src + " Sign up and Share text on tint"),
            "onInverse": color(c["black"], src + " Contact us text on white pill"),
        },
        "accent": color(c["tint"], src + " Sign up, Share, Next, --color-tint"),
        "link": color("#0984ff", src + " declared --color-link, not a painted link colour"),
        "border": {
            "default": color(c["grouped"], src + " field fill stands in for a border; fields have 0px border"),
            "hairline": color(rgba_hex(c["hairline"]), src + " pricing card border rgba(255, 255, 255, 0.2)"),
            "pro": color(c["proBorder"], src + " Pro card computed border rgb(0, 122, 255)"),
        },
        "component": {
            "button": {
                "bg": color(c["tint"], src + " Share and Next background"),
                "text": color(c["white"], src + " Share and Next color"),
                "radius": dim("8px", src + " app button and Next"),
                "height": dim("32px", src + " app button and Next"),
            },
            "pill": {
                "bg": color(c["tint"], src + " nav Sign up"),
                "text": color(c["white"], src + " nav Sign up"),
                "radius": dim("9999px", src + " rounded-full"),
            },
            "field": {
                "bg": color(c["grouped"], src + " signup and login field wrapper bg-group"),
                "text": color(c["white"], src + " field color"),
                "radius": dim("12px", src + " rounded-xl"),
                "height": dim("40px", src + " h-10"),
            },
        },
    }
    return {
        "$schema": "https://www.designtokens.org/schemas/2025.10/format/",
        "core": core,
        "dark": dark,
        "$themes": [{"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}}],
    }


if __name__ == "__main__":
    OUT.write_text(json.dumps(build(), indent=2) + "\n")
    print(f"wrote {OUT}")
