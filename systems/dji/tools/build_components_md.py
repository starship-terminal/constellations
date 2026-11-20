#!/usr/bin/env python3
"""Build components.md for the Gauth design reference.

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


def _resolve_alias(value, node, depth=0):
    m = re.fullmatch(r"\{(.+)\}", str(value))
    if not m or depth > 6:
        return value
    tgt = node
    for part in m.group(1).split("."):
        tgt = tgt.get(part) if isinstance(tgt, dict) else None
        if tgt is None:
            return value
    return _resolve_alias(tgt.get("$value", value), node, depth + 1)


BY_COLOR = {"light": {}, "dark": {}}
# Theme names first, core as the fallback: a colour a theme role shares with a core
# scale step is named by the role it plays in that theme.
for _set in ("light", "dark", "core"):
    for n, t in flat(T[_set]):
        if t["$type"] == "color":
            v = _resolve_alias(t["$value"], T[_set])
            if _set == "core":
                BY_COLOR["light"].setdefault(v, n)
                BY_COLOR["dark"].setdefault(v, n)
            else:
                BY_COLOR[_set].setdefault(v, n)

# Which theme each component's readings were painted in. dji.com scopes its
# theme to sections (.light-theme / .dark-theme), and the readings do not
# record the section class, so a component counts as dark when the token
# builder reads a dark role from it (raw/component-tokens.json, dark set).
# Set per component in the render loop and read by colour().
def _cited(node):
    if isinstance(node, dict):
        if isinstance(node.get("source"), str):
            yield from re.findall(r"(?:computed|painted) \w+ of ([\w-]+) ", node["source"])
        for v in node.values():
            yield from _cited(v)


_DARK_COMPONENTS = set(_cited(json.load(open("raw/component-tokens.json")).get("dark", {})))
_THEME = "light"


def _srgb_byte(x):
    x = max(0.0, min(1.0, x))
    x = x * 12.92 if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055
    return round(x * 255)


def _oklab_to_rgb(L, A, B):
    l_ = L + 0.3963377774 * A + 0.2158037573 * B
    m_ = L - 0.1055613458 * A - 0.0638541728 * B
    s_ = L - 0.0894841775 * A - 1.2914855480 * B
    l, m, s_ = l_ ** 3, m_ ** 3, s_ ** 3
    r = +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s_
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s_
    b = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s_
    return _srgb_byte(r), _srgb_byte(g), _srgb_byte(b)


def _oklch_to_rgb(L, C, H):
    import math
    return _oklab_to_rgb(L, C * math.cos(math.radians(H)), C * math.sin(math.radians(H)))


def _lab_to_rgb(L, A, B):
    # CIELAB D50 -> sRGB (the same matrix build_component_tokens.py applies);
    # the matrix emits linear sRGB, which _srgb_byte expects.
    fy = (L + 16) / 116
    fx, fz = fy + A / 500, fy - B / 200
    eps, kap = 216 / 24389, 24389 / 27
    f = lambda t: t ** 3 if t ** 3 > eps else (116 * t - 16) / kap
    X, Y, Z = 0.96422 * f(fx), f(fy), 0.82521 * f(fz)
    r = 3.1338561 * X - 1.6168667 * Y - 0.4906146 * Z
    g = -0.9787684 * X + 1.9161415 * Y + 0.033454 * Z
    b = 0.0719453 * X - 0.2289914 * Y + 1.4052427 * Z
    return _srgb_byte(r), _srgb_byte(g), _srgb_byte(b)


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def colour(c, tokens=True):
    """rgb()/rgba()/color(srgb) -> '#hex `token`' or 'rgba(...)'."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        tok = BY_COLOR[_THEME].get(v) if tokens else None
        return f"{v} `{tok}`" if tok else v

    c = re.sub(r"oklch\(([\d.]+) ([\d.]+) ([\d.]+)(?:deg)?(?: / ([\d.]+%?))?\)",
               lambda m: label(norm(*_oklch_to_rgb(float(m.group(1)), float(m.group(2)), float(m.group(3))),
                                   (float(m.group(4).rstrip('%')) / (100 if '%' in m.group(4) else 1)) if m.group(4) else None)), c)
    c = re.sub(r"oklab\(([\d.]+) (-?[\d.]+) (-?[\d.]+)(?: / ([\d.]+))?\)",
               lambda m: label(norm(*_oklab_to_rgb(float(m.group(1)), float(m.group(2)), float(m.group(3))), m.group(4))), c)
    c = re.sub(r"(?<![a-z])lab\(([\d.]+)[ ,]+(-?[\d.]+)[ ,]+(-?[\d.]+)(?: ?/ ?([\d.]+%?))?\)",
               lambda m: label(norm(*_lab_to_rgb(float(m.group(1)), float(m.group(2)), float(m.group(3))),
                                   (float(m.group(4).rstrip('%')) / (100 if '%' in m.group(4) else 1)) if m.group(4) else None)), c)
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
            bits.append(" ".join(x for x in (pe, colour(p["backgroundColor"]) if p.get("backgroundColor") else None, p.get("borderTopWidth"), colour(p["boxShadow"]) if p.get("boxShadow") else None, p.get("opacity")) if x))
    # A root box-shadow (e.g. the 1px focus ring gained on focus-visible) does
    # not remove the painted children: keep reporting their layers, which is
    # where a state-carrying child outline (the 3px cyan CTA ring) shows up.
    if s["backgroundColor"] == "rgba(0, 0, 0, 0)" and s["borderTopWidth"] == "0px" and s["backgroundImage"] == "none":
        for p in v.get("paint", [])[:6]:
            bits.append(" ".join(x for x in (p["node"], p.get("size"), colour(p["bg"]) if p.get("bg") else None, colour(p["border"]) if p.get("border") else None, colour(p["shadow"]) if p.get("shadow") else None, colour(p["outline"]) if p.get("outline") else None, p.get("radius")) if x))
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

PAGE_NAME = {"home": "home", "drones": "camera drones", "handheld": "handheld", "product": "product page", "support": "support", "company": "company", "stores": "where to buy", "mobile": "mobile home"}

GROUP_INTRO = {
    "Site chrome": "The top nav and footer: the DJI mark, the Camera Drones / Handheld / Lifestyle Tech / Specialized / Explore / Support / Where to Buy menus, the locale picker, Login/Register and the Store button. The home page paints the legacy dui-navbar; category and product pages paint the newer siteHeader module.",
    "Home hero": "The 800px hero panels: product art over a .dark-theme section with the Learn More / Buy Now ghost CTAs.",
    "Product cards": "The atom-design hero-vertical-cards on the category grids: product art, tagline and model name.",
    "Category page": "The category listings (/camera-drones, /handheld): display headings, sub-nav and product-card rows.",
    "Product page": "The /mavic-4-pro surface: the sticky sub-nav, atom-design Buy Now and Watch Video buttons, eyebrow headings and spec lines — measured, never pressed (purchase gates on the store account).",
    "Support / company": "The /support portal (search field, category tiles), /company and /where-to-buy/online-stores (store-type links).",
    "Mobile (390 wide)": "The phone surface at 390 wide — the separate /sg/mobile site: dui-navbar-m nav, category tabs and hero CTAs.",
}

SHOTS = [
    ("home", "Home", "/sg"),
    ("drones", "Camera Drones", "/sg/camera-drones"),
    ("handheld", "Handheld", "/sg/handheld"),
    ("product", "Mavic 4 Pro", "/sg/mavic-4-pro"),
    ("support", "Support", "/sg/support"),
    ("company", "Company", "/sg/company"),
    ("stores", "Where to Buy", "/sg/where-to-buy/online-stores"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "/sg/mobile"),
    ("mobile-product", "Mavic 4 Pro, phone", "/sg/mavic-4-pro"),
]

L = []


def W(s=""):
    L.append(s)


shots = sorted(p.name for p in Path("screenshots").glob("*.png"))


def links(prefix):
    out = []
    for f in shots:
        m = re.fullmatch(re.escape(prefix) + r"-(.+)\.png", f)
        if m:
            out.append(f"[{m.group(1)}](screenshots/{f})")
    return ", ".join(out)


n_crops = len(list(Path("components/crops").glob("*.png")))
n_states = sum(len(c["states"]) for c in C.values())
icons = []

W("# DJI components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from dji.com's geo-locale /sg site on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought, booked or submitted; nav links, store CTAs, search fields and cards were measured, never followed or pressed. The product paints both section themes signed out — .light-theme on nav/listings/support and .dark-theme on hero, product and footer sections — so both themes are real painted evidence.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [patterns.md](patterns.md).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{state}.png`; dark paint needs no forcing — the product scopes it to `.dark-theme` sections on the live pages. Desktop shots are 1440 x 900 at 1x; the phone surfaces are `mobile-{page}-{state}.png`, 780 wide (390 at 2x).")
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
    ("Dark theme", "hero, product, footer sections", "the product scopes dark paint to sections carrying its own .dark-theme class — measured on the live surfaces, no forcing needed", "[pd-buy](#atom-buy-button), [ft-link](#footer-link)"),
    ("Store / checkout", "Store buttons, Buy Now CTAs", "measured at every paintable state, never followed — the store gates on a DJI account", "boundary; see Gaps"),
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
    painted = lambda st_: any(
        float(st_[f"border{d}Width"].replace("px", "")) > 0 and st_[f"border{d}Style"] != "none"
        for d in ("Top", "Right", "Bottom", "Left")
    )
    # A border "change" counts only when a painted border exists on either
    # side — a colour move on a 0-width border is invisible.
    border = (painted(s) or painted(base)) and any(
        s[f"border{d}{p}"] != base[f"border{d}{p}"]
        for d in ("Top", "Right", "Bottom", "Left")
        for p in ("Color", "Width", "Style")
    )
    fill = s["backgroundColor"] != base["backgroundColor"]
    text = s["color"] != base["color"]
    desc = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else (f"on a child: {child_ring}" if child_ring else None)
    foc.append((k, ring or bool(child_ring), shadow, fill, border, text, desc))
with_ring = [f"`{k}` ({r})" for k, ring, sh, fl, bd, tx, r in foc if ring]
with_shadow = [f"`{k}`" for k, ring, sh, fl, bd, tx, r in foc if not ring and sh]
with_fill = [f"`{k}`" for k, ring, sh, fl, bd, tx, r in foc if not ring and not sh and fl]
with_border = [f"`{k}`" for k, ring, sh, fl, bd, tx, r in foc if not ring and not sh and not fl and bd]
with_text = [f"`{k}`" for k, ring, sh, fl, bd, tx, r in foc if not ring and not sh and not fl and not bd and tx]
without = [f"`{k}`" for k, ring, sh, fl, bd, tx, r in foc if not ring and not sh and not fl and not bd and not tx]
parts = [f"{len(with_ring)} draw an outline ring: {', '.join(with_ring)}."]
if with_shadow:
    parts.append(f"{len(with_shadow)} draw a focus ring as a shadow instead: {', '.join(with_shadow)}.")
if with_fill:
    parts.append(f"{len(with_fill)} change their fill: {', '.join(with_fill)}.")
if with_border:
    parts.append(f"{len(with_border)} change only their border: {', '.join(with_border)}.")
if with_text:
    parts.append(f"{len(with_text)} change only their text colour: {', '.join(with_text)}.")
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
for k in ["ct-card", "hh-card", "sp-card"]:
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
        _THEME = "dark" if k in _DARK_COMPONENTS else "light"
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the DJI wordmark, menu glyphs, search/account icons and footer marks) are the product's artwork. Declared under layoutGaps in the catalog entry.")
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
W("Purchase and account need the DJI account — the Store and Buy Now CTAs lead to store.dji.com sign-in and checkout, which were never opened; Login/Register redirect to the member service. What is genuinely public signed out: the home hero (/sg), the category pages (/camera-drones, /handheld), product pages (/mavic-4-pro) with specs and CTAs, /support, /company and /where-to-buy/*. The Buy/Store buttons were measured, never pressed.")
W()
W("### Pages")
W()
W("- **Store, Login and Register actions.** The Store/Buy Now CTAs and the member-service redirects gate on a DJI account; they were measured at default/hover/focus-visible/pressed, never followed.")
W("- **Mega-menu panels.** The nav product menus open hover panels that were hovered but not walked item-by-item; the panel links' own states are unmeasured.")
W("- **App-download banner.** A top banner painted on load; it was left in the captures.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Disabled, error and loading states** were not seen on the public surface.")
W()

W("### Themes")
W()
W("There is no theme toggle and no root-level dark sheet: the product scopes themes to sections — :root .light-theme and :root .dark-theme re-declare the semantic roles, and sections opt in by class. Both paint signed out (nav/listings/support light; hero/product/footer dark), so light.* and dark.* are both measured paint. A full-page dark repaint does not exist — dark is per-section by design.")
W()
W("### Fonts")
W()
W("- **Open Sans** (the UI face — every UI string) with PingFang SC / Microsoft YaHei CJK fallbacks, and **Dji** (the icon face) are the served families, read from the @font-face declarations in the served sheets; the style guide falls back to system fonts.")
W()
W("### Screenshots")
W()
W("- Full-page shots are single document captures; the marketing pages' animated hero fields are motion media, frozen at capture time.")
W("- Product names, taglines, imagery and prices are the site's published content; screenshots are 256-colour PNGs, read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Product names, taglines, imagery and prices are the site's published content; only frames and components were measured.")


Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
