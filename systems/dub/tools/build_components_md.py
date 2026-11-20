#!/usr/bin/env python3
"""Build components.md for the Dub design reference.

Reads raw/components-computed.json (every component and state, measured),
tokens.json, screenshots/ and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the
palette token whose value matches, the font family is named once per value,
and a state row shows only what differs from the first state. Adapted from
the Calendly package's builder, which read the JSON directly.

Deterministic: re-running it on the same inputs reproduces components.md byte for byte.
Run from anywhere: python3 tools/build_components_md.py
"""
import json, os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
J = json.load(open("raw/components-computed.json"))
C = J["components"]
LAYOUT = {}
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
for n, t in flat(T["core"]):
    if t["$type"] == "color":
        BY_COLOR.setdefault(t["$value"], n)


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


def _alpha(c):
    """The alpha of a computed colour; 0 for transparent, so a `2px solid transparent` outline is no ring."""
    c = (c or "").strip().lower()
    if c in ("transparent", ""):
        return 0.0
    m = re.search(r"rgba\([^)]*,\s*([\d.]+)\s*\)|/\s*([\d.]+%?)\s*\)", c)
    if not m:
        return 1.0
    a = m.group(1) or m.group(2)
    return float(a[:-1]) / 100 if a.endswith("%") else float(a)


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
    # Painted layers that carry a state but not the root box: the element's own
    # ::before/::after always, and descendant paint only when the root paints
    # nothing (the case "Child layers" reports). A nav underline that goes
    # transparent -> black on hover lives in a::after, so it diffs here.
    bits = []
    for pe in ("::before", "::after"):
        if v.get(pe):
            p = v[pe]
            bits.append(" ".join(x for x in (pe, p.get("backgroundColor"), p.get("borderTopWidth"), p.get("boxShadow"), p.get("opacity")) if x))
    # A root box-shadow (e.g. the 1px focus ring gained on focus-visible) does
    # not remove the painted children: keep reporting their layers, which is
    # where a state-carrying child outline shows up.
    if s["backgroundColor"] == "rgba(0, 0, 0, 0)" and s["borderTopWidth"] == "0px" and s["backgroundImage"] == "none":
        for p in v.get("paint", [])[:6]:
            bits.append(" ".join(x for x in (p["node"], p.get("size"), p.get("bg"), p.get("border"), p.get("shadow"), p.get("outline"), p.get("radius")) if x))
    if bits:
        o["layers"] = "; ".join(bits)[:400]
    return o


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "outline", "text", "transition", "transform", "opacity", "icon", "placeholder", "layers"]


def state_rows(c):
    # A state whose capture failed (e.g. via: "focus failed" — the element would
    # not hold a real keyboard focus) is not a captured state: it is reported
    # separately so a failed attempt can never read as a measured absence of a
    # focus ring.
    states = [s for s in c["states"] if "style" in c["states"][s] and c["states"][s].get("via") != "focus failed"]
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
        bits = [re.sub(r"\..*$", "", p["node"]) if "::" not in p["node"] else p["node"].split(".")[0], re.sub(r"\.0+(?=x|px|$)", "", p["size"])]
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

PAGE_NAME = {"home": "home", "links": "links product", "partners": "partners",
             "pricing": "pricing", "customers": "customers", "enterprise": "enterprise",
             "compare": "compare", "sales": "contact-sales", "login": "log in",
             "register": "register", "docs": "docs", "docs-dark": "docs (dark)",
             "help": "help", "mobile": "home"}

GROUP_INTRO = {
    "Shell and navigation": "The marketing chrome on the near-white field: wordmark, the Product mega-menu trigger, plain links, Log in and the black Sign-up pill.",
    "Home hero": "The 48px Satoshi hero, the announcement pill, the two CTAs and the product-demo panel under it.",
    "Pricing": "The pricing surface: the Monthly/Yearly toggle, the shared plan panel with its names, prices and CTAs, and the FAQ accordion.",
    "Compare (vs Bitly)": "The /compare/bitly surface: the Satoshi headline and the feature comparison table.",
    "Customers": "The /customers surface: the Satoshi headline and the dark customer story cards.",
    "Contact sales form": "The /contact/sales card: work-email field, message textarea, topic pills and the Send submit — measured, never submitted.",
    "Log in and sign up": "The auth boundary cards on app.dub.co, measured but never submitted: the 384px login and register cards, fields and SSO buttons in the plain system stack.",
    "Docs and help (Mintlify)": "The Mintlify docs surface on /docs and /help — the only place a real theme toggle exists: the 288px sidebar, search pill, theme button, headings and feedback controls, measured in both light and dark.",
    "Footer": "The marketing footer: link columns and the round social icon buttons.",
    "Mobile (390 wide)": "The marketing surface at phone width: the compact header, the menu overlay and the stacked hero.",
}

SHOTS = [
    ("home", "Home", "/"),
    ("links", "Links (product page)", "/links"),
    ("partners", "Partners (product page)", "/partners"),
    ("pricing", "Pricing", "/pricing"),
    ("customers", "Customers", "/customers"),
    ("enterprise", "Enterprise", "/enterprise"),
    ("compare", "Compare vs Bitly", "/compare/bitly"),
    ("sales", "Contact sales", "/contact/sales"),
    ("blog", "Blog", "/blog"),
    ("changelog", "Changelog", "/changelog"),
    ("login", "Log in", "/login"),
    ("register", "Register", "/register"),
    ("docs", "Docs", "/docs"),
    ("docs-dark", "Docs, dark theme", "/docs (theme dropdown)"),
    ("help", "Help center", "/help"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "/"),
    ("mobile-pricing", "Pricing, phone", "/pricing"),
    ("mobile-docs", "Docs, phone", "/docs"),
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
icons = []

W("# Dub components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from dub.co on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. dub.co is three surfaces signed out: the Next.js marketing site (Tailwind + Satoshi/Inter), the app.dub.co auth shell on /login and /register (measured, never submitted), and the Mintlify docs/help surface on /docs and /help — the only place a real theme toggle exists, so docs was measured in both light and dark. Nothing was signed into, sent or submitted; the login, register and contact-sales forms were never filled past a deleted sample; no time the Send or Log-in buttons were ever pressed.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [patterns.md](patterns.md).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 14/20 500, #404040`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{theme}-{state}.png`: the marketing and auth surfaces paint `light` only; `docs-dark-dark-*` is the docs page under its own theme dropdown's Dark preference. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).")
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
    ("Mobile menu overlay", "home, phone width", "the round menu button's own toggle", "[mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open)"),
    ("Product mega-menu", "every marketing page", "the nav trigger's own hover", "[home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#mega-menu-panel), [menu-link](#menu-item)"),
    ("Mintlify AI assistant + promo overlays", "docs and marketing pages", "hidden, never answered (no assistant prompt was ever opened or sent)", "hidden before every shot and reading"),
    ("Docs dark theme", "/docs", "the page's own 'Change theme preference' dropdown (System/Light/Dark), a local UI toggle held in localStorage isDarkMode", "[docs-dark-dark-default](screenshots/docs-dark-dark-default.png), the dk-docs-* entries"),
    ("Billing-period toggle", "/pricing", "the Monthly/Yearly toggle's own click", "[pricing-light-yearly](screenshots/pricing-light-yearly.png), [billing-toggle](#billing-toggle)"),
    ("Signed-in product", "app.dub.co workspace", "the link-management workspace lives behind /login", "boundary; see Gaps"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# Capture descs that claim an interaction the S() call never ran (each lists
# default, hover, focus-visible and pressed only). Corrected here until a
# recapture writes the fixed descs from tools/capture/public/measure.mjs.
DESC_FIX = {
    "billing-toggle": 'The Monthly/Yearly period toggle ("10% discount + 12x usage upfront"), read on its Yearly option at rest, on hover, on keyboard focus and forced pressed; never clicked or checked out.',
    "faq-trigger": "A billing-FAQ accordion trigger, read closed: at rest, on hover, on keyboard focus and forced pressed.",
    "sales-topic": "A selectable topic pill on the contact form (Tools/Legal/…), read unselected: at rest, on hover, on keyboard focus and forced pressed; never submitted.",
}

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement files.")
W()
foc = []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st or "style" not in st or st.get("via") == "focus failed":
        continue
    s = st["style"]
    base = next((v["style"] for v in c["states"].values() if "style" in v), s)
    ring = (s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0
            and _alpha(s["outlineColor"]) > 0)
    # A ring painted on a child layer instead of the wrapper: offer buttons
    # draw outlines on inner nodes while the wrapper's own outline stays none.
    child_ring = next((n["outline"] for n in st.get("paint", [])
                       if n.get("outline") and _alpha(n["outline"].split(" offset")[0]) > 0), None)
    shadow = s["boxShadow"] != base["boxShadow"] and s["boxShadow"] != "none"
    border = any(
        s[f"border{d}{p}"] != base[f"border{d}{p}"]
        for d in ("Top", "Right", "Bottom", "Left")
        for p in ("Color", "Width", "Style")
    )
    desc = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else (f"on a child: {child_ring}" if child_ring else None)
    foc.append((k, ring or bool(child_ring), shadow, border, desc))
with_ring = [f"`{k}` ({r})" for k, ring, sh, bd, r in foc if ring]
with_shadow = [f"`{k}`" for k, ring, sh, bd, r in foc if not ring and sh]
with_border = [f"`{k}`" for k, ring, sh, bd, r in foc if not ring and not sh and bd]
without = [f"`{k}`" for k, ring, sh, bd, r in foc if not ring and not sh and not bd]
parts = [f"{len(with_ring)} draw an outline ring: {', '.join(with_ring)}."]
if with_shadow:
    parts.append(f"{len(with_shadow)} draw a focus ring as a shadow instead: {', '.join(with_shadow)}.")
if with_border:
    parts.append(f"{len(with_border)} change only their border: {', '.join(with_border)}.")
if without:
    parts.append(f"The other {len(without)} show no measured change: {', '.join(without)}.")
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {' '.join(parts)} On dub.co the button ring is the browser-default `auto 1px rgb(0, 95, 204)` outline, the docs surface draws its own 1px `#155dfc` ring, and the email field instead takes a black border plus a 1px black ring shadow.")
W()
W("**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.")
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


def dur_ms(d):
    return float(d[:-1]) * 1000 if d.endswith("s") and not d.endswith("ms") else float(d[:-2])


for (d, e), (ps, ks) in sorted(mot.items(), key=lambda kv: (dur_ms(kv[0][0]), kv[0][1])):
    W(f"| {d} | `{e}` | {', '.join(sorted(ps))} | {', '.join(sorted(ks)[:8])}{' and more' if len(ks) > 8 else ''} |")
W()
W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
# PRODUCT (adapt): the card-like components to compare in one table.
for k in ["plan-card", "demo-panel", "menu-link", "customer-card", "login-card", "register-card", "sales-card", "docs-copy"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if "style" in s), None)
    if st is None:
        continue
    p = props(st)
    W(f"| [{c['title']}](#{re.sub(r'[^a-z0-9 -]', '', c['title'].lower()).replace(' ', '-')}) | {p['size']} | {p.get('border', '-')} | {p.get('radius', '-')} | {p.get('background', '-')} | {p.get('shadow', 'none')} | {p.get('padding', '0')} |")
W()

# ------------------------------------------------ entries
W("## Components")
groups = [g for g in GROUP_INTRO if any(c.get("group") == g for c in C.values())]
for c in C.values():
    if c.get("group") not in groups:
        groups.append(c.get("group") or "Other")
for g in groups:
    W()
    W(f"### {g}")
    W()
    W(GROUP_INTRO.get(g, ""))
    for k, c in C.items():
        if c.get("group") != g:
            continue
        W()
        W(f"#### {c['title']}")
        desc = DESC_FIX.get(k, c.get("desc") or "").strip()
        if desc and not desc.endswith((".", ")", '"')):
            desc += "."
        where = PAGE_NAME.get(c["page"], c["page"])
        W(f"{desc + ' ' if desc else ''}Read as `{k}` on the {where} page{' at 390 wide' if g.startswith('Mobile') else ''}.")
        W()
        if c.get("missing"):
            W("Not on the page when it was captured.")
            continue
        failed = [s for s, v in c["states"].items() if "style" in v and v.get("via") == "focus failed"]
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
        if failed:
            W(f"**Focus not capturable.** A real keyboard focus could not be held on this element ({', '.join(f'`{s}`' for s in failed)} recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.")
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Dub wordmark, the mega-menu product glyphs, the Google/GitHub SSO marks, the social icons and the docs chrome glyphs) are the product's artwork. Declared under layoutGaps in the catalog entry.")
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
W("### The signed-in product")
W()
W("Dub's product — the link-management workspace, link creation, analytics dashboards, domains, tags, webhooks, integrations and billing — lives behind /login on app.dub.co and was never reached. The auth cards on /login and /register were captured as surfaces, never filled past a deleted sample and never submitted; the contact-sales form on /contact/sales was measured, never sent.")
W()
W("### Pages")
W()
W("- **The workspace.** Every post-login surface (links, analytics, domains, tags, webhooks, settings, billing) needs an account and was never reached; /login and /register were captured as forms and never filled or submitted.")
W("- **The dashboard mock.** The `demo-panel` under the home hero is a published illustration of the product UI, not the app — it was measured as marketing content.")
W("- **Checkout and onboarding.** Every Sign-up, Start-for-free, Start-trial and Send-message action was measured, never followed past its public landing; no plan was ever purchased.")
W("- **The docs search palette.** The 'Search… ⌘K' trigger was measured; the palette it opens (and the Mintlify AI assistant behind it) was never opened.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Disabled, error and loading states** were not seen on the public surface (the contact-sales submit paints disabled-grey until the required fields hold text, captured at rest).")
W("- **hero-badge and sales-submit focus-visible** recorded `via: focus failed` — a real keyboard focus could not be held there — so their focus look is uncaptured, not measured as absent.")
W("- **Email-field 'focus-visible'** is the field's `focused` state (clicked into): a black border plus a 1px black ring shadow, not the browser outline buttons draw.")
W()
W("### Themes")
W()
W("dub.co is not a themed product signed out: the marketing pages and the app.dub.co auth shell paint light only. The docs/help surface (Mintlify) carries the site's one real theme toggle — a Light/Dark/System dropdown that sets `dark` on <html> (localStorage isDarkMode) — and was captured in both: the dark set is the .dark re-binding the probe and the dk-docs-* components measured.")
W()
W("### Fonts")
W()
W("- **Satoshi** (Fontshare variable, marketing headings and docs h1s), **Inter** (marketing and docs body, self-hosted woff2 subsets), **Paper Mono** (docs code, Mintlify bundle), **GeistMono** (marketing code, next/font) are the served faces; the app.dub.co auth shell paints a plain ui-sans-serif system stack. None is distributed with the package — the style guide falls back to system sans.")
W()
W("### Screenshots")
W()
W("- Product illustrations, customer logos, the Dub wordmark and blog/changelog post art in the screenshots are the product's published content.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Marketing copy, customer stories, blog and changelog posts and the comparison table's claims are the product's content; only frames and components were measured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
