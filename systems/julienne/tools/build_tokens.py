#!/usr/bin/env python3
"""Build tokens.json from the Julienne readings.

Sources, read from withjulienne.com on 2026-11-18:
  raw/components-computed.json  computed styles of signed-out controls
  raw/css-vars.json             the glass custom properties and @font-face
  raw/motion.json               the motion probe

Julienne paints light on boot (html.js.light) and dark when the header's
Toggle theme control sets html.js.dark. Colour roles are measured computed
styles. Glass elevation aliases the declared --glass-* custom properties.
Every token carries $extensions.source.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
C = json.loads((RAW / "components-computed.json").read_text())["components"]
V = json.loads((RAW / "css-vars.json").read_text())

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import motion as motion_mod

DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def norm_color(v):
    v = str(v).strip()
    if v.startswith("{"):
        return v
    hm = re.fullmatch(r"#([0-9a-fA-F]{6})", v)
    if hm:
        return "#" + hm.group(1).lower()
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if not m:
        raise ValueError("not a colour: " + v)
    r, g, b = (int(float(m.group(i))) for i in (1, 2, 3))
    a = float(m.group(4)) if m.group(4) is not None else 1
    if a >= 0.999:
        return "#%02x%02x%02x" % (r, g, b)
    return "rgba(%d, %d, %d, %g)" % (r, g, b, round(a, 3))


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "color":
        norm_color(val)
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension {val!r}")
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")
    if ty == "shadow":
        for layer in val:
            for k in ("offsetX", "offsetY", "blur", "spread"):
                if not DIM.fullmatch(layer[k]):
                    raise ValueError(f"{path}: shadow {k} {layer[k]!r}")


def color(value, source, description):
    return {"$value": norm_color(value), "$type": "color", "$description": description, "$extensions": {"source": source}}


def dim(value, source, description):
    v = value if isinstance(value, str) else "%gpx" % value
    if re.fullmatch(r"-?\d+(\.\d+)?", v):
        v += "px"
    return {"$value": v, "$type": "dimension", "$description": description, "$extensions": {"source": source}}


def num(value, source, description, ty="fontWeight"):
    return {"$value": int(value), "$type": ty, "$description": description, "$extensions": {"source": source}}


def font(value, source, description):
    return {"$value": value, "$type": "fontFamily", "$description": description, "$extensions": {"source": source}}


def text(value, source, description):
    return {"$value": value, "$type": "string", "$description": description, "$extensions": {"source": source}}


def alias(path, description, source):
    return {"$value": "{" + path + "}", "$type": "color", "$description": description, "$extensions": {"source": source}}


def st(comp, part):
    return C[comp]["states"][part]["style"]


def px(style, key):
    return style[key]


S_HEADER = "measured header on https://withjulienne.com/ at 1440x900, html.js.light"
S_DARK = "measured header on https://withjulienne.com/ at 1440x900 after the Toggle theme control set html.js.dark"
S_HERO = "measured home hero on https://withjulienne.com/ at 1440x900, html.js.light"
S_AUTH = "measured /signup form at rest on 2026-11-18; nothing typed or submitted"
S_RECIPE = "measured public recipe page at 1440x900, html.js.light"
S_DISC = "measured /discover filter chips at 1440x900"
S_FOOT = "measured home footer at 1440x900"
S_LEGAL = "measured /privacy-policy prose at 1440x900"
S_CSS = "declared in withjulienne.com/assets/index-19a84fdb.css, resolved on the probe document"

page_light = st("cookbook-boundary", "body")["backgroundColor"]
page_dark = st("header-dark", "page")["backgroundColor"]
ink = st("hero", "h1")["color"]
ink_dark = st("header-dark", "h1")["color"]
muted = st("recipe-card", "meta")["color"]
brand = st("hero", "more")["backgroundColor"]
on_brand = st("hero", "more")["color"]
link = st("auth-rest", "termsLink")["color"]
footer_bg = st("footer", "footer")["backgroundColor"]
field = st("auth-rest", "email")["backgroundColor"]
field_border = st("auth-rest", "email")["borderTopColor"]
disabled_fill = st("auth-rest", "create")["backgroundColor"]
disabled_ink = st("auth-rest", "create")["color"]
glass = st("header", "searchGlass")["backgroundColor"]
glass_dark = st("header-dark", "searchGlass")["backgroundColor"]
chip_on = st("discover-chips", "chipSelected")["backgroundColor"]
cook = st("recipe", "cook")["backgroundColor"]
prose = st("legal", "body")["color"]
nav = st("header", "navLink")["color"]
nav_dark = st("header-dark", "login")["color"]

core = {
    "$description": "Theme-independent scales measured on withjulienne.com, 2026-11-18.",
    "font": {
        "family": {
            "display": font('"EB Garamond", serif', S_HERO + "; h1 computed fontFamily", "Display face. Google Fonts stylesheet, not shipped here."),
            "body": font('ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"', S_HEADER + "; body computed fontFamily", "Body stack. The product also loads Inter for .font-inter labels; the computed body stack is the system sans."),
            "ui": font("Inter, ui-sans-serif, system-ui, sans-serif", "Google Fonts stylesheet linked from the home document (family=Inter:wght@400;500;600;700); .font-inter in the product CSS", "UI face used by filter chips and auth buttons. Licence is the Inter SIL OFL. Not shipped."),
        },
        "weight": {
            "regular": num(400, S_HERO, "h1 and body weight"),
            "medium": num(500, S_AUTH + "; Create account computed fontWeight", "Auth button weight"),
        },
        "size": {
            "caption": dim(st("recipe-card", "meta")["fontSize"], "recipe card Total Time computed fontSize", "Caption"),
            "label": dim(st("header", "navLink")["fontSize"], "nav link computed fontSize", "Nav and field label"),
            "body": dim(st("header", "header")["fontSize"], "header computed fontSize, the body default", "Body"),
            "title": dim(st("legal", "h2")["fontSize"], "legal h2 computed fontSize", "Section title"),
            "display-sm": dim(st("hero", "h1")["fontSize"], "home h1 computed fontSize at 1440", "Home display"),
            "display": dim(st("recipe", "title")["fontSize"], "recipe h1 computed fontSize", "Recipe and team display"),
        },
        "lineHeight": {
            "caption": dim(st("recipe-card", "meta")["lineHeight"], "recipe meta computed lineHeight", "Caption line height"),
            "body": dim(st("header", "header")["lineHeight"], "header computed lineHeight", "Body line height"),
            "display-sm": dim(st("hero", "h1")["lineHeight"], "home h1 computed lineHeight", "Home display line height"),
            "display": dim(st("recipe", "title")["lineHeight"], "recipe h1 computed lineHeight", "Display line height"),
        },
    },
    "radius": {
        "none": dim("0px", S_HEADER, "Header and display type have square corners"),
        "control": dim(st("auth-rest", "email")["borderTopLeftRadius"], S_AUTH + "; email field border radius", "Auth field and primary button"),
        "pill": dim(st("header", "searchGlass")["borderTopLeftRadius"], S_HEADER + "; search glass border radius", "Glass search, theme toggle, Cook and filter chips"),
    },
    "space": {
        "2": dim("8px", "header grid px-2 (0.5rem) computed as 8px at the root 16px font", "Tight inset"),
        "4": dim("16px", "body font-size 16px is the spacing unit the Tailwind scale multiplies", "Base unit"),
        "6": dim("24px", "auth field horizontal padding class pl-6, 1.5rem", "Field inset"),
        "11": dim(st("header", "searchGlass")["height"], S_HEADER + "; glass control height", "44px control"),
        "14": dim(st("auth-rest", "email")["height"], S_AUTH + "; field height", "56px field"),
        "16": dim(st("hero", "more")["height"], S_HERO + "; See more recipes height", "64px hero button"),
        "20": dim(st("header", "header")["height"], S_HEADER + "; header height", "80px header"),
    },
    "border": {
        "hairline": dim(st("auth-rest", "email")["borderTopWidth"], S_AUTH + "; field border width", "1px field border"),
    },
    "size": {
        "header": dim(st("header", "header")["height"], S_HEADER, "Fixed header"),
        "glass": dim(st("header", "searchGlass")["height"], S_HEADER, "Glass pill height"),
        "field": dim(st("auth-rest", "email")["height"], S_AUTH, "Auth field height"),
        "button": dim(st("hero", "more")["height"], S_HERO, "Hero button height"),
        "chip": dim(st("discover-chips", "chip")["height"], S_DISC, "Discover filter chip height"),
        "icon-logo": dim("24px", "header logo img computed about 23.72px, rounded", "Wordmark mark height"),
    },
}

light = {
    "$description": "Roles painted while html is js light, the boot theme.",
    "color": {
        "page": color(page_light, "body backgroundColor on /cookbook and the home document", "Page"),
        "ink": color(ink, S_HERO + "; h1 color", "Primary text"),
        "nav": color(nav, S_HEADER + "; Discover link color", "Nav text"),
        "muted": color(muted, "recipe card Total Time color", "Secondary text"),
        "prose": color(prose, S_LEGAL + "; paragraph color", "Legal body, 70% black"),
        "brand": color(brand, S_HERO + "; See more recipes background", "Brand fill #3C1518"),
        "onBrand": color(on_brand, S_HERO + "; See more recipes color", "Text on brand"),
        "link": color(link, S_AUTH + "; Terms link color", "Link, same hue as brand"),
        "footer": color(footer_bg, S_FOOT + "; footer background", "Raised footer"),
        "field": color(field, S_AUTH + "; email background", "Field fill"),
        "fieldBorder": color(field_border, S_AUTH + "; email border color", "Field border"),
        "disabledFill": color(disabled_fill, S_AUTH + "; Create account is disabled until the form is valid", "Disabled button fill"),
        "disabledInk": color(disabled_ink, S_AUTH + "; Create account color", "Disabled button text"),
        "glass": color(glass, S_HEADER + "; .glass.glass-interactive background", "Glass control fill"),
        "chipOn": color(chip_on, S_DISC + "; selected Breakfast chip background", "Selected chip"),
        "cook": color(cook, S_RECIPE + "; Cook button background", "Recipe Cook pill"),
        "darkPage": color(page_dark, S_DARK + "; body background", "Dark page, recorded so the dark set can alias it"),
        "darkInk": color(ink_dark, S_DARK + "; h1 color", "Dark primary text"),
        "darkNav": color(nav_dark, S_DARK + "; Log in color", "Dark nav text"),
        "darkGlass": color(glass_dark, S_DARK + "; search glass background", "Dark glass fill"),
    }
}

# Dark roles are literal measured colours. The catalog resolver looks up an
# alias inside the token's own set, then core, then the root, so a dark token
# cannot point at light.color.*.
dark = {
    "$description": "Roles painted after the header Toggle theme control set html.js.dark. Verified by the class before the reading.",
    "color": {
        "page": color(page_dark, S_DARK + "; body background", "Dark page"),
        "ink": color(ink_dark, S_DARK + "; h1 color", "Dark primary text"),
        "nav": color(nav_dark, S_DARK + "; Log in color", "Dark nav text"),
        "muted": color("#a3a3a3", "Reconstruction — entered by hand at capture time from the class name dark:text-gray-400 on the signup Sign in link; no dark reading holds it, and #a3a3a3 is Tailwind's neutral-400, not gray-400 (#9ca3af). The light muted #7a7a7a fails on the dark page.", "Hand-entered dark muted text"),
        "prose": color(ink_dark, S_DARK + "; dark prose follows the inverted ink", "Dark prose"),
        "brand": color(brand, S_HERO + "; brand fill does not invert", "Brand fill"),
        "onBrand": color(on_brand, S_HERO + "; text on brand", "Text on brand"),
        "link": color("rgb(255, 157, 117)", "auth Terms link class dark:text-[#FF9D75], declared in the signup markup and matching the stylesheet", "Dark link accent"),
        "footer": color(page_dark, S_DARK + "; no separate dark footer fill was measured, so the role follows the dark page", "Dark footer follows the page"),
        "field": color("rgb(42, 42, 42)", "signup email class dark:bg-[#2A2A2A], declared on the field", "Dark field"),
        "fieldBorder": color("rgb(58, 58, 58)", "signup email class dark:border-[#3A3A3A]", "Dark field border"),
        "disabledFill": color(disabled_fill, S_AUTH + "; disabled fill was read on the light form", "Disabled fill"),
        "disabledInk": color(disabled_ink, S_AUTH + "; disabled ink was read on the light form", "Disabled ink"),
        "glass": color(glass_dark, S_DARK + "; search glass background", "Dark glass"),
        "chipOn": color(chip_on, S_DISC + "; selected chip stays brand", "Selected chip"),
        "cook": color(cook, S_RECIPE + "; cook pill does not invert", "Cook pill"),
    }
}

# Glass shadows from the declared custom properties, as DTCG shadow layers.
def split_top(v, sep):
    """Split on sep outside parentheses, so rgba(255, 255, 255, .95) stays whole."""
    out, depth, cur = [], 0, ""
    for ch in v:
        depth += ch == "("
        depth -= ch == ")"
        if ch == sep and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    return [x for x in out + [cur.strip()] if x]


LENGTH = re.compile(r"-?\d*\.?\d+(px)?")


def shadow_layers(raw, source, description):
    """Every layer of a declared box-shadow: `inset` anywhere, unitless 0, a negative spread.
    Raises on a layer or colour it cannot read instead of substituting a default."""
    layers = []
    for part in split_top(raw, ","):
        words = split_top(part, " ")
        inset = "inset" in words
        words = [w for w in words if w != "inset"]
        lengths = [w for w in words if LENGTH.fullmatch(w)]
        colours = [w for w in words if not LENGTH.fullmatch(w)]
        if len(colours) != 1 or not 2 <= len(lengths) <= 4:
            raise ValueError(f"{source}: cannot read shadow layer {part!r}")
        px = [w if w.endswith("px") else w + "px" for w in lengths] + ["0px"] * (4 - len(lengths))
        layer = {"offsetX": px[0], "offsetY": px[1], "blur": px[2], "spread": px[3], "color": norm_color(colours[0])}
        if inset:
            layer["inset"] = True
        layers.append(layer)
    return {"$value": layers, "$type": "shadow", "$description": description + " Declared: " + raw[:140], "$extensions": {"source": source}}


glass_rim = V["app"][0]["properties"]["--glass-rim"]
glass_lift = V["app"][0]["properties"]["--glass-lift"]
core["shadow"] = {
    "glassLift": shadow_layers(glass_lift, S_CSS + " .glass --glass-lift", "Glass lift"),
    "glassRim": shadow_layers(glass_rim, S_CSS + " .glass --glass-rim", "Glass rim"),
}

if (RAW / "motion.json").exists():
    core["motion"], _extra = motion_mod.build(json.loads((RAW / "motion.json").read_text()))
    if _extra:
        # what DTCG cannot carry (linear()/steps() easings, transitions past the first 60) stays
        # visible under core $extensions, as the kit keeps it
        core["$extensions"] = {"notTokenised": _extra}


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        check(path, node["$type"], node["$value"])
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            yield from walk(v, f"{path}.{k}" if path else k)


names = {n for n, _ in walk({"core": core, "light": light, "dark": dark})}
for n, t in walk({"core": core, "light": light, "dark": dark}):
    if not isinstance(t["$value"], str):
        continue
    for a in re.findall(r"\{([^{}]+)\}", t["$value"]):
        if not any(x == a or x.endswith("." + a) for x in names):
            raise KeyError(f"{n}: alias {{{a}}} missing")

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
def count(d):
    return sum(count(v) for k, v in d.items() if not k.startswith("$")) if isinstance(d, dict) and "$value" not in d else 1


if __name__ == "__main__":
    (HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")
    print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
