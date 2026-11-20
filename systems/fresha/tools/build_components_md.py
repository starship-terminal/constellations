#!/usr/bin/env python3
"""Build components.md for the Fresha design reference.

Reads raw/components-computed.json (every component and state, measured), tokens.json,
screenshots/ and components/crops/, and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the token in
tokens.json whose value matches, the font family is named once per value, and a state row
shows only what differs from the first state. Adapted from the kit's builder, which read
markdown; this one reads the JSON directly.

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
# the light set is the signed-out palette; index every colour token it and the app set name
for setname in ("light", "app", "core"):
    for n, t in flat(T.get(setname, {})):
        if t["$type"] == "color":
            BY_COLOR.setdefault(t["$value"], f"{setname}.{n}" if setname != "light" else n)


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
    return re.sub(r"rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)", lambda m: label(norm(*m.group(1, 2, 3, 4))), c)


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


def px(x):
    try:
        return float(str(x).replace("px", ""))
    except ValueError:
        return 0.0


def transparent(c):
    m = re.fullmatch(r"rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)", (c or "").strip())
    return bool(m) and m.group(4) is not None and float(m.group(4)) == 0


def pseudo_paint(p):
    """The paint a ::before/::after dict carries, or '' when it draws nothing
    visible (opacity 0, or no fill/border/shadow/image at all)."""
    if not p or px(p.get("opacity", "1")) == 0:
        return ""
    bits = []
    if (p.get("boxShadow") or "none") != "none":
        bits.append("shadow " + colour(p["boxShadow"], tokens=False))
    if px(p.get("borderTopWidth", "0px")) > 0 and p.get("borderTopStyle") not in (None, "none"):
        bits.append(f"border {p['borderTopWidth']} {p['borderTopStyle']} {colour(p['borderTopColor'])}")
    if p.get("backgroundColor") not in (None, "", "rgba(0, 0, 0, 0)"):
        bits.append("bg " + colour(p["backgroundColor"]))
    if p.get("backgroundImage") not in (None, "", "none"):
        bits.append("image")
    return "; ".join(bits)


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
    if s["outlineStyle"] != "none" and px(s["outlineWidth"]) > 0:
        o["outline"] = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}"
    pseudo = []
    for pe in ("::before", "::after"):
        p = v.get(pe)
        if not p:
            continue
        body = pseudo_paint(p)
        if not body:
            continue
        dims = f"{num(p.get('width', '?'))}x{num(p.get('height', '?'))}"
        rad = f", radius {p['borderRadius']}" if p.get("borderRadius") not in (None, "0px") else ""
        pseudo.append(f"{pe} {dims}: {body}{rad}, opacity {p.get('opacity', '1')}")
    if pseudo:
        o["pseudo"] = " + ".join(pseudo)
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


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "outline", "pseudo", "text", "transition", "transform", "opacity", "icon", "placeholder"]


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

PAGE_NAME = {
    "home": "consumer home", "userflow": "user-flow shell", "auth": "consumer sign-in",
    "partner": "partner sign-in", "venue": "venue", "booking": "booking wizard",
    "pricing": "pricing", "business": "for-business", "lp": "LP browse",
    "help": "help centre",
}

GROUP_INTRO = {
    "Shell and navigation": "The consumer marketplace shell every www.fresha.com page shares: a 72px header with the Fresha wordmark, Log in, For business, a menu button and the Get the app pill, and the footer. The menu opens a drawer (its own entry, below).",
    "Dialogs, menus and overlays": "The local overlays the shell can open without submitting anything: the home page's menu drawer and its items, the search suggestion popover under the hero field, and the for-business mega-menu flyout. Each was opened, measured or photographed, then dismissed.",
    "Consumer home": "The marketplace landing page: a large display hero and the card carousels that follow it (recommended venues, categories, app promo).",
    "Search": "The hero search row on the consumer home: a What are you looking for? treatment field, a Current location field, an Any time control and the round search button. The fields were focused only; nothing was searched.",
    "Cards": "The marketplace venue card (photo, name, rating, area, category) and the business-type tile on /for-business.",
    "Sign-in shell": "The /user-flow chooser (a back button, the customer-or-business card and a language button), the /auth consumer sign-in (email field, Continue, Google/Facebook/Apple SSO buttons, a passkey button, cross-links) and the partners.fresha.com professional sign-in (email, Continue, an SSO row and a decoy password field). Nothing was submitted; the email fields were typed into and cleared.",
    "Form controls": "The sign-in email fields and the partner form's decoy password input (the LP browse page carries no sort select — `lp-sort-select` is recorded as missing).",
    "Venue page": "A public venue profile (/a/<slug>): breadcrumb, gallery, venue title and tabs, the service list with per-service Book buttons, the Book now bar, opening-hours table, staff and review cards. Booking a service was never pressed.",
    "Booking wizard": "The /booking step the venue's Book controls lead to, captured at the service-selection boundary: the step header, category pills, service rows with their own Add checkboxes and the summary cart. One service was ticked then unticked to record both states; Continue was never pressed and nothing was booked.",
    "For-business marketing": "The /for-business B2B landing (the same Panda system as the partner app): the nav with the Business types flyout button, the display hero, the Get a demo / Watch film buttons, the business-type grid and the stat row.",
    "Pricing": "The /pricing page: plan cards with prices and CTAs, the feature rows, the small info icons and the FAQ disclosures (one was opened for its capture).",
    "Marketplace browse (/lp)": "The legacy /lp/ microsite (its own stylesheet, literal values, no token vars): the LP header, the category chip rail, browse venue cards, the Show on map button and pagination. The category page /lp/en/bt/hair-salons and the Singapore browse page were both captured.",
    "Help centre": "The /help-center surface: the 654px search pill (focused only, nothing searched) and the topic/article cards.",
    "Mobile (390 wide)": "A few components as a phone draws them, at 390 x 844 with an iPhone user agent: the mobile sticky header and menu button, the compact search field and a venue card.",
}

SHOTS = [
    ("home", "Consumer home. The 72px header, the display hero with the search row, recommended-venue cards, then marketing sections and the footer.", "/"),
    ("user-flow", "The user-flow chooser: customer or business, with the back button and the language button.", "/user-flow"),
    ("auth", "The consumer sign-in: the email field (shown filled, then cleared), Continue, the SSO row, passkey and cross-links.", "/auth"),
    ("partner-signin", "The partners.fresha.com professional sign-in, in light and in the dark theme it paints under prefers-color-scheme: dark.", "/users/sign-in on partners.fresha.com"),
    ("venue", "A venue profile: gallery, title, tabs, services with Book buttons, reviews, hours and the Book now bar.", "/a/ha-lu-hair-design-singapore-11-mohamed-sultan-road-f7vhwpo1"),
    ("booking", "The booking wizard at the service-selection boundary: a service ticked (ticked), then unticked; never continued.", "/a/…/booking"),
    ("pricing", "Pricing: the plan cards, feature list and the FAQ (one disclosure opened).", "/pricing"),
    ("for-business", "For business: nav, display hero, business-type grid and stats; the Business types flyout open.", "/for-business"),
    ("lp-category", "Legacy LP category page: hero, city chips, global venue rows.", "/lp/en/bt/hair-salons"),
    ("lp-browse", "Legacy LP browse: category chip rail, venue cards, map button, pagination.", "/lp/en/bt/hair-salons/in/singapore"),
    ("help", "Help centre: the search pill and the topic/article lists.", "/help-center"),
    ("careers", "Careers.", "/careers"),
    ("blog", "The blog index.", "/blog"),
    ("download-app", "Download the app.", "/download-app"),
    ("cookies", "The cookies policy page.", "/cookies"),
]
MOBILE = [
    ("mobile-home", "Consumer home at 390: the compact header and hero.", "/"),
    ("mobile-auth", "The consumer sign-in at 390.", "/auth"),
    ("mobile-lp-browse", "LP browse at 390.", "/lp/en/bt/hair-salons/in/singapore"),
    ("mobile-venue", "The venue page at 390.", "/a/…"),
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

W("# Fresha components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from fresha.com's signed-out surfaces on {J['_meta']['lastRun'][:10]}, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, booked, bought, sent or submitted.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Roobert 16/16 400, #262627`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-light-{state}.png`; the partner sign-in also has `partner-signin-dark-default.png` (the one painted dark state). Desktop shots are 1440 x 900; `-full` shots are whole pages; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). Each PNG has a `.capture.json` sidecar with the real viewport, DPR and document size.")
W()
W("| Surface | URL | Screenshots |")
W("|---|---|---|")
for p, desc, url in SHOTS + MOBILE:
    extra = ", [dark](screenshots/partner-signin-dark-default.png)" if p == "partner-signin" else ""
    W(f"| {desc} | `{url}` | {links(p)}{extra} |")
W()
W("### Overlays and transient states")
W()
W("| State | Where | How it was reached | Captured |")
W("|---|---|---|---|")
OVER = [
    ("Menu drawer", "consumer home", "the header's Menu button; dismissed after capture", "[home-light-menu](screenshots/home-light-menu.png), [menu-drawer](#menu-drawer)"),
    ("Search suggestions", "consumer home", "focus in the What are you looking for? field; nothing searched", "[home-light-search-focus](screenshots/home-light-search-focus.png), [search-suggestions](#search-suggestions)"),
    ("Business types flyout", "/for-business", "the nav's Business types button; dismissed with Escape", "[for-business-light-flyout](screenshots/for-business-light-flyout.png), [nav-flyout](#nav-flyout)"),
    ("FAQ open", "/pricing", "one FAQ disclosure's own button", "[pricing-light-faq-open](screenshots/pricing-light-faq-open.png), [faq-item](#faq-item)"),
    ("Service ticked", "booking wizard", "a service row's own Add checkbox, then unticked; Continue never pressed", "[booking-light-ticked](screenshots/booking-light-ticked.png), [booking-cart](#cart-summary)"),
    ("Email filled", "consumer and partner sign-in", "typed into the field, then cleared before capture continued; nothing submitted", "[auth-light-filled](screenshots/auth-light-filled.png), [auth-email-field](#email-field)"),
    ("Dark theme", "partner sign-in", "data-theme=\"auto\" honours prefers-color-scheme: dark; captured under an emulated dark preference", "[partner-signin-dark-default](screenshots/partner-signin-dark-default.png)"),
]
for r in OVER:
    W("| " + " | ".join(r) + " |")
W()

# ------------------------------------------------ shared values
W("## Shared values")
W()
W("Values that apply across entries, from the measurement files.")
W()
def ring_of(st_f, st_d):
    """The visible ring a focus-visible state draws, or None: a painted root
    outline (a non-transparent colour — the common 2px transparent outline is
    not a ring), a ::before/::after layer that becomes visible on focus (the
    Panda controls fade a ring shadow in with opacity 0 -> 1), or a new ring
    painted by an ancestor."""
    s = st_f["style"]
    parts = []
    if s["outlineStyle"] != "none" and px(s["outlineWidth"]) > 0 and not transparent(s["outlineColor"]):
        parts.append(f"outline {s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'])}, offset {s['outlineOffset']}")
    for pe in ("::before", "::after"):
        p = st_f.get(pe)
        body = pseudo_paint(p)
        if not body or pseudo_paint((st_d or {}).get(pe)):
            continue
        rad = f", radius {p['borderRadius']}" if p.get("borderRadius") not in (None, "0px") else ""
        parts.append(f"{pe} {body}{rad} (opacity 0 to 1)")
    foc_anc = {(a["node"], a.get("outline"), a.get("shadow")) for a in st_f.get("ancestors", [])}
    base_anc = {(a["node"], a.get("outline"), a.get("shadow")) for a in (st_d or {}).get("ancestors", [])}
    for node, ol, sh in sorted(foc_anc - base_anc):
        if ol:
            parts.append(f"ancestor outline {colour(ol)}")
        elif sh:
            parts.append(f"ancestor shadow {colour(sh, tokens=False)}")
    return "; ".join(parts) or None


foc = []
no_focus = []  # focus-visible readings where focus never landed (D4)
for k, c in C.items():
    st = c["states"].get("focus-visible")
    if not st or "style" not in st:
        continue
    if focus_not_captured(st):
        no_focus.append(k)
        continue
    base = c["states"].get("default") or next((s for s in c["states"].values() if "style" in s), None)
    foc.append((k, ring_of(st, base)))
ring_groups = {}
for k, r in foc:
    ring_groups.setdefault(r, []).append(k)
with_ring = [r for r in ring_groups if r]
W(f"**Focus.** {len(foc)} components were given a real keyboard focus. {sum(len(ring_groups[r]) for r in with_ring)} draw a visible ring.")
for r in with_ring:
    W(f"- {r}: {', '.join(f'`{k}`' for k in ring_groups[r])}.")
if None in ring_groups:
    W(f"The rest draw none — most declare only a 2px transparent outline that stays invisible: {', '.join(f'`{k}`' for k in ring_groups[None])}.")
if no_focus:
    W(f"Focus could not be captured on {len(no_focus)}: keyboard focus never reached them (or they took focus without matching :focus-visible), so their focus look is unknown, not absent: {', '.join(f'`{k}`' for k in no_focus)}.")
W()
W("**Pressed.** Measured by forcing :active through DevTools. Fresha's solid buttons (the auth/partner Continue, the B2B CTAs, the map button) shrink slightly on press (the B2B CTA goes from 180x48 to about 173x46); the text buttons barely change.")
W()
W("**Motion.** Transitions measured on the components, by duration. The motion probe read every moving element on eight public pages both ways ([raw/motion.json](raw/motion.json)): prefers-reduced-motion only partially honoured — the consumer home, venue and LP pages reduce some motion; the pricing, for-business, help, auth and partner pages leave every transition running.")
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
for k in ["venue-card", "lp-venue-card", "m-venue-card", "plan-card", "business-type-card",
          "chooser-card", "review-card", "topic-card", "article-link", "booking-cart",
          "search-suggestions", "nav-flyout", "menu-drawer", "hours-table"]:
    c = C.get(k)
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if "style" in s), None)
    if st is None:
        continue
    p = props(st)
    # A transparent root borrows paint only from a real surface: a non-pseudo
    # descendant covering ~the whole card. A smaller child (a carousel button,
    # an avatar, a chip) describes itself, not the card — the root's own
    # values stand then, even when that means "transparent, no radius".
    if ("radius" not in p or p["background"] == "transparent") and st.get("paint"):
        rw, rh = px(st["rect"]["w"]), px(st["rect"]["h"])

        def full_surface(x):
            if "::" in x["node"] or not x.get("bg") or transparent(x["bg"]):
                return False
            m = re.match(r"([\d.]+)x([\d.]+)", x["size"].replace("px", ""))
            return bool(m) and float(m.group(1)) >= 0.9 * rw and float(m.group(2)) >= 0.9 * rh

        p0 = next((x for x in st["paint"] if full_surface(x)), None)
        if p0:
            tag = re.sub(r"\..*$", "", p0["node"])
            p = dict(p, border=colour(p0["border"].split(" | ")[0][2:]) if p0.get("border") else "-", radius=p0.get("radius", "-"), background=f"{colour(p0['bg'])} (a full-size {tag} inside)", shadow=colour(p0.get("shadow", ""), tokens=False) or "none")
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
W("## Gaps")
W()
W("### Pages")
W()
W("- **Everything behind sign-in.** Nothing in the customer account (booking history, favourites, wallet, gift cards, settings), nothing in the partner app past its sign-in form (the calendar, sales, client list and marketing screens the B2B pages advertise), and no OAuth or SSO flow was started — those pages were never reached.")
W("- **Anything that submits.** No search was run, no venue was booked (the wizard stops at service selection; Continue was never pressed), no sign-in, sign-up, demo or contact form was sent, no newsletter was joined and no app-store link was followed.")
W("- **The venue map.** The LP browse page's Show on map button and the venue pages' map blocks were measured but the map overlays were not opened; their tiles load live data.")
W("- **Blog and careers articles.** The index pages are captured; individual articles and job postings were not opened.")
W("- **terms.fresha.com** was identified as the legal-documents host; the /cookies page was captured but the terms pages were not screenshotted.")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools, so a state a script adds on mousedown (if any) is missing.")
W("- **Hover on the menu item and the venue tab** could not be applied (the elements unmount or move when the pointer leaves); those entries hold the states that did take.")
W("- **The LP browse sort select** does not exist on the captured page — its only `<select>` is the header's language picker; `lp-sort-select` is recorded missing rather than measured on the wrong control.")
W("- **Disabled, loading and error states** do not exist on the captured controls (sign-in forms disable Continue until an email is present, but no disabled example was recorded).")
W()
W("### Themes")
W()
W("Fresha ships three declared scopes. **Light** is the only theme the consumer and B2B pages paint: no signed-out page sets a data-theme, and emulating prefers-color-scheme: dark changes nothing there. **Dark** is genuinely painted on the partners.fresha.com sign-in, which sets `data-theme=\"auto\"` (screenshot partner-signin-dark-default.png). **Accent** (`[data-theme=accent]`, a violet section theme) is declared in the partner and B2B sheets but no signed-out element was observed carrying it. The consumer/B2B dark and every accent declaration are kept in tokens.json as declared-but-unpainted evidence and marked so in their $extensions.")
W()
W("### Fonts")
W()
W("- **Roobert and AktivGroteskVF** are self-hosted variable faces the site serves itself; the style guide falls back to the system font.")
W("- **Tartuffo, Changa and PlayfairDisplay** make up the display stack (`--font-display`); Tartuffo is a commercial face not on Google Fonts.")
W()
W("### Screenshots")
W()
W("- Venue photos, hero photography and map tiles are Fresha's and its venues' content and appear only inside screenshots and crops.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Venue, review and staff names in the captures are Fresha's public content, recorded as the product renders them.")
W("- No personal data was captured: every page was read signed out, the only text ever typed was a placeholder address that was cleared, and the reCAPTCHA badge (a widget, not page content) was hidden in captures.")

Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", len(C), "entries,", n_crops, "crops")
