#!/usr/bin/env python3
"""Build components.md for the Ableton design reference.

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

PAGE_NAME = {"home": "home", "live": "Live", "push": "Push", "move": "Move", "note": "Note",
             "link": "Link", "trial": "trial", "shop": "shop", "packs": "Packs", "blog": "blog",
             "about": "about", "help": "help", "jobs": "jobs", "login": "log in / register",
             "mobile": "mobile home"}

GROUP_INTRO = {
    "Shell and navigation": "The shell every marketing page shares: a 69px top bar with the grid-mark logo, the product links (Live / Push / Move / Note / Link / Shop / Packs / Help), a \"More\" disclosure, \"Try Live 12 for free\" in signature blue and \"Log in or register\"; and the fat white footer with heading columns, the newsletter form, locale picker and social buttons. Everything is square: no rounded corners anywhere.",
    "Home": "The home page is a grid of full-bleed photo/video teaser cells (one cell per product or story) under a hero, plus a striped promo card and a blog-teaser panel. Text sits on the photography in white, always Futura PT bold.",
    "Consent overlay": "Ableton's cookie consent (`#biscuits-overlay`): a black card pinned to the bottom of every page, with Accept in signature blue, and Close / More info as 2px-outline buttons. It was captured as found; Accept was never clicked (the capture hides the overlay by CSS for the clean shots, which is a hide, not a consent).",
    "Live page": "The Live product page: the biggest marketing surface (21k px tall at 1440), all dark photo bands and white type. Its own button set: Try (boxed outline), Buy (boxed deep-blue fill), Watch-video and Play-audio buttons, deep-blue anchor links, and the feature-collapse rows that open with a 2px blue border.",
    "Content pages": "The rest of the product and editorial pages share the home's vocabulary: 60px display titles, text on photography, a signature-blue or boxed CTA. Push, Move, Note and Link are product pages; about/help/jobs are the editorial trio.",
    "Trial page": "The trial landing: a title, the edition cards and the signature-blue Download buttons. Nothing was ever downloaded.",
    "Shop": "The shop index: product cards with a photo, a name, a price and an add-to-cart control. Nothing was added or bought.",
    "Packs": "The Packs catalogue: a 40k px grid of pack cards (artwork, name, genre tags) with signature-blue download/buy controls. Nothing was bought or downloaded.",
    "Blog": "The blog index: a title, then rows of posts each carrying a salmon category badge.",
    "Log in / register (resting only)": "The account page's two forms side by side: Log in (email + password + submit) and Register (email + country select + terms checkbox + submit). Captured at rest and focused only: no credentials were ever typed and neither form was submitted.",
    "Mobile (390 wide)": "A few components as a phone draws them, at 390 x 844: the collapsed top bar with its hamburger trigger, the hero title at 20px, the trial CTA.",
}

SHOTS = [
    ("home", "Home. Hero teaser, the photo-cell grid, striped promo card, blog teasers, footer. The cookie banner and the opened More menu captured as separate states.", "/en/"),
    ("live", "Live. The 21k px product page: display titles, Try/Buy buttons, video and audio controls, feature collapses, dark photo bands.", "/en/live/"),
    ("push", "Push. Product hero and feature sections.", "/en/push/"),
    ("move", "Move. Product hero and feature sections.", "/en/move/"),
    ("note", "Note. Product hero and feature sections.", "/en/note/"),
    ("link", "Link. Product page and the Link-enabled-products CTA.", "/en/link/"),
    ("trial", "Trial. Edition cards and Download buttons.", "/en/trial/"),
    ("shop", "Shop index. Product cards with prices and add-to-cart.", "/en/shop/"),
    ("packs", "Packs catalogue. The 40k px grid of pack cards.", "/en/packs/"),
    ("blog", "Blog index. Post rows with salmon category badges.", "/en/blog/"),
    ("about", "About. The company page.", "/en/about/"),
    ("help", "Help. Support sections and links.", "/en/help/"),
    ("jobs", "Jobs. Openings list.", "/en/jobs/"),
    ("login", "Log in / register. Both forms at rest; nothing submitted.", "/en/login/"),
]
MOBILE = [
    ("mobile-home", "Home at 390: collapsed nav, hero teaser, the cell grid single-column.", "/en/"),
    ("mobile-live", "Live at 390.", "/en/live/"),
    ("mobile-shop", "Shop at 390.", "/en/shop/"),
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

W("# Ableton components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from www.ableton.com on {J['_meta']['run'][:10]}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought, downloaded, sent or submitted, and the cookie consent was never answered (it was hidden for the clean captures, which is not a consent).")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts at four widths are in [raw/layout.json](raw/layout.json).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `futura-pt 20/30 700, #000000`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (Ableton has one theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 390 wide.")
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
    ("Cookie consent card", "every page, on load", "at rest; hidden by CSS for every clean capture, never accepted or closed", "[home-light-cookie-banner](screenshots/home-light-cookie-banner.png), [cookie-bar](#cookie-bar)"),
    ("Nav \"More\" panel, open", "home", "the More button pressed (opens the disclosure)", "[home-light-more-menu](screenshots/home-light-more-menu.png), [nav-more-panel](#nav-more-panel)"),
    ("Feature collapse, open", "Live", "the collapse row's own toggle pressed (a local UI disclosure)", "[collapse-toggle-open](#collapse-toggle-open)"),
    ("Video / audio players", "Live", "measured at rest; Play was never pressed (media streams and modals stay uncaptured)", "[btn-video](#btn-video), [btn-audio](#btn-audio)"),
    ("Form focus", "footer newsletter, login and register", "tabbed or clicked into; sample text typed and deleted on the field-measurement pass, nothing sent", "[newsletter-field](#newsletter-field), [login-field](#login-field), [register-field](#register-field)"),
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
    if not st or "style" not in st:
        continue
    s = st["style"]
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0
    foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else None))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} draw a ring: {', '.join(with_ring)}. The other {len(without)} draw none, so a keyboard user sees no change: {', '.join(without)}. Ableton uses two rings: the browser's `auto 1px #005fcc` on text links, and a deliberate `solid 2px #ff764d` orange on the boxed buttons.")
W()
W("**Pressed.** Forced `:active` changed almost nothing measurable on Ableton: the deep-blue Buy button darkens to `#042b9f` (its hover colour) and everything else reads the same as default. The site's controls do not shrink or recolour under the finger; hover on most `abl-button`s is likewise a no-op, with the boxed Try button instead swapping its text from blue to black.")
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


for page in ["home", "live", "packs", "shop", "trial", "blog", "about", "login"]:
    W(f"| {page} | " + " | ".join(grid_of(f"{page}@{w}") for w in (1440, 1920, 1024, 390)) + " |")
W()
W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
# The card-like components to compare in one table.
for k in ["home-promo-card", "blog-teaser", "product-card", "pack-card", "trial-edition-card", "collapse-toggle", "cookie-bar", "newsletter-field", "login-field", "register-select"]:
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
        imgs = [f"![{c['title']} {st}](components/crops/{os.path.basename(c['states'][st]['crop'])})" for st in states if c["states"][st].get("crop")]
        W(" ".join(imgs) if imgs else "No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.")

# ------------------------------------------------ icons
W()
W("## Icons")
W()
W(f"{len(icons)} SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Photography and product artwork were left out; these are the interface icons (the grid-mark logo, the social buttons, the video/audio play badges, a disclosure chevron). The SVGs are Ableton's property, kept for reference only.")
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
W("- **Everything behind the account.** The login and register forms were measured at rest and focus only: no credentials were entered and nothing was submitted, so the signed-in account area (licenses, downloads, order history, settings, the forum, the ableton.com user section) is completely uncaptured.")
W("- **The checkout.** Add-to-cart was never pressed and no purchase flow was started, so the cart, checkout and payment steps are missing.")
W("- **Downloads.** The trial Download and the Packs' download/buy controls were measured but never pressed; no file was fetched.")
W("- **Learning microsites.** `learn.ableton.com`, `learningsynths.ableton.com` and `makingmusic.ableton.com` are separate Ableton properties with their own front ends; they were linked but not captured.")
W("- **A few public sections were skipped for scope:** the Classroom, Colleges & Universities, Certified Training and Ausbildung pages were probed and are plain content pages in the same shell; they add no new components.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools (`:active`), so a state a script adds on mousedown is missing if one exists.")
W("- **The consent states.** Accept / Close / More-info were measured but never clicked: the post-consent UI (whatever the site does once you answer) is uncaptured.")
W("- **Video and audio.** The Live page's play buttons open a YouTube modal or start an audio player; neither was started, so the players are measured at rest only.")
W("- **The mobile menu overlay** was probed through `m-menu-trigger` but its opened full-screen menu was not captured as a screenshot state.")
W("- **Disabled states** were not seen on any public control.")
W()
W("### Themes")
W()
W("Ableton shows one light theme. Its stylesheets declare no CSS custom properties at all (`raw/css-vars.json` resolves zero rules; the only unreadable sheets were the two cross-origin Adobe Typekit kit sheets), no `prefers-color-scheme` variant and no theme attribute, so the token file ships a single `light` set and every colour is a measured literal rather than a variable alias.")
W()
W("### Fonts")
W()
W("- **Futura PT** is served from Adobe Typekit (`use.typekit.net`), whose sheets are cross-origin to CSSOM reads; the family name and weights are measured on the rendered elements instead, and the style guide falls back to a system sans for display.")
W()
W("### Screenshots")
W()
W("- Photography, product artwork and video frames are Ableton's content and appear only inside screenshots and crops. Hero cells carry video, so two captures of the same page can differ in the frame shown.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Article body text, product copy and form option lists were not transcribed; only the frames around them were measured.")
W("- No personal data was captured: every page was read signed out, and the only forms touched were fields measured and left empty.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops,", len(icons), "icons")
