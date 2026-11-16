#!/usr/bin/env python3
"""Build components.md for the Front design reference.

Reads raw/components-computed.json (every component and state, measured),
tokens.json, screenshots/ and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the
palette token whose value matches, the font family is named once per value,
and a state row shows only what differs from the first state. Adapted from
the Coursera kit's builder via the Deezer and Fingerprint packages, which
read markdown/JSON; this one reads the JSON directly.

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
# runs set by set — the marketing theme roles first (a white surface is
# light.surface.l0, a plum field violet.surface.l0), then the app shell's
# resolved --color-* roles, then core (the marketing palette, the app
# primitives and the Froyo ramps) — so a label names the role the paint came
# from rather than whichever ramp step shares the value. PRIMARY pins the
# roles a label should prefer when several tokens share one colour. Names
# carry their set prefix (violet.surface.l0, app.color.bg.fill.brand) so a
# label always names a real path in tokens.json.
PRIMARY = {"light.text.primary", "light.text.secondary", "violet.text.primary", "violet.surface.l0",
           "light.surface.l0", "app.color.bg.base.default", "app.color.text.primary", "app.color.bg.fill.brand.default"}
BY_COLOR = {}
for setname in ("light", "violet", "gray", "app", "dark", "companion", "companionDark", "help", "core"):
    for n, t in sorted(flat(T[setname], setname + "."), key=lambda it: (it[0].split(".", 1)[1] not in PRIMARY, it[0])):
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

PAGE_NAME = {"home": "home", "pricing": "pricing", "product": "product",
             "request-demo": "request-demo", "signup": "marketing signup",
             "signin": "signin", "signin-dark": "signin (dark)", "signup-app": "product signup",
             "forgot": "forgot-password", "help": "help centre home",
             "help-article": "help article", "dev": "developer docs", "dev-ref": "developer reference",
             "mobile": "home"}

GROUP_INTRO = {
    "Site chrome": "The header on every marketing page: the Front wordmark, the Product/Solutions/Resources mega-menu triggers, AI, Customers and Pricing links, Sign in, the bordered 'Request a demo' and the 'Try for free' action; the Product mega menu opens a full-width panel under the bar. The Qualified 'Quinn' vendor widget pins bottom-right — measured at rest, never opened.",
    "Home": "The home hero on the plum [data-theme=theme-dark-violet] field: the display1 masthead 'All your teams. All your AI agents. One place to …', the sub copy, the violet primary 'Try for free' and secondary 'Request a demo', and the themed sections below (theme-white, theme-gray).",
    "Pricing": "The /pricing surface: 'PRICING PLANS' kicker, the 'Build the best CX' display, the 'Billed Annually / SAVE 24%' switch that repaints the per-seat prices (a local UI toggle), the plan cards with their 'Try for Free' actions, 'Talk to sales', and the FAQ disclosures.",
    "Demo and signup forms": "The /request-demo and marketing /signup forms — HubSpot-powered fields and their submit buttons. Fields were typed into then cleared; the submits were measured in every state, never pressed.",
    "Auth shell (app.frontapp.com)": "app.frontapp.com /signin, /signup and /forgot-password — the product SPA's auth cards on the real --color-* token layer (Indivisible, the 'Froyo' design system), painted light and under the shell's own [data-theme=dark] (the front-theme-preference localStorage key plus prefers-color-scheme). Fields were typed into then cleared; Continue, the SSO buttons and the submits were measured, never pressed.",
    "Help centre (help.front.com)": "help.front.com — Front's own Knowledge Base product serving the help centre: its own header, the search field (typed into then cleared, never submitted), category cards and article pages on the --article-*/--gray-shade* :root layer. Front embeds its Companion messenger here (companion.frontapp.com — the Froyo token sheet's home).",
    "Developer portal (dev.frontapp.com)": "dev.frontapp.com — the developer documentation on the ReadMe vendor platform (readme.io) skinned to Front: its header, search trigger, sidebar tree and code blocks, plus the same Companion embed. Vendor platform; kept as measured evidence, not a token set.",
    "Mobile (390 wide)": "The phone surface at 390 wide: the header with the burger ('Open menu'), the full-viewport nav overlay, the hero and the CTAs.",
    "Footer": "The page footer: 'The AI customer operations platform.', the link columns, social icons, certifications and legal row.",
}

SHOTS = [
    ("home", "Home", "/"),
    ("pricing", "Pricing", "/pricing"),
    ("product", "Product", "/product"),
    ("product-omnichannel", "Omnichannel inbox", "/product/omnichannel-support-inbox"),
    ("product-ai", "Front AI", "/product/ai"),
    ("customer-service", "Customer service", "/customer-service"),
    ("customer-stories", "Customer stories", "/customer-stories"),
    ("story", "A customer story", "/customer-stories/uber-freight"),
    ("integrations", "Integrations", "/integrations"),
    ("compare", "Front vs Intercom", "/compare/front-vs-intercom"),
    ("industry", "B2B tech industry", "/industries/b2b-tech"),
    ("team", "Teams: customer service", "/teams/customer-service-support"),
    ("resources", "Resources", "/resources"),
    ("blog", "Blog", "/blog"),
    ("article", "A blog article", "/blog/customer-service-automation-ai"),
    ("glossary", "Glossary", "/glossary"),
    ("about", "About", "/about"),
    ("reviews", "Reviews", "/reviews"),
    ("download", "Download", "/download"),
    ("security", "Security", "/security"),
    ("request-demo", "Request a demo", "/request-demo"),
    ("signup", "Marketing signup", "/signup"),
    ("whats-new", "What's new", "/whats-new"),
    ("signin", "Sign in (app shell)", "app.frontapp.com/signin"),
    ("signindark", "Sign in, dark theme", "app.frontapp.com/signin"),
    ("signup-app", "Sign up (app shell)", "app.frontapp.com/signup"),
    ("signupappdark", "Sign up, dark", "app.frontapp.com/signup"),
    ("forgot", "Forgot password", "app.frontapp.com/forgot-password"),
    ("forgotdark", "Forgot password, dark", "app.frontapp.com/forgot-password"),
    ("help", "Help centre", "help.front.com/"),
    ("help-article", "A help article", "help.front.com/en/…"),
    ("help-contact", "Help: contact us", "help.front.com/en/contact-us"),
    ("dev", "Developer docs", "dev.frontapp.com/docs/welcome"),
    ("dev-ref", "API reference", "dev.frontapp.com/reference/getting-started"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "/"),
    ("mobile-pricing", "Pricing, phone", "/pricing"),
    ("mobile-signin", "Sign in, phone", "app.frontapp.com/signin"),
    ("mobile-signindark", "Sign in, phone, dark", "app.frontapp.com/signin"),
    ("mobile-help", "Help centre, phone", "help.front.com/"),
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

W("# Front components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from front.com, app.frontapp.com, help.front.com and dev.frontapp.com on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, booked, created or submitted; the demo, signup, signin, help-search and reset forms were never sent; every link, CTA, SSO button and submit was measured, never followed or pressed.")
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
W("Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the page painted at capture: `light` for every marketing, help and dev page — front.com themes its sections, not the page (the plum [data-theme=theme-dark-violet], theme-white and theme-gray blocks alternate down the same page), and neither the help centre nor the ReadMe portal offered a switch. The app shell does carry a real theme: `signindark-*`, `signupappdark-*`, `forgotdark-*` and `mobile-signindark-*` shots paint app.frontapp.com under its own [data-theme=\"dark\"] (the front-theme-preference localStorage key plus prefers-color-scheme — the product's switch, not an emulated paint). The OneTrust banner and the Qualified 'Quinn' widget are hidden in every shot except `home-light-widget.png`, which shows the vendor surface as shipped — never answered, never engaged. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages bounded at eight chunks with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x) for default shots and 390 wide for stitched `-full` tiles.")
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
    ("Product mega menu", "every page header", "clicked the 'Product' trigger (a local UI toggle; keyboard Enter is the fallback)", "[home-light-menu-product](screenshots/home-light-menu-product.png), [nav-panel](#mega-menu-panel), [nav-menu-item](#mega-menu-item)"),
    ("Solutions mega menu", "every page header", "the same activation on 'Solutions'", "[home-light-menu-solutions](screenshots/home-light-menu-solutions.png)"),
    ("Resources mega menu", "every page header", "the same activation on 'Resources'", "[home-light-menu-resources](screenshots/home-light-menu-resources.png)"),
    ("Mobile nav overlay", "home page, phone width", "the burger button's own toggle", "[m-drawer](#mobile-nav-overlay), [mobile-home-light-menu](screenshots/mobile-home-light-menu.png)"),
    ("Billing switch", "/pricing", "the 'Billed Annually' switch repaints the per-seat prices — a local UI toggle, toggled once each way", "[pricing-light-billed-monthly](screenshots/pricing-light-billed-monthly.png), [billing-toggle](#billing-switch)"),
    ("Pricing FAQ", "/pricing", "the 'What is a seat?' disclosure's own toggle", "[pricing-light-faq-open](screenshots/pricing-light-faq-open.png), [faq-item](#faq-disclosure), [faq-answer](#faq-answer)"),
    ("Quinn widget (vendor)", "marketing home", "auto-opens on load — shot once as shipped, never opened or typed into", "[home-light-widget](screenshots/home-light-widget.png), [quinn-launcher](#quinn-widget-vendor)"),
    ("Demo/signup/auth fields", "/request-demo, /signup, app /signin /signup /forgot-password, help search", "typed into then cleared — nothing sent", "[demo-email](#work-email-field), [app-email](#email-field), [help-search](#search-field)"),
    ("Auth buttons", "app /signin /signup /forgot-password", "the Continue/SSO/submit buttons were measured in every state, never pressed — nothing was submitted", "[app-continue](#continue-button), [app-sso](#sso-button)"),
    ("App dark theme", "app /signin /signup /forgot-password", "the shell's own switch: front-theme-preference= 'dark' plus prefers-color-scheme — html[data-theme=dark] painted", "[signindark-dark-default](screenshots/signindark-dark-default.png), appd-* components below"),
    ("Signed-in product", "a Front account", "the workspace — inbox, conversations, contacts, settings — needs an account", "boundary; see Gaps"),
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
for k in ["nav-panel", "plan-card", "footer", "app-panel", "appd-panel", "signup-panel", "forgot-panel", "help-card", "m-drawer"]:
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Front wordmark, the mega-menu product glyphs, the chevrons and social glyphs, partner logos) are the product's artwork. Declared under layoutGaps in the catalog entry.")
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
W("Front's product is the workspace: the shared inbox, conversations, contacts, rules, analytics and settings — everything past the auth wall on app.frontapp.com needs an account and was never reached. /signin, /signup and /forgot-password are the only product surfaces a signed-out visitor sees, and they were measured as forms, never submitted. The app's --color-* token layer is real evidence (it paints the auth shell); what it does on the inbox itself is uncaptured.")
W()
W("### Pages")
W()
W("- **The workspace.** Inbox, conversations, contacts, rules, analytics, settings and every post-login surface was never reached; the auth cards were measured as forms, never submitted, and the SSO buttons were never followed.")
W("- **Forms.** /request-demo, the marketing /signup, the auth shell's e-mail fields and the help-centre search and contact forms were typed into then cleared — nothing was sent; what a submission returns is unverified.")
W("- **Blog articles, customer stories, help articles and dev docs pages** are exemplar-level captures; sibling pages share the templates, unmeasured.")
W("- **Solutions and Resources mega-menu panels** were screenshot-captured; only the Product panel's items were component-measured.")
W("- **The Companion messenger** (companion.frontapp.com) paints inside Front's own embed on help.front.com and dev.frontapp.com; its token sheet was captured, the widget UI itself was not measured (it did not open on the captured pages).")
W("- **academy.front.com, community.front.com, frontstatus.com and research.front.com** are further signed-out surfaces on other platforms, not captured.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.")
W("- **The billing switch** was toggled each way for the screenshots; the component reading is the annual side. The 'SAVE 24%' prices are the marketing's content, not tokens.")
W()
W("### Themes")
W()
W("front.com's marketing pages paint three section themes down each page — the plum `[data-theme=theme-dark-violet]` default plus theme-white and theme-gray blocks — and offer no page-level theme switch; the three `violet`/`light`/`gray` token sets are the role tables the stylesheet declares for each. app.frontapp.com's shell carries the real theme: `html[data-theme=\"dark\"]` repaints the whole --color-* layer, driven by the front-theme-preference localStorage key falling back to prefers-color-scheme — the `app`/`dark` token sets are those two live resolutions. The Froyo messenger layer ships the same vocabulary as `--colors-*` with its own `[data-theme]` repointings (the `companion`/`companionDark` sets). help.front.com paints one theme; dev.frontapp.com follows the visitor's ReadMe preference, captured light.")
W()
W("### Fonts")
W()
W("- **Suisse Intl** carries every heading, control and body on the marketing site; **Suisse Intl Mono** draws figures and code; **Suisse Works** is the serif display face — all self-hosted. The app shell sets \"Indivisible\" with Inter fallbacks, and the help centre declares a \"CustomFont\" stack. The style guide falls back to system fonts.")
W()
W("### Screenshots")
W()
W("- The product UI mockups, customer logos, photography and the Wistia video surfaces in the screenshots are the product's published content; the Qualified widget shot shows the vendor surface as shipped.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Marketing copy, plan prices, customer names, testimonial quotes and partner names are the product's content; only frames and components were measured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
