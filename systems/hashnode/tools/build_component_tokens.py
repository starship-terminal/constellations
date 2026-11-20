#!/usr/bin/env python3
"""Build raw/component-tokens.json, the token tree build_tokens.py resolves.

hashnode.com — and townhall.hashnode.com, the hosted blog engine on the
same design system — declares its token layer in a Tailwind v4 @theme plus
a hand-written semantic layer:

  Semantic roles (re-pointed per theme):
    --background/--foreground, --primary(-foreground),
    --secondary(-foreground), --accent(-foreground),
    --muted(-foreground), --card(-foreground), --popover(-foreground),
    --destructive(-foreground|-border|-cream|-wash),
    --success(-foreground|-wash), --warning(-border|-cream|-wash),
    --disabled-foreground, --highlight(-foreground),
    --toolbar(-foreground), --border, --input, --ring,
    --brand(-foreground|-linkedin), --link(-underline),
    --sidebar(-foreground|-accent|-accent-foreground|-primary|
              -primary-foreground|-border|-ring),
    --chart-1..5, --code-block(-foreground|-muted), --reading-text,
    --surface, --scrim, --selection(-foreground), --scroll-shadow,
    --scrollbar-thumb, --command (dark only)
  Scene palettes (also re-pointed per theme):
    --ai-accent/-border/-from/-to          the AI surface gradient
    --buildful(-soft|-strong)              the hackathons/green accent
    --pro(-* 10 names)                     the Pro gold ramp
    --landing-* (12)                       marketing page scene colours
    --tod-* (36)                           the time-of-day hero scene
                                           (morning/noon/evening/night skies,
                                           hills, suns, clouds)
  Scales (theme-independent):
    --radius .5rem, --radius-xs .125rem, --spacing .25rem,
    --container-sm..6xl, --breakpoint-2xl, --blur-sm..2xl,
    --drop-shadow-sm, --aspect-video,
    --animate-bounce/-ping/-pulse/-spin,
    --ease-in-out/-out, --default-transition-*
  Elevation (re-pointed per theme): --elevation-xs/-sm/-md/-lg/-button
    box-shadow stacks — kept as "other" strings.
  Type:
    --font-app (system stack, the app face), --font-inter ("Inter", "Inter
    Fallback" — next/font), --font-mono, --font-sans, --font-weight-300..700;
    the --text-xs..6xl ramp (+ --*-line-height calc ratios) and the prose
    roles --text-body/-label/-reading/-small/-subtitle/-title-2/-title-3/
    -title-4 (each with --font-weight/--letter-spacing/--line-height);
    --tracking-tight/-wide/-widest.
  Vendor: --fa-* (Font Awesome), Tailwind's --color-* generic palette and
    --tw-prose-* internals stay out of the token tree (the tailwind bin is
    recorded in css-vars.json but not promoted to tokens).

Theme is html.light / html.dark: hashnode.com boots html.light and the
sidebar's own Theme menu (Light / Dark / System) repaints it;
townhall.hashnode.com paints html.dark under prefers-color-scheme. The
`.dark`/`:root.dark` rules re-point the same names, so `light` and `dark`
token sets resolve the same declarations under each class. --command is
declared under .dark only and exists in the dark set alone.

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
    "--font-app": "the app face — the system sans stack (-apple-system first); body text and UI",
    "--font-inter": "Inter — the product face loaded through next/font (with its metrics-matched fallback); marketing/display text",
    "--font-mono": "the mono face — ui-monospace stack; code blocks, install commands, inline code",
    "--font-sans": "Tailwind's default font-sans utility face — the same system stack as --font-app",
    "--default-font-family": "Tailwind's default body font chain — resolves to the --font-app stack",
    "--default-mono-font-family": "Tailwind's default code font chain — resolves to --font-mono",
}
FONT_KEYS = {
    "--font-app": "app", "--font-inter": "inter",
    "--font-mono": "code", "--font-sans": "systemSans",
    "--default-font-family": "sans", "--default-mono-font-family": "mono",
}
for n, desc in FONT_DESCS.items():
    if n in R:
        VAR(n, "fontFamily", f"font.family.{FONT_KEYS[n]}", desc=desc)
for n in sorted(k for k in R if re.fullmatch(r"--font-weight-[a-z]+", k)):
    VAR(n, "fontWeight", f"font.weight.{n[len('--font-weight-'):]}")
TEXT_ORDER = ["xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "6xl"]
for n in sorted((k for k in R if re.fullmatch(r"--text-(xs|sm|base|lg|xl|\dxl)", k)),
                key=lambda s: TEXT_ORDER.index(s[len('--text-'):])):
    VAR(n, "dimension", f"font.size.{n[len('--text-'):]}")
for n in sorted(k for k in R if re.fullmatch(r"--text-(xs|sm|base|lg|xl|\dxl)--line-height", k)):
    VAR(n, "number", f"font.lineHeight.{n[len('--text-'):].replace('--line-height', '')}")
for n in sorted(k for k in R if re.fullmatch(r"--tracking-[a-z]+", k)):
    # em-valued tracking keeps its declared unit: a px bake would stop
    # scaling with the element's font size.
    VAR(n, "other", f"font.tracking.{n[len('--tracking-'):]}")
# The prose roles: --text-body/-label/-reading/-small/-subtitle/-title-N
# each declare size + line-height + weight + tracking as four vars.
for n in sorted(k for k in R if re.fullmatch(r"--text-(body|label|reading|small|subtitle|title-\d)", k)):
    role = cam(n[len('--text-'):])
    VAR(n, "dimension", f"font.role.{role}.size")
    for suffix, ty, key in (("--font-weight", "fontWeight", "weight"),
                            ("--line-height", "dimension", "lineHeight"),
                            ("--letter-spacing", "other", "letterSpacing")):
        if n + suffix in R:
            VAR(n + suffix, ty, f"font.role.{role}.{key}")

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
    ("destructive", re.compile(r"--destructive(-foreground|-border|-cream|-wash)?")),
    ("success", re.compile(r"--success(-foreground|-wash)?")),
    ("warning", re.compile(r"--warning(-border|-cream|-wash)?")),
    ("disabled", re.compile(r"--disabled-foreground")),
    ("highlight", re.compile(r"--highlight(-foreground)?")),
    ("toolbar", re.compile(r"--toolbar(-foreground)?")),
    ("border", re.compile(r"--(border|input|ring)")),
    ("sidebar", re.compile(r"--sidebar(-foreground|-accent|-accent-foreground|-primary|-primary-foreground|-border|-ring)?")),
    ("chart", re.compile(r"--chart-[1-5]")),
    ("brand", re.compile(r"--brand(-foreground|-linkedin)?")),
    ("link", re.compile(r"--link(-underline)?")),
    ("codeBlock", re.compile(r"--code-block(-foreground|-muted)?")),
    ("reading", re.compile(r"--reading-text")),
    ("surface", re.compile(r"--surface")),
    ("scrim", re.compile(r"--scrim")),
    ("selection", re.compile(r"--selection(-foreground)?")),
    ("scroll", re.compile(r"--scroll-shadow")),
    ("scrollbar", re.compile(r"--scrollbar-thumb")),
    ("command", re.compile(r"--command")),
    ("root", re.compile(r"--(foreground|background)")),
    ("elevation", re.compile(r"--elevation-(xs|sm|md|lg|button)")),
    # Scene palettes — re-pointed per theme like the roles.
    ("ai", re.compile(r"--ai-(accent|border|from|to)")),
    ("buildful", re.compile(r"--buildful(-soft|-strong)?")),
    ("pro", re.compile(r"--pro(-button|-button-foreground|-button-hover|-cream|-cream-border|-foreground|-glow|-strong|-wash)?")),
    ("landing", re.compile(r"--landing-[a-z-]+")),
    ("tod", re.compile(r"--tod-[a-z0-9-]+")),
]
FIXED_LEAF = {"--input": "input", "--ring": "ring", "--command": "default",
              "--sidebar": "background", "--buildful": "default",
              "--pro": "default", "--reading-text": "text",
              "--scroll-shadow": "shadow", "--scrollbar-thumb": "thumb",
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
    if re.fullmatch(r"--color-[a-zA-Z]+-\d+", n) or n.startswith("--tw-"):
        continue  # Tailwind's generic scales — evidence in css-vars.json
    kind = (R.get(n) or RD.get(n)).get("kind", "other")
    themes = both_themes(n)
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

    geom("app-sidebar", "default", "w", "sidebar.width", "app sidebar column")
    geom("app-cta", "default", "h", "button.cta.height", "'Start your blog' CTA link")
    geom("app-nav-link", "default", "h", "navLink.height", "sidebar nav row")
    geom("app-search-dialog", "default", "w", "searchDialog.width", "the Ctrl-K search dialog")
    geom("app-search-dialog", "default", "h", "searchDialog.height", "the Ctrl-K search dialog")
    geom("post-card", "default", "h", "postCard.height", "a feed post card row")
    geom("comment-box", "default", "h", "commentBox.height", "the comment textarea")
    geom("th-header", "default", "h", "blogHeader.height", "blog header bar")
    geom("th-nav", "default", "h", "blogNav.height", "blog pill nav")
    geom("th-search-dialog", "default", "w", "blogSearchDialog.width", "blog search dialog")
    geom("th-post-card", "default", "h", "blogPostCard.height", "blog index post card")
    geom("onboard-input", "default", "h", "input.height", "onboarding text field")
    geom("m-app-header", "default", "h", "mobileHeader.height", "mobile top bar")
    geom("m-app-drawer", "opened", "w", "mobileDrawer.width", "opened nav sheet")

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

    radius_tok("app-cta", "default", "button.cta.radius", "CTA corner")
    radius_tok("app-nav-link", "default", "navLink.radius", "sidebar row corner")
    radius_tok("app-search-dialog", "default", "searchDialog.radius", "search dialog corner")
    radius_tok("onboard-input", "default", "input.radius", "text field corner")
    radius_tok("th-nav", "default", "blogNav.radius", "blog pill nav corner")
    radius_tok("th-code-block", "default", "codeblock.radius", "code block corner")
    # The 'Start your blog' CTA paints the primary role; the blog pill nav
    # paints --surface. Both are declared roles that re-point per theme.
    theme_alias("app-cta", "default", "backgroundColor", "component.button.cta.bg", "primary.default", "CTA fill")
    theme_alias("th-nav", "default", "backgroundColor", "component.blogNav.bg", "surface.default", "blog nav fill")
    style_tok("post-title-link", "hover", "color", "type.linkHover.color", "color", "post title on hover")
    style_tok("th-prose-h1", "default", "fontSize", "type.articleTitle.size", "other", "blog article h1")

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

    typ("th-prose-h1", "typography.articleTitle", "the blog article title — text-article-title")
    typ("th-prose-h2", "typography.h2", "an in-article section heading")
    typ("th-prose-p", "typography.body", "article body text — text-reading")
    typ("th-prose-link", "typography.bodyLink", "a body-text link inside the article")
    typ("th-code-block", "typography.codeBlock", "code inside the tinted block")
    typ("post-title-link", "typography.cardTitle", "a feed card's post title")
    typ("app-nav-link", "typography.navLink", "a sidebar nav label")
    typ("app-cta", "typography.button", "the primary CTA label")
    typ("app-search-input", "typography.input", "the Ctrl-K search field")
    typ("onboard-input", "typography.field", "an onboarding text field")
    typ("faq-question", "typography.faqQuestion", "a /pro FAQ question")

(RAW / "component-tokens.json").write_text(json.dumps(TREE, indent=1, ensure_ascii=False) + "\n")
print({k: sum(1 for _ in json.dumps(v).split('"type"')) - 1 for k, v in TREE.items()})
