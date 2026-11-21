#!/usr/bin/env python3
"""Build components.md for the Acne Studios design reference.

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
    "bg": ["action.", "background.", "color.blue", "color.grey", "color.black", "color.white", "text.", "border."],
    "border": ["border.", "action.selected", "color.blue", "color.grey", "text.", "background."],
    "text": ["text.", "action.", "color.blue", "color.grey", "color.black", "color.white", "border."],
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
    return {"Helvetica Now Text": "Helvetica Now Text", "Helvetica Monospaced Pro": "Helvetica Monospaced Pro"}.get(first, first)


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


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "backdrop", "outline", "text", "transition", "transform", "opacity", "icon", "placeholder"]


def state_rows(c):
    """The first state lists every value; later rows list only what changed."""
    rows = []
    states = [s for s, v in c["states"].items() if "style" in v]
    if not states:
        return rows
    base = props(c["states"][states[0]])
    rows.append((states[0], base))
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
        bits = [re.sub(r"\..*$", "", p["node"]) if "::" not in p["node"] else p["node"].split(".")[0], p["size"].replace(".0x", "x").replace(".0", "")]
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
        out.append(" ".join(bits))
    return "; ".join(out).replace("|", "/")


# --------------------------------------------------------------------------- page and group text

GROUP_INTRO = {
    "Shell and navigation": "The 60px header every page shares (45px at 390): left the section triggers WOMAN MAN BAGS SCARVES GIFTS, centre the Acne Studios wordmark linking home, right SEARCH HELP ACCOUNT and the BAG count (`00` empty). White ground, 1px hairline rules top and bottom drawn as inset shadows; every item is a header-style 12/20 caps label on a full-height 60px hit row that greys to #6b6b6b on hover.",
    "Home": "The home canvas: a full-bleed black campaign band with the giant white wordmark set over the photo, a GIFT GUIDE eyebrow top-left and WOMEN'S/MEN'S GIFT GUIDE link bars at the foot, then campaign tiles and the footer.",
    "Category page (PLP)": "A category page such as WOMEN'S NEW ARRIVALS: the under-header subnav (New Arrivals, Gifts for Her, Winter Dressing), the FILTER & SORTING rail trigger, then the product grid — 4-span tiles, photo, caps name, price. Prices on the PLP are Helvetica Now Text, not the PDP's monospace.",
    "Product page (PDP)": "A product detail page: sticky breadcrumbs over a two-column canvas (gallery left, purchase column right) — caps title, colourway in muted grey, monospace price, the Fit Predictor line, the size grid, the electric-blue ADD TO BAG bar beside the white wishlist button, then expandable service rows and the spec list.",
    "Panels and overlays": "The right-side drawers, each 360 wide on opaque white with a 45px head and a black 1px top or bottom keyline: SEARCH (a SEARCH HERE field, SUGGESTIONS in blue caps, SUGGESTED PRODUCTS), FILTER & SORTING (radio rows with 10px dots, the black SHOW N ITEMS apply bar), and the WOMAN mega-menu (a 391 tall panel under the header, alternating 30px white/grey rows).",
    "Sign in": "The account gate: Sign in or register, the member-benefit list, the grey EMAIL field, the black CONTINUE bar and the bordered GOOGLE row, then a change-location line. The place name is painted out. Captured, never submitted.",
    "Footer": "The page foot: NEWSLETTER with its email field, contact methods (Live chat, Call, Email), four link columns in blue caps, two-letter social links (IG FB TW YT PT WB), the shipping-region selector and the cookie-settings link — all under a 1px hairline rule.",
    "Mobile (390 wide)": "The same storefront at 390: the header collapses to Menu, wordmark and bag; the Menu button opens a flat drawer of 45px rows (CONTACT US, HELP, CLIENT SERVICES, COMPANY, the social links) each separated by a 1px hairline drawn as a background gradient.",
}

PAGE_DESC = [
    ("home", "Home. The hero, gift-guide bars, campaign tiles and footer. Captured at rest, with the search panel open, and full-page.", "/sg/en/home"),
    ("woman", "WOMEN'S NEW ARRIVALS, the category page. Captured at rest, with the filter rail open, after LOAD MORE, and full-page.", "/sg/en/woman/new-arrivals/"),
    ("bags", "The BAGS category landing.", "/sg/en/bags/"),
    ("pdp", "A product page (Leather Funnel Neck Jacket). Captured at rest, with a size picked, and full-page.", "/sg/en/rw-wn-leat000073/A70237-ADM.html?g=woman"),
    ("about", "The About page.", "/sg/en/about/about.html"),
    ("faq", "The FAQ.", "/sg/en/help/faq.html"),
    ("contact", "Contact us.", "/sg/en/help/contact-us.html"),
    ("stores", "The store directory.", "/sg/en/stores/stores.html"),
    ("cart", "The shopping-bag route, which renders the bag drawer over the home page when empty.", "/sg/en/cart"),
    ("login", "The account sign-in gate.", "/sg/en/account"),
]
MOBILE_DESC = [
    ("mobile-home", "Home at 390, at rest, the Menu drawer open, and full-page.", "/sg/en/home"),
    ("mobile-woman", "The category page at 390.", "/sg/en/woman/new-arrivals/"),
    ("mobile-pdp", "The product page at 390.", "/sg/en/rw-wn-leat000073/A70237-ADM.html?g=woman"),
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

W("# Acne Studios components")
W()
W("The discovery list of every page and state captured, then one entry per component with crops of the real site, the shared values and the Gaps. Recaptured from acnestudios.com on 2026-11-21 at 1440x900 and 390x844, signed out. The control map is site-tree.md. Nothing was submitted. Contact lines in screenshots and crops are painted out.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the token in [tokens.json](tokens.json) whose value is the same, when there is one. Text is written family size/line-height weight, then its colour, for example `Helvetica Now Text 12/20 400, #000000`, and is read from the first text node inside the component.")
W("- The first state of each entry lists every value; later states list only what changed. A state identical to the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
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
    ("Search panel", "home", "the SEARCH header button", "[home-light-search](screenshots/home-light-search.png), [search-panel](#search-panel)"),
    ("Filter rail", "PLP", "the FILTER button", "[woman-light-filter](screenshots/woman-light-filter.png), [filter-rail](#filter-rail)"),
    ("After LOAD MORE", "PLP", "the LOAD MORE button", "[woman-light-load-more](screenshots/woman-light-load-more.png)"),
    ("Size picked", "PDP", "a size cell's own toggle (a local pick; nothing added)", "[pdp-light-size-picked](screenshots/pdp-light-size-picked.png), [size-cell-selected](#size-cell-selected)"),
    ("WOMAN mega-menu", "home", "the WOMAN nav item", "[menu-panel](#menu-panel)"),
    ("Mobile Menu drawer", "home at 390", "the Menu button", "[mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-drawer](#m-menu-drawer)"),
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
    else:
        hovers["no change on the element"] += 1


def top(ctr, n):
    return ", ".join(f"{k} ({v})" for k, v in ctr.most_common(n))


W(f"**Radius.** {top(radii, 5) if radii else 'none — every corner on the site is 0px'}. The single curve is the filter rail's 10px radio dot (`border-radius:100%` on a `::before`).")
W()
W(f"**Hover.** Acne hovers with colour, never fills or shadows: {top(hovers, 8)}. Black fills (LOAD MORE, CONTINUE, SHOW N ITEMS) flip to Acne blue; blue fills (ADD TO BAG) deepen to {colour('rgb(5, 21, 116)')}; blue links deepen the same way; black labels (nav, FILTER, Menu) grey to {colour('rgb(107, 107, 107)', role='text')}.")
W()
W(f"**Focus.** Of {focus_n} elements given a real keyboard focus: {top(focus, 6)}. The ring Acne does draw is a 1px solid keyline 3px inside the control — white on the black/blue buttons, deep blue on the white wishlist button, black on the size cells. Text links show no ring.")
W()
W(f"**Motion.** {top(trans, 6) if trans else 'Instant: every measured control reports transition-duration 0s — hover, focus and pressed changes have no easing'}. The only transitions the stylesheet carries are the drawers' 150ms padding-bottom safe-area slide, the accordions' 200ms max-height reveal and a 500ms fade on campaign layers, none on the controls themselves.")
W()
W("**Layout.** The header is a 60px rail (45px at 390); every page is a 1440-wide fluid grid of 4-px-base cells (`as-cell`). Primary buttons and the email fields share one 60px height; the small search field, menu links, suggestions and gift-guide bars are 30px rows; size cells are 77 x 45; every right-side drawer is 360 wide with a 45px head. Hairline 1px rules in #f2f2f2 (or black on drawers and the mega-menu's top edge) separate everything — several are painted as 1px background gradients rather than borders.")
W()
W("**Accent.** Acne blue (#0018a8) is the only accent: every text link, the ADD TO BAG fill, the wishlist border, the picked size cell's border and fill, the geo selector, and the hover step of every black button. Its deeper step #051574 is hover-only. Everything else is black, white or one of four warm greys.")
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
W("- The Fit Predictor button (`fit-predictor`) never rendered in headless Chromium — the Fits.me widget did not mount on this product and geo, so it is recorded as an honest miss rather than measured on the wrong element. The PDP still shows its line (\"Item runs True to size\") in screenshots.")
W("- States that submit were never pressed: ADD TO BAG, WISHLIST, CONTINUE, GOOGLE, SHOW N ITEMS, the newsletter sign-up. Their hover, focus and pressed styles were measured through CDP-forced pseudo-classes and keyboard focus, not real clicks.")
W("- The bag drawer, checkout, account area, store stock check, size-guide drawer and search results were not captured: each either needs a cart item, an account, a purchase or a submitted form — all out of bounds. The cart route renders the home page when the bag is empty, which is what its screenshot shows.")
W("- The OneTrust consent banner never mounted (its SDK was network-blocked), so the banner's own styling is unmeasured — only its selectors are known. The geo/region prompt and the gift-guide overlay bars were handled the same way when they appeared.")
W("- The Fit Predictor, live chat and OneTrust widgets are third-party mounts; their internals are outside this package's palette either way. The few custom properties the site declares (`--safe-area-inset-bottom`, Tailwind framework internals, the Adyen checkout block) are in [raw/css-vars.json](raw/css-vars.json), not tokenised.")
W("- Hover/focus on the 390 capture was not meaningful (a phone has neither); mobile entries cover layout and the drawer only. The PDP's colour variants beyond 'Dark brown' and other products' PDPs were not visited — the capture follows one product.")
W()

open("components.md", "w").write("\n".join(L) + "\n")
print(f"components.md: {len(C)} components, {n_states} states, {n_crops} crops, {len(L)} lines")
