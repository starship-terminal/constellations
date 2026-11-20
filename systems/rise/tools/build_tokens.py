#!/usr/bin/env python3
"""Build tokens.json from the Rise public-site readings.

Values were read on 2026-11-19 from https://risecalendar.com/ (stylesheet
ec71784565c9a205.css, :root custom properties) and from computed styles on
the live pages. Rise publishes one theme. There is no dark set.

A colour token is the RGB triplet Rise declares, written as #rrggbb.
A size token is the computed px length (16px root, so 1rem is 16px).
Every token carries $extensions.source. Deterministic.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"

# :root custom properties, stylesheet ec71784565c9a205.css, confirmed by
# getComputedStyle on body, links, cards and buttons.
ROOT = {
    "foreground": (30, 42, 41),
    "background": (252, 252, 254),
    "surface": (247, 247, 252),
    "sidebar": (248, 249, 253),
    "input": (241, 242, 248),
    "border": (214, 217, 228),
    "offset-text": (183, 187, 205),
    "offset-dark": (108, 111, 125),
    "primary": (113, 97, 236),
    "negative": (255, 42, 90),
    "warning": (255, 193, 65),
    "success": (25, 190, 47),
    "system-black": (0, 0, 0),
    "system-white": (255, 255, 255),
    "system-blue": (0, 0, 238),
    "dolphin": (100, 127, 160),
    "blue": (1, 115, 240),
    "violet": (105, 70, 228),
    "pink": (228, 63, 255),
    "orange": (255, 106, 1),
    "yellow": (255, 179, 1),
    "turquoise": (19, 177, 168),
    "green": (16, 180, 38),
}

# Wordmark gradient stops, read from the header SVG on the live page.
LOGO = {
    "mark-bottom-0": "#767df9",
    "mark-bottom-1": "#7161ec",
    "mark-bottom-2": "#5730e3",
    "mark-top-0": "#ff7557",
    "mark-top-1": "#ffaf66",
}

SRC_ROOT = "Measured. :root in https://risecalendar.com/_next/static/css/ec71784565c9a205.css, 2026-11-19."
SRC_COMPUTED = "Measured. getComputedStyle on the live public page, 2026-11-19."
SRC_UTILITY = "Measured. Tailwind utility in the same stylesheet, confirmed by a computed style."
SRC_DERIVED = "Derived. 1rem is 16px on the measured root, so the utility rem converts to this px length."
# A value no file in raw/ holds: typed in from the capture session (docs/EVIDENCE.md, Reconstruction).
SRC_HAND = "Reconstruction. Entered by hand at capture time; no file in raw/ holds this reading."


def hex_of(rgb):
    return "#%02x%02x%02x" % rgb


def color(value, source, description=None):
    token = {"$type": "color", "$value": value, "$extensions": {"source": source}}
    if description:
        token["$description"] = description
    return token


def dim(value, source, description=None):
    token = {"$type": "dimension", "$value": value, "$extensions": {"source": source}}
    if description:
        token["$description"] = description
    return token


def number(value, source):
    return {"$type": "number", "$value": value, "$extensions": {"source": source}}


def font_family(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def font_weight(value, source):
    return {"$type": "fontWeight", "$value": value, "$extensions": {"source": source}}


def cubic(value, source):
    return {"$type": "cubicBezier", "$value": value, "$extensions": {"source": source}}


def duration(value, source):
    return {"$type": "duration", "$value": value, "$extensions": {"source": source}}


def shadow(value, source):
    return {"$type": "shadow", "$value": value, "$extensions": {"source": source}}


def typography(value, source):
    return {"$type": "typography", "$value": value, "$extensions": {"source": source}}


def core():
    family = font_family(
        "Inter, ui-sans-serif, system-ui, sans-serif",
        SRC_COMPUTED + " Computed font-family is __Inter_9d3317 (next/font Inter) with __Inter_Fallback_9d3317. The token names Inter, which the @font-face files are.",
    )
    return {
        "font": {
            "family": {"sans": family},
            "weight": {
                "regular": font_weight(400, SRC_COMPUTED + " Body text."),
                "medium": font_weight(500, SRC_COMPUTED + " Pricing buttons and feature values."),
                "semibold": font_weight(600, SRC_COMPUTED + " Inline links, section headings, badges."),
                "bold": font_weight(700, SRC_COMPUTED + " Page titles."),
            },
        },
        "typography": {
            "display": typography(
                {"fontFamily": "{font.family.sans}", "fontWeight": "{font.weight.bold}",
                 "fontSize": "48px", "lineHeight": "48px", "letterSpacing": "-2.4px"},
                SRC_COMPUTED + " h2.text-3xl.md:text-5xl.tracking-tighter.font-bold at 1440px (Sunsetting Rise).",
            ),
            "display-phone": typography(
                {"fontFamily": "{font.family.sans}", "fontWeight": "{font.weight.bold}",
                 "fontSize": "30px", "lineHeight": "36px", "letterSpacing": "-1.5px"},
                SRC_COMPUTED + " The same heading at innerWidth 390 (text-3xl).",
            ),
            "title": typography(
                {"fontFamily": "{font.family.sans}", "fontWeight": "{font.weight.bold}",
                 "fontSize": "36px", "lineHeight": "40px", "letterSpacing": "-1.8px"},
                SRC_COMPUTED + " Pricing and Blog h2.text-3xl.md:text-4xl at 1440px.",
            ),
            "hero": typography(
                {"fontFamily": "{font.family.sans}", "fontWeight": "{font.weight.bold}",
                 "fontSize": "56px", "lineHeight": "56px", "letterSpacing": "-2.8px"},
                SRC_COMPUTED + " Comparison-page h1.md:text-[3.5rem] at 1440px.",
            ),
            "heading": typography(
                {"fontFamily": "{font.family.sans}", "fontWeight": "{font.weight.semibold}",
                 "fontSize": "24px", "lineHeight": "32px", "letterSpacing": "0px"},
                SRC_COMPUTED + " Article h2.text-2xl.font-semibold.",
            ),
            "subheading": typography(
                {"fontFamily": "{font.family.sans}", "fontWeight": "{font.weight.semibold}",
                 "fontSize": "20px", "lineHeight": "28px", "letterSpacing": "0px"},
                SRC_COMPUTED + " Comparison h3.text-xl.font-semibold.",
            ),
            "lede": typography(
                {"fontFamily": "{font.family.sans}", "fontWeight": "{font.weight.regular}",
                 "fontSize": "20px", "lineHeight": "28px", "letterSpacing": "0px"},
                SRC_COMPUTED + " Home dek p.text-base.md:text-xl at 1440px.",
            ),
            "body": typography(
                {"fontFamily": "{font.family.sans}", "fontWeight": "{font.weight.regular}",
                 "fontSize": "16px", "lineHeight": "28px", "letterSpacing": "0px"},
                SRC_COMPUTED + " Article p.text-base.leading-7.",
            ),
            "ui": typography(
                {"fontFamily": "{font.family.sans}", "fontWeight": "{font.weight.medium}",
                 "fontSize": "14px", "lineHeight": "16px", "letterSpacing": "0px"},
                SRC_COMPUTED + " Pricing buttons, text-sm leading-4 font-medium.",
            ),
            "feature": typography(
                {"fontFamily": "{font.family.sans}", "fontWeight": "{font.weight.regular}",
                 "fontSize": "14px", "lineHeight": "20px", "letterSpacing": "0px"},
                SRC_COMPUTED + " Pricing list rows, text-sm.",
            ),
            "caption": typography(
                {"fontFamily": "{font.family.sans}", "fontWeight": "{font.weight.medium}",
                 "fontSize": "12px", "lineHeight": "16px", "letterSpacing": "0px"},
                SRC_COMPUTED + " text-xs. The -20% chip is font-weight 600.",
            ),
            "eyebrow": typography(
                {"fontFamily": "{font.family.sans}", "fontWeight": "{font.weight.semibold}",
                 "fontSize": "10px", "lineHeight": "15px", "letterSpacing": "0.5px"},
                SRC_COMPUTED + " .text-xxxs is 0.625rem. Badges are uppercase, tracking-wider (0.05em = 0.5px at 10px).",
            ),
        },
        "space": {
            "1": dim("2px", SRC_DERIVED + " p-0.5 on the switch track."),
            "2": dim("4px", SRC_DERIVED + " px-1 on the discount chip."),
            "3": dim("6px", SRC_DERIVED + " gap-x-1.5 / gap-y-1.5."),
            "4": dim("8px", SRC_COMPUTED + " Badge padding-inline and button padding-block."),
            "5": dim("12px", SRC_DERIVED + " mb-3."),
            "6": dim("16px", SRC_COMPUTED + " Button padding-inline (px-4) and article paragraph margin."),
            "7": dim("20px", SRC_COMPUTED + " Article padding-inline (px-5) and card row-gap (gap-y-5)."),
            "8": dim("24px", SRC_DERIVED + " Hero gap-y-6, my-6 divider margin, px-6 on the large button."),
            "9": dim("32px", SRC_DERIVED + " Section heading margin-top (mt-8)."),
            "10": dim("36px", SRC_COMPUTED + " Pricing card padding (p-9 = 2.25rem)."),
            "11": dim("80px", SRC_COMPUTED + " Article padding-block (py-20) and sticky header height."),
        },
        "radius": {
            "sm": dim("2px", SRC_DERIVED + " .rounded-sm is 0.125rem. Discount chip."),
            "md": dim("4px", SRC_COMPUTED + " .rounded is 0.25rem. Buttons, badges, logo link."),
            "lg": dim("6px", SRC_DERIVED + " .rounded-md is 0.375rem. Pricing cards."),
            "xl": dim("8px", SRC_DERIVED + " .rounded-lg is 0.5rem. Article images."),
            "full": dim("9999px", SRC_COMPUTED + " Switch track and thumb."),
        },
        "motion": {
            "duration": {
                "fast": duration("150ms", SRC_HAND + " .transition-all duration is 0.15s."),
                "enter": duration("150ms", SRC_HAND + " data-state=open animate-in is 0.15s. No open element was on the public pages."),
                "dialog": duration("300ms", SRC_HAND + " data-state=open duration-300 is 0.3s. Declared, not shown on a public page."),
            },
            "easing": {
                "standard": cubic(
                    [0.4, 0, 0.2, 1],
                    SRC_UTILITY + " .transition-all timing-function cubic-bezier(0.4, 0, 0.2, 1).",
                ),
            },
        },
        "size": {
            "button-sm": dim("34px", SRC_COMPUTED + " Pricing Get Started and Upgrade."),
            "button-lg": dim("46px", SRC_COMPUTED + " Comparison Get started, text-lg px-6 py-2."),
            "switch-track": dim("32px", SRC_COMPUTED + " Annual-billing track width. Height is 16px. raw/switch.json and raw/switch-on.json, w 32."),
            "switch-thumb": dim("12px", SRC_COMPUTED + " Switch thumb width and height. raw/switch.json and raw/switch-on.json, w 12, h 12."),
            "header": dim("80px", SRC_COMPUTED + " Sticky header, including 28px padding-block."),
            "logo": dim("76px", SRC_COMPUTED + " Wordmark SVG width. Height is 24px."),
            "content": dim("768px", SRC_UTILITY + " .max-w-screen-md, the article column."),
            "hero": dim("1024px", SRC_UTILITY + " .max-w-screen-lg, the comparison hero."),
            "nav": dim("1280px", SRC_HAND + " .max-w-screen-xl, the header row."),
            "card": dim("480px", SRC_COMPUTED + " Pricing card width at 1440px."),
        },
        "border": {
            "width": dim("1px", SRC_COMPUTED + " Buttons, cards, badges and the pricing rule."),
        },
        "shadow": {
            "sm": shadow(
                {"color": "rgba(0, 0, 0, 0.05)", "offsetX": "0px", "offsetY": "1px", "blur": "2px", "spread": "0px"},
                SRC_COMPUTED + " Teams card, .shadow-sm.",
            ),
        },
    }


def light():
    source = SRC_ROOT
    colors = {name: color(hex_of(rgb), source, f"--{name}: {','.join(str(c) for c in rgb)}") for name, rgb in ROOT.items()}
    colors["logo"] = {name: color(value, SRC_COMPUTED + " Header SVG linearGradient stop.", name) for name, value in LOGO.items()}
    return {
        "color": colors,
        "background": {
            "page": color("#ffffff", SRC_COMPUTED + " body background-color. The page paints white over --background."),
            "canvas": color("{color.background}", source + " --background, used by the date badge and the Solo card."),
            "surface": color("{color.surface}", source),
            "input": color("{color.input}", source + " Image placeholder and the outline-button hover."),
            "sidebar": color("{color.sidebar}", source + " Declared. No sidebar is on the public pages."),
            "primary": color("{color.primary}", source),
            "primary-hover": color("rgba(113, 97, 236, 0.8)", SRC_COMPUTED + " Upgrade hovered. .hover:bg-primary/80."),
            "primary-soft": color("rgba(113, 97, 236, 0.1)", SRC_HAND + " .bg-primary/10 on the Free for personal use chip."),
            "white": color("{color.system-white}", source),
            "switch-off": color("rgba(108, 111, 125, 0.6)", SRC_COMPUTED + " .bg-offset-dark/60 on the billing switch, off."),
        },
        "text": {
            "primary": color("{color.foreground}", SRC_COMPUTED + " body color rgb(30, 42, 41)."),
            "body": color("rgba(30, 42, 41, 0.8)", SRC_COMPUTED + " Article paragraphs, .text-foreground/80."),
            "secondary": color("{color.offset-dark}", SRC_COMPUTED + " Dek, feature labels, pricing subtitle."),
            "muted": color("{color.offset-text}", source + " Declared --offset-text. Not used as a text colour on the pages measured."),
            "link": color("{color.primary}", SRC_COMPUTED + " Inline links, text-primary font-semibold."),
            "on-primary": color("{color.system-white}", SRC_COMPUTED + " Primary button label."),
            "inverse": color("{color.system-white}", source),
        },
        "border": {
            "default": color("{color.border}", SRC_COMPUTED + " Header rule, badges, outline button, Teams card."),
            "quiet": color("rgba(214, 217, 228, 0.5)", SRC_HAND + " Solo card, .border-border/50."),
            "image": color("rgba(30, 42, 41, 0.05)", SRC_HAND + " Article images, .border-foreground/5."),
        },
        "component": {
            "button-primary-bg": color("{color.primary}", SRC_COMPUTED + " Upgrade default."),
            "button-primary-text": color("{color.system-white}", SRC_COMPUTED),
            "button-primary-radius": dim("4px", SRC_COMPUTED),
            "button-primary-padding": dim("8px", SRC_COMPUTED + " Block padding. Inline padding is 16px."),
            "button-secondary-bg": color("{color.system-white}", SRC_COMPUTED + " Get Started default."),
            "button-secondary-text": color("{color.foreground}", SRC_COMPUTED),
            "button-secondary-radius": dim("4px", SRC_COMPUTED),
            "card-bg": color("{color.background}", SRC_COMPUTED + " Solo card."),
            "card-radius": dim("6px", SRC_COMPUTED),
            "card-padding": dim("36px", SRC_COMPUTED),
            "badge-bg": color("{color.background}", SRC_COMPUTED + " Date badge. The category badge background computed transparent."),
            "badge-text": color("{color.offset-dark}", SRC_COMPUTED),
            "badge-radius": dim("4px", SRC_COMPUTED),
        },
    }


def build():
    doc = {
        "$description": "Rise public marketing site, measured 2026-11-19. One theme. The signed-in app was already shut down.",
        "core": core(),
        "light": light(),
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        ],
    }
    return doc


def write():
    text = json.dumps(build(), indent=2) + "\n"
    (HERE / "tokens.json").write_text(text)
    print("tokens.json", len(text.encode()), "bytes")


if __name__ == "__main__":
    write()
