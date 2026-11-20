#!/usr/bin/env python3
"""Build components.md for the ARKET design reference.

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

PAGE_NAME = {"home": "women landing", "clothing": "clothing listing", "service": "customer-service", "account": "account gate"}

GROUP_INTRO = {
    "Consent and location dialogs": "The two overlays the storefront mounts before the page is usable: the cookie-consent card and the location picker. Measured as they arrive, never answered.",
    "Shell and navigation": "The locale notice, the promo strip and the sticky header: wordmark, search field, account, wishlist and cart icons, and the category nav that opens the drawer.",
    "Home": "The /en-ww/women/ landing: campaign tiles and editorial sections.",
    "Listing page": "The category grid: Filter/Sort/View controls, product cards with image carousels, hover-revealed quick-adds and the colour count chip.",
    "Customer service": "The help page's disclosure rows and links.",
    "Account gate": "The Login/Signup gate: email field and continue, measured, never submitted.",
    "Footer": "The link columns, headings, socials and legal.",
    "Mobile (390 wide)": "The same surface at phone width, with the menu open.",
}

SHOTS = [
    ("women", "Women landing", "/en-ww/women/"),
    ("new-arrivals", "New arrivals", "/en-ww/women/new-arrivals/"),
    ("clothing", "Clothing listing", "/en-ww/women/clothing/"),
    ("men-clothing", "Men clothing", "/en-ww/men/clothing/"),
    ("gift-shop", "Gift shop", "/en-ww/gift-shop/"),
    ("editorial", "Editorial / About", "/en-ww/editorial/"),
    ("customer-service", "Customer service", "/en-ww/customer-service/"),
    ("account", "Account gate", "/en-ww/account/"),
    ("previous-collections", "Previous collections", "/en-ww/previous-collections/women/"),
]
MOBILE = [
    ("mobile-home", "Women landing, phone", "/en-ww/women/"),
    ("mobile-clothing", "Clothing listing, phone", "/en-ww/women/clothing/"),
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
icons = []

W("# ARKET components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from arket.com on {J['_meta']['read']}, signed out, in headed real Chrome at 1440 x 900 (the Mobile group at 390 x 844) — Akamai serves headless Chromium Access Denied (403), and also blocks every /en-ww/product/<slug>-<id>/ URL and, for this client, the /en-ww/ root: the shell and dialogs were measured on /en-ww/women/ — with computed styles read from the running page. Nothing was bought, sent, submitted or signed into.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png`: the site paints one light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).")
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
    ("Cookie consent, as it arrives", "women landing", "mounted on first load; measured and hidden, never answered", "[consent-card](#cookie-consent-card)"),
    ("Location dialog, as it arrives", "women landing", "mounted on first load; measured and hidden, never answered", "[location-dialog](#location-dialog)"),
    ("Search field, focused", "women landing", "the header search input clicked into; nothing typed or sent", "[search-field](#search-field)"),
    ("Cart drawer, empty", "women landing", "the cart icon's own press", "[cart-drawer](#cart-drawer-empty)"),
    ("Filter panel, open", "clothing", "the Filter button's own press; nothing applied", "[filter-panel](#filter-panel-open)"),
    ("Mobile menu, open", "women landing, phone", "the menu button's own toggle", "[m-menu-open](#mobile-menu-open)"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement files.")
W()
TRANSPARENT = re.compile(r"rgba\(\d+, \d+, \d+, 0\)$")
foc, failed = [], []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st or "style" not in st:
        continue
    if "failed" in str(st.get("via", "")):
        failed.append(k)
        continue
    s = st["style"]
    base = (c["states"].get("default") or {}).get("style") or {}
    # A focus only counts as visible when something a user can see changed:
    # a non-transparent outline, or a shadow/border/colour repaint. A 2px
    # transparent outline (the Tailwind focus-visible reset) is not a ring.
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0 and not TRANSPARENT.match(s["outlineColor"] or "")
    if ring:
        foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}"))
    elif any(s.get(f) != base.get(f) for f in ("boxShadow", "borderTopColor", "backgroundColor", "color")):
        changed = [f for f in ("boxShadow", "borderTopColor", "backgroundColor", "color") if s.get(f) != base.get(f)]
        foc.append((k, "visible change in " + "/".join(changed)))
    else:
        foc.append((k, None))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
line = f"**Focus.** {len(foc)} components were given a real keyboard focus"
if failed:
    line += f" (a further {len(failed)} could not be driven: {', '.join('`'+x+'`' for x in failed)})"
line += f". {len(with_ring)} show a visible focus state: {', '.join(with_ring)}." if with_ring else ". None shows a visible focus state."
if without:
    line += f" The other {len(without)} show no change a keyboard user can see: {', '.join(without)}."
W(line)
W()
W("**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): a state a real press could submit (consent, location, gate) was never pressed. Nothing was bought, sent or signed into.")
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
def covering_layer(st):
    """The first painted layer inside the component that fills or frames at least 90% of its box. The
    capture records a layer's size but not its offset, so the most it can cover is the smaller width
    times the smaller height: a wide, short child (600x100 in a 300x200 card) covers at most half the
    card and is not its look, though its own area is larger (the kit's rule)."""
    rw, rh = st["rect"]["w"], st["rect"]["h"]
    for x in st.get("paint") or []:
        dims = [float(n) for n in re.findall(r"[\d.]+", x.get("size", ""))[:2]]
        if len(dims) == 2 and rw and rh and min(dims[0], rw) * min(dims[1], rh) >= 0.9 * rw * rh and (x.get("bg") or x.get("border")):
            return x
    return None


W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
# PRODUCT (adapt): the card-like components to compare in one table.
for k in ["consent-card", "location-dialog", "filter-panel", "cart-drawer", "product-card", "search-field", "gate-field"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if "style" in s), None)
    if st is None:
        continue
    p = props(st)
    if p["background"] == "transparent" and "border" not in p and st.get("paint"):
        # The root paints nothing (a radius alone paints nothing): its look is a painted child that
        # covers it (at least 90% of its box), named in the row. A smaller child (a CTA's ::before, a
        # badge, a divider) is not the card, so the row then keeps the root's own values.
        p0 = covering_layer(st)
        if p0:
            p = dict(p, border=colour(p0["border"].split(" | ")[0][2:]) if p0.get("border") else "-", radius=p0.get("radius") or p.get("radius", "-"),
                     background=(colour(p0["bg"]) if p0.get("bg") else "-") + f" (on `{p0['node']}`)",
                     shadow=colour(p0.get("shadow", ""), tokens=False) or "none")
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are ARKET's artwork. Declared under layoutGaps in the catalog entry.")
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
W("- **Product pages (PDP).** Akamai answers every /en-ww/product/<slug>-<id>/ URL with 403 for this client, document and RSC fetch alike, so no PDP was captured; PDP-looking values come from the listing cards instead. **The /en-ww/ root** is blocked the same way at capture time; the women landing /en-ww/women/ stands in for it.")
W("- **The account behind the gate.** /en-ww/account/ stops at the Login/Signup gate; no sign-in was attempted. Checkout, the filled cart and wishlist contents were never reached.")
W("- **Anything that buys, sends, submits or signs in.** Nothing was added to the bag, no consent or location answer was given, no form was submitted. Quick-add buttons were measured under a forced card hover, never pressed.")
_typed = [k for k, c in C.items() for st in ("focused", "filled") if st in c.get("states", {})]
W("- **Anything that sends, submits or signs in.** No form was submitted, no prompt was sent, no account was created." + (f" Fields clicked into (and, where a `filled` state exists, typed into and cleared), never submitted: {', '.join(f'`{k}`' for k in dict.fromkeys(_typed))}." if _typed else ""))
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Disabled, error and loading states** were not seen on the public surface. The card quick-add/carousel controls only exist under a card :hover, captured via a CDP-forced hover.")
W()
W("### Themes")
W()
W("The site paints one light theme on every captured route: no dark class or attribute is bound, so the dark set is not emitted. The @theme palette is recorded in [raw/css-vars.json](raw/css-vars.json).")
W()
W("### Fonts")
W()
W("- **The faces** are arketSansMono (everything) and arketSCSansMono (small-caps chips), self-hosted woff with Arial-metric fallbacks; the consent and account surfaces fall back to 'Arket Sans'/'Arket-Sans-Mono'. The style guide renders with system fallbacks.")
W("- Photography, campaign art and the ARKET wordmark in the screenshots are ARKET's property.")
W()
W("### Screenshots")
W()
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W("- The changelog page is 91,833 px tall; its -full shot is the whole page stitched from 7 tiles.")
W()
W("### Content left out")
W()
W("- Product photography, campaign imagery and the wordmark are ARKET's content; only the frames and components were measured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
