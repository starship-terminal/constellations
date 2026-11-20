#!/usr/bin/env python3
"""Build raw/component-tokens.json, the token tree build_tokens.py resolves.

Handshake's two signed-out surfaces ship two declared token layers:

  joinhandshake.com (the marketing site, a Next.js app) — a thin declared
  layer over Tailwind v4 utilities. The honest :root declarations are the
  font faces (--font-noi-grotesk, --font-sans-plomb(-swap), the retro
  --font-chicago-flf/--font-geneva used on the marketing-toolkit pages), the
  --spacing unit, --container-3xs..7xl, --leading-xs..xl, --tracking-sm/-lg,
  --font-weight-light..bold, --ease-in/-out/-in-out,
  --default-transition-duration/-timing-function, --animate-pulse/-spin,
  --blur-sm..2xl, --drop-shadow-md/-2xl, --aspect-video, and the nav/hero
  geometry vars (--desktop-nav-height/-top-offset(-with-banner),
  --full-desktop/-tablet/-mobile-nav-height, --notification-banner-height/
  -offset, --container-padding). The CTA colours exist only as Tailwind
  arbitrary-property utility declarations --cta:#2e6aff /
  --cta-hover:#1552d6 / --cta-active|visited:#6fbb28 and --bg:#14151c /
  --text:#14151c on one-off classes — still the product's own declared
  values, recorded with their utility source. One page (/research/ai/) is a
  Framer site whose body declares ~100 --token-<uuid> colour styles — the
  marketing palette the Framer page paints (lime #d3fb52, blue #2e6aff,
  ink #14151c, the rainbow accents); the UUIDs are kept as the token leaf
  names because they are the declared names. The Ketch consent sheet's
  --k-*/--lanyard vars and Framer's --framer-* internals are vendor
  plumbing, not product tokens, and stay in raw/css-vars.json only.

  app.joinhandshake.com (the consumer app) — the /access "Log in or sign up"
  page ships the Rosetta design system from handshake-production-cdn: the
  semantic --rosetta-bg-*/--rosetta-fg-*/--rosetta-interactive-*/
  --rosetta-shadow-*/--rosetta-avatar-* colours, the --rosetta-size-*/
  --rosetta-spacing-*/--rosetta-type-*/--rosetta-font-family-*/--rosetta-
  typography-font-family-* scales, the component vars (--button-*,
  --nav-*, --popover-*, --modal-*, --listbox-*, --select-*, --tag-*,
  --slider-*, --tooltip-*, --day-picker-*, --feature-callout-*,
  --segmented-toggle-*, --loading-spinner-*) and the deprecated
  --rosetta-colors-* names (kept under access.deprecated).

Both surfaces paint light only: no theme class, no theme control, no
prefers-color-scheme rule. There is no dark set — nothing was inferred.

Each leaf: {"type", "var": "--name"} resolved by build_tokens.py in the
shell it was harvested from (marketing names under the marketing sheets,
rosetta names under the app sheets), or a measured {"type", "value",
"source"} from raw/components-computed.json. Every leaf carries
$extensions.source.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SITE = V["resolved"].get("site", {})
APP = V["resolved"].get("app", {})
TREE = {"core": {}, "light": {}, "access": {}, "component": {}}


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
           "easing": "cubicBezier", "number": "number", "fontFamily": "fontFamily"}

emitted = set()


def VAR(name, ty, path, root="core", desc=None):
    leaf = {"type": ty, "var": name}
    if desc:
        leaf["description"] = desc
    emit_at(root, path, leaf)
    emitted.add(name)


def lit(value, ty, src, root="component", path=None, desc=None):
    leaf = {"type": ty, "value": value, "source": src}
    if desc:
        leaf["description"] = desc
    emit_at(root, path, leaf)


DIM_RE = re.compile(r"-?\d+(\.\d+)?(px|rem)$")


def dim_or_other(name, R=SITE):
    r = R.get(name) or {}
    if r.get("kind") == "dimension" or DIM_RE.fullmatch(str(r.get("value", r.get("raw", ""))).strip()):
        return "dimension"
    return "other"


# ---------------------------------------------------------------- palette (core)
# The marketing site's declared colours live in two places: a handful of
# Tailwind arbitrary-property utilities (--cta etc. — the declaration only
# resolves on the element carrying its own utility class, so the literal
# declared value is emitted with the rule as source) and the Framer page's
# --token-<uuid> colour styles. Both are the product's own declared values.
UTIL = {}
for _r in V.get("utility", []):
    for _n, _v in _r.get("properties", {}).items():
        UTIL.setdefault(_n, (_v, _r["selector"]))
for n in sorted(k for k in UTIL if re.fullmatch(r"--(cta(-active|-hover|-visited)?|bg|text)", k)):
    lit(UTIL[n][0], "color",
        f"css-var {n} declared on the Tailwind arbitrary-property utility class {UTIL[n][1]} — the product's own value applied per element, not a :root variable",
        "core", f"color.site.{cam(n)}")
    emitted.add(n)
for n in sorted(k for k in SITE if re.fullmatch(r"--token-[0-9a-f-]{36}", k)):
    VAR(n, "color", f"color.framer.{n[len('--token-'):]}",
        desc="a Framer colour style declared on body of the Framer-built /research/ai/ page — the marketing palette that page paints")
# The grid gap vars live on the same utility classes; they are dimensions.
for n in sorted(k for k in UTIL if re.fullmatch(r"--grid-gap-x-(desktop|mobile|tablet)", k)):
    lit(UTIL[n][0], "dimension",
        f"css-var {n} declared on the Tailwind arbitrary-property utility class {UTIL[n][1]}",
        "core", f"layout.{cam(n)}")
    emitted.add(n)

# ---------------------------------------------------------------- type (core)
FONT_DESCS = {
    "--font-noi-grotesk": "NoiGrotesk — the marketing site's display/brand face with its metrics-matched fallback",
    "--font-sans-plomb": "SansPlomb — the body face with its metrics-matched fallback",
    "--font-sans-plomb-swap": "SansPlombSwap — the swap-metrics twin the site pairs with sans-plomb",
    "--font-chicago-flf": "Chicago FLF — the retro bitmap face used on the career-centers marketing toolkit",
    "--font-geneva": "Geneva — the retro face paired with Chicago on the toolkit pages",
}
for n, desc in FONT_DESCS.items():
    if n in SITE:
        VAR(n, "fontFamily", f"font.family.{cam(n[len('--font-'):])}", desc=desc)
for n in sorted(k for k in SITE if re.fullmatch(r"--font-weight-(light|normal|medium|semibold|bold)", k)):
    VAR(n, "fontWeight", f"font.weight.{n[len('--font-weight-'):]}")
for n in sorted(k for k in SITE if re.fullmatch(r"--leading-[a-z]+", k)):
    # leading is declared in % (85..140%); DTCG number keeps the ratio.
    v = SITE[n].get("value", SITE[n]["raw"])
    m = re.fullmatch(r"([\d.]+)%", str(v).strip())
    lit(round(float(m.group(1)) / 100, 4) if m else v, "number" if m else "other",
        f"css-var {n} (site)", "core", f"font.leading.{n[len('--leading-'):]}")
    emitted.add(n)
for n in sorted(k for k in SITE if re.fullmatch(r"--tracking-[a-z]+", k)):
    # em-valued tracking keeps its declared unit.
    VAR(n, "other", f"font.tracking.{n[len('--tracking-'):]}")

# ------------------------------------------------------------- core scales
if "--spacing" in SITE:
    VAR("--spacing", "dimension", "space.unit", desc="the 4px unit the spacing scale multiplies")
for n in sorted(k for k in SITE if re.fullmatch(r"--container-(3xs|2xs|xs|sm|md|lg|xl|2xl|3xl|4xl|5xl|6xl|7xl|padding)", k)):
    VAR(n, dim_or_other(n), f"container.{cam(n[len('--container-'):])}")
for n in sorted(k for k in SITE if re.fullmatch(r"--breakpoint-[a-z0-9]+", k)):
    VAR(n, dim_or_other(n), f"breakpoint.{cam(n[len('--breakpoint-'):])}")
for n in sorted(k for k in SITE if re.fullmatch(r"--ease-(in|out|in-out)", k)):
    VAR(n, "cubicBezier", f"ease.{cam(n[len('--ease-'):])}")
if "--default-transition-timing-function" in SITE:
    VAR("--default-transition-timing-function", "cubicBezier", "ease.default")
if "--default-transition-duration" in SITE:
    VAR("--default-transition-duration", "duration", "duration.default")
for n in sorted(k for k in SITE if re.fullmatch(r"--blur-(sm|md|xl|2xl)", k)):
    VAR(n, "dimension", f"blur.{n[len('--blur-'):]}")
for n in sorted(k for k in SITE if re.fullmatch(r"--drop-shadow-[a-z0-9]+", k)):
    VAR(n, "other", f"shadow.{cam(n[len('--drop-shadow-'):])}",
        desc="drop-shadow filter value, kept as the computed string")
for n in sorted(k for k in SITE if re.fullmatch(r"--animate-[a-z-]+", k)):
    VAR(n, "other", f"animation.{cam(n[len('--animate-'):])}", desc="animation shorthand as declared")
if "--aspect-video" in SITE:
    VAR("--aspect-video", "other", "aspect.video")

# ------------------------------------------------------- nav/hero geometry
for n in sorted(k for k in SITE if re.fullmatch(r"--(desktop|mobile|tablet)-nav-[a-z-]+|--full-(desktop|tablet|mobile)-nav-height|--notification-banner-(height|offset)|--banner-height", k)):
    VAR(n, dim_or_other(n), f"layout.{cam(n)}")

# ------------------------------------------------------- light roles (measured)
# The marketing site has no :root role layer — its roles are the painted
# computed styles of the live page chrome and copy. Each is a literal
# measured value with its measurement as source; none is invented.
C_PATH = RAW / "components-computed.json"
# Required: without it every measured token would drop silently.
C = json.loads(C_PATH.read_text())["components"]


def style_tok(comp, state, prop, path, ty, label, root="light"):
    st = C.get(comp, {}).get("states", {}).get(state, {})
    v = (st.get("style") or {}).get(prop)
    if v is None:
        return
    lit(v, ty, f"measured {comp} {state} on {C[comp].get('page')} ({label})", root, path)


def state_tok(comp, state, prop, path, ty, label, root="light"):
    st = C.get(comp, {}).get("states", {}).get(state, {})
    v = (st.get("style") or {}).get(prop)
    if v is None:
        return
    lit(v, ty, f"measured {comp} {state} on {C[comp].get('page')} ({label})", root, path)


# page paint — the body carries no fill, so the page's own surfaces are the
# painted section bands the layout probe recorded (blog alternates
# bg-neutral-0 / bg-neutral-10) plus the measured chrome below.
L_PATH = RAW / "layout.json"
if L_PATH.exists():
    L = json.loads(L_PATH.read_text())
    bands = {}
    for page_key, probe in L.items():
        for s in (probe or {}).get("sections") or []:
            el, bg = s.get("el") or "", s.get("bg")
            if bg and "neutral-0" in el:
                bands.setdefault("white", (bg, page_key, el))
            if bg and "neutral-10" in el:
                bands.setdefault("muted", (bg, page_key, el))
    for path, band, label in (
        ("bg.page", "white", "the bg-neutral-0 white band the index pages alternate"),
        ("bg.muted", "muted", "the bg-neutral-10 band between the white ones"),
    ):
        if band in bands:
            bg, page_key, el = bands[band]
            lit(bg, "color", f"painted section band '{el}' measured by the layout probe on {page_key} ({label})", "light", path)

style_tok("hs-nav", "default", "backgroundColor", "bg.nav", "color", "the fixed nav bar fill")
style_tok("hs-footer", "default", "backgroundColor", "bg.footer", "color", "the footer band fill")
style_tok("hs-nav-link", "default", "color", "fg.navLink", "color", "nav item text")
style_tok("hs-signup-button", "default", "backgroundColor", "button.primary.bg", "color", '"Sign up" button fill')
style_tok("hs-signup-button", "default", "color", "button.primary.fg", "color", '"Sign up" button label')
style_tok("hs-signup-button", "hover", "backgroundColor", "button.primary.hover", "color", '"Sign up" button hover fill')
style_tok("hs-login-link", "default", "color", "link.nav", "color", '"Log in" link colour')
style_tok("hs-cta", "default", "backgroundColor", "cta.bg", "color", "CTA pill fill")
style_tok("hs-cta", "default", "color", "cta.fg", "color", "CTA pill label")
style_tok("hs-cta", "hover", "backgroundColor", "cta.hover", "color", "CTA pill hover fill")
style_tok("stu-text-link", "default", "color", "link.accent", "color", "the arrow text link colour")
style_tok("stu-text-link", "hover", "color", "link.accentHover", "color", "the arrow text link hover")
style_tok("hs-footer-link", "default", "color", "link.footer", "color", "footer link colour")
style_tok("hs-search-input", "default", "backgroundColor", "input.search.bg", "color", "hero search field fill")
style_tok("hs-search-input", "default", "borderTopColor", "input.search.border", "color", "hero search field border")
style_tok("hs-filter-pill", "default", "backgroundColor", "pill.bg", "color", "job-type pill fill")
style_tok("hs-banner", "default", "backgroundColor", "banner.bg", "color", "notification banner fill")
style_tok("hs-segment-tab", "default", "color", "tab.fg", "color", "segment tab text (the unselected tab paints a muted grey)")
style_tok("car-dept-button", "default", "color", "fg.body", "color", "department accordion header text — the ink body copy")
style_tok("hs-faq", "default", "color", "accordion.question", "color", "FAQ question text")
style_tok("hs-hero-h1", "default", "color", "fg.headline", "color", "hero headline ink")
style_tok("hs-hero-h1", "default", "fontSize", "type.hero.size", "other", "hero headline size")
style_tok("hs-hero-h1", "default", "lineHeight", "type.hero.lineHeight", "other", "hero headline leading")
style_tok("legal-nav-active", "default", "color", "nav.legalActive", "color", "legal rail active link")
style_tok("legal-nav-link", "default", "color", "nav.legal", "color", "legal rail link")

# ------------------------------------------------------------ access set
# The Rosetta layer: every --rosetta-*/component var resolved inside the app
# shell. --rosetta-colors-* names carry "--deprecated" in their names and
# land under access.deprecated.
COMP_PREFIX = ("day-picker", "feature-callout", "loading-spinner", "date-picker", "segmented-toggle", "tip-popover", "side-sheet",
               "button", "checkbox", "avatar", "badge", "breadcrumbs", "listbox", "menu", "modal", "nav",
               "popover", "select", "skeleton", "slider", "submenu", "tag", "tooltip")
for n in sorted(APP):
    if n.startswith("--rosetta-colors-"):
        emit_at("access", f"deprecated.{cam(n[len('--rosetta-colors-'):].replace('--deprecated', ''))}",
                {"type": "color" if APP[n].get("kind") == "color" else "other", "var": n,
                 "description": "a --rosetta-colors-* name the Rosetta sheet marks deprecated"})
        emitted.add(n)
        continue
    comp = next((p for p in COMP_PREFIX if n.startswith("--" + p + "-")), None)
    if not n.startswith("--rosetta-") and comp is None:
        continue
    kind = APP[n].get("kind")
    ty = KIND_TY.get(kind, "other")
    stripped = n[2:]
    if stripped.startswith("rosetta-"):
        parts = stripped[len("rosetta-"):].split("-")
        root = parts[0]  # bg fg interactive shadow size spacing type font avatar typography colors
        rest = "-".join(parts[1:])
        path = f"{cam('rosetta-' + root)}.{cam(rest)}" if rest else cam("rosetta-" + root)
    else:
        path = f"component.{cam(comp)}.{cam(stripped[len(comp) + 1:])}"
    # rosetta shadow vars are shadow strings -> "other" (kept as the computed
    # string; a DTCG shadow composite would invent offsets the raw string did
    # not split).
    if "shadow" in n:
        ty = "other"
    emit_at("access", path, {"type": ty, "var": n})
    emitted.add(n)

# ------------------------------------------------- measured component tokens
if C:
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

    geom("hs-nav", "default", "h", "nav.height", "fixed pill nav height")
    geom("hs-nav", "default", "w", "nav.width", "fixed pill nav width")
    geom("hs-signup-button", "default", "h", "button.signup.height", "nav sign-up button")
    geom("hs-search-input", "default", "h", "input.search.height", "hero search field")
    geom("hs-search-button", "default", "h", "button.search.height", '"Search jobs" button')
    geom("hs-filter-pill", "default", "h", "pill.height", "job-type pill")
    geom("hs-banner", "default", "h", "banner.height", "notification banner")
    geom("hs-footer", "default", "h", "footer.height", "footer band")
    geom("hs-faq", "default", "h", "accordion.rowHeight", "FAQ question row")
    geom("hs-cta", "default", "h", "button.cta.height", "CTA pill")
    geom("app-email-field", "default", "h", "input.email.height", "login email field")
    geom("app-continue-button", "default", "h", "button.continue.height", '"Continue with email" button')
    geom("app-shell", "default", "w", "page.width", "the /access page shell — the viewport-wide main, not the card (the card itself is not separately measured)")
    geom("m-hs-topbar", "default", "h", "mobileHeader.height", "mobile top bar")
    geom("m-hs-hamburger", "default", "h", "mobileMenuButton.size", '"Open menu" button')
    geom("m-hs-drawer", "opened", "w", "mobileDrawer.width", "opened nav sheet")

    def radius_tok(comp, state, path, label):
        """The capture records the four corner properties, never the shorthand;
        emit the shared radius when all four agree. Chromium reports a fully
        rounded corner as its infinity clamp — that reads as a pill, emitted
        at the full-radius bound."""
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

    radius_tok("hs-nav", "default", "nav.radius", "pill nav corner")
    radius_tok("hs-signup-button", "default", "button.signup.radius", "nav sign-up corner")
    radius_tok("hs-search-input", "default", "input.search.radius", "search field corner")
    radius_tok("hs-search-button", "default", "button.search.radius", '"Search jobs" corner')
    radius_tok("hs-filter-pill", "default", "pill.radius", "job-type pill corner")
    radius_tok("hs-cta", "default", "button.cta.radius", "CTA corner")
    radius_tok("app-email-field", "default", "input.email.radius", "login email field corner")
    radius_tok("app-continue-button", "default", "button.continue.radius", '"Continue" corner')
    radius_tok("blog-card", "default", "card.blog.radius", "article card corner")

    # Measured type styles as DTCG typography composites — DESIGN.md reads
    # tokens under core.typography. letterSpacing stays in px as measured.
    def typ(comp, path, name):
        st = C.get(comp, {}).get("states", {}).get("default", {})
        # The capture records the painted text node's own style in textStyle
        # when it differs from the component's box — prefer it (a pill's label
        # is smaller than the pill's own inherited font).
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
                "$extensions": {"source": f"measured {comp} on {C[comp].get('page')} (default state)"}}
        emit_at("core", path, leaf)

    typ("hs-hero-h1", "typography.display", "the hero headline — the brand face at its largest")
    typ("hs-nav-link", "typography.navLink", "a nav section item")
    typ("hs-signup-button", "typography.button", "the nav sign-up button label")
    typ("hs-search-button", "typography.searchButton", 'the "Search jobs" button label')
    typ("hs-filter-pill", "typography.pill", "a job-type pill label")
    typ("hs-faq", "typography.accordion", "an FAQ question")
    typ("hs-footer-link", "typography.footerLink", "a footer link")
    typ("hs-cta", "typography.cta", "a CTA pill label")
    typ("stu-text-link", "typography.arrowLink", "the arrow-suffixed text link")
    typ("app-email-field", "typography.input", "the login email field text")
    typ("app-continue-button", "typography.appButton", 'the "Continue with email" button label')
    typ("blog-category-link", "typography.category", "an uppercase blog category link")
    typ("legal-nav-link", "typography.legalNav", "a legal rail link")

(RAW / "component-tokens.json").write_text(json.dumps(TREE, indent=1, ensure_ascii=False) + "\n")
print({k: sum(1 for _ in json.dumps(v).split('"type"')) - 1 for k, v in TREE.items()})
