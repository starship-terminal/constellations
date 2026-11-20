#!/usr/bin/env python3
"""Build components.md for the Jasper design reference.

Reads raw/components-computed.json (every component and state, measured),
tokens.json and screenshots/, and writes components.md next to them. Every value
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
for n, t in flat(T["core"].get("color", T["core"].get("palette", {}))):
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

PAGE_NAME = {"home": "Home", "platform": "Platform", "pricing": "Pricing", "brand": "Brand", "demo": "Demo", "signin": "Login", "mobile": "Mobile home"}

GROUP_INTRO = {
    "Shell and navigation": "The sticky marketing nav: a red wordmark, text menu items, Log in, Free Trial and a navy Get a Demo button.",
    "Home hero": "The light-blue hero: a Feature display headline, a red New chip, and two actions (navy Get a Demo, outlined Start Free Trial).",
    "Home": "Home sections below the hero: Feature headings and content cards.",
    "Pricing": "The pricing comparison chart: plan columns and their actions. Nothing was checked out.",
    "Brand page": "The public brand page, with logo downloads. Measured, never downloaded.",
    "Demo form boundary": "The Get a Demo HubSpot form, measured at rest. Nothing was typed or submitted.",
    "App login boundary": "The app.jasper.ai login column. The boundary before the product. Never filled, never submitted, no OAuth followed.",
    "Footer": "The site footer: link columns and legal.",
    "Mobile (390 wide)": "The same marketing page at 390 x 844, with the menu toggle.",
}

SHOTS = [
    ("home", "Home. Red wordmark, navy nav, light-blue hero, product sections, footer.", "/"),
    ("platform", "Platform overview.", "/platform"),
    ("agents", "Agents library.", "/agents"),
    ("pricing", "Pricing comparison chart.", "/pricing"),
    ("brand", "Public brand page and logo downloads.", "/brand"),
    ("blog", "Blog index.", "/blog"),
    ("company", "Company page.", "/company"),
    ("legal", "Legal index.", "/legal"),
    ("demo", "Get a Demo form, at rest. Nothing submitted.", "/demo"),
    ("signin", "app.jasper.ai login card, at rest. Nothing submitted.", "https://app.jasper.ai/auth/login"),
]
MOBILE = [
    ("mobile-home", "Home at 390, including the menu toggle state.", "/"),
    ("mobile-pricing", "Pricing at 390.", "/pricing"),
    ("mobile-signin", "Login card at 390.", "https://app.jasper.ai/auth/login"),
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
icons = []

W("# Jasper components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from www.jasper.ai on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, submitted or purchased.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).")
W()
W("| Surface | URL | Screenshots |")
W("|---|---|---|")
for p, desc, url in SHOTS + MOBILE:
    W(f"| {desc} | `{url}` | {links(p)} |")
W()
W("### Overlays and transient states")
W()
W("Consent overlays (`#cookieBanner`, `#transcend-consent-manager`) and the Qualified chat host were hidden and never clicked. The Platform mega-menu was opened by hover. The demo form and the login card were left at rest.")
W()
W("## Entries")
OVER = []
if False:
    OVER = [
    ("unused", "unused", "unused", "unused"),
    ("Create a Course dialog", "Academy", "Create Course pressed (opens the dialog); a prompt typed and deleted, no suggestion pressed", "[academy-my-light-create-dialog](screenshots/academy-my-light-create-dialog.png), [create-a-course-dialog](#create-a-course-dialog)"),
    ("Enable audio dialog", "science lesson", "on load; Not now pressed, Enable audio never pressed", "[lesson-science-light-audio-dialog](screenshots/lesson-science-light-audio-dialog.png)"),
    ("Audio gate", "math lesson", "on load; Continue pressed to start playback", "[lesson-math-light-audio-gate](screenshots/lesson-math-light-audio-gate.png)"),
    ("Settings popover", "science lesson", "the lesson's Settings button", "[lesson-science-light-settings](screenshots/lesson-science-light-settings.png)"),
    ("Ask Tutor, opened", "science lesson", "clicked into the bar; sample text typed and deleted, nothing sent", "[lesson-science-light-ask-tutor](screenshots/lesson-science-light-ask-tutor.png)"),
    ("Quiz", "science lesson", "reached by letting the lesson play about three minutes; no option chosen", "[lesson-science-light-quiz](screenshots/lesson-science-light-quiz.png)"),
    ("Chapters panel", "math and history lessons", "the chapters button", "[lesson-math-light-chapters](screenshots/lesson-math-light-chapters.png), [lesson-history-light-chapters](screenshots/lesson-history-light-chapters.png)"),
    ("Show more", "Math Curriculum", "the Show 14 more button", "[academy-math-light-show-more](screenshots/academy-math-light-show-more.png)"),
    ("Folded sidebar", "Homework home", "the sidebar's collapse button", "[home-light-sidebar-folded](screenshots/home-light-sidebar-folded.png)"),
    ("Story preview", "Atlas", "a story card pressed (opens a video preview)", "[atlas-light-story-preview](screenshots/atlas-light-story-preview.png)"),
    ("Story page", "Atlas", "Explore in the preview (opens the published story)", "[atlas-light-story](screenshots/atlas-light-story.png), [mobile-atlas-light-story](screenshots/mobile-atlas-light-story.png)"),
    ("Video Settings popover", "Atlas story", "hovering Generate Video; nothing in it pressed", "[atlas-light-story-video-settings](screenshots/atlas-light-story-video-settings.png)"),
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
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} draw a ring: {', '.join(with_ring) or 'none'}. The other {len(without)} draw none: {', '.join(without) or 'none'}.")
if no_focus:
    W(f"Focus could not be captured on {len(no_focus)}: keyboard focus never reached them (or they took focus without matching :focus-visible), so their focus look is unknown, not absent: {', '.join(f'`{k}`' for k in no_focus)}.")
W()
W("**Pressed.** Pressed was forced with DevTools `:active:hover` on the measured controls. Read the state row for the colour change. Jasper's primary button moves from flame `#fa4028` to `#801a10` on hover.")
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
W("**Layout.** Desktop captures are 1440 x 900. Phone captures are 390 CSS px at 2x. Content width on the home hero is 840px inside a 1320px section.")
if False:
    W("| Page | 1440 | 1920 | 1024 | 390 |")
    W("|---|---|---|---|---|")


def grid_of(key):
    return "-"


if False:
    for page in []:
        W(f"| {page} | " + " | ".join(grid_of(f"{page}@{w}") for w in (1440, 1920, 1024, 390)) + " |")
W()
W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
# PRODUCT (adapt): the card-like components to compare in one table.
for k in ["card", "demo-card", "price-card", "nav-dropdown", "footer"]:
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

# ------------------------------------------------ gaps
W()
W("## Icons")
W()
W("No standalone SVG icon set was lifted. The wordmark and the illustrated mega-menu art are Jasper's artwork and stay in the screenshots and crops. `icons/` is declared as a layout gap.")
W()
W("## Gaps")
W()
W("### Pages")
W()
W("- **Product app.** The canvas, agents runtime, Brand IQ editor and campaigns sit behind `https://app.jasper.ai/`. The login card at `https://app.jasper.ai/auth/login` was measured at rest. Google OAuth was not followed. Nothing was submitted.")
W("- **Signup.** `https://app.jasper.ai/auth/signup` was not followed.")
W("- **Demo form.** `https://www.jasper.ai/demo` was measured at rest and never submitted.")
W("- **Help center.** `https://help.jasper.ai/` was not captured.")
W("- **Phone menu.** At 390 the desktop `.nav_menu` is `display: none` and no hamburger mounts. The phone menu was not opened.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools `:active:hover`, so a script that only runs on a real pointer-down is missing.")
W("- **Disabled, loading and error** were not seen. Forms were not submitted.")
W("- **text-link and faq-item** were not on the pages when measured. Pricing has no FAQ accordion.")
W()
W("### Themes")
W()
W("The marketing pages paint light. `.u-theme-dark` rebinds background to `#262627` and text to `#ffffff` for dark islands (the footer). There is no page-wide theme switch, so no dark page screenshot was taken. The dark set in [tokens.json](tokens.json) is that declared rebinding.")
W()
W("### Fonts")
W()
W("- **ABC ROM** is the UI face. **Feature** is the display face. **ABC ROM Mono** is the mono face. The files are commercial and are not in this package. Inter is also declared on the Webflow sheet and is not the marketing UI face.")
W()
W("### Screenshots")
W()
W("- Illustrations, customer logos and the wordmark are Jasper's content and appear only inside screenshots and crops.")
W("- Screenshots are stored as 256-colour PNGs. Read exact colours from the tokens or the raw files.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops,", len(icons), "icons")
