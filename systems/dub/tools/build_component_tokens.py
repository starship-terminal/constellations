#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

dub.co is three surfaces signed out. The Next.js marketing site (Tailwind v4 +
its own semantic token layer, served in /_next/static/immutable/chunks/*.css)
declares Dub's semantic set — --bg-default/muted/subtle/emphasis/inverted +
--bg-info/success/attention/warning/error, --border-muted/subtle/default/
emphasis, --content-inverted/muted/subtle/default/emphasis + the same status
hues, stored as RGB triples and painted with rgb(var(--x)) — plus a shadcn
layer (--background/--foreground/--muted/--card/--popover/--primary/
--secondary/--accent/--ring). The auth cards on /login and /register paint the
app.dub.co shell's light values in a plain ui-sans-serif system stack. The
Mintlify docs/help surface (/docs, /help) adds a second bundle — the --gray-50
..950 ramp, --font-inter/--font-paper-mono/--font-family-headings-custom,
--default-border-color and the --twoslash-* code vars — and carries the only
real theme toggle: a `dark` class on <html> (localStorage isDarkMode), the
same scope vars.mjs resolves as the `dark` pass. Those become {"var": ...}
leaves resolved per theme.

What the sheets never name is measured off raw/components-computed.json:

  neutrals    the Tailwind neutral ramp the marketing and auth surfaces paint
              (#0a0a0a ink, #171717 headings, #404040 nav text, #737373 muted,
              #a3a3a3 / #d4d4d4 / #e5e5e5 borders, #f5f5f5 / #fafafa fills,
              #000000 button fill) — compiled atomic classes, not variables
  washes      the docs surface's color-mix translucencies Chrome reports as
              oklab(): the 10% primary active-nav wash, the 3%/10% search-pill
              washes, the dark sidebar's white-10% divider
  type        Satoshi 48/55.2 w500 on marketing h1s (36/40 at 390), Satoshi
              36/40 w600 on docs h1s, Inter body/nav, ui-sans-serif on the
              app.dub.co auth shell, Paper Mono docs mono, GeistMono marketing
              code
  shape       8px buttons, 6px fields, 12px cards/nav items, 9999px search
              pill and theme toggle
  states      hover paints a 4px #e5e5e5 box-shadow halo on black CTAs; focus
              keeps the browser-default `auto 1px rgb(0, 95, 204)` outline on
              buttons, while fields take a black border + 1px black ring; docs
              focus ring is 1px #155dfc

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py) or
{"value": ..., "source": ...} for a measured value. The site paints two
themes: light everywhere signed out, dark on the docs/help surface through
its own theme toggle.
"""
import colorsys, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V.get("resolved", {})
RL = RES.get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. dub.co's marketing "
    "site and app.dub.co auth shell declare a semantic + shadcn token layer in "
    "their Next.js/Tailwind bundles and paint it light; the Mintlify docs/help "
    "surface adds the --gray ramp and the site's only real theme toggle (the "
    "html.dark scope resolved as the dark set). Declared variables become var "
    "leaves; the Tailwind neutral ramp, the oklab color-mix washes, the "
    "component geometry and the state values the atomic CSS never names are "
    "measured leaves from raw/components-computed.json."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        child = node.setdefault(p, {})
        if "var" in child or "value" in child or "$value" in child:
            # A leaf displaced by children keeps its own name under `base`:
            # `default` is a real token name in this tree (`--border-default`),
            # so parking the displaced leaf there silently overwrote the real
            # `*-default` token or let it erase the leaf.
            node[p] = {"base": child}
            child = node[p]
        node = child
    last = parts[-1]
    cur = node.get(last)
    if isinstance(cur, dict) and cur and not ("var" in cur or "value" in cur or "$value" in cur):
        node = cur
        last = "default" if node.get("default") is None else "base"
    return node, last


def emit(root, name, leaf):
    node, last = descend(root, name[2:].split("-"))
    old = node.get(last)
    if old is not None:
        raise ValueError(f"emit {name}: slot already holds {old!r}")
    node[last] = leaf


def hsl_triple(spec):
    """'0 0% 9%' — an H S% L% channel triple — resolved the way the browser
    paints it: '#171717'."""
    h, s, l = spec.split()
    r, g, b = colorsys.hls_to_rgb(float(h) / 360, float(l.rstrip("%")) / 100,
                                  float(s.rstrip("%")) / 100)
    return "#%02x%02x%02x" % (round(r * 255), round(g * 255), round(b * 255))


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


def shadow_layers(spec):
    """Parse 'rgba(...) x y blur sp, ...' into DTCG shadow layers, dropping fully transparent no-ops."""
    out = []
    for m in re.finditer(
            r"(rgba?\(\s*[\d.]+,?\s*[\d.]+,?\s*[\d.]+(?:,?\s*[\d.]+)?\)|#[0-9a-fA-F]{3,8})\s+"
            r"(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(?:\s+(-?[\d.]+)px)?", spec):
        col, x, y, bl, sp = m.groups()
        if col.startswith("rgba") and col.rstrip(")").endswith(", 0"):
            continue  # rgba(0,0,0,0) 0px 0px 0px 0px placeholders Tailwind emits
        out.append({"color": norm_color(col), "offsetX": f"{x}px", "offsetY": f"{y}px",
                    "blur": f"{bl}px", "spread": f"{sp or 0}px"})
    return out


def comp_radius(comp, state):
    """The painted radius on or under the component."""
    try:
        pr = next((n.get("radius") for n in C[comp]["states"][state].get("paint", [])
                   if n.get("radius") and n["radius"] != "0px"), None)
    except KeyError:
        return None
    return pr


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("display", "hero-title", "default",
     "Satoshi (Fontshare variable): every marketing headline, 48px on desktop. The served stack."),
    ("body", "nav-link", "default",
     "Inter: the marketing body, nav and button stack, self-hosted woff2."),
    ("docs-body", "docs-sidebar", "default",
     "Inter on the Mintlify docs surface (served from /_mintlify/assets/fonts/inter/)."),
    ("auth", "login-card", "default",
     "The plain system stack the app.dub.co auth shell paints (no webfont on the card)."),
]:
    if have(comp, state, "fontFamily"):
        fam[key] = {"value": st(comp, state)["fontFamily"], "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
if "--font-family-headings-custom" in R:
    fam["docs-display"] = var("--font-family-headings-custom", "fontFamily",
        description="The docs surface's declared heading stack (Satoshi + system fallbacks).")
if "--font-paper-mono" in R:
    fam["mono"] = var("--font-paper-mono", "fontFamily",
        description="Paper Mono: the docs surface's code font (Mintlify bundle).")
fam["mono-marketing"] = {
    "value": '"GeistMono", ui-monospace, SFMono-Regular, Roboto Mono, Menlo, Monaco, '
             'Liberation Mono, DejaVu Sans Mono, Courier New, monospace',
    "type": "fontFamily",
    "source": "css-var --font-geist-mono, declared on the next/font variable class "
              "(._tsFxa_variable), not resolved on :root (raw/css-vars.json theme bin)",
    "description": "GeistMono: the marketing surface's code font."}

# ------------------------------------------------------------- neutrals

# The marketing/auth surfaces paint the Tailwind neutral ramp through atomic
# classes — never declared as variables — so each step is a measured value,
# sourced from the component that paints it.
neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, hexv, comp, state, prop, desc in [
    ("black", None, "nav-cta", "default", "backgroundColor",
     "Pure black: the button fill, nav-cta border and primary action."),
    ("white", None, "email-field", "default", "backgroundColor",
     "Pure white: fields, the auth card, bordered buttons."),
    ("50", "#fafafa", None, None, None,
     "Neutral 50: --background, the marketing field and plan-card fill."),
    ("100", "#f5f5f5", None, None, None,
     "Neutral 100: --muted, subtle fills, disabled-submit fill."),
    ("200", "#e5e5e5", None, None, None,
     "Neutral 200: --border, secondary-button borders and the 4px CTA hover halo."),
    ("300", "#d4d4d4", None, None, None,
     "Neutral 300: --border-default, field and demo-panel borders."),
    ("400", "#a3a3a3", None, None, None,
     "Neutral 400: --border-emphasis/--content-muted, strong borders and placeholder text."),
    ("500", "#737373", None, None, None,
     "Neutral 500: --muted-foreground/--content-subtle, muted text."),
    ("600", "#525252", None, None, None,
     "Neutral 600: hero lede and secondary body text."),
    ("700", "#404040", None, None, None,
     "Neutral 700: --content-default, nav-link body text."),
    ("800", "#262626", None, None, None,
     "Neutral 800: --content-emphasis-adjacent ink, hero-cta hover fill, badge text."),
    ("900", "#171717", None, None, None,
     "Neutral 900: --content-emphasis/--bg-inverted, headings and inverted fills."),
    ("950", "#0a0a0a", None, None, None,
     "Neutral 950: --foreground, the default body ink."),
]:
    if comp:
        v = norm_color(st(comp, state)[prop])
        src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
    else:
        v = hexv
        src = "computed styles across the measured components (raw/components-computed.json); " \
              "the same value the shadcn/semantic var of the role resolves to"
    neutral[key] = {"value": v, "type": "color", "source": src, "description": desc}

# --------------------------------------------------------- docs gray ramp
# The Mintlify bundle's --gray-50..950 is theme-independent (same on both
# scopes): the docs chrome, h1s and dividers paint it.

gray = SPEC["core"].setdefault("color", {}).setdefault("gray", {})
for n in ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]:
    vname = f"--gray-{n}"
    if vname in R:
        gray[n] = var(vname, "color",
                      description=f"Docs gray ramp step {n} ({R[vname]}): headings, sidebar text, dividers and the dark field steps.")

# ----------------------------------------------------------------- brand

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, vname, desc in [
    ("primary", "--color-primary", "Dub blue #155dfc: the docs accent — active nav items, focus rings, links."),
    ("blue-600", "--color-blue-600", "Tailwind blue 600 #2563eb (declared in the shared theme)."),
    ("emerald-500", "--color-emerald-500", "Emerald 500 #00bc7d (declared)."),
    ("green-400", "--color-green-400", "Green 400 #4ade80 (declared)."),
    ("green-600", "--color-green-600", "Green 600 #16a34a (declared)."),
]:
    if vname in R:
        brand[key] = var(vname, "color", description=desc)
# the named docs-field constants (same on both scopes)
for key, vname, desc in [
    ("canvas-light", "--background-light", "The #ffffff docs light field constant."),
    ("canvas-dark", "--background-dark", "The #090b10 docs dark field constant (the dark Copy-page button paints it)."),
]:
    if vname in R:
        brand[key] = var(vname, "color", description=desc)

# ------------------------------------------------- measured docs washes
# Chrome reports Mintlify's color-mix translucencies as oklab().

wash = SPEC["core"].setdefault("color", {}).setdefault("wash", {})
for key, comp, state, prop, desc in [
    ("primary-10", "docs-nav-item", "default", "backgroundColor",
     "The ~10% Dub-blue wash the active docs nav item paints (both themes)."),
    ("ink-3", "docs-search", "default", "backgroundColor",
     "The 3% ink wash on the light docs search pill."),
    ("ink-10", "docs-search", "hover", "backgroundColor",
     "The 10% ink wash the light search pill paints on hover."),
    ("ink-4", "docs-theme", "default", "backgroundColor",
     "The 4% ink wash on the light theme toggle."),
    ("white-3", "dk-docs-search", "default", "backgroundColor",
     "The 3% white wash on the dark docs search pill."),
    ("white-10", "dk-docs-sidebar", "default", "paint",
     "The 10% white divider line inside the dark docs sidebar."),
]:
    v = painted(comp, state) if prop == "paint" else st(comp, state).get(prop)
    # for the white-10 divider the element itself paints nothing; take the
    # divider layer from the sidebar's painted children
    if key == "white-10":
        v = next((p["bg"] for p in C[comp]["states"][state].get("paint", [])
                  if p.get("bg") and "sidebar-nav-group-divider" in (p.get("node") or "")), v)
    if v and v != "transparent" and v != "rgba(0, 0, 0, 0)":
        wash[key] = {"value": norm_color(v), "type": "color",
                     "source": (f"painted layer under {comp} {state}" if prop == "paint"
                                else f"computed {prop} of {comp} {state}") +
                               " (raw/components-computed.json)",
                     "description": desc}

# -------------------------------------------------------------------- roles

ALIAS = "role alias over the core palette"
DECLARED = "declared semantic/shadcn var in the site's stylesheets"
DECLARED_DOCS = "declared var in the Mintlify docs bundle"

light = SPEC["light"]

# shadcn layer (marketing + app.dub.co share the declarations)
for name, desc in [
    ("--background", "The page field (#fafafa)."),
    ("--foreground", "Default body ink (#0a0a0a)."),
    ("--card", "Card field (#fefefe)."),
    ("--card-foreground", "Card ink (#0a0a0a)."),
    ("--muted", "Muted fill (#f5f5f5)."),
    ("--muted-foreground", "Muted text (#737373)."),
    ("--popover", "Popover field (#ffffff)."),
    ("--popover-foreground", "Popover ink (#272727)."),
    ("--primary", "Primary action (#155dfc)."),
    ("--primary-foreground", "Text on primary (#fafafa)."),
    ("--secondary", "Secondary fill (#f5f5f5)."),
    ("--secondary-foreground", "Secondary ink (#171717)."),
    ("--accent", "Accent fill (#f0f0f0)."),
    ("--accent-foreground", "Accent ink (#171717)."),
    ("--ring", "Ring (#a3a3a3)."),
    ("--border", "Default border (#e5e5e5)."),
    ("--tooltip-foreground", "Tooltip ink (#ffffff)."),
]:
    if name in R:
        emit(light, name, {"var": name, "type": "color", "source": DECLARED, "description": desc})

# Dub's own semantic layer
for name, desc in [
    ("--bg-default", "Default surface (#ffffff)."),
    ("--bg-muted", "Muted surface (#fafafa)."),
    ("--bg-subtle", "Subtle surface (#f5f5f5)."),
    ("--bg-emphasis", "Emphasis surface (#e5e5e5)."),
    ("--bg-inverted", "Inverted surface (#171717)."),
    ("--bg-info", "Info surface (#dbeafe)."),
    ("--bg-success", "Success surface (#dcfce7)."),
    ("--bg-attention", "Attention surface (#ffedd5)."),
    ("--bg-warning", "Warning surface (#fef9c3)."),
    ("--bg-error", "Error surface (#fee2e2)."),
    ("--content-inverted", "Inverted text (#ffffff)."),
    ("--content-muted", "Muted text (#a3a3a3)."),
    ("--content-subtle", "Subtle text (#737373)."),
    ("--content-default", "Default text (#404040)."),
    ("--content-emphasis", "Emphasis text (#171717)."),
    ("--content-info", "Info text (#2563eb)."),
    ("--content-success", "Success text (#16a34a)."),
    ("--content-attention", "Attention text (#ea580c)."),
    ("--content-warning", "Warning text (#ca8a04)."),
    ("--content-error", "Error text (#dc2626)."),
    ("--border-muted", "Muted border (#f5f5f5)."),
    ("--border-subtle", "Subtle border (#e5e5e5)."),
    ("--border-default", "Default border (#d4d4d4)."),
    ("--border-emphasis", "Emphasis border (#a3a3a3)."),
]:
    if name in R:
        emit(light, name, {"var": name, "type": "color", "source": DECLARED, "description": desc})

# docs-bundle roles (Mintlify)
for name, desc in [
    ("--default-border-color", "The docs hairline (#eef0f5, gray-100)."),
    ("--twoslash-border-color", "Twoslash code border."),
    ("--twoslash-cursor-color", "Twoslash cursor."),
    ("--twoslash-error-bg", "Twoslash error fill."),
    ("--twoslash-error-color", "Twoslash error text."),
    ("--twoslash-highlighted-bg", "Twoslash highlighted line fill."),
    ("--twoslash-highlighted-border", "Twoslash highlighted line border."),
    ("--twoslash-popup-bg", "Twoslash popup field."),
    ("--twoslash-tag-annotate-bg", "Twoslash annotate tag fill."),
    ("--twoslash-tag-annotate-color", "Twoslash annotate tag text."),
    ("--twoslash-tag-bg", "Twoslash tag fill."),
    ("--twoslash-tag-color", "Twoslash tag text."),
    ("--twoslash-tag-warn-bg", "Twoslash warn tag fill."),
    ("--twoslash-tag-warn-color", "Twoslash warn tag text."),
    ("--twoslash-underline-color", "Twoslash underline (currentColor)."),
    ("--twoslash-unmatched-color", "Twoslash unmatched text."),
    ("--twoslash-warn-bg", "Twoslash warn fill."),
    ("--twoslash-warn-color", "Twoslash warn text."),
]:
    if name in R:
        emit(light, name, {"var": name, "type": "color", "source": DECLARED_DOCS, "description": desc})
# the docs popup shadow is a shadow shorthand, not a colour
if "--twoslash-popup-shadow" in R:
    layers = shadow_layers(R["--twoslash-popup-shadow"])
    if layers:
        emit(light, "--twoslash-popup-shadow", {"value": layers, "type": "shadow",
             "source": "css-var --twoslash-popup-shadow (light)",
             "description": "Twoslash popup shadow."})

# measured/aliased light roles
emit(light, "--action-primary-bg", {"value": "{color.neutral.black}", "type": "color",
    "source": ALIAS, "description": "The black button fill (nav Sign up, hero Start for free, auth submit)."})
emit(light, "--action-primary-bg-hover", {"value": "{color.neutral.800}", "type": "color",
    "source": "computed backgroundColor of hero-cta hover (raw/components-computed.json)",
    "description": "The #262626 the black CTA lifts to on hover."})
emit(light, "--action-primary-text", {"value": "{color.neutral.white}", "type": "color",
    "source": ALIAS, "description": "White text on the black fill."})
emit(light, "--action-hover-halo", {"value": "{color.neutral.200}", "type": "color",
    "source": "computed boxShadow of nav-cta hover (raw/components-computed.json)",
    "description": "The 4px #e5e5e5 box-shadow halo buttons paint on hover and press."})
emit(light, "--action-secondary-border", {"value": "{color.neutral.200}", "type": "color",
    "source": ALIAS, "description": "The 1px #e5e5e5 outline on bordered buttons (Log in, Get a demo, SSO)."})
emit(light, "--field-border", {"value": "{color.neutral.300}", "type": "color",
    "source": ALIAS, "description": "The 1px #d4d4d4 input border."})
emit(light, "--field-focus-border", {"value": "{color.neutral.black}", "type": "color",
    "source": "computed borderTopColor of email-field focused (raw/components-computed.json)",
    "description": "The black border a focused field takes, with a 1px black ring shadow."})
emit(light, "--focus-outline", {"value": "#005fcc", "type": "color",
    "source": "computed outlineColor of nav-cta focus-visible (raw/components-computed.json)",
    "description": "The browser-default `auto 1px rgb(0, 95, 204)` focus outline on buttons."})

docs_l = light.setdefault("docs", {})
for key, leaf in [
    ("nav-active", {"value": "{color.brand.primary}", "type": "color", "source": ALIAS,
                    "description": "The #155dfc active docs-nav text and icon."}),
    ("nav-active-bg", {"value": "{color.wash.primary-10}", "type": "color", "source": ALIAS,
                       "description": "The 10% blue wash under the active item."}),
    ("heading", {"value": "{color.gray.900}", "type": "color", "source": ALIAS,
                 "description": "Docs h1 ink #17191e."}),
    ("sidebar-text", {"value": "{color.gray.500}", "type": "color", "source": ALIAS,
                      "description": "Docs sidebar resting text #707277."}),
    ("divider", {"value": "{color.gray.100}", "type": "color", "source": ALIAS,
                 "description": "The #eef0f5 sidebar divider and hairline."}),
    ("search-bg", {"value": "{color.wash.ink-3}", "type": "color", "source": ALIAS,
                   "description": "The 3% ink wash inside the 9999px search pill."}),
    ("search-bg-hover", {"value": "{color.wash.ink-10}", "type": "color", "source": ALIAS,
                         "description": "The 10% ink wash the pill takes on hover."}),
]:
    docs_l[key] = leaf

# The marketing sheet's own --primary: the same name the docs inline sheet
# binds to the Dub blue. The shared probe resolves the name to the docs
# value, so the marketing value is namespaced under marketing.* — the
# conflicts list in raw/css-vars.json records the collision.
mkt_l = light.setdefault("marketing", {})
mkt_decl = next((r["properties"]["--primary"] for r in V.get("theme", [])
                 if r.get("selector") == ":root" and "--primary" in r.get("properties", {})),
                None)
if mkt_decl:
    mkt_l["primary"] = {"value": hsl_triple(mkt_decl), "type": "color",
        "source": f"declared --primary: {mkt_decl} on :root in the marketing stylesheet "
                  "(raw/css-vars.json theme bin); the docs surface's inline sheet binds "
                  "the same name to the Dub blue — a real collision, not one value",
        "description": f"Marketing --primary ({hsl_triple(mkt_decl)}): the near-black the "
                       "shadcn layer declares on the marketing/auth sheets."}

dark = SPEC["dark"]
# the same declared names, re-bound by the docs surface's html.dark scope
for name, desc in [
    ("--background", "Dark field (#0a0a0a)."),
    ("--foreground", "Dark body ink (#f0f0f0)."),
    ("--card", "Dark card (#0f0f0f)."),
    ("--card-foreground", "Card ink on dark (#fafafa)."),
    ("--muted", "Muted fill on dark (#212121)."),
    ("--muted-foreground", "Muted text on dark (#9b9b9b)."),
    ("--popover", "Popover field on dark (#121212)."),
    ("--popover-foreground", "Popover ink on dark (#e0e0e0)."),
    ("--primary", "Primary on dark (#155dfc, unchanged)."),
    ("--primary-foreground", "Text on primary on dark (#171717)."),
    ("--secondary", "Secondary fill on dark (#212121)."),
    ("--secondary-foreground", "Secondary ink on dark (#fafafa)."),
    ("--accent", "Accent fill on dark (#212121)."),
    ("--accent-foreground", "Accent ink on dark (#fafafa)."),
    ("--ring", "Ring on dark (#262626)."),
    ("--border", "Default border on dark (#2e2e2e)."),
    ("--tooltip-foreground", "Tooltip ink (unchanged)."),
    ("--bg-default", "Default docs surface on dark (#000000)."),
    ("--bg-muted", "Muted surface on dark (#171717)."),
    ("--bg-subtle", "Subtle surface on dark (#262626)."),
    ("--bg-emphasis", "Emphasis surface on dark (#404040)."),
    ("--bg-inverted", "Inverted surface on dark (#fafafa)."),
    ("--bg-info", "Info surface on dark (#172554)."),
    ("--bg-success", "Success surface on dark (#052e16)."),
    ("--bg-attention", "Attention surface on dark (#431407)."),
    ("--bg-warning", "Warning surface on dark (#422006)."),
    ("--bg-error", "Error surface on dark (#450a0a)."),
    ("--content-inverted", "Inverted text on dark (#000000)."),
    ("--content-muted", "Muted text on dark (#525252)."),
    ("--content-subtle", "Subtle text on dark (#a3a3a3)."),
    ("--content-default", "Default text on dark (#d4d4d4)."),
    ("--content-emphasis", "Emphasis text on dark (#fafafa)."),
    ("--content-info", "Info text on dark (#93c5fd)."),
    ("--content-success", "Success text on dark (#86efac)."),
    ("--content-attention", "Attention text on dark (#fdba74)."),
    ("--content-warning", "Warning text on dark (#fde047)."),
    ("--content-error", "Error text on dark (#fca5a5)."),
    ("--border-muted", "Muted border on dark (#262626)."),
    ("--border-subtle", "Subtle border on dark (#404040)."),
    ("--border-default", "Default border on dark (#525252)."),
    ("--border-emphasis", "Emphasis border on dark (#737373)."),
    ("--default-border-color", "The docs hairline on dark (#25282d, gray-800)."),
    ("--twoslash-border-color", "Twoslash code border on dark."),
    ("--twoslash-cursor-color", "Twoslash cursor on dark."),
    ("--twoslash-error-bg", "Twoslash error fill on dark."),
    ("--twoslash-error-color", "Twoslash error text on dark."),
    ("--twoslash-highlighted-bg", "Twoslash highlighted line fill on dark."),
    ("--twoslash-highlighted-border", "Twoslash highlighted line border on dark."),
    ("--twoslash-popup-bg", "Twoslash popup field on dark."),
    ("--twoslash-tag-annotate-bg", "Twoslash annotate tag fill on dark."),
    ("--twoslash-tag-annotate-color", "Twoslash annotate tag text on dark."),
    ("--twoslash-tag-bg", "Twoslash tag fill on dark."),
    ("--twoslash-tag-color", "Twoslash tag text on dark."),
    ("--twoslash-tag-warn-bg", "Twoslash warn tag fill on dark."),
    ("--twoslash-tag-warn-color", "Twoslash warn tag text on dark."),
    ("--twoslash-underline-color", "Twoslash underline (currentColor)."),
    ("--twoslash-unmatched-color", "Twoslash unmatched text on dark."),
    ("--twoslash-warn-bg", "Twoslash warn fill on dark."),
    ("--twoslash-warn-color", "Twoslash warn text on dark."),
]:
    if name in RES.get("dark", {}):
        emit(dark, name, {"var": name, "type": "color",
                          "source": "declared var re-bound on the docs surface's .dark scope",
                          "description": desc})
RD = {n: v.get("value", v.get("raw")) for n, v in RES.get("dark", {}).items()}
if "--twoslash-popup-shadow" in RD:
    layers = shadow_layers(RD["--twoslash-popup-shadow"])
    if layers:
        emit(dark, "--twoslash-popup-shadow", {"value": layers, "type": "shadow",
             "source": "css-var --twoslash-popup-shadow (dark)",
             "description": "Twoslash popup shadow on dark."})

docs_d = dark.setdefault("docs", {})
for key, leaf in [
    ("nav-active", {"value": "{color.brand.primary}", "type": "color", "source": ALIAS,
                    "description": "The #155dfc active docs-nav text on dark (unchanged)."}),
    ("nav-active-bg", {"value": "{color.wash.primary-10}", "type": "color", "source": ALIAS,
                       "description": "The same 10% blue wash under the active item on dark."}),
    ("heading", {"value": "{color.gray.200}", "type": "color", "source": ALIAS,
                 "description": "Docs h1 ink on dark #dfe1e6."}),
    ("sidebar-text", {"value": "{color.gray.400}", "type": "color", "source": ALIAS,
                      "description": "Docs sidebar resting text on dark #9fa1a6."}),
    ("divider", {"value": "{color.wash.white-10}", "type": "color", "source": ALIAS,
                 "description": "The 10% white sidebar divider on dark."}),
    ("search-bg", {"value": "{color.wash.white-3}", "type": "color", "source": ALIAS,
                   "description": "The 3% white wash inside the dark search pill."}),
    ("search-bg-hover", {"value": "{color.wash.white-10}", "type": "color", "source": ALIAS,
                         "description": "The 10% white wash the dark pill takes on hover."}),
    ("surface-card", {"value": "{color.brand.canvas-dark}", "type": "color", "source": ALIAS,
                      "description": "The #090b10 raised dark field (the Copy-page button paints it)."}),
]:
    docs_d[key] = leaf

mkt_d = dark.setdefault("marketing", {})
mkt_decl_d = next((r["properties"]["--primary"] for r in V.get("theme", [])
                   if r.get("selector") == ".dark" and "--primary" in r.get("properties", {})),
                  None)
if mkt_decl_d:
    mkt_d["primary"] = {"value": hsl_triple(mkt_decl_d), "type": "color",
        "source": f"declared --primary: {mkt_decl_d} on .dark in the marketing stylesheet "
                  "(raw/css-vars.json theme bin); the docs surface's inline sheet binds "
                  "the same name to the Dub blue — a real collision, not one value",
        "description": f"Marketing --primary on the .dark scope ({hsl_triple(mkt_decl_d)}): "
                       "the near-white the shadcn layer declares on the marketing sheets."}

# ------------------------------------------------------------- type scale

size = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for name in ["xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl"]:
    vname = f"--text-{name}"
    if vname in R:
        size[name] = var(vname, "dimension",
                         description=f"Declared --text-{name} step ({R[vname]}).")
for key, comp, state, desc in [
    ("display", "hero-title", "default", "The marketing display step (48px Satoshi h1)."),
    ("display-mobile", "m-hero", "default", "The hero size at 390px (36px)."),
    ("docs-h1", "docs-h1", "default", "The docs h1 size (36px)."),
    ("auth-title", "login-card", "default", "The auth card title size (20px)."),
    ("hero-lede", "hero-lede", "default", "The hero paragraph size (20px)."),
]:
    v = ts(comp, state, "fontSize")
    if v:
        size[key] = {"value": v, "type": "dimension",
                     "source": f"computed fontSize of {comp} {state} (raw/components-computed.json)",
                     "description": desc}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for name, desc in [
    ("tight", "Declared tight leading (1.25)."),
    ("normal", "Declared normal leading (1.5)."),
    ("relaxed", "Declared relaxed leading (1.625)."),
]:
    vname = f"--leading-{name}"
    if vname in R:
        leading[name] = var(vname, "number", description=desc)
if "--text-5xl--line-height" in R:
    leading["scale-5xl"] = var("--text-5xl--line-height", "number",
                               description="The declared 5xl line-height ratio (1).")
for key, comp, state, desc in [
    ("display", "hero-title", "default", "The display leading (55.2px on 48px)."),
    ("docs-h1", "docs-h1", "default", "The docs h1 leading (40px on 36px)."),
    ("hero-lede", "hero-lede", "default", "The lede leading (28px on 20px)."),
    ("nav", "nav", "default", "The nav label leading (20px on 14px)."),
]:
    v = ts(comp, state, "lineHeight")
    if v:
        leading[key] = {"value": v, "type": "dimension",
                        "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

tracking = SPEC["core"].setdefault("font", {}).setdefault("tracking", {})
for name, desc in [
    ("tighter", "Declared -0.05em tracking."),
    ("tight", "Declared -0.025em tracking."),
    ("normal", "Zero tracking."),
    ("wide", "Declared wide tracking (~0.39px)."),
]:
    vname = f"--tracking-{name}"
    if vname in R:
        tracking[name] = var(vname, "dimension", description=desc)
for key, comp, state, desc in [
    ("plan-tight", "plan-card", "default", "The -0.32px tracking on plan-card text."),
    ("price-tight", "plan-price", "default", "The -0.28px tracking on price text."),
]:
    v = ts(comp, state, "letterSpacing")
    if v and v != "normal":
        tracking[key] = {"value": v, "type": "dimension",
                         "source": f"computed letterSpacing of {comp} {state} (raw/components-computed.json)",
                         "description": desc}

weight = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for name, desc in [
    ("normal", "400 body weight."), ("medium", "500 nav/label weight."),
    ("semibold", "600 docs-heading weight."), ("bold", "700."),
    ("extrabold", "800."), ("headings-custom", "The declared docs heading weight (700)."),
]:
    vname = f"--font-weight-{name}"
    if vname in R:
        weight[name] = var(vname, "fontWeight", description=desc)
for key, comp, state, desc in [
    ("display", "hero-title", "default", "Satoshi 500: the marketing display weight."),
    ("docs-h1", "docs-h1", "default", "Satoshi 600: the docs h1 weight."),
]:
    v = ts(comp, state, "fontWeight")
    if v:
        weight[key] = {"value": v, "type": "fontWeight",
                       "source": f"computed fontWeight of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

# ---------------------------------------------------------- radius, easing

radius = SPEC["core"].setdefault("radius", {})
if "--radius-xl" in R:
    radius["xl"] = var("--radius-xl", "dimension",
                       description="The declared 12px radius (docs nav items, cards, copy button, billing toggle).")
for key, comp, state, prop, desc in [
    ("button", "nav-cta", "default", "borderTopLeftRadius", "The 8px radius on every button (CTAs, SSO, submit)."),
    ("field", "email-field", "default", "borderTopLeftRadius", "The 6px input radius."),
    ("card", "plan-card", "default", "borderTopLeftRadius", "The 12px card radius."),
    ("nav-item", "docs-nav-item", "default", "borderTopLeftRadius", "The 12px docs-nav item radius."),
    ("search-pill", "docs-search", "default", "borderTopLeftRadius", "The 9999px search pill."),
    ("toggle", "docs-theme", "default", "borderTopLeftRadius", "The 9999px theme toggle."),
    ("icon", "social-link", "default", "borderTopLeftRadius", "The 9999px social icon button."),
]:
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

easing = SPEC["core"].setdefault("easing", {})
for key, vname, desc in [
    ("in", "--ease-in", "Declared ease-in (.4,0,1,1)."),
    ("out", "--ease-out", "Declared ease-out (0,0,.2,1)."),
    ("in-out", "--ease-in-out", "Declared ease-in-out (.4,0,.2,1)."),
    ("default", "--default-transition-timing-function", "The default transition curve."),
]:
    if vname in R:
        easing[key] = var(vname, "cubicBezier", description=desc)
try:
    easing["customer-card"] = {"value": st("customer-card", "default")["transitionTimingFunction"],
                               "type": "cubicBezier",
                               "source": "computed transitionTimingFunction of customer-card default (raw/components-computed.json)",
                               "description": "The 0.5s flex-grow ease on the customer cards (~easeOutQuint)."}
except KeyError:
    pass

duration = SPEC["core"].setdefault("duration", {})
if "--default-transition-duration" in R:
    duration["default"] = var("--default-transition-duration", "duration",
                              description="The declared default transition duration (0.15s).")
for key, comp, state, desc in [
    ("topic-fast", "sales-topic", "default", "The 75ms topic-pill/footer-link colour transition."),
    ("sidebar", "docs-sidebar", "default", "The 100ms docs sidebar transform transition."),
    ("menu-button", "m-menu-button", "default", "The 200ms mobile menu button transition."),
    ("customer-card", "customer-card", "default", "The 500ms customer-card flex-grow animation."),
]:
    try:
        d = (st(comp, state).get("transitionDuration") or "").split(",")[0].strip()
        if d and d != "0s":
            duration[key] = {"value": d, "type": "duration",
                             "source": f"computed transitionDuration of {comp} {state} (raw/components-computed.json)",
                             "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------- space, layout

spacing = SPEC["core"].setdefault("spacing", {})
if "--spacing" in R:
    spacing["base"] = var("--spacing", "dimension",
                          description="The declared 4px spacing unit (Tailwind v4).")

layout = SPEC["core"].setdefault("layout", {})
for key, vname, desc in [
    ("container-xs", "--container-xs", "Container xs (320px)."),
    ("container-sm", "--container-sm", "Container sm (384px — the auth card width class max-w-sm)."),
    ("container-lg", "--container-lg", "Container lg (512px)."),
    ("container-xl", "--container-xl", "Container xl (576px)."),
    ("container-2xl", "--container-2xl", "Container 2xl (672px)."),
    ("container-3xl", "--container-3xl", "Container 3xl (768px)."),
    ("container-4xl", "--container-4xl", "Container 4xl (896px)."),
    ("container-5xl", "--container-5xl", "Container 5xl (1024px — the footer measure)."),
    ("container-6xl", "--container-6xl", "Container 6xl (1152px)."),
    ("scroll-mt", "--scroll-mt", "The docs scroll-margin-top (~101px)."),
    ("banner-height", "--banner-height", "The banner-height var (0px signed out)."),
    ("assistant-sheet-width", "--assistant-sheet-width", "The Mintlify AI-sheet width var (0px — the assistant never opened)."),
]:
    if vname in R:
        layout[key] = var(vname, "dimension", description=desc)
for key, comp, state, prop, desc in [
    ("docs-sidebar", "docs-sidebar", "default", "width", "The 288px docs sidebar."),
    ("docs-search-width", "docs-search", "default", "width", "The docs search pill width."),
]:
    if have(comp, state, prop):
        layout[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

# ----------------------------------------------------------------- shadows

shadow = SPEC["core"].setdefault("shadow", {})
for key, comp, state, desc in [
    ("field", "email-field", "default",
     "The quiet input shadow: rgba(0,0,0,.05) 0 1px 2px."),
    ("field-focus", "email-field", "focused",
     "The focused field: a white spread, a 1px black ring, over the same soft drop."),
    ("cta-hover", "nav-cta", "hover",
     "The button hover/press halo: a white spread then 4px #e5e5e5."),
]:
    try:
        layers = shadow_layers(st(comp, state)["boxShadow"])
        if layers:
            shadow[key] = {"value": layers, "type": "shadow",
                           "source": f"computed boxShadow of {comp} {state} (raw/components-computed.json)",
                           "description": desc}
    except KeyError:
        pass

# ---------------------------------------------------------------- measured

meas = SPEC["core"].setdefault("measured", {})
try:
    s = st("nav-cta", "focus-visible")
    if s.get("outlineColor"):
        meas["focus-outline"] = {"value": norm_color(s["outlineColor"]), "type": "color",
                                 "source": "computed outline of nav-cta focus-visible (raw/components-computed.json)",
                                 "description": f"The browser-default focus indicator: {s['outlineStyle']} {s['outlineWidth']} {norm_color(s['outlineColor'])}, offset {s.get('outlineOffset')}."}
        meas["focus-outline-width"] = {"value": s["outlineWidth"], "type": "dimension",
                                       "source": "computed outlineWidth of nav-cta focus-visible (raw/components-computed.json)",
                                       "description": "The 1px auto-outline width on buttons (fields take a 1px black ring shadow instead)."}
except KeyError:
    pass
try:
    s = st("docs-nav-item", "focus-visible")
    if s.get("outlineColor"):
        meas["docs-focus-outline"] = {"value": norm_color(s["outlineColor"]), "type": "color",
                                      "source": "computed outline of docs-nav-item focus-visible (raw/components-computed.json)",
                                      "description": f"The docs focus ring: {s['outlineStyle']} {s['outlineWidth']} {norm_color(s['outlineColor'])}, offset {s.get('outlineOffset')}."}
except KeyError:
    pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("nav.height", "nav", "default", "height", "The 32px desktop nav bar content row."),
    ("nav.height-mobile", "m-nav", "default", "height", "The 56px mobile top bar."),
    ("logo.width", "logo", "default", "width", "The Dub wordmark width (~61px)."),
    ("button.height-sm", "nav-cta", "default", "height", "The 32px header button."),
    ("button.height", "hero-cta", "default", "height", "The 38px hero button."),
    ("button.height-lg", "email-submit", "default", "height", "The 40px auth/SSO button."),
    ("field.height", "email-field", "default", "height", "The 38px input."),
    ("search-pill.height", "docs-search", "default", "height", "The 36px docs search pill."),
    ("theme-toggle.size", "docs-theme", "default", "height", "The 30px theme toggle."),
    ("social-icon.size", "social-link", "default", "height", "The 24px social icon button."),
    ("auth-card.width", "login-card", "default", "width", "The 384px auth card (max-w-sm)."),
    ("register-card.width", "register-card", "default", "width", "The 384px register card."),
    ("plan-card.width", "plan-card", "default", "width", "The shared pricing panel width (~1062px)."),
    ("demo-panel.width", "demo-panel", "default", "width", "The hero product-demo panel width (~882px)."),
    ("nav-dropdown.width", "nav-dropdown", "default", "width", "Width of one card inside the Product mega-menu (~319px), not of the panel."),
    ("mobile-nav-item.height", "m-nav-item", "default", "height", "Mobile menu item height (24px)."),
    ("faq-trigger.height", "faq-trigger", "default", "height", "The 56px FAQ accordion row."),
]:
    if have(cname, state, prop):
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)[prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}

# Readings that cannot be taken at face value, named on every leaf that cites
# them. recaptureMissed: a later run did not find the component and the capture
# kept the earlier run's states. WRONG: the selector caught another element (the
# README's What to distrust lists these; each needs a recapture).
FLAGGED = {k: c["recaptureMissed"] for k, c in C.items() if c.get("recaptureMissed")}
WRONG = {
    "plan-price": "the selector caught the price row's wrapper, whose first text is \"/month\", not the price figure",
    "nav-dropdown": "the selector caught one card inside the Product mega-menu, not the panel",
}


def note_flagged(node):
    if isinstance(node, dict):
        src = node.get("source")
        if isinstance(src, str):
            for k, run in FLAGGED.items():
                if re.search(rf"(?<![\w-]){re.escape(k)}(?![\w-])", src) and f"{k} was not found" not in src:
                    node["source"] = src = (src + f"; {k} was not found by the {run} re-run (recaptureMissed),"
                                            " so this is the reading kept from the earlier run")
            for k, what in WRONG.items():
                if re.search(rf"(?<![\w-]){re.escape(k)}(?![\w-])", src) and f"{k}: read from the wrong element" not in src:
                    node["source"] = src = src + f"; {k}: read from the wrong element ({what}); recapture needed"
        for v in node.values():
            note_flagged(v)


note_flagged(SPEC)

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
