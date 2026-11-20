#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

cron.com is two surfaces: the static dark marketing page (inline <style>,
literal declarations, #161412 over #0f0d0a) and the light Next.js content
app at /blog, /changelog and /blog/<post> (white page, #1a1a1a text) whose
sheets declare a real token layer on :root, harvested into raw/css-vars.json:

  --gray10..--gray900   the 14-step neutral ramp
  --chronos #ff4700     the brand orange (+ --chronos-gradient, --primary100/700)
  --eclipse/--snow/--dieter/--urushi/--ratio   the named ink/paper set
  --text-default, --material-*, --object-*     semantic surface roles
  --elevation-low/-high, --z-index-popover     elevation + layering
  --animation-duration-default, --disabled-opacity, --sans-serif-font

Those become {"var": ...} leaves resolved by build_tokens.py. The dark home
page declares no vars, so its values are measured computed styles
(raw/components-computed.json):

  type       Helvetica Neue at 700 for the 140px hero (80px mobile), 500
             links, 400 body at 22px home / 16px content pages
  actions    #ff4700 on both surfaces — the glow-shadowed Sign up pill on
             dark, plain links on light
  surfaces   #161412 page + #0f0d0a footer on dark; white content pages
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. cron.com's public "
    "surface splits in two: the dark marketing home (literal CSS, measured "
    "computed values) and the light Next.js content pages whose declared "
    "var layer (raw/css-vars.json: the 14-step gray ramp, --chronos brand, "
    "--elevation-*, --material-*/--object-* roles) is var-referenced "
    "wherever it names a value."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def st(comp, state):
    return C[comp]["states"][state]["style"]


def rc(comp, state, key):
    return C[comp]["states"][state]["rect"][key]


def ts(comp, state, prop):
    """The first text node's reading (textStyle) when the kit recorded one."""
    try:
        c = C[comp]["states"][state]
        t = c.get("textStyle") or {}
        v = t.get(prop)
        return v if v else c["style"].get(prop)
    except KeyError:
        return None


def oklab_srgb(v):
    """oklab()/oklch() (L as a number or a percentage, optional / alpha) -> #rrggbb or rgba(); None otherwise.
    The kit's conversion (OKLab -> linear sRGB -> gamma, clamped)."""
    import math
    m = re.fullmatch(r"ok(lab|lch)\(\s*([-\d.e]+)(%?)\s+([-\d.e]+)\s+([-\d.e]+|none)(?:deg)?\s*(?:/\s*([\d.]+)(%?))?\s*\)", v.strip().lower())
    if not m:
        return None
    kind, L, pct, x, y, a, apct = m.groups()
    L = float(L) / 100 if pct else float(L)
    if kind == "lch":
        c, h = float(x), 0.0 if y == "none" else math.radians(float(y))
        A, B = c * math.cos(h), c * math.sin(h)
    else:
        A, B = float(x), float(y)
    l_ = (L + 0.3963377774 * A + 0.2158037573 * B) ** 3
    m_ = (L - 0.1055613458 * A - 0.0638541728 * B) ** 3
    s_ = (L - 0.0894841775 * A - 1.2914855480 * B) ** 3
    lin = [4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
           -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
           -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_]
    rgb = [round(min(1, max(0, 12.92 * c_ if c_ <= 0.0031308 else 1.055 * c_ ** (1 / 2.4) - 0.055)) * 255) for c_ in lin]
    alpha = 1 if a is None else (float(a) / 100 if apct else float(a))
    if alpha >= 1:
        return "#%02x%02x%02x" % tuple(rgb)
    return "rgba(%d, %d, %d, %g)" % (rgb[0], rgb[1], rgb[2], round(alpha, 3))


def norm_color(v):
    v = (v or "").strip()
    ok = oklab_srgb(v)
    if ok:
        return ok
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
    return v


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False


def lit(value, ty, src, desc):
    if ty == "color" and oklab_srgb(str(value)):
        # Converted to sRGB; the source keeps the authored CSS Color 4 form.
        src += "; computed as %s, written as sRGB" % str(value).strip()
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}

# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
fam["sans"] = {"value": 'ABCDiatype, -apple-system, "system-ui", "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif',
    "type": "fontFamily",
    "source": "computed fontFamily of every measured component (raw/components-computed.json); @font-face faces for ABCDiatype are declared in the app sheets (raw/css-vars.json)",
    "description": "ABCDiatype — the product's own face on every surface."}
fam["fallback"] = var("--font-sans", "fontFamily",
    source="css-var --font-sans resolved (raw/css-vars.json)",
    description="The Tailwind system-ui stack that backs the ABCDiatype chain.")
weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, desc in [
    ("regular", "nav-button", "Measured 400 — body copy, icon glyphs."),
    ("medium", "signin-btn", "Measured 500 — buttons, tabs, headings, titles."),
]:
    if have(comp, "default", "fontWeight"):
        weights[key] = {"value": st(comp, "default")["fontWeight"], "type": "fontWeight",
                        "source": f"computed fontWeight of {comp} default (raw/components-computed.json)",
                        "description": desc}
if "--font-weight-semibold" in R:
    weights["semibold"] = var("--font-weight-semibold", "fontWeight",
        source="css-var --font-weight-semibold resolved (raw/css-vars.json)",
        description="The declared 600 weight.")
if "--font-weight-bold" in R:
    weights["bold"] = var("--font-weight-bold", "fontWeight",
        source="css-var --font-weight-bold resolved (raw/css-vars.json)",
        description="The declared 700 weight.")

# ----------------------------------------------------- declared palettes

col = SPEC["core"].setdefault("color", {})
cur = col.setdefault("curater", {})
for n in sorted(R):
    if n.startswith("--Curater-") and not n.startswith("--Curater-selection-"):
        cur[n[len("--Curater-"):]] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)",
            description=f"The {n} product-namespace value.")
sel = col.setdefault("selection", {})
for n in sorted(R):
    if n.startswith("--Curater-selection-"):
        sel[n[len("--Curater-selection-"):]] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)",
            description=f"Tag/curation accent {n} — the 9-hue selection palette.")
tail = col.setdefault("tailwind", {})
for n in sorted(R):
    if n.startswith("--color-"):
        tail[n[len("--color-"):]] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)",
            description=f"Tailwind palette step {n}.")
chart = col.setdefault("chart", {})
for n in sorted(R):
    if n.startswith("--chart-"):
        chart[n[len("--chart-"):]] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)",
            description=f"Chart hue {n}.")

# ----------------------------------------------------- semantic roles (declared)

sem = SPEC["light"].setdefault("color", {})
for key, n, group, desc in [
    ("page", "--background", "background", "The #ffffff app page fill."),
    ("surface", "--card", "background", "The #ffffff card surface."),
    ("app-field", "--Curater-background", "background", "The #f2f2f2 field — active/hover fills and the app backdrop."),
    ("text", "--foreground", "text", "The #09090b ink."),
    ("text-strong", "--primary", "text", "The #18181b primary ink."),
    ("muted", "--muted-foreground", "text", "The #71717b muted text (nav icons at rest, meta)."),
    ("muted-fill", "--muted", "background", "The #f4f4f5 muted fill."),
    ("accent-fill", "--accent", "background", "The #f4f4f5 accent fill."),
    ("accent-text", "--accent-foreground", "text", "The #18181b text on accent."),
    ("border", "--border", "border", "The #eeeef1 hairline."),
    ("input", "--input", "border", "The #e4e4e7 input hairline."),
    ("ring", "--ring", "border", "The #d4d4d8 focus ring."),
    ("destructive", "--destructive", "action", "The #e7000b destructive."),
    ("popover", "--popover", "background", "The #ffffff popover surface."),
    ("popover-text", "--popover-foreground", "text", "The #09090b popover ink."),
    ("on-primary", "--primary-foreground", "text", "The #fafafa text on primary."),
    ("sidebar", "--sidebar", "background", "The #fafafa sidebar surface."),
    ("sidebar-border", "--sidebar-border", "border", "The #e4e4e7 sidebar hairline."),
]:
    if n in R:
        sem.setdefault(group, {})[key] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)

# ------------------------------------------------- measured color corrections

# A few measured tones are the Curater-namespace roles the vars name;
# alias them instead of duplicating literals.
def alias_value(alias):
    """The resolved value of a {color.curater.*} alias, from raw/css-vars.json."""
    name = "--Curater-" + alias.strip("{}").split(".")[-1]
    v = (V.get("resolved", {}).get("light") or {}).get(name)
    v = v.get("value") if isinstance(v, dict) else v
    return norm_color(v) if v else None


for key, comp, state, prop, alias, desc in [
    ("secondary-text", "login-btn", "default", "color", "{color.curater.gray-medium}",
     "The #7c7c7c 'Log in or sign up' label — Curater gray-medium."),
    ("label", "curated-label", "default", "color", "{color.curater.gray-light}",
     "The #afafaf 'Curated by' micro-label — Curater gray-light."),
    ("hover-fill", "signin-btn", "hover", "backgroundColor", "{color.curater.background}",
     "The #f2f2f2 hover/active fill — Curater background."),
]:
    if not have(comp, state, prop):
        continue
    reading = norm_color(st(comp, state)[prop])
    # Emit the alias only when the reading really equals its target; the source names the state read.
    if reading != alias_value(alias):
        continue
    sem.setdefault("text" if "text" in key or key == "label" else "background", {})[key] = {
        "value": alias, "type": "color",
        "source": f"computed {prop} of {comp} {state} equals {alias} (raw/components-computed.json + raw/css-vars.json)",
        "description": desc}

# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, n, comp, desc in [
    ("title", "--text-2xl", "title-link", "The 24px item/curation title."),
    ("body", "--text-base", "nav-button", "The 16px base size."),
    ("field", "--text-sm", "search-field", "The 14px field/meta size."),
    ("label", "--text-xs", "save-btn", "The 12px chip/label size."),
    ("teaser", "--text-xl", "taste-desc", "The 20px TasteScope teaser."),
]:
    if n in R:
        ty[key] = var(n, "fontSize",
            source=f"css-var {n} resolved (raw/css-vars.json)",
            description=desc + f" Declared {n}.")
    elif comp in C and ts(comp, "default", "fontSize"):
        ty[key] = {"value": ts(comp, "default", "fontSize"), "type": "fontSize",
                   "source": f"computed fontSize of {comp} default (raw/components-computed.json)",
                   "description": desc}
for key, n, desc in [
    ("lg", "--text-lg", "The 18px step."),
    ("xl", "--text-xl", "The 20px step."),
    ("3xl", "--text-3xl", "The 30px step."),
    ("4xl", "--text-4xl", "The 36px step."),
    ("5xl", "--text-5xl", "The 48px step."),
]:
    if n in R:
        ty[key] = var(n, "fontSize",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)

# ------------------------------------------------------------------ shape

radii = SPEC["core"].setdefault("radius", {})
for key, n, comp, prop, desc in [
    ("pill", "--radius-full", "signin-btn", "borderTopLeftRadius", "The 9999px pill (CTAs, chips, nav icons, item menu)."),
    ("card", "--radius-2xl", "trend-card", "borderTopLeftRadius", "The 24px trend-card radius (declared --radius-2xl is 20px; the card computes 24px)."),
    ("lg", "--radius-lg", None, None, "The declared 12px radius."),
    ("md", "--radius-md", None, None, "The declared 8px radius."),
    ("sm", "--radius-sm", None, None, "The declared 6px radius."),
    ("base", "--radius", None, None, "The declared 10px base radius."),
    ("xl", "--radius-xl", None, None, "The declared 16px radius."),
]:
    if comp and have(comp, "default", prop):
        v = st(comp, "default")[prop]
        radii[key] = lit(v, "dimension",
            f"computed {prop} of {comp} default (raw/components-computed.json)", desc)
    elif n and n in R:
        radii[key] = var(n, "dimension",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)

# ------------------------------------------------------------- elevation

sh = SPEC["core"].setdefault("shadow", {})
for key, n, desc in [
    ("sm", "--shadow-sm", "The 1px/2px 5% card shadow on pills."),
    ("md", "--shadow-md", "The 4px/6px 10% shadow."),
    ("xl", "--shadow-xl", "The paired 2px/4px + wide shadow."),
]:
    if n in R:
        sh[key] = {"value": R[n], "type": "other",
                   "source": f"css-var {n} resolved (raw/css-vars.json)", "description": desc}
try:
    sh["card-lift"] = lit(st("trend-card", "default")["boxShadow"], "other",
        "computed boxShadow of trend-card default (raw/components-computed.json)",
        "The trend card's soft lift: rgba(0,0,0,0.02) 0 14px 54px.")
except KeyError:
    pass

# ---------------------------------------------------------------- spacing

sp = SPEC["core"].setdefault("spacing", {})
for n in sorted(R):
    if re.fullmatch(r"--space-\d+", n):
        sp[n[len("--space-"):]] = var(n, "dimension",
            source=f"css-var {n} resolved (raw/css-vars.json)",
            description=f"The {n} step (4px base).")
for key, n, desc in [
    ("unit", "--spacing", "The 4px spacing unit."),
    ("curation-detail", "--spacing-curation-detail", "The 56px detail-pane spacing."),
    ("header-h", "--header-height", "The 56px header."),
    ("mobile-bar-h", "--mobile-bar-height", "The 56px mobile bar."),
    ("sidebar-w", "--sidebar-width", "The 80px sidebar."),
    ("content-w", "--centered-content-width", "The 480px centred column."),
]:
    if n in R:
        sp[key] = var(n, "dimension",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)

# ----------------------------------------------------------------- motion

mo = SPEC["core"].setdefault("motion", {})
for key, n, desc in [
    ("fast", "--transition-fast", ".15s expo-out."),
    ("normal", "--transition-normal", ".2s expo-out."),
    ("slow", "--transition-slow", ".3s expo-out."),
    ("slower", "--transition-slower", ".5s expo-out."),
    ("ease-expo", "--ease-out-expo", "cubic-bezier(.19,1,.22,1)."),
    ("default-duration", "--default-transition-duration", "The 0.15s Tailwind default."),
    ("default-easing", "--default-transition-timing-function", "The default easing."),
]:
    if n in R:
        mo[key] = var(n, "other",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)

lz = SPEC["core"].setdefault("layout", {})
for n in sorted(R):
    if n.startswith("--z-") and n != "--z-base":
        lz[n[len("--z-"):]] = var(n, "other",
            source=f"css-var {n} resolved (raw/css-vars.json)",
            description=f"Z-index layer {n}.")

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, prop, ty_, desc in [
    ("nav-rail-height", "nav-rail", "h", "dimension", "The 328px desktop nav rail."),
    ("nav-button", "nav-button", "h", "dimension", "The 48px round nav button."),
    ("nav-active-fill", "nav-button-active", "bg", "color", "The #f2f2f2 active nav fill."),
    ("signin-height", "signin-btn", "h", "dimension", "The 58px sign-in pill."),
    ("signin-width", "signin-btn", "w", "dimension", "The ~259px sign-in pill width."),
    ("signin-fill", "signin-btn", "bg", "color", "The white pill fill."),
    ("save-height", "save-btn", "h", "dimension", "The 28px Save chip."),
    ("search-width", "search-field", "w", "dimension", "The 170px revealed search field."),
    ("tab-height", "tab-button", "h", "dimension", "The 40px feed tab."),
    ("theme-card", "theme-card", "h", "dimension", "The 271px theme tile."),
    ("trend-card", "trend-card", "h", "dimension", "The ~492px trend card."),
    ("trend-card-radius", "trend-card", "borderTopLeftRadius", "dimension", "The 24px trend-card radius."),
    ("curation-heading", "curation-heading", "w", "dimension", "The ~350px detail heading column."),
    ("sso-width", "sso-btn", "w", "dimension", "The 350px Google SSO button."),
    ("back-button", "back-btn", "h", "dimension", "The 36px back control."),
    ("options-button", "options-btn", "h", "dimension", "The 32px options control."),
    ("tastescope-height", "tastescope-btn", "h", "dimension", "The ~42px TasteScope header button."),
    ("profile-item", "profile-item", "h", "dimension", "The ~380px profile item tile."),
    ("item-menu", "item-menu", "h", "dimension", "The 28px item menu button."),
    ("m-nav-bar", "m-nav-rail", "h", "dimension", "The 40px mobile nav bar."),
    ("m-nav-button", "m-nav-button", "h", "dimension", "The 40px mobile nav button."),
    ("taste-panel", "taste-desc", "w", "dimension", "The 256px TasteScope teaser column."),
    ("taste-canvas", "taste-canvas", "w", "dimension", "The 1360px BrandGlobe canvas."),
]:
    try:
        s = C[cname]["states"]["default"]
        if prop in ("w", "h"):
            v = s["rect"][prop]
        elif prop == "bg":
            v = s["style"]["backgroundColor"]
        else:
            v = s["style"][prop]
        if v and v not in ("0px", "auto", "rgba(0, 0, 0, 0)"):
            comp[name] = lit(v, ty_,
                f"computed {prop} of {cname} default (raw/components-computed.json)", desc)
    except KeyError:
        pass
# measured state moves on the interactive controls
for name, cname, desc in [
    ("button-state-track", "signin-btn",
     "Sign-in pill: white at rest, #f2f2f2 on hover, sinks 2px (translateY) when pressed; 2px #d4d4d8 focus ring."),
    ("icon-state-track", "nav-button",
     "Nav icon: transparent at rest, #f4f4f5 fill + ink on hover/pressed; the active page's icon keeps the #f2f2f2 fill."),
]:
    try:
        comp.setdefault("state-track", {})[name] = {
            "type": "other",
            "value": {s2: {p: st(cname, s2)[p] for p in ("backgroundColor", "color", "transform") if st(cname, s2).get(p)}
                      for s2 in ("default", "hover", "pressed") if s2 in C[cname]["states"]},
            "source": f"computed styles of {cname} default/hover/pressed (raw/components-computed.json)",
            "description": desc}
    except KeyError:
        pass
# the shared focus ring
try:
    comp["focus-ring"] = lit(
        f"{st('save-btn', 'focus-visible')['outlineWidth']} {st('save-btn', 'focus-visible')['outlineStyle']} {st('save-btn', 'focus-visible')['outlineColor']} offset {st('save-btn', 'focus-visible')['outlineOffset']}",
        "other",
        "computed outline of save-btn focus-visible (raw/components-computed.json)",
        "2px solid #d4d4d8 (--ring), 2px offset — identical on every measured control.")
except KeyError:
    pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print("component-tokens.json:", {k: count(v) for k, v in SPEC.items() if isinstance(v, dict)})
