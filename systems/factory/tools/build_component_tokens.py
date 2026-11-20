#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

factory.com is one marketing surface signed out: every page paints
<html data-theme="light">, with scoped dark sections inside the light page —
the [data-dark-hero] heroes on /enterprise and the /product pages,
.invert-color-scheme panels and the dark site footer. There is no user
theme toggle on the marketing site. docs.factory.com shares the token layer
and ships a three-way .theme-selector-button control (Light/Dark/System),
which is where a whole-surface dark page was measured. app.factory.ai
redirects to auth.factory.ai, a dark sign-in card that does not share the
marketing token layer; its values land under component.signin.* as measured
literals.

The site declares a real design-token layer in its served Next.js CSS
bundles (raw/css-vars.json): the --neutral-100..1000 ramp, the
--accent-100..300 oranges, --surface-page/raised/sunken, the
--light-base-*/--dark-base-* primitive pairs, Tailwind palette scales
(--color-red-*/--orange-*/--amber-*/--emerald-*/--sky-*/--blue-*/
--violet-*/--yellow-*/--zinc-*/--color-neutral-*), the --text-* type ramp
with --line-height companions, --tracking-*/--leading-*/--font-weight-*,
--font-geist-sans/--font-geist-mono/--font-pixel (Geist + Geist Mono +
Geist Pixel Square, all variable wght 100-900), --spacing, --radius-*,
--container-*, --content-gutter/--content-column, --breakpoint-3xl,
--blur-*, --ease-*, --animate-* and --default-transition-* — plus a
semantic layer redeclared under [data-theme="light"] and inverted by
.invert-color-scheme: --color-background, --color-foreground,
--color-base-100..1000, --color-light-base-*/--color-dark-base-* and
--color-surface-raised. Declared scales land under core.*; every
[data-theme]-switching name is emitted under both light.* and dark.* as a
{"var": ...} leaf so each scope resolves its own value.

Measured computed styles from raw/components-computed.json:

  light       #f9f9f9 page field, #020202 ink, the dark pill CTAs
              (DOWNLOAD / CONTACT SALES), the translucent nav ink,
              the bordered secondary pills
  dark        the scoped dark sections: #020202 hero field, #eeeeee ink,
              the dark footer — and docs.factory.com's toggled dark page
  signin      auth.factory.ai's own dark card: #171717 field, white ink,
              the email field and Continue buttons — measured literals,
              honestly labelled, outside the marketing token layer
  fonts       Geist and Geist Mono variable fonts (wght 100-900) plus the
              Geist Pixel Square display mono; the --font-sans/--font-mono
              Tailwind defaults alias to them in the emitted tree
  ramp        declared 12/14/16/18/20/24/30/36/48/72/96px steps with
              --line-height companions
  shape       a 2/3/4/6/8/10/12px radius scale; pills on the CTAs,
              rounded cards and fields
  motion      the declared 0.15s cubic-bezier(.4,0,.2,1) control
              transition; 1s/2s --animate-* keyframe utilities
"""

import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
RD = V.get("resolved", {}).get("dark", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}
D = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RD.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. factory.com "
    "declares its design-token layer in the served Next.js CSS bundles "
    "(raw/css-vars.json): theme-invariant scales under core.* and a "
    "[data-theme]-switching semantic layer emitted under both light.* and "
    "dark.* so each scope resolves its own value. Measured roles alias to "
    "the declared values where they match. The auth.factory.ai sign-in is "
    "outside this layer; its values are measured literals under "
    "component.signin.*."),
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



# A transparent reading is no fill (the colour comes from an ancestor), so it
# is never committed as one (2026-11 audit, finding 14-8).
TRANSPARENT = re.compile(r"transparent|rgba\(\s*[\d.]+[,\s]+[\d.]+[,\s]+[\d.]+\s*[,/]\s*0(\.0+)?%?\s*\)")


def opaque(v):
    """v unless it is a transparent reading; a KeyError skips the token."""
    if v is None or TRANSPARENT.fullmatch(str(v).strip()):
        raise KeyError("transparent")
    return v

def lit(value, ty, src, desc):
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


EMITTED = {}   # variable name -> dotted token path it was actually written to
_OWNER = {}    # dotted token path -> variable name holding it


def _leaf(d):
    return isinstance(d, dict) and ("var" in d or "value" in d)


def emit(root, name, leaf):
    """Write `leaf` at name's dotted path.

    A declared name can be both a leaf and the parent of other names. When a
    leaf and a group must share a node, the leaf moves inside the group under
    the first free of `default`, `base`, `self` — never silently overwriting
    tokens that resolve to different states.
    """
    node = root
    parts = name[2:].split("-")
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


DECL_SRC = "declared design-system variable in the site's served CSS bundle (raw/css-vars.json)"


def declared(name):
    """The resolved light-set value, or None when the var never resolved."""
    v = R.get(name)
    return v if v not in (None, "") else None


def decl(name, ty="dimension"):
    v = declared(name)
    desc = f"The declared `{name}`."
    if ty == "dimension":
        nv = norm_len(v)
        if nv != v:
            raw = (RL.get(name) or {}).get("raw")
            desc = f"The declared `{name}` — `{raw}`, which Chromium resolves to {nv} (effectively a full pill)."
            v = nv
        if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(v).strip()):
            ty = "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", desc)


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\))")


def decl_color(name):
    v = declared(name)
    ty = "color" if COLOR_V.fullmatch(str(v).strip()) else "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


def ratio(name):
    """calc(a/b) -> float for a line-height var; everything else stays raw."""
    v = declared(name)
    m = re.fullmatch(r"calc\(\s*(-?\d*\.?\d+)\s*/\s*(-?\d*\.?\d+)\s*\)", str(v))
    if m:
        return lit(round(float(m.group(1)) / float(m.group(2)), 4), "number",
                   f"{DECL_SRC}: {name}", f"The declared `{name}` line-height ratio.")
    return decl(name, "other")


def norm_len(v):
    """Exponential lengths become ordinary pixel strings: Chromium serialises
    `calc(infinity * 1px)` as `3.35544e+07px`, which is a real length, not an
    `other` — it is how the site spells a full pill."""
    m = re.fullmatch(r"(-?[\d.]+[eE][+-]?\d+)(px|rem)", str(v).strip())
    if not m:
        return v
    return f"{float(m.group(1)):f}".rstrip("0").rstrip(".") + m.group(2)


def painted(comp, state, key):
    """A reading from the kit's paint list — the layers actually painted
    (rounded children, pseudo-elements, inset shadows) rather than the
    wrapper's computed style, which is often an unpainted positioning box.
    An entry whose recorded size matches the element's own rect wins."""
    c = C[comp]["states"][state]
    entries = [p for p in c.get("paint") or [] if p.get(key)]
    if not entries:
        raise KeyError(key)
    rect = c.get("rect") or {}
    for p in entries:
        m = re.fullmatch(r"([\d.]+)x([\d.]+)", str(p.get("size") or ""))
        if m and abs(float(m.group(1)) - rect.get("w", -9)) <= 1 and abs(float(m.group(2)) - rect.get("h", -9)) <= 1:
            return p[key]
    return entries[0][key]


def inset_shadow_color(comp, state):
    """The colour of the painted inset (hairline) box-shadow layer — how the
    site draws a 'border' when border-width is 0."""
    sh = painted(comp, state, "shadow")
    m = re.search(COLOR_V.pattern + r"(?:\s+-?[\d.]+px){2,4}\s+inset", sh)
    if not m:
        raise KeyError("insetShadowColor")
    return m.group(1)


# ------------------------------------------------------------------- fonts
#
# factory ships variable fonts: Geist (wght 100-900) for all text, Geist Mono
# for code/install frames and Geist Pixel Square for the pixel-label style.
# The generated next/font classes declare --font-geist-sans/--font-geist-mono
# on <body>; the Tailwind --font-sans/--font-mono aliases never resolve in the
# synthetic probe (the alias chain only resolves inside the real class scope),
# so they are emitted as honest aliases onto the resolved Geist families.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
FONT_MAP = [
    ("geistSans", "--font-geist-sans", "Geist (variable, wght 100-900) — every heading, control and body."),
    ("geistMono", "--font-geist-mono", "Geist Mono (variable, wght 100-900) — code blocks, the install command, eyebrows and labels."),
    ("pixel", "--font-pixel", "Geist Pixel Square — the pixel-styled label display face."),
    ("japanese", "--font-japanese", "The Japanese UI face (declared but unresolved in the probe)."),
]
for key, name, desc in FONT_MAP:
    if name in R:
        fam[key] = {"var": name, "type": "fontFamily", "description": desc}
# The Tailwind default families are declared but only resolve inside the real
# generated body classes; alias them to the resolved Geist families. The
# declared tails keep a generic fallback (`var(--font-geist-sans),
# var(--font-japanese,sans-serif)` / `...,var(--font-japanese,monospace)`):
# where --font-japanese resolved, the chain ends in its stack; where it did
# not, the declared generic name is what survives — never drop it.
if "geistSans" in fam and declared("--font-sans") is None:
    fam["sans"] = lit("{font.family.geistSans}," + ("{font.family.japanese}" if "japanese" in fam else "sans-serif"), "fontFamily",
        "the declared --font-sans default (Tailwind `--default-font-family: var(--font-geist-sans),var(--font-japanese,sans-serif)`); the alias chain does not resolve outside the generated body classes, so this aliases the resolved --font-geist-sans plus the declared generic fallback",
        "The default sans — Geist via --font-sans, ending in sans-serif.")
if "geistMono" in fam and declared("--font-mono") is None:
    fam["mono"] = lit("{font.family.geistMono}," + ("{font.family.japanese}" if "japanese" in fam else "monospace"), "fontFamily",
        "the declared --font-mono default (Tailwind `--default-mono-font-family: var(--font-geist-mono),var(--font-japanese,monospace)`); aliases the resolved --font-geist-mono plus the declared generic fallback",
        "The default mono — Geist Mono via --font-mono, ending in monospace.")

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for name in sorted(k for k in R if re.fullmatch(r"--font-weight-[a-z]+", k)):
    weights[name[len("--font-weight-"):]] = decl(name, "fontWeight")

# ------------------------------------------------------------- type ramp
#
# --text-* sizes with their --line-height companions (Tailwind-style steps:
# xs..8xl). No responsive overrides were observed in the declarations.

sizes = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for name in sorted(k for k in R if re.fullmatch(r"--text-[a-z0-9]+", k)):
    key = name[len("--text-"):]
    raw = str((RL.get(name) or {}).get("raw") or "")
    responsive = None
    if raw and not re.fullmatch(r"-?[\d.]+(px|rem)", raw):
        responsive = f"fluid — apply `{raw}`; the px value resolves it at 1440 x 900"
    sizes[key] = var(name, "dimension", responsive=responsive)

lineheights = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for name in sorted(k for k in R if k.startswith("--leading-")):
    v = str(R[name])
    if "calc" in v:
        lineheights[name[len("--leading-"):]] = ratio(name)
    elif re.fullmatch(r"-?\d+(\.\d+)?", v):
        lineheights[name[len("--leading-"):]] = lit(float(v), "number", f"{DECL_SRC}: {name}", f"The declared `{name}` line-height ratio.")
    else:
        lineheights[name[len("--leading-"):]] = decl(name, "other")
for name in sorted(k for k in R if re.fullmatch(r"--text-[a-z0-9]+--line-height", k)):
    lineheights[name[len("--text-"):].replace("--line-height", "")] = ratio(name)

tracking = SPEC["core"].setdefault("font", {}).setdefault("tracking", {})
for name in sorted(k for k in R if k.startswith("--tracking-")):
    # letter-spacing is declared in em; the probe's resolved px is sized by the
    # probe's own font size, so keep the declared relative value, not the probe
    # reading (`.1em`, never `1.59375px`).
    raw = (RL.get(name) or {}).get("raw")
    v = raw if raw not in (None, "") else R[name]
    tracking[name[len("--tracking-"):]] = lit(v, "other", f"{DECL_SRC}: {name}", f"The declared `{name}` letter-spacing.")

# ---------------------------------------------------------- core scales
#
# Theme-invariant declarations: the neutral ramp and named primitives, the
# accent oranges, the Tailwind palette scales, spacing base, radii,
# containers, the content column/gutter, the 3xl breakpoint, blurs, easings
# and durations. These resolve identically in both data-theme scopes.

color_alias = {}   # normalized colour -> 'color.<path>' for aliasing
colors = SPEC["core"].setdefault("color", {})

for name in sorted(k for k in R if re.fullmatch(r"--neutral-\d+", k)):
    colors.setdefault("neutral", {})[name[len("--neutral-"):]] = decl_color(name)
    color_alias.setdefault(norm_color(R[name]), f"color.neutral.{name[len('--neutral-'):]}")
for name in sorted(k for k in R if re.fullmatch(r"--accent-\d+", k)):
    colors.setdefault("accent", {})[name[len("--accent-"):]] = decl_color(name)
    color_alias.setdefault(norm_color(R[name]), f"color.accent.{name[len('--accent-'):]}")
for name in sorted(k for k in R if re.fullmatch(r"--surface-[a-z]+", k)):
    # --surface-raised swaps per theme (#fff light / #101010 dark): the themed
    # sets carry it; keeping it in core too would clash on the same property.
    if name == "--surface-raised":
        color_alias.setdefault(norm_color(R[name]), "color.surface.raised")
        continue
    colors.setdefault("surface", {})[name[len("--surface-"):]] = decl_color(name)
    color_alias.setdefault(norm_color(R[name]), f"color.surface.{name[len('--surface-'):]}")

BASE_PRIM = {
    "--light-base-primary": ("lightBasePrimary", "The light-page primary base (#eee) — primitive behind the light surface."),
    "--light-base-secondary": ("lightBaseSecondary", "The light-page secondary base (#fafafa)."),
    "--dark-base-primary": ("darkBasePrimary", "The dark primary base (#020202) — the near-black field of heroes, the footer and dark docs."),
    "--dark-base-secondary": ("darkBaseSecondary", "The dark secondary base (#101010) — raised dark panels."),
}
for name, (key, desc) in BASE_PRIM.items():
    if declared(name) is not None:
        colors[key] = decl_color(name)
        colors[key]["description"] = desc
        color_alias.setdefault(norm_color(R[name]), f"color.{key}")

# The Tailwind palette scales the bundle keeps (--color-<hue>-<step>), emitted
# under color.hue.<hue>.<step> — --color-neutral-* joins them beside the
# primitive --neutral-* ramp above.
hue_colors = SPEC["core"].setdefault("color", {}).setdefault("hue", {})
for name in sorted(k for k in R if re.fullmatch(r"--color-[a-z]+-\d+", k)):
    hue = re.match(r"--color-([a-z]+)-(\d+)", name)
    h, step = hue.group(1), hue.group(2)
    if h in ("accent", "base", "neutral"):
        # --color-accent-*/--color-base-* are the semantic layer, --color-neutral-* is a palette scale
        if h == "neutral":
            hue_colors.setdefault(h, {})[step] = decl_color(name)
        continue
    hue_colors.setdefault(h, {})[step] = decl_color(name)

NAMED = {
    "white": "Pure white — raised surfaces, button ink on dark fills.",
    "black": "Pure black.",
    "transparent": "Fully transparent.",
    "current": "currentColor passthrough.",
}
for name, desc in NAMED.items():
    vn = f"--color-{name}"
    if declared(vn) is not None:
        colors[re.sub(r"-([a-z])", lambda m: m.group(1).upper(), name)] = lit(
            R[vn], "color" if COLOR_V.fullmatch(str(R[vn]).strip()) else "other",
            f"{DECL_SRC}: {vn}", desc)
        color_alias.setdefault(norm_color(R[vn]), "color." + re.sub(r"-([a-z])", lambda m: m.group(1).upper(), name))

if declared("--spacing") is not None:
    SPEC["core"].setdefault("spacing", {})["base"] = decl("--spacing")

radius_alias = {}
radii = SPEC["core"].setdefault("radius", {})
for name in sorted(k for k in R if re.fullmatch(r"--radius(-[a-z0-9]+)?", k)):
    key = name[len("--radius-"):] if name != "--radius" else "default"
    radii[key] = decl(name)
    radius_alias[norm_len(R[name])] = key

containers = SPEC["core"].setdefault("container", {})
for name in sorted(k for k in R if re.fullmatch(r"--container-[a-z0-9]+", k)):
    containers[name[len("--container-"):]] = decl(name)

layout = SPEC["core"].setdefault("layout", {})
for key, name, desc, kw in [
    ("contentColumn", "--content-column", "The 1440px content column maximum.", {}),
    ("contentGutter", "--content-gutter", "The page side gutter — 36px at 1440; declared 1rem/1.5rem/2.25rem/5rem steps by breakpoint.",
     {"responsive": "declared 1rem, 1.5rem, 2.25rem and 5rem at different breakpoints (resolved 36px at 1440 x 900)"}),
]:
    if declared(name) is not None:
        layout[key] = lit(R[name], "dimension" if re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(R[name])) else "other",
                          f"{DECL_SRC}: {name}", desc)
        layout[key].update(kw)

if declared("--breakpoint-3xl") is not None:
    SPEC["core"].setdefault("breakpoint", {})["3xl"] = decl("--breakpoint-3xl")

if declared("--aspect-video") is not None:
    SPEC["core"].setdefault("aspect", {})["video"] = decl("--aspect-video", "other")

for name in sorted(k for k in R if re.fullmatch(r"--blur-[a-z0-9]+", k)):
    SPEC["core"].setdefault("blur", {})[name[len("--blur-"):]] = decl(name)

easing = SPEC["core"].setdefault("easing", {})
for name in sorted(k for k in R if k.startswith("--ease-")):
    easing[name[len("--ease-"):]] = decl(name, "cubicBezier")
if declared("--default-transition-timing-function") is not None:
    easing["default"] = decl("--default-transition-timing-function", "cubicBezier")
if declared("--default-transition-duration") is not None:
    SPEC["core"].setdefault("duration", {})["default"] = decl("--default-transition-duration", "duration")

anims = SPEC["core"].setdefault("animate", {})
for name in sorted(k for k in R if k.startswith("--animate-")):
    anims[name[len("--animate-"):]] = lit(R[name], "other", f"{DECL_SRC}: {name}", f"The declared `{name}` keyframe shorthand.")

# ------------------------------------------ per-scope semantic variables
#
# Everything redeclared inside [data-theme="light"] / .invert-color-scheme
# switches value between the scopes — every such name is emitted under both
# sets so each resolves its own value. The dark set is the :root default the
# scoped dark sections paint; docs.factory.com's toggle flips the whole page.

theme_names = set()
for rule in V.get("theme", []):
    sel = " ".join(rule.get("context") or []) + " " + rule.get("selector", "")
    if 'data-theme=' in sel or "invert-color-scheme" in sel:
        theme_names.update(rule.get("properties") or {})

semantic_names = sorted(n for n in theme_names if declared(n) is not None or D.get(n) is not None)
for root in (SPEC["light"], SPEC["dark"]):
    for name in semantic_names:
        leaf_ = var(name, "color" if COLOR_V.fullmatch(str(R.get(name, "")).strip()) else "other")
        emit(root, name, leaf_)

# --------------------------------------------- measured roles
#
# Roles measured on the real pages; each aliases to the declared token its
# value matches.

role_alias = {"light": dict(color_alias), "dark": dict(color_alias)}
for name in semantic_names:
    p = EMITTED[name]
    if R.get(name):
        role_alias["light"].setdefault(norm_color(R[name]), p)
    if D.get(name):
        role_alias["dark"].setdefault(norm_color(D[name]), p)


def semcolor(raw, src, desc, theme="light"):
    alias = role_alias[theme].get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


sem, dsem = SPEC["light"], SPEC["dark"]
for root, theme, key, comp, state, prop, group, desc in [
    (sem, "light", "ink", "hero-h1", "default", "color", "text",
     "The near-black ink on display copy, headings and card text."),
    (sem, "light", "navInk", "nav-link", "default", "color", "text",
     "The nav-link ink."),
    (sem, "light", "ctaFill", "nav-cta", "default", "backgroundColor", "action",
     "The dark fill of the DOWNLOAD pill CTAs."),
    (sem, "light", "ctaInk", "nav-cta", "default", "color", "action",
     "The light text on the dark CTA pill."),
    (sem, "light", "cta2Border", "nav-cta2", "default", "borderTopColor", "border",
     "The border of the CONTACT SALES secondary pill."),
    (sem, "light", "cta2Ink", "nav-cta2", "default", "color", "action",
     "The ink of the CONTACT SALES secondary pill."),
    (sem, "light", "focusRing", "nav-menu-btn", "focus-visible", "outlineColor", "border",
     "The keyboard focus ring on header controls."),
    (sem, "light", "subInk", "hero-sub", "default", "color", "text",
     "The muted mono tagline ink."),
    (dsem, "dark", "panel", "dark-hero", "default", "backgroundColor", "background",
     "The near-black field of a [data-dark-hero] section inside the light page."),
    (dsem, "dark", "ink", "dark-h1", "default", "color", "text",
     "The light ink of a scoped dark hero headline."),
    (dsem, "dark", "footerPanel", "footer", "default", "backgroundColor", "background",
     "The dark site-footer field."),
    (dsem, "dark", "footerInk", "footer-link", "default", "color", "text",
     "The footer link ink on the dark footer."),
    (dsem, "dark", "eyebrowInk", "dark-eyebrow", "default", "color", "text",
     "The small mono eyebrow ink inside a dark hero."),
    (dsem, "dark", "docsInk", "docs-h1-dk", "dark", "color", "text",
     "The docs page's heading ink after its theme selector switched to dark."),
    (dsem, "dark", "docsPanel", "docs-sidebar-dk", "dark", "backgroundColor", "background",
     "The docs sidebar field in dark."),
]:
    try:
        if prop == "color":
            # The element's own `color` is often inherited onto an unpainted
            # wrapper; the kit's first-text-node reading is the painted ink.
            raw = ts(comp, state, "color")
            src = f"computed color of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if raw in (None, "") or (prop == "backgroundColor" and TRANSPARENT.fullmatch(str(raw).strip())):
            raise KeyError(prop)
        root.setdefault(group, {})[key] = semcolor(raw, src, desc, theme)
    except KeyError:
        pass

# The page field: every marketing page ships <html data-theme="light"> and
# the body paints --color-background (#f9f9f9).
if declared("--color-background") is not None:
    sem.setdefault("background", {})["page"] = lit(
        "{color.background}", "color",
        "the resolved --color-background under [data-theme=\"light\"] — the #f9f9f9 field behind every marketing page (screenshots/*-light-*.png)",
        "The light page field — --color-background resolved under data-theme=\"light\".")

# ------------------------------------------------------------- type ramp
#
# One measured step per headline: the hero masthead aliases the declared step
# it matches.

size_alias = {}
for name in sorted(k for k in R if re.fullmatch(r"--text-[a-z0-9]+", k)):
    size_alias.setdefault(R[name], f"font.size.{name[len('--text-'):]}")
measured_size = {}
for key, comp, state, desc in [
    ("masthead", "hero-h1", "default", "The hero masthead size — the uppercase 'AI CODING AGENTS' display."),
    ("body", "hero-sub", "default", "The hero tagline size."),
    ("docsH1", "docs-h1", "default", "The docs masthead size."),
]:
    try:
        raw = st(comp, state)["fontSize"]
        src = f"computed fontSize of {comp} {state} (raw/components-computed.json)"
        alias = size_alias.get(raw)
        SPEC["core"].setdefault("font", {}).setdefault("size", {}).setdefault("measured", {})[key] = lit(
            f"{{{alias}}}" if alias else raw, "dimension",
            src + (f"; matches declared {alias}" if alias else ""), desc)
        measured_size[key] = raw
    except KeyError:
        pass

# ------------------------------------------------------------------ shape

for key, comp, state, prop, desc in [
    ("cta", "nav-cta", "default", "borderTopLeftRadius", "The CTA pill radius."),
    ("cta2", "nav-cta2", "default", "borderTopLeftRadius", "The secondary pill radius."),
    ("menu", "nav-panel", "default", "paint:radius", "The mega-menu panel corner radius — read from a painted rounded child; the wrapper itself may be unrounded."),
    ("field", "field-firstname", "default", "borderTopLeftRadius", "The contact field radius."),
    ("planCard", "plan-card", "default", "paint:radius", "The pricing plan-card corner radius."),
]:
    try:
        if prop == "paint:radius":
            v = norm_len(painted(comp, state, "radius"))
            src = f"the painted radius of {comp}'s rounded child {state} (raw/components-computed.json paint list)"
        else:
            v = norm_len(st(comp, state)[prop])
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        dkey = radius_alias.get(v)
        if dkey:
            radii[key] = lit(f"{{radius.{dkey}}}", "dimension", src + f"; matches declared --radius-{dkey}", desc)
        else:
            radii[key] = lit(v, "dimension" if re.fullmatch(r"[0-9.]+(px|rem)", v or "") else "other", src, desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
try:
    s = st("nav-cta", "default")
    dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        # A CSS transition list pairs every comma entry with its own timing:
        # appending one duration after the whole property list would leave the
        # earlier entries at the 0s default.
        props = [p.strip() for p in s.get("transitionProperty", "all").split(",") if p.strip()]
        val = ", ".join(f"{p} {dur} {ease or ''}".strip() for p in props)
        mo["control"] = lit(val, "other",
            "computed transition of nav-cta default (raw/components-computed.json); the declared --default-transition-duration/.4-0-.2-1 pair",
            "The control transition on pills and buttons.")
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("topbar-height", "mkt-header", "default", "h", "dimension", "The ~72px fixed marketing header bar."),
    ("logo-width", "mkt-logo", "default", "w", "dimension", "The Factory mark-and-wordmark width."),
    ("nav-pill-height", "nav-link", "default", "h", "dimension", "The header nav-link height."),
    ("cta-height", "nav-cta", "default", "h", "dimension", "The DOWNLOAD pill height."),
    ("cta2-height", "nav-cta2", "default", "h", "dimension", "The CONTACT SALES pill height."),
    ("mega-menu-width", "nav-panel", "default", "w", "dimension", "The open mega-menu panel width."),
    ("mega-menu-height", "nav-panel", "default", "h", "dimension", "The open mega-menu panel height."),
    ("hero-masthead-width", "hero-h1", "default", "w", "dimension", "The hero masthead measure (max-w)."),
    ("install-cmd-width", "install-cmd", "default", "w", "dimension", "The install-command copy box width."),
    ("plan-card-width", "plan-card", "default", "w", "dimension", "The pricing plan-card width."),
    ("field-height", "field-firstname", "default", "h", "dimension", "The contact field height."),
    ("textarea-height", "field-msg", "default", "h", "dimension", "The message textarea height."),
    ("send-width", "send-btn", "default", "w", "dimension", "The form SUBMIT button width."),
    ("dark-hero-height", "dark-hero", "default", "h", "dimension", "A scoped dark hero's height."),
    ("docs-sidebar-width", "docs-sidebar", "default", "w", "dimension", "The docs sidebar column width."),
    ("mobile-topbar-height", "m-topbar", "default", "h", "dimension", "The phone top bar height."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# The auth.factory.ai sign-in is a separate app outside the marketing token
# layer; its measured values are kept as literals, honestly labelled.
login = comp.setdefault("signin", {})
for name, cname, state, prop, ty_, desc in [
    ("panel-width", "signin-panel", "default", "w", "dimension", "The sign-in card width."),
    ("panel-height", "signin-panel", "default", "h", "dimension", "The sign-in card height."),
    ("panel-bg", "signin-panel", "default", "backgroundColor", "color", "The card field."),
    ("panel-ink", "signin-panel", "default", "color", "color", "The card ink."),
    ("field-bg", "signin-field", "default", "backgroundColor", "color", "The e-mail field fill."),
    ("field-ink", "signin-field", "default", "color", "color", "The field text ink."),
    ("field-height", "signin-field", "default", "h", "dimension", "The e-mail field height."),
    ("submit-fill", "signin-submit", "default", "backgroundColor", "color", "The 'Continue with email' button fill."),
    ("submit-ink", "signin-submit", "default", "color", "color", "The button text."),
    ("submit-height", "signin-submit", "default", "h", "dimension", "The button height."),
    ("google-ink", "signin-google", "default", "color", "color", "The 'Continue with Google' ink."),
    ("google-fill", "signin-google", "default", "backgroundColor", "color", "The 'Continue with Google' fill."),
]:
    try:
        if prop in ("w", "h"):
            v = rc(cname, state, prop)
            login[name] = lit(("%g" % v) + "px", ty_, f"measured {prop} of {cname} {state} on auth.factory.ai (raw/components-computed.json)", desc)
        else:
            login[name] = lit(norm_color(opaque(st(cname, state)[prop])), ty_,
                f"computed {prop} of {cname} {state} on auth.factory.ai (raw/components-computed.json)", desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
