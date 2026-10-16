#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from chatgpt.com on 2026-10-17 (the redesigned shell):
  raw/css-vars.json            every custom property the stylesheets declare, and `computed`: the
                               value each root-level name takes on <html> in dark and light, as the
                               browser resolved it (a colour as one sRGB value, a length in px, a
                               shadow as computed), plus the reduced-motion rules, the z-index and
                               grid declarations and the Tailwind utility counts (tools/capture/vars.mjs)
  raw/components-computed.json computed styles per component and state (measure.mjs): the focus
                               ring, the accent button's hover and pressed fills, the z-index each
                               layer actually takes, the border widths in use

Since the 2026-10 redesign ChatGPT's own names are semantic and themed by `data-theme`, so the
semantic sets mostly keep the product's names (`--color-text-secondary` is `text.secondary`) and a
`role` group points the checklist's roles (page, surface, raised, overlay, scrim; text primary to
link; border default, strong, focus; accent default, hover, pressed; status fill, text and border)
at them. Values are the computed ones; a token is an alias only where its role points at another
token with the same value in that theme.

Sets:
  core   theme-independent: the fixed colour ramps (`--blue-*`, `--gray-fixed-*`, ...), font families
         and weights, the type scale and the named type styles as composite typography, spacing (the
         unit and the steps the pages use), radii, border widths, control and icon sizes, the focus
         ring, durations and easings, breakpoints, containers, layout widths and z-index layers.
  light, dark
         the semantic palette (bg, surface, text, border, ring, variant, chatAccent, content, chart,
         status), the theme-flipping grey ramp, shadows, `role` and `component` (measured component
         values, aliased to a token where one matches).

Every token carries `$extensions.source`. Values DTCG cannot carry are listed under the set's
`$extensions.notTokenised`. Deterministic: same inputs, same bytes.
"""
import json, pathlib, re
from collections import OrderedDict

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
MEAS = json.loads((RAW / "components-computed.json").read_text())["components"]
C = V["computed"]
PROBE = C["page"]
RAWV = {"dark": C["dark"]["raw"], "light": C["light"]["raw"]}
RES = {"dark": C["dark"]["resolved"], "light": C["light"]["resolved"]}
READ = V["readAt"]

NOT = {"core": [], "dark": [], "light": []}


def src(name, theme=None):
    where = f"on <html> in {theme}" if theme else "on <html>, the same in both themes"
    return f"Measured: css-var {name}, computed {where} ({PROBE} copy, {READ})"


def tok(value, typ, source, **ext):
    e = {"source": source}
    e.update(ext)
    return {"$value": value, "$type": typ, "$extensions": e}


def put(tree, path, node):
    parts = path.split(".")
    for p in parts[:-1]:
        tree = tree.setdefault(p, OrderedDict())
    tree[parts[-1]] = node


def color(name, theme):
    """The resolved colour: the canvas gives #rrggbb or rgba() for sRGB colours and passes oklab()
    through, which canon() converts."""
    r = RES[theme].get(name)
    return canon(r["value"]) if r and r["kind"] == "color" else None


def dim(name, theme="dark"):
    r = RES[theme].get(name)
    if not r or r["kind"] != "dimension":
        return None
    v = r["value"]
    return "%gpx" % round(float(v[:-2]), 3)


def raw(name, theme="dark"):
    return RAWV[theme].get(name)


def same(name):
    return RES["dark"].get(name) == RES["light"].get(name) and RAWV["dark"].get(name) == RAWV["light"].get(name)


def names(rx):
    return sorted(n for n in RAWV["dark"] if re.search(rx, n))


def natkey(s):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


def oklab_rgb(L, a, b):
    """OKLab to 8-bit sRGB (Björn Ottosson's matrices), so a colour Chromium reports as oklab()
    (every color-mix(in oklab, ...)) compares with the canvas-resolved token values."""
    l_, m_, s_ = L + 0.3963377774 * a + 0.2158037573 * b, L - 0.1055613458 * a - 0.0638541728 * b, L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    lin = (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s, -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)
    enc = lambda x: 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055
    return [max(0, min(255, round(enc(max(0.0, x)) * 255))) for x in lin]


def canon(c):
    """A computed colour (rgb()/rgba()/oklab()) in the token form (#rrggbb or rgba(r, g, b, a))."""
    m = re.fullmatch(r"oklab\((-?[\d.e-]+) (-?[\d.e-]+) (-?[\d.e-]+)(?: / ([\d.]+))?\)", c or "")
    if m:
        r, g, b = oklab_rgb(*(float(x) for x in m.groups()[:3]))
        a = m.group(4)
        c = "rgba(%d, %d, %d, %s)" % (r, g, b, a) if a is not None and float(a) != 1 else "rgb(%d, %d, %d)" % (r, g, b)
    m = re.fullmatch(r"rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)", c or "")
    if not m:
        return c
    r, g, b, a = m.groups()
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%s, %s, %s, %s)" % (r, g, b, "%g" % float(a))


def shadow_layers(v):
    """A computed box-shadow ('rgba(0, 0, 0, 0.2) 0px 1px 2px -1px, ...') as DTCG shadow objects."""
    out = []
    for part in re.split(r",(?![^(]*\))", v):
        m = re.fullmatch(r"\s*(rgba?\([^)]*\)|#[0-9a-f]+) (-?[\d.]+px) (-?[\d.]+px) (-?[\d.]+px) (-?[\d.]+px)( inset)?\s*", part)
        if not m:
            return None
        col = canon(m.group(1))
        if col.startswith("rgba(") and col.endswith(", 0)"):
            continue
        layer = {"color": col, "offsetX": m.group(2), "offsetY": m.group(3), "blur": m.group(4), "spread": m.group(5)}
        if m.group(6):
            layer["inset"] = True
        out.append(layer)
    return out


core, sets = OrderedDict(), {"dark": OrderedDict(), "light": OrderedDict()}

# ---------------------------------------------------------------- colour ramps
# Fixed ramps (the same in both themes) go to core; `--gray-*` and `--color-gray-*` flip with the
# theme (gray-0 is #0d0d0d in dark, #ffffff in light), so they stay in each theme set.
RAMP = re.compile(r"^--(gray-fixed|blue|green|red|orange|yellow|purple|pink|cyan|teal|lime|magenta|slate|indigo|brown|gold)-(\d+)$")
ramps = {}
for n in RAWV["dark"]:
    m = RAMP.match(n)
    if m and color(n, "dark") and same(n):
        ramps.setdefault(m.group(1), []).append((int(m.group(2)), n))
for hue in sorted(ramps, key=lambda h: (h != "gray-fixed", h)):
    for step, n in sorted(ramps[hue]):
        put(core, f"color.{hue}.{step}", tok(color(n, "dark"), "color", src(n)))
for theme in sets:
    for n in names(r"^--gray-\d+$"):
        put(sets[theme], f"gray.{n.split('-')[-1]}", tok(color(n, theme), "color", src(n, theme)))

# ---------------------------------------------------------------- type
FAM = {"sans": "--font-sans", "mono": "--font-mono", "serif": "--font-serif"}
for k, n in FAM.items():
    v = raw(n)
    if v:
        put(core, f"fontFamily.{k}", tok([x.strip().strip('"') for x in v.split(",")], "fontFamily", src(n)))
oai = [f for f in V["fonts"] if "OpenAI Sans" in f.get("font-family", "")]
if oai:
    weights = sorted({w for f in oai for w in f.get("font-weight", "").split()})
    put(core, "fontFamily.openai-sans", tok(["OpenAI Sans", "-apple-system", "system-ui", "sans-serif"], "fontFamily",
        f"Measured: @font-face 'OpenAI Sans' declared {len(oai)} times (weights {', '.join(weights)}), served by OpenAI; no measured element uses it in this capture (the sidebar wordmark is the system stack at 600); the fallbacks are the stack --font-sans starts with", licence="proprietary (OpenAI); not committed"))
for n in names(r"^--font-weight-[a-z]+$"):
    put(core, f"fontWeight.{n[14:]}", tok(int(raw(n)), "fontWeight", src(n)))
for n in sorted(names(r"^--text-(3xs|2xs|xs|sm|base|lg|xl|2xl|3xl|4xl|5xl|6xl)$"), key=lambda x: ["3xs", "2xs", "xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl"].index(x[7:])):
    put(core, f"fontSize.{n[7:]}", tok(dim(n), "dimension", src(n)))
    lh = raw(n + "--line-height")
    m = lh and re.fullmatch(r"calc\(([\d.]+) / ([\d.]+)\)", lh)
    if m:
        put(core, f"lineHeight.{n[7:]}", tok(round(float(m.group(1)) / float(m.group(2)), 4), "number", src(n + "--line-height") + "; the ratio calc() divides"))


def em_px(em, size_px):
    m = re.fullmatch(r"(-?[\d.]*)em", em.strip())
    return "%gpx" % round(float(m.group(1)) * size_px, 3) if m else None


# The named styles: --font-{heading,text,small-caps}-<size>-{size,line-height,weight,tracking}.
ROLE_DESC = {"heading": "heading", "text": "body text", "small-caps": "small caps label"}
for fam in ("heading", "text", "small-caps"):
    sizes = sorted({re.match(rf"^--font-{fam}-([a-z0-9]+)-size$", n).group(1) for n in names(rf"^--font-{fam}-[a-z0-9]+-size$")},
                   key=lambda s: ["3xs", "2xs", "xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "5xl"].index(s) if s in ["3xs", "2xs", "xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "5xl"] else 99)
    for s in sizes:
        b = f"--font-{fam}-{s}-"
        size = dim(b + "size")
        px = float(size[:-2])
        tr = raw(b + "tracking") or "0em"
        ls = em_px(tr, px) if tr.endswith("em") else dim(b + "tracking")
        v = {"fontFamily": "{fontFamily.sans}", "fontSize": size, "lineHeight": dim(b + "line-height"), "fontWeight": int(raw(b + "weight")), "letterSpacing": ls or "0px"}
        put(core, f"typography.{fam}-{s}", tok(v, "typography", f"Measured: css-vars {b}size, -line-height, -weight and -tracking computed on <html> ({PROBE}, {READ}); letter spacing {tr} worked out in px at the style's size (Derived)"))
# Single-size product styles that carry a line height and weight of their own.
for key in ("card-title", "control-label", "form-title", "form-body", "onboarding-title", "onboarding-body", "onboarding-label", "unread-badge", "2xs", "3xs", "5xl", "6xl"):
    n = f"--text-{key}"
    if not raw(n):
        continue
    size = dim(n)
    if not size:
        continue
    lh = raw(n + "--line-height")
    lhv = dim(n + "--line-height") if lh and not lh.startswith("calc(") else None
    m = lh and re.fullmatch(r"calc\(([\d.]+) / ([\d.]+)\)", lh)
    if m:
        lhv = "%gpx" % round(float(size[:-2]) * float(m.group(1)) / float(m.group(2)), 3)
    w = raw(n + "--font-weight")
    v = {"fontFamily": "{fontFamily.sans}", "fontSize": size, "lineHeight": lhv or size, "fontWeight": int(w) if w and w.isdigit() else 400, "letterSpacing": "0px"}
    trk = raw(n + "--letter-spacing")
    if trk:
        v["letterSpacing"] = em_px(trk, float(size[:-2])) if trk.endswith("em") else (dim(n + "--letter-spacing") or "0px")
    put(core, f"typography.{key}", tok(v, "typography", f"Measured: css-var {n} with its --line-height, --font-weight and --letter-spacing where declared ({PROBE}, {READ}); a missing line height is the size, a missing weight 400 (Derived)"))
# Code: the mono stack at the markdown code size, measured on the code block.
cb = MEAS.get("code-block", {}).get("states", {}).get("default", {})
ts = cb.get("textStyle")
if ts:
    put(core, "typography.code", tok({"fontFamily": "{fontFamily.mono}", "fontSize": ts["fontSize"], "lineHeight": ts["lineHeight"] if ts["lineHeight"].endswith("px") else ts["fontSize"], "fontWeight": int(ts["fontWeight"]), "letterSpacing": "0px"}, "typography",
        f"Measured: computed style of the code in the thread's code block ({cb.get('snapshot')}, dark)"))
NOT["core"] += [{"name": n, "value": raw(n), "why": "tracking keyword the stylesheets set to `normal`"} for n in names(r"^--font-tracking-")]

# ---------------------------------------------------------------- spacing
unit = dim("--spacing")
put(core, "spacing.unit", tok(unit, "dimension", src("--spacing") + "; Tailwind's base unit, every p-N, m-N and gap-N is N times it"))
steps = {}
for k, u in V["classUse"].items():
    m = re.fullmatch(r"-?(?:p|px|py|pt|pb|pl|pr|ps|pe|m|mx|my|mt|mb|ml|mr|ms|me|gap|gap-x|gap-y|space-x|space-y)-(\d+(?:\.\d+)?)", k)
    if m:
        s = steps.setdefault(m.group(1), {"elements": 0, "utilities": set(), "pages": 0})
        s["elements"] += u["elements"]
        s["utilities"].add(k)
        s["pages"] = max(s["pages"], u["pages"])
U = float(unit[:-2])
for step in sorted(steps, key=float):
    s = steps[step]
    if s["elements"] < 10:
        continue
    put(core, f"spacing.{step.replace('.', '_')}", tok("%gpx" % (float(step) * U), "dimension",
        f"Derived: {step} x spacing.unit; {s['elements']} elements across the {len(V['pages'])} page copies use it ({', '.join(sorted(s['utilities'])[:6])})", elements=s["elements"]))
for n in names(r"^--(control-gutter|spacing-token|thread-gutter|dialog-container-inner-padding|modal-container-inner-padding|input-gap)"):
    d = dim(n)
    if d and same(n):
        put(core, f"spacing.named.{n[2:]}", tok(d, "dimension", src(n)))

# ---------------------------------------------------------------- shape
for n in names(r"^--radius-(?!.*-base$)"):
    d = dim(n)
    if d and same(n):
        put(core, f"radius.{n[9:]}", tok(d, "dimension", src(n)))
for n in names(r"^--control-radius-"):
    put(core, f"radius.control-{n[17:]}", tok(dim(n), "dimension", src(n)))
put(core, "borderWidth.hairline", tok(dim("--border-width-hairline"), "dimension", src("--border-width-hairline") + "; the dropdown and popover rings (--dropdown-overlay-ring-width, --popover-overlay-ring-width) are this width too"))
bw = {}
for key, c in MEAS.items():
    for st, s in c.get("states", {}).items():
        for side in ("Top", "Right", "Bottom", "Left"):
            w = (s.get("style") or {}).get(f"border{side}Width")
            if w and w != "0px" and (s.get("style") or {}).get(f"border{side}Style") != "none":
                bw.setdefault(w, set()).add(key)
for w in sorted(bw, key=lambda x: float(x[:-2])):
    nm = {"0.5px": "hairline-measured", "1px": "default", "2px": "strong"}.get(w, w.replace(".", "_"))
    put(core, f"borderWidth.{nm}", tok(w, "dimension", f"Measured: computed border width on {len(bw[w])} measured components ({', '.join(sorted(bw[w])[:5])})"))
u1 = sum(u["elements"] for k, u in V["classUse"].items() if re.fullmatch(r"border(-[trblxyse])?", k))
if u1:
    core["borderWidth"]["default"]["$extensions"]["utilityCount"] = f"{u1} elements carry Tailwind's 1px `border` utilities across the page copies"

# ---------------------------------------------------------------- sizing
for n in names(r"^--control-size-"):
    put(core, f"size.control.{n[15:]}", tok(dim(n), "dimension", src(n)))
for n in names(r"^--control-icon-size-"):
    put(core, f"size.icon.{n[20:]}", tok(dim(n), "dimension", src(n)))
for n in names(r"^--control-font-size-"):
    put(core, f"size.control-font.{n[20:]}", tok(dim(n), "dimension", src(n)))
for n in names(r"^--height-token-|^--height-toolbar"):
    d = dim(n)
    if d:
        put(core, f"size.height.{n[2:].replace('height-token-', '')}", tok(d, "dimension", src(n)))
# The focus ring, as the focus-visible readings draw it: a box-shadow ring (Tailwind's ring-2 with a
# 0px offset ring), an outline on the element, or an outline on its ::after.
rings = {}
for key, c in MEAS.items():
    for st, s in c.get("states", {}).items():
        if not st.endswith("focus-visible") or "style" not in s or st.startswith("light"):
            continue
        y = s["style"]
        found = None
        m = re.search(r"(rgb\([^)]*\)) 0px 0px 0px ([1-9][\d.]*px)( inset)?", y.get("boxShadow", ""))
        if m:
            found = ("box-shadow ring" + (" (inset)" if m.group(3) else ""), m.group(2), "0px", canon(m.group(1)))
        elif y.get("outlineStyle") == "solid" and float(y.get("outlineWidth", "0px")[:-2] or 0) > 0:
            found = ("outline", y["outlineWidth"], y["outlineOffset"], canon(y["outlineColor"]))
        else:
            for p in s.get("paint") or []:
                mm = re.fullmatch(r"([\d.]+px) solid (rgb\([^)]*\)) offset (-?[\d.]+px)", p.get("outline") or "")
                if mm and p["node"].endswith("::after"):
                    found = ("outline on ::after", mm.group(1), mm.group(3), canon(mm.group(2)))
                    break
            if not found and y.get("outlineStyle") == "auto":
                found = ("browser default (outline: auto)", y["outlineWidth"], y["outlineOffset"], canon(y["outlineColor"]))
        if found:
            rings.setdefault(found, []).append(key)
        else:
            rings.setdefault(("none visible", "0px", "0px", "-"), []).append(key)
if rings:
    drawn = {k: v for k, v in rings.items() if k[0] not in ("none visible",) and not k[0].startswith("browser")}
    (kind, w, off, col), who = max(drawn.items(), key=lambda kv: len(kv[1]))
    total = sum(len(v) for v in rings.values())
    put(core, "size.focusRing.width", tok(w, "dimension", f"Measured: the {kind} that {len(who)} of the {total} focus-visible readings draw (dark), e.g. {', '.join(who[:4])}; colour {col} (ring.default)"))
    put(core, "size.focusRing.offset", tok(off, "dimension", f"Measured: the offset of that ring on the same {len(who)} readings"))
    core["size"]["focusRing"]["$extensions"] = {"variants": [{"kind": k[0], "width": k[1], "offset": k[2], "color": k[3], "components": sorted(v)} for k, v in sorted(rings.items(), key=lambda kv: (-len(kv[1]), kv[0]))]}

# ---------------------------------------------------------------- motion
for n in names(r"^--(transition-duration-|default-transition-duration|animation-duration-)"):
    v = raw(n)
    m = re.fullmatch(r"([\d.]+)(m?s)", v)
    if m:
        ms = float(m.group(1)) * (1 if m.group(2) == "ms" else 1000)
        put(core, f"duration.{n[2:].replace('transition-duration-', '').replace('-transition-duration', '')}", tok("%gms" % ms, "duration", src(n)))
for n in names(r"^--(ease-|default-transition-timing-function|transition-ease-)"):
    v = raw(n)
    m = re.fullmatch(r"cubic-bezier\(([^)]*)\)", v)
    nm = n[2:].replace("default-transition-timing-function", "default")
    if m:
        put(core, f"easing.{nm}", tok([float(x) for x in m.group(1).split(",")], "cubicBezier", src(n)))
    elif v == "ease":
        put(core, f"easing.{nm}", tok([0.25, 0.1, 0.25, 1], "cubicBezier", src(n) + "; the keyword `ease` written as its cubic-bezier"))
    else:
        NOT["core"].append({"name": n, "value": v[:120], "why": "a linear() spring curve; DTCG cubicBezier cannot carry it"})
rm = V["reducedMotion"]
props = {}
for r in rm:
    for k, v in r["properties"].items():
        props.setdefault(k, set()).add(v[:40])
core["duration"]["$extensions"] = {"reducedMotion": {
    "source": f"Measured: {len(rm)} rules under @media (prefers-reduced-motion) or :root[data-reduced-motion] in the stylesheets; <html> carries data-reduced-motion=\"{C['captured']['reducedMotion']}\" from the account's setting",
    "propertiesChanged": {k: sorted(v)[:6] for k, v in sorted(props.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:16]},
    "examples": [{"selector": r["selector"][:120], "when": [c for c in r["context"] if "motion" in c][:1], "sets": dict(list(r["properties"].items())[:4])} for r in rm[:8]],
}}

# ---------------------------------------------------------------- layout
for n in names(r"^--breakpoint-"):
    put(core, f"breakpoint.{n[13:]}", tok(dim(n), "dimension", src(n)))
for n in names(r"^--container-"):
    put(core, f"container.{n[12:]}", tok(dim(n), "dimension", src(n)))
for n in ("--chat-max-width", "--dialog-max-width", "--markdown-wide-block-max-width", "--thread-composer-bottom-inset"):
    if dim(n):
        put(core, f"layout.{n[2:]}", tok(dim(n), "dimension", src(n)))
sb = RAWV["dark"].get("--spacing-token-sidebar")
if sb:
    NOT["core"].append({"name": "--spacing-token-sidebar", "value": sb, "why": "a clamp() of the viewport; 340px at 1440 (measured on the sidebar)"})
mc = raw("--masonry-columns")
grid_note = {"gridTemplateColumns": dict(list(V["gridColumns"].items())[:8])}
core["layout"]["$extensions"] = grid_note
# z-index: what each layer computes to on the measured elements, then the declared values by count.
Z = {"sidebar": "sidebar", "page-header": "page-header", "chat-menu": "menu", "tooltip": "tooltip", "confirm-dialog": "dialog", "search-dialog": "dialog", "pricing-dialog": "dialog", "promo-card": "promo-card", "m-drawer": "drawer"}


def eff_z(state):
    z = (state.get("style") or {}).get("zIndex")
    return z if z not in (None, "auto") else None


for key, layer in Z.items():
    s = MEAS.get(key, {}).get("states", {}).get("default")
    if not s:
        continue
    z = eff_z(s)
    anc = [a for a in s.get("zAncestors", [])] if s.get("zAncestors") else []
    if z is None and anc:
        z = anc[0]["z"]
    if z is not None:
        put(core, f"zIndex.{layer}", tok(int(z), "number", f"Measured: computed z-index of the {MEAS[key]['title'].lower()} (or its nearest positioned ancestor) on {s['snapshot']}"))
put(core, "zIndex.max-app-overlay", tok(int(raw("--max-app-overlay-z-index")), "number", src("--max-app-overlay-z-index")))
core["zIndex"]["$extensions"] = {"declared": {k: v["rules"] for k, v in list(V["zIndex"].items())[:14]}, "note": "z-index values the stylesheets declare, by number of rules"}

# ---------------------------------------------------------------- semantic sets
GROUPS = [
    ("bg", r"^--color-background-(?!.*-(soft|outline|ghost|solid|surface)(-|$))(?!(primary|secondary|danger|success|warning|info|caution|discovery)-)"),
    ("surface", r"^--color-surface"),
    ("text", r"^--color-text-(?!.*-(soft|outline|ghost|solid|surface)(-|$))(?!chat-accent-)(?!(primary|secondary|danger|success|warning|info|caution|discovery)-)"),
    ("border", r"^--color-border(?!-(primary|secondary|danger|success|warning|info|caution|discovery)-)"),
    ("ring", r"^--color-ring(-[a-z]+)?$"),
    ("token", r"^--color-token-"),
    ("chatAccent", r"^--color-text-chat-accent-|^--color-text-on-chat-accent"),
    ("chart", r"^--color-chart-"),
    ("icon", r"^--color-icon-"),
    ("app", r"^--app-color-"),
]
VARIANT = re.compile(r"^--color-(background|text|border|ring)-(primary|secondary|danger|success|warning|info|caution|discovery)-(soft-alpha|soft|outline|ghost|solid|surface)(?:-(hover|active|focus))?$")
PROP = {"background": "bg", "text": "text", "border": "border", "ring": "ring"}
SHADOW = re.compile(r"^--(shadow(-(?!alpha|color|hairline-width)[a-z0-9-]+)?|elevation-[a-z-]+|drop-shadow-[a-z]+)$")
for theme, out in sets.items():
    def add(path, n):
        c = color(n, theme)
        if c is not None:
            put(out, path, tok(c, "color", src(n, theme)))
    for n in sorted(RAWV[theme]):
        if not color(n, theme) and not SHADOW.match(n):
            continue
        m = VARIANT.match(n)
        if m:
            p, col, var, st = m.groups()
            add(f"variant.{col}.{var}.{PROP[p]}" + (f"-{st}" if st else ""), n)
            continue
        if SHADOW.match(n):
            r = RES[theme].get(n)
            if r and r["kind"] == "shadow":
                layers = shadow_layers(r["value"])
                if layers:
                    put(out, f"shadow.{n[2:]}", tok(layers, "shadow", src(n, theme) + " (box-shadow as computed, transparent layers dropped)"))
            elif raw(n, theme) and raw(n, theme) != "none" and not RES[theme].get(n):
                NOT[theme].append({"name": n, "value": raw(n, theme)[:120], "why": "a shadow geometry or keyword with no colour of its own"})
            continue
        for g, rx in GROUPS:
            if re.search(rx, n):
                short = re.sub(r"^--(color-(background|surface|text|border|ring|token|chart|icon)-?|app-color-)", "", n)
                if g == "chatAccent":
                    short = n.replace("--color-text-chat-accent-", "").replace("--color-text-on-chat-accent", "on-accent")
                if g == "surface":
                    short = n.replace("--color-surface", "").lstrip("-") or "default"
                if g == "ring":
                    short = n.replace("--color-ring", "").lstrip("-") or "default"
                add(f"{g}.{short or 'default'}", n)
                break
    # Scrims and backdrops (colour names that are not --color-*).
    for n in ("--dialog-backdrop-dim-background", "--modal-backdrop-background", "--dialog-backdrop-fade-background", "--app-color-simple-scrim"):
        add(f"scrim.{n[2:]}", n)
    for n in names(r"^--(modal-backdrop|dialog-backdrop|menu-backdrop)-.*filter$"):
        NOT[theme].append({"name": n, "value": raw(n, theme), "why": "a backdrop-filter; DTCG has no filter type"})

# ---------------------------------------------------------------- measured component values
def mstate(key, state, theme):
    st = state if theme == "dark" else ("light" if state == "default" else f"light-{state}")
    return MEAS.get(key, {}).get("states", {}).get(st)


# Names that hold a value for one specific place; a measured value is credited to them only when no
# general token holds it.
SPECIFIC = re.compile(r"tooltip|mode-toggle|home-suggestion|other-user-message|activity|coachmark|composer-action|control-opaque|recovery|execution|attribution|internal-badge|business|viewer|artifact|codex|usage|file|avatar|media|device|chatgpt-blue|discovery|caution")
PREFER = {"bg": ("surface", "bg", "variant", "token", "gray", "scrim", "app"), "text": ("text", "variant", "token", "gray", "app"), "border": ("ring", "border", "token", "variant", "gray", "app")}
# The general names a reader looks for first, when several tokens hold the same value.
FIRST = ["text.primary", "text.secondary", "text.tertiary", "text.disabled", "text.inverse", "text.accent-action", "text.danger", "text.info", "text.user-message",
         "surface.default", "surface.card", "surface.elevated", "surface.elevated-secondary", "surface.tertiary", "bg.accent-action", "bg.user-message",
         "ring.default", "border.default", "border.subtle", "border.strong", "variant.info.solid.bg", "variant.primary.solid.bg"]


def find_token(theme, value, kind="bg"):
    """The token in the theme set whose value equals `value`: general names before place-specific
    ones, then by the group order for that kind of value, then the shortest path."""
    prefer = PREFER[kind]
    hits = []

    def walk(t, path):
        for k, v in t.items():
            if k.startswith("$"):
                continue
            if isinstance(v, dict) and "$value" in v:
                if v["$type"] == "color" and v["$value"] == value:
                    hits.append(path + [k])
            elif isinstance(v, dict):
                walk(v, path + [k])
    walk(sets[theme], [])
    hits = [h for h in hits if h[0] not in ("role", "component")]
    hits.sort(key=lambda p: (p[0] not in prefer, FIRST.index(".".join(p)) if ".".join(p) in FIRST else 99, bool(SPECIFIC.search(".".join(p))), prefer.index(p[0]) if p[0] in prefer else 99, len(".".join(p)), ".".join(p)))
    return ".".join(hits[0]) if hits else None


def paint_bg(s):
    bg = (s.get("style") or {}).get("backgroundColor")
    if bg and bg != "rgba(0, 0, 0, 0)":
        return canon(bg)
    for p in s.get("paint") or []:
        if p.get("bg"):
            return canon(p["bg"])
    return None


COMP = [
    # (component token, measured key, state, property)
    ("button-accent.bg", "send-button", "default", "bg"), ("button-accent.bg-hover", "send-button", "hover", "bg"), ("button-accent.bg-pressed", "send-button", "pressed", "bg"), ("button-accent.text", "send-button", "default", "color"), ("button-accent.size", "send-button", "default", "height"),
    ("button-primary.bg", "promo-button", "default", "bg"), ("button-primary.bg-hover", "promo-button", "hover", "bg"), ("button-primary.bg-pressed", "promo-button", "pressed", "bg"), ("button-primary.text", "promo-button", "default", "color"), ("button-primary.radius", "promo-button", "default", "radius"), ("button-primary.height", "promo-button", "default", "height"),
    ("button-inverted.bg", "library-new", "default", "bg"), ("button-inverted.text", "library-new", "default", "color"), ("button-inverted.height", "library-new", "default", "height"),
    ("button-secondary.bg", "button-secondary", "default", "bg"), ("button-secondary.bg-hover", "button-secondary", "hover", "bg"), ("button-secondary.text", "button-secondary", "default", "color"), ("button-secondary.radius", "button-secondary", "default", "radius"), ("button-secondary.height", "button-secondary", "default", "height"),
    ("button-danger.bg", "button-danger", "default", "bg"), ("button-danger.bg-hover", "button-danger", "hover", "bg"), ("button-danger.text", "button-danger", "default", "color"), ("button-danger.height", "button-danger", "default", "height"),
    ("button-outline.text", "button-outline", "default", "color"), ("button-outline.bg-hover", "button-outline", "hover", "bg"), ("button-outline.height", "button-outline", "default", "height"),
    ("button-disabled.text", "button-disabled", "default", "color"), ("button-disabled.bg", "button-disabled", "default", "bg"), ("button-disabled.opacity", "button-disabled", "default", "opacity"),
    ("scrim.bg", "dialog-backdrop", "default", "bg"), ("pricing-primary.bg", "pricing-primary", "default", "bg"), ("pricing-primary.text", "pricing-primary", "default", "color"),
    ("checkbox.bg", "checkbox", "hover", "bg"), ("checkbox.border", "checkbox", "hover", "borderTopColor"), ("checkbox.border-focus", "checkbox", "focus-visible", "borderTopColor"),
    ("icon-button.bg-hover", "header-icon-button", "hover", "bg"), ("icon-button.bg-pressed", "header-icon-button", "pressed", "bg"), ("icon-button.text", "header-icon-button", "default", "color"), ("icon-button.size", "header-icon-button", "default", "height"),
    ("composer.bg", "composer", "default", "bg"), ("composer.radius", "composer", "default", "radius"), ("composer.height", "composer", "default", "height"),
    ("user-bubble.bg", "user-bubble", "default", "bg"), ("user-bubble.text", "user-bubble", "default", "color"), ("user-bubble.radius", "user-bubble", "default", "radius"),
    ("menu.bg", "chat-menu", "default", "bg"), ("menu.radius", "chat-menu", "default", "radius"),
    ("menu-item.bg-hover", "menu-item", "hover", "bg"), ("menu-item.text", "menu-item", "default", "color"), ("menu-item.height", "menu-item", "default", "height"), ("menu-item-danger.text", "menu-item-danger", "default", "color"),
    ("tooltip.bg", "tooltip", "default", "bg"), ("tooltip.text", "tooltip", "default", "color"), ("tooltip.radius", "tooltip", "default", "radius"),
    ("dialog.bg", "confirm-dialog", "default", "bg"), ("dialog.radius", "confirm-dialog", "default", "radius"),
    ("search-dialog.bg", "search-dialog", "default", "bg"), ("search-dialog.radius", "search-dialog", "default", "radius"),
    ("card.bg", "promo-card", "default", "bg"), ("card.radius", "promo-card", "default", "radius"),
    ("library-card.bg", "library-card", "default", "bg"), ("library-card.radius", "library-card", "default", "radius"),
    ("list-row.bg-hover", "chat-row", "hover", "bg"), ("list-row.bg-active", "chat-row", "active", "bg"), ("list-row.height", "chat-row", "default", "height"),
    ("nav-row.bg-active", "nav-row", "active", "bg"), ("nav-row.bg-hover", "nav-row", "hover", "bg"),
    ("tab.bg-selected", "library-tab", "selected", "bg"), ("tab.text", "library-tab", "default", "color"), ("tab.text-selected", "library-tab", "selected", "color"), ("tab.height", "library-tab", "default", "height"),
    ("switch.bg-on", "switch-on", "default", "bg"), ("switch.bg-off", "switch-off", "default", "bg"), ("switch.width", "switch-on", "default", "width"), ("switch.height", "switch-on", "default", "height"),
    ("badge.bg", "badge", "default", "bg"), ("badge.text", "badge", "default", "color"), ("badge.radius", "badge", "default", "radius"),
    ("sidebar.bg", "sidebar", "default", "bg"),
    ("table.border", "md-td", "default", "borderBottomColor"),
    ("code-block.bg", "code-block", "default", "bg"), ("code-block.radius", "code-block", "default", "radius"),
    ("link.text", "md-link", "default", "color"),
    ("text-field.bg", "library-search", "default", "bg"), ("text-field.radius", "library-search", "default", "radius"), ("text-field.height", "library-search", "default", "height"),
    ("checkbox.size", "checkbox", "hover", "height"),
    ("segmented.bg-checked", "segmented-radio", "checked", "bg"),
]
for theme, out in sets.items():
    for path, key, state, prop in COMP:
        s = mstate(key, state, theme)
        if not s or "style" not in s:
            continue
        st = s["style"]
        where = f"Measured: {MEAS[key]['title']}, {state}, {theme} ({s['snapshot']}, computed style)"
        if prop == "bg":
            v = paint_bg(s)
            if not v:
                continue
            ref = find_token(theme, v, "bg")
            put(out, f"component.{path}", tok("{" + ref + "}" if ref else v, "color", where + (f"; equals {ref}" if ref else "; no semantic token holds this value")))
        elif prop == "opacity":
            put(out, f"component.{path}", tok(float(st["opacity"]), "number", where))
        elif prop in ("color", "borderBottomColor", "borderTopColor"):
            v = canon(st.get(prop))
            if s.get("textStyle") and prop == "color" and st.get("color") == "rgba(0, 0, 0, 0)":
                v = canon(s["textStyle"]["color"])
            ref = find_token(theme, v, "text" if prop == "color" else "border")
            put(out, f"component.{path}", tok("{" + ref + "}" if ref else v, "color", where + (f"; equals {ref}" if ref else "; no semantic token holds this value")))
        elif prop in ("height", "width"):
            put(out, f"component.{path}", tok("%gpx" % round(s["rect"]["h" if prop == "height" else "w"], 2), "dimension", where + " (bounding box)"))
        elif prop == "radius":
            r = st.get("borderTopLeftRadius")
            if r and r.endswith("px"):
                v = "%gpx" % min(float(r[:-2]), 9999)
                ref = next((f"radius.{k}" for k, t in core.get("radius", {}).items() if isinstance(t, dict) and t.get("$value") == v), None)
                put(out, f"component.{path}", tok("{" + ref + "}" if ref else v, "dimension", where + (f"; equals core {ref}" if ref else "")))

# ---------------------------------------------------------------- elevation by use
# Each surface's measured box-shadow (transparent and repeated layers dropped), credited to the shadow
# token with the same layers where one exists.
ELEV = [("control", "switch-on", True), ("card", "library-card", False), ("menu", "chat-menu", False), ("tooltip", "tooltip", False),
        ("dialog", "confirm-dialog", False), ("drawer", "m-drawer", False), ("modal", "search-dialog", False), ("composer", "composer", False)]


def dedupe(layers):
    out = []
    for l in layers:
        if l not in out:
            out.append(l)
    return out


for theme, out in sets.items():
    for use, key, from_paint in ELEV:
        s_ = mstate(key, "default", theme)
        if not s_ or "style" not in s_:
            continue
        sh = s_["style"].get("boxShadow", "none")
        if from_paint or sh == "none":
            sh = next((p["shadow"] for p in s_.get("paint") or [] if p.get("shadow")), sh)
        layers = dedupe(shadow_layers(sh) or []) if sh != "none" else []
        if not layers:
            continue
        ref = next((f"shadow.{k}" for k, t in sorted(out.get("shadow", {}).items(), key=lambda kv: (len(kv[0]), kv[0])) if isinstance(t, dict) and t.get("$value") == layers), None)
        where = f"Measured: the box-shadow of the {MEAS[key]['title'].lower()} ({s_['snapshot']}, {theme})"
        put(out, f"elevation.{use}", tok("{" + ref + "}" if ref else layers, "shadow", where + (f"; equals {ref}" if ref else "; no single shadow token holds these layers")))

# ---------------------------------------------------------------- roles
ROLES = [
    ("bg.page", "token.main-surface-primary", "the thread and home ground (main)"),
    ("bg.surface", "surface.tertiary", "a sunk surface: the code-block header, sidebar hover rows"),
    ("bg.raised", "surface.elevated", "raised surfaces: search page, segmented thumb"),
    ("bg.overlay", "component.menu.bg", "menus and popovers, as measured"),
    ("bg.scrim", "component.scrim.bg", "behind dialogs, as measured on the dialog overlay (the --modal-backdrop-* names hold 50% black, the overlay paints less)"),
    ("text.primary", "text.primary", ""), ("text.secondary", "text.secondary", ""), ("text.tertiary", "text.tertiary", ""),
    ("text.disabled", "text.disabled", ""), ("text.on-accent", "text.accent-action", "on the accent send button"),
    ("text.link", "token.text-link-foreground", "markdown links"), ("text.inverse", "text.inverse", ""),
    ("border.default", "token.border-default", ""), ("border.subtle", "border.subtle", ""), ("border.strong", "border.strong", ""), ("border.focus", "ring.default", "the focus ring colour"),
    ("accent.default", "variant.info.solid.bg", "the blue solid button (Rejoin Plus), `--color-background-info-solid`"),
    ("accent.hover", "variant.info.solid.bg-hover", "`--color-background-info-solid-hover`"),
    ("accent.pressed", "variant.info.solid.bg-active", "`--color-background-info-solid-active`; :active is switched by script, so the static copies never showed it"),
    ("accent.action", "bg.accent-action", "the composer's send and voice buttons, which keep this fill on hover"),
    ("accent.text", "text.header-upgrade", "accent text (Upgrade)"),
]
for status in ("success", "warning", "danger", "info"):
    ROLES += [(f"status.{status}.fill", f"variant.{status}.surface.bg", f"`--color-background-{status}-surface`"),
              (f"status.{status}.text", f"variant.{status}.surface.text", f"`--color-text-{status}-surface`"),
              (f"status.{status}.border", f"variant.{status}.surface.border", f"`--color-border-{status}-surface`"),
              (f"status.{status}.solid", f"variant.{status}.solid.bg", f"`--color-background-{status}-solid`")]


def get(tree, path):
    for p in path.split("."):
        tree = tree.get(p) if isinstance(tree, dict) else None
        if tree is None:
            return None
    return tree


for theme, out in sets.items():
    for role, target, note in ROLES:
        t = get(out, target)
        if t is None:
            continue
        put(out, f"role.{role}", tok("{" + target + "}", "color", f"Derived: the checklist role {role} points at {target}" + (f" ({note})" if note else "")))

# ---------------------------------------------------------------- theme parity
# A name declared in one theme only: a shadow that computes to none in the other theme gets a
# transparent layer there (so both sets carry it); anything else leaves the set it is alone in and
# is listed under that set's notTokenised.
def paths(tree, pre=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield pre + k, v
        elif isinstance(v, dict):
            yield from paths(v, pre + k + ".")


def drop(tree, path):
    parts = path.split(".")
    for p_ in parts[:-1]:
        tree = tree[p_]
    del tree[parts[-1]]


for a_, b_ in (("light", "dark"), ("dark", "light")):
    have = dict(paths(sets[b_]))
    for path, node in list(paths(sets[a_])):
        if path in have:
            continue
        if node["$type"] == "shadow":
            put(sets[b_], path, tok([{"color": "rgba(0, 0, 0, 0)", "offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "0px"}], "shadow", node["$extensions"]["source"].replace(f"in {a_}", f"in {b_}") + f"; computes to none in {b_}, written as one transparent layer"))
        else:
            drop(sets[a_], path)
            NOT[a_].append({"name": path, "value": node["$value"], "why": f"declared for {a_} only; ChatGPT gives it no {b_} value"})

# ---------------------------------------------------------------- grid columns and type roles
lay = json.loads((RAW / "layout.json").read_text())
lib = lay.get("library-dark@1440", {}).get("libraryGrid")
if lib and lib.get("columns"):
    put(core, "layout.grid-columns-library", tok(int(lib["columns"]), "number", f"Measured: --masonry-columns on the Library's masonry grid at 1440 ({lib['gridTemplateColumns']}); its classes step it 1, 2, 3, 4, 5, 6 at the @sm, @xl, @3xl, @5xl and @7xl container widths"))
for label, key in (("plugins-dark@1440", "plugins"), ("images-dark@1440", "images")):
    g = next((g for g in lay.get(label, {}).get("grids", []) if "grid-cols" in g["el"]), None)
    if g:
        put(core, f"layout.grid-columns-{key}", tok(len(g["cols"].split()), "number", f"Measured: the {key} grid at 1440 ({g['el']}, columns {g['cols']}, gap {g['colGap']}) in raw/layout.json"))
core["typography"]["$extensions"] = {"roles": {
    "display": "heading-3xl, heading-4xl, heading-5xl (48 to 72, 600)",
    "heading": "heading-xs to heading-2xl (16 to 36, 600); the home heading is 28 (`--text-heading-app`)",
    "body": "text-md (16/24) in the UI, 16/26 in answers; text-sm (14/20) in rows and menus",
    "label": "control-label (13/18 510), small-caps-md and small-caps-lg (11 and 13, 600, tracked)",
    "caption": "text-xs (12/18), text-2xs (10/14)",
    "code": "code (the mono stack at 14/20)",
}, "source": "Derived: the checklist's type roles mapped onto ChatGPT's named styles"}

# ---------------------------------------------------------------- write
for k, v in NOT.items():
    tgt = core if k == "core" else sets[k]
    if v:
        tgt.setdefault("$extensions", OrderedDict())["notTokenised"] = sorted(v, key=lambda x: x["name"])
doc = OrderedDict()
doc["core"] = core
doc["light"] = sets["light"]
doc["dark"] = sets["dark"]
doc["$themes"] = [
    {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}, "$description": "ChatGPT's `.chatgpt-theme[data-theme=\"light\"]` palette; Settings > Appearance > Mode: Light"},
    {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}, "$description": "ChatGPT's `.chatgpt-theme[data-theme=\"dark\"]` palette with the Blue accent; the state every page was captured in"},
]
doc["$metadata"] = {"tokenSetOrder": ["core", "light", "dark"]}


def check(tree, setname):
    n = 0
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            n += 1
            assert v["$extensions"].get("source"), k
            if v["$type"] == "dimension":
                assert re.fullmatch(r"-?[\d.]+(px|rem)", v["$value"]) or v["$value"].startswith("{"), (k, v["$value"])
            if isinstance(v["$value"], str) and v["$value"].startswith("{"):
                ref = v["$value"][1:-1]
                base = core if setname == "core" or get(sets.get(setname, {}), ref) is None else sets[setname]
                assert get(base, ref) is not None, (setname, k, ref)
        elif isinstance(v, dict):
            n += check(v, setname)
    return n


counts = {s: check(doc[s], s) for s in ("core", "light", "dark")}
(HERE / "tokens.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
print("tokens.json", counts, {k: len(v) for k, v in NOT.items()})
