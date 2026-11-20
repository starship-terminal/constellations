#!/usr/bin/env python3
"""Build components.md for the Grammarly design reference.

Reads raw/components-computed.json (every component and state, measured), raw/layout.json,
tokens.json, screenshots/ and icons/INDEX.tsv, and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the palette token whose
value matches, the font family is named once per value, and a state row shows only what differs
from the first state. Adapted from the public-capture kit's builder.

Deterministic: re-running it on the same inputs reproduces components.md byte for byte.
Run from anywhere: python3 tools/build_components_md.py
"""
import json, os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
J = json.load(open("raw/components-computed.json"))
C = J["components"]
LAYOUT = json.load(open("raw/layout.json"))
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


def measured(s):
    """A state that was really reached. A failed focus (via: "focus failed", skipped, or
    focus.matches false) holds the resting element's values and is left out of tables,
    crops and tallies, as the kit does (PR 932)."""
    return ("style" in s and s.get("via") != "focus failed" and not s.get("skipped")
            and (s.get("focus") or {}).get("matches") is not False)


def state_rows(c):
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

PAGE_NAME = {"home": "home", "features": "features", "plans": "plans",
             "grammar-check": "grammar checker", "contact-sales": "contact sales", "signin": "sign-in"}

GROUP_INTRO = {
    "Shell and navigation": "The marketing shell shared by every public page: a 65px sticky header with the Grammarly lockup, the Product/Work/Education/Resources menu buttons, the Pricing link and the Request a demo / Log in / Sign Up cluster. The Product menu opens a flyout panel (a UI toggle, no navigation).",
    "Buttons": "The site's rounded-rectangle buttons (the `base-module_basic__*` family): the green primary, the bordered secondary and the ghost variants, plus the round carousel arrows.",
    "Pricing": "The plans page: a three-column plan grid (Free, Pro, Enterprise), the featured Pro card with its Most-popular header and Try-for-free tag, the per-plan CTAs, the Compare Plans table with its info icon buttons and the FAQ accordion. The captured page paints no billing-period switch.",
    "Feature pages": "The features page's pill tabs (Paragraph rewrites, Proofreading, Clarity, ...) that swap the demo panel.",
    "Writing tools": "The sticky secondary nav strip the free tools share (Grammar Check, Plagiarism Checker, Paraphrasing Tool, ...), each item an icon plus a label, the current tool marked.",
    "Grammar checker": "The free grammar checker at /grammar-check: a two-column panel — the contenteditable writing area at the left, the Suggestions rail at the right. A sample sentence was typed to watch the checker underline issues and fill the rail, then deleted; nothing was submitted.",
    "Forms": "The contact-sales lead form: labelled required fields, selects and the Submit button. Fields were clicked and sample text typed and deleted; nothing was submitted.",
    "Footer": "The site foot: link columns, the legal bar and the social icons.",
    "Dialogs and overlays": "The sign-in page's dialog over the dimmed home page — the email field, the provider rows and the Continue button. Shot and measured, never submitted.",
    "Content and cards": "The home page's content furniture: the Matter hero, the capability cards in the carousel, the dark enterprise strip's stat cards, the promo banner and the dark marketing sections.",
    "Mobile (390 wide)": "A few components as a phone draws them, at 390 x 844 with a mobile user agent.",
}

SHOTS = [
    ("home", "Home. Matter hero, capability carousel, the dark enterprise strip, customer stats, the footer. The Product flyout captured open.", "/"),
    ("features", "Features. The pill tabs and the feature panels; the Proofreading tab selected.", "/features"),
    ("plans", "Plans. Three plan columns, the Pro card marked Most popular, the comparison table and FAQ.", "/plans"),
    ("enterprise", "Enterprise landing.", "/business/enterprise"),
    ("business", "Grammarly Business landing.", "/business"),
    ("professionals", "The professionals page.", "/professionals"),
    ("students", "The students page.", "/students"),
    ("edu", "Grammarly for Education.", "/edu"),
    ("ai", "The AI product page.", "/ai"),
    ("ai-agents", "The AI agents page.", "/ai-agents"),
    ("grammar-check", "The free grammar checker: editor and Suggestions rail, empty and with a sample sentence analysed (deleted after).", "/grammar-check"),
    ("plagiarism-checker", "The plagiarism checker tool.", "/plagiarism-checker"),
    ("paraphrasing-tool", "The paraphrasing tool, empty and with a sample sentence (deleted after).", "/paraphrasing-tool"),
    ("ai-detector", "The AI detector tool.", "/ai-detector"),
    ("word-counter", "The word counter tool.", "/word-counter"),
    ("desktop", "The desktop apps page.", "/desktop"),
    ("browser", "The browser extensions page.", "/browser"),
    ("trust", "The trust and security page.", "/trust"),
    ("contact-sales", "The contact-sales form; a field focused.", "/contact/sales"),
    ("signin", "The sign-in dialog over the dimmed home page, empty and with a placeholder email typed and deleted. Never submitted.", "/signin"),
    ("signup", "The sign-up page.", "/signup"),
    ("blog", "The blog index.", "/blog/"),
]
MOBILE = [
    ("mobile-home", "Home at 390: header, hero, the open navigation sheet and the full page.", "/"),
    ("mobile-plans", "Plans at 390.", "/plans"),
    ("mobile-grammar-check", "The grammar checker at 390.", "/grammar-check"),
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
icons = [r.split("\t") for r in open("icons/INDEX.tsv").read().strip().split("\n")[1:]]

W("# Grammarly components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from www.grammarly.com on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent or uploaded.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [raw/layout.json](raw/layout.json).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Matter 14/21 500, #21252e`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (grammarly.com paints one light theme on its public pages; the dark values the stylesheets declare are in tokens.json but were never painted). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).")
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
    ("Product flyout", "the nav, every page", "the Product menu button (a UI toggle); closed with Escape afterwards", "[home-light-nav-product-open](screenshots/home-light-nav-product-open.png), [nav-panel](#nav-panel)"),
    ("Feature tab, selected", "features", "the tab itself pressed (a UI toggle)", "[features-light-tab-proofreading](screenshots/features-light-tab-proofreading.png), [tab-selected](#tab-selected)"),
    ("Checker, filled", "grammar checker", "a sample sentence typed into the free editor, analysed, then deleted; never submitted", "[grammar-check-light-filled](screenshots/grammar-check-light-filled.png), [checker-filled](#checker-filled)"),
    ("Paraphraser, filled", "paraphrasing tool", "a sample sentence typed, then deleted; never submitted", "[paraphrasing-tool-light-filled](screenshots/paraphrasing-tool-light-filled.png)"),
    ("Form field, focused", "contact sales", "a field clicked into; nothing typed or sent", "[contact-sales-light-field-focused](screenshots/contact-sales-light-field-focused.png)"),
    ("Email field, filled", "sign-in", "the placeholder name@example.com typed, shot, deleted; never submitted", "[signin-light-email-filled](screenshots/signin-light-email-filled.png), [signin-email](#signin-email)"),
    ("Mobile navigation sheet", "home at 390", "the menu's own Open button; closed with its Close button", "[mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu](#m-menu)"),
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
failed_focus = []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st or "style" not in st:
        continue
    if st.get("via") == "focus failed" or st.get("skipped") or (st.get("focus") or {}).get("matches") is False:
        failed_focus.append(f"`{k}`")  # focus never held: uncaptured, not "draws none"
        continue
    s = st["style"]
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0
    foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else None))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} draw a ring: {', '.join(with_ring)}. The other {len(without)} draw none, so a keyboard user sees no change: {', '.join(without)}." + (f" Focus could not be held on {len(failed_focus)} more ({', '.join(failed_focus)}), so their focus look is uncaptured, not absent." if failed_focus else ""))
W()
W("**Pressed.** Pressed was forced with DevTools (`:active` + `:hover` forced on the node), so no link, submit or sign-in control could fire. The `--button-*-background-active` tokens say the buttons change fill on press rather than transform; the state rows below record what was actually painted.")
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
W("**Layout grid.** Read on each page at each width ([raw/layout.json](raw/layout.json)).")
W()
W("| Page | 1440 | 1920 | 1024 | 390 |")
W("|---|---|---|---|---|")


def grid_of(key):
    v = LAYOUT.get(key)
    if not v:
        return "-"
    g = v["grids"][0] if v["grids"] else None
    cols = re.sub(r"(\d+\.\d)\d*px", r"\1", g["cols"]).replace("px", "") if g else ""
    main = f"content x {v['main']['x']}, {v['main']['w']} wide" if v["main"]["w"] else "content full width"
    return f"{main}; grid {cols} gap {g['colGap']}" if g else main


for page in ["home", "plans", "features", "grammar-check"]:
    W(f"| {page} | " + " | ".join(grid_of(f"{page}@{w}") for w in (1440, 1920, 1024, 390)) + " |")
W()
W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
def covers(layer, st, share=0.9):
    """True when a painted layer's box is at least `share` of the root's area."""
    try:
        w, h = (float(v) for v in str(layer.get("size", "")).split("x"))
        return w * h >= share * st["rect"]["w"] * st["rect"]["h"] > 0
    except (ValueError, KeyError, TypeError):
        return False


# The card-like components to compare in one table.
for k in ["feature-card", "stat-card", "plan-card", "plan-card-plain", "banner", "section-dark", "signin-dialog", "checker", "suggestions-panel", "suggestion-card", "m-menu"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if "style" in s), None)
    if st is None:
        continue
    p = props(st)
    p0 = None
    if ("radius" not in p or p["background"] == "transparent") and st.get("paint"):
        # borrow the card shape only from a painted layer that covers at least 90% of the
        # root box: a banner strip, CTA, input or menu button is not the card
        # root box: a banner strip, CTA, input or menu button is not the card. The covering layer
        # may paint only some of fill, border, radius and shadow; each one it lacks keeps the root's.
        p0 = next((x for x in st["paint"] if covers(x, st) and any(x.get(k) for k in ("bg", "border", "radius", "shadow"))), None)
    if p0:
        p = dict(p)
        if p0.get("border"):
            p["border"] = colour(p0["border"].split(" | ")[0][2:])
        if p0.get("radius"):
            p["radius"] = p0["radius"]
        if p0.get("bg"):
            p["background"] = colour(p0["bg"]) or p.get("background", "-")
        if p0.get("shadow"):
            p["shadow"] = colour(p0["shadow"], tokens=False) or "none"
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
        failed = [s for s, v in c["states"].items() if "style" in v and not measured(v)]
        if failed:
            W(f"**Focus not capturable.** A real keyboard focus could not be held on this element ({', '.join(f'`{s}`' for s in failed)}), so its focus look is uncaptured, not measured as absent.")
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
W(f"{len(icons)} SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. The marketing illustrations and logo walls were left out; these are the interface icons. The SVGs are Grammarly's property, kept for reference only.")
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
W("- **Signed-in pages.** Nothing behind sign-in was captured: the Grammarly editor and dashboard, documents, account and subscription settings, the workspace and admin consoles, and any app.grammarly.com surface. The kit never signs in.")
W("- **Anything that sends or creates.** No form was submitted (contact sales, sign-in, newsletter), no checkout or trial was started, and no tool's output was generated — the free checker's analysis of the typed sample was captured, but the plagiarism checker, AI detector, paraphraser and word counter only produce their result views after a submit action the kit never performs.")
W("- **Blog articles.** Only the blog index was captured; article pages were not traversed.")
W("- **Support and community.** The help centre, community forum and status pages sit on other subdomains and were not captured.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Disabled states** were not seen on any public control.")
W("- **Live suggestion cards** never painted: the free checker's issue underlines and Accept/Dismiss cards are rendered by a product overlay outside the page's light DOM, and no public selector matches them (`suggestion-card` is recorded missing). What a signed-out visitor does see — the '3 Suggestions' header and the get-started steps — was captured instead.")
W()
W("### Themes")
W()
W("grammarly.com shows one light theme on its public pages, but its stylesheets declare a full dark theme: the GDS layer under `[data-gds-theme=\"dark\"]` and the Origin layer under `[data-origin-theme=\"grammarly\"][data-origin-mode=\"dark\"]`. No public page mounts those attributes, there is no theme switch anywhere, and `prefers-color-scheme: dark` changes nothing (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)). The token file ships the dark set anyway — every value is labelled as declared evidence, resolved synthetically, never painted. The same stylesheets also carry Superhuman and Coda themes (sibling Grammarly Inc. products sharing the Origin system); only the grammarly theme was resolved.")
W()
W("### Fonts")
W()
W("- **Matter** is Grammarly's self-hosted display face; it is served from Grammarly's CDN and is not in the style guide, which falls back to Inter — the same fallback the token stacks name.")
W("- **Super Sans Mono VF** and **Super Serif VF** are Superhuman's brand faces in the Origin stacks; they resolve to the platform fallbacks here.")
W()
W("### Screenshots")
W()
W("- Illustrations, customer logos, product imagery and video frames are Grammarly's content and appear only inside screenshots and crops. Hero and feature sections animate, so two captures of the same view can differ in the frame drawn.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Marketing copy inside screenshots and crops is Grammarly's content, kept as captured for layout and proportion reference only.")
W("- No personal data was captured: the pages were read signed out, and the only text ever typed was throwaway sample text, deleted in place.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops,", len(icons), "icons")
