#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

visual.app (the catalog lists designstripe.com, which redirects here —
"Visual, formerly designstripe") is one public light surface signed out:
the marketing home, the /assets library and /assets/<kind>/<set> galleries,
/tools, /about, /contact and /blog articles. It declares a real
design-token layer (raw/css-vars.json): a shadcn-style semantic layer
(--background/--foreground/--card/--popover/--primary*/--secondary*/
--muted*/--accent*/--destructive*/--border-*/--ring*), the --neutral-50..950
and --green-50..950 hue scales plus base hues (--black/--white/--green/
--indigo/--yellow), and a theme-invariant Tailwind layer (--spacing,
--font-*, --font-weight-*, --leading-*/--tracking-*, --ease-*,
--animate-*, --blur-*, --default-*). Colour vars store bare HSL channels
("64 8% 16%"); build_tokens.py normalises them to hex. Every
theme-switching variable is emitted under both light.* and dark.* as a
{"var": ...} leaf so each theme resolves its own value; invariant names
land under core.*. A .dark block genuinely declares the dark theme (50
rules) even though no public control toggles it.

Measured computed styles from raw/components-computed.json (light surface;
the dark resolution is declared but never painted signed out):

  light       #2c2c26 olive ink (--foreground 64 8% 16%) on headings and
              the footer/logo fills, pure black body text, #6d6e5e muted
              mono subcopy, white page/cards/tiles, #e8e7d9 cream
              (--accent/--ring 56 24% 88%) on the waitlist pill, #414238
              dark-olive button hover, #7e7b4e olive-gold article links,
              #d0d0c8 neutral hairlines on tool cards
  fonts       fontSerif (display headings 96/64/48px light, article links
              20px), fontMono (nav, crumbs, buttons, accordion, body 12–20px
              medium), fontSans (declared — tools pages)
  ramp        measured 12/14/16/20/48/64/96px steps
  shape       3px nav links, 4px logo mark, 6px tool cards, 8px asset
              tiles, full pills (calc(infinity * 1px)) on the waitlist CTA
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
    "The token tree build_tokens.py turns into tokens.json. visual.app "
    "declares its design-token layer in its stylesheets "
    "(raw/css-vars.json): theme-invariant scales under core.* and every "
    "theme-switching name — the --neutral-*/--green-* scales and the shadcn "
    "semantics (--background, --primary, --accent, --border-*, --ring) — "
    "emitted under both light.* and dark.* so each theme resolves its own "
    "value. Declared HSL channel triplets are normalised to hex. The dark "
    "theme is declared, never painted while signed out. Measured roles "
    "alias to the declared values where they match."),
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
    m = re.fullmatch(r"oklab\(([\d.]+)\s+(-?[\d.]+)\s+(-?[\d.]+)(?:\s*/\s*([\d.]+%?))?\)", v)
    if m:
        l, a_, b_, al = m.groups()
        rgb = _oklab_to_hex(float(l), float(a_), float(b_))
        alpha = None if al is None else (float(al[:-1]) / 100 if al.endswith('%') else float(al))
        return _rgba_out(rgb, alpha)
    m = re.fullmatch(r"oklch\(([\d.]+)\s+([\d.]+)\s+([\d.]+)(?:\s*/\s*([\d.]+%?))?\)", v)
    if m:
        l, c, h, al = m.groups()
        a_ = float(c) * math.cos(math.radians(float(h)))
        b_ = float(c) * math.sin(math.radians(float(h)))
        rgb = _oklab_to_hex(float(l), a_, b_)
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
    # "64 8% 16% / 0.5" — the site's --* colour vars store channels only.
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
    if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(v).strip()):
        ty = "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\)|color\([^)]*\)|\d+(?:\.\d+)?\s+[\d.]+%\s+[\d.]+%(?:\s*/\s*[\d.]+%?)?)")


def decl_color(name):
    v = R[name]
    ty = "color" if COLOR_V.fullmatch(str(v).strip()) else "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


# ------------------------------------------------------------------- fonts
#
# fontSerif is the display face (page/section headings, article links);
# fontMono carries every control, crumb and body line; fontSans is declared
# for the tools surfaces.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("ui", "nav-link", "default", "fontMono — every control, crumb, accordion row, footer and body line."),
    ("display", "ast-h1", "default", "fontSerif — the display face (page headings 96px, sections 48px light, article links 20px)."),
]:
    if have(comp, state, "fontFamily"):
        v = ts(comp, state, "fontFamily")
        fam[key] = {"value": v, "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
faces = json.dumps(V.get("fonts") or [])
m = re.search(r'"font-family":\s*"\\?(fontSans)', faces)
if m:
    fam["sans"] = {"value": "fontSans", "type": "fontFamily",
                   "source": "declared @font-face in the site stylesheet (raw/css-vars.json); not exercised on any measured public component",
                   "description": "fontSans — the declared sans face (tools surfaces)."}

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, desc in [
    ("light", "sec-h2", "300 — the serif section headings."),
    ("regular", "post-h1", "400 — display headings and article links."),
    ("medium", "nav-link", "500 — the mono controls, crumbs and subcopy."),
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
# per-theme below. Scale families (12-step Radix-style palettes) are emitted
# per-theme even when a step happens to resolve identically, so each theme's
# scale stays complete.

SCALE_FAMS = {"amber", "blue", "brown", "crimson", "cyan", "gold", "grass",
              "gray", "green", "indigo", "jade", "neutral", "plum", "red", "ruby",
              "sand", "tangerine", "teal", "tomato", "violet", "yellow"}

def scale_rename(name):
    """Map a scale member to the --color-<fam>-<step> name it emits under."""
    m = re.fullmatch(r"--([a-z]+)-(\d+(?:-oklch)?)", name)
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

CORE_HANDLED = re.compile(
    r"^--(color-|text-|leading-|tracking-|container-|breakpoint-|radius-|"
    r"duration-|ease-|animate-|blur-|z-|default-|drop-shadow-|font-weight-)")

# Every remaining invariant name that wasn't bucketed or a scale member is
# emitted at its natural dashed path under core.* (the --spacing unit,
# --radius base, --border-hairline, --destructive/--info/--success/--warning,
# --head-climb, --dock-rest, --quote-glow, --person-*, --aspect-video,
# --silk-* …).
for name in sorted(R):
    if R[name] != D.get(name) or is_scale_member(name) or CORE_HANDLED.match(name):
        continue
    if name.startswith("--font-weight-"):
        continue
    if name == "--border-hairline":
        # The declared hairline is a stroke width ("1px"); the measured
        # border.hairline role in each theme carries the hairline colour.
        # Keep the width nested under it so the generated CSS names do not collide.
        SPEC["core"].setdefault("border", {}).setdefault("hairline", {})["width"] = decl(name)
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
# Measured on the light surface only — the dark theme is declared but never
# painted while signed out, so dark.* carries the declared layer alone.

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


sem = SPEC["light"]
# A measured group that collides with a declared leaf (--background under
# background, --border under border) demotes it before roles read EMITTED,
# so aliases resolve to the leaf's new path. Run the demotion on BOTH theme
# sets: the declared paths must stay identical light vs dark even when only
# light gains measured roles, or the generated CSS would mix --background
# (dark) with --background-default (light).
for group in ("background", "text", "action", "border", "surface", "foreground"):
    for root in (SPEC["light"], SPEC["dark"]):
        _demote_leaf_group(root, group)
for key, comp, state, prop, group, prefer, desc in [
    ("page", "mkt-nav", "default", "_body-bg", "background", ("--background",),
     "The white field the whole public surface paints."),
    ("card", "ast-tile-hero", "default", "backgroundColor", "background", ("--card", "--popover"),
     "The white card/tile field (asset tiles and tool cards match --card/--popover/--secondary)."),
    ("cream", "waitlist-btn", "default", "backgroundColor", "background", ("--accent", "--ring"),
     "The #e8e7d9 cream field on the waitlist pill (matches --accent/--ring, 56 24% 88%)."),
    ("hover-fill", "nav-link", "hover", "backgroundColor", "background", ("--secondary-hover", "--muted"),
     "The #f6f6f4 near-white fill nav links pick up on hover."),
    ("ink", "site-footer", "default", "backgroundColor", "background", (),
     "The #2c2c26 olive-ink dark fill — the footer field, logo mark and feature panel (matches --foreground)."),
    ("ink", "ast-h1", "default", "color", "text", ("--foreground",),
     "The #2c2c26 olive ink — headings, logo text and the dark-panel fills (matches --foreground)."),
    ("black", "hero-h1", "default", "color", "text", ("--black",),
     "Pure black body/hero text on the marketing surface (matches --black)."),
    ("muted", "hero-sub", "default", "color", "text", ("--muted-foreground",),
     "The #6d6e5e muted olive — mono subcopy, helper text and article body (matches --muted-foreground)."),
    ("on-dark", "feature-acc", "default", "color", "text", ("--white", "--primary-foreground"),
     "White text inside the dark feature panel and footer (matches --white)."),
    ("link", "post-link", "default", "color", "text", (),
     "The #7e7b4e olive-gold on article inline links."),
    ("cream", "waitlist-btn", "default", "backgroundColor", "action", ("--accent", "--ring"),
     "The #e8e7d9 cream waitlist CTA fill (matches --accent/--ring)."),
    ("cream-hover", "waitlist-btn", "hover", "backgroundColor", "action", (),
     "The #414238 dark-olive fill the waitlist CTA takes on hover/pressed."),
    ("on-cream", "waitlist-btn", "default", "color", "action", ("--foreground",),
     "The #2c2c26 ink label on the cream CTA (matches --foreground)."),
    ("olive", "waitlist-btn", "default", "borderTopColor", "border", (),
     "The #aaa674 olive border on the waitlist CTA."),
    ("hairline", "tool-card", "default", "borderTopColor", "border", ("--neutral-200", "--border-surface"),
     "The #d0d0c8 neutral hairline on tool cards (matches --neutral-200)."),
    ("focus", "nav-link", "focus-visible", "outlineColor", "border", ("--ring-a11y", "--border-a11y"),
     "The #101010 near-black focus-visible outline on nav links and cards."),
]:
    try:
        if prop == "_body-bg":
            # No measured element reports the page field; read the declared
            # --background the pages paint, not a screenshot pixel.
            raw = R["--background"]
            src = ("declared --background (raw/css-vars.json resolved.light); no computed reading of the page field "
                   "(seen in screenshots/*-light-*.png)")
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        put_sem(sem, group, key, semcolor(raw, src, desc, prefer=prefer))
    except KeyError:
        pass

# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("crumb", "tool-crumb", "default", "The 12px mono crumbs, nav links and CTA labels."),
    ("body", "post-para", "default", "The 14px mono body and subcopy."),
    ("ui", "site-footer", "default", "The 16px footer, accordion and nav base."),
    ("lead", "post-link", "default", "The 20px serif article links, accordion rows and kind links."),
    ("section", "sec-h2", "default", "The 48px serif section heading (and mobile display)."),
    ("post-title", "post-h1", "default", "The 64px serif article title."),
    ("display", "ast-h1", "default", "The 96px serif page display."),
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
    ("nav-link", "nav-link", "default", "borderTopLeftRadius", "The 3px nav-link radius."),
    ("logo", "mkt-logo", "default", "borderTopLeftRadius", "The 4px logo-mark radius."),
    ("card", "tool-card", "default", "borderTopLeftRadius", "The 6px tool-card radius."),
    ("tile", "ast-tile-hero", "default", "borderTopLeftRadius", "The 8px asset-tile radius."),
    ("pill", "waitlist-btn", "default", "borderTopLeftRadius", "The full-pill (calc(infinity * 1px)) waitlist CTA."),
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

# Every measured public component reports boxShadow: none — no shadow tokens
# are emitted rather than inventing one.

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
try:
    s = st("nav-link", "default")
    dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        mo["link"] = lit(f"{s.get('transitionProperty', 'all')} {dur} {ease or ''}".strip(), "other",
            "computed transition of nav-link default (raw/components-computed.json)",
            "The measured nav-link transition (all 0.2s).")
except KeyError:
    pass
try:
    s = st("feature-acc", "default")
    dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        mo["control"] = lit(f"{s.get('transitionProperty', 'all')} {dur} {ease or ''}".strip(), "other",
            "computed transition of feature-acc default (raw/components-computed.json)",
            "The measured accordion/control transition (all 0.15s).")
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("topbar-height", "mkt-nav", "default", "h", "dimension", "The 32px fixed top nav bar."),
    ("logo-width", "mkt-logo", "default", "w", "dimension", "The 88px logo mark."),
    ("cta-width", "waitlist-btn", "default", "w", "dimension", "The 82px waitlist CTA."),
    ("tile-hero", "ast-tile-hero", "default", "w", "dimension", "The 568.66px featured category tile (2× the standard tile)."),
    ("tile", "ast-tile", "default", "w", "dimension", "The 280.33px standard category tile."),
    ("avatar", "av-item", "default", "w", "dimension", "The ~223px avatar grid item."),
    ("tool-card-height", "tool-card", "default", "h", "dimension", "The 422.5px tool card."),
    ("footer-height", "site-footer", "default", "h", "dimension", "The 320px dark footer."),
    ("mobile-topbar-height", "m-nav", "default", "h", "dimension", "The 40px phone top bar."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# Readings a token must not pass off as the component it is named for, or as
# the latest run's: post-para's selector caught a subtitle (the README's Known
# gaps), and a state kept after a failed re-read (rerunError) is an earlier
# run's reading republished under the component's new date.
# post-para is flagged only while its reading is the short subtitle (the fixed
# selector asks for more than 80 characters), so a good recapture clears it.
WRONG_ELEMENT = {k: what for k, what, bad in [
    ("post-para", "the one-line article subtitle, not a body paragraph",
     lambda c: len((c["states"]["default"].get("text") or "").strip()) <= 80),
] if k in C and bad(C[k])}
KEPT = {(k, sn): v for k, c in C.items() for sn, v in c.get("states", {}).items() if v.get("rerunError")}


def kept_note(k, sn):
    v = KEPT[(k, sn)]
    when = f"read {v['read']}" if v.get("read") else "its own date unrecorded"
    failed = v.get("rerunOn") or C[k]["run"]
    return f"{k} {sn} is a kept reading: the {failed} re-read failed (rerunError) and the earlier reading was kept, {when}"


def note_readings(node):
    if isinstance(node, dict):
        src = node.get("source")
        if isinstance(src, str):
            for k, what in WRONG_ELEMENT.items():
                if re.search(rf"(?<![\w-]){re.escape(k)}(?![\w-])", src) and "read from the wrong element" not in src:
                    node["source"] = src = src + f"; {k} caught {what} (read from the wrong element; recapture needed)"
            for k, sn in sorted(KEPT):
                if re.search(rf"(?<![\w-]){re.escape(k)} {re.escape(sn)}(?![\w-])", src) and f"{k} {sn} is a kept reading" not in src:
                    node["source"] = src = src + "; " + kept_note(k, sn)
        for v in node.values():
            note_readings(v)


note_readings(SPEC)

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
