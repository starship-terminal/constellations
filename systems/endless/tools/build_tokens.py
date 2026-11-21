#!/usr/bin/env python3
"""Build tokens.json from the public endless.app capture.

Readings (2026-11-21, signed out, headless Chromium):
  raw/vars-light.json, raw/vars-dark.json   custom properties on :root, light and dark
  raw/home-computed.json, raw/home-dark-computed.json
  raw/signup-hover.json, raw/signup-focus.json, raw/signin.json, raw/signin-email-focus.json

Colour tokens are the browser's computed style. CSS lab() values are converted
with the CSS Color 4 Lab to sRGB path (D50, Bradford to D65) and checked
against flat pixels in the full-colour captures. A value that could not be
read is not invented.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
LIGHT = json.loads((RAW / "vars-light.json").read_text())["all"]
DARK = json.loads((RAW / "vars-dark.json").read_text())["all"]
HOME = json.loads((RAW / "home-computed.json").read_text())
HOME_DARK = json.loads((RAW / "home-dark-computed.json").read_text())


def lab_to_srgb(L, a, b):
    fy = (L + 16) / 116
    fx = fy + (a / 500)
    fz = fy - (b / 200)

    def finv(t):
        delta = 6 / 29
        return t ** 3 if t > delta else 3 * delta * delta * (t - 4 / 29)

    Xn, Yn, Zn = 0.96422, 1.0, 0.82521
    X, Y, Z = finv(fx) * Xn, finv(fy) * Yn, finv(fz) * Zn
    M = (
        (0.9555766, -0.0230393, 0.0631636),
        (-0.0282895, 1.0099416, 0.0210077),
        (0.0122982, -0.0204830, 1.3299098),
    )
    X65 = M[0][0] * X + M[0][1] * Y + M[0][2] * Z
    Y65 = M[1][0] * X + M[1][1] * Y + M[1][2] * Z
    Z65 = M[2][0] * X + M[2][1] * Y + M[2][2] * Z
    R = 3.2404542 * X65 - 1.5371385 * Y65 - 0.4985314 * Z65
    G = -0.9692660 * X65 + 1.8760108 * Y65 + 0.0415560 * Z65
    B = 0.0556434 * X65 - 0.2040259 * Y65 + 1.0572252 * Z65

    def enc(c):
        c = min(1, max(0, c))
        return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055

    return tuple(round(enc(c) * 255) for c in (R, G, B))


def hex_of(rgb):
    return "#%02x%02x%02x" % rgb


def parse_color(raw):
    raw = (raw or "").strip()
    if not raw:
        raise ValueError("empty colour")
    if re.fullmatch(r"#[0-9a-fA-F]{6}", raw):
        return raw.lower()
    if re.fullmatch(r"#[0-9a-fA-F]{3}", raw):
        return "#" + "".join(c * 2 for c in raw[1:].lower())
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", raw)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 0.999:
            return hex_of((int(r), int(g), int(b)))
        return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))
    m = re.fullmatch(r"lab\(\s*([0-9.]+)%?\s+(-?[0-9.]+)\s+(-?[0-9.]+)(?:\s*/\s*([0-9.]+))?\s*\)", raw)
    if m:
        rgb = lab_to_srgb(float(m.group(1)), float(m.group(2)), float(m.group(3)))
        if m.group(4) is None or float(m.group(4)) >= 0.999:
            return hex_of(rgb)
        return "rgba(%d, %d, %d, %g)" % (*rgb, float(m.group(4)))
    raise ValueError("not a colour: " + raw)


def src(text):
    return {"source": text}


def color_token(value, source, description=None):
    token = {"$value": parse_color(value), "$type": "color", "$extensions": src(source)}
    if description:
        token["$description"] = description
    return token


def dim(value, source, description=None):
    token = {"$value": value, "$type": "dimension", "$extensions": src(source)}
    if description:
        token["$description"] = description
    return token


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": src(source)}


def alias(path, source):
    return {"$value": "{" + path + "}", "$type": "color", "$extensions": src(source)}


VAR = "custom property on :root, raw/vars-light.json and raw/vars-dark.json, computed 2026-11-21"

core = {
    "$description": "Scales and primitives measured on endless.app, theme-free.",
    "color": {
        "ink": color_token(HOME["h1"]["color"], "computed color of h1 on the home page, light (raw/home-computed.json)", "Near-black text and the filled button."),
        "paper": color_token(HOME["page"]["backgroundColor"], "computed backgroundColor of body, light (raw/home-computed.json)", "Page ground in light."),
        "white": color_token(LIGHT["--color-white"], VAR + " --color-white"),
        "black": color_token(LIGHT["--color-black"], VAR + " --color-black"),
        "sky": color_token(LIGHT["--color-landing-action"], VAR + " --color-landing-action. Declared #11a8ff. Painted hero pixels nearby read about #21aeed; the declared value is the token."),
        "accent": color_token(LIGHT["--accent"], VAR + " --accent. CSS lab() converted to sRGB. Focus ring uses this hue."),
        "blue600": color_token(LIGHT["--color-blue-600"], VAR + " --color-blue-600"),
        "green600": color_token(LIGHT["--color-green-600"], VAR + " --color-green-600"),
        "orange600": color_token(LIGHT["--color-orange-600"], VAR + " --color-orange-600"),
        "pink600": color_token(LIGHT["--color-pink-600"], VAR + " --color-pink-600"),
        "purple600": color_token(LIGHT["--color-purple-600"], VAR + " --color-purple-600"),
        "sky600": color_token(LIGHT["--color-sky-600"], VAR + " --color-sky-600"),
        "neutral800": color_token(LIGHT["--color-neutral-800"], VAR + " --color-neutral-800"),
    },
    "font": {
        "family": {
            "sans": {
                "$value": "TikTok Sans, system-ui, arial",
                "$type": "fontFamily",
                "$extensions": src("computed fontFamily of body (raw/vars-light.json body.font) and --font-sans"),
                "$description": "The marketing and app face. Proprietary; the guide falls back to system-ui.",
            },
            "mono": {
                "$value": "Geist Mono, ui-monospace, monospace",
                "$type": "fontFamily",
                "$extensions": src("--font-mono / --default-mono-font-family, raw/vars-light.json"),
            },
        }
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {"fontFamily": "TikTok Sans, system-ui, arial", "fontSize": "59.2px", "fontWeight": 500, "lineHeight": "64px"},
            "$extensions": src("computed font of h1 on the home page at 1440 (raw/home-computed.json)"),
        },
        "body": {
            "$type": "typography",
            "$value": {"fontFamily": "TikTok Sans, system-ui, arial", "fontSize": "16px", "fontWeight": 400, "lineHeight": "24px"},
            "$extensions": src("computed font of body (raw/vars-light.json body)"),
        },
        "label": {
            "$type": "typography",
            "$value": {"fontFamily": "TikTok Sans, system-ui, arial", "fontSize": "14px", "fontWeight": 600, "lineHeight": "20px"},
            "$extensions": src("computed font of the header Sign up button (raw/home-computed.json signup)"),
        },
        "caption": {
            "$type": "typography",
            "$value": {"fontFamily": "TikTok Sans, system-ui, arial", "fontSize": "12px", "fontWeight": 400, "lineHeight": "16px"},
            "$extensions": src("computed font of the MCP banner link (raw/home-computed.json mcpLink)"),
        },
    },
    "radius": {
        "xs": dim(LIGHT["--radius-xs"], VAR + " --radius-xs"),
        "sm": dim(LIGHT["--radius-sm"], VAR + " --radius-sm"),
        "md": dim(LIGHT["--radius-md"], VAR + " --radius-md"),
        "lg": dim(LIGHT["--radius-lg"], VAR + " --radius-lg"),
        "xl": dim(LIGHT["--radius-xl"], VAR + " --radius-xl"),
        "2xl": dim(LIGHT["--radius-2xl"], VAR + " --radius-2xl"),
        "control": dim(HOME["signup"]["borderRadius"], "computed borderRadius of the header Sign up button (raw/home-computed.json)"),
        "chip": dim(HOME["chip"]["borderRadius"], "computed borderRadius of a prompt chip (raw/home-computed.json)"),
    },
    "space": {
        "1": dim("4px", "Derived from the 4px step implied by control padding. Header button padding was not a token; 4px is the smallest step that divides the measured 8px radius."),
        "2": dim("8px", "Derived: header button radius and the gap scale step (raw/home-computed.json signup borderRadius 8px)."),
        "3": dim("12px", "Measured chip radius 12px used as the 12px step (raw/home-computed.json chip)."),
        "4": dim("16px", "Measured body font size, also the composer font size (raw/vars-light.json)."),
        "6": dim("24px", "Measured body line height (raw/vars-light.json)."),
        "8": dim("32px", "Measured header button height (raw/home-computed.json signup height 32)."),
    },
    "size": {
        "headerButton": dim("32px", "computed height of header Sign up (raw/home-computed.json)"),
        "chip": dim("36px", "computed height of a prompt chip (raw/home-computed.json)"),
        "composer": dim("72px", "computed height of the home composer textarea (raw/home-computed.json)"),
        "control": dim("32px", "header control height, reused as the default control height"),
    },
    "fontWeight": {
        "regular": num(400, "--font-weight-normal " + VAR, "fontWeight"),
        "medium": num(500, "--font-weight-medium " + VAR, "fontWeight"),
        "semibold": num(600, "--font-weight-semibold " + VAR, "fontWeight"),
    },
    "focusRing": {
        "color": color_token(LIGHT["--ring"], VAR + " --ring"),
        "width": dim("2px", "computed outline width on the focused sign-in email field was 2px with a 3.98px accent halo (raw/signin-email-focus.json)"),
    },
}

def semantic(theme, readings, computed):
    g = readings
    return {
        "$description": f"Semantic roles for the {theme} theme, from :root custom properties after the footer theme control was set to {theme}.",
        "background": {
            "page": color_token(g["--background"], f"{VAR} --background, {theme}"),
            "surface": color_token(g["--card"], f"{VAR} --card, {theme}"),
            "muted": color_token(g["--muted"], f"{VAR} --muted, {theme}"),
            "popover": color_token(g["--popover"], f"{VAR} --popover, {theme}"),
            "sidebar": color_token(g["--sidebar"], f"{VAR} --sidebar, {theme}"),
        },
        "text": {
            "primary": color_token(g["--foreground"], f"{VAR} --foreground, {theme}"),
            "muted": color_token(g["--muted-foreground"], f"{VAR} --muted-foreground, {theme}"),
            "onAccent": color_token(g["--primary-foreground"], f"{VAR} --primary-foreground, {theme}"),
            "card": color_token(g["--card-foreground"], f"{VAR} --card-foreground, {theme}"),
        },
        "border": {
            "default": color_token(g["--border"], f"{VAR} --border, {theme}"),
        },
        "accent": {
            "default": color_token(g["--accent"], f"{VAR} --accent, {theme}"),
            "landing": color_token(g["--color-landing-action"], f"{VAR} --color-landing-action, {theme}"),
        },
        "action": {
            "primary": color_token(g["--primary"], f"{VAR} --primary, {theme}"),
            "primaryText": color_token(g["--primary-foreground"], f"{VAR} --primary-foreground, {theme}"),
        },
        "status": {
            "success": color_token(g["--success"], f"{VAR} --success, {theme}"),
            "warning": color_token(g["--warning"], f"{VAR} --warning, {theme}"),
            "danger": color_token(g["--destructive"], f"{VAR} --destructive, {theme}"),
            "info": color_token(g["--color-sky-600"], f"{VAR} --color-sky-600, {theme}. No separate info role; sky-600 is the closest declared info hue."),
        },
        "focus": {
            "ring": color_token(g["--ring"], f"{VAR} --ring, {theme}"),
        },
        "component": {
            "button": {
                "bg": color_token(computed["signup"]["backgroundColor"], f"computed backgroundColor of header Sign up, {theme} (raw/home-computed.json or home-dark-computed.json)"),
                "text": color_token(computed["signup"]["color"], f"computed color of header Sign up, {theme}"),
                "radius": dim(computed["signup"]["borderRadius"], f"computed borderRadius of header Sign up, {theme}"),
                "height": dim(str(computed["signup"]["h"]) + "px", f"bounding height of header Sign up, {theme}"),
            },
            "chip": {
                "bg": color_token(computed["chip"]["backgroundColor"], f"computed backgroundColor of a prompt chip, {theme}"),
                "text": color_token(computed["chip"]["color"], f"computed color of a prompt chip, {theme}"),
                "radius": dim(computed["chip"]["borderRadius"], f"computed borderRadius of a prompt chip, {theme}"),
            },
        },
    }


doc = {
    "core": core,
    "light": semantic("light", LIGHT, HOME),
    "dark": semantic("dark", DARK, HOME_DARK),
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
}

# sanity: page and ink match sampled pixels
assert doc["light"]["background"]["page"]["$value"] == "#fcfcfc", doc["light"]["background"]["page"]
assert doc["light"]["text"]["primary"]["$value"] == "#0a0a0a", doc["light"]["text"]["primary"]
assert doc["core"]["color"]["sky"]["$value"] == "#11a8ff"

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=1) + "\n")
print("wrote", out, "light page", doc["light"]["background"]["page"]["$value"], "accent", doc["core"]["color"]["accent"]["$value"])
