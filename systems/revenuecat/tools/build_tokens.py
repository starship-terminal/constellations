#!/usr/bin/env python3
"""Build tokens.json from raw/readings.json.

Values are the ones preview_evaluate read on 2026-11-19. HSL triplets were
resolved with getComputedStyle. Lab colours that the browser would not convert
were filled on a 1x1 sRGB canvas from the same lab() string. Nothing here is
recalled from memory of the product.

Two products share the slug. The public marketing site (www.revenuecat.com)
is light only. The signed-out app (app.revenuecat.com) ships a light token
sheet on :root, .light and a dark sheet on .dark. The live login and signup
pages had html.dark, so the dark sheet is what was on screen. The light app
sheet was read from the stylesheet, not from a live light page.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "readings.json").read_text())
M = RAW["marketing"]
APP = RAW["app"]


def src(evidence, **extra):
    data = {"evidence": evidence, "captured": RAW["captured"]}
    data.update(extra)
    return {"source": data}


def color(value, evidence, **extra):
    return {"$type": "color", "$value": value, "$extensions": src(evidence, **extra)}


def dim(value, evidence, **extra):
    return {"$type": "dimension", "$value": value, "$extensions": src(evidence, **extra)}


def num(value, type_, evidence, **extra):
    return {"$type": type_, "$value": value, "$extensions": src(evidence, **extra)}


def font(value, evidence, **extra):
    return {"$type": "fontFamily", "$value": value, "$extensions": src(evidence, **extra)}


def typo(family, size, weight, line, tracking, evidence, **extra):
    value = {
        "fontFamily": family,
        "fontSize": size,
        "fontWeight": weight,
        "lineHeight": line,
    }
    if tracking is not None:
        value["letterSpacing"] = tracking
    return {"$type": "typography", "$value": value, "$extensions": src(evidence, **extra)}


def shadow(layers, evidence, **extra):
    return {"$type": "shadow", "$value": layers, "$extensions": src(evidence, **extra)}


MARKETING = "www.revenuecat.com computed style, 1440x900, light"
APP_DARK = "app.revenuecat.com/login computed style, html.dark, 1440x900"
APP_SHEET = "app.revenuecat.com stylesheet :root,.light and .dark, aliases to --rc-*"


def marketing_colors():
    out = {}
    for name, row in M["customPropertiesResolvedOnRoot"].items():
        key = name.lstrip("-")
        hex_value = row["hex"]
        evidence = "Measured"
        note = row.get("note")
        if "canvasSrgb" in row:
            evidence = "Derived"
            extra = {"raw": row["raw"], "note": note or "sRGB from a canvas fill of the declared lab() string"}
        else:
            extra = {"raw": row["raw"], "computed": row.get("computed", hex_value)}
        out[key] = color(hex_value, evidence, where=MARKETING, **extra)
    return out


def app_ramps():
    """The --rc-* ramps, as declared hex on the app root."""
    # Kept inline because readings.json stores the resolved marketing sheet,
    # and the app ramps were read as raw hex in the same session. The builder
    # does not invent a step: each value is the raw custom property.
    ramps = {
        "neutral": {
            "10": "#f9fafc", "20": "#f2f3f5", "30": "#dfe1e6", "40": "#cbcdd4",
            "50": "#a2a4ab", "60": "#75777e", "70": "#505259", "80": "#2d2f35",
            "90": "#1d1f25", "100": "#14161b",
        },
        "blue": {
            "10": "#f6f8ff", "20": "#e6ecff", "30": "#d0dbff", "40": "#b4c5fe",
            "50": "#778aff", "60": "#606dff", "70": "#5256fd", "80": "#4847e7",
            "90": "#343794", "100": "#1f1f4f",
        },
        "green": {
            "10": "#f0fcf3", "20": "#d7f6e0", "30": "#b2edc3", "40": "#75e298",
            "50": "#34de70", "60": "#00c950", "70": "#04a13b", "80": "#007b30",
            "90": "#125429", "100": "#082f16",
        },
        "red": {
            "10": "#fff6f6", "20": "#fee6e6", "30": "#fdcfd1", "40": "#feafb2",
            "50": "#f66f78", "60": "#f2545b", "70": "#de2a39", "80": "#b9212e",
            "90": "#7e1c27", "100": "#471014",
        },
        "orange": {
            "10": "#fef7ec", "20": "#fbebd1", "30": "#fad7a2", "40": "#f9ba64",
            "50": "#fc9612", "60": "#ff8200", "70": "#dc5708", "80": "#ac3c05",
            "90": "#772a06", "100": "#421706",
        },
        "yellow": {
            "10": "#fdfdeb", "20": "#fcfdcd", "30": "#f4f39d", "40": "#f1e763",
            "50": "#f0d81b", "60": "#ecc200", "70": "#b98d07", "80": "#8a5b01",
            "90": "#643c00", "100": "#3b1e00",
        },
        "violet": {
            "10": "#f9f7ff", "20": "#eeeafe", "30": "#ded6fe", "40": "#cbbcfe",
            "50": "#a885ff", "60": "#8e51ff", "70": "#8531fc", "80": "#7624e7",
            "90": "#521d9e", "100": "#2c0b61",
        },
        "teal": {
            "10": "#f0fcf9", "20": "#cdf8ee", "30": "#9af0de", "40": "#56e2cb",
            "50": "#16d2bb", "60": "#00bba7", "70": "#0d988a", "80": "#0d766d",
            "90": "#16514b", "100": "#062d2b",
        },
        "pink": {
            "10": "#fef6fc", "20": "#f8e6f5", "30": "#f3cfee", "40": "#f3ade6",
            "50": "#eb76d4", "60": "#d843b9", "70": "#c6269f", "80": "#aa2283",
            "90": "#751d59", "100": "#450932",
        },
    }
    out = {}
    for ramp, steps in ramps.items():
        out[ramp] = {
            step: color(value, "Measured", where="app.revenuecat.com --rc-%s-%s" % (ramp, step), selector=":root")
            for step, value in steps.items()
        }
    out["white"] = color("#ffffff", "Measured", where="app.revenuecat.com --rc-white")
    out["black"] = color("#000000", "Measured", where="app.revenuecat.com --rc-black")
    return out


def core():
    scales = M["scales"]
    return {
        "font": {
            "family": {
                "helvetica-neue": font(
                    'helveticaNeue, "helveticaNeue Fallback", ui-sans-serif, system-ui, sans-serif',
                    "Measured", where=MARKETING, element="body"),
                "object-sans": font(
                    'objectSans, "objectSans Fallback", ui-sans-serif, system-ui, sans-serif',
                    "Measured", where=MARKETING, element="h1"),
                "ibm-plex-mono": font(
                    '"IBM Plex Mono", "IBM Plex Mono Fallback", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace',
                    "Measured", where=MARKETING, note="Declared as --default-mono-font-family. No visible element on the home page used it at rest."),
                "inter": font(
                    '"Inter Variable", sans-serif',
                    "Measured", where=APP_DARK, element="body"),
            }
        },
        "fontWeight": {
            name: num(int(value), "fontWeight", "Measured", where=MARKETING, property="--font-weight-%s" % name)
            for name, value in scales["fontWeight"].items()
        },
        "typography": {
            "display": typo("{font.family.object-sans}", "60px", "{fontWeight.medium}", "67.5px", "-2.4px",
                            "Measured", where=MARKETING, element="h1"),
            "display-phone": typo("{font.family.object-sans}", "30px", "{fontWeight.medium}", "33.75px", "-1.2px",
                                  "Measured", where="www.revenuecat.com h1 at innerWidth 390"),
            "title": typo("{font.family.object-sans}", "56px", "{fontWeight.medium}", "63px", "-2.24px",
                          "Measured", where=MARKETING, element="h2"),
            "section": typo("{font.family.object-sans}", "32px", "{fontWeight.medium}", "36px", "-0.64px",
                            "Measured", where=MARKETING, element="h2.Get started in minutes"),
            "pricing-display": typo("{font.family.object-sans}", "64px", "{fontWeight.medium}", "72px", "-1.6px",
                                    "Measured", where="www.revenuecat.com/pricing h1"),
            "lede": typo("{font.family.helvetica-neue}", "20px", "{fontWeight.normal}", "27.5px", "0px",
                         "Measured", where=MARKETING, element="hero p"),
            "body": typo("{font.family.helvetica-neue}", "16px", "{fontWeight.normal}", "24px", "0px",
                         "Measured", where=MARKETING, element="body"),
            "nav": typo("{font.family.object-sans}", "14px", "{fontWeight.normal}", "20px", "0px",
                        "Measured", where=MARKETING, element="header Pricing link"),
            "stat": typo("{font.family.object-sans}", "24px", "{fontWeight.medium}", "33px", "-0.48px",
                         "Measured", where=MARKETING, element="166K+"),
            "card-title": typo("{font.family.helvetica-neue}", "18px", "{fontWeight.medium}", "28px", "0px",
                               "Measured", where=MARKETING, element="article h3"),
            "app-heading": typo("{font.family.object-sans}", "24px", "700", "32px", "0px",
                                "Measured", where=APP_DARK, element="h2 Log in",
                                note="Computed font-family was ObjectSans. Weight 700 is not on the marketing weight scale token."),
            "app-body": typo("{font.family.inter}", "14px", "{fontWeight.normal}", "20px", "0px",
                             "Measured", where=APP_DARK, element="body"),
            "app-label": typo("{font.family.inter}", "14px", "{fontWeight.medium}", "20px", "0px",
                              "Measured", where=APP_DARK, element="label Email"),
        },
        "radius": {
            name: dim(value, "Measured", where=MARKETING, property="--radius-%s" % name)
            for name, value in scales["radius"].items()
        },
        "spacing": {
            "base": dim("0.25rem", "Measured", where=MARKETING, property="--spacing"),
            "header": dim("64px", "Measured", where=MARKETING, element="header height"),
            "button-x": dim("18px", "Measured", where=MARKETING, element="Sign up padding-inline"),
            "button-x-lg": dim("28px", "Measured", where=MARKETING, element="hero Start for free padding-inline"),
            "field-x": dim("28px", "Measured", where=MARKETING, element="email field padding-left"),
            "card": dim("16px", "Measured", where=MARKETING, element="article border-radius, also --radius-2xl"),
        },
        "size": {
            "button-sm": dim("36px", "Measured", where=MARKETING, element="header Sign up"),
            "button-md": dim("48px", "Measured", where=MARKETING, element="hero Start for free"),
            "button-phone": dim("44px", "Measured", where="www.revenuecat.com hero button at 390"),
            "field": dim("64px", "Measured", where=MARKETING, element="email input"),
            "menu-button": dim("40px", "Measured", where="www.revenuecat.com Menu button at 390"),
            "app-control": dim("32px", "Measured", where=APP_DARK, element="email field and Log in button"),
            "content": dim("1280px", "Measured", where=MARKETING, element="hero inner container"),
            "container-7xl": dim("80rem", "Measured", where=MARKETING, property="--container-7xl"),
        },
        "motion": {
            "duration": {
                "fast": num("150ms", "duration", "Measured", where=MARKETING, property="--default-transition-duration"),
                "nav": num("300ms", "duration", "Measured", where=MARKETING, element="header link transition-duration 0.3s"),
            },
            "easing": {
                "standard": num([0.4, 0, 0.2, 1], "cubicBezier", "Measured", where=MARKETING, property="--ease-in-out"),
                "out": num([0, 0, 0.2, 1], "cubicBezier", "Measured", where=MARKETING, property="--ease-out"),
            },
        },
        "color": {
            "marketing": marketing_colors(),
            "app": app_ramps(),
        },
    }


def light():
    return {
        "background": {
            "page": color("{color.marketing.color-white}", "Measured", where=MARKETING, element="body"),
            "canvas": color("{color.marketing.gray-50}", "Measured", where=MARKETING, element="header and .section-hero"),
            "surface": color("#f8f9fb", "Measured", where=MARKETING, element="article card",
                             computed="rgb(248, 249, 251)",
                             note="Not equal to --gray-50 (#f9f9fb). Read on the card itself."),
            "raised": color("{color.marketing.color-white}", "Measured", where="pricing PRO card"),
        },
        "text": {
            "primary": color("{color.marketing.primary}", "Measured", where=MARKETING, element="body"),
            "secondary": color("{color.marketing.gray-800}", "Measured", where=MARKETING, element="hero lede and Log in"),
            "link": color("{color.marketing.secondary-blue-2}", "Measured", where=MARKETING, element="Talk to sales"),
            "on-accent": color("{color.marketing.color-white}", "Measured", where=MARKETING, element="Sign up"),
            "stat": color("{color.marketing.primary-blue}", "Measured", where=MARKETING, element="166K+"),
        },
        "border": {
            "default": color("{color.marketing.gray-100}", "Measured", where=MARKETING, element="article and email field"),
            "strong": color("#d6dbf5", "Measured", where="pricing PRO card border", computed="rgb(214, 219, 245)"),
            "focus": color("{color.marketing.ring}", "Measured", where=MARKETING, element=":focus-visible ring"),
            "accent": color("#576ddb", "Derived", where="Contact sales border-[#576cdb]/70",
                            note="The class names #576cdb. Computed border was a lab() with alpha. Canvas sRGB of #576cdb is rgb(87, 108, 219), one channel off --primary-blue."),
        },
        "brand": {
            "wordmark": color("#f2545b", "Sampled", where="home-light-default.png header wordmark",
                              note="Flat pixels in the wordmark were rgb(242, 84, 91). Matches the app ramp --rc-red-60. Not a marketing custom property."),
        },
        "action": {
            "default": color("{color.marketing.secondary-blue-1}", "Measured", where=MARKETING, element="Sign up background"),
            "hover": color("{color.marketing.secondary-blue-2}", "Measured", where=MARKETING,
                           note="Declared hover:bg-secondary-blue-2 on the Sign up link. Not held in a hover state."),
            "ghost-text": color("{color.marketing.secondary-blue-2}", "Measured", where=MARKETING, element="Contact sales"),
        },
        "status": {
            "success": color("{color.marketing.secondary-green}", "Measured", where=MARKETING, property="--secondary-green"),
            "success-text": color("{color.marketing.secondary-green-text}", "Measured", where=MARKETING, property="--secondary-green-text"),
            "danger": color("{color.marketing.secondary-red}", "Measured", where=MARKETING, property="--secondary-red"),
            "danger-text": color("{color.marketing.secondary-red-text}", "Measured", where=MARKETING, property="--secondary-red-text"),
        },
        "focus": {
            "ring": color("{color.marketing.ring}", "Measured", where=MARKETING, element="focused Sign up box-shadow"),
            "offset": color("{color.marketing.color-white}", "Measured", where=MARKETING, element="focused Sign up 2px white offset"),
        },
        "component": {
            "button": {
                "bg": color("{action.default}", "Measured", where=MARKETING, element="Sign up"),
                "text": color("{text.on-accent}", "Measured", where=MARKETING, element="Sign up"),
                "radius": dim("9999px", "Derived", where=MARKETING,
                              note="Computed border-radius was 16777215px, the Tailwind rounded-full sentinel. Recorded as a pill."),
                "height": dim("{size.button-sm}", "Measured", where=MARKETING, element="header Sign up"),
            },
            "field": {
                "bg": color("{background.page}", "Measured", where=MARKETING, element="email input"),
                "text": color("{text.primary}", "Measured", where=MARKETING, element="email input"),
                "radius": dim("9999px", "Derived", where=MARKETING, note="Computed 16777215px rounded-full."),
                "height": dim("{size.field}", "Measured", where=MARKETING, element="email input"),
            },
            "card": {
                "bg": color("{background.surface}", "Measured", where=MARKETING, element="article"),
                "radius": dim("16px", "Measured", where=MARKETING, element="article"),
            },
        },
    }


def dark():
    """The app's dark sheet, which is what html.dark resolved on the login page.
    Marketing has no dark theme. These tokens are the app, not the marketing site."""
    return {
        "background": {
            "page": color("{color.app.neutral.90}", "Measured", where=APP_SHEET, selector=".dark",
                          property="--mui-palette-background-default", computed="rgb(29, 31, 37)",
                          note="The body also paints an oklch wash at alpha 0.09. That wash is not a solid page colour."),
            "surface": color("{color.app.neutral.100}", "Measured", where=APP_DARK, element="outlined input root",
                             computed="rgb(20, 22, 27)"),
            "raised": color("{color.app.neutral.100}", "Measured", where=APP_SHEET, selector=".dark", property="--bg-surface"),
        },
        "text": {
            "primary": color("{color.app.neutral.20}", "Measured", where=APP_DARK, element="h2 and label",
                             computed="rgb(242, 243, 245)"),
            "secondary": color("{color.app.neutral.50}", "Measured", where=APP_DARK, element="footer links",
                               computed="rgb(162, 164, 171)"),
            "disabled": color("{color.app.neutral.60}", "Measured", where=APP_DARK, element="disabled Log in",
                              computed="rgb(117, 119, 126)"),
            "link": color("{color.app.blue.60}", "Measured", where=APP_DARK, element="Sign up link",
                          computed="rgb(96, 109, 255)"),
            "on-accent": color("{color.app.white}", "Measured", where=APP_SHEET, property="--text-contrast"),
        },
        "border": {
            "default": color("{color.app.neutral.80}", "Measured", where=APP_DARK, element="input fieldset",
                             computed="rgb(45, 47, 53)"),
            "focus": color("{color.app.blue.60}", "Measured", where=APP_SHEET,
                           note="Stylesheet sets --border-focus to the action blue. The Mui-focused rule sets border-color to --mui-palette-primary-main. A forced Mui-focused class did not change the live computed border."),
        },
        "action": {
            "default": color("{color.app.blue.60}", "Measured", where=APP_SHEET, selector=".dark",
                             property="--button-primary-bottom", note="Enabled primary fill was not on screen. The Log in and Sign up submits were disabled."),
            "disabled": color("{color.app.neutral.80}", "Measured", where=APP_DARK, element="disabled Log in background"),
            "hover": color("#778aff", "Measured", where=APP_SHEET, property="--button-primary-hover",
                           note="Declared. Not held in a hover state."),
        },
        "status": {
            "warning": color("{color.app.yellow.50}", "Measured", where=APP_DARK, element="incident banner",
                             computed="rgb(240, 216, 27)"),
            "warning-text": color("{color.app.yellow.90}", "Measured", where=APP_DARK, element="incident banner text",
                                  computed="rgb(100, 60, 0)"),
            "danger": color("{color.app.red.60}", "Measured", where=APP_SHEET, selector=".dark", property="--error-primary"),
            "success": color("{color.app.green.60}", "Measured", where=APP_SHEET, property="--decoration-green-secondary"),
            "info": color("{color.app.blue.60}", "Measured", where=APP_SHEET, property="--info-primary"),
        },
        "focus": {
            "ring": color("{color.app.blue.60}", "Measured", where=APP_SHEET, property="--border-focus"),
        },
        "component": {
            "button": {
                "bg": color("{action.disabled}", "Measured", where=APP_DARK, element="disabled Log in",
                            note="This is the disabled fill that was on screen, not the enabled primary."),
                "text": color("{text.disabled}", "Measured", where=APP_DARK, element="disabled Log in"),
                "radius": dim("8px", "Measured", where=APP_DARK, element="Log in button"),
                "height": dim("32px", "Measured", where=APP_DARK, element="Log in button"),
            },
            "field": {
                "bg": color("{background.surface}", "Measured", where=APP_DARK, element="email input root"),
                "text": color("{text.primary}", "Measured", where=APP_DARK, element="email input"),
                "radius": dim("8px", "Measured", where=APP_DARK, element="email input"),
                "height": dim("32px", "Measured", where=APP_DARK, element="email input"),
            },
        },
    }


def build():
    tokens = {
        "$schema": "https://design-tokens.org/schema.json",
        "core": core(),
        "light": light(),
        "dark": dark(),
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
    }
    tokens["$extensions"] = {
        "source": src(
            "Measured",
            product="RevenueCat",
            marketing="https://www.revenuecat.com/",
            app="https://app.revenuecat.com/login",
            note="Light is the marketing site. Dark is the signed-out app, which was on screen with html.dark. The app also declares a light sheet that was not the live page.",
        )
    }
    return tokens


def check(tokens):
    """Refuse a token whose alias points nowhere, and a dimension that is not a length."""
    import re
    flat = {}

    def walk(node, prefix):
        for key, value in node.items():
            if key.startswith("$"):
                continue
            path = f"{prefix}.{key}" if prefix else key
            if isinstance(value, dict) and "$value" in value:
                flat[path] = value
            elif isinstance(value, dict):
                walk(value, path)

    for theme_name, theme in tokens.items():
        if theme_name.startswith("$"):
            continue
        walk(theme, theme_name)

    problems = []
    for path, token in flat.items():
        if "source" not in token.get("$extensions", {}):
            problems.append(f"{path} has no source")
        raw = json.dumps(token["$value"])
        for alias in re.findall(r"\{([^{}]+)\}", raw):
            theme = path.split(".", 1)[0]
            candidates = [f"{theme}.{alias}", f"core.{alias}", alias]
            if not any(c in flat for c in candidates):
                problems.append(f"{path} alias {{{alias}}} points nowhere")
        if token["$type"] == "dimension" and isinstance(token["$value"], str):
            if token["$value"].startswith("{") and token["$value"].endswith("}"):
                continue
            if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem|em)", token["$value"]):
                problems.append(f"{path} dimension {token['$value']!r} is not a length")
    if problems:
        raise SystemExit("tokens failed:\n  " + "\n  ".join(problems))


# raw/readings.json is the only raw file. A token labelled Measured or Derived whose value it does not
# hold (hex, rgb(), px, ms as s) was typed in from the capture session: the app ramps, for one, were read
# as raw hex in the same session but never stored. Such a token is relabelled Reconstruction.
RAW_TEXT = re.sub(r"\s+", "", (HERE / "raw" / "readings.json").read_text().lower())
HAND_NOTE = "Entered by hand at capture time; raw/readings.json holds no reading of this value."



def _colours(text):
    """Every colour written in raw/, as (r, g, b, alpha): rgb()/rgba() with commas, spaces or a slash
    alpha, and #rgb/#rrggbb/#rrggbbaa."""
    out = []
    for m in re.finditer(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)\s*(?:[,/]\s*(\d*\.?\d+)(%?))?\s*\)", text):
        a = 1.0 if m.group(4) is None else float(m.group(4)) / (100 if m.group(5) else 1)
        out.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), a))
    for m in re.finditer(r"#([0-9a-f]{8}|[0-9a-f]{6}|[0-9a-f]{3})(?![0-9a-z])", text):
        out.append(_hex(m.group(0)))
    return out


def _hex(value):
    h = value.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), int(h[6:8], 16) / 255 if len(h) == 8 else 1.0)


RAW_COLOURS = _colours((HERE / "raw" / "readings.json").read_text().lower())


def colour_in_raw(value):
    """A hex colour is backed only by a raw colour with the same channels and the same opacity."""
    r, g, b, a = _hex(value)
    return any((r, g, b) == c[:3] and abs(a - c[3]) <= 0.01 for c in RAW_COLOURS)

def in_raw(value):
    v = str(value).strip().lower()
    forms = {v.replace(" ", "")}
    if re.fullmatch(r"#[0-9a-f]{6}([0-9a-f]{2})?", v):
        return colour_in_raw(v)
    m = re.fullmatch(r"(\d*\.?\d+)ms", v)
    if m:
        forms.add(f"{float(m.group(1)) / 1000:g}s")
    if "," in v and not v.startswith(("#", "rgb")):
        forms.add(v.split(",")[0].strip().strip("'\""))  # a font stack: its first family
    m = re.fullmatch(r"(\d*\.?\d+)px", v)
    if m:
        n = float(m.group(1))
        forms |= {f":{n:g},", f":{n:g}}}"}  # a box size stored as a bare number ("height": 40)
    if v == "9999px":
        forms |= {"16777215px", "16777200px", "1.67772e+07px"}  # the full pill a computed rounded-full radius reports
    return any(f.replace(" ", "") in RAW_TEXT for f in forms)


def relabel_unread(tokens):
    def walk(node):
        for k, v in node.items():
            if k.startswith("$") or not isinstance(v, dict):
                continue
            if "$value" in v:
                yield v
            else:
                yield from walk(v)
    for tok in walk(tokens):
        value, src = tok["$value"], tok["$extensions"]["source"]
        if not isinstance(value, (str, int, float)) or (isinstance(value, str) and value.startswith("{")):
            continue  # aliases and composites carry the evidence of what they name
        if isinstance(src, dict) and src.get("evidence") in ("Measured", "Derived") and not in_raw(value):
            src["evidence"] = "Reconstruction"
            if "note" in src:
                src["captureNote"] = src.pop("note")
            src["note"] = HAND_NOTE


def main():
    tokens = build()
    relabel_unread(tokens)
    check(tokens)
    path = HERE / "tokens.json"
    path.write_text(json.dumps(tokens, indent=2) + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
