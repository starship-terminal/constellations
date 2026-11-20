#!/usr/bin/env python3
"""Build tokens.json from Rivian's measured public-site tokens.

Source: raw/css-vars.json and raw/components-computed.json, read on
https://rivian.com/ on 2026-11-19, signed out. One light theme. Colour
values are the probe-resolved computed colours, not guesses. Component
sizes that differ from the declared scale stay in the component group.

Deterministic. Edit the raw input, never tokens.json.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
COMP = json.loads((HERE / "raw" / "components-computed.json").read_text())
SRC = "declared custom property on rivian.com, resolved to computed sRGB, 2026-11-19"
COMP_SRC = "computed style on the live DOM, rivian.com, 2026-11-19"


def color(value, name):
    return {
        "$type": "color",
        "$value": value,
        "$extensions": {"source": f"{SRC}; {name}"},
    }


def dim(value, name, source=SRC):
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": f"{source}; {name}"},
    }


def duration(value, name):
    return {
        "$type": "duration",
        "$value": value,
        "$extensions": {"source": f"{SRC}; {name}"},
    }


def easing(value, name):
    nums = [float(x) for x in value.replace("cubic-bezier(", "").rstrip(")").replace(" ", "").split(",")]
    return {
        "$type": "cubicBezier",
        "$value": nums,
        "$extensions": {"source": f"{SRC}; {name}"},
    }


def shadow(value, name):
    return {
        "$type": "shadow",
        "$value": value,
        "$extensions": {"source": f"{SRC}; {name}"},
    }


def font(stack, name):
    return {
        "$type": "fontFamily",
        "$value": stack,
        "$extensions": {"source": f"{COMP_SRC}; {name}"},
    }


def typography(size, weight, line, family, name, tracking=None):
    value = {
        "fontFamily": family,
        "fontSize": size,
        "fontWeight": weight,
        "lineHeight": line,
    }
    if tracking:
        value["letterSpacing"] = tracking
    return {
        "$type": "typography",
        "$value": value,
        "$extensions": {"source": f"{SRC}; {name}"},
    }


def number(value, name):
    return {
        "$type": "number",
        "$value": value,
        "$extensions": {"source": f"{SRC}; {name}"},
    }


def main():
    r = RAW["resolved"]
    d = RAW["dimensions"]
    m = RAW["motion"]
    core = {
        "font": {
            "family": {
                "adventure": font(
                    ["Adventure", "Helvetica Neue", "Helvetica", "Arial", "sans-serif"],
                    "computed font-family on body and header at rivian.com/",
                ),
                "adventure-font": font(
                    ["adventureFont", "ui-sans-serif", "system-ui", "sans-serif"],
                    "computed font-family on h1 and buttons at rivian.com/r2",
                ),
                "mono": font(
                    ["Adventure Mono", "ui-monospace", "monospace"],
                    "--font-adventure-mono declared Adventure Mono; not computed on a specimen",
                ),
            }
        },
        "typography": {
            "body": typography(
                d["--text-base"], 400, d["--text-base--line-height"],
                "{core.font.family.adventure}", "--text-base 16px / --text-base--line-height 24px",
                d["--tracking-body"],
            ),
            "body-sm": typography(
                d["--text-sm"], 400, d["--text-sm--line-height"],
                "{core.font.family.adventure}", "--text-sm 14px / 20px",
                d["--tracking-body"],
            ),
            "label": typography(
                d["--text-sm"], 600, "16px",
                "{core.font.family.adventure}",
                "computed on Vehicles nav button: 14px / 16px weight 600 letter-spacing -0.14px",
                "-0.14px",
            ),
            "button": typography(
                d["--text-base"], 600, "18px",
                "{core.font.family.adventure-font}",
                "computed on R2 Reserve: 16px / 18px weight 600 letter-spacing -0.16px",
                "-0.16px",
            ),
            "headline": typography(
                d["--text-4xl"], 600, d["--text-4xl"],
                "{core.font.family.adventure-font}",
                "computed on R2 'Explore the lineup': 44px / 44px weight 600",
                "-0.88px",
            ),
            "display": typography(
                d["--text-6xl"], 600, d["--text-6xl"],
                "{core.font.family.adventure}",
                "computed on home h1 'Find your Rivian': 72px / 72px weight 600",
                "-3px",
            ),
        },
        "radius": {
            "nano": dim(d["--radius-nano"], "--radius-nano"),
            "micro": dim(d["--radius-micro"], "--radius-micro"),
            "macro": dim(d["--radius-macro"], "--radius-macro"),
            "mega": dim(d["--radius-mega"], "--radius-mega"),
            "s": dim(d["--radius-s"], "--radius-s"),
            "m": dim(d["--radius-m"], "--radius-m"),
            "l": dim(d["--radius-l"], "--radius-l"),
            "xl": dim(d["--radius-xl"], "--radius-xl"),
            "xxl": dim(d["--radius-xxl"], "--radius-xxl"),
            "pill": dim("9999px", "computed border-radius on Demo drive and Vehicles", COMP_SRC),
        },
        "space": {
            "1": dim(d["--spacing"], "--spacing"),
            "xxs": dim(d["--gap-xxs"], "--gap-xxs"),
            "xs": dim(d["--gap-xs"], "--gap-xs"),
            "s": dim(d["--gap-s"], "--gap-s"),
            "m": dim(d["--gap-m"], "--gap-m"),
            "l": dim(d["--gap-l"], "--gap-l"),
            "xl": dim(d["--gap-xl"], "--gap-xl"),
            "s3": dim(d["--small-s3"], "--small-s3"),
            "m2": dim(d["--medium-m2"], "--medium-m2"),
            "l1": dim(d["--large-l1"], "--large-l1"),
            "l2": dim(d["--large-l2"], "--large-l2"),
            "l3": dim(d["--large-l3"], "--large-l3"),
        },
        "control": {
            "nav-height": dim("32px", "computed height of Vehicles", COMP_SRC),
            "header-height": dim(d["--header-height"], "--header-height"),
            "hero-button-height": dim("56px", "computed height of Design yours and Reserve", COMP_SRC),
            "field-height": dim("56px", "computed height of login email and password", COMP_SRC),
            "icon-size": dim(d["--navbar-icon-size"], "--navbar-icon-size"),
            "target-size": dim(d["--target-size"], "--target-size"),
            "button-px": dim(d["--button-px"], "--button-px"),
        },
        "motion": {
            "duration": {
                "nav": duration("150ms", "computed transition-duration on Vehicles; --card-duration"),
                "card": duration(m["--card-duration"], "--card-duration"),
                "accordion": duration(m["--accordion-duration"], "--accordion-duration"),
            },
            "easing": {
                "shift-magnetic": easing(m["--ease-shift-magnetic"], "--ease-shift-magnetic"),
                "attract-standard": easing(m["--ease-attract-standard"], "--ease-attract-standard"),
                "attract-enter": easing(m["--ease-attract-enter"], "--ease-attract-enter"),
                "repel-exit": easing(m["--ease-repel-exit"], "--ease-repel-exit"),
            },
        },
        "shadow": {
            "nav": shadow(RAW["shadows"]["--shadow-nav"], "--shadow-nav"),
            "base": shadow(RAW["shadows"]["--shadow-base"], "--shadow-base"),
            "hero": shadow(RAW["shadows"]["--shadow-hero"], "--shadow-hero"),
        },
        "leading": {
            "display": number(0.96, "--leading-display"),
            "headline": number(1, "--leading-headline"),
        },
    }
    light = {
        "page": color(r["--background"], "--background"),
        "surface": color(r["--surface-secondary"], "--surface-secondary"),
        "surface-alt": color(r["--surface-primaryAlt"], "--surface-primaryAlt"),
        "text": color(r["--text-primary"], "--text-primary"),
        "muted": color(r["--text-secondary"], "--text-secondary"),
        "muted-soft": color(r["--muted-foreground"], "--muted-foreground"),
        "accent": color(r["--brand"], "--brand"),
        "accent-hover": color(r["--brand-accent"], "--brand-accent"),
        "on-accent": color(r["--brand-foreground"], "--brand-foreground"),
        "primary": color(r["--primary"], "--primary"),
        "on-primary": color(r["--primary-foreground"], "--primary-foreground"),
        "primary-accent": color(r["--primary-accent"], "--primary-accent"),
        "border": color(r["--border"], "--border"),
        "stroke": color(r["--stroke-tertiary"], "--stroke-tertiary"),
        "focus": color(r["--ring"], "--ring"),
        "link": color(r["--text-primary"], "--text-primary; legal links computed as underlined black text"),
        "destructive": color(r["--destructive"], "--destructive"),
        "on-destructive": color(r["--destructive-foreground"], "--destructive-foreground"),
        "info": color(r["--info"], "--info"),
        "success": color(r["--success"], "--success"),
        "warning": color(r["--warning"], "--warning"),
        "error": color(r["--semantic-error"], "--semantic-error"),
        "disabled": color(r["--semantic-disabled"], "--semantic-disabled"),
        "scrim": color("#00000080", "--overlay resolved rgba(0,0,0,0.5)"),
        "nav-open": color("#0000001a", "--accent resolved rgba(0,0,0,0.1); computed on open Vehicles"),
        "input": color(r["--input"], "--input"),
        "cloud": color(r["--cloud"], "--cloud"),
        "inverse": color(r["--surface-invertPrimary"], "--surface-invertPrimary"),
        "on-inverse": color(r["--text-invertPrimary"], "--text-invertPrimary"),
        "rivian-green": color(r["--rivian-green"], "--rivian-green"),
        "rivian-orange": color(r["--rivian-orange"], "--rivian-orange"),
        "black-forest": color(r["--black-forest"], "--black-forest"),
        "river-bed": color(r["--river-bed"], "--river-bed"),
        "component": {
            "button-brand-bg": color(COMP["demoDrive"]["backgroundColor"].replace("rgb(255, 170, 0)", "#ffaa00"), "computed background on Demo drive"),
            "button-brand-text": color("#000000", "computed color on Demo drive"),
            "button-primary-bg": color("#000000", "computed background on Reserve and Sign in"),
            "button-primary-text": color("#ffffff", "computed color on Reserve and Sign in"),
            "button-hero-bg": color("#ffffff", "computed background on home Design yours"),
            "field-bg": color("#f5f5f5", "login email computed oklch(0.961 0 0), the same stone as --input"),
            "header-bg": color("#ffffff", "computed background on header"),
            "card-bg": color("#f5f5f5", "navbar vehicle card computed oklch(0.96 0 0)"),
        },
    }
    # Keep the component colours as the hex the probe already resolved, with the
    # computed reading named in the source. The rgb() rewrite above is only for
    # the one value that was stored as rgb().
    light["component"]["button-brand-bg"] = color(
        "#ffaa00", "computed backgroundColor rgb(255, 170, 0) on the Demo drive link"
    )
    doc = {
        "$description": "Rivian public marketing site, rivian.com, signed out, 2026-11-19. One light theme.",
        "core": core,
        "light": light,
        "$themes": [
            {"name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
        ],
    }
    return doc


def write():
    out = HERE / "tokens.json"
    out.write_text(json.dumps(main(), indent=2) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    write()
