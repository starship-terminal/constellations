#!/usr/bin/env python3
"""Build raw/component-tokens.json, the token tree build_tokens.py resolves.

The Grok product family's public docs portal — docs.x.ai — declares its
design-token layer in a Tailwind v4 @theme plus a hand-written semantic
layer:

  --neutral2..98               the near-achromatic ramp the whole palette is
                               mixed from (HSL channel triplets)
  --solar / --darksolar        the brand accents (orange #ff640a / #cd7532)
  --white / --black            literals
  --neutral2..98 + roles       the semantic set: --bg-base/-inset(-hover)/
                               -l1..l4(-hover)/-card/-codeblock/-overlay-hover,
                               --fg/-muted/-loading/-tertiary/-quaternary/
                               -danger/-info/-warning/-success,
                               --primary(-hover|-foreground),
                               --secondary(-foreground), --accent(-foreground),
                               --muted(-foreground), --card(-foreground),
                               --popover(-foreground),
                               --destructive(-dark|-subtle|-foreground),
                               --success(-foreground), --warning(-foreground),
                               --alert/--on-alert,
                               --border(-bold|-muted|-subtle), --input, --ring,
                               --foreground/--background, --background-level-*,
                               --background-screen/-striped/-vignette,
                               --content-regular/-muted/-subtle,
                               --sb-thumb-color/-track-color, --scrollbar-color
  --sidebar-*                  the sidebar's own role set (background,
                               foreground, primary, accent, border, ring)
  --chart-1..5                 chart colours, repointed per theme
  --color-*                    Tailwind's palette (--color-neutral-50..950,
                               --color-blue-*, ...) plus var() aliases of the
                               semantic set (--color-fg, --color-card, ...)
  --sh-*                       shiki syntax colours (same in both themes)
  --font-x-vf / --font-x-mono  the proprietary faces (xVf variable 200-800,
                               xMono variable 200-800) scoped to next/font
                               classes; --default-font-family/-mono-font-family
                               and --font-display/--font-mono chain to them
  --font-sans/-serif           the Tailwind default utility faces
  --font-weight-*              light 300 .. bold 700
  --text-xs..5xl (+--line-height)  the type ramp; --leading-*, --tracking-*
  --radius-sm..4xl, --radius, --spacing(-g1), --container-*,
  --breakpoint-*, --topbar-height, --card-px, --table-border-width
  --ease-in/-out/-in-out, --default-transition-*,
  --animate-pulse/-spin, --blur-*, --drop-shadow-2xl, --aspect-video
  --cursor-*, --noise, --cmdk-list-height, --skeleton-width, --gb-*,
  --grok-bot-*, --mobile-phone-*, --ladder-surface, --sdm-c, --spread,
  --gap, --theme, --sidebar-width, --max-w-*, --z-*

Theme is html.light / html.dark (next-themes, localStorage.theme, a real
header switch): `.dark` and `:root.dark` re-point the semantic names, so the
`light` and `dark` token sets resolve the same declarations under each
class. A handful of names — --border, --input, --ring, --alert, --on-alert,
--background-*, --content-*, --sb-* — are declared under `.dark` only and
exist in the dark set alone (recorded, not inferred for light).

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


# ---------------------------------------------------------------- palette (core)
# The neutral ramp, the brand pair, the literals, the shiki syntax set and
# the Tailwind palette — all theme-independent.
for n in sorted(k for k in R if re.fullmatch(r"--neutral\d+", k)):
    VAR(n, "color", f"color.neutral.{n[len('--neutral'):]}")
for n in sorted(k for k in R if re.fullmatch(r"--sh-[a-z]+", k)):
    VAR(n, "color", f"color.shiki.{cam(n[len('--sh-'):])}",
        desc="shiki syntax colour; the code panel is dark-tinted in both themes")
if "--solar" in R:
    VAR("--solar", "color", "color.brand.solar",
        desc="the orange accent (inline code tint, link underlines, the docs' accent details)")
if "--darksolar" in R:
    VAR("--darksolar", "color", "color.brand.darksolar",
        desc="the deeper solar tone used for small accent text")
for n in ("--white", "--black"):
    if n in R:
        VAR(n, "color", f"color.{n[2:]}")
# The Tailwind palette the markup reads (generic scales), kept as declared
# evidence under color.scale — the product's own ramp is color.neutral.
for n in sorted(k for k in R if re.fullmatch(r"--color-(white|black)", k)):
    VAR(n, "color", f"color.scale.{n[len('--color-'):]}")
for n in sorted(k for k in R if re.fullmatch(r"--color-[a-zA-Z]+-\d+", k)):
    m = re.fullmatch(r"--color-([a-zA-Z]+)-(\d+)", n)
    VAR(n, "color", f"color.scale.{m.group(1)}.{m.group(2)}")
for n in sorted(k for k in R if re.fullmatch(r"--color-[a-z]+-(50|100|200|300|400|500|600|700|800|900|950)\b.*", k) and not re.fullmatch(r"--color-[a-zA-Z]+-\d+", k)):
    VAR(n, "color", f"color.scale.{cam(n[len('--color-'):])}")

# ---------------------------------------------------------------- type (core)
FONT_DESCS = {
    "--font-x-vf": "xVf — the product face, a variable font weight 200-800; declared on the next/font class (.UunFKG_variable), applied through --default-font-family and --font-display",
    "--font-x-mono": "xMono — the product mono, a variable font weight 200-800; declared on the next/font class (._4lXy9W_variable)",
    "--default-font-family": "the body font chain: xVf, its metrics-matched Arial fallback, then the system sans",
    "--default-mono-font-family": "the code font chain: xMono then ui-monospace",
    "--font-display": "the display face (headings): xVf then the system sans",
    "--font-mono": "the mono face (code): xMono then ui-monospace",
    "--font-sans": "Tailwind's default font-sans utility face (not the body font)",
    "--font-serif": "Tailwind's default serif utility face",
}
FONT_KEYS = {
    "--font-x-vf": "xVf", "--font-x-mono": "xMono",
    "--default-font-family": "sans", "--default-mono-font-family": "mono",
    "--font-display": "display", "--font-mono": "code",
    "--font-sans": "systemSans", "--font-serif": "serif",
}
for n, desc in FONT_DESCS.items():
    if n in R:
        VAR(n, "fontFamily", f"font.family.{FONT_KEYS[n]}", desc=desc)
for n in sorted(k for k in R if re.fullmatch(r"--font-weight-[a-z]+", k)):
    VAR(n, "fontWeight", f"font.weight.{n[len('--font-weight-'):]}")
TEXT_ORDER = ["xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl"]
for n in sorted((k for k in R if re.fullmatch(r"--text-(xs|sm|base|lg|xl|\dxl)", k)), key=lambda s: TEXT_ORDER.index(s[len('--text-'):])):
    VAR(n, "dimension", f"font.size.{n[len('--text-'):]}")
for n in sorted(k for k in R if re.fullmatch(r"--text-(xs|sm|base|lg|xl|\dxl)--line-height", k)):
    VAR(n, "number", f"font.lineHeight.{n[len('--text-'):].replace('--line-height', '')}")
for n in sorted(k for k in R if re.fullmatch(r"--leading-[a-z]+", k)):
    VAR(n, "number", f"font.leading.{n[len('--leading-'):]}")
for n in sorted(k for k in R if re.fullmatch(r"--tracking-[a-z]+", k)):
    # em-valued tracking keeps its declared unit: a px bake would stop
    # scaling with the element's font size.
    VAR(n, "other", f"font.tracking.{n[len('--tracking-'):]}")

# ------------------------------------------------------------- core scales
for n in sorted(k for k in R if re.fullmatch(r"--radius-(sm|md|lg|xl|2xl|3xl|4xl)", k)):
    VAR(n, "dimension", f"radius.{n[len('--radius-'):]}")
if "--radius" in R:
    VAR("--radius", "dimension", "radius.base")
if "--spacing" in R:
    VAR("--spacing", "dimension", "space.unit", desc="the 4px unit the spacing scale multiplies")
if "--spacing-g1" in R:
    VAR("--spacing-g1", "dimension" if R["--spacing-g1"]["kind"] == "dimension" else "other", "space.g1")
# A var resolved "other" that is a plain px/rem length is still a dimension
# token (rem is a valid DTCG length); only non-length others stay "other".
DIM_RE = re.compile(r"-?\d+(\.\d+)?(px|rem)$")
def dim_or_other(name):
    r = R.get(name) or RD.get(name)
    if r["kind"] == "dimension" or DIM_RE.fullmatch(str(r.get("value", r.get("raw", ""))).strip()):
        return "dimension"
    return "other"
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
for n in sorted(k for k in R if re.fullmatch(r"--blur-[a-z]+", k)):
    VAR(n, "dimension", f"blur.{n[len('--blur-'):]}")
for n in sorted(k for k in R if re.fullmatch(r"--drop-shadow-[a-z0-9]+", k)):
    VAR(n, "other", f"shadow.{cam(n[len('--drop-shadow-'):])}",
        desc="drop-shadow filter value, kept as the computed string")
for n in sorted(k for k in R if re.fullmatch(r"--animate-[a-z-]+", k)):
    VAR(n, "other", f"animation.{cam(n[len('--animate-'):])}",
        desc="animation shorthand as declared")
for n in ("--aspect-video", "--topbar-height", "--card-px", "--table-border-width", "--cmdk-list-height", "--skeleton-width"):
    if n in R:
        VAR(n, dim_or_other(n), f"layout.{cam(n)}")

# ------------------------------------------------------- semantic roles
# Re-pointed per theme: emitted into both `light` and `dark` sets, or into
# `dark` alone where the name is declared under .dark only.
GROUPS = [
    ("bg", re.compile(r"--bg-(base|inset|inset-hover|l[1-4]|l4-hover|card|codeblock|overlay-hover|hover)")),
    ("background", re.compile(r"--background(-level-1|-level-2|-screen|-striped|-vignette)?")),
    ("fg", re.compile(r"--fg(-muted|-loading|-tertiary|-quaternary|-danger|-info|-warning|-success)?")),
    ("primary", re.compile(r"--primary(-hover|-foreground)?")),
    ("secondary", re.compile(r"--secondary(-foreground)?")),
    ("accent", re.compile(r"--accent(-foreground)?")),
    ("muted", re.compile(r"--muted(-foreground)?")),
    ("card", re.compile(r"--card(-foreground)?")),
    ("popover", re.compile(r"--popover(-foreground)?")),
    ("destructive", re.compile(r"--destructive(-dark|-subtle|-foreground)?")),
    ("success", re.compile(r"--success(-foreground)?")),
    ("warning", re.compile(r"--warning(-foreground)?")),
    ("alert", re.compile(r"--(alert|on-alert)")),
    ("border", re.compile(r"--(border|border-bold|border-muted|border-subtle|input|ring)")),
    ("sidebar", re.compile(r"--sidebar-(background|foreground|primary|primary-foreground|accent|accent-foreground|border|ring|width)")),
    ("chart", re.compile(r"--chart-[1-5]")),
    ("content", re.compile(r"--content-(regular|muted|subtle)")),
    ("sb", re.compile(r"--sb-(thumb-color|track-color)")),
    ("scrollbar", re.compile(r"--scrollbar-color")),
    ("color", re.compile(r"--color-(background|border|card|card-hover|fg|l4|primary)")),
    ("root", re.compile(r"--(foreground|background)")),
]
for group, pat in GROUPS:
    for n in sorted(k for k in set(R) | set(RD) if pat.fullmatch(k)):
        if n in emitted:
            continue
        leaf_name = cam("-" + n[len(group) + 3:]) if n.startswith(f"--{group}-") else ("default" if n == f"--{group}" else cam(n))
        if group == "alert":
            leaf_name = "on" if n == "--on-alert" else "default"
        if group == "border" and n == "--input":
            leaf_name = "input"
        if group == "border" and n == "--ring":
            leaf_name = "ring"
        if group == "color":
            leaf_name = cam(n[len('--color-'):])
        if group == "root":
            leaf_name = cam(n)
        themes = tuple(t for t in ("light", "dark") if n in (R if t == "light" else RD))
        kind = (R.get(n) or RD.get(n)).get("kind", "color")
        VAR(n, KIND_TY.get(kind, "other"), f"{group}.{leaf_name}", root="theme", themes=themes,
            desc="declared under .dark only" if "light" not in themes else None)

# ------------------------------------------------------------------ misc
# Every remaining name declared in the product's own theme/skin rules —
# the component vars (--gb-*/--grok-bot-*/--mobile-phone-*), the cmdk and
# skeleton sizes, --noise, --cursor-*, --spread, --gap, --theme,
# --ladder-* — keeps its evidence under misc. The .dark re-pointing rules
# bin as "skins", so both bins are scanned.
declared = set()
for bin_name in ("theme", "skins", "app"):
    for rule in V.get(bin_name, []):
        declared.update(rule.get("properties", {}))
for n in sorted(declared):
    if n in emitted or (n not in R and n not in RD):
        continue
    kind = (R.get(n) or RD.get(n)).get("kind", "other")
    themes = tuple(t for t in ("light", "dark") if n in (R if t == "light" else RD))
    # Theme sets, not core: a misc name declared under .dark only has no
    # light resolution for the core pass, and several re-point per theme.
    VAR(n, KIND_TY.get(kind, "other"), f"misc.{cam(n)}", root="theme", themes=themes,
        desc="declared under .dark only" if "light" not in themes else None)

# ------------------------------------------------- measured component tokens
C_PATH = RAW / "components-computed.json"
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

    geom("docs-header", "default", "h", "header.height", "fixed docs header height")
    geom("docs-header", "default", "w", "header.width", "fixed docs header width")
    geom("docs-sidebar", "default", "w", "sidebar.width", "docs sidebar column")
    geom("docs-search-pill", "default", "h", "searchPill.height", "header search pill")
    geom("docs-search-pill", "default", "w", "searchPill.width", "header search pill")
    geom("docs-search-dialog", "default", "w", "searchDialog.width", "the cmdk dialog")
    geom("docs-search-dialog", "default", "h", "searchDialog.height", "the cmdk dialog")
    geom("docs-cta", "default", "h", "button.cta.height", "hero CTA link")
    geom("docs-next-card", "default", "h", "navCard.height", "the bg-card nav card")
    geom("docs-code-tab", "default", "h", "tab.height", "SDK tab")
    geom("docs-theme-button", "default", "h", "themeButton.size", "round theme button")
    geom("pricing-td", "default", "h", "table.rowHeight", "pricing table row")
    geom("docs-page-footer", "default", "h", "pageFooter.height", "sticky pager bar")
    geom("m-docs-topbar", "default", "h", "mobileHeader.height", "mobile top bar")
    geom("m-docs-drawer", "opened", "w", "mobileDrawer.width", "opened nav sheet")

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

    radius_tok("docs-code-block", "default", "codeblock.radius", "code panel corner")
    radius_tok("docs-next-card", "default", "navCard.radius", "nav card corner")
    radius_tok("docs-search-pill", "default", "searchPill.radius", "search pill corner")
    radius_tok("docs-cta", "default", "button.cta.radius", "hero CTA corner")
    # The measured code node is transparent (the fill sits on its panel
    # wrapper); the nav card's light fill matches --bg-card exactly. Both are
    # declared roles that re-point per theme, so the tokens alias the roles.
    theme_alias("docs-code-block", "default", "backgroundColor", "component.codeblock.bg", "bg.codeblock", "code panel fill")
    theme_alias("docs-next-card", "default", "backgroundColor", "component.navCard.bg", "bg.card", "nav card fill")
    style_tok("prose-h1", "default", "fontSize", "type.h1.size", "other", "article h1")
    style_tok("prose-h1", "default", "lineHeight", "type.h1.lineHeight", "other", "article h1")
    style_tok("prose-p", "default", "fontSize", "type.body.size", "other", "article paragraph")
    style_tok("prose-p", "default", "lineHeight", "type.body.lineHeight", "other", "article paragraph")
    style_tok("prose-inline-code", "default", "color", "type.inlineCode.color", "color", "inline code tint")

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

    typ("prose-h1", "typography.display", "the article h1 — xVf at 48px in the variable face's intermediate 450 weight")
    typ("prose-h2", "typography.h2", "a section heading — xVf 30px medium")
    typ("faq-question", "typography.h3", "the FAQ question heading — xVf 24px medium")
    typ("prose-p", "typography.body", "article body text — xVf 14px/24")
    typ("prose-inline-code", "typography.inlineCode", "an inline code span — xMono 13.3px tinted --solar")
    typ("docs-code-block", "typography.codeBlock", "code inside the shiki panel — xMono 13px/20")
    typ("docs-sidebar-link", "typography.navLink", "a sidebar page link — xVf 13px medium")
    typ("docs-cta", "typography.button", "the primary CTA label — xVf 14px medium")
    typ("docs-code-tab", "typography.tab", "an SDK tab label — xVf 12px")
    typ("docs-markdown-link", "typography.caption", "the small 'View as Markdown' link — xVf 12px semibold")

(RAW / "component-tokens.json").write_text(json.dumps(TREE, indent=1, ensure_ascii=False) + "\n")
print({k: sum(1 for _ in json.dumps(v).split('"type"')) - 1 for k, v in TREE.items()})
