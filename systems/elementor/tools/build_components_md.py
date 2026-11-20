#!/usr/bin/env python3
"""Build components.md for the Elementor design reference.

Reads raw/components-computed.json (every component and state, measured), tokens.json
and screenshots/, and writes components.md next to them. Every value is a cell of the
measurement file, condensed: colours are hex followed by the palette token whose
value matches, the font family is named once per value, and a state row shows only
what differs from the first state. Adapted from the kit's builder, which read
markdown; this one reads the JSON directly.

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


def zero_size(p):
    """A painted-layer entry that is not on screen (display contents / a
    hidden node): it cannot supply the surface a reader sees."""
    sz = str(p.get("size", ""))
    return sz.startswith("0.0x0.0") or sz in ("0x0", "0pxx0px")


def focus_not_captured(v):
    """A state whose reading is not what its name says: a skipped one, or a focus-visible reading
    taken where keyboard focus never landed (kbFocus returned "focus failed") or where the element
    took focus but did not match :focus-visible. Its style is the element at rest, so it is left out
    of every table and tally and listed as "focus could not be captured" (the kit's rule)."""
    return bool(v.get("skipped")) or v.get("via") == "focus failed" or (v.get("focus") or {}).get("matches") is False


def measured(v):
    return "style" in v and not focus_not_captured(v)


def child_ring(v):
    """A focus ring painted by a visible descendant — keyboard focus can land
    on a child (the mobile item's dropdown button) instead of the wrapper."""
    ring = next((p for p in (v.get("paint") or []) if p.get("outline") and not zero_size(p)), None)
    return f"{colour(ring['outline'])} (on {ring['node']})" if ring else None


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
    else:
        ring = child_ring(v)
        if ring:
            o["outline"] = ring
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
    # A control's visible box can live on a sibling/pseudo element while the
    # measured node stays invisible (the acceptance checkbox's input paints at
    # opacity 0; the label's ::before is the box a user sees).
    ex = v.get("extra") or {}
    bx = ex.get("box")
    if bx:
        parts = [bx["size"]]
        if bx.get("backgroundColor") and bx["backgroundColor"] != "rgba(0, 0, 0, 0)":
            parts.append("background " + colour(bx["backgroundColor"]))
        if bx.get("backgroundImage") and bx["backgroundImage"] != "none":
            parts.append("image " + bx["backgroundImage"])
        if bx.get("border") and bx["border"] != "none":
            parts.append("border " + colour(bx["border"].split(" | ")[0]))
        if bx.get("radius") and bx["radius"] != "0px":
            parts.append("radius " + bx["radius"])
        o["visible box"] = "; ".join(parts)
    if ex.get("checked") is True:
        o["checked"] = "true on the input"
    return o


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "outline", "visible box", "checked", "text", "transition", "transform", "opacity", "icon", "placeholder"]


def state_rows(c):
    states = [s for s in c["states"] if measured(c["states"][s])]
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
    st = next((s for s in c["states"].values() if measured(s)), None)
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

PAGE_NAME = {"home": "Home", "pricing": "Pricing", "contact": "Contact", "faq": "FAQ", "mobile": "Home"}

GROUP_INTRO = {
    "Shell and navigation": "The floating pill header shared by every page: the Elementor wordmark, the Products mega-menu trigger, plain links, the En language selector, Log in and the black Get-started pill. The header is an Elementor `header` location template (`data-elementor-type=\"header\"`) over an `e-n-menu` widget; the dropdown is the mega-menu content panel.",
    "Home hero": "The full-viewport photo hero: a `.dark-mode` island that re-binds the same named vars (`--Blank-Canvas-White` -> black, `--Kernel-Black` -> white), so the headline and the white Get-started pill read inverted against the dark media.",
    "Home": "Body sections of the home page: section headings in Roobert, white `dsm-card` tiles and icon-list rows on the light ground.",
    "Pricing": "The pricing page: plan cards (`e-loop-item` in a carousel), the billing-period toggles, Buy-now actions and feature rows. Nothing was bought; the toggles were measured as controls, not switched into checkout.",
    "Contact form": "The Elementor form widget on /contact: text inputs, textarea, select, the acceptance checkbox and the submit. Fields were focused and filled with sample text only; nothing was sent.",
    "FAQ": "The FAQ accordion on /faq: `dsm-faq--title` question rows (aria-expanded triggers) and their `dsm-faq--faq-content` answer panels.",
    "Footer": "The `dsm-footer`, another `.dark-mode` island: link columns, social icons and legal on black.",
    "Mobile (390 wide)": "A few components as a phone draws them, at 390 x 844 with a mobile user agent, including the `e-n-menu-toggle` hamburger and the opened header menu.",
}

SHOTS = [
    ("home", "Home. Photo hero with the white headline and Get-started pill, marketing sections, footer.", "/"),
    ("builder", "Website builder. The marketing page for the editor itself.", "/products/website-builder/"),
    ("pricing", "Pricing. Plan cards, billing toggles, feature rows.", "/pricing/"),
    ("enterprise", "Enterprise. The solutions pitch for large organisations.", "/solutions/enterprise/"),
    ("about", "About. The company page.", "/about/"),
    ("contact", "Contact. The Elementor form (name, email, message, acceptance, submit); nothing filled or sent.", "/contact/"),
    ("faq", "FAQ. The accordion of questions.", "/faq/"),
]
MOBILE = [
    ("mobile-home", "Home at 390, and the header menu opened by its own toggle.", "/"),
    ("mobile-pricing", "Pricing at 390.", "/pricing/"),
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


n_crops = len(list(Path("components/crops").glob("*.png"))) if Path("components/crops").exists() else 0
n_states = sum(len(c["states"]) for c in C.values())

W("# Elementor components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from elementor.com on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, bought or sent.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Roobert 88/96.8 700, #ffffff`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`). Crop scale: the capture context runs at a device scale of 2, and a crop larger than ~1.2 megapixels is saved halved (effectively 1x) to keep the folder small — the wide panels (`nav-dropdown`, `footer`, `form-popup`, `plan-card`, `m-menu-open`) are the 1x ones. Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (the site paints light with `.dark-mode` islands on the same vars). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at the context's device scale — 1x on desktop, 2x on mobile — capped at eight chunks of 14000 device px each; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).")
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
    ("Products mega-menu", "every page, header", "the Products trigger opened (hover + click); closed with Escape", "[home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#nav-dropdown)"),
    ("Mobile menu", "Home at 390", "the `e-n-menu-toggle` hamburger; closed with Escape", "[mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open)"),
    ("FAQ item, open", "FAQ", "the question row's own toggle (aria-expanded)", "[faq-light-open](screenshots/faq-light-open.png), [faq-item-open](#faq-item-open)"),
    ("Form field, filled", "Contact", "sample text typed into the name field and deleted; nothing sent", "[field-name](#name-field)"),
    ("Cookiebot consent dialog", "every page, on load", "hidden with CSS; the consent buttons were never pressed (a press POSTs)", "[home-light-default](screenshots/home-light-default.png)"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement files.")
W()
foc, failed_focus = [], []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st:
        continue
    if focus_not_captured(st) or "style" not in st:
        # A failed focus attempt is its own record — never a no-ring reading.
        failed_focus.append(k)
        continue
    s = st["style"]
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0
    if ring:
        foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}"))
    else:
        # The ring may be painted by the focused child, not the wrapper.
        foc.append((k, child_ring(st)))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
line = f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} draw a ring: {', '.join(with_ring) or 'none'}. The other {len(without)} draw none, so a keyboard user sees no change: {', '.join(without) or 'none'}."
if failed_focus:
    line += f" On {len(failed_focus)} more, keyboard focus could not be landed at all ({', '.join('`' + k + '`' for k in failed_focus)}) — recorded as a failed state, not as a no-ring reading."
W(line)
W()
W("**Pressed.** Read with DevTools `forcePseudoState` (`:active` + `:hover`), so no control was really pressed; a state a script adds on mousedown (if any) is missing.")
W()
W("**Motion.** Transitions measured on the components, by duration.")
W()
W("| Duration | Easing | Property | Where |")
W("|---|---|---|---|")
mot = {}
for k, c in C.items():
    for st in c["states"].values():
        if not measured(st):
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
for k in ["nav-dropdown", "card", "plan-card", "faq-item", "faq-answer", "field-name", "field-message", "menu-open", "m-menu-open"]:
    c = C.get(k)
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if measured(s)), None)
    if st is None:
        continue
    p = props(st)
    if ("radius" not in p or p["background"] == "transparent") and st.get("paint"):
        # Borrow only values the root lacks, and only from a descendant that is
        # on screen: a hidden (0x0) layer's colours are not the surface a
        # reader sees (the mobile menu's hidden button must not recolour it).
        vis = [x for x in st["paint"] if not zero_size(x)]
        p0 = next((x for x in vis if x.get("bg") and x.get("radius")), next((x for x in vis if x.get("bg") or x.get("bgImage")), None))
        if p0:
            if "border" not in p and p0.get("border"):
                p["border"] = colour(p0["border"].split(" | ")[0][2:])
            if "radius" not in p and p0.get("radius"):
                p["radius"] = p0["radius"]
            if p["background"] == "transparent" and p0.get("bg"):
                p["background"] = colour(p0["bg"])
            if "shadow" not in p and p0.get("shadow"):
                p["shadow"] = colour(p0["shadow"], tokens=False)
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

# ------------------------------------------------ gaps
W()
W("## Gaps")
W()
W("### Pages")
W()
W("- **Signed-in pages.** Nothing behind sign-in was captured: the Elementor editor, the my.elementor.com dashboard, hosting/site management, and the account flows the header's Log-in and Get-started actions point at. The kit never signs in.")
W("- **Anything that sends, buys or creates.** No contact form was submitted, no plan was bought (Buy now was measured, never pressed — it would open checkout), no account was created, no OAuth was completed, and the Cookiebot consent buttons were never pressed (the dialog was hidden with CSS instead).")
W("- **Editor and product surfaces.** The Elementor editor, the Angi/AI copilot chat (`#elementor-angie-root` was hidden), the site-builder canvas and the hosting admin are product surfaces behind auth — documented as boundaries, not attempted.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control except toggles, so a state a script adds on mousedown (if any) is missing.")
W("- **Billing toggles** on Pricing were measured as controls; switching them re-renders prices client-side and was not exercised into checkout.")
W("- **Disabled states** were not seen on any public control.")
W()
W("### Themes")
W()
W("Elementor paints one light page with `.dark-mode` islands: the photo hero, dark sections and the footer carry `class=\"dark-mode\"`, under which `.dark-mode *` re-binds `--Kernel-Black` to `#fff`, `--Blank-Canvas-White` to `#000` and `--Grey-800` to `--Grey-200`. There is no theme switch; the re-binding is scoped to those islands, so the same named vars produce the light and dark readings the token file ships (`darkscope` rules and the `dark` pass in [raw/css-vars.json](raw/css-vars.json)).")
W()
W("### Fonts")
W()
W("- **Roobert** (`--Roobert: 'Roobert'`) is the site face, self-hosted under wp-content/fonts; it renders in captures because the page loads it.")
W("- **Roboto** is pulled from Google Fonts (`fonts.googleapis.com/css2?family=Roboto`) for the editor-side/chrome text.")
W()
W("### Screenshots")
W()
W("- Photography, product renders and brand art are Elementor's content and appear only inside screenshots and crops. The hero media and carousels keep moving, so two captures of the same view can differ.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Page prose was not transcribed; only the frames, controls and states around it were measured.")
W("- No personal data was captured: the pages were read signed out, and no form was submitted.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops")
