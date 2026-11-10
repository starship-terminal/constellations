#!/usr/bin/env python3
"""Build components.md for the Aesop design reference.

Reads raw/components-computed.json (every component and state, measured), tokens.json,
screenshots/ and components/crops/, and writes components.md next to them. Every value is a cell
of the measurement file, condensed: colours are hex followed by the token in tokens.json whose
value is the same, the font family is named once per value, and a state row shows only what
differs from the first state. One theme only: the storefront paints a single light scheme.

Deterministic: re-running it on the same inputs reproduces components.md byte for byte.
Run from anywhere: python3 tools/build_components_md.py
"""
import collections, json, os, re
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


def resolved(v, depth=0):
    while isinstance(v, str) and v.startswith("{") and depth < 12:
        node = None
        for tree in (T["light"], T["core"]):
            n = tree
            for k in v[1:-1].split("."):
                n = n.get(k) if isinstance(n, dict) else None
            if isinstance(n, dict) and "$value" in n:
                node = n
                break
        if node is None:
            return v
        v, depth = node["$value"], depth + 1
    return v


BY_COLOR = {}
for theme in ("core", "light"):
    for n, t in flat(T[theme]):
        if t["$type"] == "color":
            v = resolved(t["$value"])
            if not isinstance(v, str) or v.startswith("{"):
                continue
            BY_COLOR.setdefault(v, []).append(n)

# Which token a colour is named after depends on what it paints: a fill prefers the action and
# background names, a border the border names, text the text names.
PREFER = {
    "bg": ["action.", "background.", "color.ink", "color.cream", "color.amber", "color.white", "text.", "border."],
    "border": ["border.", "color.keyline", "color.ink", "color.amber", "text.", "background."],
    "text": ["text.", "action.", "color.amber", "color.ink", "color.cream", "color.black", "border."],
    "icon": ["text.", "color.", "border."],
}


def pick(names, role):
    order = PREFER.get(role, PREFER["bg"])
    def rank(n):
        for i, pre in enumerate(order):
            if n == pre or (pre.endswith((".", "-")) and n.startswith(pre)):
                return (i, len(n), n)
        return (len(order), len(n), n)
    return sorted(names, key=rank)[0]


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), round(float(a), 2))


def colour(c, tokens=True, role="bg"):
    """rgb()/rgba() -> '#hex `token`' or 'rgba(...)'."""
    def label(v):
        if re.fullmatch(r"rgba\(\d+, \d+, \d+, 0\)", v):
            return "transparent"
        names = BY_COLOR.get(v) if tokens else None
        return f"{v} `{pick(names, role)}`" if names else v

    return re.sub(r"rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)",
                  lambda m: label(norm(*m.group(1, 2, 3), m.group(4))), c or "")


def sides(t, r, b, l):
    if t == r == b == l:
        return t
    if t == b and r == l:
        return f"{t} {r}"
    return f"{t} {r} {b} {l}"


def fam(f):
    first = (f or "").split(",")[0].replace('"', "").strip()
    return {"SuisseIntl": "SuisseIntl", "SuisseIntl-Medium": "SuisseIntl-Medium"}.get(first, first)


def num(x):
    return re.sub(r"(\d+\.\d\d)\d+", r"\1", str(x))


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
            bds.append(f"{s[f'border{d}Width']} {s[f'border{d}Style']} {colour(s[f'border{d}Color'], role='border')}")
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
    if s.get("backdropFilter", "none") != "none":
        o["backdrop"] = s["backdropFilter"]
    if s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0:
        o["outline"] = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'], role='border')}, offset {s['outlineOffset']}"
    t = v.get("textStyle")
    if t:
        o["text"] = f"{font(t['fontSize'], t['lineHeight'], t['fontWeight'], t['fontFamily'])}, {colour(t['color'], role='text')}"
    elif v.get("text"):
        o["text"] = f"{font(s['fontSize'], s['lineHeight'], s['fontWeight'], s['fontFamily'])}, {colour(s['color'], role='text')}"
    if s.get("textDecorationLine") not in (None, "none"):
        o["decoration"] = s["textDecorationLine"]
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
            o["transition"] = ", ".join(parts) if len(parts) < 4 else f"{parts[0].split(' ')[0]} and {len(parts) - 1} more {' '.join(parts[0].split(' ')[1:])}"
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
    if v.get("placeholder"):
        o["placeholder"] = colour(v["placeholder"]["color"], role="text")
    return o


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "backdrop", "outline", "text", "decoration", "transition", "transform", "opacity", "icon", "placeholder", "before", "after", "layers"]


def painted(v):
    """The parts of a state props() never sees: the ::before/::after boxes and
    the svg icon. state_rows compares them per state so a hover underline or an
    icon recolour is not collapsed into "same"."""
    o = {}
    for pe, key in (("::before", "before"), ("::after", "after")):
        p = v.get(pe)
        if not p:
            continue
        bits = [f"{p['width']} x {p['height']}"]
        if p.get("backgroundColor") and p["backgroundColor"] != "rgba(0, 0, 0, 0)":
            bits.append("bg " + colour(p["backgroundColor"]))
        if p.get("backgroundImage") and p["backgroundImage"] != "none":
            bits.append("image " + colour(p["backgroundImage"])[:100])
        if float((p.get("borderTopWidth") or "0px").replace("px", "") or 0) > 0 and p.get("borderTopStyle") != "none":
            bits.append(f"border {p['borderTopWidth']} {p['borderTopStyle']} {colour(p['borderTopColor'], role='border')}")
        if p.get("boxShadow") and p["boxShadow"] != "none":
            bits.append("shadow " + colour(p["boxShadow"], tokens=False)[:120])
        o[key] = "; ".join(bits)
    ic = v.get("icon")
    if ic:
        o["icon"] = f"{ic['w']} x {ic['h']}, colour {colour(ic['color'], role='icon')}"
        if ic.get("fill") and ic["fill"] not in ("none", ic["color"]):
            o["icon"] += f", fill {colour(ic['fill'], role='icon')}"
    return o


def layer_str(p):
    bits = [re.sub(r"\..*$", "", p["node"]) if "::" not in p["node"] else p["node"].split(".")[0],
            p["size"].replace(".0x", "x").replace(".0", "")]
    if p.get("bg"):
        bits.append("background " + colour(p["bg"]))
    if p.get("border"):
        bits.append("border " + colour(p["border"].split(" | ")[0][2:], role="border"))
    if p.get("radius"):
        bits.append("radius " + p["radius"])
    if p.get("shadow"):
        bits.append("shadow " + colour(p["shadow"]))
    if p.get("bgImage"):
        bits.append("image " + colour(p["bgImage"])[:120])
    return " ".join(bits)


def child_sig(v):
    """The paint layers inside the component, minus the root itself and the
    pseudo-elements the 'before'/'after' rows already report."""
    root = v.get("tag", "") + "".join("." + c for c in (v.get("classes") or "").split()[:2])
    return [layer_str(p) for p in v.get("paint", []) if p["node"] != root and "::" not in p["node"]]


def state_rows(c):
    """The first state lists every value; later rows list only what changed,
    ::before/::after, icon and child paint included."""
    rows = []
    states = [s for s, v in c["states"].items() if "style" in v]
    if not states:
        return rows
    base_v = c["states"][states[0]]
    base = {**props(base_v), **painted(base_v)}
    base_sig = child_sig(base_v)
    rows.append((states[0], base))
    same = []
    for st in states[1:]:
        v = c["states"][st]
        p = {**props(v), **painted(v)}
        diff = {k: p[k] for k in ORDER if k in p and p.get(k) != base.get(k)}
        for k in ORDER:
            if k in base and k not in p:
                diff[k] = "none"
        sig = child_sig(v)
        if sig != base_sig:
            changed = [s2 for i, s2 in enumerate(sig) if i >= len(base_sig) or s2 != base_sig[i]]
            diff["layers"] = "; ".join(changed[:3])
        if not diff:
            same.append(st)
            continue
        if rows[-1][0] != states[0] and rows[-1][1] == diff:
            rows[-1] = (rows[-1][0] + ", " + st, diff)
        else:
            rows.append((st, diff))
    if same:
        rows[0] = (f"{states[0]} (same: {', '.join(same)})", base)
    return rows


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
        out.append(layer_str(p))
    return "; ".join(out).replace("|", "/")


# --------------------------------------------------------------------------- page and group text

GROUP_INTRO = {
    "Shell and navigation": "The two-tier header every page shares: a thin utility row (Stores, Customer service / Email sign up, Account, My cart), the centred Aēsop wordmark and the main-nav row ending in a Search disclosure trigger. Cream-on-ink, transparent over the hero.",
    "Home": "The home canvas: a full-bleed campaign band under the transparent header (photography or film, an overlaid line and a bordered CTA card), then product rows and the dark footer.",
    "Catalogue page (PLP)": "A catalogue page such as Shop all: the category title and product count, an All filters toggle opening a 400px left rail of accordion groups (Price, Skin type, Skin concern, Form, Ingredients, Aroma), a Sort select, then the tile grid — photograph, bold name, descriptor, size select, price, ink add-to-cart.",
    "Product page (PDP)": "A product detail page: breadcrumbs over a two-column canvas (gallery left, purchase column right) — badge line, product title, price, descriptor, the bordered variant/size box, the ink Add to cart bar, then expandable rows and a suggested-partners rail.",
    "Panels and overlays": "The overlays: the search disclosure under the nav, the right-hand My cart drawer (405px), the Email sign up modal shell (its remote fragment did not render in headless), the Filter by rail and the locator's No-result dialog.",
    "Sign in": "The Demandware sign-in page (Login-Show): My Account heading, full-width email and password fields, a Submit bar and the Create an Account link. Measured, never submitted.",
    "Stores": "The store locator: Find a store title, an address field with a floating label, Geolocate me, a Filters select, the Map/Satellite toggle over a Google map, and the 'No result found' dialog.",
    "Footer": "The dark page foot (ink #252525): secure-checkout and complimentary-samples lines, the Orders and support / About / Sustainability link columns in cream, and the Online Preferences OneTrust trigger.",
    "Mobile (390 wide)": "The same storefront at 390: the header collapses to Stores, wordmark and My cart; the burger button opens a flat accordion drawer of 48px rows.",
}

PAGE_DESC = [
    ("home", "Home. The hero, product rows and footer. Captured at rest, search open, sign-up modal, cart drawer, nav hover, and full-page.", "/"),
    ("shopall", "Shop all, the catalogue page. Captured at rest, filters rail open, and full-page.", "/shop-all/"),
    ("skincare", "The Skin Care category landing.", "/skin-care/"),
    ("pdp", "A product page (The Aesop Valise, APB399). Captured at rest and full-page; its information accordion only renders at phone widths, so the open shot lives on the mobile capture.", "/gifts/seasonal-gift-kits/the-aesop-valise/APB399.html"),
    ("stores", "The store locator.", "/stores"),
    ("cart", "The cart route, empty.", "/cart"),
    ("login", "The Demandware sign-in page.", "/on/demandware.store/Sites-aesop-us-Site/en_US/Login-Show"),
    ("notfound", "The styled 404 / unexpected-error page.", "/account"),
]
MOBILE_DESC = [
    ("mobile-home", "Home at 390, at rest, the burger drawer open, and full-page.", "/"),
    ("mobile-shopall", "The catalogue page at 390.", "/shop-all/"),
    ("mobile-pdp", "The product page at 390.", "/gifts/seasonal-gift-kits/the-aesop-valise/APB399.html"),
]

L = []


def W(s=""):
    L.append(s)


shots = sorted(p.name for p in Path("screenshots").glob("*.png"))


def links(prefix):
    out = []
    for f in shots:
        m = re.fullmatch(re.escape(prefix) + r"-(dark|light)-(.+)\.png", f)
        if m:
            out.append(f"[{m.group(2)} ({m.group(1)})](screenshots/{f})")
    return ", ".join(out)


n_crops = len(list(Path("components/crops").glob("*.png")))
n_states = sum(len(c["states"]) for c in C.values())

W("# Aesop components")
W()
W(f"The discovery list of every page and state captured, then one entry per component with crops of the real site, the shared values and the Gaps. Captured from aesop.com on 2026-11-10 — the US storefront (Sites-aesop-us-Site, prices in US$) — as static pages rendered at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the live DOM. Nothing was submitted, bought or signed into; the only presses were local UI toggles (the Search disclosure, Email sign up modal, My cart drawer, All filters rail, burger menu). The OneTrust consent SDK was blocked at the network layer — its banner was never mounted, and no consent button was ever pressed.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the token in [tokens.json](tokens.json) whose value is the same, when there is one. Text is written family size/line-height weight, then its colour, for example `SuisseIntl 12/20 400, #000000`, and is read from the first text node inside the component.")
W("- The first state of each entry lists every value; later states list only what changed, pseudo-elements and child paint included — a hover underline or a recoloured icon shows as `before`, `after`, `icon` or `layers` in the row. A state identical to the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png`. Desktop shots are 1440 x 900 at 2x; `-full` shots are whole pages; mobile shots are `mobile-{page}-light-{state}.png`, 390 x 844 at 2x. Only light exists — the storefront has no dark theme.")
W()
W("| Surface | URL | Screenshots |")
W("|---|---|---|")
for p, desc, url in PAGE_DESC + MOBILE_DESC:
    W(f"| {desc} | `{url}` | {links(p)} |")
W()
W("### Overlays and transient states")
W()
W("| State | Where | How it was reached | Captured |")
W("|---|---|---|---|")
OVER = [
    ("Search disclosure", "home", "the Search header button", "[home-light-search](screenshots/home-light-search.png), [search-field](#search-field)"),
    ("Email sign up modal", "home", "the Email sign up button", "[home-light-signup](screenshots/home-light-signup.png), [signup-dialog](#signup-dialog)"),
    ("My cart drawer", "home", "the My cart button", "[home-light-cart](screenshots/home-light-cart.png), [cart-panel](#cart-panel)"),
    ("Filter rail", "PLP", "the All filters button", "[shopall-light-sort](screenshots/shopall-light-sort.png), [filter-panel](#filter-panel)"),
    ("PDP information accordion", "PDP at 390", "the Description row on the mobile product page — the block carries h-hide-for-large, so desktop never paints it", "[mobile-pdp-light-accordion](screenshots/mobile-pdp-light-accordion.png), [accordion](#accordion)"),
    ("Mobile burger drawer", "home at 390", "the burger button", "[mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-drawer](#m-menu-drawer)"),
]
for row in OVER:
    W("| " + " | ".join(row) + " |")
W()


# --------------------------------------------------------------------------- shared values

W("## Shared values")
W()
W("Values that apply across entries, tallied from the measurement file.")
W()
radii = collections.Counter()
trans = collections.Counter()
hovers = collections.Counter()
focus = collections.Counter()
focus_n = 0
for cid, c in C.items():
    for sname, s in c["states"].items():
        if "style" not in s:
            continue
        st = s["style"]
        r = st["borderTopLeftRadius"]
        if r != "0px" and s["rect"]["w"] > 4:
            radii[r] += 1
        if st["transitionDuration"] not in ("0s", ""):
            tf = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", st["transitionTimingFunction"])
            trans[f"{st['transitionDuration'].split(',')[0].strip()} {tf[0] if tf else st['transitionTimingFunction']}"] += 1
        if sname == "focus-visible":
            if "failed" in str(s.get("via", "")):
                focus["focus could not be driven"] += 1
                continue
            focus_n += 1
            if st["outlineStyle"] != "none" and float(st["outlineWidth"].replace("px", "")) > 0:
                focus[f"{st['outlineWidth']} {st['outlineStyle']} {colour(st['outlineColor'], role='border')} offset {st['outlineOffset']}"] += 1
            else:
                focus["no ring on the element"] += 1
for cid, c in C.items():
    a, b = c["states"].get("default"), c["states"].get("hover")
    if not a or not b or "style" not in a or "style" not in b:
        continue
    if a["style"]["backgroundColor"] != b["style"]["backgroundColor"]:
        hovers[f"{colour(a['style']['backgroundColor'])} to {colour(b['style']['backgroundColor'])}"] += 1
    elif a["style"]["color"] != b["style"]["color"]:
        hovers[f"text {colour(a['style']['color'], role='text')} to {colour(b['style']['color'], role='text')}"] += 1
    elif a["style"]["borderTopColor"] != b["style"]["borderTopColor"]:
        hovers[f"border {colour(a['style']['borderTopColor'], role='border')} to {colour(b['style']['borderTopColor'], role='border')}"] += 1
    elif a["style"]["fontWeight"] != b["style"]["fontWeight"]:
        hovers[f"weight {a['style']['fontWeight']} to {b['style']['fontWeight']}"] += 1
    elif painted(a) != painted(b):
        hovers["a painted ::before/::after or icon change"] += 1
    else:
        hovers["no change on the element"] += 1


def top(ctr, n):
    return ", ".join(f"{k} ({v})" for k, v in ctr.most_common(n))


W(f"**Radius.** {top(radii, 5) if radii else 'none — every corner on the site is 0px'}. 4px rounds the category quicklink pills and the floating label tabs of the size selects, 2px the Map/Satellite toggle, and the filter toggle's count dot is a 50% circle — every control edge stays square.")
W()
W(f"**Hover.** {top(hovers, 8)}. A hover stays quiet: the nav link goes bold and grows a 3px ink underline under its label (a `::before` bar), footer links pick up an underline, the ink buttons (ADD TO CART, the sign-in submit) deepen from #333333/#393939 to #252525, the quicklink pills go from a muted border to an ink keyline on a {colour('rgb(246, 245, 232)')} fill, the Search disclosure's Close icon dot darkens (#666666 to #343434), and the hero CTA card fills cream with ink text.")
W()
W(f"**Focus.** Of {focus_n} elements given a real keyboard focus: {top(focus, 6)}. Aesop paints no focus ring — the computed outlineWidth stays 0 on every measured control; focus is at most the hover's colour shift.")
W()
W(f"**Motion.** {top(trans, 6) if trans else 'Instant: every measured control reports transition-duration 0s'}. Eases are short and gentle: 0.5s ease-out colour fades on the header controls, 0.2s ease on field keylines, 0.25s ease-out on the ink buttons and CTA card, 0.3s on the quicklink pills. The stylesheets add a 0.1s max-height reveal on accordions and navigation groups and a 0.4s padding slide on the sliding content panels.")
W()
W("**Layout.** The header is a two-tier rail — a 30px utility row over a 50.8px nav row (50px at 390) — above a fluid grid. Fields are 40px, buttons and CTA cards 48px, the cart drawer 405px, the filter rail 400px and the sign-up dialog 970px; the hero band runs 720px tall at 1440. Hairline 1px keylines in ink or `color.creamDark` separate everything — several are painted as 1px box-shadows rather than borders.")
W()
W("**Accent.** One accent only: the tannin amber #945c26 (`color.amber`), on tile badges (New addition, Beloved formulation), promos and inline links. Everything else is ink — #333333 for text, keylines and the dark fills, #252525/#393939 for the deep and soft steps — on the cream grounds #fffef2, #ebeade and #f6f5e8.")
W()


# --------------------------------------------------------------------------- components

W("## Components")
W()
groups = collections.OrderedDict()
for cid, c in C.items():
    groups.setdefault(c["group"], []).append(cid)
for g, ids in groups.items():
    W(f"### {g}")
    W()
    if g in GROUP_INTRO:
        W(GROUP_INTRO[g])
        W()
    for cid in ids:
        c = C[cid]
        W(f"#### {c['title']}")
        W()
        W(f"<a id=\"{cid}\"></a>`{cid}`, on {c['page']}. {c.get('desc', '')}".rstrip())
        W()
        if c.get("missing"):
            W("*Not found on the captured pages — an honest miss, kept so the gap is visible.*")
            W()
            continue
        crops = []
        order = ("default", "hover", "focus-visible", "pressed", "focused", "filled", "selected", "open")
        for sname in [n for n in order if n in c["states"]] + sorted(n for n in c["states"] if n not in order):
            s = c["states"].get(sname)
            if s and s.get("crop") and Path(s["crop"]).exists():
                crops.append(f'<img src="{s["crop"]}" alt="{c["title"]}, {sname}" height="{min(120, max(24, round(s["rect"]["h"])))}"> ')
        if crops:
            W("".join(crops))
            W()
        rows = state_rows(c)
        if rows:
            W("| State | Values |")
            W("|---|---|")
            for name, d in rows:
                W(f"| {name} | {fmt(d)} |")
            W()
        cl = child_layers(c)
        if cl:
            W(f"Child layers: {cl}")
            W()

# --------------------------------------------------------------------------- gaps

W("## Gaps")
W()
W("- The Email sign up modal mounts as a cream shell (970 x 450 measured); its remote Demandware Newsletter-SignUp fragment did not render in headless Chromium, so the dialog's fields, checkboxes and submit were never measurable — `signup-field`, `signup-checkbox` and `signup-submit` are honest misses.")
W("- States that submit were never pressed: ADD TO CART, APPLY, the sign-in Submit, the store OK. Their hover, focus and pressed styles come from CDP-forced pseudo-classes and keyboard focus, not real clicks.")
W("- `search-panel`'s container eluded marking (the disclosure mounts under a different id), but `search-field` and `search-close` inside it are measured, and the open state is in screenshots. `cart-close` has no measurable button: the drawer closes on backdrop/Escape.")
W("- `qty-select` is absent on this PDP (a one-variant kit); the variant/size box is measured instead. `no-result-dialog` was measured at 415 x 211.")
W("- Cloudflare Turnstile gates second document loads per context and some system routes: PDPs are reached as a first load in a fresh context (see tools/capture/public/lib.mjs note), and a still-blocked route would be recorded, not fought.")
W("- Hover/focus on the 390 capture is not meaningful (a phone has neither); mobile entries cover layout and the burger drawer.")
W()

open("components.md", "w").write("\n".join(L) + "\n")
print(f"components.md: {len(C)} components, {n_states} states, {n_crops} crops, {len(L)} lines")
