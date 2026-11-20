#!/usr/bin/env python3
"""Write tokens.json from raw/foundations.json.

Values were read with getComputedStyle on super.so and app.super.so on
2026-11-19. This script does not invent colours. Re-run only after updating
the raw file.
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


def padding(value, source):
    """A padding shorthand as one px length per side: {block, inline} when it is symmetric, else
    {top, right, bottom, left}. A single length stays one dimension token."""
    parts = value.split()
    if len(parts) == 1:
        return dim(value, source)
    if len(parts) == 2:
        top, right, bottom, left = parts[0], parts[1], parts[0], parts[1]
    elif len(parts) == 3:
        top, right, bottom, left = parts[0], parts[1], parts[2], parts[1]
    else:
        top, right, bottom, left = parts
    note = f"{source} (computed shorthand {value})"
    if top == bottom and left == right:
        return {"block": dim(top, note), "inline": dim(right, note)}
    return {"top": dim(top, note), "right": dim(right, note), "bottom": dim(bottom, note), "left": dim(left, note)}


def font_token(family, weight, size, line, tracking, source):
    body = {
        "fontFamily": family,
        "fontWeight": weight,
        "fontSize": size,
        "lineHeight": line,
    }
    if tracking and tracking != "normal":
        body["letterSpacing"] = tracking
    return {
        "$type": "typography",
        "$value": body,
        "$extensions": {"source": source},
    }


def build():
    src = RAW["source"]
    c = RAW["colors"]
    t = RAW["type"]
    fonts = RAW["fonts"]
    r = RAW["radius"]
    s = RAW["spacing"]
    core = {
        "font": {
            "family": {
                "beausite": tok("fontFamily", fonts["beausite"], src + " body fontFamily on super.so"),
                "beausite-app": tok("fontFamily", fonts["beausiteApp"], src + " body fontFamily on app.super.so/login"),
            }
        },
        "typography": {
            "body": font_token(fonts["beausite"], t["body"]["fontWeight"], t["body"]["fontSize"], t["body"]["lineHeight"], t["body"]["letterSpacing"], src + " notion-text on super.so"),
            "hero": font_token(fonts["beausite"], t["hero"]["fontWeight"], t["hero"]["fontSize"], t["hero"]["lineHeight"], t["hero"]["letterSpacing"], src + " h1 on super.so"),
            "display": font_token(fonts["beausite"], t["display"]["fontWeight"], t["display"]["fontSize"], t["display"]["lineHeight"], t["display"]["letterSpacing"], src + " pricing h1 computed size"),
            "heading": font_token(fonts["beausite"], t["h2"]["fontWeight"], t["h2"]["fontSize"], t["h2"]["lineHeight"], t["h2"]["letterSpacing"], src + " h2 on super.so"),
            "subhead": font_token(fonts["beausite"], t["h3"]["fontWeight"], t["h3"]["fontSize"], t["h3"]["lineHeight"], t["h3"]["letterSpacing"], src + " h3 on super.so"),
            "auth-title": font_token(fonts["beausiteApp"], t["authTitle"]["fontWeight"], t["authTitle"]["fontSize"], t["authTitle"]["lineHeight"], t["authTitle"]["letterSpacing"], src + " Log into Super on app.super.so/login"),
            "field": font_token(fonts["beausiteApp"], t["authField"]["fontWeight"], t["authField"]["fontSize"], t["authField"]["lineHeight"], "normal", src + " email input on app.super.so/login"),
        },
        "radius": {k: dim(v, src + " radius " + k) for k, v in r.items()},
        "spacing": {k: padding(v, src + " spacing " + k) for k, v in s.items()},
    }
    light = {
        "page": color(c["page"], src + " body background on super.so --base-warm-gray"),
        "surface": color(c["card"], src + " plan card background on super.so/pricing"),
        "muted": color(c["muted"], src + " body copy color on super.so"),
        "accent": color(c["accent"], src + " Get started free background on super.so"),
        "background": {
            "page": color(c["page"], src + " body background"),
            "surface": color(c["card"], src + " plan card"),
            "nav": color(c["white"], src + " navbar background token painted white under 0.85 scrim"),
            "footer": color(c["footer"], src + " footer background"),
            "accent": color(c["accent"], src + " nav CTA"),
            "accent-soft": color(c["personalButtonBg"], src + " Personal Start for free"),
            "ink": color(c["black"], src + " dark CTA on pricing"),
        },
        "on-accent": color(c["accentOn"], src + " nav CTA text"),
        "on-ink": color(c["footerText"], src + " dark CTA text"),
    }
    light["text"] = {
        "primary": color(c["ink"], src + " body color rgb(38, 42, 46)"),
        "muted": color(c["muted"], src + " body copy rgb(102, 112, 122)"),
        "nav": color(c["navText"], src + " navbar rgb(55, 53, 47)"),
        "on-accent": color(c["accentOn"], src + " CTA text rgb(17, 17, 17)"),
        "on-ink": color(c["footerText"], src + " white on black CTA"),
        "footer": color(c["footerText"], src + " footer"),
        "sign-in": color(c["signInText"], src + " Sign in rgb(77, 84, 92)"),
        "features": color(c["featuresH1"], src + " Features h1 rgb(179, 186, 194)"),
        "nav-role": color(c["navText"], src + " navbar rgb(55, 53, 47)"),
        "footer-role": color(c["footerText"], src + " footer"),
        "sign-in-role": color(c["signInText"], src + " Sign in rgb(77, 84, 92)"),
    }
    light["border"] = {
        "default": color(c["border"], src + " --color-border-default #E9E9E7"),
        "sign-in": color(c["signInBorder"], src + " Sign in border rgb(242, 244, 245)"),
        "personal": color(c["personalBorder"], src + " Personal plan card border"),
        "quote": color(c["quoteBorder"], src + " quote card border"),
    }
    light["accent"] = color(c["accent"], src + " CTA rgb(255, 190, 60)")
    light["component"] = {
        "button": {
            "bg": color(c["accent"], src + " nav CTA background"),
            "text": color(c["accentOn"], src + " nav CTA text"),
            "radius": dim(r["navCta"], src + " nav CTA radius"),
            "padding": padding(s["navCtaPadding"], src + " nav CTA padding"),
            "height": dim("42px", src + " nav CTA height"),
        },
        "field": {
            "bg": color(c["appPage"], src + " login field background; marketing has no text field"),
            "text": color(c["appTextMeasured"], src + " login field text"),
            "radius": dim(r["authField"], src + " login field radius"),
            "padding": padding(s["authFieldPadding"], src + " login field padding"),
            "height": dim("44px", src + " login field height"),
        },
    }
    dark = {
        "page": color(c["appPage"], src + " body background on app.super.so/login"),
        "surface": color(c["appPage"], src + " login field and page share rgb(21, 21, 20)"),
        "text": {
            "primary": color(c["appTextMeasured"], src + " login body and field text rgb(238, 238, 237)"),
            "muted": color(c["appMuted"], src + " Sign up link rgb(126, 125, 119)"),
            "placeholder": color(c["appPlaceholder"], src + " email ::placeholder"),
            "on-accent": color(c["appAccentOn"], src + " Log in button text"),
        },
        "muted": color(c["appMuted"], src + " Sign up link"),
        "accent": color(c["appAccent"], src + " Log in button rgb(255, 178, 36)"),
        "border": color(c["appBorder"], src + " login field border rgb(45, 45, 42)"),
        "background": {
            "page": color(c["appPage"], src + " login body"),
            "surface": color(c["secondaryButtonBg"], src + " Google button"),
            "raised": color(c["passkeyBg"], src + " passkey button"),
            "accent": color(c["appAccent"], src + " Log in button"),
        },
        "focus": color(c["appFocusRing"], src + " .input-focus-within:focus-within:is(.dark *) ring #4d2e00"),
        "component": {
            "button": {
                "bg": color(c["appAccent"], src + " Log in button"),
                "text": color(c["appAccentOn"], src + " Log in button text"),
                "radius": dim(r["authButton"], src + " Log in radius"),
                "padding": padding(s["authButtonPadding"], src + " Log in padding"),
                "height": dim("44px", src + " Log in height"),
            },
            "field": {
                "bg": color(c["appPage"], src + " login field"),
                "text": color(c["appTextMeasured"], src + " login field text"),
                "radius": dim(r["authField"], src + " login field radius"),
                "padding": padding(s["authFieldPadding"], src + " login field padding"),
                "height": dim("44px", src + " login field height"),
            },
        },
    }
    # swatch paths used by the catalog: light.page, light.surface, light.text.primary, etc.
    # Also expose flat aliases the swatches name.
    light_swatch = {
        "page": light["page"],
        "surface": light["surface"],
        "text": light["text"],
        "muted": light["muted"],
        "accent": light["accent"],
        "border": light["border"]["default"],
        "background": light["background"],
        "on-accent": light["on-accent"],
        "focus": color(c["lightFocusRing"], src + " .input-focus-within:focus-within ring #ffe0b3"),
        "component": light["component"],
    }
    doc = {
        "$schema": "https://www.designtokens.org/schemas/2025.10/format/",
        "core": core,
        "light": light_swatch,
        "dark": {
            "page": dark["page"],
            "surface": dark["surface"],
            "text": dark["text"],
            "muted": dark["muted"],
            "accent": dark["accent"],
            "border": dark["border"],
            "background": dark["background"],
            "focus": dark["focus"],
            "component": dark["component"],
        },
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
        ],
    }
    return doc


def render():
    """tokens.json's exact text; nothing is written."""
    return json.dumps(build(), indent=2) + "\n"


if __name__ == "__main__":
    OUT.write_text(render())
    print(f"wrote {OUT}")
