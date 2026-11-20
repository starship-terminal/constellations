#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

biosites.com is a Next.js build (the `frontsitev2` CSS modules); it declares
no design-token custom properties at all — raw/css-vars.json records zero
--* names and the 10 @font-face rules (Canela and Clarkson). Every colour
below is therefore a computed-style measurement from
raw/components-computed.json, not a variable resolution.

The site is monochrome: black ink on white surfaces with a grey ramp, plus
one slate card colour (the persona cards) and alpha-black scrims. The nav
pills invert on hover (white pill/black text -> black pill/white text) and
so does the CTA (black pill -> white pill + hairline). A dark hero collage
and black marquee bands sit inside the light theme.

A leaf is {"value": ..., "source": "..."} — everything is measured here.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
C = json.loads((RAW / "components-computed.json").read_text())["components"]


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = None
    return node, parts[-1]


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. biosites.com "
    "declares no custom properties in its stylesheets, so the whole palette "
    "is measured: the monochrome inks and greys, the slate persona-card "
    "surface, the alpha scrims and the UA focus ring, each with the "
    "component+state it was read from. The site paints one light theme; "
    "the black hero and marquee bands live inside it."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def st(comp, state):
    c = C[comp]
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(comp)
    return c["states"][state]["style"]


def stprop(comp, state, prop):
    """prop may be `styleProp`, `textStyle.prop`, `::after.prop` or the special
    `ringShadow`: resolve the dotted path inside the measured state."""
    d = C[comp]["states"][state]
    if prop == "ringShadow":
        sh = d.get("style", {}).get("boxShadow", "") or ""
        for layer in re.split(r",(?![^(]*\))", sh):
            if re.search(r"0px 0px 0px\s+(?:0\.[5-9]|[1-9])[\d.]*px", layer):
                m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", layer)
                if m:
                    return m.group(0)
        return ""
    if "." in prop:
        head, tail = prop.split(".", 1)
        node = d.get(head)
        if not isinstance(node, dict):
            return ""
        return node.get(tail, "")
    return d.get("style", {}).get(prop, "")


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    return v


# --------------------------------------------------------------- palette
#
# Every entry is measured on the painted surface: token path ->
# (component, state, prop the value was read from). A `textStyle.` prop reads
# the deepest text-bearing child's colour; a `paint.N.bg`-style prop reads a
# painted sub-layer.
PALETTE = {
    "ink.0":   ("page-ground", "default", "backgroundColor"),       # #000000 body under the hero
    "ink.1":   ("cta", "default", "borderTopColor"),                # #010101 the CTA's hairline edge
    "ink.27":  ("claim-title", "default", "color"),                 # #1b1b1b the claim screen's ink
    "ink.42":  ("claim-submit", "default", "backgroundColor"),      # #2a2a2a the circular submit's fill
    "grey.106": ("hero-sub", "default", "color"),                   # #6a6a6a the muted grey
    "grey.156": ("claim-legal", "default", "color"),                # #9c9c9c the faint legal grey (the field placeholder reads it too)
    "grey.230": ("cta", "hover", "borderTopColor"),                 # #e6e6e6 the inverted CTA's hairline (the submit arrow's fill)
    "white":   ("nav-link", "default", "backgroundColor"),          # #ffffff
    "slate.500": ("persona-card", "default", "backgroundColor"),    # #4f566f the persona card
    "alpha.ink20": ("claim-field-wrap", "default", "borderTopColor"),  # rgba(0,0,0,.2) the field hairline
    "alpha.ink25": ("card-cta", "default", "backgroundColor"),      # rgba(0,0,0,.25) the card pill (unchanged on hover)
    "blue.focus": ("claim-login", "focus-visible", "outlineColor"), # #005fcc the UA focus ring
}

for path, (comp, state, prop) in PALETTE.items():
    v = norm_color(stprop(comp, state, prop))
    if not v or v == "transparent" or v == "rgba(0, 0, 0, 0)":
        continue
    node, last = descend(SPEC["core"].setdefault("color", {}), path.split("."))
    node[last] = {"type": "color", "value": v,
                  "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)"}

# The claim page ground is not any component's own fill: body paints #fafafa
# on /editor (read off the page during capture). No reading in raw/ holds it,
# so it is labelled as entered by hand.
SPEC["core"]["color"]["grey"]["250"] = {
    "type": "color", "value": "#fafafa",
    "source": "entered by hand at capture time, not a committed reading: the body backgroundColor on /editor (the claim screen) as read off the page; raw/components-computed.json holds no body or /editor ground"}

# An index of palette values so roles below can alias instead of repeating a hex.
BY_VALUE = {}
def collect(node, prefix=""):
    for k, v in node.items():
        if isinstance(v, dict) and "value" in v and isinstance(v["value"], str):
            BY_VALUE.setdefault(v["value"], prefix + k)
        elif isinstance(v, dict):
            collect(v, prefix + k + ".")
collect(SPEC["core"]["color"], "color.")


def role(theme, path, comp, state, prop, desc):
    v = norm_color(stprop(comp, state, prop))
    if not v or v == "transparent" or v == "rgba(0, 0, 0, 0)":
        return
    target = BY_VALUE.get(v)
    leaf = {"type": "color", "description": desc}
    if target:
        leaf["value"] = "{%s}" % target
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json); same value as core.{target}"
    else:
        leaf["value"] = v
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
    node = SPEC[theme]
    parts = path.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


# ------------------------------------------------------------- light roles
#
# One painted theme. The white content surface, the black band the hero and
# marquee sit on, the inverted pill/CTA pair, and the muted greys.
for path, comp, state, prop, desc in [
    ("page", "footer", "default", "backgroundColor", "The white content surface the sections and footer paint."),
    ("band", "page-ground", "default", "backgroundColor", "The black fill under the hero collage; the marquee bands paint it too."),
    ("surface", "nav-link", "default", "backgroundColor", "The white pill surface of the nav controls."),
    ("surfaceInverse", "nav-signup", "hover", "backgroundColor", "The black pill fill the nav controls invert to on hover, and the signup pill at rest."),
    ("card", "persona-card", "default", "backgroundColor", "The slate persona card."),
    ("scrim", "card-cta", "default", "backgroundColor", "The translucent black card-cta pill."),
    ("text", "hero-title", "default", "color", "Primary ink on the light surface."),
    ("muted", "hero-sub", "default", "color", "The grey subcopy/link colour."),
    ("faint", "claim-legal", "default", "color", "The faint legal-grey small print."),
    ("textInverse", "cta", "default", "color", "White text on black fills (pills, CTA, dark bands)."),
    ("link", "footer-link", "default", "color", "Footer column links read muted grey, not a brand blue."),
    ("accent", "cta", "default", "backgroundColor", "The CTA's black fill — the site's accent is monochrome."),
    ("accentText", "cta", "default", "color", "White label on the black CTA."),
    ("accentHover", "cta", "hover", "backgroundColor", "The CTA on hover inverts to white."),
    ("accentHoverText", "cta", "hover", "color", "The CTA label on hover reads black."),
    ("border", "claim-field-wrap", "default", "borderTopColor", "The hairline on the claim field shell."),
    ("borderHover", "cta", "hover", "borderTopColor", "The hairline on the inverted CTA."),
    ("focus", "claim-login", "focus-visible", "outlineColor", "The keyboard-focus ring the browser paints on the claim screen."),
]:
    try:
        role("light", path, comp, state, prop, desc)
    except KeyError:
        pass

# The claim page ground is not any component's own fill: body paints #fafafa
# on /editor, a value entered by hand at capture time (see grey.250 above).
SPEC["light"]["claimPage"] = {
    "type": "color", "value": "{color.grey.250}",
    "source": "alias of core.color.grey.250, which was entered by hand at capture time (the body backgroundColor on /editor, the claim screen, as read off the page), not a committed reading",
    "description": "The signed-out claim screen's ground, a whisper off pure white.",
}

# -------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})
for comp, state, key, prop, desc in [
    ("nav-link", "hover", "navpill-hover", "backgroundColor", "The nav pill's black fill on hover."),
    ("cta", "hover", "cta-hover", "backgroundColor", "The CTA's white fill on hover."),
    # card-cta keeps its rgba(0,0,0,.25) fill on hover; what changes is opacity
    # (0 -> 1, driven by the card), which components.md's state table records.
    ("claim-submit", "default", "claim-submit-bg", "backgroundColor", "The circular claim submit's grey fill."),
    ("claim-submit", "hover", "claim-submit-hover", "backgroundColor", "The claim submit on hover."),
    ("claim-login", "default", "login-pill", "backgroundColor", "The Log In pill on the claim screen."),
]:
    try:
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent":
            meas[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------------ type

def typ(comp, state):
    d = C[comp]["states"][state]
    s = d["style"]
    t = d.get("textStyle") or {}
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": (t.get("fontFamily") or s["fontFamily"]).split(",")[0].strip('"'),
            "fontSize": t.get("fontSize") or s["fontSize"],
            "fontWeight": int(float(t.get("fontWeight") or s["fontWeight"])),
            "lineHeight": t.get("lineHeight") or s["lineHeight"],
            # computed "normal" is no tracking; DTCG wants a dimension, so it is written 0px
            "letterSpacing": "0px" if (t.get("letterSpacing") or s["letterSpacing"]) == "normal" else (t.get("letterSpacing") or s["letterSpacing"]),
        },
        "$extensions": {"source": f"computed type of {comp} {state} (raw/components-computed.json)"},
    }


SPEC["core"]["typography"] = {}
for path, comp, state, desc in [
    ("marquee", "footer-cta", "default", "The giant 70px caps call (BIO.SITE/YOURNAME, the section links)."),
    ("display", "hero-title", "default", "The h1 headline (Clarkson medium, tight tracking)."),
    ("title", "section-title", "default", "An h2 section title."),
    ("body", "hero-sub", "default", "The paragraph under the hero."),
    ("question", "faq-item", "default", "An FAQ question row."),
    ("label", "nav-link", "default", "Nav pill label type (Clarkson medium, caps)."),
    ("button", "cta", "default", "CTA label type."),
    ("eyebrow", "eyebrow", "default", "The TRUSTED BY MILLIONS OF eyebrow."),
]:
    try:
        node = SPEC["core"]["typography"]
        t = typ(comp, state)
        t["$description"] = desc
        node[path] = t
    except KeyError:
        pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.heightNav", "nav-link", "default", "height", "The nav pill height."),
    ("control.heightCta", "cta", "default", "height", "The big CTA pill height."),
    ("control.heightCardCta", "card-cta", "default", "height", "The card Get-started pill height."),
    ("control.heightField", "claim-field-wrap", "default", "height", "The claim field shell height."),
    ("control.heightSubmit", "claim-submit", "default", "height", "The circular claim submit."),
    ("control.heightLogin", "claim-login", "default", "height", "The claim screen's Log In pill."),
    ("control.radiusPill", "nav-link", "default", "borderTopLeftRadius", "The nav pills' corner."),
    ("control.radiusCta", "cta", "default", "borderTopLeftRadius", "The CTA's corner."),
    ("control.radiusField", "claim-field-wrap", "default", "borderTopLeftRadius", "The claim shell's corner."),
    ("control.radiusCard", "persona-card", "default", "borderTopLeftRadius", "The persona card's corner."),
    ("header.height", "navbar", "default", "height", "The fixed navbar at 1440px."),
    ("header.heightMobile", "m-navbar", "default", "height", "The fixed navbar at 390px."),
    ("footer.height", "footer", "default", "height", "The footer band at 1440px."),
    ("mobile.ctaHeight", "m-cta", "default", "height", "The CTA at 390px."),
]:
    try:
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)[prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
