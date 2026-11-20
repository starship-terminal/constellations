#!/usr/bin/env python3
"""Build components.md for the Fourmula design reference.

Reads raw/components-computed.json (every component and state, measured),
tokens.json, screenshots/ and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the
palette token whose value matches, the font family is named once per value,
and a state row shows only what differs from the first state. Adapted from
the Enode kit's builder, which read the JSON directly.

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


# Colour labels name a token on the component's own surface and paint — a
# marketing ink is a light.*/dark.* role, an app colour is a core.appColor or
# core.component.app token. Indexing all of core would label every marketing
# #020108 as `appColor.base-900`, naming the other system's palette.
def theme_colors(setname):
    out = {}
    for n, t in flat(T[setname]):
        if t["$type"] == "color" and not str(t["$value"]).startswith("{"):
            out.setdefault(t["$value"], f"{setname}.{n}")
    return out


APP_COLORS = {}
for _grp in ("appColor", "component"):
    for n, t in flat(T["core"].get(_grp, {})):
        if t["$type"] == "color" and not str(t["$value"]).startswith("{"):
            APP_COLORS.setdefault(t["$value"], f"core.{_grp}.{n}")

BY_THEME = {"light": theme_colors("light"), "dark": theme_colors("dark"), "app": APP_COLORS}
# The paint each capture page ran under (the marketing light/dark sets, or
# the dark-only app's own palette).
PAGE_THEME = {"home": "light", "home-dark": "dark", "privacy": "light", "mobile": "light",
              "start": "app", "auth": "app", "create-pdp": "app"}


def by_color_for(page):
    return BY_THEME[PAGE_THEME.get(page, "light")]


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def colour(c, tokens=True, by=None):
    """rgb()/rgba()/color(srgb) -> '#hex `token`' or 'rgba(...)'."""
    by = by or {}
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        tok = by.get(v) if tokens else None
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


def props(v, by=None):
    s = v["style"]
    o = {}
    o["size"] = f"{num(v['rect']['w'])} x {num(v['rect']['h'])}"
    pad = sides(s["paddingTop"], s["paddingRight"], s["paddingBottom"], s["paddingLeft"])
    if pad != "0px":
        o["padding"] = pad
    bds = []
    for d in ("Top", "Right", "Bottom", "Left"):
        if float(s[f"border{d}Width"].replace("px", "")) > 0 and s[f"border{d}Style"] != "none":
            bds.append(f"{s[f'border{d}Width']} {s[f'border{d}Style']} {colour(s[f'border{d}Color'], by=by)}")
        else:
            bds.append("none")
    if any(b != "none" for b in bds):
        o["border"] = bds[0] if len(set(bds)) == 1 else "; ".join(f"{'TRBL'[i]}: {b}" for i, b in enumerate(bds) if b != "none")
    rad = sides(s["borderTopLeftRadius"], s["borderTopRightRadius"], s["borderBottomRightRadius"], s["borderBottomLeftRadius"])
    if rad != "0px":
        o["radius"] = rad
    o["background"] = colour(s["backgroundColor"], by=by)
    if s["backgroundImage"] != "none":
        img = re.sub(r'url\("data:[^)]*\)', "an image (data URI)", s["backgroundImage"])
        o["image"] = colour(img, by=by)[:200]
    if s["boxShadow"] != "none":
        sh = colour(s["boxShadow"], tokens=False)
        layers = [x.strip() for x in re.split(r",(?![^(]*\))", sh)]
        layers = [x for x in layers if not x.startswith("transparent")]
        if layers:
            o["shadow"] = ", ".join(layers)
    if s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0:
        o["outline"] = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'], by=by)}, offset {s['outlineOffset']}"
    t = v.get("textStyle")
    if t:
        o["text"] = f"{font(t['fontSize'], t['lineHeight'], t['fontWeight'], t['fontFamily'])}, {colour(t['color'], by=by)}"
    else:
        o["text"] = f"{font(s['fontSize'], s['lineHeight'], s['fontWeight'], s['fontFamily'])}, {colour(s['color'], by=by)}"
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
        o["icon"] = f"{num(v['icon']['w'])} x {num(v['icon']['h'])}, {colour(v['icon']['color'], by=by)}"
    if v.get("placeholder"):
        o["placeholder"] = colour(v["placeholder"]["color"], by=by)
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


def state_rows(c):
    # A state whose capture failed (e.g. via: "focus failed" — the element would
    # not hold a real keyboard focus) is not a captured state: it is reported
    # separately so a failed attempt can never read as a measured absence of a
    # focus ring.
    states = [s for s in c["states"] if "style" in c["states"][s] and c["states"][s].get("via") != "focus failed"]
    if not states:
        return [], states
    by = by_color_for(c["page"])
    base = props(c["states"][states[0]], by)
    rows = [(states[0], base)]
    same = []
    for st in states[1:]:
        p = props(c["states"][st], by)
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
    by = by_color_for(c["page"])
    out = []
    for p in st["paint"][:3]:
        bits = [re.sub(r"\..*$", "", p["node"]) if "::" not in p["node"] else p["node"].split(".")[0], re.sub(r"\.0+(?=x|px|$)", "", p["size"])]
        if p.get("bg"):
            bits.append("background " + colour(p["bg"], by=by))
        if p.get("bgImage"):
            bits.append("image " + colour(p["bgImage"], by=by)[:90])
        if p.get("border"):
            bits.append("border " + colour(p["border"].split(" | ")[0][2:], by=by))
        if p.get("radius"):
            bits.append("radius " + p["radius"])
        if p.get("shadow"):
            bits.append("shadow " + colour(p["shadow"], by=by))
        out.append(" ".join(bits))
    return "; ".join(out).replace("|", "/")


# --------------------------------------------------------------------------- page and group text

PAGE_NAME = {"home": "home", "home-dark": "home (dark paint)", "privacy": "privacy-policy",
             "start": "app start", "auth": "app auth", "create-pdp": "app create-pdp", "mobile": "home"}

GROUP_INTRO = {
    "Cookie consent": "The @finsweet cookie-consent layer (.cookies) that mounts on every first load of the marketing site: the bottom-right banner, the Settings outline button that opens the in-page preference manager, its category checkboxes and the Accept all / Save changes pair — measured, then hidden, never answered.",
    "Site chrome": "The 91px header on every marketing page: the fourmula.ai logo-and-wordmark, the centre pill holding the Menu toggle, the sun/moon theme switch (data-theme-toggle — writes isDarkMode, .body.dark paints LIGHT) and the scroll-percentage counter, the icon-only Fourmula-app account link and the Get started pill. A second set of entries re-reads the same chrome under the site's own dark paint (plain .body, isDarkMode=false).",
    "Nav overlay": "The fixed .menu overlay the Menu pill opens: PDP's / Products / Videos / Our features anchors, Privacy Policy / Terms of Service / Cookie Policy, Instagram / Linkedin / Youtube and the app account link — never followed.",
    "Home": "The fourmula.ai hero — 'Your catalog, instantly re-shot.' with the second line in --fonts-50, the rotating keyword chips at the right edge (PDPs / UGC / Lifestyle shots / Ads / Stories / Street style), the SCROLL DOWN cue — and the sections below: On-brand visuals, the AI features with their round app links, How It Works, the four steps with their Get started buttons.",
    "FAQ accordion": "The FAQ rows at the foot of the home page — a local UI toggle whose + flips and whose answer expands on click.",
    "Legal pages": "The /privacy-policy template (shared by /terms-of-service): the .tech section with its big title, last-updated line and long unclassed prose.",
    "App chrome": "The floating rounded-full header every app.fourmula.ai page paints (1392x56, fixed at 24,24): the 32px Open-main-menu icon button, the header Create asset submit and the Sign in button — all measured, never pressed.",
    "App start": "app.fourmula.ai/start — the signed-out start page ('Create studio-quality product photos', page title 'Formula AI | Start') with its large Create asset call-to-action, measured and never pressed.",
    "App sign-in": "app.fourmula.ai/auth — the sign-in card over the dark field: Back, Continue with Google, Email + Password fields with a visibility eye, the Sign in submit, the Forgot password? submit (validating, not switching — its reset view is uncaptured) and the Sign up switcher that flips the card to its create-account view. The fields were typed into then cleared; nothing was submitted.",
    "Create-PDP generator": "app.fourmula.ai/project/create-pdp — the signed-out PDP generator: Cancel and close / Start generation in the header, the Dashboard link, the Your visuals rail with Recommendations and the upload buttons, the Connect-your-Shopify-store banner with the accent Check-connection pill, the Adjust-look section with its What's-a-PDP explainer and the Static/Video format radios, the Signed-in chips and the full-width Start generation submit — measured, never pressed or submitted.",
    "Mobile (390 wide)": "The marketing site at 390 wide: the header, the Menu pill and its nav overlay, the hero and the FAQ rows.",
    "Footer": "The 811px page footer: the fourmula.ai mark, the section anchors, the legal links and the social column.",
}

SHOTS = [
    ("home", "Home", "/"),
    ("privacy", "Privacy policy", "/privacy-policy"),
    ("terms", "Terms of service", "/terms-of-service"),
    ("start", "App start", "app.fourmula.ai/start"),
    ("auth", "App sign-in", "app.fourmula.ai/auth"),
    ("create-pdp", "Create-PDP generator", "app.fourmula.ai/project/create-pdp"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "/"),
    ("mobile-start", "App start, phone", "app.fourmula.ai/start"),
    ("mobile-auth", "App sign-in, phone", "app.fourmula.ai/auth"),
    ("mobile-create-pdp", "Create-PDP, phone", "app.fourmula.ai/project/create-pdp"),
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

W("# Fourmula components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from fourmula.ai and app.fourmula.ai on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the sign-in fields were typed into then cleared, never sent; every link, CTA and submit was measured, never followed or pressed.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [patterns.md](patterns.md).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/22.5 600, #23252b`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{theme}-{state}.png` where the theme is the painted surface: `light` is the marketing site's first-visit paint (`.body.dark`, isDarkMode=true — the class name is inverted in the site's own code) and `dark` is either the site's own dark paint (plain `.body`) or the dark-only app. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x (bounded to 8 viewport chunks where a page runs long, with the boundary noted in the sidecars); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).")
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
    ("Cookie consent", "every marketing page", "the @finsweet layer (.cookies) mounts on every first load; it was shot once as seen, the Settings toggle was clicked to reach the preference manager, then the layer was hidden — Accept all / Save changes were never pressed", "[home-light-cookie](screenshots/home-light-cookie.png), [cookie-modal](#cookie-consent-modal)"),
    ("Nav overlay", "every marketing page header", "the header Menu pill's own toggle", "[home-light-menu](screenshots/home-light-menu.png), [home-dark-menu](screenshots/home-dark-menu.png), [nav-overlay](#nav-overlay)"),
    ("FAQ accordion", "home page", "a FAQ row's own toggle", "[home-light-faq-opened](screenshots/home-light-faq-opened.png), [faq-item](#faq-row)"),
    ("Theme toggle", "the header pill", "not pressed during measurement (it repaints the whole page); both painted themes were instead reached through the site's own isDarkMode storage key — the same key the toggle writes", "[home-dark-default](screenshots/home-dark-default.png), [mkt-header-dark](#site-header-dark-paint)"),
    ("Sign-in card switcher", "app.fourmula.ai/auth", "the card's own Sign up switcher (a local UI toggle); \"Forgot password?\" is a validating submit, so the reset view is uncaptured", "[auth-dark-signup](screenshots/auth-dark-signup.png), [auth-signup-card](#create-account-view), [auth-forgot-card](#forgot-password-view-uncaptured)"),
    ("Create-PDP dialogs", "app.fourmula.ai/project/create-pdp", "the What's-a-PDP and Recommendations triggers (local UI toggles), dismissed with Escape", "[create-pdp-dark-pdp-dialog](screenshots/create-pdp-dark-pdp-dialog.png), [pdp-what-dialog](#pdp-explainer-dialog), [pdp-reco-dialog](#recommendations-dialog)"),
    ("Sign-in fields", "app.fourmula.ai/auth", "typed into then cleared — nothing sent", "[auth-field-email](#email-field), [auth-field-pass](#password-field)"),
    ("Signed-in product", "a Fourmula account", "the dashboard, generation results and every post-login surface need an account", "boundary; see Gaps"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement files.")
W()
# A focus ring counts only when it is visible — a nonzero outline in a
# non-transparent colour — and it appeared or changed on focus. The Chakra
# controls paint "2px solid rgba(0, 0, 0, 0)" at rest and at focus alike,
# which is a spec, not a ring.
def transparent(c):
    c = (c or "").strip()
    m = re.fullmatch(r"rgba\([^,]+,[^,]+,[^,]+,\s*([\d.]+)\)", c) or re.fullmatch(r"color\(srgb [^)]*/\s*([\d.]+)\)", c)
    return bool(m) and float(m.group(1)) == 0


OUTLINE_COLOUR = re.compile(r"rgba?\([^)]*\)|color\(srgb[^)]*\)|#[0-9a-fA-F]{3,8}\b")


def visible_ring(ol):
    """A computed outlineColour or a paint-list spec
    ('1px auto rgb(16, 16, 16) offset 1px') is a visible ring only when its
    colour is not transparent."""
    m = OUTLINE_COLOUR.search(ol or "")
    return bool(m) and not transparent(m.group(0))


def paint_outlines(v):
    return {n["node"]: n["outline"] for n in (v.get("paint") or []) if n.get("outline")}


foc = []
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st or "style" not in st or st.get("via") == "focus failed":
        continue
    s = st["style"]
    base_st = next((v for v in c["states"].values() if "style" in v), st)
    base = base_st["style"]
    ring = (s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0
            and visible_ring(s["outlineColor"])
            and (s["outlineWidth"], s["outlineStyle"], s["outlineColor"], s["outlineOffset"])
            != (base["outlineWidth"], base["outlineStyle"], base["outlineColor"], base["outlineOffset"]))
    # A ring painted on a child layer instead of the wrapper: offer buttons
    # draw 1px dotted outlines on their inner anchor while the wrapper's own
    # outline stays none. Those states must count as ringed too — under the
    # same visibility and changed-on-focus rules as the root's own outline.
    base_ol = paint_outlines(base_st)
    child_ring = next((ol for node, ol in paint_outlines(st).items()
                       if base_ol.get(node) != ol and visible_ring(ol)), None)
    shadow = s["boxShadow"] != base["boxShadow"] and s["boxShadow"] != "none"
    shadow_lost = s["boxShadow"] != base["boxShadow"] and s["boxShadow"] == "none"
    border = any(
        s[f"border{d}{p}"] != base[f"border{d}{p}"]
        for d in ("Top", "Right", "Bottom", "Left")
        for p in ("Color", "Width", "Style")
    )
    desc = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'], by=by_color_for(c['page']))}, offset {s['outlineOffset']}" if ring else (f"on a child: {child_ring}" if child_ring else None)
    foc.append((k, ring or bool(child_ring), shadow, shadow_lost, border, desc))
with_ring = [f"`{k}` ({r})" for k, ring, sh, sl, bd, r in foc if ring]
with_shadow = [f"`{k}`" for k, ring, sh, sl, bd, r in foc if not ring and sh]
with_border = [f"`{k}`" for k, ring, sh, sl, bd, r in foc if not ring and not sh and bd]
lost_shadow = [f"`{k}`" for k, ring, sh, sl, bd, r in foc if not ring and not sh and not bd and sl]
without = [f"`{k}`" for k, ring, sh, sl, bd, r in foc if not ring and not sh and not bd and not sl]
parts = [f"{len(with_ring)} draw an outline ring: {', '.join(with_ring)}."]
if with_shadow:
    parts.append(f"{len(with_shadow)} draw a focus ring as a shadow instead: {', '.join(with_shadow)}.")
if with_border:
    parts.append(f"{len(with_border)} change only their border: {', '.join(with_border)}.")
if lost_shadow:
    parts.append(f"{len(lost_shadow)} drop their resting shadow without drawing a ring (the Chakra controls' focus-visible outline is the transparent 2px spec they already paint at rest): {', '.join(lost_shadow)}.")
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
for k in ["cookie-modal", "nav-overlay", "auth-card", "auth-forgot-card", "auth-signup-card", "pdp-reco-dialog", "pdp-what-dialog", "pdp-format-group", "m-nav-overlay", "app-header"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if "style" in s), None)
    if st is None:
        continue
    p = props(st, by_color_for(c["page"]))
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
        W()
        if c.get("missing"):
            W("Not on the page when it was captured.")
            continue
        if c.get("uncaptured"):
            # Recorded as never-captured on purpose (e.g. a control whose
            # press submits): the entry stays so no later pass republishes a
            # different view under this name.
            W(f"Uncaptured: {c['uncaptured']}.")
            W()
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the fourmula.ai square mark, the header theme sun/moon, the account glyph, the + FAQ icons and the app's menu/eye glyphs) are the product's artwork — the fourmula.ai logo is an inline Webflow embed, not an icon font. Declared under layoutGaps in the catalog entry.")
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
W("Fourmula's product is the app at app.fourmula.ai: the dashboard, project pages, generation results and every post-login surface need an account and were never reached. The signed-out edge — /start, /auth and the /project/create-pdp generator — was measured as far as a visitor can go without an account: fields were typed into then cleared, and Sign in, Continue with Google, Create asset, Upload Main Image, Check connection, Start generation and every other submit was never pressed. The generator's Start generation would queue a job; what it returns is unverified.")
W()
W("### Pages")
W()
W("- **The account.** The dashboard and every post-login surface were never reached; /auth was measured at rest — what a submitted sign-in or sign-up returns is unverified.")
W("- **The PDP generator** is reachable signed out and its form was measured, but the upload, the Check-connection flow and generation itself need an account and a Shopify store and were never run.")
W("- **Legal pages** — /privacy-policy was measured; /terms-of-service was screenshotted on the same .tech template, unmeasured.")
W("- **No pricing page** was found in the nav, footer or menu links at capture time; the product's cost is unobserved on the public surface.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Disabled, error, loading and validation states** were not seen on the public surface beyond the disabled Video-content radio — the sign-in fields were never submitted.")
W("- **The theme toggle was never pressed during measurement** (a press repaints the whole page); both painted themes were instead reached through the site's own isDarkMode storage key — the same key the toggle writes — so the toggled paint is the site's own, not a reconstruction.")
W()
W("### Themes")
W()
W("The marketing site ships a real two-theme switcher with inverted naming: `data-theme-toggle` writes localStorage isDarkMode and flips the `dark` class on `<body>`, but `.body.dark` paints the LIGHT surface (white `--mainbg`) and plain `.body` paints the DARK one (`#020108` `--mainbg`). A first visit stores isDarkMode=true, so visitors open on the light paint; the `light` token set is that default surface and `dark` is the toggled one. app.fourmula.ai is a separate dark-only Tailwind v4 app with its own `--color-base-*`/`--color-accent-*` layer that shares nothing but the `#020108` near-black with the marketing tokens; its declared values sit under `core.appColor`, `core.font.size.app`, `core.radius.app`, `core.spacing.app` and the other app ramps, and the measured ones under `core.component.app.*` — there is no `component.login` group.")
W()
W("### Fonts")
W()
W("- **Sf Pro Display** is the marketing site's face (`--_font-family---font-family: \"Sf Pro Display\", Arial, sans-serif`), and the app loads its own **SF Pro** variable face (sfProFont, a Next.js local-font variable). The files are Apple's proprietary fonts the site serves itself; the style guide falls back to system fonts.")
W()
W("### Screenshots")
W()
W("- The product photos, model imagery and logo artwork in the captures are the product's published content.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- The legal prose, FAQ answers and marketing copy are the product's content; only frames and components were measured.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
