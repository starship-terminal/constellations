#!/usr/bin/env python3
"""Build raw/component-tokens.json, the token tree build_tokens.py resolves.

gumroad.com declares its design-token layer in a Tailwind v4 @theme plus a
hand-written semantic layer in the one design-*.css bundle:

  --pink --purple --green --orange --red --yellow
                               the flat brand palette (hex literals)
  --gray-1 --gray-2 --gray-3   alpha fractions (.1/.2/.5) the muted greys are
                               mixed at — numbers, not colours
  --accent --accent-with-text --primary --color --filled --active-bg
  --success --warning --danger --info --indicator
  --contrast-*                 semantic roles as `R G B` channel triplets
                               consumed as rgb(var(--x) / alpha); each has a
                               --contrast-* foreground partner
  --neutral-*                  the same roles for the neutral scheme
                               (creator pages re-tint the accent)
  --color-*                    the roles wrapped and resolved — rgb(var(--x)/a)
                               (--color-body/-background/-foreground/-border/
                               -muted/-primary(-foreground)/-accent(-foreground
                               |-with-text)/-active-bg/-indicator/-backdrop/
                               -danger(-foreground)/-success(-foreground)/
                               -warning(-foreground)/-info) plus the Tailwind
                               palette (--color-gray-100..800, --color-pink-*
                               --color-red-* --color-yellow-* --color-blue-*)
  --body-bg                    the page ground (#f4f4f0 light / #242423 dark)
  --border --border-alpha      the 1px solid border shorthand and its alpha
  --border-width --border-radius-1..3
                               the signature 1px borders and 4/8/16px radii
  --box-shadow-1 --box-shadow-2
                               the hard offset shadows (4px/8px, no blur,
                               re-pointed light #000 -> dark #ddd)
  --outline                    the 2px pink focus ring shorthand
  --spacer-1..8 --spacing      the 4px-based spacing scale
  --spacing-product-page --main-stack-width --dynamic-grid
  --grid-cols-sidebar --breakpoint-* --container-*
                               layout measures
  --form-element-height --button-hover-offset --big-icon-size
  --disabled-opacity           component measures
  --font-family --font-sans --font-mono --default-font-family
  --default-mono-font-family   ABC Favorit and the system fallbacks
  --font-weight-* --text-xs..9xl(+--line-height) --leading-* --tracking-*
                               the type ramp
  --transition-duration --default-transition-* --ease-* --animate-*
                               motion declarations
  --z-index-*                  the layering steps
  --logo --loading-spinner --product-cover-placeholder
                               image url() values (kept as declared)

Theme is @media (prefers-color-scheme:dark) — no in-page toggle. The dark
:root block re-points the channel triplets (--body-bg #242423, --color/
--filled swap, --border-alpha .35) and the markup carries dark:* utilities,
so the `light` and `dark` token sets resolve the same declarations under each
scheme. The product subdomain's inline :root pins a light palette — captured
as css-vars.json's product-light/product-dark resolutions and documented, not
a third theme.

Each leaf: {"type": ..., "var": "--name"} resolved per theme by
build_tokens.py, or a measured {"type", "value", "source"} for geometry the
DOM measurement pass recorded. Every leaf carries $extensions.source.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
R = V["resolved"]["light"]
RD = V["resolved"]["dark"]
TREE = {"core": {}, "light": {}, "dark": {}, "component": {}}


def emit_at(root, path, leaf):
    cur = TREE[root]
    parts = path.split(".")
    for p in parts[:-1]:
        cur = cur.setdefault(p, {})
    cur[parts[-1]] = leaf


def cam(name):
    """--foo-bar-baz -> fooBarBaz (a token key, not a CSS name)."""
    parts = name.lstrip("-").split("-")
    return parts[0] + "".join(p[:1].upper() + p[1:] for p in parts[1:])


KIND_TY = {"color": "color", "dimension": "dimension", "duration": "duration",
           "easing": "cubicBezier", "number": "number", "fontFamily": "fontFamily",
           "shadow": "shadow"}

emitted = set()


def VAR(name, ty, path, root="core", desc=None, themes=None):
    """Leaf resolved per theme from the var's declaration. themes limits which
    theme sets it lands in ('light'/'dark'/both) — a dark-only name exists in
    dark alone."""
    leaf = {"type": ty, "var": name}
    if desc:
        leaf["description"] = desc
    for t in (themes or ("light", "dark")):
        emit_at(t if root == "theme" else root, path, leaf)
    emitted.add(name)


def lit(value, ty, src, root="component", path=None, desc=None):
    leaf = {"type": ty, "value": value, "source": src}
    if desc:
        leaf["description"] = desc
    emit_at(root, path, leaf)


DIM_RE = re.compile(r"-?\d+(\.\d+)?(px|rem)$")


def dim_or_other(name):
    r = R.get(name) or RD.get(name)
    if r["kind"] == "dimension" or DIM_RE.fullmatch(str(r.get("value", r.get("raw", ""))).strip()):
        return "dimension"
    return "other"


# ---------------------------------------------------------------- palette (core)
# The flat brand palette — the literal hex set the channel roles are mixed
# from — and the Tailwind palette, all theme-independent.
BRAND = {
    "--pink": "the signature Gumroad pink — --accent resolves to it on gumroad.com",
    "--purple": "the brand purple; --info resolves to it",
    "--green": "the brand green; --success resolves to it",
    "--orange": "the brand orange; --warning resolves to it",
    "--red": "the brand red; --danger resolves to it",
    "--yellow": "the brand yellow",
}
for n, desc in BRAND.items():
    if n in R:
        VAR(n, "color", f"color.brand.{n[2:]}", desc=desc)
if "--info" in R:
    VAR("--info", "color", "color.brand.info", desc="the info accent — the purple channel triplet")
for n in ("--white", "--black"):
    if n in R:
        VAR(n, "color", f"color.{n[2:]}")
# The gray alpha fractions — the muted-greys' opacity stops, numbers not
# colours (consumed as rgb(var(--color) / var(--gray-N))).
for n in sorted(k for k in R if re.fullmatch(r"--gray-\d+", k)):
    VAR(n, "number", f"alpha.gray.{n[len('--gray-'):]}",
        desc="an alpha fraction the muted greys are mixed at — rgb(var(--color)/var(--gray-N))")
# The Tailwind palette the markup reads, kept as declared evidence under
# color.scale — brand colours already emitted above are skipped.
for n in sorted(k for k in R if re.fullmatch(r"--color-(white|black|gray|dark-gray|blue-600|gray-\d+|pink-\d+|red-\d+|yellow-\d+)", k)):
    VAR(n, "color", f"color.scale.{cam(n[len('--color-'):])}")

# ---------------------------------------------------------------- type (core)
FONT_DESCS = {
    "--font-family": "the product face: ABC Favorit, a licensed commercial face (not loaded here — samples fall back to the system sans), then the stack fallbacks",
    "--font-sans": "Tailwind's default font-sans utility face (not the product font)",
    "--font-mono": "Tailwind's default font-mono utility face",
    "--default-font-family": "the default body chain — the system sans set",
    "--default-mono-font-family": "the default code chain — the system mono set",
}
FONT_KEYS = {
    "--font-family": "product", "--font-sans": "systemSans", "--font-mono": "systemMono",
    "--default-font-family": "sans", "--default-mono-font-family": "mono",
}
for n, desc in FONT_DESCS.items():
    if n in R:
        VAR(n, "fontFamily", f"font.family.{FONT_KEYS[n]}", desc=desc)
for n in sorted(k for k in R if re.fullmatch(r"--font-weight-[a-z]+", k)):
    VAR(n, "fontWeight", f"font.weight.{n[len('--font-weight-'):]}")
TEXT_ORDER = ["xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "7xl", "8xl", "9xl"]
for n in sorted((k for k in R if re.fullmatch(r"--text-(xs|sm|base|lg|xl|\dxl)", k)), key=lambda s: TEXT_ORDER.index(s[len('--text-'):])):
    VAR(n, "dimension", f"font.size.{n[len('--text-'):]}")
for n in sorted(k for k in R if re.fullmatch(r"--text-(xs|sm|base|lg|xl|\dxl)--line-height", k)):
    VAR(n, "number", f"font.lineHeight.{n[len('--text-'):].replace('--line-height', '')}",
        desc="the ramp's unitless leading, declared as a calc() ratio")
for n in sorted(k for k in R if re.fullmatch(r"--leading-[a-z]+", k)):
    VAR(n, "number", f"font.leading.{n[len('--leading-'):]}")
for n in sorted(k for k in R if re.fullmatch(r"--tracking-[a-z]+", k)):
    # em-valued tracking keeps its declared unit: a px bake would stop
    # scaling with the element's font size.
    VAR(n, "other", f"font.tracking.{n[len('--tracking-'):]}")

# ------------------------------------------------------------- core scales
# The product's own border radii (small sharp set) and the Tailwind ramp.
for n in sorted(k for k in R if re.fullmatch(r"--border-radius-\d+", k)):
    VAR(n, "dimension", f"radius.{n[len('--border-radius-'):]}",
        desc="the product's own radius scale — squared, neo-brutalist corners")
for n in sorted(k for k in R if re.fullmatch(r"--radius-(xs|sm|md|lg|xl|2xl|3xl)", k)):
    VAR(n, "dimension", f"radius.tailwind.{n[len('--radius-'):]}")
if "--radius" in R:
    VAR("--radius", "dimension", "radius.tailwind.base")
if "--spacing" in R:
    VAR("--spacing", "dimension", "space.unit", desc="the 4px unit the spacing scale multiplies")
for n in sorted(k for k in R if re.fullmatch(r"--spacer-\d+", k)):
    VAR(n, "dimension", f"space.spacer.{n[len('--spacer-'):]}",
        desc="the product's own spacing scale")
for n in ("--border-width", "--form-element-height", "--button-hover-offset"):
    if n in R:
        VAR(n, dim_or_other(n), f"component.{cam(n)}")
if "--big-icon-size" in R:
    VAR("--big-icon-size", "other", "component.bigIconSize",
        desc="an em length — resolves per element")
for n in sorted(k for k in R if re.fullmatch(r"--breakpoint-[a-z0-9]+", k)):
    VAR(n, dim_or_other(n), f"breakpoint.{cam(n[len('--breakpoint-'):])}")
for n in sorted(k for k in R if re.fullmatch(r"--container-[a-z0-9]+", k)):
    VAR(n, dim_or_other(n), f"container.{cam(n[len('--container-'):])}")
for n in sorted(k for k in R if re.fullmatch(r"--ease-[a-z-]+", k)):
    VAR(n, "cubicBezier", f"ease.{cam(n[len('--ease-'):])}")
if "--default-transition-timing-function" in R:
    VAR("--default-transition-timing-function", "cubicBezier", "ease.default")
if "--default-transition-duration" in R:
    VAR("--default-transition-duration", "duration", "duration.default")
if "--transition-duration" in R:
    VAR("--transition-duration", "duration", "duration.fast",
        desc="the component transition length — hover, menus, toggles")
for n in sorted(k for k in R if re.fullmatch(r"--animate-[a-z-]+", k)):
    VAR(n, "other", f"animation.{cam(n[len('--animate-'):])}",
        desc="animation shorthand as declared")
for n in sorted(k for k in R if re.fullmatch(r"--z-index-[a-z-]+", k)):
    VAR(n, "number", f"zIndex.{cam(n[len('--z-index-'):])}")
if "--aspect-video" in R:
    VAR("--aspect-video", "other", "layout.aspectVideo", desc="an aspect-ratio fraction")
if "--disabled-opacity" in R:
    VAR("--disabled-opacity", "number", "opacity.disabled",
        desc="the disabled state — a plain opacity dim")
for n in ("--main-stack-width", "--spacing-product-page", "--dynamic-grid", "--grid-cols-sidebar"):
    if n in R:
        VAR(n, dim_or_other(n), f"layout.{cam(n)}")
if "--outline" in R:
    VAR("--outline", "other", "focus.outline",
        desc="the focus ring shorthand — 2px solid pink, applied :focus-visible")
for n in ("--logo", "--loading-spinner", "--product-cover-placeholder"):
    if n in R:
        VAR(n, "other", f"asset.{cam(n)}",
            desc="a url() image value — the reference kept, the asset itself not redistributed")

# ------------------------------------------------------- semantic roles
# Re-pointed per theme by the @media (prefers-color-scheme:dark) :root block:
# emitted into both `light` and `dark` sets so each resolves its own value.
#
# role.*       the --color-* resolved roles the markup consumes
# channels.*   the `R G B` triplet mechanism the roles are mixed from
GROUPS = [
    ("role", re.compile(r"--color-(body|background|foreground|border|muted|primary|primary-foreground|accent|accent-foreground|accent-with-text|active-bg|indicator|backdrop|danger|danger-foreground|success|success-foreground|warning|warning-foreground|info|pink|purple|green|orange|red|yellow)")),
    ("channels", re.compile(r"--(color|filled|primary|accent|accent-with-text|active-bg|success|warning|danger|info|indicator|contrast-[a-z]+|parent-color)")),
    ("neutral", re.compile(r"--neutral-(color|filled|accent|danger|border-alpha)")),
]
for group, pat in GROUPS:
    for n in sorted(k for k in set(R) | set(RD) if pat.fullmatch(k)):
        if n in emitted:
            continue
        leaf_name = cam(n[len('--color-'):]) if group == "role" else cam(n)
        themes = tuple(t for t in ("light", "dark") if n in (R if t == "light" else RD))
        kind = (R.get(n) or RD.get(n)).get("kind", "color")
        VAR(n, KIND_TY.get(kind, "other"), f"{group}.{leaf_name}", root="theme", themes=themes,
            desc="declared under the dark scheme only" if "light" not in themes else None)

# The page ground, the border shorthand and its alpha, the hard offset
# shadows — all re-pointed under the dark scheme.
for n, path, ty in [
    ("--body-bg", "ground.bodyBg", "color"),
    ("--border", "border.shorthand", "other"),
    ("--border-alpha", "border.alpha", "number"),
    ("--box-shadow-1", "shadow.hard.one", "shadow"),
    ("--box-shadow-2", "shadow.hard.two", "shadow"),
]:
    if n in R or n in RD:
        themes = tuple(t for t in ("light", "dark") if n in (R if t == "light" else RD))
        VAR(n, ty, path, root="theme", themes=themes)

# ------------------------------------------------------------------ misc
# Every remaining name declared in the product's own theme/app rules keeps
# its evidence under misc.
declared = set()
for bin_name in ("theme", "app", "darkscope"):
    for rule in V.get(bin_name, []):
        declared.update(rule.get("properties", {}))
for n in sorted(declared):
    if n in emitted or (n not in R and n not in RD):
        continue
    kind = (R.get(n) or RD.get(n)).get("kind", "other")
    themes = tuple(t for t in ("light", "dark") if n in (R if t == "light" else RD))
    VAR(n, KIND_TY.get(kind, "other"), f"misc.{cam(n)}", root="theme", themes=themes,
        desc="declared under the dark scheme only" if "light" not in themes else None)

# ------------------------------------------------- measured component tokens
C_PATH = RAW / "components-computed.json"
if not C_PATH.exists():
    # The measured section is required: without the file every measured token would vanish silently.
    raise SystemExit("build_component_tokens: raw/components-computed.json is missing")
if C_PATH.exists():
    C = json.loads(C_PATH.read_text()).get("components", {})

    def geom(comp, state, field, path, label):
        st = C.get(comp, {}).get("states", {}).get(state, {})
        rect = st.get("rect") or {}
        style = st.get("style") or {}
        v = rect.get(field) if field in rect else style.get(field)
        if v is None:
            return
        try:
            px = float(re.fullmatch(r"(-?\d+(?:\.\d+)?)(?:px)?", str(v)).group(1))
        except Exception:
            return
        lit(f"{px:g}px", "dimension",
            f"measured {comp} {state} on {C[comp].get('page')} ({label})",
            "component", path)

    geom("nav-bar", "default", "h", "header.height", "discover header bar")
    geom("nav-bar", "default", "w", "header.width", "discover header bar")
    geom("nav-search", "default", "h", "searchInput.height", "header search combobox")
    geom("nav-search", "default", "w", "searchInput.width", "header search combobox")
    geom("nav-start-selling", "default", "h", "button.cta.height", "the primary auth button")
    geom("nav-category", "default", "h", "categoryLink.height", "a category nav link")
    geom("discover-featured-card", "default", "h", "featuredCard.height", "a featured carousel card")
    geom("discover-featured-card", "default", "w", "featuredCard.width", "a featured carousel card")
    geom("discover-card", "default", "h", "productCard.height", "a market grid card")
    geom("discover-card", "default", "w", "productCard.width", "a market grid card")
    geom("discover-card-price", "default", "h", "priceFlag.height", "a card price flag")
    geom("discover-tab", "default", "h", "tab.height", "a market tab")
    geom("discover-load-more", "default", "h", "button.loadMore.height", "the bordered pagination button")
    geom("discover-currency-select", "default", "h", "select.height", "a select element")
    geom("login-card", "default", "w", "loginCard.width", "the centred auth card")
    geom("login-oauth", "default", "h", "button.oauth.height", "an OAuth button")
    geom("login-email", "default", "h", "input.height", "a text field")
    geom("login-submit", "default", "h", "button.submit.height", "the auth submit")
    geom("product-header", "default", "h", "productHeader.height", "the product title block")
    geom("product-tier", "default", "h", "tierCard.height", "a priced tier radio card")
    geom("product-tier", "default", "w", "tierCard.width", "a priced tier radio card")
    geom("product-term-select", "default", "h", "select.term.height", "the billing-term select")
    geom("product-buy", "default", "h", "button.buy.height", "the purchase link")
    geom("product-buy", "default", "w", "button.buy.width", "the purchase link")
    geom("checkout-email", "default", "h", "checkoutField.height", "a checkout field")
    geom("checkout-country", "default", "h", "checkoutSelect.height", "a checkout select")
    geom("checkout-summary", "default", "w", "checkoutSummary.width", "the order summary card")
    geom("home-search", "default", "h", "heroSearch.height", "the hero marketplace search")
    geom("m-nav-bar", "default", "h", "mobileHeader.height", "mobile header")
    geom("m-discover-card", "default", "h", "mobileCard.height", "a phone market card")

    def style_tok(comp, state, prop, path, ty, label):
        st = C.get(comp, {}).get("states", {}).get(state, {})
        v = (st.get("style") or {}).get(prop)
        if v is None:
            return
        lit(v, ty, f"measured {comp} {state} on {C[comp].get('page')} ({label})",
            "component", path)

    def radius_tok(comp, state, path, label):
        """The capture records the four corner properties, never the shorthand;
        emit the shared radius when all four agree. Chromium reports a fully
        rounded corner as its infinity clamp (3.35544e+07px) — that reads as a
        pill, emitted at the full-radius bound."""
        st = C.get(comp, {}).get("states", {}).get(state, {})
        s = st.get("style") or {}
        corners = [s.get(f"border{p}Radius") for p in
                   ("TopLeft", "TopRight", "BottomRight", "BottomLeft")]
        if not all(corners) or len(set(corners)) != 1:
            return
        v = corners[0]
        desc = None
        try:
            if float(re.fullmatch(r"(-?\d+(?:\.\d+)?(?:e\+?\d+)?)px", v).group(1)) >= 9999:
                v, desc = "9999px", "all four corners measure the full-radius clamp — a pill"
        except Exception:
            pass
        lit(v, "dimension",
            f"measured {comp} {state} on {C[comp].get('page')} ({label})",
            "component", path, desc=desc)

    def theme_alias(comp, state, prop, path, role, label):
        """A measured fill that lands on a declared semantic role: the element's
        class paints the role, so each theme set gets the alias and resolves
        its own value instead of inheriting the light measurement."""
        st = C.get(comp, {}).get("states", {}).get(state, {})
        v = (st.get("style") or {}).get(prop)
        if v is None:
            return
        leaf = {"type": "color", "value": "{" + role + "}",
                "source": f"measured {comp} {state} on {C[comp].get('page')} ({label}) — the element's class paints the {role} role, so each theme resolves its own",
                "description": label}
        for t in ("light", "dark"):
            emit_at(t, path, leaf)

    radius_tok("discover-card", "default", "card.radius", "a market product card")
    radius_tok("nav-search", "default", "searchInput.radius", "the header search field")
    radius_tok("nav-start-selling", "default", "button.cta.radius", "the primary auth button")
    radius_tok("discover-tab", "default", "tab.radius", "a market tab")
    radius_tok("login-email", "default", "input.radius", "a text field")
    radius_tok("product-tier", "default", "tierCard.radius", "a priced tier card")
    radius_tok("discover-card-price", "default", "priceFlag.radius", "a card price flag")
    radius_tok("checkout-email", "default", "checkoutField.radius", "a checkout field")

    # Measured fills that land on declared roles alias the role token, so each
    # theme resolves its own value.
    theme_alias("nav-start-selling", "default", "backgroundColor", "component.cta.bg", "role.primary", "the primary CTA fill")
    theme_alias("discover-tab-active", "default", "backgroundColor", "component.tabActive.bg", "role.background", "the selected market tab fill")
    theme_alias("discover-card-price", "default", "backgroundColor", "component.priceFlag.bg", "role.accent", "the price flag fill")
    theme_alias("nav-bar", "default", "backgroundColor", "component.header.bg", "ground.bodyBg", "the header bar ground")
    theme_alias("discover-card", "default", "backgroundColor", "component.card.bg", "role.background", "the product card surface")

    # Measured type styles as DTCG typography composites — DESIGN.md reads
    # tokens under core.typography. letterSpacing stays in px as measured.
    def typ(comp, path, name, state="default"):
        st = C.get(comp, {}).get("states", {}).get(state, {})
        # A wrapper whose own font is inherited body type records its prominent
        # child text under textStyle (product-header's h1 is 40/48 while the
        # header block sits at 16/22) — prefer it so the token carries the
        # heading geometry a reader means.
        s = st.get("textStyle") or st.get("style") or {}
        if not s.get("fontSize"):
            return
        style = {
            "fontFamily": s["fontFamily"],
            "fontSize": s["fontSize"],
            "fontWeight": int(float(s["fontWeight"])),
            "lineHeight": s["lineHeight"],
        }
        if s.get("letterSpacing") and s["letterSpacing"] != "normal":
            style["letterSpacing"] = s["letterSpacing"]
        leaf = {"$value": style, "$type": "typography",
                "$description": name,
                "$extensions": {"source": f"measured {comp} on {C[comp].get('page')} ({state} state)"}}
        emit_at("core", path, leaf)

    typ("home-h1", "typography.display", "the landing hero heading — ABC Favorit display")
    typ("nav-logo", "typography.wordmark", "the GUMROAD wordmark — uppercased display type")
    typ("product-header", "typography.h1", "a product page title block")
    typ("nav-category", "typography.navLink", "a category nav link")
    typ("discover-tab", "typography.tab", "a market tab label")
    typ("nav-start-selling", "typography.button", "the primary button label")
    typ("discover-card-price", "typography.price", "the price flag label")
    typ("login-email", "typography.input", "a form field")
    typ("product-buy", "typography.buy", "the purchase link label")

(RAW / "component-tokens.json").write_text(json.dumps(TREE, indent=1, ensure_ascii=False) + "\n")
print({k: sum(1 for _ in json.dumps(v).split('"type"')) - 1 for k, v in TREE.items()})
