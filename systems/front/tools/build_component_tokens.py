#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

front.com is four public surfaces signed out, and its design layer arrives in
two vocabularies:

  The marketing site (front.com/...) is a Next.js + Tailwind app whose
  stylesheets declare almost no custom properties; the design layer is
  compiled into bespoke classes, captured verbatim in raw/css-classes.json:

    .bg-<hue>-<step> / .text-*/.border-*   the hue ramps: violet 50-1000,
                                          citron 100/500, blue 100-1000,
                                          gray 50-950, green/pink 100-900,
                                          salmon 200/950, orange 100/200,
                                          yellow 200/900, neutral-200
    .surface-l0..l3, .surface-outer, .surface-highlight, .surface-*-hover/active
                                          the semantic surface scale
    .text-primary/-inactive, .text-secondary/-inactive
                                          the text roles
    .button-surface*/.button-border*/.button-text*
                                          the button state layer (default,
                                          hover, active, disabled, outline,
                                          tab and inverted variants)
    .text-display1, .text-h1..h4, .text-p1/p2, .text-caption1/2, .text-micro1..3
                                          the type ramp, each a
                                          size/line-height/tracking/weight quad
    .font-size-*, .font-line-height-*, .font-letter-spacing-*, .font-weight-*
                                          the underlying utility scales
    .rounded-4..40, .duration-*, .ease-*  radius and motion scales
    Every semantic rule is redeclared under the page's three section themes:
    [data-theme=theme-dark-violet] (the plum default), theme-white and
    theme-gray — three complete role tables, no page-level theme switch.

  The product token layer is the real thing, shipped two ways:
    app.frontapp.com's signin shell injects a --color-* sheet: the
    --color-primitive-<hue>-<step> ramps (alpha, blue, blurple, gray, green,
    magenta, orange, purple, red, teal, yellow — 126 names) and 206
    --color-bg/text/icon/border/fill/input/accent/cell/tab/toggle/tooltip
    semantics, redeclared under [data-theme="dark"] (the theme the
    front-theme-preference localStorage key and prefers-color-scheme feed).
    Resolved live on the signin page (raw/css-vars.json: resolved.app and
    resolved.appDark).
    companion.frontapp.com — Front's own messenger product, embedded on
    help.front.com and dev.frontapp.com — loads the full Froyo build
    (@layer tokens in src.*.css): the same semantic vocabulary under the
    Panda-CSS --colors-* prefix on :where(:root, :host), its light/dark ramp
    values (--colors-light-*/--colors-dark-*/--colors-alpha-*), and the
    scale tables --sizes-*, --spacing-*, --font-sizes-*, --font-weights-*,
    --fonts-*, --line-heights-*, --letter-spacings-*, --radii-*, --shadows-*,
    --easings-*, --durations-*, --breakpoints-*, --blurs-*,
    --aspect-ratios-*, --animations-* and --borders-* — with the 205-name
    [data-theme="light"]/[data-theme="dark"] semantic repointings.

  help.front.com (Front's Knowledge Base product) resolves an inline :root
  block (--primary-color, --gray-shade*, --article-*, button and field vars);
  dev.frontapp.com is the ReadMe vendor platform, kept as measured
  component.dev.* evidence only.

Deterministic: same inputs, byte-identical output.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
CL = json.loads((RAW / "css-classes.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())["components"]

SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. "
    "core.marketing palette/type/radii/motion and the violet, light and gray "
    "sets are declared values from front.com's compiled design layer "
    "(raw/css-classes.json), each role sourced to its class and "
    "[data-theme] scope. core.primitive is the app shell's resolved "
    "--color-primitive-* ramps; core.froyo is the full Froyo build the "
    "Companion messenger ships (declared in companion.frontapp.com's "
    "@layer tokens, var() aliases resolved through the same sheet). The app "
    "and dark sets are the signin shell's resolved --color-* semantics, "
    "companion/companionDark its [data-theme] semantics, help the Knowledge "
    "Base's :root block. component.* holds measured computed-style and "
    "geometry evidence, each leaf sourced to the component and state it was "
    "read from."),
    "core": {}, "violet": {}, "light": {}, "gray": {}, "app": {}, "dark": {},
    "companion": {}, "companionDark": {}, "help": {}, "component": {}}


def lit(value, ty, src, desc):
    return {"value": value, "type": ty, "source": src, "description": desc}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def st(comp, state):
    return C[comp]["states"][state]["style"]


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False


def meas(comp, state, prop, ty, path, desc):
    # A mapped component must exist: a missing key means the builder drifted
    # from the capture, and its tokens would silently never be emitted.
    if comp not in C:
        raise KeyError(f"{path}: required component '{comp}' is not in raw/components-computed.json")
    if not have(comp, state, prop):
        return
    via = C[comp]["states"][state].get("via") or "at rest"
    emit_leaf(SPEC["component"], path, lit(st(comp, state)[prop], ty,
                          f"measured {comp} ({state}, {via}) on {C[comp].get('url', C[comp].get('page', ''))}",
                          desc))


def meas_dim(comp, state, prop, path, desc):
    meas(comp, state, prop, "dimension", path, desc)


def meas_color(comp, state, prop, path, desc):
    meas(comp, state, prop, "color", path, desc)


# ---------------------------------------------------------------- helpers

def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 6:
            return "#" + h
        r, g, b, a = (int(h[i:i + 2], 16) for i in (0, 2, 4, 6))
        return "rgba(%d, %d, %d, %g)" % (r, g, b, round(a / 255, 4))
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return "rgba(%d, %d, %d, %g)" % (int(float(r)), int(float(g)), int(float(b)), float(a))
    return v


# The marketing classes, indexed two ways: unscoped utility rules (the
# palette, the type/space scales) and the theme-scoped semantic rules.
CLASS_DECL = {}          # ".bg-violet-100" -> declarations
THEME_DECL = {}          # ("theme-white", ".text-primary") -> declarations
THEME_NAME = {"theme-dark-violet": "violet", "theme-white": "light", "theme-gray": "gray"}
for rule in CL["rules"]:
    for sel in rule["selector"].split(","):
        sel = sel.strip()
        m = re.fullmatch(r'\[data-theme="(theme-[a-z-]+)"\]\s+(\.[a-z0-9-]+)', sel)
        if m:
            THEME_DECL[(m.group(1), m.group(2))] = rule["declarations"]
        elif re.fullmatch(r"\.[a-z0-9-]+", sel):
            CLASS_DECL.setdefault(sel, rule["declarations"])

CLS_SRC = "declared class `{sel}` in front.com's marketing stylesheet (raw/css-classes.json)"
CLS_TH_SRC = "declared class `{sel}` under [data-theme=\"{theme}\"] in front.com's marketing stylesheet (raw/css-classes.json)"

# The companion (Froyo) token layer: the :where(:root, :host) declarations
# plus the [data-theme] semantic repointings, all from companion.frontapp.com's
# @layer tokens sheet. var() references resolve inside the same table.
FROOT, FTHEME = {}, {}
for rule in V.get("theme", []):
    if "companion" not in rule.get("file", ""):
        continue
    sel = rule.get("selector", "")
    if sel.startswith(":where"):
        FROOT.update(rule.get("properties") or {})
    elif '[data-theme="light"]' in sel:
        FTHEME.setdefault("light", {}).update(rule.get("properties") or {})
    elif '[data-theme="dark"]' in sel:
        FTHEME.setdefault("dark", {}).update(rule.get("properties") or {})


def fres(name, theme=None, seen=()):
    """Resolve a Froyo declaration: literal, or var(--other) chains.

    A [data-theme] scope re-declares the semantic names it repaints, so a
    themed lookup checks that scope's table before the :where(:root) one —
    reading root alone resolves every theme to the light declarations.
    """
    v = FTHEME.get(theme, {}).get(name) if theme else None
    if v is None:
        v = FROOT.get(name)
    if v is None:
        return None
    v = v.strip()
    m = re.fullmatch(r"var\((--[a-z0-9-]+)\)", v)
    if m and m.group(1) not in seen:
        return fres(m.group(1), theme, seen + (name,))
    return v


FROYO_SRC = "declared `{name}` in Front's Froyo token sheet (@layer tokens in companion.frontapp.com/assets/src.*.css, loaded by Front's own messenger embed; raw/css-vars.json)"

# The app shell's resolved values: resolved.app / resolved.appDark.
APP_L = {n: v.get("value", v.get("raw")) for n, v in V.get("resolved", {}).get("app", {}).items()}
APP_D = {n: v.get("value", v.get("raw")) for n, v in V.get("resolved", {}).get("appDark", {}).items()}
HELP = {n: v.get("value", v.get("raw")) for n, v in V.get("resolved", {}).get("help", {}).items()}


def nest(root, dotted, leaf):
    node = root
    parts = dotted.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


def _is_leaf(d):
    return isinstance(d, dict) and ("var" in d or "value" in d)


LEAF_KEYS = {"value", "var", "type", "source", "description", "resolve", "responsive", "angle"}


def emit_leaf(root, dotted, leaf):
    """Write `leaf` at the dotted path.

    A captured name can be both a leaf and the parent of longer names:
    --color-bg-fill-brand sits beside --color-bg-fill-brand-hover/-pressed/
    -disabled. When a leaf and a group must share a node, the leaf moves
    inside the group under the first free of `default`, `base`, `self`, so
    the base value and each variant stay separate tokens instead of the
    variants silently attaching to (and being dropped from) the base leaf.
    """
    node = root
    parts = dotted.split(".")
    for p in parts[:-1]:
        nxt = node.get(p)
        if nxt is None:
            nxt = node[p] = {}
        elif _is_leaf(nxt):
            nxt = node[p] = {"default": nxt}
        node = nxt
    last = parts[-1]
    if last in node and not _is_leaf(node[last]):
        for key in ("default", "base", "self"):
            if key not in node[last]:
                node[last][key] = leaf
                return
        raise ValueError(f"{dotted}: no free key to hold the leaf beside its group")
    if _is_leaf(node.get(last)):
        raise ValueError(f"{dotted}: duplicate token path")
    node[last] = leaf


def check_leaves(node, path=""):
    """A token leaf must never also hold child tokens — the mixed shape is
    what build() would silently truncate, losing every variant."""
    if _is_leaf(node):
        extra = set(node) - LEAF_KEYS
        if extra:
            raise ValueError(f"{path}: token leaf also holds child tokens {sorted(extra)}")
        return
    for k, v in node.items():
        if isinstance(v, dict) and not k.startswith("_"):
            check_leaves(v, f"{path}.{k}" if path else k)


# ------------------------------------------------------------- marketing
# palette: the unscoped colour utilities. .bg-<hue>-<step> is canonical;
# text-/border-/from-/via-/to- utilities confirm the same values.

pal = SPEC["core"].setdefault("palette", {})
PAL_RE = re.compile(r"\.(bg|text|border|from|via|to|fill|stroke)-([a-z]+)-(\d+)")
seen = {}
for sel, decl in sorted(CLASS_DECL.items()):
    m = PAL_RE.fullmatch(sel)
    if not m or "background-color" not in decl and "color" not in decl and "border-color" not in decl:
        continue
    kind, hue, step = m.groups()
    val = decl.get("background-color") or decl.get("color") or decl.get("border-color")
    if val is None or (hue, step) in seen:
        continue
    seen[(hue, step)] = sel
    nest(pal, f"{hue}.{step}", lit(norm_color(val), "color", CLS_SRC.format(sel=sel),
        f"The declared `{sel}` step of the marketing {hue} ramp."))

# Type ramp: the .text-* role classes each declare the full quad.
TYPE_RE = re.compile(r"\.text-(display\d|h[1-4]|p[12]|caption[12]|micro[123])$")
fsizes = SPEC["core"].setdefault("font", {}).setdefault("size", {})
flines = SPEC["core"]["font"].setdefault("lineHeight", {})
ftrack = SPEC["core"]["font"].setdefault("tracking", {})
fwts = SPEC["core"]["font"].setdefault("weight", {})
for sel, decl in sorted(CLASS_DECL.items()):
    m = TYPE_RE.fullmatch(sel)
    if not m:
        continue
    role = m.group(1)
    src = CLS_SRC.format(sel=sel)
    if "font-size" in decl:
        fsizes[role] = lit(decl["font-size"], "dimension", src, f"The declared `{sel}` font-size.")
    if "line-height" in decl:
        flines[role] = lit(decl["line-height"], "dimension", src, f"The declared `{sel}` line-height.")
    if "letter-spacing" in decl:
        v = decl["letter-spacing"]
        flines_tr = lit(v, "other" if not v.endswith("px") else "dimension", src, f"The declared `{sel}` letter-spacing.")
        ftrack[role] = flines_tr
    if "font-weight" in decl:
        fwts[role] = lit(int(decl["font-weight"]), "fontWeight", src, f"The declared `{sel}` font-weight.")

# The utility companions (.font-size-Npx ramps etc.) that are not covered by
# a role name.
for sel, decl in sorted(CLASS_DECL.items()):
    m = re.fullmatch(r"\.font-size-(\d+(?:\.\d+)?)", sel)
    if m and "font-size" in decl:
        fsizes.setdefault("u" + m.group(1), lit(decl["font-size"], "dimension", CLS_SRC.format(sel=sel), f"The declared `{sel}` utility."))
    m = re.fullmatch(r"\.font-line-height-(\d+(?:\.\d+)?)", sel)
    if m and "line-height" in decl:
        flines.setdefault("u" + m.group(1), lit(decl["line-height"], "dimension", CLS_SRC.format(sel=sel), f"The declared `{sel}` utility."))
    m = re.fullmatch(r"\.font-weight-(\d+)", sel)
    if m and "font-weight" in decl:
        fwts.setdefault("u" + m.group(1), lit(int(decl["font-weight"]), "fontWeight", CLS_SRC.format(sel=sel), f"The declared `{sel}` utility."))

# Radius + motion scales.
radii = SPEC["core"].setdefault("radius", {})
for sel, decl in sorted(CLASS_DECL.items()):
    m = re.fullmatch(r"\.rounded-(\d+)", sel)
    if m and "border-top-left-radius" in decl:
        radii[m.group(1)] = lit(decl["border-top-left-radius"], "dimension", CLS_SRC.format(sel=sel), f"The declared `{sel}` radius.")
motion = SPEC["core"].setdefault("motion", {})
durs = motion.setdefault("duration", {})
for sel, decl in sorted(CLASS_DECL.items()):
    m = re.fullmatch(r"\.duration-(\d+)", sel)
    if m and "transition-duration" in decl:
        durs[m.group(1)] = lit(decl["transition-duration"], "duration", CLS_SRC.format(sel=sel), f"The declared `{sel}` duration.")
eases = motion.setdefault("easing", {})
for sel, decl in sorted(CLASS_DECL.items()):
    m = re.fullmatch(r"\.ease-([a-z-]+)", sel)
    if m and "transition-timing-function" in decl:
        eases[m.group(1)] = lit(decl["transition-timing-function"], "cubicBezier", CLS_SRC.format(sel=sel), f"The declared `{sel}` easing.")

# Marketing font families: the Suisse faces the @font-face blocks serve; the
# stacks come from measured components (the classes do not name them).
fam = SPEC["core"]["font"].setdefault("family", {})
FAMILY_SRC = "Front's self-hosted Suisse faces (@font-face in the marketing stylesheet, raw/css-vars.json fonts[]), measured on {where}"
for key, comp, where, desc in [
    ("intl", "hero-h1", "the hero headline", "Suisse Intl — every heading, control and body on the marketing site; system fallbacks."),
    ("intlMono", None, None, "Suisse Intl Mono — figures and code on the marketing site."),
    ("works", None, None, "Suisse Works — the serif display face on editorial sections."),
]:
    entry = None
    if comp and have(comp, "default", "fontFamily"):
        entry = lit(st(comp, "default")["fontFamily"], "fontFamily",
                    FAMILY_SRC.format(where=where), desc + " Measured stack.")
    elif key == "intl":
        entry = lit('"Suisse Intl", sans-serif', "fontFamily", FAMILY_SRC.format(where="nothing reachable"), desc + " Stack not read on a captured element — family name declared, fallbacks guessed; treat the fallbacks as a placeholder.")
    if entry:
        fam[key] = entry
# App + KB faces, declared in their own sheets.
if have("app-continue", "default", "fontFamily"):
    fam["app"] = lit(st("app-continue", "default")["fontFamily"], "fontFamily",
                     'measured app-continue (default) — the app shell\'s "Indivisible" stack (Inter fallbacks)', "The product shell's family, measured on the Continue button.")
if HELP.get("--font"):
    fam["knowledgeBase"] = var("--font", "fontFamily", resolve="help", description="The help centre's declared --font stack (CustomFont plus system fallbacks; resolved on help.front.com).")

# ------------------------------------------------- marketing theme roles
ROLE_MAP = {
    ".surface-l0": ("surface.l0", "color"), ".surface-l1": ("surface.l1", "color"),
    ".surface-l2": ("surface.l2", "color"), ".surface-l3": ("surface.l3", "color"),
    ".surface-outer": ("surface.outer", "color"), ".surface-highlight": ("surface.highlight", "color"),
    ".surface-l1-hover": ("surface.l1Hover", "color"), ".surface-l1-active": ("surface.l1Active", "color"),
    ".text-primary": ("text.primary", "color"), ".text-primary-inactive": ("text.primaryInactive", "color"),
    ".text-secondary": ("text.secondary", "color"), ".text-secondary-inactive": ("text.secondaryInactive", "color"),
    ".button-surface": ("button.surface", "color"), ".button-surface-active": ("button.surfaceActive", "color"),
    ".button-surface-disabled": ("button.surfaceDisabled", "color"),
    ".button-surface-outline-hover": ("button.surfaceOutlineHover", "color"),
    ".button-surface-outline-active": ("button.surfaceOutlineActive", "color"),
    ".button-surface-outline-disabled": ("button.surfaceOutlineDisabled", "color"),
    ".button-surface-tab-hover": ("button.surfaceTabHover", "color"),
    ".button-border": ("button.border", "shadow"), ".button-border-hover": ("button.borderHover", "shadow"),
    ".button-border-disabled": ("button.borderDisabled", "shadow"),
    ".button-text-default": ("button.textDefault", "color"), ".button-text-inverted": ("button.textInverted", "color"),
    ".button-text-disabled": ("button.textDisabled", "color"),
    ".button-text-outline-active": ("button.textOutlineActive", "color"),
    ".button-text-tab": ("button.textTab", "color"), ".button-text-tab-active": ("button.textTabActive", "color"),
}


def shadow_layers(v):
    layers = []
    for layer in re.split(r"(?<!\d),\s+(?=rgba?\(|#)", str(v)):
        m = re.fullmatch(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\))\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(\s+inset)?", layer.strip())
        if not m:
            return None
        col, x, y, blur, spread, inset = m.groups()
        d = {"color": norm_color(col), "offsetX": f"{x}px", "offsetY": f"{y}px", "blur": f"{blur}px", "spread": f"{spread}px"}
        if inset:
            d["inset"] = True
        layers.append(d)
    return layers


for (theme, sel), decl in sorted(THEME_DECL.items()):
    if (sel not in ROLE_MAP):
        continue
    tset = THEME_NAME[theme]
    path, ty = ROLE_MAP[sel]
    prop = "background-color" if "background-color" in decl else ("box-shadow" if "box-shadow" in decl else "color")
    src = CLS_TH_SRC.format(sel=sel, theme=theme)
    if ty == "shadow":
        layers = shadow_layers(decl[prop])
        leaf = lit(layers if layers else decl[prop], "shadow" if layers else "other", src,
                   f"The declared `{sel}` under [data-theme=\"{theme}\"] — Front paints its hairline borders as 1px inset shadows.")
    else:
        leaf = lit(norm_color(decl[prop]), "color", src, f"The declared `{sel}` under [data-theme=\"{theme}\"].")
    nest(SPEC[tset], path, leaf)

# --------------------------------------------------------- froyo (core)
FROYO_NS = {
    "sizes": ("froyo.size", "other"), "spacing": ("froyo.spacing", "dimension"),
    "font-sizes": ("froyo.fontSize", "dimension"), "line-heights": ("froyo.lineHeight", "other"),
    "letter-spacings": ("froyo.tracking", "other"), "font-weights": ("froyo.fontWeight", "fontWeight"),
    "fonts": ("froyo.fontFamily", "fontFamily"), "radii": ("froyo.radius", "dimension"),
    "shadows": ("froyo.shadow", "other"), "easings": ("froyo.easing", "cubicBezier"),
    "durations": ("froyo.duration", "duration"), "breakpoints": ("froyo.breakpoint", "dimension"),
    "blurs": ("froyo.blur", "dimension"), "aspect-ratios": ("froyo.aspectRatio", "other"),
    "animations": ("froyo.animation", "other"), "borders": ("froyo.border", "other"),
}
for name, raw in sorted(FROOT.items()):
    m = re.fullmatch(r"--colors-(light|dark|alpha)-([a-z]+)-?([a-z0-9-]*)", name)
    if m:
        mode, hue, rest = m.groups()
        v = fres(name)
        if v is None:
            continue
        if mode == "alpha":
            m2 = re.fullmatch(r"(black|white)-?(.*)", hue)
            if m2:
                path = f"froyo.ramp.alpha.{m2.group(1)}.{rest or m2.group(2)}"
            else:
                path = f"froyo.ramp.alpha.{hue}.{rest}"
        else:
            path = f"froyo.ramp.{mode}.{hue}.{rest}"
        emit_leaf(SPEC["core"], path, lit(norm_color(v), "color", FROYO_SRC.format(name=name) + ("; `var()` alias resolved through the same sheet" if raw != v else ""),
            f"The declared `{name}` — the Froyo {mode} {hue} ramp."))
        continue
    m = re.fullmatch(r"--colors-(.*)", name)
    if m:
        # semantic defaults live in the root block too; they re-declare under
        # [data-theme], handled by the companion sets — skip here.
        continue
    for ns, (path, ty) in FROYO_NS.items():
        if name.startswith(f"--{ns}-"):
            key = name[len(f"--{ns}-"):]
            v = fres(name)
            if v is None:
                break
            if ty == "fontWeight" and re.fullmatch(r"\d+", str(v)):
                v = int(v)
            emit_leaf(SPEC["core"], f"{path}.{key.replace('-', '.')}", lit(v, ty, FROYO_SRC.format(name=name), f"The declared `{name}`."))
            break

# ------------------------------------------------- app / dark shell sets
def emit_color_tree(root, resolved, srctag):
    for name in sorted(resolved):
        if name.startswith("--color-primitive-"):
            continue  # ramps live under core.primitive
        rest = name[len("--color-"):]
        leaf = var(name, "color", description=f"The resolved `{name}` on the {srctag} surface.")
        emit_leaf(root, "color." + rest.replace("-", "."), leaf)


emit_color_tree(SPEC["app"], APP_L, "app.frontapp.com signin shell (light theme)")
emit_color_tree(SPEC["dark"], APP_D, "app.frontapp.com signin shell ([data-theme=dark])")

prim = SPEC["core"].setdefault("primitive", {})
for name in sorted(APP_L):
    m = re.fullmatch(r"--color-primitive-([a-z]+)-(.*)", name)
    if not m:
        continue
    hue, rest = m.groups()
    if hue == "alpha":
        m2 = re.fullmatch(r"(black|white)-(.*)", rest)
        path = f"alpha.{m2.group(1)}.{m2.group(2)}" if m2 else "alpha." + rest
    else:
        path = f"{hue}.{rest}"
    emit_leaf(prim, path, lit(norm_color(APP_L[name]), "color",
        f"resolved `--color-primitive-{hue}-{rest}` on app.frontapp.com's signin shell (raw/css-vars.json: resolved.app)",
        f"The app shell's `{hue}` primitive ramp step."))

# ------------------------------------------------- companion semantic sets
for tset, mode in (("companion", "light"), ("companionDark", "dark")):
    for name, raw in sorted(FTHEME.get(mode, {}).items()):
        m = re.fullmatch(r"--colors-(.*)", name)
        if not m:
            continue
        v = fres(name, mode)
        if v is None:
            continue
        alias = "" if raw == v else f" = `{raw.strip()}` → resolved through the same sheet"
        emit_leaf(SPEC[tset], "color." + m.group(1).replace("-", "."),
             lit(norm_color(v), "color",
                 f"declared `{name}` under [data-theme=\"{mode}\"] in the Froyo token sheet{alias}",
                 f"The Froyo semantic `{name}` under [data-theme=\"{mode}\"]."))

# ------------------------------------------------------------- help set
for name in sorted(HELP):
    rest = name.lstrip("-").replace("--", "-")
    if not rest:
        continue
    v = HELP[name]
    ty = "color" if re.fullmatch(r"#([0-9a-fA-F]{3,8})|rgba?\([^)]*\)", v.strip()) else ("fontFamily" if name == "--font" else "other")
    emit_leaf(SPEC["help"], re.sub(r"[^a-zA-Z0-9]+", ".", rest).strip(".").lower(),
         var(name, ty, description=f"The resolved `{name}` on help.front.com (Front's Knowledge Base product)."))

# ------------------------------------------------------- measured component
meas_dim("mkt-header", "default", "height", "marketing.header.height", "The marketing header's measured height.")
meas_color("mkt-header", "default", "backgroundColor", "marketing.header.bg", "The marketing header's painted background.")
meas_dim("nav-try", "default", "height", "marketing.button.header.height", "The header \"Try for free\" button's measured height.")
meas_color("nav-try", "default", "backgroundColor", "marketing.button.header.bg", "Its painted fill (the button-primary-link-header layer).")
meas_color("nav-try", "default", "color", "marketing.button.header.text", "Its label colour.")
meas_dim("nav-try", "default", "borderTopLeftRadius", "marketing.button.header.radius", "Its corner radius.")
meas_color("nav-demo", "default", "backgroundColor", "marketing.button.secondary.bg", "The \"Request a demo\" header button's painted fill.")
meas_color("nav-demo", "default", "color", "marketing.button.secondary.text", "Its label colour.")
# The hero ships one CTA — "Request demo", the citron pill on the plum field.
meas_dim("hero-cta", "default", "height", "marketing.button.hero.height", "The hero \"Request demo\" pill's measured height.")
meas_color("hero-cta", "default", "backgroundColor", "marketing.button.primary.bg", "Its painted fill (the citron violet.surface.highlight).")
meas_color("hero-cta", "hover", "backgroundColor", "marketing.button.primary.bgHover", "Its hover fill.")
meas_color("hero-cta", "pressed", "backgroundColor", "marketing.button.primary.bgActive", "Its :active fill (CDP-forced).")
meas_color("hero-cta", "default", "color", "marketing.button.primary.text", "Its label colour (the violet.button.textDefault ink).")
meas_dim("hero-cta", "default", "borderTopLeftRadius", "marketing.button.primary.radius", "Its corner radius.")
meas_dim("hero-cta", "default", "paddingLeft", "marketing.button.primary.paddingX", "Its horizontal padding.")
meas_dim("billing-toggle", "default", "width", "marketing.billingSwitch.width", "The pricing billing switch's measured width.")
meas_dim("billing-toggle", "default", "height", "marketing.billingSwitch.height", "Its measured height.")
meas_color("faq-item", "opened", "color", "marketing.faq.openColour", "The FAQ disclosure's label colour while open.")
meas_dim("nav-panel", "default", "borderTopLeftRadius", "marketing.megaMenu.radius", "The mega-menu panel's corner radius.")
meas_color("nav-panel", "default", "backgroundColor", "marketing.megaMenu.bg", "The mega-menu panel's fill.")
meas_dim("plan-card", "default", "borderTopLeftRadius", "marketing.planCard.radius", "A plan card's corner radius.")
meas_color("plan-card", "default", "backgroundColor", "marketing.planCard.bg", "A plan card's fill.")
meas_color("plan-cta", "default", "backgroundColor", "marketing.planCta.bg", "A plan CTA's fill.")
meas_color("footer", "default", "backgroundColor", "marketing.footer.bg", "The footer's painted background.")
meas_color("footer-link", "default", "color", "marketing.footer.link", "A footer link's colour.")

# The demo and signup forms' measured geometry.
meas_dim("demo-email", "default", "height", "forms.demoEmail.height", "The demo form work-email field's measured height.")
meas_color("demo-email", "default", "backgroundColor", "forms.demoEmail.bg", "Its painted fill.")
meas_dim("demo-field", "default", "height", "forms.demoField.height", "The company-size select's measured height.")
meas_dim("demo-submit", "default", "height", "forms.demoSubmit.height", "The demo submit's measured height.")
meas_color("demo-submit", "default", "backgroundColor", "forms.demoSubmit.bg", "Its painted fill.")
meas_dim("signup-field", "default", "height", "forms.signupField.height", "The marketing signup field's measured height.")
meas_dim("signup-submit", "default", "height", "forms.signupSubmit.height", "The marketing signup submit's measured height.")
meas_color("signup-submit", "default", "backgroundColor", "forms.signupSubmit.bg", "Its painted fill.")
meas_dim("signup-app-submit", "default", "height", "forms.signupAppSubmit.height", "The app shell signup submit's measured height.")
meas_color("signup-app-submit", "default", "backgroundColor", "forms.signupAppSubmit.bg", "Its painted fill.")

# The app shell's painted values (measured, to confirm the resolved vars).
meas_color("app-panel", "default", "backgroundColor", "app.panel.bg", "The signin card's painted fill.")
meas_dim("app-panel", "default", "borderTopLeftRadius", "app.panel.radius", "The signin card's corner radius.")
meas_dim("app-email", "default", "height", "app.field.height", "The signin e-mail field's measured height.")
meas_color("app-email", "default", "backgroundColor", "app.field.bg", "Its painted fill.")
meas_color("app-email", "default", "borderTopColor", "app.field.border", "Its border colour.")
meas_dim("app-email", "default", "borderTopLeftRadius", "app.field.radius", "Its corner radius.")
meas_color("app-continue", "default", "backgroundColor", "app.button.primary.bg", "The Continue button's painted fill (the --color-bg-fill-brand role).")
meas_color("app-continue", "hover", "backgroundColor", "app.button.primary.bgHover", "Its hover fill.")
meas_color("app-continue", "default", "color", "app.button.primary.text", "Its label colour.")
meas_dim("app-continue", "default", "height", "app.button.primary.height", "Its measured height.")
meas_dim("app-continue", "default", "borderTopLeftRadius", "app.button.primary.radius", "Its corner radius.")
# Dark shell measurements live under component.appDark.*, read on the
# signin-dark pass (appd-* components).
meas_color("appd-panel", "default", "backgroundColor", "appDark.panel.bg", "The signin card's fill under [data-theme=dark].")
meas_dim("appd-email", "default", "height", "appDark.field.height", "The signin e-mail field's height under [data-theme=dark].")
meas_color("appd-email", "default", "backgroundColor", "appDark.field.bg", "Its fill under dark.")
meas_color("appd-continue", "default", "backgroundColor", "appDark.button.primary.bg", "The Continue button's fill under [data-theme=dark].")
meas_color("appd-continue", "default", "color", "appDark.button.primary.text", "Its label colour under dark.")

# Help centre measured geometry.
meas_dim("help-search", "default", "height", "help.search.height", "The help search field's measured height.")
meas_color("help-search", "default", "backgroundColor", "help.search.bg", "Its painted fill.")
meas_dim("help-card", "default", "borderTopLeftRadius", "help.card.radius", "A help category card's corner radius.")
meas_color("help-card", "default", "backgroundColor", "help.card.bg", "Its painted fill.")

# Dev portal (ReadMe vendor): measured only.
meas_color("dev-header", "default", "backgroundColor", "dev.header.bg", "The developer portal header's fill (ReadMe platform).")
meas_color("dev-side-link", "default", "color", "dev.sidebar.link", "A docs sidebar link's colour.")
meas_color("devref-code", "default", "backgroundColor", "dev.code.bg", "A code block's painted fill.")
meas_color("devref-code", "default", "color", "dev.code.text", "Its text colour.")
meas_dim("m-topbar", "default", "height", "marketing.mobile.headerHeight", "The 390px mobile header's measured height.")
meas_dim("m-menu-btn", "default", "width", "marketing.mobile.burgerWidth", "The burger button's measured width at 390px.")

# Every leaf written is a real leaf: a node carrying both a value and child
# tokens is the shape that silently drops captured variants downstream.
for _set, _tree in SPEC.items():
    if not _set.startswith("_"):
        check_leaves(_tree, _set)

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "var" not in d and "value" not in d else 1


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
