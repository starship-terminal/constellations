#!/usr/bin/env python3
"""Build components.md for the Anam design reference.

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

    # one pass over every spelling, so a colour converted from color(srgb), oklab() or lab() is
    # never re-matched as rgba() and labelled a second time
    def sub(m):
        g = m.groups()
        if g[0] is not None:
            return label(norm(*(round(float(x) * 255) for x in g[0:3]), g[3]))
        if g[4] is not None:
            return label(norm(*oklab_rgb(*(float(x) for x in g[4:7])), g[7]))
        if g[8] is not None:
            return label(norm(*lab_rgb(*(float(x) for x in g[8:11])), g[11]))
        return label(norm(*g[12:15], g[15]))

    return re.sub(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)"
                  r"|oklab\(([-\d.e]+) ([-\d.e]+) ([-\d.e]+)(?: / ([\d.]+))?\)"
                  r"|(?<!ok)lab\(([-\d.e]+) ([-\d.e]+) ([-\d.e]+)(?: / ([\d.]+))?\)"
                  r"|rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)", sub, c)


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

PAGE_NAME = {"home": "anam.ai home", "api": "anam.ai API", "pricing": "anam.ai pricing",
             "get-demo": "anam.ai Get a demo", "tools": "anam.ai tools",
             "interactive-avatars": "anam.ai interactive avatars", "about": "anam.ai about",
             "research": "anam.ai research", "case-studies": "anam.ai case studies",
             "blog": "anam.ai blog", "changelog": "anam.ai changelog",
             "docs-overview": "anam.ai docs (overview)", "docs-api": "anam.ai docs (API reference)",
             "docs-dark": "anam.ai docs, dark theme"}

GROUP_INTRO = {
    "Shell and navigation": "The chrome shared by the marketing pages: a floating pill nav (Anam mark; Developers / Pricing / Resources with hover submenus; Sign in; a black Get started pill) and the footer, whose link columns sit on a 32px-radius black panel. On a phone the nav collapses to a menu button.",
    "Home": "anam.ai's home: the Inter hero with the orange 'Meet our most expressive model' badge, the persona card carousel (each card a live avatar video with frosted-glass chips), the 'Talk with …' demo card with its call controls, and the sticky CTA band.",
    "Feature sections": "The scroll-driven sections further down the home page: the TabSection feature tabs (Human realism, Expression control, …), the benchmark feature card in IBM Plex Mono, and the logo cloud.",
    "Pricing": "anam.ai/pricing, a Next.js page: the title, monthly/annual billing toggle, the plan cards (Free / Pro / Enterprise) and the FAQ list.",
    "Demo request form": "anam.ai/get-demo, a Next.js page: the 420px sales form — work email, company, use case — measured in default, focused and filled states. Nothing was submitted.",
    "Docs (Mintlify)": "anam.ai/docs, a Mintlify site: the top tabs, search pill, Ask Assistant button, warm-stone sidebar and TOC rails, link cards, code and method badges. The ⌘K dialog and ⌘I panel were opened by keyboard, never submitted; the dark theme was toggled once.",
    "Cards and lists": "The card grids on the secondary pages: avatar cards on /interactive-avatars, team cards on /about, paper entries on /research, customer stories on /case-studies, post cards on /blog, release entries on /changelog and tool cards on /tools.",
    "Panels and dialogs": "The overlays a fresh profile meets: the cookie consent card (photographed and measured, then hidden without a click — a consent choice is a submission), the docs ⌘K search dialog and the ⌘I assistant sheet.",
    "Mobile (390 wide)": "The same pages as a phone draws them, at 390 x 844 with an iPhone user agent: the nav collapses to a menu button and the persona carousel scrolls horizontally.",
}

SHOTS = [
    ("home", "anam.ai home. Hero and badge, the persona video carousel, the demo card, feature sections, logo cloud, sticky CTA and the dark footer panel.", "https://anam.ai/"),
    ("api", "anam.ai/api. The API marketing page: hero, code and feature sections.", "https://anam.ai/api"),
    ("interactive-avatars", "anam.ai/interactive-avatars. The avatar gallery page.", "https://anam.ai/interactive-avatars"),
    ("pricing", "anam.ai/pricing. Title, billing toggle, plan cards, FAQ.", "https://anam.ai/pricing"),
    ("get-demo", "anam.ai/get-demo. The demo request form; the email field shown focused.", "https://anam.ai/get-demo"),
    ("tools", "anam.ai/tools. The tools index (latency benchmark and friends).", "https://anam.ai/tools"),
    ("about", "anam.ai/about. Team and company page.", "https://anam.ai/about"),
    ("research", "anam.ai/research. Papers and model entries.", "https://anam.ai/research"),
    ("case-studies", "anam.ai/case-studies. Customer story cards.", "https://anam.ai/case-studies"),
    ("blog", "anam.ai/blog. Post cards.", "https://anam.ai/blog"),
    ("changelog", "anam.ai/changelog. Release entries.", "https://anam.ai/changelog"),
    ("docs-overview", "anam.ai docs overview. Sidebar, TOC, prose, cards; also the ⌘K dialog and the ⌘I assistant sheet.", "https://anam.ai/docs/introduction/overview"),
    ("docs-api", "anam.ai docs API reference. Sidebar with method badges, code blocks.", "https://anam.ai/docs/api-reference/overview"),
    ("docs-dark", "anam.ai docs in its dark theme (.dark on html).", "https://anam.ai/docs/introduction/overview"),
]
MOBILE = [
    ("mobile-home", "anam.ai home at 390: menu button, hero, persona carousel, CTA; the consent card shown, then hidden.", "https://anam.ai/"),
    ("mobile-pricing", "anam.ai/pricing at 390.", "https://anam.ai/pricing"),
    ("mobile-docs-overview", "anam.ai docs overview at 390: the sidebar is behind the menu button.", "https://anam.ai/docs/introduction/overview"),
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

W("# Anam components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from anam.ai on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running pages. Nothing was signed into, created, sent or uploaded; the avatar call button was never pressed and no consent choice was made.")
W()
W("anam.ai is three public surfaces with one accent: the **marketing pages** (Framer: white ground, black ink and pills, orange #ff6200, frosted-glass chips on the avatar videos), the **app pages** /pricing, /get-demo and /tools (Next.js: a small `:root` token set — `--bg`, `--surface`, `--text`, `--border`, `--brand`), and the **docs** (Mintlify: a warm-stone gray ramp on `:root`, Inter and Paper Mono, the same orange as `--primary`). Only the docs ship a dark theme.")
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
W("Screenshots are named `{page}-light-{state}.png` (the dark docs pass is `docs-dark-dark-{state}.png`). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).")
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
    ("Cookie consent card", "the marketing pages and mobile home, on load on a fresh profile", "photographed and measured in place, then hidden without a click — a consent choice is a submission", "[home-light-consent](screenshots/home-light-consent.png), [mobile-home-light-consent](screenshots/mobile-home-light-consent.png), [consent-card](#cookie-consent-card)"),
    ("Nav submenu", "the pill nav, on hover over Developers or Company", "a real hover opened the dropdown; captured open, never clicked through", "[home-light-nav-submenu](screenshots/home-light-nav-submenu.png), [nav-submenu](#nav-submenu)"),
    ("Persona carousel", "anam.ai home, on load", "the carousel keeps every persona's card parked in a strip; a second card was clicked into the centre for the selected state", "[home-light-persona-tab](screenshots/home-light-persona-tab.png), [persona-chip](#persona-chip)"),
    ("Docs ⌘K search dialog", "anam.ai/docs", "opened with ControlOrMeta+K; measured open, nothing typed", "[docs-overview-light-search-dialog](screenshots/docs-overview-light-search-dialog.png), [docs-search-dialog](#search-dialog)"),
    ("Docs ⌘I assistant sheet", "anam.ai/docs", "the sheet is open by default; measured in place, nothing sent", "[docs-overview-light-assistant-panel](screenshots/docs-overview-light-assistant-panel.png), [docs-assistant-panel](#assistant-panel)"),
    ("Talk-with call controls", "anam.ai home, inside the demo card", "measured and hovered, never pressed: a press opens a live session on Anam's servers and asks for the microphone", "[demo-cta](#demo-call-button)"),
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
    ("Button", ("hero-cta", "demo-cta", "plan-cta", "form-submit", "consent-accept", "docs-search-btn", "docs-assistant-btn", "docs-assistant-send", "docs-theme-btn"), None),
    ("Icon button", ("docs-theme-btn", "docs-assistant-send"), None),
    ("Link", ("nav-link", "nav-signin", "nav-sub-link", "footer-link", "docs-nav-link", "docs-toc-link", "docs-topnav-link"), None),
    ("Text field", ("form-input", "docs-search-input"), None),
    ("Text area", ("form-textarea",), None),
    ("Select", (), "no public page offers one"),
    ("Checkbox", (), "no public form has one"),
    ("Radio", (), "no radio control on the public pages; the billing toggle is a pair of buttons"),
    ("Switch", ("billing-toggle",), None),
    ("Tabs", ("tab-item", "docs-topnav-link"), None),
    ("Menu", ("nav-submenu",), None),
    ("Tooltip", (), "none appeared on hover or focus"),
    ("Dialog", ("docs-search-dialog", "docs-assistant-panel"), None),
    ("Toast", (), "no toast appeared after any action the capture took signed out"),
    ("Card", ("persona-chip", "persona-chip-selected", "demo-card", "plan-card", "docs-card", "consent-card", "feature-card"), None),
    ("List row", ("faq-item",), None),
    ("Table", (), "pricing lays plans out as cards, not a table"),
    ("Avatar", ("persona-chip", "demo-card"), None),
    ("Badge", ("docs-method-badge", "hero-sub"), None),
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
foc = []
unfocusable = []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st:
        continue
    # A state whose focus failed is a failed attempt, not a focus reading:
    # it is named here rather than counted or painted as captured.
    if "style" not in st:
        if st.get("via") == "focus failed" or "error" in st:
            unfocusable.append(k)
        continue
    s = st["style"]
    base = c["states"].get("default", {}).get("style", s)
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0 and (s["outlineStyle"] != base["outlineStyle"] or s["outlineWidth"] != base["outlineWidth"])
    ring_shadow = s["boxShadow"] != base["boxShadow"] and "0px 0px" in s["boxShadow"]
    foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else ("ring shadow " + colour(s["boxShadow"], tokens=False) if ring_shadow else None)))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
failed_note = f" Keyboard focus could not be moved to {', '.join(f'`{k}`' for k in unfocusable)}, so those have no focus reading." if unfocusable else ""
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} show a change: {', '.join(with_ring)}. The other {len(without)} draw nothing new — anam.ai largely lets the browser's own outline stand (Framer links take the default `auto` outline; the docs buttons keep their resting style): {', '.join(without)}.{failed_note}")
W()
W("**Pressed.** Pressed was forced with DevTools, so it is the :active styles only: the plan CTA measurably shrinks a couple of pixels under :active (137.81x44 to 133.68x42.68 — a scale press), while the marketing pills and docs buttons keep their resting paint; the call controls were never really pressed because a press opens a live session.")
W()
W("**Motion.** Transitions measured on the components, by duration. The signature motion is the persona carousel's `transform .3s cubic-bezier(.12,.23,.5,1)` spring and the consent card's 240ms rise-in (`anam-cc-rise`); the scroll-driven TabSection animates on scroll, not on a transition.")
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
W("**Card shapes.** Default-state values; the entries hold the states. The marketing site's signature card is the 32px-radius persona tile over a long soft shadow with frosted-glass chips; the docs' is a 16px-radius white card with a warm hairline border.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
for k in ["persona-chip", "demo-card", "plan-card", "docs-card", "consent-card", "feature-card", "docs-search-dialog", "docs-assistant-panel"]:
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

# ------------------------------------------------ gaps
W()
W("## Gaps")
W()
W("### Pages")
W()
W("- **The product app.** lab.anam.ai (/build, /login, /register) is the signed surface: nothing behind Sign in or Get started was captured, and the persona builder, API keys and session UI are all missing. The kit never signs in or registers.")
W("- **A live avatar session.** The 'Talk with …' button opens a WebRTC session on Anam's servers and asks for the microphone; the control was measured and hovered, never pressed, so the in-call UI is missing.")
W("- **Checkout and account.** The plan CTAs lead to checkout/registration; no purchase was made and no card field was filled.")
W("- **Article-depth pages.** The index pages were captured; the blog's posts, the case studies' stories and the guides were not opened.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on the safe controls, so a state a script adds on mousedown (if any) is missing; call, consent, search-send and submit controls were never pressed at all.")
W("- **The hero title's last word rotates** through personas and the carousel re-renders its cards as it autoplays; a capture pins whichever pass was running.")
W("- **The persona cards are live videos** (and the demo card can hold a running avatar), so a crop shows one frame of a moving face.")
W("- **Disabled, loading and error** were not seen on any public control.")
W()
W("### Themes")
W()
W("Only the docs ship a dark theme: `.dark` on html via the theme menu (measured in the docs-dark pass). The marketing pages and the /pricing, /get-demo, /tools apps declare no dark values and did not change under prefers-color-scheme (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)), so the token file's `dark` set is the docs' theme only.")
W()
W("### Fonts")
W()
W("- **Inter** is the UI face everywhere (self-hosted on the marketing pages, `--font-inter` on docs). **IBM Plex Mono** (400/500) covers code and metrics on the marketing pages; the docs code is **Paper Mono** (Mintlify's face).")
W("- **MD Thermochrome 0.4 Trial** — a licensed trial face — is loaded on the home page for display accents. It is not redistributable; substitute a close free face when reproducing the style.")
W()
W("### Screenshots")
W()
W("- Avatar faces, customer logos, blog artwork and the cookie banner are Anam's content and appear only inside screenshots and crops.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- The docs' prose was not transcribed into the package; the components around it were measured.")
W("- No personal data was captured: the pages were read signed out.")
W()

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops")
