#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

The dump is the :root custom properties and the --comp* tokens read from
sg.trip.com on 2026-11-19. Names stay the product's. A value that is a
hex or rgb() of a core colour becomes an alias. Trip Geom is proprietary
and is recorded by name; the token stack falls back to the system face
the page itself names after Trip Geom.

Run from systems/trip: python3 tools/build_tokens.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
ROOT = RAW["root"]
COMP = RAW["comp"]

SRC = (
    "Measured. Declared on :root in the online-home stylesheet "
    "(ak-s-cw.tripcdn.com/.../onlineHome.*.css) and computed on "
    "https://sg.trip.com/?locale=en-sg, 2026-11-19. Viewport at the "
    "token read: innerWidth 1169, innerHeight 731, devicePixelRatio 2."
)
SRC_COMP = (
    "Measured. :root --comp* token on the same page and stylesheet. "
    "Component tokens describe the design system's controls; the public "
    "pages paint some of them and leave others unused."
)
SRC_ALIAS = "Derived. Alias to a core colour with the same hex or rgb()."
SRC_TYPE = (
    "Derived. Split from a measured --smtcBody* / --smtcDisplay* / "
    "--smtcTypography* shorthand on :root."
)
SRC_SHADOW = (
    "Measured. Computed box-shadow on a live element of "
    "https://sg.trip.com/?locale=en-sg at innerWidth 1440."
)
SRC_STATE = (
    "Measured. Computed style or a stylesheet :hover/:disabled/:focus "
    "rule on a live public control, 2026-11-19."
)

FONT = '"Trip Geom", system-ui, -apple-system, Roboto, Helvetica, Arial, sans-serif'


def to_hex(value: str) -> str:
    """A CSS colour as #rrggbb, or #rrggbbaa when translucent; refuses anything else.
    tools/catalog.py and the contrast check read only hex, so hsla()/rgba() strings were skipped."""
    v = re.sub(r"\s+", " ", value.strip().lower())
    if v == "transparent":
        return "#00000000"
    m = re.fullmatch(r"#([0-9a-f]{3,4}|[0-9a-f]{6}|[0-9a-f]{8})", v)
    if m:
        h = m.group(1)
        h = "".join(c * 2 for c in h) if len(h) in (3, 4) else h
        return "#" + (h[:6] if h[6:] == "ff" else h)
    m = re.fullmatch(r"(rgba?|hsla?)\((.*)\)", v)
    if not m:
        raise SystemExit(f"not a colour: {value!r}")
    fn, parts = m.group(1), [x for x in re.split(r"[\s,/]+", m.group(2).strip()) if x]
    if len(parts) not in (3, 4):
        raise SystemExit(f"not a colour: {value!r}")
    pct = lambda x, scale: float(x[:-1]) / 100 * scale if x.endswith("%") else float(x)
    a = pct(parts[3], 1) if len(parts) == 4 else 1.0
    if fn.startswith("rgb"):
        r, g, b = (pct(x, 255) for x in parts[:3])
    else:
        hh, ss, ll = float(parts[0]) % 360 / 30, pct(parts[1], 1), pct(parts[2], 1)
        f = lambda n: ll - ss * min(ll, 1 - ll) * max(-1, min((n + hh) % 12 - 3, 9 - (n + hh) % 12, 1))
        r, g, b = (f(n) * 255 for n in (0, 8, 4))
    out = "#" + "".join("%02x" % max(0, min(255, round(c))) for c in (r, g, b))
    return out if a >= 1 else out + "%02x" % round(a * 255)


def tok(value, typ, source, **ext):
    if typ == "color" and isinstance(value, str) and not value.startswith("{"):
        hexed = to_hex(value)
        if hexed != value.strip().lower():
            ext = {**ext, "declared": value.strip()}
        value = hexed
    out = {"$value": value, "$type": typ, "$extensions": {"source": source}}
    out["$extensions"].update(ext)
    return out


def camel_path(name: str) -> list[str]:
    """--smtcColorBgBrand -> ['bg', 'brand']. The core/smtc/comp prefix is the group."""
    body = re.sub(r"^--(?:smtc|core|comp)", "", name)
    # Drop the group word already implied by where the token is filed.
    body = re.sub(r"^(Color|FontFamily|FontWeight|FontSize|LineHeight|Spacing|BorderRadius|BorderWidth|Typography)", "", body)
    parts = re.findall(r"[A-Z]?[a-z0-9]+|[A-Z]+(?![a-z])", body)
    return [p[:1].lower() + p[1:] for p in parts if p]


def norm_color(value: str) -> str:
    v = value.strip().lower()
    v = re.sub(r"\s+", "", v)
    if v.startswith("hsla("):
        # keep as declared; alias matching uses the dump's own spelling
        return value.strip()
    return v


def color_key(name: str) -> str:
    if name.startswith("--corePurple") or name.startswith("--coreYellow"):
        body = name[len("--core"):]
    else:
        body = name[len("--coreColor"):] if name.startswith("--coreColor") else name
    parts = re.findall(r"[A-Z]?[a-z0-9]+|[A-Z]+(?![a-z])", body)
    return "-".join(p[:1].lower() + p[1:] for p in parts if p)


def core_color_index() -> dict[str, str]:
    index = {}
    for name, value in ROOT.items():
        if not name.startswith("--coreColor") and not name.startswith("--corePurple") and not name.startswith("--coreYellow"):
            continue
        if not re.search(r"#[0-9a-fA-F]{3,8}|rgba?\(", value):
            continue
        index.setdefault(norm_color(value), "core.color." + color_key(name))
    return index


COLOR_INDEX = core_color_index()


def color_token(value: str, source: str):
    key = norm_color(value)
    if key in COLOR_INDEX and not value.strip().startswith("{"):
        return tok("{" + COLOR_INDEX[key] + "}", "color", SRC_ALIAS, declared=value.strip())
    return tok(value.strip(), "color", source)


def dim(value: str):
    return tok(value.strip(), "dimension", SRC)


def split_shorthand(value: str) -> dict | None:
    """400 16px/150% \"Trip Geom\" or 700 40px/125% \"Trip Geom\"."""
    m = re.fullmatch(
        r"\s*(\d+)\s+([\d.]+px)\s*/\s*([\d.]+(?:px|%))\s+(.+?)\s*",
        value,
    )
    if not m:
        return None
    weight, size, line, family = m.groups()
    family = family.strip().strip('"')
    line_value = line if line.endswith("px") else round(float(line[:-1]) / 100, 4)
    return {
        "fontFamily": FONT if "Trip Geom" in family else family,
        "fontWeight": int(weight),
        "fontSize": size,
        "lineHeight": line_value if isinstance(line_value, float) else line,
    }


def build() -> dict:
    core: dict = {"color": {}, "font": {}, "space": {}, "radius": {}, "border": {}, "typography": {}, "shadow": {}}
    light: dict = {"color": {}, "component": {}, "shadow": {}}

    for name, value in sorted(ROOT.items()):
        if name.startswith("--coreColor") or name.startswith("--corePurple") or name.startswith("--coreYellow"):
            if re.search(r"#[0-9a-fA-F]{3,8}|rgba?\(|hsla?\(|transparent", value):
                core["color"][color_key(name)] = tok(value.strip(), "color", SRC, css=name)
        elif name.startswith("--coreSpacing") and "Negative" not in name and name != "--coreSpacingNone":
            core["space"]["-".join(camel_path(name))] = dim(value)
            core["space"]["-".join(camel_path(name))]["$extensions"]["css"] = name
        elif name.startswith("--coreBorderRadius"):
            core["radius"]["-".join(camel_path(name))] = dim(value)
            core["radius"]["-".join(camel_path(name))]["$extensions"]["css"] = name
        elif name.startswith("--coreBorderWidth"):
            core["border"]["-".join(camel_path(name))] = dim(value)
            core["border"]["-".join(camel_path(name))]["$extensions"]["css"] = name
        elif name.startswith("--coreFontWeight"):
            core["font"]["-".join(camel_path(name))] = tok(int(value), "fontWeight", SRC, css=name)
        elif name.startswith("--coreFontFamily"):
            core["font"]["-".join(camel_path(name))] = tok(value.strip().strip('"'), "fontFamily", SRC, css=name)

    core["font"]["stack"] = tok(FONT, "fontFamily", SRC, css="computed html font-family")

    # Desktop type roles actually named as Trip Geom shorthands.
    type_names = [
        "--smtcBodyXs", "--smtcBodyS", "--smtcBodyM", "--smtcBodyL",
        "--smtcDisplayS", "--smtcDisplayM", "--smtcDisplayL",
        "--smtcTypographyBodyEmphasizedXs", "--smtcTypographyBodyEmphasizedS",
        "--smtcTypographyBodyEmphasizedM", "--smtcTypographyBodyEmphasizedL",
        "--smtcTypographyHeadingXs", "--smtcTypographyHeadingS",
        "--smtcTypographyHeadingM", "--smtcTypographyHeadingL",
        "--smtcTypographyHeadingXl", "--smtcTypographyHeading2Xl",
        "--smtcTypographyHeading3Xl",
        "--smtcTypographyResidualS", "--smtcTypographyResidualSEmphasized",
        "--smtcTypographyResidualM", "--smtcTypographyResidualL",
        "--smtcTypographyResidualXl", "--smtcTypographyResidual2Xl",
        "--smtcTypographyResidual2XlStrong",
    ]
    for name in type_names:
        parts = split_shorthand(ROOT[name])
        if not parts:
            continue
        key = "-".join(camel_path(name))
        core["typography"][key] = tok(parts, "typography", SRC_TYPE, css=name, declared=ROOT[name])

    # Semantic colours. Keep the product name under light.color.
    for name, value in sorted(ROOT.items()):
        if not name.startswith("--smtcColor"):
            continue
        light["color"]["-".join(camel_path(name))] = color_token(value, SRC)
        light["color"]["-".join(camel_path(name))]["$extensions"]["css"] = name

    # Component tokens that are colours, dimensions, or numbers.
    for name, value in sorted(COMP.items()):
        path = camel_path(name)
        if not path:
            continue
        key = "-".join(path)
        v = value.strip()
        if re.search(r"#[0-9a-fA-F]{3,8}|rgba?\(|hsla?\(|transparent", v) and "linear" not in v and " " not in v:
            light["component"][key] = color_token(v, SRC_COMP)
        elif re.fullmatch(r"-?[\d.]+px", v):
            light["component"][key] = tok(v, "dimension", SRC_COMP)
        elif re.fullmatch(r"\d+", v):
            light["component"][key] = tok(int(v), "number", SRC_COMP)
        else:
            light["component"][key] = tok(v, "other", SRC_COMP)
        light["component"][key]["$extensions"]["css"] = name

    # Computed elevation, not in the custom-property dump.
    light["shadow"]["search-card"] = tok(
        # The first layer's computed colour is rgba(7, 20, 60, 0.16), not the palette's
        # neutral-black-a16 rgba(0, 0, 0, 0.16) it was once aliased to.
        "0px 0px 4px 0px rgba(7, 20, 60, 0.16), 0px 8px 32px 0px rgba(7, 20, 60, 0.12)",
        "shadow",
        SRC_SHADOW,
        element=".mc-srh-box.experiment-e",
        computed="rgba(7, 20, 60, 0.16) 0px 0px 4px 0px, rgba(7, 20, 60, 0.12) 0px 8px 32px 0px",
    )
    light["shadow"]["coupon-card"] = tok(
        "0px 4px 16px 0px {core.color.neutral5-a8}",
        "shadow",
        SRC_SHADOW,
        element=".online-mkm-coupon-content-card",
        computed="rgba(18, 24, 38, 0.08) 0px 4px 16px 0px",
        note="0.08 alpha is close to neutral5-a8's 0.08 of #989eab; the computed colour is rgba(18, 24, 38, 0.08), which is not an exact core token. Stored as the computed string.",
    )
    # Fix coupon: do not alias a non-match.
    light["shadow"]["coupon-card"] = tok(
        "0px 4px 16px 0px rgba(18, 24, 38, 0.08)",
        "shadow",
        SRC_SHADOW,
        element=".online-mkm-coupon-content-card",
    )
    light["shadow"]["language-popover"] = tok(
        "0px 8px 16px 0px rgba(15, 41, 77, 0.08)",
        "shadow",
        SRC_SHADOW,
        element=".online-language-match-content",
    )
    light["shadow"]["hotel-card"] = tok(
        "0px 2px 6px 0px rgba(0, 0, 0, 0.08)",
        "shadow",
        "Measured. Computed box-shadow on .hotel-recommend-card-default at https://sg.trip.com/hotels/, 2026-11-19.",
        element=".hotel-recommend-card-default",
    )

    # States read off live controls, not only the token sheet.
    light["component"]["button-primary-hover-background"] = tok(
        "#2953d6",
        "color",
        SRC_STATE,
        selector=".tripui-online-btn-solid-primary:hover:not(:disabled)",
        declared="rgb(41, 83, 214)",
    )
    light["component"]["button-primary-active-background"] = tok(
        "#2346ff",
        "color",
        "Measured. Computed background of the header Sign in/register control's hover rule .mc-lhd-login-btn:hover is rgb(44, 89, 229). The search button rest state is rgb(44, 97, 254).",
        selector=".mc-lhd-head-menu .mc-lhd-menu-account .mc-lhd-login-btn:hover",
        declared="rgb(44, 89, 229)",
    )
    # The login hover is a different blue. Keep it exact; drop the invented #2346ff.
    light["component"]["button-primary-active-background"]["$value"] = "#2c59e5"
    light["component"]["button-disabled-filled-background"] = tok(
        "#ced2d9",
        "color",
        "Measured. Computed background of the disabled Continue with email button on /account/signin. The --compButtonDisabledFilledBackgroundColor token is #b9bec7; the painted control does not use it.",
        element="button.tripui-online-btn-solid-primary[disabled]",
        declared="rgb(206, 210, 217)",
    )
    light["component"]["textinput-focus-border"] = tok(
        "{light.color.bg-brand}",
        "color",
        "Measured. Computed border-top-color of the focused email field on /account/signin is rgb(44, 97, 254), which matches --smtcColorBgBrand.",
        element="input.input-module__base-input (focused)",
    )
    light["component"]["search-field-border"] = tok(
        "#dadfe6",
        "color",
        "Measured. Computed border of the home search field row (.z5SApYdkQdnm44Bv3aS2) at innerWidth 1169 is rgb(218, 223, 230). Not equal to --smtcColorBorderDefault #d4d7de.",
        element=".z5SApYdkQdnm44Bv3aS2",
    )
    light["component"]["support-hero-background"] = tok(
        "{core.color.cyan6}",
        "color",
        "Measured. Computed background of .onlineCS-headBanner on /pages/support/ is rgb(4, 124, 136).",
        element=".onlineCS-headBanner",
    )
    light["component"]["footer-background"] = tok(
        "#f5f7fa",
        "color",
        "Measured. Computed background of footer.mc-ft on the home page is rgb(245, 247, 250). Not equal to --smtcColorBgPage #ebedf1 or --coreColorNeutral1 #f6f7fa.",
        element="footer.mc-ft",
    )
    light["component"]["hotels-page-background"] = tok(
        "{core.color.neutral1}",
        "color",
        "Measured. Computed background of body.ibu-hotel-online-tripgeom on /hotels/ is rgb(246, 247, 250).",
        element="body.ibu-hotel-online-tripgeom",
    )
    light["component"]["signin-panel-background"] = tok(
        "{core.color.white}",
        "color",
        "Measured. Computed background of the sign-in card left panel on /account/signin.",
        element=".NpZ53",
    )
    light["component"]["signin-aside-background"] = tok(
        "{core.color.neutral1}",
        "color",
        "Measured. Computed background of the sign-in QR aside on /account/signin is rgb(246, 247, 250).",
        element=".Z8ALB",
    )
    light["component"]["google-button-background"] = tok(
        "#4285f4",
        "color",
        "Measured. Computed background of Continue with Google on /account/signin is rgb(66, 133, 244). A vendor colour, not a Trip core token.",
        element="button Continue with Google",
    )
    light["component"]["tab-active-text"] = tok(
        "{light.color.text-brand}",
        "color",
        "Measured. Computed color of .mc-srh-box__tab-item.is-active .mc-srh-box__tab-name is rgb(44, 97, 254).",
        element=".mc-srh-box__tab-name (active)",
    )
    light["component"]["tab-hover-text"] = tok(
        "{light.color.text-brand}",
        "color",
        "Measured. Stylesheet rule .experiment-e .mc-srh-box__tab-item:hover .mc-srh-box__tab-name sets color to var(--smtcColorTextBrand, #2c61fe).",
        selector=".experiment-e .mc-srh-box__tab-item:hover .mc-srh-box__tab-name",
    )
    light["component"]["faq-chip-background"] = tok(
        "#f5f7fa",
        "color",
        "Measured. Computed background of a.faq-item on /pages/support/ is rgb(245, 247, 250).",
        element="a.faq-item",
    )
    light["component"]["hero-title"] = tok(
        "700 40px/48px " + FONT,
        "other",
        "Measured. Computed font of .slogan-desc on the home page at innerWidth 1440: 700 40px/48px Trip Geom, color rgb(255, 255, 255).",
        element=".slogan-desc",
    )
    light["component"]["hotels-h1"] = tok(
        "700 48px/48px " + FONT,
        "other",
        "Measured. Computed font of h1 on /hotels/: 700 48px/48px Trip Geom, color rgb(255, 255, 255).",
        element="h1",
    )
    light["component"]["support-h1"] = tok(
        "700 48px/68px " + FONT,
        "other",
        "Measured. Computed font of h1 on /pages/support/: 700 48px/68px Trip Geom, color rgb(255, 255, 255). 68px matches --coreLineHeightT56.",
        element="h1",
    )

    return {
        "core": core,
        "light": light,
        "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    }


def main() -> None:
    data = build()
    path = HERE / "tokens.json"
    path.write_text(json.dumps(data, indent=2) + "\n")
    n = sum(1 for _ in _walk(data))
    print(f"wrote {path} ({n} tokens)")


def _walk(node):
    if isinstance(node, dict) and "$value" in node:
        yield node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from _walk(v)


if __name__ == "__main__":
    main()
