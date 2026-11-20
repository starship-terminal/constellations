#!/usr/bin/env python3
"""Write raw/component-tokens.json from the Krea stylesheet harvest and measurements.

krea.ai (captured 2026-11-18, signed out) paints one public theme: html.dark.
The Tailwind v4 @theme layer on :root,:host declares the primary grey ramp,
the action blue, radius, spacing and the Suisse Intl stacks. Semantic shadcn
roles (--background, --foreground, --sidebar, ...) are declared on
`.dark, :root[data-theme="dark"]` and resolved in raw/css-vars.json under
resolved.appDark.

The light comparison pass (html.light on the same sheets) is not a shipped
public theme. Docs (/docs, html.light) uses a separate sheet set and is not
folded into these tokens.

Component leaves are measured computed values. A colour that matches a
resolved custom property aliases that property.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from oklab import oklab_or_oklch  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())["components"]
RD = V["resolved"]["appDark"]


def resolved(name):
    row = RD.get(name) or {}
    return row.get("value", row.get("raw"))


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def lit(value, ty, src, desc):
    return {"value": value, "type": ty, "source": src, "description": desc}


SPEC = {
    "_about": (
        "Krea public tokens, 2026-11-18. core scales come from the Tailwind "
        "@theme layer resolved with html.dark. dark holds the painted "
        "semantic roles (the product's only public theme; there is no light "
        "set). component holds measured control values."
    ),
    "core": {},
    "dark": {},
    "component": {},
}

# --- colour ramp: --color-primary-* is the product's neutral ---
ramp = SPEC["core"].setdefault("color", {}).setdefault("primary", {})
for step in ("0", "50", "100", "150", "200", "250", "300", "400", "500", "600", "700", "800", "850", "900", "950", "975", "1000"):
    name = f"--color-primary-{step}"
    if resolved(name):
        ramp[step] = var(name, "color", description=f"Primary grey ramp step {step}, declared on :root,:host.")

action = SPEC["core"]["color"].setdefault("action", {})
for key, name in (("default", "--color-action"), ("hover", "--color-action-hover"), ("green", "--color-action-green"), ("purple", "--color-action-purple")):
    if resolved(name):
        action[key] = var(name, "color", description="Krea action colour, declared on :root,:host.")

# tailwind hue ramps that the theme layer actually declares, first 11 steps
hues = ["red", "orange", "amber", "yellow", "green", "blue", "violet", "zinc", "neutral"]
for hue in hues:
    group = {}
    for step in ("50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"):
        name = f"--color-{hue}-{step}"
        if resolved(name):
            group[step] = var(name, "color")
    if len(group) >= 8:
        SPEC["core"]["color"][hue] = group

# --- type ---
fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
fam["sans"] = var("--font-sans", "fontFamily", description="Suisse Intl, the UI face, with the system fallback stack.")
fam["mono"] = var("--font-mono", "fontFamily", description="Suisse Intl Mono.")
weights = SPEC["core"]["font"].setdefault("weight", {})
for key, name in (("light", "--font-weight-light"), ("normal", "--font-weight-normal"), ("book", "--font-weight-book"), ("medium", "--font-weight-medium"), ("semibold", "--font-weight-semibold"), ("bold", "--font-weight-bold")):
    if resolved(name) is not None:
        weights[key] = var(name, "fontWeight")

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key in ("xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl"):
    name = f"--text-{key}"
    if resolved(name):
        type_scale[key] = var(name, "dimension", description=f"Tailwind text-{key} size.")

# --- geometry ---
radius = SPEC["core"].setdefault("radius", {})
for key, name in (("xs", "--radius-xs"), ("sm", "--radius-sm"), ("md", "--radius-md"), ("lg", "--radius-lg"), ("xl", "--radius-xl"), ("2xl", "--radius-2xl"), ("3xl", "--radius-3xl"), ("4xl", "--radius-4xl")):
    if resolved(name):
        radius[key] = var(name, "dimension")
SPEC["core"].setdefault("spacing", {})["unit"] = var("--spacing", "dimension", description="The 4px spacing base.")

ease = SPEC["core"].setdefault("motion", {}).setdefault("easing", {})
for key, name in (("in", "--ease-in"), ("out", "--ease-out"), ("in-out", "--ease-in-out")):
    if resolved(name):
        ease[key] = var(name, "cubicBezier")

# --- semantic roles, the painted dark theme ---
# Map shadcn names that resolved. Prefer --color-* when the harvest stored them as colors.
roles = {
    "page": "--background",
    "surface": "--card",
    "popover": "--popover",
    "text": "--foreground",
    "text-muted": "--muted-foreground",
    "text-on-accent": "--primary-foreground",
    "muted": "--muted",
    "accent": "--color-action",
    "accent-hover": "--color-action-hover",
    "border": "--border",
    "input": "--input",
    "ring": "--ring",
    "destructive": "--destructive",
    "warning": "--warning",
    "success": "--success",
    "sidebar": "--sidebar",
    "sidebar-foreground": "--sidebar-foreground",
    "sidebar-accent": "--sidebar-accent",
    "sidebar-border": "--sidebar-border",
    "sidebar-primary": "--sidebar-primary",
}
sem = SPEC["dark"].setdefault("color", {})
for key, name in roles.items():
    if resolved(name):
        sem[key] = var(name, "color", description=f"Painted on html.dark ({name}).")

# also the primary-950 page fill, which body uses via dark:bg-primary-950
if resolved("--color-primary-950"):
    sem["page-950"] = var("--color-primary-950", "color", description="body dark:bg-primary-950, the app field.")
if resolved("--color-primary-0"):
    sem["on-dark"] = var("--color-primary-0", "color", description="White text and the Sign in fill.")


def st(comp, state):
    return C[comp]["states"][state]["style"]


def have(comp, state="default"):
    try:
        return "error" not in C[comp]["states"].get(state, {"error": 1}) and "style" in C[comp]["states"][state]
    except KeyError:
        return False


def norm_color(v):
    v = (v or "").strip()
    ok = oklab_or_oklch(v.lower())
    if ok:
        return ok
    m = re.fullmatch(r"#([0-9a-fA-F]{1,2}),\s*([0-9a-fA-F]{1,2}),\s*([0-9a-fA-F]{1,2})", v)
    if m:  # vars.mjs wrote some resolved colours as "#rr,gg,bb" (fixed in vars.mjs; the committed raw keeps them)
        return "#%02x%02x%02x" % tuple(int(x, 16) for x in m.groups())
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 0.999:
            return "#%02x%02x%02x" % tuple(int(float(x)) for x in (r, g, b))
        return "rgba(%d, %d, %d, %g)" % (int(float(r)), int(float(g)), int(float(b)), float(a))
    if v.startswith("#") and len(v) in (4, 5):
        return "#" + "".join(c * 2 for c in v[1:4])
    return v


def color_alias(value):
    n = norm_color(value).lower()
    for name, row in RD.items():
        if row.get("kind") != "color":
            continue
        if norm_color(str(row.get("value", ""))).lower() == n and name.startswith("--"):
            return name
    return None


def comp_color(comp, state, prop, token, desc):
    if not have(comp, state):
        return
    raw = st(comp, state).get(prop) or ""
    if not raw or raw in ("rgba(0, 0, 0, 0)", "transparent"):
        return
    src = f"computed {prop} of {comp}/{state} (raw/components-computed.json)"
    alias = color_alias(raw)
    node = SPEC["component"].setdefault(token, {})
    if alias:
        node[prop] = var(alias, "color", source=src, description=desc)
    else:
        node[prop] = lit(norm_color(raw), "color", src, desc)
    if raw.strip().startswith(("oklab(", "oklch(")):
        node[prop]["computed"] = raw.strip()  # the form Chromium reported, before the sRGB conversion


def comp_dim(comp, state, prop, token, desc):
    if not have(comp, state):
        return
    raw = st(comp, state).get(prop) or ""
    if not raw or raw in ("auto", "0px", "normal"):
        return
    if not re.fullmatch(r"-?\d+(\.\d+)?px", raw):
        return
    SPEC["component"].setdefault(token, {})[prop] = lit(raw, "dimension", f"computed {prop} of {comp}/{state}", desc)


# measured roles used by the style guide
comp_color("nav-signin", "default", "backgroundColor", "sign-in", "The white Sign in button fill.")
comp_color("nav-signin", "default", "color", "sign-in", "Sign in label, black on white.")
comp_color("nav-signin", "hover", "backgroundColor", "sign-in-hover", "Sign in hover fill.")
comp_color("price-cta", "default", "backgroundColor", "plan-cta", "Get Pro fill, white pill.")
comp_color("price-cta", "default", "color", "plan-cta", "Get Pro label.")
comp_color("login-email-btn", "default", "backgroundColor", "email-cta", "Continue with Email fill, the action blue.")
comp_color("login-google", "default", "backgroundColor", "oauth", "Continue with Google fill.")
comp_color("login-google", "default", "color", "oauth", "OAuth label.")
comp_color("nav-home", "default", "backgroundColor", "nav-active", "Selected sidebar item fill.")
comp_color("sidebar", "default", "backgroundColor", "sidebar", "Sidebar fill.")
comp_color("price-h1", "default", "color", "heading", "Pricing heading colour.")
comp_dim("nav-signin", "default", "height", "sign-in", "Sign in control height.")
comp_dim("nav-signin", "default", "borderTopLeftRadius", "sign-in", "Sign in corner radius.")
comp_dim("price-cta", "default", "height", "plan-cta", "Plan button height.")
comp_dim("price-cta", "default", "borderTopLeftRadius", "plan-cta", "Plan button radius.")
comp_dim("sidebar", "default", "width", "sidebar", "Sidebar width at 1440.")
comp_dim("composer", "default", "borderTopLeftRadius", "composer", "Home composer radius.")

# focus ring from a control that actually showed one. A drawn outline needs a style other than
# none or auto (auto is the UA ring, whose colour is not the recorded outlineColor) and a width;
# otherwise the ring is the outermost box-shadow layer with a spread (fal's painted_ring()).
# nav-signin draws its ring as a 2px shadow and leaves outline at none, so its outlineColor
# (#007aff, the UA default) is not what it paints.
def split_shadow(v):
    return [p.strip() for p in re.split(r",\s*(?![^()]*\))", v or "") if p.strip()]


def painted_ring(sty):
    """(colour, width, how) of the ring a focus-visible state paints, or None."""
    style = sty.get("outlineStyle", "none")
    width = float((sty.get("outlineWidth") or "0px")[:-2] or 0)
    if style not in ("none", "auto") and width > 0 and norm_color(sty.get("outlineColor")) != "rgba(0, 0, 0, 0)":
        return sty["outlineColor"], sty["outlineWidth"], f"outline {sty['outlineWidth']} {style}"
    ring = None
    for layer in split_shadow(sty.get("boxShadow")):
        m = re.match(r"^((?:rgba?|oklab|oklch)\([^)]*\))\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(\s+inset)?$", layer)
        if not m or m.group(6) or float(m.group(5)) <= 0 or norm_color(m.group(1)) == "rgba(0, 0, 0, 0)":
            continue
        ring = (m.group(1), m.group(5) + "px", f"box-shadow {m.group(5)}px spread; outline {style}")
    return ring


if have("nav-signin", "focus-visible"):
    found = painted_ring(st("nav-signin", "focus-visible"))
    if found:
        colour, width, how = found
        src = f"computed focus-visible ring of nav-signin ({how})"
        focus = SPEC["component"].setdefault("focus", {})
        focus["ring-width"] = lit(width, "dimension", src, "Keyboard focus ring width.")
        alias = color_alias(colour)
        focus["ring"] = var(alias, "color", source=src, description="Keyboard focus ring.") if alias else lit(norm_color(colour), "color", src, "Keyboard focus ring.")
        if colour.strip().startswith(("oklab(", "oklch(")):
            focus["ring"]["computed"] = colour.strip()

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1) + "\n")
print("wrote", RAW / "component-tokens.json", "components", len(C))
