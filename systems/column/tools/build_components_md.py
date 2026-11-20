#!/usr/bin/env python3
"""Build components.md for the Column design reference.

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
    # A focus ring or fill can be painted by an ancestor (sites draw a
    # field's focus ring on its wrapper), so parent-drawn changes belong in
    # the state diff or a focused state reads as unchanged.
    wrap = []
    for a in v.get("ancestors") or []:
        bits = []
        if a.get("shadow") and a["shadow"] != "none":
            layers = [x.strip() for x in re.split(r",(?![^(]*\))", colour(a["shadow"], tokens=False))]
            layers = [x for x in layers if not x.startswith("transparent") and not re.match(r"rgba?\(0, 0, 0, 0\)", x)]
            if layers:
                bits.append("shadow " + ", ".join(layers))
        if a.get("outline"):
            bits.append("outline " + colour(a["outline"], tokens=False))
        if bits:
            wrap.append(f"{a['node']}: " + "; ".join(bits))
    if wrap:
        o["wrapper"] = " / ".join(wrap)
    return o


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "outline", "wrapper", "text", "transition", "transform", "opacity", "icon", "placeholder", "child paint"]


def paint_sig(v):
    """(node, size, bg, bgImage, border, radius, shadow, outline, opacity) per
    painted child or pseudo layer — sites repaint these on state changes
    without touching the root's computed style, so they must join the state
    diff. The element-level ::before/::after blocks are appended too: they
    carry opacity, which the descendant paint layers do not record."""
    sig = [
        (p.get("node"), p.get("size"), p.get("bg"), p.get("bgImage"), p.get("border"), p.get("radius"), p.get("shadow"), p.get("outline"), p.get("opacity"))
        for p in (v.get("paint") or [])
    ]
    for pe in ("::before", "::after"):
        pb = v.get(pe)
        if pb:
            sig.append((
                "el" + pe,
                f"{pb.get('width')}x{pb.get('height')}",
                pb.get("backgroundColor") if pb.get("backgroundColor") != "rgba(0, 0, 0, 0)" else None,
                None, None,
                pb.get("borderRadius") if pb.get("borderRadius") != "0px" else None,
                pb.get("boxShadow") if pb.get("boxShadow") != "none" else None,
                None, pb.get("opacity"),
            ))
    return sig


def paint_diff(cur, base):
    """Describe the painted layers that changed vs the base state, by node. A
    layer that only exists in this state is listed with its attributes. Nodes
    repeat (two children can share a node label), so layers pair off by
    occurrence order within the node, not by node alone."""
    bmap = {}
    for p in base:
        bmap.setdefault(p[0], []).append(p[1:])
    seen = {}
    out = []
    for node, *vals in cur:
        idx = seen.get(node, 0)
        seen[node] = idx + 1
        olds = bmap.get(node)
        old = olds[idx] if olds and idx < len(olds) else None
        fields = ("size", "bg", "bgImage", "border", "radius", "shadow", "outline", "opacity")
        bits = []
        if old is None:
            vals_to_show = vals
        else:
            vals_to_show = tuple(nv if nv != bv else None for nv, bv in zip(vals, old))
            if not any(vals_to_show):
                continue
        for f, nv in zip(fields, vals_to_show):
            if not nv:
                continue
            if f == "bg":
                bits.append("background " + colour(nv))
            elif f == "border":
                bits.append("border " + colour(str(nv).split(" | ")[0][2:]))
            elif f == "outline":
                bits.append("outline " + nv)
            else:
                bits.append(f"{f} {nv}")
        out.append(f"{node}: " + "; ".join(bits or ["changed"]))
    return "; ".join(out)


def measured(v):
    """A state with a real reading: not skipped, not a focus that never landed (via "focus failed"), not a
    focus that did not match :focus-visible. Those are the element at rest (the kit's rule, PR 932)."""
    return "style" in v and not v.get("skipped") and "failed" not in str(v.get("via", "")) and (v.get("focus") or {}).get("matches") is not False


def state_rows(c):
    states = [s for s in c["states"] if "failed" not in str(c["states"][s].get("via", ""))]
    good = [s for s in states if measured(c["states"][s])]
    if not good:
        return ([(", ".join(states), {"size": "unmeasured — the capture failed on this pass"})] if states else []), states
    base = props(c["states"][good[0]])
    base_paint = paint_sig(c["states"][good[0]])
    rows = [(good[0], base)]
    same = []
    for st in good[1:]:
        p = props(c["states"][st])
        diff = {k: p[k] for k in ORDER if k in p and p.get(k) != base.get(k)}
        pd = paint_diff(paint_sig(c["states"][st]), base_paint)
        if pd:
            diff["child paint"] = pd
        for k in ORDER:
            if k in base and k not in p:
                diff[k] = "none"
        if not diff:
            same.append(st)
            continue
        if rows[-1][0] != good[0] and rows[-1][1] == diff:
            rows[-1] = (rows[-1][0] + ", " + st, diff)
        else:
            rows.append((st, diff))
    if same:
        rows[0] = (f"{good[0]} (same: {', '.join(same)})", base)
    missed = [s for s in states if not measured(c["states"][s])]
    if missed:
        rows.append((", ".join(missed), {"size": "unmeasured — the capture failed on this pass"}))
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
        bits = [re.sub(r"\..*$", "", p["node"]) if "::" not in p["node"] else p["node"].split(".")[0], re.sub(r"\.0+(?=\D|$)", "", p["size"].replace(".0x", "x"))]
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

PAGE_NAME = {"home": "home", "ach": "ACH", "cardprograms": "card programs", "signin": "sign-in"}

GROUP_INTRO = {
    "Shell and navigation": "The launch announcement banner and the fixed site nav: the Column mark, the mega-menu nav triggers, the Sign-in link, the \"Get started\" ghost and the navy Sign-up button.",
    "Home": "The hero (\"Move, hold, and lend the dollar at scale\"), the stat figures, and the near-black navy infrastructure band inside the light page.",
    "ACH page": "The /ach product route: its headline, a SectionBox content card and the rendered product-UI mock (ProductScreen).",
    "Card programs page": "The /card-programs product route: its headline and first CTA.",
    "App sign-in (boundary)": "dashboard.column.com/login — the product's public login surface, measured at rest; nothing was typed, signed into or submitted.",
    "Footer": "The light-grey closer band at the page bottom: link columns, the Column logo block and legal copy.",
    "Mobile (390 wide)": "The same surface at phone width: the collapsed bar and the open menu overlay.",
}

SHOTS = [
    ("home", "Home", "/"),
    ("ach", "ACH", "/ach/"),
    ("bankaccounts", "Bank accounts", "/bank-accounts/"),
    ("booktransfers", "Book transfers", "/book-transfers/"),
    ("cardprograms", "Card programs", "/card-programs/"),
    ("checks", "Checks", "/checks/"),
    ("globalbanking", "Global banking", "/global-banking/"),
    ("intlwires", "International wires", "/international-wires/"),
    ("loanorig", "Loan origination", "/loan-origination/"),
    ("multicurrency", "Multicurrency", "/multicurrency/"),
    ("realtime", "Real-time payments", "/realtime/"),
    ("stablecoins", "Stablecoins", "/stablecoins/"),
    ("wire", "Wire transfers", "/wire/"),
    ("company", "Company", "/company/"),
    ("careers", "Careers", "/careers/"),
    ("blog", "Blog", "/blog/"),
    ("security", "Security", "/security/"),
    ("contact", "Contact", "/contact/"),
    ("privacy", "Privacy", "/legal/privacy-notice/"),
    ("signin", "Sign-in (boundary)", "dashboard.column.com/login"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "/"),
    ("mobile-ach", "ACH, phone", "/ach/"),
    ("mobile-cardprograms", "Card programs, phone", "/card-programs/"),
    ("mobile-blog", "Blog, phone", "/blog/"),
]

L = []


def W(s=""):
    L.append(s)


shots = sorted(p.name for p in Path("screenshots").glob("*.png"))


def links(prefix):
    out = []
    for f in shots:
        m = re.fullmatch(re.escape(prefix) + r"-(?:dark|light)-(.+)\.png", f)
        if m:
            out.append(f"[{m.group(1)}](screenshots/{f})")
    return ", ".join(out)


n_crops = len(list(Path("components/crops").glob("*.png")))
n_states = sum(len(c["states"]) for c in C.values())
icons = []

W("# Column components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from column.com on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, paid for or submitted.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SuisseIntl 16/24 400, #575a64`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{theme}-{state}.png`; every public route paints the same light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages (1x on desktop, 2x on mobile); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).")
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
    ("Mobile menu, open", "bar, phone", "the hamburger's own press", "[mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu-open](#m-menu-open)"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement files.")
W()
TRANSPARENT = re.compile(r"rgba\(\d+, \d+, \d+, 0\)$")
foc, failed = [], []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st or "style" not in st:
        continue
    if "failed" in str(st.get("via", "")):
        failed.append(k)
        continue
    s = st["style"]
    base = (c["states"].get("default") or {}).get("style") or {}
    # A focus only counts as visible when something a user can see changed:
    # a non-transparent outline, or a shadow/border/colour repaint. A 2px
    # transparent outline (the Tailwind focus-visible reset) is not a ring.
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0 and not TRANSPARENT.match(s["outlineColor"] or "")
    if ring:
        foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}"))
    elif any(s.get(f) != base.get(f) for f in ("boxShadow", "borderTopColor", "backgroundColor", "color")):
        changed = [f for f in ("boxShadow", "borderTopColor", "backgroundColor", "color") if s.get(f) != base.get(f)]
        foc.append((k, "visible change in " + "/".join(changed)))
    else:
        # A child layer can paint the ring: the CTA's inner anchor picks up the
        # browser's auto outline on focus-visible, and the sign-in submit's
        # ::after grows a 3px ring shadow. Compare painted outlines and shadows
        # between the focused and default states before calling it no-change —
        # keyed on the node kind, not the styled-components hash, which
        # regenerates per state.
        def rings(v):
            out = {}
            for p in ((v or {}).get("paint") or []):
                node = (p.get("node") or "").split(".")[0]
                out[node] = (p.get("outline"), p.get("shadow"))
            return out
        base = rings(c["states"].get("default"))
        changed = []
        for n, (o, sh) in rings(st).items():
            bo, bsh = base.get(n, (None, None))
            if o and o != bo:
                changed.append(f"{o} on {n}")
            elif sh and sh != bsh:
                changed.append(f"shadow change on {n}")
        if changed:
            foc.append((k, "; ".join(changed[:2]) + " (child layer)"))
        else:
            foc.append((k, None))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
line = f"**Focus.** {len(foc)} components were given a real keyboard focus"
if failed:
    line += f" (a further {len(failed)} could not be driven: {', '.join('`'+x+'`' for x in failed)})"
line += f". {len(with_ring)} show a visible focus state: {', '.join(with_ring)}." if with_ring else ". None shows a visible focus state."
if without:
    line += f" The other {len(without)} show no change a keyboard user can see: {', '.join(without)}."
W(line)
W()
_same, _diff = [], []
for _k, _c in C.items():
    _st = _c.get("states") or {}
    if "hover" in _st and "pressed" in _st and "style" in _st["hover"] and "style" in _st["pressed"]:
        (_same if _st["hover"]["style"] == _st["pressed"]["style"] else _diff).append(_k)
W(f"**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). On {len(_same)} of {len(_same) + len(_diff)} measured controls pressed reads as the same painted step as hover{'; the rest differ — ' + ', '.join(f'`{k}`' for k in _diff) + ' (their rows show the diff)' if _diff else ''}. Nothing a real press would submit, navigate or write (the CTAs navigate onward, the sign-in OAuth and Log-in controls submit) was ever pressed.")
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
for k in ["section-box", "product-screen", "signin-card", "nav-cta"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if "style" in s), None)
    if st is None:
        continue
    p = props(st)
    if ("radius" not in p or (p["background"] == "transparent" and "image" not in p)) and st.get("paint"):
        # A painted child only describes the component when it covers it —
        # signin-card's first paint is its email input, not the form.
        def _covers(x):
            m = re.match(r"([\d.]+)x([\d.]+)", x.get("size") or "")
            return bool(m) and float(m.group(1)) >= st["rect"]["w"] * 0.9 and float(m.group(2)) >= st["rect"]["h"] * 0.9
        p0 = next((x for x in st["paint"] if x.get("bg") and x.get("radius") and _covers(x)), None)
        if p0:
            p = dict(p, border=colour(p0["border"].split(" | ")[0][2:]) if p0.get("border") else "-", radius=p0.get("radius", "-"), background=colour(p0.get("bg", "")) or "-", shadow=colour(p0.get("shadow", ""), tokens=False) or "none")
    W(f"| [{c['title']}](#{re.sub(r'[^a-z0-9 -]', '', c['title'].lower()).replace(' ', '-')}) | {p['size']} | {p.get('border', '-')} | {p.get('radius', '-')} | {p.get('image') or p.get('background', '-')} | {p.get('shadow', 'none')} | {p.get('padding', '0')} |")
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Column's artwork. Declared under layoutGaps in the catalog entry.")
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
W("- **The product itself.** Column's platform — the dashboard, ledgers, transfers and account controls — lives behind dashboard.column.com sign-in; the public login surface was measured but never submitted, and no authenticated flow was ever entered.")
W("- **The app itself is a different surface.** The marketing site is a Gatsby + styled-components build; the dashboard UI behind dashboard.column.com login is not reachable signed out and is not claimed here. docs.column.com (the API docs surface) was not captured.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Disabled, error and loading states** were not seen on the public surface.")
W()
W("### Themes")
W()
W("One theme: the whole public surface paints light. Dark islands exist inside it (the near-black navy infrastructure band, which carries the `.color-palette-inverted` class), but no second theme is offered.")
W()
W("### Fonts")
W()
W("- **The UI fonts** are webfonts the site ships (SuisseIntl body, SuisseIntlMono code and Inter UI via the --font-* stacks; `fonts` in [raw/css-vars.json](raw/css-vars.json) holds the @font-face records); the font files themselves are not committed.")
W("- Illustrations, photography, the product-UI mocks and the wordmark in the screenshots are Column's property; partner and certification marks are their owners' marks.")
W()
W("### Screenshots")
W()
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- The hero artwork, illustrations and the Column wordmark are Column's content; only the frames and components were measured. The product-UI mocks render the app's look inside marketing frames.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
