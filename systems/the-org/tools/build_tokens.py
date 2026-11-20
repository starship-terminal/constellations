#!/usr/bin/env python3
"""Build tokens.json for The Org from raw/css-vars.json and raw/components.json.

Every value is a custom property declared on :root or html, or a computed style
read on a real element, on 2026-11-19. The public site is light only. Sonner
declares a dark toast theme in CSS, but no dark product theme was on screen, so
those declarations stay in raw/css-vars.json and are not a dark token set.

Run: python3 tools/build_tokens.py
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components.json").read_text())

CAPTURE = "T3 preview evaluate on theorg.com, 2026-11-19, signed out, light, 1440x900 CSS (390x844 for the phone drawer)"


def src(evidence, detail, selector=":root"):
    return {"evidence": evidence, "selector": selector, "detail": detail, "capture": CAPTURE}


def color(value, detail, selector=":root"):
    return {"$type": "color", "$value": value, "$extensions": {"source": src("Measured", detail, selector)}}


def dim(value, detail, selector=":root"):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": src("Measured", detail, selector)}}


def num(value, detail, selector=":root"):
    return {"$type": "number", "$value": value, "$extensions": {"source": src("Measured", detail, selector)}}


def fontw(value, detail, selector):
    return {"$type": "fontWeight", "$value": value, "$extensions": {"source": src("Measured", detail, selector)}}


def cubic(value, detail, selector=":root"):
    return {"$type": "cubicBezier", "$value": value, "$extensions": {"source": src("Measured", detail, selector)}}


def shadow(value, detail, selector=":root"):
    return {"$type": "shadow", "$value": value, "$extensions": {"source": src("Measured", detail, selector)}}


def typography(value, detail, selector):
    return {"$type": "typography", "$value": value, "$extensions": {"source": src("Measured", detail, selector)}}


def text(value, detail, selector=":root"):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": src("Measured", detail, selector)}}


def other(value, detail, selector=":root"):
    return {"$type": "other", "$value": value, "$extensions": {"source": src("Measured", detail, selector)}}


def declared(name):
    row = VARS["declared"].get(name)
    if not row:
        raise SystemExit(f"missing declared var {name}")
    return row[0]["val"], row[0]["sel"]


def core():
    """Scales and families declared on :root, plus the font weights computed on elements."""
    c = {}
    neutrals = {}
    for name in ["0", "10", "20", "30", "40", "60", "70", "80", "90", "100"]:
        val, sel = declared(f"--neutral-{name}")
        neutrals[name] = color(val, f"--neutral-{name} declared {val}", sel)
    scale = {}
    for name in ["s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7"]:
        val, sel = declared(f"--scale-{name}")
        scale[name] = color(val, f"--scale-{name} declared {val}", sel)
    primary = {}
    for name in ["10", "20", "40", "100"]:
        val, sel = declared(f"--primary-{name}")
        primary[name] = color(val, f"--primary-{name} declared {val}", sel)
    val, sel = declared("--primary-100-hover")
    primary["100-hover"] = color(val, "--primary-100-hover declared #0515d4. The header Sign up control computed rgb(15, 73, 189) on hover, which is not this token.", sel)
    bg, fg = {}, {}
    for i in range(1, 7):
        val, sel = declared(f"--bg-bg{i}")
        bg[str(i)] = color(val, f"--bg-bg{i} declared {val}", sel)
    for i in range(1, 6):
        val, sel = declared(f"--fg-fg{i}")
        fg[str(i)] = color(val, f"--fg-fg{i} declared {val}", sel)
    named = {}
    for key, var in [
        ("brand", "--brand"), ("accent-100", "--accent-100"), ("error", "--error"),
        ("success", "--success"), ("warning", "--warning"), ("off-white", "--off-white"),
        ("purple77", "--purple77"), ("background", "--background"), ("border", "--border-color"),
        ("cta-link", "--cta-link-text"),
    ]:
        val, sel = declared(var)
        named[key] = color(val, f"{var} declared {val}", sel)
    # Computed colours that are not a declared custom property.
    named["ink"] = color("#0d0d0d", "body and h1 computed rgb(13, 13, 13). Not a declared custom property.", "body")
    named["ink-soft"] = color("#666666", "hero subcopy and company-card meta computed rgb(102, 102, 102).", "p")
    named["chip"] = color("#808080", "company-card industry, place and size links computed rgb(128, 128, 128).", "a")
    named["footer"] = color("#17191c", "footer computed rgb(23, 25, 28).", "footer")
    named["footer-link"] = color("#cccccc", "footer links computed rgb(204, 204, 204).", "footer a")
    named["hairline"] = color("#e6e6e6", "company card, Learn more and pricing toggle computed border rgb(230, 230, 230). Not a declared custom property.", "div")
    named["field-border"] = color("#dad9d6", "login and signup inputs computed border rgb(218, 217, 214).", "input")
    named["nav-ink"] = color("#21201c", "Pricing nav link computed rgb(33, 32, 28).", "header a")
    named["button-dark"] = color("#272725", "Start for free, Explore more and Get started computed rgb(39, 39, 37).", "a")
    named["button-dark-text"] = color("#fdfdfc", "those dark buttons computed rgb(253, 253, 252).", "a")
    named["signup"] = color("#1754cf", "header Sign up and chart-gate Sign up computed rgb(23, 84, 207). Differs from --primary-100 #0F4BE5.", "header a")
    named["signup-hover"] = color("#0f49bd", "header Sign up computed rgb(15, 73, 189) while hovered. Differs from --primary-100-hover #0515d4.", "header a:hover")
    named["focus"] = color("#003088", "button :focus-visible outline-color rgb(0, 48, 136), declared on the button classes.", "button:focus-visible")
    named["selected-pill"] = color("#201e1d", "pricing Yearly selected pill computed rgb(32, 30, 29).", "div")
    c["color"] = {
        "neutral": neutrals, "scale": scale, "primary": primary,
        "bg": bg, "fg": fg, "named": named,
    }
    space = {}
    for key, var in [
        ("0", "--sp-0"), ("1", "--sp-1"), ("2", "--sp-2"), ("2-5", "--sp-2-5"),
        ("3", "--sp-3"), ("3-5", "--sp-3-5"), ("4", "--sp-4"), ("5", "--sp-5"),
        ("6", "--sp-6"), ("6-5", "--sp-6-5"), ("7", "--sp-7"), ("8", "--sp-8"), ("9", "--sp-9"),
    ]:
        val, sel = declared(var)
        if val == "0":
            val = "0px"
        space[key] = dim(val, f"{var} declared {val}", sel)
    radius = {
        "icon": dim("4px", "--icon-radius declared 4px", ":root"),
        "control": dim("10px", "login and signup inputs and buttons computed border-radius 10px.", "input"),
        "card-token": dim("12px", "--border-radius declared 12px. Position cards computed 12px.", ":root"),
        "dialog": dim("12px", "Platform menu [role=dialog] computed 12px.", "[role=dialog]"),
        "company-card": dim("16px", "trending company card and team card computed 16px.", "div"),
        "popover": dim("16px", "--popover-rounding declared 16px.", ":root"),
        "badge": dim("16px", "pricing 33% off badge computed 16px.", "span"),
        "pill": dim("24px", "Start for free, Learn more, Get started and nav buttons computed 24px.", "a"),
        "toggle": dim("32px", "pricing Yearly/Monthly wrap computed 32px.", "div"),
        "nav-link": dim("40px", "Log in, Sign up and Pricing nav links computed 40px.", "header a"),
        "full": dim("80px", "pricing Yearly button computed 80px.", "button"),
        "avatar": other("50%", "chart initials computed border-radius 50%. A percentage is not a DTCG dimension.", "div"),
    }
    font_size = {}
    for key, var in [
        ("1", "--fs-1"), ("1-5", "--fs-1-5"), ("2", "--fs-2"), ("2-5", "--fs-2-5"),
        ("3", "--fs-3"), ("4", "--fs-4"), ("4-5", "--fs-4-5"), ("5", "--fs-5"),
        ("6", "--fs-6"), ("7", "--fs-7"), ("8", "--fs-8"), ("9", "--fs-9"),
        ("10", "--fs-10"), ("11", "--fs-11"), ("12", "--fs-12"), ("13", "--fs-13"), ("14", "--fs-14"),
    ]:
        val, sel = declared(var)
        font_size[key] = dim(val, f"{var} declared {val}", sel)
    line_height = {
        "1": num(1, "--lh-1 declared 1", ":root"),
        "2": num(1.25, "--lh-2 declared 1.25", ":root"),
        "3": num(1.5, "--lh-3 declared 1.5", ":root"),
    }
    family = {
        "primary": text("Inter, sans-serif", "--font-primary declared \"Inter\", sans-serif. Inter was registered and unloaded on the marketing pages.", ":root"),
        "secondary": text("PP Right Grotesk, helvetica neue, helvetica, arial, sans-serif", "--font-secondary declared that stack. The homepage h1 computed it.", ":root"),
        "ui": text("DMSans, sans-serif", "body, nav, buttons, cards and the chart computed DMSans. A variable font, weight 100 to 1000, loaded. Not the declared --font-primary.", "body"),
    }
    weight = {
        "regular": fontw(400, "body and most buttons computed 400.", "body"),
        "medium": fontw(500, "Log in, Sign up, company name and menu titles computed 500.", "a"),
        "semibold": fontw(600, "pricing 33% off badge and chart section headings computed 600.", "span"),
        "bold": fontw(700, "org-page h1 and the 404 h1 computed 700.", "h1"),
        "hero": fontw(400, "homepage h1 computed 400 in PP Right Grotesk, with text-transform uppercase.", "h1"),
        "subcopy": fontw(450, "hero subcopy and pricing subcopy computed 450.", "p"),
    }
    duration = {
        "80": other("80ms", "--transition-card-hover-duration declared 80ms. A time is not a DTCG dimension.", "html"),
        "100": other("100ms", "Start for free and Pricing links computed transition-duration 0.1s.", "a"),
        "200": other("200ms", "Platform and Enrich buttons computed transition-duration 0.2s on background-color.", "button"),
        "300": other("300ms", "sonner-fade-in and several menu keyframes declared 0.3s.", "@keyframes"),
        "700": other("700ms", "header chevron and the open phone drawer computed animation-duration 0.7s.", "svg"),
    }
    easing = {
        "ease": other("ease", "card hover and nav buttons use the ease keyword.", "html"),
        "ease-in-out": other("ease-in-out", "Start for free computed ease-in-out.", "a"),
        "ease-out": other("ease-out", "sonner swipe-out declared ease-out.", "@keyframes"),
        "transition-01": cubic([0.19, 1, 0.22, 1], "--transition-01 declared cubic-bezier(0.19, 1, 0.22, 1).", ":root"),
        "transition-timing": cubic([0.075, 0.82, 0.165, 1], "--transition-timing-function declared cubic-bezier(0.075, 0.82, 0.165, 1).", ":root"),
        "drawer": cubic([0.32, 0.72, 0, 1], "header chevron and drawer panels computed cubic-bezier(0.32, 0.72, 0, 1).", "svg"),
    }
    layout = {
        "content": dim("1136px", "--max-content-width declared 1136px.", ":root"),
        "prose": dim("920px", "--max-width declared 920px.", ":root"),
        "compact": dim("375px", "--max-width-compact declared 375px.", ":root"),
        "screen-xs": dim("480px", "--screen-xs-min declared 480px.", ":root"),
        "screen-sm": dim("768px", "--screen-sm-min declared 768px.", ":root"),
        "screen-md": dim("992px", "--screen-md-min declared 992px.", ":root"),
        "screen-lg": dim("1200px", "--screen-lg-min declared 1200px.", ":root"),
        "header": dim("64px", "header computed height 64px at 1440 and at 390.", "header"),
        "breadcrumbs": dim("56px", "--height-breadcrumbs declared 56px.", ":root"),
        "footer": dim("205px", "--height-footer declared 205px. The homepage footer computed 322px, so the token is the declared value.", ":root"),
        "section": dim("100px", "--sectionSpacer declared 100px.", ":root"),
    }
    c["space"] = space
    c["radius"] = radius
    c["fontSize"] = font_size
    c["lineHeight"] = line_height
    c["fontFamily"] = family
    c["fontWeight"] = weight
    c["duration"] = duration
    c["easing"] = easing
    c["layout"] = layout
    c["typography"] = typography_roles()
    return c


def typography_roles():
    """Composite roles from computed styles. Family and size are what the element computed."""
    ui = "{fontFamily.ui}"
    display = "{fontFamily.secondary}"
    return {
        "display": typography(
            {"fontFamily": display, "fontSize": "72px", "fontWeight": "{fontWeight.hero}", "lineHeight": "68.4px", "letterSpacing": "0px"},
            "homepage h1 computed 72px / 68.4px, weight 400, uppercase, PP Right Grotesk, at 1440.", "h1"),
        "display-phone": typography(
            {"fontFamily": display, "fontSize": "46px", "fontWeight": "{fontWeight.hero}", "lineHeight": "43.7px", "letterSpacing": "0px"},
            "the same h1 computed 46px / 43.7px at 390.", "h1"),
        "page-title": typography(
            {"fontFamily": ui, "fontSize": "66px", "fontWeight": "{fontWeight.regular}", "lineHeight": "75.9px", "letterSpacing": "0px"},
            "Pricing and About h1 computed 66px / 75.9px, weight 400, DMSans.", "h1"),
        "section": typography(
            {"fontFamily": ui, "fontSize": "36px", "fontWeight": "{fontWeight.medium}", "lineHeight": "45px", "letterSpacing": "0px"},
            "About h2 Our Founders computed 36px / 45px, weight 500.", "h2"),
        "heading": typography(
            {"fontFamily": ui, "fontSize": "30px", "fontWeight": "{fontWeight.medium}", "lineHeight": "37.5px", "letterSpacing": "0px"},
            "homepage Trending companies h3 computed 30px / 37.5px, weight 500.", "h3"),
        "price": typography(
            {"fontFamily": ui, "fontSize": "28px", "fontWeight": "{fontWeight.regular}", "lineHeight": "28px", "letterSpacing": "0px"},
            "pricing plan price h2 computed 28px / 28px, weight 400.", "h2"),
        "auth-title": typography(
            {"fontFamily": ui, "fontSize": "24px", "fontWeight": "{fontWeight.medium}", "lineHeight": "30px", "letterSpacing": "0px"},
            "login and signup h3 computed 24px / 30px, weight 500.", "h3"),
        "org-title": typography(
            {"fontFamily": ui, "fontSize": "22px", "fontWeight": "{fontWeight.bold}", "lineHeight": "26.4px", "letterSpacing": "0px"},
            "org page h1 computed 22px / 26.4px, weight 700, color rgb(17, 19, 33).", "h1"),
        "subcopy": typography(
            {"fontFamily": ui, "fontSize": "20px", "fontWeight": "{fontWeight.subcopy}", "lineHeight": "30px", "letterSpacing": "0px"},
            "homepage hero p computed 20px / 30px, weight 450, rgb(102, 102, 102).", "p"),
        "company": typography(
            {"fontFamily": ui, "fontSize": "18px", "fontWeight": "{fontWeight.medium}", "lineHeight": "22.5px", "letterSpacing": "0px"},
            "company name link computed 18px / 22.5px, weight 500.", "a"),
        "body": typography(
            {"fontFamily": ui, "fontSize": "16px", "fontWeight": "{fontWeight.regular}", "lineHeight": "18.4px", "letterSpacing": "0px"},
            "body computed 16px / 18.4px, weight 400, DMSans, rgb(13, 13, 13).", "body"),
        "faq-answer": typography(
            {"fontFamily": ui, "fontSize": "18px", "fontWeight": "{fontWeight.regular}", "lineHeight": "27px", "letterSpacing": "0px"},
            "open FAQ answer computed 18px / 27px, weight 400.", "div"),
        "label": typography(
            {"fontFamily": ui, "fontSize": "14px", "fontWeight": "{fontWeight.medium}", "lineHeight": "16.1px", "letterSpacing": "0px"},
            "header Sign up and plan names computed 14px, weight 500.", "a"),
        "caption": typography(
            {"fontFamily": ui, "fontSize": "12px", "fontWeight": "{fontWeight.regular}", "lineHeight": "13.8px", "letterSpacing": "0px"},
            "company-card chips computed 12px / 13.8px, rgb(128, 128, 128).", "a"),
        "field": typography(
            {"fontFamily": "{fontFamily.primary}", "fontSize": "14px", "fontWeight": "{fontWeight.regular}", "lineHeight": "20px", "letterSpacing": "0px"},
            "login and signup inputs computed Inter 14px / 20px. The only measured Inter on these pages.", "input"),
    }


def light():
    """Semantic roles for the one theme on screen."""
    return {
        "color": {
            "page": color("{color.named.background}", "body computed rgb(255, 255, 255); :root --background is #fefefe.", "body"),
            "surface": color("{color.bg.1}", "--bg-bg1 #FFFFFF. Company cards and the chart card computed white.", "div"),
            "surface-muted": color("{color.bg.2}", "--bg-bg2 #F9F9F9. Declared. Not measured on a filled element.", ":root"),
            "text": color("{color.named.ink}", "body computed rgb(13, 13, 13).", "body"),
            "text-secondary": color("{color.named.ink-soft}", "hero subcopy computed rgb(102, 102, 102).", "p"),
            "muted": color("{color.fg.2}", "--fg-fg2 #6F7179. Org meta and the signup footer computed rgb(111, 113, 121).", "p"),
            "link": color("{color.named.cta-link}", "--cta-link-text #0F4BE5. Footer logo link and the 404 home link computed rgb(15, 75, 229).", "a"),
            "accent": color("{color.named.signup}", "header Sign up computed rgb(23, 84, 207).", "header a"),
            "accent-token": color("{color.primary.100}", "--primary-100 #0F4BE5. Declared. The painted signup button is named.signup.", ":root"),
            "on-accent": color("#ffffff", "Sign up text computed rgb(255, 255, 255).", "header a"),
            "border": color("{color.named.hairline}", "cards and secondary buttons computed rgb(230, 230, 230).", "div"),
            "border-token": color("{color.named.border}", "--border-color #ebecec. Declared. The painted hairline is named.hairline.", ":root"),
            "focus": color("{color.named.focus}", "button :focus-visible outline rgb(0, 48, 136) 2px solid.", "button:focus-visible"),
            "danger": color("{color.named.error}", "--error #f6354d. Declared. No error state was shown.", ":root"),
            "success": color("{color.named.success}", "--success #009378. Declared. No success state was shown.", ":root"),
            "warning": color("{color.named.warning}", "--warning #ffb818. Declared. No warning state was shown.", ":root"),
            "footer": color("{color.named.footer}", "footer computed rgb(23, 25, 28).", "footer"),
            "footer-text": color("{color.named.footer-link}", "footer links computed rgb(204, 204, 204).", "footer a"),
            "inverse": color("{color.named.button-dark}", "Start for free computed rgb(39, 39, 37).", "a"),
            "on-inverse": color("{color.named.button-dark-text}", "Start for free text computed rgb(253, 253, 252).", "a"),
        },
        "shadow": {
            "card": shadow("0 1px 3px rgba(0, 0, 0, 0.05)", "company card computed rgba(0, 0, 0, 0.05) 0px 1px 3px 0px.", "div"),
            "elevation-1": shadow("0 1px 3px rgba(0, 0, 0, 0.07)", "--elevation-1 declared 0 1px 3px rgba(0,0,0,0.07). The selected pricing pill computed the same.", ":root"),
            "navbar": shadow("0 6px 5px -6px rgb(33 33 38 / 12%)", "--navbar-shadow declared that value. The header computed none at rest.", ":root"),
            "dialog": shadow("0 4px 20px rgba(0, 0, 0, 0.15)", "Platform menu computed rgba(0, 0, 0, 0.15) 0px 4px 20px 0px.", "[role=dialog]"),
            "card-token": shadow("0 0 1px rgba(0,0,0,0.04), 0 4px 8px rgba(0,0,0,0.04), 0 8px 16px rgba(0,0,0,0.04), 0 16px 24px rgba(0,0,0,0.04)", "--card-box-shadow declared that stack. The trending cards computed a smaller shadow.", ":root"),
            "popover": shadow("0 2px 16px rgba(0,0,0,0.05), 0 3px 4px rgba(0,0,0,0.08)", "--popover-shadow declared that stack.", ":root"),
        },
        "component": component_tokens(),
    }


def component_tokens():
    """One group per measured control. Values are the computed style, aliased where a core token matches."""
    return {
        "button-primary": {
            "background": color("{color.named.signup}", "header Sign up computed rgb(23, 84, 207).", "header a"),
            "text": color("#ffffff", "Sign up text computed white.", "header a"),
            "radius": dim("40px", "Sign up computed 40px.", "header a"),
            "padding": other("16px", "Sign up computed padding 16px.", "header a"),
            "height": dim("32px", "Sign up computed 32px.", "header a"),
            "font-size": dim("14px", "Sign up computed 14px.", "header a"),
            "font-weight": fontw(500, "Sign up computed 500.", "header a"),
        },
        "button-dark": {
            "background": color("{color.named.button-dark}", "Start for free computed rgb(39, 39, 37).", "a"),
            "text": color("{color.named.button-dark-text}", "Start for free text computed rgb(253, 253, 252).", "a"),
            "radius": dim("24px", "Start for free computed 24px.", "a"),
            "padding": other("0px 24px", "Start for free computed padding 0px 24px.", "a"),
            "height": dim("48px", "Start for free computed 48px.", "a"),
        },
        "button-secondary": {
            "background": color("#ffffff", "Learn more computed white.", "a"),
            "text": color("{color.named.ink}", "Learn more text computed rgb(13, 13, 13).", "a"),
            "border": color("{color.named.hairline}", "Learn more border computed 1px solid rgb(230, 230, 230).", "a"),
            "radius": dim("24px", "Learn more computed 24px.", "a"),
            "height": dim("48px", "Learn more computed 48px.", "a"),
        },
        "text-field": {
            "background": color("#ffffff", "login email input computed white.", "input"),
            "text": color("#000000", "login input computed rgb(0, 0, 0).", "input"),
            "border": color("{color.named.field-border}", "login input border computed 1px solid rgb(218, 217, 214).", "input"),
            "radius": dim("10px", "login input computed 10px.", "input"),
            "height": dim("48px", "login input computed 48px.", "input"),
            "padding": other("9px 12px 9px 34px", "login input computed padding 9px 12px 9px 34px.", "input"),
            "font-size": dim("14px", "login input computed 14px Inter.", "input"),
        },
        "company-card": {
            "background": color("#ffffff", "trending card computed white.", "div"),
            "border": color("{color.named.hairline}", "trending card border computed 1px solid rgb(230, 230, 230).", "div"),
            "radius": dim("16px", "trending card computed 16px.", "div"),
            "padding": dim("16px", "trending card computed 16px.", "div"),
            "shadow": shadow("0 1px 3px rgba(0, 0, 0, 0.05)", "trending card computed that shadow.", "div"),
        },
        "chart-card": {
            "background": color("#ffffff", "PositionCard container computed white.", "div.PositionCard_container__EG_jZ"),
            "radius": dim("12px", "PositionCard container computed 12px.", "div.PositionCard_container__EG_jZ"),
            "shadow": shadow("0 1px 2px rgba(0, 0, 0, 0.05)", "PositionCard computed rgba(0, 0, 0, 0.05) 0px 1px 2px 0px plus a 1px rgb(234, 234, 235) ring.", "div.PositionCard_container__EG_jZ"),
            "width": dim("216px", "PositionCard computed 216px wide and 92px tall.", "div.PositionCard_container__EG_jZ"),
            "height": dim("92px", "PositionCard computed 92px tall.", "div.PositionCard_container__EG_jZ"),
        },
        "dialog": {
            "background": color("#ffffff", "Platform menu computed white.", "[role=dialog]"),
            "border": color("rgba(0, 0, 0, 0.08)", "Platform menu border computed 1px solid rgba(0, 0, 0, 0.08).", "[role=dialog]"),
            "radius": dim("12px", "Platform menu computed 12px.", "[role=dialog]"),
            "padding": dim("20px", "Platform menu computed 20px.", "[role=dialog]"),
            "shadow": shadow("0 4px 20px rgba(0, 0, 0, 0.15)", "Platform menu computed that shadow.", "[role=dialog]"),
        },
    }


def canon(value):
    """One comparable spelling for a token value and a declared CSS value: lower case, no spaces or
    quotes, a cubic-bezier() and a 4-number list both as "cubic-bezier(a,b,c,d)", numbers without
    trailing zeros. So [0.4, 0, 0.2, 1] matches cubic-bezier(.4, 0, .2, 1) and "Inter", sans-serif
    matches the declaration's own quoting."""
    def num(x):
        f = float(x)
        return ("%g" % f)
    if isinstance(value, list) and len(value) == 4 and all(isinstance(x, (int, float)) for x in value):
        return "cubic-bezier(%s)" % ",".join(num(x) for x in value)
    text = value if isinstance(value, str) else json.dumps(value)
    text = text.lower().replace(" ", "").replace('"', "").replace("'", "")
    m = re.fullmatch(r"cubic-bezier\(([^)]*)\)", text)
    if m:
        return "cubic-bezier(%s)" % ",".join(num(x) for x in m.group(1).split(","))
    return text


def label_hand_entries(tokens):
    """raw/components.json holds no per-element reading (its note says they stayed in the capture
    notes), so a value is Measured only when the custom property its source names is declared with
    that value in raw/css-vars.json. Any other computed value was typed in: relabel it."""
    declared = VARS["declared"]

    def backed(node):
        detail = node["$extensions"]["source"].get("detail", "")
        value = canon(node["$value"])
        for name in re.findall(r"--[A-Za-z0-9_-]+", detail):
            for row in declared.get(name, []):
                raw = canon(row["val"])
                if raw in value or value == raw:
                    return True
        return False

    def walk(node):
        if isinstance(node, dict) and "$value" in node:
            source = node["$extensions"]["source"]
            if source["evidence"] == "Measured" and not (isinstance(node["$value"], str) and node["$value"].startswith("{")) and not backed(node):
                source["evidence"] = "Reconstruction"
                source["detail"] = ("Entered by hand at capture time; raw/components.json holds no per-element reading. "
                                    + source["detail"])
        elif isinstance(node, dict):
            for k, v in node.items():
                if not k.startswith("$"):
                    walk(v)

    for set_name, body in tokens.items():
        if not set_name.startswith("$"):
            walk(body)


def check(tokens):
    """Refuse a token with no source, a broken alias, or a dimension that is not one length."""
    problems = []

    def walk(node, path):
        if isinstance(node, dict) and "$value" in node:
            source = node.get("$extensions", {}).get("source", {})
            if source.get("evidence") not in ("Measured", "Derived", "Sampled", "Reconstruction", "Not captured"):
                problems.append(f"{path} has no evidence label")
            value = node["$value"]
            if node["$type"] == "dimension" and isinstance(value, str) and not value.startswith("{"):
                if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem|em)", value):
                    problems.append(f"{path} dimension {value!r} is not one length")
            if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
                # Resolve in the token's own set first, then core, as tools/catalog.py's Resolver does.
                target = value[1:-1].split(".")
                for root in (tokens[path.split(".")[0]], tokens["core"]):
                    cur = root
                    for part in target:
                        cur = cur.get(part) if isinstance(cur, dict) else None
                    if isinstance(cur, dict) and "$value" in cur:
                        break
                else:
                    problems.append(f"{path} alias {value} does not resolve")
        elif isinstance(node, dict):
            for k, v in node.items():
                if not k.startswith("$"):
                    walk(v, f"{path}.{k}" if path else k)

    for set_name, body in tokens.items():
        if set_name.startswith("$"):
            continue
        walk(body, set_name)
    if problems:
        raise SystemExit("token check failed:\n" + "\n".join(problems))


def build():
    tokens = {
        "$description": "The Org public signed-out surfaces, measured 2026-11-19. Light only.",
        "core": core(),
        "light": light(),
        "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    }
    label_hand_entries(tokens)
    check(tokens)
    return tokens


if __name__ == "__main__":
    out = HERE / "tokens.json"
    out.write_text(json.dumps(build(), indent=2) + "\n")
    print(f"wrote {out}")
