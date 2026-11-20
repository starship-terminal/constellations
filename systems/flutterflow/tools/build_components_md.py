#!/usr/bin/env python3
"""Build components.md for the FlutterFlow design reference.

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
LAYOUT = json.load(open("raw/layout.json"))
T = json.load(open("tokens.json"))

# --------------------------------------------------------------------------- colours and tokens



def focus_not_captured(v):
    """A state whose reading is not what its name says (decision D4, ported
    from the kit's builder): a skipped one, or a focus-visible reading taken
    where keyboard focus never landed (via "focus failed") or where the
    element took focus but did not match :focus-visible. Its style is the
    element at rest, so it is left out of every table and tally and listed as
    "focus could not be captured"."""
    return bool(v.get("skipped")) or v.get("via") == "focus failed" or (v.get("focus") or {}).get("matches") is False

def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


BY_COLOR = {}
for grp in ("color", "legacy", "drip"):
    for n, t in flat(T["light"].get(grp, {})):
        if t["$type"] == "color":
            BY_COLOR.setdefault(t["$value"], f"{grp}.{n}")


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def unlab(c):
    """CSS lab() (D50, Bradford-adapted) and oklab()/oklch() -> 'rgb(r, g, b)' or
    'rgba(r, g, b, a)', so colour() can label it like any other reading. The
    base kit has this; it was lost in this fork (2026-11 audit, finding 18-16)."""
    import math
    gam = lambda v: 12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055
    alpha = lambda a: 1.0 if a is None else (float(a[:-1]) / 100 if a.endswith("%") else float(a))

    def out(lin, a):
        r, g, b = (max(0, min(255, round(gam(max(0.0, v)) * 255))) for v in lin)
        al = alpha(a)
        return f"rgb({r}, {g}, {b})" if al == 1 else f"rgba({r}, {g}, {b}, {al:g})"

    m = re.fullmatch(r"lab\(\s*([\d.]+)%?\s+(-?[\d.]+)\s+(-?[\d.]+)\s*(?:/\s*([\d.]+%?))?\s*\)", c.strip())
    if m:
        L, A, B, a = m.groups()
        fy = (float(L) + 16) / 116
        fx, fz = fy + float(A) / 500, fy - float(B) / 200
        d = 6 / 29
        f = lambda t: t ** 3 if t > d else 3 * d ** 2 * (t - 4 / 29)
        x, y, z = f(fx) * 0.96422, f(fy) * 1.0, f(fz) * 0.82521
        return out((3.1338561 * x - 1.6168667 * y - 0.4906146 * z,
                    -0.9787684 * x + 1.9161415 * y + 0.0334540 * z,
                    0.0719453 * x - 0.2289914 * y + 1.4052427 * z), a)
    m = re.fullmatch(r"okl(ch|ab)\(\s*([\d.]+%?)\s+(none|-?[\d.]+%?)\s+(none|-?[\d.]+(?:deg)?)\s*(?:/\s*([\d.]+%?))?\s*\)", c.strip())
    if m:
        kind, L, x, y, a = m.groups()
        L = float(L[:-1]) / 100 if L.endswith("%") else float(L)
        num_ = lambda v, scale: 0.0 if v == "none" else (float(v[:-1]) / 100 * scale if v.endswith("%") else float(v.replace("deg", "")))
        if kind == "ch":
            C_, h = num_(x, 0.4), num_(y, 1)
            A, B = C_ * math.cos(math.radians(h)), C_ * math.sin(math.radians(h))
        else:
            A, B = num_(x, 0.4), num_(y, 0.4)
        l_ = (L + 0.3963377774 * A + 0.2158037573 * B) ** 3
        m_ = (L - 0.1055613458 * A - 0.0638541728 * B) ** 3
        s_ = (L - 0.0894841775 * A - 1.2914855480 * B) ** 3
        return out((4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
                    -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
                    -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_), a)
    return c


def colour(c, tokens=True):
    """rgb()/rgba()/color(srgb)/lab()/oklab()/oklch() -> '#hex `token`' or 'rgba(...)'."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        tok = BY_COLOR.get(v) if tokens else None
        return f"{v} `{tok}`" if tok else v

    c = re.sub(r"(?:oklab|oklch|lab)\([^)]*\)", lambda m: unlab(m.group(0)), c)
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
    states = [s for s in c["states"] if "style" in c["states"][s] and not focus_not_captured(c["states"][s])]
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

PAGE_NAME = {"home": "home", "pricing": "pricing", "enterprise": "enterprise", "product": "product",
             "studio": "studio", "showcase": "studio showcase"}

GROUP_INTRO = {
    "Shell and navigation": "The chrome every public page carries: the skip link, the 64px announcement + nav bar (56px at 390), the Product dropdown panel and its sign-in row. Sign in and Start building were read, never followed.",
    "Pricing": "The pricing page's plan grid, the Monthly/Yearly segmented control (Yearly selected through the site's own toggle), the plan CTAs and the FAQ accordion.",
    "Prompt composer": "FlutterFlow leads with an AI prompt field on the home hero and a slimmer variant on later pages: ghost idea text, idea arrows, a Tab hint chip and the round send button. Sample text was typed and deleted; the composer was never submitted.",
    "Enterprise contact form": "The Talk-to-sales form on /enterprise: labels, pill text fields, a tall textarea, radios, a custom select (opened, never submitted) and the declared-but-unpainted error slot.",
    "Tabs and disclosure": "The product page's feature tab list (a tab selected through its own control) and the accordions shared by pricing, product and the Studio FAQ.",
    "Content pages": "Headings, tag chips, link rows and cards from /studio, /studio/showcase and the feature cells on /enterprise.",
    "Home (earlier skin)": "The home page still ships the previous generation of the design (the `.composer`/`.pbtn`/`.pg-*` modules and the legacy `--accent`/`--ink` shorthand), measured alongside the ff-* layer the other pages carry.",
    "Footer": "The closing band and the real theme switch (the Light/Dark pick the dark set was captured through).",
    "Mobile (390 wide)": "A few components as a phone draws them, at 390 x 844 with a mobile user agent: the collapsed bar and the full-screen menu sheet.",
    "Dialogs and overlays": "Overlays and transient surfaces opened through the pages' own controls.",
}

SHOTS = [
    ("home", "Home. The AI prompt hero (the earlier skin), product demo modules, customer proof, the closing band and footer; the composer focused and the Product menu open.", "/"),
    ("product", "Product. Feature tabs (the Backend tab selected through its own control), editor walkthrough modules and an FAQ.", "/product"),
    ("pricing", "Pricing. The Monthly/Yearly segmented control (Yearly selected), plan cards and CTAs, the FAQ accordion (its first item ships open; the saved shot shows the list toggled shut).", "/pricing"),
    ("enterprise", "Enterprise. The Talk-to-sales contact form (a field focused; nothing sent) and the customer cells.", "/enterprise"),
    ("ai", "FlutterFlow AI. The AI product page.", "/ai"),
    ("studio", "FlutterFlow Studio. The agency arm's hero, tags and offering sections.", "/studio"),
    ("studio-showcase", "Studio showcase. The developer work gallery's cards.", "/studio/showcase"),
    ("studio-faq", "Studio FAQ. The accordion; its first item ships open, and the saved shot shows it toggled shut.", "/studio/faq"),
    ("studio-apply", "Apply to be a developer. The Studio application page (the form read, never submitted).", "/studio/apply-to-be-a-developer"),
    ("customer-stories", "Customer stories.", "/customer-stories"),
    ("blog", "Blog index.", "/blog"),
    ("changelog", "Changelog.", "/changelog"),
    ("about-us", "About us.", "/about-us"),
    ("contact-us", "Contact us.", "/contact-us"),
    ("vs-studio", "FlutterFlow vs. Studio comparison.", "/flutterflow-vs-studio"),
    ("dev-groups", "FlutterFlow developer groups.", "/flutterflow-developer-groups"),
    ("student-ambassadors", "Student ambassadors.", "/student-ambassadors"),
]
DARK = [
    ("home-dark", "Home in the dark theme (the footer switch's Dark pick): the nav menu open.", "/"),
    ("product-dark", "Product, dark.", "/product"),
    ("pricing-dark", "Pricing, dark.", "/pricing"),
    ("enterprise-dark", "Enterprise, dark.", "/enterprise"),
]
MOBILE = [
    ("mobile-home", "Home at 390: the collapsed bar and the full-screen menu sheet opened.", "/"),
    ("mobile-pricing", "Pricing at 390.", "/pricing"),
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
icons = [r.split("\t") for r in open("icons/INDEX.tsv").read().strip().split("\n")[1:]]

W("# FlutterFlow components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from flutterflow.io on {(J['_meta'].get('captured') or '')[:10]}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, submitted or sent — the composer's sample text was deleted and the send, sign-in and form submit controls were measured but never activated.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [raw/layout.json](raw/layout.json).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/24 510, #1a1a1a`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W("- The site ships two generations of its marketing skin: home's `.composer`/`.pbtn`/`.pg-*` modules and the `ff-*` layer every other page carries. The Home (earlier skin) group holds the first; the rest is ff-*.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{theme}-{state}.png`; the dark set is `{page}-dark-dark-{state}.png` (the page key carries `-dark`, the theme slot `dark`). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).")
W()
W("| Surface | URL | Screenshots |")
W("|---|---|---|")
for p, desc, url in SHOTS + DARK + MOBILE:
    W(f"| {desc} | `{url}` | {links(p)} |")
W()
W("### Overlays and transient states")
W()
W("| State | Where | How it was reached | Captured |")
W("|---|---|---|---|")
OVER = [
    ("Product dropdown", "the top nav, every page", "the nav's own Product button; closed with Escape", "[home-light-nav-product-open](screenshots/home-light-nav-product-open.png), [nav-panel](#nav-panel)"),
    ("Composer, focused", "home hero", "clicked into the field; sample text typed and deleted, nothing sent", "[home-light-composer-focused](screenshots/home-light-composer-focused.png)"),
    ("Billing: Yearly", "pricing", "the Monthly/Yearly segmented control's own Yearly option", "[pricing-light-billing-yearly](screenshots/pricing-light-billing-yearly.png)"),
    ("FAQ accordion, open and closed", "pricing and Studio FAQ", "the accordion's own summary; the first item ships open on both pages, so the saved shots show the same list toggled shut", "[pricing-light-faq-closed](screenshots/pricing-light-faq-closed.png), [studio-faq-light-faq-closed](screenshots/studio-faq-light-faq-closed.png), [accordion-item](#accordion-item)"),
    ("Contact form, field focused", "enterprise", "clicked into the first name field; nothing typed or sent", "[enterprise-light-form](screenshots/enterprise-light-form.png), [enterprise-light-field-focused](screenshots/enterprise-light-field-focused.png)"),
    ("Feature tab selected", "product", "the Backend tab's own control", "[product-light-tab-selected](screenshots/product-light-tab-selected.png)"),
    ("Mobile menu sheet", "home at 390", "the Open menu icon button; closed with its own Close menu button", "[mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu-dialog](#m-menu-dialog)"),
    ("Dark theme", "home, product, pricing, enterprise", "the footer theme switch set to Dark (data-theme=dark), restored to Light after", "[home-dark-dark-default](screenshots/home-dark-dark-default.png), [pricing-dark-dark-full](screenshots/pricing-dark-dark-full.png)"),
    ("Cookie consent banner", "every page, on load", "the privacy-choices dialog (a CookieScript embed) is closed by the kit's closePromo before each capture; it is a vendor widget, not part of the design layer", "(dismissed, not kept as a design surface)"),
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
no_focus = []  # focus-visible readings where focus never landed (D4)
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st or "style" not in st:
        continue
    if focus_not_captured(st):
        no_focus.append(k)
        continue
    s = st["style"]
    base = (c["states"].get("default") or {}).get("style") or {}
    if s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0:
        foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}"))
    elif s["boxShadow"] != base.get("boxShadow") or any(
            s[f"border{d}{p}"] != base.get(f"border{d}{p}")
            for d in ("Top", "Right", "Bottom", "Left") for p in ("Color", "Width")):
        # no outline, but the control still paints its focus: a shadow ring or a border change
        foc.append((k, "painted"))
    else:
        foc.append((k, None))
with_ring = [f"`{k}` ({r})" for k, r in foc if r and r != "painted"]
painted = [f"`{k}`" for k, r in foc if r == "painted"]
without = [f"`{k}`" for k, r in foc if not r]
painted_txt = (f" {len(painted)} paint their focus instead of drawing an outline — a 4px ink-6% box-shadow "
               f"ring over a darker border on {', '.join(painted)}.") if painted else ""
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} draw a ring: {', '.join(with_ring)}.{painted_txt} The other {len(without)} show a keyboard user no change: {', '.join(without)}. The ring is `--ff-focus-width` 2px solid `--ff-color-focus` at `--ff-focus-offset` 2px — near-black on the ff-* layer's controls, the accent blue `#0a68e0` on the home skin's buttons and the composer's send.")
if no_focus:
    W(f"Focus could not be captured on {len(no_focus)}: keyboard focus never reached them (or they took focus without matching :focus-visible), so their focus look is unknown, not absent: {', '.join(f'`{k}`' for k in no_focus)}.")
W()
W("**Pressed.** FlutterFlow's buttons shrink when pressed instead of changing colour: the pill CTAs scale to about 0.94-0.97 (`transform: scale()` at a forced :active). The segmented options and quiet buttons do the same; colour changes on press are minimal.")
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


# The header's dropdown panels (.ff-snav-panel*) and the footer's link columns
# (.ff-ftr-cols) are grids too, but they are chrome, never the page's own layout
# grid: they sit before the content grids in document order, so the first grid
# in the file is usually navigation, not the page.
CHROME_GRID = re.compile(r"ff-snav|ff-ftr")


def grid_of(key):
    v = LAYOUT.get(key)
    if not v:
        return "-"
    grids = [g for g in v["grids"] if not CHROME_GRID.search(g["el"])]
    g = max(grids, key=lambda x: x["w"]) if grids else None   # the widest content grid
    cols = re.sub(r"(\d+\.\d)\d*px", r"\1", g["cols"]).replace("px", "") if g else ""
    main = f"content x {v['main']['x']}, {v['main']['w']} wide" if v["main"]["w"] else "content full width"
    return f"{main}; grid {cols} gap {g['colGap']} on {g['el']}" if g else main


for page in ["home", "product", "pricing", "studio", "studio-showcase", "studio-faq", "vs-studio"]:
    W(f"| {page} | " + " | ".join(grid_of(f"{page}@{w}") for w in (1440, 1920, 1024, 390)) + " |")
W()
W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
# the card-like components to compare in one table (measured on the painted surfaces)
for k in ["plan-card", "showcase-card", "app-card", "cells-item", "nav-panel", "select-popup", "accordion-item", "contact-form", "m-menu-dialog"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if "style" in s), None)
    if st is None:
        continue
    # The measured values of the card element itself, never borrowed from a painted
    # child (the first rounded, filled descendant is a tag dot or a pill button, not
    # the card). When the outer element paints nothing its entry's "Child layers"
    # line names the nodes that carry the look.
    p = props(st)
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
        W(f'<a id="{k}"></a>')   # links elsewhere use the component key, not the title's slug
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
W(f"{len(icons)} SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Logos inside customer marks and the product-shot artwork were left out; these are the interface icons. The SVGs are FlutterFlow's property, kept for reference only.")
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
W("- **Signed-in surfaces.** app.flutterflow.io, the project dashboard, the editor canvas, the AI generation flow, billing/account pages and every \"Start building\"/\"Sign in\"/\"Open Studio\" destination sit behind login and were never opened. The composer submits to a signed-in flow; it was measured, focused and typed in (then cleared) but never submitted, so what a prompt generates was not captured.")
W("- **Form submissions.** The enterprise Talk-to-sales form and the Studio application form were read and focused; neither was filled meaningfully or submitted, so their success/error screens are missing. The `.ff-fld-err` error slot is in the DOM with a declared danger colour but unpainted at rest, so there is no painted validation state in the package.")
W("- **Checkout.** Choosing a paid plan leads to a signed-in checkout; the plan CTAs were measured but never followed.")
W("- **Blog and changelog entries.** The index pages were captured; individual posts follow the same article shell and were not paged through.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover), so a state a script adds on real mousedown (if any) is missing; the `How` row of each pressed reading says so.")
W("- **Hover** on several controls (the secondary plan CTA, select options, the composer send) changed nothing measurable beyond what the entry lists; the nav links' hover is a colour change to ink.")
W("- **The select popup's scroll region** was measured open; option-level checked state inside it was not exercised (an option click would close the popup).")
W("- **Disabled states** were not seen on any public control; the composer's send sits disabled until text is entered, painted at 40% ink.")
W("- **Scroll-driven animations.** Several sections animate in on scroll (the sheets declare scroll-timeline work); the measurements read resting states, and reduced-motion behaviour is in [raw/motion.json](raw/motion.json), not per-component.")
W()
W("### Themes")
W()
W("Both themes are real: the footer switch writes `ff-theme` to localStorage and sets `html[data-theme]`; the sheets rebind every `--ff-*` under `:root[data-theme=\"dark\"]` and under `prefers-color-scheme: dark` when no choice is stored. The dark set's values come from the switch's own Dark pick (verified painted, not inferred), on home, product, pricing and enterprise plus per-component `dark` states on the home composer, the announcement bar and the contrast button. Dark shots of the other pages and a mobile dark pass were not taken; the token file still carries a full dark set because the declarations are complete.")
W()
W("### Fonts")
W()
W("- **Inter** is self-hosted (variable, wght 100-900) and is what every role measures; FlutterFlow's 510 is the semibold stop.")
W("- The **mono** roles use the `ui-monospace` stack: SF Mono where present, else the platform mono — not a shipped face.")
W()
W("### Screenshots")
W()
W("- Customer logos, product-shot artwork and testimonial photos are FlutterFlow's and their customers' content and appear only inside screenshots and crops. Several hero and product modules animate or video-loop, so two captures of the same view can differ.")
W("- Full-page shots are capped at eight chunks; `/blog` and `/customer-stories` index pages are long but every captured page fit the cap (the height each shot reached is in its `.capture.json` sidecar).")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- The cookie-consent banner (a CookieScript vendor widget) was closed before each capture and is not part of the design layer; its `--ck-*` variables are in [raw/css-vars.json](raw/css-vars.json) under `vendor`.")
W("- The demo videos and animated product modules inside the pages' mock windows were not transcribed; only the frames around them were measured.")
W("- No personal data was captured: the pages were read signed out, and no form was submitted.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops,", len(icons), "icons")
