#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

fourmula.ai signed out is two surfaces that share no token layer:

  fourmula.ai — a Webflow marketing site with TWO painted themes driven by
  a header toggle that writes localStorage `isDarkMode` and flips a `dark`
  class on <body>. The class names are inverted against the paint:
  `.body.dark` paints the light surface (white --mainbg, the first-visit
  default) and plain `.body` paints the dark surface (--mainbg #020108).
  Its declared layer (raw/css-vars.json) is small and honest: a fluid-rem
  type ramp (--_fonts---*, resolved by the browser to fractional px at
  1440), the Sf Pro Display family, a five-step alpha ink ramp
  (--fonts-20/30/50/64/100) and the theme colours (--mainbg, --secondbg,
  --lines, --menu, --menu-colors, --dots-pattern, --mainbg-gradient), plus
  the --user-zoom fluid-scale factor. The themed vars are emitted as
  {var} leaves so build_tokens.py resolves them per set; the painted
  geometry and control values are measured literals from
  raw/components-computed.json.

  app.fourmula.ai — a separate dark-only Next.js/Tailwind v4 app
  (/start, /auth, /project/create-pdp are reachable signed out). Its
  @theme layer (raw/css-vars-app.json) is a real token ramp: --color-base-*
  neutrals, --color-accent-500 #ff6b02 orange, --text-* sizes 9–52px,
  --radius-* 4–40px, --spacing 4px, --ease-*, --blur-*, --container-*.
  Its declared values land under core.appColor / core.font.size.app /
  core.radius.app etc. resolved in this builder (the app resolves
  identically on either probe paint — it ships dark only), and its
  measured geometry/roles land under component.app.*.

Measured structure (desktop 1440 x 900 at 1x, mobile 390 x 844 at 2x):

  fonts   "Sf Pro Display", Arial on marketing headings; sfProFont +
  "sfProFont Fallback" (a local next/font face) everywhere in the app;
  chrome wrappers fall back to Arial/system sans
  ramp    marketing is fluid-rem — the declared ramp resolves to
  7.37–88.59px at 1440 and the page paints 73.2px hero / 99.8px section
  headings (the fluid scale reads wider than the declared step); mobile
  shrinks to 40.3px hero; the app is a fixed 9–52px declared ramp
  colour  marketing inverts: light paint is ink #020108 on #fff with
  #020108-filled CTAs, dark paint is white on #020108 with white-filled
  CTAs; the app is dark-only — #ff6b02 accent on a #111–#1e1e1e base
  stack, accent/20% translucent fills (painted oklab) for secondary pills
  shape   marketing spells pills as fluid ~1318px radii, chips 6.65px,
  the account icon 26.6px; the app spells full pills as Tailwind's
  rounded-full (serialised 3.35544e+07px), cards/dialogs 28px
  (rounded-4xl), the format radios 16px, the footer submit 12px
  motion  marketing controls transition over 0.2s ease; the app declares
  0.15s cubic-bezier(0.4,0,0.2,1) as --default-transition-*; measured
  motion is in raw/motion.json -> core.motion via motion.py
"""

import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
VA = json.loads((RAW / "css-vars-app.json").read_text())
RL = V.get("resolved", {}).get("light", {})
RD = V.get("resolved", {}).get("dark", {})
RA = VA.get("resolved", {}).get("dark", VA.get("resolved", {}).get("light", {}))
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}
D = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RD.items()}
A = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RA.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. fourmula.ai's "
    "marketing layer declares a small Webflow variable set (fluid --_fonts---* "
    "sizes, the --fonts-* alpha ink ramp, themed --mainbg/--secondbg/--lines/"
    "--menu* colours) which lands as {var} leaves resolved per theme; "
    ".body.dark paints light and plain .body paints dark, so `light` resolves "
    "the .body.dark declarations and `dark` the .body ones. Painted control "
    "colours and all geometry are measured literals. The dark-only "
    "app.fourmula.ai Tailwind theme (--color-*, --text-*, --radius-*, "
    "--spacing, --ease-*, --blur-*) lands under core.* as literals resolved "
    "from raw/css-vars-app.json; its measured surfaces live under "
    "component.app.*."),
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


def lin(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def oklab_rgb(L, a, b):
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    rgb = [4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
           -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s]
    return [round(min(1, max(0, lin(x))) * 255) for x in rgb]


def oklch_rgb(L, c, h):
    import math
    a = c * math.cos(math.radians(h))
    b = c * math.sin(math.radians(h))
    return oklab_rgb(L, a, b)


def norm_color(v):
    """A computed colour -> '#rrggbb' or 'rgba(r, g, b, a)'. oklab()/oklch() are
    converted to the sRGB the browser paints (Tailwind v4 alpha utilities like
    bg-accent-500/20 serialise as oklab)."""
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8:
            a = int(h[6:8], 16) / 255
            return "#" + h[:6] if a >= 1 else "rgba(%d, %d, %d, %s)" % (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), "%g" % round(a, 3))
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    m = re.fullmatch(r"rgba?\(([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*(?:/\s*([\d.]+%?))?\)", v)
    if m:
        r, g, b, a = m.groups()
        a = 1 if a is None else (float(a[:-1]) / 100 if a.endswith("%") else float(a))
        if a >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % round(a, 3)})"
    m = re.fullmatch(r"oklab\(([-\d.e]+)\s+([-\d.e]+)\s+([-\d.e]+)\s*(?:/\s*([\d.]+%?))?\)", v)
    if m:
        L, a, b, al = m.groups()
        al = 1 if al is None else (float(al[:-1]) / 100 if al.endswith("%") else float(al))
        r, g, b2 = oklab_rgb(float(L), float(a), float(b))
        if al >= 1:
            return "#%02x%02x%02x" % (r, g, b2)
        return "rgba(%d, %d, %d, %s)" % (r, g, b2, "%g" % round(al, 3))
    m = re.fullmatch(r"oklch\(([-\d.e]+%?)\s+([-\d.e]+)\s+([-\d.e]+)\s*(?:/\s*([\d.]+%?))?\)", v)
    if m:
        L, c, h, al = m.groups()
        L = float(L[:-1]) / 100 if L.endswith("%") else float(L)
        al = 1 if al is None else (float(al[:-1]) / 100 if al.endswith("%") else float(al))
        r, g, b2 = oklch_rgb(L, float(c), float(h))
        if al >= 1:
            return "#%02x%02x%02x" % (r, g, b2)
        return "rgba(%d, %d, %d, %s)" % (r, g, b2, "%g" % round(al, 3))
    return v


def lit(value, ty, src, desc):
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


DECL_SRC = "declared custom property in the marketing site's Webflow css bundle (raw/css-vars.json)"
APP_SRC = "declared custom property in the app's Tailwind v4 @theme layer (raw/css-vars-app.json)"


def declared(name):
    v = R.get(name)
    return v if v not in (None, "") else None


def appdecl(name):
    v = A.get(name)
    return v if v not in (None, "") else None


def norm_len(v):
    m = re.fullmatch(r"(-?[\d.]+[eE][+-]?\d+)(px|rem)", str(v).strip())
    if not m:
        return v
    f = float(m.group(1))
    return ("%g" % (f if f <= 1e7 else 9999)) + m.group(2)


def decl(name, ty="dimension"):
    v = declared(name)
    desc = f"The declared `{name}`."
    if ty == "dimension":
        nv = norm_len(v)
        if nv != v:
            raw = (RL.get(name) or {}).get("raw")
            desc = f"The declared `{name}` — `{raw}`, which Chromium resolves to {nv}."
            v = nv
        if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(v).strip()):
            ty = "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", desc)


def adecl(name, ty="dimension"):
    """A declared app (@theme) value, resolved on the app's own probe paint —
    the app ships one dark theme, so light and dark resolve identically."""
    v = appdecl(name)
    desc = f"The app's declared `{name}`."
    if ty == "dimension":
        nv = norm_len(v)
        if nv != v:
            desc = f"The app's declared `{name}` — `{v}`, which serialises as {nv} (Tailwind's full-pill sentinel)."
            v = nv
        if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(v).strip()):
            ty = "other"
    return lit(v, ty, f"{APP_SRC}: {name}", desc)


def aratio(name):
    """A declared app line-height written calc(a/b) -> the ratio."""
    v = appdecl(name)
    m = re.fullmatch(r"calc\(\s*(-?\d*\.?\d+)\s*/\s*(-?\d*\.?\d+)\s*\)", str(v))
    if m:
        return lit(round(float(m.group(1)) / float(m.group(2)), 4), "number",
                   f"{APP_SRC}: {name}", f"The app's declared `{name}` line-height ratio.")
    return adecl(name, "other")


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\)|color\([^)]*\))")


def decl_color(name):
    v = declared(name)
    ty = "color" if COLOR_V.fullmatch(str(v).strip()) else "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


def adecl_color(name):
    v = appdecl(name)
    ty = "color" if COLOR_V.fullmatch(str(v).strip()) else "other"
    return lit(v, ty, f"{APP_SRC}: {name}", f"The app's declared `{name}`.")


def msrc(comp, state, prop, extra=""):
    return f"computed {prop} of {comp} {state} (raw/components-computed.json){extra}"


# ------------------------------------------------------------------- fonts
#
# Marketing headings paint "Sf Pro Display", Arial (declared
# --_font-family---font-family). The app ships a local next/font face that
# serialises as sfProFont, "sfProFont Fallback". Wrapper chrome falls back
# to Arial on the marketing site — the honest reading.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
if declared("--_font-family---font-family"):
    fam["marketing"] = var("--_font-family---font-family", "fontFamily",
                           description="The declared marketing face: \"Sf Pro Display\", Arial, sans-serif — headings, buttons and nav paint it; plain wrapper chrome falls back to Arial.")
try:
    fam["app"] = lit(st("app-menu-btn", "default")["fontFamily"], "fontFamily",
                     "computed fontFamily of app-menu-btn default on app.fourmula.ai (raw/components-computed.json); the local next/font face the app's @theme layer declares",
                     "The app's SF Pro face, served as the local sfProFont family with its metrics fallback.")
except KeyError:
    pass
if appdecl("--font-sans"):
    fam["appSystem"] = adecl("--font-sans", "fontFamily")
    fam["appSystem"]["description"] = "The app's declared --font-sans — the Tailwind default stack behind the local sfProFont face."

weights = SPEC["core"]["font"].setdefault("weight", {})
if declared("--_font-family---regular"):
    weights["regular"] = var("--_font-family---regular", "fontWeight",
                             description="The declared marketing regular (400).")
if declared("--_font-family---medium"):
    weights["medium"] = var("--_font-family---medium", "fontWeight",
                            description="The declared marketing medium (500) — nav overlay links, legal titles, the app's /start heading and medium-weight buttons paint it.")

# ------------------------------------------------------------- type ramp
#
# The marketing --_fonts---* ramp is fluid: the rem declarations resolve
# through the site's own rem scaling, so the resolved px at the 1440x900
# capture viewport differs from the round declared rem figures — the 73.2px
# hero IS the resolved h1 step at this width. An earlier pass resolved the
# vars at Playwright's 1280x720 default and tokenized a 64.97px h1 the page
# never paints at 1440; vars.mjs now probes at the capture viewport.
# Declared steps are var leaves; painted sizes are measured literals under
# measured.

sizes = SPEC["core"]["font"].setdefault("size", {})
mkt = sizes.setdefault("marketing", {})
for name, key, desc in [
    ("--_fonts---h1", "h1", "The declared marketing h1 step (resolved fluid-rem at 1440)."),
    ("--_fonts---h2", "h2", "The declared marketing h2 step."),
    ("--_fonts---h2-5", "h2-5", "The declared marketing h2-5 step."),
    ("--_fonts---h3", "h3", "The declared marketing h3 step."),
    ("--_fonts---h4", "h4", "The declared marketing h4 step."),
    ("--_fonts---body-1", "body1", "The declared body-1 step."),
    ("--_fonts---body-2", "body2", "The declared body-2 step."),
    ("--_fonts---body-3", "body3", "The declared body-3 step."),
    ("--_fonts---btn", "button", "The declared button step."),
    ("--_fonts---title-1", "title1", "The declared title-1 step."),
    ("--_fonts---title-2", "title2", "The declared title-2 step."),
    ("--_fonts---title-3", "title3", "The declared title-3 step."),
    ("--_fonts---tag", "tag", "The declared tag step."),
    ("--_fonts---tag-small", "tagSmall", "The declared small tag step."),
    ("--_fonts---small-text-1", "smallText1", "The declared small-text-1 step."),
    ("--_fonts---small-text-2", "smallText2", "The declared small-text-2 step."),
]:
    if declared(name):
        leaf = var(name, "dimension", description=desc)
        # The resolved px at 1440 is the light-theme probe answer; the same
        # declarations shrink under the <=991px/<=767px media rules recorded
        # in raw/css-vars.json, so the token names what 1440 paints.
        mkt[key] = leaf

app_sizes = sizes.setdefault("app", {})
for name in sorted(k for k in A if re.fullmatch(r"--text-(2xs|xs|sm|md|m|lg|l|xl|2lg|2xl)", k)):
    app_sizes[name[len("--text-"):]] = adecl(name)

measured_sizes = sizes.setdefault("measured", {})
for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The 73.2px painted hero masthead at 1440 — the resolved --_fonts---h1 step at the capture width."),
    ("section", "section-h2", "default", "The 99.8px painted section heading at 1440."),
    ("step", "step-h3", "default", "The 53.2px how-it-works step heading."),
    ("legal", "legal-title", "default", "The 73.2px legal page title."),
    ("navOverlay", "nav-overlay-link", "default", "The 20px menu-overlay link."),
    ("control", "header-cta", "default", "The 14.1px marketing button size."),
    ("chrome", "mkt-header", "default", "The 14.4px default on header chrome (Arial fallback zone)."),
    ("bodyLegal", "legal-body", "default", "The 15px legal body size."),
    ("heroMobile", "m-hero-h1", "default", "The 40.3px mobile hero masthead at 390 wide."),
    ("controlMobile", "m-step-cta", "default", "The 17.1px mobile button size."),
    ("appDisplay", "start-h1", "default", "The app's 52px /start heading (--text-2xl)."),
    ("appControl", "app-create-btn", "default", "The app's 14px control size (--text-sm)."),
    ("appMeta", "auth-forgot", "default", "The app's 12px meta size (--text-xs)."),
]:
    try:
        raw = st(comp, state)["fontSize"]
        measured_sizes[key] = lit(raw, "dimension", msrc(comp, state, "fontSize"), desc)
    except KeyError:
        pass

lineheights = SPEC["core"]["font"].setdefault("lineHeight", {})
for name in sorted(k for k in A if re.fullmatch(r"--text-(2xl|xl|lg|sm|xs)--line-height", k)):
    lineheights["app" + name[len("--text-"):].replace("--line-height", "").title().replace("x", "X")] = aratio(name)
for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The 68.8px hero line-height (~0.94)."),
    ("section", "section-h2", "default", "The 99.8px section line-height (1:1)."),
    ("control", "header-cta", "default", "The 17px button line-height."),
    ("navOverlay", "nav-overlay-link", "default", "The 29.9px overlay-link line-height."),
]:
    try:
        lineheights[key] = lit(st(comp, state)["lineHeight"], "dimension", msrc(comp, state, "lineHeight"), desc)
    except KeyError:
        pass

tracking = SPEC["core"]["font"].setdefault("tracking", {})
for name in sorted(k for k in A if re.fullmatch(r"--tracking-[a-z]+", k)):
    tracking["app" + name[len("--tracking-"):].title()] = adecl(name, "other")
for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The -2.2px hero tracking."),
    ("section", "section-h2", "default", "The -3px section tracking."),
    ("step", "step-h3", "default", "The -1.6px step tracking."),
    ("legal", "legal-title", "default", "The -1.33px legal title tracking."),
    ("navOverlay", "nav-overlay-link", "default", "The -0.17px overlay-link tracking."),
    ("control", "header-cta", "default", "The -0.28px button tracking."),
    ("appDisplay", "start-h1", "default", "The -2.08px (-4%) app display tracking."),
]:
    try:
        tracking[key] = lit(st(comp, state)["letterSpacing"], "other", msrc(comp, state, "letterSpacing"), desc)
    except KeyError:
        pass

# ---------------------------------------------------------- core scales
#
# The app's declared @theme layer — the real Tailwind-v4 token ramp
# (app.fourmula.ai ships dark-only; the values are theme-independent).

appc = SPEC["core"].setdefault("appColor", {})
for name in sorted(k for k in A if re.fullmatch(r"--color-[a-z0-9-]+", k)):
    appc[name[len("--color-"):]] = adecl_color(name)
appc["_note"] = "app.fourmula.ai's declared --color-* ramp: the base-100..900 neutral stack (#fff down to #020108), the #ff6b02 accent, and the semantic steps. Read from raw/css-vars-app.json — a separate layer from the marketing site's Webflow vars."

if appdecl("--spacing"):
    SPEC["core"].setdefault("spacing", {})["app"] = adecl("--spacing")

radii = SPEC["core"].setdefault("radius", {})
app_radii = radii.setdefault("app", {})
for name in sorted(k for k in A if re.fullmatch(r"--radius-(sm|md|lg|xl|2xl|3xl|4xl|5xl|7xl)", k)):
    app_radii[name[len("--radius-"):]] = adecl(name)

containers = SPEC["core"].setdefault("container", {})
for name in sorted(k for k in A if re.fullmatch(r"--container-[a-z0-9]+", k)):
    containers[name[len("--container-"):]] = adecl(name)

blurs = SPEC["core"].setdefault("blur", {})
for name in sorted(k for k in A if re.fullmatch(r"--blur-[a-z0-9]+", k)):
    blurs[name[len("--blur-"):]] = adecl(name)

easing = SPEC["core"].setdefault("easing", {})
for name in sorted(k for k in A if k.startswith("--ease-")):
    easing["app" + name[len("--ease-"):].title().replace("-", "-")] = adecl(name, "cubicBezier")
if appdecl("--default-transition-timing-function"):
    easing["appDefault"] = adecl("--default-transition-timing-function", "cubicBezier")
if appdecl("--default-transition-duration"):
    SPEC["core"].setdefault("duration", {})["appDefault"] = adecl("--default-transition-duration", "duration")
# The marketing control transition: 0.2s ease, measured on the header CTA.
try:
    s = st("header-cta", "default")
    SPEC["core"].setdefault("duration", {})["marketingControl"] = lit(
        s["transitionDuration"], "duration", msrc("header-cta", "default", "transitionDuration"),
        "The 0.2s control transition on the marketing site's buttons and pills.")
    SPEC["core"].setdefault("easing", {})["marketingControl"] = lit(
        s["transitionTimingFunction"], "cubicBezier", msrc("header-cta", "default", "transitionTimingFunction"),
        "The plain `ease` curve on marketing controls.")
except KeyError:
    pass

if appdecl("--animate-pulse"):
    SPEC["core"].setdefault("animate", {})["appPulse"] = adecl("--animate-pulse", "other")

# The marketing hero-slider and dots-field drive variables (the Webflow
# "app" bin of raw/css-vars.json): --tx/--ty rows that translate the hero
# strips and the dots-field grid density.
mkt_app = {}
for rule in V.get("app", []):
    sel = rule.get("selector") or ""
    ctx = " @ ".join(rule.get("context") or [])
    for k, v in (rule.get("properties") or {}).items():
        mkt_app.setdefault(sel + (" <" + ctx + ">" if ctx else ""), {})[k] = v
extra = SPEC["core"].setdefault("heroSlider", {})
for sel_ctx, props in mkt_app.items():
    sel = sel_ctx.split(" <")[0]
    ctx = sel_ctx.split(" <", 1)[1][:-1] if " <" in sel_ctx else ""
    # The media context is part of the value, not a duplicate: the <=991px
    # slider rules are the phone direction (horizontal) and the <=767px dots
    # rules the denser phone grid. They get their own *Mobile keys instead of
    # overwriting the desktop declarations that precede them in the sheet.
    suffix = "Mobile" if "max-width" in ctx else ""
    if "hero__slider__row" in sel:
        for k, v in props.items():
            key = k.replace("--", "").replace("-", "") + suffix
            extra[key] = lit(v, "other", f"{DECL_SRC}: {k} on {sel_ctx}",
                             "The hero logo-strip translate variable (the phone direction under <=991px)." if suffix
                             else "The hero logo-strip translate variable (the desktop direction under >=992px).")
    elif "dots-field" in sel:
        for k, v in props.items():
            key = ("dots" if "dot-" in k else "field") + ("Size" if "size" in k else "Gap") + suffix
            extra[key] = lit(v, "other", f"{DECL_SRC}: {k} on {sel_ctx}",
                             "The dotted-background field's dot/gap size (the denser half-size under 768px)." if suffix
                             else "The dotted-background field's dot/gap size (the desktop grid at >=768px).")

if declared("--user-zoom"):
    SPEC["core"].setdefault("fluid", {})["userZoom"] = decl("--user-zoom", "number")

# ---------------------------------------- measured roles (both paints)
#
# The marketing site's theme colours are declared vars: emitted as {var}
# leaves so light resolves the .body.dark declarations and dark the .body
# ones. The control paint (inverted fills, hairlines, chips) is measured.

for setname, comps, paint in [
    ("light", {"cta": "header-cta", "ctaOnDark": "step-cta", "h1": "hero-h1", "chip": "hero-word",
               "icon": "account-link", "toggle": "theme-toggle", "counter": "prc-counter",
               "ai": "ai-btn", "outline": "cookie-settings", "faq": "faq-item"}, "light (the .body.dark paint)"),
    ("dark", {"cta": "header-cta-dark", "ctaOnDark": "step-cta-dark", "h1": "hero-h1-dark",
              "faq": "faq-item-dark"}, "dark (the plain .body paint)"),
]:
    sem = SPEC[setname]
    for name, key, group, desc in [
        ("--mainbg", "page", "background", "The declared page field."),
        ("--secondbg", "surface", "background", "The declared secondary surface."),
        ("--menu", "menu", "background", "The declared menu/overlay fill — the page ink in light, a lifted #272727 in dark."),
        ("--dots-pattern", "dots", "background", "The declared dots-pattern ink."),
        ("--mainbg-gradient", "pageFade", "background", "The declared transparent page-gradient stop used for fade-outs."),
        ("--fonts-100", "ink", "text", "The declared 100% ink."),
        ("--fonts-64", "muted", "text", "The declared 64% ink."),
        ("--fonts-50", "dim", "text", "The declared 50% ink."),
        ("--fonts-30", "faint", "text", "The declared 30% ink."),
        ("--fonts-20", "hairlineInk", "text", "The declared 20% ink — also the hairline borders paint."),
        ("--lines", "rule", "border", "The declared hairline rule colour (FAQ rows, section dividers)."),
        ("--menu-colors", "menuLine", "border", "The declared overlay hairline (white at 20% in both paints)."),
    ]:
        ty = "color" if group != "other" else "other"
        sem.setdefault(group, {})[key] = var(name, "color", description=desc + f" Resolved under the {paint} declarations.")

    # measured control paint
    for key, ckey, state, prop, group, desc in [
        ("fill", "cta", "default", "backgroundColor", "action", "The painted CTA fill — the page ink in light (#020108), white in dark."),
        ("ink", "cta", "default", "color", "action", "The ink on the filled CTA — the inversion of the page ink."),
        ("fillInverse", "ctaOnDark", "default", "backgroundColor", "action", "The inverse CTA fill on the dark how-it-works band inside the light page (white pill on ink)."),
        ("inkInverse", "ctaOnDark", "default", "color", "action", "The ink on the inverse CTA."),
        ("aiButton", "ai", "default", "backgroundColor", "background", "The white circular AI-button fill on the hero band."),
        ("chip", "chip", "default", "backgroundColor", "background", "The white rotating-word chip in the hero masthead."),
        ("counter", "counter", "default", "backgroundColor", "background", "The translucent header counter chip (white at 20% — the --menu-colors value)."),
        ("outlineFill", "outline", "default", "backgroundColor", "background", "The #d9d9d9 outline-button fill in the consent layer."),
        ("hairline", "chip", "default", "borderTopColor", "border", "The chip/icon hairline — the --fonts-20 ink alpha."),
        ("iconRing", "icon", "default", "borderTopColor", "border", "The account-icon ring border."),
        ("toggleRing", "toggle", "default", "borderTopColor", "border", "The theme-toggle ring border."),
        ("overlayLink", None, None, None, "text", "The menu-overlay link ink (the declared --fonts-100)."),
    ]:
        try:
            if ckey is None:
                sem.setdefault(group, {})[key] = lit("{text.ink}", "color",
                    "the menu overlay links paint the declared --fonts-100 ink (nav-overlay-link color, raw/components-computed.json)", desc)
                continue
            comp = comps.get(ckey)
            if comp is None or comp not in C:
                continue
            raw = st(comp, state)[prop]
            if raw in (None, "", "rgba(0, 0, 0, 0)"):
                continue
            sem.setdefault(group, {})[key] = lit(raw, "color", msrc(comp, state, prop), desc)
        except KeyError:
            pass

# ------------------------------------------------------------- components
#
# Measured geometry: every leaf is the px the page painted at the capture
# viewport, sourced to the component/state it was read from. The marketing
# site scales its rem by viewport, so its radii and paddings are fluid
# values — recorded as painted, not rounded.

comp = SPEC["component"]
mktc = comp.setdefault("marketing", {})
for name, cname, state, prop, ty_, desc in [
    ("header-height", "mkt-header", "default", "h", "dimension", "The 92.5px marketing header band."),
    ("header-side-pad", "mkt-header", "default", "paddingLeft", "dimension", "The header's ~26.6px side padding."),
    ("menu-pill-width", "menu-pill", "default", "w", "dimension", "The ~78px Menu pill width."),
    ("menu-pill-height", "menu-pill", "default", "h", "dimension", "The ~35px header pill height."),
    ("icon-btn", "theme-toggle", "default", "h", "dimension", "The 26.6px square header icon buttons (theme toggle, account)."),
    ("counter-chip", "prc-counter", "default", "h", "dimension", "The 26.6px header counter chip."),
    ("cta-width", "header-cta", "default", "w", "dimension", "The ~102px header CTA width."),
    ("cta-height", "header-cta", "default", "h", "dimension", "The ~39.9px marketing CTA height."),
    ("cta-radius", "header-cta", "default", "borderTopLeftRadius", "dimension", "The fluid ~1318px radius — a full pill at any height."),
    ("ai-btn", "ai-btn", "default", "h", "dimension", "The 53.2px circular hero AI button."),
    ("chip-radius", "hero-word", "default", "borderTopLeftRadius", "dimension", "The 6.65px rotating-word chip radius."),
    ("icon-ring", "account-link", "default", "borderTopLeftRadius", "dimension", "The 26.6px account-icon ring radius."),
    ("hero-h1-width", "hero-h1", "default", "w", "dimension", "The ~485px hero masthead line width."),
    ("nav-overlay-height", "nav-overlay", "opened", "h", "dimension", "The ~529px open menu overlay."),
    ("nav-link-height", "nav-overlay-link", "default", "h", "dimension", "The ~30px menu-overlay link row."),
    ("faq-height", "faq-item", "default", "h", "dimension", "The 75px FAQ row at rest."),
    ("faq-open-height", "faq-item", "opened", "h", "dimension", "The ~118px open FAQ row."),
    ("faq-side-pad", "faq-item", "default", "paddingLeft", "dimension", "The 26.6px FAQ row padding."),
    ("footer-height", "footer", "default", "h", "dimension", "The ~812px footer."),
    ("cookie-accept-width", "cookie-accept", "default", "w", "dimension", "The ~150px consent Accept-all button."),
    ("cookie-check-radius", "cookie-check", "default", "borderTopLeftRadius", "dimension", "The ~20px consent checkbox card radius."),
    ("legal-pad-top", "legal-section", "default", "paddingTop", "dimension", "The ~106px legal section top padding."),
    ("mobile-header-height", "m-header", "default", "h", "dimension", "The ~104px phone header."),
    ("mobile-menu-pill", "m-menu-pill", "default", "h", "dimension", "The ~42.7px phone menu pill."),
    ("mobile-nav-overlay", "m-nav-overlay", "opened", "h", "dimension", "The ~56px phone menu overlay row."),
    ("mobile-faq-height", "m-faq-item", "default", "h", "dimension", "The ~95px phone FAQ row."),
]:
    try:
        if prop in ("w", "h"):
            v = rc(cname, state, prop)
            v = ("%g" % v) + "px"
            src = f"measured {prop} of {cname} {state} (raw/components-computed.json)"
        else:
            v = norm_len(st(cname, state)[prop])
            src = msrc(cname, state, prop)
        mktc[name] = lit(v, ty_ if re.fullmatch(r"-?[\d.]+(px|rem)", str(v)) else "other", src, desc)
    except KeyError:
        pass

# app.fourmula.ai is a separate dark-only app outside the marketing token
# layer; its measured values are kept as literals, honestly labelled.
app = comp.setdefault("app", {})
for name, cname, state, prop, ty_, desc in [
    ("menu-btn", "app-menu-btn", "default", "h", "dimension", "The 32px square app menu button."),
    ("create-btn", "app-create-btn", "default", "h", "dimension", "The 32px \"Create asset\" pill height."),
    ("signin-btn", "app-signin-btn", "default", "h", "dimension", "The 32px \"Sign in\" pill height."),
    ("start-h1-width", "start-h1", "default", "w", "dimension", "The ~432px /start heading width."),
    ("start-cta", "start-cta", "default", "h", "dimension", "The 40px /start CTA height."),
    ("auth-card-width", "auth-card", "default", "w", "dimension", "The 384px sign-in card."),
    ("auth-card-height", "auth-card", "default", "h", "dimension", "The ~469px sign-in card height."),
    ("auth-card-radius", "auth-card", "default", "borderTopLeftRadius", "dimension", "The 28px card radius (rounded-4xl)."),
    ("auth-card-border", "auth-card", "default", "borderTopColor", "color", "The #1a1a1a card border (--color-base-700)."),
    ("auth-card-bg", "auth-card", "default", "backgroundColor", "color", "The #111111 card fill (--color-base-800)."),
    ("auth-card-backdrop", "auth-card", "default", "backdropFilter", "other", "The blur(24px) card backdrop (--blur-xl)."),
    ("auth-card-pad-x", "auth-card", "default", "paddingLeft", "dimension", "The 32px card side padding."),
    ("auth-card-gap", "auth-card", "default", "gap", "dimension", "The 24px card section gap."),
    ("field-height", "auth-field-email", "default", "h", "dimension", "The 48px auth field height."),
    ("field-width-email", "auth-field-email", "default", "w", "dimension", "The ~286px email field width."),
    ("google-height", "auth-google", "default", "h", "dimension", "The 40px Google button height."),
    ("submit-height", "auth-submit", "default", "h", "dimension", "The 40px Sign-in submit height."),
    ("submit-radius", "auth-submit", "default", "borderTopLeftRadius", "dimension", "The full-pill submit (Tailwind rounded-full)."),
    ("back-height", "auth-back", "default", "h", "dimension", "The 32px Back pill height."),
    ("eye-size", "auth-eye", "default", "h", "dimension", "The 16px password-visibility icon."),
    ("accent-fill", "auth-submit", "default", "backgroundColor", "color", "The #ff6b02 accent fill on primary actions (--color-accent-500)."),
    ("accent-ink", "auth-submit", "default", "color", "color", "The #020108 ink on the accent fill."),
    ("accent-tint", "auth-google", "default", "backgroundColor", "color", "The accent-at-20% translucent fill on secondary pills (painted oklab ≈ #ff6b02 at 20%)."),
    ("accent-disabled", "pdp-start-bottom", "default", "backgroundColor", "color", "The accent-at-15% fill on the not-ready Start generation submit."),
    ("muted-ink", "auth-forgot", "default", "color", "color", "The #686a6e meta ink (--color-base-600)."),
    ("dim-ink", "auth-back", "default", "color", "color", "The #b0b4ba secondary ink (--color-base-500)."),
    ("ghost-fill", "auth-back", "default", "backgroundColor", "color", "The white-at-5% fill on the Back pill."),
    ("link-accent", "auth-switch", "default", "color", "color", "The #ff6b02 accent link ink."),
    ("reco-dialog-width", "pdp-reco-dialog", "default", "w", "dimension", "The 480px Recommendations (What can I upload?) dialog."),
    ("reco-dialog-radius", "pdp-reco-dialog", "default", "borderTopLeftRadius", "dimension", "The 28px dialog radius (rounded-4xl)."),
    ("dialog-bg", "pdp-reco-dialog", "default", "backgroundColor", "color", "The #1e1e1e dialog fill (--color-base-750)."),
    ("what-dialog-width", "pdp-what-dialog", "default", "w", "dimension", "The 880px What's-a-PDP explainer dialog."),
    ("upload-height", "pdp-upload", "default", "h", "dimension", "The 40px Upload Main Image button."),
    ("shopify-cta-width", "pdp-shopify-cta", "default", "w", "dimension", "The 152px Check connection pill."),
    ("cancel-width", "pdp-cancel", "default", "w", "dimension", "The 131px Cancel and close pill."),
    ("dash-link-opacity", "pdp-dash-link", "default", "opacity", "number", "The 0.3 faded Dashboard link."),
    ("signedin-chip", "pdp-signedin-chip", "default", "h", "dimension", "The 25px Signed-in requirement chip."),
    ("format-item-height", "pdp-format-static", "default", "h", "dimension", "The 60px Static/Video content radio row."),
    ("format-item-radius", "pdp-format-static", "default", "borderTopLeftRadius", "dimension", "The 16px radio-card radius (rounded-2xl)."),
    ("format-item-bg", "pdp-format-static", "default", "backgroundColor", "color", "The #1a1a1a radio-card fill (--color-base-700)."),
    ("format-item-ink", "pdp-format-static", "default", "color", "color", "The accent ink on the selected radio."),
    ("format-video-opacity", "pdp-format-video", "default", "opacity", "number", "The 0.5 disabled Video-content radio."),
    ("start-bottom-width", "pdp-start-bottom", "default", "w", "dimension", "The ~591px full-width footer submit."),
    ("start-bottom-radius", "pdp-start-bottom", "default", "borderTopLeftRadius", "dimension", "The 12px footer-submit radius (rounded-xl)."),
    ("start-header-width", "pdp-start-header", "default", "w", "dimension", "The 123px header Start generation submit."),
]:
    try:
        if prop in ("w", "h"):
            v = rc(cname, state, prop)
            v = ("%g" % v) + "px"
            src = f"measured {prop} of {cname} {state} on app.fourmula.ai (raw/components-computed.json)"
        elif prop == "opacity":
            v = float(st(cname, state)[prop])
            src = msrc(cname, state, prop)
        else:
            v = norm_len(st(cname, state)[prop])
            src = msrc(cname, state, prop)
        if ty_ == "dimension" and not re.fullmatch(r"-?[\d.]+(px|rem)", str(v)):
            ty_ = "other"
        app[name] = lit(v, ty_, src, desc)
    except (KeyError, TypeError, ValueError):
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
