#!/usr/bin/env python3
"""Build tokens.json from the 2026-11-19 Teal readings.

Marketing colours are declared custom properties on www.tealhq.com, confirmed
by computed styles on the live home, pricing and resume-checker pages. App
colours are computed styles and declared custom properties on
app.tealhq.com/sign-in, which loaded signed out. Nothing here is invented.
A role that was not on those pages is omitted.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent

SRC_M = (
    "Measured. Declared custom property on www.tealhq.com, read from "
    "getComputedStyle(document.documentElement) on 2026-11-19."
)
SRC_APP = (
    "Measured. Declared custom property on https://app.tealhq.com/sign-in, "
    "read from getComputedStyle(document.documentElement) on 2026-11-19. "
    "The public marketing pages do not mount this sheet."
)


def color(value: str, source: str) -> dict:
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value: str, source: str) -> dict:
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def font(value: str, source: str) -> dict:
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def weight(value: str, source: str) -> dict:
    return {"$value": value, "$type": "fontWeight", "$extensions": {"source": source}}


def number(value: str, source: str) -> dict:
    return {"$value": value, "$type": "number", "$extensions": {"source": source}}


def text(value: str, source: str) -> dict:
    return {"$value": value, "$type": "other", "$extensions": {"source": source}}


def cubic(value: list, source: str) -> dict:
    return {"$value": value, "$type": "cubicBezier", "$extensions": {"source": source}}


def shadow(value: str, source: str) -> dict:
    return {"$value": value, "$type": "shadow", "$extensions": {"source": source}}


def duration(value: str, source: str) -> dict:
    return {"$value": value, "$type": "duration", "$extensions": {"source": source}}


def comp(where: str) -> str:
    return (
        f"Measured. Computed style on {where}, 2026-11-19. "
        "Marketing pages were read at innerWidth 1169, innerHeight 731, devicePixelRatio 2."
    )


def app_comp(where: str) -> str:
    return (
        f"Measured. Computed style on {where} at https://app.tealhq.com/sign-in, "
        "2026-11-19, innerWidth 1169, innerHeight 731, devicePixelRatio 2. "
        "Fields were left empty and the form was not submitted."
    )


tokens = {
    "$schema": "https://design-tokens.org/schema.json",
    "core": {
        "font": {
            "marketing": font(
                "Roobert, sans-serif",
                comp("document.body on https://www.tealhq.com/"),
            ),
            "marketingNav": font(
                "Roobert, Poppins, sans-serif",
                comp("header nav links on https://www.tealhq.com/"),
            ),
            "app": font(
                "Inter, system-ui, sans-serif",
                app_comp("document.body"),
            ),
            "mono": font(
                'ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace',
                SRC_M + " Token --font-mono. Not the computed face of body text.",
            ),
        },
        "fontWeight": {
            "light": weight("300", SRC_M + " Token --font-weight-light."),
            "regular": weight("400", SRC_M + " Token --font-weight-normal. Body copy."),
            "medium": weight("500", SRC_M + " Token --font-weight-medium. Header Sign up."),
            "semibold": weight("600", SRC_M + " Token --font-weight-semibold. Headings and yellow CTAs."),
            "bold": weight("700", SRC_M + " Token --font-weight-bold. Declared, not the computed weight of the measured headings."),
        },
        "fontSize": {
            "body": dim("16px", comp("document.body on the home page")),
            "appBody": dim("14px", app_comp("document.body")),
            "nav": dim("16px", comp("header nav link Job Tracker")),
            "headerButton": dim("15px", comp("header Sign up link")),
            "heroLead": dim("24px", comp("the div after h1 on the home page")),
            "h1": dim("64px", comp("h1 on the home page")),
            "h2": dim("40px", comp("the first feature h2 on the home page")),
            "display": dim("48px", comp("h2.n-h2-xl How it Works, and the pricing h1")),
            "price": dim("84px", comp(".text-size-huge.pricing $13 on /pricing")),
            "cta": dim("20px", comp("a.btn--yellow Build My Resume")),
            "checkerTitle": dim("67px", comp("h1 on /tool/resume-checker at innerWidth 1169")),
            "authTitle": dim("24px", app_comp("h1 Login")),
            "footerLink": dim("13px", comp("the first footer link")),
            "legal": dim("12px", "Measured. Computed style of the terms line on https://app.tealhq.com/sign-up, 2026-11-19."),
        },
        "lineHeight": {
            "body": dim("20.8px", comp("document.body on the home page")),
            "appBody": dim("20px", app_comp("document.body")),
            "heroLead": dim("31.2px", comp("the div after h1 on the home page")),
            "h1": dim("64px", comp("h1 on the home page")),
            "h2": dim("40px", comp("the first feature h2 on the home page")),
            "display": dim("45.6px", comp("h2.n-h2-xl How it Works")),
            "price": dim("84px", comp(".text-size-huge.pricing $13 on /pricing")),
            "authTitle": dim("32px", app_comp("h1 Login")),
        },
        "letterSpacing": {
            "h1": dim("-2px", comp("h1 on the home page")),
            "h2": dim("-1px", comp("the first feature h2 on the home page")),
            "cta": dim("-0.4px", comp("a.btn--yellow Build My Resume")),
            "nav": dim("-0.16px", comp("header nav")),
            "tight": text("-0.025em", SRC_M + " Token --tracking-tight."),
        },
        "space": {
            "1": dim("4px", SRC_APP + " Token --spacing is 0.25rem, computed as 4px at 16px root."),
            "2": dim("8px", comp("gap on a.btn--yellow, and the form gap on sign-in")),
            "3": dim("12px", app_comp("horizontal padding of the email field")),
            "4": dim("16px", comp("vertical padding of a.btn--yellow")),
            "5": dim("20px", comp("horizontal padding of header nav links")),
            "6": dim("24px", comp("section padding and header button horizontal padding")),
            "8": dim("32px", app_comp("main padding and the Sign in button horizontal padding")),
            "10": dim("40px", comp("section padding on .u--section")),
        },
        "radius": {
            "xs": dim("3px", app_comp("email and password fields, class rounded-xs")),
            "sm": dim("4px", SRC_APP + " Token --radius-sm."),
            "md": dim("6px", SRC_APP + " Token --radius-md."),
            "menu": dim("8px", comp("header mega-menu row, class rounded-lg")),
            "lg": dim("8px", SRC_APP + " Token --radius-lg."),
            "card": dim("16px", SRC_M + " Token --radius-card. Also the computed radius of feature cards and the How it Works pane."),
            "pricingCard": dim("24px", comp("pricing-component--col bottom radius on the home page")),
            "testimonial": dim("13px", comp(".pricing-testimonial-block on /pricing")),
            "pill": dim("100px", comp("a.btn--yellow border-radius")),
            "authButton": dim("24px", app_comp("Sign in button and Continue with LinkedIn")),
            "footer": dim("72px", comp("footer top-left radius, class rounded-tl-[72px]")),
        },
        "size": {
            "header": dim("67px", comp("header on the home page")),
            "headerSignup": dim("41px", comp("header Sign up link")),
            "headerLogin": dim("43px", comp("header Log in link")),
            "cta": dim("53px", comp("a.btn--yellow Build My Resume")),
            "toolCta": dim("45px", comp("Check your resume score on /tool/resume-checker")),
            "field": dim("36px", app_comp("email field")),
            "authButton": dim("40px", app_comp("Sign in button")),
            "authForm": dim("384px", app_comp("the sign-in form, class max-w-96")),
            "logo": dim("32px", comp("header logo image height")),
            "iconWell": dim("48px", comp("circular icon well, class w-[48px] h-[48px]")),
        },
        "borderWidth": {
            "hairline": dim("0.5px", app_comp("email field border-top-width")),
            "login": dim("1px", comp("header Log in border-top-width")),
        },
        "shadow": {
            "fieldFocus": shadow(
                "rgb(255, 255, 255) 0px 0px 0px 1px, rgb(0, 82, 73) 0px 0px 0px 2px, rgba(0, 82, 73, 0.25) 0px 0px 0px 4px",
                app_comp("email field after focus()"),
            ),
            "appSm": shadow(
                "0px 1px 2px -1px rgba(0, 0, 0, .1), 0px 1px 3px 0px rgba(0, 0, 0, .1)",
                SRC_APP + " Token --shadow-sm. Not the computed shadow of the sign-in form, which was none.",
            ),
        },
        "motion": {
            "durationFast": duration("150ms", SRC_M + " Token --default-transition-duration is .15s."),
            "durationButton": duration("200ms", comp("a.btn--yellow transition, reported as 0.2s")),
            "durationPress": duration("75ms", app_comp("Sign in button transition-duration, class duration-75")),
            "easeStandard": cubic(
                [0.4, 0, 0.2, 1],
                SRC_M + " Token --ease-in-out and --default-transition-timing-function.",
            ),
        },
    },
    "light": {
        "color": {
            "page": color("#ffffff", comp("document.body background on the home page, rgb(255, 255, 255)")),
            "surface": color("#ffffff", comp("header background, class bg-white")),
            "ink": color("#333333", SRC_M + " Token --color-ink is #333. Computed body colour rgb(51, 51, 51)."),
            "inkStrong": color("#1a1a1a", SRC_M + " Token --color-ink-strong. Not the computed colour of the measured headings."),
            "muted": color("#787878", SRC_M + " Token --colors--grey-600."),
            "border": color("#e5e7eb", SRC_M + " Token --color-border-light. Header class border-[#e5e7eb]."),
            "loginBorder": color("#2d2d2d", comp("header Log in border, class border-[#2D2D2D], rgb(45, 45, 45)")),
            "yellow": color("#f5b501", SRC_M + " Token --color-teal-yellow and --colors--goldfinch-yellow. Computed Sign up and btn--yellow fill rgb(245, 181, 1)."),
            "yellowSoft": color("#f9d367", comp("div.background-color--yellow on the home page, rgb(249, 211, 103)")),
            "teal": color("#005149", SRC_M + " Token --color-teal-green and --colors--teal-700. Computed teal band rgb(0, 81, 73)."),
            "tealSoft": color("#e9f3f3", SRC_M + " Token --colors--teal-100. Computed feature card rgb(233, 243, 243)."),
            "purple": color("#5a6fec", SRC_M + " Token --color-teal-purple and --colors--blue-700. Computed feature panel rgb(90, 111, 236)."),
            "pheasant": color("#791e3f", SRC_M + " Token --colors--pheasant-red. Computed footer rgb(121, 30, 63)."),
            "chickadee": color("#f1f2f2", SRC_M + " Token --colors--chickadee-grey and --color-surface-muted. Icon well fill."),
            "onYellow": color("#000000", comp("a.btn--yellow text, rgb(0, 0, 0)")),
            "onYellowHeader": color("#2d2d2d", comp("header Sign up text, class text-[#2D2D2D]")),
            "onDark": color("#ffffff", comp("footer link, class text-white")),
            "menuHover": color("#f9fafb", "Measured. Declared hover fill on header mega-menu rows, class hover:bg-[#F9FAFB]. Not a computed rest state."),
            "navHover": color("#005149", "Measured. Declared hover colour on header nav links, class hover:text-[#005149]. Not a computed rest state."),
            "canary": color("#f5e867", SRC_M + " Token --colors--canary-yellow."),
            "maroon": color("#e84e30", SRC_M + " Token --colors--maroon-700 and --colors--red-700."),
            "brown": color("#b58d47", SRC_M + " Token --colors--brown-700. Used as a fill in a header menu icon."),
        },
        "component": {
            "button-primary-bg": color("#f5b501", comp("a.btn--yellow and header Sign up, rgb(245, 181, 1)")),
            "button-primary-text": color("#000000", comp("a.btn--yellow text, rgb(0, 0, 0)")),
            "button-outline-bg": color("#ffffff", comp("header Log in background")),
            "button-outline-text": color("#2d2d2d", comp("header Log in text, rgb(45, 45, 45)")),
        },
    },
    "app": {
        "color": {
            "page": color("#ffffff", app_comp("document.body background")),
            "surface": color("#ffffff", app_comp("email field background")),
            "ink": color("#0a0a0a", app_comp("document.body colour, rgb(10, 10, 10)")),
            "inkStrong": color("#171717", SRC_APP + " Token --color-text-primary-default. Sign in button text computed rgb(23, 23, 23)."),
            "muted": color("#737373", SRC_APP + " Token --color-text-secondary-default. Sign-up subtitle computed rgb(115, 115, 115)."),
            "border": color("#cccccc", app_comp("email field border, rgb(204, 204, 204). Token --border is 0 0% 80%.")),
            "brand": color("#005249", SRC_APP + " Token --color-brand-900 and --primary (174 100% 16%). Link text computed rgb(0, 82, 73)."),
            "brandHover": color("#1d5851", SRC_APP + " Token --color-background-fill-bold-brand-hover. Not a computed hover on the sign-in page."),
            "accent": color("#f4b301", SRC_APP + " Token --color-accent-500 and --secondary (44 99% 48%). Sign in button computed rgb(244, 179, 1)."),
            "accentHover": color("#ffe042", SRC_APP + " Token --color-background-fill-bold-accent-hover. Not a computed hover on the sign-in page."),
            "onAccent": color("#171717", app_comp("Sign in button text, rgb(23, 23, 23)")),
            "linkedin": color("#2427ab", app_comp("Continue with LinkedIn, rgb(36, 39, 171). Also --colors--purple-700 on the marketing sheet.")),
            "onLinkedin": color("#fafafa", app_comp("Continue with LinkedIn text, rgb(250, 250, 250)")),
            "danger": color("#e84e30", SRC_APP + " Token --color-danger-500. Not shown as an error on the empty sign-in form."),
            "focusRing": color("#005249", app_comp("the middle ring of the focused email field shadow")),
            "legal": color("#94a3b8", "Measured. Computed colour of the terms line on sign-up was oklch(0.707 0.022 261.325). The hex is the sRGB equivalent of that computed oklch, rounded. The oklch string is the reading."),
        }
    },
    "$themes": [
        {"id": "light", "name": "Marketing light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
        {"id": "app", "name": "App signed-out", "selectedTokenSets": {"core": "source", "app": "enabled"}},
    ],
    "$extensions": {
        "source": "Live T3 preview readings of tealhq.com public pages and app.tealhq.com sign-in and sign-up, 2026-11-19.",
        "gaps": [
            "No dark theme was mounted on the public pages.",
            "Screenshot frames failed in the preview browser. Headless Playwright received a Cloudflare block on www.tealhq.com and app.tealhq.com.",
            "Sign-up was not submitted. No card, phone or SSO was entered.",
            "Phone width was not measured. The preview viewport was 1169 by 731.",
        ],
    },
}

# The legal colour above used a conversion. Keep the computed oklch as the token
# value instead, so the file does not contain a converted hex.
tokens["app"]["color"]["legal"] = color(
    "oklch(0.707 0.022 261.325)",
    "Measured. Computed colour of the terms line on https://app.tealhq.com/sign-up, 2026-11-19.",
)

# Values typed in from the preview that raw/readings.json does not hold (declared custom properties
# it did not record, and computed styles that were read but not saved). They carry the hand-entered
# label, not Measured; the rest of the file's values are in raw/readings.json.
HAND = [
    "core.font.marketingNav", "core.font.mono", "core.fontWeight.light", "core.fontWeight.regular",
    "core.fontWeight.bold", "core.fontSize.legal", "core.radius.md", "core.size.toolCta", "core.motion.easeStandard",
    "core.fontSize.display", "core.fontSize.price", "core.fontSize.footerLink", "core.lineHeight.heroLead",
    "core.lineHeight.display", "core.lineHeight.price", "core.letterSpacing.h2", "core.letterSpacing.tight",
    "core.radius.testimonial", "core.radius.footer", "core.size.authForm", "core.size.iconWell",
    "core.shadow.appSm", "core.motion.durationFast", "core.motion.durationButton", "core.motion.durationPress",
    "light.color.inkStrong", "light.color.muted", "light.color.border", "light.color.chickadee",
    "light.color.menuHover", "light.color.canary", "light.color.maroon", "light.color.brown",
    "app.color.brandHover", "app.color.accentHover", "app.color.danger", "app.color.legal",
]
for path in HAND:
    node = tokens
    for key in path.split("."):
        node = node[key]
    reading = node["$extensions"]["source"].removeprefix("Measured. ")
    node["$extensions"]["source"] = (
        "Reconstruction: entered by hand at capture time; no raw/ file holds this reading. " + reading
    )


def render() -> str:
    """tokens.json's exact text; importing this module writes nothing."""
    return json.dumps(tokens, indent=2) + "\n"


if __name__ == "__main__":
    out = HERE / "tokens.json"
    out.write_text(render())
    print(f"wrote {out}")
