#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

craft.do's public signed-out surface is a Next.js app on Tailwind v4
whose sheets declare a shadcn-style semantic layer on :root: --color-*
primitives plus --background/--card/--popover/--primary/--accent/--muted/
--destructive roles, --border/--ring/--input and the --sidebar-* set, all
harvested into raw/css-vars.json. Those become {"var": ...} leaves
resolved by build_tokens.py. Measured computed values
(raw/components-computed.json) pin what the vars do not: Those become
{"var": ...} leaves resolved by build_tokens.py. Everything else is
**measured computed values** from raw/components-computed.json:

  surfaces   the #fcf9f7 warm beige page, white cards/popovers/fields, the
             #fafafa sidebar set, the black footer panel
  ink        #030302 on everything — text, the black pill fills, the footer;
             the pills' text is white (measured; --primary-foreground oddly
             declares #030302)
  accent     the #427e8a teal, a #bb433a destructive and the --chart-1..5 set
  type       Untitled Serif 400 for every display heading (66/70/54px page
             titles, 48px mobile), Untitled Sans for UI (16px 400/500)
  shape      rounded-full pills (3.36e7px) on every CTA and the billing
             toggle, a 26px floating nav pill, 16/24px card radii
  states     the black CTA's 75%-ink hover; the 3px 6% ink focus ring
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
    fam["serif"] = {"value": st("hero-h1", "default")["fontFamily"], "type": "fontFamily",
                    "source": "computed fontFamily of hero-h1 default (raw/components-computed.json); the @font-face blocks are served same-origin (raw/css-vars.json fonts)",
                    "description": "Untitled Serif (Klim, licensed, not distributed) — every display heading, 400 weight only."}
if have("nav-link", "default", "fontFamily"):
    fam["sans"] = {"value": st("nav-link", "default")["fontFamily"], "type": "fontFamily",
                   "source": "computed fontFamily of nav-link default (raw/components-computed.json)",
                   "description": "Untitled Sans — all UI text, body and controls."}
if "--default-mono-font-family" in R:
    fam["mono"] = var("--default-mono-font-family", "fontFamily",
                      source="css-var --default-mono-font-family resolved (raw/css-vars.json)",
                      description="Declared mono fallback stack.")
weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, var_name, desc in [
    ("light", "--font-weight-light", "Declared 300."),
    ("regular", "--font-weight-normal", "Declared 400 — body and every display heading."),
    ("medium", "--font-weight-medium", "Declared 500 — buttons, nav pills, FAQ rows."),
    ("semibold", "--font-weight-semibold", "Declared 600."),
    ("bold", "--font-weight-bold", "Declared 700."),
    ("extrabold", "--font-weight-extrabold", "Declared 800."),
]:
    if var_name in R:
        weights[key] = var(var_name, "fontWeight",
                           source=f"css-var {var_name} resolved (raw/css-vars.json)",
                           description=desc)

# ------------------------------------------------------- declared palette

palette = SPEC["core"].setdefault("color", {}).setdefault("palette", {})
for n in sorted(R):
    if n.startswith("--color-"):
        key = n[len("--color-"):]
        palette[key] = var(n, "color",
                           source=f"css-var {n} resolved (raw/css-vars.json)",
                           description=f"Declared primitive {key}.")
brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, n, desc in [
    ("ink", "--color-black-900", "The #030302 ink — all text, the black CTA fills, the footer."),
    ("black", "--color-black", "Declared black #030302."),
    ("white", "--color-white", "Declared white — cards, popovers, inputs, the nav pill."),
    ("beige", "--color-beige", "The #fcf9f7 warm page beige (--background)."),
    ("accent", "--accent", "The #427e8a teal accent."),
    ("destructive", "--destructive", "The #bb433a destructive red."),
]:
    if n in R:
        brand[key] = var(n, "color",
                         source=f"css-var {n} resolved (raw/css-vars.json)",
                         description=desc)
charts = SPEC["core"].setdefault("color", {}).setdefault("chart", {})
for n in sorted(R):
    if re.fullmatch(r"--chart-\d", n):
        charts[n[len("--chart-"):]] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)",
            description=f"Declared chart colour {n}.")

# --------------------------------------------------------- semantic light

sem = SPEC["light"].setdefault("color", {})
for key, n, group, desc in [
    ("page", "--background", "background", "The #fcf9f7 warm beige page."),
    ("card", "--card", "background", "The #fff card surface."),
    ("popover", "--popover", "background", "The #fff popover surface."),
    ("input", "--input", "background", "The #fff field fill."),
    ("sidebar", "--sidebar", "background", "The #fafafa sidebar surface."),
    ("sidebar-accent", "--sidebar-accent", "background", "The #f5f5f5 sidebar accent."),
    ("muted", "--muted", "background", "The 4% ink muted fill."),
    ("primary", "--primary", "action", "The #030302 primary action fill."),
    ("secondary", "--secondary", "action", "The #fff secondary action fill."),
    ("accent", "--accent", "action", "The #427e8a teal accent."),
    ("destructive", "--destructive", "action", "The #bb433a destructive fill."),
    ("sidebar-primary", "--sidebar-primary", "action", "The #171717 sidebar primary."),
    ("foreground", "--foreground", "text", "The #030302 primary text."),
    ("card-foreground", "--card-foreground", "text", "Card text #030302."),
    ("popover-foreground", "--popover-foreground", "text", "Popover text #030302."),
    ("primary-foreground", "--primary-foreground", "text", "Declared #030302 (light surfaces read white text on the black pills — the measured pairing)."),
    ("accent-foreground", "--accent-foreground", "text", "Declared #030302."),
    ("secondary-foreground", "--secondary-foreground", "text", "Declared #030302."),
    ("muted-foreground", "--muted-foreground", "text", "The 50% ink muted text."),
    ("sidebar-foreground", "--sidebar-foreground", "text", "The #0a0a0a sidebar text."),
    ("sidebar-accent-foreground", "--sidebar-accent-foreground", "text", "The #171717 sidebar accent text."),
    ("sidebar-primary-foreground", "--sidebar-primary-foreground", "text", "The #fafafa text on sidebar primary."),
    ("border", "--border", "border", "The 9% ink hairline."),
    ("ring", "--ring", "border", "The 12% ink focus ring."),
    ("sidebar-border", "--sidebar-border", "border", "The #e5e5e5 sidebar border."),
    ("sidebar-ring", "--sidebar-ring", "border", "The #a1a1a1 sidebar ring."),
]:
    if n in R:
        sem.setdefault(group, {})[key] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)
# measured text pairings the declarations alias oddly
try:
    sem.setdefault("text", {})["on-primary"] = {"value": norm_color(st("try-cta", "default")["color"]), "type": "color",
        "source": "computed color of try-cta default (raw/components-computed.json)",
        "description": "The white text the black pills paint (declared --primary-foreground is #030302, so the pairing is measured here)."}
    sem.setdefault("text", {})["footer"] = {"value": norm_color(st("footer-link", "default")["color"]), "type": "color",
        "source": "computed color of footer-link default (raw/components-computed.json)",
        "description": "The white text inside the black footer."}
except KeyError:
    pass

# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for n in sorted(R):
    if re.fullmatch(r"--text-(xs|sm|base|lg|xl|\d+xl)", n):
        key = n[len("--text-"):]
        lh = R.get(n + "--line-height")
        desc = f"Declared type size {key}."
        if lh:
            desc += f" Declared line-height {lh}."
        ty[key] = var(n, "fontSize",
                      source=f"css-var {n} resolved (raw/css-vars.json)",
                      description=desc)
for key, comp, desc in [
    ("hero", "hero-h1", "The home hero's measured 66px serif."),
    ("page-title", "price-h1", "The 54px serif page headings (pricing, download, imagine)."),
    ("page-title-large", "learn-h1", "Learn's measured 70px serif."),
    ("price", "plan-price", "The serif price figure on plan cards."),
    ("hero-mobile", "m-hero", "The mobile hero's measured 48px."),
]:
    if have(comp, "default", "fontSize"):
        s = st(comp, "default")
        ty[key] = {"value": s["fontSize"], "type": "fontSize",
                   "source": f"computed fontSize of {comp} default (raw/components-computed.json)",
                   "description": desc}

# ------------------------------------------------------------------ shape

radii = SPEC["core"].setdefault("radius", {})
for key, n, desc in [
    ("default", "--radius", "Declared 10px base radius."),
    ("2xl", "--radius-2xl", "Declared 16px — cards, the mobile download pill."),
    ("3xl", "--radius-3xl", "Declared 24px — the team card and footer panel."),
    ("4xl", "--radius-4xl", "Declared 32px."),
]:
    if n in R:
        radii[key] = var(n, "dimension",
                         source=f"css-var {n} resolved (raw/css-vars.json)",
                         description=desc)
try:
    fv = st("try-cta", "default")["borderTopLeftRadius"]
    # %g keeps a fractional radius; a computed rounded-full (the CSS maximum) is written 9999px, the kit's pill.
    n = float(fv[:-2]) if fv.endswith("px") else None
    read = fv
    fv = ("9999px" if n > 9999 else "%gpx" % n) if n is not None else fv
    radii["full"] = {"value": fv, "type": "dimension",
                     "source": "computed borderTopLeftRadius of try-cta default (raw/components-computed.json)"
                               + (f"; the reading {read} is the browser's maximum radius, written as the kit's 9999px pill" if fv != read and fv == "9999px" else ""),
                     "description": "rounded-full computes to the CSS maximum — every pill control (CTAs, the billing toggle, platform buttons)."}
    radii["nav"] = {"value": st("header", "default")["borderTopLeftRadius"], "type": "dimension",
                    "source": "computed borderTopLeftRadius of header default (raw/components-computed.json)",
                    "description": "The floating nav pill's 26px radius."}
except KeyError:
    pass
bw = SPEC["core"].setdefault("border", {})
if "--border" in R:
    bw.setdefault("hairline", {})["width"] = {"value": "1px", "type": "dimension",
        "source": "Reconstruction: entered by hand at capture time; --border declares only the colour and no raw reading holds this width (the shadcn convention pairs it with 1px)",
        "description": "The 9% ink hairline width."}

# ------------------------------------------------------------- elevation

sh = SPEC["core"].setdefault("shadow", {})
try:
    s = st("team-card", "default")["boxShadow"]
    layers = re.findall(r"(rgba?\([\d.,\s]+\)|oklab?\([^)]+\))\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)( inset)?", s)
    layers = [l for l in layers if l[0] != "rgba(0, 0, 0, 0)"]
    if layers:
        sh["block"] = {"value": [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp, "inset": bool(i)} for a, x, y, bl, sp, i in layers],
                       "type": "shadow",
                       "source": "computed boxShadow of team-card default (raw/components-computed.json); read on the first element carrying .shadow-block, the 1400 x 1546 pricing section, not the TEAM card",
                       "description": "The .shadow-block utility's elevation. The capture read it on the pricing section, not on a card, so where cards paint it needs a recapture."}
except KeyError:
    pass
for key, n, desc in [
    ("drop-sm", "--drop-shadow-sm", "Declared 0 1 2 15% drop shadow."),
    ("drop-2xl", "--drop-shadow-2xl", "Declared 0 25 25 15% drop shadow."),
]:
    if n in R:
        sh.setdefault("drop", {})[key] = var(n, "other",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)
# the measured focus ring
try:
    s = st("faq-row", "focus-visible")["boxShadow"]
    layers = re.findall(r"(rgba?\([\d.,\s]+\)|oklab?\([^)]+\))\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)( inset)?", s)
    layers = [l for l in layers if l[0] != "rgba(0, 0, 0, 0)"]
    if layers:
        sh["focus-ring"] = {"value": [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp, "inset": bool(i)} for a, x, y, bl, sp, i in layers],
                            "type": "shadow",
                            "source": "computed boxShadow of faq-row focus-visible (raw/components-computed.json)",
                            "description": "The 3px 6% ink ring controls paint on keyboard focus."}
except KeyError:
    pass

# ---------------------------------------------------------------- spacing

sp = SPEC["core"].setdefault("spacing", {})
if "--spacing" in R:
    sp["base"] = var("--spacing", "dimension",
                     source="css-var --spacing resolved (raw/css-vars.json)",
                     description="Declared 4px spacing unit.")
cont = sp.setdefault("container", {})
for n in sorted(R):
    if n.startswith("--container-"):
        cont[n[len("--container-"):]] = var(n, "dimension",
            source=f"css-var {n} resolved (raw/css-vars.json)",
            description=f"Declared container {n[len('--container-'):]}.")
for key, comp, prop, desc in [
    ("header-h", "header", "height", "The floating nav pill height (52px)."),
    ("header-rad", "header", "borderTopLeftRadius", "The nav pill's 26px radius."),
]:
    if have(comp, "default"):
        v = st(comp, "default").get(prop)
        if v and v not in ("0px", "auto"):
            sp[key] = {"value": v, "type": "dimension",
                       "source": f"computed {prop} of {comp} default (raw/components-computed.json)",
                       "description": desc}

# ----------------------------------------------------------------- motion

mo = SPEC["core"].setdefault("motion", {})
for key, n in [("ping", "--animate-ping"), ("pulse", "--animate-pulse"), ("spin", "--animate-spin")]:
    if n in R:
        mo[key] = var(n, "other",
                      source=f"css-var {n} resolved (raw/css-vars.json)",
                      description=f"Declared animation {key}.")
for key, n in [("duration", "--default-transition-duration"), ("easing", "--default-transition-timing-function")]:
    if n in R:
        mo.setdefault("default", {})[key] = var(n, "other",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=f"Declared default transition {key}.")

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("button-height-nav", "try-cta", "default", "height", "dimension", "The 36px header CTA."),
    ("button-height-large", "hero-cta", "default", "height", "dimension", "The 48px hero/platform CTA."),
    ("toggle-segment", "billing-toggle", "default", "width", "dimension", "A billing-toggle segment (112px)."),
    ("menu-button", "m-menu-button", "default", "width", "dimension", "The 24px mobile menu glyph."),
    ("faq-row", "faq-row", "default", "height", "dimension", "The FAQ accordion row height."),
    ("nav-link-size", "nav-link", "default", "fontSize", "dimension", "Nav link 16px."),
]:
    if have(cname, state):
        v = st(cname, state).get(prop)
        if v and v not in ("0px", "auto"):
            comp[name] = {"value": v, "type": ty_,
                          "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                          "description": desc}
# measured state move: the black CTA's 75% ink hover
try:
    comp.setdefault("button", {})["state-move"] = {
        "type": "other",
        "value": {
            "default": {"backgroundColor": st("try-cta", "default")["backgroundColor"],
                        "color": st("try-cta", "default")["color"]},
            "hover": {"backgroundColor": st("try-cta", "hover")["backgroundColor"],
                      "color": st("try-cta", "hover")["color"]},
        },
        "source": "computed styles of try-cta default vs hover (raw/components-computed.json)",
        "description": "The black pill's signature move: the fill lifts to 75% ink on hover."}
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
