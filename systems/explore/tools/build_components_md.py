#!/usr/bin/env python3
"""Build components.md for the Explore (explore.family) design reference.

Reads raw/components-computed.json (every component and state, measured on the archived
2023-02-23 build replayed from the local Internet Archive mirror), tokens.json, screenshots/
and components/crops/, and writes components.md next to them. Every value is a cell of the
measurement file, condensed: colours are hex followed by the palette token whose value matches,
the font family is named once per value, and a state row shows only what differs from the first
state. Adapted from the Gauth kit's builder.

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


def focus_not_captured(v):
    """A state whose reading is not what its name says: a skipped one, or a focus-visible reading
    taken where keyboard focus never landed (kbFocus returned "focus failed") or where the element
    took focus but did not match :focus-visible. Its style is the element at rest, so it is left out
    of every table and tally and listed as focus that could not be captured (kit builder port)."""
    return bool(v.get("skipped")) or v.get("via") == "focus failed" or (v.get("focus") or {}).get("matches") is False


def measured(v):
    return "style" in v and not focus_not_captured(v)


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

PAGE_NAME = {"home": "home", "discover": "Discover", "login": "login", "register": "register",
             "forgot": "forgot password", "about": "about", "legal": "legal",
             "profile": "server-rendered profile", "mobile": "mobile"}

GROUP_INTRO = {
    "Auth forms": "The marketing chrome (fixed 60px grey header, E wordmark, Sign in + yellow \"Sign up free\") and the split auth screen: a community welcome over a darker `#717171` grey panel at the left, a ~424px form column at the right. Email/password fields are 8px-radius hairline inputs; all three submits (\"Log in\", \"Sign up\", \"Reset Password\") are the same full-width dark `#262626` button with 7px corners. Fields were focused and filled for measurement, then cleared; nothing was submitted.",
    "Home (marketing + feed)": "The signed-out home page: the LabilGrotesk-Medium positioning sentence over the grey hero with hairline feature tags, then a feed preview.",
    "Discover feed": "`/discover`: an intro line, a row of category pills (hairline idle, ink-bordered active) and the 3-up post grid, fed by the archived `/discover` API records. Some post media was not archived and renders as the grey placeholder.",
    "About / legal": "The /about marketing page (features, no-numbers, no-algorithms, portfolio/domain pitches, CTAs) and the Terms, Privacy and Conduct legal pages, plus the shared footer.",
    "Server-rendered profile": "Public profiles were server-rendered: these entries were measured on the archived SSR HTML for /malikafavre and /sawdust, replayed with JavaScript disabled so the SPA could not replace the server markup. Real names, post titles, avatars and gallery frames are archived data, shown as they appeared in February 2023.",
    "Mobile (390 wide)": "A few components as a phone draws them, at 390 x 844 at 2x: a 56px header, \"Sign up free\" only, the pill row and the full-width post cards.",
}

SHOTS = [
    ("home", "Home. Grey header and hero with the positioning sentence and feature tags, then the feed preview.", "/"),
    ("discover", "Discover. Intro line, category pills and the 3-up post grid from the archived feed API.", "/discover"),
    ("login", "Login. The split auth screen: welcome panel left, email/password + \"Log in\" submit right.", "/login"),
    ("register", "Register. Same split with the newsletter checkbox, the terms/privacy line and the dark \"Sign up\" submit.", "/register"),
    ("forgot-password", "Forgot password. Intro copy, the email field and the reset submit.", "/forgot-password"),
    ("about", "About. The marketing pitch: features, \"no numbers\", \"no algorithms\", portfolio and domain CTAs.", "/about"),
    ("terms", "Terms of Service, effective 2022-09-27.", "/terms"),
    ("privacy", "Privacy Policy, effective 2022-09-27.", "/privacy"),
    ("conduct", "Code of Conduct. Its illustration was not archived and renders absent.", "/conduct"),
    ("announcement", "The June 2023 closure announcement shell (2023-06-08 snapshot): the product closed on 2023-04-19.", "/"),
    ("profile-shell", "A member profile as the SPA renders it signed out: the shell only, because the member API records were never archived.", "/sawdust"),
    ("post-shell", "A post permalink as the SPA renders it: the shell only, same missing-API reason.", "/p/2193"),
    ("ssr-profile-malika", "Malika Favre's profile from the archived server-rendered HTML, replayed with JavaScript disabled.", "/malikafavre"),
    ("ssr-profile-sawdust", "Sawdust's profile, same server-rendered evidence.", "/sawdust"),
]
MOBILE = [
    ("mobile-home", "Home at 390: the 56px header, \"Sign up free\" only, hero and feed.", "/"),
    ("mobile-discover", "Discover at 390: pill row and full-width post cards.", "/discover"),
    ("mobile-login", "Login at 390.", "/login"),
    ("mobile-register", "Register at 390.", "/register"),
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

W("# Explore components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured on {J['_meta']['read']} by replaying the archived 2023-02-23 explore.family build from a local Internet Archive mirror (the product closed 2023-04-19 and the domain later lapsed), signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent or uploaded.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The mined stylesheet is [raw/css-declarations.json](raw/css-declarations.json).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `UntitledSans 14/20 400, #262626`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the replayed page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (Explore shows one fixed light theme signed out). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).")
W()
W("| Surface | URL | Screenshots |")
W("|---|---|---|")
for p, desc, url in SHOTS + MOBILE:
    W(f"| {desc} | `{url}` | {links(p)} |")
W()
W("### Archive boundaries")
W()
W("| Surface | What was reached | Captured |")
W("|---|---|---|")
OVER = [
    ("SPA profile `/sawdust`", "the app shell only: the `/user/*` API records were never archived, so the router renders an unauthenticated empty state", "[profile-shell-light-default](screenshots/profile-shell-light-default.png)"),
    ("SPA post `/p/2193`", "the app shell only: `/post/single/*` was never archived", "[post-shell-light-default](screenshots/post-shell-light-default.png)"),
    ("Server-rendered profiles", "the archived SSR HTML for /malikafavre, /sawdust and /burnttoast, replayed with JavaScript disabled", "[ssr-profile-malika-light-default](screenshots/ssr-profile-malika-light-default.png), [ssr-profile-sawdust-light-default](screenshots/ssr-profile-sawdust-light-default.png)"),
    ("Closure announcement", "the 2023-06-08 archive snapshot of the signed-out shell after the 2023-04-19 shutdown", "[announcement-light-default](screenshots/announcement-light-default.png)"),
    ("Missing media", "grey placeholders where MP4/GIF/WebP uploads were not archived; misses are recorded per capture in the `.capture.json` sidecars", "[discover-light-full](screenshots/discover-light-full.png)"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement files.")
W()
foc, failed = [], []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st:
        continue
    if focus_not_captured(st):
        # Keyboard focus never landed on the element, so this record is the
        # unfocused style, not an observed focus look: a capture gap.
        failed.append(k)
        continue
    if "style" not in st:
        continue  # an error record (the focus attempt threw, no earlier reading): nothing to report
    s = st["style"]
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0
    foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else None))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} draw a ring: {', '.join(with_ring) if with_ring else 'none'}. The other {len(without)} draw none, so a keyboard user sees no change: {', '.join(without) if without else 'none'}."
  + (f" Focus could not be moved onto {len(failed)} controls — {', '.join(f'`{k}`' for k in failed)} — so their focus appearance is a capture gap, not a measurement." if failed else ""))
W()
W("**Pressed.** Explore's controls do not redraw on press; the measured `pressed` states match their defaults, so the entries read \"same\". Hovers recolour text and borders over the shared 0.2s transition rather than repainting backgrounds.")
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
W("**Layout.** The fixed header is 60px (56px at 390) at z-index 300; content sits in a 1640px-max column with 20px gutters. The feed lays its cards out at `calc(33.3333% - .5px)` wide with 15px side padding and a 50px row pitch on the white page; at 390 each card is full width. A fixed alert tray sits bottom-left at z-index 2000.")
W()
W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
# PRODUCT (adapt): the card-like components to compare in one table.
for k in ["post-card", "auth-panel", "feature", "field-email", "login-submit", "reg-submit", "pill", "hero-tag-cta", "ssr-post", "m-post", "footer"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if measured(s)), None)
    if st is None:
        continue
    p = props(st)
    if ("radius" not in p or p["background"] == "transparent") and st.get("paint"):
        # The root paints nothing: describe the largest painted descendant,
        # naming the node, instead of letting the first filled child pose as
        # the component (the post card's PRO badge is not the card).
        def area(x):
            dims = [float(n) for n in re.findall(r"[\d.]+", x.get("size", ""))[:2]]
            return dims[0] * dims[1] if len(dims) == 2 else 0
        cands = [x for x in st["paint"]
                 if (x.get("bg") and x["bg"] != "rgba(0, 0, 0, 0)") or x.get("bgImage") or x.get("border")]
        p0 = max(cands, key=area) if cands else None
        if p0:
            p = dict(p)
            if p.get("background") in (None, "transparent") and p0.get("bg"):
                p["background"] = f"{colour(p0['bg'])} ({p0['node']})"
            if "radius" not in p and p0.get("radius"):
                p["radius"] = f"{p0['radius']} ({p0['node']})"
            if "border" not in p and p0.get("border"):
                p["border"] = f"{colour(p0['border'].split(' | ')[0][2:])} ({p0['node']})"
            if p.get("shadow", "none") == "none" and p0.get("shadow"):
                p["shadow"] = f"{colour(p0['shadow'], tokens=False)} ({p0['node']})"
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
W("Explore's interface icons (the wordmark, appreciate/comment/save glyphs, the carousel arrows, the password eye) are inline SVGs drawn by the compiled Vue bundle and were not lifted into `icons/` this pass; the catalog records the gap. They are visible inside the crops and screenshots.")

# ------------------------------------------------ gaps
W()
W("## Gaps")
W()
W("### Pages")
W()
W("- **Everything signed in.** The member app (network feed, notifications, saved posts, subscriptions, the post composer, settings) lived behind sign-in, and its API was never archived besides. The signed-out `/sawdust` and `/p/2193` shells in the discovery list are the honest boundary.")
W("- **Archive misses.** Some post videos, GIFs, WebPs and profile media were never archived and render as the grey placeholder; `/img/code-of-conduct.ddc79720.png` is missing so the Conduct page shows no illustration. Per-capture misses are listed in each screenshot's `.capture.json` sidecar.")
W("- **Anything that sends or creates.** No form was submitted, no account created, nothing posted, appreciated, saved or purchased; the PRO/subscribe plans were reached only as links.")
W("- **Reset-password.** `/reset-password/{id}/{code}` needs a live token; the route exists in the bundle but was never reachable, so only `/forgot-password` was measured.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Disabled and validation states** were not seen on any public control; error alerts exist in the CSS (`alert--visible`) but never fired without a submit.")
W()
W("### Themes")
W()
W("Explore shows one fixed light theme on every public surface: no `prefers-color-scheme` rule exists in the compiled stylesheet and nothing on a signed-out page toggles a theme. Member portfolios had a dark presentation theme in the app's marketing, but it lived behind sign-in and was never captured, so the token file ships a single `light` set.")
W()
W("### Fonts")
W()
W("- **UntitledSans** and **UntitledSansMedium** (Klim Type Foundry) carry the UI; they are proprietary served faces, so the style guide falls back to system sans.")
W("- **LabilGrotesk-Medium** (Kometa Typefaces) draws the hero sentence, section titles and the wordmark; also proprietary.")
W()
W("### Screenshots")
W()
W("- Post images and profile media are members' and Explore's content and appear only inside screenshots and crops.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Member-generated content (post bodies, comments, profile bios beyond the SSR markup) was never archived or was not transcribed; only the interface around it was measured.")
W("- No personal data was captured: the pages were read signed out, and the names and works visible in the SSR profiles are public archive records reproduced as captured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops")
