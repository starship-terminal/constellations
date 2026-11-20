#!/usr/bin/env python3
"""Build components.md for the Airbnb design reference.

Reads raw/components-computed.json (every component and state, measured),
tokens.json and screenshots/, and writes components.md next to them. Every
value is a cell of the measurement file, condensed: colours are hex followed
by the palette token whose value matches, the font family is named once per
value, and a state row shows only what differs from the first state. A
raw/layout.json or icons/INDEX.tsv, when present, adds the layout grid and the
icon index; airbnb.com's capture ships neither, so those sections are skipped.

Deterministic: re-running it on the same inputs reproduces components.md byte for byte.
Run from anywhere: python3 tools/build_components_md.public.py
"""
import json, os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
J = json.load(open("raw/components-computed.json"))
C = J["components"]
LAYOUT = json.load(open("raw/layout.json")) if Path("raw/layout.json").exists() else {}
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

    # one pass over both spellings, so a colour labelled from color(srgb ...)
    # is never re-matched as rgba() and labelled a second time
    def sub(m):
        if m.group(1) is not None:
            return label(norm(*(round(float(x) * 255) for x in m.group(1, 2, 3)), m.group(4)))
        return label(norm(*m.group(5, 6, 7), m.group(8)))

    return re.sub(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)"
                  r"|rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)", sub, c)


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
    # painted pseudo elements count toward the state: the menu's hover fill
    # and every focus ring it draws live on ::before, and a state table that
    # only compared the root would report them as unchanged
    for pe, tag in (("::before", "before"), ("::after", "after")):
        p = v.get(pe)
        if not p:
            continue
        bits = []
        if p.get("backgroundColor") and p["backgroundColor"] != "rgba(0, 0, 0, 0)":
            bits.append("background " + colour(p["backgroundColor"]))
        if p.get("backgroundImage") and p["backgroundImage"] != "none":
            bits.append("image " + colour(p["backgroundImage"])[:60])
        if p.get("boxShadow") and p["boxShadow"] != "none":
            bits.append("shadow " + colour(p["boxShadow"], tokens=False))
        if p.get("borderTopWidth") and p["borderTopWidth"] != "0px":
            bits.append("border " + p["borderTopWidth"] + " " + colour(p["borderTopColor"]))
        if p.get("borderRadius") and p["borderRadius"] != "0px":
            bits.append("radius " + p["borderRadius"])
        if bits:
            o[tag] = ", ".join(bits)
    return o


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "outline", "text", "transition", "transform", "opacity", "icon", "placeholder", "before", "after", "layers"]


# The painted non-pseudo nodes inside the component, as a state-comparison
# signature: pseudo elements are compared through the before/after props.
LAYER_PAINT = ("bg", "bgImage", "shadow", "outline", "border")


def layer_map(v):
    m = {}
    for pl in v.get("paint") or []:
        if "::" in pl["node"]:
            continue
        m[pl["node"]] = tuple(pl.get(k) for k in LAYER_PAINT)
    return m


def layer_diff(base_m, new_m):
    """Readable note of which painted child changed, with the new state's paint."""
    bits = []
    for node in dict.fromkeys(list(new_m) + list(base_m)):
        if new_m.get(node) == base_m.get(node):
            continue
        name = node.split(".")[0]
        vals = new_m.get(node) or base_m.get(node) or ()
        desc = "; ".join(f"{k} {colour(str(x)) if x else 'none'}" for k, x in zip(LAYER_PAINT, vals) if x)
        bits.append(f"{name} ({desc})" if desc else name)
        if len(bits) >= 4:
            break
    return "; ".join(bits)


def state_rows(c):
    states = [s for s in c["states"] if "style" in c["states"][s]]
    if not states:
        return [], states
    base = props(c["states"][states[0]])
    base_l = layer_map(c["states"][states[0]])
    rows = [(states[0], base)]
    same = []
    for st in states[1:]:
        p = props(c["states"][st])
        diff = {k: p[k] for k in ORDER if k in p and p.get(k) != base.get(k)}
        for k in ORDER:
            if k in base and k not in p:
                diff[k] = "none"
        # a state is not "same" when the painted layers inside the component
        # changed, even where every root prop is identical
        lm = layer_map(c["states"][st])
        if lm != base_l:
            note = layer_diff(base_l, lm)
            if note:
                diff["layers"] = note
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

PAGE_NAME = {"home": "home", "search": "search results", "room": "room", "help": "Help Centre",
             "host": "host landing", "mobile": "home"}

GROUP_INTRO = {
    "Header and navigation": "The fixed top bar every page shares: the Bélo logo, the Homes / Experiences / Services category tabs with their icons, \"Become a host\", the language globe and the profile menu. The bar is 96px tall, white, with the search pill centred under it.",
    "Search bar": "The booking search: a white pill of Where / When / Who segments with hairline dividers and the pink gradient submit button. Clicking a segment expands the bar into the suggestion panel — a local toggle, never submitted.",
    "Home galleries": "The home page's recommendation rails: a section title with a chevron, then cards that scroll sideways behind rail arrows. Each card is a 12px-radius photo with a Guest favourite badge and a wishlist heart, then title, price and star rating.",
    "Search results": "The results page: the mini search pill, the Filters button and filter chips, then full-width result cards with the fees-included tag.",
    "Room page": "A listing's own page: the photo mosaic, the reserve card in the right column, the guest plaque and the promo strip. Nothing was booked or saved.",
    "Help Centre": "The Help Centre home: the headline, the search field and topic tiles.",
    "Host landing": "The host recruiting page: the earnings headline, the Get started CTA and the earnings estimator card, measured at rest.",
    "Mobile (390 wide)": "A few components as a phone draws them, at 390 x 844 with an iPhone user agent.",
}

SHOTS = [
    ("home", "Home. The header with the category tabs, the search pill, gallery rails of home cards and the footer. The load-time modal, the search panel open and a card hovered are separate captures.", "/"),
    ("experiences", "Experiences landing. Same shell with the experiences gallery.", "/experiences"),
    ("services", "Services landing (chefs, photography, spa).", "/services"),
    ("search", "Search results for Tokyo. The mini search pill, filter chips, result cards and the fees tag; the load-time modal is a separate capture.", "/s/Tokyo--Japan/homes"),
    ("room", "A Tokyo listing's page: title, photo grid, reserve card, host row, reviews and the footer.", "/rooms/<id> (a public listing the results page linked)"),
    ("help", "Help Centre. The headline, the search field and the topic grid.", "/help"),
    ("host", "Host landing. The earnings headline, Get started and the estimator card.", "/host/homes"),
]
MOBILE = [
    ("mobile-home", "Home at 390: the compact search pill and the listing rail.", "/"),
    ("mobile-search", "Search results at 390: the pill and the card column.", "/s/Tokyo--Japan/homes"),
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

W("# Airbnb components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from www.airbnb.com — which geo-redirected to www.airbnb.com.sg from this network, the same design system on a regional mirror — on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, searched, booked or sent.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Airbnb Cereal VF 14/18 500, #222222`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`). Most are at 2x; a crop over about 1.2 megapixels is saved at 1x — each state's `cropScale` in [raw/components-computed.json](raw/components-computed.json) says which. Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (airbnb.com paints one light theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).")
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
    ("Load-time modal (a sign-up/coachmark card)", "home, search, room, on load", "at rest; then hidden by the overlay sweep for every other capture — never clicked", "[home-light-modal](screenshots/home-light-modal.png), [search-light-modal](screenshots/search-light-modal.png), [room-light-modal](screenshots/room-light-modal.png), [mobile-search-light-modal](screenshots/mobile-search-light-modal.png)"),
    ("Search panel, open", "home", "the Where segment clicked — a local UI toggle; nothing was searched", "[home-light-search-open](screenshots/home-light-search-open.png), [search-panel-open](#search-panel-open)"),
    ("Listing card, hovered", "home", "a real pointer hover over the first rail card", "[home-light-card-hover](screenshots/home-light-card-hover.png), [listing-card](#listing-card)"),
    ("Wishlist heart states", "home and search", "hovered, focused and a forced press; a real tap opens the sign-up sheet signed out, so pressed is forced", "[card-heart](#card-heart), [result-heart](#result-heart)"),
    ("Reserve card fields", "room", "the date and guest fields hovered only; a real click opens pickers the kit leaves shut", "[reserve-field](#reserve-field)"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement files.")
W()
def pseudo_shadow(st):
    return any((st.get(pe) or {}).get("boxShadow", "none") not in (None, "none") for pe in ("::before", "::after"))


foc = []
for k, c in C.items():
    if c.get("missing"):
        continue  # stale states from an earlier run are not evidence
    st = c["states"].get("focus-visible")
    if not st or "style" not in st:
        continue
    s = st["style"]
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0
    foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else None))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
sh_ring = []
for k, c in C.items():
    if c.get("missing"):
        continue
    st = c["states"].get("focus-visible")
    if not st or "style" not in st:
        continue
    s = st["style"]
    # the ring counts whether the root or a pseudo element paints it — the
    # menu's focus circle lives on ::before
    if (s["boxShadow"] != "none" or pseudo_shadow(st)) and s["outlineStyle"] == "none":
        sh_ring.append(f"`{k}`")
without = [w for w in without if w.strip("`") not in {x.strip("`") for x in sh_ring}]
focus_fail = [k for k, c in C.items() if (c["states"].get("focus-visible") or {}).get("via") == "focus failed"]
fail_txt = (" " + " and ".join(f"`{k}`" for k in focus_fail) +
            " could not be given a real keyboard focus at all, so its focus state is unmeasured rather than reported.") if focus_fail else ""
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} draw an outline ring ({', '.join(with_ring)}), the category tabs' being the 2px `#222` outline 4px out. The other buttons draw it as a box-shadow instead: a white 2px halo plus a `#222` ring hugging the shape ({', '.join(sh_ring)}). {', '.join(without) + ' show' if without else 'None shows'} neither on the measured element.{fail_txt}")
W()
W("**Pressed.** Airbnb's controls shrink rather than change colour when pressed: buttons scale to about 0.96 (the header links, the search submit, the filter chips), the wishlist heart to 0.92, and the footer link stays put. Hovering greys the background behind the target (`#f7f7f7`); the search bar deepens its shadow.")
W()
W("**Motion.** Transitions measured on the components, by duration.")
W()
W("| Duration | Easing | Property | Where |")
W("|---|---|---|---|")
mot = {}
for k, c in C.items():
    if c.get("missing"):
        continue
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
if LAYOUT:
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

    for page in ["home", "search", "room", "help", "host"]:
        W(f"| {page} | " + " | ".join(grid_of(f"{page}@{w}") for w in (1440, 1920, 1024, 390)) + " |")
    W()
def covers(x, st):
    """True when a painted layer fills or frames at least 90% of the component's box. The capture
    records a layer's size but not its offset, so the most it can cover is the smaller width times
    the smaller height (the kit's covering_layer rule)."""
    rw, rh = st["rect"]["w"], st["rect"]["h"]
    dims = [float(n) for n in re.findall(r"[\d.]+", x.get("size", ""))[:2]]
    return len(dims) == 2 and bool(rw and rh) and min(dims[0], rw) * min(dims[1], rh) >= 0.9 * rw * rh


W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
# PRODUCT (adapt): the card-like components to compare in one table.
for k in ["listing-card", "result-card", "search-bar", "search-panel-open", "help-tile", "estimator-card", "reserve-card", "promo-strip", "m-listing-card"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if "style" in s), None)
    if st is None:
        continue
    p = props(st)
    # a root that paints nothing borrows its look from the painted children —
    # property by property, each from the layer that actually paints it, so a
    # real root value is never overwritten and a missing one (reserve-card's
    # shadow lives on the aside, not the white inner div) is not lost
    # Only a layer that covers at least 90% of the root's box can stand in for
    # it: a divider, badge or CTA inside the card is not the card's look.
    if ("radius" not in p or p["background"] == "transparent" or "border" not in p or "shadow" not in p) and st.get("paint"):
        paints = [x for x in st["paint"] if covers(x, st)]
        p = dict(p)

        def first(k):
            e = next((x for x in paints if x.get(k)), None)
            return e[k] if e else None
        if "border" not in p and first("border"):
            p["border"] = colour(first("border").split(" | ")[0][2:])
        if "radius" not in p and first("radius"):
            p["radius"] = first("radius")
        if p.get("background") == "transparent" and first("bg"):
            p["background"] = colour(first("bg"))
        if "shadow" not in p and first("shadow"):
            layers = [x.strip() for x in re.split(r",(?![^(]*\))", colour(first("shadow"), tokens=False))]
            layers = [x for x in layers if not x.startswith("transparent")]
            if layers:
                p["shadow"] = ", ".join(layers)
    W(f"| [{c['title']}](#{k}) | {p['size']} | {p.get('border', '-')} | {p.get('radius', '-')} | {p.get('background', '-')} | {p.get('shadow', 'none')} | {p.get('padding', '0')} |")
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
        W(f"#### {c['title']} <a id=\"{k}\"></a>")
        desc = (c.get("desc") or "").strip()
        if desc and not desc.endswith((".", ")", '"')):
            desc += "."
        where = PAGE_NAME.get(c["page"], c["page"])
        W(f"{desc + ' ' if desc else ''}Read as `{k}` on the {where} page{' at 390 wide' if g.startswith('Mobile') else ''}.")
        W()
        if c.get("missing"):
            W("Not on the page when it was captured." + (" " + c["note"] if c.get("note") else ""))
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
if icons:
    W()
    W("## Icons")
    W()
    W(f"{len(icons)} SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. The SVGs are Airbnb's property, kept for reference only.")
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
W("- **Signed-in pages.** Nothing behind sign-in was captured: trips, wishlists, the host dashboard, account settings, checkout and messages. The kit never signs in.")
W("- **Anything that sends or creates.** No search was submitted (the Where segment was clicked into its panel and left there), no booking was made, no listing was saved, no help question was sent, no host sign-up was started, no filter was applied.")
W("- **The map.** The results page's interactive map and its price pills load late and sit in canvases; the `fees-tag` entry is the pill chrome, not the map itself.")
W("- **The app and other locales.** airbnb.com redirects by geography (this capture landed on the .sg mirror); the native apps and logged-out variants in other regions can draw different coachmarks and promos.")
W("- **The wishlist sheet.** Tapping a heart signed out opens a sign-up sheet; the heart's own states are measured but the sheet is not opened.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools (`CSS.forcePseudoState`) on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **The reserve card's pickers** (date calendar, guest stepper) were hovered but never opened — a click opens UI the kit leaves shut; nothing was booked.")
W("- **Search suggestions** come from the locale and the account; the panel's rows are a snapshot, not an exhaustive list.")
W("- **Disabled states** were not seen on any public control.")
W()
W("### Themes")
W()
W("airbnb.com paints one light theme: every page sets `data-color-scheme=\"light\"` on its roots and `prefersDarkChangesPage` is false on every capture (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)). The stylesheets do declare a full dark palette — the always-dark `.c12bynq4` theme class, and `.c1r7ywgw` rebinding every `--palette-*` name to `--x-dark` under `prefers-color-scheme: dark` — so the token file ships those declared values as a `dark` set, clearly marked never-applied. There is no theme switch in the header, the menus or the footer.")
W()
W("### Fonts")
W()
W("- **Airbnb Cereal VF** is Airbnb's variable face (203 `@font-face` declarations capture its weights); it is served from a0.muscache.com and is not on Google Fonts; the style guide falls back to the system font.")
W()
W("### Screenshots")
W()
W("- Listing photos, avatars and editorial images are Airbnb/host content and appear only inside screenshots and crops. The rails lazy-load, so a second capture of the same page can draw different listings.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Reviews, listing copy and help articles were not transcribed; only the frames around them were measured.")
W("- No personal data was captured: the pages were read signed out, and no location was searched for.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops,", len(icons), "icons")
