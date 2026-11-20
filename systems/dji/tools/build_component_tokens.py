#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

dji.com paints one product signed out: the geo-locale /sg brand site —
mega-nav marketing surfaces, category grids and product pages — over a
declared token layer in the v3 bundles: --grey-0..12, --black-1..8,
--white-1..8, --bg-0..7, --brand-1..10, --green-*/--orange-*/--red-* scales,
--brand-primary-*/--brand-text-* roles, the section-scoped semantics
(:root .light-theme and :root .dark-theme re-declare --primary/--secondary/
--tertiary/--bg/--light-bg/--border/--divider/--disabled/--reverse-* and
the status roles), --spacing-xs..xl, --radius, --grid-width/--grid-gap/
--col-width/--column-count, --zindex-* ladder and --font-*/--line-height-*.
Sections opt into light or dark paint through the product's own
.light-theme/.dark-theme classes — the dark hero and footer slabs are
themed, not baked. Theme-invariant names land under core.*; names that
differ between the two section themes emit under both light.*
(.light-theme) and dark.* (.dark-theme) as {"var": ...} leaves.

The public surfaces paint both: nav, listings, support and footer sections
carry .light-theme while the hero, product dark sections and the legacy
dui-navbar over the hero carry .dark-theme — all measured paint:

  light     #ffffff page, black@85% ink (--black-primary), #0070d5 Store
            CTA (--brand-6/--brand-default), #2490e3 hover, #0058b0
            pressed, #272727 footer slab, black@6%/15% dividers
            (--black-divider/--black-border), 1408px pill radius on the
            Store button, 0.3s background-color transitions
  dark      white@85% ink (--white-primary), #fff pill CTA over dark
            (product page Buy), white@9%/15% ghost hover/pressed fills,
            60px ghost radius, #272727 footer slab
  fonts     "Open Sans" stack (measured UI face), PingFang SC /
            Microsoft YaHei fallbacks, Dji icon face (declared)
  ramp      measured 12/14/16/20/24/32/40/48px steps
  shape     16px declared --radius; 60px/64px/1408px pill radii measured
  motion    0.3s control transitions (background-color, all)
"""


import json, math, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("lightTheme", {})
RD = V.get("resolved", {}).get("darkTheme", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}
D = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RD.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. dji.com "
    "declares its token layer in the served v3 bundles "
    "(raw/css-vars.json): theme-invariant scales under core.* and the "
    "section-scoped semantics — :root .light-theme / :root .dark-theme "
    "re-declare --primary/--secondary/--tertiary/--bg/--light-bg/"
    "--border/--divider/--disabled/--reverse-*/--brand-primary-*/"
    "--brand-text-*/status roles — emitted under both light.* "
    "(.light-theme sections) and dark.* (.dark-theme sections) so each "
    "theme resolves its own value. Both are real paint: light sections "
    "(nav, listings, support) and dark sections (hero, product, footer) "
    "are measured on the live signed-out pages. Measured roles alias to "
    "the declared values where they match."),
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


def _gam(v):
    v = max(0.0, min(1.0, v))
    return 12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055


def _lin(v):
    v = max(0.0, min(1.0, v))
    return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4


def _oklab_to_hex(l, a, b):
    l_ = l + 0.3963377774 * a + 0.2158037573 * b
    m_ = l - 0.1055613458 * a - 0.0638541728 * b
    s_ = l - 0.0894841775 * a - 1.2914855480 * b
    l3, m3, s3 = l_ ** 3, m_ ** 3, s_ ** 3
    r = +4.0767416621 * l3 - 3.3077115913 * m3 + 0.2309699292 * s3
    g = -1.2684380046 * l3 + 2.6097574011 * m3 - 0.3413193965 * s3
    bl = -0.0041960863 * l3 - 0.7034186147 * m3 + 1.7076147010 * s3
    return [_gam(r), _gam(g), _gam(bl)]


def _lab_to_hex(l, a, b):
    # CIELAB D50 -> sRGB (same matrix vars.mjs applies in the probe).
    fy = (l + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    eps, kap = 216 / 24389, 24389 / 27
    f = lambda t: t ** 3 if t ** 3 > eps else (116 * t - 16) / kap
    X, Y, Z = 0.96422 * f(fx), f(fy), 0.82521 * f(fz)
    r = 3.1338561 * X - 1.6168667 * Y - 0.4906146 * Z
    g = -0.9787684 * X + 1.9161415 * Y + 0.033454 * Z
    bl = 0.0719453 * X - 0.2289914 * Y + 1.4052427 * Z
    return [_gam(r), _gam(g), _gam(bl)]


def _p3_to_srgb(r, g, b):
    r, g, b = _lin(r), _lin(g), _lin(b)
    lr = 1.2249401 * r - 0.2249404 * g
    lg = -0.0420569 * r + 1.0420571 * g
    lb = -0.0196376 * r - 0.0786361 * g + 1.0982735 * b
    return [_gam(lr), _gam(lg), _gam(lb)]


def _rgba_out(rgb, a):
    r, g, b = (round(x * 255) for x in rgb)
    if a is None or a >= 1:
        return "#%02x%02x%02x" % (r, g, b)
    return f"rgba({r}, {g}, {b}, {'%g' % a})"


def norm_color(v):
    v = str(v or "").strip()
    # DJI's hue ramps are declared as bare comma-separated RGB channels
    # ("49,209,88"), consumed by rgb(var(--green-6)) — normalize to the
    # colour they mean so the ramps emit as colors, not "other" strings.
    m = re.fullmatch(r"(\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})", v)
    if m:
        r, g, b = (int(c) for c in m.groups())
        if max(r, g, b) <= 255:
            return "#%02x%02x%02x" % (r, g, b)
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
    m = re.fullmatch(r"oklab\(([\d.]+)\s+(-?[\d.e]+)\s+(-?[\d.e]+)(?:\s*/\s*([\d.]+%?))?\)", v)
    if m:
        l, a_, b_, al = m.groups()
        rgb = _oklab_to_hex(float(l), float(a_), float(b_))
        alpha = None if al is None else (float(al[:-1]) / 100 if al.endswith('%') else float(al))
        return _rgba_out(rgb, alpha)
    m = re.fullmatch(r"oklch\(([\d.]+)\s+([\d.e]+)\s+([\d.e]+)(?:\s*/\s*([\d.]+%?))?\)", v)
    if m:
        l, c, h, al = m.groups()
        a_ = float(c) * math.cos(math.radians(float(h)))
        b_ = float(c) * math.sin(math.radians(float(h)))
        rgb = _oklab_to_hex(float(l), a_, b_)
        alpha = None if al is None else (float(al[:-1]) / 100 if al.endswith('%') else float(al))
        return _rgba_out(rgb, alpha)
    m = re.fullmatch(r"lab\(([\d.]+)\s+(-?[\d.e]+)\s+(-?[\d.e]+)(?:\s*/\s*([\d.]+%?))?\)", v)
    if m:
        l, a_, b_, al = m.groups()
        rgb = _lab_to_hex(float(l), float(a_), float(b_))
        alpha = None if al is None else (float(al[:-1]) / 100 if al.endswith('%') else float(al))
        return _rgba_out(rgb, alpha)
    m = re.fullmatch(r"color\(srgb\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)(?:\s*/\s*([\d.]+%?))?\)", v)
    if m:
        r, g, b, al = m.groups()
        alpha = None if al is None else (float(al[:-1]) / 100 if al.endswith('%') else float(al))
        return _rgba_out([float(r), float(g), float(b)], alpha)
    m = re.fullmatch(r"color\(display-p3\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)(?:\s*/\s*([\d.]+%?))?\)", v)
    if m:
        r, g, b, al = m.groups()
        alpha = None if al is None else (float(al[:-1]) / 100 if al.endswith('%') else float(al))
        return _rgba_out(_p3_to_srgb(float(r), float(g), float(b)), alpha)
    # Tailwind-v4 HSL triplet without the hsl() wrapper: "64 8% 16%" or
    # "64 8% 16% / 0.5" — a --* colour var storing bare channels.
    m = re.fullmatch(r"([\d.]+)\s+([\d.]+)%\s+([\d.]+)%(?:\s*/\s*([\d.]+%?))?", v)
    if m:
        h, ss, ll, al = float(m.group(1)) % 360, float(m.group(2)) / 100, float(m.group(3)) / 100, m.group(4)
        c = (1 - abs(2 * ll - 1)) * ss
        x = c * (1 - abs((h / 60) % 2 - 1))
        mm = ll - c / 2
        seg = int(h // 60) % 6
        rgb = [(c, x, 0), (x, c, 0), (0, c, x), (0, x, c), (x, 0, c), (c, 0, x)][seg]
        alpha = None if al is None else (float(al[:-1]) / 100 if al.endswith('%') else float(al))
        return _rgba_out([ch + mm for ch in rgb], alpha)
    return v


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False


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
            # A leaf demoted earlier (its var became a group parent) can sit
            # where a real name belongs — e.g. --chat-background demoted to
            # chat.background.default, then --chat-background-default
            # arrives. Move the squatter to a free key and give the real
            # name its declared path.
            squatter = node[last]
            owner = _OWNER.pop(path, None)
            for key in ("base", "self", "value", "default"):
                if key not in node:
                    node[key] = squatter
                    if owner:
                        EMITTED[owner] = path.rsplit(".", 1)[0] + "." + key if "." in path else key
                        _OWNER[path.rsplit(".", 1)[0] + "." + key if "." in path else key] = owner
                    break
            else:
                raise ValueError(f"{name}: duplicate token path {path}")
            del node[last]
        node[last] = leaf
    EMITTED[name] = path
    _OWNER[path] = name


def emitted_path(name):
    return EMITTED[name]


def painted(comp, state, want=None):
    """First painted fill on or under the component (optionally one matching `want`)."""
    try:
        c = C[comp]["states"][state]
    except KeyError:
        return None
    for n in c.get("paint") or []:
        if n.get("bg") and (want is None or want(n["bg"])):
            return n["bg"]
    for n in c.get("ancestors") or []:
        if n.get("bg") and (want is None or want(n["bg"])):
            return n["bg"]
    return None


DECL_SRC = "declared design-system variable in the site stylesheet (raw/css-vars.json)"


def decl(name, ty="dimension"):
    v = R[name]
    if ty == "dimension" and not re.fullmatch(r"-?(\d+(\.\d+)?|\.\d+)(px|rem)", str(v).strip()):
        ty = "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


COLOR_V = re.compile(r"(\d{1,3},\s*\d{1,3},\s*\d{1,3}|#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\)|color\([^)]*\)|\d+(?:\.\d+)?\s+[\d.]+%\s+[\d.]+%(?:\s*/\s*[\d.]+%?)?)")


def decl_color(name):
    v = R[name]
    ty = "color" if COLOR_V.fullmatch(str(v).strip()) else "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


# ------------------------------------------------------------------- fonts
#
# "Open Sans" is the measured UI face (computed fontFamily of nav items and
# every reading); PingFang SC / Microsoft YaHei are its declared CJK
# fallbacks; Dji is the declared icon face (300/400/500 weights in the
# served sheets — icon glyphs, not text). Declared weights land in the
# generic --font-* loop below.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("ui", "nv-item", "default", 'The "Open Sans" stack — every UI string: nav, cards, CTAs, spec lines (PingFang SC / Microsoft YaHei fallbacks for CJK).'),
    ("icon", None, None, "Dji — the declared icon face (300/400/500 weights in the served sheets; icon glyphs, not text)."),
]:
    if comp and have(comp, state, "fontFamily"):
        fam[key] = {"value": st(comp, state)["fontFamily"], "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
    elif comp is None:
        fam[key] = {"value": "Dji", "type": "fontFamily",
                    "source": "declared @font-face in the served stylesheets (raw/css-vars.json)",
                    "description": desc}

# --------------------------------------------------- declared scales (core)
#
# Theme-invariant names land here; every theme-switching name is emitted
# per-theme below. Scale families (Tailwind 11-step hue palettes) are emitted
# per-theme even when a step happens to resolve identically, so each theme's
# scale stays complete.

SCALE_FAMS = {"brand", "grey", "black", "white", "bg",
              "green", "orange", "red", "background"}

def scale_rename(name):
    """Map a scale member to the color.<fam>.<step> path it emits under."""
    m = re.fullmatch(r"--([a-z][a-z-]*?)-(\d+(?:-oklch)?)", name)
    if m and m.group(1) in SCALE_FAMS:
        return f"--color-{m.group(1)}-{m.group(2)}"
    m = re.fullmatch(r"--gray(\d+)", name)
    if m:
        return f"--color-gray-{m.group(1)}"
    return name


def is_scale_member(name):
    return scale_rename(name) != name


color_alias = {}   # normalized colour -> 'color.<path>' for aliasing
colors = SPEC["core"].setdefault("color", {})
for name in sorted(k for k in R if k.startswith("--color-")):
    if R[name] != D.get(name):
        continue
    rest = name[len("--color-"):]
    # An invariant --color-<fam>-<step> whose bare twin --<fam>-<step> exists
    # and resolves identically is a silk alias: the themed scale pass emits
    # the twin under this very name, so emitting it here would collide.
    if ("--" + rest) in R and scale_rename("--" + rest) == name \
            and norm_color(R.get("--" + rest)) == norm_color(R.get(name)) \
            and norm_color(D.get("--" + rest)) == norm_color(D.get(name)):
        continue
    m = re.fullmatch(r"(.+?)-(\d+)", rest)
    if m:
        bag = colors.setdefault(m.group(1), {})
        bag[m.group(2)] = decl_color(name)
        if bag[m.group(2)]["type"] == "color":
            color_alias.setdefault(norm_color(R[name]), f"color.{m.group(1)}.{m.group(2)}")
    else:
        colors[rest] = decl_color(name)
        if colors[rest]["type"] == "color":
            color_alias.setdefault(norm_color(R[name]), f"color.{rest}")

# 'NNpx'/'Nrem' -> ('font.size.<key>', '--var'): the declared --font-size-*
# scale aliases the measured type steps.
size_alias = {}
for name in sorted(k for k in R if k.startswith("--font-size-")):
    if R[name] == D.get(name):
        size_alias.setdefault(str(R[name]), (f"font.size.{name[len('--font-size-'):]}", name))

for name in sorted(k for k in R if k.startswith("--container-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("size", {}).setdefault("container", {})[name[len("--container-"):]] = decl(name)
for name in sorted(k for k in R if k.startswith("--breakpoint-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("breakpoint", {})[name[len("--breakpoint-"):]] = decl(name)
for name in sorted(k for k in R if k.startswith("--radius-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("radius", {})[name[len("--radius-"):]] = decl(name)
for name in sorted(k for k in R if k.startswith("--duration-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("duration", {})[name[len("--duration-"):]] = decl(name, "other")
for name in sorted(k for k in R if k.startswith("--ease-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("easing", {})[name[len("--ease-"):]] = decl(name, "cubicBezier")
for name in sorted(k for k in R if k.startswith("--animate-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("motion", {})[name[len("--animate-"):]] = decl(name, "other")
for name in sorted(k for k in R if k.startswith("--blur-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("blur", {})[name[len("--blur-"):]] = decl(name, "other")
for name in sorted(k for k in R if k.startswith("--z-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("zIndex", {})[name[len("--z-"):]] = decl(name, "other")
for name in sorted(k for k in R if k.startswith("--default-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("default", {})[name[len("--default-"):]] = decl(name, "other")
for name in sorted(k for k in R if k.startswith("--drop-shadow-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("shadow", {}).setdefault("drop", {})[name[len("--drop-shadow-"):]] = decl(name, "other")
for name in sorted(k for k in R if k.startswith("--shadow-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("shadow", {})[name[len("--shadow-"):]] = decl(name, "other")
for name in sorted(k for k in R if k.startswith("--space-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("space", {})[name[len("--space-"):]] = decl(name)
for name in sorted(k for k in R if k.startswith("--spacing-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("space", {})[name[len("--spacing-"):]] = decl(name)
for name in sorted(k for k in R if k.startswith("--zindex-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("zIndex", {})[name[len("--zindex-"):]] = decl(name, "other")
for name in sorted(k for k in R if k.startswith("--grid-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("size", {}).setdefault("grid", {})[name[len("--grid-"):]] = decl(name)
for name in sorted(k for k in R if k in ("--col-width", "--column-count")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("size", {}).setdefault("grid", {})[name[2:].replace("-", ".")] = decl(name)
for name in sorted(k for k in R if k.startswith("--size-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("size", {})[name[len("--size-"):]] = decl(name)
for name in sorted(k for k in R if k.startswith("--font-weight-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("font", {}).setdefault("weight", {})[name[len("--font-weight-"):]] = decl(name, "fontWeight")
for name in sorted(k for k in R if k.startswith("--font-display-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("font", {}).setdefault("display", {})[name[len("--font-display-"):]] = decl(name, "fontFamily")
for name in sorted(k for k in R if re.fullmatch(r"--font-(headline|primary|code)", k)):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("font", {})[name[len("--font-"):]] = decl(name, "fontFamily")
for name in sorted(k for k in R if re.fullmatch(r"--font-family(-jp)?", k)):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("font", {}).setdefault("familyDeclared", {})[name[len("--font-family"):].lstrip("-") or "default"] = decl(name, "fontFamily")
for name in sorted(k for k in R if k.startswith("--font-size-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("font", {}).setdefault("size", {})[name[len("--font-size-"):]] = decl(name, "fontSize")
for name in sorted(k for k in R if k.startswith("--line-height-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})[name[len("--line-height-"):]] = decl(name, "dimension")
for name in sorted(k for k in R if re.fullmatch(r"--font-(regular|medium|semibold|bold)", k)):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("font", {}).setdefault("weight", {})[name[len("--font-"):]] = decl(name, "fontWeight")
for name in sorted(k for k in R if k.startswith("--typography-scale-")):
    if R[name] == D.get(name):
        rest = name[len("--typography-scale-"):]
        fam, _, prop = rest.partition("-font-")
        prop = prop or fam.split("-")[-1]
        fam = fam if prop != fam else rest.rsplit("-", 1)[0]
        prop = {"size": "fontSize", "weight": "fontWeight", "height": "lineHeight", "spacing": "letterSpacing"}.get(prop.replace("line-", "height").replace("letter-", "spacing"), "other") if "-" not in rest else {"size": "fontSize", "weight": "fontWeight", "height": "lineHeight", "spacing": "letterSpacing"}.get(prop, "other")
        SPEC["core"].setdefault("typography", {}).setdefault(fam, {})[prop] = decl(name, {"fontSize": "fontSize", "fontWeight": "fontWeight", "lineHeight": "dimension", "letterSpacing": "other"}.get(prop, "other"))
if R.get("--page-max-width") == D.get("--page-max-width") and "--page-max-width" in R:
    SPEC["core"].setdefault("size", {})["page-max-width"] = decl("--page-max-width")
for name in sorted(k for k in R if k.startswith("--safe-area-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("size", {}).setdefault("safeArea", {})[name[len("--safe-area-"):]] = decl(name)

CORE_HANDLED = re.compile(
    r"^--(color-|leading-|tracking-|container-|breakpoint-|radius-|"
    r"duration-|ease-|animate-|blur-|z-|default-|drop-shadow-|shadow-|"
    r"font-weight-|space-|size-|elevation-|custom-status-emoji-height|"
    r"custom-emoji|font-size-|font-display-|font-code-|font-headline-|"
    r"font-primary-|font-width-|font-|line-height-|typography-scale-|page-max-width|safe-area-|swiper-|weight-|display-lg|spacing-|zindex-|grid-|col-width|column-count|full-screen-height|"
    r"display-md|display-sm|heading-xxl|heading-xl|heading-lg|"
    r"heading-md|heading-sm|heading-deprecated|eyebrow|redesign-"
    r"heading)")

# Every remaining invariant name that wasn't bucketed or a scale member is
# emitted at its natural dashed path under core.* (the --spacing unit,
# --radius base, --media-overlay-*, --typeset-*, --site-*, --thumb-*,
# --scroll-fade-*, --rank-one, --drop-cap-*, --item-*, --topic-* …).
for name in sorted(R):
    if R[name] != D.get(name) or is_scale_member(name) or CORE_HANDLED.match(name):
        continue
    if name.startswith("--font-weight-"):
        continue
    ty = "color" if COLOR_V.fullmatch(str(R[name]).strip()) else "other"
    emit(SPEC["core"], name, lit(R[name], ty, f"{DECL_SRC}: {name}", f"The declared `{name}`."))

# ------------------------------------------- per-theme semantic variables
#
# Every theme-switching name is emitted under both sets at its natural
# dashed path, except palette-scale members which go under color.<fam>.<n>.
# --color-* silk aliases deduplicate against their shorter twins
# (--color-fg-high == --fg-high) when both themes resolve identically.

TWINS = {}
for n in R:
    if not n.startswith("--color-"):
        continue
    tn = "--" + n[len("--color-"):]
    if tn in R:
        same = (norm_color(R.get(tn)) == norm_color(R.get(n)) and
                norm_color(D.get(tn)) == norm_color(D.get(n)))
        if same:
            TWINS[n] = tn

for root, rd in ((SPEC["light"], R), (SPEC["dark"], D)):
    for name in sorted(set(R) | set(D)):
        if name in TWINS:
            continue
        # A name resolves per theme only when the browser paints it there:
        # names absent from this theme's declaration are not emitted into it.
        if name not in rd:
            continue
        if is_scale_member(name) or R.get(name) != D.get(name):
            ty = "color" if COLOR_V.fullmatch(str(rd[name]).strip()) else "other"
            emit(root, scale_rename(name), var(name, ty))

# ------------------------------------------------------- measured roles
#
# Both section themes paint signed out: nav, category listings, support and
# the where-to-buy pages carry .light-theme (black@85% ink on white), while
# the hero, the product page's dark sections, the footer and the legacy
# dui-navbar chrome over the hero carry .dark-theme (white ink and CTAs).
# The roles below are measured paint from both, aliased to the declared
# .light-theme/.dark-theme variables where the values match.

role_alias = {"light": dict(color_alias), "dark": dict(color_alias)}
for root, theme in ((SPEC["light"], "light"), (SPEC["dark"], "dark")):
    for name in sorted(R):
        if name in TWINS or not (is_scale_member(name) or R[name] != D.get(name)):
            continue
        p = EMITTED.get(scale_rename(name)) or EMITTED.get(name)
        resolved = (R if theme == "light" else D).get(name, R.get(name))
        role_alias[theme].setdefault(norm_color(resolved), p)
    for name in sorted(R):
        if R[name] == D.get(name) and not is_scale_member(name):
            p = EMITTED.get(name)
            if p:
                role_alias[theme].setdefault(norm_color(R[name]), p)


def semcolor(raw, src, desc, theme="light", prefer=(), dest=None):
    """Alias to a preferred declared name when it resolves to this colour.
    A candidate equal to `dest` would alias the leaf to itself — emit the
    colour instead."""
    for p in prefer:
        if p in R and norm_color(R[p] if theme == "light" else D.get(p, "")) == norm_color(raw):
            path = EMITTED.get(scale_rename(p)) or EMITTED.get(p)
            if path and path != dest:
                return lit(f"{{{path}}}", "color", src + f"; matches declared {p}", desc)
    alias = role_alias[theme].get(norm_color(raw))
    if alias == dest:
        alias = None
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


def _demote_leaf_group(root, group):
    node = root.get(group)
    if _leaf(node):
        old = dict(node)
        node.clear()
        node["default"] = old
        owner = _OWNER.pop(group, None)
        if owner:
            EMITTED[owner] = group + ".default"
            _OWNER[group + ".default"] = owner


def put_sem(root, group, key, leaf):
    """Nest a measured role under group; if a declared leaf already holds the
    group path, move it under `default` rather than merging keys into it."""
    node = root.setdefault(group, {})
    _demote_leaf_group(root, group)
    node = root[group]
    node[key] = leaf


# A measured group that collides with a declared leaf demotes it before roles
# read EMITTED, so aliases resolve to the leaf's new path. Run the demotion
# on BOTH theme sets: the declared paths must stay identical light vs dark.
for group in ("background", "text", "action", "border", "surface", "foreground"):
    for root in (SPEC["light"], SPEC["dark"]):
        _demote_leaf_group(root, group)

# ---- light roles (measured on /sg, /camera-drones, /handheld, /support,
# /company, /where-to-buy — the .light-theme sections)
sem = SPEC["light"]
for key, comp, state, prop, group, prefer, desc in [
    ("page", "ct-h1", "default", "_page", "background", ("--white", "--common-white"),
     "The white field the .light-theme sections paint (matches --white)."),
    ("ink", "ct-h1", "default", "color", "text", ("--black-primary", "--primary"),
     "The black@85% ink on headings and body text (matches --black-primary)."),
    ("muted", "co-lede", "default", "color", "text", ("--black-secondary", "--secondary"),
     "The black@65% muted ink on secondary text (matches --black-secondary)."),
    ("nav-ink", "nv-login", "default", "color", "text", (),
     "The #303233 account-link ink in the header."),
    ("primary", "nv-store", "default", "backgroundColor", "action", ("--brand-6", "--brand-default", "--brand-primary-default"),
     "The #0070d5 Store CTA — DJI blue (matches --brand-6/--brand-default)."),
    ("primary-hover", "nv-store", "hover", "backgroundColor", "action", ("--brand-5", "--brand-hover", "--brand-primary-hover"),
     "The #2490e3 hover of the Store CTA (mid-flight toward --brand-5 #2c8cdd at read time)."),
    ("primary-pressed", "nv-store", "pressed", "backgroundColor", "action", ("--brand-7", "--brand-active", "--brand-primary-active"),
     "The #0058b0 pressed Store CTA (matches --brand-7 #005ab1 within rounding)."),
    ("on-primary", "nv-store", "default", "color", "action", ("--white", "--white-primary"),
     "The white label on the Store CTA (matches --white)."),
    ("footer", "ft-bar", "default", "backgroundColor", "surface", ("--grey-9",),
     "The #272727 footer slab (between --grey-9 and --grey-10)."),
    ("hairline", "co-lede", "default", "_hairline", "border", ("--black-divider", "--divider"),
     "The black@6% hairline of .light-theme dividers (declared --divider)."),
]:
    try:
        if prop == "_page":
            # No measured element reports the page field; read the declared white
            # the pages paint, not a screenshot pixel.
            raw = R["--white"]
            src = ("declared --white (raw/css-vars.json resolved.light); no computed reading of the page field "
                   "(seen in screenshots/drones-default.png)")
        elif prop == "_hairline":
            # .light-theme sets --divider: var(--black-divider) (raw/css-vars.json app bin);
            # the :root --divider resolves to the dark theme's white@12%.
            raw = R["--black-divider"]
            src = "declared --black-divider, which .light-theme sections assign to --divider (raw/css-vars.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        put_sem(sem, group, key, semcolor(raw, src, desc, prefer=prefer, dest=group + "." + key))
    except KeyError:
        pass

# ---- dark roles (measured on the .dark-theme sections — the hero, the
# product page's dark panels, the footer and the dui-navbar over the hero)
sem2 = SPEC["dark"]
for key, comp, state, prop, group, prefer, desc in [
    ("ink", "pd-h", "default", "color", "text", ("--white-primary", "--primary"),
     "The white ink on dark sections (matches --white-primary)."),
    ("muted", "ft-link", "default", "color", "text", ("--white-8", "--white-secondary", "--secondary"),
     "The white@85% footer-link ink on dark (matches --white-8)."),
    ("nav-ink", "nv-item", "default", "color", "text", ("--white", "--white-primary"),
     "The white nav-item ink over the hero (legacy dui-navbar)."),
    ("cta", "pd-buy", "default", "backgroundColor", "action", ("--white",),
     "The white pill CTA on the product page's dark hero (matches --white)."),
    ("cta-hover", "pd-buy", "hover", "backgroundColor", "action", (),
     "The white@90% hover of the dark-section pill CTA."),
    ("cta-pressed", "pd-buy", "pressed", "backgroundColor", "action", (),
     "The white@80% pressed state of the dark-section pill CTA."),
    ("on-cta", "pd-buy", "default", "color", "action", ("--black-primary", "--primary"),
     "The black@85% label on the white pill (matches --black-primary)."),
    ("ghost-border", "pd-watch", "default", "borderTopColor", "border", ("--white",),
     "The white 1px ghost-button outline on dark (matches --white)."),
    ("ghost-hover", "pd-watch", "hover", "backgroundColor", "action", ("--white-2", "--light-bg"),
     "The white@9% ghost-button hover fill on dark (near --white-2 @8%)."),
    ("ghost-pressed", "pd-watch", "pressed", "backgroundColor", "action", ("--white-3",),
     "The white@15% ghost-button pressed fill on dark (near --white-3 @12%)."),
    ("footer", "ft-bar", "default", "backgroundColor", "surface", ("--grey-9",),
     "The #272727 footer slab."),
]:
    try:
        raw = st(comp, state)[prop]
        src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        put_sem(sem2, group, key, semcolor(raw, src, desc, theme="dark", prefer=prefer, dest=group + "." + key))
    except KeyError:
        pass

# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("label", "nv-login", "default", "The 12px account/footer-link size."),
    ("nav", "nv-item", "default", "The 14px nav-item and Store-button size."),
    ("body", "co-lede", "default", "The 16px body and spec-line size."),
    ("eyebrow", "pd-eyebrow", "default", "The 20px section eyebrow (text-ms-24 utility)."),
    ("title", "pd-h", "default", "The 24px product-section title."),
    ("listing", "st-h1", "default", "The 32px where-to-buy heading."),
    ("category", "hh-h1", "default", "The 40px handheld category heading."),
    ("display", "ct-h1", "default", "The 48px category/support display heading."),
]:
    try:
        raw = st(comp, state)["fontSize"]
        src = f"computed fontSize of {comp} {state} (raw/components-computed.json)"
        alias = size_alias.get(raw)
        ty.setdefault("measured", {})[key] = lit(f"{{{alias[0]}}}" if alias else raw, "fontSize",
                      src + (f"; matches declared {alias[1]}" if alias else ""), desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ shape

radii = SPEC["core"].setdefault("radius", {})
if "value" in radii:
    # The declared --radius leaf sits at the node; demote it under a child so
    # the measured radii below are not dropped by the leaf/group merge.
    radii["default"] = {k: radii.pop(k) for k in ("value", "type", "source", "description") if k in radii}
for key, comp, state, prop, desc in [
    ("pill-store", "nv-store", "default", "borderTopLeftRadius", "The 1408px pill radius on the Store button."),
    ("ghost", "pd-watch", "default", "borderTopLeftRadius", "The 60px ghost-button radius on dark sections."),
    ("hero-cta", "hm-learn", "default", "borderTopLeftRadius", "The 64px hero ghost-CTA radius."),
    ("cta", "pd-buy", "default", "borderTopLeftRadius", "The 60px product-page pill CTA radius."),
    ("mobile-cta", "m-cta", "default", "borderTopLeftRadius", "The 60px mobile CTA radius."),
]:
    try:
        v = st(comp, state)[prop]
        src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        mnum = re.match(r"[\d.eE+-]+", v)
        if mnum and float(mnum.group(0)) > 9999 and "px" in v:
            v = "calc(infinity * 1px)"
        dkey = {v_: k_ for k_, v_ in R.items() if k_.startswith("--radius-")}.get(v)
        if dkey:
            radii[key] = lit(f"{{radius.{dkey[len('--radius-'):]}}}", "dimension", src + f"; matches declared {dkey}", desc)
        else:
            radii[key] = lit(v, "dimension" if re.fullmatch(r"[0-9.]+(px|rem)", v or "") else "other", src, desc)
    except (KeyError, AttributeError):
        pass

# ------------------------------------------------------------- elevation

# No painted box-shadow was measured on the public surfaces (every reading
# reported transparent or none); elevation is absent by design on the brand
# site — chrome separates by hairlines and fills.
# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
for key, comp in [("store-cta", "nv-store"), ("ghost", "pd-watch"), ("atom-cta", "pd-buy")]:
    try:
        s_ = st(comp, "default")
        dur, ease = s_.get("transitionDuration"), s_.get("transitionTimingFunction")
        if dur and dur != "0s":
            mo[key] = lit(f"{s_.get('transitionProperty', 'all')} {dur} {ease or ''}".strip(), "other",
                f"computed transition of {comp} default (raw/components-computed.json)",
                f"The measured {comp} transition ({dur}).")
    except KeyError:
        pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("nav-bar", "nv-bar", "default", "h", "dimension", "The 64px top nav (legacy dui-navbar on the home hero)."),
    ("nav-mark", "nv-mark", "default", "w", "dimension", "The 93x64 DJI mark cell."),
    ("nav-item", "nv-item", "default", "w", "dimension", "The 100x64 nav menu item."),
    ("store-cta", "nv-store", "default", "w", "dimension", "The 84x32 Store pill button."),
    ("hero-panel", "hm-slide", "default", "h", "dimension", "The 800px home hero panel."),
    ("hero-cta", "hm-learn", "default", "w", "dimension", "The 133x32 hero ghost CTA."),
    ("category-row", "ct-card", "default", "w", "dimension", "The 1200px product-card row on the category grid."),
    ("subnav", "pd-subnav", "default", "h", "dimension", "The 64px product sub-nav bar."),
    ("atom-cta", "pd-buy", "default", "w", "dimension", "The 144x40 atom-design primary CTA."),
    ("ghost-cta", "pd-watch", "default", "w", "dimension", "The 147x40 atom-design ghost CTA."),
    ("support-search", "sp-search", "default", "w", "dimension", "The 640x32 support search field."),
    ("footer", "ft-bar", "default", "h", "dimension", "The 833px sitemap footer."),
    ("mobile-bar", "m-bar", "default", "h", "dimension", "The 50px mobile-site nav bar."),
    ("mobile-tab", "m-tab", "default", "w", "dimension", "The 54x50 mobile nav tab."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# co-lede's selector caught the "browser not supported" notice in a modal box,
# not the company page lede (the README's Known gaps; measure.mjs is fixed by
# edit, not yet re-run). Every token read from it says so.
# Flagged only while the reading is that notice, so a good recapture clears it.
WRONG_ELEMENT = {k: what for k, what, bad in [
    ("co-lede", "the unsupported-browser notice in a modal box, not the company lede",
     lambda c: "no longer supported" in (c["states"]["default"].get("text") or "")),
] if k in C and bad(C[k])}


def note_wrong(node):
    if isinstance(node, dict):
        src = node.get("source")
        if isinstance(src, str):
            for k, what in WRONG_ELEMENT.items():
                if re.search(rf"(?<![\w-]){re.escape(k)}(?![\w-])", src) and "read from the wrong element" not in src:
                    node["source"] = src = src + f"; {k} caught {what} (read from the wrong element; recapture needed)"
        for v in node.values():
            note_wrong(v)


note_wrong(SPEC)

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
