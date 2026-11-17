#!/usr/bin/env python3
"""Build components.md for the Hitchd design reference.

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

PAGE_NAME = {
    "https://www.hitchd.com/": "home",
    "https://www.hitchd.com/login": "login",
    "https://www.hitchd.com/signup": "signup",
    "https://www.hitchd.com/forgot-password": "forgot-password",
    "https://www.hitchd.com/blog": "blog index",
    "https://www.hitchd.com/blog/what-is-a-honeymoon-registry": "blog post",
    "https://www.hitchd.com/terms": "terms",
    "https://www.hitchd.com/zoeandnoah": "demo registry",
    "https://www.hitchd.com/zoeandnoah/<gift-slug>": "demo registry",
}

GROUP_INTRO = {
    "Chrome": "The page furniture: the marketing header over the home hero, the full-width closure announcement strip, the footer, and the registry's own top bar with its #hashtag link and Try It Free call to action.",
    "Type": "Hitchd's voice is a hairline serif for marketing display (DDNR, weight 100) over Inter Variable for everything else; the registry couples' names set in the app's own display face (`classic` on the demo). Each surface sets its own scale — the registry's hero runs to 96px.",
    "Cards": "The gift tiles of the registry grid, a blog index row, and the auth form's container.",
    "Forms": "The couple app's auth surfaces — /login, /signup and /forgot-password — read at rest. Nothing was focused, typed or submitted.",
    "Controls": "The registry's Sort by filter select and the phone's .mobile-menu drawer — present on the demo registry but never opened for a guest.",
    "Dialogs": "The gift modal: a gift card's own tap navigates to /<registry>/<gift-slug> and the guest app draws the modal over the list. Read at rest; the Give/contribute flow was never entered.",
    "Boundaries": "Routes that a signed-out guest cannot reach: the registry's internal pages each bounce back to /.",
}

SHOTS = [
    ("home", "Home. The closure announcement strip, the hairline-serif hero (\"Tie the knot, without tangles.\"), marketing sections, footer. Full page captured.", "/"),
    ("login", "Log in. The auth card at rest: email field, password field, disabled Continue, forgot-password and sign-up links.", "/login"),
    ("signup", "Sign up. The same auth shell at rest; nothing typed or submitted.", "/signup"),
    ("forgot-password", "Forgot password. The reset form at rest.", "/forgot-password"),
    ("blog", "Blog index. Article rows; the page is ~50,000px tall, so only the viewport is captured — see Gaps.", "/blog"),
    ("post", "Blog post. A full article (\"What is a honeymoon registry?\").", "/blog/what-is-a-honeymoon-registry"),
    ("terms", "Terms of service. Prose page.", "/terms"),
    ("privacy", "Privacy policy. Prose page.", "/privacy"),
    ("trips", "Destination landing (/trips/australia).", "/trips/australia"),
    ("guide", "Guide page (\"Add Hitchd to a Knot wedding website\").", "/guides/add-hitchd-to-knot-wedding-webiste"),
    ("registry", "The public demo registry (/zoeandnoah): hero with the couple's names, Sort by filter, gift grid, footer; the filter's opened and filtered states and a gift modal.", "/zoeandnoah"),
    ("coming-soon", "A not-yet-live registry (/avaandbenjamin) — its public countdown page.", "/avaandbenjamin"),
]
MOBILE = [
    ("mobile-home", "Home at 390: announcement strip, hero, full page.", "/"),
    ("mobile-login", "Log in at 390.", "/login"),
    ("mobile-blog", "Blog index at 390.", "/blog"),
    ("mobile-post", "Blog post at 390.", "/blog/what-is-a-honeymoon-registry"),
    ("mobile-registry", "Demo registry at 390.", "/zoeandnoah"),
    ("mobile-coming-soon", "Countdown registry at 390.", "/avaandbenjamin"),
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

W("# Hitchd components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from www.hitchd.com on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the mobile entries at 390 x 844), with computed styles read from the running page. Nothing was signed into, paid, sent or submitted.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [raw/layout.json](raw/layout.json).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter Variable 16/24 400, #111212`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png` (Hitchd has one theme — no dark variant or theme switch exists anywhere on the surveyed pages). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x, stitched from tiles when a page is taller than one GPU texture; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).")
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
    ("Sort by filter, opened", "demo registry", "the filter select's own click", "[registry-light-sort-open](screenshots/registry-light-sort-open.png), [sort-filter](#sort-filter)"),
    ("Filtered list (\"Still needed\")", "demo registry", "an option chosen in the filter select; the list re-filters, nothing is submitted", "[registry-light-filter-still-needed](screenshots/registry-light-filter-still-needed.png)"),
    ("Gift modal", "demo registry", "a gift card's own tap navigates to /<registry>/<gift-slug> and the app draws the modal; read at rest, Give never pressed", "[registry-light-gift-modal](screenshots/registry-light-gift-modal.png), [gift-modal](#gift-modal)"),
    ("Mobile menu", "demo registry at 390", "the .mobile-menu drawer exists on the page (with registry-owner links) but no guest-facing control opens it — it stays hidden, so it was measured at rest rather than captured open", "[mobile-menu](#mobile-menu)"),
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
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st or "style" not in st:
        continue
    s = st["style"]
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0
    foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else None))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
if foc:
    W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {len(with_ring)} draw a ring: {', '.join(with_ring)}. The other {len(without)} draw none: {', '.join(without)}.")
else:
    W("**Focus and pressed.** Components were read at rest — Hitchd's auth forms were never focused (that would mean typing toward a sign-in), so focus-ring and pressed evidence is a documented gap rather than a measurement.")
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
W("**Layout.** Read on each page at each width ([raw/layout.json](raw/layout.json)): the page's full height, its widest Foundation `.row` content band, and the fixed/sticky layers it carries.")
W()
W("| Page | 1440 x 900 | 390 x 844 |")
W("|---|---|---|")


def layout_of(key):
    v = LAYOUT["pages"].get(key)
    if not v or "error" in v or "blocked" in v:
        return "-"
    rows = [g for g in v.get("grids", []) if g.get("rect", {}).get("w", 0) > 0]
    widest = max(rows, key=lambda g: g["rect"]["w"], default=None)
    band = f"widest band {num(widest['rect']['w'])}px" if widest else "no band found"
    cols = f", cols {widest['columns'][:60]}" if widest and widest.get("columns") else ""
    fixed = len(v.get("fixed", []))
    return f"page {num(v.get('scrollHeight', 0))}px tall, {band}{cols}, {fixed} fixed/sticky"


for label in ["home", "login", "signup", "forgot-password", "blog", "post", "terms", "privacy", "trips", "guide", "registry"]:
    W(f"| {label} | {layout_of(label + '@desktop')} | {layout_of(label + '@mobile')} |")
W()
W("**Card shapes.** Default-state values for each component's own container part; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
# Each row reads the component's own named part — never a descendant's paint,
# which would mix parts (a heading's height, a small button's radius, a
# disabled pill's fill) into the card's shape.
SHAPE_PART = {"gift-card": "card", "mobile-gift-card": "card", "blog-card": "card", "auth-layout": "card", "gift-modal": "modal"}
for k in ["gift-card", "mobile-gift-card", "blog-card", "auth-layout", "gift-modal"]:
    c = C.get(k)
    if not c or c.get("missing"):
        continue
    st = c["states"].get(SHAPE_PART[k])
    if not st or "style" not in st:
        st = next((s for s in c["states"].values() if "style" in s), None)
    if st is None:
        continue
    p = props(st)
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
        W(f"{desc + ' ' if desc else ''}Read as `{k}` on the {where} page.")
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
n_lifted = len([r for r in icons if r[0] != "linked"])
n_linked = len([r for r in icons if r[0] == "linked"])
W(f"{n_lifted} distinct inline SVG{'s were' if n_lifted != 1 else ' was'} lifted from the pages into [icons/](icons), and {n_linked} linked SVG references were indexed, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Hitchd's icons carry no name in the DOM, so glyphs are filed by geometry hash under `unnamed/`; the wordmark itself is a linked SVG (`/marketing/images/hitchd-home-brand-logo.svg`), recorded in the index but not vendored. The SVGs are Hitchd's property, kept for reference only.")
W()
W("| Icon | Rendered size | Seen on | Context |")
W("|---|---|---|---|")
for r in icons:
    f, name, wh, seen, ctx = (r + [""] * 5)[:5]
    label_name = name or ("`linked`" if f == "linked" else f)
    if f == "linked":
        W(f"| linked svg — {wh} | — | {seen} |")
        continue
    W(f"| [{name or f}](icons/{f}) | {wh} | {seen} | {ctx.replace('|', '/')[:60]} |")
W()

# ------------------------------------------------ gaps
W("## Gaps")
W()
W("### Pages")
W()
W("- **Signed-in pages.** Nothing behind sign-in was captured: the couple dashboard, the registry editor, guest lists, contribution management, payout/payment settings and account settings. The kit never signs in.")
W("- **Anything that pays or submits.** No contribution or gift purchase was started: the gift modal's Give button and everything behind it (amounts, card details, checkout) is unmeasured by policy. No auth form was typed into or submitted, no password-reset or sign-up sent.")
W("- **Registry internal routes.** `/zoeandnoah/contributions`, `/payment-methods`, `/ask` and `/quick-thanks` each bounce the signed-out guest back to `/` (measured in `internal-route-bounces`); those views belong to the couple's live registry, not the demo.")
W("- **Redirected marketing routes.** `/how-it-works`, `/about`, `/pricing`, `/press-kit`, `/zola-alternative`, `/honeyfund-alternative`, `/travelersjoy-alternative`, `/referrals` and `/honeymoon-registry` all redirect to `/` — Hitchd announced it is closing on 31 December 2026 and is not accepting new customers, so those pages no longer exist to capture.")
W("- **Blog index, full page.** `/blog` is ~50,000px of article rows; the tiled full-page screenshot exceeded the capture timeout and was abandoned. The viewport shot stands; the truncation is the documented boundary, not a missing capture.")
W()
W("### States")
W()
W("- **Focus, hover and pressed** were not forced on the auth controls (focusing a field is the first step of signing in) and are a documented gap; the registry's filter and modal states that a guest can reach at rest are captured.")
W("- **The gift modal's later steps** (amount entry, payment method, confirmation) were never entered.")
W("- **The registry's signed-in owner view** and the couple-facing menu items (Log out, Quick Thanks) are not guest surfaces.")
W()
W("### Themes")
W()
W("Hitchd shows one light theme. No stylesheet, page or app surveyed declares a dark variant, no page sets a theme attribute, and no theme switch exists on the marketing pages, the auth app or the registry app. The token file therefore ships a single light set and no dark evidence exists to label.")
W()
W("### Fonts")
W()
W("- **DDNR** (the display serif) and **Inter Variable** are the marketing stack's self-hosted woff2 faces, declared in `/marketing/css/styles.min.css`; the style guide links to them rather than vendoring them.")
W("- The registry app loads its own display faces so each couple can theme their registry — the demo registry's heading is set in **classic**, one of ~20 registry font names (@font-face families named classic, clean, dramatic, editorial, elegant, romantic…) in the guest app's styles, alongside Google-served faces (EB Garamond, Roboto Flex, Noto Sans Display…).")
W("- The auth app and registry app otherwise set the same **Inter Variable** body stack as marketing.")
W()
W("### Screenshots")
W()
W("- Gift photography and registry images are Hitchd's or the couples' content and appear only inside screenshots and crops; remote asset URLs (the registry's CDN image URLs) were never written to a committed file — `url(…)` appears in their place in the raw readings.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- The public demo registry shows real gift data for a sample couple; only the interface was measured, not the catalogue's full contents.")
W("- No personal data was captured beyond the public names and registry content the demo itself publishes.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops,", len(icons), "icons")
