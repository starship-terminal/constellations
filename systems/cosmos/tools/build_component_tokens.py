#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

cosmos.so's public signed-out surface is a Next.js/Tailwind app whose
sheets declare a real dual semantic layer: --color-* primitives, resolved
--light-* / --dark-* semantic sets and unprefixed --background-color-*,
--text-color-*, --border-color-* and --ring-color-* aliases, all harvested
into raw/css-vars.json. Those become {"var": ...} leaves resolved by
build_tokens.py. Measured computed values
(raw/components-computed.json) pin what the vars do not: Those become
{"var": ...} leaves resolved by build_tokens.py. Everything else is
**measured computed values** from raw/components-computed.json:

  surfaces   the white page and card fills, the paper-gray element tile,
             the elevation-gray disabled button
  ink        lab(3.64 0 0) near-black text, button fills, active borders
  type       cosmosOracle throughout — 72/88px display, 15-16px UI, 700
             headings vs 500 controls
  shape      rounded-full pills (3.36e7px) everywhere, 3px element tiles,
             25% QR card, the declared --radius-* ramp
  states     the auth Next button's measured disabled->enabled inversion
  chrome     92px desktop header, 68px mobile header, 276px footer
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. copy.ai's "
    "public surface is a Webflow site whose small --colors--* declaration "
    "(raw/css-vars.json — the brand palette plus the legacy "
    "--old-swatches--* set) is var-referenced where it names the brand and "
    "neutral values, and measured computed values "
    "(raw/components-computed.json) cover the ink/white neutrals, the "
    "#693ee0 action purple and its auth-host ramp, the black-button "
    "hover-to-purple state move, the hairline borders, the inset shadows, "
    "ABC Normal and Inter type, the 4/4.5/5/8/40/48px radii and the "
    "0.1-0.4s control motion. The 'dark' set is the ink banner and the "
    "deep-purple card bands the light pages paint, not a user toggle."),
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


def find_var(value, contains=None):
    """First resolved var whose value matches; prefer a --color-* name."""
    best = None
    for n, v in R.items():
        if v == value and (contains is None or contains in n):
            if n.startswith("--color-"):
                return n
            best = best or n
    return best


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
if have("hero-h1", "default", "fontFamily"):
    fam["oracle"] = {"value": st("hero-h1", "default")["fontFamily"], "type": "fontFamily",
                     "source": "computed fontFamily of hero-h1 default (raw/components-computed.json); the @font-face blocks are served same-origin (raw/css-vars.json fonts)",
                     "description": "cosmosOracle — the single family the whole public surface paints, display and UI alike."}
weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, var_name, desc in [
    ("light", "--font-weight-light", "Declared 300."),
    ("book", "--font-weight-book", "Declared 350."),
    ("regular", "--font-weight-normal", "Declared 400 — body and UI text."),
    ("medium", "--font-weight-medium", "Declared 500 — nav links, button labels, footer links."),
    ("semibold", "--font-weight-semibold", "Declared 600."),
    ("bold", "--font-weight-bold", "Declared 700 — display headings (hero-h1, seq-h1, m-hero all measure 700)."),
    ("extrabold", "--font-weight-extrabold", "Declared 800."),
    ("black", "--font-weight-black", "Declared 900."),
]:
    if var_name in R:
        weights[key] = var(var_name, "fontWeight",
                         source=f"css-var {var_name} resolved (raw/css-vars.json)",
                         description=desc)

# ------------------------------------------------------- declared palette

palette = SPEC["core"].setdefault("color", {}).setdefault("palette", {})
for n in sorted(R):
    if n.startswith("--color-gray-") or n.startswith("--color-blue-") or \
       n.startswith("--color-green-") or n.startswith("--color-amber-") or \
       n.startswith("--color-orange-") or n.startswith("--color-red-") or \
       n.startswith("--color-warm-gray-"):
        key = n[len("--color-"):]
        palette[key] = var(n, "color",
                           source=f"css-var {n} resolved (raw/css-vars.json)",
                           description=f"Declared primitive {key}.")
brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, n, desc in [
    ("black", "--color-black", "Declared black lab(0 0 0)."),
    ("white", "--color-white", "Declared white lab(100 0 0)."),
    ("paper", "--color-paper", "Declared paper lab(96.648 0.43 1.2) — the warm off-white card surface."),
    ("arena", "--color-arena", "Declared arena brand black."),
    ("pinterest", "--color-pinterest", "Declared pinterest brand red."),
    ("tumblr", "--color-tumblr", "Declared tumblr brand navy."),
]:
    if n in R:
        brand[key] = var(n, "color",
                         source=f"css-var {n} resolved (raw/css-vars.json)",
                         description=desc)

# --------------------------------------------------- semantic light/dark

def emit_semantic(theme):
    root = SPEC[theme]
    p = f"--{theme}-"
    for group in ("background", "text", "border", "button", "hover", "shadow"):
        node = root.setdefault("color", {}).setdefault(group, {})
        for n in sorted(R):
            if n.startswith(p + group + "-"):
                key = n[len(p + group + "-"):]
                node[key] = var(n, "color",
                                source=f"css-var {n} resolved (raw/css-vars.json); the public surface declares both --light-* and --dark-* sets, data-theme paints light",
                                description=f"Declared {theme} {group}/{key}.")
emit_semantic("light")
emit_semantic("dark")

# unprefixed semantic aliases (the resolved paint layer)
sem = SPEC["light"].setdefault("color", {}).setdefault("alias", {})
for n in sorted(R):
    for pre, group in (("--background-color-", "background"),
                       ("--text-color-", "text"),
                       ("--border-color-", "border"),
                       ("--ring-color-", "ring")):
        if n.startswith(pre):
            sem.setdefault(group, {})[n[len(pre):]] = var(
                n, "color",
                source=f"css-var {n} resolved (raw/css-vars.json)",
                description=f"Resolved {group}/{n[len(pre):]} alias.")

# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for n in sorted(R):
    if n.startswith("--text-") and not n.endswith(("--line-height", "--letter-spacing")) and \
       not n.startswith("--text-color-"):
        key = n[len("--text-"):]
        lh = R.get(n + "--line-height")
        ls = R.get(n + "--letter-spacing")
        desc = f"Declared type size {key}."
        if lh or ls:
            desc += f" Declared line-height {lh}, letter-spacing {ls}."
        ty[key] = var(n, "fontSize",
                      source=f"css-var {n} resolved (raw/css-vars.json)",
                      description=desc)

# measured display sizes the ramp does not pin exactly
for key, comp, desc in [
    ("hero", "hero-h1", "The home hero's measured 72px/72px 700 display."),
    ("sequence", "seq-h1", "Sequence's measured 88px display heading."),
    ("hero-mobile", "m-hero", "The mobile hero's measured 32px 700 display."),
]:
    if have(comp, "default", "fontSize"):
        s = st(comp, "default")
        ty[key] = {"value": s["fontSize"], "type": "fontSize",
                   "lineHeight": s.get("lineHeight"),
                   "source": f"computed fontSize of {comp} default (raw/components-computed.json)",
                   "description": desc}

# ------------------------------------------------------------------ shape

radii = SPEC["core"].setdefault("radius", {})
for n in sorted(R):
    if n.startswith("--radius-"):
        radii[n[len("--radius-"):]] = var(
            n, "dimension",
            source=f"css-var {n} resolved (raw/css-vars.json)",
            description=f"Declared radius {n[len('--radius-'):]}.")
try:
    fv = st("signup-cta", "default")["borderTopLeftRadius"]
    # %g keeps 2.5px as 2.5px (int() truncated it); a computed rounded-full (3.35544e+07px, the CSS maximum)
    # is written 9999px as the kit writes a pill radius, never as an exact 33554400px.
    n = float(fv[:-2]) if fv.endswith("px") else None
    fv = ("9999px" if n > 9999 else "%gpx" % n) if n is not None else fv
    radii["full"] = {"value": fv, "type": "dimension",
                     "source": "computed borderTopLeftRadius of signup-cta default (raw/components-computed.json), %s" % st("signup-cta", "default")["borderTopLeftRadius"],
                     "description": "rounded-full computes to the CSS maximum 3.35544e+07px, written 9999px — every pill control (CTAs, tabs, menu button, Next)."}
    radii["card-quarter"] = {"value": st("qr-card", "default")["borderTopLeftRadius"], "type": "other",
                             "source": "computed borderTopLeftRadius of qr-card default (raw/components-computed.json)",
                             "description": "The QR-card's 25% radius."}
except KeyError:
    pass

# ------------------------------------------------------------- elevation

sh = SPEC["core"].setdefault("shadow", {})
if "--shadow-dynamic-island" in R:
    sh["dynamic-island"] = {"value": [
        {"color": "rgba(0, 0, 0, 0.15)", "offsetX": "0px", "offsetY": "6px", "blur": "44px", "spread": "0px", "inset": False},
        {"color": "rgba(0, 0, 0, 0.03)", "offsetX": "0px", "offsetY": "4px", "blur": "8px", "spread": "0px", "inset": False}],
        "type": "shadow",
        "source": "css-var --shadow-dynamic-island resolved (raw/css-vars.json), hex-alpha layers expanded",
        "description": "Declared floating-pill shadow 0 6 44 15% + 0 4 8 3% black."}
for key, n, desc in [
    ("primary", "--color-shadow-primary", "Declared 10% black shadow color."),
    ("secondary", "--color-shadow-secondary", "Declared 5% black."),
    ("tertiary", "--color-shadow-tertiary", "Declared 2.5% black."),
]:
    if n in R:
        sh.setdefault("color", {})[key] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)

# ---------------------------------------------------------------- spacing

sp = SPEC["core"].setdefault("spacing", {})
if "--spacing" in R:
    sp["base"] = var("--spacing", "dimension",
                     source="css-var --spacing resolved (raw/css-vars.json)",
                     description="Declared 0.25rem spacing unit.")
for key, comp, prop, desc in [
    ("header-x", "header", "paddingLeft", "Header side padding."),
    ("header-h", "header", "height", "Desktop header height (92px)."),
    ("m-header-h", "m-header", "height", "Mobile header height (68px)."),
]:
    if have(comp, "default"):
        v = st(comp, "default").get(prop)
        if v and v != "0px" and v != "auto":
            sp[key] = {"value": v, "type": "dimension",
                       "source": f"computed {prop} of {comp} default (raw/components-computed.json)",
                       "description": desc}

# ----------------------------------------------------------------- motion

mo = SPEC["core"].setdefault("motion", {})
for key, n in [("canvas-enter", "--animate-canvas-enter"), ("enter", "--animate-enter"),
               ("fade-in", "--animate-fade-in"), ("hero-enter", "--animate-hero-enter"),
               ("element-view", "--animate-element-view"), ("pulse", "--animate-pulse")]:
    if n in R:
        mo[key] = var(n, "other",
                      source=f"css-var {n} resolved (raw/css-vars.json)",
                      description=f"Declared animation {key}.")

# ------------------------------------------------------------- components

comp = SPEC["component"]
# Components the capture read from the wrong element (README, What to distrust).
WRONG_ELEMENT = {"hero-search": "the header's Log in / Sign up group, 204 x 58, not the hero search pill"}

for name, cname, state, prop, ty_, desc in [
    ("button-height-medium", "signup-cta", "default", "height", "dimension", "Header CTA height (48px)."),
    ("button-height-large", "auth-next", "default", "height", "dimension", "Auth Next / mobile sign-up height (56px)."),
    ("button-padding", "signup-cta", "default", "paddingLeft", "dimension", "CTA horizontal padding."),
    ("nav-link-size", "nav-link", "default", "fontSize", "dimension", "Nav link 15px/22."),
    ("field-height", "auth-input", "default", "height", "dimension", "Auth input height."),
    ("card-width-auth", "auth-card", "default", "width", "dimension", "Auth card width (344px)."),
    ("menu-button", "m-menu-button", "default", "width", "dimension", "Mobile menu button 44x44 hit area."),
    ("search-pill-height", "search-pill", "default", "height", "dimension", "Explore search pill height (56px)."),
    ("hero-search-height", "hero-search", "default", "height", "dimension", "Read from the wrong element: the header's Log in / Sign up group (204 x 58), not the hero search pill; recapture needed."),
    ("tab-height", "cat-tab", "default", "height", "dimension", "Category tab height (~40px)."),
]:
    if have(cname, state):
        v = st(cname, state).get(prop)
        if v and v not in ("0px", "auto"):
            src = f"computed {prop} of {cname} {state} (raw/components-computed.json)"
            if cname in WRONG_ELEMENT:
                src += "; read from the wrong element (%s); recapture needed" % WRONG_ELEMENT[cname]
            comp[name] = {"value": v, "type": ty_, "source": src, "description": desc}
# measured state move: disabled→enabled on the auth Next button
try:
    comp.setdefault("button", {})["state-move"] = {
        "type": "other",
        "value": {
            "disabled": {"backgroundColor": st("auth-next", "default")["backgroundColor"],
                         "color": st("auth-next", "default")["color"]},
            "enabled": {"backgroundColor": st("auth-next", "enabled")["backgroundColor"],
                        "color": st("auth-next", "enabled")["color"]},
        },
        "source": "computed styles of auth-next default vs enabled (raw/components-computed.json); enabled reached by typing into both fields, never submitted",
        "description": "The auth Next button's signature move: elevation-gray fill + tertiary text while disabled, inverting to ink fill + white text once both fields are filled."}
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
