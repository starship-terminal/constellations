#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

craftwork.design's public signed-out surface is a Next.js app on Tailwind
utilities whose sheets declare a real semantic layer on :root, harvested
into raw/css-vars.json under BOTH painted themes (the nav toggle flips
data-theme and repaints the page):

  --background-*   brand #cafc00 lime (+hover/pressed), primary #1e1e1e
                   (near-black fill, inverts to #fff in dark), secondary
                   #efefef, field #fafafa, plate, ghost, surface-1..5,
                   reversed, circa blue, destructive-*
  --text-icons-*   primary/secondary/tertiary/destructive/info/reversed
  --stroke-*       10% ink hairline + destructive/info strokes
  --category-*     the 12-hue asset-category palette (+*-soft washes)
  --catalog-tint-* the 12-tint library chips (+*-plate)
  --status-*/--indicators-*/--viz-*  status, indicators and chart colours
  --controls-*     switch/indicator roles; --cw-toast-* the toast skin
  --home-hero-*    the hero's easing, durations, stagger and glow colours
  --text-gradient-*/--gradient-*     declared gradient recipes

Those become {"var": ...} leaves resolved by build_tokens.py. Measured
computed values (raw/components-computed.json) pin what the vars do not:

  type       Euclid Circular A (Craftwork's own face, served same-origin)
             at 600 for every heading (68px hero, 40px prices, 38px mobile),
             400/500 for UI text at 13-16px
  buttons    #1e1e1e fill + white text, 8px nav pill, 10px hero/login pills,
             46px hero CTAs, the 9999px search pill on #fafafa
  surfaces   white page, #161616 promo bar, #efefef secondary/disabled fill,
             7% ink library-row wash
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
RD = V.get("resolved", {}).get("dark", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. craftwork.design's "
    "public surface is a Next.js app whose declared --background-*/"
    "--text-icons-*/--stroke-* semantic layer (raw/css-vars.json, resolved "
    "under both painted data-theme passes) is var-referenced wherever it "
    "names a value, and measured computed values "
    "(raw/components-computed.json) cover the rest: the Euclid Circular A "
    "ramp (68/40/38px 600 headings, 13-16px UI), the #1e1e1e button fills "
    "on white text, the 8/10px control radii and 9999px search pill, the "
    "#161616 promo bar and the category/tint palettes."),
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


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
if have("hero-h1", "default", "fontFamily"):
    fam["euclid"] = {"value": st("hero-h1", "default")["fontFamily"], "type": "fontFamily",
                     "source": "computed fontFamily of hero-h1 default (raw/components-computed.json); the @font-face blocks are served same-origin (raw/css-vars.json fonts)",
                     "description": "Euclid Circular A (Craftwork's own licensed face, served as euclidCircularA*WebS webfonts) — every heading and all UI text."}
if "--toastify-font-family" in R:
    fam["system-fallback"] = var("--toastify-font-family", "fontFamily",
                                 source="css-var --toastify-font-family resolved (raw/css-vars.json)",
                                 description="The sans-serif fallback the vendor toast layer declares.")
weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, val, desc in [
    ("regular", "nav-link", "400", "Measured 400 — body and nav text."),
    ("medium", "hero-cta", "500", "Measured 500 — buttons, card titles, promo text."),
    ("semibold", "hero-h1", "600", "Measured 600 — every heading, the logo wordmark."),
]:
    if have(comp, "default", "fontWeight"):
        weights[key] = {"value": st(comp, "default")["fontWeight"], "type": "fontWeight",
                        "source": f"computed fontWeight of {comp} default (raw/components-computed.json)",
                        "description": desc}

# ------------------------------------------------------- declared palettes

def emit_group(root, prefixes, group_desc):
    out = {}
    for n in sorted(R):
        if RL.get(n, {}).get("kind") != "color":
            continue
        for p in prefixes:
            if n.startswith(p):
                key = n[len(p):]
                out[key] = var(n, "color",
                               source=f"css-var {n} resolved (raw/css-vars.json)",
                               description=f"{group_desc} {key}.")
    return out

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, n, desc in [
    ("lime", "--background-brand", "The #cafc00 signature lime — the brand fill."),
    ("lime-hover", "--background-brand-hover", "Declared hover #bceb00."),
    ("lime-pressed", "--background-brand-pressed", "Declared pressed #a4cc00."),
    ("circa", "--background-circa", "The #063bf5 circa blue."),
    ("copied", "--background-copied", "The #4ade80 copied-state green."),
    ("orange", "--orange", "Declared #f55611 orange."),
    ("other-blue", "--other-blue", "Declared #063af5."),
    ("other-pink", "--other-pink", "Declared #c32cf8."),
    ("logo", "--logo", "The wordmark colour (black light, white dark)."),
]:
    if n in R:
        brand[key] = var(n, "color",
                         source=f"css-var {n} resolved (raw/css-vars.json)",
                         description=desc)
cat = SPEC["core"].setdefault("color", {}).setdefault("category", {})
cat.update(emit_group(cat, ["--category-"], "Declared asset-category hue"))
tint = SPEC["core"].setdefault("color", {}).setdefault("catalog-tint", {})
tint.update(emit_group(tint, ["--catalog-tint-"], "Declared library tint"))
viz = SPEC["core"].setdefault("color", {}).setdefault("viz", {})
viz.update(emit_group(viz, ["--viz-"], "Declared chart colour"))
status = SPEC["core"].setdefault("color", {}).setdefault("status", {})
status.update(emit_group(status, ["--status-", "--indicators-"], "Declared status/indicator colour"))
toast = SPEC["core"].setdefault("color", {}).setdefault("toast", {})
toast.update(emit_group(toast, ["--cw-toast-"], "Declared toast colour"))
grad = SPEC["core"].setdefault("gradient", {})
for n in sorted(R):
    if n.startswith("--text-gradient-") or n.startswith("--gradient-"):
        grad[n.lstrip("-").replace("--", "-").replace("gradient-", "").replace("text-", "text-")] = var(n, "other",
            source=f"css-var {n} resolved (raw/css-vars.json)",
            description=f"Declared gradient recipe {n}.")

# --------------------------------------------------------- semantic light

sem = SPEC["light"].setdefault("color", {})
for key, n, group, desc in [
    ("primary", "--background-primary", "action", "The #1e1e1e primary button fill (inverts to #fff in dark)."),
    ("primary-hover", "--background-primary-hover", "action", "Declared #383838 hover."),
    ("primary-pressed", "--background-primary-pressed", "action", "Declared #000 pressed."),
    ("secondary", "--background-secondary", "action", "The #efefef secondary/disabled fill (hero secondary, Send code)."),
    ("secondary-hover", "--background-secondary-hover", "action", "Declared #e0e0e0 hover."),
    ("field", "--background-field", "background", "The #fafafa field fill (the search pill)."),
    ("ghost", "--background-ghost", "action", "The #fff ghost fill."),
    ("plate", "--background-plate", "background", "The #f4f4f4 plate."),
    ("surface-1", "--background-surface-1", "background", "Declared surface-1 #fff."),
    ("surface-3", "--background-surface-3", "background", "Declared surface-3 #fafafa."),
    ("surface-4", "--background-surface-4", "background", "Declared surface-4 70% translucent — the cookie notice fill."),
    ("catalog-fill", "--catalog-fill", "background", "The 4% ink catalog row fill."),
    ("catalog-fill-active", "--catalog-fill-active", "background", "The 7% ink active row fill (measured on library-row)."),
    ("text-primary", "--text-icons-primary", "text", "The #000 primary text/icon."),
    ("text-secondary", "--text-icons-secondary", "text", "The #606060 secondary text (nav links, muted)."),
    ("text-tertiary", "--text-icons-tertiary", "text", "The #999 tertiary text (footer small print, placeholders)."),
    ("text-destructive", "--text-icons-destructive", "text", "The #f54911 destructive text."),
    ("text-info", "--text-icons-info", "text", "The #c42df9 info text."),
    ("text-reversed", "--text-icons-reversed", "text", "White text on primary fills."),
    ("stroke-primary", "--stroke-primary", "border", "The 10% ink hairline."),
    ("stroke-destructive", "--stroke-destructive", "border", "The #ffdbcc destructive stroke."),
    ("stroke-info", "--stroke-info", "border", "The #e7ccfc info stroke."),
    ("switcher", "--controls-switcher-background", "background", "The #fafafa switcher track."),
    ("switcher-active", "--controls-switcher-active", "action", "The #fff active switcher thumb."),
    ("indicator", "--controls-indicator", "background", "The #e0e0e0 control indicator."),
]:
    if n in R:
        sem.setdefault(group, {})[key] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)
# measured pairings the declarations alias oddly
try:
    sem.setdefault("background", {})["promo"] = {"value": norm_color(st("promo-banner", "default")["backgroundColor"]), "type": "color",
        "source": "computed backgroundColor of promo-banner default (raw/components-computed.json)",
        "description": "The #161616 promo/countdown bar fill."}
    sem.setdefault("text", {})["on-primary"] = {"value": norm_color(st("connect-cta", "default")["color"]), "type": "color",
        "source": "computed color of connect-cta default (raw/components-computed.json)",
        "description": "The white text the #1e1e1e pills paint."}
except KeyError:
    pass

# ---------------------------------------------------------- semantic dark

sem_d = SPEC["dark"].setdefault("color", {})
for key, n, group, desc in [
    ("primary", "--background-primary", "action", "Dark: the primary fill inverts to #fff."),
    ("text-primary", "--text-icons-primary", "text", "Dark: primary text inverts to #fff."),
    ("text-secondary", "--text-icons-secondary", "text", "Dark secondary text."),
    ("stroke-primary", "--stroke-primary", "border", "Dark hairline (white alpha)."),
    ("surface-1", "--background-surface-1", "background", "Dark surface-1."),
    ("secondary", "--background-secondary", "action", "Dark secondary fill."),
    ("field", "--background-field", "background", "Dark field fill."),
    ("brand", "--background-brand", "action", "The #cafc00 lime stays put in dark."),
]:
    if n in RD:
        sem_d.setdefault(group, {})[key] = {"var": n, "type": "color",
            "source": f"css-var {n} resolved under data-theme=dark (raw/css-vars.json)",
            "description": desc}

# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, desc in [
    ("hero", "hero-h1", "The home hero's measured 68px/70.72px Euclid 600."),
    ("price", "plan-price", "The 40px plan price figure (measured via textStyle)."),
    ("hero-mobile", "m-hero", "The mobile hero's measured 38px."),
    ("card-title", "product-card", "The 18px 500 product-card title."),
    ("body", "nav", "The 16px UI/body size."),
    ("small", "library-row", "The 14px small UI size (library rows, plan copy)."),
    ("tiny", "promo-banner", "The 13px promo-bar size."),
]:
    prop = "fontSize"
    v = ts(comp, "default", prop) if comp in C else None
    if v:
        ty[key] = {"value": v, "type": "fontSize",
                   "source": f"computed fontSize of {comp} default (raw/components-computed.json)",
                   "description": desc}
try:
    ty.setdefault("hero-lh", {})["value"] = ts("hero-h1", "default", "lineHeight")
    ty["hero-lh"]["type"] = "other"
    ty["hero-lh"]["source"] = "computed lineHeight of hero-h1 default (raw/components-computed.json)"
    ty["hero-lh"]["description"] = "The hero's 70.72px line-height (~1.04)."
except KeyError:
    pass

# ------------------------------------------------------------------ shape

radii = SPEC["core"].setdefault("radius", {})
for key, comp, prop, desc in [
    ("nav", "connect-cta", "borderTopLeftRadius", "The 8px nav-pill radius."),
    ("control", "hero-cta", "borderTopLeftRadius", "The 10px control radius — hero CTAs, login buttons, library rows."),
    ("pill", "search-field", "borderTopLeftRadius", "The 9999px search pill."),
]:
    if have(comp, "default", prop):
        v = st(comp, "default")[prop]
        # %g keeps a fractional radius; a computed rounded-full (3.35544e+07px, the CSS maximum) is
        # written 9999px, the kit's pill radius.
        n = float(v[:-2]) if v.endswith("px") else None
        fv = ("9999px" if n > 9999 else "%gpx" % n) if n is not None else v
        radii[key] = {"value": fv, "type": "dimension",
                      "source": f"computed {prop} of {comp} default (raw/components-computed.json)",
                      "description": desc}
bw = SPEC["core"].setdefault("border", {})
if "--stroke-primary" in R:
    bw.setdefault("hairline", {})["width"] = {"value": "1px", "type": "dimension",
        "source": "declared --stroke-primary pairs with 1px borders across the sheets",
        "description": "The 10% ink hairline width."}

# ------------------------------------------------------------- elevation

sh = SPEC["core"].setdefault("shadow", {})
if "--cw-toast-shadow" in R:
    s = R["--cw-toast-shadow"]
    layers = re.findall(r"(rgba?\([\d.,\s]+\))\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)( inset)?", s)
    if layers:
        sh["toast"] = {"value": [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp, "inset": bool(i)} for a, x, y, bl, sp, i in layers],
                       "type": "shadow",
                       "source": "css-var --cw-toast-shadow resolved (raw/css-vars.json)",
                       "description": "The declared toast elevation: 0 12 32 -8 28% + 0 2 6 12% ink."}

# ---------------------------------------------------------------- spacing

sp = SPEC["core"].setdefault("spacing", {})
for key, comp, prop, desc in [
    ("nav-h", "nav", "height", "The 60px nav bar height."),
    ("promo-h", "promo-banner", "height", "The 36px promo bar height."),
]:
    if have(comp, "default"):
        v = st(comp, "default").get(prop)
        if v and v not in ("0px", "auto"):
            sp[key] = {"value": v, "type": "dimension",
                       "source": f"computed {prop} of {comp} default (raw/components-computed.json)",
                       "description": desc}

# ----------------------------------------------------------------- motion

mo = SPEC["core"].setdefault("motion", {})
for key, n, desc in [
    ("hero-ease", "--home-hero-ease", "The hero's cubic-bezier(.2,0,0,1) ease."),
    ("hero-horizon", "--home-hero-horizon-duration", "The hero horizon's 1.8s drift."),
    ("hero-rise", "--home-hero-rise-duration", "The hero rise's .9s."),
    ("hero-stagger", "--home-hero-stagger", "The 90ms hero stagger."),
]:
    if n in R:
        mo[key] = var(n, "other",
                      source=f"css-var {n} resolved (raw/css-vars.json)",
                      description=desc)

# ------------------------------------------------------------- components

# Components the capture read from the wrong element (README, What is not here).
WRONG_ELEMENT = {"plan-card": "a Rebuild FlowSuite promo card", "m-menu-button": "the mobile Search button"}
comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("button-height-nav", "connect-cta", "default", "height", "dimension", "The 30px nav CTA."),
    ("button-height-large", "hero-cta", "default", "height", "dimension", "The 46px hero/login buttons."),
    ("search-pill-width", "search-field", "default", "width", "dimension", "The 350px nav search pill."),
    ("library-row", "library-row", "default", "height", "dimension", "The 34px library list row."),
    ("filter-field", "components-filter", "default", "height", "dimension", "The 30px catalog filter field."),
    ("login-field", "login-field", "default", "height", "dimension", "The 46px OTP email field."),
    ("plan-card", "plan-card", "default", "width", "dimension", "547px. Read from the wrong element: a \"Rebuild FlowSuite\" promo card, not a plan card; recapture needed."),
    ("product-card", "product-card", "default", "width", "dimension", "The 363px product card."),
    ("menu-button", "m-menu-button", "default", "width", "dimension", "44px. Read from the wrong element: the mobile Search button, not the menu button; recapture needed."),
    ("theme-toggle", "theme-toggle", "default", "width", "dimension", "The 32px theme toggle."),
    ("faq-row", "faq-row", "default", "height", "dimension", "The 68px FAQ accordion row."),
    ("promo-text", "promo-banner", "default", "fontSize", "dimension", "The 13px promo text."),
    ("nav-link-size", "nav-link", "default", "fontSize", "dimension", "Nav link 16px."),
]:
    if have(cname, state):
        v = st(cname, state).get(prop)
        if v and v not in ("0px", "auto"):
            src = f"computed {prop} of {cname} {state} (raw/components-computed.json)"
            if cname in WRONG_ELEMENT:
                src += "; read from the wrong element (%s); recapture needed" % WRONG_ELEMENT[cname]
            comp[name] = {"value": v, "type": ty_, "source": src, "description": desc}
# measured state move: the primary pill hover
try:
    comp.setdefault("button", {})["state-move"] = {
        "type": "other",
        "value": {
            "default": {"backgroundColor": st("hero-cta", "default")["backgroundColor"],
                        "color": st("hero-cta", "default")["color"]},
            "hover": {"backgroundColor": st("hero-cta", "hover")["backgroundColor"],
                      "color": st("hero-cta", "hover")["color"]},
            "pressed": {"backgroundColor": st("hero-cta", "pressed")["backgroundColor"],
                        "color": st("hero-cta", "pressed")["color"]},
        },
        "source": "computed styles of hero-cta default/hover/pressed (raw/components-computed.json)",
        "description": "The primary pill's state track: #1e1e1e at rest, the declared #383838 hover and #000 pressed."}
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
