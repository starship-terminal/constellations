#!/usr/bin/env python3
"""Build components.md for the Foodnoms design reference.

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


BY_COLOR = {}
for n, t in flat(T["core"]):
    if t["$type"] == "color":
        BY_COLOR.setdefault(t["$value"], n)


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def _p3(c):
    """color(display-p3) component values -> sRGB 0-255 ints (same conversion
    as build_tokens.py)."""
    def dec(x):
        return x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4

    def enc(x):
        x = max(0.0, min(1.0, x))
        return x * 12.92 if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055

    rl, gl, bl = dec(c[0]), dec(c[1]), dec(c[2])
    return (
        round(enc(1.224940176 * rl - 0.224703265 * gl) * 255),
        round(enc(-0.042056955 * rl + 1.042586621 * gl) * 255),
        round(enc(-0.019637555 * rl - 0.078636046 * gl + 1.098273614 * bl) * 255),
    )


def colour(c, tokens=True):
    """rgb()/rgba()/color(srgb)/color(display-p3) -> '#hex `token`' or 'rgba(...)'."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        tok = BY_COLOR.get(v) if tokens else None
        return f"{v} `{tok}`" if tok else v

    c = re.sub(r"color\(display-p3 ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)",
               lambda m: label(norm(*_p3([float(x) for x in m.group(1, 2, 3)]), m.group(4))), c)
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

PAGE_NAME = {
    "home": "home", "plus": "Foodnoms+", "help": "help center", "news": "news", "press": "press hub",
    "family-plan": "family plan", "vs-mfp": "vs MyFitnessPal", "help-article": "help article",
    "news-article": "news article", "terms": "terms", "open-signup": "open-in-app interstitial",
    "dark": "home, dark", "mobile": "home",
}

GROUP_INTRO = {
    "App shell and navigation": "The marketing header: app-icon + Foodnoms wordmark, News / Foodnoms+ / Help links and the orange \"Get the App\" App-Store pill.",
    "Home": "The home page: the rotating-benefit hero ticker, the goal-pill marquee, the \"As Featured By\" press strip, feature cards, the values trio (Privacy First / Your Data, Your Control / No Ads, Ever), the review marquee and the closing CTA.",
    "Pricing (Foodnoms+)": "The /plus surface: headline, the \"Find pricing info for your region in the app\" tag, the two download CTAs and the Free vs Foodnoms+ comparison table (a Framer Row/Header/Paragraph/Divider/Symbol component, not a <table>).",
    "Help center": "The /help landing: the Search trigger that opens Framer's search modal, the topic accordions (Closed -> Open via the section header, a local UI toggle) and the Contact Us block.",
    "News": "The /news index: article cards and the \"Become a Foodnoms Insider\" newsletter block, whose email field was focused and typed into then cleared, never submitted.",
    "Press": "The /press hub: the app-details block, the press-kit asset links (measured, never downloaded) and the press-contact mailto pill.",
    "Article pages": "The long-form surfaces: /family-plan, /vs/myfitnesspal, a help article and a news article — headline, tag/date, prose and a static FAQ block.",
    "Legal": "The /terms page: one tall Legal Item body under the h1 (/privacy is the same shape).",
    "Open-in-app interstitial": "The /open/settings/sign-up page: the \"Open in Foodnoms\" interstitial an app deep link lands on in a browser.",
    "Dark theme (emulated prefers-color-scheme)": "The same home components under the site's own (prefers-color-scheme: dark) media rule, painted in a dark-scheme browser context — the theme a dark-system visitor sees, not a reconstruction.",
    "Mobile (390 wide)": "The phone surface at 390 wide: the top bar with hamburger (its overlay is evidenced by the mobile-home-light-drawer screenshot), the hero and cards at mobile metrics.",
    "Footer": "The site footer: Explore / Comparisons / Company / Social link columns, the mailto link and the legal row.",
}

SHOTS = [
    ("home", "Home", "/"),
    ("plus", "Pricing (Foodnoms+)", "/plus"),
    ("help", "Help center", "/help"),
    ("news", "News", "/news"),
    ("press", "Press hub", "/press"),
    ("family-plan", "Family plan", "/family-plan"),
    ("vs-mfp", "vs MyFitnessPal", "/vs/myfitnesspal"),
    ("help-article", "Help article", "/help/barcode-scanning"),
    ("news-article", "News article", "/news/foodnoms-2"),
    ("terms", "Terms", "/terms"),
    ("privacy", "Privacy", "/privacy"),
    ("open-signup", "Open-in-app interstitial", "/open/settings/sign-up"),
]
DARK = [
    ("home", "Home", "/"),
    ("plus", "Pricing", "/plus"),
    ("help", "Help center", "/help"),
    ("news", "News", "/news"),
    ("help-article", "Help article", "/help/barcode-scanning"),
    ("vs-mfp", "vs MyFitnessPal", "/vs/myfitnesspal"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "/"),
    ("mobile-plus", "Pricing, phone", "/plus"),
    ("mobile-help", "Help center, phone", "/help"),
]

L = []


def W(s=""):
    L.append(s)


shots = sorted(p.name for p in Path("screenshots").glob("*.png"))


def links(prefix, theme="light"):
    out = []
    for f in shots:
        m = re.fullmatch(re.escape(prefix) + r"-" + theme + r"-(.+)\.png", f)
        if m:
            out.append(f"[{m.group(1)}](screenshots/{f})")
    return ", ".join(out)


n_crops = len(list(Path("components/crops").glob("*.png")))
n_states = sum(len(c["states"]) for c in C.values())
try:
    # INDEX.tsv is keyed by its header row: icons.mjs names every column it
    # writes, and this reader looks fields up by those names, never by
    # position, so the two can never drift a column apart again.
    _idx = open("icons/INDEX.tsv").read().strip().split("\n")
    _hdr = _idx[0].split("\t")
    icons = [dict(zip(_hdr, (r.split("\t") + [""] * len(_hdr))[:len(_hdr)])) for r in _idx[1:] if r.strip()]
except FileNotFoundError:
    icons = []

W("# Foodnoms components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from foodnoms.com on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844, the Dark group at 1440 x 900 under emulated prefers-color-scheme: dark — the site's own media rule, the theme a dark-system visitor sees), with computed styles read from the running page. There is no web sign-in anywhere: the product is an iOS/macOS app sold through the App Store, so every Download / Get-the-App / press-kit link was measured, never followed; the help search was opened and typed into then cleared, and the newsletter field was typed into then cleared — nothing was ever submitted.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The layout patterns are described in [patterns.md](patterns.md).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{theme}-{state}.png`: every captured surface paints light, and the routes listed under Dark also painted the site's authored dark theme under emulated prefers-color-scheme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). /terms is ~18k px tall, captured as two stitched tiles.")
W()
W("| Surface | URL | Light | Dark |")
W("|---|---|---|---|")
for p, desc, url in SHOTS:
    d = links(p, "dark")
    W(f"| {desc} | `{url}` | {links(p)} | {d if d else '-'} |")
for p, desc, url in MOBILE:
    W(f"| {desc} | `{url}` | {links(p)} | - |")
W()
W("### Overlays and transient states")
W()
W("| State | Where | How it was reached | Captured |")
W("|---|---|---|---|")
OVER = [
    ("Framer search modal", "/help", "the \"Search\" trigger — a local UI toggle; text was typed and deleted, never submitted", "[help-light-search](screenshots/help-light-search.png), [help-search-modal](#search-modal), [help-search-input](#search-field)"),
    ("Help accordion", "/help", "the \"About Foodnoms\" section's own header (Closed -> Open) — a local UI toggle", "[help-light-accordion-open](screenshots/help-light-accordion-open.png), [help-accordion-open](#accordion-section-open)"),
    ("Mobile nav overlay", "home, phone width", "the \"Open navigation menu\" button — a local UI toggle; its label flips to Close", "[mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-hamburger](#mobile-hamburger)"),
    ("Newsletter form", "/news", "the email field was focused and typed into then deleted; the submit was hovered and focused, never pressed", "[nl-email](#newsletter-email-field), [nl-submit](#newsletter-submit)"),
    ("App Store links", "every page", "Download / Get the App / Try Foodnoms links and the press-kit zips were measured, never followed", "boundary; see Gaps"),
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
for k in ["feature-card", "value-card", "review-card", "news-card", "pricing-table", "fp-faq", "m-feature-card"]:
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
W(f"{len(icons)} SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv): the gradient wordmark, the search magnifiers, the close/X glyphs, and the mask-painted glyphs — Framer draws most icons as a div with a `-webkit-mask-image` data-URI SVG whose `background-color` supplies the tint (recorded in the tint column): the shield/cloud/eye-off value glyphs, the pricing checks and crosses, the goal-pill star, the question, megaphone and newspaper glyphs. The press outlets' logos in the \"As Featured By\" strip, the App Store badge and the Foodnoms app icon are brand artwork and were left out. The SVGs are the product's property, kept for reference only.")
W()
W("| Icon | Rendered sizes | View box | Style | Seen on | Next to |")
W("|---|---|---|---|---|---|")
for r in icons:
    W(f"| [{r.get('name', '')}](icons/{r.get('file', '')}) | {r.get('rendered sizes', '')} | {r.get('viewBox', '')} | {r.get('source', '')} | {r.get('seen on', '')} | {r.get('next to', '').replace('|', '/')[:60]} |")
W()

# ------------------------------------------------ gaps
W("## Gaps")
W()
W("### The product itself")
W()
W("Foodnoms is an iOS/macOS app sold through the App Store — there is no web app and no web sign-in. Everything the product does inside the app (food logging, AI scanning, widgets, the community database editor, subscription purchase) lives behind the App Store download, which was never installed or opened. /download is a JS redirect to apps.apple.com and was never followed; the /open/settings/* pages are static deep-link interstitials, measured at rest only.")
W()
W("### Pages")
W()
W("- **Pricing amounts.** /plus says \"Find pricing info for your region in the app\" — no prices are rendered publicly, so none are evidence here.")
W("- **Further routes.** The sitemap lists dozens more help, news, press and comparison articles of the same templates; one representative of each was captured.")
W("- **The help search results.** The modal was opened and typed into, but result rows were never clicked.")
W("- **app./community./web. subdomains** did not answer; api.foodnoms.com 404s.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover), so a state a script adds on mousedown (if any) is missing. Several anchors' own `color` stays the browser default (rgb(0,0,238)) while the painted text inside carries the real colour — each entry's text row shows the painted value.")
W("- **Disabled, error and loading states** were not seen on the public surface.")
W("- **The mobile drawer** could not be re-measured as a component (the toggle's aria-label flips once open and its links share text with the footer); it is evidenced by the mobile-home-light-drawer screenshot.")
W()
W("### Themes")
W()
W("The site repaints a real dark theme under `(prefers-color-scheme: dark)` — 39 `--token-*` names redeclare (the neutral ramp inverts; the accent ramp re-points; the accent pills stay orange). It is captured under an emulated dark scheme, the same code path a dark-system visitor takes. There is no user-facing theme toggle on the site; the theme follows the OS.")
W()
W("### Fonts")
W()
W("- **Aquawax Pro** (Bold/DemiBold/Medium/Heavy) is a proprietary uploaded font, loaded from Framer's CDN; the style guide falls back to a rounded system sans. **Fragment Mono** is declared in @font-face but no measured surface paints it. Font files are never committed.")
W()
W("### Screenshots")
W()
W("- Product screenshots, the app icon, press-kit logos, review text and outlet marks in the screenshots are the product's published content.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Article prose, review quotes, the press-kit zips' contents and the app-store copy are the product's content; only frames and components were measured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
