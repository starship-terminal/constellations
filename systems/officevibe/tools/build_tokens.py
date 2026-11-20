#!/usr/bin/env python3
"""Build tokens.json from the live readings of the public Workleap / Officevibe site.

Read on 2026-11-19 from the attached preview tab, signed out:

  raw/marketing-root-vars.json   computed custom properties on :root at
                                 https://workleap.com/officevibe (1169 CSS px)
  raw/login-hop-vars.json        computed --hop-* and --o-ui-* properties on
                                 :root at https://login.workleap.com/
  raw/computed.json              computed styles of the elements those tokens
                                 paint, plus the stylesheet rules named in
                                 $extensions.source

The marketing page sets html font-size to 15.436px at that width, so a rem
there is not 16px. Login uses 16px. Tokens keep the declared rem or hex.
A computed px check is recorded beside the token when one was read.
Every token carries $extensions.source.evidence. A custom property read from
the two :root dumps is Measured. raw/computed.json keeps only the capture
metadata, not the element styles, so a value whose source is an element's
computed style (ELEM) was typed in by hand at capture time and is labelled
Reconstruction.

Deterministic: same inputs, same bytes.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
OUT = HERE / "tokens.json"

M = json.loads((RAW / "marketing-root-vars.json").read_text())
H = json.loads((RAW / "login-hop-vars.json").read_text())


BY_HAND = "Entered by hand at capture time; raw/computed.json does not hold this element's computed style."
NOT_IN_DUMP = "Entered by hand at capture time from the stylesheet rule; raw/ keeps only the :root custom properties, and this one is not among them."


def src(evidence_from, selector, prop, note=None):
    # Measured only when the value is one of the two :root dumps' readings; an element style or a
    # stylesheet rule (.heading-style-h2, .button) was typed in by hand.
    dump = {MKT: M, LOGIN: H}.get(evidence_from)
    reason = BY_HAND if evidence_from == ELEM else (NOT_IN_DUMP if dump is not None and (selector != ":root" or prop not in dump) else None)
    body = {"evidence": "Reconstruction" if reason else "Measured", "from": evidence_from, "selector": selector, "property": prop}
    if note:
        body["note"] = note
    if reason:
        body["note"] = (body.get("note", "") + ". " if note else "") + reason
    return {"$extensions": {"source": body}}


def inherit_labels(doc):
    """An alias of a Reconstruction token is a Reconstruction too: it carries a hand-entered value."""
    flat = {}

    def walk(node, path):
        if isinstance(node, dict) and "$value" in node:
            flat[path] = node
        elif isinstance(node, dict):
            for k, v in node.items():
                if not k.startswith("$"):
                    walk(v, f"{path}.{k}" if path else k)

    for name in ("core", "light"):
        walk(doc[name], "")
    for token in flat.values():
        v = token["$value"]
        if isinstance(v, str) and v.startswith("{") and v.endswith("}"):
            target = flat.get(v[1:-1])
            body = token["$extensions"]["source"]
            if target and target["$extensions"]["source"]["evidence"] == "Reconstruction" and body["evidence"] == "Measured":
                body["evidence"] = "Reconstruction"
                body["note"] = (body.get("note", "") + ". " if body.get("note") else "") + f"Aliases {v}, which was entered by hand."
    return doc


def color(value, **kw):
    return {"$type": "color", "$value": value, **src(**kw)}


def dim(value, **kw):
    return {"$type": "dimension", "$value": value, **src(**kw)}


def duration(value, **kw):
    return {"$type": "duration", "$value": value, **src(**kw)}


def num(value, type_, **kw):
    return {"$type": type_, "$value": value, **src(**kw)}


def font(value, **kw):
    return {"$type": "fontFamily", "$value": value, **src(**kw)}


def shadow(value, **kw):
    return {"$type": "shadow", "$value": value, **src(**kw)}


def typography(value, **kw):
    return {"$type": "typography", "$value": value, **src(**kw)}


MKT = "https://workleap.com/officevibe computed :root, 2026-11-19, viewport 1169x731, html font-size 15.436px"
LOGIN = "https://login.workleap.com/ computed :root, 2026-11-19, viewport 1169x731, html font-size 16px"
ELEM = "computed style, same capture"


def m(prop):
    return src(MKT, ":root", prop)


def hop(prop, note=None):
    return src(LOGIN, ":root", prop, note)


def build():
    core = {
        "color": {
            "brand": {
                "leapin-blue": color(M["--brand-color-palette--leapin-blue"], **{"evidence_from": MKT, "selector": ":root", "prop": "--brand-color-palette--leapin-blue"}),
                "boardroom-navy": color(M["--brand-color-palette--boardroom-navy"], evidence_from=MKT, selector=":root", prop="--brand-color-palette--boardroom-navy"),
                "workin-ivory": color(M["--brand-color-palette--workin-ivory"], evidence_from=MKT, selector=":root", prop="--brand-color-palette--workin-ivory"),
                "secondary-ivory": color(M["--brand-color-palette--secondary-ivory"], evidence_from=MKT, selector=":root", prop="--brand-color-palette--secondary-ivory"),
                "lilac": color(M["--brand-color-palette--lilac"], evidence_from=MKT, selector=":root", prop="--brand-color-palette--lilac"),
                "orange": color(M["--brand-color-palette--orange"], evidence_from=MKT, selector=":root", prop="--brand-color-palette--orange"),
                "nine-to-five-black": color(M["--brand-color-palette--9-to-5-black"], evidence_from=MKT, selector=":root", prop="--brand-color-palette--9-to-5-black"),
                "white": color("#ffffff", evidence_from=MKT, selector=":root", prop="--brand-color-palette--white", note="declared as the keyword white"),
            },
            "grey": {
                "00": color(M["--base-color-greyscale--grey-00"], evidence_from=MKT, selector=":root", prop="--base-color-greyscale--grey-00"),
                "20": color(M["--base-color-greyscale--grey-20"], evidence_from=MKT, selector=":root", prop="--base-color-greyscale--grey-20"),
                "40": color(M["--base-color-greyscale--grey-40"], evidence_from=MKT, selector=":root", prop="--base-color-greyscale--grey-40"),
                "60": color(M["--base-color-greyscale--grey-60"], evidence_from=MKT, selector=":root", prop="--base-color-greyscale--grey-60"),
                "80": color(M["--base-color-greyscale--grey-80"], evidence_from=MKT, selector=":root", prop="--base-color-greyscale--grey-80"),
                "100": color(M["--base-color-greyscale--grey-100"], evidence_from=MKT, selector=":root", prop="--base-color-greyscale--grey-100"),
            },
            "soft": {
                "20": color(M["--base-color-soft--soft-20"], evidence_from=MKT, selector=":root", prop="--base-color-soft--soft-20"),
                "40": color(M["--base-color-soft--soft-40"], evidence_from=MKT, selector=":root", prop="--base-color-soft--soft-40"),
                "60": color(M["--base-color-soft--soft-60"], evidence_from=MKT, selector=":root", prop="--base-color-soft--soft-60"),
            },
            "semantic": {
                "success-100": color(M["--base-color-semantic-colors--success-100"], evidence_from=MKT, selector=":root", prop="--base-color-semantic-colors--success-100"),
                "success-20": color(M["--base-color-semantic-colors--success-20"], evidence_from=MKT, selector=":root", prop="--base-color-semantic-colors--success-20"),
                "warning-100": color(M["--base-color-semantic-colors--warning-100"], evidence_from=MKT, selector=":root", prop="--base-color-semantic-colors--warning-100"),
                "warning-20": color(M["--base-color-semantic-colors--warning-20"], evidence_from=MKT, selector=":root", prop="--base-color-semantic-colors--warning-20"),
                "danger-100": color(M["--base-color-semantic-colors--danger-100"], evidence_from=MKT, selector=":root", prop="--base-color-semantic-colors--danger-100"),
                "danger-20": color(M["--base-color-semantic-colors--danger-20"], evidence_from=MKT, selector=":root", prop="--base-color-semantic-colors--danger-20"),
                "info-100": color(M["--base-color-semantic-colors--info-100"], evidence_from=MKT, selector=":root", prop="--base-color-semantic-colors--info-100"),
                "info-20": color(M["--base-color-semantic-colors--info-20"], evidence_from=MKT, selector=":root", prop="--base-color-semantic-colors--info-20"),
            },
            "accent": {
                "100": color(M["--base-color-accent--accent-100"], evidence_from=MKT, selector=":root", prop="--base-color-accent--accent-100"),
                "120": color(M["--base-color-accent--accent-120"], evidence_from=MKT, selector=":root", prop="--base-color-accent--accent-120"),
                "screen-green": color(M["--base-color-accent--screen-green"], evidence_from=MKT, selector=":root", prop="--base-color-accent--screen-green"),
                "feedback-yellow": color(M["--base-color-accent--feedback-yellow"], evidence_from=MKT, selector=":root", prop="--base-color-accent--feedback-yellow"),
                "blueprint": color(M["--base-color-accent--blueprint"], evidence_from=MKT, selector=":root", prop="--base-color-accent--blueprint"),
            },
        },
        "font": {
            "family": {
                "display": font("Abcfavoritvariable, Arial, sans-serif", evidence_from=MKT, selector=":root", prop="--_typography---display-font"),
                "body": font('"Inter hosted", sans-serif', evidence_from=MKT, selector=":root", prop="--_typography---body-font"),
                "content": font('"Abcfavoritmono Book"', evidence_from=MKT, selector=":root", prop="--_typography---content-font"),
                "highlight": font("Martinaplantijn, Georgia, sans-serif", evidence_from=MKT, selector=":root", prop="--_typography---highlight-font"),
                "login-heading": font("'ABC Favorit', Helvetica, Arial, sans-serif", evidence_from=LOGIN, selector=":root", prop="--hop-font-family-primary"),
                "login-body": font("'Inter', Helvetica, Arial, sans-serif", evidence_from=LOGIN, selector=":root", prop="--hop-font-family-secondary"),
                "login-mono": font("'ABC Favorit Mono', Consolas, 'SF Mono', monospace", evidence_from=LOGIN, selector=":root", prop="--hop-font-family-tertiary"),
            }
        },
        "fontWeight": {
            "regular": num(400, "fontWeight", evidence_from=MKT, selector=":root", prop="--_typography---paragraph-body--font-weight"),
            "medium": num(500, "fontWeight", evidence_from=MKT, selector=":root", prop="--_components---button--font-weight"),
            "login-book": num(410, "fontWeight", evidence_from=LOGIN, selector=":root", prop="--hop-font-weight-410"),
            "login-medium": num(505, "fontWeight", evidence_from=LOGIN, selector=":root", prop="--hop-font-weight-505"),
            "login-heading": num(580, "fontWeight", evidence_from=LOGIN, selector=":root", prop="--hop-font-weight-580"),
            "login-semibold": num(590, "fontWeight", evidence_from=LOGIN, selector=":root", prop="--hop-font-weight-590"),
            "login-display": num(680, "fontWeight", evidence_from=LOGIN, selector=":root", prop="--hop-font-weight-680", note="computed font-weight on login h1.o-ui-heading-md was 680"),
            "login-bold": num(690, "fontWeight", evidence_from=LOGIN, selector=":root", prop="--hop-font-weight-690"),
        },
        "typography": {
            "display": typography({
                "fontFamily": "{font.family.display}",
                "fontSize": "clamp(3.5rem, 2.7857rem + 3.5714vw, 6rem)",
                "fontWeight": "{fontWeight.regular}",
                "lineHeight": 1,
                "letterSpacing": "-0.05em",
            }, evidence_from=MKT, selector=".heading-style-h0", prop="font-size", note="line-height and letter-spacing from --_typography---h0--*; computed at 1169px was 84.7497px / -4.23749px"),
            "h1": typography({
                "fontFamily": "{font.family.display}",
                "fontSize": "clamp(3rem, 2.7143rem + 1.4286vw, 4rem)",
                "fontWeight": "{fontWeight.regular}",
                "lineHeight": 1,
                "letterSpacing": "-0.05em",
            }, evidence_from=MKT, selector=".heading-style-h1", prop="font-size", note="computed at 1169px was 58.5983px, line-height 58.5983px, letter-spacing -2.92991px, color #171417"),
            "h2": typography({
                "fontFamily": "{font.family.display}",
                "fontSize": "clamp(2rem, 1.7143rem + 1.4286vw, 3rem)",
                "fontWeight": "{fontWeight.regular}",
                "lineHeight": 1.1,
                "letterSpacing": "-0.02em",
            }, evidence_from=MKT, selector=".heading-style-h2", prop="font-size", note="computed at 1169px was 43.1623px / 47.4785px / -0.863246px"),
            "h3": typography({
                "fontFamily": "{font.family.display}",
                "fontSize": "clamp(1.75rem, 1.5357rem + 1.0714vw, 2.5rem)",
                "fontWeight": "{fontWeight.regular}",
                "lineHeight": 1.1,
                "letterSpacing": "-0.02em",
            }, evidence_from=MKT, selector=".heading-style-h3", prop="font-size", note="computed at 1169px was 36.2297px"),
            "h4": typography({
                "fontFamily": "{font.family.display}",
                "fontSize": "clamp(1.5rem, 1.3571rem + 0.7143vw, 2rem)",
                "fontWeight": "{fontWeight.regular}",
                "lineHeight": 1.1,
                "letterSpacing": "-0.02em",
            }, evidence_from=MKT, selector=".heading-style-h4", prop="font-size", note="computed at 1169px was 29.2984px"),
            "h5": typography({
                "fontFamily": "{font.family.display}",
                "fontSize": "clamp(1.25rem, 1.1786rem + 0.3571vw, 1.5rem)",
                "fontWeight": "{fontWeight.regular}",
                "lineHeight": 1.1,
                "letterSpacing": "-0.02em",
            }, evidence_from=MKT, selector=".heading-style-h5", prop="font-size", note="computed at 1169px was 22.3674px"),
            "body": typography({
                "fontFamily": "{font.family.body}",
                "fontSize": "1rem",
                "fontWeight": "{fontWeight.regular}",
                "lineHeight": 1.4,
                "letterSpacing": "0px",
            }, evidence_from=MKT, selector=":root", prop="--_typography---paragraph-body--font-size", note="computed .text-size-regular at 1169px was 15.436px / 21.6104px, color #171417"),
            "body-md": typography({
                "fontFamily": "{font.family.body}",
                "fontSize": "clamp(1rem, 0.9286rem + 0.3571vw, 1.25rem)",
                "fontWeight": "{fontWeight.regular}",
                "lineHeight": 1.4,
                "letterSpacing": "0px",
            }, evidence_from=MKT, selector=":root", prop="--_typography---paragraph-md--font-size"),
            "body-sm": typography({
                "fontFamily": "{font.family.body}",
                "fontSize": "0.875rem",
                "fontWeight": "{fontWeight.regular}",
                "lineHeight": 1.4,
                "letterSpacing": "0px",
            }, evidence_from=MKT, selector=":root", prop="--_typography---paragraph-sm--font-size", note="computed .text-size-small at 1169px was 13.5065px / 18.9091px"),
            "caption": typography({
                "fontFamily": "{font.family.body}",
                "fontSize": "0.75rem",
                "fontWeight": "{fontWeight.regular}",
                "lineHeight": 1.4,
                "letterSpacing": "0px",
            }, evidence_from=MKT, selector=":root", prop="--_typography---paragraph-xsm--font-size", note="computed .text-size-xsmall at 1169px was 11.577px / 16.2078px"),
            "button": typography({
                "fontFamily": "{font.family.body}",
                "fontSize": "1rem",
                "fontWeight": "{fontWeight.medium}",
                "lineHeight": "1.1em",
                "letterSpacing": "0px",
            }, evidence_from=MKT, selector=":root", prop="--_components---button--font-size", note="computed a.button.is-small at 1169px was 11.577px / weight 500; the 1rem token is the default .button rule"),
            "login-heading": typography({
                "fontFamily": "{font.family.login-heading}",
                "fontSize": "1.25rem",
                "fontWeight": "{fontWeight.login-heading}",
                "lineHeight": 1.2,
            }, evidence_from=LOGIN, selector=":root", prop="--hop-heading-md-font-size", note="computed h1.o-ui-heading-md was 24px / 32px / weight 680, which matches heading-lg more closely than heading-md"),
            "login-body": typography({
                "fontFamily": "{font.family.login-body}",
                "fontSize": "1rem",
                "fontWeight": "{fontWeight.login-book}",
                "lineHeight": 1.5,
            }, evidence_from=LOGIN, selector=":root", prop="--hop-body-md-font-size", note="computed label.o-ui-text-md was 16px / 24px / weight 410"),
        },
        "radius": {
            "none": dim("0px", evidence_from=MKT, selector=":root", prop="--_components---card--border-radius", note="declared 0px"),
            "tiny": dim("0.25rem", evidence_from=MKT, selector=":root", prop="--border-radius--border-radius-tiny"),
            "xxs": dim("0.5rem", evidence_from=MKT, selector=":root", prop="--border-radius--border-radius-xxs"),
            "xs": dim("0.75rem", evidence_from=MKT, selector=":root", prop="--border-radius--border-radius-xs"),
            "sm": dim("1rem", evidence_from=MKT, selector=":root", prop="--border-radius--border-radius-sm"),
            "md": dim("1.5rem", evidence_from=MKT, selector=":root", prop="--border-radius--border-radius-m", note="computed .pricing-card border-radius was 24px, which is 1.5rem at 16px and 23.154px at the marketing root"),
            "full": dim("100px", evidence_from=MKT, selector=":root", prop="--_components---button--border-radius", note="computed a.button.is-small border-radius was 100px"),
            "login-sm": dim("0.25rem", evidence_from=LOGIN, selector=":root", prop="--hop-shape-rounded-sm"),
            "login-md": dim("0.5rem", evidence_from=LOGIN, selector=":root", prop="--hop-shape-rounded-md"),
            "login-lg": dim("1rem", evidence_from=LOGIN, selector=":root", prop="--hop-shape-rounded-lg", note="computed login card radius was 16px"),
            "login-pill": dim("1.5rem", evidence_from=LOGIN, selector=":root", prop="--hop-shape-pill", note="computed login button and field radius was 24px"),
        },
        "spacing": {
            "0": dim("0rem", evidence_from=MKT, selector=":root", prop="--_size---0rem"),
            "xs": dim("0.5em", evidence_from=MKT, selector=":root", prop="--_layout---spacing--margin-xs"),
            "sm": dim("1em", evidence_from=MKT, selector=":root", prop="--_layout---spacing--margin-sm"),
            "md": dim("2em", evidence_from=MKT, selector=":root", prop="--_layout---spacing--margin-md"),
            "lg": dim("3em", evidence_from=MKT, selector=":root", prop="--_layout---spacing--margin-lg"),
            "xl": dim("6em", evidence_from=MKT, selector=":root", prop="--_layout---spacing--margin-xl"),
            "size-2": dim("0.125rem", evidence_from=MKT, selector=":root", prop="--_size---0-125rem"),
            "size-4": dim("0.25rem", evidence_from=MKT, selector=":root", prop="--_size---0-25rem"),
            "size-8": dim("0.5rem", evidence_from=MKT, selector=":root", prop="--_size---0-5rem"),
            "size-12": dim("0.75rem", evidence_from=MKT, selector=":root", prop="--_size---0-75rem"),
            "size-16": dim("1rem", evidence_from=MKT, selector=":root", prop="--_size---1rem"),
            "size-24": dim("1.5rem", evidence_from=MKT, selector=":root", prop="--_size---1-5rem"),
            "size-32": dim("2rem", evidence_from=MKT, selector=":root", prop="--_size---2rem"),
            "size-40": dim("2.5rem", evidence_from=MKT, selector=":root", prop="--_size---2-5rem"),
            "login-80": dim("0.5rem", evidence_from=LOGIN, selector=":root", prop="--hop-space-80"),
            "login-160": dim("1rem", evidence_from=LOGIN, selector=":root", prop="--hop-space-160", note="computed login button padding was 0px 16px; field padding was 8px 16px"),
            "login-240": dim("1.5rem", evidence_from=LOGIN, selector=":root", prop="--hop-space-240"),
            "login-320": dim("2rem", evidence_from=LOGIN, selector=":root", prop="--hop-space-320"),
        },
        "layout": {
            "container": dim("80rem", evidence_from=MKT, selector=":root", prop="--_layout---container--max-width"),
            "container-lg": dim("95rem", evidence_from=MKT, selector=":root", prop="--_layout---container-lg--max-width"),
            "container-sm": dim("50rem", evidence_from=MKT, selector=":root", prop="--_layout---container-sm--max-width"),
        },
        "motion": {
            "duration": {
                "100": duration("100ms", evidence_from=LOGIN, selector=":root", prop="--hop-easing-duration-1"),
                "200": duration("200ms", evidence_from=LOGIN, selector=":root", prop="--hop-easing-duration-2"),
                "300": duration("300ms", evidence_from=LOGIN, selector=":root", prop="--hop-easing-duration-3", note="computed a.button transition-duration was 0.3s"),
                "400": duration("400ms", evidence_from=ELEM, selector=".footer_link--social", prop="transition-duration", note="computed 0.4s on the marketing footer social link"),
                "500": duration("500ms", evidence_from=LOGIN, selector=":root", prop="--hop-easing-duration-4"),
                "800": duration("800ms", evidence_from=LOGIN, selector=":root", prop="--hop-easing-duration-5"),
            },
            "easing": {
                "productive": num([0.22, 0.61, 0.36, 1], "cubicBezier", evidence_from=LOGIN, selector=":root", prop="--hop-easing-productive", note="declared cubic-bezier(0.22, 0.61, 0.36, 1)"),
                "focus": num([0.46, 0.03, 0.52, 0.96], "cubicBezier", evidence_from=LOGIN, selector=":root", prop="--hop-easing-focus", note="declared cubic-bezier(0.46, 0.03, 0.52, 0.96)"),
                "button": num([0.25, 0.46, 0.45, 0.94], "cubicBezier", evidence_from=ELEM, selector="a.button", prop="transition-timing-function", note="computed cubic-bezier(0.25, 0.46, 0.45, 0.94)"),
            },
        },
        "elevation": {
            "login-raised": shadow(H["--hop-elevation-raised"], evidence_from=LOGIN, selector=":root", prop="--hop-elevation-raised"),
            "login-lifted": shadow(H["--hop-elevation-lifted"], evidence_from=LOGIN, selector=":root", prop="--hop-elevation-lifted"),
            "login-floating": shadow(H["--hop-elevation-floating"], evidence_from=LOGIN, selector=":root", prop="--hop-elevation-floating"),
            "pricing-card": shadow("0px 4px 8px 0px rgba(37, 69, 255, 0.1), 0px 12px 24px 0px rgba(37, 58, 177, 0.05), 0px 32px 40px 0px rgba(37, 58, 177, 0.05)", evidence_from=ELEM, selector=".pricing-card", prop="box-shadow", note="computed on https://workleap.com/pricing"),
            "login-card": shadow("0px 4px 8px 0px rgba(37, 69, 255, 0.1), 0px 12px 24px 0px rgba(37, 58, 177, 0.05), 0px 32px 40px 0px rgba(37, 58, 177, 0.05)", evidence_from=ELEM, selector="login card", prop="box-shadow"),
        },
    }
    # fix color() calls that used ** wrong for brand.leapin - already passed kwargs correctly except first. verify later.

    light = {
        "background": {
            "page": color("#ffffff", evidence_from=ELEM, selector="body", prop="background-color", note="https://workleap.com/officevibe"),
            "surface": color(M["--background-color--bg-light"], evidence_from=MKT, selector=":root", prop="--background-color--bg-light", note="computed nav product panel was rgb(249, 248, 246)"),
            "soft": color(M["--background-color--bg-soft"], evidence_from=MKT, selector=":root", prop="--background-color--bg-soft"),
            "inverse": color(M["--background-color--bg-dark"], evidence_from=MKT, selector=":root", prop="--background-color--bg-dark", note="computed footer.footer_main was rgb(12, 23, 84)"),
            "action": color(M["--background-color--bg-brand-default"], evidence_from=MKT, selector=":root", prop="--background-color--bg-brand-default", note="computed a.button.is-small was rgb(37, 69, 255)"),
            "card": color("#ffffff", evidence_from=ELEM, selector=".pricing-card", prop="background-color"),
            "login-page": color("#f8f6f3", evidence_from=ELEM, selector="html", prop="background-color", note="https://login.workleap.com/"),
            "login-card": color("#ffffff", evidence_from=ELEM, selector="login card", prop="background-color"),
            "popular": color("#ffc13a", evidence_from=ELEM, selector=".pricing-card_popular-header", prop="background-color", note="matches --base-color-accent--feedback-yellow"),
        },
        "text": {
            "primary": color(M["--content-colors--content-default"], evidence_from=MKT, selector=":root", prop="--content-colors--content-default", note="computed body color was rgb(23, 20, 23)"),
            "secondary": color(M["--content-colors--content-light"], evidence_from=MKT, selector=":root", prop="--content-colors--content-light"),
            "muted": color(M["--content-colors--content-extralight"], evidence_from=MKT, selector=":root", prop="--content-colors--content-extralight"),
            "medium": color(M["--content-colors--content-medium"], evidence_from=MKT, selector=":root", prop="--content-colors--content-medium"),
            "on-accent": color("#ffffff", evidence_from=ELEM, selector="a.button.is-small", prop="color"),
            "on-inverse": color(M["--base-color-greyscale--grey-00"], evidence_from=ELEM, selector="footer.footer_main", prop="color", note="computed rgb(249, 248, 246), same as --base-color-greyscale--grey-00"),
            "link": color(M["--content-colors--content-brand-default"], evidence_from=MKT, selector=":root", prop="--content-colors--content-brand-default"),
            "nav": color("#222222", evidence_from=ELEM, selector="a.navbar_link", prop="color"),
            "login-primary": color(H["--hop-neutral-text"], evidence_from=LOGIN, selector=":root", prop="--hop-neutral-text", note="computed h1 and input color was rgb(60, 60, 60)"),
            "login-muted": color(H["--hop-neutral-text-weak"], evidence_from=LOGIN, selector=":root", prop="--hop-neutral-text-weak", note="computed label was rgb(108, 108, 107), which is not this token"),
            "login-link": color(H["--hop-primary-text"], evidence_from=LOGIN, selector=":root", prop="--hop-primary-text", note="computed link color was rgb(59, 87, 255)"),
            "success": color(M["--base-color-semantic-colors--success-100"], evidence_from=MKT, selector=":root", prop="--base-color-semantic-colors--success-100"),
            "warning": color(M["--base-color-semantic-colors--warning-100"], evidence_from=MKT, selector=":root", prop="--base-color-semantic-colors--warning-100"),
            "danger": color(M["--base-color-semantic-colors--danger-100"], evidence_from=MKT, selector=":root", prop="--base-color-semantic-colors--danger-100"),
            "info": color(M["--base-color-semantic-colors--info-100"], evidence_from=MKT, selector=":root", prop="--base-color-semantic-colors--info-100"),
        },
        "border": {
            "stroke": color(M["--base-color-greyscale--grey-20"], evidence_from=MKT, selector=":root", prop="--base-color-greyscale--grey-20"),
            "strong": color(M["--base-color-greyscale--grey-60"], evidence_from=MKT, selector=":root", prop="--base-color-greyscale--grey-60"),
            "action": color(M["--brand-color-palette--leapin-blue"], evidence_from=ELEM, selector="a.button.is-secondary", prop="border-top-color", note="computed width 2px"),
            "input": color("#a2a2a2", evidence_from=ELEM, selector="input[name=firstname] on /demo", prop="border-top-color", note="computed width 1px; matches grey-40"),
            "focus": color("#2545ff", evidence_from=ELEM, selector="a.button:focus", prop="outline-color", note="computed outline was rgb(37, 69, 255) auto 3px, offset 0px"),
            "login": color(H["--hop-neutral-border"], evidence_from=LOGIN, selector=":root", prop="--hop-neutral-border"),
            "login-focus": color(H["--hop-primary-border-focus"], evidence_from=LOGIN, selector=":root", prop="--hop-primary-border-focus", note="computed focused field wrapper border was rgb(59, 87, 255) 1px"),
        },
        "component": {
            "button": {
                "bg": color("{background.action}", evidence_from=MKT, selector=".button", prop="background-color"),
                "text": color("{text.on-accent}", evidence_from=MKT, selector=".button", prop="color"),
                "radius": dim("{radius.full}", evidence_from=MKT, selector=".button", prop="border-radius"),
                "padding": dim("0.7em", evidence_from=MKT, selector=":root", prop="--_components---button--vertical-padding", note="horizontal padding token is 2em; computed is-small padding was 7.718px 23.154px and height 32px"),
                "height": dim("32px", evidence_from=ELEM, selector="a.button.is-small", prop="height", note="default .button height was not isolated; a full-size secondary on the page was 43px"),
            },
            "button-secondary": {
                "bg": color("rgba(0, 0, 0, 0)", evidence_from=ELEM, selector="a.button.is-secondary", prop="background-color"),
                "text": color("{text.link}", evidence_from=ELEM, selector="a.button.is-secondary", prop="color"),
                "radius": dim("{radius.full}", evidence_from=ELEM, selector="a.button.is-secondary", prop="border-radius"),
            },
            "field": {
                "bg": color("#ffffff", evidence_from=ELEM, selector="input[name=firstname] on /demo", prop="background-color"),
                "text": color("#484747", evidence_from=ELEM, selector="input[name=firstname] on /demo", prop="color"),
                "radius": dim("100rem", evidence_from=MKT, selector=":root", prop="--border-radius--border-radius-full", note="computed radius was 1543.6px, the used value of 100rem at html 15.436px"),
                "height": dim("46px", evidence_from=ELEM, selector="input[name=firstname] on /demo", prop="height"),
                "padding": dim("11.577px", evidence_from=ELEM, selector="input[name=firstname] on /demo", prop="padding-top", note="padding was 11.577px 15.436px at html 15.436px, which is 0.75rem 1rem"),
            },
            "login-button": {
                "bg": color("#2545ff", evidence_from=ELEM, selector="button.o-ui-button-primary", prop="background-color", note="declared --hop-primary-surface-strong is #4767fe; the painted button was #2545ff"),
                "text": color("#f9f8f6", evidence_from=ELEM, selector="button.o-ui-button-primary", prop="color"),
                "radius": dim("{radius.login-pill}", evidence_from=ELEM, selector="button.o-ui-button-primary", prop="border-radius"),
                "height": dim("46px", evidence_from=ELEM, selector="button.o-ui-button-primary", prop="height"),
                "padding": dim("16px", evidence_from=ELEM, selector="button.o-ui-button-primary", prop="padding-left"),
            },
            "login-field": {
                "bg": color("#ffffff", evidence_from=ELEM, selector="input[name=username]", prop="background-color"),
                "text": color("{text.login-primary}", evidence_from=ELEM, selector="input[name=username]", prop="color"),
                "radius": dim("{radius.login-pill}", evidence_from=ELEM, selector="input[name=username]", prop="border-radius"),
                "height": dim("46px", evidence_from=ELEM, selector="input[name=username]", prop="height"),
            },
            "card": {
                "bg": color("{background.card}", evidence_from=ELEM, selector=".pricing-card", prop="background-color"),
                "radius": dim("{radius.md}", evidence_from=ELEM, selector=".pricing-card", prop="border-radius"),
            },
            "nav": {
                "bg": color("#ffffff", evidence_from=ELEM, selector=".navbar_component", prop="background-color"),
                "height": dim("58px", evidence_from=ELEM, selector=".navbar_component", prop="height", note="padding 0px 58.4453px at 1169px"),
            },
        },
    }
    doc = {
        "$description": "Officevibe public marketing and signed-out Workleap login, measured 2026-11-19. Marketing tokens are the Workleap site custom properties. Login tokens are the Hop design system on login.workleap.com. No dark theme was served on these pages.",
        "core": core,
        "light": light,
        "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    }
    return inherit_labels(doc)


def check(doc):
    problems = []
    def walk(node, path):
        if not isinstance(node, dict):
            return
        if "$value" in node:
            if "$type" not in node:
                problems.append(f"{path} has $value without $type")
            ext = node.get("$extensions", {}).get("source", {})
            if ext.get("evidence") not in ("Measured", "Reconstruction"):
                problems.append(f"{path} has no evidence label")
            elif ext.get("evidence") == "Measured" and ext.get("from") == ELEM:
                problems.append(f"{path} is labelled Measured but cites a computed style raw/ does not hold")
            if node.get("$type") == "dimension" and str(node["$value"]).endswith(("ms", "s")) and not str(node["$value"]).endswith("rems"):
                problems.append(f"{path} is a duration typed dimension")
            return
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, f"{path}.{k}" if path else k)
    walk(doc, "")
    if problems:
        raise SystemExit("token check failed:\n  " + "\n  ".join(problems))


def main():
    doc = build()
    check(doc)
    OUT.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
