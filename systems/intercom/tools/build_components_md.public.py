#!/usr/bin/env python3
"""Build components.md for the Intercom design reference.

Reads raw/components-computed.json (every component and state, measured), raw/layout.json,
tokens.json, screenshots/ and icons/INDEX.tsv, and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the palette token whose
value matches, the font family is named once per value, and a state row shows only what differs
from the first state. Adapted from the public-capture kit's builder.

Deterministic: re-running it on the same inputs reproduces components.md byte for byte.
Run from anywhere: python3 tools/build_components_md.public.py
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
for n, t in flat(T["core"]["color"]):
    if t["$type"] == "color":
        BY_COLOR.setdefault(t["$value"], n)


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def _gam(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def _oklab(L, a, b):
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541729 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    r = +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    bl = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    return tuple(max(0, min(255, round(_gam(c) * 255))) for c in (r, g, bl))


def colour(c, tokens=True):
    """rgb()/rgba()/color(srgb)/oklab()/oklch() -> '#hex `token`' or 'rgba(...)'."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        tok = BY_COLOR.get(v) if tokens else None
        return f"{v} `{tok}`" if tok else v

    def _okr(m):
        L, a, b = float(m.group(1)), float(m.group(2)), float(m.group(3))
        r, g, bl = _oklab(L, a, b)
        al = m.group(4)
        return label(norm(r, g, bl, al))

    import math
    c = re.sub(r"oklab\(([-\d.]+) ([-\d.]+) ([-\d.]+)(?: / ([\d.]+))?\)", _okr, c)
    c = re.sub(r"oklch\(([-\d.]+) ([-\d.]+) (-?[\d.]+|none)(?: / ([\d.]+))?\)",
               lambda m: label(norm(*_oklab(float(m.group(1)), float(m.group(2)) * math.cos(math.radians(0.0 if m.group(3) == "none" else float(m.group(3)))), float(m.group(2)) * math.sin(math.radians(0.0 if m.group(3) == "none" else float(m.group(3))))), m.group(4))), c)
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
        o["border"] = bds[0] if len(set(bds)) == 1 else "; ".join(f"{'TRBL'[i]}: {b} {bds[i]}" for i, b in enumerate(bds) if b != "none")
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
                # props() omits a resting value (opacity 1, no radius). "none"
                # is not a valid opacity, so keep the measured reset.
                diff[k] = "1" if k == "opacity" else "none"
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

PAGE_NAME = {"home": "Home", "pricing": "Pricing", "contact-sales": "Contact sales", "help": "Help center",
             "changes": "Changelog", "blog": "Blog", "helpdesk": "Helpdesk"}

GROUP_INTRO = {
    "Shell and navigation": "The chrome every marketing page shares: the \"Introducing Fin 4\" promo banner, the shared header (`header.shared-header`) with the wordmark, Product/Customers/Resources mega-menu triggers, Pricing, Log in, Contact sales, View demo and the black \"Start free trial\" CTA. Everything is ghost-on-white until hover, when the chalk fill (`--color-nav-background-highlight`) shows.",
    "Home": "The intercom.com home page: a cream ground (`--body-bg` = `--color-cream`) under a Saans hero, eyebrow labels in SaansMono, and cards bordered at black 6%.",
    "Pricing": "The pricing page: the billed-annually/monthly segmented control, the helpdesk-blue savings badge, the plan columns and the FAQ accordion.",
    "Contact sales form": "The first step of the contact-sales form: labels, a text field, the company-size select and its listbox, the opt-in checkbox and the Next button. Nothing was typed past the throwaway filled-state reading (sample text typed and immediately deleted), nothing advanced, nothing sent.",
    "Help center": "intercom.com/help/en/, the Intercom help center: its own header and search, article cards and the docs navigation. A separate surface from the marketing shell.",
    "Changelog": "intercom.com/changes/en, the release-notes feed: the older `header__lite` surface (#f3f5f7 ground, `div.paper.newsfeed__newsitem` cards) running the MediumLL-era styles under `.intercom-legacy`.",
    "Blog": "intercom.com/blog: the article index list over a white band.",
    "Footer": "The site footer shared by every page: link columns, social icons, the locale selector and the legal row on the cream ground.",
    "Mobile (390 wide)": "A few components as a phone draws them, at 390 x 844 with a mobile user agent: the header collapses to the wordmark plus the menu button, which opens a full-height navigation sheet.",
}

SHOTS = [
    ("home", "Home. The Fin 4 promo banner, shared header, hero, logo wall, feature sections and the footer; the Product mega-menu opened.", "/"),
    ("pricing", "Pricing. Billing toggle, savings badge, plan columns, FAQ (one item opened).", "/pricing"),
    ("helpdesk", "Helpdesk product page.", "/helpdesk"),
    ("inbox", "Inbox product page (a very tall page: the full shot is stitched from two parts).", "/helpdesk/inbox"),
    ("copilot", "Copilot product page.", "/helpdesk/copilot"),
    ("customers", "Customers page.", "/customers"),
    ("integrations", "Integrations page.", "/integrations"),
    ("security", "Security page.", "/security"),
    ("view-demos", "View demos page.", "/view-demos"),
    ("contact-sales", "Contact sales. The first form step and the company-size select opened.", "/contact-sales"),
    ("why-choose", "Why choose Intercom.", "/why-choose-intercom"),
    ("enterprise", "Enterprise page.", "/enterprise"),
    ("blog", "Blog index.", "/blog"),
    ("help", "Help center home.", "/help/en/"),
    ("changes", "Changelog.", "/changes/en"),
]
MOBILE = [
    ("mobile-home", "Home at 390: header collapsed to wordmark plus menu button; the menu sheet opened.", "/"),
    ("mobile-pricing", "Pricing at 390.", "/pricing"),
    ("mobile-helpdesk", "Helpdesk at 390.", "/helpdesk"),
    ("mobile-help", "Help center at 390.", "/help/en/"),
    ("mobile-contact-sales", "Contact sales at 390.", "/contact-sales"),
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
icons = [r.split("\t") for r in open("icons/INDEX.tsv").read().strip().split("\n")[1:]] if Path("icons/INDEX.tsv").exists() else []

W("# Intercom components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from www.intercom.com on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent or uploaded.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [raw/pages.md](raw/pages.md).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Saans 64/64 400, #111111`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (the site paints one theme, `body.theme-light`). Desktop shots are 1440 x 900 at 1x (the PNG matches the viewport); `-full` shots are whole pages at the same 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). A page taller than one GPU texture is stitched from `-full.partN.png` tiles into one `-full.png`. Component crops stay at 2x.")
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
    ("Nav mega-menu", "home header", "the Product trigger pressed (opened and left open)", "[home-light-nav-menu](screenshots/home-light-nav-menu.png), [nav-menu](#nav-mega-menu)"),
    ("FAQ accordion item", "pricing", "its own question row pressed", "[pricing-light-faq](screenshots/pricing-light-faq.png), [faq-item](#faq-accordion-item)"),
    ("Select listbox", "contact sales", "the company-size select's own button pressed; no option chosen", "[contact-sales-light-select-open](screenshots/contact-sales-light-select-open.png), [select-popup](#select-popup)"),
    ("Mobile menu sheet", "home at 390", "the menu button pressed (opened, then dismissed with Escape)", "[mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-overlay](#mobile-menu-overlay)"),
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
none = f" The other {len(without)} draw none: {', '.join(without)}." if without else ""
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} draw a ring: {', '.join(with_ring)}.{none} The measured rings are black (`#101010`) on the desktop controls and orange (`#e59700`) on the mobile menu button. The declared `--color-focus-outline` (`--color-blue`, #000ce1) is a stylesheet value; these controls did not paint it.")
W()
W("**Hover and pressed.** The primary buttons (nav CTA, hero CTA, the form's Next) repaint rather than transform: `--button-primary-hover-background` is the helpdesk blue #0007cb, the pressed state the same blue at 85%. Ghost nav items fill with `--color-chalk` on hover. Pressed was forced with DevTools, so a state a script adds on mousedown (if any) is missing.")
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


for page in ["home", "pricing", "helpdesk", "help", "contact-sales", "blog"]:
    W(f"| {page} | " + " | ".join(grid_of(f"{page}@{w}") for w in (1440, 1920, 1024, 390)) + " |")
W()
W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
for k in ["feature-card", "plan-card", "promo-badge", "nav-menu", "faq-item", "input", "select", "select-popup", "help-card", "blog-card", "changes-entry", "m-menu-overlay"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if "style" in s), None)
    if st is None:
        continue
    p = props(st)
    # A transparent card or a card with no radius keeps its own values. A child's
    # fill, radius or border belongs to that child, not the card.
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
            W(c.get("captureNote") or "Not on the page when it was captured.")
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
W(f"{len(icons)} SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Marketing illustrations and product imagery were left out; these are the interface icons. The SVGs are Intercom's property, kept for reference only.")
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
W("- **Signed-in pages.** Nothing behind sign-in was captured: the Intercom app itself (app.intercom.com inbox, tickets, reports), trial onboarding at /signup, and any account surface. The kit never signs in and never follows a Log in or Start free trial link.")
W("- **Anything that sends or creates.** No form was submitted: the contact-sales form was never advanced past its first step (Next was measured with forced pseudo states, never pressed), no demo was booked, no search was run, no option was chosen in the company-size select, the marketing checkbox was never ticked, and no trial was started.")
W("- **Careers and docs.** `/careers` and `developers.intercom.com` were left out of scope; the capture covers the marketing site, the help center and the changelog.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every button and link, so a state a script adds on mousedown (if any) is missing.")
W("- **Hover on the plan cards, the article rows and the billing toggle's unselected half** changed nothing measurable; their entries read 'same'.")
W("- **The promo banner's close** was exercised by the capture kit itself; no banner dismissal state is stored.")
W("- **Disabled states** were not seen on any public control.")
W()
W("### Themes")
W()
W("www.intercom.com paints one light theme (`body.theme-light`). Its stylesheets do not declare a dark surface: no `prefers-color-scheme` dark rules that repaint the marketing pages, no dark class or attribute anywhere, and a forced `prefers-color-scheme: dark` pass changed nothing (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)). The token file therefore ships no dark set.")
W()
W("### Fonts")
W()
W("- **Saans**, **SaansMono** and **Serrif** are Intercom's own faces, declared by `@font-face` on the page. Serrif is declared and styled (`.brand-i2y4`'s `--font-serif`) but no captured page painted it, so the style guide falls back where it would have been used.")
W("- **MediumLL**, **IvoryLL** and **DmMono** are the older help/changelog faces under `.intercom-legacy`.")
W("- **Beretta, Honey, Maxi, Ozik, Planar and Raster** are campaign display faces loaded by `next/font` variable classes for one-off sections.")
W()
W("### Screenshots")
W()
W("- Product screenshots, campaign illustrations and customer logos are Intercom's content and appear only inside screenshots and crops. Animated sections (hero canvases, marquee rows) keep moving, so two captures of the same view can differ.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Article and release-note body text was not transcribed; only the frames around it were measured.")
W("- No personal data was captured: the pages were read signed out, the contact form was never advanced, and the one filled-field reading typed and deleted a placeholder address that belongs to no one.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops,", len(icons), "icons")
