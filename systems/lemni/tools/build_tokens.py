#!/usr/bin/env python3
"""Build tokens.json for Lemni from the public capture.

www.lemni.com is a Framer site with no --token-* palette. The sign-in
shell at lemni.com/signin is a separate React page and also declares no
custom properties. Every colour, size and radius here is a computed style
of a real public element, read on 2026-11-21 by
tools/capture/public/measure.mjs and stored in
raw/components-computed.json. The home page and changelog paint dark
(rgb(13, 13, 18)); pricing, docs and the sign-in shell paint light
(rgb(246, 246, 248)). Both semantic sets are emitted. core.motion comes
from raw/motion.json.

The workplace app was not entered on this pass. Tokens that previously
came from signed-in readings are omitted.

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
    when = (C[key].get("states") or {}).get(state, {}).get("read") or C[key].get("read") or "2026-11-21"
    return f"measured {what} on {key}.{state} ({page}, {when})"


# ---------------------------------------------------------------- core

core = {}

LAYOUT = json.loads((RAW / "layout.json").read_text())["pages"]


def layout_page(name):
    """A page reading in raw/layout.json; refuse to build without it."""
    if name not in LAYOUT:
        raise SystemExit(f"raw/layout.json has no pages.{name}: tools/capture/layout.mjs keeps the readings it does not take, so restore this one from git rather than rebuilding without it")
    return LAYOUT[name]

# Values with no raw reading behind them: typed in at capture time. They are kept
# (the style guide and the Do and don't use them) but labelled as reconstructions.
RECON = "Reconstruction: entered by hand at capture time; no raw reading holds this value"


def recon(note):
    return RECON + "; " + note


def read(key, state, prop):
    """One computed property of a measured state. `text.<prop>` reads the text
    node's style (textStyle), anything else the element's style."""
    s = st(key, state)
    if prop.startswith("text."):
        v = (s.get("textStyle") or {}).get(prop[5:])
    else:
        v = s["style"].get(prop)
    if v is None:
        raise SystemExit(f"{key}.{state} has no {prop}")
    return v


def color_of(key, state, prop):
    return norm_color(read(key, state, prop)), measured(key, state, prop.replace("text.", "textStyle."))


def body_bg(page):
    return norm_color(layout_page(page)["bodyBg"]), f"measured document.body backgroundColor in raw/layout.json pages.{page}"


# Palette. Steps are the colours the pages actually paint, named by role.
# There is no published 10-step ramp; these are the measured paints.
palette = {
    "ink": {
        "950": body_bg("home-1440"),
        "900": color_of("plan-cta", "default", "backgroundColor"),
        "700": color_of("auth-continue", "hover", "backgroundColor"),
        "500": color_of("auth-continue", "default", "text.color"),
        "400": color_of("nav-link", "default", "text.color"),
        "300": color_of("nav-light", "default", "text.color"),
        "200": color_of("footer-link", "hover", "text.color"),
        "100": color_of("nav-continue", "default", "text.color"),
        "50": color_of("hero-title", "default", "text.color"),
        "0": color_of("hero-continue", "default", "text.color"),
    },
    "ground": {
        "dark": body_bg("home-1440"),
        "light": body_bg("pricing-1440"),
        "light-card": ("#f5f5f7", recon("the pricing card ground; the card was not measured")),
    },
    "glass": {
        "black-80": color_of("hero-continue", "default", "backgroundColor"),
        "ink-40": color_of("watch-video", "default", "backgroundColor"),
        "white-50": color_of("email-field", "default", "backgroundColor"),
        "nav-dark": color_of("nav-dark", "default", "backgroundColor"),
    },
    "accent": {
        "violet": ("#5500ff", recon("the decorative chip fill on the home page; no chip was measured")),
        "link": ("#0099ff", recon("the link blue; the captured sheets reference --framer-link-text-color but never declare it")),
    },
    "price": {
        "struck": ("#cacacd", recon("the struck $196 figure on /pricing; only the price element's black text was measured")),
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
    measured("nav-link", "default", "textStyle.fontFamily") + "; first family only, placeholder face dropped"))
put(core, ["font", "family", "sans-medium"], tok(
    "TWK Lausanne 500, sans-serif", "fontFamily",
    measured("hero-continue", "default", "textStyle.fontFamily") + "; first family only, placeholder face dropped"))
put(core, ["font", "family", "mono"], tok(
    "Roboto Mono, ui-monospace, monospace", "fontFamily",
    "declared @font-face on www.lemni.com (raw/css-vars.json fonts); not the UI face; the ui-monospace, monospace fallbacks were added by hand"))
put(core, ["font", "family", "system"], tok(
    "system-ui, -apple-system, Helvetica Neue, sans-serif", "fontFamily",
    measured("auth-title", "default", "textStyle.fontFamily") + "; sign-in shell only; shortened by hand to the first three faces of the measured stack plus sans-serif"))

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
def dim(name, key, prop, note=""):
    put(core, name, tok(px(read(key, "default", prop)), "dimension", measured(key, "default", prop) + note))


dim(["radius", "none"], "nav-dark", "borderTopLeftRadius")
dim(["radius", "md"], "email-field", "borderTopLeftRadius", "; auth card controls")
dim(["radius", "pill"], "plan-cta", "borderTopLeftRadius", "; light-page buttons")
dim(["radius", "full"], "hero-continue", "borderTopLeftRadius", "; dark-page glass pills")

# Spacing from measured control padding and bar height.
put(core, ["spacing", "2"], tok("8px", "dimension", recon("a 4px-base step")))
put(core, ["spacing", "3"], tok("12px", "dimension", recon("a 4px-base step; 12px is measured only as the auth card radius")))
put(core, ["spacing", "4"], tok("16px", "dimension", recon("a 4px-base step")))
dim(["spacing", "5"], "nav-light", "paddingTop", "; the light bar's padding")
dim(["spacing", "10"], "hero-continue", "height")
dim(["spacing", "12"], "nav-dark", "height")

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
    "background.page": (body_bg("pricing-1440"), body_bg("home-1440")),
    "background.surface": (("#ffffff", recon("the white pricing card face; the card was not measured")), color_of("nav-dark", "default", "backgroundColor")),
    "background.raised": (("#f5f5f7", recon("the pricing card well; the card was not measured")), color_of("watch-video", "default", "backgroundColor")),
    "background.action": (color_of("plan-cta", "default", "backgroundColor"), color_of("hero-continue", "default", "backgroundColor")),
    "background.action-secondary": ((body_bg("pricing-1440")[0], "the light page has no secondary fill; the ground is the secondary"), color_of("watch-video", "default", "backgroundColor")),
    "background.field": (color_of("email-field", "default", "backgroundColor"), (color_of("email-field", "default", "backgroundColor")[0], "the field lives only on the light auth shell")),
    "text.primary": (color_of("pricing-title", "default", "text.color"), color_of("hero-title", "default", "text.color")),
    "text.secondary": (color_of("auth-continue", "default", "text.color"), color_of("footer-link", "hover", "text.color")),
    "text.muted": (color_of("nav-light", "default", "text.color"), color_of("nav-link", "default", "text.color")),
    "text.on-action": (color_of("plan-cta", "default", "text.color"), color_of("hero-continue", "default", "text.color")),
    "text.link": ((color_of("pricing-title", "default", "text.color")[0], "the current nav item is black, not a blue link"), color_of("nav-continue", "default", "text.color")),
    "border.stroke": (("rgba(0, 0, 0, 0.05)", "declared --border-color #0000000d on a light hairline preset"), ("rgba(255, 255, 255, 0.1)", "declared --border-color #ffffff1a on a dark hairline preset")),
    "border.focus": (("#000000", "keyboard focus on the light bar does not paint a separate ring; the current item is black"), ("#e3e8ff", "keyboard focus on the dark bar does not paint a separate ring")),
    "accent.default": (("{background.action}", "alias of background.action: the light CTA fill (plan-cta), black, not a hue"), ("{background.action}", "alias of background.action: the dark CTA fill (hero-continue), a glass black pill")),
}
for path, ((lv, ls), (dv, ds)) in pairs.items():
    parts = path.split(".")
    put(light, parts, tok(lv if lv.startswith(("rgba", "#", "{")) else norm_color(lv), "color", ls))
    put(dark, parts, tok(dv if dv.startswith(("rgba", "#", "{")) else norm_color(dv), "color", ds))

light["$description"] = "The light theme pricing, docs, blog, company, brand, support, privacy, terms and the sign-in shell paint. Ground #f6f6f8, ink black, CTA a black pill. Changelog paints the dark ground, not this set."
dark["$description"] = "The dark theme the home page paints. Ground #0d0d12, display ink #e3e8ff, CTA a glass black pill."

# Component slots the style guide renders.
put(light, ["component", "button", "bg"], tok("{background.action}", "color", "alias of the light plan button"))
put(light, ["component", "button", "text"], tok("{text.on-action}", "color", "alias"))
put(light, ["component", "button", "radius"], tok("{radius.pill}", "dimension", "alias"))
put(dark, ["component", "button", "bg"], tok("{background.action}", "color", "alias of the dark glass pill"))
put(dark, ["component", "button", "text"], tok("{text.on-action}", "color", "alias"))
put(dark, ["component", "button", "radius"], tok("{radius.full}", "dimension", "alias"))

doc = {
    "$description": "Lemni public surfaces, measured on 2026-11-21. The marketing site is Framer and declares no colour-token palette; the sign-in shell is styled-components with no custom properties. Values are computed styles. Home and changelog are dark; the other captured public pages are light. The workplace app was not entered.",
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
