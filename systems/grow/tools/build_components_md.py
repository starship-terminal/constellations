#!/usr/bin/env python3
"""Build components.md for the Grow with Google design reference.

Reads raw/components-computed.json (every component and state, measured), raw/layout.json,
tokens.json, screenshots/ and icons/INDEX.tsv, and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the palette token whose
value matches, the font family is named once per value, and a state row shows only what differs
from the first state. Adapted from the Gauth package's builder (the Coursera kit's lineage), which
read markdown; this one reads the JSON directly.

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
for n, t in flat(T["core"]["color"]["palette"], "color.palette."):
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


def focus_not_captured(v):
    """A state whose reading is not what its name says: a skipped one, or a focus-visible reading
    taken where keyboard focus never landed (via "focus failed") or where the element took focus
    but did not match :focus-visible. Its style is the element at rest, so it is left out of every
    table and tally and listed as "focus could not be captured" (the kit's rule, PR 932)."""
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


def covers(layer, st):
    try:
        w, h = (float(x) for x in layer["size"].split("x"))
    except (KeyError, ValueError):
        return False
    rw, rh = st["rect"]["w"], st["rect"]["h"]
    return rw > 0 and rh > 0 and w * h >= 0.9 * rw * rh


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

PAGE_NAME = {"home": "home", "certificates": "certificates catalog", "cert-ux": "UX Design certificate",
             "cert-data": "Data Analytics certificate", "ai": "AI training", "ai-pro": "AI Professional",
             "stories": "stories", "mission": "mission", "partners": "partners", "employers": "employers",
             "news": "news & insights", "mobile": "home (390 wide)"}

GROUP_INTRO = {
    'Site chrome': 'The header on every page: the "Grow with Google" lockup, the Career Certificates / AI Training / For Partners / Stories & Resources nav, its dropdown mega-menus and the promo banner. The fixed header is white at every scroll depth; the mega-menu is a full-bleed 1440px panel under it.',
    'Home': 'The US home page: the promo banner, a video-led hero ("Grow your career or business"), the Career Certificate CTA, a sectioned story and the announcement card row.',
    'Certificates': 'The /certificates catalog: the breadcrumb, the display heading, the statistics band, the Learn more anchor, the glue-jumplinks pill tab bar and the certificate card grid on the light-blue band.',
    'Certificate detail': 'A certificate page (/certificates/ux-design/): the dark editorial hero, the Coursera enrol CTA, the graduate badge and the FAQ expansion rows. Every enrolment link was measured, never followed.',
    'AI training': 'The /ai hub: a tinted heading band and the large AI course cards.',
    'Footer': 'The site footer: link columns, the legal row and the region/language <select> — measured, never changed (its form posts to services.google.com).',
    'Mobile (390 wide)': 'A few components as a phone draws them, at 390 x 844: the compact header, the drawer toggle, the opened navigation drawer.',
}

SHOTS = [
    ("home", "Home (US). The promo banner, the video hero, the Career Certificate CTA, story sections and the footer; the menu, the video modal and the full page captured.", "/"),
    ("certificates", "Certificates catalog. Breadcrumb, heading, stats band, Learn more, jumplinks, the foundational certificate card grid.", "/certificates"),
    ("cert-ux", "UX Design certificate. The dark hero, Coursera CTA, graduate badge, curriculum tabs, expansion FAQ (opened captured).", "/certificates/ux-design/"),
    ("cert-data", "Data Analytics certificate. The same detail template on a second certificate.", "/certificates/data-analytics/"),
    ("ai", "AI training hub. The tinted heading band and the course cards.", "/ai/"),
    ("ai-pro", "AI Professional Certificate page.", "/ai-professional/"),
    ("stories", "Stories. Graduate and business story cards.", "/stories/"),
    ("mission", "Our mission. The program overview page.", "/our-mission/"),
    ("partners", "For partners. The employer/consortium page.", "/partners/"),
    ("employers", "For employers. The hire-graduates page.", "/employers/"),
    ("news", "News & insights. Press and update cards.", "/news-insights/"),
    ("apac-home", "Home (APAC regional variant). The /intl/ALL_sg/ edition this host's real-UA requests are redirected to; retained as variant evidence, not the canonical surface.", "/intl/ALL_sg/"),
]
MOBILE = [
    ("mobile-home", "Home at 390: the compact header, the opened drawer and the full page in two tiles.", "/"),
    ("mobile-certificates", "Certificates catalog at 390.", "/certificates"),
    ("mobile-cert-ux", "UX Design certificate at 390.", "/certificates/ux-design/"),
    ("mobile-ai", "AI training hub at 390.", "/ai/"),
    ("apac-mobile-home", "APAC home at 390: the /intl/ALL_sg/ edition's drawer and full page.", "/intl/ALL_sg/"),
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

W("# Grow with Google components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from grow.google on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, enrolled in, bought or submitted; the only presses were local UI toggles the page's own chrome provides — the Career Certificates mega-menu, the mobile navigation drawer, one FAQ expansion row and the hero video modal (opened and closed, the YouTube embed never played). Every link and CTA was measured, never followed; the footer's language <select> was never changed — its form posts to services.google.com.")
W()
W("**Where this was read.** The canonical surface is grow.google's **US edition**: bare headless contexts (no user agent, no locale) receive it. From this capture host, a request carrying a real browser user agent or an explicit locale is 302'd from `/` to the regional `/intl/ALL_sg/` edition — the APAC variant shots (`apac-*`) record that edition, and every deep link serves the US edition regardless. The cookie notification bar was removed from captures (hidden, never answered).")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [patterns.md](patterns.md) and the layout probe in [raw/layout.json](raw/layout.json).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one — grow.google's stylesheet declares only the `--glue-*-{50..900}` colour ramps as custom properties, so most entries label against that ramp. Text is written family size/line-height weight, then its colour, for example `Google Sans Flex 16/24 500, #3c4043`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (grow.google paints one theme — light only, no toggle and no applied dark media query; the certificate pages' dark hero is a section paint). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x); `apac-*` shots are the /intl/ALL_sg/ regional variant. Tall pages split the full shot into `.partN` tiles, bounded, with the clip in each `.capture.json` sidecar.")
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
    ("Career Certificates mega-menu", "site header", "clicked the nav trigger — a local UI toggle that opens the three-column panel (Foundational / Advanced / Courses); its links were never followed", "[home-light-menu](screenshots/home-light-menu.png), [nav-drop-trigger](#mega-menu-trigger), [mega-panel](#mega-menu-panel), [mega-item](#mega-menu-item)"),
    ("Hero video modal", "home hero", "clicked the video teaser — a Glue modal opens a YouTube embed; captured and closed, the video never played", "[home-light-video](screenshots/home-light-video.png), [video-teaser](#video-teaser)"),
    ("FAQ expansion row", "UX Design certificate", "clicked the row header — the panel's own toggle; measured default and opened", "[cert-ux-light-faq-open](screenshots/cert-ux-light-faq-open.png), [expansion-panel](#expansion-panel), [expansion-content](#expansion-content)"),
    ("Mobile navigation drawer", "home at 390", "the header hamburger's own press — the drawer slides in", "[mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-drawer-btn](#drawer-toggle), [m-drawer-link](#drawer-link)"),
    ("APAC regional edition", "home, every request with a real UA or locale", "a 302 from `/` to `/intl/ALL_sg/` — the canonical US surface comes from bare contexts; the APAC shots are variant evidence", "[apac-home-light-default](screenshots/apac-home-light-default.png), [apac-mobile-home-light-drawer](screenshots/apac-mobile-home-light-drawer.png)"),
    ("Language select", "site footer", "never changed — the form posts to services.google.com, an external action", "measured as [footer-lang](#locale-select)"),
    ("Enrolment and accounts", "Coursera, Google accounts", "every 'Get started on Coursera' and sign-in affordance leads off grow.google — measured, never followed", "boundary; see Gaps"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement files.")
W()
RING = re.compile(r"(rgba?\([^)]*\))\s+0px\s+0px\s+0px\s+([\d.]+px)")


def clear(c):
    return c.strip() == "transparent" or bool(re.fullmatch(r"rgba\([^)]*,\s*0\)", c.strip()))


foc, unfocused, clear_outline = [], [], []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if st and focus_not_captured(st):
        unfocused.append(f"`{k}`")
    if not st or not measured(st):
        continue
    s = st["style"]
    ring = RING.fullmatch((s.get("boxShadow") or "none").strip())
    outlined = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0
    if outlined and clear(s["outlineColor"]):
        clear_outline.append(f"`{k}`")
        outlined = False
    if ring:
        kind = f"a {ring.group(2)} box-shadow ring in {colour(ring.group(1))}"
    elif outlined:
        kind = f"a {s['outlineWidth']} {s['outlineStyle']} outline in {colour(s['outlineColor'])} (offset {s['outlineOffset']})"
    else:
        kind = None
    foc.append((k, kind))
kinds = {}
for k, kind in foc:
    kinds.setdefault(kind, []).append(f"`{k}`")
parts = [f"{len(v)} draw {kind}: {', '.join(v)}." for kind, v in kinds.items() if kind]
if kinds.get(None):
    parts.append(f"{len(kinds[None])} draw no ring, so a keyboard user sees no change: {', '.join(kinds[None])}.")
if clear_outline:
    parts.append(f"{len(clear_outline)} also set a transparent outline, which draws nothing: {', '.join(clear_outline)}.")
if unfocused:
    parts.append(f"Focus could not be captured on {len(unfocused)} more (keyboard focus never landed, so their readings are left out): {', '.join(unfocused)}.")
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. Glue's ring is a box-shadow, not an outline. " + " ".join(parts))
W()
W("**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover) — nothing a real press would submit or open was ever pressed. A pressed filled button keeps the hover's #185abc fill and deepens the elevation (0 1px 2px / 0 2px 6px rgba(60,64,67)); pressed text links keep the faint brand wash (rgba(26,115,232,0.1)); the 5px `outline: auto` Chrome draws on forced :active is the forced-state artifact, not a page style.")
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
    main = f"content x {v['main']['x']}, {v['main']['w']} wide" if v["main"]["w"] else "content full width"
    return f"{main}; grid {cols} gap {g['colGap']}" if g else main


for page in ["home", "certificates", "cert-ux", "ai", "stories", "mission"]:
    W(f"| {page} | " + " | ".join(grid_of(f"{page}@{w}") for w in (1440, 1920, 1024, 390)) + " |")
W()
W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
# PRODUCT (adapt): the card-like components to compare in one table.
for k in ["promo-banner", "video-teaser", "card", "card-link", "mega-panel", "tab-bar", "cert-card", "cert-hero", "badge-card", "expansion-panel", "ai-card", "footer"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if measured(s)), None)
    if st is None:
        continue
    p = props(st)
    # Borrow the look from a painted child only when it covers (nearly) the whole root box, so a
    # CTA or badge inside a transparent card never stands in for the card.
    big = [x for x in st.get("paint") or [] if x.get("bg") and x.get("radius") and covers(x, st)]
    if ("radius" not in p or p["background"] == "transparent") and big:
        p0 = big[0]
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
W(f"{len(icons)} SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Photography and certificate artwork were left out; these are the interface icons. The SVGs are Google's property, kept for reference only.")
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
W("- **Enrolment.** Every 'Get started on Coursera' CTA leads to coursera.org — measured in every state, never followed; no course was enrolled in or previewed past grow.google's own pages.")
W("- **Accounts.** grow.google itself has no sign-in (the program pages are fully public); the Google-account and Coursera surfaces its links reach are off-product and were never visited.")
W("- **The hero video.** The teaser opens a Glue modal with a YouTube embed — captured open and closed; the video was never played, so the player controls are not captured.")
W("- **The regional split.** `/` with a real user agent or locale 302s to `/intl/<locale>/` (here, `/intl/ALL_sg/` — the Singapore/global-English edition with a different promo and fewer sections); the package's canonical surface is the US edition bare contexts receive, and the APAC shots are kept as variant evidence, not a second token surface.")
W("- **Other certificate detail pages.** /certificates/data-analytics/ and /certificates/ai-essentials/ share the same template; two were captured whole, the rest are catalog cards.")
W("- **Outbound resources.** The links to grow.google's YouTube channel, the Google for Employers and social marks leave the product; they were never followed.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing; the `outline: auto` ring in a pressed state is Chrome's forced-pseudo artifact, not a page style.")
W("- **Disabled states** were not seen on any public control — the site has no forms to disable.")
W("- **Hover** is a real pointer hover; a handful of controls (the footer links, the mega-menu items) change nothing measurable and read 'same'.")
W()
W("### Themes")
W()
W("grow.google paints light only: no theme control exists in the header, footer or any menu, `prefers-color-scheme: dark` repaints nothing the probe saw, and the stylesheets declare no dark block beyond the glue ramps. The certificate pages' dark hero (`#18191d`) is a section paint — an editorial band, not a theme — and is kept inside the light set as `color.surface.dark`; no dark tokens were inferred from it. The token file therefore ships no dark set.")
W()
W("### Fonts")
W()
W("- **Google Sans Flex** is the variable face (opsz 6-144, wght 100-1000) the whole site paints; the font sheet also requests Google Sans Text, Google Sans, Google Sans Display and Product Sans faces — declared evidence, the computed fontFamily is always the Flex stack.")
W("- The faces are served from fonts.googleapis.com; the style guide falls back to system sans when the variable face is unavailable.")
W()
W("### Screenshots")
W()
W("- Photos, portraits and certificate artwork are Google's content and appear only inside screenshots and crops.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files. Tall pages split `-full` shots into `.partN` tiles; each `.capture.json` sidecar records the clip.")
W()
W("### Content left out")
W()
W("- Video and animation frames are the one thing screenshots can't carry; the video modal's capture is the closed state plus the open frame.")
W("- No personal data was captured: every page was read signed out and no field was ever filled.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops,", len(icons), "icons")
