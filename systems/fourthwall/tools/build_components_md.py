#!/usr/bin/env python3
"""Build components.md for the Fourthwall design reference.

Reads raw/components-computed.json (every component and state, measured),
tokens.json, screenshots/ and writes components.md next to them. Every value
is a cell of the measurement file, condensed: colours are hex followed by the
palette token whose value matches, the font family is named once per value,
and a state row shows only what differs from the first state. Adapted from
the Coursera kit's builder via the Deezer package, which read markdown; this
one reads the JSON directly.

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


# Colour -> token name, built per surface set. The hosts remap the shared
# palette names (the dark set's `white` is #161618, not #ffffff), so a single
# merged map would label a dark component's #ffffff `white` and send readers
# to the wrong value. A component's labels come from its own set's map (core
# first, then the set's own tokens), and a colour that matches nothing there
# stays a literal.
def resolve_alias(v, setname, depth=0):
    m = re.fullmatch(r"\{([^{}]+)\}", v or "")
    if not m or depth > 6:
        return v
    for root in (T.get(setname, {}), T.get("core", {})):
        node = root
        for k in m.group(1).split("."):
            node = node.get(k) if isinstance(node, dict) else None
        if isinstance(node, dict) and "$value" in node:
            return resolve_alias(node["$value"], setname, depth + 1)
    return v


BY_COLOR = {}
SETS = ("light", "ink", "catalog", "catalogDark", "signup", "docs", "docsDark", "help", "helpDark")
for setname in SETS:
    # The tokens the theme (core + the set) carries: the set's own declaration
    # shadows core on a shared path, so the label is always the token a reader
    # of this set's theme would actually resolve.
    themed = {}
    for src in ("core", setname):
        for n, t in flat(T.get(src, {})):
            if t["$type"] == "color" and isinstance(t["$value"], str):
                themed[n] = t
    m = {}
    for n, t in themed.items():
        m.setdefault(resolve_alias(t["$value"], setname), n)
    BY_COLOR[setname] = m

# The token set a captured page's components belong to.
PAGE_SET = {"catalog": "catalog", "pdp": "catalog", "all": "catalog", "signup": "catalog",
            "docs": "docs", "docsart": "docs", "docsdark": "docsDark",
            "help": "help", "helpcat": "help", "helpdark": "helpDark"}


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def colour(c, setname="light", tokens=True):
    """rgb()/rgba()/color(srgb) -> '#hex `token`' or 'rgba(...)' — the token
    label is resolved inside the component's own surface set."""
    def label(v):
        if v == "rgba(0, 0, 0, 0)":
            return "transparent"
        tok = BY_COLOR.get(setname, {}).get(v) if tokens else None
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


def props(v, setname="light"):
    s = v["style"]
    o = {}
    o["size"] = f"{num(v['rect']['w'])} x {num(v['rect']['h'])}"
    pad = sides(s["paddingTop"], s["paddingRight"], s["paddingBottom"], s["paddingLeft"])
    if pad != "0px":
        o["padding"] = pad
    bds = []
    for d in ("Top", "Right", "Bottom", "Left"):
        if float(s[f"border{d}Width"].replace("px", "")) > 0 and s[f"border{d}Style"] != "none":
            bds.append(f"{s[f'border{d}Width']} {s[f'border{d}Style']} {colour(s[f'border{d}Color'], setname)}")
        else:
            bds.append("none")
    if any(b != "none" for b in bds):
        o["border"] = bds[0] if len(set(bds)) == 1 else "; ".join(f"{'TRBL'[i]}: {b}" for i, b in enumerate(bds) if b != "none")
    rad = sides(s["borderTopLeftRadius"], s["borderTopRightRadius"], s["borderBottomRightRadius"], s["borderBottomLeftRadius"])
    if rad != "0px":
        o["radius"] = rad
    o["background"] = colour(s["backgroundColor"], setname)
    if s["backgroundImage"] != "none":
        img = re.sub(r'url\("data:[^)]*\)', "an image (data URI)", s["backgroundImage"])
        o["image"] = colour(img, setname)[:200]
    if s["boxShadow"] != "none":
        sh = colour(s["boxShadow"], setname, tokens=False)
        layers = [x.strip() for x in re.split(r",(?![^(]*\))", sh)]
        layers = [x for x in layers if not x.startswith("transparent")]
        if layers:
            o["shadow"] = ", ".join(layers)
    if s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0:
        o["outline"] = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'], setname)}, offset {s['outlineOffset']}"
    t = v.get("textStyle")
    if t:
        o["text"] = f"{font(t['fontSize'], t['lineHeight'], t['fontWeight'], t['fontFamily'])}, {colour(t['color'], setname)}"
    else:
        o["text"] = f"{font(s['fontSize'], s['lineHeight'], s['fontWeight'], s['fontFamily'])}, {colour(s['color'], setname)}"
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
        o["icon"] = f"{num(v['icon']['w'])} x {num(v['icon']['h'])}, {colour(v['icon']['color'], setname)}"
    if v.get("placeholder"):
        o["placeholder"] = colour(v["placeholder"]["color"], setname)
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
    setname = PAGE_SET.get(c.get("page"), "light")
    base = props(c["states"][states[0]], setname)
    rows = [(states[0], base)]
    same = []
    for st in states[1:]:
        p = props(c["states"][st], setname)
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
    setname = PAGE_SET.get(c.get("page"), "light")
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
            bits.append("background " + colour(p["bg"], setname))
        if p.get("bgImage"):
            bits.append("image " + colour(p["bgImage"], setname)[:90])
        if p.get("border"):
            bits.append("border " + colour(p["border"].split(" | ")[0][2:], setname))
        if p.get("radius"):
            bits.append("radius " + p["radius"])
        if p.get("shadow"):
            bits.append("shadow " + colour(p["shadow"], setname))
        out.append(" ".join(bits))
    return "; ".join(out).replace("|", "/")


# --------------------------------------------------------------------------- page and group text

PAGE_NAME = {"home": "home", "pricing": "pricing", "blog": "blog", "compare": "compare",
             "cmparticle": "comparison (fourthwall-vs-shopify)", "shops": "shops",
             "inspired": "get-inspired", "contact": "contact", "signup": "get-started auth shell",
             "catalog": "catalogue home", "pdp": "product page", "all": "catalogue /all",
             "docs": "docs home", "docsart": "docs article", "docsdark": "docs article",
             "help": "help home", "helpcat": "help category", "helpdark": "help category",
             "mobile": "home"}

GROUP_INTRO = {
    "Site chrome": "The fixed .nav-bar on every marketing page: the Fourthwall wordmark, the Features mega-menu and Learn dropdowns, Product catalog / Pricing links, Log in and the 'Start now' pill.",
    "Home": "The marketing home page: the 'One platform for premium products and branded shops' masthead, the Start-now CTA, the Features mega-menu, product tiles, rating cards, the logo wall and the closing section.",
    "Pricing": "The /pricing page: the Pay yearly / Pay monthly billing toggle (clicked once to paint monthly), the Free / Pro / Managed plan cards, feature rows and the FAQ disclosures.",
    "Blog": "The /blog index: post cards and the newsletter field (typed into, then cleared — never subscribed).",
    "Compare": "The /compare index: the 'Compare Fourthwall to…' search field (typed into, then cleared) and the platform comparison cards.",
    "Comparison page": "A vs-page (/compare/fourthwall-vs-shopify): the masthead and the 'Choose X if' comparison cards.",
    "Shops": "The /shops showcase: example-shop tiles.",
    "Get inspired": "The /get-inspired showcase: creator and storefront cards.",
    "Contact": "The /contact page: the contact and support cards.",
    "Signup (auth shell)": "fourthwall.com/get-started — the auth.fourthwall.com (Keycloak) shell it redirects to: the Google / Apple / email provider choices on the catalogue DS. Measured at rest, never pressed.",
    "Product catalogue": "products.fourthwall.com — the public catalogue: the nav with category tabs and search, the product-finder quiz, product cards and badges.",
    "Product page": "A catalogue PDP (Comfort Colors 1717): title and badge, colour swatches, the static 'S–4XL' size-range label and size-guide dialog, price and the 'Sign in to design' CTA — measured, never activated. This PDP exposes no per-size selector or decoration picker.",
    "Developer docs": "docs.fourthwall.com — the Mintlify docs: navbar, cmdk search dialog, sidebar, article typography, code blocks and the 'Change theme preference' menu.",
    "Developer docs (dark)": "The same docs page under html.dark, painted by the site's own theme menu — the real user-facing toggle, not a reconstruction.",
    "Help center": "help.fourthwall.com — the Docusaurus help center: navbar with the ctrl-K search and the colour-mode toggle, category cards and article lists.",
    "Help center (dark)": "The same help page under data-theme=dark, painted by the site's own colour-mode toggle — the real user-facing theme.",
    "Mobile (390 wide)": "The phone surface at 390 wide: the nav bar, the menu toggle and the Start-now pill.",
    "Footer": "The .site-footer.is-warm footer — sitemap columns, legal links and social icons on the ink surface.",
    "On-ink (dark sections)": "The marketing dark bands — .leg-section.gs1000, .wordmark-section, .closer-section, the .is-warm nav/footer — painted by the sheet's own on-ink scope classes, not a user theme.",
}

SHOTS = [
    ("home", "Home", "/"),
    ("pricing", "Pricing", "/pricing"),
    ("faq", "FAQ", "/faq"),
    ("blog", "Blog", "/blog"),
    ("compare", "Compare", "/compare"),
    ("compare-shopify", "Comparison (vs Shopify)", "/compare/fourthwall-vs-shopify"),
    ("shops", "Shops", "/shops"),
    ("get-inspired", "Get inspired", "/get-inspired"),
    ("features", "Features", "/features"),
    ("memberships", "Memberships", "/memberships"),
    ("contact", "Contact", "/contact"),
    ("signup", "Get started (auth shell)", "/get-started → auth.fourthwall.com"),
    ("catalog", "Catalogue home", "products.fourthwall.com"),
    ("catalog-pdp", "Product page", "products.fourthwall.com/comfort-colors-…-dtg"),
    ("catalog-all", "Catalogue /all", "products.fourthwall.com/all"),
    ("docs", "Docs home", "docs.fourthwall.com"),
    ("docs-quickstart", "Docs quickstart", "docs.fourthwall.com/quickstart"),
    ("docs-dark", "Docs quickstart, dark", "docs.fourthwall.com/quickstart"),
    ("help", "Help home", "help.fourthwall.com"),
    ("help-category", "Help category", "help.fourthwall.com/category/setting-up-your-shop"),
    ("help-dark", "Help category, dark", "help.fourthwall.com/category/setting-up-your-shop"),
]
MOBILE = [
    ("mobile-home", "Home, phone", "/"),
    ("mobile-pricing", "Pricing, phone", "/pricing"),
    ("mobile-catalog", "Catalogue, phone", "products.fourthwall.com"),
    ("mobile-help", "Help category, phone", "help.fourthwall.com/category/setting-up-your-shop"),
]

L = []


def W(s=""):
    L.append(s)


shots = sorted(p.name for p in Path("screenshots").glob("*.png"))


# One page name can prefix another (docs/docs-dark, help/help-dark), so a bare
# `docs-(light|dark)-` match would also claim docs-dark's shots. Assign every
# file to the longest page prefix it matches and let each row link only its
# own page.
PAGE_PREFIXES = sorted((p for p, _, _ in SHOTS + MOBILE), key=len, reverse=True)


def links(prefix):
    out = []
    for f in shots:
        for p in PAGE_PREFIXES:
            m = re.fullmatch(re.escape(p) + r"-(?:light|dark)-(.+)\.png", f)
            if m:
                if p == prefix:
                    out.append(f"[{m.group(1)}](screenshots/{f})")
                break
    return ", ".join(out)


n_crops = len(list(Path("components/crops").glob("*.png")))
n_states = sum(len(c["states"]) for c in C.values())
icons = []

W("# Fourthwall components")
W()
W(f"The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from fourthwall.com, products.fourthwall.com, docs.fourthwall.com, help.fourthwall.com and the /get-started auth shell on {J['_meta']['read']}, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought, designed or submitted; the auth choices and 'Sign in to design' were never pressed; every link and CTA was measured, never followed.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). The page layouts are described in [patterns.md](patterns.md).")
W()
W("How to read an entry:")
W()
W("- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value in the component's own surface set (light+core marketing / ink / catalog / docs / help and their dark sets — the hosts carry separate vocabularies), when there is one. Text is written family size/line-height weight, then its colour, for example `Suisse Intl 17/28 420, #0a0a0a`, and is read from the first text node inside the component.")
W("- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example \"default (same: focus-visible)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component read from the live page, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the surface painted at capture: `light` for the marketing pages, the catalogue and docs/help in light — the marketing site is one light surface (its dark bands are scoped on-ink sections, not a theme); `dark` for the docs quickstart under `html.dark` (the site's own 'Change theme preference' menu) and the help category under `data-theme=dark` (its own colour-mode toggle). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).")
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
    ("Consent overlay", "marketing + docs pages", "the Osano cookie-consent layer (.cc_div/#cc-main) is hidden before every shot and reading — never answered", "hidden, never answered"),
    ("Features mega-menu", "nav bar", "hovered the 'Features' nav item", "[home-light-mega-menu](screenshots/home-light-mega-menu.png), [mega-clip](#mega-menu-panel)"),
    ("Signup modal", "nav Start now", "the nav 'Start now' control navigates to /get-started on this build — the modal was not reachable as a local toggle; the auth shell was shot instead", "[signup-light-default](screenshots/signup-light-default.png); boundary, see Gaps"),
    ("Billing toggle", "pricing", "clicked 'Pay monthly' — a local toggle that repaints the plan prices", "[pricing-light-billing-monthly](screenshots/pricing-light-billing-monthly.png), [billing-toggle](#billing-toggle)"),
    ("FAQ disclosure", "pricing", "clicked one .ph-faq-summary", "[pricing-light-faq-open](screenshots/pricing-light-faq-open.png), [faq-summary](#faq-disclosure)"),
    ("Compare search", "/compare", "typed 'shopify' into the platform search then cleared it", "[compare-light-search](screenshots/compare-light-search.png), [cmp-search](#platform-search)"),
    ("Catalogue search", "products.fourthwall.com", "typed 'hoodie' into the search then cleared it", "[catalog-light-search](screenshots/catalog-light-search.png), [cat-search](#catalogue-search)"),
    ("Quiz option", "products.fourthwall.com", "clicked one product-finder answer — a local selection, nothing submitted", "[catalog-light-quiz-answer](screenshots/catalog-light-quiz-answer.png), [quiz-option](#quiz-option)"),
    ("Size-guide dialog", "product page", "clicked 'Size guide' — a local dialog toggle", "[catalog-pdp-light-size-guide](screenshots/catalog-pdp-light-size-guide.png), [pdp-sizeguide](#size-guide-dialog)"),
    ("Docs search", "docs.fourthwall.com", "clicked the search — the cmdk dialog opened; typed 'auth'", "[docs-light-search](screenshots/docs-light-search.png), [docs-search-dialog](#search-dialog)"),
    ("Docs theme menu", "docs.fourthwall.com", "clicked 'Change theme preference'", "[docs-light-theme-menu](screenshots/docs-light-theme-menu.png), [docs-theme-btn](#theme-menu-button)"),
    ("Docs dark mode", "docs.fourthwall.com", "chose Dark in the site's own theme menu — html.dark painted", "[docs-dark-dark-default](screenshots/docs-dark-dark-default.png)"),
    ("Help search", "help.fourthwall.com", "typed 'storefront' into the navbar search then cleared it", "[help-light-search](screenshots/help-light-search.png)"),
    ("Help dark mode", "help.fourthwall.com", "clicked the navbar colour-mode toggle — data-theme=dark painted", "[help-dark-dark-default](screenshots/help-dark-dark-default.png)"),
    ("Auth providers", "/get-started → auth.fourthwall.com", "the Google/Apple/email choices were measured at rest — never pressed, no OAuth flow started", "[auth-card](#auth-card); boundary, see Gaps"),
    ("Sign in to design", "product page", "the PDP's design action starts an auth flow; measured, never pressed", "[pdp-design-cta](#sign-in-to-design-cta); boundary, see Gaps"),
    ("Signed-in product", "a Fourthwall account", "every post-login surface (the shop dashboard, the designer, checkout) needs an account", "boundary; see Gaps"),
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
    desc = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'], PAGE_SET.get(c.get('page'), 'light'))}, offset {s['outlineOffset']}" if ring else (f"on a child: {child_ring}" if child_ring else None)
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
# The card-like components to compare in one table.
for k in ["tile", "plan-card", "prod-card", "help-card", "docs-card", "rating-card", "auth-card", "shops-tile", "insp-card", "cmp-card"]:
    c = C.get(k)
    # A card the capture could not find is saved with missing: true and no states.
    if not c or c.get("missing"):
        continue
    st = next((s for s in c["states"].values() if "style" in s), None)
    if st is None:
        continue
    p = props(st, PAGE_SET.get(c.get("page"), "light"))
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
W("No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Fourthwall wordmark, the nav mega-menu glyphs, the product and help category artwork, the Eli assistant marks) are the product's artwork. Declared under layoutGaps in the catalog entry.")
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
W("Fourthwall's product is the creator storefront platform: every post-login surface — the shop dashboard (my-shop.fourthwall.com/admin), the product designer, checkout and order flows, the mobile app — needs an account and was never reached. /get-started (auth.fourthwall.com, Keycloak) is the only account surface a signed-out visitor sees, and it was measured at rest: the Google/Apple/email provider buttons were never pressed, and the signup modal's controls were never submitted. The PDP's 'Sign in to design' starts the same flow and was measured, never activated.")
W()
W("### Pages")
W()
W("- **The account.** Every post-login surface was never reached; no provider button was pressed, nothing was typed into an auth field, and the Keycloak URLs carry session/signing parameters that were sanitized out of every sidecar and never stored.")
W("- **The signup modal.** The marketing sheet mounts a `.signup-modal` (Google/Apple/email) but the nav 'Start now' control navigates to /get-started on this build, so the modal was not reachable as a local toggle — its markup was probed, the auth shell it leads to was shot instead.")
W("- **Feature/product pages** beyond the captured set (/design-and-sell, /bespoke, /designers, /websites, /print-on-demand, the /features/* detail pages, /ai-assistant-eli, the other /compare/* pages, /legal/*) are the same templates, unmeasured; one example of each family was captured.")
W("- **Blog posts and help articles** — the indexes and one category were captured; individual articles are the same template, unmeasured.")
W("- **The home page is ~14k px tall** — captured in full, stitched from contiguous parts (the part clips are recorded in the `.capture.json` sidecar).")
W()
W("### States")
W()
W("- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.")
W("- **Disabled, error, loading and validation states** were not seen on the public surface — the search fields were typed into then cleared, and no form was ever submitted.")
W("- **The quiz's later steps** (recommendations after several answers), the catalogue's logged-in design controls and any cart state are boundary states — the quiz was answered once, never completed.")
W()
W("### Themes")
W()
W("The marketing site paints one light surface — no user-facing theme control was found (`color-scheme: normal`); its dark bands are the sheet's own on-ink scope classes (.on-ink, .leg-section.gs1000, .wordmark-section, .closer-section, the .is-warm nav/footer), captured as the ink set. products.fourthwall.com declares every role as a light-dark() pair — the catalogDark set is the declared dark branch resolved under a forced color-scheme probe: declared, not observed (the catalogue ships no theme toggle and no dark paint was captured signed out). docs.fourthwall.com's 'Change theme preference' menu sets html.dark for real (the docsDark set and measurements). help.fourthwall.com's colour-mode toggle sets data-theme=\"dark\" for real (the helpDark set and measurements).")
W()
W("### Fonts")
W()
W("- **Suisse Intl** (marketing + help) and **Saans** (display) are served proprietary faces; **Inter** (docs) and a mono appear on the docs/catalogue hosts. The style guide falls back to system sans.")
W()
W("### Screenshots")
W()
W("- The product photos, creator names, shop examples and logo walls are the product's published content.")
W("- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.")
W()
W("### Content left out")
W()
W("- Article copy, product descriptions, creator names and shop handles are the product's content; only frames and components were measured.")
Path("components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines")
