#!/usr/bin/env python3
"""Write raw/component-tokens.json, the spec build_tokens.py reads.

Overflow's public CSS declares one custom property, --swiper-theme-color
(#007aff), which the captured pages do not paint. Every other token is a
computed style read on 2026-11-21 from overflow.io at 1440x900 (phone menu
at 390x844). The site paints one light theme.
"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
C = json.loads((RAW / "components-computed.json").read_text())["components"]


def st(name, state="default"):
    return C[name]["states"][state]


def style(name, state="default"):
    return st(name, state).get("style") or {}


def paint_radius(name):
    paints = st(name).get("paint") or []
    for p in paints:
        if p.get("radius"):
            return p["radius"].split(" ")[0]
    return None


def color(name, prop="color", state="default"):
    return {
        "type": "color",
        "value": style(name, state)[prop],
        "source": f"computed {prop} of {name} {state} on overflow.io",
    }


def dim(name, prop, state="default"):
    return {
        "type": "dimension",
        "value": style(name, state)[prop],
        "source": f"computed {prop} of {name} {state} on overflow.io",
    }


SPEC = {
    "core": {
        "color": {
            "ink": color("nav-link"),
            "paper": color("product-menu", "backgroundColor"),
            "hero-ink": color("hero-title"),
            "ink-soft": color("menu-link"),
            "link": color("logo"),
            "link-hover": color("nav-link", "color", "hover"),
            "link-pressed": color("nav-link", "color", "pressed"),
            "muted": color("blog-card"),
            "grey": color("nav-signin", "backgroundColor", "pressed"),
            "grey-2": {"type": "color", "value": "rgb(240, 240, 242)", "source": "declared .btn-secondary background-color in public-site-homepage.min.css; the Sign In control computes transparent until :active"},
            "hairline": color("product-menu", "borderTopColor"),
            "chip-border": color("blog-card", "borderTopColor"),
            "swiper": {"type": "color", "value": "#007aff", "source": "css-var --swiper-theme-color on :root; the only custom property the homepage stylesheet declares. Not painted on the captured controls."},
            "theme": {"type": "color", "value": "#232D41", "source": "meta name=theme-color on https://overflow.io/"},
        },
        "font": {
            "family": {
                "sans": {"type": "fontFamily", "value": 'Inter, "Helvetica Neue", Arial, "Noto Sans", sans-serif', "source": "computed fontFamily of body, read on hero-title"},
                "mono": {"type": "fontFamily", "value": 'SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace', "source": "declared font-family in public-site-homepage.min.css; no code specimen was on the captured pages"},
                "icons": {"type": "fontFamily", "value": "icomoon", "source": "declared @font-face icomoon in public-site-homepage.min.css"},
            },
            "weight": {
                "regular": {"type": "fontWeight", "value": 400, "source": "computed fontWeight of nav-link default"},
                "medium": {"type": "fontWeight", "value": 500, "source": "computed fontWeight of logo"},
                "button": {"type": "fontWeight", "value": 550, "source": "computed fontWeight of hero-cta .btn-primary"},
                "bold": {"type": "fontWeight", "value": 700, "source": "computed fontWeight of m-nav-item"},
                "display": {"type": "fontWeight", "value": 800, "source": "computed fontWeight of hero-title"},
            },
        },
        "typography": {
            "display": {
                "type": "typography",
                "value": {"fontFamily": "{font.family.sans}", "fontSize": "56px", "fontWeight": "{font.weight.display}", "lineHeight": "63.84px", "letterSpacing": "-1.2px"},
                "source": "computed type of hero-title and pricing-h1 (.intro-section__title)",
            },
            "heading": {
                "type": "typography",
                "value": {"fontFamily": "{font.family.sans}", "fontSize": "48px", "fontWeight": "{font.weight.display}", "lineHeight": "55.68px", "letterSpacing": "-0.8px"},
                "source": "computed type of section-h2 (.headline-block__title)",
            },
            "nav": {
                "type": "typography",
                "value": {"fontFamily": "{font.family.sans}", "fontSize": "15px", "fontWeight": "{font.weight.regular}", "lineHeight": "26.25px", "letterSpacing": "0px"},
                "source": "computed type of nav-link default",
            },
            "body": {
                "type": "typography",
                "value": {"fontFamily": "{font.family.sans}", "fontSize": "16px", "fontWeight": "{font.weight.regular}", "lineHeight": "28px", "letterSpacing": "0px"},
                "source": "computed type of product-menu and faq-item",
            },
            "button": {
                "type": "typography",
                "value": {"fontFamily": "{font.family.sans}", "fontSize": "16px", "fontWeight": "{font.weight.button}", "lineHeight": "16px", "letterSpacing": "0.2px"},
                "source": "computed type of hero-cta",
            },
            "menu-item": {
                "type": "typography",
                "value": {"fontFamily": "{font.family.sans}", "fontSize": "14px", "fontWeight": "{font.weight.regular}", "lineHeight": "22px", "letterSpacing": "0px"},
                "source": "computed type of menu-link",
            },
            "phone-nav": {
                "type": "typography",
                "value": {"fontFamily": "{font.family.sans}", "fontSize": "24px", "fontWeight": "{font.weight.bold}", "lineHeight": "42px", "letterSpacing": "0px"},
                "source": "computed type of m-nav-item at 390x844",
            },
        },
        "radius": {
            "button": {"type": "dimension", "value": "8px", "source": "painted borderRadius of hero-cta .btn-primary"},
            "menu-link": {"type": "dimension", "value": "12px", "source": "painted borderRadius of menu-link"},
            "card": {"type": "dimension", "value": "24px", "source": "painted borderRadius of plan-card"},
            "chip": {"type": "dimension", "value": "20px", "source": "painted borderRadius of blog-card pill"},
        },
        "space": {
            "button-x": dim("hero-cta", "paddingLeft"),
            "button-y": dim("hero-cta", "paddingTop"),
            "nav-x": dim("nav-link", "paddingLeft"),
            "nav-y": dim("nav-link", "paddingTop"),
            "menu-x": dim("menu-link", "paddingLeft"),
            "menu-y": dim("menu-link", "paddingTop"),
            "faq-y": dim("faq-item", "paddingTop"),
        },
        "size": {
            "button-height": dim("hero-cta", "height"),
            "nav-button-height": dim("nav-cta", "height"),
            "nav-link-height": dim("nav-link", "height"),
            "menu-height": dim("product-menu", "height"),
            "menu-link-height": dim("menu-link", "height"),
            "logo-height": dim("logo", "height"),
            "faq-opener-height": dim("faq-item", "height"),
            "phone-toggle": dim("m-menu-button", "width"),
            "phone-nav-item": dim("m-nav-item", "height"),
        },
        "shadow": {
            "card": {
                "type": "shadow",
                "value": [{"offsetX": "0px", "offsetY": "4px", "blur": "16px", "spread": "-8px", "color": "rgba(0, 0, 0, 0.08)"}],
                "source": "computed boxShadow of plan-card",
            },
        },
        "motion": {
            "button": {"type": "duration", "value": "400ms", "source": "declared transition transform .4s on .btn-primary"},
            "link": {"type": "duration", "value": "350ms", "source": "computed transitionDuration of nav-link"},
            "menu": {"type": "duration", "value": "200ms", "source": "computed transitionDuration of product-menu"},
            "lift": {"type": "cubicBezier", "value": [0.3, 0.86, 0.36, 0.95], "source": "declared cubic-bezier(.3,.86,.36,.95) on .navbar-nav__subnav in public-site-homepage.min.css"},
        },
        "layout": {
            "desktop": {"type": "dimension", "value": "1440px", "source": "requested and measured window.innerWidth of the desktop captures"},
            "phone": {"type": "dimension", "value": "390px", "source": "requested phone viewport width"},
            "desktop-height": {"type": "dimension", "value": "900px", "source": "requested and measured window.innerHeight of the desktop captures"},
            "phone-height": {"type": "dimension", "value": "844px", "source": "requested phone viewport height"},
        },
    },
    "light": {
        "page": {"type": "color", "value": "{color.paper}", "source": "alias of computed product-menu and body background"},
        "surface": {"type": "color", "value": "{color.paper}", "source": "alias of plan-card background"},
        "text": {"type": "color", "value": "{color.ink}", "source": "alias of nav-link color"},
        "muted": {"type": "color", "value": "{color.muted}", "source": "alias of blog-card color"},
        "accent": {"type": "color", "value": "{color.link}", "source": "alias of logo color, the painted blue"},
        "border": {"type": "color", "value": "{color.hairline}", "source": "alias of product-menu borderTopColor"},
        "on-accent": {"type": "color", "value": "{color.hero-ink}", "source": "alias of hero-cta text, white on the black button"},
        "hero-text": {"type": "color", "value": "{color.hero-ink}", "source": "alias of hero-title color on the gradient"},
    },
    "component": {
        "button": {
            "background": color("hero-cta", "backgroundColor"),
            "text": color("hero-cta"),
            "radius": {"type": "dimension", "value": "{radius.button}", "source": "alias"},
            "height": {"type": "dimension", "value": "{size.button-height}", "source": "alias"},
            "padding": {"type": "dimension", "value": "{space.button-x}", "source": "alias of hero-cta paddingLeft"},
        },
        "nav-link": {
            "text": color("nav-link"),
            "hover": color("nav-link", "color", "hover"),
            "pressed": color("nav-link", "color", "pressed"),
        },
        "card": {
            "background": color("plan-card", "backgroundColor"),
            "radius": {"type": "dimension", "value": "{radius.card}", "source": "alias"},
        },
        "menu": {
            "background": color("product-menu", "backgroundColor"),
            "border": color("product-menu", "borderTopColor"),
            "height": {"type": "dimension", "value": "{size.menu-height}", "source": "alias"},
        },
    },
}

# typography composites are already DTCG-shaped; build_tokens expects spec leaves
# with type/value. Mark typography nodes so the builder can pass them through.
(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2) + "\n")
print("wrote", RAW / "component-tokens.json")
