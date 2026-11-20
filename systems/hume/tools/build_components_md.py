#!/usr/bin/env python3
"""Build components.md for the Hume AI design reference.

Reads raw/components-computed.json (every component and state, measured),
tokens.json, screenshots/ and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the
palette token whose value matches, the font family is named once per value,
and a state row shows only what differs from the first state. Adapted from
the hashnode package's builder (the Coursera kit lineage via Deezer).

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


# A measured colour is labelled by the token whose value matches. The lookup
# runs set by set — the light theme's resolved roles first (www.hume.ai
# paints light only: the painted surface lives there), then the dark set
# (the dev.hume.ai docs' painted dark), then core, whose accent/gradient/
# spectrum and palette.* trees hold the brand literals — so a measured
# value is named by its role, not whichever literal happens to share it.
# PRIMARY pins the roles a label should prefer when several tokens share
# one colour. Names carry their set prefix (light.bg.default) so a label
# always names a real path in tokens.json.
PRIMARY = {"bg.default", "ink.default", "code.background",
           "docs.color.background", "docs.color.body", "docs.color.border"}
BY_COLOR = {}
for n, t in sorted(flat(T["light"], "light."), key=lambda it: (it[0].split(".", 1)[1] not in PRIMARY, it[0])):
    if t["$type"] == "color":
        BY_COLOR.setdefault(t["$value"], n)
for n, t in sorted(flat(T["dark"], "dark."), key=lambda it: (it[0].split(".", 1)[1] not in PRIMARY, it[0])):
    if t["$type"] == "color":
        BY_COLOR.setdefault(t["$value"], n)
for n, t in flat(T["core"], "core."):
    if t["$type"] == "color":
        BY_COLOR.setdefault(t["$value"], n)


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def _lab_okl(c):
    """CIE lab()/oklab()/oklch() -> '#rrggbb' or 'rgba(...)' for the token
    lookup, mirroring norm_color() in build_tokens.py."""
    m = re.fullmatch(r"lab\(\s*([\d.]+)\s+(-?[\d.]+)\s+(-?[\d.]+)\s*(?:/\s*([\d.]+%?))?\s*\)", c.strip())
    if m:
        L, A, B, a = m.groups()
        fy = (float(L) + 16) / 116
        fx, fz = fy + float(A) / 500, fy - float(B) / 200
        d = 6 / 29
        f = lambda t: t ** 3 if t > d else 3 * d ** 2 * (t - 4 / 29)
        x, y, z = f(fx) * 0.96422, f(fy) * 1.0, f(fz) * 0.82521
        r = 3.1338561 * x - 1.6168667 * y - 0.4906146 * z
        g = -0.9787684 * x + 1.9161415 * y + 0.0334540 * z
        b = 0.0719453 * x - 0.2289914 * y + 1.4052427 * z
        gam = lambda v: 12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055
        r, g, b = (max(0, min(255, round(gam(v) * 255))) for v in (r, g, b))
        if a is None:
            return "#%02x%02x%02x" % (r, g, b)
        al = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return "#%02x%02x%02x" % (r, g, b) if al == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, al)
    # oklab()/oklch() as Chromium computes them: the full OKLab -> linear
    # sRGB conversion, so a chromatic value keeps its hue and a grey keeps its
    # true lightness (L 0.221 is #1b1b1b, not L x 255).
    m = re.fullmatch(r"okl(ch|ab)\(\s*([\d.]+%?)\s+(none|-?[\d.]+%?)\s+(none|-?[\d.]+(?:deg)?)\s*(?:/\s*([\d.]+%?))?\s*\)", c.strip())
    if m:
        import math
        kind, L, x, y, a = m.groups()
        L = float(L[:-1]) / 100 if L.endswith("%") else float(L)
        num = lambda v, scale: 0.0 if v == "none" else (float(v[:-1]) / 100 * scale if v.endswith("%") else float(v.replace("deg", "")))
        if kind == "ch":
            C_, h = num(x, 0.4), num(y, 1)
            A, B = C_ * math.cos(math.radians(h)), C_ * math.sin(math.radians(h))
        else:
            A, B = num(x, 0.4), num(y, 0.4)
        l_ = (L + 0.3963377774 * A + 0.2158037573 * B) ** 3
        m_ = (L - 0.1055613458 * A - 0.0638541728 * B) ** 3
        s_ = (L - 0.0894841775 * A - 1.2914855480 * B) ** 3
        lin = (4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
               -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
               -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_)
        gam = lambda v: 12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055
        r, g, b = (max(0, min(255, round(gam(max(0.0, v)) * 255))) for v in lin)
        al = 1 if a is None else (float(a[:-1]) / 100 if a.endswith("%") else float(a))
        return "#%02x%02x%02x" % (r, g, b) if al == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, al)
    return c


def colour(c, tokens=True):
    """rgb()/rgba()/color(srgb)/lab()/oklab()/oklch() -> '#hex `token`' or 'rgba(...)'."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        tok = BY_COLOR.get(v) if tokens else None
        return f"{v} `{tok}`" if tok else v

    # Modern colour functions first: normalize each to sRGB so the hex/RGBA
    # passes below can attach the token name like any other measured value.
    c = re.sub(r"(?:lab|oklab|oklch)\([^)]*\)", lambda m: _lab_okl(m.group(0)), c)
    c = re.sub(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)",
               lambda m: label(norm(*(round(float(x) * 255) for x in m.group(1, 2, 3)), m.group(4))), c)
    c = re.sub(r"rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)", lambda m: label(norm(*m.group(1, 2, 3), m.group(4))), c)
    # Skip hexes a label was already attached to, so the pass is idempotent.
    return re.sub(r"#[0-9a-fA-F]{6}\b(?!\s*`)", lambda m: label(m.group(0).lower()), c)


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
            bits.append(" ".join(x for x in (pe, *(colour(p[k], tokens=False) if p.get(k) else None for k in ("backgroundColor", "borderTopWidth", "boxShadow")), p.get("opacity")) if x))
    # A root box-shadow (e.g. the 1px focus ring gained on focus-visible) does
    # not remove the painted children: keep reporting their layers, which is
    # where a state-carrying child outline (the 3px cyan CTA ring) shows up.
    if s["backgroundColor"] == "rgba(0, 0, 0, 0)" and s["borderTopWidth"] == "0px" and s["backgroundImage"] == "none":
        for p in v.get("paint", [])[:6]:
            bits.append(" ".join(x for x in (p["node"], p.get("size"), *(colour(p[k], tokens=False) if p.get(k) else None for k in ("bg", "border", "shadow", "outline")), p.get("radius")) if x))
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

PAGE_NAME = {"www.hume.ai/": "home", "www.hume.ai/products/decision-model-api": "Audio Decision Model",
             "www.hume.ai/products/expression-apis": "Expression APIs", "www.hume.ai/benchmark": "benchmark",
             "www.hume.ai/blog": "blog index", "www.hume.ai/blog/hume-audio-decision-benchmarks": "benchmark post",
             "www.hume.ai/contact-form": "contact form", "dev.hume.ai/audio-decisions/docs/overview": "docs overview",
             "dev.hume.ai/audio-decisions/reference/decisions/create": "docs API reference",
             "demo.hume.ai/decision-model/file": "invitation gate", "app.hume.ai/log-in": "log-in"}

GROUP_INTRO = {
    "Site chrome": "The frame every www.hume.ai page carries: the top nav (the wordmark, Emotion Science, the Products / Solutions / Benchmarks / Resources menu buttons, the solid 'See a Demo' action) and the footer with its link columns, newsletter form and social links. The surface has no theme control.",
    "Home": "The home surface: the 'Measure and improve real-world voice AI performance' hero, the scripted sample-call player ('Live answers from the call' — its transport was pressed for the playing state, a media control, never a submission), the audio-pipeline diagram, the benchmark table's category tabs and the newsletter form (the email field was clicked into for the focus look, never typed or submitted).",
    "Product pages": "The product surfaces: the hero headline, the 'Contact sales' action — measured, never followed — and a feature card.",
    "Blog": "The /blog index: post preview cards, title links and the category filters — 'selected' is a filter's own activation, links were measured, never followed.",
    "Prose": "The blog article layer: the title h1, body paragraphs and links, inline code, fenced blocks and the benchmark result table.",
    "Contact form": "The 'Talk to Hume' form: its fields were clicked into for the focus look — nothing was typed, and the submit button was never pressed.",
    "Docs": "The dev.hume.ai docs surface (a Fern docs build): the left nav, the 'Search /' field button (never queried), the header's Theme button — the only real theme control on any captured surface, whose own Light / Dark / System menu repainted html.dark for the dark states — the 'Get access' action, code blocks, the 'On this page' rail and the language tabs.",
    "Demo gate": "The demo.hume.ai invitation gate: 'Start from your invitation — the Audio Decision Model playground opens from the link in your invitation email'. The playground itself is a documented boundary; the gate is the honest signed-out evidence.",
    "Log-in": "The app.hume.ai sign-in card: the platform's public boundary page. Fields were clicked into for the focus look — nothing was typed and the LOG IN button was never pressed.",
    "Site chrome (mobile)": "The 390px surface: the collapsed nav and the 'Open menu' drawer, opened and closed by its own button.",
}

SHOTS = [
    ("home", "Home", "www.hume.ai/"),
    ("emotion-science", "Emotion science", "www.hume.ai/emotion-science"),
    ("decision-model", "Audio Decision Model", "www.hume.ai/products/decision-model-api"),
    ("expression-apis", "Expression APIs", "www.hume.ai/products/expression-apis"),
    ("human-feedback", "Human Feedback", "www.hume.ai/products/human-feedback"),
    ("user-testing", "User Testing", "www.hume.ai/products/user-testing"),
    ("speech-data", "Speech Data", "www.hume.ai/products/speech-data"),
    ("prism", "Prism", "www.hume.ai/products/prism"),
    ("voiceeq", "VoiceEQ platform", "www.hume.ai/products/voiceeq-platform"),
    ("develop-models", "Develop voice models", "www.hume.ai/solutions/develop-voice-models"),
    ("deploy-agents", "Deploy voice agents", "www.hume.ai/solutions/deploy-voice-agents"),
    ("benchmark", "Benchmark", "www.hume.ai/benchmark"),
    ("blog", "Blog index", "www.hume.ai/blog"),
    ("blog-post", "Benchmark post", "www.hume.ai/blog/hume-audio-decision-benchmarks"),
    ("publications", "Publications", "www.hume.ai/publications"),
    ("about", "About", "www.hume.ai/about"),
    ("careers", "Careers", "www.hume.ai/careers"),
    ("contact-form", "Contact form", "www.hume.ai/contact-form"),
    ("privacy-policy", "Privacy", "www.hume.ai/privacy-policy"),
    ("terms-of-use", "Terms", "www.hume.ai/terms-of-use"),
    ("explore", "Speech Prosody explorer", "www.hume.ai/explore/speech-prosody-model"),
    ("notfound", "404 page (stray-path probe)", "www.hume.ai/this-page-does-not-exist"),
    ("docs-overview", "Docs overview", "dev.hume.ai/audio-decisions/docs/overview"),
    ("docs-quickstart", "Docs quickstart", "dev.hume.ai/audio-decisions/docs/quickstart/python"),
    ("docs-reference", "Docs API reference", "dev.hume.ai/audio-decisions/reference/decisions/create"),
    ("docs-changelog", "Docs changelog", "dev.hume.ai/audio-decisions/changelog"),
    ("demo-gate", "Demo invitation gate", "demo.hume.ai/decision-model/file"),
    ("login", "Log-in", "app.hume.ai/log-in"),
]

MOBILE = [
    ("mobile-home", "Home, phone", "www.hume.ai/"),
    ("mobile-benchmark", "Benchmark, phone", "www.hume.ai/benchmark"),
    ("mobile-blog", "Blog index, phone", "www.hume.ai/blog"),
    ("mobile-contact-form", "Contact form, phone", "www.hume.ai/contact-form"),
    ("mobile-docs-overview", "Docs overview, phone", "dev.hume.ai/audio-decisions/docs/overview"),
    ("mobile-demo-gate", "Demo gate, phone", "demo.hume.ai/decision-model/file"),
    ("mobile-login", "Log-in, phone", "app.hume.ai/log-in"),
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

# The captured icon set: tools/capture/icons.mjs collects every distinct
# inline <svg> into icons/ and writes icons/INDEX.tsv (file, inferred_name,
# hash, rendered sizes, viewBox, style, seen_on, place, text_or_label). The
# table below is that index, so the section never contradicts the package.
icons = []
idx = Path("icons/INDEX.tsv")
if idx.exists():
    rows = [l.split("\t") for l in idx.read_text().splitlines() if l.strip()]
    header = rows[0]
    for r in rows[1:]:
        d = dict(zip(header, r + [""] * (len(header) - len(r))))
        icons.append([d.get("file", ""), d.get("inferred_name", ""), d.get("hash", ""),
                      d.get("sizes", ""), d.get("viewBox", ""), d.get("style", ""),
                      d.get("seen_on", ""), d.get("place", ""), d.get("text_or_label", "")])

W("# Hume AI components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Read from hume.ai's signed-out surfaces on {J['_meta']['read']}, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Later recaptures merge into the same file, so every entry names the date its own states were read; a state a re-read missed keeps its earlier date and says so. Nothing was signed into, bought, typed, searched or submitted; the only presses were local UI toggles the product's own chrome provides — the docs header's Theme menu (the only real theme control on any surface), the home player's transport (a scripted sample-call player, a media control), the benchmark category tabs, the blog filters and the mobile 'Open menu' drawer — and nothing was sent anywhere: the contact form, newsletter Subscribe, log-in button and the docs API playground's Send were measured, never used.")
W()
W("**Where this was read.** Four public origins carry the system: www.hume.ai — the marketing and product pages (home, /emotion-science, the /products/* and /solutions/* pages, /benchmark, /blog, /publications, /about, /careers, /contact-form, the legal pages, the Speech Prosody explorer, the not-found page); dev.hume.ai — the Audio Decisions docs (the one surface with a theme control); demo.hume.ai — the Audio Decision Model playground's invitation gate (the playground itself is a documented boundary); and app.hume.ai/log-in — the platform's sign-in surface, never entered. EVI and Octave TTS have no public surface after the pivot to the Audio Decision Model line; demo.hume.ai/evi answers 404 — all documented as boundaries under Gaps, not captures.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [patterns.md](patterns.md).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value, when there is one (the `light.*` roles first — the painted surface; `dark.*` holds only the docs' painted dark). Text is written family size/line-height weight, then its colour, for example `Inter 16/26 400, #1b1918`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{theme}-{state}.png` where `{theme}` is the theme the page painted at capture: www.hume.ai, demo.hume.ai and app.hume.ai paint one light theme with no control, so their shots are all `{page}-light-*`; the dev.hume.ai docs carry the one real theme control — the header Theme button's own Light / Dark / System menu repaints html.dark — so `docs-{page}-dark-*` shots were painted through it, verified by the painted surface and switched back to Light after. Desktop shots are 1440 x 900 at 1x; `-full` shots are the whole page at 1x, bounded at eight chunks with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x). `notfound-*` is a stray-path probe — www.hume.ai's real not-found page.")
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
    ("Docs Theme menu", "the dev.hume.ai header", "the Theme button's own press — its Light / Dark / System menu opened; Dark pressed for the dark shots, the painted surface verified, Light restored", "[docs-overview-dark-default](screenshots/docs-overview-dark-default.png), [docs-overview-light-default](screenshots/docs-overview-light-default.png)"),
    ("Customer-call player", "the home hero", "the player's own Play press — the scripted sample call running; Stop ended it (a media control, not a submission)", "[home-light-playing](screenshots/home-light-playing.png)"),
    ("Benchmark category tabs", "the home and /benchmark tables", "a category tab's own activation — a local UI toggle", "[benchmark-light-category-tab](screenshots/benchmark-light-category-tab.png)"),
    ("Blog category filters", "/blog", "the 'Research' filter's own activation — a local UI toggle; 'All' restored after", "[blog-light-category-filter](screenshots/blog-light-category-filter.png)"),
    ("Contact form", "www.hume.ai/contact-form", "a field clicked into for the focus look — nothing typed, the form never submitted", "[contact-form-light-field-focused](screenshots/contact-form-light-field-focused.png)"),
    ("Docs Search / 'Ask AI'", "the docs header", "the Search dialog was opened for its UI and closed with Escape — never queried; 'Ask AI' never pressed", "see icons; no query run"),
    ("Docs API playground", "dev.hume.ai/reference", "the request editor measured at rest — Send never pressed (issuing a request is a network side effect)", "[docs-reference-light-full](screenshots/docs-reference-light-full.png)"),
    ("Demo playground", "demo.hume.ai", "gated on an invitation email link — the gate is captured, the playground was never entered", "[demo-gate-light-default](screenshots/demo-gate-light-default.png)"),
    ("Sign-in / the platform", "app.hume.ai", "/log-in captured at rest and with a field focused — never submitted; nothing past it was entered", "[login-light-default](screenshots/login-light-default.png)"),
    ("EVI / Octave TTS", "the retired product line", "no public surface exists after the pivot to the Audio Decision Model line — demo.hume.ai/evi answers 404", "boundary; see Gaps"),
]

for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement files.")
W()
def _alpha(c):
    m = re.search(r"rgba?\([^)]*?,\s*([\d.]+)\s*\)$", c or "")
    return float(m.group(1)) if m else 1.0


def _outline_alpha(outline):
    """Alpha of the colour inside a recorded '2px solid rgba(...) offset 2px'
    outline string — 1 when the colour is a plain rgb()/named value."""
    m = re.search(r"rgba?\([^)]*\)", outline or "")
    return _alpha(m.group(0)) if m else 1.0


foc = []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st or "style" not in st or st.get("via") == "focus failed":
        continue
    s = st["style"]
    base = next((v["style"] for v in c["states"].values() if "style" in v), s)
    # A transparent outline paints nothing: the width/style test alone
    # counted invisible 2px solid rgba(0,0,0,0) outlines as rings.
    ring = (s["outlineStyle"] != "none"
            and float(s["outlineWidth"].replace("px", "")) > 0
            and _alpha(s["outlineColor"]) > 0)
    # A ring painted on a child layer instead of the wrapper: offer buttons
    # draw 1px dotted outlines on their inner anchor while the wrapper's own
    # outline stays none. Those states must count as ringed too — but only
    # when the child's outline colour is not itself transparent.
    child_ring = next((n["outline"] for n in st.get("paint", [])
                       if n.get("outline") and _outline_alpha(n["outline"]) > 0), None)
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
# the card-like components to compare in one table
for k in ["nav-cta", "player-card", "newsletter-input", "post-card", "prose-pre", "contact-field", "docs-code-block", "docs-search-button", "demo-gate-card", "login-card", "login-email-field", "login-submit"]:
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
        # Provenance: each state carries the date of the run that measured it.
        # A component a recapture missed keeps its earlier readings under the
        # earlier date (recaptureMissed), and a state whose re-read failed
        # keeps its earlier style under rerunError — never republished under
        # the new run's date.
        by_run = {}
        for s, v in c["states"].items():
            by_run.setdefault(v.get("run") or c.get("run") or J["_meta"]["read"], []).append(s)
        prov = []
        if len(by_run) == 1:
            prov.append(f"Read on {next(iter(by_run))}.")
        elif by_run:
            prov.append("States read on " + "; ".join(f"{r} ({', '.join(sorted(ss))})" for r, ss in sorted(by_run.items())) + ".")
        if c.get("recaptureMissed"):
            prov.append(f"A {c['recaptureMissed']} recapture missed it — the {c.get('run')} readings are retained, not remeasured.")
        for s, v in c["states"].items():
            if v.get("rerunError"):
                prov.append(f"`{s}` kept its {v.get('run')} reading after a failed re-read ({v['rerunError'][:90]}).")
            elif v.get("error"):
                prov.append(f"`{s}` failed at capture ({v['error'][:90]}).")
        if prov:
            W(" ".join(prov))
        W()
        if c.get("missing"):
            W("Not on the page when it was captured.")
            continue
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
if icons:
    W(f"{len(icons)} distinct inline-SVG icons were collected from the live pages into [icons/](icons) by `tools/capture/icons.mjs`, indexed in [icons/INDEX.tsv](icons/INDEX.tsv): a file is named from `tools/capture/icon-names.tsv` where its geometry hash is listed, else the label or class of the control it sits in, else `icon-<hash>`; colour is kept as `currentColor` wherever it matched the text colour, so each icon recolours from CSS `color` the way it does on the site. The icons are the product's artwork — borrow the set's grammar (sizes, stroke-vs-fill, naming roles), never the artwork itself.")
else:
    W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the product's mark, navigation glyphs, partner logos) are the product's artwork. Declared under layoutGaps in the catalog entry.")
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
W("### The blocked product surfaces")
W()
W("The signed-in product was never entered: **app.hume.ai past /log-in** — the platform's sign-in card is captured at rest and with a field focused, but no account exists and nothing was typed, submitted or entered. The **demo.hume.ai playground** is gated on an invitation email link — the gate page is captured; the Audio Decision Model playground behind it was never opened. The **EVI / Octave TTS line** has no public surface after the pivot to the Audio Decision Model / VoiceEQ line — demo.hume.ai/evi answers 404, so no EVI demo state exists to capture (the old EVI microphone-permission boundary is moot). The docs' **'Ask AI' and Search** were never queried, and the API reference's **Send** was never pressed — issuing a request is a network side effect. All are documented as boundaries, never faked.")
W()
W("### Pages")
W()
W("- **Sign-in / account surfaces** — the platform dashboard, API keys, projects and billing behind app.hume.ai/log-in: the product's own boundary, never entered.")
W("- **demo.hume.ai playground** — gated on an invitation email link; the 'Start from your invitation' gate is the honest signed-out evidence.")
W("- **EVI / Octave TTS** — no public surface exists post-pivot; demo.hume.ai/evi answers 404.")
W("- **The /explore/speech-prosody-model canvas** — the explorer renders its visualisation into a canvas; the painted bitmap is captured in the screenshots but its internal structure is not a DOM and no DOM values are invented for it.")
W("- **External links** — social links, the publications' arXiv/journal PDFs and the careers ATS links lead off-site; external surfaces, out of scope.")
W("- **Long pages** — every `-full` shot is bounded at eight chunks; any boundary the bound hit is recorded in the shot's `.capture.json` sidecar and the capture log.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on the controls that carry it, so a state a script adds on mousedown (if any) is missing.")
W("- **The docs Search and 'Ask AI' were never queried** — the dialog was opened for its UI and closed with Escape; no query was run, so result lists are uncaptured.")
W("- **The contact form, newsletter and log-in fields were never typed into or submitted** — clicked into for the focus look only.")
W("- **Send on the docs API playground was never pressed** — issuing a request is a network side effect, so the request editor's resting surface is the honest signed-out evidence.")
W("- **The home player's Play was pressed** — it drives a scripted sample call (a media control, not a submission); Stop ended it after the playing state was captured.")
W()
W("### Themes")
W()
W("www.hume.ai, demo.hume.ai and app.hume.ai paint a single light theme and have no theme control at all — a `.dark` class and a dark colour-scheme emulation both leave the painted surface unchanged, and no dark marketing shots or tokens are invented. The dev.hume.ai docs carry the one real theme control: the header Theme button's own Light / Dark / System menu repaints `html.dark`, verified by the painted surface (html class, color-scheme, the computed background), and Light was restored afterwards. The `dark` token set holds only the docs' painted dark — `light.docs.*` the same declarations under html.light.")
W()
W("### Fonts")
W()
W("- **The brand faces are proprietary and never shipped**: 'Martina Plantijn' (the www display serif), 'PP Fraktion Mono'/'Fraktion' (the code faces), 'Fellix' (the docs/app body face) and 'M PLUS 1' (Japanese) are licensed assets, declared and measured by name only. 'Inter' is open-licensed. The style guide falls back to system faces.")
W()
W("### Screenshots")
W()
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W("- The rendered brand strings on the captured pages (the wordmark and copy) are the product's published content.")
W("- Public author names, handles, headshots and company logos on the about, careers, blog and testimonial surfaces are published content and are kept; nothing private was captured.")
W()
W("### Content left out")
W()
W("- Article copy, publication text and testimonial quotes are the product's published content; only frames and components were measured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
