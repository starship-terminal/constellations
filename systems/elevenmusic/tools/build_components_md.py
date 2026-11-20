#!/usr/bin/env python3
"""Build components.md for the ElevenMusic design reference.

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
# The components were measured on the dark paint, so a value names the dark
# token first, then a light-only or core one it also matches. Themed tokens
# are named with their set ("dark.color.ink.foreground") so a reader can see
# which theme the link points into.
for setname in ("dark", "light", "core"):
    for n, t in flat(T[setname]):
        if t["$type"] == "color" and isinstance(t["$value"], str) and not t["$value"].startswith("{"):
            # Computed styles round alpha to about two places, so both sides of
            # the lookup carry a 2-decimal alpha.
            key = re.sub(r"(\d+\.\d+)\)", lambda m: f"{round(float(m.group(1)), 2):g})", t["$value"])
            BY_COLOR.setdefault(key, n if setname == "core" else f"{setname}.{n}")


def _gam(x):
    return 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055


def _clamp255(v):
    return round(min(1, max(0, v)) * 255)


def oklab_rgb(L, a, b):
    l, m, s = ((L + 0.3963377774 * a + 0.2158037573 * b) ** 3, (L - 0.1055613458 * a - 0.0638541728 * b) ** 3, (L - 0.0894841775 * a - 1.291485548 * b) ** 3)
    return [_clamp255(_gam(v)) for v in (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s, -0.0041960863 * l - 0.7034186147 * m + 1.707614701 * s)]


def lab_rgb(L, a, b):
    fy = (L + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    e, k = 216 / 24389, 24389 / 27
    finv = lambda t: t ** 3 if t ** 3 > e else (116 * t - 16) / k
    X, Y, Z = finv(fx) * 0.3457 / 0.3585, (fy ** 3 if L > k * e else L / k), finv(fz) * (1 - 0.3457 - 0.3585) / 0.3585
    x = 0.955473421488075 * X - 0.02309845494876471 * Y + 0.06325924320057072 * Z
    y = -0.0283697093338637 * X + 1.0099953980813041 * Y + 0.021041441191917323 * Z
    z = 0.012314014864481998 * X - 0.020507649298898964 * Y + 1.330365926242124 * Z
    return [_clamp255(_gam(v)) for v in (3.2409699419 * x - 1.5373831776 * y - 0.4986107603 * z, -0.9692436363 * x + 1.8759675015 * y + 0.0415550574 * z, 0.0556300797 * x - 0.2039769589 * y + 1.0569715142 * z)]


def unlab(c):
    """Tailwind 4 writes opacity modifiers as color-mix, which Chromium computes as lab() or
    oklab(); both go back to rgb() here so they compare against the tokens' sRGB values."""
    def f(m):
        L = float(m.group(2).rstrip("%")) * (0.01 if m.group(2).endswith("%") else 1)
        r, g, b = (oklab_rgb if m.group(1) else lab_rgb)(L, float(m.group(3)), float(m.group(4)))
        return f"rgba({r}, {g}, {b}, {m.group(5)})" if m.group(5) else f"rgb({r}, {g}, {b})"
    return re.sub(r"(ok)?lab\(([-\d.e]+%?) ([-\d.e]+) ([-\d.e]+)(?: / ([\d.]+))?\)", f, c)


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), round(float(a), 2))


def colour(c, tokens=True):
    """rgb()/rgba()/color(srgb)/lab()/oklab() -> '#hex `token`' or 'rgba(...)'."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        tok = BY_COLOR.get(v) if tokens else None
        return f"{v} `{tok}`" if tok else v

    c = unlab(c)
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
            bits.append(" ".join(x for x in (pe, colour(p["backgroundColor"]) if p.get("backgroundColor") else None, p.get("borderTopWidth"), colour(p["boxShadow"]) if p.get("boxShadow") else None, p.get("opacity")) if x))
    # A root box-shadow (e.g. the 1px focus ring gained on focus-visible) does
    # not remove the painted children: keep reporting their layers, which is
    # where a state-carrying child outline (the 3px cyan CTA ring) shows up.
    if s["backgroundColor"] == "rgba(0, 0, 0, 0)" and s["borderTopWidth"] == "0px" and s["backgroundImage"] == "none":
        for p in v.get("paint", [])[:6]:
            bits.append(" ".join(x for x in (p["node"], p.get("size"), colour(p["bg"]) if p.get("bg") else None, colour(p["border"]) if p.get("border") else None, colour(p["shadow"]) if p.get("shadow") else None, colour(p["outline"]) if p.get("outline") else None, p.get("radius")) if x))
    if bits:
        o["layers"] = "; ".join(bits)[:400]
    return o


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "outline", "text", "transition", "transform", "opacity", "icon", "placeholder", "layers"]


def state_rows(c):
    # A state whose capture failed (e.g. via: "focus failed" — the element would
    # not hold a real keyboard focus) is not a captured state: it is reported
    # separately so a failed attempt can never read as a measured absence of a
    # focus ring.
    states = [s for s in c["states"] if "style" in c["states"][s] and c["states"][s].get("via") != "focus failed"]
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

PAGE_NAME = {"home": "home", "explore": "explore", "charts": "charts", "pricing": "pricing",
             "login": "log in", "mobile": "home"}

GROUP_INTRO = {
    "Shell and navigation": "The app chrome: the fixed left rail (logo, Search, nav, the Publish promo, playlists), the header with its Resources dropdown, and the Sign-in / Start-free pair.",
    "Home hero": "The 'Make music yours.' waldenburg headline over the composer — the prompt field, the Attach/Create circles and the prompt chips — plus the demo list and carousel.",
    "Explore and browse": "The create surface: the pill nav, the prompt input, the featured carousel, track and genre cards, and the shelf headings.",
    "Player": "The transport bar mounted by pressing a card's own Play: progress, prev/play/next, repeat, volume, queue and the gated Remix.",
    "Charts": "The ranked chart: the Play-all and Shuffle pills, Share, chart rows and the gated Like/Remix icon buttons.",
    "Pricing": "The pricing surface: Free and Pro plan cards (the Pro card an inverted white island on the dark field), the feature rows and the FAQ accordion.",
    "Log in and sign up": "The auth boundary card, measured but never submitted: the SSO buttons, the expanded email form, the terms checkbox and the disabled Continue.",
    "Footer": "The site footer inside the shell: language selector, link columns, legal, Cookie settings and the System/Light/Dark theme control.",
    "Mobile (390 wide)": "The app at phone width: the compact header, the bottom Explore/Create/Library tab bar, and the fullscreen menu sheet.",
}

SHOTS = [
    ("home", "Home", "/"),
    ("explore", "Explore", "/explore"),
    ("charts", "Charts", "/charts"),
    ("tracks", "Tracks", "/tracks"),
    ("genres", "Genres", "/genres"),
    ("genre-electronic", "Genre: Electronic", "/genres/electronic"),
    ("sounds", "Sounds", "/sounds"),
    ("tools", "Tools", "/tools"),
    ("artist", "Artist profile", "/artists/ghostmkc-5JuuiL"),
    ("playlist", "Playlist", "/playlists/69eb381eb3c0fe73c21c695c"),
    ("blog", "Blog", "/blog"),
    ("pricing", "Pricing", "/pricing"),
    ("login", "Log in", "/login"),
    ("signin", "Sign in (alias)", "/sign-in"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "/"),
    ("mobile-explore", "Explore, phone", "/explore"),
    ("mobile-charts", "Charts, phone", "/charts"),
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
icons = []

W("# ElevenMusic components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from elevenmusic.io on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. elevenmusic.io is one Next.js app shell painting dark by default (a real light theme flips from the footer's own segmented control): a fixed left rail, a header, an inner scroller per page and a bottom player bar once a track plays, set in Inter with waldenburg display headings. Nothing was signed into, created, liked, remixed, shared or submitted; the email field was filled with sample text and cleared; a track card's Play was pressed to mount the player bar, and every gated control was measured, never pressed.")
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
W("Screenshots are named `{page}-{theme}-state.png`: the app paints `dark` by default and the `*-light-*` shots were taken after the footer's own Light-theme toggle. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x (the pages scroll inside one inner element, expanded for the shot); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).")
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
    ("Resources dropdown", "every header", "the Resources trigger's own click", "[home-dark-menu](screenshots/home-dark-menu.png), [nav-dropdown](#nav-dropdown), [menu-link](#menu-link)"),
    ("Sign-in dialog (Search)", "every page", "the sidebar Search button's own click — search is gated behind an account", "[home-dark-search](screenshots/home-dark-search.png)"),
    ("Player bar", "/explore", "a track card's own Play — local media playback; Like/Remix/Share never pressed", "[explore-dark-playing](screenshots/explore-dark-playing.png), [player-bar](#player-bar)"),
    ("Email options", "/login", "the Show-other-options button's own toggle; the form was never submitted", "[login-dark-options](screenshots/login-dark-options.png), [email-field](#email-field)"),
    ("Light theme", "the footer theme control", "the Light segment's own toggle (persisted by the product's cookie)", "[home-light-default](screenshots/home-light-default.png)"),
    ("Cookiebot / Google One-Tap overlays", "every page", "hidden, never answered (no consent button was ever clicked, nothing signed into)", "hidden before every shot and reading"),
    ("Signed-in product", "create, library, composer, chat, publish", "every Create/Library/Composer surface and Like/Remix/Share sits behind sign-in", "boundary; see Gaps"),
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
    if not st or "style" not in st or st.get("via") == "focus failed":
        continue
    s = st["style"]
    base = next((v["style"] for v in c["states"].values() if "style" in v), s)
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0
    # A ring painted on a child layer instead of the wrapper: offer buttons
    # draw 1px dotted outlines on their inner anchor while the wrapper's own
    # outline stays none. Those states must count as ringed too.
    child_ring = next((n["outline"] for n in st.get("paint", []) if n.get("outline")), None)
    shadow = s["boxShadow"] != base["boxShadow"] and s["boxShadow"] != "none"
    border = any(
        s[f"border{d}{p}"] != base[f"border{d}{p}"]
        for d in ("Top", "Right", "Bottom", "Left")
        for p in ("Color", "Width", "Style")
    )
    desc = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}" if ring else (f"on a child: {colour(child_ring)}" if child_ring else None)
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
W("**Card shapes.** Default-state values; the entries hold the states.")
W()
W("| Card | Size | Border | Radius | Background | Shadow | Padding |")
W("|---|---|---|---|---|---|---|")
# PRODUCT (adapt): the card-like components to compare in one table.
for k in ["feature-card", "track-card", "genre-card", "demo-card", "plan-card", "plan-card-pro", "auth-card", "sidebar-promo"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if "style" in s), None)
    if st is None:
        continue
    p = props(st)
    W(f"| [{c['title']}](#{re.sub(r'[^a-z0-9 -]', '', c['title'].lower()).replace(' ', '-')}) | {p['size']} | {p.get('border', '-')} | {p.get('radius', '-')} | {p.get('background', '-')} | {p.get('shadow', 'none')} | {p.get('padding', '0')} |")
W()

# Entries read while an earlier entry had left their node open (the README's
# What to distrust lists them): the default reading is of the open item.
READ_OPEN = {
    "faq-answer": "faq-item's `expanded` reading opened this row and left it open, so this default reading (152px tall, against the 68px closed row) is of the open item. tools/capture/public/measure.mjs now closes it after the reading.",
}

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
        W()
        if c.get("missing"):
            W("Not on the page when it was captured.")
            continue
        if k in READ_OPEN:
            W(f"**Read in the wrong state.** {READ_OPEN[k]} The entry needs a recapture.")
            W()
        failed = [s for s, v in c["states"].items() if "style" in v and v.get("via") == "focus failed"]
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the ElevenMusic mark, the Google and Apple SSO glyphs, the Lucide-style control glyphs, album and artist artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.")
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
W("ElevenMusic's product — Create, Composer, Library, Chat, Tools' generation surfaces, publishing (\"Publish your music\"), Likes, Remixes, Shares, playlist saving and account settings — lives behind sign-in and was never reached. Search itself opens the log-in dialog, captured as evidence of the wall. Nothing was created, liked, remixed, shared, published or submitted, and no OAuth button was ever pressed.")
W()
W("### Pages")
W()
W("- **The workspace.** Every post-login surface (Create, Composer, Chat, Library, artist-page publishing, settings, billing) needs an account and was never reached; /login and /sign-in were captured as forms and never submitted.")
W("- **Generation.** Every Create button, prompt submit and Attach control was measured, never pressed — sending a prompt would consume the product's generation quota and produce user content.")
W("- **Like, Remix, Share.** Measured on the charts and explore surfaces, never pressed — each is gated behind an account.")
W("- **Purchase.** The Get-Pro and Start-free CTAs were measured, never followed past the public card.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Hover on player-prev and player-next** could not be held (the forced hover reported the element outside the viewport); the failure is recorded in the JSON, not promoted to a reading.")
W("- **Error, loading and empty states** were not seen on the public surface.")
W("- **Focus-visible** was a real keyboard focus on every control that would take it; a small number of controls show no measured change and are named in the Focus paragraph above.")
W()
W("### Themes")
W()
W("elevenmusic.io paints **dark by default** (`html.dark`, `color-scheme: dark`) and declares a real light theme: the footer's System/Light/Dark segmented control re-binds the same semantic roles to a warm-paper field (#fdfcfb) and persists by cookie. Both passes are resolved in tokens.json (the `--lighten-*` white-alpha ramp resolves in the dark pass only).")
W()
W("### Fonts")
W()
W("- **Inter** (variable 100-900) is the UI face; **waldenburg** (light and regular) is the display face on headlines; **GeistMono** is declared for code and IDs. All are served from the site's own Next.js media; the style guide falls back to system sans.")
W()
W("### Screenshots")
W()
W("- Album art, artist photography, playlist covers, the auth dialog's marketing panel and the ElevenMusic mark in the screenshots are the product's published content.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W("- `/charts` and `/` mobile scroll beyond one GPU texture; their full shots are tiled `*.part0/.part1` PNGs — an inner-scroller boundary, not missing content.")
W()
W("### Content left out")
W()
W("- Track titles, artist names, prompt copy, blog posts and plan copy are the product's content; only frames and components were measured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
