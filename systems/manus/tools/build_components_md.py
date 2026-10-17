#!/usr/bin/env python3
"""Build components.md for the Manus design reference.

Reads raw/components-computed.json (every component and state, measured in both themes),
raw/layout.json, tokens.json, screenshots/ and icons/INDEX.tsv, and writes components.md next to
them. Every value is a cell of the measurement file, condensed: colours are hex followed by the token
in the matching theme's set whose value is the same, the font family is named once per value, and a
state row shows only what differs from the first state. Dark states come first (the pages were
captured dark); the light reading of the same state follows as `light`, `light-hover` and so on.
Adapted from the Gauth kit's builder.

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


BY_COLOR = {"dark": {}, "light": {}}
for theme in ("dark", "light"):
    for n, t in flat(T[theme]):
        if t["$type"] == "color" and not str(t["$value"]).startswith("{"):
            # computed styles round alpha to two places (#ffffff0a reads back as rgba(255, 255, 255, 0.04))
            key = re.sub(r"(\d+\.\d+)\)", lambda m: f"{round(float(m.group(1)), 2):g})", t["$value"])
            BY_COLOR[theme].setdefault(key, n)

THEME = ["dark"]  # the theme the colour() helper looks tokens up in; set per state
STATE = ["default"]  # the state being written, so own_tokens() knows which class variants apply

# The token each variable is, by name: a token's source names the css-var it was read from.
NAME2PATH = {"dark": {}, "light": {}}
for theme in ("dark", "light"):
    for n, t in flat(T[theme]):
        m = re.match(r"css-var (--[A-Za-z0-9-]+) ", t.get("$extensions", {}).get("source", ""))
        if m and not n.startswith(("role.", "component.")):
            NAME2PATH[theme].setdefault(m.group(1), n)
OWN = [{}]  # property -> {value: token}, from the state's own classes; set per state
NAMED = [{}]  # value -> token, for every variable named in the component's classes; set per state

# Which class prefix sets which property, and which class variants apply in which measured state.
PROP_CLASS = {"bg": r"bg", "text": r"text", "border": r"border(?:-[trblxyse])?"}
STATE_VARIANTS = (("pressed", ("active", "hover")), ("hover", ("hover", "group-hover")), ("focus", ("focus", "focus-visible", "focus-within")),
                  ("disabled", ("disabled",)), ("open", ("data-[state=open]", "aria-expanded")), ("selected", ("data-[active]", "aria-selected")))


def hexnorm(v):
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v.strip())
    if not m:
        return None
    h = m.group(1)
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    a = int(h[6:8], 16) / 255 if len(h) == 8 else None
    return norm(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)


def own_tokens(v, theme, state):
    """{property: {value: token}} for the colours the element's own classes set, in variants that
    apply to this state. The value is the variable's value in this theme, so a label is exact only
    when the class that names the variable is on this element, for this property, in this state."""
    variants = {""} | ({"dark"} if theme == "dark" else set())
    for key, vs in STATE_VARIANTS:
        if key in state:
            variants |= set(vs)
    vals = v.get("vars") or {}
    out = {}
    for cls in v.get("classes", "").split():
        parts = cls.split(":")
        base, mods = parts[-1], parts[:-1]
        if any(m not in variants for m in mods):
            continue
        for prop, rx in PROP_CLASS.items():
            m = re.fullmatch(rx + r"-\[var\(--([A-Za-z0-9-]+)\)\]", base)
            if not m:
                continue
            name = "--" + m.group(1)
            path = NAME2PATH[theme].get(name)
            hv = hexnorm(vals[name]) if path and isinstance(vals.get(name), str) else None
            if hv:
                out.setdefault(prop, {}).setdefault(re.sub(r"(\d+\.\d+)\)", lambda mm: f"{round(float(mm.group(1)), 2):g})", hv), path)
    return out


def named_tokens(v, theme):
    """{value: token} for every variable the component's classes (its own and its parts') name, so
    a colour matched only by value prefers a token the component actually uses."""
    out = {}
    for name, val in (v.get("vars") or {}).items():
        path = NAME2PATH[theme].get(name)
        hv = hexnorm(val) if path and isinstance(val, str) else None
        if hv:
            out.setdefault(re.sub(r"(\d+\.\d+)\)", lambda mm: f"{round(float(mm.group(1)), 2):g})", hv), path)
    return out


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), round(float(a), 2))


def colour(c, tokens=True, prop=None):
    """rgb()/rgba()/color(srgb) -> '#hex `token`' or 'rgba(...)'. With `prop` (bg, text, border), a
    value the element's own class sets for that property in this state gets that exact token."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        if not tokens:
            return v
        if prop and v in OWN[0].get(prop, {}):
            STATS["token"] += 1
            return f"`{OWN[0][prop][v]}` ({v})"
        tok = NAMED[0].get(v) or BY_COLOR[THEME[0]].get(v)
        STATS["approx" if tok else "raw"] += 1
        return f"`≈ {tok}` ({v})" if tok else v

    c = re.sub(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)",
               lambda m: label(norm(*(round(float(x) * 255) for x in m.group(1, 2, 3)), m.group(4))), c)
    return re.sub(r"rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)", lambda m: label(norm(*m.group(1, 2, 3), m.group(4))), c)


# --------------------------------------------------------------------------- core tokens by value

def resolve(v, tree):
    """Follow {a.b} aliases inside one token set until a literal remains."""
    seen = 0
    while isinstance(v, str) and re.fullmatch(r"\{[^{}]+\}", v) and seen < 8:
        node = tree
        for k in v[1:-1].split("."):
            node = node[k]
        v = node["$value"]
        seen += 1
    return v


CORE = T["core"]
DIM = {}  # (kind, "12px") -> token path. A value names a token only through tokens meant for that kind
# of value, generic ones first, so a 28px row height never reads as `size.avatar`.
KINDS = {
    "radius": ["radius.small", "radius.card", "radius.row", "radius.md", "radius.dialog", "radius.composer", "radius.full"],
    "height": ["size.row", "size.row-small", "size.control-large", "size.control-small", "size.header"],
    "icon": ["size.icon-xs", "size.icon-small", "size.icon", "size.icon-medium", "size.icon-large"],
    "space": [n for n, _ in flat(CORE["space"], "space.")] + [n for n, _ in flat(CORE["density"], "density.") if "padding" in n],
    "borderWidth": [n for n, _ in flat(CORE["borderWidth"], "borderWidth.")],
    "focusRing": ["focusRing.width", "focusRing.offset", "focusRing.input-width"],
}
for kind, paths in KINDS.items():
    for n in paths:
        node = CORE
        for k in n.split("."):
            node = node[k]
        val = resolve(node["$value"], CORE)
        if isinstance(val, str) and re.fullmatch(r"-?[\d.]+px", val):
            DIM.setdefault((kind, "%gpx" % float(val[:-2])), n)
DUR = {}
for n in ["duration.fast", "duration.sidebar", "duration.resize", "duration.theme", "duration.streamer"]:
    DUR.setdefault("%gms" % float(str(CORE["duration"][n.split(".")[1]]["$value"])[:-2]), n)
EASE = {}
for n, t in flat(CORE["easing"], "easing."):
    EASE.setdefault("cubic-bezier(" + ", ".join("%g" % x for x in t["$value"]) + ")", n)
OPACITY = {"%g" % t["$value"]: n for n, t in flat(CORE["opacity"], "opacity.")}
TYPE = {}
FAMILY = {"System": "fontFamily.sans", "Libre Baskerville": "fontFamily.serif", "Mono": "fontFamily.mono"}
for prefix, node in (("typography.role.", CORE["typography"]["role"]), ("typography.", {k: v for k, v in CORE["typography"].items() if k != "role"})):
    for n, t in flat(node, prefix):
        v = {k: resolve(x, CORE) for k, x in t["$value"].items()}
        key = ("%gpx" % float(v["fontSize"][:-2]), "%gpx" % float(v["lineHeight"][:-2]), str(v["fontWeight"]), t["$value"]["fontFamily"], "%gpx" % float(str(v.get("letterSpacing", "0px"))[:-2]))
        TYPE.setdefault(key, n)
STATS = {"token": 0, "approx": 0, "raw": 0}


def layer_key(layer, theme):
    c = resolve(layer["color"], T[theme])
    h = c.lstrip("#") if isinstance(c, str) and c.startswith("#") else None
    if h is None:
        m = re.fullmatch(r"rgba\((\d+), (\d+), (\d+), ([\d.]+)\)", c)
        col = norm(*m.groups()) if m else c
    else:
        if len(h) in (3, 4):
            h = "".join(x * 2 for x in h)
        col = norm(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), int(h[6:8], 16) / 255 if len(h) == 8 else None)
    if col == "rgba(0, 0, 0, 0)":
        return None
    return f"{col} {layer['offsetX']} {layer['offsetY']} {layer['blur']} {layer['spread']}" + (" inset" if layer.get("inset") else "")


ELEVATION = {}
for theme in ("dark", "light"):
    ELEVATION[theme] = {}
    for n, t in flat(T[theme]["elevation"], "elevation."):
        keys = [k for k in (layer_key(l, theme) for l in t["$value"]) if k]
        ELEVATION[theme].setdefault(", ".join(keys), n)


def dim(px, groups):
    """'12px' -> '`radius.card` (12px)' when a token in one of `groups` holds it, else the value."""
    key = "%gpx" % float(px[:-2]) if px.endswith("px") else px
    for g in groups:
        if (g, key) in DIM:
            STATS["token"] += 1
            return f"`{DIM[(g, key)]}` ({px})"
    if key != "0px":
        STATS["raw"] += 1
    return px


def sides(t, r, b, l):
    if t == r == b == l:
        return t
    if t == b and r == l:
        return f"{t} {r}"
    return f"{t} {r} {b} {l}"


def fam(f):
    first = f.split(",")[0].replace('"', "").strip()
    return {"-apple-system": "System", "LibreBaskerville": "Libre Baskerville", "ui-sans-serif": "System", "ui-monospace": "Mono"}.get(first, first)


def num(x):
    return re.sub(r"(\d+\.\d\d)\d+", r"\1", str(x))


def font(fz, lh, fw, f, ls="normal"):
    """A text style; it names a typography token only when family, size, line height, weight and
    letter spacing all match (normal spacing is 0px)."""
    lhn = lh.replace("px", "") if lh != "normal" else "normal"
    plain = f"{fam(f)} {num(fz.replace('px', ''))}/{num(lhn)} {fw}" + (f" tracking {ls}" if ls not in ("normal", "0px") else "")
    lsk = "0px" if ls in ("normal", None) else "%gpx" % float(ls[:-2])
    key = ("%gpx" % float(fz[:-2]), "%gpx" % float(lh[:-2]) if lh.endswith("px") else lh, str(fw), "{" + FAMILY.get(fam(f), "") + "}", lsk)
    tok = TYPE.get(key)
    STATS["token" if tok else "raw"] += 1
    return f"`{tok}` ({plain})" if tok else plain


def props(v):
    s = v["style"]
    OWN[0] = own_tokens(v, THEME[0], STATE[0])
    NAMED[0] = named_tokens(v, THEME[0])
    o = {}
    h = "%gpx" % round(v["rect"]["h"], 2)
    o["size"] = f"{num(v['rect']['w'])} x " + (dim(h, ("height",)) if ("height", h) in DIM else num(v["rect"]["h"]))
    pad = sides(s["paddingTop"], s["paddingRight"], s["paddingBottom"], s["paddingLeft"])
    if pad != "0px":
        o["padding"] = " ".join(dim(x, ("space",)) for x in pad.split(" "))
    bds = []
    for d in ("Top", "Right", "Bottom", "Left"):
        if float(s[f"border{d}Width"].replace("px", "")) > 0 and s[f"border{d}Style"] != "none":
            bds.append(f"{dim(s[f'border{d}Width'], ('borderWidth',))} {s[f'border{d}Style']} {colour(s[f'border{d}Color'], prop='border')}")
        else:
            bds.append("none")
    if any(b != "none" for b in bds):
        o["border"] = bds[0] if len(set(bds)) == 1 else "; ".join(f"{'TRBL'[i]}: {b}" for i, b in enumerate(bds) if b != "none")
    rad = sides(s["borderTopLeftRadius"], s["borderTopRightRadius"], s["borderBottomRightRadius"], s["borderBottomLeftRadius"])
    if rad != "0px":
        o["radius"] = " ".join(dim(x, ("radius",)) for x in rad.split(" "))
    o["background"] = colour(s["backgroundColor"], prop="bg")
    if s["backgroundImage"] != "none":
        img = re.sub(r'url\("data:[^)]*\)', "an image (data URI)", s["backgroundImage"])
        o["image"] = colour(img)[:200]
    if s["boxShadow"] != "none":
        sh = colour(s["boxShadow"], tokens=False)
        layers = [x.strip() for x in re.split(r",(?![^(]*\))", sh)]
        layers = [x for x in layers if not x.startswith("transparent")]
        if layers:
            el = ELEVATION[THEME[0]].get(", ".join(layers))
            if el:
                STATS["token"] += 1
            else:
                STATS["raw"] += 1
            o["shadow"] = f"`{el}` ({', '.join(layers)})" if el else ", ".join(layers)
    if s.get("backdropFilter", "none") != "none":
        o["backdrop"] = s["backdropFilter"]
    if s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0:
        o["outline"] = f"{dim(s['outlineWidth'], ('focusRing', 'borderWidth'))} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {dim(s['outlineOffset'], ('focusRing',)) if not s['outlineOffset'].startswith('-') else s['outlineOffset']}"
    t = v.get("textStyle")
    if t:
        o["text"] = f"{font(t['fontSize'], t['lineHeight'], t['fontWeight'], t['fontFamily'], t.get('letterSpacing', 'normal'))}, {colour(t['color'])}"
    elif v.get("text"):
        o["text"] = f"{font(s['fontSize'], s['lineHeight'], s['fontWeight'], s['fontFamily'], s.get('letterSpacing', 'normal'))}, {colour(s['color'], prop='text')}"
    if s["transitionDuration"] not in ("0s", ""):
        props_ = [x.strip() for x in s["transitionProperty"].split(",")]
        durs = [x.strip() for x in s["transitionDuration"].split(",")]
        tf = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", s["transitionTimingFunction"])
        parts = []
        for i, p in enumerate(props_):
            d = durs[i % len(durs)]
            if d == "0s":
                continue
            ms = "%gms" % round(float(d[:-1]) * 1000) if d.endswith("s") and not d.endswith("ms") else d
            if ms in DUR:
                STATS["token"] += 1
                d = f"`{DUR[ms]}` ({d})"
            else:
                STATS["raw"] += 1
            ease = tf[i % len(tf)] if tf else ""
            if ease in EASE:
                ease = f"`{EASE[ease]}` ({ease})"
            parts.append(f"{p} {d} {ease}".strip())
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
    if s["opacity"] != "1":
        tok = OPACITY.get("%g" % float(s["opacity"]))
        STATS["token" if tok else "raw"] += 1
        o["opacity"] = f"`{tok}` ({s['opacity']})" if tok else s["opacity"]
    ic = v.get("icon")
    if ic and ic.get("w", 0) > 0 and ic["w"] < 120:
        keep = OWN[0]
        OWN[0] = own_tokens({"classes": ic.get("classes", ""), "vars": v.get("vars")}, THEME[0], STATE[0])
        isz = "%gpx" % ic["w"]
        size_ = f"`{DIM[('icon', isz)]}` ({num(ic['w'])} x {num(ic['h'])})" if ic["w"] == ic["h"] and ("icon", isz) in DIM else f"{num(ic['w'])} x {num(ic['h'])}"
        o["icon"] = f"{size_}, {colour(ic.get('color') or ic.get('stroke') or ic.get('fill'), prop='text')}"
        OWN[0] = keep
    if v.get("placeholder"):
        o["placeholder"] = colour(v["placeholder"]["color"])
    return o


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "backdrop", "outline", "text", "transition", "transform", "opacity", "icon", "placeholder"]


def state_rows(c):
    """Dark states first, then light. Each theme has its own base row (the first state of that
    theme), later rows of the same theme list only what changed."""
    rows = []
    for theme in ("dark", "light"):
        states = [s for s, v in c["states"].items() if "style" in v and v.get("theme") == theme]
        if not states:
            continue
        THEME[0] = theme
        STATE[0] = states[0]
        base = props(c["states"][states[0]])
        trows = [(states[0], base)]
        same = []
        for st in states[1:]:
            STATE[0] = st
            p = props(c["states"][st])
            diff = {k: p[k] for k in ORDER if k in p and p.get(k) != base.get(k)}
            for k in ORDER:
                if k in base and k not in p:
                    diff[k] = "none"
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
    out = []
    for p in st["paint"][:3]:
        bits = [re.sub(r"\..*$", "", p["node"]) if "::" not in p["node"] else p["node"].split(".")[0], p["size"].replace(".0x", "x").replace(".0", "")]
        if p.get("bg"):
            bits.append("background " + colour(p["bg"]))
        if p.get("border"):
            bits.append("border " + colour(p["border"].split(" | ")[0][2:]))
        if p.get("radius"):
            bits.append("radius " + p["radius"])
        if p.get("shadow"):
            bits.append("shadow " + colour(p["shadow"]))
        out.append(" ".join(bits))
    return "; ".join(out).replace("|", "/")


# --------------------------------------------------------------------------- page and group text

GROUP_INTRO = {
    "Sidebar": "The 300px sidebar every page shares: a 48px logo row with search and collapse, eight nav tabs, a Projects section of folders and a Tasks section of recent threads (each with its type glyph, a dashed ring while it runs), the share banner, and the account row with the desktop and notification buttons. Cmd+. folds it to a 52px rail of glyphs.",
    "Top bar": "The 48px row over the content: the model picker at the left, and at the right the plan chip with its Upgrade link and the credits pill on the home, or Upgrade, Share, more and the panel toggle on a task.",
    "Home": "The new-task page: the logo with the promo carousel beside it, the Build and Create cards, the Start from a local file card, and the composer pinned at the bottom.",
    "Composer": "The task composer, shared by the home, the task page, the project page and the phone: a 22px-radius card with a 50px editor, a + button, connector chips, the Manus Desktop chip, and the microphone and send buttons. The disclaimer sits under it on a task.",
    "Menus and dialogs": "The popovers and dialogs: the model menu, the + attach menu, the search dialog, the notifications panel, the account menu, the Library's row menu and view options, the sidebar's task menu and project context menu, the More menu, the files dialog, the previewer's and settings' dialogs. All share the 12px radius card on `--background-menu-white` with a hairline border.",
    "Library": "The file library: the title bar with search, view options and the grid/list control, the strip of type tabs, then groups by day (or by task) of rows and grid cards.",
    "Document previewer": "The full-screen previewer a Library row opens: a header with the title, Last modified and five tools, and the document body set in the serif.",
    "Settings": "The settings dialog: an account header and a left nav of sections, the General pane with Language, the three theme cards, selects and toggle rows, and the Keyboard shortcuts pane.",
    "Creations": "Published websites, games and apps: a tab strip and wide cards with a thumbnail, the task they came from, a URL chip and three actions.",
    "Computers": "Cloud computers: a heading, six setup cards with badges, and the Customize and Connect bands.",
    "Agents": "The Meet Cue page: a title, a video with its play button, two download buttons, the waitlist banner and a footer link.",
    "Automations": "The empty state: a heading and three example cards (Schedule, Trigger, Advanced) over a Get started button.",
    "Plugins": "The connector gallery: header buttons, a carousel of promo cards, search, category tabs and a two-column grid of plugin rows.",
    "Settings and forms": "Added on the 2026-10-17 refresh: Settings' Developers pane (underline tabs, an info banner, the API key table with its row button and popover, the destructive confirmation), the Create API Key form (label, text field, select and its listbox, the primary button disabled and enabled), Personalization's fields, Usage & Billing loading, and the invite dialog (segmented control, black and blue buttons, the email field and Send), and the toast an invalid email raises. Pressed was read on every part here that has an `active:` style; the older parts' page copies were not kept, so their pressed rows are missing rather than measured.",
    "Project": "A project page: icon, title and meta, the recent tasks, a composer, and the right rail of cards with Add buttons.",
    "Task": "A finished task's thread: the user bubble with an attachment, assistant turns with the logo header and Lite tag, step rows, message actions, the deliverable card, file chips, View all files, Task completed, rating stars, follow-up suggestions, the step footer, and the split view's tab bar, empty state tiles and files tree.",
    "Mobile": "The same app at 390 wide: the app banner, the header with its menu button, the serif hero, the composer and suggestion chips, the carousel card, the drawer, the Library header with its type dropdown, and the task page.",
}

PAGE_DESC = [
    ("home", "Home. The logo and promo carousel, Build and Create, Start from a local file, the composer. Captured at rest, with the model menu, the + attach menu, a line typed in the composer, the sidebar collapsed, the search dialog and the notifications panel.", "/app"),
    ("library", "Library. The title bar, the type tabs, groups by day. Captured on All, on Slides, on Images in grid view, with the view options open, grouped by task, with a row's menu open, with the document previewer open, and with the account menu open.", "/app/documents"),
    ("settings", "Settings dialog. General (language, theme cards, chat and communication toggles) and Keyboard shortcuts; on 2026-10-17 also Developers (the API key table, a row's menu, the delete confirmation, the Create API Key form empty, typed and with its select open), Personalization and Usage & Billing while its history loads.", "/app#settings"),
    ("invite", "The invite dialog (2026-10-17): share tabs, Copy invitation link, the social row and the email field, empty and typed.", "/app#invitation"),
    ("creations", "Creations. Tabs and two creation cards.", "/app/creations"),
    ("computers", "Computers. The setup cards and the Customize and Connect bands.", "/app/computers"),
    ("agents", "Agents. Meet Cue.", "/app/agents"),
    ("automations", "Automations. The empty state with three example cards.", "/app/automation?tab=updates"),
    ("plugins", "Plugins. The gallery; also the More menu and a project's context menu, opened from the sidebar on this page.", "/app/plugins"),
    ("project", "Project page (Hackathons).", "/app/project/<id>"),
    ("task", "A finished task. The end of the thread with the deliverable card, the files dialog, the split view with New tab and with the Files tab, the sidebar task menu, and the thread scrolled to its top and middle.", "/app/<task id>"),
]
MOBILE_DESC = [
    ("mobile-home", "Home at 390: the app gate, the hero and composer, the drawer.", "/app"),
    ("mobile-library", "Library at 390, and its type dropdown.", "/app/documents"),
    ("mobile-task", "The finished task at 390.", "/app/<task id>"),
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

W("# Manus components")
W()
W(f"The discovery list of every page and state captured, then one entry per component with crops of the real product, the shared values, the icon index and the Gaps. Captured from manus.im/app on 2026-10-04 and refreshed on 2026-10-17, signed in, as static copies of each page state rendered in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the rendered copy in both themes. Nothing was sent or deleted in the account; the changes made were opening menus and dialogs, switching the Library's view options and switching them back, typing into the composer and into two dialog fields without submitting, and toggling the sidebar. On 2026-10-17 one click landed on a popover's \"Continue in new task\" by mistake and branched an existing task; the owner was told and the branch is theirs to remove.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [raw/pages.md](raw/pages.md).")
W()
W("How to read an entry:")
W()
W("- Every value is written token first: `` `token` (value) ``. A plain token is exact: for a colour, the variable the component's own classes name for that property in that state (bg-[var(--x)], text-, border-); for a size, radius, padding, type style, duration, easing, shadow or opacity, the core token whose value it is. `` `≈ token` `` names a colour token only by its value in that theme, for colours no class on the element names (inherited text, browser defaults). A value with no token is written alone. Text is family size/line-height weight, for example `` `typography.sm` (System 14/20 400) ``, read from the first text node inside the component. Each component's class-named colour tokens are also in tokens.json under `component.<key>` in each theme.")
W("- Dark states come first (every page was captured dark), then the same states read in light. Each theme's first row lists every value; later rows of that theme list only what changes. A state with the same values as its theme's first is named in that label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component from the rendered copy, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{theme}-{state}.png`. Desktop shots are 1440 x 900 at 2x; `-full` shots are whole pages at 2x, kept for the base pages only; mobile shots are `mobile-{page}-{theme}-{state}.png`, 390 x 844 at 2x. Every state exists in both themes.")
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
    ("Manus Flex promo dialog", "home, on load", "at rest; dismissed with Got it, not re-opened", "not captured as a copy (seen only in the live pane)"),
    ("Model menu", "home", "the model picker", "[home-dark-model-menu](screenshots/home-dark-model-menu.png), [model-menu](#model-menu)"),
    ("Attach menu", "home", "the composer's + button", "[home-dark-attach-menu](screenshots/home-dark-attach-menu.png), [attach-menu](#attach-menu)"),
    ("Composer with text", "home", "a line typed, then deleted", "[home-dark-composer-typed](screenshots/home-dark-composer-typed.png)"),
    ("Collapsed sidebar", "home", "the collapse button; Cmd+. restores it", "[home-dark-sidebar-collapsed](screenshots/home-dark-sidebar-collapsed.png), [sidebar-collapsed](#sidebar-collapsed)"),
    ("Search dialog", "home", "the sidebar's search button (also Cmd+K)", "[home-dark-search](screenshots/home-dark-search.png), [search-dialog](#search-dialog)"),
    ("Notifications panel", "home", "the bell in the account row", "[home-dark-notifications](screenshots/home-dark-notifications.png), [notifications-panel](#notifications-panel)"),
    ("Account menu", "Library", "the account row", "[library-dark-user-menu](screenshots/library-dark-user-menu.png)"),
    ("Settings dialog", "Library", "Settings in the account menu, then Shortcuts in its nav; closed with Escape", "[settings-dark-general](screenshots/settings-dark-general.png), [settings-dark-shortcuts](screenshots/settings-dark-shortcuts.png), [settings-dialog](#settings-dialog)"),
    ("Type tabs, grid view, view options, group by task", "Library", "the Slides and Images tabs, the grid control, the view options button, Group by task toggled on and back off", "[library-dark-slides](screenshots/library-dark-slides.png), [library-dark-images-grid](screenshots/library-dark-images-grid.png), [library-dark-images-grid-view-options](screenshots/library-dark-images-grid-view-options.png), [library-dark-images-grid-by-task](screenshots/library-dark-images-grid-by-task.png)"),
    ("Row menu", "Library", "a row's more button", "[library-dark-row-menu](screenshots/library-dark-row-menu.png), [row-menu](#row-menu)"),
    ("Document previewer", "Library", "a row pressed; closed with Escape", "[library-dark-preview-doc](screenshots/library-dark-preview-doc.png), [previewer](#previewer)"),
    ("More menu", "sidebar", "the More tab", "[plugins-dark-more-menu](screenshots/plugins-dark-more-menu.png), [more-menu](#more-menu)"),
    ("Project context menu", "sidebar", "right-click on the project row; View project opened the project page", "[plugins-dark-project-context-menu](screenshots/plugins-dark-project-context-menu.png), [context-menu](#context-menu)"),
    ("Task menu", "sidebar", "the more button on a hovered task row", "[task-dark-sidebar-task-menu](screenshots/task-dark-sidebar-task-menu.png), [task-menu](#task-menu)"),
    ("Files dialog", "task", "View all files in this task; closed with Escape", "[task-dark-files-dialog](screenshots/task-dark-files-dialog.png), [files-dialog](#files-dialog)"),
    ("Split view", "task", "the panel toggle, then Files in Start from scratch; closed with the Close sidebar button", "[task-dark-side-panel](screenshots/task-dark-side-panel.png), [task-dark-files-tab](screenshots/task-dark-files-tab.png)"),
    ("Mobile app gate and drawer", "home at 390", "on load, Continue with web; then the menu button", "[mobile-home-dark-app-gate](screenshots/mobile-home-dark-app-gate.png), [mobile-home-dark-drawer](screenshots/mobile-home-dark-drawer.png)"),
    ("Mobile type dropdown", "Library at 390", "the All chip", "[mobile-library-dark-type-menu](screenshots/mobile-library-dark-type-menu.png)"),
    ("API key row menu and delete confirmation", "Settings > Developers (2026-10-17)", "a row's more button, then Delete; closed with Cancel, nothing deleted", "[settings-dark-key-menu](screenshots/settings-dark-key-menu.png), [settings-dark-delete-confirm](screenshots/settings-dark-delete-confirm.png), [confirm-dialog](#confirm-dialog)"),
    ("Create API Key form", "Settings > Developers (2026-10-17)", "Create new; a name typed, the Expiration select opened; closed with Cancel, nothing created", "[settings-dark-create-key](screenshots/settings-dark-create-key.png), [settings-dark-create-key-typed](screenshots/settings-dark-create-key-typed.png), [settings-dark-select-open](screenshots/settings-dark-select-open.png), [form-dialog](#form-dialog)"),
    ("Usage history loading", "Settings > Usage & Billing (2026-10-17)", "the pane opened, copied while its history fetched", "[settings-dark-usage-loading](screenshots/settings-dark-usage-loading.png), [spinner](#spinner)"),
    ("Invite dialog", "account row banner (2026-10-17)", "the Share Manus banner; an invalid address typed, not sent; closed", "[invite-dark-dialog](screenshots/invite-dark-dialog.png), [invite-dark-email-typed](screenshots/invite-dark-email-typed.png), [invite-dialog](#invite-dialog)"),
    ("Invalid email (validation error) and toast", "invite dialog (2026-10-17)", "with the owner's go-ahead, \"not-an-email\" typed and Send pressed; Manus refused it client-side with a toast, so nothing was sent", "[invite-dark-email-error](screenshots/invite-dark-email-error.png), [toast](#toast), [email-field](#email-field)"),
    ("Toast while a task starts", "task (2026-10-17)", "seen once, \"Creating new task…\" with a spinner, top centre", "not captured as a copy; the same toast frame is measured from the validation error"),
]
for row in OVER:
    W("| " + " | ".join(row) + " |")
W()

# --------------------------------------------------------------------------- shared values

NAMED[0] = {}  # tallies across components: no component's variables apply
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
        r = st["borderTopLeftRadius"]
        if r != "0px" and s["rect"]["w"] > 4:
            radii[r] += 1
        if st["transitionDuration"] not in ("0s", ""):
            # the first duration and the first timing function; a cubic-bezier() carries commas of its own
            tf = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", st["transitionTimingFunction"])
            trans[f"{st['transitionDuration'].split(',')[0].strip()} {tf[0] if tf else st['transitionTimingFunction']}"] += 1
        if sname.endswith("focus-visible"):
            th = s["theme"]
            focus_n[th] += 1
            if st["outlineStyle"] != "none" and float(st["outlineWidth"].replace("px", "")) > 0:
                THEME[0] = th
                focus[th][f"{st['outlineWidth']} {st['outlineStyle']} {colour(st['outlineColor'])} offset {st['outlineOffset']}"] += 1
            else:
                focus[th]["no ring on the element"] += 1
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


W(f"**Radius.** {top(radii, 10)}. The density tokens name four of them: `radius.row` 10 (nav tabs, list rows), `radius.small` 8 (icon buttons, chips, the segmented control), `radius.card` 12 (cards, menus, dialogs), `radius.composer` 22. The 6 is the segmented control's thumb and the smaller icon buttons; 9999 is avatars, pills and the send button.")
W()
W(f"**Hover.** Manus hovers with a translucent fill, not a colour change. Dark: {top(hover_dark, 6)}. Light: {top(hover_light, 6)}. The two fills are `fill.tsp-white-light` (4%) and `fill.tsp-white-main` (6%); the current nav tab rests on the 6% fill and hovers to it.")
W()
W(f"**Focus.** Of {focus_n['dark']} elements given a real keyboard focus in dark: {top(focus['dark'], 6)}. In light: {top(focus['light'], 6)}. Most of Manus's controls are `div`s with `role=button` and draw no ring; the inset 1px ring is Radix's menu item focus, the 2px blue ring (`text.blue`, offset 2) is the composer's send button and the theme cards.")
W()
W(f"**Motion.** {top(trans, 6)}. Nearly every transition is Tailwind's `transition-colors` at 150 ms on the standard curve; the sidebar's width is 200 ms, the task column's theme cross-fade 500 ms, the segmented thumb 200 ms on transform.")
W()
W("**Layout grid.** The sidebar is 300 wide (52 as a rail), the main column the rest, with a 48 tall bar over it. The home, plugins and task pages set a 768 to 800 wide centred column; the Library, Creations, Computers and Automations a 960 to 1000 wide one. On a phone the sidebar is the same 300 wide column parked off-screen and slid in as a drawer. The numbers per page are in [raw/pages.md](raw/pages.md).")
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
        for sname in ("default", "hover", "light", "light-hover", "active", "selected", "checked", "open", "typed", "focus-visible"):
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
icons = [r for r in icons if len(r) >= 9 and r[0].endswith(".svg")]  # the inline glyphs; the <img> list after the blank line is separate
named = [r for r in icons if not r[0].startswith("icon-") and not r[0].startswith("lucide-")]
W(f"{len(icons)} distinct glyphs were lifted from the pages into [icons/](icons), every one named by its role or its Lucide name in [icons/INDEX.tsv](icons/INDEX.tsv) (the 67 icons.mjs had left as a hash were named on the 2026-10-17 refresh from the words beside them and by sight, through tools/capture/icon-names.tsv and name_icons.py). Glyphs named `brand-*` are other companies' marks (Gmail, Google Docs, Drive and Sheets, Instagram, Shopify, Windows, Apple) as Manus shows them in connectors and examples; they belong to those companies. Manus draws almost everything with Lucide (24-unit stroke icons at 2px, shown at 16 or 18) in `--icon-primary`, `--icon-secondary` or `--icon-tertiary`; the file-type icons in the Library are filled 32-unit glyphs in blue, red, orange and grey; the sidebar's task glyphs are images Manus serves from its CDN, kept under `icons/session/`.")
W()
W("| Icon | Where |")
W("|---|---|")
for r in named:
    W(f"| `{r[0].replace('.svg', '')}` | {(r[8] if len(r) > 8 and r[8] else r[6])[:90].replace('|', '/')} |")
W()

# --------------------------------------------------------------------------- gaps

W("## Gaps")
W()
W("- The thread of a running task (streaming text, the live computer view, tool cards as they appear, the Stop control) was not captured; every task capture is of a finished task. The `nav-task-running` entry is the sidebar's dashed ring for one that was still running.")
W("- The deliverable card's slide preview is an iframe, kept as a same-size dark box in every copy; its header, menu and the file chips under it are real.")
W("- Hover and focus on the 390-wide copies were not measured (a phone has neither), and the Library's checked view option does not exist in the mobile copy.")
W("- The first grid-view copy (`library-dark-images-grid`) was taken before thumbnails were inlined, so its cards show the placeholder; the grouped-by-task and view-options copies have the real thumbnails.")
W("- The Manus Flex promo dialog, the Create automation flow, a plugin's detail dialog, a creation's page, the Computers' create flow, the Account settings pane and the share sheet were not captured, since each either spends credits, changes the account or shows billing details.")
W("- The light theme was read by removing the `dark` class from the copies, not by switching the account's theme. Everything Manus paints is a var() of the two palette blocks, so the readings match what the Light setting shows, but any image Manus swaps per theme through JavaScript rather than CSS would not have swapped.")
W()

# How many of the written values name a token, counted on the finished entries (the value after a
# token, in parentheses, is not counted again).
def coverage(rows):
    t = " ".join(rows)
    exact = len(re.findall(r"`[a-zA-Z][\w-]*\.[^` ]+` \(", t))
    approx = len(re.findall(r"`≈ ", t))
    rest, i = "", 0
    while i < len(t):
        if t.startswith("` (", i):
            rest += "`"
            j, depth = i + 2, 0
            while j < len(t):
                depth += t[j] == "("
                depth -= t[j] == ")"
                j += 1
                if depth == 0:
                    break
            i = j
            continue
        rest += t[i]
        i += 1
    raw = len([c for c in re.findall(r"#[0-9a-f]{6}\b|rgba?\([\d., ]+\)", rest) if c != "rgba(0, 0, 0, 0)"])
    raw += len(re.findall(r"(?<![\d.])\b(?!0px)\d+(?:\.\d+)?px", rest))
    raw += len(re.findall(r"\b(?:System|Libre Baskerville|Mono|KaTeX_Main) [\d.]+/", rest))  # text styles with no token
    raw += len(re.findall(r"\bsize [\d.]+ x [\d.]+", rest))  # heights with no token
    raw += len(re.findall(r"\bicon [\d.]+ x [\d.]+", rest))  # icon sizes with no token
    raw += len(re.findall(r"\bopacity [\d.]+", rest))  # opacities with no token
    raw += len(re.findall(r"(?<![\w.(])\d*\.?\d+m?s\b", rest))  # durations with no token
    raw += len(re.findall(r"(?:cubic-bezier\([^)]*\)|\bsteps\([^)]*\)|\b(?:ease|ease-in|ease-out|ease-in-out|linear)\b)", rest))  # easings with no token
    return exact, approx, raw


entry_rows, in_states = [], False
for l in L:  # every row of every component's State | Values table, however many values it holds
    if l.startswith("| State | Values |"):
        in_states = True
        continue
    if not l.startswith("|"):
        in_states = False
    elif in_states and not l.startswith("|---"):
        entry_rows.append(l)
ex, ap, rw = coverage(entry_rows)
tot = ex + ap + rw
i = next(k for k, l in enumerate(L) if l.startswith("- Crops are images"))
L.insert(i + 1, f"- Coverage: of {tot} values written in the entries below (colours, dimensions, heights, icon sizes, text styles, durations, easings, shadows and opacities; widths and zeros aside), {ex} ({ex / tot:.0%}) name an exact token, {ap} ({ap / tot:.0%}) name a colour token by value (`≈`) and {rw} ({rw / tot:.0%}) are raw: text styles and heights off Manus's scales, hairline offsets and one-off shadows. A colour's exact token comes from the element's own class; a dimension's from the core tokens meant for that kind of value (radii from `core.radius`, heights from the control sizes in `core.size`, icons from `core.size.icon*`, paddings from `core.space`, borders from `core.borderWidth` and `core.focusRing`), generic before component-specific; text to `core.typography` and its roles; transitions to `core.duration` and `core.easing`; shadows to `elevation.*`; opacity to `core.opacity`.")
open("components.md", "w").write("\n".join(L) + "\n")
print(f"components.md: {len(C)} components, {n_states} states, {n_crops} crops, {len(L)} lines; values {ex} token, {ap} approx, {rw} raw")
