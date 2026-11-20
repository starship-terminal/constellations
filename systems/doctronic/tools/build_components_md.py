#!/usr/bin/env python3
"""Build components.md for the Doctronic design reference.

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
LAYOUT = {}
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
    # Painted layers that carry a state but not the root box: the element's own
    # ::before/::after always, and descendant paint only when the root paints
    # nothing (the case "Child layers" reports). A nav underline that goes
    # transparent -> black on hover lives in a::after, so it diffs here.
    bits = []
    for pe in ("::before", "::after"):
        if v.get(pe):
            p = v[pe]
            bits.append(" ".join(x for x in (pe, p.get("backgroundColor"), p.get("borderTopWidth"), p.get("boxShadow"), p.get("opacity")) if x))
    # A root box-shadow (e.g. the 1px focus ring gained on focus-visible) does
    # not remove the painted children: keep reporting their layers, which is
    # where a state-carrying child outline (the 3px cyan CTA ring) shows up.
    if s["backgroundColor"] == "rgba(0, 0, 0, 0)" and s["borderTopWidth"] == "0px" and s["backgroundImage"] == "none":
        for p in v.get("paint", [])[:6]:
            bits.append(" ".join(x for x in (p["node"], p.get("size"), p.get("bg"), p.get("border"), p.get("shadow"), p.get("outline"), p.get("radius")) if x))
    if bits:
        o["layers"] = "; ".join(bits)[:400]
    return o


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "outline", "text", "transition", "transform", "opacity", "icon", "placeholder", "layers"]


def focus_not_captured(v):
    """A state whose reading is not what its name says: a skipped one, or a focus-visible reading
    taken where keyboard focus never landed (kbFocus returned "focus failed") or where the element
    took focus but did not match :focus-visible. Its style is the element at rest, so it is left out
    of every table and tally and listed as "focus could not be captured"."""
    return bool(v.get("skipped")) or v.get("via") == "focus failed" or (v.get("focus") or {}).get("matches") is False


def measured(v):
    return "style" in v and not focus_not_captured(v)


def visible(colour_value):
    """False for a fully transparent colour: a `2px solid transparent` outline draws nothing."""
    return not re.search(r"rgba\(\d+, \d+, \d+, 0\)|transparent|/ 0\)", colour_value)


def state_rows(c):
    # A state whose capture failed (e.g. via: "focus failed" — the element would
    # not hold a real keyboard focus) is not a captured state: it is reported
    # separately so a failed attempt can never read as a measured absence of a
    # focus ring.
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
        bits = [re.sub(r"\..*$", "", p["node"]) if "::" not in p["node"] else p["node"].split(".")[0], re.sub(r"\.0+(?=x|px|$)", "", p["size"])]
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

PAGE_NAME = {"home": "home", "chat": "/chat/", "signin": "home (the ?modal=signin URL)", "symptom": "symptom checker",
             "blog": "blog", "telehealth": "telehealth", "authors": "authors", "resource": "resource center",
             "wall": "Wall of Love", "dark": "home in dark theme", "mobile": "home"}

GROUP_INTRO = {
    "Shell and navigation": "The 72px marketing top bar over the home page: the wordmark, Log in, the solid Sign up pill and the button that opens the site-menu drawer, plus the drawer itself. (The content pages carry a different, shorter sage bar with pill links and the dark Try Doctronic For Free CTA — see the Marketing and content pages group.)",
    "Home: hero and marketing": "The home hero with the Fraunces display greeting, the raised chat input card with its animated accent border and the accent Start chat button, the suggestion chips, then the marketing sections — feature cards, pricing, testimonials, the Hippocratic oath band and the footer.",
    "Chat surface": "The signed-out /chat/ surface: the collapsible left rail (New chat highlighted, Sign up for free and Log in pinned at the bottom), the centered empty-state greeting, the large input card with the Send control and the starter chips. Nothing was sent.",
    "Symptom checker": "The /symptom-checker/ entry point: the Fraunces headline, the symptoms textarea card and the Check My Symptoms action. Measured, never submitted.",
    "Marketing and content pages": "The Tailwind-utility content surface — the same pill-link top bar and dark CTA on /blog/, /telehealth/, /authors/, /resource-center/ and /wall-of-love/ — with its own literal hex values alongside the token layer.",
    "Dialogs and overlays": "The sign-in card reached by the public ?modal=signin URL: a centered raised dialog over a dimmed page with email and OAuth actions. Everything inside was measured, never pressed.",
    'Dark theme (data-theme="dark")': "The home surface re-measured under the site's real dark theme — localStorage.theme=dark sets data-theme on <html>, which redeclares the semantic colour roles and the focus ring.",
    "Mobile (390 wide)": "The same surface at phone width: the top bar shrinks to wordmark + actions + menu, and the chat rail collapses into a mobile header.",
}

SHOTS = [
    ("home", "Home", "/"),
    ("chat", "Chat (signed out)", "/chat/"),
    ("chat-signin", "Sign-in dialog", "/?modal=signin"),
    ("symptom-checker", "Symptom checker", "/symptom-checker/"),
    ("resource-center", "Resource center", "/resource-center/"),
    ("blog", "Blog", "/blog/"),
    ("telehealth", "Telehealth", "/telehealth/"),
    ("urology", "Urology (condition page)", "/urology/"),
    ("our-philosophy", "Our philosophy", "/our-philosophy/"),
    ("authors", "Authors", "/authors/"),
    ("careers", "Careers", "/careers/"),
    ("online-treatment", "Online treatment", "/online-treatment/"),
    ("prescription-glp-1", "GLP-1 prescriptions", "/prescription-glp-1/"),
    ("wall-of-love", "Wall of Love", "/wall-of-love/"),
    ("about", "About", "/about/"),
    ("privacy-policy", "Privacy policy", "/privacy-policy/"),
    ("partnerships", "Partnerships article", "/strategic-partnerships-driving-healthcare-innovation/"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "/"),
    ("mobile-chat", "Chat, phone", "/chat/"),
    ("mobile-symptom-checker", "Symptom checker, phone", "/symptom-checker/"),
    ("mobile-blog", "Blog, phone", "/blog/"),
]

# Entries whose committed reading is not the component the name says: the capture's `.or()`
# fallbacks are unions resolved in DOM order, so an earlier node won (README: What to distrust).
WRONG = {
    "nav-link": "The reading is the highlighted \"New chat\" row, the same node as `nav-link-current`, not a resting sidebar link.",
    "input-card": "The reading is the transparent 652 x 148 `.wrapper.chatInput`, not the painted `form` card.",
    "chat-hero": "The reading is the whole 1440 x 900 `main`, not the centred empty state.",
    "logo": "The reading is the 620 x 25 logo wrapper `div`, not the wordmark link.",
    "feature-card": "The reading is the testimonial `article` (the same card as `quote-card`), not a feature card.",
    "signin-dialog": "The reading is the transparent inner `section`, not the painted `div.modal` card.",
    "menu-item": "The reading is the \"About Chat\" expandable row, the same node as `menu-item-expand`, not a link row.",
}

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
icons = []

W("# Doctronic components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from www.doctronic.ai on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844, the Dark group on the site's real data-theme=\"dark\" theme), with computed styles read from the running page. Nothing was signed into, created, submitted or sent: the chat composer was given sample text that was deleted again, Send/Start chat and every sign-in action were never pressed.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [patterns.md](patterns.md).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{theme}-state.png`: the app surfaces (home, /chat/, the symptom checker, the resource center, the blog, telehealth and our-philosophy) were captured in both `light` and `dark`; the rest paint `light` only. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).")
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
    ("Site-menu drawer", "home, the menu button", "the header menu button's own toggle, closed with Escape", "[home-light-menu](screenshots/home-light-menu.png)"),
    ("Chat sidebar, expanded", "/chat/", "the rail's own Expand sidebar button", "[chat-light-sidebar](screenshots/chat-light-sidebar.png), [chat-sidebar-open](#chat-sidebar-expanded)"),
    ("Filled composer", "/chat/", "sample text typed into the textarea and deleted again; Send never pressed", "[chat-light-filled](screenshots/chat-light-filled.png), [chat-textarea](#chat-textarea)"),
    ("Sign-in dialog", "the ?modal=signin URL", "the public modal URL alone; nothing inside it was pressed", "[chat-signin-light-signin](screenshots/chat-signin-light-signin.png), [signin-dialog](#sign-in-dialog)"),
    ("Blog search", "/blog/", "sample text typed into the search field; search never submitted", "[blog-light-search](screenshots/blog-light-search.png)"),
    ("Cookie/consent and reCAPTCHA chrome", "every page", "hidden, never answered — the reCAPTCHA badge is Google's chrome, not the product's", "hidden before every shot and reading"),
    ("Everything behind Log in / Sign up", "the chat product, health record, prescriptions, appointments", "behind sign-in; the sign-in card was measured, never used", "boundary; see Gaps"),
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
    base = next((v["style"] for v in c["states"].values() if measured(v)), s)
    # A fully transparent outline paints nothing: a transparent outline must
    # not count as a painted ring.
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0 and s["outlineColor"] != "rgba(0, 0, 0, 0)"
    # A ring painted on a child layer instead of the wrapper counts as ringed
    # too — unless that outline is also transparent.
    child_ring = next((n["outline"] for n in st.get("paint", []) if n.get("outline") and "rgba(0, 0, 0, 0)" not in n["outline"]), None)
    shadow = s["boxShadow"] != base["boxShadow"] and s["boxShadow"] != "none"
    border = any(
        s[f"border{d}{p}"] != base[f"border{d}{p}"]
        for d in ("Top", "Right", "Bottom", "Left")
        for p in ("Color", "Width", "Style")
    )
    desc = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else (f"on a child: {child_ring}" if child_ring else None)
    foc.append((k, ring or bool(child_ring), shadow, border, desc))
with_ring = [f"`{k}` ({r})" for k, ring, sh, bd, r in foc if ring]
with_shadow = [f"`{k}`" for k, ring, sh, bd, r in foc if not ring and sh]
with_border = [f"`{k}`" for k, ring, sh, bd, r in foc if not ring and not sh and bd]
without = [f"`{k}`" for k, ring, sh, bd, r in foc if not ring and not sh and not bd]
parts = [f"{len(with_ring)} draw an outline ring: {', '.join(with_ring)}."]
if with_shadow:
    parts.append(f"{len(with_shadow)} draw a focus ring as a shadow instead: {', '.join(with_shadow)}.")
if with_border:
    parts.append(f"{len(with_border)} change only their border: {', '.join(with_border)}.")
if without:
    parts.append(f"The other {len(without)} show no measured change: {', '.join(without)}.")
if unfocused:
    parts.append(f"Focus could not be captured on {len(unfocused)} more (keyboard focus never landed on them, so their readings are left out): {', '.join(unfocused)}.")
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {' '.join(parts)}")
W()
W("**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.")
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
# PRODUCT (adapt): the card-like components to compare in one table.
for k in ["input-card", "hero-input-card", "feature-card", "pricing-card", "signin-dialog", "article-card", "author-card"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if measured(s)), None)
    if st is None:
        continue
    p = props(st)
    W(f"| [{c['title']}](#{re.sub(r'[^a-z0-9 -]', '', c['title'].lower()).replace(' ', '-')}) | {p['size']} | {p.get('border', '-')} | {p.get('radius', '-')} | {p.get('background', '-')} | {p.get('shadow', 'none')} | {p.get('padding', '0')} |")
W()

# ------------------------------------------------ entries
W("## Components")
groups = [g for g in GROUP_INTRO if any(c.get("group") == g for c in C.values())]
for c in C.values():
    if c.get("group") not in groups:
        groups.append(c.get("group") or "Other")
for g in groups:
    W()
    W(f"### {g}")
    W()
    W(GROUP_INTRO.get(g, ""))
    for k, c in C.items():
        if c.get("group") != g:
            continue
        W()
        W(f"#### {c['title']}")
        desc = (c.get("desc") or "").strip()
        if desc and not desc.endswith((".", ")", '"')):
            desc += "."
        where = PAGE_NAME.get(c["page"], c["page"])
        W(f"{desc + ' ' if desc else ''}Read as `{k}` on the {where} page{' at 390 wide' if g.startswith('Mobile') else ''}.")
        if k in WRONG:
            W()
            W(f"**Known wrong; recapture needed.** {WRONG[k]}")
        W()
        if c.get("missing"):
            W("Not on the page when it was captured.")
            continue
        failed = [s for s, v in c["states"].items() if focus_not_captured(v)]
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
        if failed:
            W(f"**Focus not capturable.** A real keyboard focus could not be held on this element ({', '.join(f'`{s}`' for s in failed)} recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.")
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Doctronic wordmark, the arrow/spark glyphs in buttons and chips, the Trustpilot stars and the testimonial artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.")
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
W("### The signed-in product")
W()
W("Everything behind Log in and Sign up — the chat product's real threads, the health record, prescriptions, appointments, account and billing — was never reached. The sign-in card was rendered from the public ?modal=signin URL and measured, and nothing inside it (email login, the OAuth buttons, Create an account) was pressed. What the authenticated app looks like or how it behaves is not documented here; the marketing pages' claims about it were never verified.")
W()
W("### Pages")
W()
W("- **Chat actions.** Start chat, Send message, Check My Symptoms, the suggestion chips, View recent chats and the Anonymous badge were measured, never pressed — each would start a session or submit text.")
W("- **Auth and sign-up actions.** Sign up, Sign up for free, Try Doctronic For Free, Log in, Log in with email, the OAuth buttons and Create an account were measured, never followed; no account was created.")
W("- **Medical record / prescription links** in the site-menu drawer and footers were left unfollowed where they lead to account surfaces.")
W("- **The mobile app's Open/App Store banner**, where it appears, was left untouched.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Disabled, error and loading states** were only seen where the page paints them at rest (the declared *-disabled tokens are in the token file); no form was submitted to provoke an error.")
W("- **The chat rail's signed-in content** (recent chats, history) only fills for a signed-in visitor; the rail was measured expanded in its signed-out state.")
W()
W("### Themes")
W()
W("doctronic.ai ships a real user-selectable dark theme: `localStorage.theme` is `light`, `dark` or `system`, an init script sets `data-theme` on `<html>` and the stylesheets redeclare the semantic `--color-*` roles and the focus ring under `[data-theme=\"dark\"]` (harvested in [raw/css-vars.json](raw/css-vars.json)). The app surfaces (home, /chat/, the symptom checker, resource center, blog, telehealth, our-philosophy) were captured in both themes; the darker content pages keep their light Tailwind paint under `data-theme=\"dark\"` — the utility classes carry literal hex, not theme vars — which the token file records honestly as a dark set scoped to the token-driven surfaces.")
W()
W("### Fonts")
W()
W("- **fraunces** (400/600, plus italics), **geist** (400/500/600) and **geistMono** (400/600) are self-hosted woff2 files declared in @font-face blocks in the Next.js chunks (the src list is in [raw/css-vars.json](raw/css-vars.json)). The style guide does not load them — they are the product's licensed faces — so its samples fall back to Georgia and the system sans.")
W("- **The plain body font** (`--font-body`) is the Apple system stack (SF Pro Text → Segoe UI → Roboto…), not a webfont.")
W()
W("### Screenshots")
W()
W("- The hero illustration, the testimonial photos, the condition-page imagery and the Doctronic wordmark in the screenshots are the product's published content; only frames and components were measured.")
W("- The invisible-reCAPTCHA badge is Google's chrome mounted over the page; it was hidden, never answered.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Article copy, condition guidance, testimonials, the Hippocratic-oath text and the privacy/terms text are the product's content; only frames and components were measured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
