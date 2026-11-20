#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

discord.com signs two products into one site. The marketing pages
(/, /download, /nitro) are a Webflow build in Ggsans / ABC Ginto over the
brand palette — the blurple gradient hero, white pill buttons, the dark
#1a1a1e plan cards. The app surfaces (/servers discovery, a /servers/<slug>
detail, /login, /register) run the real Discord design system: "gg sans"
body text, "ABC Ginto Discord Nord" display type, and a class-scoped token
layer — :root hue scales (--neutral-1..100, --blurple-1..100, --plum-0..26,
the --*-new-1..100 families, --illo-*-10..70, --opacity-*, --brand-*,
--primary-*, --chart-*) plus .theme-light/.theme-darker/.theme-dark/
.theme-midnight semantic blocks (--background-base-*/--background-surface-*/
--background-mod-*, --text-*/--header-*, --border-*, --badge-*, --button-*,
--input-*, --control-*, --status-*, --interactive-*). Colour vars arrive as
hsl()/rgba()/oklab(); build_tokens.py normalises them to hex. Every
theme-switching variable is emitted under both light.* (.theme-light) and
dark.* (.theme-darker) as a {"var": ...} leaf so each theme resolves its
own value; invariant names land under core.*.

Measured computed styles from raw/components-computed.json — the app
surfaces paint .theme-dark.theme-darker signed out, so the app roles are
measured dark paint; the marketing chrome inside them sits under a
.theme-light root and the marketing pages paint their own palette, so the
marketing roles are measured light paint:

  app dark    #121214/#202024 base fields (--background-base-*), #202024
              card bodies with rgba(151,151,159,0.12) hairlines, #efeff1
              ink (--text-normal), #fbfbfb strong, #5865f2 blurple
              (--blurple-50/--brand-experiment) on Join/Log In, #4752c4
              hover, rgba(151,151,159,0.16) selected pill fill
              (--background-mod-normal), rgba(151,151,159,0.12) chip fill
              (--background-mod-subtle), #43b581 online green, 2px #6aa8f4
              focus rings, oklab #26282c auth card
  marketing   blurple-gradient hero, white pill nav/login CTAs,
              #5865f2 Open-Discord button, #1a1a1e Nitro plan card
  fonts       gg sans (app UI), ABC Ginto Discord Nord (display),
              Ggsans / Abcgintodiscord (marketing), gg mono (declared)
  ramp        measured 14/16/18/20/24/28/31/56px steps
  shape       3px fields, 8px cards/auth, 10px chips, 12px pills/CTAs,
              16px nav pill, 40px marketing buttons, 96px nitro card
  shadow      auth card rgba(0,0,0,0.2) 0 2px 10px; nitro card
              rgba(69,42,124,0.1) 0 2px 32px
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
    "The token tree build_tokens.py turns into tokens.json. discord.com "
    "declares its design-token layer in its stylesheets "
    "(raw/css-vars.json): theme-invariant scales under core.* and every "
    "theme-switching name — the :root hue scales and the class-scoped "
    "semantics (--background-base-*, --text-*, --header-*, --border-*, "
    "--badge-*, --button-*, --input-*) — emitted under both light.* "
    "(.theme-light) and dark.* (.theme-darker) so each theme resolves its "
    "own value. Both classes paint signed out — the app surfaces carry "
    ".theme-dark.theme-darker while the marketing chrome inside them sits "
    "under .theme-light — so both resolutions are painted evidence. "
    "hsl()/rgba()/oklab() colour vars are normalised to hex. Measured "
    "roles alias to the declared values where they match."),
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


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\)|color\([^)]*\)|\d+(?:\.\d+)?\s+[\d.]+%\s+[\d.]+%(?:\s*/\s*[\d.]+%?)?)")


def decl_color(name):
    v = R[name]
    ty = "color" if COLOR_V.fullmatch(str(v).strip()) else "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


# ------------------------------------------------------------------- fonts
#
# The app paints two faces: "gg sans" for every UI string and "ABC Ginto
# Discord Nord" for display headings (the DISCOVERABLE SERVERS and server
# names). The marketing build loads its own Ggsans/Abcgintodiscord faces
# (Webflow naming). gg mono is the declared code face.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc, src_fn in [
    ("ui", "sc-name", "default", "\"gg sans\" — every app string: card names, counts, fields, buttons.", st),
    ("display", "ds-h1", "default", "ABC Ginto Discord Nord — the display headings (DISCOVERABLE SERVERS, server names).", ts),
    ("marketing", "nt-card", "default", "Ggsans — the Webflow marketing face (the card's own computed fontFamily; its nested heading is Nord).", st),
    ("marketing-display", "mk-lede", "default", "Abcgintodiscord — the marketing hero lede and CTA labels.", ts),
]:
    if have(comp, state, "fontFamily"):
        v = src_fn(comp, state)["fontFamily"] if src_fn is st else ts(comp, state, "fontFamily")
        fam[key] = {"value": v, "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
faces = {f.get("font-family", "").strip('"') for f in V.get("fonts") or []}
if "gg mono" in faces:
    fam["mono"] = {"value": "\"gg mono\", \"Source Code Pro\", monospace", "type": "fontFamily",
                   "source": "declared @font-face in the site stylesheet (raw/css-vars.json); not exercised on any measured public component",
                   "description": "gg mono — the declared code face."}

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, desc in [
    ("regular", "sc-members", "400 — member counts, fields, descriptions."),
    ("medium", "ds-tab", "500 — category pills, Join CTA, nav links."),
    ("semibold", "sc-name", "600 — server names, auth headings."),
    ("bold", "ds-h1", "700 — the display headings."),
]:
    try:
        w = int(float(ts(comp, "default", "fontWeight")))
        weights[key] = lit(w, "fontWeight",
                           f"computed fontWeight of {comp} default (raw/components-computed.json)", desc)
    except (KeyError, TypeError, ValueError):
        pass

# --------------------------------------------------- declared scales (core)
#
# Theme-invariant names land here; every theme-switching name is emitted
# per-theme below. Scale families (Tailwind 11-step hue palettes) are emitted
# per-theme even when a step happens to resolve identically, so each theme's
# scale stays complete.

SCALE_FAMS = {"black", "blue", "blue-new", "blurple", "brand",
              "brand-experiment", "chart-categorical", "chart-mono",
              "chart-mono-text", "green", "green-new", "hypesquad-house",
              "illo-blue", "illo-green", "illo-orange", "illo-pink",
              "illo-purple", "illo-yellow", "neutral", "orange",
              "orange-new", "pink", "plum", "primary", "red", "red-new",
              "teal", "teal-new", "white", "yellow", "yellow-new",
              "opacity", "opacity-black", "opacity-blue", "opacity-blurple",
              "opacity-green", "opacity-orange", "opacity-pink",
              "opacity-red", "opacity-teal", "opacity-white",
              "opacity-yellow"}

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

size_alias = {}    # 'NNpx'/'Nrem' -> ('font.size.<key>', '--var'); discord has no
                   # declared type scale — the measured ramp below is the source

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

CORE_HANDLED = re.compile(
    r"^--(color-|leading-|tracking-|container-|breakpoint-|radius-|"
    r"duration-|ease-|animate-|blur-|z-|default-|drop-shadow-|shadow-|"
    r"font-weight-|space-|size-|elevation-|custom-status-emoji-height|"
    r"custom-emoji|font-size-|font-display-|font-code-|font-headline-|"
    r"font-primary-|font-width-|line-height-|weight-|display-lg|"
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
# The app surfaces paint .theme-dark.theme-darker signed out, so their roles
# land in dark.* (real measured dark paint). The marketing pages and the
# marketing chrome inside the app pages paint light (Ggsans + the Webflow
# palette), so their roles land in light.* (real measured light paint).
# .theme-light's own app surface is declared but unpainted signed out — a
# documented boundary; the light roles below are the marketing evidence.

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

def layer(comp, state, where, node):
    """The background of the first painted layer (paint or ancestors) whose node starts with `node`."""
    return next(n["bg"] for n in C[comp]["states"][state].get(where) or [] if n.get("bg") and n.get("node", "").startswith(node))


# ---- marketing light roles (measured on /, /download, /nitro and the
# .theme-light marketing chrome inside the app pages)
sem = SPEC["light"]
for key, comp, state, prop, group, prefer, desc in [
    ("page", "dl-cta", "default", "_mktpage", "background", ("--white",),
     "The white field the light marketing pages (/download, /nitro) paint."),
    ("ink", "mk-nav", "default", "color", "text", ("--not-quite-black", "--black"),
     "The black ink of the marketing nav text."),
    ("ink-inverse", "mk-h1", "default", "color", "text", ("--white", "--always-white"),
     "The white display ink over the blurple hero (matches --white)."),
    ("primary", "mk-cta-open", "default", "backgroundColor", "action", ("--blurple", "--brand-experiment", "--blurple-50"),
     "The #5865f2 blurple on the Open-Discord CTA (matches --blurple/--blurple-50)."),
    ("on-primary", "mk-cta-open", "default", "color", "action", ("--white", "--always-white"),
     "The white label on the blurple CTA."),
    ("nav-pill", "mk-nav-login", "default", "backgroundColor", "action", ("--white", "--always-white"),
     "The white nav Log-In pill on the blurple chrome."),
    ("card", "nt-card", "default", "backgroundColor", "background", ("--dark-charcoal", "--not-quite-black"),
     "The #1a1a1e dark Nitro plan card on the light page."),
    ("focus", "mk-nav-login", "focus-visible", "outlineColor", "border", ("--blurple", "--brand-experiment", "--blurple-50"),
     "The 2px #5865f2 focus-visible outline on the nav pill (4px offset)."),
]:
    try:
        if prop == "_mktpage":
            # No measured element reports the page field (every /download and /nitro
            # reading is transparent over it), so this is a screenshot sample.
            raw = "#ffffff"
            src = ("sampled, not measured: the white field of /download and /nitro read off "
                   "screenshots/download-default.png and nitro-default.png; no computed reading of the page field")
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        put_sem(sem, group, key, semcolor(raw, src, desc, prefer=prefer, dest=group + "." + key))
    except (KeyError, StopIteration):
        pass

# ---- app dark roles (measured on /servers, /servers/<slug>, /login,
# /register — all painted .theme-dark.theme-darker signed out)
sem2 = SPEC["dark"]
for key, comp, state, prop, group, prefer, desc in [
    ("page", "sc-card", "default", "_apppage", "background", ("--background-base-lowest",),
     "The #121214 base field the app surfaces paint (matches --background-base-lowest)."),
    ("card", "sc-card", "default", "_cardbody", "background", ("--background-base-low",),
     "The #202024 card body fill with its rgba(151,151,159,0.12) hairline (matches --background-base-low)."),
    ("panel", "lg-card", "default", "backgroundColor", "background", ("--background-surface-high", "--background-base-low"),
     "The oklab #26282c auth card on the brand backdrop."),
    ("field", "lg-pass", "default", "_fieldfill", "background", ("--background-base-lowest",),
     "The black@12% input fill inside the auth card."),
    ("ink", "sc-card", "default", "color", "text", ("--text-default", "--neutral-5"),
     "The #efeff1 body ink across the app surfaces (matches --text-default)."),
    ("strong", "sc-name", "default", "color", "text", ("--header-primary", "--text-strong"),
     "The #fbfbfb strong ink on names and headings."),
    ("muted", "lg-card", "default", "color", "text", ("--text-muted",),
     "The muted ink on card descriptions and field labels (matches --text-muted)."),
    ("link", "lg-forgot", "default", "color", "text", ("--text-link", "--text-brand"),
     "The oklab blue on the Forgot-password/Register links (matches --text-link)."),
    ("primary", "lg-submit", "default", "backgroundColor", "action", ("--blurple", "--brand-experiment", "--blurple-50", "--background-brand"),
     "The #5865f2 blurple on Join and Log In (matches --blurple-50/--brand-experiment)."),
    ("primary-hover", "sv-join", "hover", "backgroundColor", "action", (),
     "The #4752c4 blurple darkens on hover."),
    ("on-primary", "lg-submit", "default", "color", "action", ("--neutral-1", "--white-500", "--white"),
     "The white label on the blurple buttons (matches --neutral-1)."),
    ("selected", "ds-tab-all", "default", "backgroundColor", "background", ("--background-mod-normal",),
     "The rgba(151,151,159,0.16) selected category-pill fill (matches --background-mod-normal)."),
    ("chip", "sv-chip", "default", "backgroundColor", "background", ("--background-mod-subtle",),
     "The rgba(151,151,159,0.12) chip fill on server categories (matches --background-mod-subtle)."),
    ("online", "sc-members", "default", "_online", "text", ("--status-positive", "--green-new-60"),
     "The #43b581 green of the Online presence dot."),
    ("hairline", "lg-submit", "default", "borderTopColor", "border", ("--border-subtle", "--app-frame-border"),
     "The rgba(255,255,255,0.08) hairline on the auth submit (matches --border-subtle)."),
    ("card-line", "ds-tab-all", "default", "borderTopColor", "border", (),
     "The rgba(151,151,159,0.12) hairline on cards and the selected pill."),
    ("focus", "ds-tab", "focus-visible", "outlineColor", "border", ("--focus-primary",),
     "The 2px #6aa8f4 focus-visible ring on app controls (2px offset)."),
]:
    try:
        # Paint layers are picked by the element that paints them, never by the colour
        # they are expected to have, and a missing layer drops the role (no typed fallback).
        if prop == "_apppage":
            # No measured element reports the app page field; the declared base the
            # app paints it with is read instead of a screenshot pixel.
            raw = D["--background-base-lowest"]
            src = ("declared --background-base-lowest (raw/css-vars.json resolved.dark); no computed reading "
                   "of the app page field (seen in screenshots/servers-default.png)")
        elif prop == "_cardbody":
            raw = layer(comp, state, "paint", "article.guildItemContainer")
            src = f"painted article.guildItemContainer card body inside {comp} {state} (raw/components-computed.json)"
        elif prop == "_fieldfill":
            raw = layer(comp, state, "ancestors", "div.wrapper_")
            src = f"painted div.wrapper field layer over {comp} {state} (raw/components-computed.json)"
        elif prop == "_online":
            raw = layer("sc-card", "default", "paint", "div.dotOnline")
            src = "painted div.dotOnline presence dot inside sc-card default (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        put_sem(sem2, group, key, semcolor(raw, src, desc, theme="dark", prefer=prefer, dest=group + "." + key))
    except (KeyError, StopIteration):
        pass

# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("label", "sc-members", "default", "The 14px member counts and descriptions."),
    ("body", "sc-card", "default", "The 16px card body, pills and fields."),
    ("lede", "mk-lede", "default", "The 20px hero lede and CTA labels."),
    ("card-title", "lg-h1", "default", "The 24px auth card heading."),
    ("section", "sv-name", "default", "The 28px server name."),
    ("display-mobile", "m-h1", "default", "The 31px display at 390px."),
    ("display", "ds-h1", "default", "The 56px DISCOVERABLE SERVERS display."),
    ("display-marketing", "mk-h1", "default", "The 56px marketing hero display."),
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
    ("field", "ds-search-input", "default", "borderTopLeftRadius", "The 3px tight radius on the search input element."),
    ("card", "lg-card", "default", "borderTopLeftRadius", "The 8px auth card / server-card radius."),
    ("chip", "sv-chip", "default", "borderTopLeftRadius", "The 10px category-chip radius."),
    ("control", "ds-tab", "default", "borderTopLeftRadius", "The 12px category pill / Join CTA / search box radius."),
    ("nav-pill", "mk-nav-login", "default", "borderTopLeftRadius", "The 16px marketing nav pill radius."),
    ("hero-card", "nt-card", "default", "borderTopLeftRadius", "The 96px rounded slab of the Nitro plan card."),
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

# Two real shadows on the public surface: the auth card's rgba(0,0,0,0.2)
# 0 2px 10px and the Nitro plan card's rgba(69,42,124,0.1) 0 2px 32px.
# Everything else reports boxShadow: none.
sh = SPEC["core"].setdefault("shadow", {})
try:
    s_ = st("lg-card", "default")
    m = re.search(r"rgba\(0, 0, 0, 0\.2\)\s+(\S+)\s+(\S+)\s+(\S+)", s_.get("boxShadow", ""))
    if m:
        sh["card"] = lit([{"offsetX": m.group(1), "offsetY": m.group(2), "blur": m.group(3), "spread": "0px", "color": "rgba(0, 0, 0, 0.2)"}], "shadow",
            "computed boxShadow of lg-card default (raw/components-computed.json)",
            "The auth card's 0 2px 10px rgba(0,0,0,0.2) shadow.")
except KeyError:
    pass
try:
    s_ = st("nt-card", "default")
    m = re.search(r"rgba\(69, 42, 124, 0\.1\)\s+(\S+)\s+(\S+)\s+(\S+)", s_.get("boxShadow", ""))
    if m:
        sh["nitro-card"] = lit([{"offsetX": m.group(1), "offsetY": m.group(2), "blur": m.group(3), "spread": "0px", "color": "rgba(69, 42, 124, 0.1)"}], "shadow",
            "computed boxShadow of nt-card default (raw/components-computed.json)",
            "The Nitro plan card's 0 2px 32px rgba(69,42,124,0.1) shadow.")
except KeyError:
    pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
for key, comp in [("control", "sv-join"), ("auth", "lg-submit"), ("pill", "ds-tab")]:
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
    ("marketing-nav", "mk-nav", "default", "h", "dimension", "The 80px marketing top bar."),
    ("nav-pill", "mk-nav-login", "default", "w", "dimension", "The 80x39 white nav Log-In pill."),
    ("hero-cta", "mk-cta-open", "default", "w", "dimension", "The 324x65 Open-Discord CTA."),
    ("hero-cta-download", "mk-cta-download", "default", "w", "dimension", "The 262x65 Download button."),
    ("search", "ds-search", "default", "w", "dimension", "The 640x64 discovery search box."),
    ("category-pill", "ds-tab", "default", "w", "dimension", "The ~146x57 Gaming category pill."),
    ("server-card", "sc-card", "default", "w", "dimension", "The 322x362 discoverable-server card."),
    ("server-icon", "sc-icon", "default", "w", "dimension", "The ~51x51 squircle server icon."),
    ("join-cta", "sv-join", "default", "w", "dimension", "The 320x48 brand-fill Join button."),
    ("share", "sv-share", "default", "w", "dimension", "The 320x44 Share button."),
    ("chip", "sv-chip", "default", "w", "dimension", "The ~122x38 category chip."),
    ("auth-card", "lg-card", "default", "w", "dimension", "The 784x414 sign-in card."),
    ("auth-field", "lg-email", "default", "w", "dimension", "The 414x44 auth field."),
    ("auth-submit", "lg-submit", "default", "w", "dimension", "The 416x40 Log In submit."),
    ("qr-panel", "lg-qr", "default", "w", "dimension", "The 240x322 QR-code panel."),
    ("nitro-card", "nt-card", "default", "w", "dimension", "The 590x683 Nitro plan card."),
    ("mobile-bar", "m-bar", "default", "w", "dimension", "The 342x64 phone marketing bar."),
    ("mobile-card", "m-card", "default", "w", "dimension", "The 358x380 phone server card."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
