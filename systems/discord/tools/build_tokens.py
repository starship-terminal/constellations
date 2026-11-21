#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

Values are the browser's computed custom properties on a probe element, read
from discord.com stylesheets on 2026-11-22 by tools/capture/vars.mjs.

Two layers:
  core     marketing :root names that do not change with .theme-light / .theme-dark
           (blurple, space, radius, breakpoints, font stacks) plus the home h1
           measurement from the same file's brand block.
  light    names whose computed value on .theme-light differs, plus the roles
           the marketing page paints (page, text, accent) measured on the live home.
  dark     the same names resolved on .theme-dark. Marketing pages do not bind
           that class. The login wall paints a dark app shell; those role values
           are declared evidence from the stylesheet, not a signed-in screen.

A colour the probe returned as color-mix() or hsl() is stored as that string
and marked Not captured as sRGB: it was read, but not converted. A name that
did not resolve is omitted, never filled from memory.

Deterministic. Edit raw/css-vars.json, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
ROOT = RAW["resolved"]["light"]
LIGHT = RAW["resolved"]["theme-light"]
DARK = RAW["resolved"]["theme-dark"]
BRAND = RAW["brand"]


def norm_color(v):
    v = v.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8 and h[6:] != "ff":
            a = round(int(h[6:8], 16) / 255, 3)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    if v.lower() in ("#fff", "white"):
        return "#ffffff"
    if v.lower() in ("#000", "black"):
        return "#000000"
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))
    return None


def leaf(value, ty, source, note=None):
    ext = {"source": source}
    if note:
        ext["note"] = note
    return {"$value": value, "$type": ty, "$extensions": ext}


def color_leaf(raw, source):
    n = norm_color(raw)
    if n:
        return leaf(n, "color", source)
    return leaf(raw, "color", source, note="Not captured as sRGB. The computed value is a color-mix or hsl string and was not converted.")


def dim_leaf(raw, source):
    raw = str(raw).strip()
    if raw == "2147483647px":
        return leaf("9999px", "dimension", source, note="Derived. The stylesheet declares 2147483647px as a pill radius. Stored as 9999px so the dimension check holds. The authored value is in the source string.")
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", raw):
        raise ValueError("not a dimension: " + raw)
    return leaf(raw, "dimension", source)


CORE_COLORS = [
    "blurple", "brand", "black", "white", "not-quite-black", "greyple", "off-white",
    "dark-not-black", "text-link", "status-green", "button-hover", "focus-border",
]
CORE_FONTS = ["font-primary", "font-headline", "font-code"]
SPACE = ["0", "4", "6", "8", "10", "12", "16", "20", "24", "32", "40", "48", "64", "80", "96"]
RADIUS = ["none", "xs", "sm", "md", "lg", "xl", "xxl", "round"]
BREAKS = ["xxs", "xs", "sm", "md", "lg", "xl"]
WEIGHTS = ["light", "normal", "medium", "semibold", "bold", "extra-bold", "black"]

SEMANTIC = [
    "text-default", "text-muted", "text-subtle", "text-strong", "text-link", "text-brand",
    "background-accent", "background-scrim", "background-code",
    "border-subtle", "border-muted", "border-normal", "border-strong", "border-focus",
    "status-positive", "status-danger", "status-warning", "status-online",
    "interactive-muted", "channels-default",
    "shadow-low", "shadow-medium", "shadow-high",
]


def require(table, name):
    key = "--" + name
    if key not in table or not table[key]:
        raise KeyError(name + " missing from readings")
    return table[key]


core = {"color": {}, "font": {}, "fontWeight": {}, "space": {}, "radius": {}, "breakpoint": {}, "typography": {}}
for name in CORE_COLORS:
    raw = require(ROOT, name)
    core["color"][name.replace("-", ".")] = color_leaf(raw, "css-var --%s resolved on :root probe (marketing page stylesheets)" % name)
# theme-color meta, measured on the live home document
core["color"]["themeColor"] = color_leaf(
    BRAND["themeColor"][0]["content"],
    "measured <meta name=theme-color> on https://discord.com/",
)
for name in CORE_FONTS:
    core["font"][name.replace("font-", "")] = leaf(require(ROOT, name), "fontFamily", "css-var --%s resolved on :root probe" % name)
for name in WEIGHTS:
    core["fontWeight"][name] = leaf(int(require(ROOT, "font-weight-" + name)), "fontWeight", "css-var --font-weight-%s" % name)
for name in SPACE:
    core["space"][name] = dim_leaf(require(ROOT, "space-" + name), "css-var --space-%s" % name)
for name in RADIUS:
    core["radius"][name] = dim_leaf(require(ROOT, "radius-" + name), "css-var --radius-%s" % name)
for name in BREAKS:
    core["breakpoint"][name] = dim_leaf(require(ROOT, "breakpoint-" + name), "css-var --breakpoint-%s" % name)

h1 = BRAND["h1"]
core["typography"]["display"] = {
    "$type": "typography",
    "$value": {
        "fontFamily": h1["fontFamily"].split(",")[0],
        "fontSize": h1["fontSize"],
        "fontWeight": int(h1["fontWeight"]),
        "lineHeight": h1["lineHeight"],
        "letterSpacing": h1["letterSpacing"],
    },
    "$extensions": {"source": "measured computed style of h1 on https://discord.com/ at 1440x900"},
}
core["typography"]["body"] = {
    "$type": "typography",
    "$value": {
        "fontFamily": BRAND["bodyFont"].split(",")[0],
        "fontSize": "Not captured",
        "fontWeight": "Not captured",
        "lineHeight": "Not captured",
        "letterSpacing": "Not captured",
    },
    "$extensions": {
        "source": "font family measured as computed fontFamily of body on https://discord.com/. Size, weight, line height and letter spacing were not read.",
        "note": "Not captured: body size, weight, line height, letter spacing.",
    },
}


def semantic(table, label):
    out = {"color": {}, "shadow": {}}
    for name in SEMANTIC:
        key = "--" + name
        if key not in table:
            continue
        raw = table[key]
        group = "shadow" if name.startswith("shadow-") else "color"
        token_name = name.split("-", 1)[1] if name.startswith(("text-", "background-", "border-", "status-", "shadow-")) else name.replace("-", ".")
        # keep the prefix so text.default and background.accent do not collide
        if name.startswith("text-"):
            out.setdefault("text", {})
            out["text"][name.split("-", 1)[1]] = color_leaf(raw, "css-var %s resolved on .%s probe" % (key, label))
        elif name.startswith("background-"):
            out.setdefault("background", {})
            out["background"][name.split("-", 1)[1]] = color_leaf(raw, "css-var %s resolved on .%s probe" % (key, label))
        elif name.startswith("border-"):
            out.setdefault("border", {})
            out["border"][name.split("-", 1)[1]] = color_leaf(raw, "css-var %s resolved on .%s probe" % (key, label))
        elif name.startswith("status-"):
            out.setdefault("status", {})
            out["status"][name.split("-", 1)[1]] = color_leaf(raw, "css-var %s resolved on .%s probe" % (key, label))
        elif name.startswith("shadow-"):
            out["shadow"][name.split("-", 1)[1]] = leaf(raw, "other", "css-var %s resolved on .%s probe" % (key, label), note="Not tokenised as a DTCG shadow. The computed value uses hsl(none …), which this builder does not parse.")
        else:
            out["color"][name.replace("-", ".")] = color_leaf(raw, "css-var %s resolved on .%s probe" % (key, label))
    return out


light = semantic(LIGHT, "theme-light")
dark = semantic(DARK, "theme-dark")

# Roles the marketing home actually paints, measured on the live document.
light["page"] = color_leaf(BRAND["bodyBg"], "measured computed backgroundColor of body on https://discord.com/ at 1440x900")
light["text"] = color_leaf(h1["color"], "measured computed color of h1 on https://discord.com/ at 1440x900")
light["accent"] = color_leaf(require(ROOT, "blurple"), "css-var --blurple on :root. Painted accent of the marketing site.")

# Painted controls, from raw/components-computed.json. Only values that were read.
COMP = json.loads((HERE / "raw" / "components-computed.json").read_text())["components"]


def comp_color(name, state, prop):
    raw = COMP[name]["states"][state]["style"]["style"][prop]
    return color_leaf(raw, "measured computed %s of %s/%s on the live page" % (prop, name, state))


def comp_dim(name, state, prop):
    raw = COMP[name]["states"][state]["style"]["style"][prop]
    # computed px can be fractional; keep one decimal when needed
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?)px", str(raw).strip())
    if not m:
        raise ValueError(raw)
    n = round(float(m.group(1)), 2)
    text = ("%g" % n) + "px"
    return dim_leaf(text, "measured computed %s of %s/%s" % (prop, name, state))


light["component"] = {
    "navLink": {
        "color": comp_color("nav-link", "default", "color"),
        "backgroundHover": comp_color("nav-link", "hover", "backgroundColor"),
        "radius": comp_dim("nav-link", "default", "borderTopLeftRadius"),
        "fontSize": comp_dim("nav-link", "default", "fontSize"),
        "paddingX": comp_dim("nav-link", "default", "paddingLeft"),
    },
    "login": {
        "background": comp_color("nav-login", "default", "backgroundColor"),
        "color": comp_color("nav-login", "default", "color"),
        "radius": comp_dim("nav-login", "default", "borderTopLeftRadius"),
    },
    "download": {
        "background": comp_color("button-download", "default", "backgroundColor"),
        "backgroundHover": comp_color("button-download", "hover", "backgroundColor"),
        "color": comp_color("button-download", "default", "color"),
        "radius": comp_dim("button-download", "default", "borderTopLeftRadius"),
        "height": comp_dim("button-download", "default", "height"),
        "fontSize": comp_dim("button-download", "default", "fontSize"),
    },
    "openApp": {
        "background": comp_color("button-open-app", "default", "backgroundColor"),
        "color": comp_color("button-open-app", "default", "color"),
        "radius": comp_dim("button-open-app", "default", "borderTopLeftRadius"),
        "height": comp_dim("button-open-app", "default", "height"),
    },
    "loginSubmit": {
        "background": comp_color("login-submit", "default", "backgroundColor"),
        "color": comp_color("login-submit", "default", "color"),
        "radius": comp_dim("login-submit", "default", "borderTopLeftRadius"),
        "height": comp_dim("login-submit", "default", "height"),
    },
    "loginField": {
        "height": comp_dim("login-field", "default", "height"),
        "radius": comp_dim("login-field", "default", "borderTopLeftRadius"),
        "fontSize": comp_dim("login-field", "default", "fontSize"),
    },
}

doc = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$extensions": {
        "capture": "2026-11-22, https://discord.com/, signed out",
        "darkNote": "dark set is resolved on a .theme-dark probe. Marketing pages paint light. The login wall paints a dark app shell and was photographed, not measured into these role tokens.",
    },
}

(HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
print("wrote tokens.json", "core colors", len(core["color"]), "light keys", list(light))
