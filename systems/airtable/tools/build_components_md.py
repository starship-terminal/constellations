#!/usr/bin/env python3
"""Build components.md for the Airtable design reference.

Reads raw/components-computed.json (every component and state, measured), raw/layout.json,
tokens.json and screenshots/, and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the palette token whose
value matches, the font family is named once per value, and a state row shows only what differs
from the first state. Adapted from the Refero package's builder, which reads the same JSON schema.

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


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


BY_COLOR = {}
for n, t in flat(T["core"]["color"]):
    if t["$type"] == "color":
        BY_COLOR.setdefault(t["$value"], n)


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def srgb_chan(c):
    c = max(0.0, min(1.0, c))
    return round((12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055) * 255)


def lab_rgb(L, a, b):
    fy = (L + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    eps, kap = 216 / 24389, 24389 / 27
    def f(t):
        t3 = t ** 3
        return t3 if t3 > eps else (116 * t - 16) / kap
    X, Y, Z = 0.96422 * f(fx), f(fy), 0.82521 * f(fz)
    return [srgb_chan(v) for v in (3.1338561 * X - 1.6168667 * Y - 0.4906146 * Z,
                                 -0.9787684 * X + 1.9161415 * Y + 0.0334540 * Z,
                                 0.0719453 * X - 0.2289914 * Y + 1.4052427 * Z)]


def oklab_rgb(L, a, b):
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return [srgb_chan(x) for x in (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
                                  -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
                                  -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)]


def colour(c, tokens=True):
    """rgb()/rgba()/lab()/oklab()/color(srgb) -> '#hex `token`' or 'rgba(...)'."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        tok = BY_COLOR.get(v) if tokens else None
        return f"{v} `{tok}`" if tok else v

    c = re.sub(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)",
               lambda m: label(norm(*(round(float(x) * 255) for x in m.group(1, 2, 3)), m.group(4))), c)
    c = re.sub(r"oklab\(([-\d.e]+) ([-\d.e]+) ([-\d.e]+)(?: / ([\d.]+))?\)",
               lambda m: label(norm(*oklab_rgb(float(m.group(1)), float(m.group(2)), float(m.group(3))), m.group(4))), c)
    c = re.sub(r"(?<!ok)lab\(([-\d.e]+) ([-\d.e]+) ([-\d.e]+)(?: / ([\d.]+))?\)",
               lambda m: label(norm(*lab_rgb(float(m.group(1)), float(m.group(2)), float(m.group(3))), m.group(4))), c)
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

PAGE_NAME = {"home": "www.airtable.com home", "platform": "www.airtable.com/platform",
             "platform-ai": "www.airtable.com/platform/ai", "solutions": "www.airtable.com/solutions",
             "enterprise": "www.airtable.com/solutions/enterprise", "pricing": "www.airtable.com/pricing",
             "contact-sales": "www.airtable.com/contact-sales", "customer-stories": "www.airtable.com/customer-stories",
             "templates": "www.airtable.com/templates", "marketplace": "www.airtable.com/marketplace",
             "whatsnew": "www.airtable.com/whatsnew", "about": "www.airtable.com/about",
             "mobile": "www.airtable.com at 390"}

GROUP_INTRO = {
    "Shell and navigation": "The chrome shared by every marketing page: a 121px top bar - a promo strip above the wordmark + section drawers (Platform / Solutions / Resources), Book Demo, a dark Sign up pill and Log in - plus the link-columns footer. Platform and Solutions open a 710px nav drawer; on a phone the bar collapses to a menu button and a side sheet.",
    "Home": "www.airtable.com's home: the 'Your team's apps. Fast.' hero with dark ink CTAs, the feature carousel (tabs, pause, prev/next arrows on a dark band), the coloured 32px-radius path tiles, and the resource cards.",
    "Cards and indexes": "The index pages: /templates (search + filter rail + card gallery), /marketplace (coloured category tiles + extension rows), /whatsnew (an embedded Airtable gallery - the release cards and 'Available on' filters live inside airtable.com/embed), /customer-stories, /solutions, /about.",
    "Platform pages": "/platform and /platform/ai: the ATSeasonSans display titles, the 'Ways to start building' linked cards, the customer-stories carousel on the dark band (pause + prev/next arrows), and the FAQ accordion.",
    "Pricing": "www.airtable.com/pricing (in Inter Display, not Haas): the Free/Team/Business/Enterprise Scale plan columns with 2px-bordered CTAs, and the 'Compare our plans' div grid of hover-container feature rows.",
    "Contact sales form": "www.airtable.com/contact-sales: the 430px-wide sales form - text fields, a phone field, a text area, the custom 'Country' combobox and the dark Submit. Measured at rest, focused and filled; never submitted.",
    "Mobile (390 wide)": "www.airtable.com at 390: the collapsed nav bar, the menu button and the side sheet it opens.",
}


SHOTS = [
    ("home", "www.airtable.com home. Hero, feature carousel, coloured path tiles, resource cards; also the nav drawer and the promo bar closed.", "https://www.airtable.com/"),
    ("platform", "www.airtable.com/platform. 'The Airtable Platform' hero, building cards, customer-stories carousel.", "https://www.airtable.com/platform"),
    ("platform-ai", "www.airtable.com/platform/ai. The AI page: 'Airtable Agents', card grids, FAQ.", "https://www.airtable.com/platform/ai"),
    ("solutions", "www.airtable.com/solutions. The solutions index.", "https://www.airtable.com/solutions"),
    ("enterprise", "www.airtable.com/solutions/enterprise. The enterprise page.", "https://www.airtable.com/solutions/enterprise"),
    ("pricing", "www.airtable.com/pricing. Plan columns, comparison grid, FAQ.", "https://www.airtable.com/pricing"),
    ("contact-sales", "www.airtable.com/contact-sales. The sales form, never submitted.", "https://www.airtable.com/contact-sales"),
    ("customer-stories", "www.airtable.com/customer-stories. The stories index.", "https://www.airtable.com/customer-stories"),
    ("templates", "www.airtable.com/templates. Filter rail + template gallery.", "https://www.airtable.com/templates"),
    ("marketplace", "www.airtable.com/marketplace. Category tiles + extension rows.", "https://www.airtable.com/marketplace"),
    ("whatsnew", "www.airtable.com/whatsnew. 'Where Airtable is headed.' + the embedded release gallery.", "https://www.airtable.com/whatsnew"),
    ("about", "www.airtable.com/about. The about page.", "https://www.airtable.com/about"),
]
MOBILE = [
    ("mobile-home", "www.airtable.com home at 390: menu button, hero, the side sheet open.", "https://www.airtable.com/"),
    ("mobile-pricing", "www.airtable.com/pricing at 390.", "https://www.airtable.com/pricing"),
    ("mobile-platform", "www.airtable.com/platform at 390.", "https://www.airtable.com/platform"),
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

W("# Airtable components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from www.airtable.com's public marketing pages on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running pages. Nothing was signed into, submitted, bought or sent; no consent dialog was answered and no form was submitted.")
W()
W("The public surface is the **www.airtable.com marketing site**: white surfaces, #181d26 ink text in Haas, a --color-primitive-* ramp system plus --color-surface/text/border-* semantics and a per-section --theme_* set all declared on :root. Most pages typeset in Haas/ATSeasonSans; /pricing runs Inter Display and /marketplace GT Eesti Display. The site is light-only - prefers-color-scheme changes nothing (`themeChecks` in raw/css-vars.json). Third-party UI (the Qualified 'Riley' chat widget and Google One Tap) is swept out of every shot.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [raw/layout.json](raw/layout.json).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/18 500, #000`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` . Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). There is no dark pass - the site ships one theme.")
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
    ("Nav drawer", "www.airtable.com", "the Platform trigger was clicked once; a local disclosure, closed with Escape", "[home-light-nav-dropdown](screenshots/home-light-nav-dropdown.png), [nav-dropdown](#nav-drawer)"),
    ("Promo dismissal", "www.airtable.com", "the promo bar's close button hid it; a local toggle", "[home-light-promo-closed](screenshots/home-light-promo-closed.png), [promo-close](#promo-close-button)"),
    ("Country dropdown", "www.airtable.com/contact-sales", "the 'Country' combobox was clicked open; nothing chosen", "[select-field-open](#select-field-open)"),
    ("FAQ accordions", "www.airtable.com/platform/ai, /pricing", "one question each was expanded; a local disclosure", "[faq-item-open](#faq-item-open), [pricing-faq-item-open](#pricing-faq-item-open)"),
    ("Mobile nav sheet", "www.airtable.com at 390", "the 'Open side menu' button opened the drawer", "[mobile-home-light-nav-open](screenshots/mobile-home-light-nav-open.png), [m-nav-sheet](#mobile-nav-sheet)"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ checklist coverage
def states_of(*names):
    seen = []
    for n in names:
        for s in C.get(n, {}).get("states", {}):
            if s not in seen:
                seen.append(s)
    return ", ".join(seen) if seen else "-"

def entry_links(*names):
    out = []
    for n in names:
        if n not in C:
            continue
        t = C[n].get("title", n)
        anchor = re.sub(r"[^a-z0-9 -]", "", t.lower()).replace(" ", "-")
        out.append(f"[{t}](#{anchor})")
    return ", ".join(out)

CHECKLIST = [
    ("Button", ("hero-cta-primary", "hero-cta-secondary", "nav-signup", "nav-demo", "platform-cta", "plan-cta", "submit-button", "marketplace-cta"), None),
    ("Icon button", ("promo-close", "carousel-control", "stories-prev", "stories-next", "stories-pause", "m-nav-menu-btn"), None),
    ("Link", ("nav-link", "footer-link", "promo-link", "see-more-link", "nav-login", "nav-dropdown-link"), None),
    ("Text field", ("text-field", "text-field-box", "email-field", "phone-field", "template-search-field", "marketplace-search"), None),
    ("Text area", ("text-area",), None),
    ("Select", ("select-field", "select-field-open", "country-selector", "whatsnew-filter"), "custom comboboxes, not native <select>s - the contact-sales mirror selects stay hidden at 0x0"),
    ("Checkbox", (), "the sales form has none; the templates filter rail is a plain link list"),
    ("Radio", (), "none on the public surface"),
    ("Switch", (), "none measured; no public toggle was found"),
    ("Tabs", ("feature-tab", "feature-tab-active", "feature-tab-list"), "the marketplace's Featured/Extensions tab rail wasn't measured"),
    ("Menu", ("nav-dropdown", "nav-dropdown-link", "m-nav-sheet", "nav-trigger"), None),
    ("Tooltip", (), "none appeared on hover or focus"),
    ("Dialog", (), "no dialog on the public pages; the nav drawer is the closest disclosure"),
    ("Toast", (), "no toast appeared after any action the capture took signed out"),
    ("Card", ("feature-card", "tile-card", "platform-card", "platform-ai-card", "resource-card", "market-card", "template-card", "whatsnew-item", "story-card", "about-card", "solutions-card", "enterprise-card", "plan-card", "ai-feature-card"), None),
    ("List row", ("story-row", "compare-table-row", "filter-section", "filter-section-open", "faq-item", "pricing-faq-item"), None),
    ("Table", ("compare-table", "compare-table-row"), "a div grid, not a <table>"),
    ("Avatar", (), "no avatars on the public surface"),
    ("Badge", (), "the whatsnew release cards carry plan chips inside the embed, not a standalone badge"),
]

present = sum(1 for _, names, _ in CHECKLIST if names)
W("## Checklist coverage")
W()
W(f"The 19 components of the library's checklist ([docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md)), each with the entries below that show it and the states captured across them. {present} of 19 are captured; the rest do not exist on the public marketing surface.")
W()
W("| Component | Entries | States captured |")
W("|---|---|---|")
for comp, names, note in CHECKLIST:
    cells = entry_links(*names) if names else f"not captured: {note}"
    W(f"| {comp} | {cells} | {states_of(*names)} |")
W()

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement files.")
W()
foc = []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st or "style" not in st:
        continue
    s = st["style"]
    base = c["states"].get("default", {}).get("style", s)
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0 and (s["outlineStyle"] != base["outlineStyle"] or s["outlineWidth"] != base["outlineWidth"])
    ring_shadow = s["boxShadow"] != base["boxShadow"] and "0px 0px" in s["boxShadow"]
    foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else ("ring shadow " + colour(s["boxShadow"], tokens=False) if ring_shadow else None)))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} show a change: {', '.join(with_ring)}. The other {len(without)} draw nothing new - buttons and nav controls take a 2px rgba(4,14,32,.69) ring offset 2-4px and fields a 1px #005fcc outline: {', '.join(without)}.")
W()
W("**Pressed.** Pressed was forced with DevTools, so it is the :active styles only: the dark ink CTAs darken to rgba(7,12,20,.82) and the outline buttons fill rgba(15,48,106,.05). The submit button and every sign-in/demo link were never pressed for real.")
W()
W("**Motion.** Transitions measured on the components, by duration; the site's declared curves are the --motion-* set (core.motion in tokens.json): standard/decelerate/accelerate at 150-600ms.")
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
W("**Layout.** Read on each page ([raw/layout.json](raw/layout.json)).")
W()
W("| Page | Frame | Content column | Grids | Fixed |")
W("|---|---|---|---|---|")


def layrow(key):
    v = LAYOUT.get(key)
    if not v:
        return f"| {key} | - | - | - | - |"
    frame = []
    if v.get("sidebar"):
        frame.append(f"sidebar {v['sidebar']['w']}px")
    if v.get("header"):
        frame.append(f"top bar {v['header']['h']}px, {v['header'].get('pos','')}, {v['header'].get('backdrop','')}")
    mw = max(v.get("maxWidths") or [{"w": 0, "max": "-"}], key=lambda m: m["w"] if m["w"] < v["vw"] * 0.99 else 0)
    col = f"max-width {mw['max']}" if mw.get("max") not in (None, "-") else "full width"
    gs = v.get("grids") or []
    g = f"{len(gs)} grids" if gs else "-"
    if gs:
        g += " (" + "; ".join(f"{len(gd['cols'].split())} col gap {gd['colGap']}" for gd in gs[:2]) + ")"
    fx = ", ".join(f"{(f.get('text','') or f.get('el','?')).split(chr(10))[0][:40].replace('|','/')} ({f.get('pos','fixed')})" for f in (v.get("fixed") or [])[:3]) or "-"
    return f"| {key} | {'; '.join(frame) or '-'} | {col} | {g} | {fx} |"


for key in LAYOUT:
    W(layrow(key))
W()
W("**Card shapes.** Default-state values; the entries hold the states. The signature cards are the 32px-radius coloured tiles (#c7e5f2 blue, #fcab79 orange) and the 16px white index cards on #e0e2e6 borders; release cards run 6px, marketplace tiles 12px.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
for k in ["feature-card", "tile-card", "platform-card", "solutions-card", "market-card", "whatsnew-item", "plan-card", "nav-dropdown", "m-nav-sheet"]:
    c = C.get(k)
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
W("- **The products.** app.airtable.com is the signed-in product: nothing behind Sign up, Log in or Book Demo was captured - the workspace, base editor, interfaces, automations and billing are all missing. The kit never signs in, registers, or books a demo.")
W("- **Checkout and account.** The plan CTAs and the contact-sales form lead to flows that were never submitted; no purchase was made and no field was filled with real contact details.")
W("- **Page-depth pages.** The index pages were captured; individual templates, marketplace extensions and customer stories were not opened.")
W("- **Embedded content.** whatsnew's release gallery is Airtable's own published interface served in an iframe (airtable.com/embed/appL2oaKxSWg9qz8y); cards and filters were measured inside it.")
W("- **Third-party widgets.** The Qualified 'Riley' chat launcher and Google One Tap are swept out of every capture; they are not Airtable design system components.")
W("- **Consent.** The 'Privacy choices' footer control opens consent settings; it was never opened because answering it is a submission.")
W()
W("### Themes")
W()
W("The site ships one theme: no dark values are declared and nothing changed under prefers-color-scheme (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)). The token file has no `dark` set - that is a documented gap, not an omission.")
W()
W("### Fonts")
W()
W("- **Haas** (Neue Haas Grotesk) is the body face and **Haas Groot Disp** the display face on most pages; **ATSeasonSans** carries the nav and platform-page headlines; **Inter Display** typesets /pricing and **GT Eesti Display** /marketplace. All are commercial faces served from Airtable's hosts (see fontFaces in [raw/css-vars.json](raw/css-vars.json)) - not redistributable; the style guide stands in with system faces.")
W()
W("### Screenshots")
W()
W("- People, logos and product imagery are Airtable's content and appear only inside screenshots and crops.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Page prose was not transcribed into the package; the components around it were measured.")
W("- No personal data was captured: the pages were read signed out, and no form was filled with real contact details.")
W()

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops")
