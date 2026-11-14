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
    "white": v("#fff", "color", css("body{background:#fff}, .input{background:#fff}")),
    "paper": v("#fafafa", "color", css(".section/background #fafafa")),
    "grey": {
        "950": v("#262626", "color", css("body{color:#262626} — the primary ink")),
        "900": v("#2c2c2c", "color", css("#2c2c2c")),
        "800": v("#333", "color", css(".btn-submit{background:#333}")),
        "750": v("#3a3a3a", "color", css(".profile__image{background:#3a3a3a}")),
        "700": v("#717171", "color", css("#717171 — secondary copy")),
        "600": v("#868686", "color", css("#868686")),
        "500": v("#9d9d9d", "color", css(".header{background:#9d9d9d} — the signature grey field")),
        "450": v("#b7b7b7", "color", css(".hero__tag{border-color:#b7b7b7}")),
        "400": v("#c1c1c1", "color", css(".auth__left{color:#c1c1c1}")),
        "300": v("#d0d0d0", "color", css(".page--arrow{background:#d0d0d0}")),
        "200": v("#e6e6e6", "color", css("#e6e6e6")),
        "150": v("#ebebeb", "color", css(".input{border-color:#ebebeb} — the hairline")),
        "100": v("#efefef", "color", css(".section--grey{background:#efefef}, .btn--grey{background:#efefef}")),
        "50": v("#f8f8f8", "color", css("#f8f8f8")),
    },
    "accent": {
        "DEFAULT": v("#ffc60a", "color", css(".btn-submit, .btn--yellow{background:#ffc60a} — the brand yellow")),
        "hover": v("#ffcc24", "color", css("#ffcc24 — yellow hover variant")),
    },
    "danger": {
        "DEFAULT": v("#f13939", "color", css(".btn--red{background:#f13939}, .svg-error{color:#f13939}")),
        "hover": v("#f35151", "color", css(".btn--red:hover{background:#f35151}")),
        "tint": v("#fdd6d6", "color", css("#fdd6d6 — error alert background")),
    },
    "success": {
        "DEFAULT": v("#2bd170", "color", css(".svg-success{color:#2bd170}")),
        "tint": v("#dffdd6", "color", css("#dffdd6 — success alert background")),
        "border": v("#d2e5cc", "color", css("#d2e5cc — success alert border")),
        "ink": v("#4f8a10", "color", css("#4f8a10 — success alert text")),
    },
    "info": {
        "DEFAULT": v("#3198ff", "color", css("#3198ff — link/notice blue")),
        "dark": v("#01558d", "color", css("#01558d")),
        "ink": v("#00529b", "color", css("#00529b — info alert text")),
        "tint": v("#add8e6", "color", css("#add8e6 — info alert background")),
    },
    "warning": {
        "tint": v("#fdf4d6", "color", css("#fdf4d6 — warning alert background")),
        "ink": v("#9f6000", "color", css("#9f6000 — warning alert text")),
    },
    "overlay": {
        "scrim": v("rgba(0,0,0,.04)", "color", css("rgba(0,0,0,.04) — feed tile hover scrim")),
        "modal": v("hsla(0,0%,44.3%,.95)", "color", css(".v--modal-overlay background — the modal veil")),
        "header-dim": v("hsla(0,0%,44.3%,.3)", "color", css("hsla(0,0%,44.3%,.3)")),
    },
    "black": v("#000", "color", css("#000")),
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
        "neutral-hover": v("#e7e7e7", "color", css(".btn--grey:hover{background:#e7e7e7}"), description="Grey button hover."),
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
    "link": v("{color.grey.950}", "color", "links render ink with underline (measured forgot-link/signup-link)", description="Inline links."),
}

# --------------------------------------------------------------------- type
core["font"] = {
    "family": {
        "sans": v("UntitledSans", "fontFamily", css("@font-face UntitledSans; body{font-family:UntitledSans}"), description="UI text."),
        "sans-medium": v("UntitledSansMedium", "fontFamily", css("@font-face UntitledSansMedium; .post__title, .hero__tag"), description="Medium cut for post titles, tags, strong UI."),
        "display": v("LabilGrotesk-Medium", "fontFamily", css("@font-face LabilGrotesk-Medium; .hero__title, .feature__title, the EXPLORE wordmark"), description="Display/brand face."),
        "system": v("system", "fontFamily", css("@font-face system — local() fallbacks for system UI")),
    },
    "weight": {
        "light": v(300, "fontWeight", css("font-weight:300")),
        "regular": v(400, "fontWeight", css("font-weight:400 — body/buttons")),
        "medium": v(500, "fontWeight", "medium cut carried by the UntitledSansMedium/LabilGrotesk-Medium families rather than font-weight:500", description="Medium weight, expressed through the medium families."),
        "bold": v(700, "fontWeight", css("font-weight:700 — strong, .page--current")),
    },
    "size": {
        "10": v("10px", "dimension", css("font-size:10px")),
        "12": v("12px", "dimension", css("font-size:12px — pills, micro labels")),
        "13": v("13px", "dimension", css("font-size:13px")),
        "14": v("14px", "dimension", css("font-size:14px — buttons, secondary")),
        "16": v("16px", "dimension", css("body{font-size:16px} — base")),
        "18": v("18px", "dimension", css("font-size:18px")),
        "21": v("21px", "dimension", css("font-size:21px — post/product titles")),
        "24": v("24px", "dimension", css("font-size:24px")),
        "32": v("32px", "dimension", css("font-size:32px")),
        "40": v("40px", "dimension", css(".hero__title{font-size:40px}")),
        "41": v("41px", "dimension", css(".feature title{font-size:41px}")),
    },
    "lineHeight": {
        "tight": v(1.02, "number", css(".hero__title 40/41px"), description="Display leading."),
        "snug": v(1.19, "number", css("16px/19px buttons")),
        "base": v(1.375, "number", css("body 16px/22px"), description="Body leading."),
        "loose": v(1.5, "number", css("legal/longform copy 16px/24px")),
    },
    "letterSpacing": {
        "none": v("0px", "dimension", "no letter-spacing declarations in the sheet; measured values are normal/0"),
    },
}

# --------------------------------------------------------------------- shape/space/motion
core["radius"] = {
    "sm": v("3px", "dimension", css("border-radius:3px")),
    "card": v("7px", "dimension", css("border-radius:7px — .hero__tag, feed cards"), description="Card/tag radius."),
    "input": v("8px", "dimension", css(".input{border-radius:8px}")),
    "lg": v("10px", "dimension", css("border-radius:10px")),
    "pill": v("20px", "dimension", css(".pill{border-radius:20px}"), description="Category pill radius."),
    "button": v("50px", "dimension", css(".btn-submit, .btn--rounded{border-radius:50px}"), description="Fully rounded buttons."),
    "avatar": v("34px", "dimension", css(".post__author-image{border-radius:34px}"), description="Round avatars (circle at any size)."),
    "avatar-lg": v("150px", "dimension", css(".profile__image{border-radius:150px}"), description="Large round profile image."),
}
core["spacing"] = {
    "2": v("2px", "dimension", css("padding/gap histogram")),
    "4": v("4px", "dimension", css("padding/gap histogram")),
    "5": v("5px", "dimension", css(".pill{margin:0 5px}")),
    "6": v("6px", "dimension", css(".pill{padding:6px …}")),
    "8": v("8px", "dimension", css("padding histogram")),
    "10": v("10px", "dimension", css("padding histogram")),
    "12": v("12px", "dimension", css(".post__content{margin:12px 0 0}")),
    "13": v("13px", "dimension", css(".pill{padding:6px 13px 7px}")),
    "15": v("15px", "dimension", css(".post{padding:0 15px 50px} — feed column gutter")),
    "16": v("16px", "dimension", css("padding histogram")),
    "20": v("20px", "dimension", css(".content{padding:0 20px}")),
    "23": v("23px", "dimension", css(".hero__tag{padding:11px 23px}")),
    "24": v("24px", "dimension", css(".discover{padding:21px 24px 0}")),
    "30": v("30px", "dimension", css("padding histogram")),
    "40": v("40px", "dimension", css("padding histogram")),
    "50": v("50px", "dimension", css(".post{padding-bottom:50px} — feed row pitch")),
    "60": v("60px", "dimension", css("padding histogram")),
    "100": v("100px", "dimension", css(".posts{margin-bottom:100px}")),
}
core["container"] = {
    "page": v("1640px", "dimension", css(".content{max-width:1640px}"), description="Max content width."),
    "footer": v("990px", "dimension", css(".footer{max-width:990px}")),
    "form": v("424px", "dimension", css(".auth__right{max-width:424px}"), description="Auth form column."),
    "legal": v("760px", "dimension", "measured legal-body width 760px", description="Legal/statement copy column."),
}
core["breakpoint"] = {
    "sm": v("650px", "dimension", css("@media (max-width:650px) — the mobile cutover, 169 rules in the sheet")),
    "md": v("980px", "dimension", css("@media (max-width:980px) and @media (max-width:980px) and (min-width:650px) — the tablet cutover (.text-center--tablet, .activity, .subscribe)")),
    "lg": v("1280px", "dimension", css("@media (max-width:1280px) — the tablet-big cutover (.hide-tablet-big/.show-tablet-big)")),
}
core["duration"] = {
    "fast": v("200ms", "duration", css(".btn,.btn-icon,.btn-submit{transition-duration:0.2s} and a{transition:color 0.2s} — links and buttons")),
    "base": v("300ms", "duration", css(".default-transition / transition .3s")),
    "slow": v("500ms", "duration", css("transition .5s on hero/reveal")),
}
core["easing"] = {
    "standard": v("ease", "cubicBezier", css("ease — declared transitions")),
    "out": v("ease-out", "cubicBezier", css("ease-out transitions")),
}
core["zIndex"] = {
    "header": v(300, "number", css(".header{z-index:300}")),
    "modal": v(999, "number", css(".v--modal overlay z-index")),
}
core["shadow"] = {
    "none": v("none", "other", "no box-shadow declarations on the signed-out chrome; cards are border/flat only", description="Flat UI — no shadows in the public surface."),
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
comp["pill"] = {"height": dim("pill", "default", "h"), "gap": v("10px", "dimension", css(".pill{margin:0 5px 9px} → 10px column gap"))}
comp["post"] = {
    "cardWidth": dim("post-card", "default", "w"),
    "galleryHeight": dim("post-gallery", "default", "h"),
    "avatarSize": dim("post-avatar", "default", "w"),
    "gridColumns": v("calc(33.3333% - .5px)", "other", css(".post{width:calc(33.3333% - .5px)}"), description="3-up feed grid."),
}
comp["mobile"] = {"postWidth": dim("m-post", "default", "w")}

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json written")
