#!/usr/bin/env python3
"""Build tokens.json from the Overflow capture readings.

Sources (all measured, none invented):
  raw/app-vars.json       custom properties resolved on body at overflow.io/n/signin
  raw/deep.json           computed styles of marketing and sign-in elements
  raw/focus-visible.json  CSS.forcePseudoState focus-visible on the header primary button
  raw/pricing-bits.json   active nav, plan card
  raw/signup.json         sign-up fields (looked at, never submitted)

Marketing pages declare almost no custom properties. Their values are computed
styles. The signed-out app shell (overflow.io/n/*) declares 257 custom
properties on body; those become the app.* groups. There is no dark theme:
prefers-color-scheme: dark left both surfaces painted light.

Deterministic: same readings, same bytes.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"

APP = json.loads((RAW / "app-vars.json").read_text())["resolved"]
DEEP = json.loads((RAW / "deep.json").read_text())
FOCUS = json.loads((RAW / "focus-visible.json").read_text())
PRICE = json.loads((RAW / "pricing-bits.json").read_text())

SRC_APP = "computed custom property on body, overflow.io/n/signin, 1440x900, 2026-11-19"
SRC_MKT = "computed style, overflow.io marketing, 1440x900, 2026-11-19"


def hex_of(value: str) -> str:
    value = value.strip()
    if value.startswith("#"):
        h = value[1:]
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        return "#" + h.lower()
    return value


def hex_rgb(value: str) -> str:
    """rgb(0, 95, 204) as #005fcc."""
    parts = value.strip()[value.index("(") + 1:-1].split(",")
    return "#%02x%02x%02x" % tuple(int(p) for p in parts[:3])


def color(value, source):
    return {"$value": hex_of(value) if value.startswith("#") else value, "$type": "color",
            "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def duration(value, source):
    return {"$value": value, "$type": "duration", "$extensions": {"source": source}}


UA_RING = ("Chromium's default focus ring, not Overflow's: the forced focus-visible outline is "
           "outline-style auto (raw/focus-visible.json outline {}), and the product sets no focus colour. "
           "Observed; do not ship it as a brand value.")


def ua_default(token):
    """A value the browser drew, not the product (finding 16-9)."""
    token["$extensions"]["evidence"] = "Observed"
    token["$extensions"]["source"] = UA_RING.format(FOCUS["outline"]) + " " + token["$extensions"]["source"]
    return token


def by_hand(token):
    """A value typed in at capture time that no file in raw/ holds (docs/EVIDENCE.md: Reconstruction)."""
    token["$extensions"]["evidence"] = "Reconstruction"
    token["$extensions"]["source"] += ". Entered by hand at capture time; no file in raw/ holds this reading."
    return token


def num(value, source):
    return {"$value": value, "$type": "number", "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def text_style(family, size, weight, line, tracking, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
            "letterSpacing": tracking,
        },
        "$extensions": {"source": source},
    }


def shadow(value, source):
    return {"$value": value, "$type": "shadow", "$extensions": {"source": source}}


def cubic(value, source):
    # value is "cubic-bezier(a, b, c, d)" or a keyword
    inner = value
    if value.startswith("cubic-bezier("):
        inner = value[len("cubic-bezier("):-1]
        parts = [float(p) for p in inner.split(",")]
        return {"$value": parts, "$type": "cubicBezier", "$extensions": {"source": source}}
    return {"$value": value, "$type": "other", "$extensions": {"source": source, "notTokenised": "keyword easing, not a cubic-bezier"}}


def build():
    """The token document, built in memory from raw/; main() writes it."""
    home = DEEP["pages"]["home"]
    signin = DEEP["pages"]["signin"]
    h1 = home["h1"]
    nav = home["navLink"]
    hero_btn = home["downloadHero"]
    footer_link = home["footerLink"]
    email = home["emailInput"]
    cookie = home["cookieLink"]
    sections = {s["cls"].split()[1] if "site-section--" in s["cls"] else s["cls"].split()[-1]: s
                for s in DEEP["pages"]["homeHero"]}

    app_colors = {}
    for name, value in sorted(APP.items()):
        if not name.startswith("--color-"):
            continue
        key = name[len("--color-"):]
        app_colors[key] = color(value, f"{SRC_APP}; {name}")

    app_shadows = {}
    for name, value in sorted(APP.items()):
        if name.startswith("--shadow-"):
            app_shadows[name[len("--shadow-"):]] = shadow(value, f"{SRC_APP}; {name}")

    app_font = {}
    for name, value in sorted(APP.items()):
        if not name.startswith("--font-"):
            continue
        key = name[len("--font-"):]
        if name.startswith("--font-family"):
            app_font[key] = font(value, f"{SRC_APP}; {name}")
        elif "letterSpacing" in name or "lineHeight" in name or name.startswith("--font-size"):
            app_font[key] = dim(value, f"{SRC_APP}; {name}")
        elif "weight" in name:
            weight = int(value) if value.isdigit() else value
            app_font[key] = num(weight, f"{SRC_APP}; {name}")

    app_motion = {}
    for name, value in sorted(APP.items()):
        if not name.startswith("--animation-"):
            continue
        key = name[len("--animation-"):]
        if value.endswith("ms"):
            app_motion[key] = duration(value, f"{SRC_APP}; {name}")
        elif value.startswith("cubic-bezier("):
            app_motion[key] = cubic(value, f"{SRC_APP}; {name}")
        else:
            app_motion[key] = {"$value": value, "$type": "other",
                               "$extensions": {"source": f"{SRC_APP}; {name}",
                                               "notTokenised": "keyword easing or named timing, kept as declared"}}

    # Marketing type styles from computed elements.
    inter = '{font.family.inter}'
    marketing_type = {
        "display": text_style(inter, h1["fontSize"], 800, h1["lineHeight"], h1["letterSpacing"],
                              f"{SRC_MKT}; h1.intro-section__title"),
        "section": by_hand(text_style(inter, "48px", 800, "55.68px", "-0.8px",
                                      f"{SRC_MKT}; features h2 Syncing")),
        "card-title": by_hand(text_style(inter, "40px", 800, "24px", "-0.5px",
                                         f"{SRC_MKT}; pricing h2 Pro (line-height 24px is the computed value, shorter than the size)")),
        "eyebrow": by_hand(text_style(inter, "14px", 700, "16.24px", "1px",
                                      f"{SRC_MKT}; footer/menu h3 OVERFLOW")),
        "nav": text_style(inter, nav["fontSize"], 400, nav["lineHeight"], "0px",
                          f"{SRC_MKT}; header a.nav-link"),
        "body": text_style(inter, "16px", 400, "28px", "0px",
                           f"{SRC_MKT}; body"),
        "footer-link": text_style(inter, footer_link["fontSize"], 400, footer_link["lineHeight"], "0px",
                                  f"{SRC_MKT}; a.footer-nav__link"),
        "button": text_style(inter, hero_btn["fontSize"], 550, hero_btn["lineHeight"], hero_btn["letterSpacing"],
                             f"{SRC_MKT}; a.btn.btn-primary in .intro-section"),
        "button-nav": text_style(inter, "15px", 550, "16px", "0.2px",
                                 f"{SRC_MKT}; header a.btn-primary"),
        "cookie": text_style(inter, "15px", 550, "24px", "0.2px",
                             f"{SRC_MKT}; button.btn-xs"),
    }
    app_type = {}
    for scale in ("h1", "h2", "h3", "h4", "h5", "h6", "p1", "p2", "small"):
        app_type[scale] = text_style(
            "{font.family.interVar}",
            f"{{font.size-{scale}}}",
            f"{{font.weight-{scale}}}",
            f"{{font.lineHeight-{scale}}}",
            f"{{font.letterSpacing-{scale}}}",
            f"{SRC_APP}; --font-size/weight/lineHeight/letterSpacing-{scale} composed",
        )

    tokens = {
        "$schema": "https://www.designtokens.org/schemas/2025.10/format.json",
        "core": {
            "font": {
                "family": {
                    "inter": font('Inter, "Helvetica Neue", Arial, "Noto Sans", sans-serif',
                                  f"{SRC_MKT}; body font-family"),
                    "interVar": font(APP["--font-family-body"], f"{SRC_APP}; --font-family-body"),
                },
                **{k: v for k, v in app_font.items() if k != "family-body"},
            },
            "color": {
                "ink": color("#000000", f"{SRC_MKT}; body color rgb(0, 0, 0)"),
                "paper": color("#ffffff", f"{SRC_MKT}; body background-color rgb(255, 255, 255)"),
                "hero-text": color("#ffffff", f"{SRC_MKT}; h1.intro-section__title color"),
                "navy": color("#161637", f"{SRC_MKT}; menu h4 color rgb(22, 22, 55); also --color-launcher-logo-text and --color-purple170"),
                "eyebrow": by_hand(color("#acacbc", f"{SRC_MKT}; h3 color rgb(172, 172, 188)")),
                "footer-link": color("rgba(0, 0, 0, 0.6)", f"{SRC_MKT}; a.footer-nav__link color"),
                "link": color("#0085e4", f"{SRC_MKT}; cookie-statement link rgb(0, 133, 228); stylesheet a:hover #0085e4"),
                "link-hover": color("#259aef", "declared a:hover in public-site-v2.min.css; not a resting computed style"),
                "gray-light": color("#fafafc", f"{SRC_MKT}; .site-section--gray-light background"),
                "gray-dark": color("#f2f2f4", f"{SRC_MKT}; .site-section--gray-dark background"),
                "cookie-secondary": by_hand(color("#f0f0f2", f"{SRC_MKT}; button.btn-secondary background")),
                "cookie-secondary-hover": color("#e8e8ea", "declared .btn-secondary:hover in public-site-v2.min.css"),
                "field": color("rgba(0, 0, 0, 0.04)", f"{SRC_MKT}; input.form-control background"),
                "field-border": color("#e8e8ea", f"{SRC_MKT}; input.form-control border-top-color"),
                "field-focus": color("#149bfe", "declared .form-control:focus border-color and box-shadow in public-site-v2.min.css"),
                "theme": color("#232d41", "meta theme-color on marketing pages; also --color-brand-blue"),
                "auth-panel": color("#d6f3ff", "computed .authpanel background rgb(214, 243, 255), overflow.io/n/signin"),
                "auth-text": color("#2a2d32", f"{SRC_APP} body color rgb(42, 45, 50); --color-text is #36383b"),
                "focus-ring": ua_default(color(hex_rgb(FOCUS["outlineColor"]), "CSS.forcePseudoState focus-visible on header a.btn-primary; outline-color rgb(0, 95, 204)")),
            },
            "radius": {
                "button": dim("8px", f"{SRC_MKT}; .btn border-radius"),
                "field": dim("8px", f"{SRC_MKT}; input.form-control border-radius"),
                "card": dim("24px", "computed .card on /pricing/, border-radius 24px"),
                "price-header": dim("7px", "computed .price-box__header border-radius 7px 7px 0 0"),
                "app-control": dim("6px", "computed sign-in input and button border-radius"),
                "app-textbutton": dim("3px", "computed a.textbutton border-radius"),
            },
            "spacing": {
                "header": dim("96px", f"{SRC_MKT}; header height"),
                "header-mobile": dim("77px", "computed header height at 390px"),
                "nav-pad-y": dim(nav["paddingTop"], f"{SRC_MKT}; a.nav-link padding-top"),
                "nav-pad-x": dim(nav["paddingRight"], f"{SRC_MKT}; a.nav-link padding-right"),
                "button-pad-y": dim(hero_btn["paddingTop"], f"{SRC_MKT}; hero .btn-primary padding-top"),
                "button-pad-x": dim(hero_btn["paddingLeft"], f"{SRC_MKT}; hero .btn-primary padding-left"),
                "button-nav-y": dim("15px", f"{SRC_MKT}; header a.btn-primary padding-top"),
                "field-pad": dim(email["paddingTop"], f"{SRC_MKT}; input.form-control padding"),
                "section": dim("156px", f"{SRC_MKT}; .site-section--tabs-presentation padding-top"),
                "hero-pad-top": dim("96px", f"{SRC_MKT}; .intro-section padding-top"),
                "footer-pad-top": dim("128px", f"{SRC_MKT}; footer padding-top"),
                "app-control-x": dim("32px", "computed sign-in button padding-left"),
                "app-field-y": dim("7px", "computed sign-in input padding-top"),
                "app-field-x": dim("11px", "computed sign-in input padding-left"),
                "app-panel": dim("485px", "computed .authpanel width at 1440"),
            },
            "size": {
                "button-hero": dim(hero_btn["height"], f"{SRC_MKT}; hero .btn-primary height"),
                "button-nav": dim("48px", f"{SRC_MKT}; header a.btn-primary height"),
                "field": dim(email["height"], f"{SRC_MKT}; input.form-control height"),
                "app-control": dim("40px", "computed sign-in input and button height"),
                "app-button-s": dim("32px", "computed .download-button height"),
            },
            "typography": {
                **marketing_type,
                **{f"app-{k}": v for k, v in app_type.items()},
            },
            "shadow": {
                "plan-card": shadow("0px 4px 16px -8px rgba(0, 0, 0, 0.08)",
                                    "computed .card box-shadow on /pricing/"),
                "app-button": shadow("0px 0px 0px 1px rgba(0, 0, 0, 0.04), 0px 1px 2px 0px rgba(0, 0, 0, 0.12)",
                                     "computed sign-in button box-shadow"),
                "app-button-hover": shadow("0px 0px 0px 1px rgba(0, 0, 0, 0.04), 0px 2px 6px -1px rgba(0, 0, 0, 0.16)",
                                           "computed .download-button:hover and .google-btn:hover box-shadow"),
                **{f"app-{k}": v for k, v in app_shadows.items()},
            },
            "motion": app_motion,
        },
        "light": {
            "background": {
                "page": color("{color.paper}", f"{SRC_MKT}; body background"),
                "surface": color("{color.paper}", "plan card and header surface"),
                "sunken": color("{color.gray-light}", f"{SRC_MKT}; .site-section--gray-light"),
                "band": color("{color.gray-dark}", f"{SRC_MKT}; .site-section--gray-dark"),
                "action": color("{color.ink}", f"{SRC_MKT}; .btn-primary background"),
                "action-secondary": color("{color.cookie-secondary}", f"{SRC_MKT}; .btn-secondary background"),
                "auth-panel": color("{color.auth-panel}", "computed .authpanel"),
                "auth-page": color("{color.paper}", f"{SRC_APP} body background"),
                "app-action": color("#0071db", "computed .download-button background rgb(0, 113, 219); matches --color-primary and --color-blue100"),
                "app-action-hover": color("#0065c5", "computed .download-button:hover background rgb(0, 101, 197); matches --color-blue110"),
                "app-disabled": color("#f0f1f3", "computed button.disabled background rgb(240, 241, 243); matches --color-button-active-fill"),
            },
            "text": {
                "primary": color("{color.ink}", f"{SRC_MKT}; body color"),
                "on-action": color("{color.paper}", f"{SRC_MKT}; .btn-primary color"),
                "secondary": color("{color.footer-link}", f"{SRC_MKT}; footer link"),
                "eyebrow": color("{color.eyebrow}", f"{SRC_MKT}; h3"),
                "link": color("{color.link}", f"{SRC_MKT}; in-content link and .nav-link.active"),
                "hero": color("{color.hero-text}", f"{SRC_MKT}; hero h1"),
                "navy": color("{color.navy}", f"{SRC_MKT}; menu item title"),
                "auth": color("{color.auth-text}", "sign-in body and h1"),
                "auth-muted": color("#767a80", "computed a.textbutton.text.secondary color rgb(118, 122, 128); matches --color-dark60"),
                "auth-disabled": color("#b7bdc5", "computed button.disabled color rgb(183, 189, 197); matches --color-dark30"),
                "auth-link": color("#0071db", "computed a.textbutton color rgb(0, 113, 219); --color-textbutton"),
            },
            "border": {
                "stroke": color("{color.field-border}", f"{SRC_MKT}; input.form-control border-top-color"),
                "action": color("{color.ink}", f"{SRC_MKT}; .btn-primary border-top-color"),
                "app-input": color("#cfd2d7", "computed sign-in input border rgb(207, 210, 215); --color-input-border"),
                "app-input-focus": color("#a3a6aa", "computed sign-in input:focus border rgb(163, 166, 170); --color-dark40, not --color-input-focus"),
            },
            "component": {
                "button-primary": {
                    "background": color("{background.action}", f"{SRC_MKT}; .btn-primary"),
                    "text": color("{text.on-action}", f"{SRC_MKT}; .btn-primary"),
                    "radius": dim("{radius.button}", f"{SRC_MKT}; .btn"),
                    "height": dim("{size.button-hero}", f"{SRC_MKT}; hero button"),
                    "padding": dim("{spacing.button-pad-x}", f"{SRC_MKT}; hero button padding-left"),
                },
                "button-secondary": {
                    "background": color("{background.action-secondary}", f"{SRC_MKT}; .btn-secondary"),
                    "text": color("{text.primary}", f"{SRC_MKT}; .btn-secondary"),
                    "radius": dim("{radius.button}", f"{SRC_MKT}; .btn"),
                },
                "text-field": {
                    "background": color("{color.field}", f"{SRC_MKT}; input.form-control"),
                    "text": color("{text.primary}", f"{SRC_MKT}; input.form-control"),
                    "radius": dim("{radius.field}", f"{SRC_MKT}; input.form-control"),
                    "height": dim("{size.field}", f"{SRC_MKT}; input.form-control"),
                },
                "plan-card": {
                    "background": color("{background.surface}", "computed .card on /pricing/"),
                    "radius": dim("{radius.card}", "computed .card"),
                },
                "app-button": {
                    "background": color("{background.app-action}", "computed .download-button"),
                    "text": color("#ffffff", "computed .download-button color"),
                    "radius": dim("{radius.app-control}", "computed .download-button"),
                    "height": dim("{size.app-button-s}", "computed .download-button"),
                },
                "app-field": {
                    "background": color("#ffffff", "computed sign-in input"),
                    "text": color("#36383b", "computed sign-in input color rgb(54, 56, 59)"),
                    "radius": dim("{radius.app-control}", "computed sign-in input"),
                    "height": dim("{size.app-control}", "computed sign-in input"),
                },
            },
            "app": app_colors,
        },
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        ],
    }

    # Record the focus ring and the hover lift where they were read.
    tokens["light"]["focus"] = {
        "outline": ua_default(color("{color.focus-ring}", "CSS.forcePseudoState focus-visible outline-color on header a.btn-primary")),
        "width": ua_default(dim(FOCUS["outlineWidth"], "CSS.forcePseudoState focus-visible outline-width")),
        "offset": ua_default(dim(FOCUS["outlineOffset"], "CSS.forcePseudoState focus-visible outline-offset")),
    }
    tokens["core"]["motion"]["marketing-button-hover"] = {
        "$value": "translateY(-2px)",
        "$type": "other",
        "$extensions": {
            "source": "declared .btn-primary:hover and .btn-secondary:hover in public-site-v2.min.css; computed hover of the header button did not change background",
            "duration": "0.4s",
            "property": "transform",
        },
    }
    tokens["$extensions"] = {
        "capture": {
            "date": "2026-11-19",
            "viewport": "1440x900 at 1x, 390x844 at 2x",
            "themes": ["light"],
            "dark": "prefers-color-scheme: dark did not repaint marketing or /n/signin",
            "notEntered": [
                "sign-in submit",
                "sign-up submit",
                "Google OAuth",
                "SSO",
                "payment",
                "desktop app download",
                "newsletter subscribe",
            ],
        }
    }

    return tokens


def main():
    out = HERE / "tokens.json"
    out.write_text(json.dumps(build(), indent=2) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
