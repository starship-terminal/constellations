#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

explore.family's February 2023 build declares no custom properties and no
prefers-color-scheme rules: one fixed light theme, every value hardcoded in
the compiled stylesheet app.4ef09b07.css (the full rule dump is
raw/css-declarations.json). Colours, the type ramp, radii and spacings below
are therefore literals mined from that sheet plus the computed styles in
raw/components-computed.json — each leaf names its evidence in `source`.

Palette roles, read from the sheet and the rendered pages:
  field      #9d9d9d — the grey field: fixed .header bar, hero section,
             avatar/media placeholders (the auth welcome panel is darker,
             #717171)
  paper      #fff    — feed and form surfaces, page background (body{})
  ink        #262626 — primary text, active pill border, dark button
  muted      #717171 / #868686 / #9d9d9d — secondary copy (discover title,
             post age, footer links)
  hairline   #ebebeb — input borders, feature separators
  surface    #efefef — grey button bg, section--grey, pill border
  accent     #ffc60a — the yellow: Sign up free pill, about CTA, PRO badge
  danger     #f13939 — error/red button
  success    #2bd170 — form success icons
  info       #3198ff — link/notice blue
Type: UntitledSans (UI), UntitledSansMedium (post titles, tags),
LabilGrotesk-Medium (display headings, the EXPLORE wordmark). Ramp
10/12/13/14/16/18/21/24/32/40/41px, weights 300/400/700.
Shape: 7–8px on cards and inputs, 20px pills, 50px button pills, round
avatars (28/64/142px boxes at 34–150px radii).

Deterministic: re-running writes the same file.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
D = json.loads((RAW / "css-declarations.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())["components"]

CSS = "stylesheet declaration in app.4ef09b07.css (raw/css-declarations.json)"


def css(sel):
    return f"{CSS}: {sel}"


def measured(comp, state, prop):
    return f"measured {comp} {state} {prop} (raw/components-computed.json)"


def st(comp, state="default"):
    return C[comp]["states"][state]["style"]


def v(value, ty, source, **kw):
    d = {"value": value, "type": ty, "source": source}
    d.update(kw)
    return d


# Every value the compiled sheet declares, by property, and every @media condition it holds.
DECLARED, MEDIA = {}, set()
for _d in D["declarations"]:
    for _p, _v in _d["properties"].items():
        DECLARED.setdefault(_p, set()).add(_v)
    MEDIA.update(_d.get("context") or [])
FAMILY = {
    "color": ("color", "background", "border", "fill", "stroke", "box-shadow", "outline"),
    "font-size": ("font-size",), "font-weight": ("font-weight",), "line-height": ("line-height",),
    "radius": ("border-top-left-radius", "border-top-right-radius", "border-bottom-left-radius", "border-bottom-right-radius"),
    "space": ("padding", "margin", "gap", "column-gap", "row-gap"),
    "width": ("max-width", "width", "min-width"), "z-index": ("z-index",),
    "duration": ("transition", "transition-duration", "animation-duration"),
    "easing": ("transition", "transition-timing-function", "animation-timing-function"),
}


def cssom(value, ty):
    """A literal in the form the CSSOM serialises it, as raw/css-declarations.json holds values."""
    s = str(value).strip().lower()
    if ty == "color":
        m = re.fullmatch(r"#([0-9a-f]{3}|[0-9a-f]{6})", s)
        if m:
            h = m.group(1) if len(m.group(1)) == 6 else "".join(c * 2 for c in m.group(1))
            return "rgb(%d, %d, %d)" % tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
        m = re.fullmatch(r"rgba\(([\d.]+),\s*([\d.]+),\s*([\d.]+),\s*([\d.]+)\)", s)
        if m:
            return "rgba(%s, %s, %s, %g)" % (*m.groups()[:3], float(m.group(4)))
        m = re.fullmatch(r"hsla\(0,\s*0%,\s*([\d.]+)%,\s*([\d.]+)\)", s)
        if m:
            lv = round(float(m.group(1)) * 2.55)
            return "rgba(%d, %d, %d, %g)" % (lv, lv, lv, float(m.group(2)))
    if ty == "duration" and s.endswith("ms"):
        return "%gs" % (float(s[:-2]) / 1000)
    return s


def mined(family, value, ty, source, **kw):
    """A value chosen from the compiled stylesheet at capture time. The sheet's rules are in
    raw/css-declarations.json, so the build checks the value is still declared there under the
    family of properties it stands for and stops if a recapture dropped it."""
    form = cssom(value, ty)
    pat = re.compile(r"(?<![\w.#-])" + re.escape(form) + r"(?![\w.%-])")
    props = [p for p in DECLARED if any(p == f or p.startswith(f + "-") for f in FAMILY[family])]
    if not any(pat.search(val) for p in props for val in DECLARED[p]):
        raise SystemExit(f"{value!r} ({form}) is not declared on any {family} property in raw/css-declarations.json; "
                         "fix the row or relabel it as entered by hand")
    return v(value, ty, source, **kw)


def media(value, source, **kw):
    """A breakpoint the sheet declares as an @media max-width condition."""
    if not any(re.search(r"max-width:\s*" + re.escape(value) + r"\b", ctx) for ctx in MEDIA):
        raise SystemExit(f"no @media (max-width: {value}) in raw/css-declarations.json")
    return v(value, "dimension", source, **kw)


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. Explore ships "
    "no design-token layer: every value here is a hardcoded literal mined "
    "from the compiled stylesheet (raw/css-declarations.json) or measured "
    "from computed styles (raw/components-computed.json) on the replayed "
    "2023-02-23 build. Theme-invariant scales under core.*, surface roles "
    "under light.*, measured component geometry under component.*."),
    "core": {}, "light": {}, "component": {}}

core, light, comp = SPEC["core"], SPEC["light"], SPEC["component"]

# --------------------------------------------------------------------- colour scales (all mined)
core["color"] = {
    "white": mined("color", "#fff", "color", css("body{background:#fff}, .input{background:#fff}")),
    "paper": mined("color", "#fafafa", "color", css(".section/background #fafafa")),
    "grey": {
        "950": mined("color", "#262626", "color", css("body{color:#262626} — the primary ink")),
        "900": mined("color", "#2c2c2c", "color", css("#2c2c2c")),
        "800": mined("color", "#333", "color", css(".btn-submit{background:#333}")),
        "750": mined("color", "#3a3a3a", "color", css(".profile__image{background:#3a3a3a}")),
        "700": mined("color", "#717171", "color", css("#717171 — secondary copy")),
        "600": mined("color", "#868686", "color", css("#868686")),
        "500": mined("color", "#9d9d9d", "color", css(".header{background:#9d9d9d} — the signature grey field")),
        "450": mined("color", "#b7b7b7", "color", css(".hero__tag{border-color:#b7b7b7}")),
        "400": mined("color", "#c1c1c1", "color", css(".auth__left{color:#c1c1c1}")),
        "300": mined("color", "#d0d0d0", "color", css(".page--arrow{background:#d0d0d0}")),
        "200": mined("color", "#e6e6e6", "color", css("#e6e6e6")),
        "150": mined("color", "#ebebeb", "color", css(".input{border-color:#ebebeb} — the hairline")),
        "100": mined("color", "#efefef", "color", css(".section--grey{background:#efefef}, .btn--grey{background:#efefef}")),
        "50": mined("color", "#f8f8f8", "color", css("#f8f8f8")),
    },
    "accent": {
        "DEFAULT": mined("color", "#ffc60a", "color", css(".btn-submit, .btn--yellow{background:#ffc60a} — the brand yellow")),
        "hover": mined("color", "#ffcc24", "color", css("#ffcc24 — yellow hover variant")),
    },
    "danger": {
        "DEFAULT": mined("color", "#f13939", "color", css(".btn--red{background:#f13939}, .svg-error{color:#f13939}")),
        "hover": mined("color", "#f35151", "color", css(".btn--red:hover{background:#f35151}")),
        "tint": mined("color", "#fdd6d6", "color", css("#fdd6d6 — error alert background")),
    },
    "success": {
        "DEFAULT": mined("color", "#2bd170", "color", css(".svg-success{color:#2bd170}")),
        "tint": mined("color", "#dffdd6", "color", css("#dffdd6 — success alert background")),
        "border": mined("color", "#d2e5cc", "color", css("#d2e5cc — success alert border")),
        "ink": mined("color", "#4f8a10", "color", css("#4f8a10 — success alert text")),
    },
    "info": {
        "DEFAULT": mined("color", "#3198ff", "color", css("#3198ff — link/notice blue")),
        "dark": mined("color", "#01558d", "color", css("#01558d")),
        "ink": mined("color", "#00529b", "color", css("#00529b — info alert text")),
        "tint": mined("color", "#add8e6", "color", css("#add8e6 — info alert background")),
    },
    "warning": {
        "tint": mined("color", "#fdf4d6", "color", css("#fdf4d6 — warning alert background")),
        "ink": mined("color", "#9f6000", "color", css("#9f6000 — warning alert text")),
    },
    "overlay": {
        "scrim": mined("color", "rgba(0,0,0,.04)", "color", css("rgba(0,0,0,.04) — feed tile hover scrim")),
        "modal": mined("color", "hsla(0,0%,44.3%,.95)", "color", css(".v--modal-overlay background — the modal veil")),
        "header-dim": mined("color", "hsla(0,0%,44.3%,.3)", "color", css("hsla(0,0%,44.3%,.3)")),
    },
    "black": mined("color", "#000", "color", css("#000")),
}

# --------------------------------------------------------------------- semantic roles (light only)
light["color"] = {
    "background": {
        "page": v("{color.white}", "color", "body{background:#fff}; measured page field", description="The page surface under feed and forms."),
        "field": v("{color.grey.500}", "color", css(".header{background:#9d9d9d}, .section--hero{background:#9d9d9d}"), description="The signature mid-grey field: fixed header bar, hero, media placeholders (the auth welcome panel is the darker #717171)."),
        "surface": v("{color.grey.100}", "color", css(".section--grey{background:#efefef}, .btn--grey"), description="Recessed grey surfaces (footer band, grey buttons)."),
        "hairline": v("{color.grey.150}", "color", css(".input, .pill{border-color:#ebebeb/#efefef}"), description="The 1px hairline on inputs, pills and separators."),
    },
    "text": {
        "primary": v("{color.grey.950}", "color", css("body{color:#262626}"), description="Primary ink."),
        "on-field": v("{color.white}", "color", css(".section--hero{color:#fff}"), description="Text on the grey field."),
        "secondary": v("{color.grey.700}", "color", css("#717171 — footer/form secondary copy"), description="Secondary copy."),
        "muted": v("{color.grey.500}", "color", css(".discover__title{color:#9d9d9d}"), description="Muted copy (discover subtitle, post age)."),
        "faint": v("{color.grey.400}", "color", css(".auth__left{color:#c1c1c1}"), description="Faint copy on the grey field."),
        "inverse-soft": v("{color.grey.50}", "color", css(".hero__tag/.pill{color:#f8f8f8}"), description="Soft white on grey (hero tags, dark-mode text)."),
    },
    "action": {
        "accent": v("{color.accent.DEFAULT}", "color", css(".btn--yellow, .btn-submit{background:#ffc60a}"), description="The yellow CTA field (the Sign up free pill, the about-page Sign up CTA, PRO badge — auth submits are the dark .btn, not this)."),
        "accent-hover": v("{color.accent.hover}", "color", css(".btn--yellow:hover/#ffcc24"), description="Yellow hover."),
        "on-accent": v("{color.grey.950}", "color", css(".btn--yellow{color:#262626}"), description="Ink on the yellow CTA."),
        "primary": v("{color.grey.950}", "color", css(".btn-submit--dark, .btn--dark{background:#262626}"), description="The dark submit (Log in, Sign up, Reset password — all three auth submits measured #262626 with 7px corners)."),
        "primary-hover": v("{color.grey.800}", "color", css(".btn--dark:hover{background:#333}"), description="Dark submit hover."),
        "on-primary": v("{color.white}", "color", css(".btn--dark{color:#fff}"), description="Text on the dark submit."),
        "neutral": v("{color.grey.100}", "color", css(".btn--grey{background:#efefef}"), description="Grey button field."),
        "neutral-hover": mined("color", "#e7e7e7", "color", css(".btn--grey:hover{background:#e7e7e7}"), description="Grey button hover."),
        "danger": v("{color.danger.DEFAULT}", "color", css(".btn--red{background:#f13939}"), description="Destructive red."),
        "danger-hover": v("{color.danger.hover}", "color", css(".btn--red:hover{background:#f35151}"), description="Destructive hover."),
        "outline": v("{color.grey.150}", "color", css(".btn--outline{border:1px solid #ebebeb}"), description="Outline button hairline."),
    },
    "border": {
        "hairline": v("{color.grey.150}", "color", css(".input{border:1px solid #ebebeb}")),
        "field": v("{color.grey.100}", "color", css(".pill{border:1px solid #efefef}"), description="Idle pill border."),
        "strong": v("{color.grey.950}", "color", css(".pill.router-link-active{border-color:#262626}"), description="Active pill border."),
        "on-field": v("{color.grey.450}", "color", css(".hero__tag, .section--hero{border-color:#b7b7b7}"), description="Borders on the grey field."),
    },
    "link": v("{color.grey.950}", "color", "measured signup-link default color (raw/components-computed.json): ink with an underline; the forgot-password link paints the muted #9d9d9d without one", description="Inline links."),
}

# --------------------------------------------------------------------- type
FACES = {f["font-family"] for f in D["fonts"]}


def face(name, source, **kw):
    """A family the sheet serves through @font-face (raw/css-declarations.json fonts)."""
    if name not in FACES:
        raise SystemExit(f"{name} has no @font-face in raw/css-declarations.json")
    return v(name, "fontFamily", source, **kw)


def face_weight(w, source, **kw):
    """A weight the sheet declares only on an @font-face rule."""
    if str(w) not in {f.get("font-weight") for f in D["fonts"]}:
        raise SystemExit(f"no @font-face with font-weight {w} in raw/css-declarations.json")
    return v(w, "fontWeight", source, **kw)


def ratio(size, line, source, **kw):
    """A unitless leading derived from a declared font-size/line-height pair."""
    for prop, val in (("font-size", size), ("line-height", line)):
        if f"{val}px" not in DECLARED.get(prop, ()):
            raise SystemExit(f"no {prop}: {val}px in raw/css-declarations.json")
    return v(round(line / size, 4), "number", f"derived: line-height {line}px / font-size {size}px, both declared in "
             f"app.4ef09b07.css (raw/css-declarations.json); {source}", **kw)


core["font"] = {
    "family": {
        "sans": face("UntitledSans", css("@font-face UntitledSans; body{font-family:UntitledSans}"), description="UI text."),
        "sans-medium": face("UntitledSansMedium", css("@font-face UntitledSansMedium; .post__title, .hero__tag"), description="Medium cut for post titles, tags, strong UI."),
        "display": face("LabilGrotesk-Medium", css("@font-face LabilGrotesk-Medium; .hero__title, .feature__title, the EXPLORE wordmark"), description="Display/brand face."),
        "system": face("system", css("@font-face system — local() fallbacks for system UI")),
    },
    "weight": {
        "light": face_weight(300, css("@font-face system{font-weight:300} — the only 300 the sheet declares; no rule sets font-weight:300")),
        "regular": mined("font-weight", 400, "fontWeight", css("font-weight:400 — body/buttons")),
        "medium": v(500, "fontWeight", "Reconstruction: entered by hand at capture time; the sheet declares no font-weight:500 — the medium cut is carried by the UntitledSansMedium/LabilGrotesk-Medium families", description="Medium weight, expressed through the medium families."),
        "bold": mined("font-weight", 700, "fontWeight", css("font-weight:700 — strong, .page--current")),
    },
    "size": {
        "10": mined("font-size", "10px", "dimension", css("font-size:10px")),
        "12": mined("font-size", "12px", "dimension", css("font-size:12px — pills, micro labels")),
        "13": mined("font-size", "13px", "dimension", css("font-size:13px")),
        "14": mined("font-size", "14px", "dimension", css("font-size:14px — buttons, secondary")),
        "16": mined("font-size", "16px", "dimension", css("body{font-size:16px} — base")),
        "18": mined("font-size", "18px", "dimension", css("font-size:18px")),
        "21": mined("font-size", "21px", "dimension", css("font-size:21px — post/product titles")),
        "24": mined("font-size", "24px", "dimension", css("font-size:24px")),
        "32": mined("font-size", "32px", "dimension", css("font-size:32px")),
        "40": mined("font-size", "40px", "dimension", css(".hero__title{font-size:40px}")),
        "41": mined("font-size", "41px", "dimension", css(".feature title{font-size:41px}")),
    },
    "lineHeight": {
        "tight": ratio(40, 41, ".hero__title", description="Display leading."),
        "snug": ratio(16, 19, "buttons"),
        "base": ratio(16, 22, "body", description="Body leading."),
        "loose": ratio(16, 24, "legal/longform copy"),
    },
    "letterSpacing": {
        "none": v("0px", "dimension", "derived: no measured component computes a letter-spacing other than normal (raw/components-computed.json); "
                  "the sheet's two declarations (.auth__stripe 0.2em, a header-menu span 0.3px) sit on elements the capture did not measure"),
    },
}

# --------------------------------------------------------------------- shape/space/motion
core["radius"] = {
    "sm": mined("radius", "3px", "dimension", css("border-radius:3px")),
    "card": mined("radius", "7px", "dimension", css("border-radius:7px — .hero__tag, feed cards"), description="Card/tag radius."),
    "input": mined("radius", "8px", "dimension", css(".input{border-radius:8px}")),
    "lg": mined("radius", "10px", "dimension", css("border-radius:10px")),
    "pill": mined("radius", "20px", "dimension", css(".pill{border-radius:20px}"), description="Category pill radius."),
    "button": mined("radius", "50px", "dimension", css(".btn-submit, .btn--rounded{border-radius:50px}"), description="Fully rounded buttons."),
    "avatar": mined("radius", "34px", "dimension", css(".post__author-image{border-radius:34px}"), description="Round avatars (circle at any size)."),
    "avatar-lg": mined("radius", "150px", "dimension", css(".profile__image{border-radius:150px}"), description="Large round profile image."),
}
core["spacing"] = {
    "2": mined("space", "2px", "dimension", css("padding/gap histogram")),
    "4": mined("space", "4px", "dimension", css("padding/gap histogram")),
    "5": mined("space", "5px", "dimension", css(".pill{margin:0 5px}")),
    "6": mined("space", "6px", "dimension", css(".pill{padding:6px …}")),
    "8": mined("space", "8px", "dimension", css("padding histogram")),
    "10": mined("space", "10px", "dimension", css("padding histogram")),
    "12": mined("space", "12px", "dimension", css(".post__content{margin:12px 0 0}")),
    "13": mined("space", "13px", "dimension", css(".pill{padding:6px 13px 7px}")),
    "15": mined("space", "15px", "dimension", css(".post{padding:0 15px 50px} — feed column gutter")),
    "16": mined("space", "16px", "dimension", css("padding histogram")),
    "20": mined("space", "20px", "dimension", css(".content{padding:0 20px}")),
    "23": mined("space", "23px", "dimension", css(".hero__tag{padding:11px 23px}")),
    "24": mined("space", "24px", "dimension", css(".discover{padding:21px 24px 0}")),
    "30": mined("space", "30px", "dimension", css("padding histogram")),
    "40": mined("space", "40px", "dimension", css("padding histogram")),
    "50": mined("space", "50px", "dimension", css(".post{padding-bottom:50px} — feed row pitch")),
    "60": mined("space", "60px", "dimension", css("padding histogram")),
    "100": mined("space", "100px", "dimension", css(".posts{margin-bottom:100px}")),
}
core["container"] = {
    "page": mined("width", "1640px", "dimension", css(".content{max-width:1640px}"), description="Max content width."),
    "footer": mined("width", "990px", "dimension", css(".footer{max-width:990px}")),
    "form": mined("width", "424px", "dimension", css(".auth__right{max-width:424px}"), description="Auth form column."),
}
core["breakpoint"] = {
    "sm": media("650px", css("@media (max-width:650px) — the mobile cutover, 169 rules in the sheet")),
    "md": media("980px", css("@media (max-width:980px) and @media (max-width:980px) and (min-width:650px) — the tablet cutover (.text-center--tablet, .activity, .subscribe)")),
    "lg": media("1280px", css("@media (max-width:1280px) — the tablet-big cutover (.hide-tablet-big/.show-tablet-big)")),
}
core["duration"] = {
    "fast": mined("duration", "200ms", "duration", css(".btn,.btn-icon,.btn-submit{transition-duration:0.2s} and a{transition:color 0.2s} — links and buttons")),
    "base": mined("duration", "300ms", "duration", css(".default-transition / transition .3s")),
    "slow": mined("duration", "500ms", "duration", css("transition .5s on hero/reveal")),
}
core["easing"] = {
    "standard": mined("easing", "ease", "cubicBezier", css("ease — declared transitions")),
    "out": mined("easing", "ease-out", "cubicBezier", css("ease-out transitions")),
}
core["zIndex"] = {
    "header": mined("z-index", 300, "number", css(".header{z-index:300}")),
    "modal": v(999, "number", "Reconstruction: entered by hand at capture time; raw/css-declarations.json declares no z-index of 999 (the sheet's highest is 2000, on .alert)"),
}
core["shadow"] = {
    "none": v("none", "other", "derived: no measured component computes a box-shadow (raw/components-computed.json); the sheet's "
              ".box-shadow/.panel utility shadows sit on surfaces the capture did not measure", description="Flat UI — no shadows on the measured public surface."),
}

# --------------------------------------------------------------------- component geometry (measured)
def dim(comp_, state, key, unit="px"):
    st_ = C[comp_]["states"][state]
    val = st_["rect"][key]
    if not val:
        # A hidden element measures a 0 rect (the marketing header is
        # display:none in the auth pages' DOM): never export 0px geometry.
        # Fall back to the element's declared CSS size when it has one.
        prop = {"w": "width", "h": "height"}[key]
        cssv = (st_.get("style") or {}).get(prop, "")
        if re.fullmatch(r"\d+(\.\d+)?px", cssv):
            return v(cssv, "dimension",
                     measured(comp_, state, f"style.{prop}") +
                     " (element display:none at capture; declared size, not a rect)")
        raise SystemExit(
            f"{comp_} {state} rect.{key} is 0 — a hidden reading slipped in; "
            "re-measure the component on a page where it is visible")
    return v(f"{val:g}px", "dimension", measured(comp_, state, f"rect.{key}"))


core["container"]["legal"] = {**dim("legal-body", "default", "w"), "description": "Legal/statement copy column."}

comp["header"] = {
    "height": dim("mkt-header", "default", "h"),
    "heightMobile": dim("m-header", "default", "h"),
    "logoHeight": dim("mkt-logo", "default", "h"),
}
comp["button"] = {
    "signupPill": {"height": dim("nav-signup", "default", "h"), "minWidth": dim("nav-signup", "default", "w")},
    "submit": {"height": dim("login-submit", "default", "h"), "formWidth": dim("login-submit", "default", "w")},
    "icon": {"size": dim("password-eye", "default", "h")},
    "aboutCta": {"width": dim("about-cta", "default", "w"), "height": dim("about-cta", "default", "h")},
}
comp["field"] = {
    "width": dim("field-email", "default", "w"),
    "inputHeight": v(st("field-email")["height"], "dimension", measured("field-email", "default", "style.height")),
    "padding": v(f'{st("field-email")["paddingTop"]} {st("field-email")["paddingLeft"]}', "other", measured("field-email", "default", "style.padding"), description="Block and inline padding."),
}
comp["pill"] = {"height": dim("pill", "default", "h"),
               "gap": {**mined("space", "5px", "dimension", ""), "value": "10px",
                       "source": "derived: two .pill{margin:0 5px 9px} side margins of 5px make a 10px column gap (raw/css-declarations.json)"}}
comp["post"] = {
    "cardWidth": dim("post-card", "default", "w"),
    "galleryHeight": dim("post-gallery", "default", "h"),
    "avatarSize": dim("post-avatar", "default", "w"),
    "gridColumns": {**mined("width", "calc(33.3333% - 0.5px)", "other", css(".post{width:calc(33.3333% - .5px)}"), description="3-up feed grid."),
                    "value": "calc(33.3333% - .5px)"},
}
comp["mobile"] = {"postWidth": dim("m-post", "default", "w")}

# The measured link ink must still be the colour the link role aliases.
for _k in ("signup-link",):
    if cssom(st(_k)["color"], "color") != cssom(core["color"]["grey"]["950"]["value"], "color"):
        raise SystemExit(f"{_k} no longer paints {core['color']['grey']['950']['value']}; fix light.color.link")

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json written")
