#!/usr/bin/env python3
"""Write raw/component-tokens.json, the spec build_tokens.py reads.

Leonardo.Ai paints three signed-out surfaces on 2026-11-18:

  marketing   leonardo.ai. Black canvas, violet #6e60ee wordmark, white
              Start now. Tailwind v4 names on :root. One dark paint.
  app         app.leonardo.ai signed-out shell. #0a0a0a canvas, violet
              brand, white foreground, prompt composer.
  docs        docs.leonardo.ai ReadMe. data-color-mode switches light and
              dark. The public page paints dark. Light is the declared
              alternate, resolved in the probe, not a marketing capture.

Product colour roles (--background, --accent-brand, the purple ramp) do not
switch with the docs color mode. Docs roles that do switch (--color-bg-page,
--color-text-default, ReadMe syntax) are emitted in both themes. Measured
geometry hangs off component.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = {}
comp_path = RAW / "components-computed.json"
if comp_path.exists():
    C = json.loads(comp_path.read_text()).get("components", {})

PLAIN = V["resolved"]["plain"]
LIGHT = V["resolved"]["colorModeLight"]
DARK = V["resolved"]["colorModeDark"]


def val(bucket, name):
    item = bucket.get(name) or {}
    return item.get("value", item.get("raw"))


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def measured(value, source, ty="color"):
    return {"value": value, "type": ty, "source": source}


def put(tree, parts, leaf):
    node = tree
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


def slug_parts(name):
    return [p for p in name.lstrip("-").split("-") if p]


SPEC = {
    "_about": (
        "Leonardo.Ai public token spec, 2026-11-18. Declared names from "
        "raw/css-vars.json. Dark is the live paint of marketing, the signed-out "
        "app and the docs dark color mode. Light is the docs data-color-mode=light "
        "resolution. Product brand names are theme-invariant."
    ),
    "core": {},
    "light": {},
    "dark": {},
    "component": {},
}

# Brand and product ramps. Theme-invariant. Docs ReadMe ramps stay out.
CORE_COLOR = [
    "--color-purple", "--color-black", "--color-white", "--color-leo-white",
    "--color-pink", "--color-hotpink", "--color-green", "--color-yellow",
    "--color-orange", "--color-blue", "--color-watermelon", "--color-gray-100",
    "--color-gray-200", "--color-gray-300", "--color-gray2", "--color-light-gray",
    "--color-neutral-900", "--color-panel", "--color-hover", "--color-red-400",
    "--color-pink2", "--color-secondary",
    "--purple-50", "--purple-100", "--purple-200", "--purple-300", "--purple-400",
    "--purple-500", "--purple-600", "--purple-700", "--purple-800", "--purple-900",
    "--purple-950", "--purple-pastel",
    "--accent-brand", "--accent-brand-light", "--accent-brand-strong",
    "--primary-brand", "--primary-brand-light", "--primary-brand-strong",
    "--primary-brand-foreground",
    "--color-primary-brand", "--color-primary-brand-light",
    "--accent", "--accent-light", "--accent-strong",  # neon green, not the violet brand
    "--accent-secondary", "--accent-secondary-light", "--accent-secondary-strong",
    "--accent-tertiary", "--accent-tertiary-light", "--accent-tertiary-strong",
    "--positive", "--positive-light", "--positive-strong",
    "--negative", "--negative-light", "--negative-strong",
    "--warning", "--warning-light", "--warning-strong",
    "--destructive",
]
CORE_DIM = [
    "--radius", "--radius-sm", "--radius-xl", "--radius-4xl", "--radius-full",
    "--border-radius", "--border-radius-sm", "--border-radius-md",
    "--border-radius-lg", "--border-radius-xl", "--border-radius-full",
    "--border-width", "--spacing",
]
CORE_FONT = [
    "--font-sans", "--font-mono", "--font-inter",
    "--font-family-mono", "--default-font-family", "--default-mono-font-family",
]
CORE_SIZE = [
    "--font-size-xs", "--font-size-sm", "--font-size-md", "--font-size-lg",
    "--font-size-xl", "--font-size-2xl", "--font-size-3xl", "--font-size-4xl",
    "--font-base",
]
CORE_WEIGHT = [
    "--font-weight", "--font-weight-normal", "--font-weight-medium",
    "--font-weight-semibold", "--font-weight-bold", "--font-weight-extrabold",
    "--font-weight-black",
]
CORE_EASE = ["--ease-in", "--ease-out", "--ease-in-out"]
CORE_DURATION = ["--default-transition-duration"]
CORE_LAYOUT = [
    "--breakpoint-sm", "--breakpoint-md", "--breakpoint-lg", "--breakpoint-xl",
    "--container", "--container-sm", "--container-lg",
    "--container-xs", "--container-md", "--container-xl",
    "--container-2xl", "--container-3xl", "--container-4xl",
    "--container-5xl", "--container-6xl", "--container-7xl",
]
CORE_Z = [
    "--z-alert-dialog", "--z-dialog", "--z-popover", "--z-loading-overlay",
    "--z-banner", "--z-toolbar", "--z-modal", "--z-dropdown",
    "--z-toaster", "--z-tooltip",
]

for name in CORE_COLOR:
    if name not in PLAIN or PLAIN[name].get("kind") not in ("color", "other"):
        continue
    raw = str(val(PLAIN, name) or "")
    if raw.startswith("oklch") or raw.startswith("color("):
        continue
    parts = slug_parts(name)
    if parts and parts[0] == "color":
        parts = parts[1:]
    # --accent is the neon green. The violet brand keeps the accent path.
    if parts and parts[0] == "accent" and "brand" not in parts:
        parts = ["neon", *parts[1:]]
    put(SPEC["core"], ["color", *parts], var(name))

for name in CORE_DIM:
    if name not in PLAIN or PLAIN[name].get("kind") not in ("dimension", "other"):
        continue
    parts = slug_parts(name)
    if name == "--spacing":
        put(SPEC["core"], ["spacing", "unit"], var(name, "dimension"))
    elif name == "--border-width":
        put(SPEC["core"], ["border", "width"], var(name, "dimension"))
    else:
        put(SPEC["core"], ["radius", *parts], var(name, "dimension"))

for name in CORE_FONT:
    if name not in PLAIN:
        continue
    put(SPEC["core"], ["font", "family", name.lstrip("-").replace("font-", "").replace("default-", "")], var(name, "fontFamily"))

for name in CORE_SIZE:
    if name not in PLAIN:
        continue
    put(SPEC["core"], ["font", "size", name.replace("--font-size-", "").replace("--font-", "")], var(name, "dimension"))

for name in CORE_WEIGHT:
    if name not in PLAIN:
        continue
    put(SPEC["core"], ["font", "weight", name.replace("--font-weight-", "").replace("--font-weight", "base")], var(name, "fontWeight"))

for name in CORE_EASE:
    if name not in PLAIN:
        continue
    put(SPEC["core"], ["motion", "easing", name.replace("--ease-", "")], var(name, "cubicBezier"))

for name in CORE_DURATION:
    if name not in PLAIN:
        continue
    put(SPEC["core"], ["motion", "duration", "default"], var(name, "duration"))

for name in CORE_LAYOUT:
    if name not in PLAIN or PLAIN[name].get("kind") != "dimension":
        continue
    kind = "breakpoint" if "breakpoint" in name else "container"
    put(SPEC["core"], ["layout", kind, name.split("-")[-1]], var(name, "dimension"))

for name in CORE_Z:
    if name not in PLAIN:
        continue
    put(SPEC["core"], ["layout", "z", name.replace("--z-", "")], var(name, "number"))

# Product semantic roles. Same value in both themes: marketing and the app
# paint one dark canvas, and these names do not switch with docs color mode.
PRODUCT = {
    "page": "--background",
    "foreground": "--foreground",
    "surface": "--color-panel",
    "raised": "--primary",
    "overlay": "--popover",
    "scrim": "--input",
    "text-primary": "--foreground",
    "text-secondary": "--secondary-foreground",
    "text-muted": "--muted-foreground",
    "text-disabled": "--disabled-foreground",
    "text-on-accent": "--primary-brand-foreground",
    "text-link": "--color-primary-brand-light",
    "border": "--border-secondary",
    "border-strong": "--border-primary",
    "border-focus": "--ring",
    "accent": "--accent-brand",
    "accent-hover": "--primary-brand-light",
    "accent-pressed": "--primary-brand-strong",
    "card": "--card",
    "card-foreground": "--card-foreground",
    "sidebar": "--sidebar-accent",
    "sidebar-foreground": "--sidebar-foreground",
    "sidebar-border": "--sidebar-border",
    "positive-foreground": "--positive-foreground",
    "negative-foreground": "--negative-foreground",
    "warning-foreground": "--warning-foreground",
    "info": "--border-notification",
    "status-positive": "--positive",
    "status-negative": "--negative",
    "status-warning": "--warning",
    "status-danger": "--destructive",
}
for slug, name in PRODUCT.items():
    if name not in PLAIN:
        continue
    put(SPEC["light"], ["color", *slug.split("-")], var(name))
    put(SPEC["dark"], ["color", *slug.split("-")], var(name))

# Docs roles that actually switch. These are the light theme's only honest source.
DOCS = {
    "docs-page": "--color-bg-page",
    "docs-page-muted": "--color-bg-page-muted",
    "docs-overlay": "--color-bg-overlay",
    "docs-text-primary": "--color-text-default",
    "docs-text-muted": "--color-text-muted",
    "docs-text-minimum": "--color-text-minimum",
    "docs-text-inverse": "--color-text-inverse",
    "docs-border": "--color-border-default",
    "docs-border-strong": "--color-border-heavy",
    "docs-focus": "--color-focus-ring",
    "docs-input": "--color-input-background",
    "docs-input-text": "--color-input-text",
    "docs-accent": "--blue",
    "docs-success": "--color-bg-success-emphasis",
    "docs-success-text": "--color-text-success",
    "docs-warning": "--color-bg-attention-emphasis",
    "docs-warning-text": "--color-text-attention",
    "docs-danger": "--color-bg-danger-emphasis",
    "docs-danger-text": "--color-text-danger",
    "docs-info": "--color-text-accent",
}
for slug, name in DOCS.items():
    if name not in LIGHT and name not in DARK:
        continue
    lv, dv = val(LIGHT, name), val(DARK, name)
    if lv == dv:
        continue
    put(SPEC["light"], ["color", *slug.split("-")], var(name))
    put(SPEC["dark"], ["color", *slug.split("-")], var(name))


def style(comp, state="default"):
    return (C.get(comp) or {}).get("states", {}).get(state, {}).get("style") or {}


def rect(comp, state="default"):
    return (C.get(comp) or {}).get("states", {}).get(state, {}).get("rect") or {}


def family(comp):
    raw = style(comp).get("fontFamily") or ""
    return raw.split(",")[0].strip().strip('"')


if style("mkt-h1"):
    put(SPEC["core"], ["font", "size", "display"], measured(style("mkt-h1").get("fontSize"), "measured mkt-h1 font-size on leonardo.ai/", "dimension"))
    put(SPEC["core"], ["font", "weight", "display"], measured(style("mkt-h1").get("fontWeight"), "measured mkt-h1 font-weight", "fontWeight"))
    put(SPEC["core"], ["font", "family", "display"], measured(family("mkt-h1") + ", sans-serif", "measured mkt-h1 font-family ufficioDisplay", "fontFamily"))
if style("app-h1"):
    put(SPEC["core"], ["font", "size", "app-display"], measured(style("app-h1").get("fontSize"), "measured app-h1 font-size on app.leonardo.ai/", "dimension"))
    put(SPEC["core"], ["font", "weight", "app-display"], measured(style("app-h1").get("fontWeight"), "measured app-h1 font-weight", "fontWeight"))
    put(SPEC["core"], ["font", "family", "app-display"], measured(family("app-h1") + ", sans-serif", "measured app-h1 font-family leoRenaisans", "fontFamily"))
if style("api-h1"):
    put(SPEC["core"], ["font", "family", "marketing"], measured(family("api-h1") + ", sans-serif", "measured api-h1 font-family leoSans", "fontFamily"))
if style("app-generate"):
    put(SPEC["component"], ["generate", "height"], measured(rect("app-generate").get("h"), "measured app-generate height", "dimension"))
    put(SPEC["component"], ["generate", "radius"], measured(style("app-generate").get("borderTopLeftRadius"), "measured app-generate radius", "dimension"))
if style("app-prompt"):
    put(SPEC["component"], ["prompt", "font-size"], measured(style("app-prompt").get("fontSize"), "measured app-prompt font-size", "dimension"))
if style("li-canva"):
    put(SPEC["component"], ["oauth", "height"], measured(rect("li-canva").get("h"), "measured li-canva height", "dimension"))
    put(SPEC["component"], ["oauth", "radius"], measured(style("li-canva").get("borderTopLeftRadius"), "measured li-canva radius", "dimension"))
if style("mkt-footer"):
    put(SPEC["component"], ["footer", "color"], measured(style("mkt-footer").get("backgroundColor"), "measured marketing footer background", "color"))


def prune(node):
    if not isinstance(node, dict):
        return node
    out = {}
    for k, v in node.items():
        if isinstance(v, dict) and "type" not in v and "value" not in v and "var" not in v:
            child = prune(v)
            if child:
                out[k] = child
        elif v is not None and (not isinstance(v, dict) or v.get("value") is not None or "var" in v):
            out[k] = v
    return out


for key in ("core", "light", "dark", "component"):
    SPEC[key] = prune(SPEC[key])

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1) + "\n")
print("wrote", RAW / "component-tokens.json")
