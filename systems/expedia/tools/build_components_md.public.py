#!/usr/bin/env python3
"""Build components.md for the Expedia design reference.

Reads raw/components-computed.json (every component and state, measured), raw/layout.json,
tokens.json and screenshots/, and writes components.md next to them. Every value is a cell of
the measurement file, condensed: colours are hex followed by the palette token whose value
matches, the font family is named once per value, and a state row shows only what differs from
the first state. Adapted from the Gauth builder, which read markdown; this one reads the JSON
directly.

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


PAL = T["core"]["color"]["palette"]


def by_colour(first):
    """hex -> palette token, preferring the palette of the theme a component paints in, so a shared
    hex labels as that theme's colour rather than an identical one from another palette."""
    out = {}
    for theme in sorted((k for k in PAL if not k.startswith("$")), key=lambda k: k != first):
        for n, t in flat({theme: PAL[theme]}):
            if t["$type"] == "color":
                out.setdefault(t["$value"], "color.palette." + n)
    return out


# The pages pin data-theme-light="light-1" on the body; the promo band re-themes itself to
# marketing-3 (README, Themes), so its colours label from that palette.
COMPONENT_THEME = {"marketing-band": "marketing3"}
BY_THEME = {t: by_colour(t) for t in {"light1", *COMPONENT_THEME.values()}}
BY_COLOR = BY_THEME["light1"]


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


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "outline", "text", "transition", "transform", "opacity", "icon", "placeholder", "child paint"]


def paint_diff(st, base):
    """Painted-layer deltas between two states, by node. The wrapper's own
    computed style is not the whole story: fields repaint their inner input's
    border and hearts outline their inner button, neither of which reaches the
    root — those changes live only in the captured paint list."""
    # Pair layers by node label and occurrence: two sibling `span`s are two layers, and a dict keyed
    # by label alone would compare the second against the first.
    bp, seen = {}, {}
    for p in (base or {}).get("paint") or []:
        bp.setdefault(p["node"], []).append(p)
    out = []
    for p in (st or {}).get("paint") or []:
        i = seen[p["node"]] = seen.get(p["node"], -1) + 1
        same = bp.get(p["node"]) or []
        b = same[i] if i < len(same) else None
        if b is None:
            continue
        changes = []
        if p.get("outline") != b.get("outline") and p.get("outline"):
            changes.append("outline " + colour(p["outline"]))
        if p.get("border") != b.get("border") and p.get("border"):
            changes.append("border " + colour(p["border"].split(" | ")[0][2:]))
        if p.get("shadow") != b.get("shadow") and p.get("shadow"):
            changes.append("ring " + colour(p["shadow"]))
        if p.get("bg") != b.get("bg") and p.get("bg"):
            changes.append("background " + colour(p["bg"]))
        if changes:
            out.append(re.sub(r"\..*$", "", p["node"]) + ": " + ", ".join(changes))
    return "; ".join(out)


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
            # identical root styles can still hide a state painted on a child
            # layer (the fields' focus border, the hearts' focus outline)
            pd = paint_diff(c["states"][st], c["states"][states[0]])
            if pd:
                diff["child paint"] = pd
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

PAGE_NAME = {"home": "home", "home-i": "home (hydrated)", "search": "hotel results", "mobile": "home"}

GROUP_INTRO = {
    "Header and navigation": "The 72px global header: the Expedia logo, the Shop travel menu, the USD currency control, List your property, Support, Trips, the notifications bell and Sign in. The sign-in card opens through the header's no-JS checkbox mechanism; nothing navigates to a login.",
    "Search form": "The multi-product search card under the hero: the product tabs (Stays, Flights, Cars, Packages, Things to do, Cruises), the three uitk-field triggers (Where to?, Dates, Travelers), the blue Search button and the bundle checkbox.",
    "Menus and dialogs": "What the search fields open, measured on the same page hydrated with Expedia's own JavaScript: the two-month calendar dialog with its range chips, the travellers stepper menu and the Where-to destination panel.",
    "Home content": "Below the search shell: the Reckless XPD hero title, the marketing-3 re-themed promo band, the deals carousels of cards with save hearts, and the footer.",
    "Hotel results": "The Hotel-Search results page: the compact sticky search form, the stay-type segmented control, the sort pill, the filter rail with its map card, and the result cards with gallery, VIP badge, rating, savings pill and price block.",
    "Mobile (390 wide)": "A few components as a phone draws them, at 390 x 844 at 2x.",
}

SHOTS = [
    ("home", "Home. Hero photo, the Reckless XPD title, the multi-product search card, marketing bands, deals carousels, footer. The sign-in card and Shop travel menu are shown open.", "/"),
    ("home-i", "Home, hydrated. The calendar dialog, travellers menu and Where-to panel opened by clicking the field triggers; the Flights tab variant.", "/ (hydrated)"),
    ("search", "Hotel search results. Compact search form, stay-type tabs, sort pill open, filter rail and map card, property cards.", "/Hotel-Search"),
]
MOBILE = [
    ("mobile-home", "Home at 390: the hero and search card, the full page.", "/"),
    ("mobile-home-i", "Home at 390, hydrated: the calendar sheet.", "/ (hydrated)"),
    ("mobile-search", "Hotel results at 390.", "/Hotel-Search"),
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

W("# Expedia components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from www.expedia.com on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, searched for, booked, created, sent or uploaded.")
W()
W("expedia.com answers automation with a 429 \"Bot or Not?\" challenge, so the DOM is a Wayback snapshot of the public home and hotel-search pages served locally and painted with Expedia's live travel-assets.com CSS and fonts. Entries on the `home-i` page were read on the same snapshot hydrated with the site's own JavaScript, so the field panels (calendar, travellers, destination) open on click; hydration's API refetches fail on the archived page, so only no-submit UI states were read.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [raw/pages.md](raw/pages.md).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Centra No2 14/20 400, #191e3b`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (`home-i` is the hydrated home). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).")
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
    ("Sign-in card", "header, every page", "the header's no-JS checkbox menu, forced open; the Sign in button inside was hovered only, never followed", "[home-light-signin-open](screenshots/home-light-signin-open.png), [signin-card](#sign-in-card)"),
    ("Shop travel menu", "header", "the Shop travel control, opened by its trigger", "[home-light-shoptravel-open](screenshots/home-light-shoptravel-open.png)"),
    ("Calendar dialog", "home search form, hydrated", "the Dates field clicked; a selected day and range chip read at rest; Done never pressed to search", "[home-i-light-calendar-open](screenshots/home-i-light-calendar-open.png), [calendar-dialog](#calendar-dialog)"),
    ("Travellers menu", "home search form, hydrated", "the Travelers field clicked; the steppers left untouched", "[home-i-light-travelers-open](screenshots/home-i-light-travelers-open.png), [travelers-menu](#travelers-menu)"),
    ("Where-to panel", "home search form, hydrated", "the Where to? field clicked; sample text typed and deleted, nothing searched", "[home-i-light-whereto-open](screenshots/home-i-light-whereto-open.png), [whereto-panel](#destination-panel)"),
    ("Flights tab", "home search form, hydrated", "the Flights product tab", "[home-i-light-flights-tab](screenshots/home-i-light-flights-tab.png)"),
    ("Sort pill, open", "hotel results", "the Sort by pill clicked; no order applied", "[search-light-sort-open](screenshots/search-light-sort-open.png)"),
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
    rest = next((v for v in c["states"].values() if "style" in v), None)
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0
    # A ring painted on a child layer while the wrapper's own outline stays
    # none: the hearts outline their inner favorite-button, and the fields
    # trade the inner input's grey border for blue plus an inset ring. The
    # wrapper's outline alone would call all of those "no change".
    child_ring = next((n["outline"] for n in st.get("paint", []) if n.get("outline") and not ring), None)
    desc = (f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring
            else f"on a child layer: {colour(child_ring)}" if child_ring else None)
    foc.append((k, ring or bool(child_ring), desc, paint_diff(st, rest)))
with_ring = [f"`{k}` ({r})" for k, ringed, r, pd in foc if ringed]
with_child = [f"`{k}` ({pd})" for k, ringed, r, pd in foc if not ringed and pd]
without = [f"`{k}`" for k, ringed, r, pd in foc if not ringed and not pd]
parts = [f"{len(with_ring)} draw a ring: {', '.join(with_ring)}."]
if with_child:
    parts.append(f"{len(with_child)} show the change only on a painted child layer: {', '.join(with_child)}.")
if without:
    parts.append(f"The other {len(without)} show no measured change: {', '.join(without)}.")
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {' '.join(parts)} The header currency control could not be reached by keyboard in the static capture, so its focus state is unmeasured rather than absent.")
W()
W("**Pressed.** Pressed states are forced with DevTools (`:active:hover`), so no button or link ever fired. Expedia's controls react to press mostly through their scrim layers: buttons keep their fill and the overlay opacity token steps up (`--egds-button-opacity-overlay-*`), which computed styles on the root do not always show.")
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


for page in ["home", "search"]:
    W(f"| {page} | " + " | ".join(grid_of(f"{page}@{w}") for w in (1440, 1920, 1024, 390)) + " |")
W()
W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
# PRODUCT (adapt): the card-like components to compare in one table.
for k in ["search-shell", "signin-card", "deal-card", "property-card", "map-card", "filters", "calendar-dialog", "whereto-panel", "travelers-menu", "m-card"]:
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
        BY_COLOR = BY_THEME[COMPONENT_THEME.get(k, "light1")]  # colour() reads the global
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

BY_COLOR = BY_THEME["light1"]  # back to the page theme for the shared sections
# ------------------------------------------------ gaps
W("## Gaps")
W()
W("### Pages")
W()
W("- **The live site.** expedia.com answers every automated request with a 429 \"Bot or Not?\" challenge (headless and headed, several user agents, regional domains). The DOM evidence is therefore a Wayback snapshot: fresh component styles come from live CDN CSS, but a page that changed after the snapshot or that the archive renders differently is not covered. Flights, cars, packages, things-to-do and cruise results pages were not captured.")
W("- **Signed-in pages.** Nothing behind sign-in: trips, loyalty account, member pricing, checkout and booking, settings. The header sign-in card was measured at rest; its links were never followed.")
W("- **Anything that sends or creates.** No search was submitted (the results page is an archived capture of someone else's public query), no booking started, no sort order applied, no destination typed and kept, no filter toggled.")
W("- **Hydrated results.** On the archived search page the app's own JS refetches its GraphQL and empties regions, so the results page was measured statically; the sort pill's open state is a screenshot only.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **The header currency control** could not be reached by keyboard focus in the static capture; its focus-visible state is unmeasured.")
W("- **The checkbox, switch and radio states** were read resting and hovered only; nothing was toggled.")
W("- **Disabled states** were not seen on any public control except the stay-type segmented options, which render selected-and-disabled at rest.")
W()
W("### Themes")
W()
W("The pages pin `data-theme-light=\"light-1\"` on the body; `prefers-color-scheme: dark` changes nothing (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)). The promo sections re-theme to `marketing-3` via their own `data-theme-light` attribute. The stylesheets also ship `dark-1`, `dark-2`, `bright-1`, `marketing-1`, `marketing-2`, `ai-local-1`, `romie` and eight global-loyalty palettes; tokens.json holds sets for the five themes resolved on the pages (light-1, dark-1, dark-2, marketing-3, bright-1) and every palette literal in `core.color.palette`.")
W()
W("### Fonts")
W()
W("- **Centra No2** (the UI face) and **Reckless XPD** (the display face) are Expedia's proprietary fonts, served from travel-assets.com; they loaded during the capture, so measurements name the real faces. The style guide falls back to the system stack without the font files.")
W()
W("### Screenshots")
W()
W("- Hotel photos, destination imagery and the hero are Expedia's and the properties' content and appear only inside screenshots and crops.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- No personal data was captured: the pages are public signed-out surfaces, and the archived search results carry no account information.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops")
