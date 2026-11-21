#!/usr/bin/env python3
"""Build systems/weavy/tokens.json from the public CSS readings.

Sources, read on 2026-11-21 from weave.figma.com (www.weavy.ai redirects there):
  raw/css-vars.json            custom properties declared on :root in
                               weavy-ai.webflow.shared.12c2e7cf9.css, resolved
                               on the home page
  raw/component-tokens.json    computed styles of the controls that paint

The marketing site ships one theme. There is no dark set. Unread values stay
out of the file; the README coverage table marks them Not captured.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"


def tok(value, ty, source):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def put(tree, path, token):
    node = tree
    for key in path[:-1]:
        node = node.setdefault(key, {})
    node[path[-1]] = token


def color(value):
    value = value.strip()
    named = {"white": "#ffffff", "black": "#000000", "azure": "#f0ffff"}
    if value.lower() in named:
        return named[value.lower()]
    match = re.fullmatch(r"#([0-9a-fA-F]{3,8})", value)
    if match:
        hex_value = match.group(1)
        if len(hex_value) in (3, 4):
            hex_value = "".join(ch * 2 for ch in hex_value)
        rgb = [int(hex_value[i:i + 2], 16) for i in (0, 2, 4)]
        if len(hex_value) == 8:
            alpha = int(hex_value[6:8], 16) / 255
            if alpha >= 0.999:
                return "#%02x%02x%02x" % tuple(rgb)
            return "rgba(%d, %d, %d, %g)" % (*rgb, round(alpha, 3))
        return "#%02x%02x%02x" % tuple(rgb)
    match = re.fullmatch(r"rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)", value)
    if match:
        rgb = [int(match.group(i)) for i in (1, 2, 3)]
        alpha = float(match.group(4)) if match.group(4) else 1
        if alpha >= 0.999:
            return "#%02x%02x%02x" % tuple(rgb)
        return "rgba(%d, %d, %d, %g)" % (*rgb, round(alpha, 3))
    raise ValueError("colour not understood: " + value)


def px(value):
    match = re.fullmatch(r"(-?\d*\.?\d+)px", str(value).strip())
    if not match:
        raise ValueError("not a px length: %r" % value)
    return "%gpx" % round(float(match.group(1)), 3)


VARS = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())
RESOLVED = VARS["resolved"]
ROOT = "css-var %s (:root in weavy-ai.webflow.shared.12c2e7cf9.css, resolved on https://weave.figma.com/)"

core = {}
brand = {
    "lemon": "--brand--lemon",
    "lemon-100": "--brand--lemon-100",
    "lemon-40": "--brand--lemon-40",
    "rich-black": "--brand--rich-black",
    "richer-black": "--brand--richer-black",
    "black": "--brand--base--black",
    "white": "--brand--base--white",
    "azure": "--brand--azure",
    "ash-grey": "--brand--ash-grey",
    "eggshell": "--brand--eggshell",
    "spring-wood": "--brand--spring-wood",
    "moon-mist": "--brand--moon-mist",
    "french-gray": "--brand--french-gray",
    "pink-lavender": "--pink-lavender",
    "stone-grey": "--stone-grey",
    "paper": "--wv--paper",
    "ink": "--wv--ink",
    "dark": "--wv--dark",
    "pink": "--wv--pink",
    "mint": "--wv--mint",
    "night": "--wv--night",
    "cream": "--wv--cream",
    "grey-100": "--wv--grey-100",
    "grey-400": "--wv--grey-400",
    "grey-500": "--wv--grey-500",
    "surface-grey-300": "--brand--base--surface--grey-300",
    "surface-grey-400": "--brand--base--surface--grey-400",
    "soft-grey-200": "--border--soft-grey-200",
    "french-gray-45": "--brand--french-gray-op-45",
    "white-30": "--brand--white-op-30",
    "transparent-surface": "--transparent-surface",
}
for leaf, name in brand.items():
    put(core, ["color", "brand", leaf], tok(color(RESOLVED[name]), "color", ROOT % name))

put(core, ["fontFamily", "sans"], tok(
    "Figma Sans Regular, Arial, sans-serif", "fontFamily",
    "Measured computed font-family on body, nav, hero h1 and plan cards at https://weave.figma.com/. "
    "The stylesheet @font-face names the face and points at a woff2 on cdn.prod.website-files.com. "
    "Figma Sans is proprietary; the stack falls back to Arial."))
put(core, ["fontFamily", "sans-vf"], tok(
    "Figma Sans Vf, Arial, sans-serif", "fontFamily",
    "Declared @font-face in weavy-ai.webflow.shared.12c2e7cf9.css (Figma-Sans-VF.ttf). "
    "Not the computed family of the measured controls."))
put(core, ["fontFamily", "meta"], tok(
    "Dmsans, Arial, sans-serif", "fontFamily",
    "Measured on .billing-toggle_badge (Save 30%). @font-face Dmsans loads DM Sans woff2 at weights 200, 400, 500 and 600."))

# Type roles measured on the live home and pricing pages.
for leaf, size, line, tracking, source in (
    ("display", "94px", "79.9px", "-4.32px", "Measured .heading_h1-hero on https://weave.figma.com/ (Figma Weave)"),
    ("heading", "94px", "82px", "-4.608px", "Measured .heading-style-xl on the home page"),
    ("title", "56px", "67.2px", "0px", "Derived from .heading-style-h1 { font-size: 3.5rem; line-height: 1.2; font-weight: 700 } at a 16px root. The live hero does not use this class"),
    ("body", "14.4px", "20px", "0px", "Measured computed font-size and line-height on body and .pricing_plan-v4"),
    ("label", "12px", "16px", "0.15px", "Measured .nav_text-link (uppercase, letter-spacing 0.15px). Line-height Not captured as a separate token; 16px is the element's used line box, Derived"),
    ("caption", "13px", "16.9px", "0.1px", "Measured .billing-toggle_badge"),
    ("button", "14.4px", "20px", "0px", "Measured .button.w-button (Start free)"),
    ("cta", "40px", "40px", "0px", "Measured a.huge_nav-button.is-real (Start Now). CSS declares 2.77778rem"),
):
    put(core, ["fontSize", leaf], tok(px(size), "dimension", source))
    put(core, ["lineHeight", leaf], tok(px(line), "dimension", source))

put(core, ["fontWeight", "regular"], tok(400, "fontWeight", "Measured font-weight 400 on the hero, nav, plan button and body"))
put(core, ["fontWeight", "bold"], tok(700, "fontWeight", "Declared font-weight 700 on .heading-style-h1. The live hero computed 400"))

put(core, ["typography", "display"], tok(
    {"fontFamily": "{fontFamily.sans}", "fontSize": "{fontSize.display}", "fontWeight": "{fontWeight.regular}", "lineHeight": "{lineHeight.display}", "letterSpacing": "-4.32px"},
    "typography", "Measured .heading_h1-hero"))
put(core, ["typography", "heading"], tok(
    {"fontFamily": "{fontFamily.sans}", "fontSize": "{fontSize.heading}", "fontWeight": "{fontWeight.regular}", "lineHeight": "{lineHeight.heading}", "letterSpacing": "-4.608px"},
    "typography", "Measured .heading-style-xl"))
put(core, ["typography", "body"], tok(
    {"fontFamily": "{fontFamily.sans}", "fontSize": "{fontSize.body}", "fontWeight": "{fontWeight.regular}", "lineHeight": "{lineHeight.body}", "letterSpacing": "0px"},
    "typography", "Measured body"))
put(core, ["typography", "label"], tok(
    {"fontFamily": "{fontFamily.sans}", "fontSize": "{fontSize.label}", "fontWeight": "{fontWeight.regular}", "lineHeight": "{lineHeight.label}", "letterSpacing": "0.15px"},
    "typography", "Measured .nav_text-link"))
put(core, ["typography", "caption"], tok(
    {"fontFamily": "{fontFamily.meta}", "fontSize": "{fontSize.caption}", "fontWeight": "{fontWeight.regular}", "lineHeight": "{lineHeight.caption}", "letterSpacing": "0.1px"},
    "typography", "Measured .billing-toggle_badge"))
put(core, ["typography", "button"], tok(
    {"fontFamily": "{fontFamily.sans}", "fontSize": "{fontSize.button}", "fontWeight": "{fontWeight.regular}", "lineHeight": "{lineHeight.button}", "letterSpacing": "0px"},
    "typography", "Measured .button.w-button"))

# Spacing: measured padding, not a declared scale.
for leaf, value, source in (
    ("2", "2px", "Measured padding on .billing-toggle_badge"),
    ("6", "6px", "Measured horizontal padding on .billing-toggle_badge"),
    ("8", "8px", "Declared border-bottom-left-radius 8px on .huge_nav-button.is-real"),
    ("11", "10.8px", "Measured vertical padding on .button.w-button"),
    ("13", "12.76px", "Measured padding-left on a.huge_nav-button.is-real"),
    ("21", "21.07px", "Measured padding on .pricing_plan-v4"),
    ("22", "21.6px", "Measured horizontal padding on .button.w-button"),
    ("24", "24.36px", "Measured padding-right on a.huge_nav-button.is-real"),
):
    put(core, ["spacing", leaf], tok(px(value), "dimension", source))

for leaf, value, source in (
    ("badge", "2px", "Measured border-radius on .billing-toggle_badge"),
    ("control", "4px", "Measured border-radius on .button.w-button and .audience-tabs_link"),
    ("nav", "8px", "Declared border-bottom-left-radius 8px on .huge_nav-button.is-real. The computed radius of that fixed button was 0px"),
    ("search", "8px", "Measured border-radius on the knowledge-center search input"),
    ("card", "13px", "Measured border-radius on .pricing_plan-v4"),
    ("pill", "144px", "Measured border-radius on .billing-toggle_switch (32x16)"),
):
    put(core, ["radius", leaf], tok(px(value), "dimension", source))

put(core, ["borderWidth", "hairline"], tok("1px", "dimension", "Measured border-top-width 1px on .pricing_plan-v4"))
put(core, ["duration", "nav"], tok("200ms", "duration", "Declared transition all .2s on .huge_nav-button.is-real"))
put(core, ["easing", "nav"], tok([0.25, 0.46, 0.45, 0.94], "cubicBezier", "Declared cubic-bezier(.25, .46, .45, .94) on .huge_nav-button.is-real"))
put(core, ["size", "nav-cta-height"], tok("89.9px", "dimension", "Measured height of a.huge_nav-button.is-real at 1440"))
put(core, ["size", "plan-button-height"], tok("41.6px", "dimension", "Measured height of .button.w-button Start free"))
put(core, ["size", "switch"], tok("32px", "dimension", "Measured width of .billing-toggle_switch; height 16px"))
put(core, ["size", "audience-tab-height"], tok("38px", "dimension", "Measured height of .audience-tabs_link"))
put(core, ["layout", "desktop"], tok("1440px", "dimension", "Requested and measured viewport width, window.innerWidth 1440"))
put(core, ["layout", "phone"], tok("390px", "dimension", "Requested and measured viewport width, window.innerWidth 390"))
put(core, ["layout", "content"], tok("1310px", "dimension", "Measured width of .pricing-grid at 1440"))
put(core, ["layout", "breakpoint-tablet"], tok("991px", "dimension", "Declared @media screen and (max-width: 991px) in the Webflow stylesheet"))
put(core, ["layout", "breakpoint-phone"], tok("767px", "dimension", "Declared @media screen and (max-width: 767px)"))
put(core, ["layout", "breakpoint-small"], tok("479px", "dimension", "Declared @media screen and (max-width: 479px)"))

light = {}
roles = {
    ("color", "page"): ("#ffffff", "Measured body background-color rgb(255, 255, 255). Aliases {color.brand.white}"),
    ("color", "surface"): ("#f5f5f6", "Measured .pricing_plan-v4 background. Same as --brand--base--surface--grey-300"),
    ("color", "surface-muted"): ("#ececec", "css-var --brand--base--surface--grey-400"),
    ("color", "inverse"): ("#252525", "Measured footer background and plan-button fill. Same as --brand--rich-black"),
    ("color", "ink"): ("#000000", "Measured hero h1 color"),
    ("color", "text"): ("#333333", "Measured body color rgb(51, 51, 51)"),
    ("color", "text-on-inverse"): ("#ffffff", "Measured .nav_text-link and plan-button text"),
    ("color", "text-on-accent-hover"): ("#f4f4f4", "Measured color of a.huge_nav-button.is-real:hover. CSS declares #f4f4f4"),
    ("color", "muted"): ("#656568", "css-var --stone-grey. Used as a quiet label; not measured on a specific muted paragraph"),
    ("color", "accent"): ("#f7ff9e", "css-var --brand--lemon, measured as the Start Now fill rgb(247, 255, 158)"),
    ("color", "accent-hover"): ("#252525", "Measured a.huge_nav-button.is-real:hover background. CSS .huge_nav-button.is-real:hover"),
    ("color", "button"): ("#252525", "Measured .button.w-button background"),
    ("color", "button-hover"): ("#eaf297", "Measured Start free :hover background rgb(234, 242, 151)"),
    ("color", "button-pressed"): ("#f7ff9e", "Measured Start free while the pointer was held down"),
    ("color", "button-text-hover"): ("#2f2f33", "Measured Start free :hover color"),
    ("color", "tab-selected"): ("#212126", "Measured .audience-tabs_link.w--current background rgb(33, 33, 38)"),
    ("color", "border"): ("#e6e6e6", "Measured .pricing_plan-v4 border-top-color"),
    ("color", "border-strong"): ("#d0d0d2", "css-var --border--soft-grey-200"),
    ("color", "help-page"): ("#232329", "Sampled from the knowledge-center screenshot is not used. Measured collection-card background rgb(35, 35, 41) is the raised surface; page fill was not read as a computed style and is Not captured as a separate token beyond the card"),
}
# fix help-page: don't invent. Use card only.
del roles[("color", "help-page")]
put(light, ["color", "help-card"], tok("#232329", "color", "Measured a[href*='/collections/'] background rgb(35, 35, 41) on https://help.weavy.ai/en/"))
put(light, ["color", "help-card-border"], tok("rgba(255, 255, 255, 0.15)", "color", "Measured collection-card border-top-color"))
put(light, ["color", "search-text"], tok("#1a1a1a", "color", "Measured knowledge-center input color rgb(26, 26, 26)"))

for (group, leaf), (value, source) in roles.items():
    put(light, [group, leaf], tok(color(value) if not value.startswith("rgba") else value, "color", source))

put(light, ["shadow", "card"], tok(
    [{"color": "rgba(0, 0, 0, 0.05)", "offsetX": "0px", "offsetY": "1px", "blur": "2px", "spread": "0px"}],
    "shadow", "Measured box-shadow on a knowledge-center collection card"))

# component tokens the style guide and DESIGN.md can read
put(light, ["component", "button-primary", "background"], tok("{color.button}", "color", "alias of the measured plan button"))
put(light, ["component", "button-primary", "text"], tok("{color.text-on-inverse}", "color", "alias of the measured plan button text"))
put(light, ["component", "button-primary", "radius"], tok("{radius.control}", "dimension", "alias"))
put(light, ["component", "button-primary", "height"], tok("{size.plan-button-height}", "dimension", "alias"))
put(light, ["component", "nav-cta", "background"], tok("{color.accent}", "color", "alias of Start Now"))
put(light, ["component", "nav-cta", "text"], tok("{color.ink}", "color", "alias of Start Now text"))
put(light, ["component", "nav-cta", "height"], tok("{size.nav-cta-height}", "dimension", "alias"))
put(light, ["component", "card", "background"], tok("{color.surface}", "color", "alias of the plan card"))
put(light, ["component", "card", "radius"], tok("{radius.card}", "dimension", "alias"))
put(light, ["component", "card", "border"], tok("{color.border}", "color", "alias"))

doc = {
    "$schema": "https://tr.designtokens.org/format/",
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
    }],
}
(HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", HERE / "tokens.json")
