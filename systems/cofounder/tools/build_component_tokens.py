"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

cofounder.co is a Next.js/Tailwind v4 build: the sheet declares a small
custom-property layer on `:root` — `--background`/`--foreground`,
`--color-surface`, `--color-ink-ui-solid`, the `--color-lime-*` accent pair,
`--color-feature-*` support colours, the `--font-*` families (TT Neoris,
Inter, Departure Mono, IBM Plex Mono), `--font-weight-*` steps, the
`--radius-*` and `--spacing` primitives, `--blur-*` steps and the
`--ease-*`/`--default-transition-*` motion vars — while its semantic
palette (ink at three opacities, surface-raised, border-card, the #1a6fd1
tools band, the dark cta gradient) ships as literal utility values, not
vars. Every role below is still measured on the painted chrome and cited
back to raw/components-computed.json — declarations say what Cofounder
named, the measurements say what it paints.

The site paints ONE light theme; the #1a6fd1 tools band and the pixel-art
hero are coloured bands inside it. app.cofounder.co/os/login is a separate
app surface (the sign-in boundary), measured at rest and never submitted.

The declared palette:

  surface   #f5f5f2 ground (--background/--color-surface); raised #fbfbf8
  ink       #171717 foreground, #202020 ink-ui-solid, #262323 at
            80/70/50% opacities as literal utility colours
  lime      #bbf451 lime-300 accent, #d8f999 lime-200 light
  band      #1a6fd1 tools band; #dee2de card border; #f3f3f0 logo tile
  feature   #34a853 success, #bfbfbf neutral
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
# cofounder paints light only (catalog theme list): resolve against the light pass, never a dark probe.
RL = V["resolved"]["light"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}

# Scoped declarations the resolved map does not reach: next/font loader
# classes declare the real family stacks, and :root re-exports them through
# var() aliases. APP flattens every app-scope rule's properties; appvar()
# resolves var() chains inside it.
APP = {}
for _r in V.get("app", []):
    for _k, _v in _r.get("properties", {}).items():
        APP.setdefault(_k, _v)


def appvar(name, depth=0):
    v = APP.get(name)
    if v is None or depth > 6:
        return v
    m = re.fullmatch(r"var\(\s*(--[\w-]+)\s*\)", v.strip())
    return appvar(m.group(1), depth + 1) if m else v


# The Tailwind v4 sheet declares its primitives on :root; declared leaves
# resolve through R (the var name stays the provenance). The semantic shades
# the site paints without declaring (ink at 80/70/50% opacities, the #fbfbf8
# raised surface, #dee2de card border, the #1a6fd1 tools band, the logo-tile
# fill) ship as literal utility values, so they are measured leaves cited to
# the component that paints them.
#   (token path, declared var name, description)
DECLARED = [
    ("surface", "--color-surface", "Declared color-surface (#f5f5f2) — the warm off-white page ground (same value as --background)."),
    ("ink.90", "--foreground", "Declared foreground (#171717) — the deepest text ink."),
    ("ink.ui", "--color-ink-ui-solid", "Declared ink-ui-solid (#202020) — solid UI ink, the dark CTA base."),
    ("lime.200", "--color-lime-200", "Declared lime-200 (lab ≈ #d8f999) — the light lime accent step."),
    ("lime.300", "--color-lime-300", "Declared lime-300 (lab ≈ #bbf451) — the lime accent."),
    ("feature.neutral", "--color-feature-neutral", "Declared feature-neutral (#bfbfbf)."),
    ("feature.success", "--color-feature-success", "Declared feature-success (#34a853) — the only status colour declared."),
    ("black", "--color-black", "Declared color-black (#000)."),
    ("white", "--color-white", "Declared color-white (#fff) — text on the dark CTA and the blue band."),
]
#   (token path, component, state, style prop, description) — literal
#   utility colours the site paints without naming a var for them.
CORE = [
    ("surfaceRaised", "plan-card", "default", "paint.0.bg", "The #fbfbf8 raised card ground (bg-surface-raised literal, painted on the inner .pricing-card layer)."),
    ("ink.80", "section-title", "default", "textStyle.color", "The primary ink #262323 at 80% (text-ink literal)."),
    ("ink.70", "plan-name", "default", "color", "Muted ink #262323 at 70% (text-ink-muted literal)."),
    ("ink.50", "footer-social", "default", "color", "Faint ink #262323 at 50% — the footer social icons."),
    ("band", "blue-section", "default", "backgroundColor", "The #1a6fd1 tools band (bg-[#1a6fd1] literal)."),
    ("borderCard", "plan-card", "default", "paint.0.border", "The #dee2de card border (border-border-card literal, on the inner .pricing-card)."),
    ("tile", "logo-tile", "default", "backgroundColor", "The #f3f3f0 logo-tile fill."),
    ("ctaDark", "cta-dark", "default", "backgroundImage.lastColor", "The dark CTA gradient's base colour (≈ #202020d9 at the bottom stop)."),
]
SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. cofounder.co "
    "declares a Tailwind v4 custom-property layer on :root (raw/css-vars.json) "
    "plus literal semantic utility colours. The core ramps below are the "
    "declared values plus the literal utility colours the sheet paints "
    "(ink opacities, surface-raised, border-card, the #1a6fd1 band). "
    "Semantic roles are measured on the painted chrome in "
    "raw/components-computed.json and alias the core when the value "
    "matches. One theme exists (light); coloured bands live inside it."),
    "core": {}, "light": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = None
    return node, parts[-1]


# ------------------------------------------------------------- light roles
#
# The bundle declares no semantic role names of its own; every role below is
# measured on the painted chrome (header, hero cards, plan carousel, search
# filters, footer) and aliases a core token when the value matches. The
# marketing site paints one light theme, emitted under `light`; the footer
# is a black island inside it, so its text role is named onDark.
def st(comp, state):
    c = C[comp]
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(comp)
    return c["states"][state]["style"]


def stprop(comp, state, prop):
    """prop may be `styleProp`, `textStyle.prop`, `paint.N.prop` (the Nth
    painted child layer) or the special `ringShadow`: resolve the dotted path
    inside the measured state (the anchors keep UA-default colour, so painted
    text/fill lives on the text child, a sibling layer or a pseudo).
    `ringShadow` returns the colour of the `0 0 0 Npx` ring layer in the
    element's own boxShadow — the hairline many Framer controls paint instead
    of a real border."""
    d = C[comp]["states"][state]
    # `.firstColor`/`.lastColor` pull the first/last colour literal out of a
    # string property (gradient stops in backgroundImage, shadow layers).
    for suffix, pick in ((".firstColor", 0), (".lastColor", -1)):
        if prop.endswith(suffix):
            v = stprop(comp, state, prop[: -len(suffix)])
            cols = re.findall(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", v or "")
            return cols[pick] if cols else ""
    if prop == "ringShadow":
        sh = d.get("style", {}).get("boxShadow", "") or ""
        for layer in re.split(r",(?![^(]*\))", sh):
            if re.search(r"0px 0px 0px\s+(?:0\.[5-9]|[1-9])[\d.]*px", layer):
                m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", layer)
                if m:
                    return m.group(0)
        return ""
    # A bare property reads the computed style block (backgroundColor); a
    # dotted path walks the state dict (textStyle.color, paint.2.bg,
    # ancestors.0.bg), a numeric step indexing a list. A `.border` tail reads
    # the colour out of the "T:1px solid rgba(...)" string styleOf records.
    if "." not in prop:
        return d.get("style", {}).get(prop, "")
    node = d
    for part in prop.split("."):
        if isinstance(node, list) and part.isdigit():
            node = node[int(part)] if int(part) < len(node) else None
        elif isinstance(node, dict):
            node = node.get(part)
        else:
            return ""
        if node is None:
            return ""
    if isinstance(node, str) and prop.endswith(".border"):
        m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", node)
        return m.group(0) if m else ""
    return node if isinstance(node, str) else ""


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
    m = re.fullmatch(r"rgb\(([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*/\s*([\d.]+%?)\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % a})"
    m = re.fullmatch(r"lab\(\s*([\d.]+%?)\s+(-?[\d.]+)\s+(-?[\d.]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        # Tailwind v4 declares colours as lab() (D50 white); convert through
        # XYZ with Bradford adaptation to D65 so the token is an sRGB value.
        L = float(m.group(1).rstrip("%"))
        if m.group(1).endswith("%"):
            L /= 100
        a_, b_ = float(m.group(2)), float(m.group(3))
        fy = (L * 100 + 16) / 116
        fx, fz = fy + a_ / 500, fy - b_ / 200
        d = 6 / 29
        finv = lambda t: t ** 3 if t > d else 3 * d * d * (t - 4 / 29)
        X, Y, Z = 0.964212 * finv(fx), finv(fy), 0.825188 * finv(fz)
        # Bradford D50 -> D65
        X, Y, Z = (0.9555766 * X - 0.0230393 * Y + 0.0631636 * Z,
                   -0.0282895 * X + 1.0099416 * Y + 0.0210077 * Z,
                   0.0122982 * X - 0.020483 * Y + 1.3299098 * Z)
        R_ = 3.2404542 * X - 1.5371385 * Y - 0.4985314 * Z
        G_ = -0.9692660 * X + 1.8760108 * Y + 0.0415560 * Z
        B_ = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
        gam = lambda x: max(0, min(255, round((12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055) * 255)))
        al = m.group(4)
        al = float(al[:-1]) / 100 if al and al.endswith("%") else float(al) if al else 1
        if al >= 1:
            return "#%02x%02x%02x" % (gam(R_), gam(G_), gam(B_))
        return f"rgba({gam(R_)}, {gam(G_)}, {gam(B_)}, {'%g' % al})"
    m = re.fullmatch(r"oklab\(\s*([\d.]+)\s+(-?[\d.]+)\s+(-?[\d.]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        # Framer paints some alpha greys as oklab(); convert to sRGB.
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
    m = re.fullmatch(r"oklch\(\s*([\d.]+%?)\s+([\d.]+)\s+([\d.]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        # Sheets can paint oklch(); convert through OKLab to sRGB so the
        # token is a usable colour value.
        import math
        L = float(m.group(1).rstrip("%"))
        if m.group(1).endswith("%"):
            L /= 100
        C_, H = float(m.group(2)), math.radians(float(m.group(3)))
        A, B = C_ * math.cos(H), C_ * math.sin(H)
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
        if isinstance(v, dict) and ("var" in v or "value" in v):
            val = norm_color(R[v["var"]]) if "var" in v else norm_color(v["value"])
            BY_VALUE.setdefault(val, prefix + k)
        elif isinstance(v, dict):
            collect(v, prefix + k + ".")
core_color = SPEC["core"].setdefault("color", {})
for path, var, desc in DECLARED:
    v = R.get(var)
    if not v:
        raise SystemExit(f"declared var missing: {var}")
    node, last = descend(core_color, path.split("."))
    node[last] = {"value": norm_color(v), "type": "color",
                  "source": f"declared {var} (raw/css-vars.json)",
                  "description": desc}
for path, cname, state, prop, desc in CORE:
    v = stprop(cname, state, prop)
    if "shadow" in prop.lower():
        m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", v or "")
        v = m.group(0) if m else ""
    v = norm_color(v)
    if not v or v == "transparent":
        raise SystemExit(f"core palette source missing: {cname} {state} {prop}")
    node, last = descend(core_color, path.split("."))
    node[last] = {"value": v, "type": "color",
                  "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                  "description": desc}
collect(core_color, "color.")


def role(path, comp, state, prop, desc):
    v = stprop(comp, state, prop)
    if "shadow" in prop.lower():
        m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", v or "")
        v = m.group(0) if m else ""
    v = norm_color(v)
    if not v or v == "transparent":
        return
    target = BY_VALUE.get(v)
    leaf = {"type": "color", "description": desc}
    if target:
        leaf["value"] = "{%s}" % target
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json); same value as core.{target}"
    else:
        leaf["value"] = v
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
    theme, _, rest = path.partition(":")
    node = SPEC[theme or "dark"]
    parts = rest.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf



for path, comp, state, prop, desc in [
    # ----- the single light surface
    ("light:surface.page", "page-ground", "default", "backgroundColor", "The page ground — painted by the body (#f5f5f2 = declared --background/--color-surface)."),
    ("light:surface.raised", "plan-card", "default", "paint.0.bg", "The raised card ground (#fbfbf8) the pricing card paints."),
    ("light:surface.band", "blue-section", "default", "backgroundColor", "The #1a6fd1 tools band inside the single light theme."),
    ("light:text.primary", "section-title", "default", "textStyle.color", "The primary ink (#262323 at 80% = the text-ink utility)."),
    ("light:text.muted", "plan-name", "default", "color", "Muted ink (#262323 at 70% = text-ink-muted)."),
    ("light:text.faint", "footer-social", "default", "color", "Faint ink (#262323 at 50%) — the footer social icons and the tool-button captions."),
    ("light:text.nav", "nav-item", "default", "color", "The nav-link ink at rest (#fbfbf8 surface-raised text on the glass nav)."),
    ("light:text.onAccent", "cta-dark", "default", "textStyle.color", "White-90 text on the dark CTA controls."),
    ("light:text.onBand", "tool-tab", "default", "textStyle.color", "White text on the #1a6fd1 tools band."),
    ("light:text.link", "footer-link", "default", "color", "Footer link ink at rest (text-ink; hover keeps the colour and paints a rounded highlight behind it)."),
    ("light:text.linkHover", "footer-link", "hover", "color", "Footer link ink on hover — the colour holds, a 4px-radius tint pill appears behind it."),
    ("light:accent", "cta-dark", "default", "backgroundImage.lastColor", "The dark CTA fill — the surface's accent control (gradient base ≈ #202020d9)."),
    ("light:accentHover", "cta-dark", "hover", "backgroundImage.lastColor", "The dark CTA's hover fill (gradient base on hover)."),
    ("light:border.subtle", "cta-light", "default", "borderTopColor", "The 1px rgba(32,32,32,.1) hairline on the light-surface buttons."),
    ("light:border.card", "plan-card", "default", "paint.0.border", "The pricing card border (#dee2de = border-border-card utility, on the inner .pricing-card)."),
    ("light:border.cta", "cta-dark", "default", "borderTopColor", "The dark CTA's #383838 edge."),
    ("light:focus", "nav-item", "focus-visible", "outlineColor", "The focus ring on the surface's controls (outline-ink/outline-white depending on ground)."),
]:

    try:
        role(path, comp, state, prop, desc)
    except KeyError:
        pass

# The glass nav/hero buttons paint translucent white gradients (the
# glass-pill layer) — kept as a measured role because the blur-tint is the
# surface's signature chrome.
# Read from the nav pill's painted gradient (the header's paint list): its top stop. raw/css-vars.json holds
# no .glass-pill rule, so the token cites the reading, not a declaration.
_glass = next((p_["bgImage"] for p_ in (C.get("header", {}).get("states", {}).get("default", {}).get("paint") or [])
               if str(p_.get("bgImage", "")).startswith("linear-gradient(rgba(255, 255, 255")), None)
if not _glass:
    raise SystemExit("build_component_tokens: no glass gradient in the header's paint list")
_top = re.match(r"linear-gradient\((rgba\([^)]*\))", _glass).group(1)
SPEC["light"]["surface"]["glass"] = {
    "type": "color", "value": norm_color(_top),
    "source": f"computed paint bgImage of header default (raw/components-computed.json): {_glass}, its top stop",
    "description": "The white-glass tint on the nav pill and hero prompt button (backdrop-blur 16px over it); the gradient's top stop."}

# -------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})
for comp, state, key, prop, desc in [
]:
    try:
        v = norm_color(stprop(comp, state, prop))
        if v and v != "transparent":
            meas[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# The surface's painted elevations: layered inset+drop shadows on the
# buttons and the pricing card. The first component with a real shadow wins
# each slot.
for _cname in ("plan-card", "cta-dark", "hero-prompt-btn"):
    try:
        _sh = stprop(_cname, "default", "boxShadow") or ""
        if _sh and _sh != "none":
            _layers = []
            for _ly in re.split(r",(?![^(]*\))", _sh):
                m = re.match(
                    r"\s*(rgb[a]?\([^)]*\)|#[0-9a-fA-F]{3,8})\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(\s+inset)?",
                    _ly)
                if m:
                    _layer = {"color": m.group(1), "offsetX": m.group(2) + "px",
                              "offsetY": m.group(3) + "px", "blur": m.group(4) + "px",
                              "spread": m.group(5) + "px"}
                    if m.group(6):
                        _layer["inset"] = True
                    _layers.append(_layer)
            if _layers:
                SPEC["light"]["shadow"] = {"card" if _cname == "plan-card" else "control": {
                    "type": "shadow", "value": _layers,
                    "source": f"computed boxShadow of {_cname} default (raw/components-computed.json)",
                    "description": f"The {_cname}'s layered shadow — the surface's painted elevation (inset edge lights + ambient drops)."}}
            break
    except KeyError:
        continue

# Declared radii: the Tailwind theme ships md/lg/xl/2xl; measured control
# radii (8px buttons, 10px tiles/tool buttons, full pills) sit beside them.
rad = SPEC["core"].setdefault("radius", {})
for key, var, desc in [
    ("md", "--radius-md", "Declared radius-md (.375rem = 6px)."),
    ("lg", "--radius-lg", "Declared radius-lg (.5rem = 8px) — the button radius."),
    ("xl", "--radius-xl", "Declared radius-xl (.75rem = 12px)."),
    ("xxl", "--radius-2xl", "Declared radius-2xl (1rem = 16px) — pricing cards."),
]:
    v = R.get(var)
    if v:
        rad[key] = {"value": v, "type": "dimension",
                    "source": f"declared {var} (raw/css-vars.json)",
                    "description": desc}
for key, cname, desc in [
    ("control", "nav-cta", "The button radius on the pill controls."),
    ("tile", "logo-tile", "The logo-tile corner (10px)."),
]:
    try:
        v = stprop(cname, "default", "borderTopLeftRadius")
        if v:
            rad[key] = {"value": v, "type": "dimension",
                        "source": f"computed borderTopLeftRadius of {cname} default (raw/components-computed.json)",
                        "description": desc}
    except KeyError:
        pass

# Declared motion: the ease steps and the default transition duration.
for key, var in [
    ("default", "--default-transition-duration"),
]:
    v = R.get(var)
    if v:
        SPEC["core"].setdefault("motion", {}).setdefault("duration", {})[key] = {
            "value": v, "type": "duration",
            "source": f"declared {var} (raw/css-vars.json)",
            "description": "The default transition duration (.15s)."}
for key, cname, prop, desc in [
    ("control", "hero-cta", "transitionDuration", "The control transition (.14s on the light pill buttons)."),
    ("nav", "nav-item", "transitionDuration", "The nav-link colour transition (.06s)."),
]:
    try:
        v = stprop(cname, "default", prop)
        if v and v != "0s":
            SPEC["core"].setdefault("motion", {}).setdefault("duration", {})[key] = {
                "value": v.split(",")[0].strip(), "type": "duration",
                "source": f"computed {prop} of {cname} default (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass
for key, var in [
    ("in_", "--ease-in"), ("out", "--ease-out"), ("inOut", "--ease-in-out"),
    ("default", "--default-transition-timing-function"),
]:
    v = R.get(var)
    if v:
        SPEC["core"].setdefault("motion", {}).setdefault("curve", {})[key] = {
            "value": v, "type": "cubicBezier",
            "source": f"declared {var} (raw/css-vars.json)",
            "description": f"Declared {var[2:]}."}
for key, cname, desc in [
    ("control", "tool-button", "The tool-button ease (the declared default curve, measured on the paint)."),
]:
    try:
        v = stprop(cname, "default", "transitionTimingFunction")
        m = re.search(r"cubic-bezier\([^)]+\)", v or "")
        if m:
            SPEC["core"].setdefault("motion", {}).setdefault("curve", {})[key] = {
                "value": m.group(0), "type": "cubicBezier",
                "source": f"computed transitionTimingFunction of {cname} default (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass

# Spacing: Tailwind declares the single --spacing base unit (.25rem = 4px);
# every layout gap derives calc(var(--spacing) * N). Measured paddings live
# in the component dimensions below.
v = R.get("--spacing")
if v:
    SPEC["core"].setdefault("spacing", {})["unit"] = {
        "value": v, "type": "dimension",
        "source": "declared --spacing (raw/css-vars.json)",
        "description": "The spacing base unit (.25rem = 4px) — every gap/padding multiplies it."}
# The blur steps are declared too (the glass chrome depends on them).
for key, var in [("sm", "--blur-sm"), ("md", "--blur-md"), ("lg", "--blur-lg")]:
    v = R.get(var)
    if v:
        SPEC["core"].setdefault("blur", {})[key] = {
            "value": v, "type": "dimension",
            "source": f"declared {var} (raw/css-vars.json)",
            "description": f"Declared {var[2:]} — backdrop-blur step (the glass pill uses 16px+)."}

# Type: Tailwind declares --text-xs/--text-sm and the weight steps;
# measured display sizes live in font.size below.
for key, var in [
    ("xs", "--text-xs"), ("sm", "--text-sm"),
]:
    v = R.get(var)
    if v:
        SPEC["core"].setdefault("fontSize", {})[key] = {
            "value": v, "type": "dimension",
            "source": f"declared {var} (raw/css-vars.json)",
            "description": f"Declared {var[2:]}."}
for key, var in [
    ("normal", "--font-weight-normal"), ("medium", "--font-weight-medium"),
    ("semibold", "--font-weight-semibold"),
]:
    v = R.get(var)
    if v:
        SPEC["core"].setdefault("fontWeight", {})[key] = {
            "value": int(v), "type": "fontWeight",
            "source": f"declared {var} (raw/css-vars.json)",
            "description": f"Declared {var[2:]}."}

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.heightNavCta", "nav-cta", "default", "height", "The nav Run-a-company pill."),
    ("control.heightNavItem", "nav-item", "default", "height", "Nav links."),
    ("control.heightHeroCta", "hero-cta", "default", "height", "The hero Run-a-company button."),
    ("control.heightPromptBtn", "hero-prompt-btn", "default", "height", "The glass copy-prompt button (41px)."),
    ("control.heightMenuButton", "m-menu-button", "default", "height", "The mobile menu toggle (41x41)."),
    ("control.radiusCta", "nav-cta", "default", "borderTopLeftRadius", "Button corner radius."),
    ("card.radiusPlan", "plan-card", "default", "paint.0.radius", "Pricing-card corner (radius-2xl, on the inner .pricing-card)."),
    ("nav.height", "header", "default", "height", "The fixed header bar at 1440px."),
    ("footer.height", "footer", "default", "height", "The footer block at 1440px."),
    ("drawer.width", "m-menu-open", "default", "width", "The mobile menu panel at 390px."),
    ("heroTitle.width", "hero-title", "default", "width", "The hero headline's measure."),
    ("tile.width", "logo-tile", "default", "width", "A customer logo tile (170x84)."),
    ("card.width", "plan-card", "default", "width", "A pricing card column at 1440px."),
]:
    try:
        v = stprop(cname, state, prop)
        if not v:
            continue
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": v,
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------- typography
#
# Families are declared on next/font loader classes (--font-neoris,
# --font-inter, --font-departure, --font-mono) and re-exported on :root
# through var() aliases; appvar() follows the chain. Measured display sizes
# sit beside the declared --text-* steps.

font = SPEC["core"].setdefault("family", {})
# The families are declared on :root and resolve through next/font loaders.
for key, var, desc in [
    ("display", "--font-neoris", "TT Neoris — the declared display/default face."),
    ("ui", "--font-inter", "Inter — the UI face."),
    ("mono", "--font-mono", "The declared mono face (IBM Plex Mono loader)."),
    ("departure", "--font-departure", "Departure Mono — the pixel-flavoured display mono."),
]:
    _v = appvar(var)
    if _v:
        font[key] = {"type": "fontFamily", "value": _v.replace("'", '"'),
            "source": f"declared {var} (raw/css-vars.json)",
            "description": desc}
font = SPEC["core"].setdefault("font", {"family": SPEC["core"].pop("family")})
for key, cname, prop, desc in [
    ("family.display", "hero-title", "fontFamily", "The display face on the hero headline."),
]:
    try:
        f = (stprop(cname, "default", prop) or stprop(cname, "default", "textStyle.fontFamily") or "").strip()
        if f:
            font.setdefault("family", {})[key.split(".")[-1]] = {"type": "fontFamily", "value": f,
                                        "source": f"computed {prop} of {cname} default (raw/components-computed.json)",
                                        "description": desc}
    except KeyError:
        pass

for key, cname, desc in [
    ("size.hero", "hero-title", "The hero display headline at 1440px (46px/108%)."),
    ("size.h2", "section-title", "Section headings."),
    ("size.mHero", "m-hero", "The hero headline at 390px."),
    ("size.nav", "nav-item", "Nav labels (15px)."),
    ("size.footer", "footer-link", "Footer links."),
    ("size.planName", "plan-name", "The plan label inside a pricing card (15px)."),
    ("size.howtoCard", "howto-card-title", "The guide card titles (20px Neoris)."),
]:
    try:
        sz = stprop(cname, "default", "textStyle.fontSize") or stprop(cname, "default", "fontSize")
        if sz:
            font.setdefault("size", {})[key.split(".")[-1]] = {"type": "dimension", "value": sz,
                                        "source": f"computed fontSize of {cname} default (raw/components-computed.json)",
                                        "description": desc}
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
