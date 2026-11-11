#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

b150.ai is a Next.js/Tailwind marketing site: it declares no app design-token
custom properties (the sheets carry only Tailwind --tw-* internals — see
raw/css-vars.json), so every value here is measured from computed styles on
the running page (raw/components-computed.json). Each leaf is
{"value": ..., "source": "..."} naming the measurement.

The palette is read off the components: ink text, the paper and wash
surfaces, whatever accent the buttons/CTAs paint, plus hover/focus/pressed
variants where states differ. Roles in `light` are only asserted where a
measured component wears the value. The site paints one theme (dark chrome, warm-cream sections); `dark`
is empty.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
C = json.loads((RAW / "components-computed.json").read_text())["components"]

SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. b150.ai is a "
    "Tailwind site that declares no design-token custom properties "
    "(css-vars.json records only --tw-* internals), so every value is a "
    "computed-style measurement on a named component. The site paints one "
    "painted theme; dark is empty."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    return node, parts[-1]


def emit(root, dotted, leaf):
    node, last = descend(root, dotted.split("-"))
    node[last] = leaf


def st(comp, state="default"):
    return C[comp]["states"][state]


def style(comp, state="default"):
    return st(comp, state)["style"]


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        return "#" + h
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    return v


def color_of(comp, prop="color", state="default"):
    return norm_color(style(comp, state).get(prop, ""))


meas = SPEC["core"].setdefault("measured", {})
pal = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
acc = SPEC["core"]["color"].setdefault("accent", {})

# ------------------------------------------------- palette from components
# Every measured colour is recorded once, keyed by what it paints.
CANDIDATES = [
    ("neutral", "ink", "nav-item", "color", "The body/nav text colour."),
    ("neutral", "paper", "header", "backgroundColor", "The header's surface (fallback: body)."),
    ("neutral", "wash", "footer", "backgroundColor", "The footer's surface."),
    ("accent", "primary", "signup-btn", "backgroundColor", "The SIGN UP pill fill."),
    ("accent", "primaryText", "signup-btn", "color", "Text on the accent pill."),
    ("accent", "cta", "hero-cta", "backgroundColor", "The JOIN THE BETA fill."),
    ("accent", "ctaText", "hero-cta", "color", "Text on the hero CTA."),
    ("accent", "hover", "signup-btn", "backgroundColor", "The accent's hover fill."),
]
for fam, key, comp, prop, desc in CANDIDATES:
    state = "hover" if key == "hover" else "default"
    try:
        v = color_of(comp, prop, state)
        if v and v not in ("transparent", "none", "rgba(0, 0, 0, 0)"):
            SPEC["core"]["color"].setdefault(fam, {})[key] = {
                "value": v, "type": "color",
                "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass

# Fallbacks for transparent-root components: header/footer sit on the page.
try:
    if pal.get("paper", {}).get("value") in (None, "transparent"):
        del pal["paper"]
except KeyError:
    pass

# --------------------------------------------------------------- roles
# Roles verified on a measured component. The light set mirrors the measured
# fills: text.primary is the nav/body colour; surfaces come from header,
# footer and section backgrounds; the action is the CTA pill.
ROLES = [
    ("text-primary", "nav-item", "color", "default", "Nav/body text colour — computed on the header nav."),
    ("text-inverse", "signup-btn", "color", "default", "Text on the accent pill."),
    ("surface-page", "footer", "backgroundColor", "default", "Page/footer surface."),
    ("action-primary", "hero-cta", "backgroundColor", "default", "The JOIN THE BETA CTA fill."),
    ("action-primaryText", "hero-cta", "color", "default", "Text on the CTA."),
    ("action-hover", "hero-cta", "backgroundColor", "hover", "The CTA's hover fill."),
    ("focus-ring", "nav-item", "outlineColor", "focus-visible", "The focus ring on header/footer links."),
]
for role, comp, prop, state, desc in ROLES:
    try:
        v = color_of(comp, prop, state)
        if v and v not in ("transparent", "none", "rgba(0, 0, 0, 0)"):
            node, last = descend(SPEC["light"], role.split("-"))
            node[last] = {"value": v, "type": "color",
                          "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                          "description": desc}
    except KeyError:
        pass

# --------------------------------------------------------------- fonts
SPEC["core"]["font"] = {"family": {}, "weight": {}, "size": {}, "tracking": {}}
fam_seen = {}
for comp in ("nav-item", "hero", "signup-btn", "talent-title", "footer-link", "contact-input"):
    try:
        f = style(comp)["fontFamily"].split(",")[0].strip('"').strip("'")
        fam_seen.setdefault(f, comp)
    except KeyError:
        pass
for i, (f, comp) in enumerate(sorted(fam_seen.items())):
    key = "primary" if i == 0 else f"alt{i}"
    SPEC["core"]["font"]["family"][key] = {
        "value": f, "type": "fontFamily",
        "source": f"computed fontFamily of {comp} (raw/components-computed.json)",
        "description": f"The {'main' if i == 0 else 'secondary'} family, measured."}
for comp, key, desc in [
    ("nav-item", "nav", "Nav links."),
    ("signup-btn", "button", "The SIGN UP pill label."),
    ("hero", "display", "The hero display heading."),
    ("talent-title", "title", "Page titles."),
    ("footer-link", "footer", "Footer links."),
    ("contact-input", "field", "Form fields."),
]:
    try:
        s = style(comp)
        fs = (st(comp).get("textStyle") or {}).get("fontSize") or s["fontSize"]
        SPEC["core"]["font"]["size"][key] = {
            "value": fs, "type": "dimension",
            "source": f"computed fontSize of {comp} (raw/components-computed.json)",
            "description": desc}
        w = s["fontWeight"]
        wk = {"300": "light", "400": "regular", "500": "medium", "600": "semibold", "700": "bold", "800": "black"}.get(w, "w" + w)
        SPEC["core"]["font"]["weight"].setdefault(wk, {
            "value": w, "type": "fontWeight",
            "source": f"computed fontWeight of {comp} (raw/components-computed.json)"})
    except KeyError:
        pass

# --------------------------------------------------------------- radius/layout
rad = SPEC["core"].setdefault("radius", {})
for comp, prop, key, desc in [
    ("signup-btn", "borderTopLeftRadius", "pill", "The SIGN UP pill's radius (rounded-full)."),
    ("contact-input", "borderTopLeftRadius", "field", "Field corners."),
    ("talent-card", "borderTopLeftRadius", "card", "Card corners."),
    ("hero-cta", "borderTopLeftRadius", "cta", "CTA corners."),
]:
    try:
        v = style(comp)[prop]
        if v and v != "0px":
            rad[key] = {"value": v, "type": "dimension",
                        "source": f"computed {prop} of {comp} (raw/components-computed.json)",
                        "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------------ component
comp_spec = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.height", "signup-btn", "default", "height", "The SIGN UP pill height."),
    ("control.ctaHeight", "hero-cta", "default", "height", "The JOIN THE BETA CTA height."),
    ("control.fieldHeight", "contact-input", "default", "height", "Contact field height."),
    ("header.height", "header", "default", "height", "The desktop header height."),
    ("header.heightMobile", "m-header", "default", "height", "The mobile header height."),
]:
    try:
        node = comp_spec
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)["style"][prop],
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
