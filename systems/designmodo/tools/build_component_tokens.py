#!/usr/bin/env python3
"""Build raw/component-tokens.json — the token tree build_tokens.py
consumes — for designmodo.com.

designmodo.com declares almost nothing as custom properties (the resolved
set is Font Awesome widget internals only), so this tree is measured from
computed styles rather than declared variables:

  color/roles  the measured semantic layer — background.page/navy/card/
               field, text.ink/ink-body/app-ink/muted/on-dark, action
               accent/orange/blue/dark with their hover siblings
  fonts        InterVariable (the marketing face) and Fira Sans (the
               Postcards app face) with the measured weights
  type ramp    the measured font.size.measured.* roles, 91.5px display
               down to the 9px badges
  radii        5-12px app/product radii plus the 999px marketing pills
  shadow       the welcome-modal shadow
  motion       the 0.15-0.35s link/button transitions
  components   the measured dimensions under core.component.*
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
    "The token tree build_tokens.py turns into tokens.json. designmodo.com "
    "declares almost nothing in its stylesheets (raw/css-vars.json resolves "
    "to Font Awesome internals only), so the tree is measured from computed "
    "styles: theme-invariant font/radius/shadow/motion scales and component "
    "dimensions under core.* and the measured semantic roles under light.*. "
    "No public dark variant is declared or painted, so dark stays empty "
    "rather than invented."),
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
# InterVariable carries the marketing surface (nav, hero, pricing, forms);
# Fira Sans is the Postcards app face (sidebar, modal, gallery, badges).

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("ui", "nav-apps", "default", "InterVariable — the marketing face (nav, hero, pricing, forms)."),
    ("app", "modal-google", "default", "Fira Sans — the Postcards app face (sidebar, modal, gallery, badges)."),
]:
    try:
        fam[key] = lit(st(comp, state)["fontFamily"], "fontFamily",
            f"computed fontFamily of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, desc in [
    ("nav", "nav-apps", "The nav link weight."),
    ("cta", "openapp-cta", "The Open App CTA weight."),
    ("plan", "plan-cta", "The plan button weight."),
]:
    try:
        weights[key] = lit(st(comp, "default")["fontWeight"], "fontWeight",
            f"computed fontWeight of {comp} default (raw/components-computed.json)", desc)
    except KeyError:
        pass

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
JUNK = re.compile(r"^--(fa-|w-tc-editor|sweep|swiper|no-of-|website-|email-|variable-width|a$)")
for name in sorted(R):
    if R[name] != D.get(name) or is_scale_member(name) or CORE_HANDLED.match(name):
        continue
    if name.startswith("--font-weight-") or JUNK.match(name):
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
        if name in TWINS or JUNK.match(name):
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
        if name in TWINS or JUNK.match(name) or not (is_scale_member(name) or R[name] != D.get(name)):
            continue
        p = EMITTED.get(scale_rename(name)) or EMITTED.get(name)
        resolved = R[name] if theme == "light" else D[name]
        role_alias[theme].setdefault(norm_color(resolved), p)
    for name in sorted(R):
        if JUNK.match(name) or (R[name] == D.get(name) and not is_scale_member(name)):
            continue
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
    ("page", "site-footer", "default", "_body-bg", "background", (),
     "The white field the marketing surface paints (footer/section paint; #fff on the pricing tint)."),
    ("paper", "sidebar", "default", "_bg-app", "background", (),
     "The #f4f4f4 app canvas behind the gallery (the app shell's page paint)."),
    ("navy", "app-header", "default", "backgroundColor", "background", (),
     "The #071c26 dark navy app header band."),
    ("card", "plan-card", "default", "backgroundColor", "background", (),
     "The near-white plan/gallery card field (#f7f9fc at 90% over the pricing tint)."),
    ("card-face", "create-blank", "default", "_card-face", "background", (),
     "The #f4f6f7 dashed Create-Blank/AI card faces in the app gallery."),
    ("field", "login-email", "default", "backgroundColor", "background", (),
     "The white 380x50 form fields."),
    ("modal", "welcome-modal", "default", "backgroundColor", "background", (),
     "The white welcome-modal card."),
    ("secondary", "modal-create", "default", "backgroundColor", "action", (),
     "The #e8ecf0 secondary button fill (Create Account)."),
    ("ink", "pricing-h1", "default", "color", "text", (),
     "The #101d24 ink — headings, pricing text, plan features."),
    ("ink-body", "site-footer", "default", "color", "text", (),
     "The #313942 body ink on the marketing surface."),
    ("app-ink", "welcome-modal", "default", "color", "text", (),
     "The #2d3a41 app ink — modal copy, sidebar, gallery labels."),
    ("muted", "filter-industry", "default", "color", "text", (),
     "The #585d63 muted app label (filters, secondary text)."),
    ("muted-mkt", "seemore-link", "default", "color", "text", (),
     "The #c3cecb muted 'See more' link on the dark marketing strips."),
    ("on-dark", "mkt-header", "default", "color", "text", (),
     "White text painted on the dark hero/header regions."),
    ("accent", "openapp-cta", "default", "backgroundColor", "action", (),
     "The #27ae60 green — Open App, + Create, Login, Create Account, NEW badges."),
    ("accent-hover", "openapp-cta", "hover", "backgroundColor", "action", (),
     "The #1e8449 darker green on hover/pressed."),
    ("orange", "nav-signup", "default", "backgroundColor", "action", (),
     "The #f49a40 orange — the marketing Sign Up pill."),
    ("orange-hover", "nav-signup", "hover", "backgroundColor", "action", (),
     "The #f18110 deeper orange on hover/pressed."),
    ("blue", "app-login", "default", "backgroundColor", "action", (),
     "The #2198ed blue — the app Login pill and FREE badges."),
    ("blue-hover", "app-login", "hover", "backgroundColor", "action", (),
     "The #344a56 slate the app Login pill takes on hover/pressed."),
    ("auth-blue", "login-submit", "default", "backgroundColor", "action", (),
     "The #2f80ed blue on the /my-account/sign-in/ form's Login button."),
    ("auth-blue-hover", "login-submit", "hover", "backgroundColor", "action", (),
     "The #1366d6 deeper blue on the auth Login's hover/pressed."),
    ("slate", "app-signup", "default", "backgroundColor", "action", (),
     "The #485f6b slate on the app Sign Up button."),
    ("slate-hover", "app-signup", "hover", "backgroundColor", "action", (),
     "The #344a56 deeper slate on the app Sign Up's hover/pressed."),
    ("dark", "pc-cta", "default", "backgroundColor", "action", (),
     "The #0d1d24 near-black CTA on product pages (Sign-in with SSO shares it)."),
    ("dark-hover", "pc-cta", "hover", "backgroundColor", "action", (),
     "The #fb754b coral the product CTA flips to on hover/pressed."),
    ("link", "side-templates", "default", "color", "text", (),
     "The #2198ed link blue on the selected sidebar item."),
    ("hairline", "login-email", "default", "borderTopColor", "border", (),
     "The 1px #e0e5eb hairline on the auth fields."),
    ("focus", "pc-cta", "focus-visible", "outlineColor", "border", (),
     "The 2px #101d24 outline the product CTA takes on focus-visible."),
]:
    try:
        if prop == "_body-bg":
            raw = st(comp, state)["backgroundColor"]
            src = f"computed backgroundColor of {comp} {state}: the marketing surface paints white (raw/components-computed.json)"
        elif prop == "_bg-app":
            # No file in raw/ holds this: the recon read the app body background as
            # rgb(244,244,244) but that reading was never saved. Kept, labelled as typed.
            raw = "#f4f4f4"
            src = ("entered by hand at capture time, not measured: the recon's app body background "
                   "rgb(244,244,244) was never saved to raw/ (compare screenshots/app-*.png); recapture needed")
        elif prop == "_card-face":
            raw = next(pl["bg"] for pl in C[comp]["states"][state]["paint"] if pl.get("node", "").startswith("div.sc-hBxvHn") and pl.get("bg"))
            src = f"painted background of the div.sc-hBxvHn card face inside {comp} {state} (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        put_sem(sem, group, key, semcolor(raw, src, desc, prefer=prefer))
    except (KeyError, StopIteration):
        pass


# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("badge", "new-badge", "default", "The 9px badge size (NEW / FREE)."),
    ("filter", "filter-industry", "default", "The 13px app filter label."),
    ("control", "modal-google", "default", "The 15px app control size (modal buttons, sidebar items)."),
    ("ui", "nav-apps", "default", "The 15px marketing nav size."),
    ("body", "site-footer", "default", "The 16px body/footer text."),
    ("field", "login-email", "default", "The 17px form field text."),
    ("sub", "seemore-link", "default", "The 18px marketing secondary size."),
    ("product-cta", "pc-cta", "default", "The 20px product CTA."),
    ("section", "login-h1", "default", "The 24px form/section heading."),
    ("mobile-display", "m-h1", "default", "The 44px mobile hero size at 390px."),
    ("display", "hero-h1", "default", "The 56px marketing hero display."),
    ("tpl-display", "tpl-h1", "default", "The 63px gallery page display."),
    ("mega", "pricing-h1", "default", "The 91.5px pricing/product display."),
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
    ("form", "login-submit", "default", "borderTopLeftRadius", "The 5px auth button/field radius."),
    ("app", "app-login", "default", "borderTopLeftRadius", "The 6px app pill/button radius."),
    ("modal-btn", "modal-login", "default", "borderTopLeftRadius", "The 8px modal button radius."),
    ("product", "pc-cta", "default", "borderTopLeftRadius", "The 12px product CTA radius."),
    ("pill", "openapp-cta", "default", "borderTopLeftRadius", "The 999px marketing pill (Open App, Sign Up)."),
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
for name, comp, state, desc in [
    ("modal", "welcome-modal", "default",
     "The shadow the welcome modal casts over the dimmed gallery."),
    ("cta", "openapp-cta", "default",
     "The tinted lift the green CTAs carry (a deeper 0 6px 12px on hover/pressed)."),
    ("cta-hover", "openapp-cta", "hover",
     "The raised hover/pressed shadow on the green CTAs."),
    ("card", "plan-card", "default",
     "The plan-card elevation on the pricing strip."),
    ("badge-inset", "free-badge", "default",
     "The 1px inset line under the FREE/NEW badges."),
    ("field-focus", "login-email", "focused",
     "The blue glow a focused auth field paints."),
]:
    try:
        sh[name] = lit(st(comp, state)["boxShadow"], "other",
            f"computed boxShadow of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
try:
    s = st("openapp-cta", "default")
    dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        mo["control"] = lit(f"{s.get('transitionProperty', 'all')} {dur} {ease or ''}".strip(), "other",
            "computed transition of openapp-cta default (raw/components-computed.json)",
            "The measured control transition.")
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("topbar-height", "mkt-header", "default", "h", "dimension", "The 70px marketing top bar."),
    ("appbar-height", "app-header", "default", "h", "dimension", "The 60px navy app header."),
    ("sidebar-width", "sidebar", "default", "w", "dimension", "The 241px app workspace sidebar."),
    ("cta-height", "openapp-cta", "default", "h", "dimension", "The 53px Open App CTA."),
    ("plan-card-width", "plan-card", "default", "w", "dimension", "The 313px pricing plan card."),
    ("plan-cta-width", "plan-cta", "default", "w", "dimension", "The 233px plan action."),
    ("modal-width", "welcome-modal", "default", "w", "dimension", "The 423px welcome modal card."),
    ("modal-btn-width", "modal-google", "default", "w", "dimension", "The 343px modal action."),
    ("field-width", "login-email", "default", "w", "dimension", "The 380px auth field."),
    ("tpl-card-width", "tpl-card", "default", "w", "dimension", "The 266px template card."),
    ("tpl-card-height", "tpl-card", "default", "h", "dimension", "The 592px template card."),
    ("badge-height", "new-badge", "default", "h", "dimension", "The 14px NEW badge."),
    ("free-badge", "free-badge", "default", "w", "dimension", "The 43px FREE badge."),
    ("filter-height", "filter-industry", "default", "h", "dimension", "The 15px gallery filter label."),
    ("auth-submit-width", "login-submit", "default", "w", "dimension", "The 186px auth button pair."),
    ("mobile-topbar-height", "m-header", "default", "h", "dimension", "The 70px phone top bar."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# A component the last run could not find keeps its earlier states (measure.mjs marks it
# recaptureMissed and keeps the first run's page/run/url). Say so on every token read from it,
# so a kept reading never ships as if the latest run had confirmed it.
FLAGGED = {k: v["recaptureMissed"] for k, v in C.items() if v.get("recaptureMissed")}


def note_flagged(node):
    if isinstance(node, dict):
        src = node.get("source")
        if isinstance(src, str):
            for k, missed in FLAGGED.items():
                if re.search(rf"(?<![\w-]){re.escape(k)}(?![\w-])", src) and f"{k} was not found" not in src:
                    node["source"] = src = (src + f"; {k} was not found by the {missed} re-run (recaptureMissed),"
                                            " so this is the reading kept from the earlier run")
        for v in node.values():
            note_flagged(v)


note_flagged(SPEC)

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
