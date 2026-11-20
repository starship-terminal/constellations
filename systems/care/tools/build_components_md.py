#!/usr/bin/env python3
"""Build components.md for the Care.com design reference.

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

PAGE_NAME = {"home": "home", "childcare": "child care", "listing": "babysitters listing", "login": "login", "join": "join", "pricing": "pricing", "footer": "home", "mobile": "home"}

GROUP_INTRO = {
    "Shell and navigation": "The fixed white header: wordmark, the Find care / Find jobs / List your business / Resources mega-menu triggers, Log in and the lime Join-now pill.",
    "Home": "The full-bleed photo hero with the 64px display headline and the ZIP + Search band, the membership category cards and the testimonials.",
    "Category page": "A category landing page (/child-care): the display title over photo, the service cards (Nannies / Babysitters / Daycares), member reviews and the FAQ accordion.",
    "Provider listing": "The /babysitters public results page: real caregivers' first-name-plus-initial listings (photos, rates, tags) under the City/State and Filter toolbar, the signup-gate modal that mounts on scroll, and the pager.",
    "Login page": "The signed-out login card on /vis/auth/login: an email step only — the password step sits behind Continue and was never reached.",
    "Join page": "The /app/vhp/get-started chooser: I need a caregiver / I want a care job cards; captured as a boundary, never followed.",
    "Pricing": "The /app/vhp/plans-and-pricing page: the Premium monthly/quarterly/annual columns, the Senior Care Advisor bundle and the add-on cards.",
    "Footer": "The deep-green GlobalFooter: link columns, legal and the social row.",
    "Mobile (390 wide)": "The same surface at phone width: slimmer header, the full-screen CareMobileDrawer menu, smaller display type.",
}

SHOTS = [
    ("home", "Home", "/"),
    ("child-care", "Child care", "/child-care"),
    ("senior-care", "Senior care", "/senior-care"),
    ("pet-care", "Pet care", "/pet-care"),
    ("housekeeping", "Housekeeping", "/housekeeping"),
    ("tutoring", "Tutoring", "/tutoring"),
    ("babysitters", "Babysitters listing", "/babysitters"),
    ("safety", "Safety", "/about/safety/"),
    ("resources", "Resource centre", "/c/"),
    ("about", "About", "/about/"),
    ("pricing", "Plans and pricing", "/app/vhp/plans-and-pricing"),
    ("login", "Log in", "/vis/auth/login"),
    ("join", "Get started", "/app/vhp/get-started"),
    ("rates", "Caregiver rates", "/caregiver-rates"),
    ("terms", "Terms of use", "/about/terms-of-use"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "/"),
    ("mobile-child-care", "Child care, phone", "/child-care"),
    ("mobile-senior-care", "Senior care, phone", "/senior-care"),
    ("mobile-pet-care", "Pet care, phone", "/pet-care"),
    ("mobile-housekeeping", "Housekeeping, phone", "/housekeeping"),
    ("mobile-tutoring", "Tutoring, phone", "/tutoring"),
    ("mobile-babysitters", "Babysitters listing, phone", "/babysitters"),
    ("mobile-safety", "Safety, phone", "/about/safety/"),
    ("mobile-pricing", "Pricing, phone", "/app/vhp/plans-and-pricing"),
    ("mobile-login", "Log in, phone", "/vis/auth/login"),
    ("mobile-join", "Get started, phone", "/app/vhp/get-started"),
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

W("# Care.com components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from care.com on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, joined, searched, booked or paid for; the login and signup forms were never filled; the ZIP search, provider profiles, plan checkout and the signup-gate dialog's own actions were never followed or submitted.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [patterns.md](patterns.md).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
try:
    SCALES = json.load(open("raw/crop-scales.json"))
    _one = [k for k, v in SCALES.items() if v["scale"] == 1]
    _sc = f"; {len(SCALES) - len(_one)} at 2x, {len(_one)} halved to 1x over the ~1.2-megapixel crop cap (per-crop sizes in [raw/crop-scales.json](raw/crop-scales.json))" if _one else f"; all {len(SCALES)} at 2x (per-crop sizes in [raw/crop-scales.json](raw/crop-scales.json))"
except FileNotFoundError:
    _sc = ""
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`{_sc}). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).")
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
    ("Mobile menu overlay", "home, phone width", "the header menu button's own toggle", "[mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-nav-item)"),
    ("Find care mega menu", "every desktop page", "the Find care trigger's own toggle", "[home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#mega-menu), [menu-item](#mega-menu-tab), [menu-link](#menu-link)"),
    ("Cookie consent bar", "every page", "hidden, never answered (the OneTrust buttons were never clicked)", "hidden before every shot and reading"),
    ("Join Care.com signup gate", "/babysitters", "mounts over the results once they are scrolled to; measured open, then hidden, never answered", "[gate-dialog](#signup-gate-dialog), [gate-cta](#gate-cta)"),
    ("FAQ accordion", "/babysitters", "a question row's own toggle", "[babysitters-light-faq](screenshots/babysitters-light-faq.png), [list-faq](#faq-question)"),
    ("Signed-in product", "care.com member dashboard, messages, bookings, payments", "requires an account; only the public login/join shells were measured, never filled", "boundary; see Gaps"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement files.")
W()
def _node_key(n):
    """Paint-node identity minus state classes: 'button::before.MuiButtonBase-root.Mui-focusVisible' -> 'button::before'."""
    return (n.get("node") or "").split(".")[0]


def _laid_border(n):
    """A paint node carrying a real laid-out border line (not an auto-sized, unpainted ::before)."""
    b = n.get("border") or ""
    return bool(re.search(r"(0*[1-9][\d.]*)px (solid|dashed|double)", b)) and "auto" not in (n.get("size") or "auto")


foc = []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st or "style" not in st or st.get("via") == "focus failed":
        continue
    s = st["style"]
    bst = next((v for v in c["states"].values() if "style" in v), st)
    base = bst["style"]
    # A fully transparent outline paints nothing: several of Care's controls
    # carry an outline whose colour is rgba(0,0,0,0) at rest, so a transparent
    # outline must not count as a painted ring.
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0 and s["outlineColor"] != "rgba(0, 0, 0, 0)"
    # A ring painted on a child layer instead of the wrapper counts as ringed
    # too — unless that outline is also transparent.
    child_ring = next((n["outline"] for n in st.get("paint", []) if n.get("outline") and "rgba(0, 0, 0, 0)" not in n["outline"]), None)
    shadow = s["boxShadow"] != base["boxShadow"] and s["boxShadow"] != "none"
    border = any(
        s[f"border{d}{p}"] != base[f"border{d}{p}"]
        for d in ("Top", "Right", "Bottom", "Left")
        for p in ("Color", "Width", "Style")
    ) and any(  # a border-*colour* restyle on a 0px border paints nothing
        float(s[f"border{d}Width"].replace("px", "")) > 0 and s[f"border{d}Style"] not in ("none", "hidden")
        for d in ("Top", "Right", "Bottom", "Left")
    )
    # A border can appear on a child/pseudo layer (nav-trigger's ::before grows
    # from an auto size to a laid-out green ring on focus). Compare paint nodes
    # by their class-stripped name against the base state's.
    base_paint = {_node_key(n): n for n in bst.get("paint", [])}
    child_border = any(
        _laid_border(n) and (_node_key(n) not in base_paint or not _laid_border(base_paint[_node_key(n)]))
        for n in st.get("paint", [])
    )
    bg = s["backgroundColor"] != base["backgroundColor"]
    desc = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else (f"on a child: {child_ring}" if child_ring else None)
    foc.append((k, ring or bool(child_ring), shadow, border, child_border, bg, desc))
with_ring = [f"`{k}` ({r})" for k, ring, sh, bd, cb, bg, r in foc if ring]
with_shadow = [f"`{k}`" for k, ring, sh, bd, cb, bg, r in foc if not ring and sh]
with_border = [f"`{k}`" for k, ring, sh, bd, cb, bg, r in foc if not ring and not sh and bd]
with_cborder = [f"`{k}`" for k, ring, sh, bd, cb, bg, r in foc if not ring and not sh and not bd and cb]
with_bg = [f"`{k}`" for k, ring, sh, bd, cb, bg, r in foc if not ring and not sh and not bd and not cb and bg]
without = [f"`{k}`" for k, ring, sh, bd, cb, bg, r in foc if not ring and not sh and not bd and not cb and not bg]
parts = [f"{len(with_ring)} draw an outline ring: {', '.join(with_ring)}."]
if with_shadow:
    parts.append(f"{len(with_shadow)} draw a focus ring as a shadow instead: {', '.join(with_shadow)}.")
if with_border:
    parts.append(f"{len(with_border)} change only their border: {', '.join(with_border)}.")
if with_cborder:
    parts.append(f"{len(with_cborder)} grow a border on a child layer: {', '.join(with_cborder)}.")
if with_bg:
    parts.append(f"{len(with_bg)} paint a background wash: {', '.join(with_bg)}.")
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
for k in ["category-card", "service-card", "review-card", "provider-card", "plan-card", "addon-card", "join-card", "login-card"]:
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
        if c.get("recaptureMissed"):
            W(f"Kept from an earlier run: the {c['recaptureMissed']} recapture did not find this component, so these readings may not match the current page or script.")
            W()
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Care.com wordmark, the mega-menu chevrons and arrows, the rating stars, the social glyphs and the listing photography) are the product's artwork. Declared under layoutGaps in the catalog entry.")
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
W("The member product — the dashboard, inbox and messaging, bookings, payments, job applications, caregiver profiles behind login and every membership flow — sits behind the login and join shells. The email step on /vis/auth/login was measured as a card, never filled, so the password step, two-factor screens and everything past them were never reached and are not inferred.")
W()
W("### Pages")
W()
W("- **The member surface.** Everything post-login was never reached; the login card, the get-started chooser and the signup-gate modal were measured as boundaries, never used.")
W("- **Search, booking and payment.** The hero ZIP search, the provider cards' own links, the City/State and Filter controls, the plan Get-started buttons and every \"Join now\" action were measured or screenshotted, never followed through to a search, message, hire or checkout.")
W("- **Provider profiles.** /babysitters lists real public caregivers (first name + initial, photo, rate, tags); the rows were measured as components, never opened, and no contact detail appears on the public page.")
W("- **External surfaces** (Care for Business, the app-store links, social profiles and the linked partner pages) were never opened.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Disabled, error and loading states** were not seen on the public surface.")
W("- **The signup gate** was measured open once (it mounts on scroll) and then hidden, never answered; a run where it did not mount records the dialog missing.")
W()
W("### Themes")
W()
W("One theme is painted: the white/light canvas with deep-green and lime accents and the dark footer panel. No dark toggle exists on the public surface; tokens.json keeps the dark-painted surfaces' roles in the dark set.")
W()
W("### Fonts")
W()
W("- **Oceanic Grotesk** is the UI family (400/450/500/550 measured), **NaN Druid Sans** the display family on headlines, **Oceanic Text Semibold** the serif accent on testimonial names — all served from care.com's own /css/cms/font-face/ files. The legacy login form paints in **Proxima Nova**. The style guide falls back to system fonts.")
W()
W("### Screenshots")
W()
W("- Caregiver photography, listing profile photos, the hero imagery and the Care.com wordmark in the screenshots are the product's published content; real public names appear on the listing under the repo's private-library policy (no contact details are shown by the product or kept here).")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Caregiver bios, review text, FAQ answers and marketing copy are the product's content; only frames and components were measured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
