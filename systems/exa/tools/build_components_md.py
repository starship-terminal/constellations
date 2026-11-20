#!/usr/bin/env python3
"""Build components.md for the Exa design reference.

Reads raw/components-computed.json (every component and state, measured),
tokens.json and screenshots/, and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the palette token whose
value matches, the font family is named once per value, and a state row shows only what differs
from the first state. Adapted from the Equals package's builder, which read
the same JSON.

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

PAGE_NAME = {"home": "marketing home", "pricing": "pricing", "product": "products/search",
             "signin": "auth.exa.ai sign-in", "docs": "docs", "docsdark": "docs dark",
             "mobile": "marketing home"}

GROUP_INTRO = {
    "Marketing chrome": "The exa.ai header: the 55px bar under the Exa 3.0 announcement strip, with the exa wordmark, the Products/Solutions/Resources hover menus, Docs, Pricing, Sign in, Contact sales and the black Sign-up pill.",
    "Home hero and search demo": "The 'The world's data for AI agents' hero and the live search-demo widget below it: the Arizona display, the 'Try API for free' pill, the Search/Agent mode toggle, the LATENCY and CATEGORY pills, the OUTPUT tabs, the blue Run-preview arrow and the output panel's signed-out state.",
    "Pricing": "The /pricing page: the heading, the use-case scenario pills and the plan cards with their Get-started actions.",
    "Product pages": "The /products/search page: its heading, code sample and call to action.",
    "Sign in (auth.exa.ai)": "The signed-out login card dashboard.exa.ai redirects to on auth.exa.ai: 'Start building with Exa', the Continue-with-Google and Continue-with-email buttons, the e-mail field, the SSO link and the code sample — measured, never submitted.",
    "Docs (exa.ai/docs) (light)": "The Mintlify docs shell in light mode: the sidebar, search pill, theme button, nav items, page heading, body copy, links, code blocks, language tabs, the 'Add Exa to your agent' banner and the assistant field.",
    "Docs (exa.ai/docs) (dark)": "The same docs shell under html.dark: the #0b0b10 canvas, flipped borders and code surfaces, the same #1840ed primary.",
    "Footer": "The marketing footer: link columns, status and social marks.",
    "Mobile (390 wide)": "The phone surface at 390 wide: the header, the hamburger and its drawer, the hero display and the demo field.",
}

SHOTS = [
    ("home-light", "Home (marketing)", "exa.ai/"),
    ("pricing-light", "Pricing", "exa.ai/pricing"),
    ("product-light", "Search API product", "exa.ai/products/search"),
    ("about-light", "About", "exa.ai/about"),
    ("blog-light", "Blog", "exa.ai/blog"),
    ("demos-light", "Demos", "exa.ai/demos"),
    ("evals-light", "Evals", "exa.ai/evals"),
    ("brand-light", "Brand", "exa.ai/brand"),
    ("customers-light", "Customers", "exa.ai/customers"),
    ("versus-light", "Versus", "exa.ai/versus"),
    ("signin-light", "Sign in", "dashboard.exa.ai/ → auth.exa.ai"),
    ("websets-light", "Websets", "websets.exa.ai/websets"),
    ("docs-light", "Docs (light)", "exa.ai/docs"),
    ("docs-ref-light", "Docs: quickstart", "exa.ai/docs/quickstart"),
    ("docs-dark-dark", "Docs (dark)", "exa.ai/docs, dark"),
]
MOBILE = [
    ("mobile-home-light", "Home, phone", "exa.ai/"),
    ("mobile-pricing-light", "Pricing, phone", "exa.ai/pricing"),
    ("mobile-signin-light", "Sign-in, phone", "dashboard.exa.ai/ → auth.exa.ai"),
    ("mobile-docs-dark-dark", "Docs dark, phone", "exa.ai/docs, dark"),
]

L = []


def W(s=""):
    L.append(s)


shots = sorted(p.name for p in Path("screenshots").glob("*.png"))


def links(prefix):
    """prefix is the full '{page}-{theme}' stem (screenshots are {page}-{theme}-{state}.png)."""
    out = []
    for f in shots:
        m = re.fullmatch(re.escape(prefix) + r"-(.+)\.png", f)
        if m:
            out.append(f"[{m.group(1)}](screenshots/{f})")
    return ", ".join(out)


n_crops = len(list(Path("components/crops").glob("*.png")))
n_states = sum(len(c["states"]) for c in C.values())
icons_idx = Path("icons/INDEX.tsv")
icons = [r.split("\t") for r in icons_idx.read_text().strip().split("\n")[1:]] if icons_idx.exists() else []

W("# Exa components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from exa.ai, auth.exa.ai and exa.ai/docs on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the sign-in e-mail and the demo query fields were focused and filled for measurement, then cleared, and never sent; the demo's Run-preview arrow, every Get-started/Sign-up action and the login buttons were never pressed, and the demo widget's pills were toggled only as local preview configuration. The dashboard, API keys and playground behind login were never reached.")
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
W("Screenshots are named `{page}-{theme}-{state}.png`: marketing and sign-in surfaces paint `light`; the docs' dark-mode pages are the `*-dark-dark-*` files. Desktop shots are 1440 x 900 at DPR 2 (256-colour PNGs); `-full` shots are whole pages, chunked and stitched; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).")
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
    ("Products mega-menu", "exa.ai header", "a real pointer hover on the 'Products' trigger — a local open, its links never followed", "[home-light-menu](screenshots/home-light-menu.png), [mkt-menu](#products-mega-menu), [mkt-menu-item](#mega-menu-link)"),
    ("Demo widget pills", "exa.ai home", "the LATENCY/CATEGORY/OUTPUT pills' own toggles — they re-configure the preview, never fire it", "[home-light-demo-tabs](screenshots/home-light-demo-tabs.png), [demo-pill](#latency-pill), [demo-category](#category-pill), [demo-output-tab](#output-tab)"),
    ("Pricing use-case pills", "exa.ai/pricing", "the scenario pill's own toggle", "[pricing-light-usecase-chatbots](screenshots/pricing-light-usecase-chatbots.png), [pricing-pill](#use-case-pill)"),
    ("Mobile nav drawer", "home, phone width", "the hamburger's own toggle", "[mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-drawer](#mobile-nav-drawer)"),
    ("Input fields", "sign-in card, demo and assistant", "focused and filled with test text, then cleared — never submitted or sent", "[auth-email](#email-field), [demo-textarea](#demo-query-field), [docs-assistant](#assistant-field)"),
    ("Docs theme", "exa.ai/docs", "html.dark painted by the capture context (prefers-color-scheme), never through the theme menu", "the `d-docs-*` entries and `docs-dark` shots"),
    ("Demo request", "exa.ai home", "the Run-preview arrow would fire a real search; the widget could not verify the headless browser either way", "boundary; [demo-output](#demo-output-panel) shows its honest resting state"),
    ("Signed-in product", "dashboard.exa.ai / post-login", "every post-login surface needs an account", "boundary; see Gaps"),
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
for k in ["plan-card", "mkt-menu", "auth-card", "demo-widget", "docs-cta", "m-drawer", "docs-sidebar"]:
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
        # a skipped record (newer captures) has no style; an older one kept the element at rest
        failed = [s for s, v in c["states"].items() if v.get("skipped") or v.get("via") == "focus failed"]
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
if icons:
    W()
    W("## Icons")
    W()
    W(f"{len(icons)} SVGs were lifted from the pages into [icons/](icons), named by role where a label gave one, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. The set holds the chevrons and hamburger strokes, the mega-menu product glyphs, the demo controls (search, run-preview, clear-query, show-code-view), the use-case pill glyphs and the social/integration marks (parallel, perplexity, brave…). The SVGs are Exa's property, kept for reference only.")
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
W("The real Exa product lives behind login — the dashboard, API keys, the playground and websets all need an account and were never reached. `dashboard.exa.ai` was measured only as the signed-out `auth.exa.ai` card it redirects to; the form was never submitted. The home page's search demo widget is the closest public view of the product: its pills and query field are real controls, but firing a request needs the Run-preview arrow (never pressed) and the widget could not verify the headless browser anyway — its output panel reads 'We couldn't verify your browser … Sign in to continue', the widget's own honest signed-out state.")
W()
W("### Pages")
W()
W("- **The account and API flow.** Every post-login surface was never reached; the sign-in form and the demo/assistant fields were measured as fields and never submitted, and Get-started/Sign-up/API-key actions were never followed.")
W("- **websets.exa.ai** rate-limits headless browsers (HTTP 429); the `websets-light-default` shot, when present, is its block page, kept as the boundary evidence rather than retried.")
W("- **Subpages of /products and /use-cases** (contents, agent, deep, monitors, snapshot, library, the use-case detail pages) share the marketing chrome; a subset beyond the measured pass was screenshotted where listed above.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active), so a state a script adds on real mousedown (if any) is missing.")
W("- **Disabled, error and loading states** were not seen on the public surface.")
W("- **The demo widget is live** — its query field was typed into and restored, its pills toggled as preview configuration; the request itself was never fired.")
W("- **The announcement strip's dismiss button** was never pressed; the strip stays in the shots.")
W()
W("### Themes")
W()
W("Three distinct public surfaces were captured: the marketing site (light only — its sole prefers-color-scheme:dark rule is one utility class, not a theme), the auth.exa.ai sign-in card (light only), and the Mintlify docs, which genuinely switch on `html.dark`. tokens.json keeps real light and dark sets; the dark set holds docs roles only, since marketing and sign-in paint no dark theme.")
W()
W("### Fonts")
W()
W("- **ABCDiatype** (marketing body/UI), **Arizona**/**ABC Arizona Flare** (marketing display, auth display), **SuisseIntlMono** (marketing mono), **ABC Diatype Unlicensed Trial** and **Geist Mono** (auth card), **Inter** and **Paper Mono** (docs) are the served faces — the brand faces are trial-licensed ABC fonts served from the sites' CDNs; the style guide falls back to system sans.")
W()
W("### Screenshots")
W()
W("- The exa wordmark, integration logos, photography and page artwork in the screenshots are the product's published content.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files, never off a screenshot.")
W()
W("### Content left out")
W()
W("- Customer names, quotes, eval copy, blog posts and doc page content are the product's published text; only frames and components were measured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
