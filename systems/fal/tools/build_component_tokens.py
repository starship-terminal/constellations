#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

fal.ai is three surfaces signed out: the single-theme Webflow marketing pages
(/, /pricing, /serverless, /contact-sales), the Next.js app (/explore,
/models/*, /login — a Tailwind v4-style token layer themed by html.light |
html.dark via prefers-color-scheme) and the fumadocs docs (/docs/*, its own
layer, themed by data-theme-preference). vars.mjs resolves each surface's
stylesheets into raw/css-vars.json passes: marketing, appLight, appDark,
docsLight, docsDark.

The app declares a real design-token layer (~839 resolved names): raw colour
scales (--color-*, --primary-*/--secondary-*/--error-*/--info-*/
--success-*/--warning-*/--neutral-*/--lightblue-* held as `H S% L%` triplets
and #hex), the semantic --surface-*/--content-*/--stroke-*/--overlay-*/
--shadow-*/--backdrop/--indicator-* roles that switch per theme, the
--accent-{hue}-{solid,alpha,foreground,...} families, --badge-*, the
--product-banner-{blue,green,purple}-{light,dark}-{background,foreground,mark}
banner palette, --composer-prompt-*, --chart-* dataviz, the
--swatch-{name}-{role} landing-page palettes, the --text-*/--leading-*/
--tracking-* type layer, --font-*, --radius-*, --spacing, --ease-*, --animate-*,
--breakpoint-*/--container-* and --header-expanded.

Theme-dependent names (the surface/content/stroke/overlay/shadow/backdrop/
indicator/badge/indicator/accent/*semantic* roles, the bare --error/-foreground
+ --error-page-* group, --composer-prompt-*, --brand-sky, --neutral-background,
--selection-scrim, --generation-loading-border, --copy-text-shimmer-highlight)
are emitted under both light.* and dark.* as {"var": name} leaves so each
theme resolves its own value. Theme-invariant scales land under core.*.

Marketing's Webflow layer (--brand-colors--*, --base-color-*/--background-color--*/
--border-color--*/--text-color--* aliases, --size-*) is single-theme and lands
under core.marketing. The docs layer (--primary/-light/-dark, --gray-*,
--background-light/-dark, --default-border-color, --tooltip-foreground,
--font-family-*-custom, --font-inter/--font-paper-mono, --topbar-tabs-height,
--twoslash-*) lands under core.docs, with the few theme-dependent docs names
(--default-border-color, --twoslash-*) emitted per theme under light.docs and
dark.docs.

Measured computed styles from raw/components-computed.json:

  marketing   Focal Web 96px hero on the cyan #99edff field, .nav-main 88px
              fixed bar, a.nav-list-item links, a.button CTAs, w-dropdown
              Products trigger
  app dark    --surface-page 18 18 22 canvas, Public Sans Rounded UI, the
              model-card grid, the playground form and its Sign-in-to-run
              action
  docs        Focal 36px "Build with fal" h1, Public Sans prose, .nav-tabs
              strip, the fixed sidebar, .code-group samples
"""

import colorsys, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RA = V.get("resolved", {}).get("appLight", {})
RD = V.get("resolved", {}).get("appDark", {})
RM = V.get("resolved", {}).get("marketing", {})
RDL = V.get("resolved", {}).get("docsLight", {})
RDD = V.get("resolved", {}).get("docsDark", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]


def valof(v):
    return v.get("value", v.get("raw")) if isinstance(v, dict) else v


A = {n: valof(v) for n, v in RA.items()}
D = {n: valof(v) for n, v in RD.items()}
M = {n: valof(v) for n, v in RM.items()}
DL = {n: valof(v) for n, v in RDL.items()}
DD = {n: valof(v) for n, v in RDD.items()}

# The app's family stacks are carried by next/font class names, not custom
# properties (the only --font-* names the sheets declare are the
# --font-weight-* scale), so the family tokens below are the measured
# computed fontFamily of real components.


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. fal.ai declares "
    "its design-token layer in its stylesheets (raw/css-vars.json): "
    "theme-invariant scales under core.* (the app colour scales and type/"
    "space/motion layer, the marketing Webflow palette, the docs layer), the "
    "theme-dependent semantic roles under both light.* and dark.* so each "
    "theme resolves its own value. Measured roles alias to the declared "
    "values where they match."),
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
    # vars.mjs resolves colours as #rr,gg,bb
    m = re.fullmatch(r"#([0-9a-fA-F]{2}),([0-9a-fA-F]{2}),([0-9a-fA-F]{2})", v)
    if m:
        return "#" + "".join(x.lower() for x in m.groups())
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    # fal keeps its semantic scales as raw `H S% L%` triplets and raw `R G B` triplets
    m = re.fullmatch(r"(-?[\d.]+)\s+([\d.]+)%\s+([\d.]+)%", v)
    if m:
        h, s, l = (float(x) for x in m.groups())
        r, g, b = colorsys.hls_to_rgb((h % 360) / 360, l / 100, s / 100)
        return "#%02x%02x%02x" % (round(r * 255), round(g * 255), round(b * 255))
    m = re.fullmatch(r"(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})", v)
    if m:
        return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())
    return v


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False


def lit(value, ty, src, desc):
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


EMITTED = {}   # emitted name -> dotted token path it was actually written to
_OWNER = {}    # dotted token path -> emitted name holding it


def _leaf(d):
    return isinstance(d, dict) and ("var" in d or "value" in d)


def emit(root, name, leaf):
    """Write `leaf` at name's dotted path."""
    node = root
    parts = [p for p in name[2:].split("-") if p]  # '--' runs (stripped <deleted|variable-…> markers) leave empty segments
    for i, p in enumerate(parts[:-1]):
        nxt = node.get(p)
        prefix = ".".join(parts[:i + 1])
        if nxt is None:
            nxt = node[p] = {}
        elif _leaf(nxt):
            owner = _OWNER.pop(prefix, None)
            nxt = node[p] = {"default": nxt}
            if owner:
                EMITTED[owner] = prefix + ".default"
                _OWNER[prefix + ".default"] = owner
        node = nxt
    last = parts[-1]
    path = ".".join(parts)
    if last in node and not _leaf(node[last]):
        for key in ("default", "base", "self"):
            if key not in node[last]:
                node[last][key] = leaf
                path += "." + key
                break
        else:
            raise ValueError(f"{name}: no free key to hold the leaf beside its group")
    else:
        if last in node:
            raise ValueError(f"{name}: duplicate token path {path}")
        node[last] = leaf
    EMITTED[name] = path
    _OWNER[path] = name


def emitted_path(name):
    return EMITTED[name]


DECL_SRC = "declared fal.ai design-system variable in the site stylesheet (raw/css-vars.json)"

COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|#[0-9a-fA-F]{2}(,[0-9a-fA-F]{2}){2}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|-?[\d.]+\s+[\d.]+%\s+[\d.]+%|\d{1,3}\s+\d{1,3}\s+\d{1,3})")


def is_colorish(v):
    return bool(COLOR_V.fullmatch(str(v).strip()))


def viewport_note(name):
    """The committed raw/css-vars.json resolved viewport-relative values on a default
    1280 x 720 probe page while its note says 1440 x 900; say so on any token built from
    one. A capture from the fixed vars.mjs records probeViewport and gets no warning."""
    if V.get("probeViewport") == "1440x900":
        return ""
    for entry in V.get("resolved", {}).values():
        e = entry.get(name)
        if isinstance(e, dict) and "viewport-relative" in str(e.get("note", "")):
            return (f"; viewport-relative (declared {e.get('raw')}), resolved on a 1280 x 720 probe page, "
                    "not the 1440 x 900 capture viewport: recapture needed")
    return ""


def decl(name, ty="dimension", bag=A):
    v = bag[name]
    if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(v).strip()):
        ty = "other"
    return lit(v, ty, f"{DECL_SRC}: {name}{viewport_note(name)}", f"The declared `{name}`.")


def decl_color(name, bag=A):
    v = bag[name]
    ty = "color" if is_colorish(v) else "other"
    return lit(norm_color(v), ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


# ------------------------------------------------------------------- fonts
#
# fal ships its families as next/font classes, not --font-* variables (the
# sheets only declare --font-weight-*), so every family token is the measured
# computed fontFamily of a real component. The surfaces paint: publicSansRounded
# for every app control and body, focal for product headings, chivoMono for
# code, "Focal Web" and "Focal Text" on the Webflow marketing pages, "Public
# Sans" body + "Focal Medium" headings on the docs.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("ui", "app-btn-signup", "default",
     "The computed fontFamily of an app header button — publicSansRounded over publicSans and system fallbacks; every app control and body text paints this stack."),
    ("app-heading", "mp-h1", "default",
     "The computed fontFamily of the model endpoint heading — focal over ui-sans-serif/system-ui; product headings on the app surface."),
    ("mono", "api-code", "default",
     "The computed fontFamily of the API code sample — chivoMono over ui-monospace; code and endpoint ids on the app surface."),
    ("marketing-display", "mkt-hero-h1", "default",
     "The computed fontFamily of the home hero h1 — Focal Web over Arial; the Webflow marketing display face."),
    ("marketing-body", "pr-price-row", "default",
     "The computed fontFamily of a pricing table row — Focal Text over Arial; the Webflow marketing text face."),
    ("docs-heading", "docs-h1", "default",
     "The computed fontFamily of the docs h1 — Focal Medium over Focal and system sans."),
    ("docs-body", "docs-card", "default",
     "The computed fontFamily of a docs section card — Public Sans over the system sans stack; docs body text."),
    ("docs-hero", "docs-prose", "default",
     "The computed fontFamily of the docs hero lead — Focal Medium, the same face as the docs h1, not the Public Sans body."),
]:
    try:
        raw = st(comp, state)["fontFamily"]
        fam[key] = lit(raw, "fontFamily",
                       f"computed fontFamily of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for name in sorted(k for k in A if k.startswith("--font-weight-")):
    leaf = decl(name, "fontWeight")
    try:
        leaf["value"] = int(float(leaf["value"]))
    except (TypeError, ValueError):
        leaf["type"] = "other"
    weights[name[len("--font-weight-"):]] = leaf

# ------------------------------------------------- declared scales (app)
#
# Type sizes --text-* (+--line-height twins), tracking, leading — emitted
# under core.font as the app's Tailwind-type scale.

for name in sorted(A):
    m = re.fullmatch(r"--text-(xs|sm|base|lg|xl|\dxl|landing-display|landing-title)(--line-height)?", name)
    if not m:
        continue
    step, lh = m.groups()
    bag = SPEC["core"].setdefault("font", {}).setdefault("lineHeight" if lh else "size", {}).setdefault("text", {})
    leaf = decl(name, "dimension" if not lh else "number")
    if lh and not re.fullmatch(r"-?\d+(\.\d+)?", str(leaf["value"])):
        # Tailwind v4 --text-*--line-height can be a length or a ratio
        leaf["type"] = "dimension" if str(leaf["value"]).endswith(("px", "rem")) else "other"
    bag[step] = leaf

for name in sorted(k for k in A if k.startswith("--tracking-")):
    SPEC["core"].setdefault("font", {}).setdefault("tracking", {})[name[len("--tracking-"):]] = decl(name, "other")
for name in sorted(k for k in A if k.startswith("--leading-")):
    leaf = decl(name, "number")
    if not re.fullmatch(r"-?\d+(\.\d+)?", str(leaf["value"])):
        leaf["type"] = "other"
    SPEC["core"].setdefault("font", {}).setdefault("leading", {})[name[len("--leading-"):]] = leaf

# Radii, spacing, layout, motion — theme-invariant under core.
for name in sorted(k for k in A if k.startswith("--radius-")):
    SPEC["core"].setdefault("radius", {})[name[len("--radius-"):]] = decl(name)
if "--spacing" in A:
    SPEC["core"].setdefault("spacing", {})["unit"] = decl("--spacing")
for name in sorted(k for k in A if re.fullmatch(r"--spacing-\d+-\d+", k)):
    SPEC["core"].setdefault("spacing", {})[name[len("--spacing-"):]] = decl(name)
for name in sorted(k for k in A if k.startswith("--container-")):
    SPEC["core"].setdefault("container", {})[name[len("--container-"):]] = decl(name)
for name in sorted(k for k in A if k.startswith("--breakpoint-")):
    SPEC["core"].setdefault("breakpoint", {})[name[len("--breakpoint-"):]] = decl(name)
for name in sorted(k for k in A if k.startswith("--blur-")):
    SPEC["core"].setdefault("blur", {})[name[len("--blur-"):]] = decl(name)
for name in sorted(k for k in A if k.startswith("--ease-")):
    SPEC["core"].setdefault("easing", {})[name[len("--ease-"):]] = decl(name, "cubicBezier")
for name in sorted(k for k in A if k.startswith(("--animate-", "--animation-", "--default-transition-"))):
    ty = "duration" if name.endswith("duration") else ("cubicBezier" if name.endswith("timing-function") else "other")
    emit(SPEC["core"], "--motion" + name[1:], decl(name, ty))
for name in sorted(k for k in A if k in ("--aspect-video", "--scroll-mt", "--header-expanded", "--banner-height", "--sticky-below-nav")):
    emit(SPEC["core"], name, decl(name))

# --------------------------------------------------- colour scales (core)
#
# Raw scales that do not switch theme: --color-*, the --primary/-secondary/
# -error/-info/-success/-warning/-neutral/-lightblue numeric ramps (the bare
# family name --error etc. DOES switch and goes to the themes), --chart-*,
# --product-banner-{hue}-{light,dark}-*, --swatch-*.

def scale_bag(name):
    m = re.fullmatch(r"--(primary|secondary|error|info|success|warning|neutral|lightblue)-(\d+)", name)
    if m:
        return f"--palette-{m.group(1)}-{m.group(2)}"
    m = re.fullmatch(r"--(primary|secondary|error|info|success|warning|neutral|lightblue)-(1000)", name)
    if m:
        return f"--palette-{m.group(1)}-{m.group(2)}"
    return None

# Names that are theme-dependent (emitted under both sets below).
def theme_dependent(n):
    return (
        n.startswith(("--surface", "--content", "--stroke", "--overlay", "--shadow",
                      "--backdrop", "--indicator", "--badge", "--accent-", "--composer-",
                      "--error", "--selection", "--generation-loading", "--copy-text-shimmer-highlight",
                      "--neutral-background", "--brand-sky", "--twoslash-",
                      "--color-content-", "--color-stroke-", "--color-surface"))
        and not re.fullmatch(r"--(error|info|success|warning|primary|secondary|neutral|lightblue)-\d+", n)
    )

for name in sorted(A):
    if theme_dependent(name):
        continue
    if name.startswith("--f-"):
        continue  # fancybox widget internals — vendor chrome, not the system
    if re.fullmatch(r"--color-\d+", name):
        continue
    if name.startswith("--color-"):
        emit(SPEC["core"], name, decl_color(name))
        continue
    sb = scale_bag(name)
    if sb:
        emit(SPEC["core"], sb, decl_color(name))
        continue
    if re.fullmatch(r"--(primary|secondary|info|success|warning|neutral|lightblue)", name):
        emit(SPEC["core"], f"--palette-{name[2:]}-default", decl_color(name))
        continue
    if name.startswith("--chart-"):
        emit(SPEC["core"], name, decl_color(name))
        continue
    if name.startswith("--product-banner-"):
        emit(SPEC["core"], name, decl_color(name))
        continue
    if name.startswith("--swatch-"):
        emit(SPEC["core"], name, decl_color(name) if is_colorish(A[name]) else decl(name, "other"))
        continue
    if name in ("--brand-sky",):
        continue

# ------------------------------------------- per-theme semantic variables
#
# Every theme-dependent name is emitted under both light.* and dark.* as a
# {"var": name} leaf, so each set resolves the value its theme paints.

for root, bag in ((SPEC["light"], A), (SPEC["dark"], D)):
    for name in sorted(k for k in bag if theme_dependent(k)):
        v = str(bag[name]).strip()
        ty = ("color" if is_colorish(v)
              else "shadow" if "px" in v and v.startswith(("rgba", "rgb(", "#", "hsla", "hsl(", "inset", "lab(", "lch(", "oklab", "oklch"))
              else "dimension" if re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", v)
              else "other")
        emit(root, name, var(name, ty))

# --------------------------------------------------- marketing (Webflow)
#
# The marketing pages paint one theme; their Webflow variables land under
# core.marketing. build_tokens.py resolves {"var"} leaves for core in the
# light pass, which carries the marketing resolution.

mkt = SPEC["core"].setdefault("marketing", {})
for name in sorted(M):
    if name.startswith("--brand-colors--"):
        emit(mkt, name.replace("--brand-colors--", "--brand-"), decl_color(name, M))
for name in sorted(M):
    if name.startswith("--size-"):
        emit(mkt, name, decl(name, "dimension", M))
    elif re.match(r"--(base-color|background-color|background-colors|border-color|text-color|accessible-components)--", name):
        short = re.sub(r"<deleted\|variable-[0-9a-f-]+>", "", name)
        emit(mkt, short, decl_color(name, M))
    elif name in ("--home-nav-sweep-color",):
        emit(mkt, "--brand-nav-sweep", decl_color(name, M))

# ------------------------------------------------------------- docs layer
#
# The docs declare their own layer; theme-invariant names land under
# core.docs, theme-dependent ones (--default-border-color, --twoslash-*)
# under light.docs/dark.docs.

for name in sorted(DL):
    if DL.get(name) != DD.get(name):
        continue
    if name.startswith("--gray-"):
        emit(SPEC["core"].setdefault("docs", {}), name, decl_color(name, DL))
for name in sorted(DL):
    if DL.get(name) != DD.get(name):
        continue
    if name in ("--primary", "--primary-light", "--primary-dark", "--background-light",
                "--background-dark", "--tooltip-foreground", "--default-font-family",
                "--default-mono-font-family", "--font-family-body-custom",
                "--font-family-headings-custom", "--font-inter", "--font-paper-mono",
                "--topbar-tabs-height", "--color-primary"):
        emit(SPEC["core"].setdefault("docs", {}), name, decl_color(name, DL) if is_colorish(DL[name]) or re.fullmatch(r"\d{1,3}\s+\d{1,3}\s+\d{1,3}", str(DL[name])) else decl(name, "fontFamily" if "font" in name else "other", DL))
for root, bag, pname in ((SPEC["light"].setdefault("docs", {}), DL, "docs light"), (SPEC["dark"].setdefault("docs", {}), DD, "docs dark")):
    for name in sorted(k for k in bag if k == "--default-border-color" or k.startswith("--twoslash-")):
        v = bag[name]
        leaf = lit(norm_color(v) if is_colorish(v) else v,
                   "color" if is_colorish(v) else ("shadow" if "px" in str(v) and str(v).startswith(("rgba", "rgb(", "#", "inset")) else "other"),
                   f"{DECL_SRC}: {name} ({pname} pass)",
                   f"The declared docs `{name}` (the docs layer has its own value for this name in each theme).")
        emit(root, name, leaf)

# ------------------------------------------------ measured semantic roles
#
# Roles measured on the painted surfaces; each aliases to the declared
# token whose per-theme value it matches.

role_alias = {"light": {}, "dark": {}}
for theme, bag in (("light", A), ("dark", D)):
    for name in sorted(k for k in bag if theme_dependent(k) and is_colorish(bag[k])):
        if name in EMITTED:
            role_alias[theme].setdefault(norm_color(bag[name]), EMITTED[name])
for theme, bag in (("light", DL), ("dark", DD)):
    for name in sorted(k for k in bag if (k.startswith("--gray-") or k in ("--primary", "--primary-light", "--primary-dark")) and is_colorish(bag[k])):
        emitted = name
        if emitted in EMITTED:
            role_alias[theme].setdefault(norm_color(bag[name]), "docs." + EMITTED[emitted])
for name in sorted(M):
    if name.startswith("--brand-colors--"):
        emitted = name.replace("--brand-colors--", "--brand-")
        if emitted in EMITTED:
            role_alias["light"].setdefault(norm_color(M[name]), "marketing." + EMITTED[emitted])


def split_shadow(v):
    """Top-level comma split of a computed box-shadow list."""
    return [p.strip() for p in re.split(r",\s*(?![^()]*\))", v) if p.strip()]


def painted_ring(sty):
    """(colour, how) of the focus ring a state really paints, from its computed style dict: a drawn outline
    (non-none style, width above 0), else the outermost visible box-shadow
    layer with a spread — fal's app buttons draw a 3px shadow ring and leave
    `outline` at none, so the outline colour is the inactive default."""
    if sty.get("outlineStyle", "none") != "none" and float(sty.get("outlineWidth", "0px")[:-2] or 0) > 0 \
            and sty.get("outlineColor") != "rgba(0, 0, 0, 0)":
        return sty["outlineColor"], f"outline {sty['outlineWidth']} {sty['outlineStyle']}"
    ring = None
    for layer in split_shadow(sty.get("boxShadow", "none")):
        if layer.startswith("none"):
            continue
        m = re.match(r"^(rgba?\([^)]*\))\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(\s+inset)?$", layer)
        if not m or m.group(6) or float(m.group(5)) <= 0:
            continue
        if re.fullmatch(r"rgba\(\s*\d+,\s*\d+,\s*\d+,\s*0\s*\)", m.group(1)):
            continue
        ring = (m.group(1), f"box-shadow {m.group(5)}px spread")
    if ring:
        return ring
    raise KeyError("no painted ring")


def semcolor(raw, src, desc, theme="light"):
    alias = role_alias[theme].get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


sem = SPEC["light"]
dsem = SPEC["dark"]
# The app pages (explore/model/login) are measured under their dark theme —
# their readings feed the dark set; the light set's measured roles come from
# the marketing and docs pages, which paint light.
for root, theme, key, comp, state, prop, group, desc in [
    (sem, "light", "primary", "mkt-btn-start", "default", "backgroundColor", "action",
     "The primary Get-Started button fill on the marketing header."),
    (sem, "light", "primary-foreground", "mkt-btn-start", "default", "color", "action",
     "The label colour on the primary Get-Started button."),
    (sem, "light", "primary-hover", "mkt-btn-start", "hover", "backgroundColor", "action",
     "The primary marketing button fill on hover."),
    (sem, "light", "secondary", "mkt-btn-sales", "default", "backgroundColor", "action",
     "The secondary Contact-Sales button fill on the marketing header."),
    (sem, "light", "hero-cta", "mkt-hero-cta", "default", "backgroundColor", "action",
     "The hero call-to-action fill on the marketing home page."),
    (sem, "light", "focus", "mkt-btn-start", "focus-visible", "focusRing", "border",
     "The keyboard focus ring on the marketing surface."),
    (sem, "light", "hero-text", "mkt-hero-h1", "default", "color", "marketing-text",
     "The display colour the marketing hero paints."),
    (sem, "light", "hero-field", "mkt-hero-field", "default", "backgroundColor", "marketing-surface",
     "The dark bronze field the hero section paints behind the display headline (read on the h1's section, since the h1 itself is transparent)."),
    (sem, "light", "card", "docs-card", "default", "backgroundColor", "docs",
     "The docs section card fill on the light docs surface."),
    (sem, "light", "card-hover", "docs-card", "hover", "backgroundColor", "docs",
     "The docs card fill on hover."),
    (sem, "light", "search-fill", "docs-search", "default", "backgroundColor", "docs",
     "The docs search trigger fill."),
    (dsem, "dark", "primary", "app-btn-signup", "default", "backgroundColor", "action",
     "The primary Sign-up button fill on the dark app surface."),
    (dsem, "dark", "primary-foreground", "app-btn-signup", "default", "color", "action",
     "The label colour on the primary Sign-up button: dark text on the near-white fill."),
    (dsem, "dark", "primary-hover", "app-btn-signup", "hover", "backgroundColor", "action",
     "The dark primary fill on hover."),
    (dsem, "dark", "secondary", "app-btn-login", "default", "backgroundColor", "action",
     "The Log-in button fill on the dark app surface."),
    (dsem, "dark", "focus", "app-btn-signup", "focus-visible", "focusRing", "border",
     "The keyboard focus ring on the dark app surface: the 3px box-shadow ring the button paints (its outline is none)."),
    (dsem, "dark", "run", "mp-run", "default", "backgroundColor", "action",
     "The Sign-in-to-run action fill on the model playground."),
    (dsem, "dark", "run-hover", "mp-run", "hover", "backgroundColor", "action",
     "The Sign-in-to-run fill on hover."),
    (dsem, "dark", "badge", "mp-badge", "default", "backgroundColor", "action",
     "The model badge fill (the brand-alpha tint)."),
    (dsem, "dark", "card", "model-card", "default", "backgroundColor", "catalog",
     "The model tile fill on the explore grid."),
    (dsem, "dark", "card-hover", "model-card", "hover", "backgroundColor", "catalog",
     "The model tile fill on hover."),
]:
    try:
        if prop == "focusRing":
            raw, how = painted_ring(st(comp, state))
            src = f"painted focus ring ({how}) of {comp} {state} (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if not raw or raw == "rgba(0, 0, 0, 0)":
            continue
        root.setdefault(group, {})[key] = semcolor(raw, src, desc, theme)
    except KeyError:
        pass

# ------------------------------------------------------------- type ramp
#
# Measured sizes alias to the declared --text-* step they match.

size_alias = {}
for name in A:
    m = re.match(r"--text-(xs|sm|base|lg|xl|\dxl|landing-display|landing-title)$", name)
    if m:
        size_alias.setdefault(A[name], (f"font.size.text.{m.group(1)}", name))

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {}).setdefault("measured", {})
for key, comp, state, desc in [
    ("button", "app-btn-signup", "default", "The header button label size on the app surface."),
    ("model-h1", "mp-h1", "default", "The model endpoint heading size (krea/v3/text-to-image)."),
    ("hero-mkt", "mkt-hero-h1", "default", "The marketing hero display size — Focal Web in cyan on the dark bronze field."),
    ("docs-h1", "docs-h1", "default", "The docs page heading size — Focal."),
    ("docs-body", "docs-prose", "default", "The docs body text size."),
    ("nav-item", "app-nav-docs", "default", "The app header nav item size."),
]:
    try:
        raw = st(comp, state)["fontSize"]
        src = f"computed fontSize of {comp} {state} (raw/components-computed.json)"
        alias = size_alias.get(raw)
        ty[key] = lit(f"{{{alias[0]}}}" if alias else raw, "dimension",
                      src + (f"; matches declared {alias[1]}" if alias else ""), desc)
    except KeyError:
        pass
if not ty:
    SPEC["core"]["font"]["size"].pop("measured", None)

# ------------------------------------------------------------------ shape

radius_alias = {A[n]: n for n in A if n.startswith("--radius-")}
for key, comp, state, prop, desc in [
    ("measured-button", "app-btn-signup", "default", "borderTopLeftRadius", "The measured app button radius."),
    ("measured-card", "model-card", "default", "borderTopLeftRadius", "The model card's surface radius."),
    ("measured-field", "search-models", "default", "borderTopLeftRadius", "The model search field radius."),
    ("measured-badge", "mp-badge", "default", "borderTopLeftRadius", "The model badge radius."),
    ("measured-mkt-button", "mkt-btn-start", "default", "borderTopLeftRadius", "The marketing button radius."),
]:
    try:
        v = st(comp, state)[prop]
        src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        dkey = radius_alias.get(v)
        if dkey:
            radii = SPEC["core"]["radius"]
            radii[key] = lit(f"{{radius.{dkey[len('--radius-'):]}}}", "dimension", src + f"; matches declared {dkey}", desc)
        else:
            SPEC["core"]["radius"][key] = lit(v, "dimension" if re.fullmatch(r"[0-9.]+(px|rem)", v or "") else "other", src, desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ motion

try:
    s = st("app-btn-signup", "default")
    dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        emit(SPEC["core"], "--motion-control", lit(f"{s.get('transitionProperty', 'all')} {dur} {ease or ''}".strip(), "other",
            "computed transition of app-btn-signup default (raw/components-computed.json)",
            "The measured control transition on app buttons."))
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("app-header-height", "app-header", "default", "h", "dimension", "The 48px app navigation header."),
    ("mkt-header-height", "mkt-header", "default", "h", "dimension", "The 88px fixed marketing bar (div.nav-main) — matches --header-expanded."),
    ("announce-height", "app-announce", "default", "h", "dimension", "The announcement strip height."),
    ("button-height", "app-btn-signup", "default", "h", "dimension", "The app header button height."),
    ("icon-button", "app-announce-x", "default", "h", "dimension", "The dismiss-X icon button size."),
    ("search-field-height", "search-models", "default", "h", "dimension", "The model search input height."),
    ("model-card-width", "model-card", "default", "w", "dimension", "The explore model card width."),
    ("model-card-height", "model-card", "default", "h", "dimension", "The explore model card height."),
    ("run-button-height", "mp-run", "default", "h", "dimension", "The Sign-in-to-run action height."),
    ("prompt-min-height", "mp-prompt", "default", "h", "dimension", "The playground prompt field height."),
    ("param-option-height", "mp-param", "default", "h", "dimension", "A playground parameter option pill height."),
    ("tab-height", "mp-tab", "default", "h", "dimension", "The model page tab height."),
    ("login-card-width", "li-card", "default", "w", "dimension", "The OAuth login card width."),
    ("oauth-button-height", "li-oauth-github", "default", "h", "dimension", "The Continue-with-* OAuth button height."),
    ("docs-topbar-height", "docs-topbar", "default", "h", "dimension", "The docs tab strip height."),
    ("docs-search-height", "docs-hero-search", "default", "h", "dimension", "The docs hero search field height."),
    ("docs-toc-width", "docs-toc", "default", "w", "dimension", "The on-this-page TOC width."),
    ("mkt-button-height", "mkt-btn-start", "default", "h", "dimension", "The marketing header button height."),
    ("mkt-nav-height", "mkt-nav-pricing", "default", "h", "dimension", "The marketing nav link height."),
    ("mobile-header-height", "m-header", "default", "h", "dimension", "The phone app top bar height."),
    ("mobile-card-width", "m-model-card", "default", "w", "dimension", "The phone model card width."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
