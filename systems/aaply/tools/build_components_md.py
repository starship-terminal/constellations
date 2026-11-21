#!/usr/bin/env python3
"""Build components.md for the aaply design reference.

Reads raw/components-computed.json (every component and state, measured), tokens.json,
screenshots/ and icons/INDEX.tsv, and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the palette token whose
value matches, the font family is named once per value, and a state row shows only what differs
from the first state. Adapted from the public-route builder.

Deterministic: re-running it on the same inputs reproduces components.md byte for byte.
Run from anywhere: python3 tools/build_components_md.py
"""
import json, os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
J = json.load(open("raw/components-computed.json"))
C = J["components"]
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
for n, t in flat(T["core"]["palette"]):
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
    return o


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "outline", "text", "transition", "transform", "opacity", "icon", "placeholder"]


def state_rows(c):
    states = [s for s in c["states"] if "style" in c["states"][s]]
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
        bits = [re.sub(r"\..*$", "", p["node"]) if "::" not in p["node"] else p["node"].split(".")[0], p["size"].replace(".0x", "x").replace(".0", "")]
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

PAGE_NAME = {"home": "home", "features": "features", "value": "value", "pricing": "pricing", "reviews": "reviews", "story": "our-story", "team": "team", "figma": "figma-plugin", "early": "early-program", "manual": "manual", "mobile": "home"}

GROUP_INTRO = {
    "Shell and navigation": "The chrome on the public pages: the floating white nav bar (aaply wordmark left, Features / Value / Pricing / Reviews links centre, Log in ghost pill and the black Sign up pill right), and the black footer band with the mail link, social icons and second nav list.",
    "Home": "The landing page: the Poppins display headline with inline emoji/avatar atoms, the lime \"Sign up fo free\" and black \"Try demo project\" pills, the browser-chrome product mockup, chat-annotation bubbles and the numbered how-it-works steps down ~5000px.",
    "Features": "The workflow walkthrough: numbered steps (Start your new mobile app design project / Add your first mobile screen …), each pairing a chat bubble with a browser-chrome product panel, ending on the oversized \"Try DEMO project\" button.",
    "Value": "The value page: the \"Aaply is here to boost your creativity\" display and a grid of square rounded value cells.",
    "Pricing": "The pricing page: the Monthly / Yearly segment rail with the \"Save 30%\" badge, the white Free card and lime Plus card with 3D characters, \"Compare features\" and the feature-comparison table.",
    "Reviews": "The reviews page: a wide lime featured-review slide (avatar, quote, \"Try it for free\" pill) with carousel dots, over a grid of testimonial cards.",
    "Our story": "The our-story page: a single editorial column in the display face — \"Our story started with a wish!\" and long-form paragraphs.",
    "Team": "The team page: \"Our Team\" display and a grid of member cards (3D character avatar, name, role).",
    "Figma plugin": "The figma-plugin page: \"Aaply Figma Plugin\" display and numbered export-step cards (Design in aaply → Click export → Follow the link).",
    "Early program": "The Early Users Program page (/early-program). In the sitemap, not linked from nav, footer, or the phone menu. Numbered steps and a lime Sign up for FREE pill that leaves for the app host.",
    "Manual": "The manual page (/manual). Sitemap-only. A display heading over an embedded product video, and a Start new project pill that leaves for the app host.",
    "Mobile (390 wide)": "The same pages as a phone draws them, at 390 x 844 with an iPhone user agent: the burger, the open overlay menu, the hero and the full-width CTAs.",
    "Sign-in boundary": "go.aaply.app — the app host the nav's Log in / Sign up / demo links point at. Every tested route (/login, /sign, /signup, /workspace/demo) returned the bare body \"Not found\" to this client, so no auth surface exists to measure: it is recorded as an unreachable boundary, not captured.",
}

SHOTS = [
    ("home", "Home. Display headline, hero CTAs, product mockup, chat bubbles, black footer; full page.", "/"),
    ("features", "Features. Numbered workflow steps, product panels, mega demo CTA; full page.", "/features"),
    ("value", "Value. Display heading, value cells; full page.", "/value"),
    ("pricing", "Pricing. Billing rail, plan cards, feature table; yearly state and full page.", "/pricing"),
    ("reviews", "Reviews. Featured slide, testimonial grid; full page.", "/reviews"),
    ("our-story", "Our story. The editorial column; full page.", "/our-story"),
    ("team", "Team. Display heading, member grid; full page.", "/team"),
    ("figma-plugin", "Figma plugin. Display heading, export steps; full page.", "/figma_plugin"),
    ("early-program", "Early Users Program. Sitemap-only. Numbered steps, lime Sign up pill; full page.", "/early-program"),
    ("manual", "Manual. Sitemap-only. Display heading, embedded video; full page.", "/manual"),
]
MOBILE = [
    ("mobile-home", "Home at 390: burger, hero, CTAs; full page and the open menu.", "/"),
    ("mobile-pricing", "Pricing at 390; full page.", "/pricing"),
    ("mobile-features", "Features at 390; full page.", "/features"),
    ("mobile-value", "Value at 390; full page.", "/value"),
    ("mobile-reviews", "Reviews at 390; full page.", "/reviews"),
    ("mobile-our-story", "Our story at 390; full page.", "/our-story"),
    ("mobile-team", "Team at 390; full page.", "/team"),
    ("mobile-figma-plugin", "Figma plugin at 390; full page.", "/figma_plugin"),
    ("mobile-early-program", "Early Users Program at 390; full page.", "/early-program"),
    ("mobile-manual", "Manual at 390; full page.", "/manual"),
]

L = []


def W(s=""):
    L.append(s)


shots = sorted(p.name for p in Path("screenshots").glob("*.png"))


def links(prefix):
    out = []
    for f in shots:
        m = re.fullmatch(re.escape(prefix) + r"-light-(.+)\.png", f)
        if m:
            out.append(f"[{m.group(1)}](screenshots/{f})")
    return ", ".join(out)


n_crops = len(list(Path("components/crops").glob("*.png")))
n_states = sum(len(c["states"]) for c in C.values())
icons_idx = Path("icons/INDEX.tsv")
icons = [r.split("\t") for r in icons_idx.read_text().strip().split("\n")[1:]] if icons_idx.exists() else []

read_on = (J["_meta"].get("run") or "")[:10]
W("# aaply components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from aaply.app on {read_on}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was bought, downloaded, signed into, sent or submitted.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Poppins 57/60 700, #000000`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (the marketing site is light, with a black footer band). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). The app host go.aaply.app returned \"Not found\" on /login, /sign, /signup and /workspace/demo, so the authenticated product is listed as an unreachable boundary, not captured. Which control opens which page is in [site-tree.md](site-tree.md).")
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
    ("Monthly billing", "pricing", "the Monthly segment pressed (client-side state, nothing sent)", "[billing-monthly-on](#monthly-option-selected), [plan-price-monthly](#plan-price-monthly)"),
    ("Reviews slide 2", "/reviews", "carousel dot button[aria-label=\"2 of 6\"] clicked; stays on the page", "[reviews-light-slide-2.png](screenshots/reviews-light-slide-2.png)"),
    ("Phone menu", "home at 390", "burger a[href=\"#open-nav\"] clicked; closed with #close-nav", "[mobile-home-light-menu-open.png](screenshots/mobile-home-light-menu-open.png)"),
    ("App host", "go.aaply.app", "nav Log in / Sign up / demo links followed to the app host", "every route returned \"Not found\" — an unreachable boundary, not captured"),
    ("Chat bubbles", "home / features / value", "static annotation bubbles baked into the marketing pages", "measured as elements ([chat-bubble](#chat-annotation-bubble)); no live widget was opened"),
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
failed = []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st or "style" not in st:
        continue
    if "failed" in str(st.get("via", "")):
        failed.append(f"`{k}`")
        continue
    s = st["style"]
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0
    foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else None))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} draw a ring: {', '.join(with_ring) or 'none'}. The other {len(without)} draw none, so a keyboard user sees no change: {', '.join(without)}." + (f" Focus could not be driven to {', '.join(failed)} — its focus state is recorded as not captured." if failed else ""))
W()
W("**Pressed.** Only the nav Sign up pill swaps under :active — black to lime, the same as its hover; the hero and mega demo pills hold black through hover and pressed, and the lime pills hold flat; see the per-component state rows.")
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
# The card-like and chrome surfaces, compared in one table.
for k in ["nav-bar", "plan-card-free", "plan-card-plus", "review-slide", "review-card", "member-card", "value-card", "feature-table", "figma-step", "billing-toggle", "footer"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if "style" in s), None)
    if st is None:
        continue
    p = props(st)
    if ("radius" not in p or p["background"] == "transparent") and st.get("paint"):
        p0 = next((x for x in st["paint"] if x.get("bg") and x.get("radius")), st["paint"][0])
        p = dict(p, border=colour(p0["border"].split(" | ")[0][2:]) if p0.get("border") else "-", radius=p0.get("radius", "-"), background=colour(p0.get("bg", "")) or "-", shadow=colour(p0.get("shadow", ""), tokens=False) or "none")
    W(f"| [{c['title']}](#{re.sub(r'[^a-z0-9 -]', '', c['title'].lower()).replace(' ', '-')}) | {p['size']} | {p.get('border', '-')} | {p.get('radius', '-')} | {p.get('background', '-')} | {p.get('shadow', 'none')} | {p.get('padding', '0')} |")
W()

# ------------------------------------------------ entries
W("## Components")
groups = [g for g in GROUP_INTRO if any(c["group"] == g for c in C.values())]
for c in C.values():
    if c["group"] not in groups:
        groups.append(c["group"])
for g in groups:
    W()
    W(f"### {g}")
    W()
    W(GROUP_INTRO.get(g, ""))
    for k, c in C.items():
        if c["group"] != g:
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
        cl = child_layers(c)
        if cl:
            W(f"Child layers that carry the look: {cl}.")
            W()
        # A crop that is only a published contact address is not kept.
        DROP_CROPS = {"footer-link"}
        imgs = []
        if k not in DROP_CROPS:
            imgs = [f"![{c['title']} {st}](components/crops/{os.path.basename(c['states'][st]['crop'])})" for st in states if c["states"][st].get("crop") and os.path.exists(os.path.join("components", "crops", os.path.basename(c["states"][st]["crop"])))]
        if k in DROP_CROPS:
            W("No crop is kept: the element is the published contact address, which is not written into the package. The values above were read from computed styles.")
        else:
            W(" ".join(imgs) if imgs else "No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.")

# ------------------------------------------------ icons
if icons:
    W()
    W("## Icons")
    W()
    W(f"{len(icons)} SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. The SVGs are Untitled's property, kept for reference only.")
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
W("### Pages")
W()
W("- **The app and everything behind sign-in.** The product itself lives on go.aaply.app (Log in / Sign up / \"Try demo project\" all point there). Probed again on 2026-11-21: /login, /sign, /signup and /workspace/demo each returned HTTP 404 with the body \"Not found\". The host root (https://go.aaply.app/) returned HTTP 200 but the document is not Aaply (a foreign title, no Aaply in the body), so it was not captured and no app package was invented from it. The marketing site is the only measured surface.")
W("- **Sitemap drafts, not product pages.** /page28901772.html (\"Copy of Aaply\", contains a Tilda form that was not submitted), /page29112172.html (\"Blank page\") and /page37280974.html (\"test Pricing\") are in the sitemap and are not opened by any control on the live pages. They were not captured. /workflow is the same walkthrough as /features and was not shot a second time.")
W("- **Anything that sends.** No form was submitted, nothing bought, nothing signed into; the auth-bound pills (Log in, Sign up, the demo CTAs) were hovered and focused but never pressed through.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover), so a state a script adds on mousedown (if any) is missing.")
W("- **The billing toggle's held segment** paints its lime fill on a sibling shape, not on the text atom itself — the segment atoms measure transparent in both positions; the swap is visible in [pricing-light-yearly.png](screenshots/pricing-light-yearly.png).")
W("- **Monthly billing** was reached by pressing the Monthly segment (client-side state, nothing posted); Yearly was restored after.")
W("- **The reviews carousel** was measured on slide 1. Slide 2 was opened by clicking the dot (`button[aria-label=\"2 of 6\"]`) and shot as [reviews-light-slide-2.png](screenshots/reviews-light-slide-2.png). Slides 3 to 6 use the same control and were not shot.")
W()
W("### Themes")
W()
W("The marketing site paints one theme — light surfaces with a black footer band. Tilda declares no `[data-theme]` overrides and the app (which may theme differently) was never reached.")
W()
W("### Fonts")
W()
W("- **Poppins** (display, 700 and 500) and **Inter** (UI, 400 / 500 / 300) load from Google Fonts via stylesheet link, so they do not appear in the page's own @font-face rules (`fonts` in [raw/css-vars.json](raw/css-vars.json) is empty). The style guide renders them with the system fallback stack.")
W()
W("### Screenshots")
W()
W("- Screens and product imagery are aaply.app's content and appear only inside screenshots and crops.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- No personal data was captured: every page was read signed out with an empty session, and the only presses were the Monthly billing toggle; no text was ever typed into a form.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops,", len(icons), "icons")
