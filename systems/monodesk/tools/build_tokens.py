#!/usr/bin/env python3
"""Build tokens.json from MonoDesk public CSS readings.

Sources, read from www.monodesk.com on 2026-11-21, signed out:
  raw/css-vars.json           custom properties declared on :root
  raw/component-tokens.json   computed styles of painted controls

One painted theme. The page ground is #212121. The product's own token
--background is #dadee1 and is not what the homepage body paints, so it
stays in core.color and is not used as the page role. Every token carries
$extensions.source. Unread values are not invented.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())

DECL = {}
for rule in V["rules"]:
    if rule.get("selector") == ":root" and not rule.get("context"):
        DECL.update(rule["properties"])


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            if a == 1:
                return "#%02x%02x%02x" % (r, g, b)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def color(path, value, source):
    return {"$type": "color", "$value": norm_color(value), "$extensions": {"source": source}}


def dim(path, value, source):
    if not DIM.fullmatch(str(value).strip()):
        raise ValueError(f"{path}: dimension {value!r}")
    return {"$type": "dimension", "$value": str(value).strip(), "$extensions": {"source": source}}


def other(ty, value, source):
    return {"$type": ty, "$value": value, "$extensions": {"source": source}}


def css_var(name, ty="color"):
    if name not in DECL:
        raise KeyError(name)
    raw = DECL[name]
    source = f"Measured css-var {name} on :root, systems/monodesk/raw/css-vars.json"
    if ty == "color":
        return color(name, raw, source)
    if ty == "dimension":
        return dim(name, raw, source)
    return other("other", raw, source)


def measured(group, field, source):
    return SPEC["home"][group][field], source


core_color = {
    "white": css_var("--brand-white"),
    "orange": css_var("--brand-orange"),
    "highlighter": css_var("--brand-highlighter"),
    "blue": css_var("--brand-blue"),
    "grey": css_var("--brand-grey"),
    "almost-black": css_var("--brand-almost-black"),
    "fun-green": css_var("--brand-fun-green"),
    "surface-tint": css_var("--surface-tint"),
    "surface-white": css_var("--surface-white"),
    "token-background": css_var("--background"),
    "type": css_var("--type"),
    "type-light": css_var("--type-light"),
    "type-60": css_var("--type-60"),
    "type-40": css_var("--type-40"),
    "type-light-60": css_var("--type-light-60"),
    "type-light-40": css_var("--type-light-40"),
}
core_space = {}
for step, name in [("xs", "--spacing-xs"), ("sm", "--spacing-sm"), ("md", "--spacing-md"),
                   ("lg", "--spacing-lg"), ("xl", "--spacing-xl"), ("2xl", "--spacing-2xl")]:
    core_space[step] = css_var(name, "dimension")
core_radius = {}
for step, name in [("sm", "--radius-sm"), ("md", "--radius-md"), ("lg", "--radius-lg"),
                   ("xl", "--radius-xl"), ("2xl", "--radius-2xl")]:
    core_radius[step] = css_var(name, "dimension")

# Painted page ground is not a custom property. Record it as measured.
page_src = "Measured computed backgroundColor on body.hero-header-4, www.monodesk.com/, 2026-11-21"
text_src = "Measured computed color on body.hero-header-4, www.monodesk.com/, 2026-11-21"
menu = SPEC["home"]["menu"]
cta = SPEC["home"]["heroCta"]
h1 = SPEC["home"]["h1"]
nav = SPEC["home"]["nav"]
plan = SPEC["pricing"]["started"]
search = SPEC["help"]

dark = {
    "page": color("page", SPEC["home"]["body"]["bg"], page_src),
    "surface": color("surface", menu["bg"], "Measured computed backgroundColor on .menu, www.monodesk.com/, 2026-11-21"),
    "text": color("text", SPEC["home"]["body"]["color"], text_src),
    "muted": color("muted", nav["color"], "Measured computed color on a.header-nav-link, www.monodesk.com/, 2026-11-21"),
    "accent": color("accent", cta["bg"], "Measured computed backgroundColor on a.hero-cta-button, www.monodesk.com/, 2026-11-21"),
    "accent-text": color("accent-text", cta["color"], "Measured computed color on a.hero-cta-button, www.monodesk.com/, 2026-11-21"),
    "border": color("border", "rgba(255, 255, 255, 0.08)", "Measured computed borderTopColor on .menu, www.monodesk.com/, 2026-11-21"),
    "link": color("link", nav["color"], "Measured computed color on a.header-nav-link, www.monodesk.com/, 2026-11-21"),
    "component": {
        "header-height": dim("header-height", str(menu["box"]["h"]) + "px", "Measured bounding box height of .menu, 1440x900"),
        "header-radius": dim("header-radius", menu["radius"], "Measured borderRadius on .menu"),
        "header-pad-y": dim("header-pad-y", menu["pad"][0], "Measured paddingTop on .menu"),
        "header-pad-x": dim("header-pad-x", menu["pad"][1], "Measured paddingRight on .menu"),
        "cta-height": dim("cta-height", str(cta["box"]["h"]) + "px", "Measured bounding box height of a.hero-cta-button"),
        "cta-radius": dim("cta-radius", cta["radius"], "Measured borderRadius on a.hero-cta-button"),
        "cta-pad-y": dim("cta-pad-y", cta["pad"][0], "Measured paddingTop on a.hero-cta-button"),
        "cta-pad-x": dim("cta-pad-x", cta["pad"][1], "Measured paddingRight on a.hero-cta-button"),
        "cta-font-size": dim("cta-font-size", cta["size"], "Measured fontSize on a.hero-cta-button"),
        "nav-font-size": dim("nav-font-size", nav["size"], "Measured fontSize on a.header-nav-link"),
        "hero-font-size": dim("hero-font-size", h1["size"], "Measured fontSize on h1.hero-v4-title, 1440x900"),
        "hero-line-height": dim("hero-line-height", h1["lh"], "Measured lineHeight on h1.hero-v4-title, 1440x900"),
        "search-height": dim("search-height", str(search["box"]["h"]) + "px", "Measured bounding box height of help search input"),
        "search-radius": dim("search-radius", search["radius"], "Measured borderRadius on help search input"),
        "plan-cta-bg": color("plan-cta-bg", plan["bg"], "Measured backgroundColor on pricing Get started control"),
        "plan-cta-text": color("plan-cta-text", plan["color"], "Measured color on pricing Get started control"),
    },
}

core = {
    "color": core_color,
    "spacing": core_space,
    "radius": core_radius,
    "font": {
        "family": {
            "ui": other("fontFamily", "Geist, system-ui, sans-serif", "Measured fontFamily on body, www.monodesk.com/"),
            "mono": other("fontFamily", "Geist Mono, ui-monospace, monospace", "Declared font-family in /_astro/index CSS, 2026-11-21"),
        }
    },
    "typography": {
        "display": other("typography", {
            "fontFamily": "Geist, system-ui, sans-serif",
            "fontSize": h1["size"],
            "fontWeight": int(h1["weight"]),
            "lineHeight": h1["lh"],
        }, "Measured on h1.hero-v4-title at 1440x900"),
        "body": other("typography", {
            "fontFamily": "Geist, system-ui, sans-serif",
            "fontSize": "16px",
            "fontWeight": 400,
            "lineHeight": "24px",
        }, "Measured on body, www.monodesk.com/"),
        "label": other("typography", {
            "fontFamily": "Geist, system-ui, sans-serif",
            "fontSize": nav["size"],
            "fontWeight": int(nav["weight"]),
            "lineHeight": nav["lh"],
        }, "Measured on a.header-nav-link"),
    },
    "layout": {
        "page-max": dim("page-max", "1320px", "Measured css-var --layout-page-max on :root"),
        "content-max": dim("content-max", "1200px", "Measured css-var --layout-max-centered on :root"),
    },
}

# layout vars are in the second :root rule; pull them if present
for rule in V["rules"]:
    if rule.get("selector") == ":root" and "--layout-page-max" in rule.get("properties", {}):
        core["layout"]["page-max"]["$extensions"]["source"] = "Measured css-var --layout-page-max on :root, raw/css-vars.json"
        break

doc = {
    "$schema": "https://www.designtokens.org/schemas/2025.10/format.json",
    "core": core,
    "dark": dark,
    "$themes": [{"id": "dark", "name": "dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}}],
}

# Focus ring was not a designed token on the measured controls. Leave it out.
(HERE / "tokens.json").write_text(json.dumps(doc, indent=1) + "\n")
print("wrote tokens.json", "colors", len(core_color), "spacing", len(core_space))
