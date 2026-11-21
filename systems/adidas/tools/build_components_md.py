#!/usr/bin/env python3
"""Build components.md for the adidas design reference.

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
    "bg": ["action.", "background.", "color.white", "color.offWhite", "color.greyLight", "text.", "border."],
    "border": ["border.", "color.grey", "color.black", "text.", "background."],
    "text": ["text.", "action.", "color.black", "color.greyDark", "color.grey", "border."],
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
    return {"微软雅黑": "Microsoft YaHei", "AdihausDIN-Woff": "AdihausDIN"}.get(first, first)


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


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "backdrop", "outline", "text", "transition", "transform", "opacity", "icon", "placeholder", "child paint"]


def paint_delta(a, b):
    """Describe how the painted child layers differ between two states.

    props() only reads the component root's computed style, so a hover that
    repaints a child (the product card's border going #eceff1 to black) would
    otherwise read 'same'. Layers are aligned by node name; only fields that
    changed are reported.
    """
    if not a or not b:
        return ""
    fields = ("border", "bg", "shadow", "outline", "bgImage")
    out = []
    bmap = {p["node"]: p for p in b}
    seen = set()
    for pa in a:
        pb = bmap.get(pa["node"])
        if not pb:
            continue
        seen.add(pa["node"])
        for f in fields:
            va, vb = pa.get(f), pb.get(f)
            if va != vb:
                name = "background" if f == "bg" else ("image" if f == "bgImage" else f)
                out.append(f"{pa['node']}: {name} {colour(va or 'none', tokens=False)} → {colour(vb or 'none', tokens=False)}")
    added = [p["node"] for p in b if p["node"] not in seen and p["node"] not in {x["node"] for x in a}]
    out += [f"{n} appears" for n in added[:3]]
    return "; ".join(out)


def state_rows(c):
    """The first state lists every value; later rows list only what changed."""
    rows = []
    states = [s for s, v in c["states"].items() if "style" in v]
    if not states:
        return rows
    base = props(c["states"][states[0]])
    base_paint = c["states"][states[0]].get("paint")
    rows.append((states[0], base))
    same = []
    for st in states[1:]:
        v = c["states"][st]
        p = props(v)
        diff = {k: p[k] for k in ORDER if k in p and p.get(k) != base.get(k)}
        for k in ORDER:
            if k in base and k not in p:
                diff[k] = "none"
        delta = paint_delta(base_paint, v.get("paint"))
        if delta:
            diff["child paint"] = delta
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
    "Shell and navigation": "The 124px two-strip header every page shares: a 40px black utility strip (在线客服 online service, 请登录 sign in), then an 84px nav bar — the adidas mark, the category nav (男装, 男鞋, 女装…), search, help, account, bag — over a #eceff1 hairline, plus the off-white campaign tag strip.",
    "Home": "The home canvas: the 540px full-bleed campaign band (.feed-com-carousel) under the header — photography, a banner headline and a lib-button 立即选购 CTA — then product rows and the footer.",
    "Catalogue page (PLP)": "A catalogue page (/plp/sp_run_app_male): grey filter/sort labels, then the product grid — a bordered photo tile, bold 13/18 name and ¥ price per card.",
    "Product page (PDP)": "A product page (/pdp?articleId=JP1477): a two-column canvas — gallery left, purchase column right — adineuePRO title and ¥ price, the white disabled add-to-cart bar, size cells and accordion rows.",
    "Footer": "The page foot (360px): bold 15/20 column titles (帮助中心…) over 11/16 link columns and the service line.",
    "Mobile (390 wide)": "The same storefront at 390: the top bar collapses to a search-field pill — no nav row and no burger menu.",
}

PAGE_DESC = [
    ("home", "Home. The campaign band, tag strip, product rows and footer. Captured at rest, search open, and full-page.", "/"),
    ("plp", "A catalogue page (跑步 running, men's). Captured at rest, filter open, and full-page.", "/plp/sp_run_app_male"),
    ("pdp", "A product page (articleId JP1477 — pinned so the screenshots and the measurements describe the same product). Captured at rest and full-page.", "/pdp?articleId=JP1477"),
    ("cart", "The empty bag.", "/cart"),
    ("sitemap", "The public site map: the catalog tree as a page.", "/siteMap"),
    ("campaign", "A campaign listing (one /splp tile from home).", "/splp?contentId=SPLP_NGuAJiSc"),
    ("clp", "A brand content page linked from the home brand tiles.", "/clp?contentId=904"),
    ("privacy", "The published privacy statement. The registered-address span is painted out.", "/my-account/privacy-statement"),
]
MOBILE_DESC = [
    ("mobile-home", "Home at 390, at rest, search open, and full-page. No burger is mounted.", "/"),
    ("mobile-plp", "The catalogue page at 390.", "/plp/sp_run_app_male"),
    ("mobile-pdp", "The product page at 390.", "/pdp?articleId=JP1477"),
    ("mobile-cart", "The empty bag at 390.", "/cart"),
    ("mobile-category", "The category tab: the catalog tree, already open.", "/category"),
    ("mobile-account", "The account tab. Login wall. The register control was not clicked.", "/my-account"),
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

W("# adidas components")
W()
W(f"The discovery list of every page and state captured, then one entry per component with crops of the real site, the shared values and the Gaps. Captured from adidas.com.cn on {J['_meta'].get('read', '2026-11-10')} — the China flagship storefront (prices in CNY ¥) — as static pages rendered at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the live DOM. Nothing was submitted, bought or signed into; the only presses were local UI toggles (the Search disclosure, the nav flyout, the filter rail). No consent SDK mounts on these routes.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the token in [tokens.json](tokens.json) whose value is the same, when there is one. Text is written family size/line-height weight, then its colour, for example `AdihausDIN 15/20 700, #000000`, and is read from the first text node inside the component.")
W("- The first state of each entry lists every value; later states list only what changed. A state identical to the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do; a state that only repaints a child layer is listed as \"child paint\".")
W(f"- Crops are images of the component in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png`. Desktop viewport shots are 1440 x 900. Phone viewport shots are 390 x 844 at 2x (780 x 1688). `-full` shots tile the inner scroll shell, so they are taller than the viewport. Only light exists. The storefront has no dark theme. Which control opens which page is in [site-tree.md](site-tree.md).")
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
    ("Search disclosure", "home", "the search pill", "[home-light-search](screenshots/home-light-search.png), [mobile-home-light-search](screenshots/mobile-home-light-search.png)"),
    ("Filter rail", "PLP", "the filter/sort control", "[plp-light-filter](screenshots/plp-light-filter.png), [filter-row](#filter-row)"),
    ("Login drawer", "home", "请登录 and the profile icon. Branch stopped. Not screenshotted.", "not captured: login wall"),
    ("Catalog mega-menu", "home", "a category label. Parent stayed hidden in this headless session.", "[sitemap](screenshots/sitemap-light-default.png) and [mobile category](screenshots/mobile-category-light-default.png) show the same links"),
    ("Staff password dialog", "every desktop load", "mounted with no close control. Not clicked. Hidden before shots.", "not captured: password change"),
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
            oc = st["outlineColor"]
            transparent = bool(re.fullmatch(r"rgba\(\d+, \d+, \d+, 0\)", oc or ""))
            if st["outlineStyle"] != "none" and float(st["outlineWidth"].replace("px", "")) > 0 and not transparent:
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
    elif a.get("paint") != b.get("paint"):
        hovers["a child layer repaints (the entry's child paint row has the detail)"] += 1
    else:
        hovers["no change on the element"] += 1


def top(ctr, n):
    return ", ".join(f"{k} ({v})" for k, v in ctr.most_common(n))


W(f"**Radius.** {top(radii, 5) if radii else 'none — every corner measured on the storefront is 0px'} — buttons, fields, tiles, drawers and cells are all square.")
W()
W(f"**Hover.** {top(hovers, 8)}. The one measured hover effect is painted by a child: the product card's border steps from #eceff1 to black while its fill stays grey. Buttons and links show no hover change on the element itself.")
W()
W(f"**Focus.** Of {focus_n} elements given a real keyboard focus: {top(focus, 6)}. The only ring measured is the browser's own (footer-link takes Chromium's 1px auto #005fcc outline); buttons and nav items paint no focus style at all, and several controls (div nav items, the promo tag) are not keyboard-focusable — {focus['focus could not be driven']} focus attempts could not land.")
W()
W(f"**Motion.** {top(trans, 6) if trans else 'Instant: every measured control reports transition-duration 0s — hover, focus and pressed changes have no easing'}. The header bar itself carries `all 0.3s ease-in`; the readable stylesheets' declared transitions are listed in [raw/measurements.md](raw/measurements.md).")
W()
W("**Layout.** The header is a 124px rail (a 40px black utility strip over an 84px nav bar); the campaign band under it runs 540px tall at 1440. Buttons share one 48px height with 16px side padding; the PLP grid runs 338.5px product cards at 454.5px tall; the PDP purchase column is ~400px; the footer is a 360px block. Edges, where they exist, are 1px hairlines in #eceff1, #c8cbcc or black.")
W()
W("**Accent.** None — the storefront is strict monochrome: black text and keylines on white, grey steps (#9a9b9b muted, #c8cbcc disabled/hairline, #eceff1 and #f9f9f9 surfaces). No accent colour was measured on the public surface.")
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
W("- States that submit were never pressed: 加入购物袋 (add to cart) and the checkout controls. Hover, focus and pressed styles come from CDP-forced pseudo-classes and keyboard focus, not real clicks.")
W("- The captured PDP showed add-to-cart in its disabled state (white fill, #c8cbcc text and border); an in-stock enabled bar was not measured.")
W("- The nav flyout did not open on hover in headless (some items open on click); the search disclosure is in the screenshots, its panel is not measured.")
W("- `plp-title`, `product-card-price`, `size-cell`, `accordion` and `m-burger` are recorded misses — the selectors found nothing, so nothing is reported; `size-cell`/`accordion` may not exist on this PDP variant, and no burger menu mounts at 390 (the top bar is the search pill).")
W("- Pages are fixed-height app shells with inner scroll containers, so the `-full` screenshots capture the viewport-height shell, not a tall page — a boundary of the front end, not a truncation.")
W("- The global adidas.com storefront is Akamai-blocked from the capture environment (every regional domain answers HTTP 403), so this package covers adidas.com.cn, a related but different zh-CN front end.")
W("- Hover/focus on the 390 capture is not meaningful (a phone has neither); the mobile entries cover layout.")
W()

open("components.md", "w").write("\n".join(L) + "\n")
print(f"components.md: {len(C)} components, {n_states} states, {n_crops} crops, {len(L)} lines")
