#!/usr/bin/env python3
"""Write tokens.json from raw/foundations.json.

Values were read with getComputedStyle on slack.com on 2026-11-19. This
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


def dim(value, source):
    return tok("dimension", value, source)


def build():
    src = RAW["source"]
    c = RAW["colors"]
    fonts = RAW["fonts"]
    brand = {k: color(v, src + " --dt_color-brand-core-" + k.replace("_", "-"))
             for k, v in c["brand"].items()}
    semantic = {k: color(v, src + " Slack Kit " + k)
                for k, v in c["semantic"].items()}
    marketing = {k: color(v, src + " marketing computed " + k)
                 for k, v in c["marketing"].items()}
    core = {
        "color": {
            "brand": brand,
            "semantic": semantic,
            "marketing": marketing,
        },
        "font": {
            "family": {
                "marketingHeading": tok("fontFamily", fonts["marketingHeading"], src + " --font-family-heading"),
                "marketingBody": tok("fontFamily", fonts["marketingBody"], src + " --font-family-body"),
                "authBody": tok("fontFamily", fonts["authBody"], src + " sign-in body font-family"),
                "mono": tok("fontFamily", fonts["mono"], src + " --font-family-monospace"),
            },
            "weight": {
                "regular": tok("fontWeight", 400, src + " body font-weight"),
                "semibold": tok("fontWeight", 600, src + " pricing strike and badge font-weight"),
                "bold": tok("fontWeight", 700, src + " button and h1 font-weight"),
            },
            "size": {
                "badge": dim("10px", src + " pricing promo pill font-size"),
                "button": dim("14px", src + " marketing .c-button font-size"),
                "nav": dim("15px", src + " nav trigger and sign-in body font-size"),
                "body": dim("16px", src + " marketing body font-size"),
                "lede": dim("18px", src + " home lede and sign-in subhead font-size"),
                "authButton": dim("18px", src + " sign-in button font-size"),
                "pricingLede": dim("20px", src + " pricing .c-type-paragraph-hero font-size"),
                "price": dim("28px", src + " pricing .plan-free-price font-size"),
                "heroPhone": dim("32px", src + " home h1 at 390px"),
                "hero": dim("48px", src + " home h1 and sign-in h1 at 1169px"),
                "section": dim("50px", src + " home h2 and pricing h1 at 1169px"),
            },
        },
        "typography": {
            "hero": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["marketingHeading"],
                    "fontSize": "48px",
                    "fontWeight": 700,
                    "lineHeight": "53.76px",
                    "letterSpacing": "-0.576px",
                },
                "$extensions": {"source": src + " home h1 at 1169px"},
            },
            "heroPhone": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["marketingHeading"],
                    "fontSize": "32px",
                    "fontWeight": 700,
                    "lineHeight": "35.84px",
                    "letterSpacing": "-0.384px",
                },
                "$extensions": {"source": src + " home h1 at 390px"},
            },
            "section": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["marketingHeading"],
                    "fontSize": "50px",
                    "fontWeight": 600,
                    "lineHeight": "56px",
                    "letterSpacing": "-0.6px",
                },
                "$extensions": {"source": src + " home h2 .c-dark-ai-headline at 1169px"},
            },
            "authHeading": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["marketingHeading"],
                    "fontSize": "48px",
                    "fontWeight": 700,
                    "lineHeight": "46px",
                    "letterSpacing": "-0.75px",
                },
                "$extensions": {"source": src + " sign-in h1"},
            },
            "lede": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["marketingBody"],
                    "fontSize": "18px",
                    "fontWeight": 400,
                    "lineHeight": "27.99px",
                    "letterSpacing": "-0.0216px",
                },
                "$extensions": {"source": src + " home .c-billboard__subhead"},
            },
            "body": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["marketingBody"],
                    "fontSize": "16px",
                    "fontWeight": 400,
                    "lineHeight": "normal",
                    "letterSpacing": "normal",
                },
                "$extensions": {"source": src + " marketing body"},
            },
            "button": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["marketingBody"],
                    "fontSize": "14px",
                    "fontWeight": 700,
                    "lineHeight": "18.004px",
                    "letterSpacing": "0.798px",
                },
                "$extensions": {"source": src + " marketing .c-button.v--primary"},
            },
            "authButton": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["authBody"],
                    "fontSize": "18px",
                    "fontWeight": 700,
                    "lineHeight": "normal",
                    "letterSpacing": "normal",
                },
                "$extensions": {"source": src + " sign-in submit"},
            },
        },
        "radius": {
            "none": dim("0px", src + " --dt_static_radius-none"),
            "small": dim("2px", src + " --dt_static_radius-small"),
            "base": dim("4px", src + " marketing button border-radius and --dt_static_radius-base"),
            "large": dim("8px", src + " --dt_static_radius-large"),
            "xlarge": dim("12px", src + " sign-in field and button border-radius, pricing column radius"),
            "pill": dim("20px", src + " pricing .promo-pill-text border-radius"),
            "rounded": dim("9999px", src + " --dt_static_radius-rounded"),
        },
        "spacing": {
            "0": dim("0px", src + " --dt_static_space-0"),
            "px": dim("1px", src + " --dt_static_space-px"),
            "0125": dim("2px", src + " --dt_static_space-0125"),
            "025": dim("4px", src + " --dt_static_space-025"),
            "050": dim("8px", src + " --dt_static_space-050"),
            "075": dim("12px", src + " --dt_static_space-075"),
            "100": dim("16px", src + " --dt_static_space-100"),
            "125": dim("20px", src + " --dt_static_space-125"),
            "150": dim("24px", src + " --dt_static_space-150"),
            "200": dim("32px", src + " --dt_static_space-200"),
            "250": dim("40px", src + " --dt_static_space-250"),
            "300": dim("48px", src + " --dt_static_space-300"),
        },
        "shadow": {
            "sm": tok("shadow", RAW["shadows"]["sm"], src + " --dt_static_shadow-sm"),
            "base": tok("shadow", RAW["shadows"]["base"], src + " --dt_static_shadow-base"),
            "md": tok("shadow", RAW["shadows"]["md"], src + " --dt_static_shadow-md"),
            "lg": tok("shadow", RAW["shadows"]["lg"], src + " --dt_static_shadow-lg"),
            "pricing": tok("shadow", RAW["shadows"]["pricing"], src + " featured pricing column box-shadow"),
            "focus": tok("shadow", RAW["shadows"]["focus"], src + " sign-in email field box-shadow"),
        },
        "motion": {
            "duration160": tok("duration", "160ms", src + " --dt_static_transition-duration-160 0.16s"),
            "duration200": tok("duration", "200ms", src + " --dt_static_transition-duration-200 0.2s"),
            "duration80": tok("duration", "80ms", src + " --dt_static_transition-duration-80"),
            "easeDefault": tok("cubicBezier", [0.36, 0.19, 0.29, 1], src + " --dt_static_transition-ease-default"),
        },
    }
    light = {
        "color": {
            "bg": {
                "page": color(c["page"], src + " html background-color on marketing"),
                "surface": color(c["surface"], src + " sign-in .get-started-app-root background"),
                "aubergine": color(c["marketing"]["aubergine"], src + " .c-dark-ai-container background"),
                "nav": color(c["nav"], src + " .c-nav background, transparent over the page"),
            },
            "text": {
                "primary": color(c["text"], src + " sign-in body and --dt_color-content-pry"),
                "secondary": color(c["muted"], src + " --dt_color-content-sec and sign-in subhead"),
                "legal": color(c["legal"], src + " sign-in footer link color"),
                "onAubergine": color("#ffffff", src + " home h2 color on aubergine"),
                "onPrimary": color("#ffffff", src + " marketing primary button color"),
            },
            "accent": color(c["accent"], src + " marketing .c-button.v--primary background"),
            "border": color(c["border"], src + " pricing column border-color"),
            "focus": color(c["focus"], src + " sign-in link color and field focus ring"),
            "component": {
                "button": {
                    "bg": color(c["accent"], src + " marketing primary button background"),
                    "text": color("#ffffff", src + " marketing primary button color"),
                    "radius": dim("4px", src + " marketing button border-radius"),
                    "padding": dim("12px", src + " marketing button padding-top"),
                    "height": dim("42px", src + " header GET STARTED height at 1169px"),
                },
                "field": {
                    "bg": color("#ffffff", src + " sign-in email field background"),
                    "text": color(c["text"], src + " sign-in email field color"),
                    "radius": dim("12px", src + " sign-in email field border-radius"),
                    "padding": dim("12px", src + " sign-in email field padding"),
                    "height": dim("44px", src + " sign-in email field height"),
                },
            },
        }
    }
    return {
        "$schema": "https://www.designtokens.org/schemas/2025.10/format/",
        "core": core,
        "light": light,
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}
        ],
    }


def main():
    data = build()
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
