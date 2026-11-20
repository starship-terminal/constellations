#!/usr/bin/env python3
"""Build components.md for the Refero design reference.

Reads raw/components-computed.json (every component and state, measured), raw/layout.json,
tokens.json, screenshots/ and icons/INDEX.tsv, and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the palette token whose
value matches, the font family is named once per value, and a state row shows only what differs
from the first state. Adapted from the Gauth package's builder, which reads the same JSON schema.

Deterministic: re-running it on the same inputs reproduces components.md byte for byte.
Run from anywhere: python3 tools/build_components_md.public.py
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



def focus_not_captured(v):
    """D4, as the kit's builder: a skipped state, or a focus-visible reading taken where keyboard focus
    never landed (via "focus failed") or did not match :focus-visible, is the element at rest. It is
    left out of every table and tally and listed as "focus could not be captured"."""
    return bool(v.get("skipped")) or v.get("via") == "focus failed" or (v.get("focus") or {}).get("matches") is False

def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


BY_COLOR = {}
for n, t in flat(T["core"]["palette"]):
    if t["$type"] == "color":
        BY_COLOR.setdefault(t["$value"], n)


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def srgb_chan(c):
    c = max(0.0, min(1.0, c))
    return round((12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055) * 255)


def lab_rgb(L, a, b):
    fy = (L + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    eps, kap = 216 / 24389, 24389 / 27
    def f(t):
        t3 = t ** 3
        return t3 if t3 > eps else (116 * t - 16) / kap
    X, Y, Z = 0.96422 * f(fx), f(fy), 0.82521 * f(fz)
    return [srgb_chan(v) for v in (3.1338561 * X - 1.6168667 * Y - 0.4906146 * Z,
                                 -0.9787684 * X + 1.9161415 * Y + 0.0334540 * Z,
                                 0.0719453 * X - 0.2289914 * Y + 1.4052427 * Z)]


def oklab_rgb(L, a, b):
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return [srgb_chan(x) for x in (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
                                  -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
                                  -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)]


def colour(c, tokens=True):
    """rgb()/rgba()/lab()/oklab()/color(srgb) -> '#hex `token`' or 'rgba(...)'."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        tok = BY_COLOR.get(v) if tokens else None
        return f"{v} `{tok}`" if tok else v

    c = re.sub(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)",
               lambda m: label(norm(*(round(float(x) * 255) for x in m.group(1, 2, 3)), m.group(4))), c)
    c = re.sub(r"oklab\(([-\d.e]+) ([-\d.e]+) ([-\d.e]+)(?: / ([\d.]+))?\)",
               lambda m: label(norm(*oklab_rgb(float(m.group(1)), float(m.group(2)), float(m.group(3))), m.group(4))), c)
    c = re.sub(r"(?<!ok)lab\(([-\d.e]+) ([-\d.e]+) ([-\d.e]+)(?: / ([\d.]+))?\)",
               lambda m: label(norm(*lab_rgb(float(m.group(1)), float(m.group(2)), float(m.group(3))), m.group(4))), c)
    return re.sub(r"rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)", lambda m: label(norm(*m.group(1, 2, 3), m.group(4))), c)


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
        o["padding"] = pad
    bds = []
    for d in ("Top", "Right", "Bottom", "Left"):
        if float(s[f"border{d}Width"].replace("px", "")) > 0 and s[f"border{d}Style"] != "none":
            bds.append(f"{s[f'border{d}Width']} {s[f'border{d}Style']} {colour(s[f'border{d}Color'])}")
        else:
            bds.append("none")
    if any(b != "none" for b in bds):
        o["border"] = bds[0] if len(set(bds)) == 1 else "; ".join(f"{'TRBL'[i]}: {b}" for i, b in enumerate(bds) if b != "none")
    rad = sides(s["borderTopLeftRadius"], s["borderTopRightRadius"], s["borderBottomRightRadius"], s["borderBottomLeftRadius"])
    if rad != "0px":
        o["radius"] = rad
    o["background"] = colour(s["backgroundColor"])
    if s["backgroundImage"] != "none":
        img = re.sub(r'url\("data:[^)]*\)', "an image (data URI)", s["backgroundImage"])
        o["image"] = colour(img)[:200]
    if s["boxShadow"] != "none":
        sh = colour(s["boxShadow"], tokens=False)
        layers = [x.strip() for x in re.split(r",(?![^(]*\))", sh)]
        layers = [x for x in layers if not x.startswith("transparent")]
        if layers:
            o["shadow"] = ", ".join(layers)
    if s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0:
        o["outline"] = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}"
    t = v.get("textStyle")
    if t:
        o["text"] = f"{font(t['fontSize'], t['lineHeight'], t['fontWeight'], t['fontFamily'])}, {colour(t['color'])}"
    else:
        o["text"] = f"{font(s['fontSize'], s['lineHeight'], s['fontWeight'], s['fontFamily'])}, {colour(s['color'])}"
    if s["transitionDuration"] not in ("0s", ""):
        props_ = [x.strip() for x in s["transitionProperty"].split(",")]
        durs = [x.strip() for x in s["transitionDuration"].split(",")]
        tf = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", s["transitionTimingFunction"])
        parts = []
        for i, p in enumerate(props_):
            d = durs[i % len(durs)]
            if d == "0s":
                continue
            parts.append(f"{p} {d} {tf[i % len(tf)] if tf else ''}".strip())
        if parts:
            o["transition"] = ", ".join(parts)
    if s["transform"] not in ("none", "matrix(1, 0, 0, 1, 0, 0)"):
        m = re.fullmatch(r"matrix\(([\d.]+), 0, 0, ([\d.]+), (-?[\d.]+), (-?[\d.]+)\)", s["transform"])
        if m and m.group(1) == m.group(2) and m.group(3) == m.group(4) == "0":
            o["transform"] = f"scale({m.group(1)})"
        elif m and m.group(1) == m.group(2) == "1":
            o["transform"] = f"translate({m.group(3)}px, {m.group(4)}px)"
        else:
            o["transform"] = s["transform"]
    if s["opacity"] != "1":
        o["opacity"] = s["opacity"]
    if v.get("icon") and v["icon"]["w"] > 0 and v["icon"]["w"] < 120:
        o["icon"] = f"{num(v['icon']['w'])} x {num(v['icon']['h'])}, {colour(v['icon']['color'])}"
    if v.get("placeholder"):
        o["placeholder"] = colour(v["placeholder"]["color"])
    return o


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "outline", "text", "transition", "transform", "opacity", "icon", "placeholder"]


def state_rows(c):
    states = [s for s in c["states"] if "style" in c["states"][s] and not focus_not_captured(c["states"][s])]
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
            bits.append("background " + colour(p["bg"]))
        if p.get("bgImage"):
            bits.append("image " + colour(p["bgImage"])[:90])
        if p.get("border"):
            bits.append("border " + colour(p["border"].split(" | ")[0][2:]))
        if p.get("radius"):
            bits.append("radius " + p["radius"])
        if p.get("shadow"):
            bits.append("shadow " + colour(p["shadow"]))
        out.append(" ".join(bits))
    return "; ".join(out).replace("|", "/")


# --------------------------------------------------------------------------- page and group text

PAGE_NAME = {"home": "refero.design home", "search": "refero.design search", "apps": "refero.design iOS apps search",
             "pricing": "refero.design pricing", "mcp": "refero.design MCP", "styles": "styles.refero.design index",
             "entity": "styles.refero.design style page"}

GROUP_INTRO = {
    "Shell and navigation": "refero.design's frame: a fixed 270px left rail (logo, New research, Web apps / iOS apps / Styles / Beta, then Pricing / Connect MCP / Figma Plugin / Log In Sign Up at its foot) and the content pane; styles.refero.design instead uses a translucent 81px top bar. On a phone the rail collapses to a top bar.",
    "Home and research": "The home page of refero.design: a cycling serif headline over the centred research card (prompt field, Search by Image, mode chips), the coach box under it, then the Page Types / Flows / UX Patterns / UI Elements / Sites sections of screenshot cards.",
    "Search and galleries": "The web-apps search and the iOS-apps search: the mode chips and Screens/Flows toggle, a wider search field, then a grid of screenshot tiles (each a page thumbnail over a favicon and name) ending at a paywall panel.",
    "Pricing": "refero.design's pricing page: the serif title, plan cards, the student discount card and the enterprise band.",
    "MCP page": "The MCP marketing page (Give your AI agent design taste): install instructions, the Refero Skill section and pricing, plus the fixed promo card that also floats on every page.",
    "Promos and overlays": "The two dismissable layers the home page opens with: the fixed MCP promo card at lower left and the coach box pinned under the research field. Both were closed for every other capture.",
    "Styles gallery": "styles.refero.design's index: the kalice serif headline (Your favorite sites, in DESIGN.md), the search pill, filter chips, and the card grid whose tiles play a scroll-through video on hover.",
    "Style entity page": "A style's page on styles.refero.design: media frame (poster with the scroll video fading in over it), circular favicon and kalice title, the DESIGN.md / Tailwind v4 / CSS Variables / Design Tokens documentation tabs, and the similar-styles grid.",
    "Mobile (390 wide)": "The same pages as a phone draws them, at 390 x 844 with an iPhone user agent: the rail becomes a top bar on refero.design; the styles index keeps its top bar and one-column cards.",
}

SHOTS = [
    ("home", "refero.design home. Serif headline, centred research card, coach box, the Page Types / Flows / UX Patterns sections; the two promos closed, the MCP card open, and the field focused.", "https://refero.design/"),
    ("search", "refero.design web-apps search. Mode chips, Screens/Flows toggle, the wide search field and screenshot tiles down to the paywall panel.", "https://refero.design/search"),
    ("apps", "refero.design iOS-apps search. The same chrome with iPhone screenshot tiles.", "https://refero.design/apps/search"),
    ("pricing", "refero.design pricing. Serif title, plan cards, student discount, enterprise band.", "https://refero.design/pricing"),
    ("mcp", "refero.design MCP. Give your AI agent design taste; install steps, Refero Skill, pricing.", "https://refero.design/mcp"),
    ("styles", "styles.refero.design index. Kalice headline, search pill, chips, the video-tile card grid; one card's hover video.", "https://styles.refero.design/"),
    ("styles-entity", "A style page. Media frame with the scroll video, favicon and kalice title, doc tabs and the similar-styles grid.", "https://styles.refero.design/style/a73148b9-449b-42cd-9f38-86ef694f500e"),
]
MOBILE = [
    ("mobile-home", "refero.design home at 390: top bar, the cycling headline, the research card, the MCP promo.", "https://refero.design/"),
    ("mobile-search", "refero.design web-apps search at 390.", "https://refero.design/search"),
    ("mobile-styles", "styles.refero.design index at 390: the same bar and hero over a one-column card list.", "https://styles.refero.design/"),
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

W("# Refero components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real products, the icon index and the Gaps. Captured from refero.design and styles.refero.design on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running pages. Nothing was signed into, created, sent or uploaded.")
W()
W("The two hosts are one product family with two surfaces: **refero.design** is the design-research app (left rail, research box, screenshot galleries, pricing and MCP marketing); **styles.refero.design** is the public styles gallery (top bar, the video-tile card index, a documentation page per style). They share one token system: the same `--gray-solid`/`--gray-alpha` scales, `--fill-*`/`--stroke-*`/`--text-*`/`--status-*` names and the same inverted dark values, each host adding its own display serif (Title on refero.design, kalice on styles) and UI sans (Base-Variable, neueMontreal).")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [raw/layout.json](raw/layout.json).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Base-Variable 14/20 500, rgba(3, 14, 49, 0.54)`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). Both hosts honour prefers-color-scheme: the dark values are in the token file's `dark` set rather than a second screenshot pass.")
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
    ("MCP promo card", "every refero.design page, on load", "at rest; then dismissed with its own Close button for the other captures", "[home-light-promo](screenshots/home-light-promo.png), [mcp-card](#mcp-card)"),
    ("Coach box (\"Tell me what you're designing\")", "refero.design home, on load", "at rest; dismissed with its X (a cursor:pointer svg, not a button)", "[coach-box](#coach-box)"),
    ("Search-by-image affordance", "the research box, every refero.design page", "at rest inside the field", "inside [research-box](#research-box)"),
    ("Card hover video", "styles.refero.design index", "a 3-second real hover so the card's scroll-preview mp4 buffered and faded in over the poster", "[styles-light-card-hover](screenshots/styles-light-card-hover.png), [styles-card-video](#styles-card-video)"),
    ("Entity scroll video", "a style page", "the page loads the mp4 over the poster frame on its own", "[styles-entity-light-default](screenshots/styles-entity-light-default.png), [entity-frame](#entity-frame)"),
    ("Paywall panel", "the end of each search grid", "the last tile scrolls into a Sign up to see more panel", "in [search-light-full](screenshots/search-light-full.png)"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ checklist coverage
def states_of(*names):
    """The states captured across these entries. A failed or skipped focus is the element at rest, so
    it is not a captured state here either (D4, as in the entry tables)."""
    seen = []
    for n in names:
        for s, v in C.get(n, {}).get("states", {}).items():
            if focus_not_captured(v):
                continue
            if s not in seen:
                seen.append(s)
    return ", ".join(seen) if seen else "-"

def entry_links(*names):
    out = []
    for n in names:
        if n not in C:
            continue
        t = C[n].get("title", n)
        anchor = re.sub(r"[^a-z0-9 -]", "", t.lower()).replace(" ", "-")
        out.append(f"[{t}](#{anchor})")
    return ", ".join(out)

CHECKLIST = [
    ("Button", ("plan-cta", "mcp-card-cta", "entity-copy"), None),
    ("Icon button", ("mcp-card-close", "coach-close"), None),
    ("Link", (), "the rail's nav links and the promo's Explore MCP were measured inside their parents, not as standalone entries"),
    ("Text field", ("research-box", "research-input", "styles-search", "search-box"), None),
    ("Text area", ("research-box-state", "m-research-box"), None),
    ("Select", (), "no public page offers one"),
    ("Checkbox", (), "no public form has one"),
    ("Radio", ("research-chip", "styles-chip"), None),
    ("Switch", (), "the search page's Screens/Flows toggle was not measured as an entry"),
    ("Tabs", ("entity-tab", "entity-tab-active"), None),
    ("Menu", (), "no menu is reachable signed out"),
    ("Tooltip", (), "none appeared on hover or focus"),
    ("Dialog", (), "the only dismissible overlay is the MCP promo card, a fixed corner card rather than a modal"),
    ("Toast", (), "no toast appeared after any action the capture took signed out"),
    ("Card", ("result-card", "search-tile", "ios-tile", "plan-card", "discount-card", "mcp-card", "styles-card", "entity-similar", "m-styles-card"), None),
    ("List row", (), "the rail's nav items were not measured as rows"),
    ("Table", (), "pricing lays plans out as cards, not a table"),
    ("Avatar", ("styles-card-favicon", "entity-favicon"), None),
    ("Badge", ("discount-card",), None),
]
present = sum(1 for _, names, _ in CHECKLIST if names)
W("## Checklist coverage")
W()
W(f"The 19 components of the library's checklist ([docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md)), each with the entries below that show it and the states captured across them. {present} of 19 are captured; the rest do not exist on the public pages.")
W()
W("| Component | Entries | States captured |")
W("|---|---|---|")
for comp, names, note in CHECKLIST:
    cells = entry_links(*names) if names else f"not captured: {note}"
    W(f"| {comp} | {cells} | {states_of(*names)} |")
W()

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement files.")
W()
foc, unfocused = [], []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if st and focus_not_captured(st):
        unfocused.append(f"`{k}`")
        continue
    if not st or "style" not in st:
        continue
    s = st["style"]
    base = c["states"].get("default", {}).get("style", s)
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0 and (s["outlineStyle"] != base["outlineStyle"] or s["outlineWidth"] != base["outlineWidth"])
    ring_shadow = s["boxShadow"] != base["boxShadow"] and "0px 0px" in s["boxShadow"]
    foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else ("ring shadow " + colour(s["boxShadow"], tokens=False) if ring_shadow else None)))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} show a change: {', '.join(with_ring)}. The other {len(without)} draw nothing new (the research input and the result card among them): {', '.join(without)}.{f" Focus could not be captured on {len(unfocused)} more (keyboard focus never landed on them, so their readings are left out): {', '.join(unfocused)}." if unfocused else ""} The two hosts focus differently: on refero.design the browser's own `auto` outline (1px #005fcc) appears on CTAs and links, plus the research chips' custom `rgba(1, 17, 88, 0.24)` ring shadow; on styles.refero.design the controls draw their own 2-3px ring shadow in `rgba(111, 113, 121, 0.4-0.5)` (the --ring colour at half alpha).")
W()
W("**Pressed.** Pressed was forced with DevTools, so it is the :active styles only: the research chips and entity tabs go from muted to ink on press exactly as on hover, the MCP card's Close fills #ddddea, and the promo card's plain link takes the browser's default :active red (an artefact of the forced state, not a design colour).")
W()
W("**Motion.** Transitions measured on the components, by duration. The signature motion is not a transition at all: a styles card's scroll-preview mp4 fades in over the poster after a hover, and the entity page's video does the same on load (opacity 0.5s).")
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


def dur_ms(d):
    return float(d[:-1]) * 1000 if d.endswith("s") and not d.endswith("ms") else float(d[:-2])


for (d, e), (ps, ks) in sorted(mot.items(), key=lambda kv: (dur_ms(kv[0][0]), kv[0][1])):
    W(f"| {d} | `{e}` | {', '.join(sorted(ps))} | {', '.join(sorted(ks)[:8])}{' and more' if len(ks) > 8 else ''} |")
W()
W("**Layout.** Read on each page ([raw/layout.json](raw/layout.json)).")
W()
W("| Page | Frame | Content column | Grids | Fixed |")
W("|---|---|---|---|---|")


def layrow(key):
    v = LAYOUT.get(key)
    if not v:
        return f"| {key} | - | - | - | - |"
    frame = []
    if v.get("sidebar"):
        frame.append(f"sidebar {v['sidebar']['w']}px")
    if v.get("header"):
        frame.append(f"top bar {v['header']['h']}px, {v['header'].get('pos','')}, {v['header'].get('backdrop','')}")
    mw = max(v.get("maxWidths") or [{"w": 0, "max": "-"}], key=lambda m: m["w"] if m["w"] < v["vw"] * 0.99 else 0)
    col = f"max-width {mw['max']}" if mw.get("max") not in (None, "-") else "full width"
    gs = v.get("grids") or []
    g = f"{len(gs)} grids" if gs else "-"
    if gs:
        g += " (" + "; ".join(f"{len(gd['cols'].split())} col gap {gd['colGap']}" for gd in gs[:2]) + ")"
    fx = ", ".join(f"{(f.get('text','') or f.get('el','?')).split(chr(10))[0][:40].replace('|','/')} ({f.get('pos','fixed')})" for f in (v.get("fixed") or [])[:3]) or "-"
    return f"| {key} | {'; '.join(frame) or '-'} | {col} | {g} | {fx} |"


for key in LAYOUT:
    W(layrow(key))
W()
W("**Card shapes.** Default-state values; the entries hold the states. The two galleries draw different cards: refero.design's tiles are rounded rectangles inside padded cards, styles.refero.design's are the signature 32px-radius padded tile with a favicon and name under it.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
for k in ["research-box", "result-card", "search-tile", "ios-tile", "plan-card", "discount-card", "mcp-card", "coach-box", "styles-card", "entity-similar", "m-styles-card"]:
    c = C.get(k)
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if "style" in s), None)
    if st is None:
        continue
    p = props(st)
    if ("radius" not in p or p["background"] == "transparent") and st.get("paint"):
        p0 = next((x for x in st["paint"] if x.get("bg") and x.get("radius")), st["paint"][0])
        p = dict(p, border=colour(p0["border"].split(" | ")[0][2:]) if p0.get("border") else "-", radius=p0.get("radius", "-"), background=colour(p0.get("bg", "")) or "-", shadow=colour(p0.get("shadow", ""), tokens=False) or "none")
    W(f"| [{c['title']}](#{re.sub(r'[^a-z0-9 -]', '', c['title'].lower()).replace(' ', '-')}) | {p['size']} | {p.get('border', '-')} | {p.get('radius', '-')} | {p.get('background', '-')} | {p.get('shadow', 'none')} | {p.get('padding', '0')} |")
W()

# ------------------------------------------------ entries
W("## Components")
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
        imgs = [f"![{c['title']} {st}](components/crops/{os.path.basename(c['states'][st]['crop'])})" for st in states if c["states"][st].get("crop")]
        W(" ".join(imgs) if imgs else "No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.")

# ------------------------------------------------ icons
W()
W("## Icons")
W()
W(f"{len(icons)} SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Product artwork, favicons, brand marks and site screenshots were left out; these are the interface icons. The SVGs are Refero's property, kept for reference only.")
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
W("- **Signed-in pages.** Nothing behind Log In / Sign Up was captured: saved research, the account page, and whatever the New research button's submit does past its empty state. The kit never signs in.")
W("- **Paywalled results.** Both search pages end their grids at a Sign-up-to-see-more panel; the full libraries (web apps, iOS apps, flows and the site pages a card links to) were not entered.")
W("- **The Figma plugin and the checkout.** The Figma Plugin link and the plan CTAs lead off the measured scope; no purchase was made and no card field was filled.")
W("- **New research as a flow.** The mode chips were measured, but submitting a prompt creates a research job, so the result page and its streaming UI are missing.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing; the promo card's plain link paints the browser's default :active red under the forced state.")
W("- **The home h1 cycles** its second line through colourways (the --reveal-* gradient vars on the shell, driven by the same-name keyframe animation); a capture pins whichever pass was running.")
W("- **The Page Types cards rotate** their product links on a timer and are rebuilt by the page's hydration; the measured card is whichever the timer had dealt.")
W("- **Disabled and loading** were not seen on any public control, and **error** exists only as declared status colours.")
W()
W("### Themes")
W()
W("Both hosts ship a light and a dark theme. refero.design applies `body#dark-theme` manually or `body:not(#light-theme)` under prefers-color-scheme: dark; styles.refero.design holds its dark values on `:root` under the same media query. Every page painted dark under prefers-color-scheme: dark (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)). The token file carries a `dark` set built from those declarations; the screenshots stayed in light, so dark component appearance is unverified beyond the variable values.")
W()
W("### Fonts")
W()
W("- **Base-Variable** (refero.design UI, 200-800) and **Title** (its serif display) are self-hosted faces; neither is on a public font CDN.")
W("- **neueMontreal** (styles.refero.design UI, drawn at weight 530), **kalice** (its serif display) and **JetBrains Mono** (the documentation panes) are served by the Next app; kalice and neueMontreal are commercial faces.")
W("- The README's guidance on these fonts applies: substitute close free faces (Instrument Serif for the display serifs, Inter/Public Sans for the UI, JetBrains Mono is freely available) when reproducing the style.")
W()
W("### Screenshots")
W()
W("- Site thumbnails, favicons, app screenshots and the scroll-preview videos inside cards are Refero's content and appear only inside screenshots and crops.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- The text a style's documentation tabs render was not transcribed into the package; the tab controls and the pane around them were measured.")
W("- No personal data was captured: the pages were read signed out.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops,", len(icons), "icons")
