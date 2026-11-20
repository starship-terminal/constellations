#!/usr/bin/env python3
"""Build components.md for the Endless design reference.

Reads raw/components-computed.json (every component and state, measured),
tokens.json and screenshots/, and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the token whose
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


# ------------------------------------------------- lab / oklab -> sRGB hex
# Chromium computes Tailwind v4 colours (oklch declarations, color-mix opacity
# modifiers) as lab()/oklab() strings in raw/components-computed.json — most of
# the saved readings use them, so colour() must convert them before the token
# lookup or no reading ever matches a token name. Same conversion as
# build_component_tokens.py.
def _gam(x):
    return 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055


def _oklab(L, a, b):
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.291485548 * b) ** 3
    return [_gam(4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s),
            _gam(-1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s),
            _gam(-0.0041960863 * l - 0.7034186147 * m + 1.707614701 * s)]


def _lab(L, a, b):
    fy = (L + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    e, k = 216 / 24389, 24389 / 27
    finv = lambda t: t ** 3 if t ** 3 > e else (116 * t - 16) / k
    X = finv(fx) * 0.3457 / 0.3585
    Y = fy ** 3 if L > k * e else L / k
    Z = finv(fz) * (1 - 0.3457 - 0.3585) / 0.3585
    # D50 -> D65 (Bradford), then XYZ -> linear sRGB
    x = 0.955473421488075 * X - 0.02309845494876471 * Y + 0.06325924320057072 * Z
    y = -0.0283697093338637 * X + 1.0099953980813041 * Y + 0.021041441191917323 * Z
    z = 0.012314014864481998 * X - 0.020507649298898964 * Y + 1.330365926242124 * Z
    return [_gam(3.2409699419 * x - 1.5373831776 * y - 0.4986107603 * z),
            _gam(-0.9692436363 * x + 1.8759675015 * y + 0.0415550574 * z),
            _gam(0.0556300797 * x - 0.2039769589 * y + 1.0569715142 * z)]


def _tohex(rgb):
    return "#" + "".join("%02x" % round(min(1, max(0, v)) * 255) for v in rgb)


def norm_color(v):
    v = (v or "").strip()
    # A percentage alpha ("/ 50%", "rgba(..., 50%)") becomes the 0-1 number the
    # patterns below read; without this the colour passed through unconverted.
    v = re.sub(r"(/\s*|^rgba\([^,]+,[^,]+,[^,]+,\s*)([\d.]+)%\)$", lambda m: f"{m.group(1)}{float(m.group(2)) / 100:g})", v)
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    m = re.fullmatch(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)", v)
    if m:
        r, g, b = (round(float(x) * 255) for x in m.group(1, 2, 3))
        a = m.group(4)
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (r, g, b)
        return f"rgba({r}, {g}, {b}, {'%g' % float(a)})"
    m = re.fullmatch(r"(ok)?lab\(([-\d.e]+%?)\s+([-\d.e]+)\s+([-\d.e]+)(?:\s*/\s*([\d.]+))?\)", v)
    if m:
        ok, L, A, B, al = m.groups()
        # lab() carries L in the 0-100 range (the % is notation); oklab() uses 0-1.
        Lf = (float(L[:-1]) * (0.01 if ok else 1)) if L.endswith("%") else float(L)
        rgb = _oklab(Lf, float(A), float(B)) if ok else _lab(Lf, float(A), float(B))
        h = _tohex(rgb)
        if al is None or float(al) >= 1:
            return h
        r, g, b = (int(h[i:i + 2], 16) for i in (1, 3, 5))
        return f"rgba({r}, {g}, {b}, {'%g' % float(al)})"
    m = re.fullmatch(r"oklch\(([-\d.e]+)\s+([-\d.e]+)\s+([-\d.e]+|none)(?:\s*/\s*([\d.]+|none))?\)", v)
    if m:
        import math
        L, Cc, H, al = m.groups()
        H = 0.0 if H == "none" else float(H)
        A, B = float(Cc) * math.cos(math.radians(H)), float(Cc) * math.sin(math.radians(H))
        h = _tohex(_oklab(float(L), A, B))
        if al in (None, "none") or float(al) >= 1:
            return h
        r, g, b = (int(h[i:i + 2], 16) for i in (1, 3, 5))
        return f"rgba({r}, {g}, {b}, {'%g' % float(al)})"
    return v


# One value -> token map per theme. A dark-group component (measured under
# .dark) is labelled from core + dark, never from the light set: #fafafa is
# light.primary.foreground but dark.foreground. THEME is set per component.
BY_THEME = {}
for _theme in ("light", "dark"):
    _m = BY_THEME[_theme] = {}
    for _set in ("core", _theme):
        for n, t in flat(T.get(_set, {})):
            if t["$type"] == "color":
                _m.setdefault(norm_color(t["$value"]), n if _set == "core" else f"{_set}.{n}")
THEME = "light"


def theme_of(c):
    return "dark" if (c.get("group") or "").startswith("Dark theme") else "light"


# Every colour expression the readings carry; each is normalised to #hex or
# rgba() before the BY_COLOR token lookup.
COL_EXPR = re.compile(r"color\(srgb [^)]*\)|oklch\([^)]*\)|(?:ok)?lab\([^)]*\)|rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}")


def colour(c, tokens=True):
    """Any colour expression -> '#hex `token`' or 'rgba(...)'."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        tok = BY_THEME[THEME].get(v) if tokens else None
        return f"{v} `{tok}`" if tok else v

    return COL_EXPR.sub(lambda m: label(norm_color(m.group(0))), c)


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
            bits.append(" ".join(x for x in (pe, colour(p["backgroundColor"]) if p.get("backgroundColor") else None,
                                             p.get("borderTopWidth"), colour(p["boxShadow"]) if p.get("boxShadow") else None,
                                             p.get("opacity")) if x))
    # A root box-shadow (e.g. the 1px focus ring gained on focus-visible) does
    # not remove the painted children: keep reporting their layers, which is
    # where a state-carrying child outline (the 3px cyan CTA ring) shows up.
    if s["backgroundColor"] == "rgba(0, 0, 0, 0)" and s["borderTopWidth"] == "0px" and s["backgroundImage"] == "none":
        for p in v.get("paint", [])[:6]:
            bits.append(" ".join(x for x in (p["node"], p.get("size"),
                                             colour(p["bg"]) if p.get("bg") else None,
                                             colour(p["border"]) if p.get("border") else None,
                                             colour(p["shadow"]) if p.get("shadow") else None,
                                             colour(p["outline"]) if p.get("outline") else None,
                                             p.get("radius")) if x))
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

# Entries whose selector caught another control. The readings stay as
# evidence of what was read, but the entry says so (README, What to distrust).
WRONG_ELEMENT = {
    "composer-send": "These readings are the composer's \"Add to prompt\" attach button, not the send control: the selector's `form button` fallback matched it first. Recapture needed.",
}

PAGE_NAME = {"home": "home", "pricing": "pricing", "contact": "contact", "toolgen": "AI image generator",
             "models": "models", "radar": "radar", "brand": "brand", "blog": "blog", "docs": "docs",
             "mcp": "MCP", "mobile": "home"}

GROUP_INTRO = {
    "Shell and navigation": "The marketing chrome: the logo mark, flat nav links, Sign in and the dark Sign-up-for-free pill on the near-white field. The desktop header has no dropdown menu; the nav is plain links at every width it was captured.",
    "Home hero": "The home hero: the display headline and the Ask-Endless prompt composer with its model pill, send control and prompt chips. Nothing was ever sent.",
    "Home": "Sections of the home page.",
    "Pricing": "The pricing surface: the Monthly/Annual billing segment, the shared-credits slider, the plan cards with their CTAs and the FAQ rows.",
    "Contact form": "The contact/sales form, measured but never submitted: text, email and company inputs, the message textarea and the Send-message button.",
    "AI image generator (free tool)": "One of the ~70 free tool pages: the prompt field and the Generate-the-image submit — measured, never run.",
    "Model catalog": "The /models grid: search, the modality tabs and the model cards.",
    "Radar trends": "The social radar: live trend rows, Copy buttons and Find-out-why actions.",
    "Brand kit": "The /brand asset page: logo blocks, swatches and the Copy/Download buttons — measured, never downloaded.",
    "Docs shell": "/docs is a separate documentation shell with its own sidebar and Search button, inside the same token layer.",
    "MCP page": "The /mcp page: install code blocks and their Copy buttons.",
    "Blog": "The /blog index: category pills and post cards.",
    "Footer": "The marketing footer: link columns, legal, and the Cookie-settings and Theme controls.",
    "Dark theme (system dark)": "The same home chrome re-measured under emulated prefers-color-scheme dark — the trigger next-themes honours, so these are the values a dark-system visitor gets.",
    "Mobile (390 wide)": "The marketing surface at phone width: the compact header, the menu overlay and the stacked hero.",
}

SHOTS = [
    ("home", "Home", "/"),
    ("pricing", "Pricing", "/pricing"),
    ("contact", "Contact", "/contact"),
    ("tools", "Tools index", "/tools"),
    ("toolgen", "AI image generator (a free tool)", "/tools/ai-image-generator"),
    ("models", "Model catalog", "/models"),
    ("model-index", "Model index (pricing table)", "/model-index"),
    ("blog", "Blog index", "/blog"),
    ("brand", "Brand kit", "/brand"),
    ("docs", "Documentation shell", "/docs"),
    ("radar", "Social radar", "/radar"),
    ("mcp", "MCP server", "/mcp"),
    ("about", "About", "/about"),
    ("industries", "Industries", "/industries"),
    ("compare", "Compare", "/compare"),
    ("status", "Status", "/status"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "/"),
    ("mobile-pricing", "Pricing, phone", "/pricing"),
    ("mobile-toolgen", "AI image generator, phone", "/tools/ai-image-generator"),
    ("mobile-models", "Models, phone", "/models"),
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

W("# Endless components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from endless.app (what endless.io redirects to) on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. endless.app is one Next.js surface — marketing pages, ~70 free tools, the model catalog, social radar, /docs and /brand — over a single shadcn-style token layer (TikTok Sans + Geist Mono). Nothing was signed into, sent, generated, downloaded or submitted; the contact form and every tool's prompt field were never filled past a deleted sample; sign-in (clerk.endless.app) and sign-up (s.endless.app) were never followed.")
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
W("Screenshots are named `{page}-{theme}-state.png`: the site paints `light` on a light system and `dark` on a dark one (the `-dark` shots emulate prefers-color-scheme, the same trigger next-themes honours). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).")
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
    ("Mobile menu overlay", "home, phone width", "the hamburger button's own toggle", "[mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open)"),
    ("Desktop header menu", "every marketing page", "not present: the desktop header is flat nav links, the Menu button only paints at phone width", "[nav-dropdown](#nav-dropdown) recorded missing"),
    ("Composer focus", "home", "clicking into the Ask-Endless textarea (nothing typed or sent)", "[home-light-composer](screenshots/home-light-composer.png), [composer-input](#composer-input)"),
    ("Billing segment", "/pricing", "the Monthly/Annual toggle's own press", "[pricing-light-annual](screenshots/pricing-light-annual.png), [billing-toggle](#billing-toggle)"),
    ("Field focus", "/contact, free tools", "clicking into a field; sample text typed and deleted, nothing sent", "[contact-light-field](screenshots/contact-light-field.png), [toolgen-light-prompt](screenshots/toolgen-light-prompt.png)"),
    ("Consent/chat overlays", "every page", "hidden, never answered (no consent button was ever clicked, no consent POST sent)", "hidden before every shot and reading"),
    ("Signed-in workspace", "s.endless.app; auth on clerk.endless.app", "the product's chat workspace lives behind sign-in", "boundary; see Gaps"),
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
    THEME = theme_of(c)
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
for k in ["composer", "plan-card", "contact-form", "tool-panel", "model-card", "blog-card", "brand-logo-block", "docs-sidebar", "mcp-code"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    THEME = theme_of(c)
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
        THEME = theme_of(c)
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
        if k in WRONG_ELEMENT:
            W(f"**Wrong element.** {WRONG_ELEMENT[k]}")
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Endless mark, tool glyphs, model tiles and illustrations) are the product's artwork. Declared under layoutGaps in the catalog entry.")
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
W("Endless's product — the chat workspace, canvas, projects, files, MCP connections and billing — lives behind sign-in (auth on clerk.endless.app, the app at s.endless.app) and was never reached. The public surface was captured fully: the marketing pages, the free tool pages (their prompt fields were measured, never submitted — a tool page renders a quota card signed out), the model catalog, radar, docs and brand.")
W()
W("### Pages")
W()
W("- **The workspace.** Every post-login surface (chat, canvas, projects, automations, settings) needs an account and was never reached; Sign-in and Sign-up-for-free were measured, never followed.")
W("- **Tool results.** The free tools render their prompt field signed out, but pressing Generate was never done — the generated image/audio/video outputs are uncaptured.")
W("- **Checkout and onboarding.** Every Start-free, Get-started and plan CTA was measured, never followed past its public landing; /contact was never submitted.")
W("- **Model and tool detail pages.** The indexes were captured; ~70 tool pages and ~20 model detail pages share the same shell — one representative tool (/tools/ai-image-generator) and the catalog were measured, the rest are recorded as same-family.")
W("- **Radar detail.** /radar/trends/<country> and /radar/tiktok/<country> deep links exist; the index was captured.")
W("- **Localized routes.** /de, /es, /fr, /pt serve the same marketing surface in other languages; only English was captured.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Disabled, error and loading states** were not seen on the public surface.")
W("- **Menu and dropdown states**: the desktop header has no dropdown (flat links; the menu is a phone-width overlay, captured open); nav-dropdown and menu-link are recorded missing.")
W()
W("### Themes")
W()
W("endless.app paints light on a light system and dark on a dark one via next-themes (a `.dark` class on the html element that re-binds every semantic role; a footer Theme control writes the same class). The `-dark` shots and the dark component group were taken under emulated prefers-color-scheme dark — the same trigger the site honours — so they are the theme a dark-system visitor gets, not a reconstruction.")
W()
W("### Fonts")
W()
W("- **TikTok Sans** (the UI sans) and **Geist Mono** (code and code blocks) are the served faces, via next/font; the style guide falls back to system sans and mono.")
W()
W("### Screenshots")
W()
W("- Product illustrations, tool previews, model tiles and the Endless artwork in the screenshots are the product's published content.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Marketing copy, blog posts, tool descriptions and radar trend text are the product's content; only frames and components were measured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
