#!/usr/bin/env python3
"""Build raw/component-tokens.json, the token tree build_tokens.py resolves.

huddlekit.com — and app.huddlekit.com, the product shell on the same
design system — declares its token layer in a Tailwind v4 @theme plus a
hand-written shadcn-style semantic layer:

  Semantic roles (re-pointed per theme):
    --background/--foreground, --primary(-foreground),
    --secondary(-foreground), --accent(-foreground),
    --muted(-foreground), --card(-foreground), --popover(-foreground),
    --destructive, --border, --input, --ring,
    --sidebar(-foreground|-accent|-accent-foreground|-primary|
              -primary-foreground|-border|-ring),
    --chart-1..5, --upgrade(-foreground|-muted-foreground), --canvas,
    --color-page, --color-primary-dark,
    --scroll-mask-t/-b/-l/-r-from, --mode-glow-strength
  Scales (theme-independent):
    --radius .75rem, --radius-xs/-md/-lg/-xl/-2xl,
    --spacing .25rem, --container-xs..5xl, --blur-sm/-md,
    --aspect-video, --animate-ping/-pulse/-spin,
    --ease-in/-in-out/-out, --default-transition-*,
    --section-padding, --section-gap, --card-gap
  Type:
    --font-sans ("Inter","Inter Fallback",sans-serif — next/font), --font-inter,
    --font-geist-mono ("Geist Mono", next/font), --font-mono (ui-monospace
    stack), --font-weight-normal/-medium/-semibold/-bold; the
    --text-xs..7xl ramp (+ --*-line-height calc ratios), --leading-tight/
    -snug/-normal/-relaxed, --tracking-tighter/-tight/-normal/-wider/-widest.
  Vendor: Tailwind's --color-* generic palette and --tw-* internals stay out
    of the token tree (the tailwind bin is recorded in css-vars.json but not
    promoted to tokens).

Theme: huddlekit.com paints light only — its `.dark` rules re-point the same
names inside nested .dark panels (the MCP card, dark testimonials, the
footer), never on <html>. app.huddlekit.com paints html.dark +
data-theme="dark" under prefers-color-scheme — the resolved `dark` set comes
from those declarations applied on a probe carrying the app's own sheets,
verified against the app's painted dark login. `light` and `dark` resolve
the same names under each class.

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
           "easing": "cubicBezier", "number": "number", "fontFamily": "fontFamily"}

emitted = set()


def VAR(name, ty, path, root="core", desc=None, themes=None):
    """Leaf resolved per theme from the var's declaration. themes limits which
    theme sets it lands in ('light'/'dark'/both) — a .dark-only name exists in
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


# A var resolved "other" that is a plain px/rem length is still a dimension
# token (rem is a valid DTCG length); only non-length others stay "other".
DIM_RE = re.compile(r"-?\d+(\.\d+)?(px|rem)$")
def dim_or_other(name):
    r = R.get(name) or RD.get(name)
    if r["kind"] == "dimension" or DIM_RE.fullmatch(str(r.get("value", r.get("raw", ""))).strip()):
        return "dimension"
    return "other"

def both_themes(name):
    return tuple(t for t in ("light", "dark") if name in (R if t == "light" else RD))


# ---------------------------------------------------------------- type (core)
FONT_DESCS = {
    "--font-sans": "the product face — \"Inter\",\"Inter Fallback\",sans-serif loaded through next/font; body text and UI",
    "--font-inter": "Inter — the next/font face itself (with its metrics-matched fallback)",
    "--font-geist-mono": "Geist Mono — the next/font mono face (with fallback); code and MCP snippets",
    "--font-mono": "the mono face — ui-monospace system stack; inline code and pre blocks",
    "--default-font-family": "Tailwind's default body font chain",
    "--default-mono-font-family": "Tailwind's default code font chain",
}
FONT_KEYS = {
    "--font-sans": "sans", "--font-inter": "inter",
    "--font-geist-mono": "geistMono", "--font-mono": "mono",
    "--default-font-family": "defaultSans", "--default-mono-font-family": "defaultMono",
}
for n, desc in FONT_DESCS.items():
    if n in R:
        VAR(n, "fontFamily", f"font.family.{FONT_KEYS[n]}", desc=desc)
for n in sorted(k for k in R if re.fullmatch(r"--font-weight-[a-z]+", k)):
    VAR(n, "fontWeight", f"font.weight.{n[len('--font-weight-'):]}")
TEXT_ORDER = ["xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "7xl", "8xl", "9xl"]
for n in sorted((k for k in R if re.fullmatch(r"--text-(xs|sm|base|lg|xl|\dxl)", k)),
                key=lambda s: TEXT_ORDER.index(s[len('--text-'):])):
    VAR(n, "dimension", f"font.size.{n[len('--text-'):]}")
for n in sorted(k for k in R if re.fullmatch(r"--text-(xs|sm|base|lg|xl|\dxl)--line-height", k)):
    VAR(n, "number", f"font.lineHeight.{n[len('--text-'):].replace('--line-height', '')}")
for n in sorted(k for k in R if re.fullmatch(r"--leading-[a-z]+", k)):
    VAR(n, "number", f"font.lineHeight.{n[len('--leading-'):]}")
for n in sorted(k for k in R if re.fullmatch(r"--tracking-[a-z]+", k)):
    # em-valued tracking keeps its declared unit: a px bake would stop
    # scaling with the element's font size.
    VAR(n, "other", f"font.tracking.{n[len('--tracking-'):]}")

# ------------------------------------------------------------- core scales
for n in sorted(k for k in R if re.fullmatch(r"--radius.*", k)):
    VAR(n, "dimension", f"radius.{'base' if n == '--radius' else cam(n[len('--radius-'):])}")
if "--spacing" in R:
    VAR("--spacing", "dimension", "space.unit", desc="the 4px unit the spacing scale multiplies")
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
for n in sorted(k for k in R if re.fullmatch(r"--blur-[a-z0-9]+", k)):
    VAR(n, "dimension", f"blur.{n[len('--blur-'):]}")
for n in sorted(k for k in R if re.fullmatch(r"--drop-shadow-[a-z0-9]+", k)):
    VAR(n, "other", f"shadow.{cam(n[len('--drop-shadow-'):])}",
        desc="drop-shadow filter value, kept as the computed string")
for n in sorted(k for k in R if re.fullmatch(r"--animate-[a-z-]+", k)):
    VAR(n, "other", f"animation.{cam(n[len('--animate-'):])}",
        desc="animation shorthand as declared")
for n in ("--aspect-video",):
    if n in R:
        VAR(n, dim_or_other(n), f"layout.{cam(n)}")
# The layout rhythm vars: --section-padding (5rem), --section-gap (3rem) and
# --card-gap (1rem) — same in both themes, so core tokens.
for n in ("--section-padding", "--section-gap", "--card-gap"):
    if n in R:
        VAR(n, "dimension", f"layout.{cam(n)}")

# ------------------------------------------------------- semantic roles
# Re-pointed per theme: emitted into both `light` and `dark` sets, or into
# `dark` alone where the name is declared under .dark only.
GROUPS = [
    ("primary", re.compile(r"--primary(-foreground)?")),
    ("secondary", re.compile(r"--secondary(-foreground)?")),
    ("accent", re.compile(r"--accent(-foreground)?")),
    ("muted", re.compile(r"--muted(-foreground)?")),
    ("card", re.compile(r"--card(-foreground)?")),
    ("popover", re.compile(r"--popover(-foreground)?")),
    ("destructive", re.compile(r"--destructive")),
    ("border", re.compile(r"--(border|input|ring)")),
    ("sidebar", re.compile(r"--sidebar(-foreground|-accent|-accent-foreground|-primary|-primary-foreground|-border|-ring)?")),
    ("chart", re.compile(r"--chart-[1-5]")),
    ("upgrade", re.compile(r"--upgrade(-foreground|-muted-foreground)?")),
    ("canvas", re.compile(r"--canvas")),
    ("mode", re.compile(r"--mode-glow-strength")),
    ("scrollMask", re.compile(r"--scroll-mask-[tblr]-from")),
    ("color", re.compile(r"--color-(page|primary-dark)")),
    ("root", re.compile(r"--(foreground|background)")),
]
FIXED_LEAF = {"--input": "input", "--ring": "ring",
              "--sidebar": "background",
              "--mode-glow-strength": "glowStrength",
              "--scroll-mask-t-from": "top", "--scroll-mask-b-from": "bottom",
              "--scroll-mask-l-from": "left", "--scroll-mask-r-from": "right",
              "--foreground": "foreground", "--background": "background"}
for group, pat in GROUPS:
    for n in sorted(k for k in set(R) | set(RD) if pat.fullmatch(k)):
        if n in emitted:
            continue
        if n in FIXED_LEAF:
            leaf_name = FIXED_LEAF[n]
        elif n == f"--{group}":
            leaf_name = "default"
        elif n.startswith(f"--{group}-"):
            leaf_name = cam("-" + n[len(group) + 3:])
        else:
            leaf_name = cam(n)
        themes = both_themes(n)
        kind = (R.get(n) or RD.get(n)).get("kind", "color")
        ty = "other" if group == "elevation" else KIND_TY.get(kind, "other")
        desc = "declared under .dark only" if "light" not in themes else None
        if group == "elevation":
            desc = "box-shadow stack re-pointed per theme, kept as the computed string"
        VAR(n, ty, f"{group}.{leaf_name}", root="theme", themes=themes, desc=desc)

# ------------------------------------------------------------------ misc
# Every remaining name declared in the product's own theme/skin rules —
# the --color-* aliases of the semantic set and stragglers — keeps its
# evidence under misc. The .dark re-pointing rules bin as "skins", so both
# bins are scanned. Tailwind's generic --color-{hue}-{step} palette and the
# --tw-* internals stay out: they are framework palette, not product roles.
declared = set()
for bin_name in ("theme", "skins", "app"):
    for rule in V.get(bin_name, []):
        declared.update(rule.get("properties", {}))
for n in sorted(declared):
    if n in emitted or (n not in R and n not in RD):
        continue
    if re.fullmatch(r"--color-[a-zA-Z]+-\d+", n) or n in ("--color-black", "--color-white") or n.startswith("--tw-"):
        continue  # Tailwind's generic scales — evidence in css-vars.json
    kind = (R.get(n) or RD.get(n)).get("kind", "other")
    themes = both_themes(n)
    VAR(n, KIND_TY.get(kind, "other"), f"misc.{cam(n)}", root="theme", themes=themes,
        desc="declared under .dark only" if "light" not in themes else None)

# ------------------------------------------------- measured component tokens
C_PATH = RAW / "components-computed.json"
# Required: without it every measured token would drop silently.
if True:
    C = json.loads(C_PATH.read_text())["components"]

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

    geom("nav-header", "default", "h", "header.height", "the site header bar")
    geom("cta-primary", "default", "h", "button.cta.height", "'Get started for free' CTA")
    geom("cta-secondary", "default", "h", "button.secondary.height", "header 'Get started' button")
    geom("nav-menu-surface", "opened", "w", "navMenu.width", "the open Solutions nav popover")
    geom("consent-banner", "default", "w", "consentBanner.width", "the cookie consent banner")
    # planCard.width / planCard.radius stay out until a recapture reads the
    # full card. The saved reading is the "Free forever" label (274.66x16).
    geom("app-login-card", "default", "w", "loginCard.width", "the sign-in panel")
    geom("app-google-button", "default", "h", "button.oauth.height", "'Continue with Google'")
    geom("support-search", "default", "h", "input.supportSearch.height", "the /support search field")
    geom("app-email-input", "default", "h", "input.loginEmail.height", "the login email field")
    geom("feature-tab", "default", "h", "tab.height", "a vertical feature tab row")
    geom("m-header", "default", "h", "mobileHeader.height", "phone top bar")
    # mobileDrawer.width stays out until a recapture reads the sheet. The
    # saved reading is the Features link (62px), not the drawer.

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

    radius_tok("cta-primary", "default", "button.cta.radius", "CTA corner")
    radius_tok("cta-secondary", "default", "button.secondary.radius", "secondary button corner")
    radius_tok("cta-outline", "default", "button.outline.radius", "outline button corner")
    radius_tok("consent-banner", "default", "consentBanner.radius", "consent banner corner")
    radius_tok("support-search", "default", "input.radius", "text field corner")
    radius_tok("app-login-card", "default", "loginCard.radius", "sign-in panel corner")
    # planCard.radius: see the note above geom(); the label's 0px is not the card.
    radius_tok("testimonial-card-dark", "default", "card.testimonial.radius", "dark testimonial card corner")
    # The 'Get started for free' CTA and the login's 'Continue with Google'
    # both paint the primary role, declared per theme.
    theme_alias("cta-primary", "default", "backgroundColor", "component.button.cta.bg", "primary.default", "CTA fill")
    theme_alias("app-google-button", "default", "backgroundColor", "component.button.oauth.bg", "primary.default", "'Continue with Google' fill")
    # The .dark footer paints the dark --background role regardless of the
    # light site around it — a literal measurement, not a theme alias.
    style_tok("footer", "default", "backgroundColor", "component.footer.bg", "color", "dark footer fill (the .dark --background role)")
    style_tok("nav-link", "hover", "color", "type.linkHover.color", "color", "nav link on hover")

    # Measured type styles as DTCG typography composites — DESIGN.md reads
    # tokens under core.typography. letterSpacing stays in px as measured
    # (Chromium computes the em tracking to px at this size).
    def typ(comp, path, name):
        st = C.get(comp, {}).get("states", {}).get("default", {})
        s = st.get("style") or {}
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

    typ("prose-h1", "typography.articleTitle", "the blog article title")
    typ("prose-p", "typography.body", "article body text")
    # bodyLink stays out until a recapture reads a link inside the article.
    # The saved reading is the breadcrumb "Home".
    typ("nav-link", "typography.navLink", "a header nav label")
    typ("cta-primary", "typography.button", "the primary CTA label")
    typ("support-search", "typography.input", "the /support search field")
    typ("app-google-button", "typography.oauthButton", "the 'Continue with Google' label")
    # faqQuestion stays out until a recapture reads a question row. The saved
    # reading is the header "Solutions" trigger.
    typ("feature-tab", "typography.tabLabel", "a feature tab label")

(RAW / "component-tokens.json").write_text(json.dumps(TREE, indent=1, ensure_ascii=False) + "\n")
print({k: sum(1 for _ in json.dumps(v).split('"type"')) - 1 for k, v in TREE.items()})
