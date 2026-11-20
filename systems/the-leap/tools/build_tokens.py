#!/usr/bin/env python3
"""Write tokens.json from raw/foundations.json.

Values were read with getComputedStyle on www.theleap.co and
make.theleap.co on 2026-11-19. This script does not invent colours.
Re-run only after updating the raw file.
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


def dim(value, source):
    return tok("dimension", value, source)


def build():
    src = RAW["source"]
    c = RAW["colors"]
    t = RAW["type"]
    fonts = RAW["fonts"]
    core = {
        "color": {
            "page": color(c["page"], src + " body background #f0edee"),
            "surface": color(c["surface"], src + " pricing-plan #fafafa"),
            "text": color(c["text"], src + " body and nav #482317"),
            "textDeep": color(c["textDeep"], src + " html and h2 #4c2116"),
            "ink": color(c["ink"], src + " logo fill #4d2114"),
            "white": color(c["white"], src + " field background"),
            "accent": color(c["accent"], src + " button-yellow #ecf956"),
            "brown": color(c["brown"], src + " container-brown #4c2116"),
            "cookie": color(c["cookie"], src + " cookie banner #eeeeee"),
            "placeholder": color(c["placeholder"], src + " login placeholder #a1a1a1"),
            "sky": color(c["sky"], src + " home block-images #b1dcfc"),
            "green": color(c["green"], src + " home block-images #c6e57d"),
            "lilac": color(c["lilac"], src + " --background-four-steps #e3c6e4"),
            "coral": color(c["coral"], src + " creator-details #fb7259"),
            "blue": color(c["blue"], src + " --background-signup blue scheme #29a7ff"),
            "greenSolid": color(c["greenSolid"], src + " --background-signup green scheme #52b448"),
        },
        "font": {
            "family": {
                "display": tok("fontFamily", fonts["display"], src + " h1 Tobias"),
                "ui": tok("fontFamily", fonts["ui"], src + " body Favorit"),
                "prose": tok("fontFamily", fonts["prose"], src + " hero subtitle ABC Favorit"),
            },
            "weight": {
                "light": tok("fontWeight", 300, src + " Tobias light and Favorit Book"),
                "book": tok("fontWeight", 350, src + " nav link font-weight 350"),
                "regular": tok("fontWeight", 400, src + " body and button"),
                "bold": tok("fontWeight", 700, src + " price and cookie close"),
            },
        },
        "typography": {
            "hero": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["display"],
                    "fontSize": t["hero"]["size"],
                    "fontWeight": t["hero"]["weight"],
                    "letterSpacing": t["hero"]["letterSpacing"],
                },
                "$extensions": {"source": src + " home h1 at 1169px"},
            },
            "section": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["display"],
                    "fontSize": t["section"]["size"],
                    "fontWeight": t["section"]["weight"],
                    "letterSpacing": t["section"]["letterSpacing"],
                },
                "$extensions": {"source": src + " home h2 buying journey"},
            },
            "display": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["display"],
                    "fontSize": t["display"]["size"],
                    "fontWeight": t["display"]["weight"],
                    "lineHeight": t["display"]["lineHeight"],
                    "letterSpacing": t["display"]["letterSpacing"],
                },
                "$extensions": {"source": src + " pricing h1 at 1169px"},
            },
            "lede": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["prose"],
                    "fontSize": t["lede"]["size"],
                    "fontWeight": t["lede"]["weight"],
                    "letterSpacing": t["lede"]["letterSpacing"],
                },
                "$extensions": {"source": src + " home hero-subtitle"},
            },
            "body": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["ui"],
                    "fontSize": t["body"]["size"],
                    "fontWeight": t["body"]["weight"],
                    "lineHeight": t["body"]["lineHeight"],
                    "letterSpacing": t["body"]["letterSpacing"],
                },
                "$extensions": {"source": src + " body"},
            },
            "nav": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["ui"],
                    "fontSize": t["nav"]["size"],
                    "fontWeight": t["nav"]["weight"],
                    "lineHeight": t["nav"]["lineHeight"],
                    "letterSpacing": t["nav"]["letterSpacing"],
                },
                "$extensions": {"source": src + " nav FEATURES"},
            },
            "button": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["ui"],
                    "fontSize": t["button"]["size"],
                    "fontWeight": t["button"]["weight"],
                    "lineHeight": t["button"]["lineHeight"],
                    "letterSpacing": t["button"]["letterSpacing"],
                },
                "$extensions": {"source": src + " button-yellow"},
            },
            "field": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "Favorit",
                    "fontSize": t["field"]["size"],
                    "fontWeight": t["field"]["weight"],
                    "lineHeight": t["field"]["lineHeight"],
                },
                "$extensions": {"source": src + " login email input"},
            },
        },
        "radius": {
            "cookie": dim("8px", src + " cookie-banner"),
            "card": dim("16px", src + " auth card md:rounded-2xl"),
            "pricing": dim("20px", src + " pricing-plan and pricing SIGN UP"),
            "feature": dim("30px", src + " testimonial-card and block-image"),
            "pill": dim("100px", src + " button-yellow border-radius"),
        },
        "spacing": {
            "1": dim("6px", src + " login field padding-top"),
            "2": dim("7px", src + " button-yellow padding-bottom"),
            "3": dim("10px", src + " button-yellow padding-top"),
            "4": dim("12px", src + " login field padding-left"),
            "5": dim("16px", src + " cookie close padding"),
            "6": dim("24px", src + " LEARN MORE horizontal padding"),
            "7": dim("30px", src + " button-yellow horizontal padding"),
            "8": dim("32px", src + " auth card padding"),
            "9": dim("40px", src + " pricing-plan and testimonial padding"),
            "10": dim("48px", src + " auth submit horizontal padding and brown pad"),
            "11": dim("80px", src + " fixed nav height"),
            "12": dim("88px", src + " feature-block horizontal padding"),
            "13": dim("100px", src + " feature-block vertical padding"),
        },
        "motion": {
            "duration": {
                "hover": tok("duration", "150ms", src + " button-yellow::before opacity 0.15s ease-in"),
            },
            "easing": {
                "ease-in": tok("cubicBezier", [0.42, 0, 1, 1], src + " button-gray background 0.15s ease-in, keyword expanded"),
            },
        },
    }
    light = {
        "surface": {
            "page": color(c["page"], src + " body background"),
            "raised": color(c["surface"], src + " pricing-plan and auth card"),
            "inverse": color(c["brown"], src + " container-brown"),
        },
        "text": {
            "primary": color(c["text"], src + " body color"),
            "secondary": color(c["textDeep"], src + " hero subtitle and h2"),
            "onAccent": color(c["text"], src + " button-yellow color on #ecf956"),
            "placeholder": color(c["placeholder"], src + " login ::placeholder"),
        },
        "accent": color(c["accent"], src + " button-yellow background"),
        "border": {
            "default": color(c["text"], src + " button and nav border #482317"),
            "strong": color(c["textDeep"], src + " login field border #4c2116"),
        },
        "status": {
            "sky": color(c["sky"], src + " block-images"),
            "green": color(c["green"], src + " block-images"),
            "lilac": color(c["lilac"], src + " solutions pink scheme"),
        },
        "component": {
            "button": {
                "bg": color(c["accent"], src + " button-yellow background"),
                "text": color(c["text"], src + " button-yellow color"),
                "radius": dim("100px", src + " button-yellow border-radius"),
                "height": dim("39px", src + " home button-yellow height"),
                "padding": dim("30px", src + " button-yellow horizontal padding"),
            },
            "field": {
                "text": color(c["textDeep"], src + " login input color"),
                "radius": dim("0px", src + " login input border-radius"),
                "height": dim("44px", src + " login input height"),
                "padding": dim("12px", src + " login input horizontal padding"),
            },
        },
    }
    doc = {
        "$schema": "https://www.designtokens.org/schemas/2025.10/format/",
        "core": core,
        "light": light,
        "$themes": [
            {"name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
        ],
    }
    OUT.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    build()
