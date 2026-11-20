#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

family.co is one public surface signed out: the marketing home, /blog +
/blog/<post>, /changelog, /support + /support/<article>, /faqs, /legal,
/docs, /docs/connectkit and /docs/family-account, plus the app.family.co
login ("Aave Account"), which shares the product's token layer. Two declared
layers are captured (raw/css-vars.json for the styled-components marketing
sheets, raw/app-css-vars.json for the app's Next.js chunks):

  marketing   a small role layer in Display-P3 — --body/--body-muted/
              --heading inks, --blue/--orange/--beige/--gray-light/--white/
              --twitter-blue/--grey brand fills, the --graphic-* gradients,
              --app-*, --color-* surface roles, --focus, --font,
              --h-pad/--nh-pad/--gap/--scrollbar-* layout values
  app         the product token layer — --family-*/--primary-*/
              --danger-*/--valid-*/--warning-* 100-800 scales, the --wallet-*
              palette, --body-*/--overlay-*/--input-*/--icon-*/--selection-*/
              --hyperlink-*/--hr-*/--logo-*/--focus-* roles, --duration-*/
              --ease-* motion, --font-*, --z-*, --border-*/--shadow-*/
              --padding-*, --txn-speed-*/--otp-*/--qr-*/--skeleton-*/
              --token-picker-* component values

Every public surface paints the light theme signed out; the marketing sheet
declares no theme switch, but the app's chunks declare a real
[data-theme="dark"] theme the login never paints (38 switching names —
--body-*/--input-*/--overlay-*/--icon-*/--selection-* …). Theme-invariant
names land under core.*: colour-valued names under core.color.<path> and the
rest at their natural dashed path (with a `declared.` prefix when the top
segment would collide with a generated group). Switching names are emitted
under both light.* and dark.* as {var} leaves, and the light set carries the
measured roles, which alias the declared values they match.

Measured computed styles from raw/components-computed.json (the light
surface; there is no other theme):

  light       a #171717 ink (--heading) on white, #5e5e5e/#6e6e6e muted
              copy (--body-muted), a #2f69e3 blue accent on the Download on
              iOS pill and link text (--blue), a near-black Get Started
              pill, a #e7e1d5 beige Log In pill (--beige), translucent
              hairlines and the #f6f7f9 app input field
  fonts       the marketing stack (system sans via --font) and Inter on the
              app surface (--font-primary); SF Pro Rounded / Nunito is the
              declared secondary stack, SF Mono the code stack
"""

import json, math, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
AV = json.loads((RAW / "app-css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())["components"]
# R is the merged resolved light layer (marketing under the app's — the two
# sets do not collide on names); RRES keeps each name's resolution kind. D is
# the same under [data-theme="dark"]: the app declares a dark theme the login
# never paints; the marketing sheet declares no theme attribute, so its dark
# pass re-resolves the same values.
RRES = {**V.get("resolved", {}).get("light", {}), **AV.get("resolved", {}).get("light", {})}
DRES = {**V.get("resolved", {}).get("dark", {}), **AV.get("resolved", {}).get("dark", {})}
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RRES.items()}
D = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in DRES.items()}
SWITCHING = {n for n in R if n in D and D[n] != R[n]}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. family.co and "
    "the app.family.co login declare their token layers in their "
    "stylesheets (raw/css-vars.json, raw/app-css-vars.json): the marketing "
    "role layer and the app's --family-*/--wallet-*/--overlay-* product "
    "layer. Theme-invariant names land under core.*; names the app switches "
    "under [data-theme=\"dark\"] are emitted under both light.* and dark.* "
    "as {var} leaves — the dark theme is declared, never painted while "
    "signed out. Measured roles under light.* alias the declared values "
    "where they match."),
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


def painted(comp, state, key):
    """A reading from the kit's paint list — the layers actually painted
    (rounded children, pseudo-elements, shadows) rather than the wrapper's
    computed style, which is often an unpainted positioning box. An entry
    whose recorded size matches the element's own rect wins."""
    c = C[comp]["states"][state]
    entries = [p for p in c.get("paint") or [] if p.get(key)]
    if not entries:
        raise KeyError(key)
    rect = c.get("rect") or {}
    for p in entries:
        m = re.fullmatch(r"([\d.]+)x([\d.]+)", str(p.get("size") or ""))
        if m and abs(float(m.group(1)) - rect.get("w", -9)) <= 1.5 and abs(float(m.group(2)) - rect.get("h", -9)) <= 1.5:
            return p[key]
    return entries[0][key]


def ancestor(comp, state, key):
    """A reading from the kit's ancestor list (a painted wrapper above the
    element — a field's rounded shell)."""
    c = C[comp]["states"][state]
    for a in c.get("ancestors") or []:
        if a.get(key) not in (None, ""):
            return a[key]
    raise KeyError(key)


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
    """Write `leaf` at name's dashed path under `root` (the variable name
    minus its -- prefix, split on -). When a leaf and a group must share a
    node, the leaf moves inside the group under the first free of `default`,
    `base`, `self` — never silently overwriting tokens."""
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
            raise ValueError(f"{name}: no free key to hold the leaf beside its group {path}")
    else:
        if last in node:
            raise ValueError(f"duplicate token path {path}")
        node[last] = leaf
    EMITTED[name] = path
    _OWNER[path] = name


def emitted_path(name):
    return EMITTED[name]


DECL_SRC = "declared design-system variable in the site or app stylesheet (raw/css-vars.json, raw/app-css-vars.json)"


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
# The marketing stack (system sans via --font) carries the public site; the
# app surface carries Inter through --font-primary. SF Pro Rounded / Nunito
# is the declared secondary stack and SF Mono the declared code stack — both
# recorded under font.family from the app's declarations.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("display", "hero-h1", "default", "The proprietary \"Family\" display face — every page title, hero and section heading."),
    ("ui", "nav-developers", "default", "The marketing/UI stack — nav labels, buttons and body copy (Inter with system fallbacks)."),
    ("app", "login-field", "default", "The app surface's variable Inter — the login card and its field."),
]:
    if have(comp, state, "fontFamily"):
        v = ts(comp, state, "fontFamily")
        fam[key] = {"value": v, "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
# Declared app stacks: --font-secondary (SF Pro Rounded / Nunito) and
# --font-code (SF Mono) land at font.family.secondary / font.family.code.
for name in sorted(k for k in R if re.fullmatch(r"--font-(primary|secondary|code|body|inter)", k)):
    key = name[len("--font-"):]
    if key in fam:
        continue
    fam[key] = lit(R[name], "fontFamily",
                   f"{DECL_SRC}: {name}", f"The declared `{name}` stack.")
    EMITTED[name] = f"font.family.{key}"

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
# Only the weights actually painted signed out are exported: the Family
# display face and the controls all paint 500, the kickers/entry headings
# 600 — nothing paints 700.
for key, comp, desc in [
    ("regular", "feature-body", "400 — body and feature copy."),
    ("medium", "nav-developers", "500 — nav labels, control text and the Family display headings."),
    ("semibold", "feature-label", "600 — feature labels/kickers and entry headings; the heaviest weight painted signed out."),
]:
    try:
        w = int(float(ts(comp, "default", "fontWeight")))
        weights[key] = lit(w, "fontWeight",
                           f"computed fontWeight of {comp} default (raw/components-computed.json)", desc)
    except (KeyError, TypeError, ValueError):
        pass

# --------------------------------------------------- declared layer (core)
#
# A declared name's resolution kind picks its group: colours under
# core.color.<dashed path>, durations under core.duration.*, easings under
# core.easing.*, font families under font.family.*, lengths under
# core.size.<path> (radius-named ones under core.radius.*), shadows under
# core.shadow.*, z indices under core.zIndex.*; anything else at its natural
# dashed path, prefixed `declared.` when the top segment would collide with
# a generated group (the marketing --font stack, the --border-* roles).

RESERVED = {"font", "color", "size", "radius", "duration", "easing", "motion",
            "shadow", "zindex", "breakpoint", "tracking", "component",
            "measured", "weight", "lineheight", "spacing", "layout", "border",
            "background", "text", "action", "surface", "foreground", "input",
            "palette", "grid", "typography", "other"}

colors = SPEC["core"].setdefault("color", {})
color_alias = {}   # normalized colour -> 'color.<path>' for aliasing


def _place(node, parts, leaf, gprefix=()):
    """Write `leaf` at parts' nested path under `node`, demoting a leaf that
    a group must share a node with under `default`/`base`/`self`. Returns the
    final dotted path. `gprefix` is the group chain the caller already
    descended, so EMITTED/_OWNER (full dotted paths) stay correct when a
    leaf is demoted."""
    base = []
    for p in parts[:-1]:
        nxt = node.get(p)
        if nxt is None:
            nxt = node[p] = {}
        elif _leaf(nxt):
            prefix = ".".join(tuple(gprefix) + tuple(base) + (p,))
            owner = _OWNER.pop(prefix, None)
            nxt = node[p] = {"default": nxt}
            if owner:
                EMITTED[owner] = prefix + ".default"
                _OWNER[prefix + ".default"] = owner
        node = nxt
        base.append(p)
    path = ".".join(base + [parts[-1]])
    if parts[-1] in node and not _leaf(node[parts[-1]]):
        for key in ("default", "base", "self"):
            if key not in node[parts[-1]]:
                node[parts[-1]][key] = leaf
                path = ".".join(base + [parts[-1], key])
                break
        else:
            raise ValueError(f"{'.'.join(tuple(gprefix) + tuple(parts))}: no free key to hold the leaf beside its group")
    else:
        if parts[-1] in node:
            raise ValueError(f"duplicate token path {path}")
        node[parts[-1]] = leaf
    return path


# The marketing --color-<x> surface roles and the app's shorter --<x> twins
# carry different values (--color-primary #343433 ink vs --primary #9896ff
# violet). When both exist they cannot share color.<x>, so each keeps its
# own origin group: color.marketing.<x> for --color-*, color.app.<x> for
# the app's short names.
TWIN = {}
for _n in R:
    if _n.startswith("--color-") and ("--" + _n[len("--color-"):]) in R:
        TWIN[_n] = "marketing"
        TWIN["--" + _n[len("--color-"):]] = "app"


def target(name):
    """The (group chain, parts) a declared var lands at — under core for
    theme-invariant names, or under each theme set for switching ones.
    Returns (groups, parts): groups is the leading group list, parts the
    nested keys below it."""
    parts = name[2:].split("-")
    kind = (RRES.get(name) or {}).get("kind")
    if parts[0] == "color":
        parts = parts[1:]
    if COLOR_V.fullmatch(str(R.get(name, D.get(name, ""))).strip()):
        if name in TWIN:
            return ("color", [TWIN[name]] + parts)
        return ("color", parts)
    if kind == "dimension" and re.search(r"radius|rounded", name):
        return ("radius", parts[1:] if parts[0] == "radius" and len(parts) > 1 else parts)
    if kind == "duration":
        return ("duration", parts[1:] if parts[0] == "duration" and len(parts) > 1 else parts)
    if kind == "easing":
        return ("easing", parts[1:] if parts[0] == "ease" and len(parts) > 1 else parts)
    if kind == "fontFamily":
        return (("font", "family"), ["marketing"] if parts == ["font"] else (parts[1:] if parts[0] == "font" else parts))
    if kind == "shadow":
        return ("shadow", parts[1:] if parts[0] == "shadow" and len(parts) > 1 else parts)
    if name.startswith("--z-"):
        return ("zIndex", parts[1:])
    if kind == "dimension":
        return ("size", parts)
    return ([], ["declared"] + parts if parts[0].lower() in RESERVED else parts)


def leaf_type(name):
    kind = (RRES.get(name) or DRES.get(name) or {}).get("kind")
    v = str(R.get(name, D.get(name, ""))).strip()
    if COLOR_V.fullmatch(v):
        return "color"
    if kind == "duration":
        return "duration"
    if kind == "easing":
        return "cubicBezier"
    if kind == "fontFamily":
        return "fontFamily"
    if kind == "shadow":
        # A resolved box-shadow is a raw CSS string; the DTCG "shadow" type
        # wants parsed layer objects, so declared shadows ride as "other"
        # (they still group under core.shadow.* via target()).
        return "other"
    if kind == "dimension":
        return "dimension"
    return "other"


for name in sorted(R):
    if name in EMITTED:
        continue
    groups, parts = target(name)
    if isinstance(groups, str):
        groups = (groups,)
    ty = leaf_type(name)
    if name in SWITCHING:
        # A var the app's [data-theme="dark"] rules change: emitted under both
        # theme sets so each resolves its own declared value.
        path = None
        for setname in ("light", "dark"):
            node = SPEC[setname]
            for g in groups:
                node = node.setdefault(g, {})
            p = _place(node, parts, var(name, ty), groups)
            path = path or p
        EMITTED[name] = ".".join(tuple(groups) + tuple(path.split("."))) if path else ".".join(tuple(groups) + tuple(parts))
        continue
    node = SPEC["core"]
    for g in groups:
        node = node.setdefault(g, {})
    value = R[name]
    leaf = lit(value, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")
    p = _place(node, parts, leaf, groups)
    full = ".".join(tuple(groups) + tuple(p.split(".")))
    EMITTED[name] = full
    _OWNER[full] = name
    if groups == ("color",) and leaf["type"] == "color":
        color_alias.setdefault(norm_color(value), full)

# Dark-only declarations: names the app's [data-theme="dark"] rules set
# that have no light counterpart land under dark alone.
for name in sorted(set(D) - set(R)):
    groups, parts = target(name)
    if isinstance(groups, str):
        groups = (groups,)
    node = SPEC["dark"]
    for g in groups:
        node = node.setdefault(g, {})
    p = _place(node, parts, var(name, leaf_type(name)), groups)
    EMITTED[name] = ".".join(tuple(groups) + tuple(p.split(".")))

# ------------------------------------------------------- measured roles
#
# Measured on the one light surface both sites paint; roles alias the
# declared values they match.

role_alias = dict(color_alias)


def var_path(tree, name, prefix=""):
    """The dotted path of the leaf that resolves `name` in a spec tree, read from the tree
    itself (a demoted leaf lives under .default)."""
    for k, v in tree.items():
        if not isinstance(v, dict) or k.startswith("_"):
            continue
        here = f"{prefix}.{k}" if prefix else k
        if v.get("var") == name:
            return here
        if "var" not in v and "value" not in v:
            hit = var_path(v, name, here)
            if hit:
                return hit
    return None


TRANSPARENT = re.compile(r"transparent|rgba\(\s*\d+,\s*\d+,\s*\d+,\s*0(\.0+)?\s*\)")


def semcolor(raw, src, desc, prefer=()):
    """Alias to a preferred declared name when it resolves to this colour."""
    for p in prefer:
        if p in R and norm_color(R[p]) == norm_color(raw):
            path = EMITTED.get(p)
            if path:
                return lit(f"{{{path}}}", "color", src + f"; matches declared {p}", desc)
    alias = role_alias.get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


def put_sem(root, group, key, leaf):
    node = root.setdefault(group, {})
    node[key] = leaf


sem = SPEC["light"]
for key, comp, state, prop, group, prefer, desc in [
    ("page", "mkt-header", "default", "_body-bg", "background", ("--white", "--color-background", "--background"),
     "The white field the whole public surface paints."),
    ("card", "tweet-card", "default", "backgroundColor", "background", ("--white",),
     "The white testimonial card field (matches --white)."),
    ("field", "login-field", "default", "backgroundColor", "background", ("--input-background",),
     "The app input paints transparent over the card; the field fill it sits on is the declared light.color.input.background.default."),
    ("ink", "hero-h1", "default", "color", "text", ("--heading",),
     "The near-black ink on headings and body text (matches --heading)."),
    ("muted", "feature-body", "default", "color", "text", ("--body-muted", "--body"),
     "The muted body-copy colour (matches --body-muted/--body)."),
    ("low", "blog-date", "default", "color", "text", (),
     "The low-emphasis meta text on post dates."),
    ("kicker", "feature-label", "default", "color", "text", (),
     "The coloured feature label/kicker text."),
    ("on-dark", "download-cta", "default", "color", "text", ("--white",),
     "White text on the dark/blue buttons."),
    ("accent", "download-cta", "default", "backgroundColor", "action", ("--overlay-background", "--heading"),
     "The near-black pill fill on the primary CTAs (Download on iOS, Get Started) — matches the app's declared --overlay-background #171717."),
    ("beige", "login-btn", "default", "paint:bg", "action", (),
     "The warm beige pill fill on the secondary actions (the header Log In, the hero's Watch the Video) — #f6f4ef; the declared --beige #e7e1d5 is a deeper cream nothing sampled paints."),
    ("hairline", "blog-card", "default", "borderBottomColor", "border", ("--gray-light",),
     "The bottom hairline under cards and list items (matches --gray-light)."),
    ("field-border", "login-field", "default", "borderTopColor", "border", ("--input-color", "--border-light"),
     "The app input is borderless (0px); the recorded colour is the inherited text colour."),
    ("focus", "nav-developers", "focus-visible", "outlineColor", "border", ("--focus", "--focus-color"),
     "The marketing focus-visible ring (matches --focus #848281; the app draws a blue --focus-color rgba(0,122,255,.5) ring)."),
]:
    try:
        if prop == "_body-bg":
            raw = "#ffffff"
            src = "the public surfaces paint a white field (screenshots/*-light-*.png; --color-background resolves #fff)"
        elif prop == "paint:bg":
            raw = painted(comp, state, "bg")
            src = f"the painted background of {comp}'s layer {state} (raw/components-computed.json paint list)"
        elif prop == "color":
            # The first text node's reading: a wrapper's own colour is what
            # children inherit, not what the visible text paints.
            raw = ts(comp, state, "color")
            if not raw:
                raise KeyError(prop)
            src = f"computed color of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if TRANSPARENT.fullmatch(norm_color(raw)):
            # A transparent reading paints nothing: never commit it as a fill. Take the declared
            # role the element sits on when there is one, else leave the role out.
            found = next(((d, var_path(SPEC["light"], d)) for d in prefer if var_path(SPEC["light"], d)), None)
            if not found:
                continue
            decl, where = found
            put_sem(sem, group, key, lit(f"{{{where}}}", "color",
                    f"declared {decl}; {comp} {state} itself paints {prop} transparent (raw/components-computed.json)", desc))
            continue
        put_sem(sem, group, key, semcolor(raw, src, desc, prefer=prefer))
    except KeyError:
        pass

# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
size_alias = {}
for key, comp, state, desc in [
    ("xs", "blog-date", "default", "The small meta/date line."),
    ("sm", "faq-item", "default", "The FAQ item copy."),
    ("control", "nav-developers", "default", "The nav/button label size."),
    ("body", "feature-body", "default", "The body/feature copy size."),
    ("lg", "login-field", "default", "The app field and larger body size."),
    ("section", "feature-h2", "default", "The marketing section heading."),
    ("article", "post-h1", "default", "The article title size."),
    ("mobile-display", "m-h1", "default", "The mobile display size at 390px."),
    ("display", "hero-h1", "default", "The hero display size."),
]:
    # Prefer the kit's first-text-node reading (textStyle): a wrapper's own
    # fontSize is what children inherit, not what the visible text paints —
    # the FAQ item's shell is 16px over 19px copy.
    raw = ts(comp, state, "fontSize")
    if not raw:
        continue
    src = f"computed fontSize of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
    alias = size_alias.get(raw)
    ty.setdefault("measured", {})[key] = lit(f"{{{alias[0]}}}" if alias else raw, "dimension",
                  src + (f"; matches declared {alias[1]}" if alias else ""), desc)

# ------------------------------------------------------------------ shape

radii = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("field", "login-field", "default", "ancestor:radius", "The app input's painted shell radius — the input itself is borderless; its wrapper draws the rounded fill."),
    ("card", "tweet-card", "default", "borderTopLeftRadius", "The testimonial card radius (post cards sit flat on hairlines)."),
    ("item", "faq-item", "default", "borderTopLeftRadius", "The FAQ item radius — flat rows on hairlines."),
    ("button", "getstarted-btn", "default", "borderTopLeftRadius", "The pill button radius — Get Started, Download on iOS, Log In."),
]:
    try:
        if prop == "ancestor:radius":
            v = ancestor(comp, state, "radius")
            src = f"the painted radius of {comp}'s wrapper ancestor {state} (raw/components-computed.json)"
        else:
            v = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        mnum = re.match(r"[\d.eE+-]+", v)
        if mnum and float(mnum.group(0)) > 9999 and "px" in v:
            v = "calc(infinity * 1px)"
        radii[key] = lit(v, "dimension" if re.fullmatch(r"[0-9.]+(px|rem)", v or "") else "other", src, desc)
    except (KeyError, AttributeError):
        pass

# ------------------------------------------------------------- elevation

sh = SPEC["core"].setdefault("shadow", {})
try:
    # Named demo-overlay, not overlay: the declared --overlay-*-shadow
    # variables already landed under core.shadow.overlay.*.
    sh["demo-overlay"] = lit(st("demo-overlay", "default")["boxShadow"], "other",
        "computed boxShadow of demo-overlay default (raw/components-computed.json)",
        "The video overlay's own boxShadow — none; it dims the page with an 80% scrim layer instead.")
except KeyError:
    pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
try:
    s = st("getstarted-btn", "default")
    dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        mo["control"] = lit(f"{s.get('transitionProperty', 'all')} {dur} {ease or ''}".strip(), "other",
            "computed transition of getstarted-btn default (raw/components-computed.json)",
            "The measured control transition.")
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("topbar-height", "mkt-header", "default", "h", "dimension", "The public top bar height."),
    ("logo-width", "mkt-logo", "default", "w", "dimension", "The header wordmark width."),
    ("faq-toggle", "faq-toggle", "default", "w", "dimension", "The 14px FAQ collapse toggle."),
    ("search-field-width", "sup-search", "default", "w", "dimension", "The support search field width."),
    ("control-height", "download-cta", "default", "h", "dimension", "The 48px CTA pill height — Download on iOS, Get Started."),
    ("login-field-width", "login-field", "default", "w", "dimension", "The app login field width."),
    ("login-field-height", "login-field", "default", "h", "dimension", "The app login field height."),
    ("login-card-width", "login-card", "default", "w", "dimension", "The Aave Account login card."),
    ("post-card-width", "blog-card", "default", "w", "dimension", "A post card on /blog."),
    ("mobile-topbar-height", "m-header", "default", "h", "dimension", "The phone top bar height."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

if __name__ == "__main__":
    (RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
    print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
