#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

base44.com is a Remix/Vite site; its bundle declares on `:root`
(raw/css-vars.json, read by tools/capture/vars.mjs):

  shadcn channels   --background, --foreground, --primary, --secondary,
                    --muted, --accent, --card, --popover, --destructive,
                    --border, --input, --ring and their -foreground pairs plus
                    --chart-1..5 and --sidebar-*: "H S% L%" triplets consumed
                    as `hsl(var(--x))`. They are the only names a `.dark`
                    block redefines, so they carry the light/dark split:
                    emitted as the light.* and dark.* role sets.
  named palette     --blue-*, --green-*, --orange-*, --ink-100..900,
                    --neutral-*, --lime-cta-*, --paper, --offwhite, --sand,
                    --black, --white, --hairline, --disabled, --invalid
                    -> core.color.*
  semantic paints   --text-*, --surface-*, --border-*, --cta-*, --intent-*,
                    --icon-*, --marketing-*, --focus-ring, --site-focus-ring:
                    hex roles the site paints directly
                    -> core.color.* (constants, same in both themes)
  scales            --radius-*, --space-*, --shadow-*, --dur-*, --ease-*,
                    --fw-*, --font-*, --track-*, --maxw-*, --header-*,
                    --page-*, --frame-w -> core.radius/space/elevation/
                    motion/fontWeight/fontFamily/layout
  app scopes        --tw-*, --br-*, --b44-*, --pg-*, --rh-*, --cc-*,
                    --sendoff-*, --ds-*, --ricos-*, --sem-*: page or widget
                    internals, recorded in css-vars.json, not tokenised

A leaf is {"var": "--name"} (resolved by build_tokens.py) or {"value": ...,
"source": "..."} for a measured value.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V["resolved"]["light"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}

# token path -> declared variable. Palette colours; the semantic paints are
# constants in both themes, so they sit in core.color next to the palette.
PALETTE = {
    "ink.100": "--ink-100", "ink.200": "--ink-200", "ink.300": "--ink-300", "ink.400": "--ink-400",
    "ink.500": "--ink-500", "ink.600": "--ink-600", "ink.700": "--ink-700", "ink.800": "--ink-800",
    "ink.900": "--ink-900",
    "neutral.100": "--neutral-100", "neutral.200": "--neutral-200", "neutral.300": "--neutral-300",
    "neutral.400": "--neutral-400", "neutral.500": "--neutral-500",
    "blue.100": "--blue-100", "blue.200": "--blue-200", "blue.300": "--blue-300",
    "blue.500": "--blue-500", "blue.600": "--blue-600", "blue.700": "--blue-700",
    "blue.default": "--blue", "blue.accent": "--blue-accent",
    "green.100": "--green-100", "green.300": "--green-300", "green.500": "--green-500",
    "green.700": "--green-700",
    "orange.100": "--orange-100", "orange.200": "--orange-200", "orange.500": "--orange-500",
    "orange.600": "--orange-600", "orange.700": "--orange-700", "orange.default": "--orange",
    "lime.cta": "--lime-cta", "lime.ctaHover": "--lime-cta-hover", "lime.ctaLine": "--lime-cta-line",
    "brand.paper": "--paper", "brand.offwhite": "--offwhite", "brand.sand": "--sand",
    "brand.black": "--black", "brand.white": "--white", "brand.hairline": "--hairline",
    "brand.marketingCard": "--marketing-card", "brand.marketingCardStrong": "--marketing-card-strong",
    "cta.orange": "--cta-orange", "cta.orangeHover": "--cta-orange-hover", "cta.orangeText": "--cta-orange-text",
    "cta.black": "--cta-black", "cta.blackHover": "--cta-black-hover",
    "cta.blueHover": "--cta-blue-hover", "cta.whiteHover": "--cta-white-hover",
    "text.body": "--text-body", "text.faint": "--text-faint", "text.inverse": "--text-inverse",
    "text.link": "--text-link", "text.muted": "--text-muted", "text.onBlue": "--text-on-blue",
    "text.placeholder": "--text-placeholder", "text.secondary": "--text-secondary",
    "text.strong": "--text-strong",
    "surface.blue": "--surface-blue", "surface.canvas": "--surface-canvas", "surface.card": "--surface-card",
    "surface.cardWarm": "--surface-card-warm", "surface.grey": "--surface-grey",
    "surface.inverse": "--surface-inverse", "surface.main": "--surface-main",
    "surface.sunken": "--surface-sunken", "surface.warm": "--surface-warm",
    "border.warm": "--border-warm", "border.mid": "--border-mid", "border.soft": "--border-soft",
    "border.strong": "--border-strong",
    "icon.blue": "--icon-blue", "icon.green": "--icon-green", "icon.orange": "--icon-orange",
    "intent.accent": "--intent-accent", "intent.danger": "--intent-danger",
    "intent.primary": "--intent-primary", "intent.primaryHover": "--intent-primary-hover",
    "intent.success": "--intent-success",
    "misc.disabled": "--disabled", "misc.invalid": "--invalid",
    "misc.focusRing": "--focus-ring", "misc.siteFocusRing": "--site-focus-ring",
}

# The shadcn channel roles: the only names the `.dark` block redefines, so they
# carry the light/dark split. token path -> var.
ROLES = {
    "background": "--background", "foreground": "--foreground",
    "card": "--card", "cardForeground": "--card-foreground",
    "popover": "--popover", "popoverForeground": "--popover-foreground",
    "primary": "--primary", "primaryForeground": "--primary-foreground",
    "secondary": "--secondary", "secondaryForeground": "--secondary-foreground",
    "muted": "--muted", "mutedForeground": "--muted-foreground",
    "accent": "--accent", "accentForeground": "--accent-foreground",
    "destructive": "--destructive", "destructiveForeground": "--destructive-foreground",
    "border": "--border", "input": "--input", "ring": "--ring",
    "chart.1": "--chart-1", "chart.2": "--chart-2", "chart.3": "--chart-3",
    "chart.4": "--chart-4", "chart.5": "--chart-5",
    "sidebar.background": "--sidebar-background", "sidebar.foreground": "--sidebar-foreground",
    "sidebar.primary": "--sidebar-primary", "sidebar.primaryForeground": "--sidebar-primary-foreground",
    "sidebar.accent": "--sidebar-accent", "sidebar.accentForeground": "--sidebar-accent-foreground",
    "sidebar.border": "--sidebar-border", "sidebar.ring": "--sidebar-ring",
}

SCALES = {
    "radius": {
        "none": "--radius-none", "xs": "--radius-xs", "sm": "--radius-sm", "md": "--radius-md",
        "lg": "--radius-lg", "xl": "--radius-xl", "2xl": "--radius-2xl", "cta": "--radius-cta",
        "pill": "--radius-pill", "default": "--radius",
    },
    "space": {
        "1": "--space-1", "2": "--space-2", "3": "--space-3", "4": "--space-4", "5": "--space-5",
        "6": "--space-6", "7": "--space-7", "8": "--space-8", "9": "--space-9",
        "gutter": "--space-gutter", "blogBlock": "--space-blog-block",
    },
    "duration": {"fast": "--dur-fast", "base": "--dur-base", "hover": "--dur-hover", "menu": "--dur-menu"},
    "easing": {"standard": "--ease-standard", "inOut": "--ease-in-out", "snap": "--ease-snap"},
    "fontWeight": {"light": "--fw-light", "regular": "--fw-regular", "medium": "--fw-medium",
                   "semibold": "--fw-semibold", "bold": "--fw-bold"},
    "fontFamily": {
        "display": "--font-display", "displayVf": "--font-display-vf", "body": "--font-body",
        "ui": "--font-ui", "mono": "--font-mono", "base44": "--font-family-base44",
    },
    "layout": {
        "maxwContent": "--maxw-content", "maxwWide": "--maxw-wide", "maxwProse": "--maxw-prose",
        "maxwBlogArtifact": "--maxw-blog-artifact", "maxwBlogArtifactWide": "--maxw-blog-artifact-wide",
        "headerBarHeight": "--header-bar-h", "headerMargin": "--header-margin",
        "headerOffset": "--header-offset", "pageInsetX": "--page-inset-x",
        "pagePaddingX": "--page-padding-x", "frameWidth": "--frame-w",
    },
    "elevation": {
        "xs": "--shadow-xs", "sm": "--shadow-sm", "md": "--shadow-md",
        "lg": "--shadow-lg", "pop": "--shadow-pop", "menu": "--shadow-menu",
    },
}

SCALE_TYPES = {
    "radius": "dimension", "space": "dimension", "layout": "dimension",
    "duration": "duration", "easing": "cubicBezier", "fontWeight": "fontWeight",
    "fontFamily": "fontFamily", "elevation": "shadow",
}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = None
    return node, parts[-1]


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. base44.com is a "
    "Remix/Vite build: the shadcn channel vars carry the light/dark role split, "
    "the named palette and semantic paints are constants in core.color, and the "
    "radius/space/shadow/motion/type/layout scales sit under core. \"var\" "
    "leaves resolve through the live document; \"value\" leaves are measured."),
    "core": {}, "light": {}, "dark": {}, "component": {}}

for path, var in PALETTE.items():
    node, last = descend(SPEC["core"].setdefault("color", {}), path.split("."))
    node[last] = {"var": var, "type": "color"}

for scale, entries in SCALES.items():
    node_root = SPEC["core"].setdefault(scale, {})
    for name, var in entries.items():
        node, last = descend(node_root, name.split("."))
        node[last] = {"var": var, "type": SCALE_TYPES[scale]}

for path, var in ROLES.items():
    for theme in ("light", "dark"):
        node, last = descend(SPEC[theme], path.split("."))
        node[last] = {"var": var, "type": "color"}

# ------------------------------------------------------------- light roles
#
# A few roles the channels do not name are measured on the painted chrome and
# point at palette tokens where the value matches.
def st(comp, state):
    c = C[comp]
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(comp)
    return c["states"][state]["style"]


def stprop(comp, state, prop):
    """prop may be `styleProp`, `textStyle.prop`, `::after.prop` or the special
    `ringShadow`: resolve the dotted path inside the measured state.
    `ringShadow` returns the colour of the `0 0 0 Npx` ring layer in the
    element's own boxShadow — the hairline many controls paint instead of a
    real border."""
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
    m = re.fullmatch(r"oklab\(\s*([\d.]+)\s+(-?[\d.]+)\s+(-?[\d.]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        L, A, B = (float(m.group(i)) for i in (1, 2, 3))
        l_ = (L + 0.3963377774 * A + 0.2158037573 * B) ** 3
        m_ = (L - 0.1055613458 * A - 0.0638541729 * B) ** 3
        s_ = (L - 0.0894841775 * A - 1.2914855480 * B) ** 3
        R_ = +4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_
        G_ = -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_
        B_ = -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_
        gam = lambda x: max(0, min(255, round((12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055) * 255)))
        a = m.group(4)
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a) if a else 1
        if a >= 1:
            return "#%02x%02x%02x" % (gam(R_), gam(G_), gam(B_))
        return f"rgba({gam(R_)}, {gam(G_)}, {gam(B_)}, {'%g' % a})"
    return v


BY_VALUE = {}
def collect(node, prefix=""):
    for k, v in node.items():
        if isinstance(v, dict) and "var" in v:
            val = norm_color(R.get(v["var"], ""))
            if val:
                BY_VALUE.setdefault(val, prefix + k)
        elif isinstance(v, dict):
            collect(v, prefix + k + ".")
collect(SPEC["core"].setdefault("color", {}), "color.")


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


for path, comp, state, prop, desc in [
    ("brand", "nav-cta", "default", "backgroundColor", "The dark CTA fill on Start building."),
    # its own key: "accent" is the --accent role (#f3f0ed light, #27272a dark), which this
    # measured orange would otherwise replace in light only
    ("accent-cta", "prompt-submit", "default", "backgroundColor", "The orange send/button accent (measured; not the --accent role)."),
    ("focus", "nav-cta", "focus-visible", "outlineColor", "The keyboard-focus ring where one is drawn."),
    ("measured.linkHover", "signin-signup", "hover", "color", "The Sign up link on hover."),
]:
    try:
        role("light", path, comp, state, prop, desc)
    except KeyError:
        pass

# -------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})
for comp, state, key, prop, desc in [
    ("nav-cta", "hover", "cta-hover", "backgroundColor", "Start building on hover."),
    ("prompt-submit", "hover", "send-hover", "backgroundColor", "The orange send on hover."),
    ("prompt-submit", "pressed", "send-pressed", "backgroundColor", "The send while pressed (CDP-forced)."),
    ("billing-toggle", "default", "toggle-shell", "backgroundColor", "The billing toggle's translucent track (the selected segment's orange fill rides on a sliding indicator, not the button)."),
    ("signin-submit", "default", "submit-disabled-bg", "backgroundColor", "The email submit disabled for an empty field."),
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
    ("display", "hero-title", "default", "The h1 display face (Dazzed)."),
    ("title", "section-title", "default", "An h2 section title (Dazzed)."),
    ("body", "hero-sub", "default", "The paragraph under the hero (Geist)."),
    ("label", "nav-link", "default", "Nav-item label type (Geist medium)."),
    ("button", "nav-cta", "default", "CTA label type."),
    ("price", "price", "default", "A plan's price figure."),
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
    ("control.heightCta", "nav-cta", "default", "height", "The Start building pill height."),
    ("control.heightNav", "nav-link", "default", "height", "Nav link height."),
    ("control.heightField", "signin-field-wrap", "default", "height", "The email field shell height."),
    ("control.heightOauth", "signin-google", "default", "height", "The OAuth button height."),
    ("control.heightSubmit", "signin-submit", "default", "height", "The email submit height."),
    ("control.heightToggle", "billing-toggle", "default", "height", "The billing toggle height."),
    ("control.heightTile", "build-tile", "default", "height", "A build-type tile height."),
    ("control.radiusCta", "nav-cta", "default", "borderTopLeftRadius", "The CTA's corner."),
    ("control.radiusField", "signin-field-wrap", "default", "borderTopLeftRadius", "The email shell's corner."),
    ("control.radiusCard", "plan-card", "default", "borderTopLeftRadius", "The plan card's corner."),
    ("control.radiusBadge", "popular-badge", "default", "borderTopLeftRadius", "The Popular chip's corner."),
    ("control.radiusToggle", "billing-toggle", "default", "borderTopLeftRadius", "The toggle's corner."),
    ("header.height", "header", "default", "height", "The fixed header block at 1440px."),
    ("footer.height", "footer", "default", "height", "The footer block at 1440px."),
    ("prompt.height", "prompt-box", "default", "height", "The hero composer height."),
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
