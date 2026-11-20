#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

cartesia.ai is three surfaces signed out:

- the marketing site (Astro + Tailwind v4) declares a real token layer — the
  --cartesia-*/--color-cartesia-* palette plus a shadcn-style semantic layer
  (--background/--foreground/--primary/--card/…), --control-* sizing,
  --motion-* ramps and --site-* layout vars — harvested into
  raw/css-vars.json by tools/capture/vars.mjs. Those become {"var": ...}
  leaves, resolved per theme by build_tokens.py. The site paints light and
  declares a `.dark` scope that re-binds the same roles.
- the Playground auth boundary (play.cartesia.ai) is a Clerk app that shares
  the same semantic layer; its cards were measured, never submitted.
- docs.cartesia.ai is a separate Mintlify app in Inter — measured for
  reference (raw/css-vars-docs.json), kept out of the export.

Measured values come from raw/components-computed.json
(tools/capture/public/measure.mjs). A leaf is {"var": "--name"} or
{"value": ..., "source": "..."} for a measured/derived value.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())["components"]
RL = {n for n in V.get("resolved", {}).get("light", {})}
RD = {n for n in V.get("resolved", {}).get("dark", {})}

missing = []


def var(name, ty="color", **kw):
    """A declared-variable leaf; errors when the probe never resolved it."""
    if name not in RL and name not in RD:
        missing.append(name)
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def st(comp, state="default"):
    return C[comp]["states"][state]["style"]


def px(v):
    """Normalize a computed px length: 254.797px -> 254.8px."""
    m = re.fullmatch(r"(-?[\d.eE+]+)px", str(v))
    if not m:
        return str(v)
    f = float(m.group(1))
    s = f"{f:.2f}".rstrip("0").rstrip(".")
    return s + "px"


def rounded(v, cap=9999):
    """rounded-full resolves to a giant computed radius; clamp it to 9999px."""
    f = float(re.fullmatch(r"([\d.eE+]+)px", str(v)).group(1))
    return "9999px" if f > cap else px(v)


def dim(comp, prop, state="default"):
    return px(st(comp, state)[prop])


def labkey(v):
    """Normalize lab()/oklab() serializations ('lab(66.1% -0.0 0)' == 'lab(66.1 -0.0 0)')."""
    m = re.match(r"(?:ok)?lab\(([^)]+)\)", v.strip())
    if not m:
        return None
    parts = re.findall(r"-?[\d.eE+]+%?", m.group(1))
    return " ".join("%g" % float(p.rstrip("%")) for p in parts)


LABS = {}
for theme in ("light", "dark"):
    for n, e in V.get("resolved", {}).get(theme, {}).items():
        k = labkey(str(e.get("raw", "")))
        if k and e.get("value"):
            LABS.setdefault(k, e["value"])


def col(v):
    v = (v or "").strip()
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    if v.startswith(("lab(", "oklab(")):
        k = labkey(v)
        if k in LABS:  # the computed lab equals a declared var's resolved value
            return LABS[k]
    return v


def meas(comp, prop, state="default", colour=False, cap=None, src=None, **kw):
    """A leaf whose value is read live from components-computed.json."""
    v = st(comp, state)[prop]
    if colour:
        v = col(v)
    elif str(v).endswith("%"):
        v = float(v[:-1]) / 100
    elif str(v).endswith("px"):
        v = rounded(v, cap) if cap else px(v)
    d = {"value": v, "source": (src or f"computed {prop} of {comp} {state} (raw/components-computed.json)") + stale(comp)}
    d.update(kw)
    return d


def stale(comp):
    """A component flagged recaptureMissed kept an earlier run's readings; a token built from one says so."""
    m = C[comp].get("recaptureMissed")
    return "; stale: kept from an earlier run (the %s recapture did not find %s)" % (m, comp) if m else ""


def measrect(comp, prop="w", state="default", src=None, **kw):
    """The on-screen size (bounding rect), for elements painted under a
    transform whose computed style keeps the pre-scale length."""
    v = C[comp]["states"][state]["rect"][prop]
    d = {"value": px(f"{v}px"),
         "source": src or f"bounding-rect {prop} of {comp} {state} (raw/components-computed.json): the displayed size after any transform"}
    d.update(kw)
    return d


S = {"_about": (
     "The token tree build_tokens.py turns into tokens.json. cartesia.ai's "
     "marketing site declares a shadcn-style semantic layer "
     "(--background/--foreground/--primary/--card/…) over a "
     "--cartesia-*/--color-cartesia-* palette plus --control-* sizing, "
     "--motion-* ramps and --site-* layout vars in its Astro/Tailwind "
     "stylesheets, paints it light and re-binds the same roles under .dark "
     "(a declared scope the public pages paint only in .dark islands). "
     "Declared variables become var leaves resolved per theme; measured "
     "values come from raw/components-computed.json (the sign-in surface on "
     "play.cartesia.ai shares the same layer). The docs surface "
     "(docs.cartesia.ai) is a Mintlify app in Inter — a separate system "
     "recorded in raw/css-vars-docs.json, not merged here."),
     "core": {}, "light": {}, "dark": {}, "component": {}}

CORE, LIGHT, DARK, COMP = S["core"], S["light"], S["dark"], S["component"]

# ------------------------------------------------------------------- fonts

CORE["font"] = {"family": {
    "sans": var("--font-sans", "fontFamily",
                description="ABC Diatype: body text, nav, buttons and most UI."),
    "display": var("--font-display", "fontFamily",
                   description="PP Kyoto: the display face for headlines (h1/h2) and brand moments."),
    "mono": var("--font-mono", "fontFamily",
                description="IBM Plex Mono: code, figures and technical labels."),
    "handwriting": var("--font-handwriting", "fontFamily",
                       description="Homemade Apple: the annotation/handwriting accent."),
    "docs": {"value": "Inter, -apple-system, \"system-ui\", \"Segoe UI\", system-ui, sans-serif",
             "type": "fontFamily",
             "source": "computed fontFamily of docs-nav-item default (raw/components-computed.json)",
             "description": "Inter: the Mintlify docs app's stack — a separate surface, not the marketing fonts."},
}}

CORE["font"]["size"] = {
    "xs": var("--text-xs", "dimension", description="Declared --text-xs (12px)."),
    "sm": var("--text-sm", "dimension", description="Declared --text-sm (14px)."),
    "base": var("--text-base", "dimension", description="Declared --text-base (16px)."),
    "lg": var("--text-lg", "dimension", description="Declared --text-lg (18px)."),
    "xl": var("--text-xl", "dimension", description="Declared --text-xl (20px)."),
    "2xl": var("--text-2xl", "dimension", description="Declared --text-2xl (24px)."),
    "3xl": var("--text-3xl", "dimension", description="Declared --text-3xl (30px)."),
    "4xl": var("--text-4xl", "dimension", description="Declared --text-4xl (36px)."),
    "5xl": var("--text-5xl", "dimension", description="Declared --text-5xl (48px)."),
    "6xl": var("--text-6xl", "dimension", description="Declared --text-6xl (60px)."),
    "control-xs": var("--control-font-size-xs", "dimension", description="Control label size xs (12px)."),
    "control-sm": var("--control-font-size-sm", "dimension", description="Control label size sm (13px)."),
    "control-default": var("--control-font-size-default", "dimension",
                           description="Control label size default (14px — nav buttons, chips, CTAs)."),
    "control-lg": var("--control-font-size-lg", "dimension", description="Control label size lg (15px — the sign-in submit)."),
    "control-xl": var("--control-font-size-xl", "dimension", description="Control label size xl (16px)."),
    "control-2xl": var("--control-font-size-2xl", "dimension", description="Control label size 2xl (18px)."),
    "hero": meas("hero-title", "fontSize", type="dimension",
                 description="The PP-Kyoto hero headline."),
    "section-h2": meas("h2-display", "fontSize", type="dimension",
                       description="The display section heading."),
    "mobile-hero": meas("m-hero", "fontSize", type="dimension",
                        description="The hero size at 390px."),
    "docs-title": meas("docs-h1", "fontSize", type="dimension",
                       description="The Mintlify docs page title (Inter)."),
}

CORE["font"]["lineHeight"] = {
    "xs": var("--text-xs--line-height", "number", description="Declared leading for --text-xs."),
    "sm": var("--text-sm--line-height", "number", description="Declared leading for --text-sm."),
    "base": var("--text-base--line-height", "number", description="Declared leading for --text-base."),
    "lg": var("--text-lg--line-height", "number", description="Declared leading for --text-lg."),
    "xl": var("--text-xl--line-height", "number", description="Declared leading for --text-xl."),
    "2xl": var("--text-2xl--line-height", "number", description="Declared leading for --text-2xl."),
    "3xl": var("--text-3xl--line-height", "number", description="Declared leading for --text-3xl."),
    "4xl": var("--text-4xl--line-height", "number", description="Declared leading for --text-4xl."),
    "5xl": var("--text-5xl--line-height", "number", description="Declared leading for --text-5xl (1)."),
    "6xl": var("--text-6xl--line-height", "number", description="Declared leading for --text-6xl (1)."),
    "tight": var("--leading-tight", "number", description="Declared --leading-tight (1.25)."),
    "snug": var("--leading-snug", "number", description="Declared --leading-snug (1.375)."),
    "normal": var("--leading-normal", "number", description="Declared --leading-normal (1.5)."),
    "relaxed": var("--leading-relaxed", "number", description="Declared --leading-relaxed (1.625)."),
    "header": var("--leading-header", "number", description="Declared --leading-header (1.3)."),
    "header-1": var("--leading-header-1", "number", description="Declared --leading-header-1 (1.15)."),
    "control-default": var("--control-line-height-default", "dimension", description="Control label leading (20px on 14px)."),
    "control-sm": var("--control-line-height-sm", "dimension", description="Control label leading sm (18px)."),
    "control-2xl": var("--control-line-height-2xl", "dimension", description="Control label leading 2xl (24px)."),
    "hero": meas("hero-title", "lineHeight", type="dimension",
                 description="The hero headline leading."),
}

# Tracking is declared in em — a ratio of the running font size — so the
# leaves hold the declared ratio (type number), not a probe-frozen px length.
CORE["font"]["tracking"] = {
    "tight": {"value": -0.025, "type": "number",
              "source": "css-var --tracking-tight -.025em (declared em ratio; multiply by the font size — -0.4px at 16px)",
              "description": "The -0.025em tight tracking."},
    "normal": var("--tracking-normal", "dimension", description="Zero tracking."),
    "wide": {"value": 0.025, "type": "number",
             "source": "css-var --tracking-wide .025em (declared em ratio; 0.4px at 16px)",
             "description": "The +0.025em wide tracking."},
    "wider": {"value": 0.05, "type": "number",
              "source": "css-var --tracking-wider .05em (declared em ratio; 0.8px at 16px)",
              "description": "The +0.05em wider tracking."},
    "widest": {"value": 0.1, "type": "number",
               "source": "css-var --tracking-widest .1em (declared em ratio; 1.6px at 16px)",
               "description": "The +0.1em widest tracking."},
}

CORE["font"]["weight"] = {
    "normal": var("--font-weight-normal", "fontWeight", description="400 body weight."),
    "medium": var("--font-weight-medium", "fontWeight", description="500 — headings, nav and button labels."),
    "semibold": var("--font-weight-semibold", "fontWeight", description="600."),
    "bold": var("--font-weight-bold", "fontWeight", description="700."),
}

# ------------------------------------------------------------------ colours

CORE["color"] = {"brand": {
    "forest": var("--cartesia-forest", description="Forest #004e23: the deep brand green (dark accents, the wordmark's alt tone)."),
    "verdant": var("--cartesia-verdant", description="Verdant #309d4b: the primary action green (Try Cartesia, Play, selected markers)."),
    "growth": var("--cartesia-growth", description="Growth #abd49e: the light green tint — the .dark primary."),
    "canvas": var("--cartesia-canvas", description="Canvas #e4e3db: the warm grey field and border tone."),
    "field": var("--cartesia-field", description="Field #f4f4f1: the light warm-grey surface."),
    "mist": var("--cartesia-mist", description="Mist #d1e2e8: the cool blue-grey tint."),
    "carbon": var("--cartesia-carbon", description="Carbon #1e1e1e: the near-black ink."),
    "memory": var("--cartesia-memory", description="Memory #99b0c8: the muted blue accent."),
}}

CORE["color"]["green"] = {n: var(f"--color-cartesia-green-{n}") for n in ("50","100","200","300","400","500","600","700","800","900","950")}
CORE["color"]["green"]["500"]["description"] = "Green 500 = verdant #309d4b."
CORE["color"]["green"]["900"]["description"] = "Green 900 = forest #004e23."
CORE["color"]["blue"] = {n: var(f"--color-cartesia-blue-{n}") for n in ("50","100","200","300","400","500","600","700","800","900","950")}
CORE["color"]["blue"]["100"]["description"] = "Blue 100 = mist #d1e2e8."
CORE["color"]["blue"]["500"]["description"] = "Blue 500 = memory #99b0c8."
CORE["color"]["orange"] = {n: var(f"--color-cartesia-orange-{n}") for n in ("50","100","200","300","400","500","600","700","800","900","950")}
CORE["color"]["orange"]["500"]["description"] = "Orange 500 #fc7a37 — the warm accent (chart-1)."
CORE["color"]["neutral"] = {
    "10": var("--cartesia-neutral-10", description="Neutral ramp 10 #f4f4f1."),
    "20": var("--cartesia-neutral-20", description="Neutral ramp 20 #f0efe9."),
    "30": var("--cartesia-neutral-30", description="Neutral ramp 30 #e4e3db."),
    "40": var("--cartesia-neutral-40", description="Neutral ramp 40 #cdc8c1 — the .dark foreground."),
    "50": var("--cartesia-neutral-50", description="Neutral ramp 50 #9fa09f."),
    "60": var("--cartesia-neutral-60", description="Neutral ramp 60 #525150 — muted-foreground."),
    "70": var("--cartesia-neutral-70", description="Neutral ramp 70 #39342f."),
    "80": var("--cartesia-neutral-80", description="Neutral ramp 80 #282523."),
    "90": var("--cartesia-neutral-90", description="Neutral ramp 90 #1e1e1e — carbon."),
    "100": var("--cartesia-neutral-100", description="Neutral ramp 100 #1e1c1a — the light foreground."),
    **{f"scale-{n}": var(f"--color-cartesia-neutral-{n}") for n in ("50","100","200","300","400","500","600","700","800","900","950")},
}
CORE["color"]["neutral"]["scale-50"]["description"] = "Neutral scale 50 #fefefe — the page field."
CORE["color"]["neutral"]["scale-100"]["description"] = "Neutral scale 100 #f9f9f8 — card."
CORE["color"]["neutral"]["scale-200"]["description"] = "Neutral scale 200 #f3f2ef — muted/accent."
CORE["color"]["neutral"]["scale-300"]["description"] = "Neutral scale 300 #f0efe9."
CORE["color"]["neutral"]["scale-400"]["description"] = "Neutral scale 400 #e4e3db — border/canvas."
CORE["color"]["neutral"]["scale-900"]["description"] = "Neutral scale 900 #1e1c1a — foreground."
CORE["color"]["named"] = {
    "white": var("--color-white", description="Pure white: the sign-in field fill."),
    "black": var("--color-black", description="Pure black."),
    "servicenow": var("--color-servicenow", description="Partner green #62d84e (customer logo accents)."),
    "artificial-analysis": var("--color-artificial-analysis", description="Artificial Analysis purple #8842fd (benchmark logo accents)."),
}

# --------------------------------------------------------------- primitives

CORE["radius"] = {
    "xs": var("--radius-xs", "dimension", description="Declared --radius-xs (2px)."),
    "sm": var("--radius-sm", "dimension", description="Declared --radius-sm (4px)."),
    "md": var("--radius-md", "dimension", description="Declared --radius-md (6px — menu links)."),
    "lg": var("--radius-lg", "dimension", description="Declared --radius-lg (8px — buttons, fields, cards' base radius)."),
    "xl": var("--radius-xl", "dimension", description="Declared --radius-xl (12px — the sign-in submit, docs nav items)."),
    "2xl": var("--radius-2xl", "dimension", description="Declared --radius-2xl (16px)."),
    "3xl": var("--radius-3xl", "dimension", description="Declared --radius-3xl (20px)."),
    "4xl": var("--radius-4xl", "dimension", description="Declared --radius-4xl (24px)."),
    "full": meas("usecase-chip", "borderTopLeftRadius", cap=9999, type="dimension",
                 src="computed borderTopLeftRadius of usecase-chip default (raw/components-computed.json): rounded-full resolves to the browser's clamp",
                 description="rounded-full: chips, the voice orb and chooser buttons, the docs search pill. The globe dots paint a 50% circle instead (percentage radii are not length-scale entries)."),
}

CORE["spacing"] = {
    "unit": var("--spacing", "dimension", description="The 4px spacing unit the Tailwind scale multiplies."),
    "hairline": var("--theme-border-width-hairline", "dimension", description="The 1px hairline border width."),
}

CORE["layout"] = {
    "content-max": var("--site-content-max", "dimension", description="The 1280px content column."),
    "gutter": var("--site-gutter", "dimension", description="The 48px page gutter at desktop."),
    "nav-height": var("--site-nav-height", "dimension", description="The 64px sticky header height."),
    "breakpoint-sm": var("--breakpoint-sm", "dimension", description="The 640px small breakpoint."),
    **{f"container-{k}": var(f"--container-{k}", "dimension",
                            description=f"Container {k} ({w}px).")
       for k, w in [("xs", 320), ("sm", 384), ("md", 448), ("lg", 512), ("xl", 576),
                    ("2xl", 672), ("3xl", 768), ("4xl", 896), ("5xl", 1024), ("6xl", 1152)]},
}

CORE["control"] = {
    **{f"height-{k}": var(f"--control-height-{k}", "dimension", description=d)
       for k, d in [("xs", "Control height xs (24px)."), ("sm", "Control height sm (32px)."),
                    ("default", "Control height default (36px — nav buttons, CTAs, play)."),
                    ("lg", "Control height lg (36px)."), ("xl", "Control height xl (44px — sign-in fields and submit)."),
                    ("2xl", "Control height 2xl (48px).")]},
    **{f"icon-{k}": var(f"--control-icon-size-{k}", "dimension", description=f"Control icon {k}.")
       for k in ("xs", "sm", "default", "xl")},
    **{f"padding-{k}": var(f"--control-padding-{k}", "dimension", description=f"Control inline padding {k}.")
       for k in ("xs", "sm", "default", "lg", "2xl")},
    **{f"field-{k}": var(f"--field-padding-{k}", "dimension", description=f"Field padding {k}.")
       for k in ("default", "sm")},
}

CORE["motion"] = {
    "duration-fast": var("--motion-duration-fast", "duration", description="100ms — the fastest feedback."),
    "duration-label": var("--motion-duration-label", "duration", description="120ms — label fades."),
    "duration-normal": var("--motion-duration-normal", "duration", description="150ms — the default transition (--default-transition-duration)."),
    "duration-panel": var("--motion-duration-panel", "duration", description="200ms — panels/menus."),
    "ease-out": var("--motion-ease-out", "cubicBezier", description="The standard ease-out cubic-bezier(.23,1,.32,1)."),
    "ease-layout": var("--motion-ease-layout", "cubicBezier", description="The layout ease cubic-bezier(.2,0,0,1)."),
    "ease-in": var("--ease-in", "cubicBezier", description="Tailwind ease-in."),
    "ease-out-tw": var("--ease-out", "cubicBezier", description="Tailwind ease-out."),
    "default-ease": var("--default-transition-timing-function", "cubicBezier", description="The default transition timing cubic-bezier(.4,0,.2,1)."),
    "disclosure-ease": var("--motion-disclosure-ease", "cubicBezier", description="Disclosure ease (same curve as ease-out)."),
    "disclosure-enter": var("--motion-disclosure-enter-duration", "duration", description="Disclosure enter 200ms."),
    "disclosure-exit": var("--motion-disclosure-exit-duration", "duration", description="Disclosure exit 200ms."),
    "feedback-enter": var("--motion-feedback-enter-duration", "duration", description="Feedback enter 100ms."),
    "feedback-exit": var("--motion-feedback-exit-duration", "duration", description="Feedback exit 100ms."),
    "overlay-enter": var("--motion-overlay-enter-duration", "duration", description="Overlay enter 150ms."),
    "overlay-exit": var("--motion-overlay-exit-duration", "duration", description="Overlay exit 100ms."),
    "panel-enter": var("--motion-panel-enter-duration", "duration", description="Panel enter 200ms."),
    "panel-exit": var("--motion-panel-exit-duration", "duration", description="Panel exit 150ms."),
    "sidebar-ease": var("--motion-sidebar-ease", "cubicBezier", description="Sidebar ease cubic-bezier(.2,0,0,1)."),
    "sidebar-enter": var("--motion-sidebar-enter-duration", "duration", description="Sidebar enter 200ms."),
    "sidebar-exit": var("--motion-sidebar-exit-duration", "duration", description="Sidebar exit 200ms."),
    "site-accordion-duration": var("--site-accordion-duration", "duration", description="The marketing accordion's 350ms."),
    "site-accordion-ease": var("--site-accordion-ease", "cubicBezier", description="The marketing accordion ease (ease keyword)."),
    "site-reveal-duration": var("--site-reveal-duration", "duration", description="The scroll-reveal 700ms."),
    "site-reveal-ease": var("--site-reveal-ease", "cubicBezier", description="The scroll-reveal ease cubic-bezier(.32,.72,0,1)."),
    "site-reveal-step": var("--site-reveal-step", "duration", description="The 60ms stagger between reveal items."),
}

CORE["blur"] = {k: var(f"--blur-{k}", "dimension", description=f"Blur {k}.")
                for k in ("xs", "sm", "md")}

CORE["measured"] = {
    "focus-ring": meas("faq-trigger", "outlineColor", "focus-visible", colour=True, type="color",
                       src="computed outlineColor of faq-trigger focus-visible (raw/components-computed.json): 2px solid var(--ring)",
                       description="The default 2px focus ring (--ring)."),
    "focus-ring-width": meas("faq-trigger", "outlineWidth", "focus-visible", type="dimension",
                             src="computed outlineWidth of faq-trigger focus-visible (raw/components-computed.json)",
                             description="Focus ring width."),
    "focus-ring-verdant": meas("voice-row", "outlineColor", "focus-visible", colour=True, type="color",
                               description="The verdant 2px focus ring on voice-list rows."),
    "hover-dim": {"value": float(re.search(r"/\s*([\d.]+)\)", st("nav-cta", "hover")["backgroundColor"]).group(1)),
                  "type": "number",
                  "source": "computed backgroundColor of nav-cta hover (raw/components-computed.json): the primary fill at reduced opacity",
                  "description": "Primary buttons hover at a fraction of the verdant fill."},
}

# -------------------------------------------------------------------- themes

SEM = [
    ("background", "The page field #fefefe."),
    ("foreground", "Body/headline ink #1e1c1a."),
    ("primary", "Verdant #309d4b — solid CTAs and selections."),
    ("primary-foreground", "Text on primary."),
    ("secondary", "Secondary fill."),
    ("secondary-foreground", "Text on secondary."),
    ("accent", "Accent/hover fill."),
    ("accent-foreground", "Text on accent."),
    ("card", "Card fill."),
    ("card-foreground", "Text on card."),
    ("muted", "Muted fill (hover surfaces)."),
    ("muted-foreground", "Secondary text #525150."),
    ("surface", "Raised surface."),
    ("surface-foreground", "Text on surface."),
    ("field", "Input fill (#ffffff light, white/4.5% dark)."),
    ("popover", "Popover/menu fill."),
    ("popover-foreground", "Popover text."),
    ("popover-border", "Popover hairline."),
    ("border", "The border tone (#e4e3db light, white/10% dark)."),
    ("boundary", "The hairline (header underline, column rules)."),
    ("input", "Input border."),
    ("ring", "Focus ring."),
    ("focus", "Focus border (focus-visible:border-focus)."),
    ("placeholder", "Placeholder ink."),
    ("subtle-foreground", "Subtle text."),
    ("destructive", "Error/destructive."),
    ("destructive-foreground", "Text on destructive."),
    ("success", "Success."),
    ("success-foreground", "Text on success."),
    ("warning", "Warning."),
    ("warning-foreground", "Text on warning."),
    ("sidebar", "Sidebar fill (declared; the app shell behind sign-in)."),
    ("sidebar-foreground", "Sidebar text."),
    ("sidebar-border", "Sidebar border."),
    ("sidebar-accent", "Sidebar hover fill."),
    ("sidebar-primary", "Sidebar primary."),
    ("sidebar-ring", "Sidebar focus ring."),
    ("sidebar-raised", "Sidebar raised fill."),
    ("chart-1", "Chart 1 (declared chart ramp)."),
    ("chart-2", "Chart 2."),
    ("chart-3", "Chart 3."),
    ("chart-4", "Chart 4."),
    ("chart-5", "Chart 5."),
]
LIGHT["color"] = {n: var(f"--{n}", description=d) for n, d in SEM}
DARK["color"] = {n: var(f"--{n}", description=d) for n, d in SEM}
DARK_DESCS = {
    "background": "The .dark field #171715.",
    "foreground": "Dark-surface text #cdc8c1 (neutral-40).",
    "primary": "Growth #abd49e — the .dark primary.",
    "primary-foreground": "Text on dark primary #0a0a0a.",
    "card": "Dark card #171717.",
    "muted-foreground": "Dark secondary text #a1a1a1.",
    "surface": "Dark raised surface #262421.",
    "field": "Dark input fill white/4.5%.",
    "border": "Dark border white/10%.",
    "boundary": "Dark hairline white/6%.",
    "input": "Dark input border white/15%.",
    "ring": "Dark focus ring #737373.",
    "destructive": "Dark error #ff6467.",
    "success": "Dark success #56da7d.",
    "warning": "Dark warning #fe9a00.",
}
for n, d in DARK_DESCS.items():
    DARK["color"][n]["description"] = d
LIGHT["action"] = {"link-verdant": {"value": "{color.brand.verdant}", "type": "color",
                                    "source": "alias of core.color.brand.verdant (css-var --cartesia-verdant); the Tools breadcrumb measured text-cartesia-verdant",
                                    "description": "Inline verdant links (the Tools breadcrumb, text accents)."}}
DARK["action"] = {"link-verdant": {"value": "{color.brand.growth}", "type": "color",
                                   "source": "alias of core.color.brand.growth (css-var --cartesia-growth); on the .dark scope --primary rebinds to growth",
                                   "description": "On the .dark scope the accent reads growth."}}

# ----------------------------------------------------------------- components

COMP["header"] = {"height": meas("header", "height", type="dimension",
                                 src="measured header default (raw/components-computed.json); --site-nav-height",
                                 description="Sticky header height.")}
COMP["banner"] = {"height": meas("banner", "height", type="dimension",
                                 description="Announcement banner height.")}
COMP["button"] = {
    "height": meas("nav-cta", "height", type="dimension",
                   src="measured nav-cta/nav-sales/play-btn default",
                   description="The standard control height (control-height-default)."),
    "radius": meas("nav-cta", "borderTopLeftRadius", type="dimension",
                   src="measured nav-cta/play-btn default; --radius-lg",
                   description="Button radius."),
    "padding-x": meas("nav-cta", "paddingLeft", type="dimension",
                      description="Button inline padding."),
    "label-size": meas("nav-cta", "fontSize", type="dimension",
                       src="measured nav-cta/play-btn default",
                       description="Button label size."),
    "height-lg": meas("pd-cta", "height", type="dimension",
                      src="measured pd-cta/pd-secondary default",
                      description="Hero CTA height on product pages."),
    "height-auth": meas("continue-btn", "height", type="dimension",
                        src="measured continue-btn/email-field default",
                        description="Sign-in control height (control-height-xl)."),
    "radius-auth": meas("continue-btn", "borderTopLeftRadius", type="dimension",
                        src="measured continue-btn/sso-btn default",
                        description="Sign-in control radius."),
}
COMP["nav"] = {
    "link-height": meas("nav-link", "height", type="dimension",
                        src="measured nav-link/nav-trigger default",
                        description="Nav item height."),
    "menu-width": meas("nav-dropdown", "width", type="dimension",
                       description="Products mega-menu panel width."),
    "menu-radius": meas("menu-link", "borderTopLeftRadius", type="dimension",
                        description="Menu item radius (--radius-md)."),
    "menu-pad": meas("nav-dropdown", "paddingTop", type="dimension",
                     description="Menu panel padding."),
}
COMP["field"] = {
    "height": meas("email-field", "height", type="dimension", description="Sign-in field height."),
    "radius": meas("email-field", "borderTopLeftRadius", type="dimension", description="Sign-in field radius."),
    "padding-x": meas("email-field", "paddingLeft", type="dimension", description="Field inline padding."),
}
COMP["auth"] = {
    "column-width": meas("signup-card", "width", type="dimension",
                         src="measured login-card/signup-card default",
                         description="The centred sign-in column."),
    "field-width": meas("email-field", "width", type="dimension",
                        src="measured email-field/continue-btn default",
                        description="The auth form width."),
    "sso-width": meas("sso-btn", "width", type="dimension",
                      description="The SSO/passkey button width (the two buttons split the 420px form with a gap)."),
}
COMP["orb"] = {
    "size": meas("hero-orb", "width", type="dimension", description="The Talk-to-Skylar orb diameter."),
    "chooser-size": measrect("voice-choose", "w", type="dimension",
                             src="bounding-rect of voice-choose default (raw/components-computed.json): the buttons are scale-transformed, so the computed width is the pre-scale length and the rect is what paints",
                             description="A voice-chooser button diameter as displayed (ring of voices around the orb)."),
    "arrow-size": meas("voice-nav", "width", type="dimension", description="Voice carousel arrow size."),
}
COMP["chip"] = {
    "height": meas("usecase-chip", "height", type="dimension", description="Use-case chip height."),
    "voice-height": meas("voice-chip", "height", type="dimension", description="Voice/locale chip height."),
    "label-size": meas("usecase-chip", "fontSize", type="dimension", description="Chip label size."),
}
COMP["card"] = {
    "product-width": meas("product-card", "width", type="dimension",
                          description="Product card width (half of the two-up grid)."),
    "product-height": meas("product-card", "height", type="dimension", description="Product card height."),
    "story-tile": meas("story-card", "width", type="dimension",
                       src="measured media-frame/story-card default",
                       description="Customer-story media tile (square)."),
    "plan-width": meas("plan-card", "width", type="dimension", description="Plan card cell width."),
    "plan-padding": meas("plan-card", "paddingLeft", type="dimension",
                         description="Plan card inline padding (40px top)."),
}
COMP["play"] = {
    "sample-size": meas("word-play", "width", type="dimension",
                        description="Square pronunciation/clone play button."),
    "globe-dot": meas("globe-dot", "width", type="dimension", description="Voices-globe locale dot."),
    "globe-play": meas("globe-play", "width", type="dimension", description="Globe play button diameter."),
    "globe-voice-height": meas("globe-voice", "height", type="dimension", description="Globe voice row height."),
}
COMP["accordion"] = {
    "height": meas("accordion-trigger", "height", type="dimension", description="Deployment accordion row height."),
    "faq-padding": meas("faq-trigger", "paddingLeft", type="dimension",
                        description="FAQ summary inline padding (56px top)."),
}
COMP["docs"] = {
    "search-width": meas("docs-search", "width", type="dimension",
                         description="Docs search input width (Mintlify surface)."),
    "nav-height": meas("docs-nav-item", "height", type="dimension", description="Docs sidebar item height."),
    "nav-radius": meas("docs-nav-item", "borderTopLeftRadius", type="dimension",
                       description="Docs sidebar item radius."),
}
COMP["mobile"] = {
    "menu-height": meas("m-menu-open", "height", type="dimension",
                        description="Mobile menu covers the full viewport."),
    "nav-item-height": meas("m-nav-item", "height", type="dimension", description="Mobile nav item height."),
    "menu-button": meas("m-menu-button", "width", type="dimension", description="Mobile menu toggle size."),
}

# Refuse before writing: a failed build must not leave a half-built spec for build_tokens.py to read.
if missing:
    sys.exit(f"var leaves that never resolved: {missing}")
(RAW / "component-tokens.json").write_text(json.dumps(S, indent=1) + "\n")


def count(node):
    return sum(1 if isinstance(v, dict) and ("var" in v or "value" in v) else count(v)
               for v in node.values() if isinstance(v, dict))


print("component-tokens.json:", {s: count(S[s]) for s in ("core", "light", "dark", "component")})
