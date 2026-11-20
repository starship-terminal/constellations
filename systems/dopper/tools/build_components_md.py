#!/usr/bin/env python3
"""Build components.md for the Gauth design reference.

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
    # where a state-carrying child outline (the 3px cyan CTA ring) shows up.
    if s["backgroundColor"] == "rgba(0, 0, 0, 0)" and s["borderTopWidth"] == "0px" and s["backgroundImage"] == "none":
        for p in v.get("paint", [])[:6]:
            bits.append(" ".join(x for x in (p["node"], p.get("size"), p.get("bg"), p.get("border"), p.get("shadow"), p.get("outline"), p.get("radius")) if x))
    if bits:
        o["layers"] = "; ".join(bits)[:400]
    return o


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "outline", "text", "transition", "transform", "opacity", "icon", "placeholder", "layers"]


# Three focus-visible states (nav-link, m-burger, m-menu-pill) were recorded `via: focus failed`;
# their via was later rewritten by hand to this sentence, not re-measured.
HAND_RELABELLED_FOCUS = "el.focus() — a real ring painted; document.activeElement read the shadow host (check fixed in kbFocus)"

# An entry flagged missing keeps no readings: four (flyout, flyout-tab, flyout-card, m-filter-radio)
# were flagged by hand with their misidentified states left in raw/, and none of those states is
# a reading of the component.
LIVE = {k: c for k, c in C.items() if not c.get("missing")}

# Entries whose committed reading is not the component the name says.
WRONG = {
    "cart-empty": "The reading is the 1440 x 80 \"Your cart\" h1, not the empty-basket block; the 2026-11-13 run did not find the block and kept these states (recaptureMissed).",
}


def focus_not_captured(v):
    """A state whose reading is not what its name says: a skipped one, or a focus-visible reading
    taken where keyboard focus never landed (kbFocus returned "focus failed") or where the element
    took focus but did not match :focus-visible. Its style is the element at rest, so it is left out
    of every table and tally and listed as "focus could not be captured"."""
    return (bool(v.get("skipped")) or v.get("via") in ("focus failed", HAND_RELABELLED_FOCUS)
            or (v.get("focus") or {}).get("matches") is False)


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

PAGE_NAME = {"home": "home", "shop": "shop home", "category": "category (PLP)", "pdp": "product page", "cart": "cart", "login": "login", "mobile": "home", "mobile-category": "category (PLP)"}

GROUP_INTRO = {
    "Shell and navigation": "The DOPPER-NAVIGATION custom element on both hosts: the dopper. wordmark, the Bottle / Travel Mug / Tap / Mission / Get Involved flyout triggers, right links (Impact report / Find a Store / For Businesses / EN) and the bag button. The Bottle trigger opens a yellow mega-menu; its shadow DOM carries the nav content.",
    "Home (www)": "The video hero with the \"Whatever the season\" display and Watch now / Shop our collection pills, the yellow Bottle flyout, the collections tab showcase, the impact calculator, content cards and the newsletter band.",
    "Shop": "The Magento storefront (shop.dopper.com): the same header plus the catalog nav row (All products / Mugs / Bottles / …) and hero tiles with darkBlue CTAs.",
    "Product list (PLP)": "The /bottles list: centred display title, the teal + Filters pill, the light-blue filter sheet (open on desktop), product cards with badge chips and EUR prices.",
    "Product page (PDP)": "The /dopper-original-pacific-blue detail: breadcrumb, gallery, price, the colour/collection/pattern configurator rows, the darkBlue Add to cart and the icon feature list.",
    "Cart": "The /checkout/cart empty state: \"Your cart\" display, the darkBlue-3 continue-shopping strip, the basket illustration and Back to shop CTA. A filled cart was not exercised.",
    "Login and signup": "The Magento /customer/account/login surface: the darkBlue \"Registered Customers\" card (Email + Password fields, Sign in, Show password, Remember Me, Forgot link) beside the light-blue \"New Customers\" card with Create an Account. Fields were focused and typed into, then cleared — nothing sent; Sign in was never pressed.",
    "Footer": "The sand footer: newsletter band (name + email fields), \"Just refill\" columns, social icons, certification and payment logos.",
    "Mobile (390 wide)": "The same surfaces at phone width: the header shrinks to wordmark + sand burger, the menu opens as a darkBlue full-screen panel, and the PLP filters open as a full sheet.",
}

SHOTS = [
    ("home", "Marketing home (www.dopper.com)", "/"),
    ("mission", "Mission story", "/en/mission/story"),
    ("product-insulated", "Insulated product page", "/en/products/insulated"),
    ("blog", "Blog", "/en/blog/just-refill"),
    ("shop", "Shop home (shop.dopper.com)", "shop.dopper.com/"),
    ("category", "Bottles PLP", "shop.dopper.com/bottles"),
    ("pdp", "Product detail", "shop.dopper.com/dopper-original-pacific-blue"),
    ("cart", "Cart (empty)", "shop.dopper.com/checkout/cart/"),
    ("login", "Customer login", "shop.dopper.com/customer/account/login/"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "/"),
    ("mobile-shop", "Shop home, phone", "shop.dopper.com/"),
    ("mobile-category", "Bottles PLP, phone", "shop.dopper.com/bottles"),
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

W("# Dopper components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from www.dopper.com and shop.dopper.com on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running pages. Prices render in EUR. Nothing was signed into, created, submitted or paid for: the login fields were focused and typed into then cleared, never sent, and Add to cart / Sign in / checkout were never pressed for real.")
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
W("Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).")
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
    ("Bottle mega-menu", "home", "the Bottle nav trigger's own hover/click", "[home-light-menu](screenshots/home-light-menu.png), [flyout](#mega-menu), [flyout-tab](#flyout-tab), [flyout-card](#flyout-card)"),
    ("Mobile menu overlay", "home, phone width", "the burger button's own toggle", "[mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-nav-item), [m-menu-pill](#mobile-menu-pill)"),
    ("Collections tab", "home", "a collection tab's own click (local swap)", "[collection-tab](#collection-tab)"),
    ("PLP filter sheet", "the Bottles list", "open by default on desktop; the + Filters pill's own toggle on mobile", "[category-light-default](screenshots/category-light-default.png), [mobile-category-light-filter](screenshots/mobile-category-light-filter.png), [filter-panel](#filter-panel), [filter-radio](#filter-radio), [m-filter-sheet](#filter-sheet-mobile)"),
    ("Cookiebot consent dialog", "every page on both hosts", "hidden, never answered (Allow all / Allow selection / Deny were never clicked)", "hidden before every shot and reading"),
    ("Login fields", "customer login", "focused and typed into, then cleared — Sign in was never pressed", "[login-email](#email-field), [login-password](#password-field)"),
    ("Checkout and account", "shop.dopper.com checkout, customer area", "behind checkout/sign-in; the empty cart and the login card were measured, never used", "boundary; see Gaps"),
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
for k, c in LIVE.items():
    st = c["states"].get("focus-visible")
    if st and focus_not_captured(st):
        unfocused.append(f"`{k}`")
    if not st or not measured(st):
        continue
    s = st["style"]
    base = next((v["style"] for v in c["states"].values() if measured(v)), s)
    # A fully transparent outline paints nothing: a transparent outline must
    # not count as a painted ring.
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0 and s["outlineColor"] != "rgba(0, 0, 0, 0)"
    # A ring painted on a child layer instead of the wrapper counts as ringed
    # too — unless that outline is also transparent.
    child_ring = next((n["outline"] for n in st.get("paint", []) if n.get("outline") and "rgba(0, 0, 0, 0)" not in n["outline"]), None)
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
for k, c in LIVE.items():
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
# PRODUCT (adapt): the card-like components to compare in one table.
for k in ["content-card", "product-card", "login-card", "new-card", "flyout-card", "filter-panel"]:
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
        if k in WRONG:
            W()
            W(f"**Known wrong; recapture needed.** {WRONG[k]}")
        if c.get("note"):
            # A recorded caveat on the entry itself — e.g. a selector that
            # measured a neighbouring section until it was scoped.
            W()
            W(f"**Note:** {c['note']}")
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
            hand = any(c["states"][s].get("via") == HAND_RELABELLED_FOCUS for s in failed)
            W(f"**Focus not capturable.** A real keyboard focus could not be held on this element ({', '.join(f'`{s}`' for s in failed)} recorded `via: focus failed`{'; the via was later rewritten by hand, not re-measured' if hand else ''}), so its focus look is uncaptured — not measured as absent.")
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the dopper. wordmark, the nav chevrons and bag glyph, the feature-line iconography, the 'Be my hero' basket illustration, the social and payment marks) are the product's artwork. The shop serves a Dopper-Icons icon font (raw/css-vars.json fonts). Declared under layoutGaps in the catalog entry.")
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
W("Everything behind the login card — the customer account, order history, addresses and the whole checkout flow — was never reached. The Magento checkout begins at /checkout/ past the cart and was never opened; Add to cart was measured and its pressed state CDP-forced, never really clicked, so a filled cart, the cart drawer, shipping, payment and any logged-in surface are undocumented. The marketing site's \"For Businesses\" B2B portal, the Digital Product Passport and the Tap/Map/community apps are linked surfaces that were not captured.")
W()
W("### Pages")
W()
W("- **Two hosts.** www.dopper.com is the Next.js/Storyblok marketing site; shop.dopper.com is Magento 2 (theme Dopper/dopper_b2c). The header and brand palette are shared; shop values are compiled literals (measured, not declared). Other locales (/nl/, /de/, /fr/) were not captured — English only.")
W("- **Add to cart was never really clicked** (its pressed state is CDP-forced): the filled cart, mini-cart and every step past it are uncaptured by design.")
W("- **Configurator rows** ('Choose collection', 'Select your pattern', 'Own text or image', 'Accessories') are links to filtered/option views, not in-page toggles — the kit's toggle refused them; measured at rest only.")
W("- **The flyout card's inner CTAs** ('Buy a bottle', 'Customise 60+ bottles') sit inside the card's own markup — probably a closed shadow root — no standalone leaf exposed them. The same deep-sea pill is measured as btn-dark.")
W("- **External surfaces** (Dopper app stores, social profiles, Cradle to Cradle, the Digital Product Passport) are linked but were never opened.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover); on elements inside DOPPER-NAVIGATION's shadow root the CDP node lookup could not reach them, so nav-trigger/nav-link/m-burger/m-nav-item/m-menu-pill have no pressed reading (recorded as errors, not absence).")
W("- **Disabled, error and loading states** were not seen on the public surface (the PDP buy box's skeleton shimmer was caught mid-load in the default shot).")
W("- **The mega-menu closes on blur**; each flyout-child measurement re-opened it via the Bottle trigger before reading.")
W()
W("### Themes")
W()
W("Light-only. Neither host has a dark theme mechanism — no theme class, attribute or prefers-color-scheme retheme was found, and vars.mjs resolved only a light set. The darkBlue mobile menu and the deep-sea/darkBlue bands are brand-painted surfaces of the light page, not a theme — the export holds no invented dark set.")
W()
W("### Fonts")
W()
W("- **Dopper** (regular — the display face and wordmark) and **Gilroy** (Medium/400, Bold/600) are served from www.dopper.com's Next.js media; the shop also serves Gilroy 400/600/800 and a Dopper-Icons icon font. The @font-face blocks are harvested in raw/css-vars.json. The style guide falls back to system sans — the faces are licensed, not shipped.")
W()
W("### Screenshots")
W()
W("- The hero is a full-bleed video ('Whatever the season'): screenshots freeze one frame; its motion is not a token.")
W("- Full-page captures were bounded at the kit's 8-chunk cap: home is ~10k px (9999 captured), shop ~13k px, category ~11.9k px; mobile pages exceed 15k px and were stitched from tiles. Everything below the cap is documented but the longest tails were truncated.")
W("- The Cookiebot dialog and the chat widget were hidden before every shot, never answered; where a page reserves their layer the shots show the page as a consenting visitor sees it.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Product photography, the bottle artwork, marketing copy and article content are the product's; only frames and components were measured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
