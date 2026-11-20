#!/usr/bin/env python3
"""Build components.md for the Glorify design reference.

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
for setname in ("light", "app"):
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
PAGE_SET = {"login": "app", "register": "app", "designer": "app"}


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
        o["text"] = f"{font(t['fontSize'], t['lineHeight'], t.get('fontWeight') or s['fontWeight'], t['fontFamily'])}, {colour(t['color'], setname)}"
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


def measured(v):
    """A state with a real reading: not skipped, not a focus that never landed (via "focus failed"), not a
    focus that did not match :focus-visible. Those are the element at rest (the kit's rule, PR 932)."""
    return "style" in v and not v.get("skipped") and v.get("via") != "focus failed" and (v.get("focus") or {}).get("matches") is not False


def clear(c):
    """A colour that paints nothing (alpha 0)."""
    c = c.strip()
    return c == "transparent" or bool(re.fullmatch(r"rgba\([^)]*,\s*0(?:\.0+)?\)", c))


def visible_shadow(v):
    """True when a box-shadow list paints something: a layer with a colour that is not clear and a
    non-zero offset, blur or spread (Tailwind's all-zero ring slots paint nothing)."""
    if not v or v == "none":
        return False
    for part in re.split(r",\s*(?![^()]*\))", v):
        colour_ = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", part)
        lengths = re.findall(r"-?[\d.]+px", part)
        if colour_ and not clear(colour_.group(0)) and any(float(x[:-2]) != 0 for x in lengths):
            return True
    return False


def child_layers(c):
    setname = PAGE_SET.get(c.get("page"), "light")
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

PAGE_NAME = {"home": "home", "pricing": "pricing", "feature": "background-remover feature",
             "templates": "templates", "marketplace": "template marketplace",
             "learn": "learn", "submit": "submit a template",
             "login": "app sign-in", "register": "app sign-up",
             "designer": "anonymous editor", "mobile": "home"}

GROUP_INTRO = {
    "Site chrome": "The header on every marketing page: the Glorify wordmark, the 'Who is it for?'/Features/Resources/Templates dropdowns, Pricing, Login, 'Play for free' and 'Get Started Now'.",
    "Home": "The light home page: the 'Easily create marketing visuals that turn browsers to buyers' masthead over the Ecom subline, the 'Play for free' action into the anonymous editor, and the feature cards.",
    "Pricing": "The /pricing page: the Monthly/Yearly billing switcher and the Basic/Pro/Business plan cards with their 'Start … Trial' actions.",
    "Feature page": "A /features/<name> product page (background-remover captured): the display heading, the page CTA and the capability cards.",
    "Templates": "The /templates gallery: template cards and the category links.",
    "Template marketplace": "The /template-marketplace grid: the use-case filter pills and template cards.",
    "Learn": "The /learn hub: the category filters and article cards.",
    "Submit a template": "The /submit-template page: the guidelines copy and the creator-privileges card.",
    "App sign-in": "app.glorify.com/dashboard/login (reached through /welcome) — the signed-out dark sign-in card: e-mail and password fields, the primary 'Sign in' submit (disabled at rest; enabled once both fields hold sample text — never clicked), the Google OAuth button and the sign-up link.",
    "App sign-up": "app.glorify.com/dashboard/register — the signed-out dark sign-up card: name, e-mail and password fields, the primary submit and the Google button. Measured as a form, never submitted.",
    "Anonymous editor": "app.glorify.com/designer/use-template/0 — the product's own Play-for-free path: the SPA creates a scratch /file/<id> and paints the upload onboarding, the Craft dialog behind 'Try with Placeholder Image', and the canvas chrome — header, tool rail, inspector — of the real editor.",
    "Mobile (390 wide)": "The phone surface at 390 wide: the header, the burger menu, the masthead and the hero CTA.",
    "Footer": "The marketing footer: sitemap columns, legal links and social marks.",
}

SHOTS = [
    ("home", "Home", "/"),
    ("pricing", "Pricing", "/pricing"),
    ("feature-bg", "Background Remover feature", "/features/background-remover"),
    ("templates", "Templates", "/templates"),
    ("marketplace", "Template marketplace", "/template-marketplace"),
    ("learn", "Learn", "/learn"),
    ("learn-article", "Learn article", "/learn/facebook-ad-sizes-best-practices-2024"),
    ("team", "Team", "/team"),
    ("affiliates", "Affiliates", "/affiliates"),
    ("webinars", "Webinars", "/webinars"),
    ("submit-template", "Submit a template", "/submit-template"),
    ("canva-alternative", "Canva alternative", "/canva-alternative"),
    ("terms", "Terms", "/terms-of-service"),
    ("privacy", "Privacy", "/privacy-policy"),
    ("login", "App sign-in", "app.glorify.com/dashboard/login"),
    ("register", "App sign-up", "app.glorify.com/dashboard/register"),
    ("designer", "Anonymous editor", "app.glorify.com/designer/use-template/0"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "/"),
    ("mobile-pricing", "Pricing, phone", "/pricing"),
    ("mobile-login", "App sign-in, phone", "app.glorify.com/dashboard/login"),
]

L = []


def W(s=""):
    L.append(s)


shots = sorted(p.name for p in Path("screenshots").glob("*.png"))


def links(prefix):
    out = []
    for f in shots:
        m = re.fullmatch(re.escape(prefix) + r"-(?:light|dark|app)-(.+)\.png", f)
        if m:
            out.append(f"[{m.group(1)}](screenshots/{f})")
    return ", ".join(out)


n_crops = len(list(Path("components/crops").glob("*.png")))
n_states = sum(len(c["states"]) for c in C.values())
icons = []

W("# Glorify components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from glorify.com and app.glorify.com on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the sign-in and sign-up forms were never sent; every link and CTA was measured, never followed.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [patterns.md](patterns.md).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value in the component's own surface set (light / app — the two hosts declare separate vocabularies), when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/24 500, #131e40`, and is read from the first text node inside the component.")
W("- Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the surface painted at capture: `light` for the marketing pages (light-only — no toggle, no dark media query) and `app` for the dark app/editor surfaces. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
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
    ("Consent overlay", "every page", "no consent banner was observed on either host; any layer would be hidden, never answered", "hidden before every shot and reading"),
    ("Features dropdown", "marketing header", "hovered the 'Features' nav trigger to open its Framer dropdown", "[home-light-features-menu](screenshots/home-light-features-menu.png), [nav-features](#features-nav-trigger)"),
    ("Billing switcher", "pricing", "clicked 'Monthly' and 'Yearly' — local UI toggles that only swap the displayed prices", "[pricing-light-billed-yearly](screenshots/pricing-light-billed-yearly.png), [pricing-light-billed-monthly](screenshots/pricing-light-billed-monthly.png), [bill-monthly](#billing-tab-monthly), [bill-yearly](#billing-tab-yearly)"),
    ("Mobile menu", "home, phone width", "tapped the nav burger", "[mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-burger](#mobile-burger), [m-menu-link](#mobile-menu-link)"),
    ("Craft dialog", "anonymous editor", "clicked the 'Try with Placeholder Image' card — the product's demo path on the scratch file", "[designer-app-dialog](screenshots/designer-app-dialog.png), [ed-craft](#craft-dialog), [ob-ph](#placeholder-image-card)"),
    ("Craft style pick", "anonymous editor", "clicked the 'Modern' style card — the local toggle that enables 'Add to canvas'", "[designer-app-style-picked](screenshots/designer-app-style-picked.png), [ed-craft-style](#style-card), [ed-add](#add-to-canvas)"),
    ("Canvas view", "anonymous editor", "pressed 'Add to canvas' once on the scratch file (the screenshot pass) — it ran a server-side AI generation; a boundary since 2026-11, no longer pressed", "[designer-app-canvas](screenshots/designer-app-canvas.png)"),
    ("Inspector LAYERS tab", "anonymous editor", "clicked the LAYERS inspector tab — a local UI toggle", "[designer-app-layers](screenshots/designer-app-layers.png), [ed-tab](#inspector-tab), [ed-tab-layers](#layers-tab)"),
    ("Auth fields", "app.glorify.com", "typed into then cleared — nothing sent; the sign-in submit's enabled fill was measured with sample text in both fields, never clicked", "[login-field](#email-field-sign-in), [login-submit](#sign-in-submit)"),
    ("Signed-in product", "a Glorify account", "every post-login surface (the real projects, dashboards, brand kit, billing) needs an account", "boundary; see Gaps"),
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
    if not st or not measured(st):
        continue
    s = st["style"]
    base = next((v["style"] for v in c["states"].values() if measured(v)), s)
    # A transparent outline passes the width/style test but draws nothing.
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0 and not clear(s["outlineColor"])
    # A ring painted on a child layer instead of the wrapper: offer buttons
    # draw 1px dotted outlines on their inner anchor while the wrapper's own
    # outline stays none. Those states must count as ringed too.
    child_ring = next((n["outline"] for n in st.get("paint", []) if n.get("outline")
                       and not any(clear(x) for x in re.findall(r"rgba?\([^)]*\)|transparent", n["outline"]))), None)
    shadow = s["boxShadow"] != base["boxShadow"] and visible_shadow(s["boxShadow"])
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
for k in ["home-card", "plan-card", "feat-card", "tpl-card", "mk-card", "learn-card", "st-quote", "login-card", "ob-ph", "ed-craft", "ed-craft-style", "ed-inspector", "m-menu-link"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if measured(s)), None)
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Glorify wordmark, the feature-card glyphs, the editor tool-rail icons and the template artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.")
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
W("Glorify's product is the design workspace: every post-login surface — saved projects, the real editor on a user's files, brand kit, dashboards and billing — needs an account and was never reached. app.glorify.com/dashboard/login and /dashboard/register are the auth surfaces a signed-out visitor sees, and they were measured as forms, never submitted. The anonymous editor at /designer/use-template/0 is genuinely public — the marketing 'Play for free' action opens it on a scratch file the SPA creates — and it paints the real chrome (header, tool rail, inspector) around the onboarding and Craft dialog; deeper editor work (saving, sharing, downloading, the tool flyouts) is the product's own demo path or needs the account. The product mocks inside the marketing cards are illustrations, not the product.")
W()
W("### Pages")
W()
W("- **The account.** Every post-login surface was never reached; the sign-in and sign-up forms were measured and typed into then cleared — 'Sign in', 'Sign up' and the OAuth buttons were never pressed, and what a submitted form returns is unverified.")
W("- **Purchase.** Plan CTAs ('Start Basic/Pro/Business Trial', 'Book a demo') were measured, never followed; no checkout or trial flow was started.")
W("- **Feature and comparison routes** beyond the captured set (the other /features/* pages, the alternative pages, the rest of /learn's articles) are the same templates, unmeasured; one example of each family was captured.")
W("- **Editor depth.** On the anonymous scratch file the Craft dialog was opened, a style picked, and 'Add to canvas' pressed once to paint the canvas state, which ran a server-side AI generation (a boundary since 2026-11: the screenshot pass no longer presses it). Share, Download, the tool flyouts and the sign-in nudges inside the editor were measured, never activated.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Error, loading and validation states** were not seen on the public surface — the forms were never submitted. The sign-in submit's disabled fill is measured at rest and its enabled fill with sample text in both fields.")
W("- **The editor's deeper states** (canvas editing gestures, layer selection beyond the tab switch, generation progress) are beyond what a state list can capture; the canvas state is a screenshot.")
W()
W("### Themes")
W()
W("The marketing site paints light only — no theme toggle and no `prefers-color-scheme` dark rule was observed on glorify.com (`color-scheme: normal`). The app surface genuinely paints dark chrome — the auth cards and the editor are dark signed out — and its tokens live in the separate `app` set. No theme switcher was observed on either host; the SPA's `--light-*` and `--dark-*` ramps are both declared on the same :root, not alternate themes.")
W()
W("### Fonts")
W()
W("- The served faces (the marketing site's Framer-bundled fonts and the app's own faces, listed in raw/css-vars.json `fonts`) are the product's; the style guide falls back to system sans.")
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
