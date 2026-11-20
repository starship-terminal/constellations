#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

Exa's signed-out surface is three public sites, captured on 2026-11-14:

  exa.ai          the marketing site: light only, a Next.js app whose
                  :root declares a real token layer — --cream/--greige*/
                  --gold/--charcoal neutrals, the --brand-* #1f40ed scale,
                  --secondary-*, a --gray-50..950 hex ramp, --accent-* and
                  --dark-accent-* badge pairs, named one-off colours
                  (raven, orchid, pauper…), --text-dark-*/--text-light-*
                  roles, --font-family-* stacks (ABCDiatype / Arizona /
                  SuisseIntlMono), --nav-height/--announcement-banner-height/
                  --*-container layout metrics, --border-radius-* radii and
                  the --hero-*/--text-swap-*/--digit-* animation vars.
  auth.exa.ai     the sign-in card dashboard.exa.ai redirects to: light only,
                  its own --background/--foreground/--text-light-* roles, a
                  cream-toned --secondary-* scale (different values from the
                  marketing one), --gray-*, --brand-*, --color-* utility
                  hues and --font-family-arizona-flare/--font-family-geist-mono
                  over "ABC Diatype Unlicensed Trial".
  exa.ai/docs     the Mintlify docs: a real light AND dark pair on
                  html.light/html.dark — --primary "24 64 237" (#1840ed, a
                  hair off the marketing --brand-default #1f40ed), the
                  docs' own cool-toned --gray-* triplet ramp,
                  --background-light/--background-dark and
                  --default-border-color that flips #eeeff5 -> #26272c, the
                  Mintlify --color-* design layer (the --color-exa-blue-*/
                  --color-exa-gray-* ramps, --color-brand-*/--color-neutral-*/
                  --color-danger-*/--color-success-*/--color-warning-*
                  roles), --docs-* component vars, --twoslash-* code vars,
                  --motion-*, Inter + Paper Mono + a headings stack that
                  reuses ABCDiatype.

The names collide across surfaces — marketing and docs both declare
--gray-*/--background/--secondary-*/--text-light-* with different values —
so vars.mjs resolves each name in a probe carrying its own surface's sheets
(resolved.surfaces.*); the spec reads the marketing values from the
marketing probe, the docs values from docs-light/docs-dark and the auth
values from auth, and resolved.light (marketing preferred) only where a
name has no collision risk.

Declared scales land under core.*; per-theme semantics under light.* and
dark.*; measured geometry under component.*. The marketing site and sign-in
card paint light only, so their roles exist only in the light set — the
dark set holds the docs theme alone.
"""

import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
RD = V.get("resolved", {}).get("dark", {})
SURF = V.get("resolved", {}).get("surfaces", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]


def surf(name):
    return {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v)
            for n, v in SURF.get(name, {}).items()}


R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}
D = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RD.items()}
RM = surf("marketing")
RA = surf("auth")
RLD = surf("docs-light")
RDD = surf("docs-dark")


def var(name, ty="color", surface=None, **kw):
    """A leaf that names a declared variable. `surface` notes which probe's
    value the token resolves to when several surfaces declare the name —
    build_tokens.py reads it to pick the right DECL map."""
    d = {"var": name, "type": ty}
    if surface:
        d["surface"] = surface
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. Exa's public "
    "surface is three sites: the exa.ai marketing pages (light only, a "
    "--brand-*/--gray-*/--secondary-*/--cream token layer), the auth.exa.ai "
    "sign-in card dashboard.exa.ai redirects to (light only, its own "
    "--text-light-*/--secondary-* values) and the exa.ai/docs Mintlify docs "
    "(a real light/dark pair: --primary/--gray-* triplets, "
    "--default-border-color flips, the Mintlify --color-* layer and "
    "--docs-*/--twoslash-* component vars). Declared scales under core.*; "
    "the marketing and sign-in roles under light.*; the docs roles under "
    "light.* and dark.*. Measured roles alias the declared values they "
    "match."),
    "core": {}, "light": {}, "dark": {}, "component": {}, "_gaps": []}


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


def _srgb_to_hex(r, g, b):
    return "#%02x%02x%02x" % tuple(max(0, min(255, round(x * 255))) for x in (r, g, b))


def _linear(u):
    return u / 12.92 if u <= 0.04045 else ((u + 0.055) / 1.055) ** 2.4


def _gamma(u):
    return 12.92 * u if u <= 0.0031308 else 1.055 * u ** (1 / 2.4) - 0.055


def oklab_to_rgb(L, a, b):
    """Björn Ottosson's OKLab -> sRGB matrix, for the oklab()/oklch() tints
    Mintlify's Tailwind-v4 stylesheet paints (nav-item hovers, overlay
    alphas)."""
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l_, m_, s_ = l_ ** 3, m_ ** 3, s_ ** 3
    r = +4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_
    g = -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_
    b_ = -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_
    return _gamma(r), _gamma(g), _gamma(b_)


def lab_to_rgb(L, a, b):
    """CIE Lab -> XYZ (D50 white) -> linear sRGB (Bradford-adapted, combined
    in one matrix), for the plain lab()/lch() strings computed styles emit."""
    fy = (L + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    eps, kap = 0.008856, 903.3
    xr = fx ** 3 if fx ** 3 > eps else (116 * fx - 16) / kap
    yr = fy ** 3 if L > kap * eps else L / kap
    zr = fz ** 3 if fz ** 3 > eps else (116 * fz - 16) / kap
    X, Y, Z = xr * 0.96422, yr, zr * 0.82521
    r = +3.1338561 * X - 1.6168667 * Y - 0.4906146 * Z
    g = -0.9787684 * X + 1.9161415 * Y + 0.0334540 * Z
    b_ = +0.0719453 * X - 0.2289914 * Y + 1.4052427 * Z
    return _gamma(r), _gamma(g), _gamma(b_)


def css_color(v):
    """Normalize a computed colour string to hex/rgba. Handles rgb(), hex,
    color(srgb ...), oklab() and oklch() — the forms the computed styles carry."""
    v = (v or "").strip()
    m = re.fullmatch(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)", v)
    if m:
        r, g, b, a = (float(x) if x else None for x in m.groups())
        if a is None or a >= 1:
            return _srgb_to_hex(r, g, b)
        return "rgba(%d, %d, %d, %s)" % (round(r * 255), round(g * 255), round(b * 255), "%g" % a)
    m = re.fullmatch(r"oklab\(([\d.]+) ([-\d.]+) ([-\d.]+)(?: / ([\d.]+))?\)", v)
    if m:
        L, a, b, al = (float(x) if x else None for x in m.groups())
        r, g, b2 = oklab_to_rgb(L, a, b)
        if al is None or al >= 1:
            return _srgb_to_hex(r, g, b2)
        return "rgba(%d, %d, %d, %s)" % (round(r * 255), round(g * 255), round(b2 * 255), "%g" % al)
    m = re.fullmatch(r"oklch\(([\d.]+) ([\d.]+) ([\d.]+)(?:deg)?(?: / ([\d.]+))?\)", v)
    if m:
        import math
        L, cc, h, al = (float(x) if x else None for x in m.groups())
        a = cc * math.cos(math.radians(h))
        b = cc * math.sin(math.radians(h))
        r, g, b2 = oklab_to_rgb(L, a, b)
        if al is None or al >= 1:
            return _srgb_to_hex(r, g, b2)
        return "rgba(%d, %d, %d, %s)" % (round(r * 255), round(g * 255), round(b2 * 255), "%g" % al)
    # Plain CIE lab()/lch() — Chrome reports a declared lab() colour back in
    # the computed style (the sign-in field's placeholder painted as
    # "lab(65.9269 -0.832707 -8.17473)").
    m = re.fullmatch(r"lch\(([\d.]+) ([\d.]+) ([\d.]+)(?:deg)?(?: / ([\d.]+))?\)", v)
    if m:
        import math
        L, cc, h, al = (float(x) if x else None for x in m.groups())
        a = cc * math.cos(math.radians(h))
        b = cc * math.sin(math.radians(h))
        r, g, b2 = lab_to_rgb(L, a, b)
        if al is None or al >= 1:
            return _srgb_to_hex(r, g, b2)
        return "rgba(%d, %d, %d, %s)" % (round(r * 255), round(g * 255), round(b2 * 255), "%g" % al)
    m = re.fullmatch(r"lab\(([\d.]+) ([-\d.]+) ([-\d.]+)(?: / ([\d.]+))?\)", v)
    if m:
        L, a, b, al = (float(x) if x else None for x in m.groups())
        r, g, b2 = lab_to_rgb(L, a, b)
        if al is None or al >= 1:
            return _srgb_to_hex(r, g, b2)
        return "rgba(%d, %d, %d, %s)" % (round(r * 255), round(g * 255), round(b2 * 255), "%g" % al)
    return norm_color(v)


COLOR_FULL = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\))")


def need(comp, state, prop=None):
    """The style (or one property) of a reading a row relies on. A renamed or missing
    component, state or property stops the build: a silent skip would drop the token and
    still pass."""
    try:
        s = C[comp]["states"][state]
    except KeyError:
        raise SystemExit(f"{comp} {state}: no such reading in raw/components-computed.json; fix the row or recapture")
    if "style" not in s or s.get("skipped") or s.get("via") == "focus failed":
        raise SystemExit(f"{comp} {state}: no usable reading ({s.get('skipped') or s.get('error') or s.get('via')})")
    if prop is None:
        return s["style"]
    v = s["style"].get(prop)
    if v is None or not str(v).strip():
        raise SystemExit(f"{comp} {state}: no {prop} in its reading")
    return v


def gap(path, why):
    """A token the spec deliberately leaves out, with the reason; written to
    raw/component-tokens.json `_gaps` so the omission is on the record."""
    SPEC["_gaps"].append({"token": path, "why": why})


def transparent(v):
    return bool(re.fullmatch(r"rgba\(\s*\d+,\s*\d+,\s*\d+,\s*0\s*\)", css_color(v)))


def split_list(v):
    """Top-level comma split of a computed list value (transitions, shadows)."""
    return [p.strip() for p in re.split(r",\s*(?![^()]*\))", v or "") if p.strip()]


UA_RING = "#101010"  # Chrome's own -webkit-focus-ring-color: an `auto` outline in it is the browser default


def painted_ring(sty):
    """(colour, how) of the focus ring a state really paints, from its computed style: a drawn
    outline (a style other than none, a width above 0, and not the browser's default `auto` ring
    colour), else the outermost visible box-shadow layer with a spread, else None. Ported from
    fal's builder."""
    style, colour = sty.get("outlineStyle", "none"), sty.get("outlineColor")
    if style != "none" and float(sty.get("outlineWidth", "0px")[:-2] or 0) > 0 and not transparent(colour) \
            and not (style == "auto" and css_color(colour) == UA_RING):
        return colour, f"outline {sty['outlineWidth']} {style}"
    ring = None
    for layer in split_list(sty.get("boxShadow", "none")):
        m = re.match(r"^(rgba?\([^)]*\))\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(\s+inset)?$", layer)
        if not m or m.group(6) or float(m.group(5)) <= 0 or transparent(m.group(1)):
            continue
        ring = (m.group(1), f"box-shadow {m.group(5)}px spread")
    return ring


def fill(comp, state, prop, parent=False):
    """(raw colour, source) of a surface. A transparent reading is no surface: with parent=True
    (the row names a container the element sits in) the parent's painted background is used,
    otherwise (None, why) so the caller records a gap."""
    raw = need(comp, state, prop)
    if not transparent(raw):
        return raw, f"computed {prop} of {comp} {state} (raw/components-computed.json)"
    if parent:
        a = next((a for a in C[comp]["states"][state].get("ancestors") or []
                  if a.get("up") == 1 and a.get("bg") and not transparent(a["bg"])), None)
        if a:
            return a["bg"], (f"the background of {comp}'s parent {a['node']} {state} (raw/components-computed.json "
                             f"ancestors); {comp} itself computes a transparent {prop}")
    return None, f"{comp} {state} computes a transparent {prop} (rgba(0, 0, 0, 0)) and paints no fill of its own"


def lit(value, ty, src, desc):
    return {"value": css_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


colors = SPEC["core"].setdefault("color", {})
color_alias = {}   # normalized colour -> 'color.<path>' for aliasing measured roles


# ------------------------------------------------------------- marketing palette
#
# exa.ai declares the real token layer on :root: the --brand-* scale around
# #1f40ed, --secondary-* neutrals, --gray-50..950, --cream/--greige*/--gold/
# --charcoal, --accent-*/--dark-accent-* badge pairs, --text-dark-*/
# --text-light-* roles and a shelf of named one-off colours.

brand = colors.setdefault("brand", {})
for name in sorted(k for k in RM if k.startswith("--brand-")):
    key = name[len("--brand-"):]
    ty = "color" if COLOR_FULL.fullmatch(str(RM[name]).strip()) else "other"
    brand[key] = var(name, ty, "marketing", description=f"The declared `{name}` — the marketing brand scale (#1f40ed blue).")
    if ty == "color":
        color_alias.setdefault(norm_color(RM[name]), f"color.brand.{key}")

secondary = colors.setdefault("secondary", {})
for name in sorted(k for k in RM if k.startswith("--secondary-")):
    key = name[len("--secondary-"):]
    ty = "color" if COLOR_FULL.fullmatch(str(RM[name]).strip()) else "other"
    secondary[key] = var(name, ty, "marketing", description=f"The declared `{name}` — the marketing secondary scale.")
    if ty == "color":
        color_alias.setdefault(norm_color(RM[name]), f"color.secondary.{key}")

gray = colors.setdefault("gray", {})
for name in sorted(k for k in RM if re.fullmatch(r"--gray-\d+", k)):
    key = name[len("--gray-"):]
    gray[key] = var(name, "color", "marketing", description=f"The declared `{name}` — the marketing neutral ramp.")
    color_alias.setdefault(norm_color(RM[name]), f"color.gray.{key}")

neutral = colors.setdefault("neutral", {})
for name, key, desc in [
    ("--cream", "cream", "The cream #faf9f7 page field."),
    ("--cream-darker", "cream-darker", "The darker cream #f0ece8 band."),
    ("--greige", "greige", "The #58544e greige body ink."),
    ("--greige-light", "greige-light", "The #787572 lighter greige."),
    ("--greige-lightest", "greige-lightest", "The #c2bfbb lightest greige."),
    ("--gold", "gold", "The #89661a gold (the announcement strip, rating stars)."),
    ("--charcoal", "charcoal", "The #111111 charcoal ink."),
    ("--black", "black", "Pure black."),
    ("--white", "white", "Pure white."),
    ("--background", "background", "The declared white surface."),
]:
    if name in RM:
        neutral[key] = var(name, "color", "marketing", description=desc)
        color_alias.setdefault(norm_color(RM[name]), f"color.neutral.{key}")

# The named one-offs the marketing sheets declare — poetic names kept as-is.
named = colors.setdefault("named", {})
for name in sorted(k for k in RM if re.fullmatch(
        r"--(raven|orchid|pauper|thamar-black|carbon|winter-park|burnished-metal|pearl-necklace|cerebral-grey|lucky-grey|virtual-violet|blood-burst|pouty-purple|light-shojin-blue|paper-white)", k)):
    key = name[len("--"):]
    ty = "color" if COLOR_FULL.fullmatch(str(RM[name]).strip()) else "other"
    named[key] = var(name, ty, "marketing", description=f"The declared `{name}` — a named marketing colour.")
    if ty == "color":
        color_alias.setdefault(norm_color(RM[name]), f"color.named.{key}")

accent = colors.setdefault("accent", {})
for name in sorted(k for k in RM if re.fullmatch(r"--accent(-[a-z0-9-]+)?", k)):
    key = name[len("--accent-"):] if name != "--accent" else "default"
    accent[key] = var(name, "color", "marketing", description=f"The declared `{name}` — a light-theme badge accent pair member.")
    color_alias.setdefault(norm_color(RM[name]), f"color.accent.{key}")

dark_accent = colors.setdefault("darkAccent", {})
for name in sorted(k for k in RM if k.startswith("--dark-accent-")):
    key = name[len("--dark-accent-"):]
    dark_accent[key] = var(name, "color", "marketing", description=f"The declared `{name}` — a dark-theme badge accent pair member.")
    color_alias.setdefault(norm_color(RM[name]), f"color.darkAccent.{key}")

txt = colors.setdefault("text", {})
for name in sorted(k for k in RM if re.fullmatch(r"--text-(dark|light)-[a-z]+", k)):
    key = name[len("--text-"):]
    txt[key] = var(name, "color", "marketing",
                   description=f"The declared `{name}` — the text roles for {'dark' if 'text-dark' in name else 'light'} surfaces.")
    color_alias.setdefault(norm_color(RM[name]), f"color.text.{key}")

# ------------------------------------------------------------- auth palette
#
# auth.exa.ai re-declares --brand-*/--gray-* (same values) plus its own
# --text-light-* roles and a cream-toned --secondary-* scale — the card's
# surface differs from the marketing site's white.

auth_c = colors.setdefault("auth", {})
for name in sorted(k for k in RA if re.fullmatch(r"--text-light-[a-z]+", k)):
    key = name[len("--text-light-"):]
    auth_c.setdefault("text-light", {})[key] = var(name, "color", "auth",
        description=f"The declared `{name}` — the sign-in card's own text roles.")
    color_alias.setdefault(norm_color(RA[name]), f"color.auth.text-light.{key}")
for name in sorted(k for k in RA if re.fullmatch(r"--secondary-[a-z0-9]+", k)):
    key = name[len("--secondary-"):]
    auth_c.setdefault("secondary", {})[key] = var(name, "color", "auth",
        description=f"The declared `{name}` — the auth card's cream-toned secondary scale (different values from marketing's).")
    color_alias.setdefault(norm_color(RA[name]), f"color.auth.secondary.{key}")
for name in sorted(k for k in RA if re.fullmatch(r"--(background|foreground)", k)):
    key = name[len("--"):]
    auth_c[key] = var(name, "color", "auth", description=f"The declared `{name}` — the sign-in card's surface role.")
    color_alias.setdefault(norm_color(RA[name]), f"color.auth.{key}")

# ------------------------------------------------------------- docs palette (Mintlify)
#
# The docs' own layer: --primary triplets, their cool-toned --gray-* ramp,
# the Mintlify --color-* design layer (exa-blue/exa-gray ramps, brand/
# neutral/danger/success/warning roles) and --docs-* component vars.

docs_c = colors.setdefault("docs", {})
for name in sorted(k for k in RLD if re.fullmatch(r"--gray-\d+", k)):
    key = name[len("--gray-"):]
    docs_c.setdefault("gray", {})[key] = var(name, "color", "docs-light",
        description=f"The declared `{name}` — the docs' cool-toned grey ramp (different values from marketing's).")
    color_alias.setdefault(norm_color(RLD[name]), f"color.docs.gray.{key}")
for name, key in [("--primary", "primary"), ("--primary-light", "primary-light"),
                  ("--primary-dark", "primary-dark"), ("--background-light", "background-light"),
                  ("--background-dark", "background-dark"), ("--default-border-color", "default-border"),
                  ("--tooltip-foreground", "tooltip-foreground"), ("--docs-accent", "docs-accent")]:
    if name in RLD:
        ty = "color" if COLOR_FULL.fullmatch(str(RLD[name]).strip()) else "other"
        docs_c[key] = var(name, ty, "docs-light", description=f"The declared `{name}` — the docs theme vars.")
        if ty == "color":
            color_alias.setdefault(norm_color(RLD[name]), f"color.docs.{key}")
# The Mintlify --color-* layer, grouped by family.
mlp = docs_c.setdefault("mintlify", {})
seen_grp = {}
for name in sorted(k for k in RLD if k.startswith("--color-")):
    rest = name[len("--color-"):]
    m = re.fullmatch(r"((?:exa-)?[a-z]+)-(\d+)", rest) or re.fullmatch(r"(exa-[a-z]+)-(\d+)", rest)
    if m:
        grp, key = m.group(1), m.group(2)
    else:
        parts = rest.split("-", 1)
        grp, key = parts[0], (parts[1] if len(parts) > 1 else "default")
    ty = "color" if COLOR_FULL.fullmatch(str(RLD[name]).strip()) else "other"
    node = mlp.setdefault(grp, {})
    node[key] = var(name, ty, "docs-light", description=f"The declared `{name}` — the docs' Mintlify design layer.")
    if ty == "color":
        color_alias.setdefault(norm_color(RLD[name]), f"color.docs.mintlify.{grp}.{key}")
# --docs-* component vars that resolve to colours.
ddv = docs_c.setdefault("vars", {})
for name in sorted(k for k in RLD if k.startswith("--docs-")):
    if COLOR_FULL.fullmatch(str(RLD[name]).strip()):
        key = name[len("--docs-"):]
        ddv[key] = var(name, "color", "docs-light", description=f"The declared `{name}` — a docs component colour.")
        color_alias.setdefault(norm_color(RLD[name]), f"color.docs.vars.{key}")

# ------------------------------------------------------------------- fonts
#
# Marketing: ABCDiatype body/UI, Arizona (ABC Arizona Flare) display,
# SuisseIntlMono. Auth: ABC Diatype Unlicensed Trial, ABC Arizona Flare,
# Geist Mono. Docs: Inter, Paper Mono, and a headings stack that reuses
# ABCDiatype.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for name, m, where, key, desc in [
    ("--font-family-sans", RM, "marketing", "diatype", "ABCDiatype — the marketing body/UI face."),
    ("--font-family-serif", RM, "marketing", "arizona", "Arizona (ABC Arizona Flare) — the marketing display face ('The world's data for AI agents')."),
    ("--font-family-monospace", RM, "marketing", "mono", "SuisseIntlMono — the marketing mono."),
    ("--font-family-sans", RA, "auth", "auth-sans", "ABC Diatype Unlicensed Trial — the sign-in card's face."),
    ("--font-family-arizona-flare", RA, "auth", "auth-flare", "ABC Arizona Flare — the sign-in card's display face."),
    ("--font-family-geist-mono", RA, "auth", "geist-mono", "Geist Mono — the sign-in card's code face."),
    ("--font-inter", RLD, "docs-light", "inter", "Inter — the docs body/UI face."),
    ("--font-paper-mono", RLD, "docs-light", "paper-mono", "Paper Mono — the docs code face."),
    ("--default-font-family", RLD, "docs-light", "docs-sans", "The docs' declared default stack (Inter first)."),
    ("--default-mono-font-family", RLD, "docs-light", "docs-mono", "The docs' declared default mono stack (Paper Mono first)."),
    ("--font-family-headings-custom", RLD, "docs-light", "docs-headings", "The docs' headings stack — ABCDiatype first, the marketing face reused."),
]:
    if name in m:
        fam[key] = var(name, "fontFamily", where, description=desc)

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for name, m, key, desc in [
    ("--font-weight-normal", RLD, "normal", "400 — body and UI text everywhere."),
    ("--font-weight-medium", RLD, "medium", "500 — nav items, labels, docs code."),
    ("--font-weight-semibold", RLD, "semibold", "600 — docs headings."),
    ("--font-weight-bold", RLD, "bold", "700 — declared."),
    ("--font-weight-extrabold", RLD, "extrabold", "800 — declared."),
    ("--font-weight-headings-custom", RLD, "headings", "The docs headings' declared weight."),
]:
    if name in m:
        weights[key] = var(name, "fontWeight", "docs-light", description=desc)

# ------------------------------------------------------------- type ramp

size = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("nav", "mkt-nav-link", "default", "The marketing header-link size."),
    ("small", "demo-output", "default", "The small copy size inside the demo output."),
    ("docs-body", "docs-para", "default", "The docs paragraph size."),
    ("docs-code", "docs-code", "default", "The docs code size."),
    ("field", "demo-textarea", "default", "The demo query field size."),
    ("body", "hero-sub", "default", "The hero lede size."),
    ("auth", "auth-google", "default", "The sign-in button text size."),
    ("docs-h1", "docs-h1", "default", "The docs page heading size."),
    ("pricing-h1", "pricing-h1", "default", "The pricing page heading size."),
    ("mobile-display", "m-hero-h1", "default", "The display size at 390px."),
    ("display", "hero-h1", "default", "The marketing display size ('The world's data for AI agents')."),
]:
    need(comp, state, "fontSize")
    size[key] = lit(ts(comp, state, "fontSize"), "dimension",
                    f"computed fontSize of {comp} {state} (raw/components-computed.json)", desc)

lh = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for name, key, desc in [
    ("--leading-tight", "tight", "The declared tight leading."),
    ("--leading-normal", "normal", "The declared normal leading."),
    ("--leading-relaxed", "relaxed", "The declared relaxed leading."),
]:
    if name in RLD:
        lh[key] = var(name, "number", "docs-light", description=desc)
for key, comp, desc in [
    ("display", "hero-h1", "The display's own leading."),
    ("body", "hero-sub", "The lede's leading."),
    ("docs-body", "docs-para", "The docs paragraph leading."),
    ("nav", "mkt-nav-link", "The header link's leading."),
    ("auth", "auth-google", "The sign-in button's leading."),
]:
    state = "default"
    need(comp, state, "lineHeight")
    lh[key] = lit(ts(comp, state, "lineHeight"), "dimension",
                  f"computed lineHeight of {comp} {state} (raw/components-computed.json)", desc)

tr = SPEC["core"].setdefault("font", {}).setdefault("tracking", {})
for name, key, desc in [
    ("--tracking-tighter", "tighter", "The declared tighter tracking."),
    ("--tracking-tight", "tight", "The declared tight tracking."),
    ("--tracking-normal", "normal", "The declared normal tracking."),
    ("--tracking-wide", "wide", "The declared wide tracking."),
]:
    if name in RLD:
        tr[key] = var(name, "other", "docs-light", description=desc)
for key, comp, desc in [
    ("display", "hero-h1", "The display's tracking."),
    ("nav", "mkt-nav-link", "The header link's tracking."),
]:
    state = "default"
    need(comp, state, "letterSpacing")
    if ts(comp, state, "letterSpacing") != "normal":
        tr[key] = lit(ts(comp, state, "letterSpacing"), "dimension",
                      f"computed letterSpacing of {comp} {state} (raw/components-computed.json)", desc)

# ------------------------------------------------- declared layout metrics

dim = SPEC["core"].setdefault("size", {})
for name, key, desc in [
    ("--nav-height", "nav", "The declared 55px marketing header."),
    ("--total-header-height", "header", "The declared 55px total header height."),
    ("--announcement-banner-height", "banner", "The declared 48px announcement strip."),
    ("--banner-height", "docs-banner", "The docs' banner slot."),
    ("--mintlify-slot-header-height", "docs-header", "The docs' declared header slot."),
    ("--spacing", "docs-base", "The docs/Tailwind 4px spacing base."),
    ("--scroll-mt", "docs-scroll-mt", "The docs' scroll offset for anchors."),
]:
    m = RM if name in RM else RLD
    if name in m:
        dim[key] = var(name, "dimension", "marketing" if m is RM else "docs-light", description=desc)
cont = dim.setdefault("container", {})
for m, where in ((RM, "marketing"), (RLD, "docs-light")):
    for name in sorted(k for k in m if re.fullmatch(r"--[a-z-]*container[a-z0-9-]*", k)):
        key = name.lstrip("-")
        if key not in cont:
            cont[key] = var(name, "dimension", where,
                            description=f"The declared `{name}` container/page width ({where}).")

radii = SPEC["core"].setdefault("radius", {})
for name, key, desc in [
    ("--border-radius-default", "default", "The declared 2px default radius."),
    ("--border-radius-4", "4", "The declared 4px radius."),
    ("--border-radius-8", "8", "The declared 8px radius (matches --radius)."),
    ("--border-radius-10", "10", "The declared 10px radius."),
    ("--border-radius-20", "20", "The declared 20px radius."),
    ("--border-radius-1000", "pill", "The declared 1000px pill radius."),
    ("--radius", "base", "The declared 8px base radius."),
    ("--docs-radius", "docs", "The docs' declared 6px radius."),
    ("--radius-xl", "docs-xl", "The docs' declared 12px extra-large radius."),
]:
    m = RM if name in RM else RLD
    if name in m:
        radii[key] = var(name, "dimension", "marketing" if m is RM else "docs-light", description=desc)
for key, comp, state, prop, desc in [
    ("control", "demo-pill", "default", "borderTopLeftRadius", "The demo pill radius."),
    ("field", "demo-textarea", "default", "borderTopLeftRadius", "The demo field's radius."),
    ("menu", "mkt-menu", "default", "paint:radius", "The mega-menu card radius — the rounded child paints 8px; the wrapper itself is unrounded."),
    ("cta", "hero-cta", "default", "borderTopLeftRadius", "The CTA pill radius."),
    ("auth-field", "auth-email", "default", "borderTopLeftRadius", "The sign-in field radius."),
    ("search", "docs-search", "default", "borderTopLeftRadius", "The docs search pill radius."),
]:
    if prop == "paint:radius":
        need(comp, state)
        try:
            v = painted(comp, state, "radius")
        except KeyError:
            raise SystemExit(f"{comp} {state}: no painted radius in its paint list")
        radii.setdefault(key + "-measured", lit(v, "dimension",
            f"the painted radius of {comp}'s rounded child {state} (raw/components-computed.json paint list)", desc))
    else:
        radii.setdefault(key + "-measured", lit(need(comp, state, prop), "dimension",
            f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc))

# ------------------------------------------------------------- elevation

sh = SPEC["core"].setdefault("shadow", {})
for key, comp, prop, desc in [
    ("menu", "mkt-menu", "paint:shadow", "The mega-menu's drop shadow — painted on the rounded child; the wrapper itself is an unshadowed positioning box."),
    ("widget", "demo-widget", "boxShadow", "The demo widget's shadow."),
    ("cta", "hero-cta", "boxShadow", "The CTA's shadow."),
]:
    state = "default"
    if prop == "paint:shadow":
        need(comp, state)
        try:
            shadow = painted(comp, state, "shadow")
        except KeyError:
            raise SystemExit(f"{comp} {state}: no painted shadow in its paint list")
    else:
        shadow = need(comp, state, prop)
    if shadow == "none":
        gap(f"core.shadow.{key}", f"{comp} {state} computes no box-shadow")
    else:
        src = (f"the painted shadow of {comp}'s rounded child {state} (raw/components-computed.json paint list)"
               if prop == "paint:shadow" else
               f"computed boxShadow of {comp} {state} (raw/components-computed.json)")
        sh[key] = lit(shadow, "other", src, desc)
for name in sorted(k for k in RLD if re.search(r"shadow", k)):
    key = name.lstrip("-")
    sh.setdefault(key, var(name, "other", "docs-light", description=f"The declared `{name}`."))

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
for name, m, key, ty, desc in [
    ("--default-transition-duration", RLD, "duration", "duration", "The declared 150ms default transition duration."),
    ("--default-transition-timing-function", RLD, "easing", "cubicBezier", "The declared default curve."),
    ("--ease-in", RLD, "ease-in", "cubicBezier", "The declared ease-in curve."),
    ("--ease-out", RLD, "ease-out", "cubicBezier", "The declared ease-out curve."),
    ("--ease-in-out", RLD, "ease-in-out", "cubicBezier", "The declared ease-in-out curve."),
    ("--motion-duration", RLD, "docs-duration", "duration", "The docs' declared motion duration."),
    ("--motion-duration-fast", RLD, "docs-fast", "duration", "The docs' fast motion duration."),
    ("--motion-duration-slow", RLD, "docs-slow", "duration", "The docs' slow motion duration."),
    ("--motion-duration-drawer", RLD, "docs-drawer", "duration", "The docs' drawer motion duration."),
    ("--motion-easing-standard", RLD, "docs-easing", "cubicBezier", "The docs' standard curve."),
    ("--motion-easing-out", RLD, "docs-ease-out", "cubicBezier", "The docs' ease-out."),
    ("--motion-easing-in-out", RLD, "docs-ease-in-out", "cubicBezier", "The docs' ease-in-out."),
    ("--motion-easing-drawer", RLD, "docs-drawer-ease", "cubicBezier", "The docs' drawer easing."),
    ("--text-swap-dur", RM, "text-swap", "duration", "The hero headline's word-swap duration."),
    ("--text-swap-ease", RM, "text-swap-ease", "other", "The word-swap easing."),
    ("--digit-dur", RM, "digit", "duration", "The stat digits' roll duration."),
]:
    if name in m:
        mo[key] = var(name, ty, "docs-light" if m is RLD else "marketing", description=desc)


def transition(s):
    """The transition shorthand of a computed style, one `<property> <duration> <easing>` item
    per property: CSS repeats the duration and easing lists to the length of the property list,
    so they are paired by index, never pasted after the whole property list."""
    props = split_list(s.get("transitionProperty") or "all")
    durs = split_list(s.get("transitionDuration") or "0s")
    eases = split_list(s.get("transitionTimingFunction") or "ease")
    return ", ".join(f"{p} {durs[i % len(durs)]} {eases[i % len(eases)]}" for i, p in enumerate(props))


if need("mkt-nav-link", "default", "transitionDuration") != "0s":
    mo["control"] = lit(transition(need("mkt-nav-link", "default")), "other",
                        "computed transition of mkt-nav-link default (raw/components-computed.json)",
                        "The marketing nav control's transition.")
else:
    gap("core.motion.control", "mkt-nav-link default declares no transition")
# A reduced-motion reading counts only when it names a transition with a non-zero duration:
# Chrome reports a declared-nothing transition as "all", which is not a transition at all.
rm = json.loads((RAW / "components-computed.json").read_text())["_meta"].get("reducedMotion") or {}
for slot, info in rm.items():
    tr_ = (info.get("reduce") or {}).get("transition") or ""
    if re.search(r"(?<![\d.])(?!0s\b)(?!0ms\b)\d*\.?\d+m?s\b", tr_):
        mo.setdefault("control-reduced", lit(tr_, "other",
            f"transition of {info.get('selector')} still applied under prefers-reduced-motion on {info.get('page', slot)} (raw/components-computed.json)",
            "The control transition that survives reduced motion."))
if "control-reduced" not in mo:
    gap("core.motion.control-reduced", "no reduced-motion reading names a running transition: "
        + "; ".join(f"{i.get('selector')} on {i.get('page', k)} computes {((i.get('reduce') or {}).get('transition'))!r}" for k, i in rm.items()))

# ------------------------------------------------------------- breakpoints
#
# The public sheets' media contexts — declared @media conditions.

seen = set()
bps = SPEC["core"].setdefault("breakpoint", {})
for bin_ in ("theme", "app", "docs", "utility", "tailwind"):
    for r in V.get(bin_, []):
        for ctx in r.get("context", []):
            for m in re.finditer(r"(min|max)-width:\s*([\d.]+)px|width\s*(>=|<=)\s*([\d.]+)px", ctx or ""):
                kind = m.group(1) or {" >=": "min", " <=": "max"}.get(" " + m.group(3), m.group(3))
                kind = {"min": "min", "max": "max", ">=": "min", "<=": "max"}[kind]
                num = m.group(2) or m.group(4)
                val = num + "px"
                if val in seen:
                    continue
                seen.add(val)
                bps[f"{kind}-{num.replace('.', '-')}"] = lit(
                    val, "dimension", f"`{ctx.strip()}` in a public stylesheet (raw/css-vars.json rules)",
                    "A declared breakpoint in the public CSS.")

# ------------------------------------------- per-theme semantic variables
#
# The docs' Mintlify layer genuinely switches under html.dark:
# --default-border-color flips and the --docs-*/--twoslash-* component vars
# re-resolve. {"var"} leaves carry surface= so each set resolves its own
# probe's value.

ld, dd = SPEC["light"].setdefault("docs", {}), SPEC["dark"].setdefault("docs", {})
for name, key in [("--background-light", "surface"), ("--default-border-color", "border"),
                  ("--primary", "primary"), ("--docs-accent", "accent")]:
    if name in RLD:
        ld[key] = var(name, "color", "docs-light", description=f"The declared `{name}` on the docs light theme.")
for name, key in [("--background-dark", "surface"), ("--default-border-color", "border"),
                  ("--primary", "primary"), ("--docs-accent", "accent")]:
    if name in RDD:
        dd[key] = var(name, "color", "docs-dark", description=f"The declared `{name}` on the docs dark theme.")
for name in sorted(k for k in RLD if k.startswith("--twoslash-")):
    key = name[len("--twoslash-"):]
    ty = "color" if COLOR_FULL.fullmatch(str(RLD[name]).strip()) else "other"
    ld.setdefault("twoslash", {})[key] = var(name, ty, "docs-light")
    dd.setdefault("twoslash", {})[key] = var(name, ty, "docs-dark")
for name in sorted(k for k in RLD if k.startswith("--docs-") and COLOR_FULL.fullmatch(str(RLD[k]).strip())):
    key = name[len("--docs-"):]
    ld.setdefault("vars", {})[key] = var(name, "color", "docs-light")
for name in sorted(k for k in RDD if k.startswith("--docs-") and COLOR_FULL.fullmatch(str(RDD[k]).strip())):
    key = name[len("--docs-"):]
    dd.setdefault("vars", {})[key] = var(name, "color", "docs-dark")
for name in sorted(k for k in RDD if re.fullmatch(r"--color-(background|brand|neutral|danger|success|warning)[a-z-]*", k)):
    # Mintlify's own semantic layer flips per theme; the docs-light values
    # already sit under core.color.docs.mintlify.
    rest = name[len("--color-"):]
    parts = rest.split("-", 1)
    grp, key = parts[0], parts[1] if len(parts) > 1 else "default"
    dd.setdefault("mintlify", {}).setdefault(grp, {})[key] = var(name, "color", "docs-dark")

# --------------------------------------------- measured roles

role_alias = {"light": dict(color_alias), "dark": dict(color_alias)}
# The paths core.color.docs emitted above for these names, so an alias can never point at a
# path that does not exist (the old .replace('docs-', '') made --docs-accent color.docs.accent).
DOCS_PATH = {"--default-border-color": "color.docs.default-border", "--primary": "color.docs.primary",
             "--docs-accent": "color.docs.docs-accent"}
for name, path in DOCS_PATH.items():
    if name in RLD:
        assert path.split(".")[-1] in docs_c, path
        role_alias["light"].setdefault(norm_color(RLD.get(name)), path)
        # core holds the docs-light value, so a dark reading may alias it only when equal
        if norm_color(RDD.get(name)) == norm_color(RLD.get(name)):
            role_alias["dark"].setdefault(norm_color(RDD.get(name)), path)


def semcolor(raw, src, desc, theme="light"):
    v = css_color(raw)
    alias = role_alias[theme].get(v)
    value = f"{{{alias}}}" if alias else v
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


L = SPEC["light"]

# Components whose reading is of another element (README Known gaps): no colour is taken from them.
WRONG = {"auth-card": "auth-card measured the 360 x 98 e-mail form inside the card, not the card; recapture needed"}


def role(root, where, key, comp, state, prop, desc, theme, parent=False):
    """One measured colour role. `prop` is a computed property, "paint:bg" (the painted child's
    background) or "ring" (the focus ring the state really paints). A reading that paints nothing
    (a transparent fill, no ring) or comes from the wrong element is recorded under _gaps."""
    path = f"{theme}.{where}.{key}"
    if comp in WRONG:
        return gap(path, f"read from the wrong element: {WRONG[comp]}")
    if prop == "paint:bg":
        need(comp, state)
        try:
            raw = painted(comp, state, "bg")
        except KeyError:
            raise SystemExit(f"{comp} {state}: no painted background in its paint list")
        src = f"the painted background of {comp}'s rounded child {state} (raw/components-computed.json paint list)"
    elif prop == "ring":
        sty = need(comp, state)
        ring = painted_ring(sty)
        if not ring:
            return gap(path, f"{comp} {state} paints no focus ring of its own: outline {sty.get('outlineWidth')} "
                             f"{sty.get('outlineStyle')} {css_color(sty.get('outlineColor'))} is the browser's default "
                             f"auto ring, and no box-shadow layer has a spread")
        raw, how = ring
        src = (f"the {how} focus ring of {comp} {state} (raw/components-computed.json); "
               f"its outline is {sty.get('outlineWidth')} {sty.get('outlineStyle')}")
    elif prop == "backgroundColor":
        raw, src = fill(comp, state, prop, parent)
        if raw is None:
            return gap(path, src)
    else:
        raw = need(comp, state, prop)
        src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
    if str(raw).startswith(("oklab", "oklch")):
        src += f"; the browser painted {raw}, converted here"
    root[key] = semcolor(raw, src, desc, theme)


# ---- marketing surface (light only) ----
mkt = L.setdefault("marketing", {})
for key, comp, state, prop, desc in [
    ("surface", "mkt-header", "default", "backgroundColor", "The marketing field behind the header."),
    ("header-line", "mkt-header", "default", "borderBottomColor", "The header's hairline."),
    ("text", "mkt-nav-link", "default", "color", "The marketing header ink."),
    ("muted", "demo-output", "default", "color", "The muted text inside the demo output."),
    ("focus", "mkt-nav-link", "focus-visible", "ring", "The keyboard-focus ring on marketing links."),
    ("action", "mkt-signup", "default", "backgroundColor", "The black Sign-up pill fill."),
    ("on-action", "mkt-signup", "default", "color", "White text on the Sign-up pill."),
    ("sales-border", "mkt-sales", "default", "borderTopColor", "The Contact-sales button's border."),
    ("menu-surface", "mkt-menu", "default", "paint:bg", "The mega-menu surface — painted on the rounded child; the wrapper is a transparent positioning box."),
    ("menu-hover", "mkt-menu-item", "default", "backgroundColor", "The menu item's field."),
    ("demo-surface", "demo-widget", "default", "backgroundColor", "The demo widget's surface."),
    ("demo-pill-active", "demo-pill", "default", "color", "The active demo pill's ink."),
    ("run-fill", "demo-run", "default", "backgroundColor", "The blue Run-preview arrow fill."),
    ("announce-surface", "mkt-announce", "default", "backgroundColor", "The announcement strip's field."),
]:
    role(mkt, "marketing", key, comp, state, prop, desc, "light", parent=key == "announce-surface")
role(mkt, "marketing", "action-hover", "mkt-signup", "hover", "backgroundColor", "The Sign-up pill's hover fill.", "light")


def placeholder(comp):
    try:
        return C[comp]["states"]["default"]["placeholder"]["color"]
    except (KeyError, TypeError):
        raise SystemExit(f"{comp} default: no placeholder colour in raw/components-computed.json")


mkt["placeholder"] = semcolor(placeholder("demo-textarea"), "computed placeholder colour of demo-textarea default (raw/components-computed.json)",
                              "The demo query field's placeholder.", "light")

# ---- sign-in surface (light only) ----
sgn = L.setdefault("signin", {})
for key, comp, state, prop, desc in [
    ("card", "auth-card", "default", "backgroundColor", "The sign-in card's surface."),
    ("heading", "auth-heading", "default", "color", "The 'Start building with Exa' heading ink."),
    ("field", "auth-email", "default", "backgroundColor", "The e-mail field's fill."),
    ("field-border", "auth-email", "default", "borderTopColor", "The e-mail field's border."),
    ("field-focus", "auth-email", "focused", "borderTopColor", "The border the field draws when focused."),
    ("text", "auth-email", "default", "color", "The field text colour."),
    ("action", "auth-email-btn", "default", "backgroundColor", "The 'Continue with email' button fill."),
    ("on-action", "auth-email-btn", "default", "color", "The text on the e-mail button."),
    ("google-border", "auth-google", "default", "borderTopColor", "The Google button's border."),
    ("code-bg", "auth-code", "default", "backgroundColor", "The code sample's surface."),
]:
    role(sgn, "signin", key, comp, state, prop, desc, "light", parent=key == "code-bg")
sgn["placeholder"] = semcolor(placeholder("auth-email"), "computed placeholder colour of auth-email default (raw/components-computed.json)",
                              "The sign-in field's placeholder.", "light")

# ---- docs measured roles, both themes ----
for root, theme, rows in [
    (ld, "light", [
        ("text", "docs-h1", "default", "color", "The docs heading ink."),
        ("body-text", "docs-para", "default", "color", "The docs paragraph colour."),
        ("link", "docs-link", "default", "color", "The docs body-link colour."),
        ("nav-text", "docs-nav-item", "default", "color", "The sidebar nav item ink."),
        ("nav-active", "docs-nav-item", "default", "backgroundColor", "The active nav item's field."),
        ("code-bg", "docs-code", "default", "backgroundColor", "The code block's surface."),
        ("field", "docs-search", "default", "backgroundColor", "The search pill's field."),
        ("focus", "docs-search", "focus-visible", "ring", "The focus ring on docs controls."),
        ("rail-line", "docs-sidebar", "default", "borderRightColor", "The sidebar's hairline."),
        ("cta-surface", "docs-cta", "default", "backgroundColor", "The 'Add Exa to your agent' banner's field."),
    ]),
    (dd, "dark", [
        ("text", "d-docs-h1", "default", "color", "The docs dark heading ink."),
        ("body-text", "d-docs-para", "default", "color", "The docs dark paragraph colour."),
        ("link", "d-docs-link", "default", "color", "The docs dark body-link colour."),
        ("nav-text", "d-docs-nav-item", "default", "color", "The dark sidebar nav item ink."),
        ("nav-active", "d-docs-nav-item", "default", "backgroundColor", "The active nav item's field on dark."),
        ("code-bg", "d-docs-code", "default", "backgroundColor", "The code block's surface on dark."),
        ("field", "d-docs-search", "default", "backgroundColor", "The search pill's field on dark."),
        ("focus", "d-docs-search", "focus-visible", "ring", "The focus ring on dark."),
        ("rail-line", "d-docs-sidebar", "default", "borderRightColor", "The sidebar's hairline on dark."),
        ("cta-surface", "d-docs-cta", "default", "backgroundColor", "The CTA banner's field on dark."),
    ]),
]:
    for key, comp, state, prop, desc in rows:
        role(root, "docs", key, comp, state, prop, desc, theme, parent=key == "cta-surface")

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("header-height", "mkt-header", "default", "h", "dimension", "The marketing header height (the 55px --nav-height bar; the 48px --announcement-banner-height strip sits above it as a sibling)."),
    ("banner-height", "mkt-announce", "default", "h", "dimension", "The announcement strip's text row height (the strip itself is --announcement-banner-height 48px)."),
    ("mobile-header-height", "m-header", "default", "h", "dimension", "The phone header height."),
    ("menu-width", "mkt-menu", "default", "w", "dimension", "The Products mega-menu width."),
    ("hero-cta-height", "hero-cta", "default", "h", "dimension", "The Try-API CTA height."),
    ("demo-widget-width", "demo-widget", "default", "w", "dimension", "The demo widget width."),
    ("demo-field-height", "demo-textarea", "default", "h", "dimension", "The demo query field height."),
    ("demo-pill-height", "demo-pill", "default", "h", "dimension", "The demo pill height."),
    ("signup-height", "mkt-signup", "default", "h", "dimension", "The Sign-up pill height."),
    ("plan-card-width", "plan-card", "default", "w", "dimension", "A pricing plan card's width."),
    ("auth-card-width", "auth-card", "default", "w", "dimension", "The sign-in card width."),
    ("auth-field-height", "auth-email", "default", "h", "dimension", "The sign-in field height."),
    ("auth-button-height", "auth-google", "default", "h", "dimension", "The sign-in button height."),
    ("docs-sidebar-width", "docs-sidebar", "default", "w", "dimension", "The docs rail width."),
    ("docs-nav-item-height", "docs-nav-item", "default", "h", "dimension", "The docs nav item height."),
    ("docs-search-height", "docs-search", "default", "h", "dimension", "The docs search pill height."),
    ("hamburger", "m-hamburger", "default", "h", "dimension", "The phone hamburger hit area."),
]:
    need(cname, state)
    v = rc(cname, state, prop)
    src = f"measured {prop} of {cname} {state} (raw/components-computed.json)"
    if cname in WRONG:
        src = f"Reconstruction: read from the wrong element ({WRONG[cname]}); {src}"
    comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px", ty_, src, desc)

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
for g in SPEC["_gaps"]:
    print("  gap:", g["token"], "-", g["why"])
