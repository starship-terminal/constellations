#!/usr/bin/env python3
"""Build tokens.json from Raster's public signed-out readings.

Sources, read on 2026-11-19:
  raw/css-vars.json            custom properties on html.dark at raster.app
  raw/components-computed.json computed styles of the controls that were on screen
  raw/docs-computed.json       raster.app/docs, html.light

Marketing pages paint one dark theme (html.dark, color-scheme dark, body
rgb(0, 0, 0), root 14px). Docs paints a separate light surface. No light
marketing theme was on the page, so the docs surface is its own `docs` set
(not `light`: there is no light marketing theme to name), which the style
guide and the catalog entry read by that name.

Every value below was read. A role that was not on the page is absent.
Deterministic: same inputs, byte-identical output.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"


def C(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def D(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def N(value, source, typ="number"):
    return {"$value": value, "$type": typ, "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def typography(family, size, weight, line, tracking, source):
    return {
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
            "letterSpacing": tracking,
        },
        "$type": "typography",
        "$extensions": {"source": source},
    }


M = "Measured on raster.app, html.dark, 2026-11-19"
DOCS = "Measured on raster.app/docs, html.light, 2026-11-19"

tokens = {
    "core": {
        "color": {
            "brand": {
                "red": C("#ff2f66", f"{M}; --color-raster-red, computed rgb(255, 47, 102)"),
                "orange": C("#ff6a4d", f"{M}; --raster-gradient-orange"),
                "yellow": C("#ffc861", f"{M}; --raster-gradient-yellow"),
                "pink": C("#ff7ab8", f"{M}; --raster-gradient-pink"),
                "rose": C("#ff5fa4", f"{M}; --raster-gradient-rose"),
                "violet": C("#c66bff", f"{M}; --raster-gradient-violet"),
                "daisy-yellow": C("#ffb800", f"{M}; --color-daisy-yellow, computed rgb(255, 184, 0)"),
                "primary-inset": C("#ff5381", f"{M}; primary button inset shadow rgb(255, 83, 129)"),
            },
            "gray": {
                "50": C("#fafafa", f"{M}; --color-gray-50"),
                "100": C("#f4f4f5", f"{M}; --color-gray-100, published on /design"),
                "200": C("#e4e4e7", f"{M}; --color-gray-200, published on /design"),
                "300": C("#d4d4d8", f"{M}; --color-gray-300, published on /design"),
                "400": C("#a1a1aa", f"{M}; --color-gray-400, computed rgb(161, 161, 170)"),
                "500": C("#71717a", f"{M}; --color-gray-500, computed rgb(113, 113, 122); hero h1 color"),
                "600": C("#52525b", f"{M}; --color-gray-600, published on /design"),
                "700": C("#3f3f46", f"{M}; --color-gray-700, computed; tabs indicator and solid tag"),
                "800": C("#27272a", f"{M}; --color-gray-800, html background and --background"),
                "900": C("#18181b", f"{M}; --color-gray-900, tabs track and field face"),
                "950": C("#09090b", f"{M}; --color-gray-950"),
            },
            "neutral-50": C("#fafafa", f"{M}; --color-neutral-50 lab(98.26 0 0), hero body lines"),
            "white": C("#ffffff", f"{M}; --color-white / --foreground"),
            "black": C("#000000", f"{M}; --color-black, body background"),
            "docs": {
                "page": C("#f5f5f5", f"{DOCS}; body background rgb(245, 245, 245)"),
                "ink": C("#0a0a0a", f"{DOCS}; body and h1 rgb(10, 10, 10)"),
                "muted": C("#737373", f"{DOCS}; lede rgb(115, 115, 115)"),
                "card": C("#f1f1f1", f"{DOCS}; guide card rgb(241, 241, 241)"),
                "line": C("rgba(204, 204, 204, 0.5)", f"{DOCS}; card and search border"),
                "active": C("oklab(0.654023 0.231638 0.0531938 / 0.1)", f"{DOCS}; active sidebar row wash"),
            },
        },
        "font": {
            "family": {
                "display": font("\"Raster Neue\", sans-serif", f"{M}; --font-family-display; @font-face /site-assets/fonts/raster-neue.woff2, weight 100 900. Computed on the wordmark."),
                "sans": font("-apple-system, system-ui, \"Segoe UI\", Roboto, \"Helvetica Neue\", \"Noto Sans\", Arial, sans-serif", f"{M}; computed body font-family (html font-size 14px)"),
                "mono": font("ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, \"Liberation Mono\", \"Courier New\", monospace", f"{M}; --font-mono"),
                "docs": font("ui-sans-serif, system-ui, -apple-system, \"Segoe UI\", Roboto, \"Helvetica Neue\", Arial, sans-serif", f"{DOCS}; computed body font-family"),
            },
            "weight": {
                "light": N(300, f"{M}; --font-weight-light; body computed weight on header"),
                "normal": N(400, f"{M}; --font-weight-normal"),
                "medium": N(500, f"{M}; --font-weight-medium; buttons, nav, hero"),
                "semibold": N(600, f"{M}; --font-weight-semibold; pricing plan titles"),
                "bold": N(700, f"{M}; --font-weight-bold"),
            },
        },
        "typography": {
            "hero": typography("{font.family.sans}", "36px", "{font.weight.medium}", "39.6px", "-0.9px", f"{M}; h1 at 1440, text-[36px] leading-[1.1] tracking-[-0.025em]"),
            "hero-phone": typography("{font.family.sans}", "28px", "{font.weight.medium}", "1.1", "-0.025em", f"{M}; h1 class text-[28px] below md; phone innerWidth 390"),
            "section": typography("{font.family.sans}", "29px", "{font.weight.medium}", "31.9px", "-0.638px", f"{M}; home h2 md:text-[29px] leading-[1.1] tracking-[-0.022em]"),
            "lede": typography("{font.family.sans}", "18px", "{font.weight.medium}", "27px", "-0.09px", f"{M}; home paragraph md:text-[18px] leading-[1.5]"),
            "body": typography("{font.family.sans}", "15px", "{font.weight.medium}", "21px", "-0.075px", f"{M}; feature paragraph text-[15px] leading-[1.4]"),
            "nav": typography("{font.family.display}", "14px", "{font.weight.medium}", "21px", "0px", f"{M}; header .nav-link Raster Neue 14px/500"),
            "nav-sm": typography("{font.family.display}", "12.25px", "{font.weight.medium}", "17.5px", "0px", f"{M}; Sign in .text-sm, 0.875rem at the 14px root"),
            "button": typography("{font.family.sans}", "14px", "{font.weight.medium}", "21px", "0px", f"{M}; .button-primary on the hero"),
            "button-sm": typography("{font.family.sans}", "12.25px", "{font.weight.medium}", "17.5px", "0px", f"{M}; nav Start for free, text-sm"),
            "eyebrow": typography("{font.family.sans}", "13px", "{font.weight.medium}", "17.55px", "0px", f"{M}; Trusted by amazing teams, text-[13px] leading-[1.35]"),
            "plan": typography("{font.family.display}", "26.25px", "{font.weight.semibold}", "32px", "0px", f"{M}; pricing h2 .title.text-3xl, Raster Neue 600"),
            "price-band": typography("{font.family.sans}", "48px", "{font.weight.medium}", "50px", "-0.03em", f"{M}; Deploy once heading, md:text-[48px]"),
            "tag": typography("{font.family.sans}", "10.5px", "{font.weight.light}", "14px", "0px", f"{M}; .tag on /design"),
            "docs-title": typography("{font.family.display}", "28px", "{font.weight.semibold}", "42px", "0px", f"{DOCS}; h1 Raster Documentation"),
            "docs-lede": typography("{font.family.docs}", "18px", "{font.weight.normal}", "28px", "0px", f"{DOCS}; first paragraph, color rgb(115, 115, 115)"),
        },
        "radius": {
            "sm": D("3.5px", f"{M}; --radius-sm 0.25rem at the 14px root"),
            "md": D("5.25px", f"{M}; --radius-md 0.375rem; computed on .button, .input, .tag track"),
            "control": D("5.25px", f"{M}; .button and .input border-radius"),
            "tabs": D("7px", f"{M}; .tabs border-radius on /design"),
            "docs-row": D("8px", f"{DOCS}; search and active sidebar radius"),
            "docs-card": D("12px", f"{DOCS}; guide card radius"),
            "lg": D("7px", f"{M}; --radius-lg 0.5rem at the 14px root"),
            "xl": D("10.5px", f"{M}; --radius-xl 0.75rem at the 14px root"),
            "2xl": D("14px", f"{M}; --radius-2xl 1rem at the 14px root"),
            "pill": D("9999px", f"{M}; .tag border-radius computed as 1.67772e+07px, a pill"),
        },
        "spacing": {
            "unit": D("3.5px", f"{M}; --spacing 0.25rem at the 14px root"),
            "1": D("3.5px", f"{M}; 0.25rem"),
            "2": D("7px", f"{M}; 0.5rem; button padding-block"),
            "3": D("10.5px", f"{M}; 0.75rem; nav Start for free padding-inline, field padding-inline"),
            "4": D("14px", f"{M}; 1rem"),
            "5": D("17.5px", f"{M}; 1.25rem; nav link padding-inline"),
            "8": D("28px", f"{M}; 2rem; hero .button-primary padding-inline"),
            "nav-height": D("53px", f"{M}; header.navbar height, fixed"),
            "button-height": D("37px", f"{M}; hero .button-primary and sign-in buttons"),
            "button-sm-height": D("27px", f"{M}; nav Start for free and Book demo"),
            "field-height": D("37px", f"{M}; .input on /design and the sign-in email field"),
        },
        "motion": {
            "duration": {
                "fast": N("150ms", f"{M}; --default-transition-duration 0.15s", "duration"),
                "fade": N("200ms", f"{M}; --animate-fade-in 0.2s", "duration"),
                "slide": N("300ms", f"{M}; --animate-slide-up and --stageFoldDuration 0.3s", "duration"),
                "sidebar": N("460ms", f"{M}; --sidebarDuration 0.46s", "duration"),
                "editor": N("500ms", f"{M}; --editorDuration 0.5s", "duration"),
                "reveal": N("1200ms", f"{M}; --animate-reveal 1.2s", "duration"),
            },
            "easing": {
                "standard": N([0.4, 0, 0.2, 1], f"{M}; --default-transition-timing-function", "cubicBezier"),
                "out": N([0, 0, 0.2, 1], f"{M}; --ease-out", "cubicBezier"),
                "sidebar": N([0.32, 0.72, 0, 1], f"{M}; --sidebarEase and --assistantEase", "cubicBezier"),
                "slide": N([0.33, 1, 0.68, 1], f"{M}; --animate-slide-up", "cubicBezier"),
                "editor": N([0.8, 0, 0.2, 1], f"{M}; --editorEase", "cubicBezier"),
            },
        },
    },
    "dark": {
        "background": {
            "page": C("{color.black}", f"{M}; body background-color rgb(0, 0, 0)"),
            "canvas": C("{color.gray.800}", f"{M}; html background-color rgb(39, 39, 42), --background"),
            "nav": C("rgba(0, 0, 0, 0.5)", f"{M}; header.navbar background"),
            "field": C("{color.gray.900}", f"{M}; .input on /design, rgb(39, 39, 42) was the sign-in field's dark:bg-black/20 parent; design input computed rgb(39, 39, 42) on a zinc page and rgb(24, 24, 27) is the tabs track"),
            "tabs": C("{color.gray.900}", f"{M}; .tabs background rgb(24, 24, 27)"),
            "indicator": C("{color.gray.700}", f"{M}; .tab-indicator rgb(63, 63, 70)"),
            "tag-solid": C("{color.gray.700}", f"{M}; .tag.tag-solid"),
            "glass": C("oklab(0.210329 0.00161358 -0.00563219 / 0.7)", f"{M}; .glass on /design"),
            "secondary": C("oklab(0.999994 0.0000455678 0.0000200868 / 0.08)", f"{M}; .button-secondary and Book demo"),
            "action": C("{color.brand.red}", f"{M}; .button-primary"),
        },
        "text": {
            "primary": C("{color.white}", f"{M}; body color and nav links"),
            "hero": C("{color.neutral-50}", f"{M}; hero lines .text-neutral-50, lab(98.26 0 0)"),
            "muted": C("{color.gray.500}", f"{M}; h1 computed rgb(113, 113, 122); footer"),
            "faint": C("oklab(0.984998 -0.00000956655 0.0000230074 / 0.38)", f"{M}; Trusted by amazing teams"),
            "soft": C("oklab(0.984998 -0.00000956655 0.0000230074 / 0.58)", f"{M}; home lede text-neutral-50/58"),
            "tag": C("{color.gray.400}", f"{M}; .tag.tag-outline"),
            "tag-solid": C("#d4d4d8", f"{M}; .tag.tag-solid color rgb(212, 212, 216)"),
            "on-action": C("{color.white}", f"{M}; .button-primary color"),
        },
        "border": {
            "hairline": C("oklab(0.999994 0.0000455678 0.0000200868 / 0.15)", f"{M}; .button-secondary border"),
            "action": C("oklab(0.999994 0.0000455678 0.0000200868 / 0.18)", f"{M}; .button-primary border"),
            "field": C("oklab(0.999994 0.0000455678 0.0000200868 / 0.1)", f"{M}; .input and sign-in email border"),
            "tabs": C("rgba(255, 255, 255, 0.08)", f"{M}; .tabs border"),
            "tag": C("oklab(0.71181 0.00361261 -0.0124171 / 0.2)", f"{M}; .tag.tag-outline border"),
        },
        "focus": {
            "ring": C("#99c8ff", f"{M}; focused Get started outline rgb(153, 200, 255) auto 1px, offset 1px. Browser default, not a product token."),
        },
        "component": {
            "button": {
                "background": C("{background.action}", f"{M}; .button-primary"),
                "text": C("{text.on-action}", f"{M}; .button-primary"),
                "radius": D("{radius.control}", f"{M}; .button-primary"),
                "padding": D("7px", f"{M}; padding-block; padding-inline is 28px on the hero button"),
                "height": D("{spacing.button-height}", f"{M}; hero button"),
            },
            "field": {
                "background": C("{color.gray.800}", f"{M}; .input on /design computed rgb(39, 39, 42)"),
                "text": C("{text.primary}", f"{M}; .input color"),
                "radius": D("{radius.control}", f"{M}; .input"),
                "height": D("{spacing.field-height}", f"{M}; .input"),
            },
        },
    },
}

# The docs set goes after $themes and $metadata, where the committed tokens.json has it.
DOCS_SET = {
    "background": {
        "page": C("{color.docs.page}", f"{DOCS}; the only light surface captured"),
        "surface": C("{color.docs.card}", f"{DOCS}; guide card"),
        "active": C("{color.docs.active}", f"{DOCS}; sidebar current row"),
    },
    "text": {
        "primary": C("{color.docs.ink}", DOCS),
        "muted": C("{color.docs.muted}", DOCS),
        "accent": C("{color.brand.red}", f"{DOCS}; current sidebar label and On this page links"),
    },
    "border": {
        "default": C("{color.docs.line}", DOCS),
    },
}

tokens.update({
    "$themes": [
        {
            "id": "dark",
            "name": "Dark",
            "selectedTokenSets": {"core": "source", "dark": "enabled"},
            "$description": "The marketing theme. html.dark, color-scheme dark, black page, zinc canvas, Raster Red actions.",
        },
        {
            "id": "docs",
            "name": "Docs",
            "selectedTokenSets": {"core": "source", "docs": "enabled"},
            "$description": "Docs only. raster.app/docs sets html.light. The marketing site had no light theme.",
        },
    ],
    "$metadata": {"tokenSetOrder": ["core", "dark", "docs"]},
    "docs": DOCS_SET,
})

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", HERE / "tokens.json")
