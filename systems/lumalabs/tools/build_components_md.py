#!/usr/bin/env python3
"""Build components.md for the Luma AI design reference.

Reads raw/components-computed.json (every component and state, measured), raw/layout.json,
tokens.json, screenshots/ and icons/INDEX.tsv, and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the palette token whose
value matches, the font family is named once per value, and a state row shows only what differs
from the first state. Adapted from the Coursera kit's builder, which read markdown; this one reads
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
LAYOUT = json.load(open("raw/layout.json")) if Path("raw/layout.json").exists() else {}
T = json.load(open("tokens.json"))

# Components whose computed values come from another element (2026-11 audit, recapture needed). A
# state whose S() target was a stand-in carries the real element's reading in extra.card (measure.mjs
# writes it for price-card since the audit); when it is there, it replaces the stand-in's reading.
WRONG_ELEMENT = {
    "price-card": "The computed values in the raw reading are the page `body`'s, not the plan card's: the capture's target was `body`, and only the crop was taken from the Plus card. They are left out here. Recapture needed (the pk-k recapture tracking issue, 2026-11 audit).",
}
for _k, _c in C.items():
    for _st, _v in (_c.get("states") or {}).items():
        _ex = _v.get("extra") or {}
        if _ex.get("card"):
            _c["states"][_st] = {**_ex["card"], "crop": _ex.get("crop") or _v.get("crop"), "via": _v.get("via")}
            WRONG_ELEMENT.pop(_k, None)
        elif _ex.get("crop") and not _v.get("crop"):
            _v["crop"] = _ex["crop"]

# --------------------------------------------------------------------------- colours and tokens


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


BY_COLOR = {}
# Theme names first, core as the fallback: a colour a theme role shares with a core
# scale step is named by the role it plays in that theme.
for setname in ("light", "dark", "core"):
    node = T.get(setname) or {}
    for n, t in flat(node):
        if isinstance(t, dict) and t.get("$type") == "color" and isinstance(t.get("$value"), str):
            BY_COLOR.setdefault(t["$value"].lower(), f"{setname}.{n}")


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def colour(c, tokens=True):
    """rgb()/rgba()/color(srgb) -> '#hex `token`' or 'rgba(...)'."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        tok = BY_COLOR.get(v) if tokens else None
        return f"{v} `{tok}`" if tok else v

    c = re.sub(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)",
               lambda m: label(norm(*(round(float(x) * 255) for x in m.group(1, 2, 3)), m.group(4))), c)
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


def focus_not_captured(v):
    """A focus-visible reading taken where keyboard focus never landed (kbFocus returned "focus failed"),
    a skipped state, or one that did not match :focus-visible: its style is the element at rest, so it
    is left out of every table and tally (ported from the kit's builder, 2026-11 audit D4)."""
    return bool(v.get("skipped")) or v.get("via") == "focus failed" or (v.get("focus") or {}).get("matches") is False


def measured(v):
    return "style" in v and not focus_not_captured(v)


def state_rows(c):
    states = [s for s in c["states"] if measured(c["states"][s])]
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
    st = next((s for s in c["states"].values() if measured(s)), None)
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

# The pages measure.mjs reads, named as an entry says them ("Read as `x` on the home page").
PAGE_NAME = {"home": "home", "pricing": "pricing", "about": "about", "api": "API", "enterprise": "enterprise", "ray": "Ray", "news": "news"}

GROUP_INTRO = {
    "Marketing shell": "The header shared by the public pages: a wordmark, uppercase nav labels, and a Sign In pill. Sign In was measured and never followed.",
    "Home": "The dark video hero, the Try for free pill, and the prompt composer. The prompt was filled and cleared. Submit was not clicked.",
    "Pricing": "A light page with a Monthly / Yearly toggle and three plan cards. Start Now was measured and never followed.",
    "About": "A light editorial page.",
    "API": "A light page with Use the API, Explore docs, and a model tab. Use the API was never followed.",
    "Ray": "A dark cinematic page for Ray3.2.",
    "News": "A light index with category filters and article cards. Subscribe was not clicked.",
    "Enterprise": "A dark photograph hero and a sales form. The field was focused. Submit was never clicked.",
    "Phone (390 wide)": "The home at 390: Sign In and a menu button that opens the nav. Sign In was not followed.",
}

SHOTS = [
    ("home-dark", "Home. Dark video hero, Sign In, Try for free, prompt filled and cleared.", "https://lumalabs.ai/"),
    ("pricing-light", "Pricing. Monthly and Yearly, three plan cards. Start Now was not followed.", "https://lumalabs.ai/pricing"),
    ("about-light", "About. Editorial heading and company copy.", "https://lumalabs.ai/about"),
    ("api-light", "API. Use the API, Explore docs, Uni-1.1 tab.", "https://lumalabs.ai/api"),
    ("enterprise-light", "Enterprise. Dark photograph hero. The form was not submitted.", "https://lumalabs.ai/enterprise"),
    ("ray-dark", "Ray3.2. Dark cinematic page.", "https://lumalabs.ai/ray"),
    ("uni-light", "Uni-1 product page.", "https://lumalabs.ai/uni-1"),
    ("news-light", "News index. Category filters and article cards.", "https://lumalabs.ai/news"),
    ("mcp-light", "MCP page.", "https://lumalabs.ai/mcp"),
    ("careers-light", "Careers.", "https://lumalabs.ai/careers"),
    ("cases-light", "Case studies.", "https://lumalabs.ai/case-studies"),
    ("learning-light", "Learning center.", "https://lumalabs.ai/learning-center"),
    ("create-light", "AI video generator marketing page.", "https://lumalabs.ai/create/ai-video-generator"),
    ("agents-light", "Dream Machine to Luma Agents.", "https://lumalabs.ai/models/luma-dream-machine-evolved-into-luma-agents"),
    ("terms-light", "Terms of service.", "https://lumalabs.ai/legal/terms-of-service"),
    ("docs-light", "Docs hub (ReadMe). Sheets are not in the marketing tokens.", "https://docs.lumalabs.ai/docs/welcome"),
]
MOBILE = [
    ("mobile-home-dark", "Home at 390, including the opened nav. Sign In was not followed.", "https://lumalabs.ai/"),
    ("mobile-pricing-light", "Pricing at 390.", "https://lumalabs.ai/pricing"),
    ("mobile-ray-dark", "Ray at 390.", "https://lumalabs.ai/ray"),
    ("mobile-news-light", "News at 390.", "https://lumalabs.ai/news"),
]

L = []


def W(s=""):
    L.append(s)


shots = sorted(p.name for p in Path("screenshots").glob("*.png"))


def links(prefix):
    out = []
    for f in shots:
        if f.startswith(prefix + "-") and f.endswith(".png"):
            label = f[len(prefix) + 1:-4]
            out.append(f"[{label}](screenshots/{f})")
    return ", ".join(out) or "-"


n_crops = len(list(Path("components/crops").glob("*.png")))
n_states = sum(len(c["states"]) for c in C.values())
icons = []
index = Path("icons/INDEX.tsv")
if index.exists():
    icons = [r.split("\t") for r in index.read_text().strip().split("\n")[1:]]

W("# Luma AI components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from lumalabs.ai on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, submitted or purchased.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{theme}-{state}.png`. Inner pages are light. The home hero and /ray are dark. Desktop shots are 1440 x 900 at 1x. Phone shots are 390 x 844 at 2x, so the PNG is 780 wide.")
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
    ("Prompt filled", "home", "sample text typed, then deleted; Submit was not clicked", "[home-dark-prompt-filled](screenshots/home-dark-prompt-filled.png)"),
    ("Yearly interval", "pricing", "the Yearly button, a local toggle", "[pricing-light-yearly](screenshots/pricing-light-yearly.png)"),
    ("Phone nav", "home at 390", "the menu button, a local toggle; Sign In was not followed", "[mobile-home-dark-nav](screenshots/mobile-home-dark-nav.png)"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
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
    if not st or not measured(st):
        continue
    s = st["style"]
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0
    foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else None))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
none_text = f" The other {len(without)} draw none, so a keyboard user sees no change: {', '.join(without)}." if without else ""
unfocused_text = f" Focus could not be captured on {len(unfocused)} more (keyboard focus never landed on them, so their readings are left out): {', '.join(unfocused)}." if unfocused else ""
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} draw a ring: {', '.join(with_ring)}.{none_text}{unfocused_text}")
W()
W("**Pressed.** Pressed on Sign In, Try for free, Start Now and Use the API was a forced :active:hover so the link was not followed. Monthly, Yearly and the news filter are local toggles.")
W()
W("**Motion.** Transitions measured on the components, by duration.")
W()
W("| Duration | Easing | Property | Where |")
W("|---|---|---|---|")
mot = {}
for k, c in C.items():
    for st in c["states"].values():
        if not measured(st):
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
if LAYOUT:
    W("**Layout grid.** Read on each page at each width ([raw/layout.json](raw/layout.json)).")
    W()
    W("| Page | 1440 | 1920 | 1024 | 390 |")
    W("|---|---|---|---|---|")
else:
    W("**Layout grid.** Not captured: `tools/capture/layout.mjs` was not run, so there is no `raw/layout.json`.")


def grid_of(key):
    v = LAYOUT.get(key)
    if not v:
        return "-"
    g = v["grids"][0] if v["grids"] else None
    cols = re.sub(r"(\d+\.\d)\d*px", r"\1", g["cols"]).replace("px", "") if g else ""
    main = f"content x {v['main']['x']}, {v['main']['w']} wide" if v["main"]["w"] else "content full width"
    return f"{main}; grid {cols} gap {g['colGap']}" if g else main


for page in ["home", "pricing", "about", "api", "ray", "news"] if LAYOUT else []:
    row = " | ".join(grid_of(f"{page}@{w}") for w in (1440, 1920, 1024, 390))
    if row.replace("|", "").replace("-", "").strip():
        W(f"| {page} | {row} |")
W()
def covering_layer(st):
    """The first painted layer inside the component that fills or frames at least 90% of its box. The
    capture records a layer's size but not its offset, so the most it can cover is the smaller width
    times the smaller height (ported from the kit's builder, 2026-11 audit finding 18-3)."""
    rw, rh = st["rect"]["w"], st["rect"]["h"]
    for x in st.get("paint") or []:
        dims = [float(n) for n in re.findall(r"[\d.]+", x.get("size", ""))[:2]]
        if len(dims) == 2 and rw and rh and min(dims[0], rw) * min(dims[1], rh) >= 0.9 * rw * rh and (x.get("bg") or x.get("border")):
            return x
    return None


W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
# PRODUCT (adapt): the card-like components to compare in one table.
for k in ["price-card", "prompt", "nav-signin", "hero-cta", "news-card", "ent-field"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing") or k in WRONG_ELEMENT:
        continue
    st = next((s for s in c["states"].values() if measured(s)), None)
    if st is None:
        continue
    p = props(st)
    if p["background"] == "transparent" and "border" not in p and st.get("paint"):
        # The root paints nothing: its look is a painted child that covers it (at least 90% of its
        # box), named in the row. A smaller child (a CTA, a badge, a divider) is not the card, so the
        # row then keeps the root's own values.
        p0 = covering_layer(st)
        if p0:
            p = dict(p, border=colour(p0["border"].split(" | ")[0][2:]) if p0.get("border") else "-", radius=p0.get("radius") or p.get("radius", "-"),
                     background=(colour(p0["bg"]) if p0.get("bg") else "-") + f" (on `{p0['node']}`)",
                     shadow=colour(p0.get("shadow", ""), tokens=False) or "none")
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
        if k in WRONG_ELEMENT:
            W(WRONG_ELEMENT[k])
            W()
            imgs = [f"![{c['title']} {st}](components/crops/{os.path.basename(v['crop'])})" for st, v in c["states"].items() if v.get("crop")]
            W(" ".join(imgs) if imgs else "No crop was saved for this entry.")
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
W("No standalone SVG set was extracted. The wordmark and control glyphs are in the crops and screenshots. This is a layout gap.")
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
W("- **Signed-in app.** https://app.lumalabs.ai redirects to a WorkOS sign-up host. Generation, account, billing, API keys and checkout were not entered. Sign In, Try for free, Start Now and Use the API were measured and never followed.")
W("- **Enterprise form.** The field was focused. Submit was hovered and never clicked, so no sales form was sent.")
W("- **Public gallery.** There is no signed-out user gallery. Stills on /ray and the marketing pages are product demos.")
W("- **404.** A missing path rendered a Vercel invalid-slug page, not a Luma 404. It was not kept.")
W()
W("### States")
W()
W("- **Pressed** on gated links was forced with DevTools, so a script that runs on mousedown was not observed.")
W("- **Disabled, loading and error** states do not paint on the public pages.")
W("- **Pricing FAQ** was not found as a stable button. About and Ray FAQ rows were measured.")
W()
W("### Themes")
W()
W("Two resolutions of the same marketing sheets are in tokens.json. Inner pages paint html.light. The home hero and /ray paint dark media, and html.dark resolves a black page with white text. There is no theme switch. Docs (docs.lumalabs.ai) is a ReadMe hub and its tokens are not folded in.")
W()
W("### Fonts")
W()
W("- **Graphik** is the computed body and h1 family, under a Next.js local-font class name. The file is not redistributed.")
W("- **PP Editorial** is loaded on the page and was not the computed h1 family on this pass.")
W()
W("### Screenshots")
W()
W("- Generated stills and the home video are Luma's content and appear only inside screenshots and crops.")
W("- The news index is very tall. The full-page news shot was dropped. The viewport shot was kept.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- No prompt was submitted and no account was created. The pages were read signed out.")

# Every image or file this page links must exist in the package (2026-11 audit finding 18-2: rows
# copied from another product's builder linked screenshots this capture never took).
dead = sorted({t for t in re.findall(r"\]\(((?:screenshots|components|raw|icons)/[^)#\s]+)\)", "\n".join(L)) if not Path(t).exists()})
if dead:
    raise SystemExit("components.md links files that do not exist: " + ", ".join(dead))
Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops,", len(icons), "icons")
