#!/usr/bin/env python3
"""Build components.md for the HBO Max design reference.

Reads raw/components-computed.json (every component and state, measured),
tokens.json, screenshots/ and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the
token whose value matches, the font family is named once per value,
and a state row shows only what differs from the first state. Adapted from
the grok package's builder (itself the Coursera kit's).

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
# runs set by set — the dark theme's resolved roles first (the site paints one
# dark theme, html data-theme="max": color.surface.low black, the white
# general.text), then core, whose spacer/border/font scales hold no colours —
# so a white label is named color.general.text.high, not whichever component
# token happens to share the value. PRIMARY pins the roles a label should
# prefer when several tokens share one colour (many --color_* roles are
# #ffffff; the general text and surface roles are the ones the page paints
# with). Names carry their set prefix (dark.color.general.text.high) so a
# label always names a real path in tokens.json.
PRIMARY = {"color.surface.low", "color.surface.high", "color.general.text.high",
           "color.general.text.mid", "color.general.text.low", "color.action.primary.fill.high",
           "color.general.border.low"}
BY_COLOR = {}
for n, t in sorted(flat(T["dark"], "dark."), key=lambda it: (it[0].split(".", 1)[1] not in PRIMARY, it[0])):
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

PAGE_NAME = {"/sg/en": "home", "/sg/en/show/e6e7bad9-d48d-4434-b334-7c651ffc4bdf": "series detail",
             "/sg/en/movie/710798da-f811-40be-9ed9-3a7443e36278": "movie detail",
             "/sg/en/movies": "movies browse", "/privacy": "privacy policy",
             "mobile": "home"}

GROUP_INTRO = {
    "Site chrome": "The fixed shell every marketing page carries: the translucent navbar over the hero (the HBO Max wordmark, section links and the Sign In pill that leads to auth.hbomax.com — measured, never followed).",
    "Hero": "The full-bleed autoplay carousel under the navbar (Bootstrap markup): backdrop art per slide, a 'Start Subscription' CTA, the Next control and the slide indicators.",
    "Plans": "The subscription section: the monthly/yearly billing toggle, the tier cards and their Choose buttons — hovered and focused, never pressed.",
    "FAQ": "The 'Questions' accordion near the foot of the home page, opened by its own chevron.",
    "Content rails": "The horizontal 'Discover' rows of poster cards on the home and browse pages, each card a link to a title detail page.",
    "Footer": "The link columns, the legal row and the language selector at the bottom of every page.",
    "Title detail": "The backdrop hero, display title, meta row and subscribe CTA on the series and movie detail pages.",
    "Legal prose": "The privacy policy: headings, paragraphs and inline links.",
    "Cookie consent": "The consent modal that opens over a fresh visit — measured as loaded; Accept/Manage were styled, never pressed.",
    "Site chrome (mobile)": "The 390px surface: the navbar, the menu button and the navigation it opens.",
}

SHOTS = [
    ("home", "Home (marketing)", "/sg/en"),
    ("movies", "Movies browse", "/sg/en/movies"),
    ("shows", "Series browse", "/sg/en/shows"),
    ("channel", "Channel hub", "/sg/en/channel"),
    ("show", "Series detail", "/sg/en/show/e6e7bad9-d48d-4434-b334-7c651ffc4bdf"),
    ("movie", "Movie detail", "/sg/en/movie/710798da-f811-40be-9ed9-3a7443e36278"),
    ("collection", "Kids & Family collection", "/sg/en/collections/genre/kids-family"),
    ("sitemap", "Sitemap", "/sg/en/sitemap"),
    ("corp-info", "Corporate information", "/sg/en/corp-info"),
    ("privacy", "Privacy policy", "/privacy"),
]

MOBILE = [
    ("mobile-home", "Home, phone", "/sg/en"),
    ("mobile-movies", "Movies browse, phone", "/sg/en/movies"),
    ("mobile-show", "Series detail, phone", "/sg/en/show/e6e7bad9-d48d-4434-b334-7c651ffc4bdf"),
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

W("# HBO Max components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Read from www.hbomax.com/sg/en on {J['_meta']['read']}, signed out, in headed Chromium under Xvfb at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Later recaptures merge into the same file, so every entry names the date its own states were read; a state a re-read missed keeps its earlier date and says so. Nothing was signed into, bought, searched or submitted; the only presses were local UI toggles the page's own chrome provides — the hero carousel's Next arrow, the billing toggle, an FAQ chevron, the language selector and the phone's menu button; every link was measured, never followed.")
W()
W("**Where this was read.** `hbomax.com` redirects to `www.hbomax.com`, which serves the marketing site in the visitor's locale — the capture host resolved to Singapore, so everything below is the `/sg/en` locale (title 'HBO Max | Stream Series and Movies', canonical www.hbomax.com). Akamai's edge returns a 403 'Access Denied' page to headless Chromium, so every capture here ran headed under Xvfb — that block is documented as an access constraint, not worked around. The app itself (play.hbomax.com), sign-in and checkout (auth.hbomax.com) and the help centre (help.hbomax.com) are separate signed-in or out-of-scope surfaces, listed under Gaps.")
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
W("Screenshots are named `{page}-{theme}-{state}.png` where `{theme}` is the surface the page painted at capture: every www.hbomax.com page ships one theme — `html data-theme=\"max\"`, a dark surface — so every shot is `-dark-`. Desktop shots are 1440 x 900 at 1x; `-full` shots are the whole document bounded at eight GPU-texture chunks (the over-cap remainder recorded as `.partN.png` with the boundary in the shot's `.capture.json` sidecar); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x). The cookie-consent modal shot is `-promo`; `carousel-next`, `plan-yearly` and `faq-open` are the same page after each control's own press.")
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
    ("Cookie consent modal", "home (fresh visit)", "the page's own modal, captured as it loaded, then hidden without accepting or rejecting for the rest of the pass", "[home-dark-promo](screenshots/home-dark-promo.png), [mobile-home-dark-promo](screenshots/mobile-home-dark-promo.png), [consent-dialog](#consent-modal)"),
    ("Hero carousel next slide", "home hero", "the carousel's own Next-arrow press — the slide advanced one step", "[home-dark-carousel-next](screenshots/home-dark-carousel-next.png), [hero-next](#carousel-next-control)"),
    ("Yearly billing", "home plans", "the billing toggle's own press — the card prices repainted", "[home-dark-plan-yearly](screenshots/home-dark-plan-yearly.png), [plan-toggle](#billing-period-toggle)"),
    ("FAQ item open", "home FAQ", "a question's own chevron press — the answer expanded", "[home-dark-faq-open](screenshots/home-dark-faq-open.png), [faq-item](#faq-accordion-item)"),
    ("Language selector", "home footer", "the selector's own press — the locale list opened, nothing chosen", "[lang-selector](#language-selector)"),
    ("Mobile navigation", "home, phone width", "the menu button's own press", "[m-nav-open](#mobile-nav-open)"),
    ("Sign in, subscribe and checkout", "auth.hbomax.com", "signed-in surface — never opened; every CTA pointing at it was measured, never followed", "boundary; see Gaps"),
    ("The app (play.hbomax.com) and help centre (help.hbomax.com)", "player and help", "separate surfaces outside the signed-out marketing site — never opened", "boundary; see Gaps"),
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
for k in ["consent-dialog", "plan-card", "rail-card", "faq-section", "hero-slide", "m-nav-open"]:
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
W("The streaming app itself was never reached: **play.hbomax.com** (the player) is signed-in, and every entry point to it passes through **auth.hbomax.com** — the navbar's Sign In, each hero slide's 'Start Subscription' CTA and every plan card's Choose button point at `auth.hbomax.com/login` or `auth.hbomax.com/product`. None was followed. **help.hbomax.com** is a separate help-centre site, linked from the footer but never opened. Headless Chromium is refused by Akamai at the edge with a 403 'Access Denied' page — the standard headless pass is documented as that boundary and every capture here ran headed under Xvfb; no other client shape was tried.")
W()
W("### Pages")
W()
W("- **Sign-in, account and checkout (auth.hbomax.com)** — the signed-in surface; never opened.")
W("- **The player (play.hbomax.com)** — requires an account; never opened.")
W("- **The help centre (help.hbomax.com)** — a separate site linked in the footer; not captured.")
W("- **Other locales** — the capture host resolves to Singapore, so only `/sg/en` loaded; `max.com` and other region/locale pairs were not probed.")
W("- **Student, savings and bundle pages** (`/student`, `/savings`, `/bundle/*`) — marketing landers on the same template family; not each measured.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on the controls that carry it, so a state a script adds on mousedown (if any) is missing.")
W("- **The consent modal** was captured as it mounted and then hidden without accepting or rejecting — its Accept/Manage styles are measured, its consent write was never exercised.")
W("- **The language selector** was opened for measurement; no locale was switched.")
W("- **The carousel** autoplays; the `-next` shots are one Next-arrow press past whatever slide the timing landed on.")
W("- **mobile-movies** lost its default shot to a screenshot timeout on the first pass; a re-run is queued — see the capture sidecars.")
W()
W("### Themes")
W()
W("www.hbomax.com ships one theme: `<html data-theme=\"max\">` is the only theme attribute the bundle sets, and the token sheet loads the same `--color_*` declarations on every page — a dark surface. There is no theme control anywhere in the chrome, so there is no light set, no dark-state pass and nothing was fabricated; the `dark` name in file and token names is the painted surface's own.")
W()
W("### Fonts")
W()
W("- **Max Sans** (woff2, weights 300/400/600, `font-display: swap`) is the product face — the token sheet's own `@font-face` in /dotcom/generated/css/hbomax/styles.*.css — proprietary to Warner Bros. Discovery, declared and measured, not shipped. The rendered stack is `Max Sans,Inter,sans-serif,-apple-system,…`; the style guide falls back to the system sans.")
W()
W("### Screenshots")
W()
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W("- The rendered brand strings on the captured pages (the wordmark and copy) are the product's published content.")
W()
W("### Content left out")
W()
W("- Title names, prices, plan copy and FAQ text are the product's content; only frames and components were measured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
