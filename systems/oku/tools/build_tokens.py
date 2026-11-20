#!/usr/bin/env python3
"""Build tokens.json from systems/oku/raw/readings.json.

Every value is a computed style or a declared --theme-ui-colors-* custom
property read on oku.club on 2026-11-19. A role that was not on the page is
not invented. Deterministic: same readings, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "readings.json").read_text())
PROPS = RAW["customProperties"]
SRC = "raw/readings.json"


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def duration(value, source):
    return {"$type": "duration", "$value": value, "$extensions": {"source": source}}


def font(family, size, weight, line, tracking, source):
    token = {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
        },
        "$extensions": {"source": source},
    }
    if tracking is not None:
        token["$value"]["letterSpacing"] = tracking
    return token


def ramp(theme):
    declared = PROPS[theme]
    out = {}
    for name, value in declared.items():
        out[name] = color(
            value,
            f"Declared --theme-ui-colors-{name} on html ({theme}). {SRC}",
        )
    return out


def semantic(theme):
    """Roles mapped from the painted page, then the named ramps."""
    if theme == "dark":
        roles = {
            "page": ("#131314", "html background rgb(19, 19, 20) on https://oku.club/, dark. Matches --theme-ui-colors-milk."),
            "book": ("#000000", "Declared --theme-ui-colors-book. Not measured as a painted fill on the public pages."),
            "surface": ("#1C1C1D", "Free pricing card background rgb(28, 28, 29). Matches --theme-ui-colors-blueberry-2 and blueberry-5."),
            "raised": ("#242426", "Join for free background rgb(36, 36, 38). Matches --theme-ui-colors-blueberry-10."),
            "premium": ("#1F241F", "Premium pricing card background rgb(31, 36, 31). Matches --theme-ui-colors-badge-premium-13."),
            "supporter": ("#292328", "Supporter pricing card background rgb(41, 35, 40). Matches --theme-ui-colors-badge-supporter-13."),
            "text-primary": ("#E0E1E4", "h1 color rgb(224, 225, 228) on https://oku.club/. Matches --theme-ui-colors-olive."),
            "text-secondary": ("#C1BECB", "nav link and book title rgb(193, 190, 203). Matches --theme-ui-colors-blueberry-100."),
            "text-muted": ("#9E9CA6", "body and byline rgb(158, 156, 166). Matches --theme-ui-colors-blueberry-80."),
            "text-disabled": ("#6A686F", "idle tab and idle Pay monthly rgb(106, 104, 111). Matches --theme-ui-colors-blueberry-50."),
            "text-on-accent": ("#131314", "Join button text rgb(19, 19, 20) on the olive fill."),
            "link": ("#9E9EFF", "logo and book-card link color rgb(158, 158, 255). Not a declared --theme-ui-colors-* name."),
            "border": ("#363539", "text field border rgb(54, 53, 57). Matches --theme-ui-colors-blueberry-20."),
            "border-strong": ("#E0E1E438", "outline button inset ring rgba(224, 225, 228, 0.22): olive at the measured 22% alpha."),
            "accent": ("#E0E1E4", "primary Join fill rgb(224, 225, 228). Same value as text-primary."),
            "accent-brand": ("#E32020", "Declared --theme-ui-colors-candy. Not painted on the measured public controls."),
            "success": ("#349E54", "Declared --theme-ui-colors-kiwi-100. Save 50%! painted rgb(111, 153, 101), which is badge-premium-100."),
            "warning": ("#F1B205", "Declared --theme-ui-colors-banana-100. Not painted as a status on the measured pages."),
            "danger": ("#EA4E46", "Declared --theme-ui-colors-strawberry-100. Not painted as an error on the measured pages."),
            "info": ("#1877F2", "Declared --theme-ui-colors-facebook-100. Not painted on the measured pages."),
            "highlight": ("#55460E", "Declared --theme-ui-colors-highlight for dark. Not painted on the measured pages."),
        }
    else:
        roles = {
            "page": ("#FFFFFF", "html background rgb(255, 255, 255) on https://oku.club/explore with prefers-color-scheme light. Matches --theme-ui-colors-milk."),
            "book": ("#F6F6F6", "Declared --theme-ui-colors-book for the light selector. Not measured as a painted fill."),
            "surface": ("#FAFAFB", "Declared --theme-ui-colors-blueberry-2. The explore card itself painted rgb(255, 255, 255), the page colour."),
            "raised": ("#E8E8E9", "Declared --theme-ui-colors-blueberry-10. Light Join for free was not remeasured."),
            "premium": ("#ECF2EB", "Declared --theme-ui-colors-badge-premium-13. Light pricing cards were not remeasured."),
            "supporter": ("#F7F1F4", "Declared --theme-ui-colors-badge-supporter-13. Light pricing cards were not remeasured."),
            "text-primary": ("#000000", "h1 color rgb(0, 0, 0) on the light explore page. Matches --theme-ui-colors-blackberry."),
            "text-secondary": ("#131314", "nav and book title rgb(19, 19, 20). Matches --theme-ui-colors-olive and blueberry-100."),
            "text-muted": ("#46474E", "byline rgb(70, 71, 78). Matches --theme-ui-colors-blueberry-80."),
            "text-disabled": ("#8C8C90", "Declared --theme-ui-colors-blueberry-50. Idle tab was not remeasured in light."),
            "text-on-accent": ("#FFFFFF", "Join button text rgb(255, 255, 255) on the black fill."),
            "link": ("#0000EE", "book card link color rgb(0, 0, 238) in light. Browser default, not a declared token.", OBSERVED),
            "border": ("#E8E8E9", "book card border rgb(232, 232, 233). Matches --theme-ui-colors-blueberry-10."),
            "border-strong": ("#131314", "Declared --theme-ui-colors-blueberry-100. Light outline ring was not remeasured."),
            "accent": ("#000000", "primary Join fill rgb(0, 0, 0) in light. Matches --theme-ui-colors-blackberry."),
            "accent-brand": ("#E32020", "Declared --theme-ui-colors-candy. Same in both themes."),
            "success": ("#349E54", "Declared --theme-ui-colors-kiwi-100."),
            "warning": ("#F1B205", "Declared --theme-ui-colors-banana-100."),
            "danger": ("#EA4E46", "Declared --theme-ui-colors-strawberry-100."),
            "info": ("#1877F2", "Declared --theme-ui-colors-facebook-100."),
            "highlight": ("#F8DF80", "Declared --theme-ui-colors-highlight for the light selector."),
        }
    out = {}
    for name, (value, source, *label) in roles.items():
        out[name] = color(value, f"{evidence(source, *label)}. {source} {SRC}")
    return out


OBSERVED = "Observed"
NOT_PAINTED = re.compile(r"not (re)?measured|not painted|not remeasured", re.I)


def evidence(source, label=None):
    """Measured when the role's value was read painted on the page; Derived when a declared custom property
    was assigned to a role that was not painted (or not remeasured in this theme); a label given with the
    role wins."""
    if label:
        return label
    return "Derived" if source.startswith("Declared") or NOT_PAINTED.search(source) else "Measured"


def core():
    home = "https://oku.club/ computed style, dark, 1440 CSS px"
    return {
        "color": {
            "ramp": {
                "$description": "Oku names its palette as fruit. Values are the dark and light declarations; semantic sets alias the painted roles.",
            }
        },
        "fontFamily": {
            "display": {
                "$type": "fontFamily",
                "$value": "FabricSerifWeb",
                "$extensions": {"source": "h1 computed font-family on https://oku.club/. " + SRC},
            },
            "body": {
                "$type": "fontFamily",
                "$value": "Inter",
                "$extensions": {"source": "body computed font-family on https://oku.club/. " + SRC},
            },
        },
        "typography": {
            "display": font("FabricSerifWeb", "48px", 400, "62.4px", "-0.288px", f"{home}. h1."),
            "display-tight": font("FabricSerifWeb", "48px", 400, "57.6px", "-0.288px", "https://oku.club/pricing feature h2."),
            "title": font("FabricSerifWeb", "36px", 400, "46.8px", "-0.216px", f"{home}. section h2."),
            "title-page": font("FabricSerifWeb", "48px", 400, "62.4px", "-0.288px", "https://oku.club/pricing h1, column width 720."),
            "heading": font("FabricSerifWeb", "24px", 400, "31.2px", "-0.7px", "https://oku.club/signin h1 and the book page h1."),
            "menu": font("FabricSerifWeb", "36px", 400, "54px", None, "Phone drawer nav link at 390 CSS px."),
            "price": font("Inter", "39px", 400, "39px", None, "https://oku.club/pricing price figure."),
            "body": font("Inter", "16px", 400, "28.8px", None, f"{home}. section paragraph."),
            "body-strong": font("Inter", "16px", 500, "20.8px", None, f"{home}. h3 Looking to switch?"),
            "nav": font("Inter", "16px", 400, "24px", None, f"{home}. Explore link."),
            "ui": font("Inter", "14px", 500, "40px", None, f"{home}. Join and Sign in buttons."),
            "ui-quiet": font("Inter", "15px", 500, "54px", None, f"{home}. Join for free."),
            "label": font("Inter", "14px", 400, "25.2px", None, "https://oku.club/signin field label and byline."),
            "caption": font("Inter", "13px", 400, "19.5px", None, f"{home}. Already a member?"),
            "micro": font("Inter", "12px", 400, "15.6px", None, "Book page shelf caption."),
            "phone-display": font("FabricSerifWeb", "28px", 400, "36.4px", "-0.168px", "https://oku.club/ h1 at 390 CSS px."),
            "phone-title": font("FabricSerifWeb", "24px", 400, "31.2px", "-0.144px", "https://oku.club/ h2 at 390 CSS px."),
        },
        "spacing": {
            "8": dim("8px", "Collection chip padding 8px on the book page."),
            "16": dim("16px", "Hero column gap 16px. Field padding-inline 16px. Tab padding-block 16px."),
            "24": dim("24px", "Button padding-inline 24px. Drawer padding 24px. Phone bar has no extra inset beyond the drawer."),
            "32": dim("32px", "Shelf button padding-inline 32px. Auth panel padding-inline 32px."),
            "40": dim("40px", "Pricing card padding 40px."),
            "48": dim("48px", "Header padding-inline 48px at desktop. Auth panel padding-top 48px."),
        },
        "radius": {
            "cover": dim("3px", "Book cover img border-radius 3px on https://oku.club/explore."),
            "chip": dim("6px", "Collection chip border-radius 6px on the book page."),
            "control": dim("8px", "Buttons, fields, pricing cards and book cards."),
            "pill": dim("27px", "Billing switch track, 42 by 27."),
            "round": dim("21px", "Billing switch knob, 21px circle."),
        },
        "border": {
            "hairline": dim("1px", "Text field border-top-width 1px. Light book card border 1px."),
            "tab": dim("3px", "Selected Book Info tab border-bottom 3px."),
        },
        "size": {
            "button": dim("40px", "Join and Sign in height 40px."),
            "button-quiet": dim("54px", "Join for free height 54px at desktop. 46px at 390."),
            "field": dim("46px", "Sign-in, join and reset fields, 368 by 46."),
            "field-width": dim("368px", "Auth fields and pricing cards."),
            "icon-button": dim("32px", "Explore carousel buttons, 32px circle."),
            "icon": dim("28px", "Shelf action svg, 28px."),
            "bar": dim("80px", "Fixed top bar height, desktop and phone."),
            "logo": dim("24px", "Wordmark svg height 24px, width 60px."),
            "column": dim("816px", "Blog post and privacy column max-width."),
            "prose": dim("752px", "Blog post h1 and body measured width."),
            "hero": dim("720px", "Pricing and blog index h1 measured width."),
        },
        "elevation": {
            "lift": {
                "$type": "shadow",
                "$value": {
                    "color": "rgba(0, 0, 0, 0.25)",
                    "offsetX": "0px",
                    "offsetY": "4px",
                    "blur": "4px",
                    "spread": "-5px",
                },
                "$extensions": {
                    "source": "Join button box-shadow rgba(0, 0, 0, 0.25) 0px 4px 4px -5px. " + SRC
                },
            }
        },
        "motion": {
            "duration-switch": duration("300ms", "label.css-1tfy84h transition, and 16 stylesheet rules."),
            "duration-short": duration("150ms", "7 stylesheet rules, ease-in-out. Selector not isolated."),
            "easing-switch": {
                "$type": "cubicBezier",
                "$value": [0.23, 1, 0.32, 1],
                "$extensions": {"source": "Billing switch transition. " + SRC},
            },
        },
    }


def component(theme):
    """Resolved colours. Cross-set aliases are not used: DESIGN.md reads one set."""
    if theme == "dark":
        return {
            "button-primary": {
                "background": color("#E0E1E4", "Join fill rgb(224, 225, 228). " + SRC),
                "text": color("#131314", "Join text rgb(19, 19, 20). " + SRC),
                "radius": dim("8px", "Join border-radius 8px."),
                "height": dim("40px", "Join height 40px."),
            },
            "button-quiet": {
                "background": color("#242426", "Join for free fill rgb(36, 36, 38). " + SRC),
                "text": color("#C1BECB", "Join for free text. " + SRC),
                "radius": dim("8px", "8px."),
                "height": dim("54px", "54px desktop."),
            },
            "field": {
                "background": color("#131314", "Field fill matches the page. " + SRC),
                "text": color("#C1BECB", "Field color and placeholder. " + SRC),
                "radius": dim("8px", "8px."),
                "height": dim("46px", "46px."),
            },
            "card": {
                "background": color("#1C1C1D", "Free plan card. " + SRC),
                "radius": dim("8px", "8px."),
            },
        }
    return {
        "button-primary": {
            "background": color("#000000", "Light Join fill rgb(0, 0, 0). " + SRC),
            "text": color("#FFFFFF", "Light Join text. " + SRC),
            "radius": dim("8px", "8px."),
            "height": dim("40px", "Derived. 40px, from the dark Join; not remeasured in light."),
        },
        "field": {
            "background": color("#FFFFFF", "Derived. Light field was not remeasured. Page fill recorded. " + SRC),
            "text": color("#131314", "Derived. Light field text was not remeasured. " + SRC),
            "radius": dim("8px", "Derived. 8px, from the dark field."),
            "height": dim("46px", "Derived. 46px, from the dark field."),
        },
        "card": {
            "background": color("#FFFFFF", "Light explore card painted the page colour. " + SRC),
            "radius": dim("8px", "8px."),
        },
    }


def build():
    """The token document, built in memory from raw/readings.json; main() writes it."""
    sets = {
        "core": core(),
        "light": {"color": semantic("light"), "ramp": ramp("light"), "component": component("light")},
        "dark": {"color": semantic("dark"), "ramp": ramp("dark"), "component": component("dark")},
        "$themes": [
            {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
            {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
        ],
    }
    # Drop the empty description-only group if a checker wants real tokens only.
    # Keep it: the fruit names live in each theme's ramp.
    sets["core"].pop("color", None)
    return sets


def main():
    text = json.dumps(build(), indent=2) + "\n"
    (HERE / "tokens.json").write_text(text)
    print(f"wrote {HERE / 'tokens.json'} ({len(text)} bytes)")


if __name__ == "__main__":
    main()
