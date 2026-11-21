#!/usr/bin/env python3
"""Build tokens.json from Quizlet custom properties read on the signed-out homepage.

Source: raw/css-vars.json, computed on documentElement while body had
theme-default. The same ramps were read on a prior signed-in theme-night page
and saved as raw/css-vars-night-2026-11-21.json. The hex values match. This
builder uses the public file. Cross-origin stylesheets on assets.quizlet.com
were CSSOM-blocked, so these are resolved custom properties, not parsed
declarations.

Semantic roles are aliases into those ramps, matched to computed styles in
raw/components-computed.json. The light set is the public marketing page. The
night set is the prior signed-in shell and is kept so those readings stay in
the file. This public pass did not open the signed-in app.

Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
COMPUTED = RAW["computed"]

HUES = ("gray", "error", "lemon", "lilac", "mint", "sherbert", "sky", "sunset", "twilight")


def color(value):
    value = value.strip()
    if not re.fullmatch(r"#[0-9A-Fa-f]{6}", value):
        raise ValueError("not a 6-digit hex colour: %r" % value)
    return value.upper()


def token(value, ty, source, description=None):
    out = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    if description:
        out["$description"] = description
    return out


def core_colors():
    group = {}
    for name, value in COMPUTED.items():
        if not name.startswith("--"):
            continue
        body = name[2:]
        hue, _, step = body.partition("-")
        if hue not in HUES or not step.isdigit():
            continue
        group.setdefault(hue, {})[step] = token(
            color(value),
            "color",
            "css-var %s, computed on :root (theme-default, signed out)" % name,
        )
    return group


def alias(path, source, description=None):
    return token("{%s}" % path, "color", source, description)


def main():
    light_src = "computed style on the signed-out homepage, theme-default, matched to a core ramp"
    night_src = "prior signed-in theme-night reading, same ramp hex as the public file, matched to a core ramp"
    light = {
        "page": alias("color.gray.200", light_src, "Body background rgb(246, 247, 251)."),
        "text": alias("color.gray.800", light_src, "Body text rgb(40, 46, 62)."),
        "text-strong": alias("color.gray.900", light_src, "Nearest ramp to the h1, which computed as rgb(0, 0, 0). The h1 itself is not a ramp step."),
        "accent": alias("color.twilight.500", light_src, "Log in and Sign up pills rgb(66, 85, 255)."),
        "accent-hover": alias("color.twilight.600", light_src, "Log in hover rgb(66, 62, 216)."),
        "link": alias("color.twilight.500", light_src, "I'm a teacher link rgb(66, 85, 255)."),
        "surface": alias("color.gray.200", light_src, "Search field AssemblyTextInput rgb(246, 247, 251)."),
        "trial": alias("color.sunset.400", light_src, "Upgrade trial button rgb(255, 205, 31)."),
        "on-trial": alias("color.gray.800", light_src, "Trial label rgb(40, 46, 62)."),
        "pricing-page": alias("color.twilight.900", light_src, "Public /upgrade page background rgb(10, 9, 45)."),
    }
    night = {
        "page": alias("color.twilight.900", night_src, "Prior signed-in body background rgb(10, 9, 45)."),
        "text": alias("color.gray.200", night_src, "Prior signed-in body text rgb(246, 247, 251)."),
        "text-strong": alias("color.gray.100", night_src, "Prior primary button label and menu text."),
        "text-muted": alias("color.gray.400", night_src, "Prior section label rgb(217, 221, 232)."),
        "accent": alias("color.twilight.500", night_src, "Prior primary button rgb(66, 85, 255)."),
        "accent-text": alias("color.twilight.300", night_src, "Prior edit link rgb(168, 177, 255)."),
        "selected": alias("color.twilight.400", night_src, "Prior selected nav rgb(117, 131, 255)."),
        "surface": alias("color.gray.700", night_src, "Prior search field rgb(46, 56, 86)."),
        "trial": alias("color.sunset.400", night_src, "Prior trial button rgb(255, 205, 31)."),
        "on-trial": alias("color.gray.800", night_src, "Prior trial label rgb(40, 46, 62)."),
        "danger": alias("color.error.300", night_src, "Error ramp step used as the danger role. Not observed on a public error state."),
    }
    doc = {
        "core": {
            "color": core_colors(),
            "font": {
                "family": {
                    "body": token(
                        "hurme_no2-webfont, -apple-system, system-ui, sans-serif",
                        "fontFamily",
                        "computed fontFamily of body on https://quizlet.com/ signed out",
                    )
                },
                "weight": {
                    "body": token(400, "fontWeight", "computed fontWeight of body"),
                    "label": token(600, "fontWeight", "computed fontWeight of the Log in pill"),
                    "heading": token(700, "fontWeight", "computed fontWeight of the homepage h1"),
                },
                "size": {
                    "body": token("16px", "dimension", "computed fontSize of body"),
                    "label": token("14px", "dimension", "computed fontSize of the Log in pill"),
                    "signup": token("16px", "dimension", "computed fontSize of the hero Sign up for free pill"),
                    "heading": token("44px", "dimension", "computed fontSize of the homepage h1"),
                },
                "line-height": {
                    "body": token("26px", "dimension", "computed lineHeight of body"),
                    "heading": token("56px", "dimension", "computed lineHeight of the homepage h1"),
                },
            },
            "radius": {
                "field": token("8px", "dimension", "computed borderRadius of the search field"),
                "pill": token("200px", "dimension", "computed borderRadius of the Log in pill"),
            },
            "space": {
                "login-y": token("10px", "dimension", "computed padding-block of the Log in pill"),
                "login-x": token("16px", "dimension", "computed padding-inline of the Log in pill"),
                "signup-y": token("12px", "dimension", "computed padding-block of the hero Sign up pill"),
                "signup-x": token("24px", "dimension", "computed padding-inline of the hero Sign up pill"),
            },
            "size": {
                "login": token("40px", "dimension", "computed height of the Log in pill"),
                "signup": token("48px", "dimension", "computed height of the hero Sign up pill"),
                "field": token("40px", "dimension", "computed height of the search field"),
                "trial": token("48px", "dimension", "computed height of the upgrade trial button"),
            },
        },
        "light": light,
        "night": night,
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"id": "night", "name": "Night", "selectedTokenSets": {"core": "source", "night": "enabled"}},
        ],
    }
    text = json.dumps(doc, indent=1) + "\n"
    (HERE / "tokens.json").write_text(text)
    print("wrote", HERE / "tokens.json")


if __name__ == "__main__":
    main()
