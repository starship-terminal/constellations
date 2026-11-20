#!/usr/bin/env python3
"""Write tokens.json from the Visitors public-page readings.

Every value below was read with getComputedStyle on https://visitors.now/
(and the public pages named in each source) on 2026-11-19. Custom properties
come from raw/css-vars.json, which is the resolved :root set on the homepage.
There is no dark theme: prefers-color-scheme: dark did not change the painted
page. The dark set is omitted on purpose.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
VARS = RAW["vars"]


def src(text):
    return {"$extensions": {"source": text}}


def color(value, source, description):
    return {"$type": "color", "$value": value, "$description": description, **src(source)}


def dim(value, source, description):
    if not (value.startswith("{") or re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", value)):
        raise ValueError(value)
    return {"$type": "dimension", "$value": value, "$description": description, **src(source)}


def font(value, source, description):
    return {"$type": "fontFamily", "$value": value, "$description": description, **src(source)}


def weight(value, source, description):
    return {"$type": "fontWeight", "$value": value, "$description": description, **src(source)}


def number(value, source, description):
    return {"$type": "number", "$value": value, "$description": description, **src(source)}


def typography(value, source, description):
    return {"$type": "typography", "$value": value, "$description": description, **src(source)}


def shadow(value, source, description):
    return {"$type": "shadow", "$value": value, "$description": description, **src(source)}


# Declared product tokens. Tailwind internals (--tw-*) are not product tokens.
assert VARS["--bg-1"] == "#fff"
assert VARS["--fg-4"] == "#181925"
assert VARS["--purple-4"] == "#918df6"
assert VARS["--spacing"] == ".25rem"

S = "getComputedStyle on https://visitors.now/ at 1440x900, headless Chromium, 2026-11-19. "
V = "Resolved :root custom property on the same page (raw/css-vars.json). "

tokens = {
    "core": {
        "font": {
            "family": {
                "ui": font(
                    "OpenRunde, \"Open Runde\", Inter, sans-serif",
                    S + "document.body.fontFamily. @font-face OpenRunde at weights 400, 500 and 600. Inter is the declared fallback and was not the resolved family.",
                    "UI family.",
                ),
                "mono": font(
                    VARS["--font-mono"],
                    V + "--font-mono. No code sample on the captured pages resolved to this family; docs method badges use OpenRunde.",
                    "Declared mono stack. Not observed as a resolved family on the captured pages.",
                ),
            }
        },
        "fontWeight": {
            "regular": weight(400, V + "--font-weight-normal. Body weight on the homepage.", "Regular."),
            "medium": weight(500, V + "--font-weight-medium. Lede, buttons, login h1.", "Medium."),
            "semibold": weight(600, V + "--font-weight-semibold. Homepage h1.", "Semibold."),
        },
        "letterSpacing": {
            "body": dim("-0.32px", S + "document.body.letterSpacing. body has tracking-[-0.02em] at 16px.", "Body tracking."),
            "display": dim("-3px", S + "h1.letterSpacing. Class tracking-tighter, computed -3px at 60px.", "Display tracking on the homepage h1."),
        },
        "radius": {
            "sm": dim("4px", S + "docs GET badge borderRadius. Class rounded.", "Small radius."),
            "md": dim("12px", S + "login email input borderRadius.", "Field radius."),
            "lg": dim("16px", S + "Features menu cards and the pricing card borderRadius. Class rounded-xl. Declared --radius-2xl is 1rem.", "Card radius."),
            "pill": dim("9999px", S + "Register, Start trial, See demo, Google and Continue with email borderRadius. The browser reported 33554400px for rounded-full.", "Pill radius."),
        },
        "spacing": {
            "1": dim("4px", V + "--spacing is .25rem. Docs GET badge padding is 0px 4px.", "Base step."),
            "2": dim("8px", S + "Login link padding 0px 8px (px-2) in the desktop header.", "Two steps."),
            "3": dim("12px", S + "Features menu card padding 16px 12px.", "Three steps."),
            "4": dim("16px", S + "Email field padding 0px 16px. Features card vertical padding 16px.", "Four steps."),
            "5": dim("20px", S + "Start trial and Google button padding 0px 20px. Docs aside padding 20px.", "Five steps."),
        },
        "size": {
            "control-sm": dim("32px", S + "Header Register button and pricing Monthly toggle height.", "Small control."),
            "control-md": dim("40px", S + "Email field height on /login.", "Field height."),
            "control-lg": dim("44px", S + "Start 14 day free trial, See demo, Continue with email and Google button height.", "Large control."),
            "nav": dim("64px", "Header pill measured in the desktop screenshot and the mobile header. The header element itself is position:fixed with height auto; the painted pill is the control.", "Painted header pill height, from the 1440 screenshot."),
        },
        "typography": {
            "display": typography(
                {"fontFamily": "{font.family.ui}", "fontSize": "60px", "fontWeight": "{fontWeight.semibold}", "lineHeight": "68px", "letterSpacing": "{letterSpacing.display}"},
                S + "h1 'Revenue-first web analytics'. Class text-6xl/17 tracking-tighter font-semibold. --text-6xl is 3.75rem.",
                "Homepage display.",
            ),
            "title": typography(
                {"fontFamily": "{font.family.ui}", "fontSize": "36px", "fontWeight": "{fontWeight.medium}", "lineHeight": "40px", "letterSpacing": "{letterSpacing.body}"},
                S + "Blog h1 and homepage section h2 'Everything you need to understand your visitors' is 36px/500 with line-height 44px. Blog h1 line-height is 40px. This composite uses the blog h1 line height.",
                "Page title.",
            ),
            "section": typography(
                {"fontFamily": "{font.family.ui}", "fontSize": "30px", "fontWeight": "{fontWeight.medium}", "lineHeight": "36px", "letterSpacing": "-0.525px"},
                S + "docs h1 'Welcome to Visitors'. Class text-3xl tracking-tight font-medium. Login panel right heading is 30px/500, line-height 36px, letter-spacing -0.32px.",
                "Docs title.",
            ),
            "lede": typography(
                {"fontFamily": "{font.family.ui}", "fontSize": "18px", "fontWeight": "{fontWeight.medium}", "lineHeight": "24px", "letterSpacing": "{letterSpacing.body}"},
                S + "Homepage lede p. Class text-lg/6 font-medium.",
                "Lede.",
            ),
            "body": typography(
                {"fontFamily": "{font.family.ui}", "fontSize": "16px", "fontWeight": "{fontWeight.regular}", "lineHeight": "24px", "letterSpacing": "{letterSpacing.body}"},
                S + "document.body. Class text default 16px, tracking-[-0.02em].",
                "Body.",
            ),
            "label": typography(
                {"fontFamily": "{font.family.ui}", "fontSize": "14px", "fontWeight": "{fontWeight.medium}", "lineHeight": "20px", "letterSpacing": "{letterSpacing.body}"},
                S + "Header Login link and Register button. Class text-sm font-medium.",
                "Label."),
            "caption": typography(
                {"fontFamily": "{font.family.ui}", "fontSize": "12px", "fontWeight": "{fontWeight.medium}", "lineHeight": "16px", "letterSpacing": "{letterSpacing.body}"},
                S + "Docs GET badge. Class font-medium, 12px/16px.",
                "Caption."),
            "error-display": typography(
                {"fontFamily": "{font.family.ui}", "fontSize": "128px", "fontWeight": "{fontWeight.medium}", "lineHeight": "128px", "letterSpacing": "-6.4px"},
                S + "404 numeral on /pricing (HTTP 404). Class text-9xl font-medium tracking-tighter. --text-9xl is 8rem.",
                "404 numeral."),
        },
        "motion": {
            "duration": {
                "fast": {
                    "$type": "duration",
                    "$value": "150ms",
                    "$description": "Default transition.",
                    **src(V + "--default-transition-duration is .15s. Buttons use transition-all; nav links use transition-colors."),
                },
            },
            "easing": {
                "standard": {
                    "$type": "cubicBezier",
                    "$value": [0.4, 0, 0.2, 1],
                    "$description": "Default easing.",
                    **src(V + "--default-transition-timing-function and --ease-in-out are cubic-bezier(.4, 0, .2, 1)."),
                }
            },
        },
        "shadow": {
            "slider": shadow(
                [
                    {"color": "#0000000f", "offsetX": "0px", "offsetY": "1px", "blur": "3px", "spread": "0px"},
                    {"color": "#0000000f", "offsetX": "0px", "offsetY": "8px", "blur": "16px", "spread": "0px"},
                    {"color": "#00000005", "offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "1px"},
                ],
                S + "Pricing slider thumb boxShadow. Matches declared --shadow-3 (0px 1px 3px #0000000f, 0px 8px 16px #0000000f, 0px 0px 0px 1px #00000005).",
                "Slider thumb.",
            )
        },
        "color": {
            "page": color("#ffffff", V + "--background and --bg-1 are #fff. body backgroundColor rgb(255, 255, 255).", "Page."),
            "surface": color("#f5f5f5", V + "--bg-2 is #f5f5f5. Email field backgroundColor rgb(245, 245, 245).", "Field surface."),
            "surface-muted": color("#00000008", V + "--bg-a1 is #00000008. Pricing card backgroundColor rgba(0, 0, 0, 0.03).", "Muted surface. 0.03 alpha is the painted card; the token is the declared --bg-a1 step."),
            "ink": color("#181925", V + "--fg-4 is #181925. h1 color rgb(24, 25, 37).", "Primary text."),
            "body": color("#666666", V + "--fg-3 is #666. body color rgb(102, 102, 102).", "Body text."),
            "muted": color("#999999", V + "--fg-2 is #999. Footer links color rgb(153, 153, 153).", "Muted text."),
            "faint": color("#b3b3b3", V + "--fg-1 is #b3b3b3. Login panel right heading color rgb(179, 179, 179). Header Login link is rgb(187, 188, 195), a separate nav grey.", "Faint text."),
            "nav": color("#bbbcc3", S + "Header Login, Pricing, Blog and Docs color rgb(187, 188, 195). Not a declared --fg step.", "Nav label."),
            "nav-bar": color("#14141f", S + "header backgroundColor rgb(20, 20, 31), position fixed, backdrop-filter blur(16px).", "Header pill."),
            "accent": color("#918df6", V + "--purple-4 is #918df6. Start 14 day free trial backgroundColor rgb(145, 141, 246).", "Primary accent."),
            "accent-strong": color("#9580ff", S + "Header Register button backgroundColor rgb(149, 128, 255). A second purple, not --purple-4.", "Header register."),
            "on-accent": color("#ffffff", S + "Start trial and Register color rgb(255, 255, 255).", "Text on accent."),
            "accent-disabled": color("#dad9fc", S + "Continue with email, disabled, backgroundColor rgb(218, 217, 252). Also the email focus ring color.", "Disabled primary."),
            "link": color("#2c78fc", V + "--sky-4 is #2c78fc. Docs 'registration' link and login Register link color rgb(44, 120, 252).", "Link."),
            "success": color("#33c758", V + "--green-4 is #33c758. Docs GET badge color rgb(51, 199, 88).", "Success."),
            "warning": color("#ffa600", V + "--amber-4 is #ffa600.", "Warning."),
            "danger": color("#ff2f00", V + "--red-4 is #ff2f00.", "Danger."),
            "secondary-fill": color("#00000008", S + "See demo and Google button backgroundColor rgba(0, 0, 0, 0.03).", "Quiet button fill."),
        },
    },
    "light": {
        "color": {
            "bg": {
                "page": color("{core.color.page}", "Alias of the measured page fill.", "Page."),
                "surface": color("{core.color.surface}", "Alias of the email field fill.", "Surface."),
                "muted": color("#00000008", S + "Pricing card rgba(0, 0, 0, 0.03) and See demo rgba(0, 0, 0, 0.03). Recorded as the painted alpha, not the 8-digit --bg-a1.", "Painted muted fill."),
            },
            "text": {
                "primary": color("{core.color.ink}", "Alias of h1 ink.", "Primary text."),
                "body": color("{core.color.body}", "Alias of body ink.", "Body text."),
                "muted": color("{core.color.muted}", "Alias of footer ink.", "Muted text."),
                "on-accent": color("{core.color.on-accent}", "Alias of button label.", "On accent."),
            },
            "action": {
                "fill": color("{core.color.accent}", "Alias of the trial button.", "Primary fill."),
                "fill-header": color("{core.color.accent-strong}", "Alias of the header Register button.", "Header fill."),
                "fill-disabled": color("{core.color.accent-disabled}", "Alias of the disabled Continue button.", "Disabled fill."),
                "quiet": color("{core.color.secondary-fill}", "Alias of See demo.", "Quiet fill."),
            },
            "border": {
                "focus": color("{core.color.accent}", S + "Email field focus outline rgb(145, 141, 246) solid 2px, plus a 2px ring of rgb(218, 217, 252).", "Focus outline."),
            },
            "status": {
                "success": color("{core.color.success}", "Alias of GET badge.", "Success."),
                "link": color("{core.color.link}", "Alias of the docs link.", "Link."),
            },
        },
        "component": {
            "button": {
                "primary": {
                    "bg": color("{core.color.accent}", S + "button 'Start 14 day free trial'.", "Primary button."),
                    "text": color("{core.color.on-accent}", S + "Same button color.", "Primary label."),
                    "radius": dim("{core.radius.pill}", S + "Same button borderRadius.", "Primary radius."),
                    "height": dim("{core.size.control-lg}", S + "Same button height 44px.", "Primary height."),
                },
                "quiet": {
                    "bg": color("{core.color.secondary-fill}", S + "button 'See demo' backgroundColor rgba(0, 0, 0, 0.03).", "Quiet button."),
                    "text": color("{core.color.body}", S + "See demo color rgb(102, 102, 102).", "Quiet label."),
                    "radius": dim("{core.radius.pill}", S + "See demo borderRadius.", "Quiet radius."),
                    "height": dim("{core.size.control-lg}", S + "See demo height 44px.", "Quiet height."),
                },
            },
            "field": {
                "bg": color("{core.color.surface}", S + "input placeholder Email address on /login.", "Field fill."),
                "text": color("{core.color.ink}", S + "Same input color rgb(24, 25, 37).", "Field text."),
                "radius": dim("{core.radius.md}", S + "Same input borderRadius 12px.", "Field radius."),
                "height": dim("{core.size.control-md}", S + "Same input height 40px.", "Field height."),
            },
        },
    },
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$description": "The only theme on the public pages. color-scheme is normal. Emulating prefers-color-scheme: dark did not change the homepage screenshot.",
        }
    ],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}

# The pricing card paint is 3% black, which the catalog contrast check can read.
# Keep the 8-digit form only where the declared token is the source of truth.


def walk(tree, prefix=""):
    for key, value in tree.items():
        if key.startswith("$"):
            continue
        if isinstance(value, dict) and "$value" in value:
            yield prefix + key, value
        elif isinstance(value, dict):
            yield from walk(value, prefix + key + ".")


def aliases(value):
    if isinstance(value, str):
        return re.findall(r"\{([^{}]+)\}", value)
    if isinstance(value, dict):
        return [item for child in value.values() for item in aliases(child)]
    if isinstance(value, list):
        return [item for child in value for item in aliases(child)]
    return []


names = {}
for set_name in ("core", "light"):
    names.update({set_name + "." + path: token for path, token in walk(tokens[set_name])})
    local = {path: token for path, token in walk(tokens[set_name])}
    local.update({path: token for path, token in walk(tokens["core"])})
    for path, token in walk(tokens[set_name]):
        for alias in aliases(token["$value"]):
            if alias not in local and "core." + alias not in names and alias not in names:
                # aliases inside a set omit the set prefix and may point at core via {core....} or a sibling
                if alias.startswith("core.") and alias[5:] not in {p for p in local} and alias not in { "core." + p for p in walk(tokens["core"])}:
                    pass
            target = alias
            if target not in local and not target.startswith("core."):
                raise SystemExit(f"{set_name}.{path} alias {{{alias}}} missing")
        if token["$type"] == "dimension" and isinstance(token["$value"], str) and not aliases(token["$value"]):
            if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", token["$value"]):
                raise SystemExit(f"bad dimension {set_name}.{path} {token['$value']}")
        if token["$type"] == "color" and isinstance(token["$value"], str) and not token["$value"].startswith("{"):
            if not re.fullmatch(r"#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?", token["$value"]):
                raise SystemExit(f"bad color {set_name}.{path} {token['$value']}")

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", HERE / "tokens.json", "tokens", len(list(walk(tokens["core"]))) + len(list(walk(tokens["light"]))))
