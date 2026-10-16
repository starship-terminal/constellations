#!/usr/bin/env python3
"""Build components.md for the Claude design reference.

Reads raw/components-computed.json (every component and state, measured in both themes),
raw/layout.json, tokens.json, screenshots/ and icons/INDEX.tsv, and writes components.md next to
them. Every value is a cell of the measurement file, condensed and written in tokens: a colour, shadow,
radius, padding, opacity, duration or easing is named by the token in tokens.json that holds it (the
token the element's own utility classes name, when there is one), with the measured value after it in
brackets; a value no token holds is written raw. The font family is named once per value, and a
state row shows only what differs from the first state. Dark states come first (the pages were
captured dark); the light reading of the same state follows as `light`, `light-hover` and so on.
Adapted from the Manus kit's builder.

Deterministic: re-running it on the same inputs reproduces components.md byte for byte.
Run from anywhere: python3 tools/build_components_md.py
"""
import collections, json, os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
J = json.load(open("raw/components-computed.json"))
C = J["components"]
META = J["_meta"]
LAYOUT = json.load(open("raw/layout.json"))
T = json.load(open("tokens.json"))

# --------------------------------------------------------------------------- colours and tokens


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


BY_COLOR = {"dark": {}, "light": {}}  # value -> every token holding it, role groups first


def resolve(theme, v, depth=0):
    """Follow {alias} through the theme's set and core to a literal."""
    m = re.fullmatch(r"\{([^{}]+)\}", str(v))
    if not m or depth > 8:
        return v
    for tree in (T[theme], T["core"]):
        node = tree
        for k in m.group(1).split("."):
            node = node.get(k) if isinstance(node, dict) else None
        if node and "$value" in node:
            return resolve(theme, node["$value"], depth + 1)
    return v


# The semantic groups first, so a colour is named by its role (text.primary) before its ramp step.
ORDER_GROUPS = ["surface", "text", "alpha", "border", "fill", "bg", "frame", "control", "on", "neutral", "legacy"]
for theme in ("dark", "light"):
    toks = sorted(flat(T[theme]), key=lambda nt: (ORDER_GROUPS.index(nt[0].split(".")[0]) if nt[0].split(".")[0] in ORDER_GROUPS else 99, nt[0]))
    for n, t in toks + list(flat(T["core"])):
        if t["$type"] == "color":
            v = resolve(theme, t["$value"])
            # computed styles round alpha to two places
            key = re.sub(r"(\d+\.\d+)\)", lambda m: f"{round(float(m.group(1)), 2):g})", v)
            BY_COLOR[theme].setdefault(key, [])
            if n not in BY_COLOR[theme][key]:
                BY_COLOR[theme][key].append(n)


def css_shadow(layers):
    """A shadow token's value written the way getComputedStyle writes a box-shadow."""
    out = []
    for ly in layers if isinstance(layers, list) else [layers]:
        c = ly["color"]
        if c.startswith("#"):
            c = "rgb(%d, %d, %d)" % tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))
        c = re.sub(r"(\d+\.\d+)\)", lambda m: f"{round(float(m.group(1)), 2):g})", c)  # computed styles round alpha to two places
        out.append(f"{c} {ly['offsetX']} {ly['offsetY']} {ly['blur']} {ly['spread']}" + (" inset" if ly.get("inset") else ""))
    return out


BY_SHADOW = {"dark": {}, "light": {}}
for theme in ("dark", "light"):
    for n, t in flat(T[theme]):
        if t["$type"] == "shadow":
            v = t["$value"]
            if isinstance(v, str):
                v = resolve(theme, v)
            if isinstance(v, (list, dict)):
                layers = [{**ly, "color": resolve(theme, ly["color"])} for ly in (v if isinstance(v, list) else [v])]
                BY_SHADOW[theme].setdefault(tuple(css_shadow(layers)), n)

# Dimensions, durations and curves by value, from core; the first group listed wins.
BY_DIM = {}
for grp in ("radius", "density", "size", "layout"):
    for n, t in flat(T["core"][grp], grp + "."):
        if t["$type"] == "dimension" and "--" not in n and not n.startswith(("density.avatar", "density.checkbox", "density.icon")):
            if n.startswith("density.gap"):
                continue
            BY_DIM.setdefault((grp if grp == "radius" or n.startswith("density.radius") else "pad" if n.startswith("density.pad") else "size", t["$value"]), n)
# Paddings off the density steps fall back to the spacing scale (Tailwind's 4px unit and its half steps).
for n, t in sorted(flat(T["core"]["space"], "space."), key=lambda nt: float(nt[1]["$value"][:-2])):
    BY_DIM.setdefault(("pad", t["$value"]), n)
# Icon glyph sizes: the density icon steps, the small one included.
BY_ICON = {}
for step in ("icon", "icon--sm", "icon--lg"):
    BY_ICON.setdefault(T["core"]["density"][step]["$value"], "density." + step)
# Box sizes: a height is named by the control-height, size or layout token that holds it; a width
# only by a layout width token, or by the height's token when the box is square (an icon button).
# Content-driven widths stay raw.
BY_HEIGHT, BY_WIDTH = {}, {}
for n, t in flat(T["core"]["density"], "density."):
    if n.startswith("density.h-control") and t["$type"] == "dimension":
        BY_HEIGHT.setdefault(t["$value"], n)
for grp in ("size", "layout"):
    for n, t in flat(T["core"][grp], grp + "."):
        if t["$type"] == "dimension":
            (BY_WIDTH if n.endswith("width") else BY_HEIGHT).setdefault(t["$value"], n)
BY_BW = {}
for n, t in flat(T["core"]["borderWidth"], "borderWidth."):
    if not n.endswith("focus-outline"):
        BY_BW.setdefault(t["$value"], n)
BY_BW.setdefault("2px", "borderWidth.focus-outline")
BY_PRESS = {t["$value"]: "press." + n for n, t in T["core"]["press"].items() if not n.startswith("$") and t["$type"] == "number"}
BY_OFFSET = {T["core"]["focusRing"]["outline-offset"]["$value"]: "focusRing.outline-offset"}
BY_DUR = {}
for n, t in flat(T["core"]["duration"], "duration."):
    ms = float(t["$value"].replace("ms", ""))
    BY_DUR.setdefault(f"{ms / 1000:g}s", n)
BY_EASE = {}
for n, t in flat(T["core"]["easing"], "easing."):
    if isinstance(t["$value"], list):
        BY_EASE.setdefault("cubic-bezier(%s)" % ", ".join(f"{x:g}" for x in t["$value"]), n)
BY_OPACITY = {}
for n, t in sorted(flat(T["core"]["opacity"], "opacity."), key=lambda nt: nt[0] != "opacity.disabled"):
    BY_OPACITY.setdefault(str(t["$value"]), n)


def core_value(v):
    """A core alias such as {fontSize.body} -> its literal."""
    m = re.fullmatch(r"\{([^{}]+)\}", str(v))
    if not m:
        return v
    node = T["core"]
    for k in m.group(1).split("."):
        node = node.get(k, {}) if isinstance(node, dict) else {}
    return core_value(node.get("$value", v))



# Counts of what the entries name: every colour, shadow and dimension written, and how many name a token.
NAMED = collections.Counter()

THEME = ["dark"]  # the theme the colour() helper looks tokens up in; set per state
HINTS = [set()]  # tokens the current element's utility classes name; set per state

# Which token groups a colour is looked for in first, by the property it paints.
ROLE = {
    "text": ("text", "on", "fill", "alpha", "surface"),
    "background": ("fill", "surface", "bg", "alpha", "frame", "control", "on", "text"),
    "border": ("border", "alpha", "fill"),
}
UTIL = re.compile(r"(?<![\w-])(?:[\w\[\]&=/-]*:)*(bg|text|border|ring|shadow|fill|outline|placeholder|decoration)-([a-z][a-z0-9-]*)")


def hints_of(classes):
    """Token names an element's Tailwind utilities point at: bg-fill-danger -> fill.danger,
    text-on-primary -> on.primary, text-muted -> text.muted, border-strong -> border.strong."""
    out = set()
    for pre, rest in UTIL.findall(classes or ""):
        out.add(rest.replace("-", ".", 1))
        out.add(f"{'text' if pre == 'placeholder' else pre}.{rest}")
    return out


def pick(cands, role):
    if not cands:
        return None
    for c in cands:
        if c in HINTS[0]:
            return c
    for g in ROLE.get(role, ()):
        for c in cands:
            if c.split(".")[0] == g:
                return c
    return cands[0]


def tok(name, value):
    NAMED["token" if name else "raw"] += 1
    return f"`{name}` ({value})" if name else value


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), round(float(a), 2))


def colour(c, tokens=True, role=None):
    """rgb()/rgba()/color(srgb)/oklab() -> '`token` (#hex)', or the bare value when no token holds it.
    Every form is first rewritten as rgb()/rgba() text, then labelled in one pass, so no value is
    labelled twice."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)" or v.endswith(", 0)"):
            return "transparent"
        if not tokens:
            return v
        return tok(pick(BY_COLOR[THEME[0]].get(v), role), v)

    def as_rgb(rgb, a):
        return "rgb(%d, %d, %d)" % tuple(rgb) if a is None or float(a) == 1 else "rgba(%d, %d, %d, %s)" % (*rgb, a)

    def oklab(m):
        L, A, B = (float(m.group(i)) for i in (1, 2, 3))
        lin = lambda x: 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055
        l, mm, sv = ((L + 0.3963377774 * A + 0.2158037573 * B) ** 3, (L - 0.1055613458 * A - 0.0638541728 * B) ** 3, (L - 0.0894841775 * A - 1.2914855480 * B) ** 3)
        rgb = (4.0767416621 * l - 3.3077115913 * mm + 0.2309699292 * sv, -1.2684380046 * l + 2.6097574011 * mm - 0.3413193965 * sv, -0.0041960863 * l - 0.7034186147 * mm + 1.7076147010 * sv)
        return as_rgb([round(min(1, max(0, lin(x))) * 255) for x in rgb], m.group(4))

    c = re.sub(r"oklab\(([-\d.e]+) ([-\d.e]+) ([-\d.e]+)(?: / ([\d.]+))?\)", oklab, c)
    c = re.sub(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)", lambda m: as_rgb([round(float(x) * 255) for x in m.group(1, 2, 3)], m.group(4)), c)
    return re.sub(r"rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)", lambda m: label(norm(*m.group(1, 2, 3), m.group(4))), c)


def sides(t, r, b, l):
    t, r, b, l = (("9999px" if re.fullmatch(r"[\d.]+e\+\d+px", x) else x) for x in (t, r, b, l))
    if t == r == b == l:
        return t
    if t == b and r == l:
        return f"{t} {r}"
    return f"{t} {r} {b} {l}"


def fam(f):
    first = f.split(",")[0].replace('"', "").strip()
    return {"anthropic-sans": "Anthropic Sans", "anthropic-serif": "Anthropic Serif", "anthropic-mono": "Anthropic Mono", "Anthropicons-Variable": "Anthropicons", "ui-sans-serif": "System", "ui-monospace": "Mono"}.get(first, first)


def num(x):
    return re.sub(r"(\d+\.\d\d)\d+", r"\1", str(x))


BY_ROLE = {}
for role, t in T["core"]["fontSize"].items():
    lh_ = T["core"]["lineHeight"].get(role)
    if not role.startswith("$") and lh_ and not str(t["$value"]).startswith("{"):
        BY_ROLE.setdefault((t["$value"], lh_["$value"]), role)
BY_WEIGHT = {str(t["$value"]): "fontWeight." + n for n, t in T["core"]["fontWeight"].items() if not n.startswith("$")}
# Type by (family, size, line height, weight), from the composite typography tokens; the plain
# role names (body-regular) before the measured ones that share a value.
BY_TYPE = {}
for n, t in flat(T["core"]["typography"], "typography."):
    v = t["$value"]
    fam_ = core_value(v["fontFamily"])
    fam_ = fam_[0] if isinstance(fam_, list) else str(fam_).split(",")[0]
    key = (fam(str(fam_)), num(str(core_value(v["fontSize"])).replace("px", "")), num(str(core_value(v["lineHeight"])).replace("px", "")), str(core_value(v["fontWeight"])))
    BY_TYPE.setdefault(key, n)


def font(fz, lh, fw, f):
    lh = lh.replace("px", "") if lh != "normal" else "normal"
    raw = f"{fam(f)} {num(fz.replace('px', ''))}/{num(lh)} {fw}"
    if fam(f) == "Anthropicons":  # an icon glyph: its size is an icon step, not a type role
        # cds sets the glyph's weight from its size (thinner as it grows), so the size token carries both
        return f"Anthropicons {tok(BY_ICON.get(fz), f'{fz}, weight {fw}') if BY_ICON.get(fz) else f'{fz} at weight {fw}'}"
    name = BY_TYPE.get((fam(f), num(fz.replace("px", "")), num(lh), str(fw)))
    if not name and fam(f) == "Anthropic Sans" and (fz, lh + "px") in BY_ROLE and str(fw) in BY_WEIGHT:
        # no composite style for this weight: name the role's size and line height and the weight
        role = BY_ROLE[(fz, lh + "px")]
        NAMED["token"] += 1
        return f"`fontSize.{role}` / `lineHeight.{role}` at `{BY_WEIGHT[str(fw)]}` ({raw})"
    return tok(name, raw)


def dim(kind, value):
    return tok(BY_DIM.get((kind, value)), value)


def shadow(raw):
    """A box-shadow, named by the shadow token it equals; the focus rings match whatever surface
    their inset sits on, since that first layer takes the page colour."""
    sh = colour(raw, tokens=False)
    layers = [x.strip() for x in re.split(r",(?![^(]*\))", sh)]
    # layers that paint nothing: a transparent colour, or no offset, blur or spread (Tailwind's ring placeholders)
    layers = [x for x in layers if not x.startswith("transparent") and not re.match(r"rgba\([^)]*, 0\) ", x) and not re.search(r" 0px 0px 0px 0px( inset)?$", x)]
    if not layers:
        return None
    rgb = [re.sub(r"#([0-9a-f]{6})", lambda m: "rgb(%d, %d, %d)" % tuple(int(m.group(1)[i:i + 2], 16) for i in (0, 2, 4)), x) for x in layers]
    name = BY_SHADOW[THEME[0]].get(tuple(rgb))
    rings = [re.fullmatch(r"(.+) 0px 0px 0px ([\d.]+px)( inset)?", x) for x in rgb]
    if not name and all(rings):
        # a hairline drawn as a box-shadow: name its colour as a border
        return ", ".join(f"{tok(BY_BW.get(m.group(2)), m.group(2))} ring{' inset' if m.group(3) else ''} {colour(m.group(1), role='border')}" for m in rings)
    if not name and rgb[0].endswith(" 0px 0px 0px 1px inset"):
        for k, n in BY_SHADOW[THEME[0]].items():
            if len(k) == len(rgb) > 1 and k[0].endswith(" 0px 0px 0px 1px inset") and list(k[1:]) == rgb[1:]:
                name = n + " on this surface"
                break
    if not name and len(rgb) > 1:
        # a hairline ring layered with a shadow token: name both parts
        for i in (0, len(rgb) - 1):
            ring, others = rings[i], tuple(rgb[:i] + rgb[i + 1:])
            if ring and others in BY_SHADOW[THEME[0]]:
                part = tok(BY_SHADOW[THEME[0]][others], ", ".join(others))
                return f"{tok(BY_BW.get(ring.group(2)), ring.group(2))} ring{' inset' if ring.group(3) else ''} {colour(ring.group(1), role='border')} + {part}"
    return tok(name, ", ".join(layers))


def props(v):
    s = v["style"]
    o = {}
    HINTS[0] = hints_of(v.get("classes"))
    w, h = num(v["rect"]["w"]), num(v["rect"]["h"])
    wt = BY_WIDTH.get(w + "px") or (BY_HEIGHT.get(h + "px") if w == h else None)
    # a width no token holds is the instance's content width, written raw and not counted as a spec value
    o["size"] = f"{tok(wt, w) if wt else w} x {tok(BY_HEIGHT.get(h + 'px'), h)}"
    pad = sides(s["paddingTop"], s["paddingRight"], s["paddingBottom"], s["paddingLeft"])
    if pad != "0px":
        o["padding"] = " ".join(dim("pad", x) if x != "0px" else "0" for x in pad.split(" "))
    bds = []
    for d in ("Top", "Right", "Bottom", "Left"):
        if float(s[f"border{d}Width"].replace("px", "")) > 0 and s[f"border{d}Style"] != "none":
            bds.append(f"{tok(BY_BW.get(s[f'border{d}Width']), s[f'border{d}Width'])} {s[f'border{d}Style']} {colour(s[f'border{d}Color'], role='border')}")
        else:
            bds.append("none")
    if any(b != "none" for b in bds):
        o["border"] = bds[0] if len(set(bds)) == 1 else "; ".join(f"{'TRBL'[i]}: {b}" for i, b in enumerate(bds) if b != "none")
    rad = sides(s["borderTopLeftRadius"], s["borderTopRightRadius"], s["borderBottomRightRadius"], s["borderBottomLeftRadius"])
    if rad != "0px":
        o["radius"] = dim("radius", rad) if " " not in rad else rad
    o["background"] = colour(s["backgroundColor"], role="background")
    if s["backgroundImage"] != "none":
        img = re.sub(r'url\("data:[^)]*\)', "an image (data URI)", s["backgroundImage"])
        o["image"] = colour(img)[:200]
    if s["boxShadow"] != "none":
        sh = shadow(s["boxShadow"])
        if sh:
            o["shadow"] = sh
    # cds often draws the focus ring on an inner layer (the button inside a row, a tab's own button,
    # a row's link overlay); name it, with the layer it sits on
    if "focus" not in (o.get("shadow") or ""):
        for ly in (v.get("paint") or [])[:4]:
            if ly.get("shadow") == s["boxShadow"]:
                continue  # the element itself, whose shadow the row already gives
            lab = shadow(ly["shadow"]) if ly.get("shadow") else None
            # a shadow.focus ring, or any other ring drawn in the accent or danger colour (the sidebar
            # row's link draws a 1px inset accent ring with a 6px glow, which no token holds)
            if lab and ("`shadow.focus" in lab or re.search(r"#2a78d6|#d03b3b|42, 120, 214|208, 59, 59", lab)):
                o["focus ring"] = f"on the inner {ly['node'].split('.')[0]}: {lab}"
                break
    if s.get("backdropFilter", "none") != "none":
        o["backdrop"] = s["backdropFilter"]
    if s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0:
        o["outline"] = f"{tok(BY_BW.get(s['outlineWidth']), s['outlineWidth'])} {s['outlineStyle']} {colour(s['outlineColor'], role='border')}, offset {tok(BY_OFFSET.get(s['outlineOffset']), s['outlineOffset']) if s['outlineOffset'] != '0px' else '0'}"
    t = v.get("textStyle")
    if t:
        o["text"] = f"{font(t['fontSize'], t['lineHeight'], t['fontWeight'], t['fontFamily'])}, {colour(t['color'], role='text')}"
    elif v.get("text"):
        o["text"] = f"{font(s['fontSize'], s['lineHeight'], s['fontWeight'], s['fontFamily'])}, {colour(s['color'], role='text')}"
    if s["textDecorationLine"] not in ("none", "") and v.get("text"):
        uo = s["textUnderlineOffset"]
        o["underline"] = f"{colour(s['textDecorationColor'], role='text')}, offset {tok('link.underline-offset' if uo == T['core']['link']['underline-offset']['$value'] else None, uo)}"
    if s["transitionDuration"] not in ("0s", ""):
        props_ = [x.strip() for x in s["transitionProperty"].split(",")]
        durs = [x.strip() for x in s["transitionDuration"].split(",")]
        tf = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", s["transitionTimingFunction"])
        parts = []
        for i, p in enumerate(props_):
            d = durs[i % len(durs)]
            if d == "0s":
                continue
            e = tf[i % len(tf)] if tf else ""
            parts.append(f"{p} {tok(BY_DUR.get(d), d)} {tok(BY_EASE.get(e), e) if e.startswith('cubic') else e}".strip())
        if parts:
            o["transition"] = ", ".join(parts) if len(parts) < 4 else f"{parts[0].split(' ')[0]} and {len(parts) - 1} more {' '.join(parts[0].split(' ')[1:])}"
    if s["transform"] not in ("none", "matrix(1, 0, 0, 1, 0, 0)"):
        m = re.fullmatch(r"matrix\(([\d.]+), 0, 0, ([\d.]+), (-?[\d.]+), (-?[\d.]+)\)", s["transform"])
        if m and m.group(1) == m.group(2) and m.group(3) == m.group(4) == "0":
            o["transform"] = f"scale({m.group(1)})"
        elif m and m.group(1) == m.group(2) == "1":
            o["transform"] = f"translate({m.group(3)}px, {m.group(4)}px)"
        else:
            o["transform"] = s["transform"]
    sq = (v.get("squish") or {}).get("transform", "none")
    m = re.fullmatch(r"matrix\(([\d.]+), 0, 0, ([\d.]+), 0, 0\)", sq)
    if m and m.group(1) == m.group(2) and abs(float(m.group(1)) - 1) > 0.001:
        o["press"] = f"paint layer {tok(BY_PRESS.get(float(m.group(1))), 'scale(' + m.group(1) + ')')}"
    if s["opacity"] != "1":
        o["opacity"] = tok(BY_OPACITY.get(s["opacity"]), s["opacity"])
    ic = v.get("icon")
    if ic and ic.get("w", 0) > 0 and ic["w"] < 120:
        iw, ih = num(ic["w"]), num(ic["h"])
        it = BY_ICON.get(ih + "px")
        o["icon"] = f"{tok(it, iw) if iw == ih and it else iw} x {tok(it, ih) if it else ih}, {colour(ic.get('color') or ic.get('stroke') or ic.get('fill'), role='text')}"
    if v.get("placeholder"):
        o["placeholder"] = colour(v["placeholder"]["color"], role="text")
    return o


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "focus ring", "backdrop", "outline", "text", "underline", "transition", "transform", "press", "opacity", "icon", "placeholder"]


def state_rows(c):
    """Dark states first, then light. Each theme has its own base row (the first state of that
    theme), later rows of the same theme list only what changed."""
    rows = []
    for theme in ("dark", "light"):
        states = [s for s, v in c["states"].items() if "style" in v and v.get("theme") == theme]
        if not states:
            continue
        THEME[0] = theme
        base = props(c["states"][states[0]])
        trows = [(states[0], base)]
        same = []
        for st in states[1:]:
            p = props(c["states"][st])
            diff = {k: p[k] for k in ORDER if k in p and p.get(k) != base.get(k)}
            for k in ORDER:
                if k in base and k not in p:
                    diff[k] = "1" if k == "opacity" else "none"
            if not diff:
                same.append(st)
                continue
            if trows[-1][0] != states[0] and trows[-1][1] == diff:
                trows[-1] = (trows[-1][0] + ", " + st, diff)
            else:
                trows.append((st, diff))
        if same:
            trows[0] = (f"{states[0]} (same: {', '.join(same)})", base)
        rows += trows
    return rows


def fmt(d):
    return "; ".join(f"{k} {d[k]}" for k in ORDER if k in d).replace("|", "/")


def child_layers(c):
    st = next((s for s in c["states"].values() if "style" in s and s.get("theme") == "dark"), None)
    if not st or not st.get("paint"):
        return None
    s = st["style"]
    if s["backgroundColor"] != "rgba(0, 0, 0, 0)" or s["boxShadow"] != "none" or s["borderTopWidth"] != "0px" or s["backgroundImage"] != "none":
        return None
    THEME[0] = "dark"
    HINTS[0] = set()
    out = []
    for p in st["paint"][:3]:
        bits = [re.sub(r"\..*$", "", p["node"]) if "::" not in p["node"] else p["node"].split(".")[0], p["size"].replace(".0x", "x").replace(".0", "")]
        if p.get("bg"):
            bits.append("background " + colour(p["bg"], role="background"))
        if p.get("border"):
            bw_, rest_ = p["border"].split(" | ")[0][2:].split(" ", 1)
            bits.append("border " + tok(BY_BW.get(bw_), bw_) + " " + colour(rest_, role="border"))
        if p.get("radius"):
            r = "9999px" if re.fullmatch(r"[\d.]+e\+\d+px", p["radius"]) else p["radius"]
            bits.append("radius " + (dim("radius", r) if " " not in r else r))
        if p.get("shadow"):
            bits.append("shadow " + (shadow(p["shadow"]) or "none"))
        out.append(" ".join(bits))
    return "; ".join(out).replace("|", "/")


# --------------------------------------------------------------------------- page and group text

GROUP_INTRO = {
    "Sidebar": "The 288px sidebar every desktop page shares, on its own ground a step darker than the page in dark: a 44px title row (the serif \"Claude\" wordmark, Hide sidebar, Search), the Home/Code pills, New, Artifacts and More, then the Pinned and \"Chats and tasks\" sections whose rows lead with a 6px hollow ring, and the account row with the plan. Hiding it leaves one Show sidebar button in the corner.",
    "Header": "The 48px row over the content column: empty on the home page but for Use incognito; on a chat, the title button with its more menu, and Share.",
    "Home and composer": "The new-chat page: the serif greeting led by the clay asterisk, and the composer, the same card on the home page, in a chat and on a project page: a 20px-radius card on surface-3 with a ring, the editor, then +, the Chat/Cowork segments, the model selector (model and effort), dictation and voice. Typing swaps voice for the clay send button.",
    "Menus and dialogs": "Base UI popovers on surface-popover with radius 12, a 1px ring (outset in light, inset in dark) and the popover drop: the plus menu, the model menu, the account menu, a chat row's menu, the sidebar's More menu, and the search dialog over its backdrop.",
    "Settings": "The settings dialog: a 192px nav with a search field and two groups (Settings, Customize), and the General pane: section titles, rows with a title, an optional description and a control (the System/Light/Dark theme picker, selects, segmented controls, switches), split by hairlines.",
    "Thread": "A chat: the 768px transcript, the user's bubble, \"Thought for 6s\", Claude's reply in the chat font (Anthropic Serif by default) with a code block and a table, the message actions, and the dock that holds the composer.",
    "Pages": "The list pages share one 960px page column with a serif page title: Artifacts (tabs, a notice card, the Make something new tiles, month groups of rows), Chats and tasks (a table of rows with times), Projects (a two-column grid of cards) and a project page (breadcrumb, title, composer, Recents, the Instructions, Memory and Context cards).",
    "Forms and feedback": "Added on 2026-10-17 from nine new copies: the tooltip, the text link, the checkbox, the confirmation and form dialogs with their primary, secondary, danger and disabled buttons, the text field (with its error state) and text area, the list search, empty result, filter menu, loading skeleton and the two page grids. Every button here was also read pressed, with the pointer held down: cds keeps the hover fill and squishes the paint layer to 97.5% (`core.press.button-scale`).",
    "Mobile": "The same app at 390 wide: a Show sidebar button, the greeting and the pinned composer whose segments drop to icons, the sidebar as a full-screen drawer sheet with 44px rows, and a chat.",
}

PAGE_DESC = [
    ("home", "Home (new chat). The greeting and the composer. Captured at rest, with the plus menu, the model menu, the account menu, a chat row's menu, the search dialog, a line typed in the composer, and with the sidebar hidden (the account's own setting); on 2026-10-17 also with the Search button's tooltip open.", "/new"),
    ("thread", "A chat, one copy read at three scroll positions: the top (user message, Thought for 6s, the code block), the table (scroll 1150) and the follow-up (scroll 1780).", "/chat/<id>"),
    ("artifacts", "Artifacts. Tabs, the notice card, Make something new, month groups of rows; also with the sidebar's More menu open. On 2026-10-17 the page had become a grid of cards, captured while loading (skeletons).", "/artifacts"),
    ("chats", "Chats and tasks. The table of chats and tasks with their times; on 2026-10-17 also in Select mode with one row ticked, with the filter menu open, with a search that matches nothing, and with a chat's delete confirmation open.", "/chats"),
    ("projects", "Projects. The two project cards; on 2026-10-17 also with the Create a project dialog open.", "/projects"),
    ("project", "A project page.", "/project/<id>"),
    ("settings", "Settings dialog: the General pane; on 2026-10-17 also the Account pane (text fields, a text area, a disabled button, links) and the Capabilities pane (a disabled switch, inline links).", "/settings/general"),
]
MOBILE_DESC = [
    ("mobile-home", "Home at 390 wide, and the drawer.", "/new"),
    ("mobile-thread", "The chat at 390 wide.", "/chat/<id>"),
]

L = []


def W(s=""):
    L.append(s)


shots = sorted(p.name for p in Path("screenshots").glob("*.png"))


def links(prefix):
    out = []
    for f in shots:
        m = re.fullmatch(re.escape(prefix) + r"-(dark|light)-(.+)\.png", f)
        if m:
            out.append(f"[{m.group(2)} ({m.group(1)})](screenshots/{f})")
        elif re.fullmatch(re.escape(prefix) + r"-(dark|light)\.png", f):
            out.append(f"[default ({f.split('-')[-1][:-4]})](screenshots/{f})")
    return ", ".join(out)


n_crops = len(list(Path("components/crops").glob("*.png")))
n_states = sum(len(c["states"]) for c in C.values())
icons = [r.split("\t") for r in open("icons/INDEX.tsv").read().strip().split("\n")[1:]]

W("# Claude components")
W()
W(f"The discovery list of every page and state captured, then one entry per component with crops of the real product, the shared values, the icon index and the Gaps. Captured from claude.ai on {META['read']} and refreshed on 2026-10-17, signed in, as static copies of each page state rendered in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the rendered copy in both themes. Nothing was sent, created or deleted in the account: a line was typed into the composer and deleted, menus and dialogs were opened and closed (the delete confirmation with Escape, Create a project with Cancel), a checkbox was ticked in Select mode and the mode left, and the sidebar was shown for the captures and hidden again.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [raw/pages.md](raw/pages.md).")
W()
W("How to read an entry:")
W()
W("- Values are written as tokens: a colour, shadow, radius, padding, type style, icon size, opacity, duration or easing reads as the token in [tokens.json](tokens.json) that holds it in that theme, then the measured value in brackets, for example `` `text.primary` (#f0efec) ``. Where several tokens hold the value, the one the element's own utility classes name wins (`bg-fill-danger` is `fill.danger`), then a role that fits the property (text and on for text, fill and surface for backgrounds, border for edges). A focus ring drawn on another surface reads `` `shadow.focus on this surface` ``, and a hairline ring names its colour as a border. A height is named by the control-height, size or layout token that holds it; a width only when a layout width token holds it or the box is square, and otherwise it is the instance's content width, written raw and not counted below. A colour with zero alpha reads `transparent`. A value no token holds is written raw: a few line heights (14/21), odd paddings and some drop shadows inside components. @@NAMED@@")
W("- Text is written as its typography token, then family size/line-height weight in brackets, then its colour, for example `` `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec) ``, and is read from the first text node inside the component. A glyph from the icon font reads `Anthropicons` with its icon size step and weight.")
W("- Dark states come first (every page was captured dark), then the same states read in light. Each theme's first row lists every value; later rows of that theme list only what changes. A state with the same values as its theme's first is named in that label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do: a cds Button paints its fill on an inner span, so its hover shows there.")
W(f"- Crops are images of the component from the rendered copy, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{theme}-{state}.png`. Desktop shots are 1440 x 900 at 2x; `-full` shots are whole pages at 2x, kept for the dark Artifacts and Chats pages; phone shots are `mobile-{page}-{theme}-{state}.png`, 390 x 844 at 2x. Every state exists in both themes.")
W()
W("| Surface | URL | Screenshots |")
W("|---|---|---|")
for p, desc, url in PAGE_DESC + MOBILE_DESC:
    W(f"| {desc} | `{url}` | {links(p)} |")
W()
W("### Overlays and transient states")
W()
W("| State | Where | How it was reached | Captured |")
W("|---|---|---|---|")
OVER = [
    ("Plus menu", "home", "the composer's + button", "[home-dark-plus-menu](screenshots/home-dark-plus-menu.png), [plus-menu](#plus-menu)"),
    ("Model menu", "home", "the model selector", "[home-dark-model-menu](screenshots/home-dark-model-menu.png), [model-menu](#model-menu)"),
    ("Account menu", "home", "the account row", "[home-dark-user-menu](screenshots/home-dark-user-menu.png), [user-menu](#user-menu)"),
    ("Chat row menu", "home", "a sidebar chat row's more button", "[home-dark-chat-menu](screenshots/home-dark-chat-menu.png), [chat-menu](#chat-menu)"),
    ("Search dialog", "home", "the sidebar's Search button", "[home-dark-search](screenshots/home-dark-search.png), [search-dialog](#search-dialog)"),
    ("Composer with text", "home", "a line typed, then deleted", "[home-dark-composer-typed](screenshots/home-dark-composer-typed.png), [send-button](#send-button)"),
    ("Sidebar hidden", "home", "the account's own state; the sidebar was shown for every other capture and hidden again after", "[home-dark-sidebar-collapsed](screenshots/home-dark-sidebar-collapsed.png), [sidebar-collapsed](#sidebar-collapsed)"),
    ("More menu", "Artifacts", "the sidebar's More row", "[artifacts-dark-more-menu](screenshots/artifacts-dark-more-menu.png), [more-menu](#more-menu)"),
    ("Settings dialog", "any page", "Settings in the account menu; closed with Escape", "[settings-dark-general](screenshots/settings-dark-general.png), [settings-dialog](#settings-dialog)"),
    ("Tooltip", "home", "synthetic pointer events on the sidebar Search button (2026-10-17)", "[home-dark-tooltip](screenshots/home-dark-tooltip.png), [tooltip](#tooltip)"),
    ("Select mode", "Chats", "the Select button, then one row's checkbox; left with the exit button (2026-10-17)", "[chats-dark-select](screenshots/chats-dark-select.png), [checkbox](#checkbox)"),
    ("Filter menu", "Chats", "the header's filter button (2026-10-17)", "[chats-dark-filter-menu](screenshots/chats-dark-filter-menu.png), [filter-menu](#filter-menu)"),
    ("Empty search", "Chats", "the header's search button, then a word that matches nothing, cleared after (2026-10-17)", "[chats-dark-search-empty](screenshots/chats-dark-search-empty.png), [empty-state](#empty-state)"),
    ("Delete confirmation", "Chats", "a sidebar chat row's menu, Delete; dismissed with Escape (2026-10-17)", "[chats-dark-delete-confirm](screenshots/chats-dark-delete-confirm.png), [confirm-dialog](#confirm-dialog)"),
    ("Create a project", "Projects", "New project; closed with Cancel (2026-10-17)", "[projects-dark-create](screenshots/projects-dark-create.png), [form-dialog](#form-dialog)"),
    ("Loading", "Artifacts", "the snapshot taken 120 ms after clicking Artifacts in the sidebar (2026-10-17)", "[artifacts-dark-loading](screenshots/artifacts-dark-loading.png), [skeleton](#skeleton)"),
    ("Drawer sheet", "home at 390", "the Show sidebar button; it could not be closed in the copy, so it was hidden by hand before the phone chat copy", "[mobile-home-dark-drawer](screenshots/mobile-home-dark-drawer.png), [m-drawer](#m-drawer)"),
]
for row in OVER:
    W("| " + " | ".join(row) + " |")
W()

# --------------------------------------------------------------------------- shared values

W("## Shared values")
W()
W("Values that apply across entries, tallied from the measurement file.")
W()
radii = collections.Counter()
trans = collections.Counter()
hover_dark = collections.Counter()
hover_light = collections.Counter()
focus = {"dark": collections.Counter(), "light": collections.Counter()}
focus_n = {"dark": 0, "light": 0}
for cid, c in C.items():
    for sname, s in c["states"].items():
        if "style" not in s:
            continue
        st = s["style"]
        r = "9999px" if re.fullmatch(r"[\d.]+e\+\d+px", st["borderTopLeftRadius"]) else st["borderTopLeftRadius"]
        if r != "0px" and s["rect"]["w"] > 4:
            radii[r] += 1
        if st["transitionDuration"] not in ("0s", ""):
            # the first duration and the first timing function; a cubic-bezier() carries commas of its own
            tf = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", st["transitionTimingFunction"])
            trans[f"{st['transitionDuration'].split(',')[0].strip()} {tf[0] if tf else st['transitionTimingFunction']}"] += 1
        if sname.endswith("focus-visible"):
            th = s["theme"]
            focus_n[th] += 1
            THEME[0] = th
            rest = c["states"].get(sname[: -len("focus-visible")].rstrip("-") or "default") or {}
            rest = rest.get("style") or {}
            visible = lambda col: not re.search(r"(, 0\)|/ 0\))$", col) and col != "rgba(0, 0, 0, 0)"
            shs = [st["boxShadow"]] + [ly.get("shadow") or "" for ly in (s.get("paint") or [])[:4]]
            outs = [ly.get("outline") or "" for ly in (s.get("paint") or [])[:4]]
            if st["outlineStyle"] != "none" and float(st["outlineWidth"].replace("px", "")) > 0 and visible(st["outlineColor"]):
                focus[th][f"a {st['outlineWidth']} {st['outlineStyle']} outline in {colour(st['outlineColor'], role='border')}, offset {st['outlineOffset']}"] += 1
            elif any(re.search(r"42, 120, 214|0\.164706 0\.470588 0\.839216|208, 59, 59|0\.815686 0\.231373 0\.231373", x) for x in shs):
                focus[th]["the shadow.focus ring (or shadow.focus-danger), on the element or an inner layer"] += 1
            elif any(o and not o.split(" offset")[0].endswith(", 0)") for o in outs):
                focus[th]["a 2px outline on an inner layer"] += 1
            elif rest and st["boxShadow"] != rest.get("boxShadow"):
                focus[th]["its own ring turns border.strong (the composer, a field that holds the caret)"] += 1
            elif rest and st["backgroundColor"] != rest.get("backgroundColor"):
                focus[th]["the hover wash, no ring"] += 1
            else:
                focus[th]["nothing visible on the element or its first layers"] += 1
for cid, c in C.items():
    for th, base, hov, ctr in (("dark", "default", "hover", hover_dark), ("light", "light", "light-hover", hover_light)):
        a, b = c["states"].get(base), c["states"].get(hov)
        if not a or not b or "style" not in a or "style" not in b:
            continue
        THEME[0] = th
        if a["style"]["backgroundColor"] != b["style"]["backgroundColor"]:
            ctr[f"{colour(a['style']['backgroundColor'])} to {colour(b['style']['backgroundColor'])}"] += 1
        elif a["style"]["color"] != b["style"]["color"]:
            ctr[f"text {colour(a['style']['color'])} to {colour(b['style']['color'])}"] += 1
        elif a["style"]["opacity"] != b["style"]["opacity"]:
            ctr[f"opacity {a['style']['opacity']} to {b['style']['opacity']}"] += 1
        else:
            ctr["no change on the element"] += 1


def top(ctr, n):
    return ", ".join(f"{k} ({v})" for k, v in ctr.most_common(n))


W(f"**Radius.** {top(radii, 10)}. Most of the interface is 8 (rows, icon buttons, menu items, list hover fills, the code block: the comfortable `--cds-radius`); 12 is cards, menus, dialogs and the user bubble (`rounded-card`, radius + 4); 7 and 6 are segmented tracks and their thumbs; 20 is the composer alone; 14 the Make something new tiles; 9999 avatars and switches.")
W()
W(f"**Hover.** Claude hovers with a translucent wash of the text colour. Dark: {top(hover_dark, 6)}. Light: {top(hover_light, 6)}. The wash is `fill.ghost-hover` (`rgba(255, 255, 255, 0.075)` in dark, `rgba(11, 11, 11, 0.05)` in light) on buttons, menu items and list rows; sidebar rows use `frame.hover`, the same wash in dark and a solid `#f0efec` in light; a selected row is `frame.selected` (15% white, or `#edece8`). A cds Button paints that fill on its inner `.cds-btn-squish` span, so the button itself reads \"no change\".")
W()
W(f"**Focus.** Of {focus_n['dark']} elements given a real keyboard focus in dark: {top(focus['dark'], 4)}. In light: {top(focus['light'], 4)}. The common ring is `shadow.focus`: a 1px inset of the page colour, a 1px `fill.accent` blue (`#2a78d6`) ring and a 6px blue glow, so focus reads as a blue outline with a halo. The composer's mic and voice buttons, the Thought for N s pill and the message actions use a 2px blue outline offset 2 instead. A row (sidebar row, Chats row, settings nav item) puts the ring on its inner link or button and the sidebar rows add the hover wash; a tab puts it on its inner button. The segmented controls (Chat/Cowork, the Theme picker) are radio groups whose checked radio takes the ring. Menu items take no ring: keyboard focus in a cds Menu is the same `fill.ghost-hover` wash as the pointer ([menu-item-keyboard](#menu-item-keyboard)). The one element that shows nothing is the search dialog's field row, whose focus is the caret in its text area. States named `refresh-focus-visible` were read on the 2026-10-17 copies for components whose 2026-10-04 copy had no focus reading.")
W()
W(f"**Motion.** {top(trans, 5)}. Buttons press on `duration.fast` (60 ms) and colour changes run 200 ms on the standard curve; the cds tokens name five durations (60, 120, 200, 300, 450 ms) and three curves (out, snap, overshoot), plus a `linear()` spring for button presses that DTCG cannot carry.")
W()
W("**Rings.** Claude draws hairlines as box-shadows, not borders: a 1px ring of `border.default` (10% ink) that sits outside the element in light (`--cds-ring-outer: 1px`) and inside it in dark (`--cds-ring-inner: 1px`). The composer, menus, dialogs and cards all carry it.")
W()
W("**Layout grid.** The sidebar is 288 wide on its own ground, the content column starts 8 further on and a 48 tall header runs over it. The home composer is 672 wide, the chat transcript 768, list pages a 960 column. On a phone the sidebar becomes a full-screen sheet. The numbers per page are in [raw/pages.md](raw/pages.md).")
W()

# --------------------------------------------------------------------------- components

W("## Components")
W()
groups = collections.OrderedDict()
for cid, c in C.items():
    groups.setdefault(c["group"], []).append(cid)
for g, ids in groups.items():
    W(f"### {g}")
    W()
    if g in GROUP_INTRO:
        W(GROUP_INTRO[g])
        W()
    for cid in ids:
        c = C[cid]
        W(f"#### {c['title']}")
        W()
        W(f"<a id=\"{cid}\"></a>`{cid}`, on {', '.join(c.get('pages') or [c['page']])}. {c.get('desc', '')}".rstrip())
        W()
        crops = []
        # The usual states first, then every other state that has a crop, so no captured image is left out.
        order = ("default", "hover", "light", "light-hover", "active", "selected", "checked", "on", "open", "typed", "pinned", "thread", "short", "focus-visible")
        for sname in [n for n in order if n in c["states"]] + sorted(n for n in c["states"] if n not in order):
            s = c["states"].get(sname)
            if s and s.get("crop") and Path(s["crop"]).exists():
                crops.append(f'<img src="{s["crop"]}" alt="{c["title"]}, {sname}" height="{min(120, max(24, round(s["rect"]["h"])))}"> ')
        if crops:
            W("".join(crops))
            W()
        rows = state_rows(c)
        if rows:
            W("| State | Values |")
            W("|---|---|")
            for name, d in rows:
                W(f"| {name} | {fmt(d)} |")
            W()
        cl = child_layers(c)
        if cl:
            W(f"Child layers: {cl}")
            W()
        vars_ = next((s.get("vars") for s in c["states"].values() if s.get("vars")), None)
        if vars_:
            W("Tokens named in its classes: " + ", ".join(f"`{k}`" for k in sorted(vars_)) + ".")
            W()

# --------------------------------------------------------------------------- icons

W("## Icon index")
W()
W(f"{len(icons)} icons were lifted from the pages into [icons/](icons), indexed in [icons/INDEX.tsv](icons/INDEX.tsv). Claude draws nearly every glyph with its own variable icon font, Anthropicons-Variable: one private-use character per icon in a `span[data-cds=Icon]`, at 12, 16 or 20 px, with the weight thinned as the size grows (577.8 at 12, 533.3 at 16, 433.3 at 20) so the stroke looks the same. [icons.mjs](tools/capture/icons.mjs) draws each glyph's outline from the font at the weight it was shown at; the names come from the labels of the controls they sat in. The few inline SVGs are the Claude wordmark, the clay asterisk, the incognito ghost, the voice bars and the GitHub mark. All are Anthropic's property (GitHub's mark is GitHub's), kept for reference only.")
W()
W("| Icon | Source | Sizes | Seen with |")
W("|---|---|---|---|")
for r in [r for r in icons if len(r) > 9]:
    W(f"| `{r[0].replace('.svg', '')}` | {'icon font ' + r[3] if r[1].startswith('Anthropicons') else 'inline svg'} | {r[4]} | {(r[9] or '-')[:70].replace('|', '/')} |")
W()

# --------------------------------------------------------------------------- gaps

W("## Gaps")
W()
W("- Captured 2026-10-04 from the owner's signed-in account (Max plan) in dark mode, at 1440 x 900 and 390 x 844. The light readings and screenshots come from the same copies with every `[data-mode]` set to light, which is all Claude's own switch does; no account setting changed. Anything Claude swaps per theme in JavaScript rather than CSS would not have swapped.")
W("- The capture pane was hidden, so the page ran no animation frames. Base UI clears a popup's `data-starting-style` and unmounts a closed one from a frame, so entrance animations froze and closed menus stayed mounted; [snapshot.js](tools/capture/signed-in/snapshot.js) drops closed popups and settles opening ones. Modal backdrops may render undimmed. The first model in the model menu shows a highlight that is the frozen keyboard highlight, not a hover. On the phone the drawer sheet could not be closed (its exit animation never ran), so it was hidden by hand before the phone chat copy.")
W("- Syntax-highlighted code keeps the dark theme's inline colours, so code colours in the light renders are not trustworthy; read them from the dark copies.")
W("- The thread is not virtualised: one copy rendered at three scroll positions (`thread-dark`, `-table` at 1150, `-followup` at 1780). Its replies hold a code block, a table and paragraphs but no visible heading or list; the prose heading sizes are in [raw/css-vars.json](raw/css-vars.json) (`--_prose-h*`), not measured. The user message carries the only list.")
W("- Artifact previews are iframes and render as dark boxes where present.")
W("- Hover and focus on the 390 wide copies were not measured (a phone has neither). The segmented controls' radio spans take no focus in a static copy, so their focus-visible state is skipped.")
W("- Refreshed 2026-10-17 with nine more copies (Forms and feedback, and the overlays marked with that date). The 2026-10-04 screenshots and crops were not retaken, so the two days sit side by side: the Artifacts page is a list in the first and a grid of cards in the second.")
W("- Focus was not read on the code block's copy button, the chat title's more button, search results, Artifacts list rows and a project's recent rows: their 2026-10-04 copies are gone and no 2026-10-17 copy shows them. The search dialog's field row shows no ring when its text area takes focus; the caret is the only sign.")
W("- A toast was not captured: the toast region is mounted on every page but stayed empty, and the actions that raise one change the account. The text field's error state was read by setting `data-invalid` on the copy, so its ring is Claude's own CSS but the message under the field was never seen. A button's loading state needs a sent message.")
W("- Streaming (a reply being written, the stop button), the artifact panel beside a chat, the Code mode, Cowork, the share sheet, and the Privacy, Billing and Usage settings panes were not captured: each would need sending a message or shows account and billing details.")
W("- Chat and artifact titles are the owner's own. The account's name was replaced with \"Learner\" and its email with an example address, and two health-related titles were replaced with neutral ones, by the redaction file, which lives outside the repository.")
W()

out = "\n".join(L) + "\n"
# The share is counted over what the entries actually say: every value written in a state row or a
# child-layer line, named (a backticked token with its value in brackets) or raw. Zeros need no token and
# a box's width is the instance's content width, so neither is counted.
entries = out[out.index("## Components"):out.index("## Icon index")]
written = "\n".join(l.split("|", 2)[2] for l in entries.split("\n") if l.startswith("| ") and not l.startswith("| State")) + "\n" + "\n".join(l for l in entries.split("\n") if l.startswith("Child layers"))
TOKEN = re.compile(r"`[a-z][\w.-]*(?: on this surface)?` \((?:[^()]|\([^()]*\))*\)|`fontSize\.[^(]*\((?:[^()]|\([^()]*\))*\)")
named = len(TOKEN.findall(written))
rest = re.sub(r"`[^`]*`", "", TOKEN.sub("TOKEN", written))
rest = re.sub(r"(?<![\w.])\d+(?:\.\d+)? x ", "", rest)  # content widths
rest = re.sub(r"and \d+ more", "", rest)
# a shadow no token holds is one raw value, however many layers it has
rest = re.sub(r"shadow (?!TOKEN)[^;|\n]*", "shadow RAWSHADOW", rest)
raw_shadows = rest.count("RAWSHADOW")
raw = [m.group(0) for m in re.finditer(r"#[0-9a-f]{6}|rgba?\([^)]*\)|cubic-bezier\([^)]*\)|[A-Z][a-z]+ [A-Z]?[a-z]* ?\d+/[\d.]+ \d+|(?<![\w.])\d+(?:\.\d+)?(?:px|ms|s)?(?![\w.])", rest) if not re.fullmatch(r"0(px|s)?", m.group(0))] + ["shadow"] * raw_shadows
out = out.replace("@@NAMED@@", f"Of the {named + len(raw)} values written in the state rows and child-layer lines below (zeros and content widths aside), {named} ({round(100 * named / (named + len(raw)))}%) name a token.")
open("components.md", "w").write(out)
print(f"components.md: {len(C)} components, {n_states} states, {n_crops} crops, {len(L)} lines")
