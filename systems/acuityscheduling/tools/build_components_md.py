#!/usr/bin/env python3
"""Build components.md for the Acuity Scheduling design reference.

Reads raw/components-computed.json (every component and state, measured), tokens.json,
screenshots/ and components/crops/, and writes components.md next to them. Every value is a cell
of the measurement file, condensed: colours are hex followed by the token in tokens.json whose
value is the same, the font family is named once per value, and a state row shows only what
differs from the first state. One theme only: the marketing site and account gate paint a single light scheme.

Deterministic: re-running it on the same inputs reproduces components.md byte for byte.
Run from anywhere: python3 tools/build_components_md.py
"""
import collections, json, os, re
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


def resolved(v, depth=0):
    while isinstance(v, str) and v.startswith("{") and depth < 12:
        node = None
        for tree in (T["light"], T["core"]):
            n = tree
            for k in v[1:-1].split("."):
                n = n.get(k) if isinstance(n, dict) else None
            if isinstance(n, dict) and "$value" in n:
                node = n
                break
        if node is None:
            return v
        v, depth = node["$value"], depth + 1
    return v


BY_COLOR = {}
for theme in ("core", "light"):
    for n, t in flat(T[theme]):
        if t["$type"] == "color":
            v = resolved(t["$value"])
            if not isinstance(v, str) or v.startswith("{"):
                continue
            BY_COLOR.setdefault(v, []).append(n)

# Which token a colour is named after depends on what it paints: a fill prefers the component and
# surface names, a border the border names, text the text names.
PREFER = {
    "bg": ["surface-", "surface", "page", "palette.", "component.", "overlay", "disabled-bg", "accent"],
    "border": ["border-", "border", "palette.line", "palette.", "component."],
    "text": ["text-", "text", "muted", "link", "accent", "disabled-text", "palette.", "component."],
    "icon": ["text-", "text", "palette.", "component."],
}


def pick(names, role):
    order = PREFER.get(role, PREFER["bg"])
    def rank(n):
        for i, pre in enumerate(order):
            if n == pre or (pre.endswith((".", "-")) and n.startswith(pre)):
                return (i, len(n), n)
        return (len(order), len(n), n)
    return sorted(names, key=rank)[0]


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), round(float(a), 2))


def colour(c, tokens=True, role="bg"):
    """rgb()/rgba() -> '#hex `token`' or 'rgba(...)'."""
    def label(v):
        if re.fullmatch(r"rgba\(\d+, \d+, \d+, 0\)", v):
            return "transparent"
        names = BY_COLOR.get(v) if tokens else None
        return f"{v} `{pick(names, role)}`" if names else v

    return re.sub(r"rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)",
                  lambda m: label(norm(*m.group(1, 2, 3), m.group(4))), c or "")


def sides(t, r, b, l):
    if t == r == b == l:
        return t
    if t == b and r == l:
        return f"{t} {r}"
    return f"{t} {r} {b} {l}"


def fam(f):
    first = (f or "").split(",")[0].replace('"', "").strip()
    return {"Clarkson-Serif": "Clarkson Serif", "Clarkson Serif": "Clarkson Serif"}.get(first, first)


def num(x):
    return re.sub(r"(\d+\.\d\d)\d+", r"\1", str(x))


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
            bds.append(f"{s[f'border{d}Width']} {s[f'border{d}Style']} {colour(s[f'border{d}Color'], role='border')}")
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
    if s.get("backdropFilter", "none") != "none":
        o["backdrop"] = s["backdropFilter"]
    if s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0:
        o["outline"] = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'], role='border')}, offset {s['outlineOffset']}"
    t = v.get("textStyle")
    if t:
        o["text"] = f"{font(t['fontSize'], t['lineHeight'], t['fontWeight'], t['fontFamily'])}, {colour(t['color'], role='text')}"
    elif v.get("text"):
        o["text"] = f"{font(s['fontSize'], s['lineHeight'], s['fontWeight'], s['fontFamily'])}, {colour(s['color'], role='text')}"
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
            o["transition"] = ", ".join(parts) if len(parts) < 4 else f"{parts[0].split(' ')[0]} and {len(parts) - 1} more {' '.join(parts[0].split(' ')[1:])}"
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
    if v.get("placeholder"):
        o["placeholder"] = colour(v["placeholder"]["color"], role="text")
    return o


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "backdrop", "outline", "text", "transition", "transform", "opacity", "icon", "placeholder"]


def layer_diff(a, b):
    """Changes in the parts props() does not carry: child paint layers,
    ::before/::after and text decoration, so a visible hover/focus change on a
    child is not reported as 'same'."""
    out = {}
    for pe in ("::before", "::after"):
        pa, pb = a.get(pe), b.get(pe)
        if pa != pb:
            bits = []
            for k in ("backgroundColor", "boxShadow", "borderTopColor", "borderTopWidth", "opacity", "content"):
                va, vb = (pa or {}).get(k), (pb or {}).get(k)
                if va != vb:
                    bits.append(f"{k} {colour(str(vb), role='border') if vb else 'none'}")
            if bits:
                out[pe] = "; ".join(bits[:3])
    ta, tb = a.get("style", {}), b.get("style", {})
    for k in ("textDecorationLine", "textDecorationColor", "textDecorationThickness", "textUnderlineOffset"):
        if ta.get(k) != tb.get(k):
            out["decoration"] = f"{k} {tb.get(k)}"
    pa, pb = a.get("paint"), b.get("paint")
    if pa != pb:
        ch = []
        for x, y in zip(pa or [], pb or []):
            for f in ("bg", "border", "shadow", "outline", "bgImage"):
                if x.get(f) != y.get(f):
                    ch.append(f"{x['node'].split('.')[0]} {f} {colour(str(y[f]), role='border') if y[f] else 'none'}")
                    break
        if (pa or [])[(len(pb or [])):] or (pb or [])[len(pa or []):]:
            ch.append("layer added or removed")
        if ch:
            out["layers"] = "; ".join(ch[:3])
    return out


LAYER_ORDER = ["::before", "::after", "decoration", "layers"]
ALL_ORDER = ORDER + LAYER_ORDER


def state_rows(c):
    """The first state lists every value; later rows list only what changed."""
    rows = []
    states = [s for s, v in c["states"].items() if "style" in v]
    if not states:
        return rows
    base = props(c["states"][states[0]])
    rows.append((states[0], base))
    same = []
    for st in states[1:]:
        v = c["states"][st]
        p = props(v)
        diff = {k: p[k] for k in ORDER if k in p and p.get(k) != base.get(k)}
        for k in ORDER:
            if k in base and k not in p:
                diff[k] = "none"
        diff.update(layer_diff(c["states"][states[0]], v))
        if not diff:
            same.append(st)
            continue
        if rows[-1][0] != states[0] and rows[-1][1] == diff:
            rows[-1] = (rows[-1][0] + ", " + st, diff)
        else:
            rows.append((st, diff))
    if same:
        rows[0] = (f"{states[0]} (same: {', '.join(same)})", base)
    return rows


def fmt(d):
    return "; ".join(f"{k} {d[k]}" for k in ALL_ORDER if k in d).replace("|", "/")


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
        if p.get("border"):
            bits.append("border " + colour(p["border"].split(" | ")[0][2:], role="border"))
        if p.get("radius"):
            bits.append("radius " + p["radius"])
        if p.get("shadow"):
            bits.append("shadow " + colour(p["shadow"]))
        if p.get("bgImage"):
            bits.append("image " + colour(p["bgImage"])[:120])
        out.append(" ".join(bits))
    return "; ".join(out).replace("|", "/")


# --------------------------------------------------------------------------- page and group text

GROUP_INTRO = {
    "Shell and navigation": "The 80px white bar every marketing page shares (55px at 390): the acuity:scheduling wordmark left, How It Works / Solutions / Product / Resources (the last three open mega-menu panels) / Pricing centre, Log in and the ink Get started pill right. Links are Clarkson 14/18.76; hover fades them to 50% opacity.",
    "Home": "The home page: a pastel gradient hero (nine declared variants rotate; the capture shows one) with a serif headline and two ghost signup CTAs, the cream industry cards, a grey feature card with an ink CTA, the auto-playing lavender testimonial carousel, and the pale-blue bottom band holding the navy support card and a tall ink CTA.",
    "Footer": "The white page foot: 'Get Started' link columns in Clarkson 16/18.4 titles and 12px links, the social icon circles, then the legal row under a hairline. Footer links underline on hover.",
    "Pricing": "The pricing page: a photographic hero band (a background image, not a flat fill) with the serif headline and the white-pill annual/monthly segment, three white plan cards on 1px hairlines with ink Start-free-trial buttons, then the navy FAQ accordion with white rows.",
    "Auth gate (Squarespace)": "Squarespace's shared account surface: /get-started lands on a white 'Create your account' dialog (Continue with Google/Apple/Email rows on 1px black rules, MORE OPTIONS caps toggle) and secure.acuityscheduling.com/login on the sign-in card with underlined fields, a greyed LOG IN and the same OAuth rows. Measured and state-forced, never submitted.",
    "Mobile (390 wide)": "The same site at 390: the bar collapses to wordmark plus hamburger, which opens a full-height white sheet over a 50% scrim — 28px Clarkson links on hairline rows, an ink Get started bar and a Log in. Focus inside the sheet is an amber ring.",
}

PAGE_DESC = [
    ("home", "Home. The gradient hero, industry cards, feature card, testimonial carousel, support card and footer. Captured at rest, with the Solutions mega-menu open, and full-page.", "/"),
    ("pricing", "Pricing. The plan cards, segment toggle and navy FAQ. Captured at rest, with the first FAQ open, and full-page.", "/pricing"),
    ("how-it-works", "How Acuity works.", "/features/how-acuity-works"),
    ("features", "The features index.", "/features"),
    ("solutions", "The solutions index.", "/solutions"),
    ("beauty", "An industry page (Beauty).", "/solutions/beauty"),
    ("about", "The about page.", "/about"),
    ("learn", "The Learn resources page.", "/learn"),
    ("get-started", "Get started, which lands on Squarespace's public 'Create your account' gate. Captured at rest and with MORE OPTIONS open.", "/get-started?type=professional"),
    ("login", "Log in, which redirects to Squarespace's public sign-in page. Captured at rest only.", "https://secure.acuityscheduling.com/login?nav=1"),
]
MOBILE_DESC = [
    ("mobile-home", "Home at 390: collapsed bar, the hamburger menu open, and full-page.", "/"),
    ("mobile-pricing", "Pricing at 390.", "/pricing"),
]

L = []


def W(s=""):
    L.append(s)


shots = sorted(p.name for p in Path("screenshots").glob("*.png"))


def links(prefix):
    out = []
    for f in shots:
        m = re.fullmatch(re.escape(prefix) + r"-(dark|light)-(.+)\.png", f)
        if m:
            out.append(f"[{m.group(2)} ({m.group(1)})](screenshots/{f})")
    return ", ".join(out)


n_crops = len(list(Path("components/crops").glob("*.png")))
n_states = sum(len(c["states"]) for c in C.values())

W("# Acuity Scheduling components")
W()
W(f"The discovery list of every page and state captured, then one entry per component with crops of the real site, the shared values and the Gaps. Captured from acuityscheduling.com on 2026-11-09 and 2026-11-10, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was submitted, bought or signed into; the only presses were local UI toggles (the nav mega-menu, the pricing FAQ accordion, the mobile hamburger, the gate's MORE OPTIONS). Consent SDKs were aborted at request level, so no consent button was ever mounted or pressed — a hide, not a consent.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the token in [tokens.json](tokens.json) whose value is the same, when there is one. Text is written family size/line-height weight, then its colour, for example `Clarkson 14/22 500, #0e0e0e`, and is read from the first text node inside the component.")
W("- The first state of each entry lists every value; later states list only what changed. A state identical to the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at the same width; mobile shots are `mobile-{page}-light-{state}.png`, 390 x 844 at 2x. Only light exists — the marketing site and the gate have no dark theme.")
W()
W("| Surface | URL | Screenshots |")
W("|---|---|---|")
for p, desc, url in PAGE_DESC + MOBILE_DESC:
    W(f"| {desc} | `{url}` | {links(p)} |")
W()
W("### Overlays and transient states")
W()
W("| State | Where | How it was reached | Captured |")
W("|---|---|---|---|")
OVER = [
    ("Solutions mega-menu", "home", "hover on the Solutions nav trigger (a local disclosure)", "[home-light-dropdown](screenshots/home-light-dropdown.png), [nav-dropdown](#nav-dropdown), [dropdown-item](#dropdown-item)"),
    ("Pricing FAQ, first answer open", "pricing", "the accordion row's own toggle", "[pricing-light-faq-open](screenshots/pricing-light-faq-open.png), [accordion-title-open](#accordion-title-open), [accordion-panel](#accordion-panel)"),
    ("Mobile menu sheet", "home at 390", "the hamburger button", "[mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu](#m-menu), [m-menu-link](#m-menu-link)"),
    ("MORE OPTIONS, open", "get-started", "the caps toggle on the account gate", "[get-started-light-more-options](screenshots/get-started-light-more-options.png), [more-options-open](#more-options-open)"),
    ("Form focus and fill", "the login card", "tabbed into and typed (sample text, deleted; nothing sent)", "[login-email](#login-email), [login-password](#login-password)"),
]
for row in OVER:
    W("| " + " | ".join(row) + " |")
W()


# --------------------------------------------------------------------------- shared values

W("## Shared values")
W()
W("Values that apply across entries, tallied from the measurement file.")
W()
radii = collections.Counter()
trans = collections.Counter()
hovers = collections.Counter()
focus = collections.Counter()
focus_n = 0
for cid, c in C.items():
    for sname, s in c["states"].items():
        if "style" not in s:
            continue
        st = s["style"]
        r = st["borderTopLeftRadius"]
        if r != "0px" and s["rect"]["w"] > 4:
            radii[r] += 1
        if st["transitionDuration"] not in ("0s", ""):
            tf = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", st["transitionTimingFunction"])
            trans[f"{st['transitionDuration'].split(',')[0].strip()} {tf[0] if tf else st['transitionTimingFunction']}"] += 1
        if sname == "focus-visible":
            focus_n += 1
            if st["outlineStyle"] != "none" and float(st["outlineWidth"].replace("px", "")) > 0:
                focus[f"{st['outlineWidth']} {st['outlineStyle']} {colour(st['outlineColor'], role='border')} offset {st['outlineOffset']}"] += 1
            else:
                focus["no ring on the element"] += 1
for cid, c in C.items():
    a, b = c["states"].get("default"), c["states"].get("hover")
    if not a or not b or "style" not in a or "style" not in b:
        continue
    if a["style"]["backgroundColor"] != b["style"]["backgroundColor"]:
        hovers[f"{colour(a['style']['backgroundColor'])} to {colour(b['style']['backgroundColor'])}"] += 1
    elif a["style"]["color"] != b["style"]["color"]:
        hovers[f"text {colour(a['style']['color'], role='text')} to {colour(b['style']['color'], role='text')}"] += 1
    elif a["style"]["borderTopColor"] != b["style"]["borderTopColor"]:
        hovers[f"border {colour(a['style']['borderTopColor'], role='border')} to {colour(b['style']['borderTopColor'], role='border')}"] += 1
    else:
        hovers["no change on the element"] += 1


def top(ctr, n):
    return ", ".join(f"{k} ({v})" for k, v in ctr.most_common(n))


W(f"**Radius.** {top(radii, 8) if radii else 'none'}. The 12px step is the signature: nav pill, hero CTAs, plan buttons, the bottom CTA and the plan cards share it.")
W()
W(f"**Hover.** {top(hovers, 8)}. Links fade to 50% opacity or gain an underline rather than recolouring; the ink fills split — the header pill lightens to {colour('rgb(62, 87, 114)')} while the plan button darkens to {colour('rgb(30, 45, 58)')}.")
W()
W(f"**Focus.** Of {focus_n} elements given a real keyboard focus: {top(focus, 6)}. Links and accordions take Chromium's 1px {colour('rgb(0, 95, 204)', role='border')} auto ring; the mobile menu's controls draw {colour('rgb(229, 151, 0)', role='border')} amber; the gate's buttons paint a double box-shadow ring (2px white, 4px black); plan-cta draws a 2px solid {colour('rgb(40, 56, 73)', role='border')} ring offset 2px.")
W()
W(f"**Motion.** {top(trans, 6) if trans else 'Instant: no measured control carries a transition'}. The blanket step is 50ms ease on links and gate rows; the header pill takes 150ms ease-in; the mega-menu opens over 250ms ease-in-out.")
W()
W("**Layout.** The desktop bar is an 80px rail (55px at 390; the open mobile menu's header block 104px). Controls come in four heights: the 42.8px nav pill, 46px plan buttons, 55px gate/OAuth rows and the 56px hero CTAs (the bottom CTA stretches to 72px). The mega-menu panel pads 44px at a 22px radius; the FAQ column is 640px; plan cards are ~449px across on 1px #e4e4e4 hairlines.")
W()
W("**Accent.** Navy ink #283849 does all the work: every primary button fill, the serif headlines' colour, the hero ghost CTAs' 1px rules, the FAQ band and the support card. There is no bright accent at all — the loudest secondary is the pale-blue #e0ebf4 bottom band and the lavender #d6d0ed testimonial card.")
W()


# --------------------------------------------------------------------------- components

W("## Components")
W()
groups = collections.OrderedDict()
for cid, c in C.items():
    groups.setdefault(c["group"], []).append(cid)
for g, ids in groups.items():
    W(f"### {g}")
    W()
    if g in GROUP_INTRO:
        W(GROUP_INTRO[g])
        W()
    for cid in ids:
        c = C[cid]
        W(f"#### {c['title']}")
        W()
        W(f"<a id=\"{cid}\"></a>`{cid}`, on {c['page']}. {c.get('desc', '')}".rstrip())
        W()
        if c.get("missing"):
            W("*Not found on the captured pages — an honest miss, kept so the gap is visible.*")
            W()
            continue
        crops = []
        order = ("default", "hover", "focus-visible", "pressed", "focused", "filled", "selected", "open")
        for sname in [n for n in order if n in c["states"]] + sorted(n for n in c["states"] if n not in order):
            s = c["states"].get(sname)
            if s and s.get("crop") and Path(s["crop"]).exists():
                crops.append(f'<img src="{s["crop"]}" alt="{c["title"]}, {sname}" height="{min(120, max(24, round(s["rect"]["h"])))}"> ')
        if crops:
            W("".join(crops))
            W()
        rows = state_rows(c)
        if rows:
            W("| State | Values |")
            W("|---|---|")
            for name, d in rows:
                W(f"| {name} | {fmt(d)} |")
            W()
        cl = child_layers(c)
        if cl:
            W(f"Child layers: {cl}")
            W()

# --------------------------------------------------------------------------- gaps

W("## Gaps")
W()
W("- `carousel-nav` and `login-card` are honest misses: the testimonials carousel has no arrow buttons (a dotted indicator row only, see `carousel-dots`), and the login card's own wrapper element could not be isolated — its children (fields, submit, OAuth rows) are measured instead.")
W("- Everything behind the sign-in is out of bounds: the scheduling app itself, account creation, checkout, the OAuth redirects. The gate and login card were measured and state-forced but never submitted, and no account exists to continue into.")
W("- `social-link` and `m-menu-link`'s pressed rows show `rgb(255, 0, 0)`: those anchors carry no `color` of their own (default link blue `rgb(0, 0, 238)` at rest), so the forced `:active` falls back to the UA stylesheet's red. It is a measurement artifact of unstyled anchors, not a design value.")
W("- The pricing hero's dark band is a background photograph (`pricing-background.webp`), not a flat fill — its sampled pixels (~#334e53) are image content. Likewise the home hero repaints one of nine declared pastel gradient variants per load (raw/css-vars.json); the tokens record the variant live during the capture.")
W("- `plan-card` itself paints transparent: the white card with the hairline border and 12px radius is its `.plan-wrapper` sibling, which the paint layers record.")
W("- The testimonials carousel auto-plays, so `testimonial-card` is measured on its first slide only and two captures of the same section can differ.")
W("- Consent SDKs (OneTrust/Cookiebot) were aborted at the network layer before any banner mounted, so no consent UI was captured or measured — there was nothing to hide after the fact.")
W("- Disabled, error, loading and selected states barely exist on the public surface: the disabled LOG IN (`field-disabled-bg`) is the only disabled control captured; error and loading states live behind submitted forms and were never reached.")
W()

open("components.md", "w").write("\n".join(L) + "\n")
print(f"components.md: {len(C)} components, {n_states} states, {n_crops} crops, {len(L)} lines")
