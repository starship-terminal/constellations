#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/computed-home.json.

reclaim.ai's marketing CSS declares a Webflow variable set on :root
(--_brand-colors-2026---*, --_apps---colors--*, --royal-blue). Those are
Measured custom properties. The public site paints light only. The *-dark
names are declared and recorded under core.declaredDark. They are not a
painted theme.

The visible desktop "Get Started" button paints #0061fe. The declared
primary is var(--royal-blue) = #5562eb. Both are kept. The painted value
is the light.accent role.

Deterministic. Edit the raw files, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "computed-home.json").read_text())

ROOT = next(r for r in V["app"] if r.get("selector") == ":root")["properties"]


def norm_color(v):
    v = str(v).strip().lower()
    if v.startswith("var("):
        return None
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8 and h[6:] != "ff":
            a = round(int(h[6:8], 16) / 255, 3)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    return None


def color(path, value, source):
    hexed = norm_color(value)
    if not hexed:
        raise ValueError(f"{path}: not a colour {value!r}")
    return {"$type": "color", "$value": hexed, "$extensions": {"source": source}}


def dim(path, value, source):
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(value)):
        raise ValueError(f"{path}: dimension {value!r}")
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$type": ty, "$value": value, "$extensions": {"source": source}}


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.strip("-").lower()).strip("-")


def resolve(raw, name):
    raw = str(raw).strip()
    src = f"css-var {name}"
    if raw.startswith("var("):
        inner = raw[4:].split(")")[0].strip()
        if inner not in ROOT:
            raise ValueError(f"{name} aliases missing {inner}")
        raw = ROOT[inner]
        src = f"css-var {name} alias of {inner}, resolved {raw}"
    return raw, src


core_color = {}
declared_dark = {}
for name, raw in sorted(ROOT.items()):
    if name.startswith("--_apps---charts--"):
        group = core_color.setdefault("chart", {})
        key = slug(name.replace("--_apps---charts--chart-", "chart-"))
        val, src = resolve(raw, name)
        if key.endswith("-dark"):
            declared_dark.setdefault("chart", {})[key[:-5]] = color(name, val, src + "; declared, not painted on the public site")
        else:
            group[key] = color(name, val, src)
        continue
    if name.startswith("--_apps---colors--"):
        key = slug(name.replace("--_apps---colors--", ""))
        val, src = resolve(raw, name)
        if key.endswith("-dark"):
            declared_dark.setdefault("app", {})[key[:-5]] = color(name, val, src + "; declared, not painted on the public site")
        else:
            core_color.setdefault("app", {})[key] = color(name, val, src)
        continue
    if name.startswith("--_brand-colors-2026---"):
        key = slug(name.replace("--_brand-colors-2026---", ""))
        core_color.setdefault("brand", {})[key] = color(name, raw, f"css-var {name}")
        continue
    if name in ("--royal-blue", "--goldenrod", "--case-study-blurple", "--case-study-corn", "--case-study-pink"):
        core_color.setdefault("named", {})[slug(name)] = color(name, raw, f"css-var {name}")

# Painted roles from the live homepage computed styles.
body = C["body"]
h1 = C["h1"]
h2 = C["h2"]
nav_cta = next(b for b in C["buttons"] if b["cls"].startswith("nav_start_button w-button") and b["w"] > 0)
demo = next(b for b in C["buttons"] if "Book a Demo" in b["text"] and b["w"] > 0)
pricing = C["pricing"]

light = {
    "page": color("page", body["bg"], "measured computed backgroundColor on body, home, 1440"),
    "surface": color("surface", "#ffffff", "measured computed backgroundColor on body; card token --_apps---colors--card is also #fff"),
    "text": color("text", body["color"], "measured computed color on body, home, 1440"),
    "muted": color("muted", "#7d797a", "css-var --_apps---colors--muted-foreground; not sampled from a muted label this pass"),
    "accent": color("accent", nav_cta["bg"], "measured computed backgroundColor on a.nav_start_button.w-button (Get Started), home, 1440"),
    "onAccent": color("onAccent", nav_cta["color"], "measured computed color on a.nav_start_button.w-button"),
    "border": color("border", "#181d25", "css-var --_apps---colors--border; the Book a Demo outline paints #000000 instead"),
    "link": color("link", pricing["color"], "measured computed color on the Pricing nav link"),
    "destructive": {"$value": "{color.app.destructive}", "$type": "color", "$extensions": {"source": "alias of declared --_apps---colors--destructive"}},
}

typography = {
    "display": {
        "$type": "typography",
        "$value": {
            "fontFamily": "Sharp Grotesk DB Book 23",
            "fontSize": "90px",
            "fontWeight": 500,
            "lineHeight": "90px",
            "letterSpacing": "-2px",
        },
        "$extensions": {"source": "measured computed style on h1._26_h1, home, 1440"},
    },
    "heading": {
        "$type": "typography",
        "$value": {
            "fontFamily": "Sharp Grotesk DB Book 20",
            "fontSize": "48px",
            "fontWeight": 400,
            "lineHeight": "57.6px",
            "letterSpacing": "0px",
        },
        "$extensions": {"source": "measured computed style on h2._25_h2, home, 1440"},
    },
    "body": {
        "$type": "typography",
        "$value": {
            "fontFamily": "Poppins",
            "fontSize": "18px",
            "fontWeight": 400,
            "lineHeight": "32px",
            "letterSpacing": "0px",
        },
        "$extensions": {"source": "measured computed style on body, home, 1440"},
    },
    "label": {
        "$type": "typography",
        "$value": {
            "fontFamily": "Atlas Grotesk Web",
            "fontSize": "16px",
            "fontWeight": 300,
            "lineHeight": "20px",
            "letterSpacing": "0px",
        },
        "$extensions": {"source": "measured computed style on a.nav_start_button.w-button, home, 1440"},
    },
}

radius = {
    "control": dim("radius.control", "10px", "measured borderRadius on a.nav_start_button and css-var --_apps---sizes--radius"),
    "pill": dim("radius.pill", "100px", "measured borderRadius on a.hero_cta_button (hidden at 1440, painted in CSS)"),
}

spacing = {
    "2": dim("spacing.2", "10px", "measured paddingTop on a.nav_start_button"),
    "4": dim("spacing.4", "15px", "measured paddingLeft on the Pricing nav link"),
    "6": dim("spacing.6", "30px", "measured paddingRight on a.nav_start_button"),
}

component = {
    "button": {
        "bg": color("button.bg", nav_cta["bg"], "measured a.nav_start_button backgroundColor"),
        "text": color("button.text", nav_cta["color"], "measured a.nav_start_button color"),
        "radius": dim("button.radius", "10px", "measured a.nav_start_button borderRadius"),
        "height": dim("button.height", "40px", "measured a.nav_start_button height, 1440"),
    },
    "button-quiet": {
        "bg": color("button-quiet.bg", "rgba(0, 0, 0, 0)", "measured Book a Demo backgroundColor"),
        "text": color("button-quiet.text", demo["color"], "measured Book a Demo color"),
        "border": color("button-quiet.border", "#000000", "measured Book a Demo borderTopColor"),
        "radius": dim("button-quiet.radius", "10px", "measured Book a Demo borderRadius"),
    },
}

tokens = {
    "$schema": "https://www.designtokens.org/schemas/2025.10/format.json",
    "core": {
        "color": core_color,
        "declaredDark": declared_dark,
        "typography": typography,
        "radius": radius,
        "spacing": spacing,
    },
    "light": {
        **light,
        "component": component,
    },
    "$themes": [{"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}

# Alias check
def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        val = node["$value"]
        if isinstance(val, str) and val.startswith("{") and val.endswith("}"):
            parts = val[1:-1].split(".")
            cur = tokens["core"] if parts[0] == "color" else None
            # aliases in this file are {color.app.destructive} resolved from core.color
            cur = tokens["core"]["color"]
            for p in parts[1:]:
                cur = cur[p]
            if "$value" not in cur:
                raise SystemExit(f"bad alias {path} -> {val}")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, path + "." + k)

walk(tokens)
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1) + "\n")
print("wrote tokens.json", "brand", len(core_color.get("brand", {})), "app", len(core_color.get("app", {})))
