#!/usr/bin/env python3
"""Build components.md for the Gauth design reference.

Reads raw/components-computed.json (every component and state, measured), raw/layout.json,
tokens.json, screenshots/ and icons/INDEX.tsv, and writes components.md next to them. Every value
is a cell of the measurement file, written as the token in tokens.json that holds it: a colour is its
semantic token (light.*) or palette token, a radius, padding, border width, shadow, duration or press
scale its core or elevation token, and a text style its typography token when one matches exactly.
A value no token holds stays raw and is counted, so the share written in tokens is reported. A state
row shows only what differs from the first state. Adapted from the Coursera kit's builder, which read markdown; this one reads
the JSON directly.

Deterministic: re-running it on the same inputs reproduces components.md byte for byte.
Run from anywhere: python3 tools/build_components_md.py
"""
import json, os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
J = json.load(open("raw/components-computed.json"))
C = J["components"]
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


TOK = {}  # every token: name -> resolved value


def resolve(v, depth=0):
    if isinstance(v, str):
        m = re.fullmatch(r"\{([^{}]+)\}", v)
        if m and depth < 8:
            return resolve(TOK_RAW[m.group(1)], depth + 1)
        return v
    if isinstance(v, list):
        return [resolve(x, depth) for x in v]
    if isinstance(v, dict):
        return {k: resolve(x, depth) for k, x in v.items()}
    return v


TOK_RAW = {}
for set_ in ("core", "light"):
    for n, t in flat(T[set_]):
        TOK_RAW[n] = t["$value"]
TYPES = {n: t["$type"] for set_ in ("core", "light") for n, t in flat(T[set_])}
for n in TOK_RAW:
    TOK[n] = resolve(TOK_RAW[n])

# Which token names a value. Semantic roles first, then component colours, then the palette, so a
# colour reads as what it is for wherever Gauth gives it a role.
COLOR_ORDER = ["background.", "text.", "border.", "action.", "status.", "component.", "palette."]


STATEFUL = ("hover", "pressed", "link", "disabled", "on-accent", "selected", "surface", "raised", "overlay", "focus", "strong", "default")


def _rank(n):
    """Group order, then a plain role before a state- or use-specific one (text.meta before text.link-hover)."""
    leaf = n.rsplit(".", 1)[-1]
    return next((i for i, p in enumerate(COLOR_ORDER) if n.startswith(p)), 99), any(w in leaf for w in STATEFUL), n


def ckey(v):
    """A colour as a lookup key: an alpha rounded to two places, since #5058651a reads back as 0.1 when computed."""
    return re.sub(r"(rgba\(\d+, \d+, \d+, )([\d.]+)\)", lambda m: f"{m.group(1)}{round(float(m.group(2)), 2):g})", v)


BY_COLOR = {}
for n in sorted((n for n in TOK if TYPES[n] == "color"), key=_rank):
    BY_COLOR.setdefault(ckey(TOK[n]), n)

# The same colour can hold several roles (#21252e is both text.primary and action.primary), so a value is
# looked up by what it paints: a fill prefers background, action and status roles, text the text roles,
# a border or outline the border roles. Each falls back to the general order above.
ROLE_ORDER = {
    "fill": ["background.", "action.", "status.", "component.", "palette."],
    "fill-control": ["action.", "background.", "status.", "component.", "palette."],
    "text": ["text.", "status.", "action.", "component.", "palette."],
    "line": ["border.", "action.", "status.", "component.", "palette."],
}


def by_role(v, role):
    if role not in ROLE_ORDER:
        return BY_COLOR.get(ckey(v))
    names = [n for n in TOK if TYPES[n] == "color" and ckey(TOK[n]) == ckey(v)]
    if not names:
        return None
    if role == "fill" and _control[0]:
        role = "fill-control"
    order = ROLE_ORDER[role]
    # a token named for another job (action.primary-text is a label colour, not a fill) ranks last
    other = {"fill": ("text", "border", "line"), "fill-control": ("text", "border", "line"), "text": ("border", "line", "fill", "background", "bg"), "line": ("text", "fill", "background", "bg")}[role]

    def rank(n):
        leaf = n.rsplit(".", 1)[-1]
        wrong = any(w in leaf for w in other) or (role != "text" and n.startswith("text.")) or (role == "text" and n.startswith(("background.", "border.")))
        return wrong, next((i for i, p in enumerate(order) if n.startswith(p)), 99), any(w in leaf for w in STATEFUL), n
    return min(names, key=rank)
BY_DIM = {}
for grp in ("radius", "spacing", "spacing-offgrid", "borderWidth", "focus", "size"):
    for n in sorted(n for n in TOK if n.startswith(grp + ".") and TYPES[n] == "dimension"):
        BY_DIM.setdefault((grp, TOK[n]), n)
BY_DUR = {}
for n in sorted(n for n in TOK if n.startswith("duration.")):
    BY_DUR.setdefault(TOK[n], n)
BY_SCALE = {str(TOK[n]): n for n in sorted(n for n in TOK if n.startswith("scale."))}


def shadow_key(layers):
    return " | ".join(f"{l['color']} {l['offsetX']} {l['offsetY']} {l['blur']} {l['spread']}{' inset' if l.get('inset') else ''}" for l in layers)


BY_SHADOW = {}
for n in sorted((n for n in TOK if TYPES[n] == "shadow" and not n.startswith("elevation.level-")), key=lambda n: n):
    BY_SHADOW.setdefault(shadow_key(TOK[n]), n)
for n in sorted(n for n in TOK if n.startswith("elevation.level-")):
    BY_SHADOW[shadow_key(TOK[n])] = n  # a level names the shadow when one matches
def stack(f):
    return [x.strip().strip('"').strip("'") for x in f.split(",") if x.strip()]


# A measured family stack names its font family token: the token whose stack starts with the same family, else
# the one that lists it ("SF Pro" is fontFamily.sf-pro, whose stack opens with -apple-system for Apple devices).
FAMILIES = {n: stack(TOK[n]) for n in sorted(n for n in TOK if TYPES[n] == "fontFamily")}


def fam_token(f):
    """The family token sharing the longest opening run of families with the measured stack, else the one that
    lists its first family anywhere."""
    ms = stack(f)
    if not ms:
        return ""

    def run(st):
        k = 0
        while k < min(len(st), len(ms)) and st[k] == ms[k]:
            k += 1
        return k
    best = max(FAMILIES, key=lambda n: (run(FAMILIES[n]), n == "fontFamily.system"))
    if run(FAMILIES[best]) > 0:
        return best
    return next((n for n, st in FAMILIES.items() if ms[0] in st), ms[0])


def px2(v):
    """'20.0004px' -> '20px', '0.126px' -> '0.13px': lengths compared at two decimals, as computed styles drift."""
    if v in ("normal", "", None):
        return "0px"
    m = re.fullmatch(r"(-?[\d.]+)px", str(v))
    return f"{round(float(m.group(1)), 2):g}px" if m else str(v)


BY_TYPE = {}
for n in sorted(n for n in TOK if TYPES[n] == "typography"):
    v = TOK[n]
    BY_TYPE.setdefault((fam_token(TOK_RAW[n]["fontFamily"]) if TOK_RAW[n]["fontFamily"].startswith("{") is False else TOK_RAW[n]["fontFamily"].strip("{}"), px2(v["fontSize"]), px2(v["lineHeight"]), str(v["fontWeight"]), px2(v.get("letterSpacing", "0px"))), n)

USED = {}  # component -> tokens it cites
_cur = [None]
_control = [False]  # the entry being written is a button or link, so a fill reads as an action colour first


# Values are marked while the file is written (\x03token\x04, \x01raw\x02) so the entries can be counted;
# the marks become backticks and plain text before the file is saved.
def cite(name):
    if _cur[0]:
        USED.setdefault(_cur[0], set()).add(name)
    return f"\x03{name}\x04"


def raw(v):
    return f"\x01{v}\x02"


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def colour(c, tokens=True, role=None):
    """rgb()/rgba()/color(srgb) -> '`token`' (or the raw value when no token holds it). `role` (fill, text,
    line) picks the token for what the colour paints."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        if not tokens:
            return v
        tok = by_role(v, role)
        return cite(tok) if tok else raw(v)

    c = re.sub(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)",
               lambda m: label(norm(*(round(float(x) * 255) for x in m.group(1, 2, 3)), m.group(4))), c)
    return re.sub(r"rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)", lambda m: label(norm(*m.group(1, 2, 3), m.group(4))), c)


def dim(v, *groups):
    """'12px' -> '`radius.12`' from the first group that holds it, else the raw value."""
    if v in ("0px", "auto", "normal", "none"):
        return v
    for g in groups:
        n = BY_DIM.get((g, v))
        if n:
            return cite(n)
    return raw(v)


def dim_named(v, names):
    """'2px' -> the first of `names` whose value it is (outline width is focus.width, not focus.offset)."""
    for n in names:
        if TOK.get(n) == v:
            return cite(n)
    return dim(v, "focus", "borderWidth")


def dims(v, *groups):
    return " ".join(dim(x, *groups) for x in v.split())


def shadow(css):
    """A computed box-shadow -> its elevation token, else the raw layers."""
    layers = []
    for part in re.split(r",(?![^(]*\))", css):
        m = re.match(r"\s*(rgba?\([^)]*\))\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+(-?[\d.]+px)(\s+inset)?", part)
        if not m:
            return None
        col = colour(m.group(1), tokens=False)
        if col == "transparent":
            continue
        layers.append({"color": col, "offsetX": m.group(2), "offsetY": m.group(3), "blur": m.group(4), "spread": m.group(5), "inset": bool(m.group(6))})
    if not layers:
        return ""
    n = BY_SHADOW.get(shadow_key(layers))
    if n:
        return cite(n)
    return raw(", ".join(f"{l['offsetX']} {l['offsetY']} {l['blur']} {l['spread']} {l['color']}{' inset' if l['inset'] else ''}" for l in layers))


def typeset(fz, lh, fw, f, ls="normal"):
    """A text style -> its typography token when family, size, line height, weight and letter spacing all
    match; otherwise the measured style, with its letter spacing when it is not zero."""
    ls = px2(ls)
    n = BY_TYPE.get((fam_token(f), px2(fz), px2(lh) if lh != "normal" else "normal", str(fw), ls))
    return cite(n) if n else raw(font(fz, lh, fw, f) + (f", letter spacing {ls}" if ls != "0px" else ""))


KEYWORD_EASE = {"ease": [0.25, 0.1, 0.25, 1], "ease-in-out": [0.42, 0, 0.58, 1], "ease-in": [0.42, 0, 1, 1], "ease-out": [0, 0, 0.58, 1], "linear": [0, 0, 1, 1]}


def easing(e):
    """A timing function -> its core.easing token (CSS keywords compared by their curves), else the raw value."""
    m = re.fullmatch(r"cubic-bezier\(([^)]*)\)", e)
    curve = [round(float(x), 3) for x in m.group(1).split(",")] if m else KEYWORD_EASE.get(e)
    if curve:
        n = next((n for n in sorted(TOK) if n.startswith("easing.") and [round(float(x), 3) for x in TOK[n]] == curve), None)
        if n:
            return cite(n)
    return raw(e)


def dur_ms(d):
    return float(d[:-1]) * 1000 if d.endswith("s") and not d.endswith("ms") else float(d[:-2])


def sides(t, r, b, l):
    if t == r == b == l:
        return t
    if t == b and r == l:
        return f"{t} {r}"
    return f"{t} {r} {b} {l}"


def fam(f):
    return f.split(",")[0].replace('"', "")


def num(x):
    x = str(x)
    return re.sub(r"(\d+\.\d\d)\d+", r"\1", x)


def font(fz, lh, fw, f):
    lh = lh.replace("px", "") if lh != "normal" else "normal"
    return f"{fam(f)} {num(fz.replace('px', ''))}/{num(lh)} {fw}"


def props(v):
    s = v["style"]
    o = {}
    o["size"] = f"{num(v['rect']['w'])} x {num(v['rect']['h'])}"
    pad = sides(s["paddingTop"], s["paddingRight"], s["paddingBottom"], s["paddingLeft"])
    if pad != "0px":
        o["padding"] = dims(pad, "spacing", "spacing-offgrid")
    bds = []
    for d in ("Top", "Right", "Bottom", "Left"):
        if float(s[f"border{d}Width"].replace("px", "")) > 0 and s[f"border{d}Style"] != "none":
            bds.append(f"{dim_named(s[f'border{d}Width'], ['borderWidth.hairline', 'borderWidth.strong', 'borderWidth.choice', 'borderWidth.indicator'])} {s[f'border{d}Style']} {colour(s[f'border{d}Color'], role='line')}")
        else:
            bds.append("none")
    if any(b != "none" for b in bds):
        o["border"] = bds[0] if len(set(bds)) == 1 else "; ".join(f"{'TRBL'[i]}: {b}" for i, b in enumerate(bds) if b != "none")
    rad = sides(s["borderTopLeftRadius"], s["borderTopRightRadius"], s["borderBottomRightRadius"], s["borderBottomLeftRadius"])
    if rad != "0px":
        o["radius"] = dims(rad, "radius")
    o["background"] = colour(s["backgroundColor"], role="fill")
    if s["backgroundImage"] != "none":
        img = re.sub(r'url\("data:[^)]*\)', "an image (data URI)", s["backgroundImage"])
        o["image"] = colour(img)[:200]
    if s["boxShadow"] != "none":
        sh = shadow(s["boxShadow"])
        if sh is None:
            sh = colour(s["boxShadow"], tokens=False)
            layers = [x.strip() for x in re.split(r",(?![^(]*\))", sh)]
            sh = raw(", ".join(x for x in layers if not x.startswith("transparent")))
        if sh:
            o["shadow"] = sh
    if s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0:
        o["outline"] = f"{dim_named(s['outlineWidth'], ['focus.width', 'borderWidth.focus'])} {s['outlineStyle']} {colour(s['outlineColor'], role='line')}, offset {dim_named(s['outlineOffset'], ['focus.offset', 'focus.offset-astryx']) if s['outlineOffset'] != '0px' else '0px'}"
    if "outline" not in o:
        # a focus ring drawn by a child (the link inside a pagination item) or by a parent
        ring = next((p for p in v.get("paint", [])[1:] if p.get("outline")), None)
        if ring:
            o["outline"] = f"on {re.sub(r'[.].*$', '', ring['node'])}: {colour(ring['outline'], role='line')}"
        else:
            anc = next((a for a in v.get("ancestors", []) if a.get("outline") and not a["outline"].startswith(("0px", "medium none")) and "none" not in a["outline"]), None)
            if anc:
                o["outline"] = f"on its parent: {colour(anc['outline'], role='line')}"
    t = v.get("textStyle")
    if not t and (v.get("icon") or not v.get("text")):
        pass  # an icon-only control or an empty box draws no text, so it has no text style to record
    elif t:
        o["text"] = f"{typeset(t['fontSize'], t['lineHeight'], t['fontWeight'], t['fontFamily'], t.get('letterSpacing', 'normal'))}, {colour(t['color'], role='text')}"
    else:
        o["text"] = f"{typeset(s['fontSize'], s['lineHeight'], s['fontWeight'], s['fontFamily'], s.get('letterSpacing', 'normal'))}, {colour(s['color'], role='text')}"
    if s["transitionDuration"] not in ("0s", ""):
        props_ = [x.strip() for x in s["transitionProperty"].split(",")]
        durs = [x.strip() for x in s["transitionDuration"].split(",")]
        tf = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", s["transitionTimingFunction"])
        parts = []
        for i, p in enumerate(props_):
            d = durs[i % len(durs)]
            if d == "0s":
                continue
            ms = f"{round(dur_ms(d))}ms"
            parts.append(f"{p} {cite(BY_DUR[ms]) if ms in BY_DUR else raw(d)} {easing(tf[i % len(tf)]) if tf else ''}".strip())
        if parts:
            o["transition"] = ", ".join(parts)
    if s["transform"] not in ("none", "matrix(1, 0, 0, 1, 0, 0)"):
        m = re.fullmatch(r"matrix\(([\d.]+), 0, 0, ([\d.]+), (-?[\d.]+), (-?[\d.]+)\)", s["transform"])
        if m and m.group(1) == m.group(2) and m.group(3) == m.group(4) == "0":
            o["transform"] = f"scale {cite(BY_SCALE[m.group(1)])}" if m.group(1) in BY_SCALE else f"scale({raw(m.group(1))})"
        elif m and m.group(1) == m.group(2) == "1":
            o["transform"] = f"translate({m.group(3)}px, {m.group(4)}px)"
        else:
            o["transform"] = s["transform"]
    if s["opacity"] != "1":
        o["opacity"] = s["opacity"]
    if v.get("icon") and v["icon"]["w"] > 0 and v["icon"]["w"] < 120:
        o["icon"] = f"{num(v['icon']['w'])} x {num(v['icon']['h'])}, {colour(v['icon']['color'], role='text')}"
    if v.get("placeholder"):
        o["placeholder"] = colour(v["placeholder"]["color"], role="text")
    return o


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "outline", "text", "transition", "transform", "opacity", "icon", "placeholder"]


def state_rows(c):
    states = [s for s in c["states"] if "style" in c["states"][s]]
    if not states:
        return [], states
    base = props(c["states"][states[0]])
    rows = [(states[0], base)]
    same = []
    for st in states[1:]:
        p = props(c["states"][st])
        diff = {k: p[k] for k in ORDER if k in p and p.get(k) != base.get(k)}
        for k in ORDER:
            if k in base and k not in p:
                diff[k] = "none"
        if not diff:
            same.append(st)
            continue
        if rows[-1][0] != states[0] and rows[-1][1] == diff:
            rows[-1] = (rows[-1][0] + ", " + st, diff)
        else:
            rows.append((st, diff))
    if same:
        rows[0] = (f"{states[0]} (same: {', '.join(same)})", base)
    return rows, states


def fmt(d):
    return "; ".join(f"{k} {d[k]}" for k in ORDER if k in d).replace("|", "/")


def child_layers(c):
    st = next((s for s in c["states"].values() if "style" in s), None)
    if not st or not st.get("paint"):
        return None
    s = st["style"]
    if s["backgroundColor"] != "rgba(0, 0, 0, 0)" or s["boxShadow"] != "none" or s["borderTopWidth"] != "0px" or s["backgroundImage"] != "none":
        return None
    out = []
    for p in st["paint"][:3]:
        bits = [re.sub(r"\..*$", "", p["node"]) if "::" not in p["node"] else p["node"].split(".")[0], p["size"].replace(".0x", "x").replace(".0", "")]
        if p.get("bg"):
            bits.append("background " + colour(p["bg"], role="fill"))
        if p.get("bgImage"):
            bits.append("image " + colour(p["bgImage"])[:90])
        if p.get("border"):
            bw, _, bc = p["border"].split(" | ")[0][2:].partition(" solid ")
            bits.append("border " + (f"{dim_named(bw, ['borderWidth.hairline', 'borderWidth.strong', 'borderWidth.choice', 'borderWidth.indicator'])} solid {colour(bc, role='line')}" if bc else colour(p["border"].split(" | ")[0][2:], role="line")))
        if p.get("radius"):
            bits.append("radius " + dims(p["radius"], "radius"))
        if p.get("shadow"):
            sh = shadow(p["shadow"])
            bits.append("shadow " + (sh if sh is not None else colour(p["shadow"], tokens=False)))
        out.append(" ".join(bits))
    return "; ".join(out).replace("|", "/")


# --------------------------------------------------------------------------- page and group text

PAGE_NAME = {"home": "Homework home", "science": "Academy (Science Labs)", "math": "Academy (Math Curriculum)", "history": "Academy (History Signature)",
             "my": "Academy (My Course)", "unit": "unit", "lesson-science": "science lesson", "lesson-math": "math lesson",
             "lesson-history": "history lesson", "atlas": "Atlas", "story": "Atlas story", "news": "Insights",
             "plus": "Gauth PLUS plans", "blog": "Blog"}

GROUP_INTRO = {
    "Shell and navigation": "The app shell shared by Homework, Academy and Insights: a fixed 220px sidebar and a 60px top bar over the content. The sidebar is white with a cool grey current item on Homework and Insights, and takes the warm `#faf9f5` ground with a beige current item on Academy. Atlas and the lesson players have shells of their own (their groups below).",
    "Homework home": "The question-first home page: a serif hero over a lilac gradient, the question field, an upload panel and subject chips, then marketing sections. Nothing was ever sent or uploaded.",
    "Academy catalogue": "The course catalogue: the Playfair title and Create Course, four category tabs, then course sections of card grids. Science Labs and History Signature use cover cards with a progress track; Math Curriculum uses unit cards with an 80px cover tile.",
    "Unit page": "A math course's page: a back link, a tinted course banner, the unit rail at the left and the topic path at the right, with a floating Start panel.",
    "Lesson player: science canvas": "The science player is built in Astryx, a separate design system (`astryx-*` classes, StyleX variables, the \"stone\" theme): a narrated canvas that pans by itself, a section rail, transport controls and a docked Ask Tutor bar. Its focus ring is the only blue one on the site.",
    "Lesson player: math": "The math player puts a tutor column at the left and the slide in a white frame at the right, on the warm ground.",
    "Lesson player: history": "The history player is immersive: chapter pills at the top, the scene in the middle, a play disc and a caption line.",
    "Atlas": "Atlas has its own shell (a 56px header and a 230px drawer), a prompt box, recommendation chips and a grid of story cards. A story opens as a video preview, then a story page.",
    "Insights": "The news and blog list in the app shell, and the blog's pagination.",
    "Plans page": "`/plus`, the plans page the top bar's Upgrade opens: two plan cards and a real `<table>` comparing them. Read only; no button on it was pressed.",
    "Dialogs and overlays": "The promo dialog every page opens with, the Sign in dialog, the Gauth PLUS dialog, the Create a Course dialog, the science player's audio dialog, the math player's audio gate and the Atlas story preview. The promo's overlay is `rgba(15, 17, 20, 0.45)`; Gauth's own dialogs sit on `rgba(31, 35, 43, 0.7)`. Dialogs were opened and closed again: nothing in them was submitted, chosen or bought.",
    "Mobile (390 wide)": "A few components as a phone draws them, at 390 x 844 with an iPhone user agent.",
}

SHOTS = [
    ("home", "Homework home. Serif hero, question field, upload panel, subject chips, then the Atlas, AI solution and live tutor bands, comments and the footer. The promo dialog, the field focused and the folded sidebar captured.", "/"),
    ("academy-science", "Academy, Science Labs. Title, Create Course, tabs, course sections of lesson cards.", "/course/science"),
    ("academy-math", "Academy, Math Curriculum. Unit cards, six per course, and Show more expanded (the toolbar sticks with Create Course in it).", "/course/math"),
    ("academy-history", "Academy, History Signature. Illustrated lesson cards.", "/course/history"),
    ("academy-my", "Academy, My Course. The signed-out empty state, and the Create a Course dialog.", "/course/my"),
    ("unit", "Unit page (Algebra 1). Banner, unit rail, topic path, Start panel; scrolled down the path; Unit 2 chosen in the rail.", "/course/math/algebra-1?unit=real-numbers-and-sets"),
    ("lesson-science", "Science lesson. The audio dialog, the first chapter, Settings open, the Playback speed menu, a tooltip, Ask Tutor opened, a figure with its callout and list, a quiz, and the quiz answered (its result card).", "/course/science/how-things-work-1/learn"),
    ("lesson-math", "Math lesson. The audio gate, the playing slide with the tutor column, the chapters panel.", "/course/math/algebra-1/fundamentals-of-set-theory/learn"),
    ("lesson-history", "History lesson. The opening scene, the chapter panel.", "/course/history/crossing-the-ocean-wall/learn"),
    ("atlas", "Atlas. Landing, prompt box, chips, Popular Stories, FAQ; a story card's video preview; the Apollo 11 story page, and its Video Settings popover.", "/atlas"),
    ("news", "Insights. Breadcrumb, News and Blog tabs, featured article, article rows.", "/news"),
    ("blog", "Blog. The article list and its pagination.", "/blog"),
    ("signin", "Sign in dialog, opened from the top bar.", "/"),
    ("plus-dialog", "Gauth PLUS dialog, opened from the sidebar card's Start Free Trial.", "/"),
    ("plus", "Plans page. Two plan cards and the features-by-plan table.", "/plus"),
    ("footer", "Footer language select, opened.", "/"),
]
MOBILE = [
    ("mobile-home", "Homework home at 390: the promo dialog, the hero, the full page with the app banner.", "/"),
    ("mobile-academy", "Academy at 390: Math Curriculum (Science Labs is not offered on a phone).", "/course/math"),
    ("mobile-unit", "Unit page at 390, and scrolled down the path.", "/course/math/algebra-1?unit=real-numbers-and-sets"),
    ("mobile-lesson-math", "Math lesson at 390: the audio gate and the slide.", "/course/math/algebra-1/fundamentals-of-set-theory/learn"),
    ("mobile-atlas", "Atlas at 390, and a story page (Artemis II).", "/atlas"),
]

L = []


def W(s=""):
    L.append(s)


shots = sorted(p.name for p in Path("screenshots").glob("*.png"))


def links(prefix):
    out = []
    for f in shots:
        m = re.fullmatch(re.escape(prefix) + r"-light-(.+)\.png", f)
        if m:
            out.append(f"[{m.group(1)}](screenshots/{f})")
    return ", ".join(out)


n_crops = len(list(Path("components/crops").glob("*.png")))
n_states = sum(len(c["states"]) for c in C.values())
icons = [r.split("\t") for r in open("icons/INDEX.tsv").read().strip().split("\n")[1:]]

W("# Gauth components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from www.gauth.com on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent or uploaded.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [raw/pages.md](raw/pages.md).")
W()
W("How to read an entry:")
W()
W("- Every value is written as the token in [tokens.json](tokens.json) that holds it: a colour as the role token for what it paints (a fill as `action.*` or `background.*`, text as `text.*`, a border or outline as `border.*`) or, failing that, its palette token; a radius, padding, border width, focus ring, shadow, duration or press scale as its core or elevation token; text as its typography token, then its colour. A value no token holds is written raw (a text style as family size/line-height weight, for example `SF Pro 14/21 500`). {{TOKEN_SHARE}}. Each entry ends with the list of tokens it uses. Sizes are the element's measured box and stay in px.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (Gauth has one theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).")
W()
W("| Surface | URL | Screenshots |")
W("|---|---|---|")
for p, desc, url in SHOTS + MOBILE:
    W(f"| {desc} | `{url}` | {links(p)} |")
W()
W("### Overlays and transient states")
W()
W("| State | Where | How it was reached | Captured |")
W("|---|---|---|---|")
OVER = [
    ("Promo dialog (\"Introducing Gauth Academy\")", "every page, on load", "at rest; then dismissed with its own close button for every other capture", "[home-light-promo](screenshots/home-light-promo.png), [promo-dialog](#promo-dialog)"),
    ("Create a Course dialog", "Academy", "Create Course pressed (opens the dialog); a prompt typed and deleted, no suggestion pressed", "[academy-my-light-create-dialog](screenshots/academy-my-light-create-dialog.png), [create-a-course-dialog](#create-a-course-dialog)"),
    ("Enable audio dialog", "science lesson", "on load; Not now pressed, Enable audio never pressed", "[lesson-science-light-audio-dialog](screenshots/lesson-science-light-audio-dialog.png)"),
    ("Audio gate", "math lesson", "on load; Continue pressed to start playback", "[lesson-math-light-audio-gate](screenshots/lesson-math-light-audio-gate.png)"),
    ("Settings popover", "science lesson", "the lesson's Settings button", "[lesson-science-light-settings](screenshots/lesson-science-light-settings.png)"),
    ("Ask Tutor, opened", "science lesson", "clicked into the bar; sample text typed and deleted, nothing sent", "[lesson-science-light-ask-tutor](screenshots/lesson-science-light-ask-tutor.png)"),
    ("Quiz", "science lesson", "reached by letting the lesson play about three minutes", "[lesson-science-light-quiz](screenshots/lesson-science-light-quiz.png)"),
    ("Quiz answered", "science lesson", "the last option of the practice check-in picked; the check-in comes back as a result card in the notes", "[lesson-science-light-quiz-answered](screenshots/lesson-science-light-quiz-answered.png), [quiz-result-card](#quiz-result-card)"),
    ("Playback speed menu", "science lesson", "Settings, then its Speed row; no speed chosen", "[lesson-science-light-speed-menu](screenshots/lesson-science-light-speed-menu.png), [playback-speed-menu](#playback-speed-menu)"),
    ("Tooltip", "science lesson", "hovering a header control", "[lesson-science-light-tooltip](screenshots/lesson-science-light-tooltip.png), [tooltip](#tooltip)"),
    ("Sign in dialog", "every page with the top bar", "the top bar's Sign in; a throwaway string typed into the email field and deleted, nothing submitted", "[signin-light-dialog](screenshots/signin-light-dialog.png), [sign-in-dialog](#sign-in-dialog)"),
    ("Sign in, enabled", "Sign in dialog", "name@example.com typed so the brand-red button enables; never pressed", "[signin-light-filled](screenshots/signin-light-filled.png), [primary-button-brand-red-sign-in](#primary-button-brand-red-sign-in)"),
    ("Sign-up view", "Sign in dialog", "its Sign up link; the password field focused (never typed into) to show its rule line", "[signin-light-signup-focused](screenshots/signin-light-signup-focused.png), [field-helper-text](#field-helper-text)"),
    ("Field error (forced)", "Sign in dialog", "Gauth's own form_error class added to the email field in DevTools; its error shows only after a submit", "[text-field-error-forced](#text-field-error-forced)"),
    ("Quiz answered right", "science lesson", "a second visit, the option naming lift, thrust and climb cost picked", "[quiz-result-card-right-answer](#quiz-result-card-right-answer)"),
    ("Gauth PLUS dialog", "every page with the sidebar", "the sidebar card's Start Free Trial; nothing chosen, typed or bought", "[plus-dialog-light-default](screenshots/plus-dialog-light-default.png), [gauth-plus-dialog](#gauth-plus-dialog)"),
    ("Language list", "footer", "the footer's language select; no language chosen", "[footer-light-language-open](screenshots/footer-light-language-open.png), [select-list-language](#select-list-language)"),
    ("Chapters panel", "math and history lessons", "the chapters button", "[lesson-math-light-chapters](screenshots/lesson-math-light-chapters.png), [lesson-history-light-chapters](screenshots/lesson-history-light-chapters.png)"),
    ("Show more", "Math Curriculum", "the Show 14 more button", "[academy-math-light-show-more](screenshots/academy-math-light-show-more.png)"),
    ("Folded sidebar", "Homework home", "the sidebar's collapse button", "[home-light-sidebar-folded](screenshots/home-light-sidebar-folded.png)"),
    ("Story preview", "Atlas", "a story card pressed (opens a video preview)", "[atlas-light-story-preview](screenshots/atlas-light-story-preview.png)"),
    ("Story page", "Atlas", "Explore in the preview (opens the published story)", "[atlas-light-story](screenshots/atlas-light-story.png), [mobile-atlas-light-story](screenshots/mobile-atlas-light-story.png)"),
    ("Video Settings popover", "Atlas story", "hovering Generate Video; nothing in it pressed", "[atlas-light-story-video-settings](screenshots/atlas-light-story-video-settings.png)"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ checklist coverage
CHECKLIST = [
    ("Button", ["start-button", "create-button", "accent-button", "audio-not-now", "start-free-button", "join-button", "signin-submit"]),
    ("Icon button", ["canvas-control", "canvas-exit", "header-round-button", "page-nav", "modal-close"]),
    ("Link", ["inline-link", "footer-link", "terms-link", "signup-link", "back-link"]),
    ("Text field", ["signin-email", "field-focused", "field-error", "field-helper", "question-box", "atlas-search", "header-question", "tutor-input"]),
    ("Text area", ["atlas-textarea", "atlas-composer", "create-prompt"]),
    ("Select", ["language-select", "language-list", "language-option-selected", "language-option"]),
    ("Checkbox", []),
    ("Radio", ["quiz-option", "plan-card", "plan-card-selected"]),
    ("Switch", ["switch", "search-toggle"]),
    ("Tabs", ["category-tab", "category-tab-active", "pill-tab", "pill-tab-active"]),
    ("Menu", ["settings-popover", "speed-menu", "menu-item", "menu-item-selected"]),
    ("Tooltip", ["tooltip"]),
    ("Dialog", ["signin-dialog", "plus-dialog", "create-dialog", "audio-dialog", "promo-dialog"]),
    ("Toast", []),
    ("Card", ["lesson-card", "unit-card", "story-card", "plan-box", "review-card"]),
    ("List row", ["article-row", "chapter-option", "chapter-panel-item", "unit-button", "benefits-row"]),
    ("Table", ["plan-table", "plan-table-row", "benefits-table"]),
    ("Avatar", ["review-avatar"]),
    ("Badge", ["new-badge", "plan-tag", "video-badge"]),
]
WHY_NOT = {
    "Checkbox": "not present on any public page; no public form has one",
    "Toast": "not seen: no toast appeared after any action the capture took signed out",
}


def anchor(c):
    return re.sub(r"[^a-z0-9 -]", "", c["title"].lower()).replace(" ", "-")


W("## Checklist coverage")
W()
present = [n for n, ks in CHECKLIST if any(k in C and not C[k].get("missing") for k in ks)]
W(f"The 19 components of the library's checklist ([docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md)), each with the entries below that show it and the states captured across them. {len(present)} of 19 are captured.")
W()
W("| Component | Entries | States captured |")
W("|---|---|---|")
for name, keys in CHECKLIST:
    ks = [k for k in keys if k in C and not C[k].get("missing")]
    if not ks:
        W(f"| {name} | not captured: {WHY_NOT[name]} | - |")
        continue
    sts = []
    for k in ks:
        for st, v in C[k]["states"].items():
            if "style" in v and st not in sts:
                sts.append(st)
    W(f"| {name} | " + ", ".join(f"[{C[k]['title']}](#{anchor(C[k])})" for k in ks) + " | " + ", ".join(sts) + " |")
W()

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement files.")
W()
def focus_change(c):
    """What keyboard focus changes against the first state: an outline (on the element, a child or a
    parent), a shadow ring, the border colour or the fill. None when it changes nothing visible."""
    st = c["states"].get("focus-visible")
    first = next((v for v in c["states"].values() if "style" in v), None)
    if not st or "style" not in st or first is st:
        return None
    a, b = props(first), props(st)
    bits = []
    if b.get("outline") and b.get("outline") != a.get("outline"):
        bits.append("outline " + b["outline"])
    for key, label in (("shadow", "shadow ring"), ("border", "border"), ("background", "fill")):
        if b.get(key) and b.get(key) != a.get(key):
            bits.append(f"{label} {b[key]}")
    return "; ".join(bits) or None


_cur[0] = None
foc = []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st or "style" not in st:
        continue
    foc.append((k, focus_change(c)))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} show a visible change (an outline on the element, a child or a parent, a shadow ring, a border or a fill): {', '.join(with_ring)}. The other {len(without)} change nothing, so a keyboard user sees no focus: {', '.join(without)}. The Upgrade and Sign in buttons in the top bar are a `div` and a `span` and cannot take focus at all.")
W()
W("**Pressed.** Gauth's own button component, the brand-red primary in the Sign in dialog, darkens when pressed (`action.accent` `#ff013e`, hover `#f00039`, pressed `#d80033`). The learning pages' buttons shrink instead of changing colour much: Create, Start, Create Course and the Astryx buttons scale to 0.98, the math player's round buttons to 0.94, the promo button to 0.99. Cards deepen their shadow on hover and keep it when pressed.")
W()
W("**Motion.** Transitions measured on the components, by duration.")
W()
W("| Duration | Easing | Property | Where |")
W("|---|---|---|---|")
mot = {}
for k, c in C.items():
    for st in c["states"].values():
        if "style" not in st:
            continue
        s = st["style"]
        if s["transitionDuration"] in ("0s", ""):
            continue
        props_ = [x.strip() for x in s["transitionProperty"].split(",")]
        durs = [x.strip() for x in s["transitionDuration"].split(",")]
        tfs = re.findall(r"cubic-bezier\([^)]*\)|[a-z-]+", s["transitionTimingFunction"])
        for i, p in enumerate(props_):
            d = durs[i % len(durs)]
            if d == "0s":
                continue
            key = (d, tfs[i % len(tfs)] if tfs else "")
            ent = mot.setdefault(key, (set(), set()))
            ent[0].add(p)
            ent[1].add(k)
        break


for (d, e), (ps, ks) in sorted(mot.items(), key=lambda kv: (dur_ms(kv[0][0]), kv[0][1])):
    W(f"| {d} | `{e}` | {', '.join(sorted(ps))} | {', '.join(sorted(ks)[:8])}{' and more' if len(ks) > 8 else ''} |")
W()
W("**Layout grid.** Read on each page at each width ([raw/layout.json](raw/layout.json)).")
W()
W("| Page | 1440 | 1920 | 1024 | 390 |")
W("|---|---|---|---|---|")


def grid_of(key):
    v = LAYOUT.get(key)
    if not v:
        return "-"
    g = v["grids"][0] if v["grids"] else None
    cols = re.sub(r"(\d+\.\d)\d*px", r"\1", g["cols"]).replace("px", "") if g else ""
    main = f"content x {v['main']['x']}, {v['main']['w']} wide" if v["main"]["w"] else "content full width"
    return f"{main}; grid {cols} gap {g['colGap']}" if g else main


for page in ["home", "academy-science", "academy-math", "unit", "lesson-math", "atlas"]:
    W(f"| {page} | " + " | ".join(grid_of(f"{page}@{w}") for w in (1440, 1920, 1024, 390)) + " |")
W()
W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
for k in ["lesson-card", "unit-card", "story-card", "feature-card", "solution-option", "create-suggestion", "quiz-card", "quiz-option", "learning-panel", "settings-popover", "chapters-panel", "video-settings", "view-rail", "m-unit-card"]:
    c = C.get(k)
    if not c:
        continue
    st = next(iter(c["states"].values()))
    if "style" not in st:
        continue
    p = props(st)
    if ("radius" not in p or p["background"] == "transparent") and st.get("paint"):
        p0 = next((x for x in st["paint"] if x.get("bg") and x.get("radius")), st["paint"][0])
        bw, _, bc = (p0.get("border") or "").split(" | ")[0][2:].partition(" solid ")
        sh = shadow(p0["shadow"]) if p0.get("shadow") else None
        p = dict(p, border=f"{dim_named(bw, ['borderWidth.hairline', 'borderWidth.strong', 'borderWidth.choice', 'borderWidth.indicator'])} solid {colour(bc, role='line')}" if bc else "-",
                 radius=dims(p0["radius"], "radius") if p0.get("radius") else "-", background=colour(p0.get("bg", ""), role="fill") or "-",
                 shadow=sh if sh else (colour(p0.get("shadow", ""), tokens=False) or "none"))
    W(f"| [{c['title']}](#{re.sub(r'[^a-z0-9 -]', '', c['title'].lower()).replace(' ', '-')}) | {p['size']} | {p.get('border', '-')} | {p.get('radius', '-')} | {p.get('background', '-')} | {p.get('shadow', 'none')} | {p.get('padding', '0')} |")
W()

# ------------------------------------------------ entries
W("## Components")
ENTRY_START = len(L)
groups = [g for g in GROUP_INTRO if any(c["group"] == g for c in C.values())]
for c in C.values():
    if c["group"] not in groups:
        groups.append(c["group"])
for g in groups:
    W()
    W(f"### {g}")
    W()
    W(GROUP_INTRO.get(g, ""))
    for k, c in C.items():
        if c["group"] != g:
            continue
        _cur[0] = k
        _control[0] = bool(re.search(r"button|link|chip|tab|toggle|arrow|pagination item|option|close", c["title"], re.I))
        W()
        W(f"#### {c['title']}")
        desc = (c.get("desc") or "").strip()
        if desc and not desc.endswith((".", ")", '"')):
            desc += "."
        where = PAGE_NAME.get(c["page"], c["page"])
        W(f"{desc + ' ' if desc else ''}Read as `{k}` on the {where} page{' at 390 wide' if g.startswith('Mobile') else ''}.")
        W()
        if c.get("missing"):
            W("Not on the page when it was captured.")
            continue
        rows, states = state_rows(c)
        if len(states) == 1 and rows:
            W(f"**Values ({states[0]}).** {fmt(rows[0][1])}.")
            W()
        elif rows:
            W("| State | Values (later rows list only what changes from the first row) |")
            W("|---|---|")
            for lab, d in rows:
                W(f"| {lab} | {fmt(d)} |")
            W()
        cl = child_layers(c)
        if cl:
            W(f"Child layers that carry the look: {cl}.")
            W()
        used = sorted(USED.get(k, ()))
        if used:
            W("**Tokens.** " + ", ".join(f"`{u}`" for u in used) + ".")
            W()
        imgs = [f"![{c['title']} {st}](components/crops/{os.path.basename(c['states'][st]['crop'])})" for st in states if c["states"][st].get("crop")]
        W(" ".join(imgs) if imgs else "No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.")

ENTRY_END = len(L)
_cur[0] = None

# ------------------------------------------------ icons
W()
W("## Icons")
W()
W(f"{len(icons)} SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Lesson content (the canvas, slides and formulas) was left out; these are the interface icons. The SVGs are Gauth's property, kept for reference only.")
W()
W("| Icon | Rendered sizes | View box | Style | Seen on | Next to |")
W("|---|---|---|---|---|---|")
for r in icons:
    f, name, h, sizes, vb, style, seen, place, label = (r + [""] * 9)[:9]
    W(f"| [{name}](icons/{f}) | {sizes} | {vb} | {style} | {seen} | {label.replace('|', '/')[:60]} |")
W()

# ------------------------------------------------ gaps
W("## Gaps")
W()
W("### Pages")
W()
W("- **Signed-in pages.** Nothing behind sign-in was captured: a learner's own My Course list, course progress, history, the homework answer page, Atlas topics a learner made, account settings and the subscription checkout. The kit never signs in.")
W("- **Anything that sends or creates.** No homework question was submitted (so the answer and step-by-step pages are missing), no course was generated from Create a Course, no tutor message or voice question was sent, no Atlas story was generated, no file was uploaded, and no dialog was submitted. The answers given are to the science lesson's practice check-in, once wrong and once right on two visits, which a signed-out visitor answers as part of the lesson.")
W("- **Toast and checkbox.** Neither was seen. No toast appeared after any action the capture took, and no public form has a checkbox; the Sign in dialog states its terms in a line of text instead.")
W("- **Study Resources.** `/study-resources/*` redirects to gauthmath.com, which answers a headless browser with Access Denied.")
W("- **The science lesson's Completed screen** (a cover, a laurel \"Completed\" title, Share and View Canvas) was seen while exploring, after a lesson played to its end, but the kit does not wait the several minutes it takes, so there is no crop or measurement.")
W("- **Mobile science lessons.** A phone is redirected from `/course/science` to `/course/math`; Science Labs is not offered on a phone.")
W("- **Other lesson kinds.** Math lessons carry interactive steps (matching, drag, number lines, flashcards, graphs; their CSS is in the stylesheets) that only appear as a lesson plays on; the capture saw the first slides only.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control except toggles, so a state a script adds on mousedown (if any) is missing.")
W("- **Hover on the feature cards, the article rows, the Share button and the play disc** changed nothing measurable; their entries read 'same'.")
W("- **The tutor transcript** held only the status line during the 25 seconds of playback the kit waits; transcript text was not captured.")
W("- **Disabled states** were found on three controls: the Sign in dialog's Sign in button (brand red at low strength), the Atlas Send button while the box is empty (it turns dark, enabled, once text is typed), and the blog's Previous arrow on page 1. Gauth shows no inline error while typing: the Sign in dialog keeps its button disabled instead. Its CSS declares the error state a submit would show (`form_error`: a `#fff2f2` field with a `#f00039` border, a red 14/20 message); the capture forced that class in DevTools to read it ([text-field-error-forced](#text-field-error-forced)).")
W("- **Loading states.** The pages render on the server, so the skeletons in Gauth's CSS (`catalog_mathSkeleton*`, `math-course-detail_detailSkeletonBanner`) never showed, even with the data request held back. The nearest to a loading state is the math tutor's status line, which shimmers while it narrates; it was read at rest, as its default state ([tutor-status-line](#tutor-status-line)).")
W()
W("### Themes")
W()
W("Gauth shows one light theme. Its stylesheets do declare dark values: TikTok's TUX theme under `[data-theme=\"dark\"]` and `.twv-container` with `prefers-color-scheme: dark`, the lesson palette under `[data-lesson-style=\"dark\"]`, and Astryx's stone theme as `light-dark()` pairs. None of them is applied on any page captured: no page sets a dark attribute, the science player pins `data-theme=\"light\"`, and every page painted the same under `prefers-color-scheme: dark` (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)). There is no theme switch in the sidebar, the lesson Settings or the footer. The token file therefore ships no dark set, and the dark declarations stay in the raw file for reference.")
W()
W("### Fonts")
W()
W("- **SF Pro** is Apple's system face; Gauth declares an \"SF Pro\" family over `local()` only, so it renders as SF Pro on Apple devices and falls back elsewhere.")
W("- **Satoshi** (the science canvas's \"Canvas Print\" and \"Canvas Heading\") is from Fontshare and is not on Google Fonts; the style guide falls back to the system font.")
W("- **Rubik**, named on small Atlas labels, has no `@font-face` on the page and rendered as a fallback in the capture.")
W()
W("### Screenshots")
W()
W("- Covers, illustrations, videos and story images are Gauth's content and appear only inside screenshots and crops. The lesson canvas and the Atlas story keep moving, so two captures of the same view can differ in what the narration has drawn.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Lesson content (slides, canvas drawings, formulas, narration) was not transcribed; only the frames around it were measured.")
W("- No personal data was captured: the pages were read signed out, and the Atlas drawer was empty.")

# count the values in the entries, then turn the marks into Markdown
body = "\n".join(L[ENTRY_START:ENTRY_END])
n_tok, n_raw = body.count("\x03"), body.count("\x01")
share = f"{n_tok} of {n_tok + n_raw} values in the entries ({round(100 * n_tok / max(1, n_tok + n_raw))}%) are written as tokens. The other {n_raw} are marked †: a value used by one component only (a one-off padding, colour or text style), a `50%` circle radius, or a line height of `normal`, none of which a DTCG token in this file holds; every other value used by two or more components has a token"
text = "\n".join(L).replace("{{TOKEN_SHARE}}", share)
text = re.sub("\x03([^\x04]*)\x04", r"`\1`", text).replace("\x01", "").replace("\x02", "†")
Path("components.md").write_text(text + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops,", len(icons), "icons")
