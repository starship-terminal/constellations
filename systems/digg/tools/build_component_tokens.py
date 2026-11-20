#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

digg.com (the 2025 reboot) paints both themes signed out: the trending feed
(story cards with the digg-it vote pill, comment count, source cluster and
"N Sources" link), a category feed, story pages, /u/<source> profiles and
the Clerk auth forms. It declares a real design-token layer
(raw/css-vars.json): the shadcn-style semantic layer
(--background/--foreground/--card/--popover/--primary*/--secondary*/
--muted*/--accent*/--destructive*/--border/--input/--ring, the --sidebar-*
rail set, --chart-1..5, --rank-one/--success), the full Tailwind hue scales
(--red-50..950, --featured-image-gray-*, --color-gray-*) and a
theme-invariant Tailwind layer (--text-*, --leading-*, --tracking-*,
--radius-*, --ease-*, --animate-*, --container-*, --breakpoint-*, --blur-*).
Colour vars arrive as lab()/oklab()/oklch()/rgb(); build_tokens.py
normalises them to hex. Every theme-switching variable is emitted under
both light.* and dark.* as a {"var": ...} leaf so each theme resolves its
own value; invariant names land under core.*.

Measured computed styles from raw/components-computed.json — light pass
plus a real dark pass (the sidebar theme pill was cycled to dark, so the
d-* components are measured dark paint, not declared-only guesses):

  light       #fdfdff near-white page (--background), #ffffff white cards
              (--card), #f0f0f5 sidebar-accent/muted fills, #161617 ink
              (--foreground), ink@70% muted text (--muted-foreground),
              #1c66eb primary blue (--primary/--accent/--sidebar-primary)
              on Sign up/Continue/links, rgba(0,0,0,0.08) hairlines
              (--border), #e5e5e5 field borders (--input), #ababbf focus
              ring (--ring), #e37b4c rank-one orange
  dark        #161617 page, #1c1c1f cards, #fdfdff ink, ink@70% muted,
              rgba(255,255,255,0.08/0.15) hairlines — all measured with the
              theme pill set to dark
  fonts       roobert everywhere — UI/headlines 400–700, headings to 36px;
              declared @font-face ibmPlexSans (typeset) and vt323 (the
              retro vote-odometer face)
  ramp        measured 10/12/13/14/16/18/20/24/30/36px steps
  shape       2px tight links, 8px fields, 18px cards (rounded-2xl), 26px
              controls (rounded-4xl), full pills (calc(infinity * 1px),
              999px on the story vote) on sidebar items and primary CTAs
  shadow      one real shadow: the field's rgba(0,0,0,0.05) 0 1px 2px
"""


import json, math, pathlib, re

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
    "The token tree build_tokens.py turns into tokens.json. digg.com "
    "declares its design-token layer in its stylesheets "
    "(raw/css-vars.json): theme-invariant scales under core.* and every "
    "theme-switching name — the Tailwind hue scales and the shadcn "
    "semantics (--background, --primary, --accent, --border, --input, "
    "--ring, --sidebar-*) — emitted under both light.* and dark.* so each "
    "theme resolves its own value. Both themes are really painted signed "
    "out: the dark roles below are measured through the sidebar theme "
    "pill's System -> Light -> Dark cycle. lab()/oklab()/oklch() colour "
    "vars are normalised to hex. Measured roles alias to the declared "
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
            raise ValueError(f"{name}: duplicate token path {path}")
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


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\)|color\([^)]*\)|\d+(?:\.\d+)?\s+[\d.]+%\s+[\d.]+%(?:\s*/\s*[\d.]+%?)?)")


def decl_color(name):
    v = R[name]
    ty = "color" if COLOR_V.fullmatch(str(v).strip()) else "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


# ------------------------------------------------------------------- fonts
#
# roobert is the single UI face — every sidebar row, card, control and
# heading, 400 through 700. The stylesheet declares three faces: roobert
# (+italic +fallbacks), ibmPlexSans (the typeset/prose face) and vt323 —
# the retro bitmap mono the vote odometer's digits are drawn in.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("ui", "post-headline", "default", "roobert — every sidebar row, card, control and heading, 400–700."),
    ("body", "st-para", "default", "roobert — the TLDR story prose at 18px medium."),
]:
    if have(comp, state, "fontFamily"):
        v = ts(comp, state, "fontFamily")
        fam[key] = {"value": v, "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
# vt323 and ibmPlexSans paint no measured component, so their stacks are the
# declared next/font variables, verbatim (raw/css-vars.json theme bin), never
# a stack composed here.
DECL_FONT = {n: v for rule in V.get("theme") or [] for n, v in (rule.get("properties") or {}).items() if n.startswith("--font-")}
for key, name, why, desc in [
    ("mono", "--font-vt323", "the retro bitmap face of the vote-odometer digits",
     "vt323 — the pixel-style mono the odometer counts are drawn in."),
    ("typeset", "--font-ibm-plex", "not exercised on any measured public component",
     "ibmPlexSans — the declared typeset/prose face."),
]:
    if name in DECL_FONT:
        fam[key] = {"value": DECL_FONT[name], "type": "fontFamily",
                    "source": f"declared {name} in the site stylesheet (raw/css-vars.json); {why}",
                    "description": desc}

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, desc in [
    ("regular", "post-summary", "400 — card summaries, TLDR lead and rail panels."),
    ("medium", "post-vote", "500 — vote pills, controls and OAuth buttons."),
    ("semibold", "post-headline", "600 — card headlines, sidebar rows and source counts."),
    ("bold", "st-h1", "700 — the story and category headings."),
]:
    try:
        w = int(float(ts(comp, "default", "fontWeight")))
        weights[key] = lit(w, "fontWeight",
                           f"computed fontWeight of {comp} default (raw/components-computed.json)", desc)
    except (KeyError, TypeError, ValueError):
        pass
for name in sorted(k for k in R if k.startswith("--font-weight-")):
    weights.setdefault("declared", {})[name[len("--font-weight-"):]] = decl(name, "other")

# --------------------------------------------------- declared scales (core)
#
# Theme-invariant names land here; every theme-switching name is emitted
# per-theme below. Scale families (Tailwind 11-step hue palettes) are emitted
# per-theme even when a step happens to resolve identically, so each theme's
# scale stays complete.

SCALE_FAMS = {"amber", "blue", "cyan", "emerald", "featured-image-gray",
              "fuchsia", "gray", "green", "indigo", "lime", "neutral",
              "orange", "pink", "purple", "red", "rose", "sky", "slate",
              "stone", "teal", "violet", "yellow", "zinc"}

def scale_rename(name):
    """Map a scale member to the --color-<fam>-<step> name it emits under."""
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

size_alias = {}    # 'NNpx'/'Nrem' -> ('font.size.<key>', '--var')
for name in sorted(k for k in R if k.startswith("--text-")):
    if R[name] != D.get(name):
        continue
    m = re.fullmatch(r"--text-(.+?)--line-height", name)
    if m:
        SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})[m.group(1)] = decl(name)
        continue
    m = re.fullmatch(r"--text-(.+?)--letter-spacing", name)
    if m:
        SPEC["core"].setdefault("font", {}).setdefault("tracking", {})[m.group(1)] = decl(name)
        continue
    key = name[len("--text-"):]
    SPEC["core"].setdefault("font", {}).setdefault("size", {})[key] = decl(name)
    size_alias.setdefault(R[name], (f"font.size.{key}", name))

for name in sorted(k for k in R if k.startswith("--leading-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})[name[len("--leading-"):]] = decl(name)
for name in sorted(k for k in R if k.startswith("--tracking-")):
    if R[name] == D.get(name):
        SPEC["core"].setdefault("font", {}).setdefault("tracking", {})[name[len("--tracking-"):]] = decl(name)
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

CORE_HANDLED = re.compile(
    r"^--(color-|text-|leading-|tracking-|container-|breakpoint-|radius-|"
    r"duration-|ease-|animate-|blur-|z-|default-|drop-shadow-|shadow-|font-weight-)")

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

for root in (SPEC["light"], SPEC["dark"]):
    for name in sorted(R):
        if name in TWINS:
            continue
        if is_scale_member(name) or R[name] != D.get(name):
            ty = "color" if COLOR_V.fullmatch(str(R[name]).strip()) else "other"
            emit(root, scale_rename(name), var(name, ty))

# ------------------------------------------------------- measured roles
#
# digg paints both themes signed out, so dark.* carries real measured roles
# (the d-* components) beside the declared layer — not declared-only guesses.

role_alias = {"light": dict(color_alias), "dark": dict(color_alias)}
for root, theme in ((SPEC["light"], "light"), (SPEC["dark"], "dark")):
    for name in sorted(R):
        if name in TWINS or not (is_scale_member(name) or R[name] != D.get(name)):
            continue
        p = EMITTED.get(scale_rename(name)) or EMITTED.get(name)
        resolved = R[name] if theme == "light" else D[name]
        role_alias[theme].setdefault(norm_color(resolved), p)
    for name in sorted(R):
        if R[name] == D.get(name) and not is_scale_member(name):
            p = EMITTED.get(name)
            if p:
                role_alias[theme].setdefault(norm_color(R[name]), p)


def semcolor(raw, src, desc, theme="light", prefer=()):
    """Alias to a preferred declared name when it resolves to this colour."""
    for p in prefer:
        if p in R and norm_color(R[p] if theme == "light" else D[p]) == norm_color(raw):
            path = EMITTED.get(scale_rename(p)) or EMITTED.get(p)
            if path:
                return lit(f"{{{path}}}", "color", src + f"; matches declared {p}", desc)
    alias = role_alias[theme].get(norm_color(raw))
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


# A measured group that collides with a declared leaf (--background under
# background, --border under border) demotes it before roles read EMITTED,
# so aliases resolve to the leaf's new path. Run the demotion on BOTH theme
# sets: the declared paths must stay identical light vs dark even when only
# one gains measured roles, or the generated CSS would mix --background
# with --background-default.
for group in ("background", "text", "action", "border", "surface", "foreground"):
    for root in (SPEC["light"], SPEC["dark"]):
        _demote_leaf_group(root, group)

sem = SPEC["light"]
for key, comp, state, prop, group, prefer, desc in [
    ("page", "st-vote", "default", "backgroundColor", "background", ("--background",),
     "The #fdfdff near-white field the public surfaces paint (the vote pill's fill)."),
    ("card", "rail-contribs", "default", "backgroundColor", "background", ("--card",),
     "The #ffffff white card field on rail panels."),
    ("fill", "sb-home", "default", "backgroundColor", "background", ("--sidebar-accent", "--muted", "--secondary"),
     "The #f0f0f5 light-gray fill on the selected sidebar row and story crumb (matches --sidebar-accent/--muted/--secondary)."),
    ("input-fill", "feed-trending", "default", "backgroundColor", "background", (),
     "The translucent wash (bg-input/30) on the feed sort controls."),
    ("ink", "post-headline", "default", "color", "text", ("--foreground",),
     "The #161617 ink — every headline, sidebar row and control label (matches --foreground)."),
    ("muted", "post-summary", "default", "color", "text", ("--muted-foreground",),
     "The ink@70% muted text — card summaries, source counts, footer links (matches --muted-foreground)."),
    ("link", "lg-signup", "default", "color", "text", ("--primary", "--accent"),
     "The #1c66eb blue on text links like the login Sign up link (matches --primary/--accent)."),
    ("primary", "sb-signup", "default", "backgroundColor", "action", ("--primary", "--accent", "--sidebar-primary"),
     "The #1c66eb primary blue on Sign up and Continue (matches --primary/--accent/--sidebar-primary)."),
    ("primary-hover", "sb-signup", "hover", "backgroundColor", "action", (),
     "The blue @80% the primary CTAs take on hover/pressed."),
    ("on-primary", "lg-continue", "default", "color", "action", ("--primary-foreground",),
     "The white label on the primary CTAs (matches --primary-foreground)."),
    ("oauth-fill", "lg-google", "default", "backgroundColor", "action", ("--background",),
     "The near-white fill on the OAuth outline buttons."),
    ("vote-border", "st-vote", "default", "borderTopColor", "border", (),
     "The primary-blue @20% border on the story digg-it pill."),
    ("hairline", "rail-contribs", "default", "borderTopColor", "border", ("--border",),
     "The rgba(0,0,0,0.08) hairline on cards and panels (matches --border)."),
    ("input", "lg-email", "default", "borderTopColor", "border", ("--input",),
     "The #e5e5e5 field border (matches --input)."),
    ("focus", "sb-signup", "focus-visible", "outlineColor", "border", ("--ring", "--sidebar-ring"),
     "The #ababbf focus-visible ring on controls (matches --ring/--sidebar-ring)."),
    ("rank-one", "rail-contribs", "default", "_rankone", "text", ("--rank-one",),
     "The #e37b4c orange of the #1 contributor rank (declared --rank-one)."),
]:
    try:
        if prop == "_rankone":
            raw = R["--rank-one"]
            src = "declared --rank-one (raw/css-vars.json resolved.light); no measured component paints it"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        put_sem(sem, group, key, semcolor(raw, src, desc, prefer=prefer))
    except KeyError:
        pass

# Measured dark roles — d-* components read with the theme pill set to dark.
sem2 = SPEC["dark"]
for key, comp, state, prop, group, prefer, desc in [
    ("card", "d-rail", "default", "backgroundColor", "background", ("--card", "--popover"),
     "The #1c1c1f dark card field on rail panels (matches --card)."),
    ("input-fill", "d-trending", "default", "backgroundColor", "background", (),
     "The white @4.5% wash on the feed sort controls in dark."),
    ("ink", "d-headline", "default", "color", "text", ("--foreground",),
     "The #fdfdff near-white ink in dark (matches --foreground)."),
    ("muted", "d-vote", "default", "color", "text", ("--muted-foreground",),
     "The ink@70% muted text in dark (matches --muted-foreground)."),
    ("primary", "d-signup", "default", "backgroundColor", "action", ("--primary", "--accent", "--sidebar-primary"),
     "The #1c66eb primary blue, identical in dark (matches --primary/--accent)."),
    ("on-primary", "d-signup", "default", "color", "action", ("--primary-foreground",),
     "The white label on the primary CTA in dark (matches --primary-foreground)."),
    ("hairline", "d-rail", "default", "borderTopColor", "border", ("--border",),
     "The rgba(255,255,255,0.08) hairline on dark cards (matches --border)."),
    ("input", "d-trending", "default", "borderTopColor", "border", ("--input",),
     "The white @15% control border in dark (matches --input)."),
    ("focus", "d-signup", "focus-visible", "outlineColor", "border", (),
     "The #1c66eb primary at 50% the focus-visible outline resolves in dark."),
    ("primary-hover", "d-signup", "hover", "backgroundColor", "action", (),
     "The primary blue @80% the CTA takes on hover — identical in dark."),
]:
    try:
        raw = st(comp, state)[prop]
        src = f"computed {prop} of {comp} {state} (raw/components-computed.json, theme pill set to dark)"
        put_sem(sem2, group, key, semcolor(raw, src, desc, theme="dark", prefer=prefer))
    except KeyError:
        pass

# Dark roles with no d-* reading: the declared .dark values, plus the
# theme-invariant recipes (border-primary/20) whose computed colour depends
# only on --primary, which resolves #1c66eb in both themes.
for key, name, group, prefer, desc in [
    ("page", "--background", "background", ("--background",),
     "The #161617 near-black field the dark captures paint."),
    ("fill", "--sidebar-accent", "background", ("--sidebar-accent", "--muted", "--secondary"),
     "The #27272c selected-row fill on the dark sidebar (matches --sidebar-accent)."),
    ("link", "--primary", "text", ("--primary", "--accent"),
     "The #1c66eb blue on text links, theme-invariant (matches --primary)."),
    ("oauth-fill", "--background", "action", ("--background",),
     "The dark field the OAuth outline buttons' bg-background recipe paints (theme-invariant recipe; the auth pages were not re-captured in dark)."),
    ("rank-one", "--rank-one", "text", ("--rank-one",),
     "The #e37b4c rank-one orange, theme-invariant (matches --rank-one)."),
]:
    put_sem(sem2, group, key, semcolor(
        D[name],
        f"declared .dark value of {name} (raw/css-vars.json resolved.dark); no d-* component reading of it",
        desc, theme="dark", prefer=prefer))

put_sem(sem2, "border", "vote-border", semcolor(
    st("st-vote", "default")["borderTopColor"],
    "computed borderTopColor of st-vote default (raw/components-computed.json): the border-primary/20 recipe — --primary resolves the identical #1c66eb in dark (raw/css-vars.json); measured on the light story vote pill, not re-measured in dark",
    "The primary-blue @20% border on the story digg-it pill, theme-invariant.",
    theme="dark"))

# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("label", "st-tldr", "default", "The 10px tracked-out TLDR/REPORT labels."),
    ("micro", "site-footer", "default", "The 12px footer and meta text."),
    ("note", "lg-signup", "default", "The 13px auth link text."),
    ("body", "post-summary", "default", "The 14px card body, controls and sidebar."),
    ("headline", "post-headline", "default", "The 16px card headline (and story kicker)."),
    ("lead", "st-para", "default", "The 18px TLDR story prose."),
    ("deck", "st-summary", "default", "The 20px story summary / profile name."),
    ("card-title", "lg-h1", "default", "The 24px auth card heading."),
    ("page", "cat-title", "default", "The 30px category page heading."),
    ("display", "st-h1", "default", "The 36px story headline."),
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
for key, comp, state, prop, desc in [
    ("tight", "post-sources", "default", "borderTopLeftRadius", "The 2px tight link radius."),
    ("field", "lg-email", "default", "borderTopLeftRadius", "The 8px auth-field radius."),
    ("card", "post-card", "default", "borderTopLeftRadius", "The 18px story-card / rail-panel radius (rounded-2xl)."),
    ("control", "sb-signup", "default", "borderTopLeftRadius", "The 26px control radius on Sign up/Log in/theme pill (rounded-4xl)."),
    ("pill", "sb-home", "default", "borderTopLeftRadius", "The full-pill radius (calc(infinity * 1px)) on sidebar items and primary CTAs."),
    ("vote", "st-vote", "default", "borderTopLeftRadius", "The 999px story digg-it pill radius."),
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

# One real shadow on the public surface: the auth field's 0 1px 2px black@5%.
# Cards carry a 0-blur ring shadow (a painted hairline, covered by
# border.hairline) and every other component reports boxShadow: none.
sh = SPEC["core"].setdefault("shadow", {})
SHADOW_LAYER = re.compile(r"(rgba?\([^)]*\))\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+([\d.]+px)\s+(-?[\d.]+px)")


def painted_shadow(box):
    """Every layer of a computed boxShadow, parsed in full (a layer the pattern cannot read stops the
    build), minus Tailwind's transparent ring placeholders."""
    if box in ("", "none"):
        return []
    layers = SHADOW_LAYER.findall(box)
    if SHADOW_LAYER.sub("", box).replace(",", "").strip() or "inset" in box:
        raise SystemExit(f"boxShadow not fully parsed: {box!r}")
    return [{"offsetX": x, "offsetY": y, "blur": b, "spread": sp, "color": c}
            for c, x, y, b, sp in layers if not re.fullmatch(r"rgba\([^)]*,\s*0\)", c)]


try:
    layers = painted_shadow(st("lg-email", "default").get("boxShadow", ""))
    if layers:
        sh["field"] = lit(layers, "shadow",
            "computed boxShadow of lg-email default, transparent ring placeholders left out (raw/components-computed.json)",
            "The auth field's 0 1px 2px rgba(0,0,0,0.05) shadow (shadow-xs).")
except KeyError:
    pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
try:
    s = st("sb-signup", "default")
    dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        mo["control"] = lit(f"{s.get('transitionProperty', 'all')} {dur} {ease or ''}".strip(), "other",
            "computed transition of sb-signup default (raw/components-computed.json)",
            "The measured control transition (all 0.15s cubic-bezier(0.4,0,0.2,1)).")
except KeyError:
    pass
try:
    s = st("lg-continue", "default")
    dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        mo["auth"] = lit(f"{s.get('transitionProperty', 'all')} {dur} {ease or ''}".strip(), "other",
            "computed transition of lg-continue default (raw/components-computed.json)",
            "The measured auth-button transition (0.1s).")
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("sidebar-item", "sb-home", "default", "w", "dimension", "The 231x40 full-width sidebar row (items, theme pill, Log in, Sign up all share it)."),
    ("sort-control", "feed-trending", "default", "w", "dimension", "The 105x36 Trending sort trigger."),
    ("density-control", "feed-compact", "default", "w", "dimension", "The 64x36 Compact density control."),
    ("story-card", "post-card", "default", "h", "dimension", "The ~183px feed story card (704px column)."),
    ("vote-pill", "post-vote", "default", "w", "dimension", "The 32x24 card vote pill (icon + odometer)."),
    ("comment-link", "post-comment", "default", "w", "dimension", "The 32x32 comment-count link."),
    ("avatar", "post-avatars", "default", "w", "dimension", "The 24x24 source avatar in the cluster."),
    ("thumb", "post-thumb", "default", "w", "dimension", "The 120x80 card thumbnail."),
    ("rail-card", "rail-contribs", "default", "w", "dimension", "The 376px right-rail panel width."),
    ("digg-it", "st-vote", "default", "w", "dimension", "The 138x44 story digg-it pill."),
    ("auth-field", "lg-email", "default", "w", "dimension", "The 353x36 auth form field/button width."),
    ("auth-link", "lg-signup", "default", "h", "dimension", "The ~18px auth link line."),
    ("mobile-bar", "m-bar", "default", "h", "dimension", "The 107px phone top bar."),
    ("mobile-card", "m-card", "default", "w", "dimension", "The 390px phone story card."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
