#!/usr/bin/env python3
"""Build components.md for the Aboard design reference.

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


LAYER_KEYS = ("bg", "bgImage", "border", "radius", "shadow", "outline")


def is_root_layer(st, p):
    """The paint list starts with the component's own element when it paints; a
    same-tag, same-size first entry is that element, not a child."""
    if p["node"].split(".", 1)[0].split(":", 1)[0] != st.get("tag"):
        return False
    try:
        w, h = p["size"].split("x")
        return abs(float(w) - st["rect"]["w"]) < 0.6 and abs(float(h) - st["rect"]["h"]) < 0.6
    except Exception:
        return False


def child_paint(st):
    """Painted layers below the root element."""
    return [p for p in st.get("paint") or [] if not is_root_layer(st, p)]


def paint_diff(base_v, v):
    """Changes in the painted layers between two states, as 'node: key value' bits.
    The root comparison alone misses hovers the site paints on children (the case
    cards lift on the figure's shadow, not the card root)."""
    a = {p["node"]: p for p in child_paint(base_v)}
    b = {p["node"]: p for p in child_paint(v)}
    out = []
    for node, p in b.items():
        prev = a.get(node, {})
        bits = []
        for k in LAYER_KEYS:
            if p.get(k) == prev.get(k):
                continue
            val = colour(p[k])[:160] if k in ("bg", "bgImage", "border", "shadow", "outline") else p[k]
            bits.append(f"{k} {val}")
        if bits:
            out.append(f"{node}: {', '.join(bits)}")
    return out


def state_rows(c):
    states = [s for s in c["states"] if "style" in c["states"][s]]
    if not states:
        return [], states
    base = props(c["states"][states[0]])
    rows = [(states[0], base, [])]
    same = []
    for st in states[1:]:
        p = props(c["states"][st])
        diff = {k: p[k] for k in ORDER if k in p and p.get(k) != base.get(k)}
        for k in ORDER:
            if k in base and k not in p:
                diff[k] = "none"
        layers = paint_diff(c["states"][states[0]], c["states"][st])
        if not diff and not layers:
            same.append(st)
            continue
        if rows[-1][0] != states[0] and rows[-1][1] == diff and rows[-1][2] == layers:
            rows[-1] = (rows[-1][0] + ", " + st, diff, layers)
        else:
            rows.append((st, diff, layers))
    if same:
        rows[0] = (f"{states[0]} (same: {', '.join(same)})", base, [])
    return rows, states


def fmt(d):
    return "; ".join(f"{k} {d[k]}" for k in ORDER if k in d).replace("|", "/")


def child_layers(c):
    st = next((s for s in c["states"].values() if "style" in s), None)
    if not st or not st.get("paint"):
        return None
    s = st["style"]
    # A painted background/image/shadow on the root already carries the look; a
    # hairline border alone does not, so the children's paint still gets named.
    if s["backgroundColor"] != "rgba(0, 0, 0, 0)" or s["boxShadow"] != "none" or s["backgroundImage"] != "none":
        return None
    out = []
    for p in child_paint(st)[:3]:
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

PAGE_NAME = {"home": "home", "how-we-work": "How We Work", "case-studies": "case studies",
             "case-study": "case study", "foundry": "Foundry", "perspectives": "Perspectives",
             "newsletter": "newsletter", "podcast": "podcast", "podcast-episode": "podcast episode",
             "events": "events", "media": "media", "about": "about", "faq": "FAQ",
             "careers": "careers", "security": "security", "aboard-sign": "newsletter article",
             "mobile": "mobile home"}

GROUP_INTRO = {
    "Shell and navigation": "The shell every page shares: a 78px fixed header with the Aboard wordmark, the section links (How We Work / Case Studies / Foundry / Perspectives / About) and the boxed \"Get in Touch\" CTA; and the bright-citrus footer with the \"We Can Help\" serif display heading, the newsletter-signup iframe, link columns and the legal row.",
    "Home": "The home page: the \"Your partner for the big AI leap\" display hero (words animate in one by one), the \"Your roadmap, realized\" section, a media carousel with tick pagination and a pause control, and the feed rows linking events, the newsletter and the podcast.",
    "Consent overlay": "Aboard's cookie consent is CookieYes: a bottom strip with \"We use cookies...\" copy and Customize / Accept All buttons, plus a preferences modal that lives in the DOM. Captured as found; nothing was pressed (the capture hides the strip by CSS for the clean shots, which is a hide, not a consent).",
    "How We Work": "The process page: the \"95% of AI software initiatives fail\" headline, the principle cards and the Landscape / Audit / Blueprint / Architecture / Migrate step row.",
    "Case studies": "The work index and one detail page (City of Boston scheduling app): a full-width featured card, then a grid of case cards with industry tags.",
    "Foundry": "The Foundry page: the products Aboard builds for itself (Aboard Sign, TinyLittleOffice) as cards in the same shell.",
    "Feeds: perspectives, newsletter, events, media": "The content indexes share one row vocabulary: a kind tag or date, a serif title and a thumbnail. The newsletter page adds the dark signup form and the latest-issue card.",
    "Podcast": "The podcast index (cream type on dark forest green) and one episode page: episode rows and the dock player's seek bar. Transport buttons were measured at rest, never pressed.",
    "Article page": "A long-form piece (\"Meet Aboard Sign\") in the centred article column with the SHARE rail and newsletter cards; a boxed variant of the signup form closes the page.",
    "Newsletter signup (resting only)": "The one real form on the site, rendered twice: inline on the newsletter page (dark variant) and boxed under articles (is-card variant), plus embedded in the footer through a same-origin iframe. It posts to /wp-json/aboard/v1/newsletter-signups. Fields were measured at rest and focused only: no address was typed and the form was never submitted.",
    "About, careers, security": "The company pages in the same shell: team photos on about, the openings list on careers, the security posture text.",
    "Mobile (390 wide)": "A few components as a phone draws them, at 390 x 844: the header with its Open-menu trigger, the opened nav panel, the hero title and a feed row.",
}

SHOTS = [
    ("home", "Home. Display hero, media carousel, feed rows, contact section with the signup iframe, citrus footer. The cookie strip captured as a separate state.", "/"),
    ("how-we-work", "How We Work. The process page and its step row.", "/how-we-work/"),
    ("case-studies", "Case studies index. Featured card and the card grid.", "/case-studies/"),
    ("case-study", "Case study detail. City of Boston scheduling app.", "/case-studies/city-of-boston-scheduling-app/"),
    ("foundry", "Foundry. The self-built products page.", "/foundry/"),
    ("perspectives", "Perspectives index.", "/perspectives/"),
    ("newsletter", "Newsletter. Latest issue, index rows and the dark signup form.", "/newsletter/"),
    ("podcast", "Podcast index. Episode rows on dark green, dock player.", "/podcast/"),
    ("podcast-episode", "Podcast episode detail.", "/podcast/jason-goldman-from-vc-pitches-to-ai-kill-switches/"),
    ("events", "Events index.", "/events/"),
    ("media", "Media index.", "/media/"),
    ("about", "About. Team and company page.", "/about/"),
    ("faq", "FAQ. Accordion of questions.", "/faq/"),
    ("careers", "Careers. Openings list.", "/careers/"),
    ("security", "Security. Posture and practices text.", "/security/"),
    ("aboard-sign", "Newsletter article. Meet Aboard Sign, with the share rail.", "/meet-aboard-sign/"),
]
MOBILE = [
    ("mobile-home", "Home at 390: collapsed header, the opened menu, feed rows single-column.", "/"),
    ("mobile-how-we-work", "How We Work at 390.", "/how-we-work/"),
    ("mobile-case-studies", "Case studies at 390.", "/case-studies/"),
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

W("# Aboard components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real site, the icon index and the Gaps. Captured from aboard.com on {J['_meta']['run'][:10]}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was sent or submitted: the newsletter signup was measured at rest and focus only, and the cookie consent was never answered (it was hidden for the clean captures, which is not a consent).")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts at four widths are in [raw/layout.json](raw/layout.json).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Tobias 64/68 400, #232a20`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (Aboard has one theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 390 wide.")
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
    ("Cookie consent strip", "every page, on load", "at rest; hidden by CSS for every clean capture, never answered", "[home-light-cookie-banner](screenshots/home-light-cookie-banner.png), [cookie-bar](#cookie-bar)"),
    ("Cookie preferences modal", "in the DOM on every page", "never opened (Customize was not pressed); the DOM node was measured where visible", "[cookie-bar](#cookie-bar)"),
    ("Mobile menu, open", "home at 390", "the Open-menu trigger pressed (a local disclosure)", "[mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-nav-panel](#m-nav-panel)"),
    ("FAQ answer, open", "FAQ", "the question heading pressed (a local accordion disclosure)", "[faq-panel-open](#faq-panel-open)"),
    ("Podcast dock player", "podcast pages", "measured at rest; transport controls were never pressed", "[pod-seek](#pod-seek), [pod-play](#pod-play)"),
    ("Form focus", "newsletter signup", "the email field tabbed or clicked into; nothing typed, nothing sent", "[nl-field](#nl-field)"),
    ("Contact / signup iframe", "home contact section and footer", "the same-origin embed was measured as a frame; its fields are the newsletter signup's", "[contact-iframe](#contact-iframe)"),
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
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} draw a ring: {', '.join(with_ring)}. The other {len(without)} draw none, so a keyboard user sees no change: {', '.join(without)}.")
W()
W("**Pressed.** Forced `:active` was applied to the buttons and links above; the site changes very little under the finger (the nav CTA and consent buttons keep their fills). See each entry's Pressed row for what did move.")
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


for page in ["home", "how-we-work", "case-studies", "foundry", "newsletter", "podcast", "about", "faq"]:
    W(f"| {page} | " + " | ".join(grid_of(f"{page}@{w}") for w in (1440, 1920, 1024, 390)) + " |")
W()
W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
# The card-like components to compare in one table.
for k in ["case-card-feature", "case-card", "foundry-card", "art-nl-card", "nl-form", "nl-form-card", "nl-field", "cookie-bar", "feed-row", "pod-ep-row"]:
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
            for lab, d, layers in rows:
                cell = fmt(d)
                if layers:
                    cell += ("; " if cell else "") + "painted layers: " + "; ".join(layers).replace("|", "/")
                W(f"| {lab} | {cell} |")
            W()
        cl = child_layers(c)
        if cl:
            W(f"Child layers that carry the look: {cl}.")
            W()
        imgs = [f"![{c['title']} {st}](components/crops/{os.path.basename(c['states'][st]['crop'])})" for st in states if c["states"][st].get("crop")]
        failed = [st for st in states if c["states"][st].get("cropError")]
        if imgs:
            W(" ".join(imgs))
        elif failed:
            W(f"No crop was saved: capture failed for {', '.join(f'`{s}`' for s in failed)}; the values are from the computed styles.")
        else:
            W("No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.")

# ------------------------------------------------ icons
W()
W("## Icons")
W()
W(f"{len(icons)} SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Photography and artwork were left out; these are the interface icons (the wordmark, the menu trigger, the player controls, arrows). The SVGs are Aboard's property, kept for reference only.")
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
W("- **There is no account area.** aboard.com is a marketing site with one form (the newsletter signup); there is no login, dashboard, cart or checkout to be behind.")
W("- **The contact path is the signup.** The \"Get in Touch\" CTA and the #contact section embed the same newsletter-signup iframe (`/contact-form/?iframe=contactForm`), a same-origin page that posts to a WordPress REST endpoint. It was measured as a frame and at rest; no address was typed and nothing was submitted.")
W("- **Embedded media.** Podcast and article pages embed third-party players (YouTube iframes and the like); the embeds were screenshotted in place but not opened, played or probed.")
W("- **External destinations.** The footer and cards link out to LinkedIn, YouTube, Instagram, Facebook and X; outbound pages were not visited.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools (`:active`), so a state a script adds on mousedown is missing if one exists.")
W("- **The consent states.** Customize / Accept All / the modal's preference toggles were measured but never clicked: the post-consent UI is uncaptured.")
W("- **Audio playback.** The podcast dock's transport buttons were measured at rest; playback was never started, so playing/paused/buffering states are missing.")
W("- **Carousel autoplay.** The home carousel's ticks and pause button were measured at rest; the pause toggle was not flipped.")
W("- **Disabled states** were not seen on any public control.")
W()
W("### Themes")
W()
W("Aboard shows one theme. The page paints warm off-white (`--wp--preset--color--parchment` / `--rd-parchment`) with dark forest-green and bright-citrus sections inside the same paint; there is no `prefers-color-scheme` variant and no theme attribute, so the token file ships a single `light` set. 124 custom properties resolve from the WordPress theme sheets (245 declared; see [raw/css-vars.json](raw/css-vars.json)); the token file aliases the --wp--preset--* and --rd-* names where the site declares them.")
W()
W("### Fonts")
W()
W("- **Work Sans** is the interface sans (headings, nav, buttons, body); **Tobias** is the serif used for display headings and card titles. Both are served same-origin by the theme; the @font-face rules are in [raw/css-vars.json](raw/css-vars.json).")
W()
W("### Screenshots")
W()
W("- Photography, project artwork and media frames are Aboard's content and appear only inside screenshots and crops.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Article body text, case-study copy and the FAQ answers were not transcribed; only the frames around them were measured.")
W("- No personal data was captured: every page was read signed out, and the only form touched was the newsletter field measured and left empty.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops,", len(icons), "icons")
