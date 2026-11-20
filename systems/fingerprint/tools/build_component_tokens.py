#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

fingerprint.com is three public surfaces signed out. The marketing site
(fingerprint.com/...) is an Astro + Tailwind v4 app that declares a real
design-token layer in its stylesheets (raw/css-vars.json):

  --fpds-color-*       the FPDS palette as `H S% L%` channel triplets: ten
                       ramps (gray, blue, green, orange, pink, purple, red,
                       teal, yellow + black/white) on a 1-10 scale, and the
                       11 --fpds-color-syntax-* code-highlighting colours.
                       --color-* aliases them one step coarser (--color-blue-100
                       is hsl(var(--fpds-color-blue-1)), through the 1000s)
  --fpds-shadow-*      the declared shadow ramp 100-700 plus the
                       inset/inset-t/inset-b hairline steps
  --text-*             the Tailwind v4 type ramp 2xs (11px) - 6xl (48px),
                       each with a --text-*--line-height and a
                       --text-*--letter-spacing companion
  --font-*             --font-sans/--font-serif/--font-mono/--font-pixel
                       stacks (Inter, Petrona, JetBrains Mono, Geist Pixel)
                       and the --font-weight-* steps 200-700
  --radius-*           2/4/6/8/12/16/24px and the --radius 8px default
  --spacing            the 4px spacing base --container-* and
                       --container-content-* max-widths
  --shadow-*           the marketing aliases over --fpds-shadow-* plus
                       --shadow-button
  --ease-*, --leading-*, --tracking-*, --blur-*, --animate-*,
                       --default-transition-*
  --primary, --primary-hover, --primary-active, --border, --surface-raised
                       the semantic HSL triplets whose --color-* aliases are
                       the orange brand (#f35820), the gray-3 hairline and
                       the raised surface
  .dark                the only dark redeclaration the site ships: the 11
                       --fpds-color-syntax-* names, repointed at lighter
                       ramp steps inside code blocks. No public page carried
                       a dark theme while captured — an emulated
                       prefers-color-scheme: dark probe resolved :root
                       identically (raw/css-vars.json). The dark token set
                       holds only these declared syntax values, labelled so.

docs.fingerprint.com is a Mintlify docs site with its own token layer and a
real light/dark preference ("Change theme preference"); its measured values
land under component.*. dashboard.fingerprint.com /login and /signup are the
product shell's auth cards, a third stack; their measured values are
component.productShell literals.

Deterministic: same inputs, byte-identical output.
"""
import colorsys, json, pathlib, re

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
    "The token tree build_tokens.py turns into tokens.json. fingerprint.com "
    "declares its design-token layer in the marketing site's stylesheets "
    "(raw/css-vars.json): the FPDS channel-triplet palette under fpds.*, its "
    "resolved --color-* hex ramp under color.*, the Tailwind type/space/"
    "radius/container/shadow/ease scales under core.*, and the semantic "
    "--color-primary/-border/-surface-raised roles under light.*. The dark "
    "set holds only the 11 .dark-scoped syntax redeclarations — the site "
    "ships no dark theme, so they are declared values, not a painted page "
    "theme. Measured roles alias the declared values they match."),
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
    m = re.fullmatch(r"okl(?:ch|ab)\(\s*([\d.]+)\s+(?:0(?:\.0+)?|none)\s+(?:none|[-\d.]+)\s*(?:/\s*([\d.]+))?\s*\)", v)
    if m:
        # an achromatic OKLab colour is linear grey L^3, then sRGB gamma:
        # oklch(0.5 0 0) is #636363, not L x 255 (2026-11 audit, finding 14-22)
        lin = float(m.group(1)) ** 3
        lvl = max(0, min(255, round((12.92 * lin if lin <= 0.0031308 else 1.055 * lin ** (1 / 2.4) - 0.055) * 255)))
        a = float(m.group(2) or 1)
        return "#%02x%02x%02x" % (lvl, lvl, lvl) if a == 1 else "rgba(%d, %d, %d, %g)" % (lvl, lvl, lvl, a)
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
_OWNER = {}


def _leaf(d):
    return isinstance(d, dict) and ("var" in d or "value" in d)


def emit_at(root, path, leaf, name=None):
    """Write `leaf` at a dotted path. A leaf sharing a node with a group
    moves inside it under `default`."""
    node = root
    parts = path.split(".")
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
    full = ".".join(parts)
    if last in node and not _leaf(node[last]):
        for key in ("default", "base", "self"):
            if key not in node[last]:
                node[last][key] = leaf
                full += "." + key
                break
        else:
            raise ValueError(f"{path}: no free key to hold the leaf beside its group")
    else:
        if last in node:
            raise ValueError(f"{path}: duplicate token path")
        node[last] = leaf
    if name:
        EMITTED[name] = full
        _OWNER[full] = name


DECL_SRC = "declared design-system variable in the site's stylesheets (raw/css-vars.json)"


def declared(name):
    v = R.get(name)
    return v if v not in (None, "") else None


def norm_len(v):
    m = re.fullmatch(r"(-?[\d.]+[eE][+-]?\d+)(px|rem)", str(v).strip())
    if not m:
        return v
    return f"{float(m.group(1)):f}".rstrip("0").rstrip(".") + m.group(2)


# A font-relative length resolves against the element's own font size; the
# empty probe that produced raw/css-vars.json read it through a fixed-size
# box instead (.005em came back 0.078125px — at the declared 11px text-2xs
# step it is 0.055px). Keep the declared unit rather than publish a fixed px
# that no longer scales.
FONT_REL = re.compile(r"-?(?:\d+\.?\d*|\.\d+)(em|ex|ch|cap|ic|lh)")


def decl(name, ty="dimension"):
    v = declared(name)
    desc = f"The declared `{name}`."
    raw = (RL.get(name) or {}).get("raw")
    if ty == "dimension" and isinstance(raw, str) and FONT_REL.fullmatch(raw.strip()):
        return lit(raw.strip(), "other", f"{DECL_SRC}: {name}",
                   f"The declared `{name}` — `{raw.strip()}`; font-relative, so it scales with the text it spaces.")
    if ty == "dimension":
        nv = norm_len(v)
        if nv != v:
            desc = f"The declared `{name}` — `{raw}`, which Chromium resolves to {nv}."
            v = nv
        if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(v).strip()):
            ty = "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", desc)


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\)|color\([^)]*\))")


def num_decl(name):
    v = declared(name)
    return lit(v, "number", f"{DECL_SRC}: {name}", f"The declared `{name}`.")


def painted(comp, state, key):
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


# Names whose :root declaration is overridden in a @media (min|max-width)
# block — the resolved value is the 1440px view; the override list travels on
# $extensions.responsive.
MEDIA_OVERRIDES = {}
for rule in V.get("theme", []):
    ctx = " ".join(rule.get("context") or [])
    mq = re.search(r"@media \((min|max)-width: (\d+)px\)", ctx)
    if mq and rule.get("selector") in (":root", ":root, :host"):
        for n in rule.get("properties") or {}:
            tag = f"{mq.group(1)}-width:{mq.group(2)}px"
            MEDIA_OVERRIDES.setdefault(n, [])
            if tag not in MEDIA_OVERRIDES[n]:
                MEDIA_OVERRIDES[n].append(tag)


def resp_kw(name):
    if name in MEDIA_OVERRIDES:
        return {"responsive": "viewport-conditional: also declared under @media (" + ", ".join(MEDIA_OVERRIDES[name]) + "); resolved at 1440 x 900"}
    return {}


# ------------------------------------------------------------------- fonts
#
# fingerprint.com serves Inter (400-700), JetBrains Mono, Petrona and the
# "Geist Pixel" display face; the --font-sans/--font-serif/--font-mono/
# --font-pixel stacks carry hashed family names plus fallback entries.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, name, desc in [
    ("sans", "--font-sans", "Inter — every heading, control and body on the marketing site; hashed family name plus Arial/system fallbacks."),
    ("serif", "--font-serif", "Petrona — the serif display face used on editorial sections; Times New Roman/Georgia fallback."),
    ("mono", "--font-mono", "JetBrains Mono — code, prompts and signal values; Courier New/monospace fallback."),
    ("pixel", "--font-pixel", "Geist Pixel — the pixel display face; ui-monospace fallback."),
]:
    if name in R:
        fam[key] = var(name, "fontFamily", description=desc)

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for name in sorted(k for k in R if re.fullmatch(r"--font-weight-[a-z]+", k)):
    weights[name[len("--font-weight-"):]] = lit(R[name], "fontWeight", f"{DECL_SRC}: {name}", f"The declared `{name}`.")

# ------------------------------------------------------------- type ramp
#
# --text-2xs (11px) through --text-6xl (48px), each with a
# --text-*--line-height and a --text-*--letter-spacing companion. Em-valued
# tracking (-.017em) stays `other`; px tracking stays a dimension.

sizes = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for name in sorted(k for k in R if re.fullmatch(r"--text-(?:2?xs|sm|base|lg|xl|[2-9]xl)$", k)):
    sizes[name[len("--text-"):]] = var(name, "dimension", **resp_kw(name))

lineheights = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for name in sorted(k for k in R if re.fullmatch(r"--text-(?:2?xs|sm|base|lg|xl|[2-9]xl)--line-height", k)):
    lineheights[name[len("--text-"):-len("--line-height")]] = var(name, "dimension")
for name in sorted(k for k in R if re.fullmatch(r"--leading-[a-z]+", k)):
    lineheights[name[len("--leading-"):]] = num_decl(name)

tracking = SPEC["core"].setdefault("font", {}).setdefault("tracking", {})
for name in sorted(k for k in R if re.fullmatch(r"--text-(?:2?xs|sm|base|lg|xl|[2-9]xl)--letter-spacing", k)):
    tracking[name[len("--text-"):-len("--letter-spacing")]] = decl(name)
for name in sorted(k for k in R if re.fullmatch(r"--tracking-[a-z]+", k)):
    tracking[name[len("--tracking-"):]] = decl(name)

# ---------------------------------------------------------- core scales

spacing = SPEC["core"].setdefault("spacing", {})
if declared("--spacing") is not None:
    spacing["base"] = var("--spacing", "dimension",
                          description="The declared `--spacing` base — 4px; every Tailwind space-n utility is a multiple of it.")

radius_alias = {}
radii = SPEC["core"].setdefault("radius", {})
for name in sorted(k for k in R if re.fullmatch(r"--radius(?:-[0-9a-z]+)?$", k)):
    key = name[len("--radius"):] .lstrip("-") or "default"
    radii[key] = decl(name)
    radius_alias[norm_len(R[name])] = key

layout = SPEC["core"].setdefault("layout", {})
containers = layout.setdefault("container", {})
for name in sorted(k for k in R if re.fullmatch(r"--container(-[0-9a-z-]+)?$", k)):
    key = name[len("--container"):] .lstrip("-") or "default"
    containers[key] = decl(name)
if declared("--content-width") is not None:
    layout["contentWidth"] = decl("--content-width")

# Elevation: --fpds-shadow-* is the declared ramp; --shadow-* aliases it.
def shadow_lit(name):
    raw = declared(name)
    if not raw:
        return lit(raw, "other", f"{DECL_SRC}: {name}", f"The declared `{name}` shadow.")
    layers = []
    # resolved form: "rgba(r, g, b, a) Xpx Ypx BLURpx SPREADpx( inset)?(, ...)*"
    for layer in re.split(r"(?<!\d),\s+(?=rgba?\(|#)", str(raw)):
        m = re.fullmatch(
            r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(?:ok)?l(?:ch|ab)\([^)]*\))\s+"
            r"(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(\s+inset)?", layer.strip())
        if not m:
            return lit(raw, "other", f"{DECL_SRC}: {name}", f"The declared `{name}` shadow.")
        col, x, y, blur, spread, inset = m.groups()
        d = {"color": norm_color(col), "offsetX": f"{x}px", "offsetY": f"{y}px",
             "blur": f"{blur}px", "spread": f"{spread}px"}
        if inset:
            d["inset"] = True
        layers.append(d)
    return lit(layers, "shadow", f"{DECL_SRC}: {name}",
               f"The declared `{name}` shadow ({len(layers)} layer{'s' if len(layers) > 1 else ''}).")

elevation = SPEC["core"].setdefault("elevation", {})
for name in sorted(k for k in R if re.fullmatch(r"--fpds-shadow-[a-z0-9-]+", k)):
    key = name[len("--fpds-shadow-"):]
    node = elevation
    # inset-b-black-100 -> inset.b.black.100 style nesting would over-nest;
    # keep a flat, hyphen-preserving key.
    node[key] = shadow_lit(name)
for name in sorted(k for k in R if re.fullmatch(r"--shadow-(?:[0-9]+|button|inset-[a-z0-9-]+)", k)):
    key = "alias." + name[len("--shadow-"):]
    node = elevation
    parts = key.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = shadow_lit(name)

motion = SPEC["core"].setdefault("motion", {})
easing = motion.setdefault("easing", {})
for name in sorted(k for k in R if re.fullmatch(r"--ease-[a-z-]+", k)):
    easing[name[len("--ease-"):]] = var(name, "cubicBezier")
if declared("--default-transition-duration") is not None:
    motion.setdefault("duration", {})["default"] = lit(R["--default-transition-duration"], "duration", f"{DECL_SRC}: --default-transition-duration", "The declared `--default-transition-duration`.")
if declared("--default-transition-timing-function") is not None:
    easing["default"] = var("--default-transition-timing-function", "cubicBezier")

misc = SPEC["core"].setdefault("misc", {})
for name, key, ty in [
    ("--blur-xs", "blur.xs", "dimension"), ("--blur-sm", "blur.sm", "dimension"),
    ("--aspect-video", "aspectVideo", "other"), ("--drop-shadow-xl", "dropShadow.xl", "other"),
]:
    if declared(name) is not None:
        node = misc
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = decl(name) if ty == "dimension" else lit(R[name], ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")

anim = SPEC["core"].setdefault("animation", {})
for name in sorted(k for k in R if re.fullmatch(r"--animate-[a-z-]+", k)):
    anim[name[len("--animate-"):]] = lit(R[name], "other", f"{DECL_SRC}: {name}", f"The declared `{name}` animation shorthand.")

# ------------------------------------------------------------- colours
#
# Two honest layers. fpds.* keeps the declared `H S% L%` channel triplets
# (type other — they are channels, not a colour literal); color.* keeps the
# resolved --color-* hex aliases the utilities actually paint. The semantic
# triplets (--primary/-hover/-active, --border, --surface-raised) sit under
# light.theme as role tokens pointing at the --color-* aliases.

TRIPLET = re.compile(r"(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)%\s+(\d+(?:\.\d+)?)%")

fpds = SPEC["core"].setdefault("fpds", {})
for name in sorted(k for k in R if re.fullmatch(r"--fpds-color-[a-z]+(?:-\d+)?$", k)):
    key = name[len("--fpds-color-"):].replace("-", ".")
    node = fpds
    parts = key.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = lit(R[name], "other", f"{DECL_SRC}: {name}",
                          f"The declared `{name}` — the `H S% L%` channel triplet the `--color-*` alias resolves through.")

cols = SPEC["core"]
for name in sorted(k for k in R if re.fullmatch(r"--color-(?:[a-z]+-\d+|black|white)$", k)):
    key = name[len("--color-"):]
    if key in ("black", "white"):
        emit_at(cols, "color.base." + key, var(name, "color"), name)
    else:
        fam_, step = key.rsplit("-", 1)
        emit_at(cols, "color." + fam_ + "." + step, var(name, "color"), name)

# Syntax colours: declared as hex on :root, redeclared under .dark to the
# lighter ramp steps inside code blocks. The light values are resolved; the
# dark values are computed from the declared .dark aliases
# (hsl(var(--fpds-color-*-N))) — declared, never painted as a page theme.
syn = SPEC["core"].setdefault("color", {}).setdefault("syntax", {})
for name in sorted(k for k in R if re.fullmatch(r"--fpds-color-syntax-[a-z]+$", k)):
    syn[name[len("--fpds-color-syntax-"):]] = var(name, "color")


def triplet_hex(t):
    m = TRIPLET.fullmatch(str(t).strip())
    if not m:
        return None
    h, s_, l_ = float(m.group(1)) / 360, float(m.group(2)) / 100, float(m.group(3)) / 100
    r, g, b = colorsys.hls_to_rgb(h, l_, s_)
    return "#%02x%02x%02x" % (round(r * 255), round(g * 255), round(b * 255))


DARK_SYNTAX = {}
for rule in V.get("theme", []):
    if rule.get("selector") == ".dark":
        for n, v in (rule.get("properties") or {}).items():
            mm = re.fullmatch(r"hsl\(var\((--fpds-color-[a-z]+(?:-\d+)?)\)\)", str(v).strip())
            DARK_SYNTAX[n] = R.get(mm.group(1)) if mm else v

syn_d = SPEC["dark"].setdefault("syntax", {})
for name in sorted(DARK_SYNTAX):
    t = DARK_SYNTAX[name]
    hx = triplet_hex(t)
    base = name[len("--fpds-color-syntax-"):]
    src = (f"declared {name} under the .dark selector (raw/css-vars.json): `hsl(var(--fpds-color-*))` "
           f"re-pointed at the `{t}` triplet = {hx}; the .dark scope is mounted by code blocks only — "
           "no public page paints a dark theme")
    syn_d[base] = lit(hx if hx else str(t), "color" if hx else "other", src,
                      f"The `.dark` redeclaration of `{name}` — code-block syntax colours, not a page theme.")

# ------------------------------------------------- per-scope semantic roles
#
# --primary/-hover/-active, --border and --surface-raised are the semantic
# HSL triplets; their --color-* aliases are what the utilities paint. Emitted
# as role tokens under light.theme.* so measured values can alias them.

sem0 = SPEC["light"]
PREFIX = "theme."
ROLE = {
    "--color-primary": ("action.primary", "The brand orange — primary buttons, links, the slider and focus accents."),
    "--color-primary-hover": ("action.primaryHover", "The primary's hover step."),
    "--color-primary-active": ("action.primaryActive", "The primary's active step."),
    "--color-border": ("border.default", "The gray-3 hairline on cards, fields and dividers."),
    "--color-surface-raised": ("surface.raised", "The raised surface fill (cards, the dropdown panel)."),
    "--color-black": ("ink.default", "The near-black ink — `hsl(var(--fpds-color-black))`."),
    "--color-white": ("ink.inverse", "White — text on the dark CTA and dark sections."),
}
for name in sorted(ROLE):
    if name in R:
        path, desc = ROLE[name]
        emit_at(sem0, PREFIX + path, var(name, "color", description=desc), name)
# The raw triplets ride alongside as provenance.
for name, path, desc in [
    ("--primary", "triplet.primary", "The `--primary` channel triplet the --color-primary alias wraps."),
    ("--primary-hover", "triplet.primaryHover", "The `--primary-hover` triplet."),
    ("--primary-active", "triplet.primaryActive", "The `--primary-active` triplet."),
    ("--border", "triplet.border", "The `--border` triplet behind --color-border."),
    ("--surface-raised", "triplet.surfaceRaised", "The `--surface-raised` triplet behind --color-surface-raised."),
]:
    if name in R:
        emit_at(sem0, PREFIX + path, lit(R[name], "other", f"{DECL_SRC}: {name}", desc))

# ----------------------------------------------------- measured roles

role_alias = {}
for name, p in EMITTED.items():
    v = R.get(name)
    if v:
        role_alias.setdefault(norm_color(v) if isinstance(v, str) else v, p)
# Prefer the semantic roles when several tokens share a colour.
for name in ("--color-black", "--color-white", "--color-primary", "--color-border",
             "--color-surface-raised", "--color-gray-700", "--color-gray-600"):
    v = R.get(name)
    if v and EMITTED.get(name):
        role_alias[norm_color(v)] = EMITTED[name]


def semcolor(raw, src, desc):
    alias = role_alias.get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


sem = SPEC["light"]
for key, comp, state, prop, group, desc in [
    ("ink", "hero-h1", "default", "color", "text",
     "The near-black ink on display copy, headings and body."),
    ("navInk", "nav-pricing", "default", "color", "text",
     "The header link ink."),
    ("ctaFill", "nav-cta", "default", "backgroundColor", "action",
     "The orange fill of the 'Get Started' header pill — the brand primary."),
    ("ctaInk", "nav-cta", "default", "color", "action",
     "The text on the orange 'Get Started' pill."),
    ("ctaHover", "nav-cta", "hover", "backgroundColor", "action",
     "The CTA pill's hover fill."),
    ("focusRing", "nav-cta", "focus-visible", "outlineColor", "border",
     "The keyboard focus ring colour on the header CTA."),
    ("fieldBg", "contact-email", "default", "backgroundColor", "form",
     "The contact-sales field fill."),
    ("fieldInk", "contact-email", "default", "color", "form",
     "The field text ink."),
    ("placeholder", "contact-email", "default", "placeholder", "form",
     "The placeholder ink on the sales form."),
    ("submitFill", "contact-submit", "default", "backgroundColor", "action",
     "The 'Submit' button fill on the sales form."),
    ("submitInk", "contact-submit", "default", "color", "action",
     "The 'Submit' button text."),
    ("planCardBg", "plan-card", "default", "backgroundColor", "surface",
     "The plan card's fill on /pricing."),
    ("pillBg", "hero-pill", "default", "backgroundColor", "surface",
     "The 'New' announcement pill fill."),
]:
    try:
        if prop == "color":
            raw = ts(comp, state, "color")
            src = f"computed color of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
        elif prop == "placeholder":
            raw = (C[comp]["states"][state].get("placeholder") or {}).get("color")
            src = f"computed ::placeholder color of {comp} {state} (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if raw in (None, "") or (prop == "backgroundColor" and TRANSPARENT.fullmatch(str(raw).strip())):
            raise KeyError(prop)
        sem.setdefault(group, {})[key] = semcolor(raw, src, desc)
    except KeyError:
        pass

# The white page field behind every marketing page.
if declared("--color-white") is not None:
    sem.setdefault("background", {})["page"] = lit(
        "{color.base.white}", "color",
        "the :root --color-white resolved on the marketing pages (raw/css-vars.json); visible as the page field behind every page (screenshots/*-light-*.png)",
        "The white page field — --color-white.")

# ----------------------------------------------------- measured type size

size_alias = {}
for name in sorted(k for k in R if re.fullmatch(r"--text-(?:2?xs|sm|base|lg|xl|[2-9]xl)$", k)):
    size_alias.setdefault(str(R[name]), f"font.size.{name[len('--text-'):]}")
for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The hero display heading — aliases a --text-* step where it matches."),
    ("section", "section-h2", "default", "A section heading size."),
    ("body", "footer-link", "default", "A footer link's body size."),
]:
    try:
        raw = st(comp, state)["fontSize"]
        src = f"computed fontSize of {comp} {state} (raw/components-computed.json)"
        alias = size_alias.get(raw)
        SPEC["core"].setdefault("font", {}).setdefault("size", {}).setdefault("measured", {})[key] = lit(
            f"{{{alias}}}" if alias else raw, "dimension",
            src + (f"; matches declared {alias}" if alias else ""), desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ shape

for key, comp, state, prop, desc in [
    ("cta", "nav-cta", "default", "borderTopLeftRadius", "The header CTA pill radius."),
    ("navLink", "nav-pricing", "default", "borderTopLeftRadius", "The header link radius."),
    ("card", "plan-card", "default", "borderTopLeftRadius", "The plan-card corner radius."),
    ("field", "contact-email", "default", "borderTopLeftRadius", "The contact field radius."),
    ("dropdown", "nav-panel", "default", "borderTopLeftRadius", "The product-dropdown panel corner radius."),
]:
    try:
        v = norm_len(st(comp, state)[prop])
        src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        dkey = radius_alias.get(v)
        if dkey:
            radii[key] = lit(f"{{radius.{dkey}}}", "dimension", src + f"; matches declared --radius{'-' + dkey if dkey != 'default' else ''}", desc)
        else:
            radii[key] = lit(v, "dimension" if re.fullmatch(r"-?[0-9.]+(px|rem)", v or "") else "other", src, desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
try:
    s = st("nav-cta", "default")
    dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        props = [p.strip() for p in s.get("transitionProperty", "all").split(",") if p.strip()]
        durs = [d.strip() for d in dur.split(",")]
        tfs = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", ease or "")
        parts = []
        for i, p in enumerate(props):
            d = durs[i % len(durs)]
            if d == "0s":
                continue
            parts.append(f"{p} {d} {tfs[i % len(tfs)] if tfs else ''}".strip())
        if parts:
            mo["control"] = lit(", ".join(parts), "other",
                "computed transition of nav-cta default (raw/components-computed.json); the --ease-*/--default-transition-* steps are the declared easings",
                "The control transition on the header CTA.")
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("topbar-height", "mkt-header", "default", "h", "dimension", "The marketing header bar height."),
    ("cta-height", "nav-cta", "default", "h", "dimension", "The header CTA pill height."),
    ("dropdown-width", "nav-panel", "default", "w", "dimension", "The open product-dropdown panel width."),
    ("hero-headline-width", "hero-h1", "default", "w", "dimension", "The hero display heading's measure."),
    ("field-height", "contact-email", "default", "h", "dimension", "The contact field height."),
    ("submit-width", "contact-submit", "default", "w", "dimension", "The 'Submit' button width."),
    ("plan-card-width", "plan-card", "default", "w", "dimension", "The plan-card column width."),
    ("slider-width", "price-slider", "default", "w", "dimension", "The pricing volume slider width."),
    ("newsletter-width", "newsletter-field", "default", "w", "dimension", "The footer newsletter field width."),
    ("mobile-topbar-height", "m-topbar", "default", "h", "dimension", "The phone header bar height."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# docs.fingerprint.com (Mintlify) and dashboard.fingerprint.com (the product
# auth shell) are different stacks that do not share the marketing token
# layer; their measured values are kept as literals, honestly labelled.
docs = comp.setdefault("docs", {})
for name, cname, state, prop, ty_, desc in [
    ("sidebar-link-ink", "docs-side-link", "default", "color", "color", "A docs sidebar link's ink."),
    ("search-btn-bg", "docs-search", "default", "backgroundColor", "color", "The docs 'Open search' button fill."),
    ("code-bg", "docs-code", "default", "backgroundColor", "color", "A docs code block's fill."),
]:
    try:
        docs[name] = lit(norm_color(opaque(st(cname, state)[prop])), "color",
            f"computed {prop} of {cname} {state} on docs.fingerprint.com (raw/components-computed.json)", desc)
    except KeyError:
        pass

shell = comp.setdefault("productShell", {})
for name, cname, state, prop, ty_, desc in [
    ("login-panel-width", "login-panel", "default", "w", "dimension", "The sign-in card width on dashboard.fingerprint.com/login."),
    ("google-btn-fill", "login-google", "default", "backgroundColor", "color", "The 'Continue with Google' button fill."),
    ("google-btn-ink", "login-google", "default", "color", "color", "The 'Continue with Google' button text."),
    ("email-btn-fill", "login-email-btn", "default", "backgroundColor", "color", "The 'Continue with email' control fill on /login."),
]:
    try:
        if prop in ("w", "h"):
            v = rc(cname, state, prop)
            shell[name] = lit(("%g" % v) + "px", ty_, f"measured {prop} of {cname} {state} on the product shell (raw/components-computed.json)", desc)
        else:
            shell[name] = lit(norm_color(opaque(st(cname, state)[prop])), "color",
                f"computed {prop} of {cname} {state} on the product shell (raw/components-computed.json)", desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
