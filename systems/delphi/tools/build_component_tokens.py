#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

delphi.co (the catalog lists delphi.ai, which redirects here) is one public
surface signed out: the marketing/search home, /discover/<topic> galleries,
public /search/<question> results, public expert profiles (/<expert>) and
public chat surfaces (/<expert>/chat). It declares a real design-token layer
(raw/css-vars.json): a themed Radix-style 12-step palette (--amber-1..12,
--gray1..12 plus --sand, --tangerine, --mind-*, --person-*), a shadcn-style
semantic layer (--background/--foreground/--card/--popover/--primary/
--secondary/--muted/--accent/--border/--ring/--input and their -foreground
twins), Delphi's own semantic roles (--fg-*, --surface-*, --brand-accent,
--bubble-accent, --avatar-*, --sidebar-*, --chart-*, --border-hairline), and
a theme-invariant Tailwind layer (--text-* sizes, --leading-*/--tracking-*,
--font-weight-*, --radius-*, --spacing, --container-*, --breakpoint-*,
--animate-*, --duration-*/--ease-*, --blur-*, --z-*, --drop-shadow-*). Every
theme-switching variable is emitted under both light.* and dark.* as a
{"var": ...} leaf so each theme resolves its own value; invariant names land
under core.*. The --color-* silk aliases are deduplicated against their
twins (--color-sand-1 == --sand-1) so one token never ships under two names.

Measured computed styles from raw/components-computed.json (light surface;
the dark resolution is declared but never painted signed out):

  light       #21201c ink (--fg-high), #63635e mid (--fg-mid), #82827c low
              (--fg-low), #161615 strong section heads, white cards and page,
              a #f7f3f0 warm field on the topic/ask cards, the #fd5400
              --brand-accent orange on Create/Expand/Send, #21201c dark
              button fill (--primary), translucent oklab hairlines and chips,
              #f0eae4 quote text on the dark perspective flip cards
  fonts       Delphi Inter (every UI control), Delphi Pythia (display
              headings, quotes, the 10px credential badges), Delphi Geist
              Mono (declared @font-face only — not exercised on any public
              component measured)
  ramp        measured 50/34/32/20/18/16/14/13/12/10px steps
  shape       6px badges, 18px suggested chips, 20px experience/mobile
              cards, 24px topic/discover cards, 26px buttons and the sign-in
              dialog, 28px flip cards, full pills (calc(infinity * 1px))
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
    "The token tree build_tokens.py turns into tokens.json. delphi.co "
    "declares its design-token layer in its stylesheets "
    "(raw/css-vars.json): theme-invariant scales under core.* and every "
    "theme-switching name — Radix-style palette steps, shadcn semantics and "
    "Delphi's --fg-*/--surface-*/--mind-* roles — emitted under both light.* "
    "and dark.* so each theme resolves its own value. The dark theme is "
    "declared, never painted while signed out. Measured roles alias to the "
    "declared values where they match."),
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


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\)|color\([^)]*\))")


def decl_color(name):
    v = R[name]
    ty = "color" if COLOR_V.fullmatch(str(v).strip()) else "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


# ------------------------------------------------------------------- fonts
#
# Delphi Inter carries every UI control; Delphi Pythia is the display face
# (hero/section headings, quoted perspectives, the small credential badges);
# Delphi Geist Mono is declared as a @font-face but is not exercised on any
# public component that was measured.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("ui", "chat-input", "default", "Delphi Inter — every UI control, body and meta text."),
    ("display", "hero-h1", "default", "Delphi Pythia — the serif display face (hero 50px, names 34px, quotes 18px, badges 10px)."),
]:
    if have(comp, state, "fontFamily"):
        v = ts(comp, state, "fontFamily")
        fam[key] = {"value": v, "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
faces = json.dumps(V.get("fonts") or [])
m = re.search(r'"font-family":\s*"\\?(Delphi Geist Mono)', faces)
if m:
    fam["mono"] = {"value": "Delphi Geist Mono", "type": "fontFamily",
                   "source": "declared @font-face in the site stylesheet (raw/css-vars.json); not exercised on any measured public component",
                   "description": "Delphi Geist Mono — the declared mono face."}

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, desc in [
    ("regular", "chat-input", "400 — body and field text."),
    ("book", "share-btn", "450 — the profile Share pill."),
    ("medium", "signin-btn", "500 — pill buttons, chips and card actions."),
    ("semibold", "exp-name", "600 — expert names and credential badges."),
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
              "gray", "green", "indigo", "jade", "plum", "red", "ruby",
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
    ("page", "mkt-header", "default", "_body-bg", "background", ("--background",),
     "The white field the whole public surface paints."),
    ("card", "disc-card", "default", "backgroundColor", "background", ("--card",),
     "The white card field (result and gallery cards match --card/--popover)."),
    ("warm", "topic-card", "default", "backgroundColor", "background", (),
     "The #f7f3f0 warm field on the topic/ask cards."),
    ("chip", "suggested-chip", "default", "backgroundColor", "background", (),
     "The ~10% ink chip fill on suggested questions, nav topics and dialog alternatives."),
    ("badge", "srch-badge", "default", "backgroundColor", "background", (),
     "The ~6% ink fill behind credential badges."),
    ("ink", "hero-h1", "default", "color", "text", ("--fg-high", "--foreground"),
     "The #21201c ink — headings and body text (matches --fg-high/--foreground)."),
    ("mid", "nav-topic", "default", "color", "text", ("--fg-mid",),
     "The #63635e mid text — nav topics, pills, helper copy (matches --fg-mid)."),
    ("low", "m-signin", "default", "color", "text", ("--fg-low",),
     "The #82827c low text — bylines and the mobile sign-in (matches --fg-low)."),
    ("strong", "exp-section", "default", "color", "text", (),
     "The #161615 near-black on profile section headings."),
    ("on-dark", "persp-quote", "default", "color", "text", (),
     "The #f0eae4 quote text painted on the dark perspective flip cards."),
    ("accent", "create-cta", "default", "backgroundColor", "action", ("--brand-accent", "--ring"),
     "The #fd5400 orange — Create Your Delphi, Expand, Send (matches --brand-accent/--ring/--chart-1/--bubble-accent)."),
    ("accent-fg", "create-cta", "default", "color", "action", ("--primary-foreground",),
     "White text on the orange accent."),
    ("dark-button", "dialog-google", "default", "backgroundColor", "action", ("--primary",),
     "The #21201c near-black fill on primary dialog actions (matches --primary)."),
    ("share", "share-btn", "default", "backgroundColor", "action", (),
     "The ~10% dark-ink fill on the profile Share pill."),
    ("hairline", "disc-card", "default", "borderTopColor", "border", (),
     "The ~12% ink hairline around cards and fields."),
    ("card-border", "srch-expert-card", "default", "borderTopColor", "border", ("--input",),
     "The ~20% ink border on result cards."),
    ("focus", "signin-btn", "focus-visible", "borderTopColor", "border", ("--ring", "--brand-accent"),
     "The orange focus-visible border on buttons (matches --ring/--brand-accent); cards take an ink outline instead."),
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
    ("badge", "srch-badge", "default", "The 10px uppercase credential badge (Pythia 600)."),
    ("xs", "chat-terms", "default", "The 12px terms/helper line under the composer."),
    ("sm", "m-signin", "default", "The 13px mobile sign-in link."),
    ("control", "signin-btn", "default", "The 14px pill-button, chip and nav-topic label."),
    ("body", "chat-name", "default", "The 16px body, card and profile text."),
    ("lg", "hero-search", "default", "The 18px ask fields, quotes and section headings."),
    ("section", "section-h2", "default", "The 20px marketing section heading."),
    ("mobile-display", "m-h1", "default", "The 32px mobile display size at 390px."),
    ("name", "exp-name", "default", "The 34px expert display name (Pythia 600)."),
    ("display", "hero-h1", "default", "The 50px Pythia display on home and discover."),
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
    ("badge", "srch-badge", "default", "borderTopLeftRadius", "The 6px credential-badge radius."),
    ("chip", "suggested-chip", "default", "borderTopLeftRadius", "The 18px suggested-question chip."),
    ("card-sm", "m-topic-card", "default", "borderTopLeftRadius", "The 20px mobile topic card and experience item."),
    ("card", "topic-card", "default", "borderTopLeftRadius", "The 24px topic/gallery card."),
    ("button", "create-cta", "default", "borderTopLeftRadius", "The 26px button/dialog radius — CTAs, dialog actions, expert cards, Share."),
    ("flip", "persp-flip", "default", "borderTopLeftRadius", "The 28px perspective flip card."),
    ("pill", "mic-btn", "default", "borderTopLeftRadius", "The full-pill (calc(infinity * 1px)) on round and topic buttons."),
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

sh = SPEC["core"].setdefault("shadow", {})
try:
    sh["dialog"] = lit(st("signin-dialog", "default")["boxShadow"], "other",
        "computed boxShadow of signin-dialog default (raw/components-computed.json)",
        "The layered shadow the sign-in dialog carries.")
except KeyError:
    pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
try:
    s = st("create-cta", "default")
    dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        mo["control"] = lit(f"{s.get('transitionProperty', 'all')} {dur} {ease or ''}".strip(), "other",
            "computed transition of create-cta default (raw/components-computed.json)",
            "The measured control transition.")
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("topbar-height", "mkt-header", "default", "h", "dimension", "The 64px public top bar."),
    ("logo-width", "mkt-logo", "default", "w", "dimension", "The 91.5px header wordmark."),
    ("search-field-width", "hero-search", "default", "w", "dimension", "The 624px hero ask field."),
    ("query-field-width", "srch-field", "default", "w", "dimension", "The 664px results query field."),
    ("dialog-width", "signin-dialog", "default", "w", "dimension", "The 448px sign-in dialog."),
    ("dialog-button-width", "dialog-google", "default", "w", "dimension", "The 400px dialog action."),
    ("topic-card-width", "topic-card", "default", "w", "dimension", "The ~347px topic card."),
    ("flip-card-width", "persp-card", "default", "w", "dimension", "The 272px perspective flip card."),
    ("expert-card-width", "srch-expert-card", "default", "w", "dimension", "The 672px search result card."),
    ("chat-input-width", "chat-input", "default", "w", "dimension", "The 592px composer field."),
    ("send-size", "chat-send", "default", "w", "dimension", "The 48px round send button."),
    ("scroll-pill", "scroll-bottom", "default", "w", "dimension", "The ~30px scroll-to-bottom pill."),
    ("portrait", "exp-portrait", "default", "w", "dimension", "The 110px expert portrait."),
    ("mobile-topbar-height", "m-header", "default", "h", "dimension", "The 64px phone top bar."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
