#!/usr/bin/env python3
"""Build components.md for the Hello Ivy design reference.

Reads raw/components-computed.json (every component and state, measured),
tokens.json, screenshots/ and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the
palette token whose value matches, the font family is named once per value,
and a state row shows only what differs from the first state. Adapted from
the hashnode package's builder (itself the Coursera kit's via gladia/Deezer).

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
# palette lives there: color.ground cream, color.ink black), then core, whose
# app.color.* tree holds the product layer's own palette — so a white surface
# is named light.color.inverseSurface, not whichever app token happens to
# share the value. PRIMARY pins the roles a label should prefer when several
# tokens share one colour. Names carry their set prefix (light.color.ink) so
# a label always names a real path in tokens.json.
PRIMARY = {"color.ground", "color.ink", "color.muted", "color.inverseSurface", "color.inverseInk"}
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


def _lab_okl(c):
    """CIE lab()/oklab()/oklch() -> '#rrggbb' or 'rgba(...)' for the token
    lookup, mirroring norm_color() in build_tokens.py."""
    m = re.fullmatch(r"lab\(\s*([\d.]+)\s+(-?[\d.]+)\s+(-?[\d.]+)\s*(?:/\s*([\d.]+%?))?\s*\)", c.strip())
    if m:
        L, A, B, a = m.groups()
        fy = (float(L) + 16) / 116
        fx, fz = fy + float(A) / 500, fy - float(B) / 200
        d = 6 / 29
        f = lambda t: t ** 3 if t > d else 3 * d ** 2 * (t - 4 / 29)
        x, y, z = f(fx) * 0.96422, f(fy) * 1.0, f(fz) * 0.82521
        r = 3.1338561 * x - 1.6168667 * y - 0.4906146 * z
        g = -0.9787684 * x + 1.9161415 * y + 0.0334540 * z
        b = 0.0719453 * x - 0.2289914 * y + 1.4052427 * z
        gam = lambda v: 12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055
        r, g, b = (max(0, min(255, round(gam(v) * 255))) for v in (r, g, b))
        if a is None:
            return "#%02x%02x%02x" % (r, g, b)
        al = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return "#%02x%02x%02x" % (r, g, b) if al == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, al)
    # achromatic oklch()/oklab(): L 0 is black, L 1 is white. Chromium's
    # computed a/b can be signed or `none`; the tiny chroma these shadows
    # carry is within a rounding step of the grey L gives.
    m = re.fullmatch(r"okl(?:ch|ab)\(\s*([\d.]+)\s+(?:none|-?[\d.]+)\s+(?:none|-?[\d.]+)\s*(?:/\s*([\d.]+%?))?\s*\)", c.strip())
    if m:
        lvl = round(float(m.group(1)) * 255)
        a = float(m.group(2) or 1)
        return "#%02x%02x%02x" % (lvl, lvl, lvl) if a == 1 else "rgba(%d, %d, %d, %g)" % (lvl, lvl, lvl, a)
    return c


def colour(c, tokens=True):
    """rgb()/rgba()/color(srgb)/lab()/oklab()/oklch() -> '#hex `token`' or 'rgba(...)'."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        tok = BY_COLOR.get(v) if tokens else None
        return f"{v} `{tok}`" if tok else v

    # Modern colour functions first: normalize each to sRGB so the hex/RGBA
    # passes below can attach the token name like any other measured value.
    c = re.sub(r"(?:lab|oklab|oklch)\([^)]*\)", lambda m: _lab_okl(m.group(0)), c)
    c = re.sub(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)",
               lambda m: label(norm(*(round(float(x) * 255) for x in m.group(1, 2, 3)), m.group(4))), c)
    c = re.sub(r"rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)", lambda m: label(norm(*m.group(1, 2, 3), m.group(4))), c)
    # Skip hexes a label was already attached to, so the pass is idempotent.
    return re.sub(r"#[0-9a-fA-F]{6}\b(?!\s*`)", lambda m: label(m.group(0).lower()), c)


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
            bits.append(" ".join(x for x in (pe, *(colour(p[k], tokens=False) if p.get(k) else None for k in ("backgroundColor", "borderTopWidth", "boxShadow")), p.get("opacity")) if x))
    # A root box-shadow (e.g. the 1px focus ring gained on focus-visible) does
    # not remove the painted children: keep reporting their layers, which is
    # where a state-carrying child outline (the 3px cyan CTA ring) shows up.
    if s["backgroundColor"] == "rgba(0, 0, 0, 0)" and s["borderTopWidth"] == "0px" and s["backgroundImage"] == "none":
        for p in v.get("paint", [])[:6]:
            bits.append(" ".join(x for x in (p["node"], p.get("size"), *(colour(p[k], tokens=False) if p.get(k) else None for k in ("bg", "border", "shadow", "outline")), p.get("radius")) if x))
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

PAGE_NAME = {"home": "home", "pricing": "pricing", "features": "features", "blog": "blog",
             "doc-post": "docs article", "login": "app login", "share": "public share",
             "mobile": "home"}

GROUP_INTRO = {
    "Site chrome": "The marketing shell every www.helloivy.co page carries: the 116px top strip (wordmark, Framer-built nav links, the black pill 'Start for free' CTA, the 'Menu' control whose full-screen overlay is measured under 'opened'), the footer with its links and the real 'Change theme' control whose own press repaints the page dark — measured, never navigated.",
    "Marketing": "The home page's editorial layer: the Unbounded display hero (heading, lead copy, the pill CTA) and the mid-page section headings.",
    "Pricing": "The /pricing page: the plan column cards, their pill CTAs, and the FAQ accordion whose question rows open answers locally.",
    "Features": "The /features page's feature tile cards — measured at rest and hover.",
    "Blog": "The /blog index's post cards — measured at rest and hover, never followed.",
    "Docs": "The hosted docs platform (a separate surface from the Framer site — General Sans, its own chrome): the left nav rail and its links.",
    "App login": "app.helloivy.co/login, at rest only: the centred card (heading, email/password fields, Continue, Google SSO, the sign-up and forgot-password links). Fields were measured, never typed into; Continue was never pressed.",
    "Share document": "The public share route (app.helloivy.co/\u2026/share — a media-kit document anyone with the link can read): the header strip, the settings popover opened through its own control, and the document canvas itself. Nothing was submitted, printed or mailed.",
    "Site chrome (mobile)": "The 390px surface: the compact top strip and the 'Menu' control's drawer, opened through its own tap.",
    "Marketing (mobile)": "The 390px home hero — the display heading drops to 32px.",
}

SHOTS = [
    ("home", "Home", "/"),
    ("about", "About", "/about"),
    ("features", "Features", "/features"),
    ("feature-tasks", "Feature: tasks", "/features/tasks"),
    ("feature-annotate", "Feature: annotate", "/features/annotate"),
    ("feature-portal", "Feature: client portal", "/features/client-portal"),
    ("pricing", "Pricing", "/pricing"),
    ("project-management", "Project management", "/project-management"),
    ("project-collab", "Collaboration software", "/project-collaboration-software"),
    ("alt-notion", "Alternative: Notion", "/notion-alternative"),
    ("blog", "Blog index", "/blog"),
    ("blog-post", "Blog article", "/blog/announcing-hello-ivy-2-0"),
    ("release-notes", "Release notes", "/release-notes"),
    ("terms", "Terms", "/terms"),
    ("docs", "Docs index", "/docs"),
    ("doc-page", "Docs article", "/docs/create-a-project"),
    ("app-login", "App login (rest only)", "app.helloivy.co/login"),
    ("app-share", "Public share document", "app.helloivy.co/\u2026/share/\u2026"),
]

MOBILE = [
    ("mobile-home", "Home, phone", "/"),
    ("mobile-features", "Features, phone", "/features"),
    ("mobile-pricing", "Pricing, phone", "/pricing"),
    ("mobile-blog", "Blog, phone", "/blog"),
    ("mobile-app-login", "App login, phone", "app.helloivy.co/login"),
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

# The captured icon set: tools/capture/icons.mjs collects every distinct
# inline <svg> into icons/ and writes icons/INDEX.tsv (file, inferred_name,
# hash, rendered sizes, viewBox, style, seen_on, place, text_or_label). The
# table below is that index, so the section never contradicts the package.
icons = []
idx = Path("icons/INDEX.tsv")
if idx.exists():
    rows = [l.split("\t") for l in idx.read_text().splitlines() if l.strip()]
    header = rows[0]
    for r in rows[1:]:
        d = dict(zip(header, r + [""] * (len(header) - len(r))))
        icons.append([d.get("file", ""), d.get("inferred_name", ""), d.get("hash", ""),
                      d.get("sizes", ""), d.get("viewBox", ""), d.get("style", ""),
                      d.get("seen_on", ""), d.get("place", ""), d.get("text_or_label", "")])

W("# Hello Ivy components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Read from www.helloivy.co, app.helloivy.co and the hosted /docs on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Later recaptures merge into the same file, so every entry names the date its own states were read; a state a re-read missed keeps its earlier date and says so. Nothing was signed into, bought, searched, typed or submitted; the only presses were local UI toggles the pages' own chrome provides — the Framer 'Menu' overlay, the footer's real 'Change theme' control, the pricing FAQ accordion, the share page's settings popover and the phone's menu drawer; every link was measured, never followed.")
W()
W("**Where this was read.** Three public surfaces: www.helloivy.co — the Framer marketing site (home, about, features and its feature pages, pricing, project-management and collaboration landing pages, the Notion alternative page, blog, release notes, terms) — app.helloivy.co — the product, seen only at the /login boundary (at rest, never signed into) and the public share route a document link exposes — and the hosted /docs platform, a third surface with its own face (General Sans). Everything behind the login — the real workspace, projects, clients — was never entered. All of that is a boundary listed under Gaps, not captures.")
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
W("Screenshots are named `{page}-{theme}-{state}.png` where `{theme}` is the surface the page painted at capture: every page boots `light`; `{page}-dark-*` shots are the same marketing page after the footer's own 'Change theme' control repainted `html[toggle-theme=dark]`, verified by the painted surface and switched back after — dark shots exist only on pages where that real control demonstrably repaints (the marketing site); the app and docs surfaces paint light only and have no `dark` shots. Desktop shots are 1440 x 900 at 1x; `-full` shots are the whole page at 1x, bounded with the boundary recorded in the shot's `.capture.json` sidecar (a page whose scroll exceeds the bound is stitched from tiles); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x). `app-*` pages are on app.helloivy.co.")
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
    ("Menu overlay", "home", "the nav 'Menu' control's own press — Framer's full-screen overlay opened, captured, closed through its own close control (it ignores Escape)", "[home-light-menu](screenshots/home-light-menu.png)"),
    ("Mobile menu drawer", "home, phone width", "the 'Menu' control's own tap at 390px", "[mobile-home-light-menu](screenshots/mobile-home-light-menu.png)"),
    ("FAQ accordion", "Pricing", "a question row's own press — the answer expanded", "[pricing-light-faq-open](screenshots/pricing-light-faq-open.png)"),
    ("Settings popover", "public share", "the share header's own settings control — the popover opened and captured; nothing in it was submitted", "[app-share-light-settings-menu](screenshots/app-share-light-settings-menu.png)"),
    ("Change theme control", "home footer", "the footer's own 'Change theme' control — verified to repaint the page (html[toggle-theme=dark], body rgb(22,22,26)) before any dark reading; switched back after", "[home-light-theme-control](screenshots/home-light-theme-control.png), [home-dark-default](screenshots/home-dark-default.png)"),
    ("Dark theme", "marketing pages", "the same footer control's real repaint — captured on the pages where the repaint was verified", "[home-dark-default](screenshots/home-dark-default.png), [about-dark-default](screenshots/about-dark-default.png), [features-dark-default](screenshots/features-dark-default.png), [pricing-dark-default](screenshots/pricing-dark-default.png), [blog-dark-default](screenshots/blog-dark-default.png)"),
    ("Sign-in, dashboard, workspace", "app.helloivy.co behind /login", "the auth wall — the login card measured at rest, never signed into", "boundary; see Gaps"),
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
# the card-like components to compare in one table
for k in ["nav-bar", "nav-menu-box", "plan-card", "feature-card", "post-card", "docs-nav", "login-card", "share-header", "share-doc", "m-nav-bar"]:
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
        # Provenance: each state carries the date of the run that measured it.
        # A component a recapture missed keeps its earlier readings under the
        # earlier date (recaptureMissed), and a state whose re-read failed
        # keeps its earlier style under rerunError — never republished under
        # the new run's date.
        by_run = {}
        for s, v in c["states"].items():
            by_run.setdefault(v.get("run") or c.get("run") or J["_meta"]["read"], []).append(s)
        prov = []
        if len(by_run) == 1:
            prov.append(f"Read on {next(iter(by_run))}.")
        elif by_run:
            prov.append("States read on " + "; ".join(f"{r} ({', '.join(sorted(ss))})" for r, ss in sorted(by_run.items())) + ".")
        if c.get("recaptureMissed"):
            prov.append(f"A {c['recaptureMissed']} recapture missed it — the {c.get('run')} readings are retained, not remeasured.")
        for s, v in c["states"].items():
            if v.get("rerunError"):
                prov.append(f"`{s}` kept its {v.get('run')} reading after a failed re-read ({v['rerunError'][:90]}).")
            elif v.get("error"):
                prov.append(f"`{s}` failed at capture ({v['error'][:90]}).")
        if prov:
            W(" ".join(prov))
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
if icons:
    W(f"{len(icons)} distinct inline-SVG icons were collected from the live pages into [icons/](icons) by `tools/capture/icons.mjs`, indexed in [icons/INDEX.tsv](icons/INDEX.tsv): a file is named from `tools/capture/icon-names.tsv` where its geometry hash is listed, else the label or class of the control it sits in, else `icon-<hash>`; colour is kept as `currentColor` wherever it matched the text colour, so each icon recolours from CSS `color` the way it does on the site. The icons are the product's artwork — borrow the set's grammar (sizes, stroke-vs-fill, naming roles), never the artwork itself.")
else:
    W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the product's mark, navigation glyphs, partner logos) are the product's artwork. Declared under layoutGaps in the catalog entry.")
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
W("### The blocked product surfaces")
W()
W("The signed-in product was never entered: **app.helloivy.co/login** and everything behind it (the real workspace, projects, clients, files, settings) stays outside — the login card's fields were measured at rest, never typed into, and 'Continue' was never pressed. The **public share route** is captured as far as a signed-out reader gets: the document, its header and the settings popover opened through its own control — nothing was submitted, printed, mailed or exported. All documented as boundaries, never faked.")
W()
W("### Pages")
W()
W("- **The workspace and every post-auth surface** — the auth wall, see above. The public share document is the only app interior a signed-out reader can reach.")
W("- **/docs content beyond the index and one article** — the hosted docs platform was sampled at its index and the 'create a project' guide; it is a separate platform from the marketing site (its own chrome, General Sans) and light-only — no dark pass exists to capture.")
W("- **Remaining marketing routes** — the other feature pages (feed, chat, docs, files, roadmap, calendar, version-control) and alternative pages (asana, basecamp, clickup, monday) were probed and share the same Framer chrome and theme layer; three feature pages and the Notion alternative were screenshotted as representatives rather than all crawled.")
W("- **Blog articles beyond the sample** — /blog/announcing-hello-ivy-2-0 stands in for the article template.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.")
W("- **The login fields were never typed into** — the email field was given a real keyboard focus for its focused state and nothing was entered; 'Continue', Google SSO and the sign-up/forgot links were measured, never activated.")
W("- **The FAQ accordion and menu overlay** were opened and closed through their own controls — the Framer overlay ignores Escape and takes its own close control; captures were reloaded to a clean state after overlays.")
W("- **The theme control** was pressed to paint dark for the `dark` states and shots, verified by the repainted surface, then switched back — no theme was held across navigations.")
W()
W("### Themes")
W()
W("www.helloivy.co boots `html[toggle-theme=light]` and the footer carries a real 'Change theme' control that repaints `html[toggle-theme=dark]` (persisted in `localStorage.currentToggleState`). `light` is the painted default; `dark` states and `{page}-dark-*` screenshots were painted through that control, verified by the painted surface (the html attribute and the computed background rgb(22,22,26)), and the theme was switched back afterwards. The same re-pointing exists under `@media (prefers-color-scheme: dark)` in the probe. app.helloivy.co has no theme control on its public routes and paints light only — no app dark values are inferred. /docs is light-only.")
W()
W("### Fonts")
W()
W("- **Unbounded** (marketing display), **Inter** (marketing UI + the whole app face, `--main-font-family`) and **General Sans** (docs platform) are declared and measured, not shipped — the style guide falls back to system faces.")
W()
W("### Screenshots")
W()
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W("- The rendered brand strings on the captured pages (the wordmark and copy) are the product's published content.")
W("- The public share document's contents are a published media kit the author chose to share by link; nothing private was captured.")
W()
W("### Content left out")
W()
W("- Marketing copy, blog prose and pricing text are the product's published content; only frames and components were measured.")
W()

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
