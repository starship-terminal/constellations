#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

farfetch.com exposes two token layers in its stylesheets. The "pulse" layer
in the portal-core bundles declares ~590 semantic --colors-<family>-<role>-
<state>-<slot> custom properties on :root (families: actions, forms,
navigation, content, cards, messaging, notifications, modality, pos, rating,
access, general, page), ~29 --typography-<role>-<prop>, the --spacers-c*
(component) and --spacers-l* (layout) scales, --gutter-*, --borders-*,
--motion-functional/emotional-*, --icons-*, --button-* and --page-*. The
older camelCase layer in the SSR Emotion blocks adds the named palette
(--color-branco/--color-preto/--color-ouro/--color-red and the
--color<Tier><Shade> Access loyalty ramps), the --gradientAccess<tier>*
gradients, and the legacy type scale (--fontSize*/--lineHeight*/
--letterSpacing*/--textTransform*/--fontNormal/--displayLarge*).

farfetch.com refuses every automated request (Akamai 403, CDN 429), so every
value is resolved from the Wayback-served sheets in raw/css-vars.json; the
component dimensions and state tracks are computed styles measured on the
same archived pages in raw/components-computed.json.

What the capture shows (desktop 1440x900 unless noted):

  #222222   the ink — brand-ui01/text01/icon01: every button fill (Add To
            Bag), every label, the wordmark, the body text
  #727272   the muted grey — text02/brand-ui02: secondary text, nav labels,
            hover on the primary button
  #b6b6b6   the soft grey — brand-ui03: disabled text, strokes
  #e6e6e6   the hairline — brand-ui04: every border and divider
  #f5f5f5   the panel grey — brand-ui05/ui-skeleton: skeletons, chips, hover
            washes, loading surfaces
  #ffffff   the page field — ui06/ui-background: every surface
  #e71d34   the sale red — sale01/pos-sales: Sale nav link, sale prices,
            the sale badge surface
  #c41429   error01; #048273 success01; #faca21 warning01; #943c39
            highlight01 (FARFETCH Edits); #a68245 the FARFETCH First gold
  Typography: "Farfetch Basis" everywhere (body 15px/1.3333, display 30px,
            display-large 38px, title/heading 22px, caption/footnote 13px,
            kicker 15px uppercase); "Nimbus Roman D" serif for the editorial
            dek (20px/1.2). Buttons and fields are square (corners 0); the
            1000px --borders-corner-rounded is reserved for pills.

The page paints ONE theme — white surfaces, black ink, sale red. There is no
dark hook, so the export keeps `dark` empty.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. "
    "farfetch.com is a single-theme luxury storefront on the pulse token "
    "layer: white surfaces, #222 ink and #727272 secondary text, sale red "
    "#e71d34 and the FARFETCH First gold #a68245, square corners with a "
    "1000px pill radius, 'Farfetch Basis' UI type with 'Nimbus Roman D' "
    "editorial serif. The ~590 --colors-* semantics are exported whole "
    "under light.<family>.<role>.<state>.<slot>; the legacy palette, type "
    "and spacing scales sit under core. Component dimensions and state "
    "tracks are measured computed styles."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def st(comp, state):
    return C[comp]["states"][state]["style"]


def ts(comp, state, prop):
    try:
        c = C[comp]["states"][state]
        t = c.get("textStyle") or {}
        v = t.get(prop)
        return v if v else c["style"].get(prop)
    except KeyError:
        return None


def norm_color(v):
    v = (v or "").strip()
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
    return v


def lit(value, ty, src, desc):
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


def has(n):
    return n in R


def ref(name, ty, desc, **kw):
    """A var leaf only when the resolved probe actually holds the name."""
    if not has(name):
        return None
    return var(name, ty, source=f"css-var {name} resolved (raw/css-vars.json)", description=desc, **kw)



def gradient_stops(body):
    """The colour stops of a linear-gradient() body after its angle, split on
    top-level commas only (rgb(), oklab() keep their commas) and keeping an
    explicit stop position; stops without one are spread evenly, as CSS does
    between known neighbours (2026-11 audit, finding 14-29)."""
    parts, depth, cur = [], 0, ""
    for ch in body:
        depth += ch == "("
        depth -= ch == ")"
        if ch == "," and depth == 0:
            parts.append(cur.strip()); cur = ""
        else:
            cur += ch
    parts.append(cur.strip())
    stops = []
    for p in parts:
        m = re.fullmatch(r"(.+?\)|#[0-9a-fA-F]{3,8}|[a-z]+)(?:\s+(-?[\d.]+)%)?", p)
        if not m:
            raise ValueError(f"unreadable gradient stop {p!r}")
        stops.append([m.group(1), None if m.group(2) is None else float(m.group(2)) / 100])
    if stops[0][1] is None:
        stops[0][1] = 0.0
    if stops[-1][1] is None:
        stops[-1][1] = 1.0
    # CSS: a position smaller than an earlier one is moved up to it, before
    # the missing positions are spread
    top = float("-inf")
    for st in stops:
        if st[1] is not None:
            st[1] = max(st[1], top)
            top = st[1]
    i = 0
    while i < len(stops):
        if stops[i][1] is None:
            j = i
            while stops[j][1] is None:
                j += 1
            a, b = stops[i - 1][1], stops[j][1]
            for k in range(i, j):
                stops[k][1] = a + (b - a) * (k - i + 1) / (j - i + 1)
            i = j
        i += 1
    return [(c, round(pos, 4)) for c, pos in stops]

def put(tree, path, leaf):
    if leaf is None:
        return
    node = tree
    for k in path[:-1]:
        node = node.setdefault(k, {})
    node[path[-1]] = leaf


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
put(fam, ("sans",), ref("--typography-body-font-family", "fontFamily",
    "'Farfetch Basis' — every UI string, button, label, heading and card text."))
put(fam, ("editorial",), ref("--typography-editorial-font-family", "fontFamily",
    "'Nimbus Roman D' — the serif for editorial deks and luxury copy."))
put(fam, ("normal",), ref("--fontNormal", "fontFamily",
    "The legacy body stack — 'Farfetch Basis' again."))
put(fam, ("condensed",), ref("--fontCondensed", "fontFamily",
    "The legacy condensed stack (declared as 'Farfetch Basis')."))
put(fam, ("display-large",), ref("--displayLargeFontFamily", "fontFamily",
    "The legacy display stack — 'Nimbus Sans Extended D'."))

fs = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for n in sorted(R):
    if n.startswith("--fontSize"):
        put(fs, (n[len("--fontSize"):].lower(),), ref(n, "dimension", f"The legacy type-size step {n}."))
put(fs, ("displaylarge",), ref("--displayLargeFontSize", "dimension", "The legacy 38px display size ('Nimbus Sans Extended D')."))

lh = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for n in sorted(R):
    if n.startswith("--lineHeight"):
        put(lh, (n[len("--lineHeight"):].lower(),), ref(n, "number", f"The legacy line-height step {n}."))

ls = SPEC["core"].setdefault("font", {}).setdefault("letterSpacing", {})
for n in sorted(R):
    if n.startswith("--letterSpacing"):
        put(ls, (n[len("--letterSpacing"):].lower(),), ref(n, "other", f"The legacy letter-spacing step {n}."))

tt = SPEC["core"].setdefault("font", {}).setdefault("textTransform", {})
for n in sorted(R):
    if n.startswith("--textTransform"):
        put(tt, (n[len("--textTransform"):].lower(),), ref(n, "other", f"The legacy text-transform step {n}."))

# ------------------------------------------------------------- typography
# The pulse layer declares each style as --typography-<stem>-{font-family,
# font-size, line-height} (+text-transform on the kicker), re-declared under
# the 36em/60em breakpoints. The export composes one DTCG typography token
# per stem, resolved at 1440.
typegrp = SPEC["core"].setdefault("typography", {})
TYPE_DESC = {
    "display-large": "The 38px hero/department DisplayLarge.",
    "display": "The 30px Display page/module heading.",
    "title": "The 22px section Title.",
    "heading": "The 22px Heading.",
    "kicker": "The 15px uppercase Kicker over a heading (brand names, categories).",
    "body": "The 15px default UI body.",
    "editorial": "The 20px Nimbus Roman D serif dek.",
    "caption": "The 13px caption.",
    "footnote": "The 13px micro-label.",
}
STEMS = {}
for n in sorted(R):
    m = re.fullmatch(r"--typography-([a-z-]+)-font-(family|size)|--typography-([a-z-]+)-(line-height|text-transform)", n)
    if m:
        stem = m.group(1) or m.group(3)
        prop = {"family": "fontFamily", "size": "fontSize", "line-height": "lineHeight", "text-transform": "textTransform"}[m.group(2) or m.group(4)]
        STEMS.setdefault(stem, {})[prop] = n
for stem in sorted(STEMS):
    parts = STEMS[stem]
    val, used = {}, []
    for prop, name in parts.items():
        v = R[name]
        val[prop] = v
        used.append(name)
    put(typegrp, (stem,), {
        "$value": val, "$type": "typography",
        "$extensions": {"source": "; ".join(f"css-var {n}" for n in used) + " resolved (raw/css-vars.json)"},
        "$description": TYPE_DESC.get(stem, f"The --typography-{stem} style.") + " (resolved at 1440; the stems re-declare font-size under the 36em/60em breakpoints)"})

# --------------------------------------------------------------- spacing

sp = SPEC["core"].setdefault("space", {})
csp = sp.setdefault("component", {})
for n in sorted(R):
    if re.fullmatch(r"--spacers-c\d+", n):
        put(csp, (n[len("--spacers-"):],), ref(n, "dimension", f"Component padding step {n} — gaps and inset inside controls."))
lsp = sp.setdefault("layout", {})
for n in sorted(R):
    if re.fullmatch(r"--spacers-l\d+", n):
        put(lsp, (n[len("--spacers-"):],), ref(n, "dimension", f"Layout spacing step {n} — margins between blocks."))
lg = sp.setdefault("legacy", {})
for n in sorted(R):
    if re.fullmatch(r"--spacer-[A-Z]+", n):
        put(lg, (n[len("--spacer-"):].lower(),), ref(n, "dimension", f"The older named spacer {n}."))

# ----------------------------------------------------------------- layout

lay = SPEC["core"].setdefault("layout", {})
put(lay, ("columns",), ref("--columns", "number", "The 12-column page grid."))
put(lay, ("page-max-width",), ref("--page-max-width", "dimension", "The 1440px page shell max width."))
put(lay, ("page-lateral-spacer",), ref("--page-lateral-spacer", "dimension", "The 24px page side padding."))
gut = lay.setdefault("gutter", {})
for n in sorted(R):
    if n.startswith("--gutter"):
        key = n[len("--gutter"):].strip("-").lower() or "base"
        put(gut, (key,), ref(n, "dimension", f"The {n} grid gutter."))
bp = lay.setdefault("breakpoint", {})
BPS = set()
for r in V.get("theme", []) + V.get("app", []):
    for c in r.get("context", []):
        for m in re.finditer(r"@media \((min|max)-width: (\d+(?:\.\d+)?)em\)", c):
            BPS.add((m.group(2), m.group(1)))
for em, kind in sorted(BPS, key=lambda x: float(x[0])):
    put(bp, (f"{kind}-{em}em",), lit(f"{float(em)*16:g}px", "dimension",
        f"@media ({kind}-width: {em}em) context in the readable sheets (raw/css-vars.json)",
        f"A responsive breakpoint the token sheets gate on — {em}em."))

# ------------------------------------------------------------------ other

rad = SPEC["core"].setdefault("radius", {})
for n in sorted(R):
    if n.startswith("--borders-corner-"):
        put(rad, (n[len("--borders-corner-"):],), ref(n, "dimension",
            "The square corner every surface and control paints (0px)." if n != "--borders-corner-rounded"
            else "The pill radius reserved for rounded controls (chips)."))

bw = SPEC["core"].setdefault("borderWidth", {})
for n in sorted(R):
    if n.startswith("--borders-border-"):
        put(bw, (n[len("--borders-border-"):],), ref(n, "dimension", f"The {n} stroke width."))

ic = SPEC["core"].setdefault("icon", {})
for n in sorted(R):
    if n.startswith("--icons-"):
        put(ic, tuple(n[len("--icons-"):].split("-")), ref(n, "dimension", f"The {n} icon box."))

bt = SPEC["core"].setdefault("button", {})
put(bt, ("base-padding",), ref("--button-base-padding", "dimension", "The 16px horizontal padding every button shares."))
put(bt, ("icon-positioning",), ref("--button-icon-positioning", "dimension", "The 12px icon offset inside a button."))
put(bt, ("icon-spacing",), ref("--button-icon-spacing", "dimension", "The 28px icon-to-label gap inside a button."))

mo = SPEC["core"].setdefault("motion", {})
for n in sorted(R):
    m = re.fullmatch(r"--motion-(functional|emotional)-(duration|easing)-(\w+)", n)
    if m:
        kind, prop, step = m.groups()
        ty = "duration" if prop == "duration" else "cubicBezier"
        put(mo, (kind, prop, step), ref(n, ty, f"The {kind} {prop} step {step} ({'UI control' if kind=='functional' else 'page-emphasis'} motion)."))

# ------------------------------------------------------- legacy palette

pal = SPEC["core"].setdefault("palette", {})
PAL_DESC = {
    "branco": "White — the page field.", "whiteSmoke": "The #f5f5f5 panel grey.",
    "shell": "The #eeeeee soft grey.", "platinum": "The #dddddd grey.",
    "silver": "The #cccccc grey.", "nimbus": "The #aaaaaa grey.",
    "hina": "The #888888 grey.", "emperor": "The #555555 grey.",
    "preto": "The #222222 ink — the signature black.", "red": "The #fd4f57 bright red.",
    "ouro": "The #c2a67d gold ('ouro' = gold).", "ouro-light": "The #e3c29d pale gold.",
    "beige": "The #eeccab beige.", "cadetBlue": "The #6092af muted blue.",
    "turquoise": "The #29ccbf turquoise.", "facebook": "The #4267b2 social blue.",
    "success": "The #3eb46e legacy success green.", "error": "The #e13f5a legacy error red.",
    "warning": "The #f4b350 legacy warning amber.",
}
for n in sorted(R):
    if re.fullmatch(r"--color-[a-zA-Z-]+", n):
        leaf = n[len("--color-"):]
        put(pal, ("named", leaf), ref(n, "color", PAL_DESC.get(leaf, f"The legacy named colour {n}.")))
for n in sorted(R):
    if re.fullmatch(r"--color[A-Z][a-zA-Z]+", n):
        leaf = n[len("--color"):]
        family = re.match(r"([A-Z][a-z]+)", leaf).group(1).lower()
        put(pal, ("legacy", family, leaf[len(family):].lower() or "base"), ref(n, "color", f"The legacy --{n[2:]} palette colour."))
for n in sorted(R):
    if re.fullmatch(r"--gradientAccess[A-Z][a-z]+(Start|End)?", n):
        leaf = n[len("--gradientAccess"):]
        m = re.fullmatch(r"([A-Z][a-z]+)(Start|End)?", leaf)
        tier, part = m.group(1).lower(), (m.group(2) or "").lower()
        if part:
            put(pal, ("access-gradient", tier, part), ref(n, "color", f"The {part} stop of the {tier} access-tier gradient."))
        else:
            raw = R[n]
            gm = re.fullmatch(r"linear-gradient\((\d+)deg,\s*(.+)\)", raw)
            if gm:
                stops = gradient_stops(gm.group(2))
                put(pal, ("access-gradient", tier, "gradient"), {
                    "value": [{"color": norm_color(c), "position": pos} for c, pos in stops],
                    "type": "gradient", "angle": f"{gm.group(1)}deg",
                    "source": f"css-var {n} resolved (raw/css-vars.json)",
                    "description": f"The {tier} FARFETCH Access tier gradient ({raw})."})

# ------------------------------------------------- the pulse colour layer
# --colors-<family>-<role>-<state>-<slot>: every semantic colour, exported
# whole under light.<family>.<role>.<state>.<slot>. The "general" family is
# flat (--colors-general-<leaf>); "forms" and "notifications" carry a
# variant segment between role and state.
STATES = {"enabled", "hover", "pressed", "active", "focus", "readonly", "selected", "disabled", "loading", "default"}
FAMILY = {
    "actions": "action", "forms": "form", "navigation": "navigation", "content": "content",
    "cards": "card", "messaging": "messaging", "notifications": "notification", "modality": "modality",
    "pos": "pos", "rating": "rating", "access": "access", "general": "general", "page": "page",
}
ROLE_DESC = {
    ("action", "primary"): "The filled ink button (Add To Bag, Sign Up).",
    ("action", "secondary"): "The outlined secondary button (Shop Now).",
    ("action", "tertiary"): "The quiet tertiary action.",
    ("action", "ghost-dark"): "The ghost action on light surfaces (icon buttons, carousel arrows).",
    ("action", "ghost-light"): "The ghost action on dark/photo surfaces.",
    ("action", "wishlist"): "The wishlist heart action.",
    ("navigation", "primary"): "The header/footer navigation colours.",
    ("navigation", "secondary"): "The secondary navigation colours (filter chips, selected rows).",
    ("navigation", "tertiary"): "The tertiary navigation colours.",
    ("content", "primary"): "Body content: card labels, prices, subtext and sale accents.",
    ("card", "light"): "Card on light surfaces.",
    ("card", "dark"): "Card on dark surfaces.",
    ("card", "highlight"): "The highlighted card.",
    ("messaging", "primary"): "The dark messaging banner/badge.",
    ("messaging", "secondary"): "The white-outlined messaging banner.",
    ("messaging", "tertiary"): "The translucent messaging banner.",
    ("messaging", "quaternary"): "The pale messaging badge.",
    ("notification", "light"): "The light toast/notice.",
    ("notification", "dark"): "The dark toast/notice.",
    ("modality", "primary"): "The modal/scrim layer colours.",
    ("modality", "secondary"): "The light scrim layer colours.",
    ("pos", "generic"): "The neutral price/point-of-sale badge.",
    ("pos", "promotions"): "The dark promotion badge.",
    ("pos", "sales"): "The #e71d34 sale badge.",
    ("rating", "primary"): "The star-rating colours.",
    ("page", "primary"): "The page surface and its loading state.",
    ("access", None): "The FARFETCH Access loyalty-tier palettes.",
}
light = SPEC["light"]
for n in sorted(R):
    m = re.match(r"--colors-([a-z]+)-(.+)$", n)
    if not m:
        continue
    fam_, rest = m.group(1), m.group(2)
    group = FAMILY[fam_]
    if fam_ == "general":
        put(light, (group, rest), ref(n, "color", f"The general {rest} role — part of the brand ramp and system colours."))
        continue
    if fam_ == "access":
        tier, _, num = rest.rpartition("-")
        put(light, (group, tier, num), ref(n, "color", f"The {tier} access-tier palette shade {num}."))
        continue
    segs = rest.split("-")
    # The state is the LAST state word — forms/notifications names carry a
    # variant segment before it (--colors-forms-primary-default-enabled-*,
    # where "default" is the variant, "enabled" the state).
    si = next((i for i in range(len(segs) - 1, 0, -1) if segs[i] in STATES), None)
    if si is None:
        put(light, (group, rest), ref(n, "color", f"The {rest} role."))
        continue
    role = "-".join(segs[:si])
    state = segs[si]
    slot = "-".join(segs[si + 1:])
    desc = ROLE_DESC.get((group, role)) or ROLE_DESC.get((group, role.split("-")[0])) or f"The {role} colours."
    put(light, (group, role, state, slot), ref(n, "color", f"{desc} ({state} {slot})."))

# ------------------------------------------------------------- components

comp = SPEC["component"]
COMP_DIMS = [
    ("header-height", "header", "default", "h", "The ~124px desktop top chrome (TopBar + NavBar)."),
    ("topbar-icon-size", "topbar-bag", "default", "w", "The 44px square icon hit area (bag, wishlist, account, locale)."),
    ("dept-link-height", "topbar-dept", "default", "h", "The 44px department link row."),
    ("logo-width", "logo", "default", "w", "The ~201px FARFETCH wordmark."),
    ("search-field-width", "search-field", "default", "w", "The ~270px header search field."),
    ("search-field-height", "search-field", "default", "h", "The 44px header search field."),
    ("search-submit-size", "search-submit", "default", "w", "The 32px search submit icon button."),
    ("hero-height", "hero-module", "default", "h", "The listing hero module (~1008px with the 3:4 campaign image)."),
    ("hero-cta-height", "hero-cta", "default", "h", "The 44px 'Shop Now' secondary button."),
    ("product-card-width", "product-card", "default", "w", "The ~336px listing product card (4-up at 1440)."),
    ("product-card-height", "product-card", "default", "h", "The ~557px product card."),
    ("card-wishlist-size", "card-wishlist", "default", "w", "The 44px wishlist heart hit area on a card."),
    ("filter-height", "filter-button", "default", "h", "The All Filters button height."),
    ("gallery-arrow-size", "pdp-arrow", "default", "w", "The carousel arrow hit area."),
    ("size-selector-height", "size-selector", "default", "h", "The 44px 'Select size' combobox."),
    ("add-to-bag-height", "add-to-bag", "default", "h", "The primary Add To Bag button."),
    ("pdp-wishlist-width", "pdp-wishlist", "default", "w", "The Wishlist secondary button beside Add To Bag."),
    ("accordion-button-height", "accordion-button", "default", "h", "The accordion section toggle row."),
    ("dept-tile-height", "dept-tile", "default", "h", "A home department chooser tile."),
    ("footer-height", "footer", "default", "h", "The desktop footer block."),
    ("news-field-width", "news-field", "default", "w", "The 300px newsletter email field."),
    ("news-submit-width", "news-submit", "default", "w", "The 90px 'Sign Up' button."),
    ("social-icon-size", "footer-social", "default", "w", "The 44px social icon hit area."),
    ("m-header-height", "m-header", "default", "h", "The top chrome at 390 wide."),
    ("m-dept-menu-width", "m-dept-menu", "default", "w", "The mobile departments dropdown trigger."),
    ("m-product-card-width", "m-product-card", "default", "w", "The product card at 390 wide."),
    ("m-add-to-bag-height", "m-add-to-bag", "default", "h", "The Add To Bag button at 390 wide."),
]
for name, cname, state, prop, desc in COMP_DIMS:
    try:
        s_ = C[cname]["states"][state]
        v = s_["rect"][prop] if prop in ("w", "h") else s_["style"][prop]
        if v and v not in ("0px", "auto", "rgba(0, 0, 0, 0)", 0):
            comp[name] = lit(("%gpx" % v) if isinstance(v, (int, float)) else v, "dimension",
                f"computed {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# measured state moves on the interactive controls
for name, cname, desc in [
    ("add-to-bag-track", "add-to-bag",
     "Add To Bag: the square #222 fill with white label at rest; hover lifts the fill toward #727272; focus paints a ring; pressed stays dark."),
    ("hero-cta-track", "hero-cta",
     "Shop Now secondary: white fill, #222 label and 1px #222 stroke at rest; hover shifts the palette per the secondary action track."),
    ("nav-link-track", "nav-link",
     "Category link: ink at rest; the hover/active navigation track keeps it monochrome — an underline/indicator, never a colour change."),
    ("nav-sale-track", "nav-sale",
     "Sale link: the pos-sales #e71d34 red in every state — the one chromatic item in the nav."),
    ("filter-track", "filter-button",
     "All Filters button: an outlined control at rest, hover per the secondary action track."),
    ("wishlist-heart-track", "card-wishlist",
     "Card wishlist heart: a ghost icon button over the photo; hover darkens/fills the heart."),
    ("search-field-track", "search-field",
     "Search field: the outlined 44px field; focused/filled tighten the stroke to ink."),
    ("size-selector-track", "size-selector",
     "Select size combobox: the 44px outlined field; hover shifts to the forms hover stroke."),
    ("news-submit-track", "news-submit",
     "Sign Up button: the square #222 fill with white label; hover lifts toward the primary hover surface."),
    ("pdp-wishlist-track", "pdp-wishlist",
     "PDP Wishlist: the outlined secondary action with the heart icon; the aria-pressed on state could not be opened in the static copy."),
]:
    try:
        states = {s2: {p: C[cname]["states"][s2]["style"][p] for p in ("backgroundColor", "color", "transform", "outlineStyle", "outlineColor", "borderTopColor", "borderColor") if C[cname]["states"][s2]["style"].get(p)}
                  for s2 in ("default", "hover", "pressed", "focus-visible", "focused", "filled")
                  if s2 in C[cname]["states"] and C[cname]["states"][s2].get("style")}
        if states:
            comp.setdefault("state-track", {})[name] = {
                "type": "other",
                "value": states,
                "source": f"computed styles of {cname} across states (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass

# the shared focus outline
for cname in ("nav-link", "add-to-bag", "hero-cta", "topbar-bag", "filter-button", "search-submit"):
    try:
        s = st(cname, "focus-visible")
        if s.get("outlineStyle") and s["outlineStyle"] != "none":
            comp["focus-ring"] = lit(
                f"{s['outlineWidth']} {s['outlineStyle']} {s['outlineColor']} offset {s.get('outlineOffset','')}".strip(),
                "other",
                f"computed outline of {cname} focus-visible (raw/components-computed.json)",
                "The painted focus indicator — a solid ring around the control.")
            break
    except KeyError:
        continue

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print("component-tokens.json:", {k: count(v) for k, v in SPEC.items() if isinstance(v, dict)})
