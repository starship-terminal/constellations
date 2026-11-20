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


def norm_color(v):
    v = (v or "").strip()
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
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
fam["sans"] = var("--sans-serif-font", "fontFamily",
    source="css-var --sans-serif-font resolved (raw/css-vars.json); every measured component computes Helvetica Neue",
    description="Helvetica Neue, Helvetica, Arial, sans-serif — every surface.")
weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, desc in [
    ("regular", "post-body", "Measured 400 — body copy."),
    ("medium", "nav-link", "Measured 500 — nav, links, buttons."),
    ("bold", "hero-h1", "Measured 700 — headings, the wordmark weight."),
]:
    if have(comp, "default", "fontWeight"):
        weights[key] = {"value": st(comp, "default")["fontWeight"], "type": "fontWeight",
                        "source": f"computed fontWeight of {comp} default (raw/components-computed.json)",
                        "description": desc}

# ------------------------------------------------------- declared palettes

col = SPEC["core"].setdefault("color", {})
gray = col.setdefault("gray", {})
for n in sorted(R):
    if re.fullmatch(r"--gray\d+", n):
        gray[n[6:]] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)",
            description=f"The {n} neutral step.")
brand = col.setdefault("brand", {})
for key, n, ty_, desc in [
    ("chronos", "--chronos", "color", "The #ff4700 brand orange — Sign up fill, every link on the content pages."),
    ("chronos-gradient", "--chronos-gradient", "other", "The declared linear-gradient(#fa6c38, #f44e25) brand gradient."),
    ("primary-100", "--primary100", "color", "The #ffcdb3 light orange step."),
    ("primary-700", "--primary700", "color", "The #ca3800 dark orange step."),
]:
    if n in R:
        brand[key] = var(n, ty_,
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)
named = col.setdefault("named", {})
for key, n, desc in [
    ("eclipse", "--eclipse", "#000000 — the named black."),
    ("snow", "--snow", "#ffffff — the named white."),
    ("dieter", "--dieter", "#eeeeee — the named light fill."),
    ("urushi", "--urushi", "#282828 — the named dark fill."),
]:
    if n in R:
        named[key] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)
semantic = col.setdefault("semantic", {})
for key, n, desc in [
    ("red-100", "--semantic-red100", "Declared #f8c4c7 light red."),
    ("red-500", "--semantic-red500", "Declared #ed4556 red."),
]:
    if n in R:
        semantic[key] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)

# ----------------------------------------------------- semantic (content pages)

sem = SPEC["light"].setdefault("color", {})
for key, n, group, desc in [
    ("page", "--snow", "background", "The white content-page fill."),
    ("text", "--text-default", "text", "The #1a1a1a body text."),
    ("meta", "--ratio", "text", "The #616161 meta/date text."),
    ("accent", "--chronos", "action", "The #ff4700 link/action orange."),
    ("object", "--object-default", "text", "The #999 object/icon tone."),
    ("object-highlight", "--object-highlight-bg", "background", "The #ededed highlighted object fill."),
    ("border", "--object-border", "border", "The #e5e5e5 object border."),
    ("material", "--material-default", "background", "The #fff material surface."),
]:
    if n in R:
        sem.setdefault(group, {})[key] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)

# --------------------------------------------------------- dark home (measured)

dsem = SPEC["dark"].setdefault("color", {})
for key, comp, prop, group, desc in [
    ("page", "m-menu-open", "backgroundColor", "background", "The #161412 dark page fill (also the banner's)."),
    ("footer", "footer", "backgroundColor", "background", "The #0f0d0a footer band."),
    ("text", "site-header", "color", "text", "The #ccc body text on dark."),
    ("strong", "nav-link", "color", "text", "The #fff strong text/links on dark."),
    ("accent", "signup-btn", "backgroundColor", "action", "The #ff4700 Sign up / accent fill on dark."),
    ("on-accent", "signup-btn", "color", "text", "White text on the orange fill."),
]:
    try:
        v = st(comp, "default")[prop]
        dsem.setdefault(group, {})[key] = lit(v, "color",
            f"computed {prop} of {comp} default (raw/components-computed.json)", desc)
    except KeyError:
        pass

# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, desc in [
    ("display", "hero-h1", "The 140px home hero (-3px tracking, 90% leading)."),
    ("m-display", "m-heading", "The 80px mobile hero."),
    ("h1", "blog-h1", "The 40px index heading (blog/changelog)."),
    ("post-h1", "post-h1", "The 32px article title."),
    ("h2", "feature-h2", "The 24px feature title."),
    ("body", "hero-sub", "The 22px home body size."),
    ("content", "post-body", "The 16px content-page body size."),
    ("nav", "nav-link", "The 22px nav link size."),
    ("footer", "footer-link", "The 13px footer size."),
]:
    v = ts(comp, "default", "fontSize") if comp in C else None
    if v:
        ty[key] = {"value": v, "type": "fontSize",
                   "source": f"computed fontSize of {comp} default (raw/components-computed.json)",
                   "description": desc}
try:
    ty["display-lh"] = lit(st("hero-h1", "default")["lineHeight"], "other",
        "computed lineHeight of hero-h1 default (raw/components-computed.json)",
        "The hero's 90% line-height.")
    ty["display-ls"] = lit(st("hero-h1", "default")["letterSpacing"], "other",
        "computed letterSpacing of hero-h1 default (raw/components-computed.json)",
        "The hero's -3px tracking.")
except KeyError:
    pass

# ------------------------------------------------------------------ shape

radii = SPEC["core"].setdefault("radius", {})
for key, comp, prop, desc in [
    ("pill", "signup-btn", "borderTopLeftRadius", "The 9999px pill (Sign up, integration chips)."),
    ("banner", "banner", "borderTopLeftRadius", "The 4px banner radius."),

]:
    if have(comp, "default", prop):
        v = st(comp, "default")[prop]
        # %g keeps a fractional radius (int() truncated 2.5px to 2px); a computed rounded-full above
        # 9999px is written 9999px, the kit's pill.
        try:
            n = float(v[:-2]) if v.endswith("px") else None
        except ValueError:
            n = None
        fv = ("9999px" if n > 9999 else "%gpx" % n) if n is not None else v
        radii[key] = lit(fv, "dimension",
            f"computed {prop} of {comp} default (raw/components-computed.json)", desc)

# ------------------------------------------------------------- elevation

sh = SPEC["core"].setdefault("shadow", {})
for key, n, desc in [
    ("low", "--elevation-low", "The declared low elevation."),
    ("high", "--elevation-high", "The declared high elevation."),
]:
    if n in R:
        sh[key] = {"value": R[n], "type": "other",
                   "source": f"css-var {n} resolved (raw/css-vars.json)", "description": desc}
# the declared glow pair lives on .primary-link-button.glow in the app bin
for e in V.get("app", []):
    if "glow" not in e.get("selector", ""):
        continue
    for p, v in e.get("properties", {}).items():
        k = "glow" if p == "--glow" else "glow-hover" if p == "--glow-hover" else None
        if k:
            sh[k] = {"value": v, "type": "other",
                     "source": f"css-var {p} declared on {e['selector']} (raw/css-vars.json)",
                     "description": "The Sign up pill's orange glow — 0 0 100px 20% at rest, 0 0 25px 40% on hover."}
try:
    sh["banner"] = {"value": st("banner", "default")["boxShadow"], "type": "other",
                    "source": "computed boxShadow of banner default (raw/components-computed.json)",
                    "description": "The rebrand banner's inset 0.5px orange ring + 28px 20% glow."}
except KeyError:
    pass

# ---------------------------------------------------------------- spacing

sp = SPEC["core"].setdefault("spacing", {})
for key, comp, prop, val, desc in [
    ("header-h", "site-header", None, None, "The 120px desktop header."),
    ("content-max", None, None, "1000px", "The .content max-width (1000px; 800px under 1000px viewport)."),
    ("entry-w", "post-entry", None, None, "The 676px article column width."),
    ("footer-h", "footer", None, None, "The 180px footer."),
]:
    if comp and have(comp, "default") and key.endswith("-w"):
        sp[key] = lit(rc(comp, "default", "w"), "dimension",
            f"computed rect width of {comp} default (raw/components-computed.json)", desc)
    elif comp and have(comp, "default"):
        sp[key] = lit(rc(comp, "default", "h"), "dimension",
            f"computed rect height of {comp} default (raw/components-computed.json)", desc)
    elif comp is None:
        sp[key] = lit(val, "dimension",
            "Reconstruction: entered by hand at capture time; raw/css-vars.json holds no .content max-width rule", desc)
    else:
        w = rc(comp, "default", "w")
        sp[key] = lit(w, "dimension",
            f"computed rect width of {comp} default (raw/components-computed.json)", desc)

# ----------------------------------------------------------------- motion

mo = SPEC["core"].setdefault("motion", {})
if "--animation-duration-default" in R:
    mo["duration"] = var("--animation-duration-default", "other",
        source="css-var --animation-duration-default resolved (raw/css-vars.json)",
        description="The declared 0.175s default duration (Sign up glow, banner shadow).")
if "--disabled-opacity" in R:
    mo.setdefault("_", {})
    SPEC["core"].setdefault("opacity", {})["disabled"] = var("--disabled-opacity", "other",
        source="css-var --disabled-opacity resolved (raw/css-vars.json)",
        description="The declared 0.33 disabled opacity.")
if "--z-index-popover" in R:
    SPEC["core"].setdefault("layout", {})["z-popover"] = var("--z-index-popover", "other",
        source="css-var --z-index-popover resolved (raw/css-vars.json)",
        description="The declared popover z-index (10).")

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, prop, ty_, desc in [
    ("header-height", "site-header", "h", "dimension", "The 120px desktop header."),
    ("logotype-height", "logotype", "h", "dimension", "The 40px logotype."),
    ("signup-height", "signup-btn", "h", "dimension", "The 46px Sign up pill."),
    ("signup-fill", "signup-btn", "bg", "color", "The #ff4700 Sign up fill."),
    ("banner-height", "banner", "h", "dimension", "The 44-45px rebrand banner."),
    ("banner-fill", "banner", "bg", "color", "The #161412 banner fill."),
    ("hero-size", "hero-h1", "fontSize", "fontSize", "The 140px hero."),
    ("entry-width", "post-entry", "w", "dimension", "The 676px article column."),
    ("footer-height", "footer", "h", "dimension", "The 180px footer."),
    ("m-header-height", "m-header", "h", "dimension", "The ~96px mobile header."),
    ("m-menu-height", "m-menu-open", "h", "dimension", "The 736px opened nav overlay."),
    ("m-signup-width", "m-signup-btn", "w", "dimension", "The ~342px full-width mobile Sign up."),
    ("nav-link-size", "nav-link", "fontSize", "fontSize", "Nav link 22px."),

]:
    try:
        s = C[cname]["states"]["default"]
        if prop in ("w", "h"):
            v = s["rect"][prop]
        else:
            v = s["style"][prop]
        if v and v not in ("0px", "auto"):
            comp[name] = lit(v, ty_,
                f"computed {prop} of {cname} default (raw/components-computed.json)", desc)
    except KeyError:
        pass
# measured state move: the Sign up glow track
try:
    comp.setdefault("button", {})["signup-glow"] = {
        "type": "other",
        "value": {s2: {"boxShadow": st("signup-btn", s2)["boxShadow"]}
                  for s2 in ("default", "hover", "pressed") if s2 in C["signup-btn"]["states"]},
        "source": "computed boxShadow of signup-btn default/hover/pressed (raw/components-computed.json)",
        "description": "The Sign up pill's glow track: 0 0 100px 20% orange at rest, tightening to 0 0 25px 40% on hover."}
except KeyError:
    pass
# Emit the alias only when its target exists, so a missed --ratio never leaves a dangling alias.
if "meta" in SPEC["light"].get("color", {}).get("text", {}):
    comp["meta-color"] = {"value": "{color.text.meta}", "type": "color",
        "source": "alias of color.text.meta (the declared --ratio #616161)",
        "description": "The #616161 meta/date tone — the entries' dates render it; the post-meta element itself computed #000."}

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print("component-tokens.json:", {k: count(v) for k, v in SPEC.items() if isinstance(v, dict)})
