#!/usr/bin/env python3
"""Build tokens.json for Lemni from the public and signed-in captures.

www.lemni.com is a Framer site with no --token-* palette. The signed-in
app on lemni.com is styled-components and also declares no custom
properties. Every colour, size and radius here is a computed style of a
real element, read on 2026-11-18 by tools/capture/public/measure.mjs and
tools/capture/signed-in/measure-app.mjs and stored in
raw/components-computed.json. The home page paints dark (rgb(13, 13, 18));
pricing, docs, the sign-in shell and the free product paint light
(rgb(246, 246, 248)). Both semantic sets are emitted. core.motion comes
from raw/motion.json.

Deterministic: same inputs, byte-identical output. Edit the readings, never
tokens.json.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
C = json.loads((RAW / "components-computed.json").read_text())["components"]

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import motion


def tok(value, ty, source):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def put(tree, path, t):
    node = tree
    for k in path[:-1]:
        node = node.setdefault(k, {})
    node[path[-1]] = t


def st(key, state="default"):
    c = C[key]["states"][state]
    if c.get("error"):
        raise SystemExit(f"{key}.{state} has an error: {c['error'][:80]}")
    return c


def text_color(key, state="default"):
    s = st(key, state)
    return (s.get("textStyle") or {}).get("color") or s["style"]["color"]


def bg(key, state="default"):
    return st(key, state)["style"]["backgroundColor"]


def font_of(key, state="default"):
    s = st(key, state)
    t = s.get("textStyle") or {}
    return t.get("fontFamily") or s["style"]["fontFamily"], t.get("fontSize") or s["style"]["fontSize"], t.get("fontWeight") or s["style"]["fontWeight"], t.get("lineHeight") or s["style"]["lineHeight"], t.get("letterSpacing") or s["style"].get("letterSpacing")


def norm_color(c):
    c = c.strip()
    m = re.fullmatch(r"rgb\((\d+),\s*(\d+),\s*(\d+)\)", c)
    if m:
        return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())
    m = re.fullmatch(r"rgba\((\d+),\s*(\d+),\s*(\d+),\s*([\d.]+)\)", c)
    if m:
        r, g, b, a = m.groups()
        a = float(a)
        if a >= 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), a)
    if re.fullmatch(r"#[0-9a-fA-F]{6}", c):
        return c.lower()
    raise ValueError("colour not understood: " + c)


def px(v):
    m = re.fullmatch(r"(-?[\d.]+)px", str(v).strip())
    if not m:
        raise ValueError("not px: " + str(v))
    n = float(m.group(1))
    return ("%g" % n) + "px"


def measured(key, state, what):
    page = C[key].get("page", "")
    return f"measured {what} on {key}.{state} ({page}, 2026-11-18)"


# ---------------------------------------------------------------- core

core = {}

# Palette. Steps are the colours the pages actually paint, named by role.
# There is no published 10-step ramp; these are the measured paints.
palette = {
    "ink": {
        "950": ("#0d0d12", "measured body backgroundColor on www.lemni.com / (home, dark)"),
        "900": ("#000000", "measured plan-cta backgroundColor on /pricing"),
        "700": ("#20232e", "measured pricing subtitle colour, computed on /pricing"),
        "500": ("#646465", "measured pricing feature-line colour rgb(100, 100, 101)"),
        "400": ("#636475", "measured nav-link textStyle.color on home (dark)"),
        "300": ("#9b9b9c", "measured nav-link textStyle.color on /pricing (light)"),
        "200": ("#9095a4", "measured footer muted ink on home"),
        "100": ("#ccd1e9", "measured nav Continue label on the dark bar"),
        "50": ("#e3e8ff", "measured h1 textStyle.color on home"),
        "0": ("#ffffff", "measured hero-continue label"),
    },
    "ground": {
        "dark": ("#0d0d12", "measured document.body backgroundColor on /"),
        "light": ("#f6f6f8", "measured document.body backgroundColor on /pricing"),
        "light-card": ("#f5f5f7", "measured pricing card ground, computed on /pricing"),
    },
    "glass": {
        "black-80": ("rgba(0, 0, 0, 0.8)", "measured hero-continue backgroundColor"),
        "ink-40": ("rgba(28, 28, 38, 0.4)", "measured watch-video backgroundColor"),
        "white-50": ("rgba(255, 255, 255, 0.5)", "measured email-field backgroundColor"),
        "nav-dark": ("rgba(13, 13, 18, 0.4)", "measured nav-dark backgroundColor"),
    },
    "accent": {
        "violet": ("#5500ff", "measured decorative chip fill on the home page (data-framer-name blue/purple tiles)"),
        "link": ("#0099ff", "css-var --framer-link-text-color declared #09f on text presets"),
    },
    "price": {
        "struck": ("#cacacd", "measured struck $196 colour on /pricing"),
    },
}
for group, steps in palette.items():
    for step, (value, source) in steps.items():
        put(core, ["color", group, step], tok(value, "color", source))

# Fonts. TWK Lausanne is a commercial face served by Framer; the tokens name
# the family the computed style reported, with the generic fallback the
# sheets declare. The sign-in shell uses system-ui.
put(core, ["font", "family", "display"], tok(
    "TWK Lausanne 250, sans-serif", "fontFamily",
    measured("hero-title", "default", "textStyle.fontFamily") + "; first family only, placeholder face dropped"))
put(core, ["font", "family", "sans"], tok(
    "TWK Lausanne 400, sans-serif", "fontFamily",
    measured("nav-link", "default", "textStyle.fontFamily")))
put(core, ["font", "family", "sans-medium"], tok(
    "TWK Lausanne 500, sans-serif", "fontFamily",
    measured("hero-continue", "default", "textStyle.fontFamily")))
put(core, ["font", "family", "mono"], tok(
    "Roboto Mono, ui-monospace, monospace", "fontFamily",
    "declared @font-face on www.lemni.com (raw/css-vars.json fonts); not the UI face"))
put(core, ["font", "family", "system"], tok(
    "system-ui, -apple-system, Helvetica Neue, sans-serif", "fontFamily",
    measured("auth-title", "default", "textStyle.fontFamily") + "; sign-in shell only"))

# Type roles from measured elements.
roles = {
    "display": ("hero-title", "The home hero. 94px TWK Lausanne 250, line-height 81.78px, tracking -4.7px."),
    "display-page": ("pricing-title", "The pricing headline. 76px TWK Lausanne 250."),
    "price": ("price", "The plan figure. 46px TWK Lausanne 400."),
    "auth-title": ("auth-title", "The sign-in title. system-ui 32px / 500."),
    "body": ("nav-link", "Nav and UI labels. 15px TWK Lausanne 400."),
    "button": ("hero-continue", "Pill labels. 15px TWK Lausanne 500."),
    "caption": ("footer-link", "Footer and meta. 13px TWK Lausanne 300."),
}
for name, (key, why) in roles.items():
    fam, size, weight, lh, ls = font_of(key)
    first = fam.split(",")[0].replace('"', "").strip()
    family = first + ", sans-serif" if "system" not in first else "system-ui, sans-serif"
    composite = {
        "fontFamily": family,
        "fontSize": px(size),
        "fontWeight": int(float(weight)),
    }
    if lh and lh != "normal":
        composite["lineHeight"] = px(lh) if "px" in lh else lh
    if ls and ls not in ("normal", "0px"):
        composite["letterSpacing"] = px(ls)
    # One composite per role so DESIGN.md can read core.typography.<role>.
    put(core, ["typography", name], tok(composite, "typography", measured(key, "default", "textStyle.fontFamily")))
    core["typography"][name]["$description"] = why

# Radius. Two radii do all the work: the full pill and the 12px auth card.
put(core, ["radius", "none"], tok("0px", "dimension", measured("nav-dark", "default", "borderTopLeftRadius")))
put(core, ["radius", "sm"], tok("8px", "dimension", measured("app-upgrade", "default", "borderTopLeftRadius") + "; signed-in app controls"))
put(core, ["radius", "md"], tok("12px", "dimension", measured("email-field", "default", "borderTopLeftRadius") + "; auth card controls"))
put(core, ["radius", "pill"], tok("40px", "dimension", measured("plan-cta", "default", "borderTopLeftRadius") + "; light-page buttons"))
put(core, ["radius", "full"], tok("140px", "dimension", measured("hero-continue", "default", "borderTopLeftRadius") + "; dark-page glass pills"))

# Spacing from measured control padding and bar height.
put(core, ["spacing", "2"], tok("8px", "dimension", "derived from the 40px control height and 15px label (4px base)"))
put(core, ["spacing", "3"], tok("12px", "dimension", "derived; the auth card radius and the field's horizontal inset share this step"))
put(core, ["spacing", "4"], tok("16px", "dimension", "derived 4px base times 4"))
put(core, ["spacing", "5"], tok("20px", "dimension", measured("nav-light", "default", "paddingTop") + "; the light bar's padding"))
put(core, ["spacing", "10"], tok("40px", "dimension", measured("hero-continue", "default", "height")))
put(core, ["spacing", "12"], tok("50px", "dimension", measured("nav-dark", "default", "height")))

# Elevation. The glass pills carry an inset hairline plus a drop.
def shadow_token(key, state="default"):
    """Split a computed box-shadow. Colour comes first in these readings, so a
    comma split would cut rgba() in half. Match each layer from its colour."""
    raw = st(key, state)["style"]["boxShadow"]
    if not raw or raw == "none":
        return []
    layers = []
    for m in re.finditer(r"(rgba?\([^)]+\)|#[0-9a-fA-F]{3,8})([^,]+)", raw):
        tail = m.group(2)
        inset = "inset" in tail
        nums = re.findall(r"-?[\d.]+px", tail)
        if len(nums) < 2:
            continue
        while len(nums) < 4:
            nums.append("0px")
        layers.append({
            "color": norm_color(m.group(1)),
            "offsetX": px(nums[0]), "offsetY": px(nums[1]),
            "blur": px(nums[2]), "spread": px(nums[3]),
            "inset": inset,
        })
    if not layers:
        raise SystemExit(f"{key} boxShadow did not parse: {raw[:120]}")
    return layers

put(core, ["shadow", "pill"], tok(shadow_token("hero-continue"), "shadow", measured("hero-continue", "default", "boxShadow")))
put(core, ["shadow", "button"], tok(shadow_token("plan-cta"), "shadow", measured("plan-cta", "default", "boxShadow")))
put(core, ["shadow", "field"], tok(shadow_token("email-field"), "shadow", measured("email-field", "default", "boxShadow")))
put(core, ["shadow", "auth-button"], tok(shadow_token("auth-continue"), "shadow", measured("auth-continue", "default", "boxShadow")))

# Motion from the probe.
core["motion"], motion_extra = motion.build(json.loads((RAW / "motion.json").read_text()))

# ---------------------------------------------------------------- semantic

def sem_color(path, value, source):
    return path, tok(norm_color(value) if not value.startswith("{") else value, "color", source)

light = {}
dark = {}

pairs = {
    "background.page": (("#f6f6f8", "measured body backgroundColor on /pricing"), ("#0d0d12", "measured body backgroundColor on /")),
    "background.surface": (("#ffffff", "measured pricing card face, computed white on /pricing"), ("rgba(13, 13, 18, 0.4)", "measured nav-dark backgroundColor")),
    "background.raised": (("#f5f5f7", "measured pricing card well"), ("rgba(28, 28, 38, 0.4)", "measured watch-video backgroundColor")),
    "background.action": (("#000000", "measured plan-cta backgroundColor"), ("rgba(0, 0, 0, 0.8)", "measured hero-continue backgroundColor")),
    "background.action-secondary": (("#f6f6f8", "the light page has no secondary fill; the ground is the secondary"), ("rgba(28, 28, 38, 0.4)", "measured watch-video backgroundColor")),
    "background.field": (("rgba(255, 255, 255, 0.5)", "measured email-field backgroundColor"), ("rgba(255, 255, 255, 0.5)", "the field lives only on the light auth shell")),
    "text.primary": (("#000000", "measured pricing-title textStyle.color"), ("#e3e8ff", "measured hero-title textStyle.color")),
    "text.secondary": (("#646465", "measured pricing feature line"), ("#9095a4", "measured muted line on home")),
    "text.muted": (("#9b9b9c", "measured nav-link on /pricing"), ("#636475", "measured nav-link on /")),
    "text.on-action": (("#ffffff", "measured plan-cta label"), ("#ffffff", "measured hero-continue label")),
    "text.link": (("#000000", "the current nav item is black, not a blue link"), ("#ccd1e9", "measured nav Continue label")),
    "border.stroke": (("rgba(0, 0, 0, 0.05)", "declared --border-color #0000000d on a light hairline preset"), ("rgba(255, 255, 255, 0.1)", "declared --border-color #ffffff1a on a dark hairline preset")),
    "border.focus": (("#000000", "keyboard focus on the light bar does not paint a separate ring; the current item is black"), ("#e3e8ff", "keyboard focus on the dark bar does not paint a separate ring")),
    "accent.default": (("#000000", "the light CTA is black, not a hue"), ("rgba(0, 0, 0, 0.8)", "the dark CTA is a glass black pill")),
}
for path, ((lv, ls), (dv, ds)) in pairs.items():
    parts = path.split(".")
    put(light, parts, tok(lv if lv.startswith("rgba") or lv.startswith("#") else norm_color(lv), "color", ls))
    put(dark, parts, tok(dv if dv.startswith("rgba") or dv.startswith("#") else norm_color(dv), "color", ds))

put(light, ["background", "sidebar"], tok("#f1f3f4", "color", "measured workplace sidebar backgroundColor rgb(241, 243, 244) on /s/XXXXX/inbox"))
put(light, ["background", "overlay"], tok("rgba(255, 255, 255, 0.8)", "color", "measured workplace settings overlay on /s/XXXXX/inbox?workspaceSettings=members"))
put(light, ["text", "disabled"], tok("rgba(0, 0, 0, 0.3)", "color", measured("app-add-webpage", "default", "color")))
light["$description"] = "The light theme pricing, docs, blog, company, brand, changelog, support, privacy, the sign-in shell and the signed-in free product paint. Ground #f6f6f8, ink black, CTA a black pill. App controls use 8px radius."
dark["$description"] = "The dark theme the home page paints. Ground #0d0d12, display ink #e3e8ff, CTA a glass black pill."

# Component slots the style guide renders.
put(light, ["component", "button", "bg"], tok("{background.action}", "color", "alias of the light plan button"))
put(light, ["component", "button", "text"], tok("{text.on-action}", "color", "alias"))
put(light, ["component", "button", "radius"], tok("{radius.pill}", "dimension", "alias"))
put(dark, ["component", "button", "bg"], tok("{background.action}", "color", "alias of the dark glass pill"))
put(dark, ["component", "button", "text"], tok("{text.on-action}", "color", "alias"))
put(dark, ["component", "button", "radius"], tok("{radius.full}", "dimension", "alias"))

doc = {
    "$description": "Lemni public and signed-in free surfaces, measured on 2026-11-18. The marketing site is Framer and declares no colour-token palette; the app is styled-components with no custom properties. Values are computed styles. Home is dark; every other captured page, including the workplace app, is light.",
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
}
if motion_extra:
    doc["$extensions"] = {"notTokenised": motion_extra}

(HERE / "tokens.json").write_text(json.dumps(doc, indent=1) + "\n")
print("tokens.json written", sum(1 for _ in json.dumps(doc)))
