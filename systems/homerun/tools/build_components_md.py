#!/usr/bin/env python3
"""Build components.md for the Homerun design reference.

Reads raw/components-computed.json (every component and state, measured), raw/layout.json,
tokens.json, screenshots/ and icons/INDEX.tsv, and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the palette token whose
value matches, the font family is named once per value, and a state row shows only what differs
from the first state. Adapted from the Gauth kit's builder.

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
for n, t in flat(T["core"]["color"]):
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
        o["text"] = f"{font(t.get('fontSize', s['fontSize']), t.get('lineHeight', s['lineHeight']), t.get('fontWeight', s['fontWeight']), t.get('fontFamily', s['fontFamily']))}, {colour(t.get('color', s['color']))}"
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

PAGE_NAME = {"home": "home", "pricing": "pricing", "ats": "ATS product", "careers": "careers (jobs.homerun.co)",
             "job": "job ad", "apply": "application form", "signin": "ATS sign-in", "signinhr": "HR sign-in"}

GROUP_INTRO = {
    "Shell and navigation": "The sticky top bar of the marketing site: logo, product pill, the Resources and Log in dropdowns (both open on hover), the dark Book-a-demo button and the blue Start-free-trial button.",
    "Home": "The home page: GT Walsheim hero headline over the white ground, a blue primary CTA next to a dark secondary one, the rating row, feature accordions, testimonial cards on the beige band, the logo marquee and the closing dark CTA band.",
    "Pricing": "The pricing page: three plan cards with the job-slot stepper, a feature table, the FAQ accordion and the closing CTA.",
    "ATS page": "The ATS product page: hero, feature tabs, integration cards.",
    "Careers site (jobs.homerun.co)": "Homerun's own employer careers site, a separate client-rendered app on the same palette: header, job list, the cookie banner (hidden, never answered), a job ad and the share/back chrome.",
    "Application form": "The public application wizard a job ad links to: steps strip, fields, file upload and checkbox, Back/Next. Measured at rest; nothing was typed, uploaded or submitted.",
    "ATS sign-in (boundary)": "app.homerun.co/login, the Angular sign-in card: SSO buttons, email/password fields, Log in. Measured at rest; nothing was typed or submitted.",
    "HR sign-in (boundary)": "app.homerun.hr/Account/Logon, the .NET HR sign-in card on the Tailwind UI stack, its button in the HR green. Measured at rest; nothing was typed or submitted.",
    "Mobile (390 wide)": "The marketing nav and hero as a phone draws them, at 390 x 844 with an iPhone user agent, and the hamburger's opened menu sheet.",
}

SHOTS = [
    ("home", "Home. Hero, rating row, feature accordions, testimonials, logo marquee, dark CTA band, footer. The two hover-open nav dropdowns captured.", "/"),
    ("ats", "ATS product page. Hero, feature tabs, integration cards.", "/ats"),
    ("hr", "HR product page.", "/hr"),
    ("features", "Product features page.", "/product/features"),
    ("pricing", "Pricing. Plan cards, feature table, FAQ (one item opened), CTA.", "/pricing"),
    ("customers", "Customers page.", "/customers"),
    ("about", "About page.", "/about"),
    ("contact", "Contact page.", "/contact"),
    ("blog", "Blog index.", "/blog"),
    ("templates", "Job-template library.", "/templates"),
    ("integrations", "Integrations directory.", "/integrations"),
    ("guides", "Guides index.", "/guides"),
    ("updates", "Product updates index.", "/updates/"),
    ("trial", "Start-free-trial page.", "/trial"),
    ("privacy", "Privacy statement.", "/privacy-statement"),
    ("careers", "Careers site root (jobs.homerun.co): header, job list, cookie banner hidden.", "https://jobs.homerun.co/"),
    ("job", "A job ad on the careers site: title, Apply button, description prose, share and back.", "https://jobs.homerun.co/open/en"),
    ("apply", "The public application form: steps strip, fields, upload and checkbox, Back/Next. At rest; nothing typed, uploaded or submitted.", "https://jobs.homerun.co/open/en/apply"),
    ("signin", "ATS sign-in at app.homerun.co/login. SSO buttons, email/password, Log in. At rest; never submitted.", "https://app.homerun.co/login"),
    ("signinhr", "HR sign-in at app.homerun.hr/Account/Logon. Email/password, green Log in. At rest; never submitted.", "https://app.homerun.hr/Account/Logon"),
]
MOBILE = [
    ("mobile-home", "Home at 390: bar, hero, full page, and the hamburger's open menu sheet.", "/"),
    ("mobile-pricing", "Pricing at 390.", "/pricing"),
    ("mobile-ats", "ATS product page at 390.", "/ats"),
    ("mobile-careers", "Careers site at 390.", "https://jobs.homerun.co/"),
    ("mobile-apply", "Application form at 390.", "https://jobs.homerun.co/open/en/apply"),
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

W("# Homerun components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from www.homerun.co, jobs.homerun.co, app.homerun.co/login and app.homerun.hr/Account/Logon on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent, uploaded or submitted.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The layout geometry is in [raw/layout.json](raw/layout.json).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `GT America 16/24 400, #4a3e3e`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (Homerun shows one light theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x stitched from `.partN` tiles when the page is taller than one GPU texture; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).")
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
    ("Resources dropdown", "marketing nav", "hovering the Resources toggle (Webflow data-hover)", "[home-light-nav-resources-open](screenshots/home-light-nav-resources-open.png), [nav-resources-panel](#resources-panel)"),
    ("Log in dropdown", "marketing nav", "hovering the Log in toggle", "[home-light-nav-login-open](screenshots/home-light-nav-login-open.png), [nav-login-panel](#log-in-panel)"),
    ("Pricing FAQ, opened", "pricing", "the question's own toggle", "[pricing-light-faq-open](screenshots/pricing-light-faq-open.png), [faq-item](#faq-item)"),
    ("Mobile menu, opened", "home at 390", "the hamburger's own press (an in-page click; the tap layer never reaches it)", "[mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu-open](#m-menu-open)"),
    ("Cookie consent", "careers site", "present on load; hidden for every capture, never accepted or declined", "[cookie-banner](#cookie-banner)"),
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
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0
    foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else None))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} draw a ring: {', '.join(with_ring)}. The other {len(without)} draw none, so a keyboard user sees no change: {', '.join(without)}.")
if no_focus:
    W(f"Focus could not be captured on {len(no_focus)}: keyboard focus never reached them (or they took focus without matching :focus-visible), so their focus look is unknown, not absent: {', '.join(f'`{k}`' for k in no_focus)}.")
W()
W("**Pressed.** The blue controls darken on press to blue-600 `#254cda` (the hero CTA, the nav trial button and the ATS sign-in button all read the same value); the dark buttons lighten toward brown-300 `#4a3e3e`; the HR button darkens toward `#128053`. The careers and apply buttons hold their fill. What changed is in each entry's state row.")
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


for page in ["home", "pricing", "ats", "careers", "job", "signin"]:
    W(f"| {page} | " + " | ".join(grid_of(f"{page}@{w}") for w in (1440, 1920, 1024, 390)) + " |")
W()
W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
for k in ["plan-card", "testimonial-card", "ats-card", "ats-integrate-card", "careers-job-card", "signin-card", "hr-card", "cookie-banner", "faq-item", "feature-accordion", "nav-resources-panel", "nav-login-panel", "m-menu-open", "apply-next"]:
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
if icons:
    W(f"{len(icons)} SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Product screenshots, mockups and the logo-marquee artwork were left out; these are the interface icons. The SVGs are Homerun's property, kept for reference only.")
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
W("- **Signed-in pages.** Nothing behind sign-in was captured: the ATS dashboard, pipelines, job editor, candidate profiles and the HR admin. Both sign-in cards were measured at rest and never submitted; no credentials exist in this capture.")
W("- **Anything that converts or sends.** The trial and demo forms were not filled or sent (the /trial page was captured as marketing, not signed up through), the application wizard was never advanced past its first step, no file was uploaded, no newsletter or contact form was submitted.")
W("- **Article and entry pages.** Blog posts, guide entries, update notes, template detail pages and customer stories are linked lists only — the index pages were captured, individual articles were not opened.")
W("- **The careers cookie banner** was hidden for every capture, never answered, so a consent-accepted render is not in this set.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **pricing-table, pricing-table-head and pricing-table-row** kept their earlier readings (the feature table was below the lazy-load line on the recapture pass); their entries carry `recaptureMissed` provenance in the JSON.")
W("- **ats-tab** read 0 x 0: the feature tabs render their labels through a script that had not painted them at measure time.")
W("- **apply-file and apply-checkbox** read 0 x 0: the wizard hides its file input and checkbox inputs visually (custom controls paint them).")
W("- **Disabled states** were not seen on any public control.")
W()
W("### Themes")
W()
W("Homerun shows one light theme on every captured surface. The marketing pages paint dark content bands inside that theme (the closing CTA band, `.dark`/`.darkbg` classes on sections) and the careers, ATS and HR surfaces are all light; no dark switch or `prefers-color-scheme` variant was found (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)). The token file therefore ships one `light` set, and the dark bands are captured as `light.surface.dark`, not as a theme.")
W()
W("### Fonts")
W()
W("- **GT America** (UI text, buttons, nav) and **GT Walsheim** (display headlines, weight 900) are Grilli Type faces served from Homerun's CDN; they are commercial fonts, so the style guide falls back to a system sans where they are not installed.")
W("- The careers site paints `GTAmerica-Regular` and the application wizard paints **Inter**; the app sign-in bundle names the same family `GT-America`; the HR card paints the `ui-sans-serif` stack.")
W()
W("### Screenshots")
W()
W("- Customer logos, product mockups and team photos are Homerun's content and appear only inside screenshots and crops.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Job-ad prose, plan pricing copy and article text were not transcribed; only the frames around them were measured.")
W("- No personal data was captured: the pages were read signed out, the sign-in fields stayed empty and the application form was never filled.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops,", len(icons), "icons")
