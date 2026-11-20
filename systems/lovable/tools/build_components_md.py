#!/usr/bin/env python3
"""Build components.md for the Lovable design reference.

Reads raw/components-computed.json and tokens.json, and writes components.md.
Every value is a cell of the measurement file. Colours stay as the browser
reported them (oklch and rgb). A state row shows only what differs from the
first state. Docs components are a separate host and are not tokenised.

Deterministic: re-running it on the same inputs reproduces components.md.
"""
import json, os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
J = json.load(open("raw/components-computed.json"))
C = J["components"]
T = json.load(open("tokens.json"))


def num(x):
    x = str(x)
    if re.fullmatch(r"[\d.eE+-]+", x) and float(x) > 1000:
        return "pill"
    return re.sub(r"(\d+\.\d\d)\d+", r"\1", x)


def colour(c):
    if not c:
        return c
    if c in ("rgba(0, 0, 0, 0)", "oklch(0 0 0 / 0)"):
        return "transparent"
    c = re.sub(r"oklch\(([\d.]+(?:e[+-]?\d+)?) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)",
               lambda m: "oklch(" + " ".join(num(g) for g in m.groups() if g) + ")", c)
    return re.sub(r"(\d+\.\d{3})\d+", r"\1", c)


def sides(t, r, b, l):
    t, r, b, l = num(t), num(r), num(b), num(l)
    if t == r == b == l:
        return t
    if t == b and r == l:
        return f"{t} {r}"
    return f"{t} {r} {b} {l}"


def fam(f):
    return (f or "").split(",")[0].replace('"', "")


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
    if s.get("boxShadow") and s["boxShadow"] != "none":
        sh = colour(s["boxShadow"])
        layers = [x.strip() for x in re.split(r",(?![^(]*\))", sh)]
        layers = [x for x in layers if "rgba(0, 0, 0, 0)" not in x and not x.startswith("transparent")]
        if layers:
            o["shadow"] = ", ".join(layers)[:180]
    if s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0:
        o["outline"] = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}"
    t = v.get("textStyle")
    if t:
        o["text"] = f"{font(t['fontSize'], t['lineHeight'], t['fontWeight'], t['fontFamily'])}, {colour(t['color'])}"
    else:
        o["text"] = f"{font(s['fontSize'], s['lineHeight'], s['fontWeight'], s['fontFamily'])}, {colour(s['color'])}"
    if s.get("transitionDuration") not in ("0s", "", None):
        o["transition"] = f"{s['transitionProperty']} {s['transitionDuration']}"
    if v.get("placeholder"):
        o["placeholder"] = colour(v["placeholder"]["color"])
    return o


ORDER = ["size", "padding", "border", "radius", "background", "shadow", "outline", "text", "transition", "placeholder"]


def focus_not_captured(v):
    """A focus-visible reading taken where keyboard focus never landed (measure.mjs's kbFocus returned
    "focus failed"), a skipped state, or one that did not match :focus-visible. Its style is the element
    at rest, so it is left out of every table and tally and listed as "focus could not be captured"
    (ported from the kit's builder, 2026-11 audit D4)."""
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


PAGE_NAME = {
    "home": "home",
    "pricing": "pricing",
    "login": "log in",
    "docs": "docs",
    "mobile-home": "home, phone",
}

GROUP_INTRO = {
    "Shell and navigation": "The sticky 56px header: Solutions, Resources and Community menus, Log in, and the inverse Get started pill.",
    "Home": "The hero kicker, the prompt composer and the Additional actions icon button. The composer was never submitted.",
    "Pricing": "The Monthly and Yearly segments, a plan CTA, the credit combobox and one expanded FAQ row. Nothing was purchased.",
    "Log in": "OAuth buttons, the email field and Continue. The field was filled and cleared. Continue was never pressed.",
    "Docs": "docs.lovable.dev, a separate host. Inter, not Camera Plain Variable. Not in tokens.json.",
    "Mobile (390 wide)": "The same marketing header at phone width. The menu-open screenshot exists; the sheet itself was not measured.",
}

SHOTS = [
    ("home", "Home", "https://lovable.dev/"),
    ("pricing", "Pricing", "https://lovable.dev/pricing"),
    ("blog", "Blog", "https://lovable.dev/blog"),
    ("security", "Security", "https://lovable.dev/security"),
    ("templates", "Templates", "https://lovable.dev/templates"),
    ("enterprise-landing", "Enterprise landing", "https://lovable.dev/enterprise"),
    ("enterprise-form", "Enterprise form (dark)", "https://lovable.dev/enterprise-form"),
    ("login", "Log in", "https://lovable.dev/login"),
    ("docs", "Docs welcome", "https://docs.lovable.dev/introduction/welcome"),
    ("docs-plans", "Docs plans", "https://docs.lovable.dev/introduction/plans-and-credits"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "https://lovable.dev/"),
    ("mobile-pricing", "Pricing, phone", "https://lovable.dev/pricing"),
    ("mobile-login", "Log in, phone", "https://lovable.dev/login"),
    ("mobile-docs", "Docs, phone", "https://docs.lovable.dev/introduction/welcome"),
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

W("# Lovable components")
W()
W(f"Every measured component from lovable.dev and docs.lovable.dev on {J['_meta']['captured']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844). Nothing was signed into, submitted or purchased.")
W()
W(f"The machine-readable copy is [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states).")
W()
W("How to read an entry:")
W()
W("- Colours are the computed values the browser returned (oklch on lovable.dev, rgb on docs). Tokens live in [tokens.json](tokens.json). Text is family size/line-height weight, then colour.")
W("- The state table's first row lists every value. Later rows list only what changes. A state with the same values as the first is named in the first row's label.")
W(f"- Crops are in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Desktop shots are 1440 x 900 at 1x. `-full` shots are whole pages. Phone shots are 780 wide (390 at 2x). Phone full-page shots were not kept: the page height and the screenshot height disagreed.")
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
    ("Solutions menu, open", "header, home", "the nav button's own press", "[home-light-solutions-menu](screenshots/home-light-solutions-menu.png)"),
    ("Yearly billing", "pricing", "the segment's own press", "[pricing-light-yearly](screenshots/pricing-light-yearly.png)"),
    ("FAQ item, expanded", "pricing", "the question row's own press", "[pricing-light-faq-open](screenshots/pricing-light-faq-open.png)"),
    ("Docs search, open", "docs", "the Search button's own press", "[docs-light-search-open](screenshots/docs-light-search-open.png)"),
    ("Mobile menu, open", "header, phone", "the menu trigger's own press", "[mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png)"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()
W("## Shared values")
W()
TRANSPARENT = re.compile(r"(rgba\(\d+, \d+, \d+, 0\)|oklch\(0 0 0 / 0\))$")
foc, unfocused = [], []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if st and focus_not_captured(st):
        unfocused.append(f"`{k}`")
    if not st or not measured(st):
        continue
    s = st["style"]
    base = (c["states"].get("default") or {}).get("style") or {}
    ring = s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0 and not TRANSPARENT.search(s["outlineColor"] or "")
    if ring:
        foc.append((k, f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}"))
    elif any(s.get(f) != base.get(f) for f in ("boxShadow", "borderTopColor", "backgroundColor", "color")):
        changed = [f for f in ("boxShadow", "borderTopColor", "backgroundColor", "color") if s.get(f) != base.get(f)]
        foc.append((k, "visible change in " + "/".join(changed)))
    else:
        foc.append((k, None))
with_ring = [f"`{k}` ({r})" for k, r in foc if r]
without = [f"`{k}`" for k, r in foc if not r]
line = f"**Focus.** {len(foc)} components were given a real keyboard focus. "
line += (f"{len(with_ring)} show a visible focus state: {', '.join(with_ring)}." if with_ring else "None shows a visible focus state.")
if without:
    line += f" The other {len(without)} show no change a keyboard user can see: {', '.join(without)}."
if unfocused:
    line += f" Focus could not be captured on {len(unfocused)} more (keyboard focus never landed on them, so their readings are left out): {', '.join(unfocused)}."
W(line)
W()
W("**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active). Get started, Continue, OAuth and plan CTAs were never given a real press that would sign in or submit.")
W()

W("## Components")
groups = [g for g in GROUP_INTRO if any(c.get("group") == g for c in C.values())]
for g in groups:
    W()
    W(f"### {g}")
    W()
    W(GROUP_INTRO.get(g, ""))
    for k, c in C.items():
        if c.get("group") != g:
            continue
        W()
        W(f"#### {c.get('title') or k}")
        desc = (c.get("desc") or "").strip()
        if desc and not desc.endswith((".", ")", '"')):
            desc += "."
        where = PAGE_NAME.get(c.get("page"), c.get("page"))
        W(f"{desc + ' ' if desc else ''}Read as `{k}` on the {where} page.")
        W()
        if c.get("missing") or not c["states"]:
            W("Not measured. The selector did not match a visible element.")
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
        imgs = [f"![{c.get('title') or k} {st}](components/crops/{os.path.basename(c['states'][st]['crop'])})" for st in states if c["states"][st].get("crop")]
        W(" ".join(imgs) if imgs else "No crop was saved for this entry.")

W()
W("## Icons")
W()
W("No standalone SVG icon set was lifted. The glyphs in the crops and screenshots are Lovable's artwork.")
W()
W("## Gaps")
W()
W("### Pages")
W()
W("- **The builder behind sign-in.** The product was never signed into. Log in, Get started and the docs signup link were measured, never followed.")
W("- **Forms were not submitted.** The prompt composer, the log-in email field and the enterprise demo form were not submitted. Continue and the OAuth buttons were never pressed.")
W("- **Checkout was not reached.** Plan CTAs were measured, never followed. The credit combobox list was not opened.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools, so a handler that only runs on a real pointer event is missing.")
W("- **Disabled, error and loading** were not seen on the public surface.")
W("- **docs-cta** and **m-menu** selectors did not match. The mobile menu-open screenshot still exists.")
W()
W("### Themes")
W()
W("Marketing routes paint light (`html.light`). Dark is declared and painted on `/enterprise-form`. Docs has its own theme control; it was not changed.")
W()
W("### Fonts")
W()
W("- **Camera Plain Variable** and **Roboto Mono Variable** are webfonts in the lovable.dev bundle. The font files are not committed. Docs uses Inter.")
W()
W("### Screenshots")
W()
W("- Screenshots are 256-colour PNGs. Read exact colours from tokens.json or the raw JSON.")
W("- Phone full-page shots were dropped. The screenshot height and the page height disagreed by more than one pixel.")
W()

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", n_states, "states")
