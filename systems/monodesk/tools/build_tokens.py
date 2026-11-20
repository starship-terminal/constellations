#!/usr/bin/env python3
"""Write tokens.json from the MonoDesk readings in raw/.

Marketing colours come from computed custom properties on www.monodesk.com
(:root, captured 2026-11-19). App colours come from computed styles on
app.monodesk.com/login and /create, signed out. Geometry comes from
raw/components-computed.json. Nothing here is sampled from a screenshot.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"


def tok(value, type_, source, description=None):
    out = {"$value": value, "$type": type_, "$extensions": {"source": source}}
    if description:
        out["$description"] = description
    return out


def dim(px, source, description=None):
    return tok(f"{px}px" if isinstance(px, (int, float)) else px, "dimension", source, description)


def color(value, source, description=None):
    return tok(value, "color", source, description)


def main():
    pages = json.loads((RAW / "pages.json").read_text())
    home = next(p for p in pages["pages"] if p.get("prefix") == "home-light")
    login = next(p for p in pages["pages"] if p.get("prefix") == "app-login-light")
    comps = json.loads((RAW / "components-computed.json").read_text())["components"]

    def style(name):
        node = comps[name]
        return node.get("style") or node

    cta = style("cta-primary-default")
    plan = style("plan-cta-default")
    badge = style("badge-popular")
    search = style("search-default")
    field = style("field-email-default")
    google = style("button-google-default")
    login_btn = style("button-login-default")
    card = style("login-card")
    hero = style("heading-hero")
    price = style("price-amount")
    link = style("link-create-default")
    nav = style("nav-link-default")

    ghost = json.loads((RAW / "ghost.json").read_text()) if (RAW / "ghost.json").exists() else None

    core = {
        "font": {
            "family": {
                "geist": tok(
                    "Geist, system-ui, sans-serif",
                    "fontFamily",
                    "computed font-family on www.monodesk.com body, 1440px, 2026-11-19",
                    "Marketing face. Variable Geist (woff2) is licensed and not shipped.",
                ),
                "geistApp": tok(
                    'Geist, -apple-system, "system-ui", "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
                    "fontFamily",
                    "computed font-family on app.monodesk.com/login heading, 2026-11-19",
                    "App face. Same Geist, longer system fallback stack.",
                ),
                "geistMono": tok(
                    '"Geist Mono", ui-monospace, monospace',
                    "fontFamily",
                    "@font-face Geist Mono on www.monodesk.com/_astro/geist-mono-latin-wght-normal, 2026-11-19",
                    "Declared on the marketing site. Not used as body text.",
                ),
            },
            "weight": {
                "regular": tok(400, "fontWeight", "computed font-weight on marketing body"),
                "medium": tok(500, "fontWeight", "computed font-weight on plan CTA and nav links"),
                "semibold": tok(600, "fontWeight", "computed font-weight on pricing h1 and Create account link"),
                "bold": tok(700, "fontWeight", "computed font-weight on the $0 price"),
            },
            "size": {
                "badge": dim(10, "computed font-size on MOST POPULAR badge"),
                "plan": dim(13, "computed font-size on pricing Get started"),
                "nav": dim(14, "computed font-size on header Log in"),
                "body": dim(16, "computed font-size on marketing body"),
                "appHeading": dim(22, "computed font-size on Login to your account"),
                "price": dim(32, "computed font-size on $0"),
                "section": dim(36, "computed font-size on pricing h2 How pricing will work"),
                "hero": dim(72, "computed font-size on home h1 at 1440px"),
            },
        },
        "radius": {
            "field": dim(9, "computed border-radius on login email input"),
            "google": dim(7, "computed border-radius on Login with Google"),
            "login": dim(12, "computed border-radius on Login button"),
            "card": dim(16, "computed border-radius on login card and help card; also --radius-lg"),
            "xl": dim(20, "declared --radius-xl on :root"),
            "2xl": dim(30, "declared --radius-2xl on :root"),
            "pill": dim(100, "computed border-radius 100px on Get started free and search"),
        },
        "spacing": {
            "xs": dim(8, "declared --spacing-xs"),
            "sm": dim(16, "declared --spacing-sm"),
            "md": dim(24, "declared --spacing-md"),
            "lg": dim(40, "declared --spacing-lg"),
            "xl": dim(60, "declared --spacing-xl"),
            "2xl": dim(80, "declared --spacing-2xl"),
        },
        "layout": {
            "pageMax": dim(1320, "declared --layout-page-max"),
            "centered": dim(1200, "declared --layout-max-centered"),
            "insetSm": dim(24, "declared --layout-inset-fluid-sm"),
        },
        "motion": {
            "duration": {
                "nav": tok("200ms", "duration", "computed transition-duration 0.2s on header nav links"),
                "menu": tok("150ms", "duration", "computed transition-duration 0.15s on header menu items"),
            },
            "easing": {
                "ease": tok([0.25, 0.1, 0.25, 1], "cubicBezier", "Derived: CSS ease keyword expanded to its control points. Computed timing-function on header links was the keyword ease."),
            },
        },
        "typography": {
            "hero": tok(
                {
                    "fontFamily": "{font.family.geist}",
                    "fontSize": "{font.size.hero}",
                    "fontWeight": "{font.weight.regular}",
                    "lineHeight": "1.05",
                    "letterSpacing": "0",
                },
                "typography",
                "computed h1 on www.monodesk.com/ at 1440px (72px / 400 / Geist / #ffffff)",
            ),
            "section": tok(
                {
                    "fontFamily": "{font.family.geist}",
                    "fontSize": "{font.size.section}",
                    "fontWeight": "{font.weight.semibold}",
                    "lineHeight": "1.2",
                    "letterSpacing": "0",
                },
                "typography",
                "computed h2 on /pricing (36px / 600)",
            ),
            "body": tok(
                {
                    "fontFamily": "{font.family.geist}",
                    "fontSize": "{font.size.body}",
                    "fontWeight": "{font.weight.regular}",
                    "lineHeight": "1.5",
                    "letterSpacing": "0",
                },
                "typography",
                "computed body on www.monodesk.com (16px / 400 / Geist)",
            ),
            "nav": tok(
                {
                    "fontFamily": "{font.family.geist}",
                    "fontSize": "{font.size.nav}",
                    "fontWeight": "{font.weight.medium}",
                    "lineHeight": "1.2",
                    "letterSpacing": "0",
                },
                "typography",
                "computed header Log in link (14px / 500)",
            ),
            "price": tok(
                {
                    "fontFamily": "{font.family.geist}",
                    "fontSize": "{font.size.price}",
                    "fontWeight": "{font.weight.bold}",
                    "lineHeight": "1.1",
                    "letterSpacing": "0",
                },
                "typography",
                "computed $0 on /pricing (32px / 700 / #161616)",
            ),
            "appHeading": tok(
                {
                    "fontFamily": "{font.family.geistApp}",
                    "fontSize": "{font.size.appHeading}",
                    "fontWeight": "{font.weight.medium}",
                    "lineHeight": "30px",
                    "letterSpacing": "-0.015px",
                },
                "typography",
                "computed Login to your account (22px / 500 / line-height 30px)",
            ),
            "label": tok(
                {
                    "fontFamily": "{font.family.geistApp}",
                    "fontSize": "12px",
                    "fontWeight": "{font.weight.medium}",
                    "lineHeight": "20px",
                    "letterSpacing": "-0.015px",
                },
                "typography",
                "computed Email label on the login form (12px / 500)",
            ),
        },
        "component": {
            "button": {
                "primary": {
                    "background": color(cta["backgroundColor"], "computed background-color on Get started free pill"),
                    "text": color(cta["color"], "computed color on Get started free pill"),
                    "radius": dim(100, "computed border-radius 100px on Get started free"),
                    "height": dim(cta.get("h") or 40, "bounding box height of Get started free pill"),
                },
                "plan": {
                    "background": color(plan["backgroundColor"], "computed background-color on pricing Get started"),
                    "text": color(plan["color"], "computed color on pricing Get started"),
                    "hoverBackground": color(style("plan-cta-hover")["backgroundColor"], "computed background-color on pricing Get started :hover"),
                    "hoverText": color(style("plan-cta-hover")["color"], "computed color on pricing Get started :hover"),
                    "radius": dim(100, "computed border-radius on pricing Get started"),
                    "height": dim(plan["height"], "computed height of pricing Get started (raw/components-computed.json plan-cta-default)"),
                },
                "login": {
                    "background": color(login_btn["backgroundColor"], "computed background-color on Login button"),
                    "text": color(login_btn["color"], "computed color on Login button"),
                    "radius": dim(12, "computed border-radius on Login button"),
                    "height": dim(40, "bounding box height of Login button"),
                    "size": dim(13, "computed font-size 13.333px on Login button, rounded to 13px"),
                },
                "google": {
                    "background": color(google["backgroundColor"], "computed background-color on Login with Google"),
                    "hoverBackground": color(style("button-google-hover")["backgroundColor"], "computed background-color on Login with Google :hover"),
                    "text": color(google["color"], "computed color on Login with Google"),
                    "radius": dim(7, "computed border-radius on Login with Google"),
                    "height": dim(44, "bounding box height of Login with Google"),
                    "border": color("#e2e2e2", "computed border-top-color rgb(226, 226, 226) on Login with Google"),
                },
            },
            "field": {
                "background": color(field["backgroundColor"], "computed background-color on login email input"),
                "text": color(field["color"], "computed color on login email input"),
                "radius": dim(9, "computed border-radius on login email input"),
                "height": dim(44, "bounding box height of login email input"),
                "border": color("#ebebeb", "computed border-top-color rgb(235, 235, 235) on login email input"),
                "fontSize": dim(16, "computed font-size on login email input"),
            },
            "search": {
                "background": color(search["backgroundColor"], "computed background-color on help search"),
                "radius": dim(100, "computed border-radius on help search"),
                "height": dim(search.get("h") or 54, "bounding box height of help search"),
                "heightFocus": dim(54, "bounding box height of help search while focused"),
            },
            "card": {
                "login": {
                    "background": color(card["backgroundColor"], "computed background-color on login card"),
                    "radius": dim(16, "computed border-radius on login card"),
                    "width": dim(card.get("w") or 450, "bounding box width of login card at 1440px"),
                },
                "help": {
                    "background": color("#ffffff", "computed background-color on help category card"),
                    "radius": dim(16, "computed border-radius on help category card"),
                },
            },
            "badge": {
                "background": color(badge["backgroundColor"], "computed background-color on MOST POPULAR"),
                "text": color(badge["color"], "computed color on MOST POPULAR"),
                "radius": dim(100, "computed border-radius on MOST POPULAR"),
            },
        },
    }
    light = {
        "background": {
            "page": color("#1c64f5", "computed page fill rgb(28, 100, 245) on www.monodesk.com; declared --brand-blue", "Marketing page wash."),
            "pageInk": color("#212121", "computed background-color rgb(33, 33, 33) on marketing body", "Body background under the blue wash. Header and footer sit on this."),
            "surface": color("#ffffff", "computed background-color on help cards and the login card"),
            "tint": color("#eef2f5", "declared --surface-tint"),
            "canvas": color("#dadee1", "declared --background on marketing :root"),
            "app": color("#e5eaed", "computed background-color rgb(229, 234, 237) on app.monodesk.com/login body"),
            "field": color("#f8f8f8", "computed background-color on login inputs"),
            "action": color("#d1ff6e", "declared --brand-highlighter; computed fill of Get started free"),
            "actionHover": color("#026232", "computed background-color on pricing Get started :hover; declared --brand-fun-green"),
            "inkButton": color("#161616", "computed background-color on the Login button"),
        },
        "text": {
            "onBlue": color("#ffffff", "computed color on home h1"),
            "onBlueMuted": color("rgba(255, 255, 255, 0.85)", "computed color on header Log in at rest"),
            "primary": color("#161616", "declared --type; computed color on pricing prices and login labels"),
            "secondary": color("rgba(22, 22, 22, 0.6)", "declared --type-60; computed color on struck-through $19"),
            "light": color("#e7e7e7", "declared --type-light; computed color on marketing body"),
            "onAction": color("#026232", "computed color on Get started free"),
            "link": color("#1c64f5", "computed color on Create account and Forgot password?"),
            "muted": color("#515151", "computed color rgb(81, 81, 81) on or continue with"),
        },
        "border": {
            "stroke": color("#ebebeb", "computed border-top-color on login inputs"),
            "google": color("#e2e2e2", "computed border-top-color on Login with Google"),
            "ghost": color("rgba(255, 255, 255, 0.15)", "computed background-color of the hero Log in pill"),
        },
        "brand": {
            "blue": color("#1c64f5", "declared --brand-blue"),
            "highlighter": color("#d1ff6e", "declared --brand-highlighter"),
            "funGreen": color("#026232", "declared --brand-fun-green"),
            "orange": color("#ff5b26", "declared --brand-orange"),
            "grey": color("#94959a", "declared --brand-grey"),
            "almostBlack": color("#272727", "declared --brand-almost-black"),
            "white": color("#ffffff", "declared --brand-white"),
            "appOrange": color("#f14e13", "computed custom property --brandOrange on app.monodesk.com/login"),
        },
    }

    # The app's Tamagui layer resolves dark semantic names even on the light login.
    # Those names are recorded, but the painted login stayed light under
    # prefers-color-scheme: dark, so this set is the declared dark scale, not a
    # painted page theme.
    dark = {
        "background": {
            "page": color("#15181c", "computed --background on app.monodesk.com/login documentElement. The login page itself stayed rgb(229, 234, 237) under prefers-color-scheme: dark."),
            "surface": color("#1c2025", "computed --backgroundHover / --surfaceTint on the app documentElement"),
            "strong": color("#25292e", "computed --backgroundStrong on the app documentElement"),
        },
        "text": {
            "primary": color("#ffffff", "computed --type on the app documentElement"),
            "secondary": color("#dbdfe2", "computed --type60 on the app documentElement"),
            "muted": color("#c5cdd2", "computed --type40 on the app documentElement"),
        },
        "border": {
            "stroke": color("#424a53", "computed --borderColor on the app documentElement"),
        },
        "brand": {
            "blue": color("#1c64f5", "computed --blue on the app documentElement"),
            "highlighter": color("#d1ff6e", "computed --highlighter on the app documentElement"),
            "orange": color("#f14e13", "computed --brandOrange on the app documentElement"),
        },
    }

    tokens = {"core": core, "light": light, "dark": dark}
    relabel_unread(tokens)
    return tokens


# raw/css-vars.json holds one empty dump per page, so no custom property reading survived the capture:
# a value sourced to a declared or computed --name was typed in from the capture session. So were
# these computed values, which no file in raw/ holds.
UNREAD = {
    "core.font.size.appHeading",  # "Login to your account"; raw has only create-heading (16px)
    "core.typography.appHeading",  # the same heading's 22px / 30px composite
    "light.text.muted",  # rgb(81, 81, 81) on "or continue with"
}
HAND = ("Reconstruction: entered by hand at capture time; no file in raw/ holds this reading "
        "(raw/css-vars.json dumps are empty). Capture note: ")


def leaves(node, path=""):
    for k, v in node.items():
        if k.startswith("$") or not isinstance(v, dict):
            continue
        here = f"{path}.{k}" if path else k
        if "$value" in v:
            yield here, v
        else:
            yield from leaves(v, here)


def relabel_unread(tokens):
    import re
    for path, tok in leaves(tokens):
        src = tok["$extensions"]["source"]
        if path not in UNREAD and isinstance(tok["$value"], str) and tok["$value"].startswith("{"):
            continue  # an alias carries the evidence of the token it names
        # A source that cites only a custom property has nothing behind it; one that also cites a
        # computed style on an element ("computed color on ...") is backed by that reading.
        cites_var = bool(re.search(r"(?<![\w-])--[A-Za-z]", src))
        cites_style = bool(re.search(r"computed (?!--|custom property)", src))
        if path in UNREAD or (cites_var and not cites_style):
            tok["$extensions"]["source"] = HAND + src


def write():
    tokens = main()
    (HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
    print("wrote", HERE / "tokens.json")


if __name__ == "__main__":
    write()
