#!/usr/bin/env python3
"""Build tokens.json from District's declared CSS custom properties.

Source: raw/css-vars.json, parsed from the public district-web stylesheet
(:root,html[data-theme=light] and html[data-theme=dark]) on 2026-11-21.
The public site painted light only. Dark tokens are declared and included,
labelled as declared, not shown on a public page.

Every token carries $extensions.source. Aliases point at core ramps.
Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
LIGHT = RAW["light"]
DARK = RAW["dark"]


def hex_color(v):
    v = v.strip().lower()
    if v == "#fff":
        return "#ffffff"
    if v == "#000":
        return "#000000"
    if re.fullmatch(r"#[0-9a-f]{6}", v):
        return v
    if re.fullmatch(r"#[0-9a-f]{8}", v):
        r, g, b, a = (int(v[i:i + 2], 16) for i in (1, 3, 5, 7))
        if a == 255:
            return "#%02x%02x%02x" % (r, g, b)
        return "rgba(%d, %d, %d, %g)" % (r, g, b, round(a / 255, 3))
    if re.fullmatch(r"#[0-9a-f]{3}", v):
        return "#" + "".join(c * 2 for c in v[1:])
    if re.fullmatch(r"#[0-9a-f]{4}", v):
        # #rgba shorthand
        r, g, b, a = (int(c * 2, 16) for c in v[1:])
        if a == 255:
            return "#%02x%02x%02x" % (r, g, b)
        return "rgba(%d, %d, %d, %g)" % (r, g, b, round(a / 255, 3))
    raise ValueError("not a colour: " + v)


def token(value, typ, source, description):
    return {
        "$value": value,
        "$type": typ,
        "$description": description,
        "$extensions": {"source": source},
    }


def ramp(prefix, source_note):
    out = {}
    for name, raw in LIGHT.items():
        if not name.startswith(prefix):
            continue
        step = name[len(prefix):]
        if not re.fullmatch(r"[a-z0-9-]+", step):
            continue
        if not raw.startswith("#"):
            continue
        out[step] = token(hex_color(raw), "color", "css-var " + name + " (" + source_note + ")", name)
    return out


CORE_COLOR = {
    "brand": {
        "pink": token(hex_color(LIGHT["--color-brand-district-pink"]), "color", "css-var --color-brand-district-pink", "Declared brand pink."),
        "purple": token(hex_color(LIGHT["--color-brand-district-purple"]), "color", "css-var --color-brand-district-purple", "Declared brand purple."),
        "purpleSecondary": token(hex_color(LIGHT["--color-brand-district-purple-secondary"]), "color", "css-var --color-brand-district-purple-secondary", "Declared secondary brand purple."),
        "black": token("#000000", "color", "css-var --color-brand-district-black", "Declared brand black."),
        "white": token("#ffffff", "color", "css-var --color-brand-pure-white", "Declared pure white."),
    },
    "grey": ramp("--color-grey-", "light :root"),
    "purple": ramp("--color-purple-", "light :root"),
    "pink": ramp("--color-pink-", "light :root"),
    "green": ramp("--color-green-", "light :root"),
    "yellow": ramp("--color-yellow-", "light :root"),
    "ember": ramp("--color-ember-", "light :root"),
    "blue": ramp("--color-blue-", "light :root"),
    "red": ramp("--color-red-", "light :root"),
}

# Drop empty ramps if a hue is absent.
CORE_COLOR = {k: v for k, v in CORE_COLOR.items() if v}

FONT = {
    "family": {
        "base": token("BeVietnamPro, sans-serif", "fontFamily", "computed fontFamily of body on https://www.district.in/ (2026-11-21)", "The family the public pages paint. The face file is not in this package."),
    },
    "weight": {
        "regular": token("400", "fontWeight", "css-var --font-regular", "Declared regular weight."),
        "medium": token("500", "fontWeight", "css-var --font-medium", "Declared medium weight."),
        "semibold": token("600", "fontWeight", "css-var --font-semibold", "Declared semibold weight."),
        "bold": token("700", "fontWeight", "css-var --font-bold", "Declared bold weight."),
    },
    "size": {
        "xs": token("10px", "dimension", "css-var --font-size-xs", "Declared size."),
        "sm": token("12px", "dimension", "css-var --font-size-sm", "Declared size."),
        "base": token("14px", "dimension", "css-var --font-size-base", "Declared size."),
        "lg": token("16px", "dimension", "css-var --font-size-lg", "Declared size. Body computed font-size was 16px."),
        "xl": token("18px", "dimension", "css-var --font-size-xl", "Declared size. Login dialog title computed 18px."),
        "2xl": token("24px", "dimension", "css-var --font-size-2xl", "Declared size. Section heading computed 24px."),
        "3xl": token("32px", "dimension", "css-var --font-size-3xl", "Declared size."),
        "4xl": token("40px", "dimension", "css-var --font-size-4xl", "Declared size."),
    },
}

RADIUS = {
    "chip": token("6px", "dimension", "computed borderRadius of Events Today chip", "Filter chips."),
    "field": token("12px", "dimension", "computed borderRadius of login phone field and Continue button", "Fields and the dialog primary button."),
    "card": token("16px", "dimension", "computed borderRadius of login dialog and event poster top corners", "Dialogs and poster cards."),
    "pill": token("9999px", "dimension", "computed borderRadius of header Login and SMS chip", "Pill controls."),
}

SPACE = {
    "2": token("8px", "dimension", "computed padding of Events filter chip (8px 12px)", "Chip vertical padding."),
    "3": token("12px", "dimension", "computed padding of Events filter chip (8px 12px)", "Chip horizontal padding."),
    "4": token("16px", "dimension", "computed padding of header Login (0px 16px)", "Control horizontal padding."),
    "6": token("24px", "dimension", "computed lineHeight of body", "Body line height, used as a spacing step."),
}

SIZE = {
    "chip": token("32px", "dimension", "computed height of Events Today chip", "Filter chip height."),
    "login": token("40px", "dimension", "computed height of header Login", "Header control height."),
    "field": token("48px", "dimension", "computed height of login Continue button", "Dialog primary button height."),
    "nav": token("47px", "dimension", "computed height of For you nav link", "Primary nav item height."),
}

MOTION = {
    "fast": token("150ms", "duration", "stylesheet transition-duration .15s", "A declared transition duration."),
    "base": token("200ms", "duration", "stylesheet transition-duration .2s on the header", "Header shadow transition."),
    "slow": token("300ms", "duration", "stylesheet transition-duration .3s", "A declared transition duration."),
    "ease": token("cubic-bezier(0.4, 0, 0.2, 1)", "cubicBezier", "stylesheet cubic-bezier(.4,0,.2,1)", "The standard easing in the stylesheet."),
}

ALIAS = {
    # semantic name -> core path, from the light (or dark) var() declaration
    "text.primary": "color.grey.900",
    "text.secondary": "color.grey.500",
    "text.tertiary": "color.grey.400",
    "text.disabled": "color.grey.200",
    "text.inverse": "color.grey.50",
    "text.brand": "color.brand.purple",
    "text.offer": "color.purple.400",
    "text.success": "color.green.700",
    "text.warning": "color.yellow.600",
    "text.error": "color.ember.600",
    "surface.page": "color.brand.white",
    "surface.secondary": "color.grey.100",
    "surface.inverse": "color.grey.900",
    "border.brand": "color.brand.purple",
    "border.success": "color.green.700",
    "border.warning": "color.yellow.600",
    "icon.brand": "color.brand.purple",
    "icon.primary": "color.grey.800",
    "accent.default": "color.brand.purple",
    "accent.offer": "color.purple.400",
}


def semantic(theme, decls, alias_overrides):
    out_text, out_surface, out_border, out_icon, out_accent = {}, {}, {}, {}, {}
    groups = {
        "text": out_text,
        "surface": out_surface,
        "border": out_border,
        "icon": out_icon,
        "accent": out_accent,
    }
    mapping = {
        "text.primary": "--color-text-primary",
        "text.secondary": "--color-text-secondary",
        "text.tertiary": "--color-text-tertiary",
        "text.disabled": "--color-text-disabled",
        "text.inverse": "--color-text-inverse",
        "text.brand": "--color-text-brand",
        "text.offer": "--color-text-offer",
        "text.success": "--color-text-success",
        "text.warning": "--color-text-warning",
        "text.error": "--color-text-error",
        "surface.page": "--color-surface-primary",
        "surface.secondary": "--color-surface-secondary",
        "surface.inverse": "--color-surface-inverse",
        "border.brand": "--color-border-brand",
        "border.success": "--color-border-success",
        "border.warning": "--color-border-warning",
        "icon.brand": "--color-icon-brand",
        "icon.primary": "--color-icon-primary",
        "accent.default": "--color-text-brand",
        "accent.offer": "--color-surface-offer-primary",
    }
    for path, css_name in mapping.items():
        group, leaf = path.split(".")
        raw = decls.get(css_name, "")
        alias = alias_overrides.get(path) or ALIAS.get(path)
        # Prefer an alias when the declaration is a var() we tokenised.
        if raw.startswith("var(") and alias:
            value = "{" + alias + "}"
            source = "css-var " + css_name + " (" + theme + ") alias"
        elif raw.startswith("#"):
            value = hex_color(raw)
            source = "css-var " + css_name + " (" + theme + ")"
        elif raw.startswith("var("):
            value = "{" + alias + "}" if alias else raw
            source = "css-var " + css_name + " (" + theme + ")"
        else:
            continue
        groups[group][leaf] = token(value, "color", source, css_name + " in " + theme)
    return {
        "color": {
            "text": out_text,
            "surface": out_surface,
            "border": out_border,
            "icon": out_icon,
            "accent": out_accent,
        }
    }


# Dark overrides: the dark block re-points several roles.
DARK_ALIAS = dict(ALIAS)
DARK_ALIAS.update({
    "text.primary": "color.grey.50",
    "text.secondary": "color.grey.250",
    "text.disabled": "color.grey.500",
    "text.inverse": "color.grey.900",
    "surface.page": "color.grey.800",
    "surface.secondary": "color.grey.700",
    "surface.inverse": "color.grey.50",
    "icon.primary": "color.grey.50",
})

# Measured control colours that are not a single semantic alias.
LIGHT_MEASURED = {
    "control": {
        "loginText": token("#2c2c2e", "color", "computed color of header Login on /", "Header Login label."),
        "loginBorder": token("#bfbfc4", "color", "computed borderColor of header Login on /", "Header Login border. Matches --color-grey-200."),
        "loginHover": token("#f7f7f7", "color", "computed backgroundColor of header Login on hover", "Header Login hover fill. Matches --color-grey-50."),
        "chipBorder": token("rgba(0, 0, 0, 0.239)", "color", "computed border of Events Today chip (rgba(0,0,0,0.24))", "Filter chip border."),
        "disabledText": token("#77777e", "color", "computed color of login Continue while empty", "Disabled primary label. Matches --color-grey-400."),
        "disabledFill": token("#bfbfc4", "color", "computed backgroundColor of login Continue while empty", "Disabled primary fill. Matches --color-grey-200."),
        "selectedFill": token("#131316", "color", "computed backgroundColor of SMS chip in the login dialog", "Selected OTP channel."),
        "onSelected": token("#ffffff", "color", "computed color of SMS chip label", "Text on the selected OTP channel."),
        "navSelected": token("#5815fd", "color", "computed color of For you label and its 3px underline on /", "Selected primary nav. Not a declared --color-* name in the harvested sheet."),
        "headerBorder": token("#f1f1f2", "color", "computed borderBottomColor of the header bar", "Header hairline. Matches --color-grey-100."),
        "scrim": token("rgba(0, 0, 0, 0.25)", "color", "Not captured as a flat scrim fill; dialog shadow is rgba(0,0,0,0.25) 0px 25px 50px -12px", "Dialog elevation, not a page scrim token."),
    }
}

doc = {
    "core": {
        "color": CORE_COLOR,
        "font": FONT,
        "radius": RADIUS,
        "space": SPACE,
        "size": SIZE,
        "motion": MOTION,
    },
    "light": semantic("light", LIGHT, {}),
    "dark": semantic("dark", DARK, DARK_ALIAS),
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$extensions": {"source": "Public pages painted this theme. Selector :root,html[data-theme=light]."},
        },
        {
            "id": "dark",
            "name": "Dark",
            "selectedTokenSets": {"core": "source", "dark": "enabled"},
            "$extensions": {"source": "Declared on html[data-theme=dark]. No public theme toggle was found, so this set was not shown in a capture."},
        },
    ],
}
doc["light"]["color"]["control"] = LIGHT_MEASURED["control"]

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out, "core hues", list(CORE_COLOR))
