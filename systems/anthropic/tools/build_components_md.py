#!/usr/bin/env python3
"""Build components.md for the Anthropic design reference.

Reads raw/components-computed.json (every component and state, measured), raw/layout.json,
tokens.json and screenshots/, and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the palette token whose
value matches, the font family is named once per value, and a state row shows only what differs
from the first state. Adapted from the Refero package's builder, which reads the same JSON schema.

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


BY_COLOR = {}
for n, t in flat(T["core"]["color"]):
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


def focus_not_captured(v):
    """A state whose reading is not what its name says: a skipped one, or a focus-visible reading
    taken where keyboard focus never landed (kbFocus returned "focus failed") or where the element
    took focus but did not match :focus-visible. Its style is the element at rest, so it is left out
    of every table and tally and listed as "focus could not be captured"."""
    return bool(v.get("skipped")) or v.get("via") == "focus failed" or (v.get("focus") or {}).get("matches") is False


def measured(v):
    return "style" in v and not focus_not_captured(v)


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

PAGE_NAME = {"home": "www.anthropic.com home", "news": "www.anthropic.com/news",
             "research": "www.anthropic.com/research", "engineering": "www.anthropic.com/engineering",
             "product": "claude.com/product/overview", "platform-api": "claude.com/platform/api",
             "pricing": "claude.com/pricing", "contact-sales": "claude.com/contact-sales",
             "docs-home": "docs.claude.com home", "docs-start": "docs.claude.com get-started",
             "docs-api": "docs.claude.com API reference"}

GROUP_INTRO = {
    "Shell and navigation": "The chrome shared by the marketing and product pages: an 84px bar of ivory pills (a wordmark, section links, a Search pill and the Try Claude CTA) over the ivory ground, and the ink footer whose prompt bar takes a clay Send. On a phone the pills collapse to a menu button and a full-screen ink sheet.",
    "Home": "www.anthropic.com's home: the serif hero ('AI research and products that put safety at the frontier.') with an ink CTA, the big #f5f4ed feature card, and the news card list.",
    "Cards and indexes": "The card grids on the index pages: news and engineering cards on ivory, and the research cards that sit on ink-tinted media.",
    "Product pages": "claude.com/product/overview and /platform/api: serif display titles, ink CTAs and the muted media cards (radius 19, gray-150).",
    "Pricing": "claude.com/pricing: the serif title, the segmented plan tabs (gray-150 track, white selected), white plan cards at radius 24, the batch-processing switch and the FAQ list.",
    "Contact sales form": "claude.com/contact-sales: the 755px sales form - text fields, a text area, a select and a radio row measured in default, focused and filled states. Nothing was submitted.",
    "Docs (platform.claude.com)": "docs.claude.com: a cooler cds-* system - the 56px topbar, 264px sidebar with an ink-tint active pill, serif titles, 13/19 anthropicMono code, and the #184f95 method badge.",
    "Overlays": "The overlays a fresh profile meets: the nav dropdown (opened by a real hover) and the docs search dialog (opened from its field, measured open, nothing typed).",
    "Mobile (390 wide)": "The same pages as a phone draws them, at 390 x 844 with an iPhone user agent: the nav collapses to a menu button and a full-screen ink sheet.",
}

SHOTS = [
    ("home", "www.anthropic.com home. Serif hero, feature card, news cards; also the nav dropdown opened by hover.", "https://www.anthropic.com/"),
    ("news", "www.anthropic.com/news. The announcements index.", "https://www.anthropic.com/news"),
    ("research", "www.anthropic.com/research. The research index on dark media.", "https://www.anthropic.com/research"),
    ("engineering", "www.anthropic.com/engineering. The engineering index.", "https://www.anthropic.com/engineering"),
    ("product", "claude.com/product/overview. The Claude product page.", "https://claude.com/product/overview"),
    ("platform-api", "claude.com/platform/api. The API platform page.", "https://claude.com/platform/api"),
    ("pricing", "claude.com/pricing. Plan tabs, plan cards, batch switch, FAQ; the Developer tab shown selected.", "https://claude.com/pricing"),
    ("contact-sales", "claude.com/contact-sales. The sales form, never submitted.", "https://claude.com/contact-sales"),
    ("docs-home", "docs.claude.com/en/home. The docs home; also the search dialog.", "https://docs.claude.com/en/home"),
    ("docs-start", "docs.claude.com/en/docs/get-started. Prose, code block, inline code, copy-page button.", "https://docs.claude.com/en/docs/get-started"),
    ("docs-api", "docs.claude.com/en/api/messages. The API reference with method badges.", "https://docs.claude.com/en/api/messages"),
]
MOBILE = [
    ("mobile-home", "www.anthropic.com home at 390: menu button, hero, the ink nav sheet.", "https://www.anthropic.com/"),
    ("mobile-pricing", "claude.com/pricing at 390.", "https://claude.com/pricing"),
    ("mobile-docs-home", "docs.claude.com/en/home at 390.", "https://docs.claude.com/en/home"),
]

L = []


def W(s=""):
    L.append(s)


shots = sorted(p.name for p in Path("screenshots").glob("*.png"))


def links(prefix):
    out = []
    for f in shots:
        m = re.fullmatch(re.escape(prefix) + r"-(?:light|dark)-(.+)\.png", f)
        if m:
            out.append(f"[{m.group(1)}](screenshots/{f})")
    return ", ".join(out)


n_crops = len(list(Path("components/crops").glob("*.png")))
n_states = sum(len(c["states"]) for c in C.values())

W("# Anthropic components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from www.anthropic.com, claude.com and docs.claude.com on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running pages. Nothing was signed into, submitted, bought or sent; no consent dialog was answered and no form was submitted.")
W()
W("The public surface is three hosts sharing one type system: **www.anthropic.com** (the marketing site: ivory #faf9f5 ground, ink #141413, anthropicSerif headlines, pill nav chrome, a --color-* palette on :root), **claude.com** (the product pages: the same build plus a `--theme-*` semantic set and fluid clamp() type), and **docs.claude.com** (the Claude Platform docs: the cds-* Tailwind system on a cooler gray ramp, anthropicSans/anthropicMono, a #184f95 accent). Only the docs ship a dark theme.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [raw/layout.json](raw/layout.json).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/18 500, #000`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (the docs dark pass is `{page}-dark-{state}.png`). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).")
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
    ("Nav dropdown", "the marketing nav, on hover over Product", "a real hover opened the dropdown; captured open, never clicked through", "[home-light-nav-dropdown](screenshots/home-light-nav-dropdown.png), [nav-dropdown](#nav-dropdown)"),
    ("Docs search dialog", "docs.claude.com", "opened from the header's search field; measured open, nothing typed", "[docs-home-light-search-dialog](screenshots/docs-home-light-search-dialog.png), [docs-search-dialog](#search-dialog)"),
    ("Pricing plan tabs", "claude.com/pricing", "the Developer tab was clicked once for the selected state (local UI)", "[pricing-light-plan-tab](screenshots/pricing-light-plan-tab.png), [plan-tab-active](#plan-tab-switched)"),
    ("Mobile nav sheet", "www.anthropic.com at 390", "the menu button opened the full-screen ink sheet", "[m-nav-sheet](#mobile-nav-sheet)"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ checklist coverage
def states_of(*names):
    seen = []
    for n in names:
        for s in C.get(n, {}).get("states", {}):
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
    ("Button", ("hero-cta", "nav-cta", "product-cta", "api-cta", "plan-cta", "submit-button", "docs-copy-page"), None),
    ("Icon button", ("nav-search", "m-nav-menu-btn", "docs-search-field"), None),
    ("Link", ("footer-link", "news-card-link", "research-card-link", "engineering-card-link", "docs-nav-link"), None),
    ("Text field", ("text-field", "text-field-box", "docs-search-input"), None),
    ("Text area", ("text-area",), None),
    ("Select", ("select-field",), None),
    ("Checkbox", (), "no public form has one; --theme-checkbox-* tokens exist on claude.com"),
    ("Radio", ("topic-radio", "topic-radio-row"), None),
    ("Switch", ("batch-toggle",), None),
    ("Tabs", ("plan-tab", "plan-tab-active", "docs-tab"), None),
    ("Menu", ("nav-dropdown", "m-nav-sheet"), None),
    ("Tooltip", (), "none appeared on hover or focus"),
    ("Dialog", ("docs-search-dialog",), None),
    ("Toast", (), "no toast appeared after any action the capture took signed out"),
    ("Card", ("feature-card", "news-card", "research-card", "engineering-card", "product-card", "plan-card"), None),
    ("List row", ("faq-item", "news-card"), None),
    ("Table", (), "pricing lays plans out as cards, not a table"),
    ("Avatar", (), "no avatars on the public surface"),
    ("Badge", ("docs-method-badge",), None),
]
present = sum(1 for _, names, _ in CHECKLIST if names)
W("## Checklist coverage")
W()
W(f"The 19 components of the library's checklist ([docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md)), each with the entries below that show it and the states captured across them. {present} of 19 are captured; the rest do not exist on the public marketing surface.")
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
    if not st or not measured(st):
        continue
    s = st["style"]
    base = c["states"].get("default", {}).get("style", s)
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0 and (s["outlineStyle"] != base["outlineStyle"] or s["outlineWidth"] != base["outlineWidth"])
    ring_shadow = s["boxShadow"] != base["boxShadow"] and "0px 0px" in s["boxShadow"]
    foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else ("ring shadow " + colour(s["boxShadow"], tokens=False) if ring_shadow else None)))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} show a change: {', '.join(with_ring)}. The other {len(without)} draw nothing new - the marketing pills draw a deliberate 2px #154c92 periwinkle ring offset 4px, the product pages a 2px #c46849 clay-dark ring offset 2-4px, the docs outline in #2a78d6, and text links take the browser's ring: {', '.join(without)}.{f" Focus could not be captured on {len(unfocused)} more (keyboard focus never landed on them, so their readings are left out): {', '.join(unfocused)}." if unfocused else ""}")
W()
W("**Pressed.** Pressed was forced with DevTools, so it is the :active styles only: the nav pills swap to their #e8e6dc pressed fill under :active, while the ink CTAs and docs controls keep their resting paint. The submit button and every sign-in link were never pressed for real.")
W()
W("**Motion.** Transitions measured on the components, by duration. The everyday hover rides 0.2s ease-out on colour and fill; the pills press in 0.15s; menus and overlays take 0.25-0.5s on the site's quart/expo curves.")
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
def covering_layer(st):
    """The first painted layer inside the component that fills or frames at least 90% of its box. The
    capture records a layer's size but not its offset, so the most it can cover is the smaller width
    times the smaller height: a wide, short child (600x100 in a 300x200 card) covers at most half the
    card and is not its look, though its own area is larger (the kit's rule)."""
    rw, rh = st["rect"]["w"], st["rect"]["h"]
    for x in st.get("paint") or []:
        dims = [float(n) for n in re.findall(r"[\d.]+", x.get("size", ""))[:2]]
        if len(dims) == 2 and rw and rh and min(dims[0], rw) * min(dims[1], rh) >= 0.9 * rw * rh and (x.get("bg") or x.get("border")):
            return x
    return None


W("**Card shapes.** Default-state values; the entries hold the states. The signature card is the 24px-radius white plan card on ivory; media cards run 19px on gray-150 and the docs dialog is a 12px white panel with an ink ring.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
for k in ["feature-card", "news-card", "product-card", "plan-card", "docs-search-dialog", "m-nav-sheet"]:
    c = C.get(k)
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if measured(s)), None)
    if st is None:
        continue
    p = props(st)
    if p["background"] == "transparent" and "border" not in p and st.get("paint"):
        # The root paints nothing (a radius alone paints nothing): its look is a painted child that
        # covers it (at least 90% of its box), named in the row. A smaller child (a CTA's ::before, a
        # badge, a divider) is not the card, so the row then keeps the root's own values.
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

# ------------------------------------------------ gaps
W()
W("## Gaps")
W()
W("### Pages")
W()
W("- **The products.** claude.ai and console.anthropic.com are the signed-in surfaces: nothing behind Try Claude, Log in or Console was captured, and the chat UI, API keys, billing and Workbench are all missing. The kit never signs in or registers.")
W("- **Checkout and account.** The plan CTAs and the contact-sales form lead to flows that were never submitted; no purchase was made and no field was filled for real.")
W("- **Article-depth pages.** The index pages were captured; news posts, research papers and engineering entries were not opened.")
W("- **Privacy choices dialog.** The footer's 'Privacy choices' opens a consent settings dialog; it was never opened because answering it is a submission.")
W()
W("### Themes")
W()
W("Only the docs ship a dark theme: `data-mode=\"system\"` on html flips it under prefers-color-scheme: dark (captured as docs-home-dark / docs-api-dark). The marketing and product pages declare no dark values and did not change under prefers-color-scheme (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)), so the token file's `dark` set is the docs' theme only.")
W()
W("### Fonts")
W()
W("- **anthropicSans** is the UI face everywhere (also as anthropicSansDisplay and anthropicSansRomanFallback). **anthropicSerif** carries display headlines and the docs' titles; **anthropicMono** is 13/19 code on the docs. All are variable 300-800 faces served from Anthropic's hosts (see fontFaces in [raw/css-vars.json](raw/css-vars.json)).")
W("- **Anthropicons-Variable** is the docs' icon font; its measured fractional weights tune the glyphs. All are commercial faces, not redistributable; Lato, Newsreader and IBM Plex Mono stand in inside the style guide.")
W()
W("### Screenshots")
W()
W("- People, paper and product imagery are Anthropic's content and appear only inside screenshots and crops.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- The docs' prose was not transcribed into the package; the components around it were measured.")
W("- No personal data was captured: the pages were read signed out, and no form was filled with real contact details.")
W()

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops")
