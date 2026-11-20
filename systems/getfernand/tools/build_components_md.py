#!/usr/bin/env python3
"""Build components.md for the Fernand design reference.

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


# Colour -> token name, built per surface set. The hosts remap the shared
# palette names (the dark set's `white` is #161618, not #ffffff), so a single
# merged map would label a dark component's #ffffff `white` and send readers
# to the wrong value. A component's labels come from its own set's map (core
# first, then the set's own tokens), and a colour that matches nothing there
# stays a literal.
def resolve_alias(v, setname, depth=0):
    m = re.fullmatch(r"\{([^{}]+)\}", v or "")
    if not m or depth > 6:
        return v
    for root in (T.get(setname, {}), T.get("core", {})):
        node = root
        for k in m.group(1).split("."):
            node = node.get(k) if isinstance(node, dict) else None
        if isinstance(node, dict) and "$value" in node:
            return resolve_alias(node["$value"], setname, depth + 1)
    return v


BY_COLOR = {}
for setname in ("light", "help", "app", "dark"):
    # The tokens the theme (core + the set) carries: the set's own declaration
    # shadows core on a shared path, so the label is always the token a reader
    # of this set's theme would actually resolve.
    themed = {}
    for src in ("core", setname):
        for n, t in flat(T.get(src, {})):
            if t["$type"] == "color" and isinstance(t["$value"], str):
                themed[n] = t
    m = {}
    for n, t in themed.items():
        m.setdefault(resolve_alias(t["$value"], setname), n)
    BY_COLOR[setname] = m

# The token set a captured page's components belong to.
PAGE_SET = {"login": "app", "signup": "app", "help": "help", "helparticle": "help", "helpdark": "dark"}


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def colour(c, setname="light", tokens=True):
    """rgb()/rgba()/color(srgb) -> '#hex `token`' or 'rgba(...)' — the token
    label is resolved inside the component's own surface set."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        tok = BY_COLOR.get(setname, {}).get(v) if tokens else None
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


def props(v, setname="light"):
    s = v["style"]
    o = {}
    o["size"] = f"{num(v['rect']['w'])} x {num(v['rect']['h'])}"
    pad = sides(s["paddingTop"], s["paddingRight"], s["paddingBottom"], s["paddingLeft"])
    if pad != "0px":
        o["padding"] = pad
    bds = []
    for d in ("Top", "Right", "Bottom", "Left"):
        if float(s[f"border{d}Width"].replace("px", "")) > 0 and s[f"border{d}Style"] != "none":
            bds.append(f"{s[f'border{d}Width']} {s[f'border{d}Style']} {colour(s[f'border{d}Color'], setname)}")
        else:
            bds.append("none")
    if any(b != "none" for b in bds):
        o["border"] = bds[0] if len(set(bds)) == 1 else "; ".join(f"{'TRBL'[i]}: {b}" for i, b in enumerate(bds) if b != "none")
    rad = sides(s["borderTopLeftRadius"], s["borderTopRightRadius"], s["borderBottomRightRadius"], s["borderBottomLeftRadius"])
    if rad != "0px":
        o["radius"] = rad
    o["background"] = colour(s["backgroundColor"], setname)
    if s["backgroundImage"] != "none":
        img = re.sub(r'url\("data:[^)]*\)', "an image (data URI)", s["backgroundImage"])
        o["image"] = colour(img, setname)[:200]
    if s["boxShadow"] != "none":
        sh = colour(s["boxShadow"], setname, tokens=False)
        layers = [x.strip() for x in re.split(r",(?![^(]*\))", sh)]
        layers = [x for x in layers if not x.startswith("transparent")]
        if layers:
            o["shadow"] = ", ".join(layers)
    if s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0:
        o["outline"] = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'], setname)}, offset {s['outlineOffset']}"
    t = v.get("textStyle")
    if t:
        o["text"] = f"{font(t['fontSize'], t['lineHeight'], t['fontWeight'], t['fontFamily'])}, {colour(t['color'], setname)}"
    else:
        o["text"] = f"{font(s['fontSize'], s['lineHeight'], s['fontWeight'], s['fontFamily'])}, {colour(s['color'], setname)}"
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
        o["icon"] = f"{num(v['icon']['w'])} x {num(v['icon']['h'])}, {colour(v['icon']['color'], setname)}"
    if v.get("placeholder"):
        o["placeholder"] = colour(v["placeholder"]["color"], setname)
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
    setname = PAGE_SET.get(c.get("page"), "light")
    base = props(c["states"][states[0]], setname)
    rows = [(states[0], base)]
    same = []
    for st in states[1:]:
        p = props(c["states"][st], setname)
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
    setname = PAGE_SET.get(c.get("page"), "light")
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
            bits.append("background " + colour(p["bg"], setname))
        if p.get("bgImage"):
            bits.append("image " + colour(p["bgImage"], setname)[:90])
        if p.get("border"):
            bits.append("border " + colour(p["border"].split(" | ")[0][2:], setname))
        if p.get("radius"):
            bits.append("radius " + p["radius"])
        if p.get("shadow"):
            bits.append("shadow " + colour(p["shadow"], setname))
        out.append(" ".join(bits))
    return "; ".join(out).replace("|", "/")


# --------------------------------------------------------------------------- page and group text

PAGE_NAME = {"home": "home", "pricing": "pricing", "updates": "updates", "integrations": "integrations",
             "alternative": "comparison (alternative/intercom)", "feature": "ai-agents feature",
             "login": "app sign-in", "signup": "app signup", "help": "docs home",
             "helparticle": "docs article", "helpdark": "docs article", "mobile": "home"}

GROUP_INTRO = {
    "Site chrome": "The fixed header on every marketing page: wordmark, About us / Pricing / Log in links, the 'Book a demo' Cal.com action and the 'Start for free' button.",
    "Home": "The light home page: the 38px 'The free customer support platform for SaaS teams' masthead, the dated changelog eyebrow pill, the dark 'Start for free' CTA and 'Book a demo' action, the Install-with-AI menu, the demo dialog, the channels carousel, feature cards, the widget playground and testimonials.",
    "Pricing": "The /pricing/ page: the FREE/PAID plan cards ($0 and $29 per active human per month), plan feature rows, the large Start-for-free button and the questions-&-answers list.",
    "Updates": "The /updates changelog: sticky entry titles and article bodies.",
    "Integrations": "The /integrations catalogue: Essentials cards with product mocks and the grouped integration grids.",
    "Alternative page": "The /alternative/intercom comparison page: the Intercom-vs-Fernand data table and the FAQ accordion.",
    "Feature page": "The /feature/ai-agents product page: the permissions switches and replay control of the agent demo.",
    "App login": "app.getfernand.com/auth/login — the signed-out Vue SPA sign-in card: e-mail and password fields, the primary 'Login' submit and the account links. Measured as a form, never submitted.",
    "App signup": "app.getfernand.com/create — the signed-out signup: the 'Bonjour, I'm Fernand' intro panel, work-email and product-name fields, the terms checkbox and the 'Continue' button. Measured as a form, never submitted.",
    "Help center": "help.getfernand.com — the Nuxt docs site on the same palette: header nav, the search field and results popover, collection cards and article rows, and the 'Switch to dark mode' link.",
    "Help center (dark)": "The same docs site under body.dark-mode, painted by its own 'Switch to dark mode' link — the real user-facing toggle, not a reconstruction.",
    "Mobile (390 wide)": "The phone surface at 390 wide: the header, the masthead and the hero CTA.",
    "Footer": "The marketing footer: the 'Start free. Email included.' closing CTA, sitemap columns, legal links and social icons.",
    "Fernand widget": "The product's own embeddable chat widget on the marketing site — the 48px launcher bubble and the panel it opens; opened once, never typed into.",
}

SHOTS = [
    ("home", "Home", "/"),
    ("pricing", "Pricing", "/pricing/"),
    ("about", "About", "/about-us/"),
    ("blog", "Blog", "/blog/"),
    ("updates", "Updates", "/updates/"),
    ("updates-article", "Updates article", "/updates/dodo-payments-integration/"),
    ("integrations", "Integrations", "/integrations/"),
    ("integration-slack", "Integration (Slack)", "/integrations/slack/"),
    ("feature-ai", "AI agents", "/feature/ai-agents/"),
    ("feature-headless", "Headless support", "/feature/headless-customer-support/"),
    ("alternative-intercom", "Intercom alternative", "/alternative/intercom/"),
    ("privacy", "Privacy", "/privacy/"),
    ("login", "App sign-in", "app.getfernand.com/auth/login"),
    ("signup", "App signup", "app.getfernand.com/create"),
    ("help", "Docs home", "help.getfernand.com"),
    ("help-article", "Docs article", "help.getfernand.com/getting-started"),
    ("help-dark", "Docs article, dark", "help.getfernand.com/getting-started"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "/"),
    ("mobile-pricing", "Pricing, phone", "/pricing/"),
    ("mobile-help", "Docs article, phone", "help.getfernand.com/getting-started"),
    ("mobile-login", "App sign-in, phone", "app.getfernand.com/auth/login"),
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

W("# Fernand components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from getfernand.com, app.getfernand.com and help.getfernand.com on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the login and signup forms were never sent; every link and CTA was measured, never followed.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [patterns.md](patterns.md).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value in the component's own surface set (light / help / app / dark — the hosts remap the shared palette names), when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/24 500, #131e40`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the surface painted at capture: `light` for every marketing page, the signed-out app forms and the docs site in light — getfernand.com is light-only (`color-scheme: light`); `dark` for the docs article painted under `body.dark-mode` by the site's own 'Switch to dark mode' link. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).")
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
    ("Consent overlay", "every page", "no consent banner was observed on any of the three hosts; any layer would be hidden, never answered", "hidden before every shot and reading"),
    ("Install-with-AI menu", "home hero", "clicked the 'Install with AI' aria-haspopup button", "[home-light-ai-menu](screenshots/home-light-ai-menu.png), [ai-setup-toggle](#install-with-ai-menu-button), [ai-setup-item](#ai-setup-menu-item)"),
    ("Demo dialog", "home hero", "clicked 'Watch a 2 minute demo'; the video pauses for the shot and Escape closes it", "[home-light-demo-modal](screenshots/home-light-demo-modal.png), [demo-dialog](#demo-dialog)"),
    ("Widget panel", "every marketing page", "clicked the Fernand chat-widget launcher — the product's own embed; never typed into", "[home-light-launcher-open](screenshots/home-light-launcher-open.png), [launcher](#widget-launcher), [launcher-panel](#widget-panel)"),
    ("Docs search", "help.getfernand.com", "typed 'channel' into #search-field then cleared it", "[help-light-search](screenshots/help-light-search.png), [help-search-pop](#search-popover)"),
    ("Docs dark mode", "help.getfernand.com", "clicked the site's own 'Switch to dark mode' link", "[help-dark-default](screenshots/help-dark-dark-default.png), [help-dark-toggle](#dark-mode-switch)"),
    ("Mobile menu", "docs article, phone width", "the docs site's menu toggle", "[mobile-help-light-menu](screenshots/mobile-help-light-menu.png)"),
    ("Login/signup fields", "app.getfernand.com", "typed into then cleared — nothing sent", "[login-field](#email-field-login), [create-field](#email-field-signup)"),
    ("Cal.com booking", "every marketing page", "the 'Book a demo' action loads the Cal.com scheduler; measured, never activated", "boundary; see Gaps"),
    ("Signed-in product", "a Fernand account", "every post-login surface (the inbox workspace, settings, API keys) needs an account", "boundary; see Gaps"),
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
    desc = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'], PAGE_SET.get(c.get('page'), 'light'))}, offset {s['outlineOffset']}" if ring else (f"on a child: {child_ring}" if child_ring else None)
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
for k in ["channels-card", "price-free", "price-paid", "feat-card", "int-essential", "help-card", "trusted-card", "login-card", "wpg-playground"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if "style" in s), None)
    if st is None:
        continue
    p = props(st, PAGE_SET.get(c.get("page"), "light"))
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Fernand wordmark, the channel and feature glyphs, the widget launcher mark, the emoji glyphs on the docs collection cards) are the product's artwork. Declared under layoutGaps in the catalog entry.")
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
W("Fernand's product is the support workspace: every post-login surface — the inbox, conversation views, settings, API keys, the team/AI-agent configuration — needs an account and was never reached. app.getfernand.com/auth/login and /create are the only app surfaces a signed-out visitor sees, and they were measured as forms, never submitted. The product mocks inside the marketing cards and the widget playground are illustrations, not the product.")
W()
W("### Pages")
W()
W("- **The account.** Every post-login surface was never reached; the sign-in and signup forms were measured and typed into then cleared — 'Login'/'Continue' were never pressed, the terms checkbox was never toggled, and what a submitted form returns is unverified.")
W("- **Book a demo.** The 'Book a demo' action is a Cal.com scheduling link; opening it starts a real booking flow, so it was measured at rest and never activated.")
W("- **Alternative pages** beyond /alternative/intercom, the rest of the feature pages, and the other integrations are the same templates, unmeasured; one example of each family was captured.")
W("- **/updates/ is a ~44k-px changelog** — captured in full, stitched from 4 contiguous parts (the part clips are recorded in the `.capture.json` sidecar).")
W("- **blog articles** — the /blog index was captured; individual posts are the same template, unmeasured.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.")
W("- **The widget panel's inner states** (an open conversation, the chat input) were not reached — the panel was opened and shot, never typed into.")
W()
W("### Themes")
W()
W("The marketing site and the signed-out app paint light only — no toggle, no `prefers-color-scheme` switch was observed on them (`color-scheme: light` on :root). The docs site ships a real 'Switch to dark mode' link that sets body.dark-mode and persists it in localStorage; the dark set and the Help-center-(dark) measurements are that genuinely-toggled surface. The SPA's stylesheet also declares a body.dark-mode remap — captured in raw/css-vars.json — but nothing signed out paints it.")
W()
W("### Fonts")
W()
W("- **Inter** (self-hosted woff2, weights 300–700 plus italics on the marketing site) is the served face on all three hosts. The style guide falls back to system sans.")
W()
W("### Screenshots")
W()
W("- The product mocks, screenshots-in-screenshots and logo walls are the product's published content.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Article copy, testimonial names and the changelog text are the product's content; only frames and components were measured.")
Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
