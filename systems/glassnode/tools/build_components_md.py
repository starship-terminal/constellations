#!/usr/bin/env python3
"""Build components.md for the Glassnode design reference.

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


# A measured colour is labelled by the token whose value matches. The lookup
# runs set by set — the light theme's resolved roles first (the marketing
# palette lives there: theme.fg.default black, theme.bg white), then core,
# whose component.* tree holds the product-shell fallbacks — so a white
# surface is named theme.bg, not whichever component token happens to share
# the value. PRIMARY pins the roles a label should prefer when several tokens
# share one colour (badge.fg and fg.default are both #000000; fg is the role
# the text is painted in). Names carry their set prefix (light.theme.bg) so a
# label always names a real path in tokens.json.
PRIMARY = {"theme.ink.default", "theme.ink.inverse", "theme.border.default", "theme.action.primary", "theme.surface.raised"}
BY_COLOR = {}
for n, t in sorted(flat(T["light"], "light."), key=lambda it: (it[0].split(".", 1)[1] not in PRIMARY, it[0])):
    if t["$type"] == "color":
        BY_COLOR.setdefault(t["$value"], n)
for n, t in flat(T["core"], "core."):
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

PAGE_NAME = {"home": "home", "vector": "pricing/vector", "contact": "contact",
             "studio-pricing": "studio /pricing", "auth-login": "auth login",
             "research": "research", "research-article": "research article",
             "docs": "docs landing", "docs-metric": "docs metric catalog",
             "tokenization": "tokenization registry", "mobile": "home"}

GROUP_INTRO = {
    "Marketing site chrome": "The header on every glassnode.com page: the wordmark, the 'Products' dropdown trigger (hover opens it), Pricing, Data, About and the 'Launch Studio' CTA.",
    "Marketing home": "The home hero and sections: the 'Pioneering digital asset market intelligence' masthead, the metric comparison controls and display section headings.",
    "Vector pricing page": "/pricing/vector — the Bitcoin Vector product page: the quarterly/monthly billing select, the plan card, 'Download sample' and the FAQ accordion.",
    "Marketing contact page": "/contact — the 'How can we connect' category cards and the research subscribe band.",
    "Studio shell (signed out)": "studio.glassnode.com — the React product shell on the declared --gds-* layer: the navbar (Home/Dashboards/Charts/Market Compass/Alpha Lab/Research/Tokenization, search, 'Log in', 'Sign up'), the /pricing plan grid with its metric-catalog expanders and FAQ. Signed-out only; the declared dark-theme layer has no public control.",
    "Auth0 universal login": "auth.glassnode.com/u/login — the Auth0 card the studio 'Log in' navigates to (username/password, 'Continue', 'Continue with Google', 'Reset password', 'Sign up'). Reached through the real button; the volatile ?state= is never recorded; the form was never submitted.",
    "Research publication (Ghost)": "research.glassnode.com — the Ghost publication: the tag nav, the 'Switch to dark mode' toggle (measured at rest), article cards, the subscribe field and a published article's prose.",
    "Docs site (GitBook)": "docs.glassnode.com — the GitBook docs site (the platform's own token layer): the header, Website/Studio/Insights links, the 'Switch to dark theme' button (never switched here), search, sidebar links and the metric catalog.",
    "Tokenization registry": "tokenization.glassnode.com — the dark-by-default registry app: the nav with live asset/issuer/product/derivative counts, search, the 'Switch to light theme' button and 'Request access'.",
    "Mobile (390 wide)": "The phone surface at 390 wide: the header with the hamburger, the nav overlay, the hero and the newsletter field.",
    "Footer": "The marketing page footer: sitemap columns, the 'Enter your email' subscribe field with 'Send me free research', and the 'Privacy settings' consent control.",
}

SHOTS = [
    ("home", "Home", "glassnode.com/"),
    ("products-studio", "Studio (product page)", "glassnode.com/products/studio"),
    ("products-data", "Data (product page)", "glassnode.com/products/data"),
    ("products-research", "Research services", "glassnode.com/products/research"),
    ("products-market-compass", "Market Compass", "glassnode.com/products/studio/market-compass"),
    ("products-alpha-lab", "Alpha Lab", "glassnode.com/products/studio/alpha-lab"),
    ("pricing-vector", "Bitcoin Vector pricing", "glassnode.com/pricing/vector"),
    ("about", "About", "glassnode.com/about"),
    ("contact", "Contact", "glassnode.com/contact"),
    ("customer-stories", "Customer stories", "glassnode.com/customer-stories"),
    ("events", "Events", "glassnode.com/events"),
    ("solutions-trading", "For trading and investing", "glassnode.com/solutions/trading-and-investing"),
    ("solutions-content", "For content creation", "glassnode.com/solutions/crypto-content-creation"),
    ("studio-pricing", "Studio pricing", "studio.glassnode.com/pricing"),
    ("studio-charts", "Studio charts", "studio.glassnode.com/charts"),
    ("studio-dashboards", "Studio dashboards", "studio.glassnode.com/dashboards"),
    ("studio-market-compass", "Studio Market Compass gate", "studio.glassnode.com/market-compass"),
    ("studio-get-listed", "Studio get-listed", "studio.glassnode.com/get-listed"),
    ("studio-contact", "Studio contact", "studio.glassnode.com/contact"),
    ("auth-login", "Auth0 login", "auth.glassnode.com/u/login"),
    ("research-home", "Research", "research.glassnode.com/"),
    ("research-article", "Research article", "research.glassnode.com/ (first index article)"),
    ("docs-home", "Docs overview", "docs.glassnode.com/"),
    ("docs-metric", "Docs metric catalog", "docs.glassnode.com/data/metric-catalog"),
    ("tokenization", "Tokenization registry", "tokenization.glassnode.com/"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "glassnode.com/"),
    ("mobile-studio-pricing", "Studio pricing, phone", "studio.glassnode.com/pricing"),
    ("mobile-research-home", "Research, phone", "research.glassnode.com/"),
    ("mobile-docs-home", "Docs, phone", "docs.glassnode.com/"),
    ("mobile-tokenization", "Tokenization, phone", "tokenization.glassnode.com/"),
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
n_states = sum(len(c.get("states", {})) for c in C.values())
icons = []

W("# Glassnode components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from glassnode.com and its public subdomains on {J['_meta']['read']}, signed out, in headed Chromium under Xvfb at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the newsletter and Auth0 username fields were typed into then cleared, never submitted; every link and CTA was measured, never followed.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [patterns.md](patterns.md).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 16/20.8 400, #000000`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the page painted at capture: `light` for the marketing pages, the studio shell, research and docs; `dark` for the tokenization registry (its painted default). Theme-switched states keep the page's painted theme and take a `theme-*` state name: `*-light-theme-dark.png` is the Ghost/GitBook dark surface reached by the site's own theme control, and `tokenization-dark-theme-light.png` the registry's light surface. The studio's `html[data-theme='dark-theme']` layer is declared but has no public control, so no screenshot paints it — its values are declared-not-painted tokens only. The Auth0 login is reached by the studio shell's real 'Log in' button; its landing URL's volatile `?state=` is sanitized to origin+path in every sidecar. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages bounded at eight chunks with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x) for default shots and 390 wide for stitched `-full` tiles.")
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
    ("Products dropdown", "every marketing page header", "the 'Products' trigger (a local UI toggle — a hover opens it; click/Enter the fallback)", "[nav-dropdown-btn](#nav-dropdown-trigger), [nav-menu-item](#dropdown-item)"),
    ("Mobile nav overlay", "home page, phone width", "the header hamburger's own toggle", "[m-drawer](#mobile-nav-overlay)"),
    ("Research theme toggle", "research pages", "the '.gh-theme-toggle' button — measured at rest; the dark surface was captured as the theme-dark screenshots rather than by holding the toggle", "[res-theme-toggle](#theme-toggle), [research-home-light-theme-dark](screenshots/research-home-light-theme-dark.png)"),
    ("Docs theme buttons", "docs pages", "'Switch to light/dark theme' — measured at rest; the dark surface is the theme-dark screenshots", "[docs-theme-btn](#theme-button), [docs-home-light-theme-dark](screenshots/docs-home-light-theme-dark.png)"),
    ("Tokenization theme button", "the registry", "'Switch to light theme' — measured at rest on the painted dark surface; the light surface is the theme-light screenshot", "[tok-theme-btn](#theme-button-2), [tokenization-dark-theme-light](screenshots/tokenization-dark-theme-light.png)"),
    ("Vector FAQ", "/pricing/vector", "the question rows are local toggles; 'Download sample' and the billing select were measured, never pressed or changed", "[vec-faq](#faq-accordion), [vec-download-btn](#download-sample-button), [vec-billing-select](#billing-cycle-select)"),
    ("Studio catalog expanders", "studio /pricing", "'Show N more metrics' rows are local toggles; the pricing FAQ rows likewise", "[st-metrics-expander](#metric-catalog-expander), [st-faq](#faq-accordion-2)"),
    ("Newsletter + username fields", "the marketing footer, /contact, research, the Auth0 card", "typed into then cleared — nothing sent; the Auth0 form was never submitted", "[newsletter-field](#newsletter-field), [auth-email](#username-field)"),
    ("Log in / Sign up", "the studio navbar", "'Log in' navigates to the Auth0 universal login — captured on auth-login; 'Sign up' and every CTA were measured, never followed", "[st-login-btn](#log-in-button), [auth-card](#login-card)"),
    ("Signed-in product", "a Glassnode account", "the charting workbench, saved dashboards, API keys and billing need an account", "boundary; see Gaps"),
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
    st = c.get("states", {}).get("focus-visible")
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
    for st in c.get("states", {}).values():
        if "style" not in st or st.get("via") == "focus failed":  # a failed focus is the resting element: not a tally
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
for k in ["st-plan-card", "auth-card", "res-post-card", "footer", "m-drawer", "contact-category"]:
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
        where = PAGE_NAME.get(c.get("page", ""), c.get("page", ""))
        W(f"{desc + ' ' if desc else ''}Read as `{k}` on the {where} page{' at 390 wide' if g.startswith('Mobile') else ''}.")
        W()
        if "states" not in c:  # a page marker (e.g. __auth): provenance, not a measured component
            continue
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Glassnode mark, the nav glyphs, social glyphs and partner logos) are the product's artwork. Declared under layoutGaps in the catalog entry.")
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
W("Glassnode's product is Studio: the charting workbench, saved dashboards, the metric workbench editor, alerts, API keys and billing all sit after 'Log in' on auth.glassnode.com and were never reached. The Auth0 login card is the only account surface a signed-out visitor sees, and it was measured as a form, never submitted. studio.glassnode.com /login, /sign-up and /signup are in-app Page Not Found routes — the only real login is the Auth0 page the navbar hands to.")
W()
W("### Pages")
W()
W("- **The account.** Studio's workbench, saved dashboards, alerts, API keys, billing and every post-login surface were never reached; the Auth0 card was measured as a form and never submitted.")
W("- **Forms.** The newsletter fields and the Auth0 username field were typed into then cleared — nothing was sent; what a submission returns is unverified.")
W("- **Studio charts and dashboards** are captured as screenshots of their public signed-out views (/charts and /dashboards redirect to public BTC/asset views); deeper interactions (metric picker, time ranges) sit behind the account wall.")
W("- **The Market Compass page** on studio.glassnode.com is an upgrade gate signed out — its content was captured as shown to an anonymous visitor.")
W("- **Research articles** are exemplar-level: the index and the current first article were captured; sibling articles share the templates, unmeasured.")
W("- **Marketing product pages, solutions, events and customer stories** were captured as index/landing pages; subpages were not.")
W()
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.")
W("- **The studio dark theme** is declared (html[data-theme=\"dark-theme\"] with --gds-*/--ant-* redeclarations) but no public control reaches it signed out — it is captured as declared-not-painted tokens, never as a screenshot or measured state.")
W("- **Theme toggles** (research, docs, tokenization) were measured at rest; the switched surfaces are screenshot evidence, not measured component states.")
W()
W()
W("### Themes")
W()
W("The marketing site paints the `:root` light layer only — dark in-page sections, no global theme or control. The studio shell paints light signed out and declares a `html[data-theme=\"dark-theme\"]` layer no public control reaches (declared-not-painted tokens). research.glassnode.com and docs.glassnode.com each carry a real theme control whose dark surfaces are the `theme-dark` screenshots and the dark.research.* token roles; tokenization.glassnode.com paints dark by default and light via its button (`theme-light` screenshot, light.tokenization.* roles).")
W()
W("### Fonts")
W()
W("- **Inter/Inter Variable** carries the studio shell, the research body and the registry; **fraktion** is the marketing display face (the marketing --font-family var is a system stack — the webfonts paint per-module); **JetBrains Mono** is the registry mono; **Roboto/IBM Plex Mono** are the GitBook docs fonts — all self-hosted. The style guide falls back to system fonts.")
W()
W("### Screenshots")
W()
W("- The product imagery, partner logos and photography in the screenshots are the product's published content; the Auth0 login shot's landing URL is sanitized (the volatile ?state= is never kept).")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Marketing copy, plan prices, report text, issuer/asset names and customer names are the product's content; only frames and components were measured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
