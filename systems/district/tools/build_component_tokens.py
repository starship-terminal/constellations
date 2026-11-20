#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

district.in ("District by Zomato") paints one product signed out: public
booking surfaces in the District Design System (DDS) — BeVietnamPro UI text,
PassengerSerif display type, and an attribute-scoped token layer —
:root/html[data-theme=light] and html[data-theme=dark] blocks carrying the
--color-<hue>-<step> scales (grey, purple, pink, blue, red, yellow, green,
ember, peach) plus --color-<role> semantics (background/surface/border/icon/
text/button/gradient/pastel/vivid/extended/overlay/switch/selection),
--font-<weight>, --font-size-*, --line-height-*, --space-*,
--typography-scale-* and --page-max-width vars over dds-* utilities.
Every theme-switching variable is emitted under both light.*
(data-theme=light) and dark.* (data-theme=dark) as a {"var": ...} leaf so
each theme resolves its own value; invariant names land under core.*.

The public pages paint light by default; the dark pass applies the product's
own html[data-theme=dark] attribute and repaints, so both role sets are
measured paint:

  light     #ffffff page (--color-background-primary), #131316 ink
            (--color-text-primary) and Book CTA
            (--color-button-primary-background), #f7f7f7 label
            (--color-button-primary-label), #eae5ff selected tab
            (--color-purple-100/--color-gradient-purple) with #231268
            label (--color-purple-800/--color-text-accent-purple),
            #545459 muted tabs (--color-text-secondary/--color-grey-500),
            black@8%/24% borders (--color-border-subtle/--color-border-intense),
            #1e1e20 footer (--color-grey-800), #6e52fa theme purple
  dark      #131316 page (--color-background-primary dark), #f7f7f7 ink
            (--color-text-primary dark), white@8% hairlines
            (--color-border-subtle dark)
  fonts     BeVietnamPro (UI text), PassengerSerif (display serif)
  ramp      measured 14/16/24/40px steps over declared
            --font-size-base..4xl and --typography-scale-*
  shape     6px filter chips, 8px mobile tabs, 12px Book CTA,
            9999px category tab pills
  motion    0.2s cubic-bezier(0.4,0,0.2,1) tab transition
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
    "The token tree build_tokens.py turns into tokens.json. district.in "
    "declares the District Design System in its stylesheets "
    "(raw/css-vars.json): theme-invariant scales under core.* and every "
    "theme-switching name — the --color-<hue>-<step> scales and the "
    "attribute-scoped semantics (--color-background-*/--color-surface-*/"
    "--color-border-*/--color-icon-*/--color-text-*/--color-button-*/"
    "--color-gradient-*) — emitted under both light.* (data-theme=light) "
    "and dark.* (data-theme=dark) so each theme resolves its own value. "
    "Both are real paint: light is the default render and dark is the "
    "forced html[data-theme=dark] pass. Measured roles alias to the "
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
# BeVietnamPro is the measured UI face (computed fontFamily of nav tabs and
# card titles); PassengerSerif is the served display serif (5 @font-face
# weights each in the harvest — display headings fall back to ui-sans-serif
# in the readings when the woff2 has not painted). Declared weights land in
# the generic --font-* loop below.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("ui", "nv-tab", "default", "BeVietnamPro — every UI string: tabs, cards, filters, prices."),
    ("display", None, None, "PassengerSerif — the served display serif (declared @font-face, weights 300-700; headings fall back to ui-sans-serif when it has not painted)."),
]:
    if comp and have(comp, state, "fontFamily"):
        fam[key] = {"value": st(comp, state)["fontFamily"], "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
    elif comp is None:
        fam[key] = {"value": "PassengerSerif", "type": "fontFamily",
                    "source": "declared @font-face in the served stylesheets (raw/css-vars.json)",
                    "description": desc}

# --------------------------------------------------- declared scales (core)
#
# Theme-invariant names land here; every theme-switching name is emitted
# per-theme below. Scale families (Tailwind 11-step hue palettes) are emitted
# per-theme even when a step happens to resolve identically, so each theme's
# scale stays complete.

SCALE_FAMS = {"black-alpha", "blue", "ember", "green", "grey",
              "orange", "peach", "pink", "purple", "red", "white-alpha",
              "yellow", "pastel", "vivid"}

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
        fam, prop = rest, "other"
        for suffix, key in (
            ("-font-size", "fontSize"), ("-font-weight", "fontWeight"),
            ("-line-height", "lineHeight"), ("-letter-spacing", "letterSpacing"),
        ):
            if rest.endswith(suffix):
                fam, prop = rest[: -len(suffix)], key
                break
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
    r"font-primary-|font-width-|font-|line-height-|typography-scale-|page-max-width|safe-area-|swiper-|weight-|display-lg|"
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

# ---- light roles (measured on /, /movies/, /events/, /events/comedy,
# the artist and ticket pages — every public surface paints data-theme=light)
sem = SPEC["light"]
for key, comp, state, prop, group, prefer, desc in [
    ("page", "nv-bar", "default", "_page", "background", ("--color-background-primary",),
     "The white field every public page paints (matches --color-background-primary)."),
    ("ink", "nv-search", "default", "color", "text", ("--color-text-primary", "--color-grey-900", "--color-theme-black"),
     "The #131316 ink on headings, prices and body text (matches --color-text-primary)."),
    ("muted", "nv-tab", "default", "color", "text", ("--color-text-secondary", "--color-grey-500"),
     "The #545459 muted ink on inactive category tabs (matches --color-text-secondary/--color-grey-500)."),
    ("on-accent", "nv-tab-active", "default", "color", "text", ("--color-text-accent-purple", "--color-purple-800"),
     "The #231268 deep-purple label on the selected tab (matches --color-text-accent-purple/--color-purple-800)."),
    ("primary", "tk-book", "default", "backgroundColor", "action", ("--color-button-primary-background", "--color-grey-900", "--color-theme-black"),
     "The #131316 Book-tickets CTA (matches --color-button-primary-background)."),
    ("on-primary", "tk-book", "default", "_ctaLabel", "action", ("--color-button-primary-label", "--color-grey-50"),
     "The #f7f7f7 label on the Book CTA (matches --color-button-primary-label)."),
    ("selected", "nv-tab-active", "default", "backgroundColor", "background", ("--color-purple-100", "--color-gradient-purple"),
     "The #eae5ff selected category-tab fill (matches --color-purple-100/--color-gradient-purple)."),
    ("hairline", "nv-bar", "default", "borderBottomColor", "border", ("--color-border-subtle", "--color-black-alpha-8"),
     "The black@8% hairline under the app bar (matches --color-border-subtle)."),
    ("chip-line", "mv-chip", "default", "borderBottomColor", "border", ("--color-border-intense", "--color-black-alpha-24"),
     "The black@24% filter-chip border (matches --color-border-intense)."),
    ("footer", "ft-bar", "default", "backgroundColor", "background", ("--color-grey-800",),
     "The #1e1e20 sitemap footer slab (matches --color-grey-800)."),
]:
    try:
        if prop == "_page":
            # No light-pass element reports the page field; read the declared role the
            # pages paint it with, not a screenshot pixel.
            raw = R["--color-background-primary"]
            src = ("declared --color-background-primary (raw/css-vars.json resolved.light); no computed reading "
                   "of the light page field (seen in screenshots/home-default.png)")
        elif prop == "_ctaLabel":
            raw = C[comp]["states"][state]["textStyle"]["color"]
            src = f"computed label colour of {comp} {state} (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        put_sem(sem, group, key, semcolor(raw, src, desc, prefer=prefer, dest=group + "." + key))
    except KeyError:
        pass

# ---- dark roles (measured on a forced html[data-theme=dark] pass — the
# attribute the product's own theme layer resolves)
sem2 = SPEC["dark"]
for key, comp, state, prop, group, prefer, desc in [
    ("page", "dk-body", "default", "backgroundColor", "background", ("--color-background-primary",),
     "The #131316 field the pages repaint under data-theme=dark (matches --color-background-primary dark)."),
    ("nav", "dk-nav", "default", "backgroundColor", "background", ("--color-background-primary", "--color-grey-900"),
     "The #131316 nav bar under dark."),
    ("hairline", "dk-nav", "default", "borderBottomColor", "border", ("--color-border-subtle", "--color-white-alpha-8"),
     "The white@8% hairline under the dark app bar (matches --color-border-subtle dark)."),
    ("ink", "dk-nav", "default", "_darkink", "text", ("--color-text-primary", "--color-grey-50"),
     "The #f7f7f7 ink the dark theme paints on its text roles (matches --color-text-primary dark)."),
    ("card", "dk-card", "default", "backgroundColor", "surface", ("--color-surface-primary",),
     "The card surface under dark (transparent over the #131316 field here)."),
]:
    try:
        if prop == "_darkink":
            raw = st(comp, state)["color"]
            src = f"computed color of {comp} {state}, the repainted nav ink under data-theme=dark (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        put_sem(sem2, group, key, semcolor(raw, src, desc, theme="dark", prefer=prefer, dest=group + "." + key))
    except KeyError:
        pass

# ------------------------------------------------------------- type ramp

# Components whose selector caught another element in the 2026-11 run (the
# README's Known gaps; the capture script is fixed by edit, not yet re-run).
# A token read from one says so, so a wrong-element reading never ships as the
# component it is named for.
# Each is flagged only while its reading still shows the fault, so a good
# recapture clears it.
def _rect(k):
    return C[k]["states"]["default"].get("rect") or {}


_OFFSCREEN = lambda k: _rect(k).get("x", 0) + _rect(k).get("w", 0) <= 0
WRONG_ELEMENT = {k: what for k, what, bad in [
    ("mv-h1", "an off-screen carousel slide title, not the listing heading", _OFFSCREEN),
    ("ev-h1", "an off-screen carousel slide title, not the listing heading", _OFFSCREEN),
    ("cm-h1", "an off-screen carousel slide title, not the listing heading", _OFFSCREEN),
    ("cm-filter", "the 632x500 sort dropdown panel, not a filter control", lambda k: _rect(k).get("h", 0) >= 200),
    ("at-book", "the same show card as at-show, not a booking control", lambda k: "at-show" in C and _rect(k) == _rect("at-show")),
] if k in C and bad(k)}

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("label", "nv-tab", "default", "The 14px tab, chip and price-adjacent label."),
    ("body", "mc-title", "default", "The 16px card title and body text."),
    ("price", "ev-price", "default", "The 16px bold price line."),
    ("section", "tk-h1", "default", "The 24px section/ticket heading."),
    ("display", "ev-h1", "default", "The 40px listing display heading."),
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
    ("chip", "mv-chip", "default", "borderTopLeftRadius", "The 6px filter-chip radius."),
    ("tab-mobile", "m-tab", "default", "borderTopLeftRadius", "The 8px mobile tab radius."),
    ("cta", "tk-book", "default", "borderTopLeftRadius", "The 12px Book-tickets CTA radius."),
    ("pill", "nv-tab", "default", "borderTopLeftRadius", "The 9999px category-tab pill radius."),
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

# The artist-page show-card badge is the one painted shadow found on the
# public surfaces (the paint walk's second layer on at-show/at-book); the
# declared --shadow-* utilities above are the rest of the elevation evidence.
try:
    _badge_shadow = C["at-show"]["states"]["default"]["paint"][1]["shadow"]
    SPEC["core"].setdefault("shadow", {})["badge"] = lit(
        _badge_shadow, "other",
        "paint layer of the artist-page show-card badge (raw/components-computed.json)",
        "The show-card badge's painted shadow — a 4px drop at 25% black; every other public reading reported transparent or none.")
except (KeyError, IndexError, TypeError):
    pass
# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
for key, comp in [("control", "nv-tab"), ("chip", "mv-chip"), ("cta", "tk-book")]:
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
    ("nav-bar", "nv-bar", "default", "h", "dimension", "The 75px app top bar."),
    ("nav-mark", "nv-mark", "default", "w", "dimension", "The 108x44 District mark."),
    ("category-tab", "nv-tab", "default", "w", "dimension", "The 84x36 category tab pill."),
    ("search", "nv-search", "default", "w", "dimension", "The 28x28 search affordance."),
    ("movie-card", "mc-card", "default", "w", "dimension", "The 197x348 movie card."),
    ("artist-card", "ar-card", "default", "w", "dimension", "The 190x222 circular artist card."),
    ("venue-card", "ev-card", "default", "w", "dimension", "The 236x325 venue/event card."),
    ("filter-chip", "mv-chip", "default", "w", "dimension", "The 56x32 filter chip."),
    ("footer", "ft-bar", "default", "h", "dimension", "The ~410px sitemap footer."),
    ("book-cta", "tk-book", "default", "w", "dimension", "The 163x52 Book-tickets button."),
    ("show-card", "at-show", "default", "w", "dimension", "The 296x544 artist-page show card."),
    ("mobile-bar", "m-bar", "default", "w", "dimension", "The 390x60 phone app bar."),
    ("mobile-card", "m-card", "default", "w", "dimension", "The 364x272 phone content card."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

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
