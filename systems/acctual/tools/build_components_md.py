#!/usr/bin/env python3
"""Build components.md for the Acctual design reference.

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


def _p3_to_srgb(r, g, b):
    """Display-P3 channel triplet (0-1) -> sRGB 0-255 triple, the same conversion the token file used."""
    def lin(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    R, G, B = lin(r), lin(g), lin(b)
    X = 0.48657095 * R + 0.26566769 * G + 0.19821729 * B
    Y = 0.22897456 * R + 0.69173852 * G + 0.07928691 * B
    Z = 0.04511338 * G + 1.04394437 * B
    r2 = 3.2404542 * X - 1.5371385 * Y - 0.4985314 * Z
    g2 = -0.9692660 * X + 1.8760108 * Y + 0.0415560 * Z
    b2 = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    def enc(c):
        c = max(0, min(1, c))
        return c * 12.92 if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055
    return tuple(round(enc(c) * 255) for c in (r2, g2, b2))


def colour(c, tokens=True):
    """rgb()/rgba()/color(srgb|display-p3) -> '#hex `token`' or 'rgba(...)'."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        tok = BY_COLOR.get(v) if tokens else None
        return f"{v} `{tok}`" if tok else v

    c = re.sub(r"color\(display-p3 ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)",
               lambda m: label(norm(*_p3_to_srgb(float(m.group(1)), float(m.group(2)), float(m.group(3))), m.group(4))), c)
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


def focus_not_captured(v):
    """A state whose reading is not what its name says: a skipped one, or a focus-visible reading
    taken where keyboard focus never landed (kbFocus returned "focus failed") or where the element
    took focus but did not match :focus-visible. Its style is the element at rest, so it is left out
    of every table and tally and listed as "focus could not be captured"."""
    return bool(v.get("skipped")) or v.get("via") == "focus failed" or (v.get("focus") or {}).get("matches") is False


def measured(v):
    return "style" in v and not focus_not_captured(v)


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

PAGE_NAME = {"home": "home", "pricing": "pricing", "teams": "teams", "about": "about",
             "blog": "blog", "blog-post": "blog post", "altitude": "Altitude announcement",
             "freelancer-invoicing": "freelancer invoicing", "stablecoin-invoicing": "stablecoin invoicing",
             "location": "US to Japan corridor", "terms": "terms", "privacy": "privacy", "mobile": "mobile home"}

GROUP_INTRO = {
    "Shell and navigation": "The shell every page shares: a top bar with the Acctual wordmark, the Freelancer / Agency / Pricing / Blog links, Log in and the dark Sign-up pill, under the 'Acctual is joining Altitude' announcement strip; and a footer with the 'Create the world&rsquo;s most flexible invoice in seconds' heading, link columns and the 'from NYC' credit.",
    "Home": "The home page: the 'Small business invoices: Get paid on time' display hero with the interactive invoice mock (a marketing demo, not a live product), the fee-comparison rows, persona cards, the security trust rows and the FAQ accordion.",
    "Pricing": "The pricing page: the fee comparison (bank transfer / card / stablecoin, currencies, payout speed) and the same Sign-up CTA.",
    "Company and content pages": "Teams, About, the blog index, one post (the Altitude announcement) and the /altitude page the banner links to.",
    "Landing pages (programmatic)": "The templated landing pages: freelancer-invoicing, stablecoin-invoicing and one location corridor (US to Japan) standing in for the ~30 corridor pages.",
    "Legal text": "The terms and privacy pages: heading plus running legal copy in the same shell.",
    "Mobile (390 wide)": "A few components as a phone draws them, at 390 x 844: the collapsed header with its menu trigger, the opened nav panel and the hero title.",
}

SHOTS = [
    ("home", "Home. Display hero, interactive invoice mock, fee rows, FAQ.", "/"),
    ("pricing", "Pricing. The fee comparison.", "/pricing"),
    ("teams", "Teams. The team plan page. Sitemap only; not in the current nav.", "/teams"),
    ("about", "About. Company page. Sitemap only; not in the current nav.", "/about"),
    ("blog", "Blog index.", "/blog"),
    ("blog-post", "Blog post. Acctual joins Altitude.", "/blog/acctual-joins-altitude"),
    ("altitude", "Altitude announcement page the banner links to.", "/altitude"),
    ("freelancer-invoicing", "Freelancer invoicing. Persona landing page.", "/freelancer-invoicing"),
    ("agency-invoicing", "Agency invoicing. The nav Agency link.", "/agency-invoicing"),
    ("stablecoin-invoicing", "Stablecoin invoicing. Product landing page.", "/stablecoin-invoicing"),
    ("usdc-invoicing", "USDC invoicing. Product landing page.", "/usdc-invoicing"),
    ("usdt-invoicing", "USDT invoicing. Product landing page.", "/usdt-invoicing"),
    ("exporters", "Exporters landing page.", "/exporters"),
    ("invoice-templates", "Invoice templates. Footer link.", "/invoice-templates"),
    ("freshbooks-alternative", "FreshBooks alternative. Footer link.", "/freshbooks-alternative"),
    ("free-invoice-software", "Free invoice software. Reached from the public graph.", "/free-invoice-software"),
    ("location", "US to Japan corridor. Sitemap template, not linked from the homepage footer.", "/locations/us-to-japan"),
    ("location-us-uk", "US to UK corridor. Footer link.", "/locations/us-to-uk"),
    ("terms", "Terms. Legal text.", "/terms"),
    ("privacy", "Privacy. Legal text.", "/privacy"),
    ("old-home", "Retired homepage. Sitemap only.", "/old-home"),
    ("blog-old", "Retired blog index. Sitemap only.", "/blog-old"),
    ("not-found", "The published 404 page.", "/404"),
    ("blog-recurring", "Footer-linked post. Recurring invoices.", "/blog/how-to-set-up-recurring-invoices"),
    ("blog-graphic", "Footer-linked post. Graphic design invoice.", "/blog/graphic-design-invoice"),
    ("blog-web", "Footer-linked post. Web design invoice.", "/blog/web-design-development-invoice"),
    ("blog-video", "Footer-linked post. Video production invoice.", "/blog/video-film-production-invoices"),
    ("blog-paypal", "Footer-linked post. PayPal invoice fees.", "/blog/paypal-invoice-fees-are-they-worth-it"),
    ("blog-upwork", "Footer-linked post. Upwork alternatives.", "/blog/best-upwork-alternatives-12-platforms-to-find-better-work-in-2026"),
    ("blog-pastdue", "Footer-linked post. Past due vs overdue.", "/blog/past-due-vs-overdue-invoices"),
    ("guide", "Public help centre. Getting started.", "https://guides.acctual.com/guide/getting-started"),
    ("guide-overview", "Public help centre. Overview.", "https://guides.acctual.com/guide/overview"),
    ("guide-invoice", "Public help centre. Create and send an invoice.", "https://guides.acctual.com/guide/send-an-invoice/create-send-an-invoice"),
    ("guide-pay", "Public help centre. Pay a bill from wallet.", "https://guides.acctual.com/guide/pay-a-bill/pay-a-bill-from-wallet"),
    ("guide-rates", "Public help centre. Rates and fees.", "https://guides.acctual.com/guide/resources/rates-fees"),
]
MOBILE = [
    ("mobile-home", "Home at 390: collapsed header, the opened menu, single-column cards.", "/"),
    ("mobile-pricing", "Pricing at 390.", "/pricing"),
    ("mobile-blog", "Blog index at 390.", "/blog"),
    ("mobile-freelancer-invoicing", "Freelancer invoicing at 390.", "/freelancer-invoicing"),
    ("mobile-agency-invoicing", "Agency invoicing at 390.", "/agency-invoicing"),
    ("mobile-altitude", "Altitude announcement at 390.", "/altitude"),
    ("mobile-invoice-templates", "Invoice templates at 390.", "/invoice-templates"),
    ("mobile-blog-post", "Altitude blog post at 390.", "/blog/acctual-joins-altitude"),
    ("mobile-location", "US to UK corridor at 390.", "/locations/us-to-uk"),
    ("mobile-terms", "Terms at 390. Full page is truncated at 8 tiles.", "/terms"),
    ("mobile-privacy", "Privacy at 390. Full page is truncated at 8 tiles.", "/privacy"),
    ("mobile-guide", "Getting started guide at 390.", "https://guides.acctual.com/guide/getting-started"),
    ("mobile-guide-invoice", "Create-invoice guide at 390.", "https://guides.acctual.com/guide/send-an-invoice/create-send-an-invoice"),
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
icons = [r.split("\t") for r in open("icons/INDEX.tsv").read().strip().split("\n")[1:]]

W("# Acctual components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real site, the icon index and the Gaps. Captured from acctual.com on {J['_meta']['run'][:10]}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was sent or submitted: the app.acctual.com Log-in and Sign-up links were never opened, and no consent banner ever rendered (none was answered).")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts at four widths are in [raw/layout.json](raw/layout.json).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `system-ui 64/70.4 600, #262626`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (acctual.com has one theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 390 wide.")
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
    ("Mobile menu, open", "home at 390", "the nav trigger pressed (a local disclosure)", "[mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-nav-panel](#m-nav-panel)"),
    ("Invoice demo", "home hero", "the interactive invoice mock scrolled into view; a marketing demo, not a live product", "[home-light-invoice-demo](screenshots/home-light-invoice-demo.png), [invoice-demo](#invoice-demo)"),
    ("FAQ answer, open", "home FAQs", "the question pressed (a local accordion disclosure)", "[home-light-faq-open](screenshots/home-light-faq-open.png), [faq-item](#faq-item)"),
    ("App sign-in / sign-up", "nav links out to app.acctual.com", "recorded at https://app.acctual.com/sign-in (email, password, Continue with Google); nothing typed, Google not clicked, branch stopped", "no screenshot; documented under Gaps"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement files.")
W()
foc, unfocused = [], []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if st and focus_not_captured(st):
        unfocused.append(f"`{k}`")
    if not st or not measured(st):
        continue
    s = st["style"]
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0
    foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else None))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} draw a ring: {', '.join(with_ring)}. The other {len(without)} draw none, so a keyboard user sees no change: {', '.join(without)}.{f" Focus could not be captured on {len(unfocused)} more (keyboard focus never landed on them, so their readings are left out): {', '.join(unfocused)}." if unfocused else ""}")
W()
W("**Pressed.** Forced `:active` was applied to the buttons and links above; the buttons keep their fills, and Framer's stylesheet paints the links `#ff0000` under `:active`. See each entry's Pressed row for what did move.")
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
    # The content column is the tallest fixed-max-width wrapper in maxWidths;
    # "main" is the page-width root (1440 at x=0), not the column.
    cand = [e for e in v.get("maxWidths", []) if re.fullmatch(r"\d+px", e.get("max", ""))]
    if cand:
        e = max(cand, key=lambda e: e["h"])
        main = f"content x {e['x']}, {e['w']} wide"
    else:
        main = f"content x {v['main']['x']}, {v['main']['w']} wide (outer page bounds)" if v["main"]["w"] else "content full width"
    return f"{main}; grid {cols} gap {g['colGap']}" if g else main


for page in ["home", "pricing", "teams", "about", "blog", "freelancer-invoicing", "stablecoin-invoicing", "location"]:
    W(f"| {page} | " + " | ".join(grid_of(f"{page}@{w}") for w in (1440, 1920, 1024, 390)) + " |")
W()
W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
# The card-like components to compare in one table.
for k in ["persona-card", "fee-row", "invoice-demo", "faq-item", "blog-item", "nav-cta"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if measured(s)), None)
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
        # A stable anchor per component key: titles repeat ("Page title" on
        # every page), so the generated #page-title-N anchors drift.
        W(f"#### {c['title']} <a id=\"{k}\"></a>")
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
W(f"{len(icons)} SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Photography and artwork were left out; these are the interface icons (the wordmark, the menu trigger, fee and feature marks, social marks). The SVGs are Acctual's property, kept for reference only.")
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
W("- **The product app stays out.** app.acctual.com (the invoicing product itself) sits behind a sign-in that was never opened; this package covers the public marketing site only. The invoice mock on the home page is an interactive demo, not the app.")
W("- **Programmatic pages are sampled, not exhaustive.** ~30 /locations/* corridors and the persona/product landing pages share templates; one of each was captured (US to Japan, freelancer-invoicing, stablecoin-invoicing). /old-home, /blog-old and /404 were skipped by choice.")
W("- **External destinations.** Help/docs links and social profiles outbound were not visited.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools (`:active`), so a state a script adds on mousedown is missing if one exists. The site's stylesheet paints links `#ff0000` under `:active` where the Framer rule applies.")
W("- **Focus rings are the browser's.** Where the site declares no `:focus-visible` style, the measured ring is headless Chromium's default, not a product choice.")
W("- **Hover moves are JS.** Framer runs its hovers and reveals in script (spring animations), so CSS transition measurements come back 0s and hover diffs are mostly colour-only.")
W("- **Disabled, error, loading and selected states** were not seen on any public control.")
W()
W("### Themes")
W()
W("acctual.com shows one theme: a #fafafa ground with dark text, a single #0098f2 accent and #0d111b button pills; there is no `prefers-color-scheme` variant and no theme attribute, so the token file ships a single `light` set. The site's design tokens are hashed `--token-<uuid>` custom properties resolved in [raw/css-vars.json](raw/css-vars.json); the token file names them where a leaf aliases one.")
W()
W("### Fonts")
W()
W("- Everything reads **Open Runde** except the programmatic landing pages (**Selecta Medium**), the legal body (**Selecta Regular**) and the announcement strip (**Inter**). Geist, Caveat, Fragment Mono and the SF Pro family are declared in @font-face (see [raw/css-vars.json](raw/css-vars.json)) but nothing measured uses them.")
W()
W("### Screenshots")
W()
W("- Photography, illustration and the invoice demo are Acctual's content and appear only inside screenshots and crops.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Blog-post and legal body copy was not transcribed; only the frames around it were measured.")
W("- No personal data was captured: every page was read signed out and no form exists on the marketing surface to touch.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops,", len(icons), "icons")
