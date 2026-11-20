#!/usr/bin/env python3
"""Build components.md for the ResearchRabbit design reference.

Reads raw/components-computed.json (every component and state, measured by
tools/capture/measure.mjs), raw/css-vars.json (the :root custom properties and the per-component CSS
rules), tokens.json, components/crops/, screenshots/ and icons/INDEX.tsv, and writes components.md next
to them. Every value is a cell of the measurement file, condensed: a colour, shadow or radius is its
value followed by the tokens.json token with the same value, a state row shows only what differs from
the row it belongs to, and a state with the same values as its base is named in the base row's label.

Deterministic: re-running it on the same inputs reproduces components.md byte for byte.
Run from anywhere: python3 tools/build_components_md.py
"""
import csv
import json
import os
import re
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
J = json.load(open("raw/components-computed.json"))
C = J["components"]
PG = J["pages"]
V = json.load(open("raw/css-vars.json"))

# --------------------------------------------------------------------------- colours and tokens


def norm_hex(h):
    h = h.lower()
    if len(h) == 4:
        h = "#" + "".join(c * 2 for c in h[1:])
    return h


ROOTV = V["root"]
BY_COLOR = {}
for name, val in ROOTV.items():
    m = re.fullmatch(r"var\((--[\w-]+)\)", val.strip())
    if m:
        val = ROOTV.get(m.group(1), val)
    if re.fullmatch(r"#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6}", val.strip()) and not name.endswith("-dark"):
        BY_COLOR.setdefault(norm_hex(val.strip()), []).append(name)
for k in BY_COLOR:
    BY_COLOR[k].sort(key=lambda n: (len(n), n))


TOK = json.load(open("tokens.json"))


def _leaves(tree, prefix=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from _leaves(v, prefix + k + ".")


LEAF = {n: t for n, t in _leaves({k: v for k, v in TOK["core"].items() if k != "graph"})}
LEAF.update(_leaves(TOK["light"]))


def resolve(v, depth=0):
    if isinstance(v, str) and v.startswith("{") and v.endswith("}") and depth < 8:
        return resolve(LEAF[v[1:-1]]["$value"], depth + 1)
    return v


def _rank(path):
    """Primitive palette tokens first, literals and alphas last among them; then semantic sets."""
    order = ("palette.base.", "palette.grey.", "palette.lavender.", "palette.turq.", "palette.green.", "palette.peach.",
             "palette.selection.", "palette.activity.", "palette.ugc.", "palette.ui.", "palette.alpha.", "palette.literal.")
    for i, o in enumerate(order):
        if path.startswith(o):
            return (i, len(path), path)
    return (len(order), len(path), path)


TOK_COLOR = {}
for n, t in sorted(LEAF.items(), key=lambda kv: _rank(kv[0])):
    if t["$type"] == "color":
        TOK_COLOR.setdefault(resolve(t["$value"]), n)
# semantic roles from the light set (referenced without the set name) by what the colour paints; the general roles first, component roles last
ROLE_PRE = {
    "bg": ("background.", "action.", "status.", "component."),
    "text": ("text.", "status.", "action.primary-text"),
    "border": ("border.", "status.", "action.focus-ring"),
    "image": ("gradient.", "background."),
}
ROLE_OK = {"image": lambda n: True, "bg": lambda n: not n.startswith("status.") or n.endswith(".fill"),
           "text": lambda n: not n.startswith("status.") or n.endswith(".text"),
           "border": lambda n: not n.startswith("status.") or n.endswith(".border")}
TOK_ROLE = {}
for role, pres in ROLE_PRE.items():
    m = TOK_ROLE[role] = {}
    for i, pre in enumerate(pres):
        for n, t in LEAF.items():  # tokens.json order: the general role in each group comes first
            if n.startswith(pre) and t["$type"] == "color" and ROLE_OK[role](n):
                m.setdefault(resolve(t["$value"]), n)
# a component's own light-set token (component.toast for the toast entry) wins over a general role
TOK_COMP = defaultdict(dict)
for n, t in LEAF.items():
    if n.startswith("component.") and t["$type"] == "color":
        TOK_COMP[n.split(".")[1]].setdefault(resolve(t["$value"]), n)
CUR = {"comp": None}


def comp_tok(key):
    k = CUR["comp"]
    if not k:
        return None
    for name, vals in TOK_COMP.items():
        if (name == k or name.startswith(k + "-") or k.endswith("-" + name)) and key in vals:
            return vals[key]
    return None


TOK_RADIUS = {}
for n, t in sorted(LEAF.items(), key=lambda kv: (len(kv[0]), kv[0])):
    if n.startswith("radius."):
        v = resolve(t["$value"])
        v = f"{float(v[:-3]) * 16:g}px" if v.endswith("rem") else v
        TOK_RADIUS.setdefault(v, n)


TOK_SPACE = {}
for n, t in sorted(LEAF.items(), key=lambda kv: (len(kv[0]), kv[0])):
    if n.startswith("spacing.") and not n.startswith("spacing.neg"):
        v = resolve(t["$value"])
        TOK_SPACE.setdefault(f"{float(v[:-3]) * 16:g}px" if v.endswith("rem") else v, n)
TOK_SIZE = {}
for n, t in sorted(LEAF.items(), key=lambda kv: (len(kv[0]), kv[0])):
    if n.startswith("size.") and t["$type"] == "dimension":
        TOK_SIZE.setdefault(resolve(t["$value"]), n)


def space_tok(v):
    """'8px 12px' -> '8px 12px `{spacing.2} {spacing.3}`' when every part is a spacing step."""
    parts = v.split()
    toks = [TOK_SPACE.get(x) for x in parts]
    return f"{v} `{' '.join('{' + t + '}' for t in toks)}`" if parts and all(toks) and v != "0px" else v


def size_tok(w, h):
    """Name the control-height token a component's height equals, when there is one."""
    t = TOK_SIZE.get(f"{h}px") if isinstance(h, (int, float)) and float(h).is_integer() else None
    return f" (height `{{{t}}}`)" if t and (t.startswith("size.control") or t == "size.field") else ""


def radius_tok(r):
    return f"{r} `{{{TOK_RADIUS[r]}}}`" if r in TOK_RADIUS else r


def to_hex(r, g, b):
    return "#%02x%02x%02x" % (int(round(float(r))), int(round(float(g))), int(round(float(b))))


def colour(c, tokens=True, role=None):
    """rgb()/rgba() inside any string -> '#hex `{token.path}`' or 'rgba(...) `{token.path}`'.

    With a role ("bg", "text" or "border") the light-set token for that role is named when one has the
    value, and the palette token otherwise."""
    def look(key):
        if not tokens:
            return None
        return (comp_tok(key) if role == "bg" else None) or (TOK_ROLE[role].get(key) if role else None) or TOK_COLOR.get(key)
    def one(m):
        r, g, b = m.group(1), m.group(2), m.group(3)
        a = m.group(4)
        if a is not None and float(a) == 0:
            return "transparent"
        h = to_hex(r, g, b)
        if a is not None and float(a) != 1:
            txt = "rgba(%d, %d, %d, %g)" % (round(float(r)), round(float(g)), round(float(b)), round(float(a), 3))
            tok = look(h + "%02x" % round(float(a) * 255))
            return f"{txt} `{{{tok}}}`" if tok else txt
        tok = look(h)
        return f"{h} `{{{tok}}}`" if tok else h
    return re.sub(r"rgba?\(\s*([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\s*\)", one, c)


def num(x):
    return re.sub(r"(\d+\.\d\d)\d+", r"\1", str(x))


def px(v):
    return num(str(v).replace("px", ""))


def sides(t, r, b, l):
    if t == r == b == l:
        return t
    if t == b and r == l:
        return f"{t} {r}"
    return f"{t} {r} {b} {l}"


def fam(f):
    return f.split(",")[0].replace('"', "")


def font(fz, lh, fw, f, style="normal"):
    lh = "normal" if lh == "normal" else px(lh)
    return f"{fam(f)} {px(fz)}/{lh} {fw}" + (" italic" if style == "italic" else "")


def shadow_layers(s):
    """Both 'rgba(..) 0px 2px 3px 0px, ...' and '0px 2px 3px #a9b3c64d,...' -> comparable tuples."""
    out = []
    parts = re.split(r",(?![^(]*\))", s)
    for p in parts:
        p = p.strip()
        if not p or p == "none":
            continue
        col = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", p)
        c = col.group(0) if col else "rgb(0,0,0)"
        rest = p.replace(c, "")
        nums = [float(x) for x in re.findall(r"-?[\d.]+(?=px)", rest)]
        nums = (nums + [0, 0, 0, 0])[:4]
        if c.startswith("#"):
            h = c[1:]
            if len(h) in (3, 4):
                h = "".join(ch * 2 for ch in h)
            r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
            a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
        else:
            m = re.findall(r"[\d.]+", c)
            r, g, b = (float(x) for x in m[:3])
            a = float(m[3]) if len(m) > 3 else 1.0
        out.append((tuple(nums), round(r), round(g), round(b), round(a, 2), bool(re.search(r"\binset\b", p))))
    return out


SHADOW_TOK = {}
for name, val in ROOTV.items():
    if name.startswith("--shadow-") and not name.endswith("-dark"):
        SHADOW_TOK[tuple(shadow_layers(val))] = name


for n, t in LEAF.items():
    if t["$type"] == "shadow":
        val = ", ".join(f"{l['color']} {l['offsetX']} {l['offsetY']} {l['blur']} {l['spread']}{' inset' if l.get('inset') else ''}"
                        for l in t["$value"])
        SHADOW_TOK.setdefault(tuple(shadow_layers(val)), "{" + n + "}")


def shadow_token(s):
    # offsets, blur, spread (0 when a root var omits it), colour and inset must all match
    return SHADOW_TOK.get(tuple(shadow_layers(s)))


def shadow_text(s):
    if not s or s == "none":
        return None
    tok = shadow_token(s)
    layers = []
    for p in re.split(r",(?![^(]*\))", s):
        p = p.strip()
        col = re.search(r"rgba?\([^)]*\)", p)
        c = colour(col.group(0), tokens=False) if col else ""
        rest = (p.replace(col.group(0), "") if col else p).strip()
        layers.append(f"{c} {rest}".strip())
    return ", ".join(layers) + (f" (`{tok}`)" if tok else "")


# --------------------------------------------------------------------------- properties of one state


def props(v):
    s = v["style"]
    o = OrderedDict()
    o["size"] = f"{px(v['rect']['w'])} x {px(v['rect']['h'])}" + size_tok(v["rect"]["w"], v["rect"]["h"])
    pad = sides(s["paddingTop"], s["paddingRight"], s["paddingBottom"], s["paddingLeft"])
    if pad != "0px":
        o["padding"] = space_tok(pad)
    if s["display"] in ("flex", "inline-flex", "grid") and s["gap"] not in ("normal", "0px"):
        o["gap"] = space_tok(s["gap"])
    bds = []
    for d in ("Top", "Right", "Bottom", "Left"):
        if float(s[f"border{d}Width"].replace("px", "")) > 0 and s[f"border{d}Style"] != "none":
            bds.append(f"{s[f'border{d}Width']} {s[f'border{d}Style']} {colour(s[f'border{d}Color'], role='border')}")
        else:
            bds.append("none")
    if any(b != "none" for b in bds):
        o["border"] = bds[0] if len(set(bds)) == 1 else "; ".join(f"{'TRBL'[i]}: {b}" for i, b in enumerate(bds) if b != "none")
    rad = sides(s["borderTopLeftRadius"], s["borderTopRightRadius"], s["borderBottomRightRadius"], s["borderBottomLeftRadius"])
    if rad != "0px":
        o["radius"] = radius_tok(rad)
    o["background"] = colour(s["backgroundColor"], role='bg')
    if s["backgroundImage"] != "none":
        img = re.sub(r'url\("data:[^)]*\)', "an image (data URI)", s["backgroundImage"])
        o["image"] = colour(img, role='image')[:200]
    if s["boxShadow"] != "none":
        o["shadow"] = shadow_text(s["boxShadow"])
    if s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0:
        o["outline"] = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'], role='border')}, offset {s['outlineOffset']}"
    t = v.get("textStyle")
    if t:
        o["text"] = f"{font(t['fontSize'], t['lineHeight'], t['fontWeight'], t['fontFamily'], t.get('fontStyle', 'normal'))}, {colour(t['color'], role='text')}"
        if t.get("textDecorationLine") not in (None, "none"):
            o["text"] += f", {t['textDecorationLine']}"
    else:
        o["text"] = f"{font(s['fontSize'], s['lineHeight'], s['fontWeight'], s['fontFamily'], s.get('fontStyle', 'normal'))}, {colour(s['color'], role='text')}"
        if s["textDecorationLine"] != "none":
            o["text"] += f", {s['textDecorationLine']}"
    if s["opacity"] != "1":
        o["opacity"] = s["opacity"]
    if s["transform"] not in ("none", "matrix(1, 0, 0, 1, 0, 0)"):
        o["transform"] = s["transform"]
    if s["cursor"] not in ("auto", "default"):
        o["cursor"] = s["cursor"]
    if s["transitionDuration"] not in ("0s", ""):
        pr = [x.strip() for x in s["transitionProperty"].split(",")]
        du = [x.strip() for x in s["transitionDuration"].split(",")]
        tf = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", s["transitionTimingFunction"])
        parts = [f"{p} {du[i % len(du)]} {tf[i % len(tf)] if tf else ''}".strip() for i, p in enumerate(pr) if du[i % len(du)] != "0s"]
        if parts:
            o["transition"] = ", ".join(parts)
    if v.get("icon") and 0 < v["icon"]["w"] < 120:
        ic = v["icon"]
        o["icon"] = f"{px(ic['w'])} x {px(ic['h'])}, {colour(ic['stroke'] if ic['fill'] == 'none' and ic['stroke'] != 'none' else ic['color'], role='text')}"
    if v.get("placeholder"):
        o["placeholder"] = colour(v["placeholder"]["color"], role='text')
    return o


ORDER = ["size", "padding", "gap", "border", "radius", "background", "image", "shadow", "outline", "text", "opacity", "transform", "cursor", "transition", "icon", "placeholder"]


def fmt(d):
    return "; ".join(f"{k} {d[k]}" for k in ORDER if k in d).replace("|", "/")


def diff(p, base):
    d = {k: p[k] for k in ORDER if k in p and p.get(k) != base.get(k)}
    for k in ORDER:
        if k in base and k not in p:
            d[k] = "none"
    return d


def focus_not_captured(v):
    """A state whose reading is not what its name says: a skipped one, or a focus-visible reading
    taken where keyboard focus never landed (kbFocus returned "focus failed") or where the element
    took focus but did not match :focus-visible. Its style is the element at rest, so it is left out
    of every table and tally and listed as "focus could not be captured"."""
    return bool(v.get("skipped")) or v.get("via") == "focus failed" or (v.get("focus") or {}).get("matches") is False


NOT_CAPTURED = "not focusable, or focused without matching :focus-visible"


def groups_of_states(c):
    """[(base_label, base_value, [(variant_label, value)])] from the states in file order.

    A base state is read at rest; a hover, focus-visible or pressed state belongs to the base it was read
    with (same label with the suffix removed)."""
    bases = OrderedDict()
    variants = []
    for lab, v in c["states"].items():
        if "style" not in v:
            continue
        via = v.get("via", "")
        if via == "mouse hover":
            variants.append((lab[: -len("hover")].rstrip("-") or "default", "hover", v))
        elif via.startswith("keyboard"):
            variants.append((lab[: -len("focus-visible")].rstrip("-") or "default", "focus-visible", v))
        elif via == "mouse held down":
            variants.append((lab[: -len("pressed")].rstrip("-") or "default", "pressed", v))
        else:
            bases[lab] = v
    out = []
    for lab, v in bases.items():
        out.append((lab, v, [(kind, vv) for b, kind, vv in variants if b == lab or (b == "default" and lab == "default")]))
    return out


# --------------------------------------------------------------------------- parts (the `extra` blobs)


def part(name, b, origin=None):
    r = b["rect"]
    bits = [f"{px(r['w'])} x {px(r['h'])}"]
    if origin is not None:
        bits.append(f"at {px(round(r['x'] - origin[0], 1))}, {px(round(r['y'] - origin[1], 1))}")
    f = b.get("font", "")
    m = re.match(r"(\d+) ([\d.]+)px/([\d.a-z]+) (.*)", f)
    if m and b.get("text") is not None or (m and b.get("tag") in ("p", "h1", "h2", "h3", "h4", "h5", "span", "label", "a", "button", "input")):
        lh = "normal" if m.group(3) == "normal" else px(m.group(3))
        bits.append(f"{m.group(4)} {px(m.group(2))}/{lh} {m.group(1)}{' italic' if b.get('fontStyle') == 'italic' else ''}, {colour(b['color'], role='text')}")
    for k, lab in (("bg", "background"), ("radius", "radius"), ("padding", "padding"), ("margin", "margin"), ("gap", "gap"), ("border", "border"), ("boxShadow", "shadow")):
        if b.get(k) and b[k] not in ("0px", "normal"):
            val = (colour(b[k], role=k) if k in ("bg", "border") else shadow_text(b[k]) if k == "boxShadow"
                   else space_tok(b[k]) if k in ("padding", "margin", "gap") else radius_tok(b[k]) if k == "radius" else b[k])
            bits.append(f"{lab} {val}")
    if b.get("bgImage"):
        bits.append("image " + colour(b["bgImage"], role='image')[:110])
    if b.get("opacity"):
        bits.append(f"opacity {b['opacity']}")
    if b.get("text"):
        bits.append(f"text \"{b['text'][:30]}\"")
    return f"{name}: " + "; ".join(bits).replace("|", "/")


def kids_lines(name, v):
    cont = v["container"]
    origin = (cont["rect"]["x"], cont["rect"]["y"])
    out = [f"{name}: {part('container', cont).split(': ', 1)[1]}"]
    for ch in v["children"][:10]:
        nm = (ch.get("text") or ch.get("label") or ch["tag"])[:24]
        out.append("  child " + part(nm, ch, origin))
    return out


def parts_lines(extra):
    out = []
    if not extra:
        return out
    if "children" in extra and "container" in extra:
        return kids_lines("container", extra)
    for k, v in extra.items():
        if isinstance(v, dict) and "rect" in v:
            out.append(part(k, v))
        elif isinstance(v, dict) and "children" in v:
            out.extend(kids_lines(k, v))
        elif isinstance(v, list):
            for i, it in enumerate(v):
                if isinstance(it, dict) and "rect" in it:
                    out.append(part(f"{k} {i + 1}", it))
    return out


# --------------------------------------------------------------------------- text blocks

PAGE_NAME = {
    "sp": "search split view", "sp-hover-input": "search split view (hovering a search input node)",
    "sp-hover-result": "search split view (hovering a result node)", "sp-hover-list-card": "search split view (hovering a list card)",
    "sp-hover-legend-inputs": "search split view (hovering the Search inputs legend chip)", "sp-hover-legend-results": "search split view (hovering the Results legend chip)",
    "sp-inspect": "search split view (a node inspected)", "sm": "search map view", "sm-zoom": "search map view (zoomed in)",
    "sm-inspect": "search map view (a node inspected)", "sm-x": "search map view (layout settings, X Axis)", "sm-y": "search map view (layout settings, Y Axis)",
    "sm-size": "search map view (layout settings, Size)", "sm-adv": "search map view (layout settings, Advanced)", "sm-filter": "search map view (filter popover open)",
    "sl": "search list view", "lm": "library map view", "lm-hover": "library map view (hover)", "lm-moved": "library map view (positions moved)",
    "lm-reset": "library map view (reset menu open)", "ll": "library list view", "home": "home page",
    "home2": "home page (2026-10-17)", "home-typed": "home page (a query typed, not sent)", "menu-ws": "home page (workspace menu open)",
    "menu-acc": "home page (account menu open)", "acc-profile": "Account Settings dialog (Profile)", "acc-edit": "Update profile dialog",
    "acc-delete": "Delete Account confirmation", "acc-prefs": "Account Settings dialog (Preferences)", "acc-subs": "Account Settings dialog (Subscription, empty)",
    "kw": "keyword search results (list view)", "kw-loading": "keyword search results (next page loading)", "kw-updating": "keyword search results (updating dialog)",
    "kw-selected": "keyword search results (one article selected)", "st-open": "Search Settings drawer (open)", "st-select": "Search Settings drawer (select open)",
    "st-checked": "Search Settings drawer (Open Access checked)", "lib-all": "library, All Articles", "lib-table": "library, All Articles in table view",
    "lib-reading": "library, Reading List (empty)", "mobile-warn": "library at 390px (Screen too small)", "mobile-lib": "library at 390px (after Continue anyway)",
    "search-start": "Search start page (recent searches)",
    "lib-cite": "library, Cite Article dialog", "lib-toast": "library, Cite Article (citation copied, toast showing)",
    "kw-missing": "keyword search results (an article with no citation data inspected)", "tablet": "search list view at 1000 x 800 (an article inspected)",
    "home-narrow": "home page at 800 x 900", "lib-notes": "library, article Notes tab (empty)", "lib-selected": "library, All Articles (one selected)",
}

GROUP_INTRO = {
    "Shell and navigation": "The frame shared by every signed-in page: a pastel gradient ground, a 64px top bar that paints nothing, a half-white main card with a solid white header strip, and a 390px right panel. Search pages add a translucent grey session bar under the top bar.",
    "Search header": "The row at the top of the main card: the \"Similar articles to 9 Articles\" summary capsule at the left, then the filter button and the three-way view toggle at the right.",
    "Graph": "The graph area. Everything drawn on the canvas (nodes, edges, labels, the hover title box) is a bitmap in the snapshots; this group measures the DOM around it: the legend, the axis captions, the toolbar, the Positions moved pill and the legend tooltip. The canvas crops are the only record of node drawing, so read node colours and sizes from graph.md and raw/graph-code-notes.md.",
    "Article list": "The 400px column of result cards in the split view, and the same cards at full width in the list view and in the library.",
    "Next Search panel": "The right panel when nothing is selected: a header, a dismissible tip, an empty state, and the black Search Settings drawer.",
    "Article detail panel": "The right panel when an article is selected, from the graph or from the list. It reuses the black drawer as \"Dive deeper on this article\".",
    "Layout settings": "The right panel the graph toolbar opens: four tabs for how the map is laid out (X Axis, Y Axis, Size, Advanced).",
    "Library": "The Library page: a sidebar of lists and collections, a collection header, a selection bar, and the same list, split and map views as search.",
    "Home": "The home page: a hero with a search field, then three white cards (recent articles, collections, getting started).",
    "Dialogs": "Read on 2026-10-17. Account Settings, a form dialog stacked on it, the destructive confirmation and the loading dialog all use one modal: a white sheet over a teal-grey scrim.",
    "Buttons": "Read on 2026-10-17. The button kinds outside the search chrome: the black primary, the text-only secondary, the pale red destructive button, disabled buttons, and text buttons. Pressed is the mouse held down; no captured rule styles `:active` except the slider thumb's cursor, so a pressed button keeps its hover fill.",
    "Form controls": "Read on 2026-10-17. Fields, the checkbox, single- and multi-choice pills, the select, the range slider and the note composer. The light controls live in dialogs; the dark ones on the black Search Settings drawer.",
    "Tabs and navigation": "Read on 2026-10-17. The vertical tabs of Account Settings and the filter pills above the Reading List.",
    "Menus": "Read on 2026-10-17. The workspace menu (Radix dropdown) and the account popover.",
    "Avatar and badges": "Read on 2026-10-17. The placeholder avatar, the green Upgrade badge and the notice banner.",
    "Feedback and loading": "Read on 2026-10-17. The spinner, the selection circle and its Clear link, the toast (raised by copying a citation), the inline error and the incomplete-data warning.",
    "Data display": "Read on 2026-10-17. The library table and the recent-search rows.",
    "Empty states": "Read on 2026-10-17. Each empty list or tab has its own line of copy; the Reading List and Notes add an illustration or a heading.",
    "Phone width": "Read on 2026-10-17 at 390 x 844, 800 x 900 and 1000 x 800. Below 641px the app has no layout and shows a notice instead; between that and desktop it keeps the desktop frame and changes only what its script breakpoints switch (raw/app-code-notes.md).",
}

SHOTS = [
    ("search-split", "Search, split view. The list of result cards beside the graph, Next Search at the right. Default, a search input node hovered, a result node hovered, a list card hovered (it stays tinted), the two legend chips hovered, and a node inspected.", "/search/<id>/0"),
    ("search-map", "Search, map view. The graph fills the main card. Default, zoomed in, a node inspected, the four layout settings tabs, and the filter popover.", "/search/<id>/0"),
    ("search-list", "Search, list view. The result cards at full width; on 2026-10-17 a keyword search: results, the next page loading, the updating dialog, one article selected, an article with no citation data (the inline error), and the Search Settings drawer open, with its select open and a checkbox checked.", "/search/<id>/0"),
    ("search-start", "Search start page (2026-10-17): the search field, the BibTeX drop zone and the recent searches.", "/search"),
    ("library-map", "Library, map view of one collection. Default, hovering, after a node was dragged (Positions moved), and the Reset menu open.", "/library/<id>"),
    ("library-list", "Library, list view of one collection, with the sidebar and the collection header.", "/library/<id>"),
    ("home", "Home. Hero with the search field, recent articles, collections and guides; on 2026-10-17 again, with a query typed and the workspace and account menus open.", "/"),
    ("account", "Account Settings dialog (2026-10-17), opened from the account menu: Profile, Preferences, an empty Subscription tab, the Update profile dialog stacked on it, and the Delete Account confirmation (cancelled).", "/?account=<tab>"),
    ("library-all", "Library, All Articles (2026-10-17): the list, one article selected, an article's empty Notes tab, the Cite Article dialog, and the toast after copying a citation.", "/library"),
    ("library-table", "Library, All Articles in the table view (2026-10-17).", "/library"),
    ("library-reading", "Library, the empty Reading List (2026-10-17).", "/library/reading"),
    ("search-tablet", "Search list view at 1000 x 800 (2026-10-17), an article inspected: the right panel shrinks toward its 290px minimum (314.67px here) and the list narrows.", "/search/<id>/0"),
    ("home-narrow", "Home at 800 x 900 (2026-10-17): below 896px the three cards stack in one column.", "/"),
    ("library-mobile", "Library at 390 x 844 (2026-10-17): the Screen too small notice, and the clipped desktop layout after Continue anyway.", "/library"),
]

OVER = [
    ("Legend tooltip", "search split view", "pointer over a legend chip when the snapshot was taken", "[search-split-light-hover-legend-inputs](screenshots/search-split-light-hover-legend-inputs.png), [search-split-light-hover-legend-results](screenshots/search-split-light-hover-legend-results.png), [graph-tooltip](#legend-tooltip)"),
    ("Node hover title", "search split view", "pointer over a node; the white title box is drawn on the canvas, so it is only in the crop", "[search-split-light-hover-result](screenshots/search-split-light-hover-result.png), [search-split-light-hover-input](screenshots/search-split-light-hover-input.png)"),
    ("Tinted list card", "search split view", "pointer over a card when the snapshot was taken; its node is highlighted in the graph", "[search-split-light-hover-list-card](screenshots/search-split-light-hover-list-card.png), [result card](#result-card)"),
    ("Article detail panel", "search split and map views", "a node clicked", "[search-split-light-inspect-node](screenshots/search-split-light-inspect-node.png), [search-map-light-inspect-node](screenshots/search-map-light-inspect-node.png), [article detail panel](#article-detail-panel)"),
    ("Layout settings, four tabs", "search map view", "the settings button in the graph toolbar, then each tab", "[x-axis](screenshots/search-map-light-settings-x-axis.png), [y-axis](screenshots/search-map-light-settings-y-axis.png), [size](screenshots/search-map-light-settings-size.png), [advanced](screenshots/search-map-light-settings-advanced.png), [layout settings panel](#layout-settings-panel)"),
    ("Filter popover", "search map view", "the filter button", "[search-map-light-filter-popover](screenshots/search-map-light-filter-popover.png), [filter popover](#filter-popover)"),
    ("Positions moved and Reset menu", "library map view", "a node dragged, then the pill pressed", "[library-map-light-positions-moved](screenshots/library-map-light-positions-moved.png), [library-map-light-positions-reset-menu](screenshots/library-map-light-positions-reset-menu.png), [positions moved pill](#positions-moved-pill)"),
    ("Zoomed graph", "search map view", "scroll or zoom button; the canvas is redrawn at a larger scale", "[search-map-light-zoomed-in](screenshots/search-map-light-zoomed-in.png)"),
    ("Workspace and account menus", "home page", "the top-bar buttons, one item under the pointer", "[home-light-workspace-menu](screenshots/home-light-workspace-menu.png), [home-light-account-menu](screenshots/home-light-account-menu.png), [menu](#menu), [account menu](#account-menu)"),
    ("Dialogs, stacked", "Account Settings", "account menu, then Preferences or Profile, then Update Profile", "[account-light-profile](screenshots/account-light-profile.png), [account-light-edit-profile-dialog](screenshots/account-light-edit-profile-dialog.png), [dialog](#dialog)"),
    ("Destructive confirmation", "Account Settings, Profile", "Delete Account, then Cancel; nothing typed", "[account-light-delete-confirm](screenshots/account-light-delete-confirm.png), [destructive confirmation](#destructive-confirmation)"),
    ("Loading", "keyword search results", "the copy was taken by a script the moment the spinner or loading dialog mounted", "[search-list-light-loading](screenshots/search-list-light-loading.png), [search-list-light-updating-dialog](screenshots/search-list-light-updating-dialog.png), [spinner](#spinner)"),
    ("Selected article", "keyword search results, All Articles", "the selection circle clicked, then Clear", "[search-list-light-selected](screenshots/search-list-light-selected.png), [library-all-light-selected](screenshots/library-all-light-selected.png), [selection circle](#selection-circle)"),
    ("Toast", "library, All Articles", "an article's Cite button, then the citation box clicked (copies to the clipboard); the copy was taken the moment the toast mounted", "[library-all-light-cite-dialog](screenshots/library-all-light-cite-dialog.png), [library-all-light-toast](screenshots/library-all-light-toast.png), [toast](#toast)"),
    ("Inline error", "keyword search results", "an article with no references and no citations inspected; the drawer shows Cannot search", "[search-list-light-citation-missing](screenshots/search-list-light-citation-missing.png), [inline error](#inline-error), [incomplete data warning](#incomplete-data-warning)"),
    ("Select list, checked checkbox", "Search Settings drawer", "the Retractions select opened; Open Access checked, then unchecked", "[search-list-light-settings-select-open](screenshots/search-list-light-settings-select-open.png), [search-list-light-settings-checked](screenshots/search-list-light-settings-checked.png)"),
]

SHAPES = ["main-card", "side-panel", "list-card", "search-summary", "view-toggle", "filter-popover", "graph-tooltip", "tip-banner", "drawer", "inspector", "layout-option", "layout-select", "positions-moved", "reset-menu", "library-sidebar", "collection-header", "home-section", "home-guide-card"]

L = []


def W(s=""):
    L.append(s)


def slug(title):
    return re.sub(r"[^a-z0-9 -]", "", title.lower()).replace(" ", "-")


shots = sorted(p.name for p in Path("screenshots").glob("*.png"))


def links(prefix):
    out = []
    for f in shots:
        m = re.fullmatch(re.escape(prefix) + r"-light-(.+)\.png", f)
        if m:
            out.append(f"[{m.group(1)}](screenshots/{f})")
    return ", ".join(out)


crop_files = sorted(p.name for p in Path("components/crops").glob("*.png"))
n_states = sum(len(c["states"]) for c in C.values())
icons = [r for r in csv.reader(open("icons/INDEX.tsv"), delimiter="\t")][1:]

# ------------------------------------------------ head
W("# ResearchRabbit components")
W()
W("The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Read on 2026-10-04 and again on 2026-10-17 (the dialogs, menus, forms, table, empty, loading and error states, the toast, pressed states, and the tablet and phone widths) from static, redacted snapshots of signed-in pages on app.researchrabbit.ai, rendered in headless Chromium at 1440 x 900 (2x; the narrow pages at 1000 x 800, 800 x 900 and 390 x 844), with computed styles read from the rendered page. The workspace, account and collection names in the snapshots are redacted. Nothing was created, sent or changed; one keyword search was run, an article was selected and cleared, a filter was checked and unchecked, and a citation was copied to the clipboard.")
W()
W(f"The machine-readable copy is [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). Custom properties and per-component CSS rules are in [raw/css-vars.json](raw/css-vars.json); how the graph engine draws is in [raw/graph-code-notes.md](raw/graph-code-notes.md).")
W()
W("How to read an entry:")
W()
W("- A component is found by its styled-components display name (`GraphControls__StyledButton`), so `generateVariantComponent__default`, which many unrelated buttons share, is found by text or position instead. The entry's heading is the product's name for the part, and the key in backticks is the key in the JSON.")
W("- A colour, shadow, radius, padding, gap or control height is its value followed by the [tokens.json](tokens.json) token with the same value (`{palette.grey.primary}`, `{elevation.menu}`, `{radius.lg}`, `{spacing.2}`, `{size.control-md}`), when there is one; a colour names the light-set role for what it paints (`{background.surface}` for a fill, `{text.default}` for text, `{border.default}` for a border; these live in the light set) and falls back to the palette token when no role has that value; an entry's own `component.*` token (by name: `component.toast` for the toast, `component.tooltip` for the graph tooltip, `component.menu-separator` for a menu's rule) is named first for its fill, so a token is only chosen by value when the component has none of its own. Collection colours (`palette.ugc.*`) stay palette tokens because the user picks them per collection. Text is written family size/line-height weight, then its colour, for example `Plus Jakarta Sans 14/21 400, #000000 {palette.base.black}`, and is read from the first text node inside the component.")
W("- The state table has one row per element or snapshot state read at rest. A hover, focus-visible or pressed row lists only what changes from the row above it; a state with the same values is named in the row's label, for example \"default (same: hover)\". Hover is a real mouse hover, focus-visible a real keyboard focus and pressed the mouse held down (2026-10-17 pages only); where a snapshot state could not be reached it says so.")
W("- \"Parts\" lists the pieces inside the component, with sizes and offsets measured from the component's corner.")
W(f"- Crops are images of the component read from the rendered snapshot, in [components/crops/](components/crops) ({len(crop_files)} files, named `{{component}}-{{state}}.png`, at 2x, 256 colours). A crop wider than 1600px was halved. A state that paints the same pixels as its default has no file of its own. Screenshots are in [screenshots/](screenshots).")
W()

# ------------------------------------------------ discovery list
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (the captured theme is light; the product has no dark theme). They are 1440 x 900 at 2x (the two `library-mobile` ones 390 x 844), 256 colours. The graph canvas in every one of them is a bitmap, frozen exactly as captured.")
W()
W("| Surface | URL | Screenshots |")
W("|---|---|---|")
for p, desc, url in SHOTS:
    W(f"| {desc} | `{url}` | {links(p)} |")
W()
W("### Overlays and transient states")
W()
W("| State | Where | How it was reached | Captured |")
W("|---|---|---|---|")
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement file. Counts are components whose first state has the value.")
W()

first_state = {}
for k, c in C.items():
    for lab, v in c["states"].items():
        if "style" in v:
            first_state[k] = v
            break

# fonts
fonts = V.get("fonts", [])
fam_count = Counter()
for k, v in first_state.items():
    t = v.get("textStyle")
    fam_count[fam(t["fontFamily"]) if t else fam(v["style"]["fontFamily"])] += 1
unused_fonts = [f.replace('+', ' ') for f in fonts if f.replace('+', ' ') not in fam_count]
W(f"**Type.** Two faces are loaded from Google Fonts: {', '.join(f.replace('+', ' ') for f in fonts)}. First-state text is set in {', '.join(f'{n} ({c} components)' for n, c in sorted(fam_count.items(), key=lambda kv: (-kv[1], kv[0])))}." + (f" No measured component renders in {', '.join(unused_fonts)}, which is requested in a light weight only." if unused_fonts else ""))
W()
tcount = defaultdict(list)
for k, v in first_state.items():
    t = v.get("textStyle")
    s = v["style"]
    key = (fam(t["fontFamily"]), px(t["fontSize"]), px(t["lineHeight"]) if t["lineHeight"] != "normal" else "normal", t["fontWeight"], t.get("fontStyle", "normal")) if t else (fam(s["fontFamily"]), px(s["fontSize"]), px(s["lineHeight"]) if s["lineHeight"] != "normal" else "normal", s["fontWeight"], s.get("fontStyle", "normal"))
    tcount[key].append(k)
W("| Type | Components using it |")
W("|---|---|")
for key, ks in sorted(tcount.items(), key=lambda kv: (-len(kv[1]), kv[0])):
    if len(ks) < 2:
        continue
    W(f"| {key[0]} {key[1]}/{key[2]} {key[3]}{' italic' if key[4] == 'italic' else ''} | {len(ks)}: {', '.join('`' + x + '`' for x in sorted(ks)[:6])}{' and more' if len(ks) > 6 else ''} |")
W()

# radii
rad = defaultdict(list)
for k, v in first_state.items():
    s = v["style"]
    r = sides(s["borderTopLeftRadius"], s["borderTopRightRadius"], s["borderBottomRightRadius"], s["borderBottomLeftRadius"])
    if r != "0px":
        rad[r].append((k, v["rect"]["h"]))
W("**Radii.**")
W()
W("| Radius | Count | Components |")
W("|---|---|---|")


def rkey(r):
    try:
        return -float(r.split()[0].replace("px", ""))
    except ValueError:
        return 0


for r, ks in sorted(rad.items(), key=lambda kv: (rkey(kv[0]), kv[0])):
    W(f"| {r} | {len(ks)} | {', '.join('`' + x[0] + '`' for x in sorted(ks)[:7])}{' and more' if len(ks) > 7 else ''} |")
W()
pills = sorted(k for k, v in first_state.items() if v["style"]["borderTopLeftRadius"].endswith("px") and float(v["style"]["borderTopLeftRadius"].replace("px", "") or 0) >= v["rect"]["h"] / 2 and v["rect"]["h"] >= 20 and v["style"]["borderTopLeftRadius"] == v["style"]["borderBottomRightRadius"])
h48 = [first_state[k]["rect"]["h"] for k in pills if first_state[k]["style"]["borderTopLeftRadius"] == "48px"]
# A recapture with no 48px pill drops that clause instead of failing on min() of nothing.
r48 = f" {len(h48)} of them use `48px` whatever their height ({min(h48)} to {max(h48)}px), so `48px` reads as fully round." if h48 else ""
W(f"**Pill shape.** A component is a pill when its radius is at least half its height. {len(pills)} are: {', '.join('`' + k + '`' for k in pills)}.{r48} Cards, panels and menus use `6px` to `16px`; the drawer's top corners are `32px`.")
W()

# shadows
sh = defaultdict(list)
for k, c in C.items():
    for lab, v in c["states"].items():
        if "style" not in v:
            continue
        s = v["style"]["boxShadow"]
        if s != "none":
            sh[shadow_text(s)].append(k)
used_tok = {shadow_token(s_) for s_ in sh if s_} - {None}
W("**Shadows.** Every box shadow read on a component, with the token it equals where there is one. " + ("The :root shadow tokens (" + ", ".join(f"`{n}`" for n in sorted(set(SHADOW_TOK.values()))) + ") are not used by any measured component, so cards and panels are flat; the shadows below are focus-like rings and the popover, tooltip and menu drop shadows." if not used_tok else ""))
W()
W("| Shadow | Where |")
W("|---|---|")
for s, ks in sorted(sh.items(), key=lambda kv: (-len(set(kv[1])), kv[0])):
    ks = sorted(set(ks))
    W(f"| {s} | {', '.join('`' + x + '`' for x in ks[:8])}{' and more' if len(ks) > 8 else ''} |")
if not sh:
    W("| none | |")
W()

# colours
cc = Counter()
cwhere = defaultdict(set)
for k, v in first_state.items():
    s = v["style"]
    for prop in ("backgroundColor", "color"):
        c = colour(s[prop], role='bg' if prop == "backgroundColor" else "text")
        if c != "transparent":
            cc[(prop, c)] += 1
            cwhere[(prop, c)].add(k)
W("**Colours in use.** Background and text colours of the first state of each component, most used first.")
W()
W("| Use | Colour | Components |")
W("|---|---|---|")
for (prop, c), n in sorted(cc.items(), key=lambda kv: (-kv[1], kv[0]))[:28]:
    W(f"| {'background' if prop == 'backgroundColor' else 'text'} | {c} | {n} |")
W()

# motion
mot = defaultdict(lambda: (set(), set()))


def dur_ms(d):
    d = d.strip()
    return float(d[:-2]) if d.endswith("ms") else float(d[:-1]) * 1000


for k, c in C.items():
    for v in c["states"].values():
        if "style" not in v:
            continue
        s = v["style"]
        if s["transitionDuration"] in ("0s", ""):
            continue
        pr = [x.strip() for x in s["transitionProperty"].split(",")]
        du = [x.strip() for x in s["transitionDuration"].split(",")]
        tf = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", s["transitionTimingFunction"])
        for i, p in enumerate(pr):
            d = du[i % len(du)]
            if d == "0s":
                continue
            key = (f"{int(round(dur_ms(d)))}ms", tf[i % len(tf)] if tf else "ease")
            mot[key][0].add(p)
            mot[key][1].add(f"`{k}`")
for name, rules in V["components"].items():
    for r in rules:
        for m in re.finditer(r"transition\s*:\s*([^;}]+)", r):
            for part_ in re.split(r",(?![^(]*\))", m.group(1)):
                bits = part_.replace("!important", "").split()
                if len(bits) >= 2 and re.fullmatch(r"[\d.]+m?s", bits[1]) and dur_ms(bits[1]) < 5000:
                    key = (f"{int(round(dur_ms(bits[1])))}ms", bits[2] if len(bits) > 2 else "ease")
                    mot[key][0].add(bits[0])
                    mot[key][1].add(name)
W("**Motion.** Transitions in the page's CSS (every styled component's rules, in [raw/css-vars.json](raw/css-vars.json)) and on the measured elements. The CSS defines no transition on a hover or focus colour except the scrollbar thumb; the rest are opacity, transform and width changes on panels, the drawer and overlays.")
W()
W("| Duration | Easing | Property | Where |")
W("|---|---|---|---|")
for (d, e), (ps, ks) in sorted(mot.items(), key=lambda kv: (dur_ms(kv[0][0]), kv[0][1])):
    ks = sorted(ks)
    W(f"| {d} | `{e}` | {', '.join(sorted(ps))} | {', '.join(ks[:6])}{' and more' if len(ks) > 6 else ''} |")
if not mot:
    W("| none found | | | |")
W()

# focus
ring, same_f, changed_f, nofocus = defaultdict(list), [], [], []
for k, c in C.items():
    for bl, bv, vs in groups_of_states(c):
        for kind, v in vs:
            if kind != "focus-visible":
                continue
            if focus_not_captured(v):
                nofocus.append(k)
                continue
            s_ = v["style"]
            if s_["outlineStyle"] != "none" and float(s_["outlineWidth"].replace("px", "")) > 0:
                ring[f"{s_['outlineWidth']} {s_['outlineStyle']} {colour(s_['outlineColor'], role='border')}, offset {s_['outlineOffset']}"].append(k)
            elif diff(props(v), props(bv)):
                changed_f.append(k)
            else:
                same_f.append(k)
n_ring = len({k for ks in ring.values() for k in ks})
focus_txt = f"**Focus.** Real keyboard focus was given to every component that could take it. {n_ring} draw an outline ring, in {len(ring)} styles: " + "; ".join(
    f"{r} on {', '.join('`' + k + '`' for k in sorted(set(ks))[:5])}{' and more' if len(set(ks)) > 5 else ''}" for r, ks in sorted(ring.items(), key=lambda kv: (-len(set(kv[1])), kv[0]))) + ". "
if changed_f:
    focus_txt += f"{len(set(changed_f))} change something other than an outline: {', '.join('`' + k + '`' for k in sorted(set(changed_f))[:8])}. "
if same_f:
    focus_txt += f"{len(set(same_f))} show no change in computed style, so a keyboard user sees nothing: {', '.join('`' + k + '`' for k in sorted(set(same_f))[:12])}. "
if nofocus:
    focus_txt += f"Focus could not be captured on {len(set(nofocus))} more ({NOT_CAPTURED}), left out of the tally: {', '.join('`' + k + '`' for k in sorted(set(nofocus)))}."
W(focus_txt.strip())
W()

# hover
hv = Counter()
hv_bg = Counter()
for k, c in C.items():
    for bl, bv, vs in groups_of_states(c):
        for kind, v in vs:
            if kind == "hover" and v.get("hovered") is not False:
                d = diff(props(v), props(bv))
                hv["changes" if d else "same"] += 1
                if "background" in d:
                    hv_bg[(props(bv)["background"], d["background"])] += 1
W(f"**Hover.** {hv['changes']} hovered states differ from their rest state in computed style and {hv['same']} do not (they change something drawn on the canvas, or nothing). Background changes on hover, most common first:")
W()
W("| From | To | Count |")
W("|---|---|---|")
for (a_, b_), n in sorted(hv_bg.items(), key=lambda kv: (-kv[1], kv[0]))[:12]:
    W(f"| {a_} | {b_} | {n} |")
W()

# layout
W("**Layout regions.** The page's main regions at the captured size, from the DOM ([raw/components-computed.json](raw/components-computed.json), `pages`). Pages with the same region are listed together.")
W()
W("| Region | x | y | width | height | Background | Radius | Pages |")
W("|---|---|---|---|---|---|---|---|")
reg = OrderedDict()
for pk, pv in PG.items():
    for rn, r in pv.get("regions", {}).items():
        key = (rn, px(r["x"]), px(r["y"]), px(r["w"]), px(r["h"]), colour(r["bg"], role='bg') if r.get("bg") else "-", r.get("radius", "-"))
        reg.setdefault(key, []).append(pk)
for key, pks in sorted(reg.items(), key=lambda kv: (kv[0][0], kv[1][0])):
    W(f"| {' | '.join(key)} | {', '.join(pks) if len(pks) <= 4 else f'{pks[0]} and {len(pks) - 1} more'} |")
W()

# shapes
W("**Surface shapes.** Values from the first state of each; the entries hold the others.")
W()
W("| Surface | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
for k in SHAPES:
    if k not in C or k not in first_state:
        continue
    st = first_state[k]
    p = props(st)
    if (p["background"] == "transparent" or "radius" not in p) and st.get("paint"):
        p0 = next((x for x in st["paint"] if x.get("bg") and x.get("radius")), st["paint"][0])
        p = dict(p, border=colour(p0["border"].split(" | ")[0][2:]) if p0.get("border") else "-", radius=p0.get("radius", "-"), background=colour(p0.get("bg", ""), role='bg') or "-", shadow=shadow_text(p0.get("shadow", "")) or "none")
    W(f"| [{C[k]['name']}](#{slug(C[k]['name'])}) | {p['size']} | {p.get('border', '-')} | {p.get('radius', '-')} | {p.get('background', '-')} | {p.get('shadow', 'none')} | {p.get('padding', '0')} |")
W()

# ------------------------------------------------ entries
W("## Components")
group_order = list(GROUP_INTRO)
for k, c in C.items():
    if c["group"] not in group_order:
        group_order.append(c["group"])
for g in group_order:
    if not any(c["group"] == g for c in C.values()):
        continue
    W()
    W(f"### {g}")
    W()
    W(GROUP_INTRO.get(g, ""))
    for k, c in C.items():
        if c["group"] != g:
            continue
        CUR["comp"] = k
        W()
        W(f"#### {c['name']}")
        desc = (c.get("description") or "").strip()
        if desc and not desc.endswith((".", ")", '"')):
            desc += "."
        pgs = ", ".join(PAGE_NAME.get(p, p) for p in c["pages"][:3]) + (f" and {len(c['pages']) - 3} more" if len(c["pages"]) > 3 else "")
        W(f"{desc + ' ' if desc else ''}Read as `{k}` on the {pgs}.")
        W()
        errs = [lab for lab, v in c["states"].items() if "error" in v]
        gs = groups_of_states(c)
        if not gs:
            W("Not on the page when it was captured.")
            continue
        rows = []
        first_props = None
        notes = []
        for bl, bv, vs in gs:
            bp = props(bv)
            same = []
            vrows = []
            for kind, v in vs:
                if kind == "focus-visible" and focus_not_captured(v):
                    notes.append(f"focus could not be captured on {bl if bl != 'default' else 'the component'} ({NOT_CAPTURED})")
                    continue
                if kind == "hover" and v.get("hovered") is False:
                    notes.append(f"the pointer did not reach {bl if bl != 'default' else 'the component'} in the snapshot")
                    continue
                d = diff(props(v), bp)
                if not d:
                    same.append(kind)
                else:
                    if vrows and vrows[-1][1] == d:
                        vrows[-1] = (vrows[-1][0] + ", " + kind, d)
                    else:
                        vrows.append((kind, d))
            label = bl + (f" (same: {', '.join(same)})" if same else "")
            if first_props is None:
                rows.append((label, fmt(bp)))
                first_props = bp
            else:
                d0 = diff(bp, first_props)
                if not d0:
                    rows.append((label + " (same as the first row)", "same values"))
                elif len(d0) <= max(1, len(bp) // 2):
                    rows.append((label + " (as the first row, except)", fmt(d0)))
                else:
                    rows.append((label, fmt(bp)))
            for kind, d in vrows:
                rows.append((f"{bl}, {kind}" if bl != "default" else kind, fmt(d)))
        if len(rows) == 1:
            W(f"**Values ({rows[0][0].split(' (')[0]}).** {rows[0][1]}.")
            W()
        else:
            W("| State | Values (a hover, focus-visible or pressed row lists only what changes) |")
            W("|---|---|")
            for lab, val in rows:
                W(f"| {lab} | {val} |")
            W()
        for n in sorted(set(notes)):
            W(f"- Not measured: {n}.")
        if notes:
            W()
        # child layers
        st0 = gs[0][1]
        s0 = st0["style"]
        if st0.get("paint") and s0["backgroundColor"] == "rgba(0, 0, 0, 0)" and s0["boxShadow"] == "none" and s0["borderTopWidth"] == "0px" and s0["backgroundImage"] == "none":
            out = []
            for p in st0["paint"][:3]:
                bits = [p["node"].split(".")[0] if "::" not in p["node"] else p["node"].split(".")[0], p["size"].replace(".0x", "x").replace(".0", "")]
                if p.get("bg"):
                    bits.append("background " + colour(p["bg"], role='bg'))
                if p.get("border"):
                    bits.append("border " + colour(p["border"].split(" | ")[0][2:], role='border'))
                if p.get("radius"):
                    bits.append("radius " + p["radius"])
                if p.get("shadow"):
                    bits.append("shadow " + (shadow_text(p["shadow"]) or ""))
                out.append(" ".join(bits))
            W("Child layers that carry the look: " + "; ".join(out).replace("|", "/") + ".")
            W()
        extra = next((v.get("extra") for _, v, _ in gs if v.get("extra")), None)
        pl = parts_lines(extra)
        if pl:
            W("Parts:")
            W()
            for line in pl[:24]:
                W(("  - " + line[2:]) if line.startswith("  ") else f"- {line}")
            W()
        rules = next((v.get("rules") for _, v, _ in gs if v.get("rules")), None)
        if rules:
            W("Authored state rules (from the page's CSS): " + "; ".join(f"`{colour(r, tokens=False)[:150]}`" for r in rules[:3]) + ".")
            W()
        # crops: a state whose focus could not be captured shows the element at rest, so it is not linked
        seen = []
        for lab, v in c["states"].items():
            cp = v.get("crop")
            if cp and cp not in seen and not focus_not_captured(v) and Path(cp).exists():
                seen.append(cp)
        W(" ".join(f"![{c['name']} {Path(cp).stem[len(k) + 1:]}]({cp})" for cp in seen) if seen else "No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.")
        if errs:
            W()
            W(f"Not found on the page: {', '.join(errs)}.")

# ------------------------------------------------ icons
W()
W("## Icons")
W()
W(f"{len(icons)} SVGs: {sum(1 for r in icons if not r[0].startswith('graph-'))} lifted from the snapshots and {sum(1 for r in icons if r[0].startswith('graph-'))} copied as path strings from the graph engine's `graphIconPathMap` (the `graph-*` files, 24 x 24, drawn on the canvas with Path2D). They are in [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. The big Lottie rabbit and the illustration art are not included. The SVGs are ResearchRabbit's, kept for reference only.")
W()
W("| Icon | Rendered sizes | View box | Style | Seen on | Place |")
W("|---|---|---|---|---|---|")
for r in icons:
    f, name, h, sizes, vb, style, seen, place, label = (r + [""] * 9)[:9]
    pages = [x for x in seen.split("; ") if x]
    seen_txt = f"{len(pages)} pages" if len(pages) > 4 else "; ".join(pages)
    W(f"| ![{name}](icons/{f}) [{name}](icons/{f}) | {sizes} | {vb} | {style} | {seen_txt} | {place.split('; ')[0]} |")
W()

# ------------------------------------------------ gaps
CUR["comp"] = None
W("## Gaps")
W()
W("### Graph")
W()
W("- **Canvas states are bitmaps.** The graph is drawn on a canvas, and each snapshot holds an image of it. Node fills, rings, edge colours, label placement and the hover title box have no computed style; read them from [raw/graph-code-notes.md](raw/graph-code-notes.md) and measure them off the crops. A node's hit area and the camera are not in the snapshots at all.")
W("- **Drag and box select are only partly captured.** The library snapshots show one state after dragging a node (Positions moved) and the Reset menu. There is no mid-drag frame, no box-select rectangle, no multi-select state and no resize drag.")
W("- **Pan and zoom are one before and after.** Zoomed in is a single snapshot; the zoom steps and the transition between them are not.")
W("- **The author-ring layout** (articles on the map, authors on a ring) was not captured.")
W("- **One screenshot disagrees with a fresh render.** In [library-map-light-positions-reset-menu](screenshots/library-map-light-positions-reset-menu.png) the Positions moved pill is a salmon gradient; rendering the same snapshot file again paints it `#f5c751` (as in library-map-light-positions-moved), and the measurements here use the fresh render. If the live pill turns salmon when its menu is open, that is an animation or a state the snapshot did not keep.")
W()
W("### States")
W()
W("- **Pressed** was measured only on the 2026-10-17 pages (and the top-bar, view toggle, Auto-save and home controls read again there). No captured rule styles `:active` except the slider thumb's cursor, so every pressed state keeps the hover fill.")
W("- **Hover states of the canvas** (a node, an edge) are only in the three hover snapshots; the DOM tooltip is measured, the title box on the canvas is not.")
W("- **Components that did not take focus** (legend chips, the disabled pager and drawer Search button, text tabs that are divs) are named in each entry.")
W("- **Still missing**: an error toast (only the copy toast was raised; the bundle styles an error toast with an orange border), the Sort select list, the Collection and Reading List menus, the share dialog, list scrolling, the drawer opening and closing, and every transition between panels. Only the states captured are measured.")
W("- **Error states.** One inline error was captured: Cannot search, for an article with no citation data, with the incomplete-data chip and banner. Form validation was not reached: the only forms edit the account, and the capture did not submit or empty them. Disabled is measured on Reset Tutorials, the selection actions, the danger button and the disabled pager.")
W()
W("### Themes")
W()
W("Only the light theme was captured. The stylesheets declare dark values (the `--shadow-*-dark` variables and a few others), but no page was captured in dark, so no dark component values exist here.")
W()
W("### Pages and widths")
W()
W("- **Widths.** Pages were read at 1440 x 900, with search at 1000 x 800 and home at 800 x 900. At 640px or less the app covers every page with the Screen too small notice (captured at 390 x 844); there is no phone layout. Between 641px and desktop the frame stays and only the script breakpoints act (home cards stack below 896px, the split view gives way to the list below 1024px); 1024 to 1280 was not captured on its own.")
W("- **Not captured:** sign-in and first-run onboarding (the account is not new, and Reset Tutorials is disabled), billing and plans (paid), the share dialog, the import (BibTeX, Zotero) flows, the authors view, the Reading List with content, and the PDF reader.")
W()
W("### Screenshots and crops")
W()
W("- Article cards show public papers; the workspace name is redacted. The graph bitmap in each crop is the app's own, so two states of the same search can differ in which nodes are labelled.")
W("- Crops and screenshots are 256-colour PNGs; read exact colours from the tables above or from [raw/css-vars.json](raw/css-vars.json), not from the images.")
W("- Images from the app's own `/assets/` (the home page's illustration and guide thumbnails) are allowed through while measuring so the crops show them; no other request is let through.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", len(crop_files), "crops,", len(icons), "icons")
