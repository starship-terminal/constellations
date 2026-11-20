#!/usr/bin/env python3
"""Build tokens.json from raw/readings.json.

The readings were taken live on 2026-11-19 from the signed-out TIDAL web
player (tidal.com) and the public login chrome (login.tidal.com/authorize),
through the T3 preview browser's DOM. Headless Playwright was blocked, and
the preview browser did not paint screenshots, so every colour, type size,
radius and spacing step here is a computed style or a resolved custom
property, not a pixel sample. Those values were typed in from the inspector:
raw/readings.json holds only the capture's metadata (pages, viewports, theme,
what was not entered), so a value read that way is labelled Reconstruction,
entered by hand at capture time, and a value worked out from one stays Derived.

A token is an alias when the product's own variable resolved to the same
colour. Sizes stay in px as the browser computed them. Every token carries
$extensions.source. Deterministic: same readings, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent
RAW = json.loads((PKG / "raw" / "readings.json").read_text())

HOME = "https://tidal.com/ and https://tidal.com/view/pages/explore"
LOGIN = "https://login.tidal.com/authorize"
CAPTURE = "2026-11-19, signed out, prefers-color-scheme dark, preview viewport"


HAND = ("Entered by hand at capture time from the preview inspector; raw/readings.json holds the "
        "capture's metadata, not this reading. ")


def src(evidence, where, note):
    # raw/readings.json records pages, viewports and what was not entered, but no style or custom
    # property value, so a value read in the inspector and typed in here is a hand entry.
    if evidence == "Measured":
        evidence, note = "Reconstruction", HAND + note
    return {"$extensions": {"source": {
        "evidence": evidence,
        "capture": f"{CAPTURE}; {where}",
        "note": note,
    }}}


def color(value, where, note, evidence="Measured"):
    return {"$type": "color", "$value": value, **src(evidence, where, note)}


def dim(value, where, note, evidence="Measured"):
    return {"$type": "dimension", "$value": value, **src(evidence, where, note)}


def font_weight(value, where, note):
    return {"$type": "fontWeight", "$value": value, **src("Measured", where, note)}


def typography(value, where, note):
    return {"$type": "typography", "$value": value, **src("Measured", where, note)}


def cubic(value, where, note):
    return {"$type": "cubicBezier", "$value": value, **src("Measured", where, note)}


def duration(value, where, note):
    return {"$type": "duration", "$value": value, **src("Measured", where, note)}


def core():
    wave = "resolved custom property on :root of the signed-out player"
    return {
        "color": {
            "accent": {
                "fill": color("#33FFEE", HOME, f"{wave}: --wave-color-solid-accent-fill resolved #3fe"),
                "bright": color("#66FFF3", HOME, f"{wave}: --wave-color-solid-accent-bright"),
                "brighter": color("#99FFF7", HOME, f"{wave}: --wave-color-solid-accent-brighter"),
                "dark": color("#3D8F88", HOME, f"{wave}: --wave-color-solid-accent-dark"),
                "darker": color("#244240", HOME, f"{wave}: --wave-color-solid-accent-darker"),
                "darkest": color("#141F1E", HOME, f"{wave}: --wave-color-solid-accent-darkest"),
            },
            "base": {
                "fill": color("#000000", HOME, f"{wave}: --wave-color-solid-base-fill resolved #000"),
                "bright": color("#18181B", HOME, f"{wave}: --wave-color-solid-base-bright"),
                "brighter": color("#242429", HOME, f"{wave}: --wave-color-solid-base-brighter"),
                "brightest": color("#303036", HOME, f"{wave}: --wave-color-solid-base-brightest"),
            },
            "contrast": {
                "fill": color("#FFFFFF", HOME, f"{wave}: --wave-color-solid-contrast-fill resolved #fff"),
                "dark": color("#E4E4E7", HOME, f"{wave}: --wave-color-solid-contrast-dark"),
                "darker": color("#AFAFB6", HOME, f"{wave}: --wave-color-solid-contrast-darker"),
                "darkest": color("#787887", HOME, f"{wave}: --wave-color-solid-contrast-darkest"),
            },
            "warning": {
                "fill": color("#FF3269", HOME, f"{wave}: --wave-color-solid-warning-fill"),
            },
            "danger": color("#FF4242", HOME, f"{wave}: --wave-color-text-danger"),
            "headliners": color("#C0FF00", HOME, "resolved custom property --headliners-green on :root. Not seen on a control in this capture."),
        },
        "font": {
            "text": {
                "$type": "fontFamily",
                "$value": "Square Sans Text VF, Square Sans Text, Helvetica, Arial, sans-serif",
                **src("Measured", HOME, "computed font-family on body of the signed-out player"),
            },
            "display": {
                "$type": "fontFamily",
                "$value": "Square Sans Display VF, Square Sans Display, Helvetica, Arial, sans-serif",
                **src("Measured", HOME, "computed font-family on the home h2 The Hits"),
            },
            "login": {
                "$type": "fontFamily",
                "$value": "nationale, nationale-regular, helvetica, arial, sans-serif",
                **src("Measured", LOGIN, "computed font-family on the authorize page body"),
            },
        },
        "fontWeight": {
            "regular": font_weight(400, HOME, "computed font-weight on the transfer card body"),
            "medium": font_weight(500, HOME, "computed font-weight on a sidebar link, and --wave-font-weight--medium"),
            "demi": font_weight(600, HOME, "computed font-weight on Log in, and --wave-font-weight--demi"),
            "bold": font_weight(700, HOME, "computed font-weight on the home h1, and --wave-font-weight--bold"),
        },
        "radius": {
            "none": dim("0px", HOME, "--wave-border-radius--none resolved 0, written as 0px", "Derived"),
            "extraSmall": dim("4px", HOME, "--wave-border-radius--extra-small; also the artwork img border-radius"),
            "small": dim("8px", HOME, "--wave-border-radius--small"),
            "regular": dim("12px", HOME, "--wave-border-radius--regular; sidebar link and login Continue button"),
            "panel": dim("16px", HOME, "--floating-panel-border-radius; login field wrapper"),
            "full": dim("1000px", HOME, "--wave-border-radius--full; pill buttons"),
        },
        "space": {
            "4": dim("4px", HOME, "tab padding-top on For you"),
            "8": dim("8px", HOME, "sidebar link padding and button gap"),
            "9": dim("9px", HOME, "small button padding-block"),
            "14": dim("14px", HOME, "Log in top offset inside the 48px bar"),
            "16": dim("16px", HOME, "button padding-inline, and sidebar inset"),
            "32": dim("32px", HOME, "small button height, and back-button size"),
            "40": dim("40px", HOME, "sidebar row height and Get started height"),
            "48": dim("48px", HOME, "--desktop-navbar-height"),
            "56": dim("56px", HOME, "--headerHeight, and the phone bottom bar height"),
            "78": dim("78px", HOME, "--collapsedSidebarWidth"),
            "240": dim("240px", HOME, "measured width of aside[aria-label=Navigation sidebar] at 1440"),
        },
        "typography": {
            "body": typography({
                "fontFamily": "{font.text}",
                "fontSize": "14px",
                "fontWeight": "{fontWeight.regular}",
                "lineHeight": "20px",
            }, HOME, "computed style on body"),
            "sidebar": typography({
                "fontFamily": "{font.text}",
                "fontSize": "14px",
                "fontWeight": "{fontWeight.medium}",
                "lineHeight": "20px",
            }, HOME, "computed style on a sidebar link"),
            "button": typography({
                "fontFamily": "{font.text}",
                "fontSize": "14px",
                "fontWeight": "{fontWeight.demi}",
                "lineHeight": "22px",
            }, HOME, "computed style on Log in and Create a free account"),
            "cardBody": typography({
                "fontFamily": "{font.text}",
                "fontSize": "12px",
                "fontWeight": "{fontWeight.regular}",
                "lineHeight": "18px",
            }, HOME, "computed style on the transfer-card paragraph"),
            "pageTitle": typography({
                "fontFamily": "{font.text}",
                "fontSize": "24px",
                "fontWeight": "{fontWeight.bold}",
                "lineHeight": "28px",
            }, HOME, "computed style on the home h1 Home"),
            "section": typography({
                "fontFamily": "{font.display}",
                "fontSize": "19px",
                "fontWeight": "{fontWeight.bold}",
                "lineHeight": "26px",
            }, HOME, "computed style on the home h2 The Hits"),
            "exploreTitle": typography({
                "fontFamily": "{font.text}",
                "fontSize": "27px",
                "fontWeight": "{fontWeight.bold}",
                "lineHeight": "28px",
            }, "https://tidal.com/view/pages/explore", "computed style on the Explore h1 at 1169px. lineHeight was not re-read on this heading, so the home h1 line-height is recorded"),
            "exploreSection": typography({
                "fontFamily": "{font.text}",
                "fontSize": "20px",
                "fontWeight": "{fontWeight.demi}",
                "lineHeight": "24px",
            }, "https://tidal.com/view/pages/explore", "computed style on the Explore h2 Featured at 1440px"),
            "loginTitle": typography({
                "fontFamily": "{font.login}",
                "fontSize": "20px",
                "fontWeight": "{fontWeight.bold}",
                "lineHeight": "24px",
            }, LOGIN, "computed style on the h1 Sign up or log in"),
            "loginBody": typography({
                "fontFamily": "{font.login}",
                "fontSize": "16px",
                "fontWeight": "{fontWeight.regular}",
                "lineHeight": "24px",
            }, LOGIN, "computed style on the authorize page body"),
            "loginButton": typography({
                "fontFamily": "{font.login}",
                "fontSize": "16px",
                "fontWeight": "{fontWeight.demi}",
                "lineHeight": "24px",
            }, LOGIN, "computed font-size and weight on Continue. The computed line-height was 49.7778px, the button height, so the body line-height is recorded"),
            "marketingTitle": typography({
                "fontFamily": "{font.login}",
                "fontSize": "32px",
                "fontWeight": "{fontWeight.bold}",
                "lineHeight": "38px",
            }, "https://offer.tidal.com/download", "computed style on the h1 Download TIDAL. line-height was 38.4px, rounded to 38px"),
        },
        "motion": {
            "button": duration("240ms", HOME, "computed transition on Log in: background-color 0.24s and color 0.24s"),
            "buttonEasing": cubic([0.76, 0, 0.24, 1], HOME, "computed cubic-bezier on the Log in transition"),
        },
    }


def semantic():
    """One palette. The signed-out player did not expose a light theme."""
    home = HOME
    login = LOGIN
    return {
        "color": {
            "bg": {
                "page": color("{color.base.fill}", home, "computed background-color on body: rgb(0, 0, 0)"),
                "sidebar": color("{color.base.fill}", home, "computed background-color on the navigation aside"),
                "footer": color("{color.base.bright}", home, "computed background-color on footer: rgb(24, 24, 27)"),
                "nav": color("#0000008C", home, "resolved --frosted-glass-nav-surface"),
                "floating": color("#282828BF", home, "resolved --frosted-glass-floating-surface"),
                "secondaryButton": color("#282828BF", home, "computed background-color on Log in: rgba(40, 40, 40, 0.75)"),
                "quietButton": color("#FFFFFF14", home, "computed background-color on Get started: rgba(255, 255, 255, 0.08)"),
                "selected": color("#FFFFFF26", home, "computed background-color on the selected sidebar link Music: rgba(255, 255, 255, 0.15)"),
                "selectedPhone": color("#FFFFFF1A", home, "computed background-color on the selected phone tab Search: rgba(255, 255, 255, 0.1)"),
                "loginField": color("{color.base.fill}", login, "login field wrapper background was transparent over the black page"),
            },
            "text": {
                "primary": color("{color.contrast.fill}", home, "computed color on body: rgb(255, 255, 255)"),
                "secondary": color("#FFFFFF8C", home, "computed color on an unselected sidebar link: rgba(255, 255, 255, 0.55)"),
                "tertiary": color("{color.contrast.darkest}", home, "resolved --wave-color-text-tertiary"),
                "disabled": color("{color.base.brightest}", home, "resolved --wave-color-text-disabled. A disabled control was not on screen"),
                "inverse": color("#101010", home, "computed color on Create a free account: rgb(16, 16, 16)"),
                "link": color("{color.accent.fill}", home, "resolved --wave-color-text-link"),
                "danger": color("{color.danger}", home, "resolved --wave-color-text-danger"),
                "loginMuted": color("#888F98", login, "computed color on the or divider"),
            },
            "accent": {
                "default": color("{color.accent.fill}", home, "the player accent, resolved from --wave-color-solid-accent-fill"),
            },
            "border": {
                "field": color("{color.contrast.fill}", login, "login field wrapper box-shadow: rgb(255, 255, 255) 0px 0px 0px 1px inset"),
                "focus": color("{color.contrast.fill}", home, "declared :focus-visible outline on the player button: 3px solid --wave-color-solid-contrast-fill"),
                "divider": color("{color.contrast.darker}", home, "resolved --wave-color-solid-contrast-darker. A divider rule was not measured on an element"),
            },
            "button": {
                "primaryBg": color("{color.contrast.fill}", home, "computed background-color on Create a free account"),
                "primaryText": color("#101010", home, "computed color on Create a free account"),
                "secondaryBg": color("#282828BF", home, "computed background-color on Log in"),
                "secondaryText": color("{color.contrast.fill}", home, "computed color on Log in"),
                "loginBg": color("{color.contrast.fill}", login, "computed background-color on Continue"),
                "loginText": color("#000000", login, "computed color on Continue"),
                "loginDisabled": color("#FFFFFF66", login, "Continue was disabled at opacity 0.4 over white. The opacity is the measured state; the colour is that white at 0.4", "Derived"),
            },
        },
        "component": {
            "button": {
                "radius": dim("{radius.full}", home, "computed border-radius on Log in: 1000px"),
                "height": dim("32px", home, "computed height of the small Log in button"),
                "padding": dim("16px", home, "computed padding-inline on Log in"),
                "fontSize": dim("14px", home, "computed font-size on Log in"),
            },
            "loginButton": {
                "radius": dim("{radius.regular}", login, "computed border-radius on Continue: 12px"),
                "height": dim("50px", login, "computed height of Continue"),
                "padding": dim("20px", login, "computed padding-inline on Continue"),
            },
            "field": {
                "radius": dim("{radius.panel}", login, "computed border-radius on the email field wrapper: 16px"),
                "height": dim("54px", login, "computed height of the email field wrapper"),
            },
            "sidebar": {
                "width": dim("240px", home, "measured aside width at a 1440 CSS viewport"),
                "rowHeight": dim("40px", home, "computed height of a sidebar link"),
                "radius": dim("{radius.regular}", home, "computed border-radius on a sidebar link: 12px"),
            },
        },
    }


class CheckError(AssertionError):
    pass


def require(ok, message):
    if not ok:
        raise CheckError(message)


def walk(node, path=()):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v, path + (k,))


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    return []


def check(doc):
    sets = [s for s in ("core", "dark") if s in doc]
    paths = {".".join(p) for name in sets for p, _ in walk(doc[name])}
    for name in sets:
        for p, t in walk(doc[name]):
            where = name + "." + ".".join(p)
            source = t.get("$extensions", {}).get("source", {})
            require(source.get("evidence") and source.get("capture"), f"{where}: no source")
            v = t["$value"]
            for a in aliases(v):
                require(a in paths, f"{where}: alias {{{a}}} points at nothing")
            if isinstance(v, str) and v.startswith("{"):
                continue
            if t["$type"] == "color":
                require(re.fullmatch(r"#[0-9A-Fa-f]{6}([0-9A-Fa-f]{2})?", v), f"{where}: bad colour {v}")
            elif t["$type"] == "dimension":
                require(re.fullmatch(r"-?\d+(\.\d+)?px", v), f"{where}: bad dimension {v}")


def build():
    doc = {
        "core": core(),
        "dark": semantic(),
        "$themes": [{
            "id": "dark",
            "name": "Dark",
            "selectedTokenSets": {"core": "source", "dark": "enabled"},
            "$description": "The only theme the signed-out player showed. prefers-color-scheme was dark. No light switch was on the public chrome.",
        }],
        "$metadata": {"tokenSetOrder": ["core", "dark"]},
    }
    check(doc)
    return doc


def render(doc):
    """tokens.json's exact text."""
    return json.dumps(doc, indent=1, ensure_ascii=False) + "\n"


def main():
    doc = build()
    (PKG / "tokens.json").write_text(render(doc))
    n = sum(1 for _ in walk(doc["core"])) + sum(1 for _ in walk(doc["dark"]))
    print(f"tokens.json: {n} tokens")


if __name__ == "__main__":
    main()
