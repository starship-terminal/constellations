#!/usr/bin/env python3
"""Build components.md for the 1Password design reference.

Reads raw/components-computed.json (every component and state, measured), tokens.json,
screenshots/ and icons/INDEX.tsv, and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the palette token whose
value matches, the font family is named once per value, and a state row shows only what differs
from the first state. Adapted from the public-route builder.

Deterministic: re-running it on the same inputs reproduces components.md byte for byte.
Run from anywhere: python3 tools/build_components_md.py
"""
import json, os, re
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

PAGE_NAME = {"home": "home", "collection": "collection", "product": "product", "search": "search", "account": "account"}

GROUP_INTRO = {
    "Shell and navigation": "The chrome on every public page: the tan announcement strip, then the white `header-navigation` bar (wordmark, nav-group flyout buttons, Pricing link, Talk to sales, the blue Get started free pill), and the dark footer.",
    "Home": "The marketing home page: the navy gradient hero with the 88px display headline and the product collage below, plus section bands down the page.",
    "Pricing": "The pricing page: the `segment-selector` plan pill (Enterprise/Business/Individual) beside the title, the five-column platform/product grid with Request a quote pills, and the FAQ accordions.",
    "Product page": "The enterprise-password-manager marketing page: title, CTAs, feature cards and the Marketplace link.",
    "Downloads": "The per-platform download page: title, the macOS platform pill and the download button. Clicking it starts a download, which was never done.",
    "Developer": "The developer-security page: title, feature/link cards and docs CTAs.",
    "Dialogs and overlays": "Overlays the public site raises: the nav flyout on click, the mobile drawer, and the OneTrust consent card (dismissed, see Gaps).",
    "Forms": "Fields reachable signed out: the contact-sales page's embedded Marketo form (cross-origin, measured as a frame only).",
    "Mobile (390 wide)": "The same chrome as a phone draws it, at 390 x 844 with an iPhone user agent.",
    "Sign-in boundary": "start.1password.com under a headless browser: it redirects to /unsupported, captured as the honest edge of the public surface. The vault needs an account, a secret key and a master password.",
}

SHOTS = [
    ("home", "Home. Tan announcement strip, white nav bar, the navy gradient hero and product collage. Nav flyout and full page captured.", "/"),
    ("pricing", "Pricing. Plan-selector pill, the platform/product column grid, a FAQ row open; full page.", "/pricing"),
    ("product", "Enterprise Password Manager product page.", "/product/enterprise-password-manager"),
    ("download", "Download 1Password for macOS: platform pill and download button.", "/downloads/mac"),
    ("developer", "Developer Security page.", "/developer-security"),
    ("contact", "Contact sales: the embedded Marketo form (cross-origin).", "/contact-sales"),
    ("account", "start.1password.com under a headless browser redirects to its unsupported-browser page.", "https://start.1password.com/unsupported?l=en"),
]
MOBILE = [
    ("mobile-home", "Home at 390: header, hamburger, hero, full page.", "/"),
    ("mobile-pricing", "Pricing at 390; full page.", "/pricing"),
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
icons_idx = Path("icons/INDEX.tsv")
icons = [r.split("\t") for r in icons_idx.read_text().strip().split("\n")[1:]] if icons_idx.exists() else []

read_on = (J["_meta"].get("run") or "")[:10]
W("# 1Password components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from 1password.com on {read_on}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was bought, downloaded, signed into, sent or submitted.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `agileSans 16/24 350, #303136`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (1password.com serves one light theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).")
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
    ("Nav flyout", "desktop nav", "click on the Business group button", "[menu](screenshots/home-light-menu.png), [nav-flyout](#nav-flyout)"),
    ("FAQ accordion", "pricing", "the first collapsed row toggled open", "[faq](screenshots/pricing-light-faq.png), [faq-answer](#faq-answer)"),
    ("Mobile menu drawer", "mobile home", "the hamburger button", "[m-nav-drawer](#mobile-nav-drawer)"),
    ("OneTrust consent card", "first visit, any page", "an OptanonAlertBoxClosed cookie is pre-seeded so it never mounts; a closed-shadow sweep hides it if it still appears", "dismissed before every capture"),
    ("Vimeo embed", "home hero", "a cross-origin player.vimeo.com iframe", "measured as an element box only; contents unreachable"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement files.")
W()
def _alpha(c):
    m = re.search(r"rgba?\([^)]*?,\s*([\d.]+)\s*\)$", c or "")
    return float(m.group(1)) if m else 1.0


foc = []
focus_failed = []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st or "style" not in st:
        continue
    if "failed" in str(st.get("via", "")):
        focus_failed.append(k)
        continue
    s = st["style"]
    base = (c["states"].get("default") or {}).get("style") or {}
    ring = (s["outlineStyle"] != "none"
            and float(s["outlineWidth"].replace("px", "")) > 0
            and _alpha(s["outlineColor"]) > 0)
    if ring:
        foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}"))
    elif base and any(s.get(f) != base.get(f) for f in ("borderTopColor", "borderTopWidth", "borderBottomColor", "borderBottomWidth", "boxShadow", "backgroundColor")):
        foc.append((k, "border/fill change, no visible outline"))
    else:
        foc.append((k, None))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} show a visible change (outline, or a border/fill change where the outline stays transparent): {', '.join(with_ring) or 'none'}. The other {len(without)} draw none, so a keyboard user sees no change: {', '.join(without)}." + (f" Focus could not be driven on: {', '.join(f'`{k}`' for k in focus_failed)}." if focus_failed else ""))
W()
W("**Pressed.** 1Password's CTAs darken a step (secure-blue to its pressed navy) or hold flat; the segment-selector pills take a filled state — see the per-component state rows.")
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
# The card-like and chrome surfaces, compared in one table.
for k in ["header", "promo-bar", "mega-menu", "cart-drawer", "filter-sheet", "m-header", "m-menu-drawer", "product-card", "cart-upsell-card", "tooltip-pill", "m-ai-chip", "size-button", "swatch"]:
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
if icons:
    W()
    W("## Icons")
    W()
    W(f"{len(icons)} SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. The SVGs are 1Password's property, kept for reference only.")
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
W("- **The vault and everything behind sign-in.** The product itself is credential-gated (account + secret key + master password, not OAuth): app views, the admin console, settings and billing were never reached. start.1password.com gates headless browsers to /unsupported, which was captured instead.")
W("- **Anything that sends.** No form was submitted, nothing bought, nothing downloaded; the contact form's fields live inside a cross-origin Marketo iframe and were neither introspected nor submitted.")
W("- **The OneTrust consent card** mounts on first visits only (it renders in a closed shadow root, invisible to DOM queries). An OptanonAlertBoxClosed cookie is seeded before navigation and a geometric sweep hides any residual overlay, so it has no component entry.")
W("- **The nav flyout's other tabs** (Personal, Developers, Partners, Resources) were not opened; only the Business panel was measured.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover), so a state a script adds on mousedown (if any) is missing.")
W("- **The Vimeo player and Marketo form** are cross-origin iframes: their element boxes are measured (video-embed, form-embed) but their contents are unreachable, so nothing inside them is claimed.")
W("- **The sign-in card itself** never renders headlessly (start.1password.com redirects to /unsupported), so only the unsupported page carries measurements.")
W()
W("### Themes")
W()
W("1password.com serves one light theme: no dark attribute is set anywhere, the Tailwind build declares no dark variant, and nothing in the capture hints at a toggle. The token file therefore ships no dark set.")
W()
W("### Fonts")
W()
W("- **Agile Sans Variable** and **Agile Mono Variable** are 1Password's own faces, served as woff/woff2 from `/_next/static/media/` (`fonts` in [raw/css-vars.json](raw/css-vars.json)). The style guide falls back to the system sans/mono for them.")
W("- The **Marketo iframe** and **start.1password.com** use their own faces, which are not part of this token set.")
W()
W("### Screenshots")
W()
W("- Screens and product imagery are 1Password's content and appears only inside screenshots and crops.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- No personal data was captured: every page was read signed out with an empty session, and the only fields touched were the consent sweep and UI toggles; no text was ever typed into a form.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops,", len(icons), "icons")
