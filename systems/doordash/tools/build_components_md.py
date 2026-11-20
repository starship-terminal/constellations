#!/usr/bin/env python3
"""Build components.md for the DoorDash design reference.

Reads raw/components-computed.json (every component and state, measured), tokens.json,
screenshots/ and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the palette token whose
value matches, the font family is named once per value, and a state row shows only what differs
from the first state. Adapted from the Calendly package's builder.

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


def sides(t, r, b, l):
    if t == r == b == l:
        return t
    if t == b and r == l:
        return f"{t} {r}"
    return f"{t} {r} {b} {l}"


# The browser's own link colours (unvisited, visited, active): an icon or text painted in one
# inherited it from an unstyled anchor in the Wayback replay.
UA_LINK = ("rgb(0, 0, 238)", "rgb(85, 26, 139)", "rgb(255, 0, 0)")


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
    elif s["fontFamily"].startswith("Times"):
        # No text node was read, and the element kept the browser's inherited defaults in the
        # Wayback replay (Times 16px, black or link blue): a UA value, not a DoorDash one.
        o["text"] = f"browser default ({font(s['fontSize'], s['lineHeight'], s['fontWeight'], s['fontFamily'])}, {colour(s['color'], tokens=False)})"
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
        icol = v["icon"].get("color") or v["icon"].get("stroke") or v["icon"].get("fill") or ""
        o["icon"] = f"{num(v['icon']['w'])} x {num(v['icon']['h'])}, {colour(icol)}"
        if icol in UA_LINK:
            o["icon"] += " (the browser's default link colour, inherited in the replay)"
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
    # where a state-carrying child outline (the 3px cyan CTA ring) shows up.
    if s["backgroundColor"] == "rgba(0, 0, 0, 0)" and s["borderTopWidth"] == "0px" and s["backgroundImage"] == "none":
        for p in v.get("paint", [])[:6]:
            bits.append(" ".join(x for x in (p["node"], p.get("size"), p.get("bg"), p.get("border"), p.get("shadow"), p.get("outline"), p.get("radius")) if x))
    if bits:
        o["layers"] = "; ".join(bits)[:400]
    return o


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "outline", "text", "transition", "transform", "opacity", "icon", "placeholder", "layers"]


def focus_not_captured(v):
    """A state whose reading is not what its name says: a skipped one, or a focus-visible reading
    taken where keyboard focus never landed (kbFocus returned "focus failed") or where the element
    took focus but did not match :focus-visible. Its style is the element at rest, so it is left out
    of every table and tally and listed as "focus could not be captured"."""
    return bool(v.get("skipped")) or v.get("via") == "focus failed" or (v.get("focus") or {}).get("matches") is False


def measured(v):
    return "style" in v and not focus_not_captured(v)


def visible(colour_value):
    """False for a fully transparent colour: a `2px solid transparent` outline draws nothing."""
    return not re.search(r"rgba\(\d+, \d+, \d+, 0\)|transparent|/ 0\)", colour_value)


def state_rows(c):
    # A state whose capture failed (e.g. via: "focus failed" — the element would
    # not hold a real keyboard focus) is not a captured state: it is reported
    # separately so a failed attempt can never read as a measured absence of a
    # focus ring.
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

PAGE_NAME = {"home": "home", "food-delivery": "food delivery", "business": "DoorDash for Business",
             "dashpass": "DashPass student", "restaurants": "restaurants-near-me", "store": "restaurant storefront",
             "hsa": "HSA/FSA store", "promos": "promo codes", "careers": "careers", "mobile": "home"}

GROUP_INTRO = {
    "App shell and navigation": "The consumer app chrome that ships signed out: the marketing top bar with Sign in / Sign Up and the storefront Header (logo, address gate, side-nav, cart, bell).",
    "Marketing hero": "The red campaign hero — TTNormsProCond-Blk display headline, the DoorDash wordmark, and the two address-gate pills, measured but never pressed.",
    "CTA bands and cards": "The mid-page call-to-action sections (CTASplash bands, business and DashPass CTAs) and the Become-a-Dasher-style value-prop cards.",
    "Directory lists and tabs": "The SEO directory surfaces: the Top Cities / Top Cuisines / Top Chains tabs, city/cuisine link lists and the Show-more toggles.",
    "Storefront (menu page)": "A real public restaurant page (/en-US/store/…): store header, Delivery/Pickup toggle, the menu grid, quick-add circles and the recommended carousel — all read-only.",
    "Restaurant directory": "The /en-US/restaurants-near-me/ listings: compact cards with offer and leaderboard badges, FAQ accordions and pagination.",
    "Fields, search and gates": "The native language select, the address-search gate (measured and focused, never submitted), catalog search fields and the cookie banner (measured then re-hidden, never answered).",
    "Footer": "The marketing footer: link columns, app-store badges, language select and social links.",
    "Careers site (WordPress stack)": "careersatdoordash.com — a separate WordPress/Tailwind stack (bg-pinot-noir, .btn pills), not the prism consumer system; measured only for context.",
    "Mobile (390 wide)": "The marketing home at phone width: the compact top bar and stacked hero.",
}

SHOTS = [
    ("home", "Home", "/ (wayback 2026-11-12)"),
    ("food-delivery", "Food delivery directory", "/food-delivery/ (wayback 2026-10-04)"),
    ("business", "DoorDash for Business", "/en-US/business/ (wayback 2026-10-12)"),
    ("dashpass", "DashPass student", "/en-US/dashpass/student (wayback 2026-10-12)"),
    ("restaurants", "Restaurants near me", "/en-US/restaurants-near-me/ (wayback 2026-10-05)"),
    ("store", "Restaurant storefront", "/en-US/store/the-sweet-tooth-north-miami-beach-33434247/ (wayback 2026-10-24)"),
    ("hsa", "HSA/FSA store", "/en-US/p/hsa-fsa-store (wayback 2026-09-30)"),
    ("seasonal", "Seasonal campaign", "/en-US/p/seasonal-holidays/ (wayback 2026-10-25)"),
    ("promos", "Promo codes", "/en-US/promos/ (wayback 2026-10-08)"),
    ("careers", "Careers", "careersatdoordash.com (wayback 2026-10-09)"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "/ (wayback 2026-11-12)"),
    ("mobile-store", "Storefront, phone", "/en-US/store/… (wayback 2026-10-24)"),
    ("mobile-food-delivery", "Food delivery, phone", "/food-delivery/ (wayback 2026-10-04)"),
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

W("# DoorDash components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from www.doordash.com pages rendered from Internet Archive snapshots on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page — archival evidence: every live *.doordash.com route Cloudflare-blocked this client, so each page is the product's own SSR HTML and CSS proxied by the Wayback Machine (routes and snapshot ids in [raw/archive-urls.json](raw/archive-urls.json)). The consumer stack is consumer-web-next (Next.js SSR, styled-components) over the prism design-token system (:where(.prism-theme): --base-*, --usage-*, --comp-*); careers is a separate WordPress/Tailwind stack. Nothing was signed into, ordered, address-entered or submitted; the address-gate field was focused once for measurement and never filled; consent and Turnstile elements were hidden, never answered.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [patterns.md](patterns.md).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-state.png`: every captured surface paints `light` — no dark theme is published on these pages. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). The Wayback Machine's replay toolbar is hidden in every shot.")
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
    ("Wayback Machine toolbar", "every page", "hidden on every shot — archive chrome is not the product", "never visible in committed evidence"),
    ("Cookie banner", "storefront + directory pages", "un-hidden for one computed-style reading, then re-hidden — never answered", "[cookie-banner](#cookie-banner) values only"),
    ("Cloudflare Turnstile nodes", "every consumer page", "dormant testids hidden, never answered", "hidden before every shot and reading"),
    ("Directory tabs", "home", "the Top Cuisines tab's own toggle — a local reveal", "[home-light-cuisines](screenshots/home-light-cuisines.png)"),
    ("Delivery/Pickup toggle", "storefront", "the Pickup option's own toggle — local UI state", "[store-light-pickup](screenshots/store-light-pickup.png)"),
    ("Address gate", "home, promos, storefront", "the field was focused for measurement; nothing typed, never submitted — the gate stays closed", "boundary; see Gaps"),
    ("Signed-in product", "consumer app, ordering, cart, checkout", "every Sign-in / Sign-up / cart / quick-add action measured, never followed", "boundary; see Gaps"),
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
    base = next((v["style"] for v in c["states"].values() if measured(v)), s)
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0 and visible(s["outlineColor"])
    # A ring painted on a child layer instead of the wrapper: offer buttons
    # draw 1px dotted outlines on their inner anchor while the wrapper's own
    # outline stays none. Those states must count as ringed too.
    child_ring = next((n["outline"] for n in st.get("paint", []) if n.get("outline") and visible(n["outline"])), None)
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
if unfocused:
    parts.append(f"Focus could not be captured on {len(unfocused)} more (keyboard focus never landed on them, so their readings are left out): {', '.join(unfocused)}.")
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {' '.join(parts)}")
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
W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
for k in ["cta-band", "value-prop-card", "rest-card", "menu-item", "cookie-banner", "hero-band"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if measured(s)), None)
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
        desc = (c.get("desc") or "").strip()
        if desc and not desc.endswith((".", ")", '"')):
            desc += "."
        where = PAGE_NAME.get(c["page"], c["page"])
        W(f"{desc + ' ' if desc else ''}Read as `{k}` on the {where} page{' at 390 wide' if g.startswith('Mobile') else ''}.")
        W()
        if c.get("missing"):
            W("Not on the page when it was captured.")
            continue
        failed = [s for s, v in c["states"].items() if focus_not_captured(v)]
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the DoorDash wordmark, social glyphs, store badges, product illustrations and the storefront imagery) are the product's artwork. Declared under layoutGaps in the catalog entry.")
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
W("DoorDash's product — the consumer ordering flow, restaurant browsing past the address gate, cart, checkout, DashPass membership, merchant dashboard and Dasher app — lives behind sign-in or the address search and was never reached. Every Sign-in, Sign-up, cart, quick-add, group-order and address action was measured, never followed. Identity anchors point at identity.doordash.com OAuth and were never clicked.")
W()
W("### Live access")
W()
W("- **Cloudflare gating.** Every live *.doordash.com surface tried on 2026-11-13 (home, /about/, /careers/, /merchant/, /dasher/, /en-US, /business/, merchants.doordash.com, dasher.doordash.com, help.doordash.com, plus robots.txt and the favicon) answered a 403 managed challenge — 'Performing security verification' — that never resolved in headless Chromium, new-headless or headed Chrome. The Wayback Machine holds the product's own SSR output, which is what this package captures; every page is labelled with its snapshot id in [raw/archive-urls.json](raw/archive-urls.json).")
W("- **What 'archived' means here.** The DOM, stylesheets and token layer are the product's own; the Wayback Machine proxies them and injects its toolbar (hidden in every shot). Images served from img.cdn4dd.com render live because that CDN is not gated. Nothing is presented as a current live capture.")
W()
W("### Pages")
W()
W("- **Behind the address gate.** The consumer browsing experience past 'enter your address' — local restaurant lists, personalised carousels, delivery times and fees — requires a real address or sign-in and was never entered; a generic landmark was not tried either, because the gate's submit would place state on the session.")
W("- **Ordering and checkout.** The menu item's quick-add, cart, group-cart and every checkout step were measured or left unpressed: a press would start a cart.")
W("- **Merchant and Dasher onboarding.** merchants.doordash.com and dasher.doordash.com are Cloudflare-gated live and had no usable Wayback captures; the marketing links that reach them are present but their signup wizards are uncaptured.")
W("- **Store directory pages.** /en-US/store/… pages are public once a store slug is known; one real storefront (The Sweet Tooth, North Miami Beach) was captured. Other stores' pages exist but were not enumerated.")
W("- **Sign-in and sign-up.** The anchors point at identity.doordash.com/auth with signed state parameters; the OAuth flow was never opened.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Disabled, error and loading states** exist richly in the --comp-* token layer (…-disabled, …-progressing) and were tokenised from the declarations; the public surface rarely paints them.")
W("- **Browser defaults in the replay.** Elements the site styles only through their text children kept the browser's inherited defaults in the Wayback replay: Times 16px, #000000 text and the #0000ee link blue on anchors and the icons inside them. An entry whose text reads \"browser default (...)\" or whose icon is marked as the browser's link colour shows that, not a DoorDash value; the component tokens take their text colour from the first text node instead.")
W("- **Hydration.** The archived pages are the SSR output; React hydration may not complete under Wayback, so lazy content that mounts after hydration (extra directory rows, some imagery) can be absent from a shot — the DOM and styles that did render are real.")
W()
W("### Themes")
W()
W("The prism consumer system publishes one light theme on this surface: no `.dark` scope, no `data-theme` attribute and no `prefers-color-scheme` bindings appear in the captured sheets, so there is no dark set — one is not inferred.")
W()
W("### Fonts")
W()
W("- **DD Norms** (proprietary; families `--base-font-family-default/brand/condensed`, weights 300-800, a 28-step px size scale) is the prism face, served from web-assets.cdn4dd.com; **TTNormsProCond-Blk** at weight 900 is the campaign display face set inline on hero headlines. The careers site's WordPress theme loads its own faces. The style guide falls back to system sans.")
W()
W("### Screenshots")
W()
W("- Product photography (the hero flat-lay, restaurant imagery), the DoorDash wordmark and merchant logos in the screenshots are the product's published content, rendered from the archive.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Marketing copy, restaurant names, menus and prices are the product's content; only frames and components were measured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
