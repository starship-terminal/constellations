#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

endless.app (what endless.io redirects to) is one Next.js + Tailwind v4 surface
that declares a shadcn-style token layer: the semantic roles
(--background/--foreground/--primary/--secondary/--muted/--accent/--ring/
--border/--input/--card/--popover/--sidebar-*/--surface-*), the product
palettes (--mode-*/--label-*/--chart-*/--series-*), Tailwind's theme vars
(--text-*/--leading-*/--tracking-*/--radius-*/--container-*/--spacing/
--ease-*/--blur-*) and the site's own easings and durations, all resolved in
raw/css-vars.json once plain (:root, light) and once under the html `dark`
class (next-themes — the same re-binding a dark-system visitor gets).

Semantic vars that re-bind per theme become {"var": ...} leaves emitted into
both the light and dark sets; theme-stable declarations (the --label-*
palette, Tailwind hue steps, scales) live in core. Painted/measured values the
stylesheets never declare (font stacks, the card shadow, the pill radius, the
focus ring, component geometry) are {"value": ..., "source": ...} leaves from
raw/components-computed.json.

A leaf is {"var": "--name"} (resolved on the surface the set names), or
{"value": ..., "source": ...} for a measured value.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V.get("resolved", {})
R = {n: v.get("value", v.get("raw")) for n, v in RES.get("light", {}).items()}
D = {n: v.get("value", v.get("raw")) for n, v in RES.get("dark", {}).items()}
C = json.loads((RAW / "components-computed.json").read_text())["components"]

# A named row whose reading is missing is recorded here instead of being
# dropped silently; the build stops on any gap not listed in KNOWN_GAPS (at the
# end), and listed ones are written to raw/component-tokens.json `_gaps`.
GAPS = []


def gap(what):
    GAPS.append(what)


def declared(vname):
    """Gate for one named declared variable: a miss is recorded as a gap."""
    if vname not in R:
        gap(f"{vname} not declared")
    return vname in R


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. endless.app "
    "declares a shadcn-style token layer in its Tailwind v4 theme — semantic "
    "roles that re-bind under .dark, the --mode-*/--label-*/--chart-*/"
    "--series-* product palettes, and Tailwind's own type/radius/container/"
    "ease scales. Declared variables become var leaves resolved per theme; "
    "font stacks, the card shadow, the focus ring and component geometry are "
    "measured leaves from raw/components-computed.json."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        child = node.setdefault(p, {})
        if "var" in child or "value" in child or "$value" in child:
            node[p] = {"default": child}
            child = node[p]
        node = child
    last = parts[-1]
    cur = node.get(last)
    if isinstance(cur, dict) and cur and not ("var" in cur or "value" in cur or "$value" in cur):
        node = cur
        node.setdefault("default", None)
        last = "default"
    return node, last


def emit(root, name, leaf):
    node, last = descend(root, name[2:].split("-"))
    if node.get(last) is not None:
        raise SystemExit(f"duplicate token path for {name}: {last} is already set")
    node[last] = leaf


def st(comp, state):
    return C[comp]["states"][state]["style"]


def ts(comp, state, prop):
    """The first text node's reading (textStyle) when the kit recorded one —
    the wrapper's own fontSize can be the container's, not the text's."""
    try:
        c = C[comp]["states"][state]
        t = c.get("textStyle") or {}
        v = t.get(prop)
        return v if v else c["style"].get(prop)
    except KeyError:
        return None


# ------------------------------------------------- lab / oklab -> sRGB hex
# Chromium computes Tailwind v4 colours (oklch declarations, color-mix opacity
# modifiers) as lab()/oklab() strings in raw/components-computed.json; the
# resolved css-vars already carry hex, so this only serves measured leaves.
def _gam(x):
    return 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055


def _oklab(L, a, b):
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.291485548 * b) ** 3
    return [_gam(4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s),
            _gam(-1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s),
            _gam(-0.0041960863 * l - 0.7034186147 * m + 1.707614701 * s)]


def _lab(L, a, b):
    fy = (L + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    e, k = 216 / 24389, 24389 / 27
    finv = lambda t: t ** 3 if t ** 3 > e else (116 * t - 16) / k
    X = finv(fx) * 0.3457 / 0.3585
    Y = fy ** 3 if L > k * e else L / k
    Z = finv(fz) * (1 - 0.3457 - 0.3585) / 0.3585
    # D50 -> D65 (Bradford), then XYZ -> linear sRGB
    x = 0.955473421488075 * X - 0.02309845494876471 * Y + 0.06325924320057072 * Z
    y = -0.0283697093338637 * X + 1.0099953980813041 * Y + 0.021041441191917323 * Z
    z = 0.012314014864481998 * X - 0.020507649298898964 * Y + 1.330365926242124 * Z
    return [_gam(3.2409699419 * x - 1.5373831776 * y - 0.4986107603 * z),
            _gam(-0.9692436363 * x + 1.8759675015 * y + 0.0415550574 * z),
            _gam(0.0556300797 * x - 0.2039769589 * y + 1.0569715142 * z)]


def _tohex(rgb):
    return "#" + "".join("%02x" % round(min(1, max(0, v)) * 255) for v in rgb)


def norm_color(v):
    v = (v or "").strip()
    # A percentage alpha ("/ 50%", "rgba(..., 50%)") becomes the 0-1 number the
    # patterns below read; without this the colour passed through unconverted.
    v = re.sub(r"(/\s*|^rgba\([^,]+,[^,]+,[^,]+,\s*)([\d.]+)%\)$", lambda m: f"{m.group(1)}{float(m.group(2)) / 100:g})", v)
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    m = re.fullmatch(r"(ok)?lab\(([-\d.e]+%?)\s+([-\d.e]+)\s+([-\d.e]+)(?:\s*/\s*([\d.]+))?\)", v)
    if m:
        ok, L, A, B, al = m.groups()
        # lab() carries L in the 0-100 range (the % is notation); oklab() uses 0-1.
        Lf = (float(L[:-1]) * (0.01 if ok else 1)) if L.endswith("%") else float(L)
        rgb = _oklab(Lf, float(A), float(B)) if ok else _lab(Lf, float(A), float(B))
        h = _tohex(rgb)
        if al is None or float(al) >= 1:
            return h
        r, g, b = (int(h[i:i + 2], 16) for i in (1, 3, 5))
        return f"rgba({r}, {g}, {b}, {'%g' % float(al)})"
    m = re.fullmatch(r"oklch\(([-\d.e]+)\s+([-\d.e]+)\s+([-\d.e]+|none)(?:\s*/\s*([\d.]+|none))?\)", v)
    if m:
        import math
        L, Cc, H, al = m.groups()
        H = 0.0 if H == "none" else float(H)
        A, B = float(Cc) * math.cos(math.radians(H)), float(Cc) * math.sin(math.radians(H))
        h = _tohex(_oklab(float(L), A, B))
        if al in (None, "none") or float(al) >= 1:
            return h
        r, g, b = (int(h[i:i + 2], 16) for i in (1, 3, 5))
        return f"rgba({r}, {g}, {b}, {'%g' % float(al)})"
    return v


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False


def painted(comp, state):
    """First painted fill on or under the component."""
    try:
        c = C[comp]["states"][state]
    except KeyError:
        return None
    for n in c.get("paint") or []:
        if n.get("bg"):
            return n["bg"]
    for n in c.get("ancestors") or []:
        if n.get("bg"):
            return n["bg"]
    return None


COL = r"(?:rgba?\([^)]*\)|(?:ok)?lab\([^)]*\)|oklch\([^)]*\)|#[0-9a-fA-F]{3,8})"


def shadow_layers(spec):
    """Parse '<color> x y blur sp, ...' into DTCG shadow layers, dropping fully transparent no-ops."""
    out = []
    # One layer per top-level comma, so an `inset` keyword stays with its own
    # layer (Chromium writes it last) instead of being dropped.
    for part in re.split(r",(?![^(]*\))", spec or ""):
        m = re.search(
            r"(" + COL + r")\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(?:\s+(-?[\d.]+)px)?", part)
        if not m:
            continue
        col, x, y, bl, sp = m.groups()
        if col.startswith("rgba") and col.rstrip(")").endswith(", 0"):
            continue  # rgba(0,0,0,0) 0px 0px 0px 0px placeholders Tailwind emits
        layer = {"color": norm_color(col), "offsetX": f"{x}px", "offsetY": f"{y}px",
                 "blur": f"{bl}px", "spread": f"{sp or 0}px"}
        if re.search(r"\binset\b", part):
            layer["inset"] = True
        out.append(layer)
    return out


def gradient_stops(spec):
    """Parse 'linear-gradient(to <dir>, <color> <pct>, ...)' into DTCG gradient stops."""
    out = []
    for m in re.finditer(r"(" + COL + r")\s+([\d.]+)%", spec or ""):
        out.append({"color": norm_color(m.group(1)), "position": float(m.group(2)) / 100})
    return out


def measure(key, comp, state, prop, ty, desc, bag, val=None, paint=False):
    """A measured leaf from components-computed.json into bag[key]."""
    try:
        v = val
        if v is None:
            v = norm_color(painted(comp, state)) if paint else st(comp, state)[prop]
        if v is None or v == "" or v == "rgba(0, 0, 0, 0)":
            return gap(f"{key}: {comp} {state} {prop} is empty")
        if ty == "color":
            v = norm_color(v)
        bag[key] = {"value": v, "type": ty,
                    "source": f"computed {prop if not paint else 'paint'} of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
    except (KeyError, TypeError):
        gap(f"{key}: no {comp} {state} {prop} reading")


# ------------------------------------------------------------------- fonts
# No --font-* vars are declared; the stacks arrive as next/font classes and are
# read off computed styles.
fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("sans", "header", "default", "TikTok Sans: the product face everywhere — headings, body, nav and buttons."),
    ("mono", "mcp-code", "default", "Geist Mono: code snippets, the MCP install command and numeric/readout text."),
]:
    try:
        fam[key] = {"value": st(comp, state)["fontFamily"], "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
    except KeyError:
        gap(f"font.family.{key}: no {comp} {state} reading")

weight = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for name, desc in [
    ("normal", "400 body weight."),
    ("medium", "500 heading, button and label weight."),
    ("semibold", "600 — CTA buttons and docs headings."),
]:
    vname = f"--font-weight-{name}"
    if declared(vname):
        weight[name] = var(vname, "fontWeight", description=desc)

size = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for name in ["xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl"]:
    vname = f"--text-{name}"
    if declared(vname):
        size[name] = var(vname, "dimension",
                         description=f"Declared --text-{name} step of the Tailwind ramp ({R[vname]}).")
for key, comp, state, desc in [
    ("display", "hero-title", "default", "The home hero display size (59.2px — a fluid clamp, not a declared step)."),
    ("display-mobile", "m-hero", "default", "The hero display size at 390px (37.6px)."),
    ("docs-h1", "docs-h1", "default", "The docs page heading (28px)."),
    ("lede", "hero-lede", "default", "The hero lede (18px)."),
]:
    v = ts(comp, state, "fontSize")
    if v:
        size[key] = {"value": v, "type": "dimension",
                     "source": f"computed fontSize of {comp} {state} (raw/components-computed.json)",
                     "description": desc}
    else:
        gap(f"font.size.{key}: no {comp} {state} fontSize reading")

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for name in ["xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl"]:
    vname = f"--text-{name}--line-height"
    if declared(vname):
        leading[name] = var(vname, "number",
                            description=f"Declared line-height ratio for --text-{name} ({R[vname]}).")
for name in ["tight", "snug", "normal", "relaxed"]:
    vname = f"--leading-{name}"
    if declared(vname):
        leading[name] = var(vname, "number",
                            description=f"Declared --leading-{name} ({R[vname]}).")
for key, comp, state, desc in [
    ("display", "hero-title", "default", "The display leading as a length (63.9px on 59.2px)."),
    ("lede", "hero-lede", "default", "The lede leading (29.25px on 18px)."),
]:
    v = ts(comp, state, "lineHeight")
    if v:
        leading[key] = {"value": v, "type": "dimension",
                        "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}
    else:
        gap(f"font.lineHeight.{key}: no {comp} {state} lineHeight reading")

tracking = SPEC["core"].setdefault("font", {}).setdefault("tracking", {})
for name in ["tighter", "tight", "normal", "wide", "wider"]:
    vname = f"--tracking-{name}"
    if not declared(vname):
        continue
    v = R[vname].strip()
    if v.endswith("em"):
        # em trackings scale with the font size; stored as the 16px-base px
        # equivalent with the declared em value in the description.
        tracking[name] = {"value": f"{'%g' % (float(v[:-2]) * 16)}px", "type": "dimension",
                          "source": f"css-var {vname} (light)",
                          "description": f"Declared --tracking-{name} = {v} (em tracking scales with font size; "
                                         f"the value here is the 16px-base equivalent)."}
    else:
        tracking[name] = var(vname, "dimension", description=f"Declared --tracking-{name} ({v}).")
for key, comp, state, desc in [
    ("display", "hero-title", "default", "The display tracking (-1.89px on the 59.2px hero)."),
    ("h1", "pricing-h1", "default", "The h1 tracking (-2.4px on 48px titles)."),
    ("h2", "h2-section", "default", "The h2 tracking (-0.9px on 36px)."),
]:
    v = ts(comp, state, "letterSpacing")
    if v:
        tracking[key] = {"value": v, "type": "dimension",
                         "source": f"computed letterSpacing of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    else:
        gap(f"font.tracking.{key}: no {comp} {state} letterSpacing reading")

# --------------------------------------------------- theme-stable palettes
# These read identically under .dark, so they are scale values, not roles.
brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, vname, desc in [
    ("accent", "--accent", "Endless sky #01bcff: the brand accent, focus ring and chart/label seed."),
    ("landing-action", "--color-landing-action", "Landing action blue #11a8ff."),
    ("ring", "--ring", "The focus/interactive ring (same value as accent)."),
]:
    if declared(vname):
        brand[key] = var(vname, "color", description=desc)

hue = SPEC["core"].setdefault("color", {}).setdefault("tailwind", {})
for key, vname, desc in [
    ("blue-600", "--color-blue-600", "Tailwind blue 600."),
    ("sky-600", "--color-sky-600", "Tailwind sky 600."),
    ("green-600", "--color-green-600", "Tailwind green 600."),
    ("orange-600", "--color-orange-600", "Tailwind orange 600."),
    ("pink-600", "--color-pink-600", "Tailwind pink 600."),
    ("purple-600", "--color-purple-600", "Tailwind purple 600."),
    ("neutral-800", "--color-neutral-800", "Tailwind neutral 800."),
    ("black", "--color-black", "Pure black."),
    ("white", "--color-white", "Pure white."),
]:
    if declared(vname):
        hue[key] = var(vname, "color", description=desc)

label = SPEC["core"].setdefault("color", {}).setdefault("label", {})
for key in ["blue", "gray", "green", "orange", "pink", "purple", "red", "yellow"]:
    vname = f"--label-{key}"
    if declared(vname):
        label[key] = var(vname, "color",
                         description=f"Declared --label-{key} ({R[vname]}): a tag/label hue, identical on both themes.")

# ---------------------------------------------------------- radius, easing

radius = SPEC["core"].setdefault("radius", {})
for key, vname, desc in [
    ("md", "--radius-md", "Declared --radius-md (8px): nav links, small buttons, fields."),
    ("lg", "--radius-lg", "Declared --radius-lg = --radius (12px): chips, cards, CTAs."),
    ("xl", "--radius-xl", "Declared --radius-xl (16px): plan/blog cards."),
    ("2xl", "--radius-2xl", "Declared --radius-2xl (20px): the composer, model cards, brand tiles."),
]:
    if declared(vname):
        radius[key] = var(vname, "dimension", description=desc)
if declared("--radius-icon"):
    # The declared value is a percentage ("22.5%"), not a length: type "other"
    # keeps it out of the length-only export — a bare number under core.radius
    # would be read as pixels (0.225px) and a "dimension" would fail the
    # px/rem check.
    radius["icon"] = var("--radius-icon", "other",
                         description="The app-icon corner radius (22.5%, the Apple icon mask).")
# The pill: mode tabs, filter chips and the billing toggle compute a
# 3.35544e+07px radius (rounded-full); stored as the practical 9999px.
measure("pill", "mode-tab", "default", "borderTopLeftRadius", "dimension",
        "The fully-round pill on filter chips and the billing toggle (the browser computes "
        "rounded-full as 3.35544e+07px; stored here as the practical 9999px).", radius)
if "pill" in radius:
    radius["pill"]["value"] = "9999px"

easing = SPEC["core"].setdefault("easing", {})
for key, vname, desc in [
    ("out", "--ease-out", "ease-out (0,0,.2,1)."),
    ("out-expo", "--ease-out-expo", "ease-out-expo (.16,1,.3,1)."),
    ("pop", "--ease-pop", "ease-pop (.32,.72,0,1)."),
    ("snappy", "--ease-snappy", "ease-snappy (.2,0,0,1)."),
    ("standard", "--ease-standard", "ease-standard (.22,1,.36,1)."),
    ("default", "--default-transition-timing-function", "The default transition curve (.4,0,.2,1)."),
]:
    if declared(vname):
        easing[key] = var(vname, "cubicBezier", description=desc)

duration = SPEC["core"].setdefault("duration", {})
for key, vname, desc in [
    ("default", "--default-transition-duration", "The default transition duration (150ms)."),
    ("hover", "--transition-duration-hover", "Hover transitions (150ms)."),
    ("enter", "--transition-duration-enter", "Element entrances (200ms)."),
    ("slow", "--transition-duration-slow", "Slow transitions (300ms)."),
]:
    if declared(vname):
        duration[key] = var(vname, "duration", description=desc)

# ------------------------------------------------------------- space, layout

spacing = SPEC["core"].setdefault("spacing", {})
if declared("--spacing"):
    spacing["base"] = var("--spacing", "dimension",
                          description="The Tailwind spacing unit (4px); all gutters are multiples of it.")

layout = SPEC["core"].setdefault("layout", {})
cont = layout.setdefault("container", {})
for name in ["xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl"]:
    vname = f"--container-{name}"
    if declared(vname):
        cont[name] = var(vname, "dimension",
                         description=f"Declared --container-{name} max-width ({R[vname]}).")
persp = layout.setdefault("perspective", {})
for name in ["normal", "distant"]:
    vname = f"--perspective-{name}"
    if declared(vname):
        persp[name] = var(vname, "dimension", description=f"Declared --perspective-{name} ({R[vname]}).")

# ----------------------------------------------------------------- shadows

shadow = SPEC["core"].setdefault("shadow", {})
# The card/composer elevation is painted, not a named var: a 6% ring + two
# soft umbrae, read off the composer (same shadow on tool panels and CTAs).
layers = shadow_layers(C.get("composer", {}).get("states", {}).get("default", {}).get("style", {}).get("boxShadow"))
if layers:
    shadow["card"] = {"value": layers, "type": "shadow",
                      "source": "computed boxShadow of composer default (raw/components-computed.json)",
                      "description": "The floating-card elevation (a 1px 6% keyline ring plus 1px/2px umbrae): "
                                     "composer, tool panel, plan CTA."}
else:
    gap("shadow.card: no composer default boxShadow layer")
for key, vname, desc in [
    ("drop-sm", "--drop-shadow-sm", "Declared drop-shadow filter sm (15% black, 1px 2px)."),
    ("drop-md", "--drop-shadow-md", "Declared drop-shadow filter md (12% black, 3px 3px)."),
]:
    if declared(vname):
        layers = shadow_layers(R[vname])
        if layers:
            shadow[key] = {"value": layers, "type": "shadow",
                           "source": f"css-var {vname} (light)",
                           "description": desc}
        else:
            gap(f"shadow.{key}: {vname} has no shadow layer")

# ------------------------------------------------------- z-index, backdrop

z = SPEC["core"].setdefault("zIndex", {})
if declared("--z-index-dropdown"):
    z["dropdown"] = {"value": int(float(R["--z-index-dropdown"])), "type": "number",
                     "source": "css-var --z-index-dropdown (light)",
                     "description": "Declared dropdown/menu z-index (40); the sticky header also paints z-40."}

blur = SPEC["core"].setdefault("blur", {})
for name in ["xs", "sm", "md"]:
    vname = f"--blur-{name}"
    if declared(vname):
        blur[name] = var(vname, "dimension", description=f"Declared --blur-{name} ({R[vname]}).")

# ---------------------------------------------------------------- measured

meas = SPEC["core"].setdefault("measured", {})
# The keyboard focus ring: buttons and links recolor their border to the
# accent and paint a 3px 30% accent ring shadow (the computed outline-style
# stays none — the ring is the shadow, not an outline).
# The alias is published only for the components whose real keyboard focus
# painted a border in the --ring colour (a failed focus is not a reading), and
# only while --ring and --accent (color.brand.accent) still resolve alike.
_ring = norm_color(R.get("--ring", ""))
_ringed = [k for k in ("nav-signin", "nav-cta", "send-btn")
           if have(k, "focus-visible", "borderTopColor")
           and C[k]["states"]["focus-visible"].get("via") != "focus failed"
           and norm_color(st(k, "focus-visible")["borderTopColor"]) == _ring]
if not _ringed or norm_color(R.get("--accent", "")) != _ring:
    raise SystemExit("focus-ring: no focus-visible reading paints the --ring colour, or --ring != --accent")
meas["focus-ring"] = {"value": "{color.brand.accent}", "type": "color",
                      "source": f"computed focus-visible borderTopColor of {', '.join(_ringed)} == --ring (raw/components-computed.json)",
                      "description": "The keyboard focus ring: the accent sky #01bcff as a 3px 30% ring plus an accent border."}
# The 30% ring shadow buttons paint on focus-visible.
layers = shadow_layers(C.get("nav-signin", {}).get("states", {}).get("focus-visible", {}).get("style", {}).get("boxShadow"))
if layers:
    shadow["focus-ring"] = {"value": layers, "type": "shadow",
                            "source": "computed boxShadow of nav-signin focus-visible (raw/components-computed.json)",
                            "description": "The 3px 30% accent ring buttons paint on keyboard focus (plus an accent border)."}
    meas["focus-ring-width"] = {"value": max(layers, key=lambda l: float(l["spread"][:-2]))["spread"], "type": "dimension",
                                "source": "computed boxShadow spread of nav-signin focus-visible (raw/components-computed.json)",
                                "description": "The 3px focus ring spread."}
else:
    gap("shadow.focus-ring: no nav-signin focus-visible boxShadow layer")
# Field fill: the translucent #ebebeb/50% the text inputs paint.
measure("field-fill", "field-name", "default", "backgroundColor", "color",
        "The translucent field fill the contact/tool inputs paint (≈47% neutral grey).", meas)
# The header veil: the sticky header paints a translucent backdrop-filtered field.
try:
    s = st("header", "default")
    v = norm_color(s["backgroundColor"])
    meas["header-veil"] = {"value": v, "type": "color",
                           "source": "computed backgroundColor of header default (raw/components-computed.json)",
                           "description": "The sticky header's translucent veil (≈90% page field, backdrop-blurred)."}
except KeyError:
    gap("measured.header-veil: no header default reading")
for key, comp, state, desc in [
    ("link-transition", "nav-link", "default", "The 150ms colour transition on nav links and buttons."),
]:
    try:
        s = st(comp, state)
        d = (s.get("transitionDuration") or "").split(",")[0].strip()
        if d and d != "0s":
            meas[key] = {"value": d, "type": "duration",
                         "source": f"computed transition of {comp} {state} (raw/components-computed.json)",
                         "description": desc + f" ({s.get('transitionProperty', '')[:80]})"}
        else:
            gap(f"measured.{key}: {comp} {state} has no transition")
    except (KeyError, TypeError):
        gap(f"measured.{key}: no {comp} {state} reading")

# ---------------------------------------------------------------- themes
# The shadcn-style roles, emitted into light and dark off the same var names.
ROLE_VARS = [
    ("background", "The page field (#fcfcfc light / #000000 dark)."),
    ("foreground", "Body and heading ink."),
    ("card", "Card fills (#ffffff / #171717)."),
    ("card-foreground", "Text on cards."),
    ("popover", "Popover/menu surfaces."),
    ("popover-foreground", "Text on popovers."),
    ("primary", "The primary fill (#171717 / #e5e5e5) — buttons, active pills."),
    ("primary-foreground", "Text on the primary fill."),
    ("secondary", "Secondary fills (#f5f5f5 / #262626)."),
    ("secondary-foreground", "Text on secondary fills."),
    ("muted", "Muted surfaces (#f5f5f5 / #262626)."),
    ("muted-foreground", "Secondary text (#6e6e6e / #a1a1a1)."),
    ("muted-hover", "Muted hover fill (light #f5f5f5 / dark 50% #262626)."),
    ("accent", "The accent sky #01bcff (identical in both themes)."),
    ("accent-foreground", "Text on the accent (#fafafa / #0a0a0a)."),
    ("destructive", "Destructive red (#d40c1a / #f75e54)."),
    ("destructive-foreground", "Text on the destructive fill."),
    ("destructive-border", "Destructive border."),
    ("destructive-ring", "Destructive focus ring (20–40% red)."),
    ("destructive-subtle", "Destructive tint fill (10–20% red)."),
    ("success", "Success green (#037650 / #00bc7d)."),
    ("success-foreground", "Text on the success fill."),
    ("warning", "Warning amber (#a16601 / #fe9a00)."),
    ("warning-foreground", "Text on the warning fill."),
    ("warning-content", "Warning text/icon on light tints."),
    ("warning-icon", "Warning icon colour."),
    ("warning-border", "Warning border."),
    ("warning-subtle", "Warning tint fill."),
    ("warning-subtle-hover", "Warning tint hover."),
    ("highlight", "Highlight yellow (#f7cc4b / #efa30f)."),
    ("highlight-foreground", "Text on the highlight."),
    ("border", "Hairline borders (#e5e5e5 / 10% white)."),
    ("input", "Field borders (#e5e5e5 / 15% white)."),
    ("ring", "The interactive ring — accent sky (identical in both themes)."),
    ("hairline", "The 5–10% hairline (dividers, underlines)."),
    ("paper", "The paper/print surface (white)."),
    ("overlay", "The overlay/scrim colour (black)."),
    ("overlay-foreground", "Text on the scrim (white)."),
    ("surface-sunken", "The sunken surface (white / black)."),
    ("surface-bubble", "The chat-bubble surface (#f5f5f5 / 60% #262626)."),
    ("surface-control", "Control fill (#f5f5f5 / #171717)."),
    ("surface-mention", "The mention/chip surface (#e5e5e5 / #040404)."),
]
SIDEBAR_VARS = [
    ("sidebar", "Docs/sidebar field."),
    ("sidebar-foreground", "Sidebar text."),
    ("sidebar-foreground-muted", "Muted sidebar text."),
    ("sidebar-primary", "Sidebar primary fill."),
    ("sidebar-primary-foreground", "Text on the sidebar primary."),
    ("sidebar-accent", "Sidebar hover/accent fill."),
    ("sidebar-accent-foreground", "Text on the sidebar accent."),
    ("sidebar-border", "Sidebar hairline."),
    ("sidebar-ring", "Sidebar focus ring."),
]
PALETTES = [
    ("mode-image", "Image-mode hue (blue)."), ("mode-image-foreground", "Text on image-mode."),
    ("mode-video", "Video-mode hue (purple)."), ("mode-video-foreground", "Text on video-mode."),
    ("mode-audio", "Audio-mode hue (orange)."), ("mode-audio-foreground", "Text on audio-mode."),
    ("mode-3d", "3D-mode hue (teal)."), ("mode-3d-foreground", "Text on 3D-mode."),
    ("series-1", "Chart series 1 (blue)."), ("series-2", "Chart series 2 (orange)."),
    ("series-3", "Chart series 3 (green)."), ("series-4", "Chart series 4 (amber)."),
    ("series-5", "Chart series 5 (pink)."), ("series-other", "Chart series for the rest (grey)."),
    ("chart-1", "Chart grey ramp 1."), ("chart-2", "Chart grey ramp 2."),
    ("chart-3", "Chart grey ramp 3."), ("chart-4", "Chart grey ramp 4."),
    ("chart-5", "Chart grey ramp 5."),
]

DECLARED = "declared shadcn-style role on the Tailwind v4 theme layer"


def emit_role(root, name, desc):
    vname = f"--{name}"
    if declared(vname):
        emit(root, vname, {"var": vname, "type": "color",
                           "source": DECLARED, "description": desc})


for name, desc in ROLE_VARS:
    emit_role(SPEC["light"], name, desc)
    emit_role(SPEC["dark"], name, desc)
for name, desc in SIDEBAR_VARS:
    emit_role(SPEC["light"], name, desc)
    emit_role(SPEC["dark"], name, desc)
pal_l = SPEC["light"].setdefault("palette", {})
pal_d = SPEC["dark"].setdefault("palette", {})
for name, desc in PALETTES:
    vname = f"--{name}"
    if declared(vname):
        emit(pal_l, vname, {"var": vname, "type": "color", "source": DECLARED, "description": desc})
        emit(pal_d, vname, {"var": vname, "type": "color", "source": DECLARED, "description": desc})

# The sky gradient the hero paints: lab stops converted to sRGB, one literal
# per theme (the var re-binds).
grad_l = gradient_stops(R.get("--gradient-sky", ""))
grad_d = gradient_stops(D.get("--gradient-sky", ""))
if not (grad_l and grad_d):
    gap("gradient-sky: --gradient-sky has no stops in one theme")
if grad_l:
    SPEC["light"]["gradient-sky"] = {"value": grad_l, "type": "gradient",
                                     "source": "css-var --gradient-sky (light; lab stops converted to sRGB)",
                                     "description": "The hero sky wash (light): pale blue to white, top to bottom."}
if grad_d:
    SPEC["dark"]["gradient-sky"] = {"value": grad_d, "type": "gradient",
                                    "source": "css-var --gradient-sky (dark; lab stops converted to sRGB)",
                                    "description": "The hero sky wash (dark): deep blue-black gradient."}

# ------------------------------------------------------------ typography

type_ = SPEC["core"].setdefault("font", {}).setdefault("type", {})


def typo(key, comp, state, desc):
    try:
        s = st(comp, state)
        type_[key] = {"$type": "typography",
                      "$value": {
                          "fontFamily": s["fontFamily"],
                          "fontSize": s["fontSize"],
                          "lineHeight": s["lineHeight"],
                          "fontWeight": int(float(s["fontWeight"])),
                          "letterSpacing": s["letterSpacing"] if s["letterSpacing"] != "normal" else "0px"},
                      "$description": desc,
                      "$extensions": {"source": f"computed type of {comp} {state} (raw/components-computed.json)"}}
    except (KeyError, ValueError):
        gap(f"font.type.{key}: no {comp} {state} reading")


typo("display", "hero-title", "default", "The home hero display (59.2px medium, tight tracking).")
typo("display-mobile", "m-hero", "default", "The hero display at 390px (37.6px).")
typo("h1", "pricing-h1", "default", "Page titles (48px medium, -2.4px).")
typo("h2", "h2-section", "default", "Section headings (36px medium, -0.9px).")
typo("h3", "plan-name", "default", "Card/sub headings (18px semibold).")
typo("body", "header", "default", "Body text (16px/24px regular).")
typo("small", "nav-link", "default", "Small text (14px/20px) — nav, buttons, fields.")
typo("lede", "hero-lede", "default", "The hero lede (18px/29.25px at 75% ink).")
typo("docs-h1", "docs-h1", "default", "Docs page heading (28px semibold).")
typo("code", "mcp-code", "default", "Code (Geist Mono 14px/20px).")

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("header.height", "header", "default", "height", "The 56px sticky marketing header."),
    ("header.height-mobile", "m-header", "default", "height", "The 56px mobile header."),
    ("button.height-sm", "nav-cta", "default", "height", "Small buttons (32px: header CTA, nav, pills, icon rows)."),
    ("button.height-md", "tool-generate", "default", "height", "Medium buttons (36px: tool Generate, model pill)."),
    ("button.height-lg", "send-btn", "default", "height", "Large buttons (52px: Send, plan CTA)."),
    ("button.padding-x-sm", "nav-cta", "default", "paddingLeft", "Small-button horizontal padding (16px)."),
    ("button.padding-x-lg", "send-btn", "default", "paddingLeft", "Large-button horizontal padding (28px)."),
    ("button.radius-sm", "nav-cta", "default", "borderTopLeftRadius", "Small-button radius (8px)."),
    ("button.radius-md", "send-btn", "default", "borderTopLeftRadius", "Standard button radius (12px)."),
    # Not composer-send: that reading caught the composer's "Add to prompt"
    # attach button, not the send control (README, Known gaps).
    ("icon-button.size", "m-menu-button", "default", "height", "The 36px square icon button (the phone-width Menu button)."),
    ("icon-button.size-sm", "theme-toggle", "default", "height", "The 32px icon button (theme toggle)."),
    ("nav-link.height", "nav-link", "default", "height", "Header nav link height (32px)."),
    ("field.height", "field-name", "default", "height", "Text field height (40px; textarea 64px min)."),
    ("field.radius", "field-name", "default", "borderTopLeftRadius", "Field radius (8px)."),
    ("field.width", "field-name", "default", "width", "The contact form's 640px field measure."),
    ("search.height", "models-search", "default", "height", "Compact search/doc-search field (32–36px)."),
    ("card.radius", "plan-card", "default", "borderTopLeftRadius", "Plan/blog card radius (16px)."),
    ("card.radius-lg", "model-card", "default", "borderTopLeftRadius", "Large tile radius (20px: model cards, brand tiles, composer)."),
    ("card.padding", "plan-card", "default", "paddingTop", "Card padding (24px)."),
    ("card.width-plan", "plan-card", "default", "width", "Plan card width (273px)."),
    ("card.width-model", "model-card", "default", "width", "Model card width (≈355px)."),
    ("composer.width", "composer", "default", "width", "The hero prompt composer width (660px)."),
    ("composer.radius", "composer", "default", "borderTopLeftRadius", "Composer radius (20px)."),
    ("composer.padding-x", "composer-input", "default", "paddingLeft", "Composer inner padding (20px)."),
    ("form.width", "contact-form", "default", "width", "The contact form column (640px)."),
    ("sidebar.width", "docs-sidebar", "default", "width", "The docs sidebar (268px)."),
    ("menu-panel.width", "m-menu-open", "default", "width", "The mobile menu panel (full 390px width)."),
    ("swatch.width", "brand-swatch", "default", "width", "Brand colour swatch tile (285px)."),
]:
    if have(cname, state, prop):
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)[prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}
    else:
        gap(f"component.{key}: no {cname} {state} {prop} reading")

# Rows missing from the committed readings, kept visible in `_gaps`. Empty:
# every named row has its reading today, so any miss is a new gap.
KNOWN_GAPS = set()
_new = [g for g in GAPS if g not in KNOWN_GAPS]
if _new:
    raise SystemExit("missing readings for named token rows (recapture, or list them in KNOWN_GAPS):\n  " + "\n  ".join(_new))
if GAPS:
    SPEC["_gaps"] = GAPS

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
