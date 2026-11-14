#!/usr/bin/env python3
"""Build components.md for the Faire design reference.

Reads raw/components-computed.json (every component and state, measured),
tokens.json, screenshots/ and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the
palette token whose value matches, the font family is named once per value,
and a state row shows only what differs from the first state. Adapted from
the Coursera kit's builder via the Deezer package, which read markdown; this
one reads the JSON directly.

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

PAGE_NAME = {"home": "home", "category": "category teaser", "brand": "brand storefront",
             "suppliers": "suppliers listing", "suppliersAll": "suppliers A-Z",
             "howItWorks": "how-faire-works", "about": "about", "news": "newsroom",
             "careers": "careers", "largeRetailers": "large-retailers", "pos": "point-of-sale",
             "markets": "markets", "support": "help center", "affiliates": "affiliates",
             "apply": "brand application", "signin": "sign-in dialog", "signup": "sign-up dialog",
             "notfound": "404", "mobile": "home"}

GROUP_INTRO = {
    "Site chrome": "The fixed header on every page: the Faire wordmark, the 'All categories' dropdown (its panel is a full-width white sheet), the search field, the EN-US locale control, Blog, 'Sign up to sell', 'Sign in' and the dark 'Sign up to buy' fs-button--primary — plus the sub-header category strip and the promo line above.",
    "Home": "The home page: the 'Find your next bestseller' serif display hero over lifestyle media, the featured-brands pill tabs, brand and category tiles and the sign-up CTAs.",
    "Category teaser": "/category/Home Decor — the public teaser grid: a 'Wholesale home decor' serif masthead over media, the 'All filters' pill, subcategory cards, product tiles that all link to the sign-up dialog and a sign-up wall at the bottom.",
    "Brand storefront": "/brand/b_d72c56fe — a public brand page (54 Celsius): cover photo, circular fs-avatar, 'Top Shop' and rating badges, the section tab row, product tiles and an 'About' card; every buy path leads to the sign-up wall.",
    "Suppliers listings": "The SEO /suppliers/* listings (the candles subcategory and the /suppliers/All Brands A-Z): breadcrumb, 'Wholesale … suppliers' masthead and rows of brand cards — intermittently gated by the Cloudflare edge challenge.",
    "Marketing pages": "The signed-out marketing surface — /how-faire-works, /about, /news, /careers, /large-retailers, /point-of-sale/about, /markets, /affiliates: serif mastheads, CTAs and content cards.",
    "Brand application (/apply)": "The /apply brand-onboarding form measured at rest: name/e-mail/phone/password fields, the +1 country-code prefix, show-password icon, terms and marketing fs-checkbox inputs and the 'Next' submit — focused and typed into then cleared, never submitted.",
    "Sign-in dialog": "The 'Sign in to Faire' fs-modal mounted by ?signIn=1 over the home page — e-mail and password fields, the dark Sign in submit, Google/Apple SSO buttons, a sign-up link and the close icon; measured at rest, never submitted.",
    "Sign-up dialog": "The 'Unlock wholesale pricing' fs-modal mounted by ?signUp=1 — the business-e-mail field, 'Sign up for free' submit, Google/Apple SSO and a sign-in link; measured at rest, never submitted. The same dialog mounts when a product tile is clicked.",
    "Help center": "/support — the help-center masthead, the 'Search retailer guides' field and topic links.",
    "Mobile (390 wide)": "The phone surface at 390 wide: the top bar with Menu button and search icon, the nav drawer the Menu button opens, the search overlay the magnifier opens and the hero.",
    "Footer": "The page footer: the brand promise line in the serif face, sitemap columns, locale/social links and the legal row.",
}

SHOTS = [
    ("home", "Home", "/"),
    ("category-home-decor", "Category teaser (Home decor)", "/category/Home Decor"),
    ("category-new-products", "Category teaser (New products)", "/category/New Products"),
    ("brand", "Brand storefront (54 Celsius)", "/brand/b_d72c56fe"),
    ("suppliers-candles", "Suppliers listing (Candles)", "/suppliers/Home Decor/subcategory/Candles & Holders/Candles"),
    ("suppliers-all", "Suppliers A-Z", "/suppliers/All Brands/brand-value/women-owned"),
    ("how-faire-works", "How Faire works", "/how-faire-works"),
    ("about", "About", "/about"),
    ("news", "Newsroom", "/news"),
    ("careers", "Careers", "/careers"),
    ("large-retailers", "Large retailers", "/large-retailers"),
    ("point-of-sale", "Point of sale", "/point-of-sale/about"),
    ("markets", "Faire Markets", "/markets"),
    ("support", "Help center", "/support"),
    ("affiliates", "Affiliates", "/affiliates"),
    ("apply", "Brand application", "/apply"),
    ("signin", "Sign-in dialog", "/?signIn=1"),
    ("signup", "Sign-up dialog", "/?signUp=1"),
    ("notfound", "404", "/pagenotfound"),
    ("tos", "Terms of service", "/tos"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "/"),
    ("mobile-category-home-decor", "Category teaser, phone", "/category/Home Decor"),
    ("mobile-apply", "Brand application, phone", "/apply"),
    ("mobile-signin", "Sign-in dialog, phone", "/?signIn=1"),
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

W("# Faire components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from faire.com on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, registered, bought or submitted; the application and auth forms were measured and typed into then cleared, never sent; every link and CTA was measured, never followed — product tiles open the sign-up dialog, which is the deepest public surface.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [patterns.md](patterns.md).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Graphik_fix 14/20 400, #333333`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the page painted at capture — `light` on every surface here: faire.com paints a single light theme signed out (no theme attribute, no user toggle, and the probe's .dark pass resolves identically to :root). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).")
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
    ("OneTrust consent layer", "every page", "the consent SDK mounts a banner or the Privacy Preference Center; it is hidden with display:none, never answered — no accept/reject was clicked", "hidden before every shot and reading"),
    ("Cloudflare edge challenge", "fresh clients, some routes", "an intermittent Turnstile 'Just a moment…' interstitial; waited out and retried on a fresh context, never solved or clicked", "category/suppliers/brand routes intermittently degrade; the states it ate are listed in Gaps"),
    ("All categories menu", "home page header", "the 'All categories' button's own toggle — pointer click, keyboard Enter as fallback", "[home-light-categories-menu](screenshots/home-light-categories-menu.png), [all-categories-btn](#all-categories-button), [categories-panel](#categories-menu-panel)"),
    ("Mobile nav drawer", "home page, phone width", "the Menu button's own toggle", "[mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-drawer](#mobile-nav-drawer)"),
    ("Mobile search overlay", "home page, phone width", "the unlabelled magnifier button's own toggle", "[m-search](#mobile-search-field)"),
    ("Sign-in dialog", "/?signIn=1", "mounted by the query parameter; fields typed into then cleared — nothing sent", "[signin-light-default](screenshots/signin-light-default.png), [signin-dialog](#sign-in-dialog), [signin-email](#email-field-sign-in)"),
    ("Sign-up dialog", "/?signUp=1 (also every product tile)", "mounted by the query parameter; fields typed into then cleared — nothing sent", "[signup-light-default](screenshots/signup-light-default.png), [signup-dialog](#sign-up-dialog), [signup-email](#business-email-field)"),
    ("Application fields", "/apply", "typed into then cleared — nothing sent", "[field-firstname](#first-name-field), [field-email](#email-field), [field-phone](#phone-field), [field-password](#password-field)"),
    ("Signed-in marketplace", "a Faire account", "every post-dialog surface — search results, product detail, cart, checkout, account — needs an account", "boundary; see Gaps"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

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
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0
    # A ring painted on a child layer instead of the wrapper: offer buttons
    # draw 1px dotted outlines on their inner anchor while the wrapper's own
    # outline stays none. Those states must count as ringed too.
    child_ring = next((n["outline"] for n in st.get("paint", []) if n.get("outline")), None)
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
for k in ["categories-panel", "subcat-card", "brand-card", "news-card", "signin-dialog", "signup-dialog", "m-drawer"]:
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
        desc = (c.get("desc") or "").strip()
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Faire wordmark, the header glyphs, social icons, the product badges) are the product's artwork. Declared under layoutGaps in the catalog entry.")
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
W("### The signed-in marketplace")
W()
W("Faire's product is the marketplace: every surface past the sign-up/sign-in dialogs — search results, product detail, cart, checkout, orders, the retailer and brand dashboards — needs an account and was never reached. Product tiles link to `?signUp=product`, which mounts the sign-up dialog: the deepest public surface, and it was measured as a form, never submitted. The /brand-portal route redirects to sign-in.")
W()
W("### Pages")
W()
W("- **The account.** Every post-sign-in surface was never reached; both auth dialogs were measured at rest and never submitted; Google/Apple SSO was never followed.")
W("- **Forms.** The /apply brand application was measured at rest and typed into then cleared — 'Next' was never pressed; what the second step or a submission returns is unverified.")
W("- **Cloudflare.** The edge intermittently serves a Turnstile interstitial, worst on the category/suppliers/brand routes; those components were captured across several passes and a few entries below are marked missing or carry `recaptureMissed` runs — the routes it ate during a pass are documented, not patched over.")
W("- **Blog.** The header's Blog link leaves faire.com for the blog subdomain; not captured.")
W("- **Newsroom articles** are not followed; /news is covered by the index and its cards.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.")
W("- **Dialog fields' validation states** are unseen — validation needs a submit, which was never performed.")
W("- **signup-apple** is absent from the sign-up dialog as rendered to this client (Google only); `brand-tile`, `sup-h1` and `wall-submit` stayed missing/unmeasured because the routes degraded during every later pass.")
W()
W("### Themes")
W()
W('faire.com has no user theme toggle, no theme attribute and no `prefers-color-scheme` switch: one light theme signed out. The vars probe resolved every custom property a second time under a `dark` class nothing on the site sets and the values are identical — the only "dark" contexts are inverse surfaces inside the light page (the dark marketing band, controls over hero media), which the declared `.fs-mode-on-surface` scope re-themes; its resolved values sit under `light.color.onSurface.*`.')
W()
W("### Fonts")
W()
W("- **Graphik_fix** (the UI sans — body, controls, fields), **Nantes_fix** (the marketing display serif — mastheads, the footer promise line) are the declared faces; **GT Canon** (category mastheads, dialog titles), **GT Standard** (large CTAs) and **GT Standard M** (mono accents) appear in measured styles. All are served woff2 faces from cdn.faire.com; the style guide falls back to system sans.")
W()
W("### Screenshots")
W()
W("- The product photography, brand imagery and video frames in the screenshots are the site's published content.")
W("- The suppliers-candles default screenshot caught the skeleton loader; the full shot and the measurements show the real listing.")
W("- Full-page shots are bounded at eight chunks; the bounds each page hit are in the `.png.capture.json` sidecars.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Article copy, product names, brand names and prices are the site's content; only frames and components were measured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
