#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

luma.com declares a real token layer on html.theme-root and rebinds the
semantic roles under html.theme-root.dark. Marketing pages paint light. A
public event page paints dark on its own. Declared variables become var
leaves. Geometry the stylesheets do not name (the landing title, the painted
button radii) is a measured leaf from raw/components-computed.json.

A leaf is {"var": "--name", "type": ...} or {"value": ..., "source": "..."}.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V["resolved"]
RL = {n: v.get("value", v.get("raw")) for n, v in RES["light"].items()}
RD = {n: v.get("value", v.get("raw")) for n, v in RES["dark"].items()}
C = json.loads((RAW / "components-computed.json").read_text())["components"]


def var(name, ty="color", **kw):
    if name not in RL and name not in RD:
        raise KeyError(name)
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


LAYER = re.compile(
    r"(rgba?\(\s*[\d.]+,?\s*[\d.]+,?\s*[\d.]+(?:,?\s*[\d.]+)?\)|#[0-9a-fA-F]{3,8})\s+"
    r"(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(?:\s+(-?[\d.]+)px)?")


def shadow_layers(spec):
    """Parse 'rgba(...) x y blur spread [inset], ...' (the computed form) into DTCG shadow layers.

    Every top-level layer must parse, and an inset layer keeps inset: true. Before the 2026-11
    audit the inset top edge of --shadow-modal was written as an outer drop shadow.
    """
    parts, depth, cur = [], 0, ""
    for ch in spec:
        depth += ch == "("
        depth -= ch == ")"
        if ch == "," and depth == 0:
            parts.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur.strip())
    out = []
    for part in parts:
        words = part.split()
        inset = "inset" in words
        body = " ".join(w for w in words if w != "inset")
        m = LAYER.fullmatch(body)
        if not m:
            raise ValueError(f"shadow layer not understood: {part!r}")
        col, x, y, bl, sp = m.groups()
        layer = {
            "color": col, "offsetX": f"{x}px", "offsetY": f"{y}px",
            "blur": f"{bl}px", "spread": f"{sp or 0}px",
        }
        if inset:
            layer["inset"] = True
        out.append(layer)
    return out


SPEC = {
    "_about": (
        "Luma's declared --color / --gray / --font layer, resolved on "
        "html.theme-root.light and html.theme-root.dark, plus measured "
        "geometry from the public signed-out pages."
    ),
    "core": {},
    "light": {},
    "dark": {},
    "component": {},
}


def put(tree, path, leaf):
    node = tree
    parts = path.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


# Gray ramp and named inks. These do not flip with the theme.
for step in ("10", "20", "30", "40", "50", "60", "70", "80", "90", "100"):
    put(SPEC["core"], f"color.gray.{step}", var(f"--gray-{step}"))
put(SPEC["core"], "color.ink", var("--black"))
put(SPEC["core"], "color.white", var("--white"))
put(SPEC["core"], "color.pure-black", var("--pure-black"))

# Status hues that stay in core as the light-theme declaration. Dark rebinds
# the same names, so the semantic sets carry the theme-specific values.
for name, key in (
    ("brand", "--brand-color"),
    ("brand-active", "--brand-active-color"),
    ("success", "--success-color"),
    ("error", "--error-color"),
    ("warning", "--warning-color"),
):
    put(SPEC["core"], f"color.status.{name}", var(key, description=f"Light-theme declaration of {key}. Dark rebinds it."))

# Type. --font is the UI stack. --title-font prepends Google Sans Flex, the
# face event titles actually paint. --font-weight-light is declared and unused
# by the measured surfaces, so it stays out.
put(SPEC["core"], "font.family.sans", var("--font", "fontFamily"))
put(SPEC["core"], "font.family.title", var("--title-font", "fontFamily"))
put(SPEC["core"], "font.family.mono", var("--mono-font", "fontFamily"))
for step, name in (
    ("xxxs", "xxxs"), ("xxs", "xxs"), ("xs", "xs"), ("sm", "sm"), ("md", "md"),
    ("lg", "lg"), ("xl", "xl"), ("xxl", "xxl"), ("xxxl", "xxxl"),
):
    put(SPEC["core"], f"font.size.{step}", var(f"--font-size-{name}", "dimension"))
for w, name in (("regular", "regular"), ("medium", "medium"), ("bold", "bold")):
    put(SPEC["core"], f"font.weight.{w}", var(f"--font-weight-{name}", "fontWeight"))

# Geometry declared on body (inherited). These are theme-independent.
for key, token in (
    ("--small-border-radius", "sm"),
    ("--border-radius", "md"),
    ("--card-border-radius", "card"),
    ("--large-border-radius", "lg"),
    ("--squircle-border-radius", "squircle"),
    ("--card-squircle-border-radius", "card-squircle"),
    ("--modal-border-radius", "modal"),
    ("--modal-squircle-border-radius", "modal-squircle"),
):
    if key in RL:
        put(SPEC["core"], f"radius.{token}", var(key, "dimension"))

for key, token in (
    ("--input-height", "input"),
    ("--large-input-height", "input-lg"),
    ("--input-horizontal-padding", "input-x"),
    ("--input-vertical-padding", "input-y"),
    ("--button-icon-only-padding", "icon-button"),
    ("--horizontal-padding", "page-x"),
):
    if key in RL:
        put(SPEC["core"], f"size.{token}", var(key, "dimension"))

# Elevation. The light-shadow scale is what cards and modals name. The
# medium-shadow scale is a second declared family, heavier, and stays beside it.
for key, token, note in (
    ("--shadow-xs", "xs", "Hairline lift."),
    ("--shadow-sm", "sm", "Small card lift. Same layers as --light-shadow-sm and --chat-box-shadow."),
    ("--shadow", "md", "Default elevation. Same layers as --light-shadow."),
    ("--shadow-lg", "lg", "Large elevation. Same layers as --light-shadow-lg."),
    ("--shadow-xl", "xl", "Largest elevation. Same layers as --light-shadow-xl."),
    ("--shadow-modal", "modal", "Modal: a 1px hairline plus the large shadow and an inset top edge."),
    ("--card-hover-shadow", "card-hover", "The hover lift named for content cards."),
):
    raw = RL.get(key)
    if not isinstance(raw, str):
        raise KeyError(key)
    layers = shadow_layers(raw)
    if not layers:
        raise ValueError(f"{key} parsed to no layers")
    put(SPEC["core"], f"shadow.{token}", {
        "value": layers, "type": "shadow",
        "source": f"css-var {key} (light); {note}",
    })

# Motion. Durations are declared. The easing is the standard material curve.
put(SPEC["core"], "duration.fast", var("--fast-transition-duration", "duration"))
put(SPEC["core"], "duration.base", var("--transition-duration", "duration"))
put(SPEC["core"], "duration.slow", var("--slow-transition-duration", "duration"))
put(SPEC["core"], "easing.standard", var("--transition-fn", "cubicBezier"))
put(SPEC["core"], "easing.bounce", var("--bounce-transition-fn", "cubicBezier"))

# Semantic roles, both themes.
ROLES = {
    "color.text.primary": "--primary-color",
    "color.text.secondary": "--secondary-color",
    "color.text.tertiary": "--tertiary-color",
    "color.text.quaternary": "--quaternary-color",
    "color.bg.page": "--primary-bg-color",
    "color.bg.sunken": "--secondary-bg-color",
    "color.bg.muted": "--tertiary-bg-color",
    "color.bg.elevated": "--elevated-primary-bg-color",
    "color.bg.modal": "--modal-bg-color",
    "color.bg.menu": "--menu-bg-color",
    "color.border.primary": "--primary-border-color",
    "color.border.divider": "--divider-color",
    "color.bg.hover": "--hover-bg-color",
    "color.brand": "--brand-color",
    "color.brand-active": "--brand-active-color",
    "color.success": "--success-color",
    "color.error": "--error-color",
    "color.warning": "--warning-color",
}
for path, name in ROLES.items():
    put(SPEC["light"], path, var(name))
    put(SPEC["dark"], path, var(name))

# Measured component geometry. These do not flip with the theme.
def style_px(comp, state, prop):
    st = C[comp]["states"][state]["style"]
    return {"value": st[prop], "type": "dimension", "source": f"measured {comp} {state} {prop}"}


def style_color(comp, state, prop):
    st = C[comp]["states"][state]["style"]
    return {"value": st[prop], "type": "color", "source": f"measured {comp} {state} {prop}"}


if "nav-signin" in C:
    put(SPEC["component"], "signin-pill.radius", style_px("nav-signin", "default", "borderTopLeftRadius"))
    put(SPEC["component"], "signin-pill.height", {
        "value": f"{C['nav-signin']['states']['default']['rect']['h']}px",
        "type": "dimension",
        "source": "measured nav-signin default rect height",
    })
if "cta-create" in C:
    put(SPEC["component"], "create-pill.radius", style_px("cta-create", "default", "borderTopLeftRadius"))
    put(SPEC["component"], "create-pill.bg", style_color("cta-create", "default", "backgroundColor"))
    put(SPEC["component"], "create-pill.color", style_color("cta-create", "default", "color"))
if "plan-cta" in C:
    put(SPEC["component"], "primary-button.radius", style_px("plan-cta", "default", "borderTopLeftRadius"))
    put(SPEC["component"], "primary-button.bg", style_color("plan-cta", "default", "backgroundColor"))
    put(SPEC["component"], "primary-button.height", {
        "value": f"{C['plan-cta']['states']['default']['rect']['h']}px",
        "type": "dimension",
        "source": "measured plan-cta default rect height",
    })
if "plan-cta-brand" in C:
    put(SPEC["component"], "brand-button.bg", style_color("plan-cta-brand", "default", "backgroundColor"))
    put(SPEC["component"], "brand-button.radius", style_px("plan-cta-brand", "default", "borderTopLeftRadius"))
if "email-field" in C:
    put(SPEC["component"], "field.radius", style_px("email-field", "default", "borderTopLeftRadius"))
    put(SPEC["component"], "field.height", {
        "value": f"{C['email-field']['states']['default']['rect']['h']}px",
        "type": "dimension",
        "source": "measured email-field default rect height",
    })
if "plan-card" in C:
    put(SPEC["component"], "plan-card.radius", style_px("plan-card", "default", "borderTopLeftRadius"))
if "hero-title" in C:
    put(SPEC["component"], "hero-title.size", style_px("hero-title", "default", "fontSize"))
    put(SPEC["component"], "hero-title.weight", {
        "value": int(float(C["hero-title"]["states"]["default"]["style"]["fontWeight"])),
        "type": "fontWeight",
        "source": "measured hero-title default fontWeight",
    })
if "pricing-title" in C:
    put(SPEC["component"], "pricing-title.size", style_px("pricing-title", "default", "fontSize"))

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2) + "\n")
print("wrote", RAW / "component-tokens.json")
