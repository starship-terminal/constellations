#!/usr/bin/env python3
"""Build tokens.json from the Workflow marketing readings in raw/.

Read on 2026-11-19 from signed-out pages in the T3 preview browser:

  raw/css-vars.json              computed custom properties on
                                 https://www.workflow.design/
  raw/components-computed.json   computed styles of the visible controls

The marketing site declares one light set on :root. No dark override was
present, so there is no dark set. Prices are not tokens.

Every token carries $extensions.source. A value the browser computed is
Measured. An alias to another token is Derived. Deterministic: same inputs,
same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())["computed"]
COMP = json.loads((RAW / "components-computed.json").read_text())["controls"]

SRC = (
    "Computed custom property on documentElement, "
    "https://www.workflow.design/, 2026-11-19, viewport 1169x731"
)
SRC_EL = (
    "Computed style, https://www.workflow.design/, resting, 2026-11-19"
)


def src(note):
    return {"source": note}


def color(value, note):
    return {"$type": "color", "$value": value, "$extensions": src(note)}


def dim(value, note):
    return {"$type": "dimension", "$value": value, "$extensions": src(note)}


def font(value, note):
    return {"$type": "fontFamily", "$value": value, "$extensions": src(note)}


def typography(family, size, weight, line_height, note, tracking=None):
    value = {
        "fontFamily": family,
        "fontSize": size,
        "fontWeight": weight,
        "lineHeight": line_height,
    }
    if tracking:
        value["letterSpacing"] = tracking
    return {"$type": "typography", "$value": value, "$extensions": src(note)}


def alias(path, note):
    return {"$type": "color", "$value": "{" + path + "}", "$extensions": src(note)}


def main():
    core = {
        "color": {
            "black": color("#1a1a1a", SRC + "; --color--base--black"),
            "white": color("#ffffff", SRC + "; --color--base--white computed white"),
            "black-10": color("#1a1a1a1a", SRC + "; --color--base--black-10"),
            "black-30": color("#1a1a1a4d", SRC + "; --color--base--black-30"),
            "black-50": color("#1a1a1a80", SRC + "; --color--base--black-50"),
            "black-70": color("#1a1a1ab3", SRC + "; --color--base--black-70"),
            "black-80": color("#1a1a1acc", SRC + "; --color--base--black-80"),
            "page": color("#f6f4f0", SRC + "; --color--surface--page"),
            "surface": color("#ffffff", SRC + "; --color--surface--default"),
            "surface-light": color("#f9f9f9", SRC + "; --color--surface--light"),
            "surface-medium": color("#f6f6f6", SRC + "; --color--surface--medium"),
            "surface-secondary": color("#f3f3f3", SRC + "; --color--surface--secondary"),
            "surface-strong": color("#ececec", SRC + "; --color--surface--strong"),
            "invert": color("#1a1a1a", SRC + "; --color--surface--invert"),
            "invert-medium": color("#1a1a1acc", SRC + "; --color--surface--invert-medium"),
            "invert-strong": color("#1a1a1a80", SRC + "; --color--surface--invert-strong"),
            "text": color("#1a1a1a", SRC + "; --color--text--default"),
            "text-weak": color("#1a1a1aa6", SRC + "; --color--text--weak"),
            "text-disabled": color("#1a1a1a4d", SRC + "; --color--text--disabled"),
            "text-invert": color("#f6f6f6", SRC + "; --color--text--invert"),
            "text-invert-weak": color("#f6f6f6a6", SRC + "; --color--text--invert-weak"),
            "border": color("#1a1a1a1f", SRC + "; --color--border--default"),
            "border-weak": color("#1a1a1a0f", SRC + "; --color--border--weak"),
            "border-hover": color("#1a1a1a33", SRC + "; --color--border--hover"),
            "border-active": color("#1a1a1acc", SRC + "; --color--border--active"),
            "error-surface": color("#faebed", SRC + "; --color--error--surface"),
            "error-surface-hover": color("#f6dbe0", SRC + "; --color--error--surface-hover"),
            "error-surface-active": color("#f1c8ce", SRC + "; --color--error--surface-active"),
            "error-border": color("#d99ba4", SRC + "; --color--error--border"),
            "error-border-hover": color("#ce6878", SRC + "; --color--error--border-hover"),
            "error-text": color("#923d56", SRC + "; --color--error--text"),
            "error-text-hover": color("#8a3853", SRC + "; --color--error--text-hover"),
            "error-icon": color("#923d56", SRC + "; --color--error--icon"),
            "success-surface": color("#f1fcf6", SRC + "; --color--success--surface"),
            "success-surface-medium": color("#e9f6ee", SRC + "; --color--success--surface-medium"),
            "success-surface-strong": color("#c4e6d5", SRC + "; --color--success--surface-strong"),
            "success-border": color("#9dbfad", SRC + "; --color--success--border"),
            "success-border-weak": color("#74a486", SRC + "; --color--success--border-weak"),
            "success-text": color("#547e69", SRC + "; --color--success--text"),
            "success-text-weak": color("#60886f", SRC + "; --color--success--text-weak"),
            "success-icon": color("#547e69", SRC + "; --color--success--icon"),
            "overlay-30": color("#0000004d", SRC + "; --color--overlay--30"),
            "overlay-50": color("#00000080", SRC + "; --color--overlay--50"),
            "overlay-70": color("#000000b3", SRC + "; --color--overlay--70"),
            "shadow-comment": color("#1a1a1a14", SRC + "; --color--shadow--comment"),
            "shadow-comment-dark": color("#1a1a1a21", SRC + "; --color--shadow--comment-dark"),
            "logo": color(
                "#0f0f0e",
                "Fill declared in the marketing wordmark SVG, icons/logo.svg, 2026-11-19",
            ),
            "focus-play": color(
                "#3b79c3",
                "Declared outline-color on .w-backgroundvideo-backgroundvideoplaypausebutton:focus-visible",
            ),
        },
        "font": {
            "body": font(
                "Inter, Arial, sans-serif",
                SRC + "; --type--body",
            ),
            "display": font(
                "Crimson Pro, Times New Roman, sans-serif",
                SRC + "; --type--display",
            ),
        },
        "typography": {
            "body": typography(
                "{font.body}", "14px", 400, "21px",
                SRC_EL + "; body",
            ),
            "card-title": typography(
                "{font.body}", "15px", 400, "22px",
                SRC_EL + "; h3.features_card-heading-lead",
            ),
            "eyebrow": typography(
                "{font.body}", "14px", 400, "19.6px",
                SRC_EL + "; h1.content-text-top-subhead on /pricing, color is text-weak",
            ),
            "display": typography(
                "{font.display}", "32px", 300, "32px",
                SRC_EL + "; h1.heading-style-h2 on the home page",
            ),
            "display-features": typography(
                "{font.display}", "60.992px", 300, "60.992px",
                SRC_EL + "; h1 on /features at 1169px. The size is the computed value, not a round token.",
            ),
            "price": typography(
                "{font.display}", "32px", 300, "21px",
                SRC_EL + "; .pricing--price-yearly, letter-spacing -1.6px",
                tracking="-1.6px",
            ),
        },
        "radius": {
            "small": dim("4px", SRC + "; --radius--small"),
            "medium": dim("8px", SRC + "; --radius--medium"),
            "large": dim("12px", SRC + "; --radius--large"),
            "full": dim("9999px", SRC + "; --radius--full"),
            "approve": dim(
                "5px",
                SRC_EL + "; .workflow--app-toolbarbutton-approve in the marketing demo",
            ),
            "switch": dim(
                "24px",
                SRC_EL + "; .toggle in the marketing demo",
            ),
        },
        "space": {
            "3xs": dim("4px", SRC + "; --space--3xs"),
            "2xs": dim("8px", SRC + "; --space--2xs"),
            "xs": dim("12px", SRC + "; --space--xs"),
            "sm": dim("16px", SRC + "; --space--sm"),
            "md": dim("24px", SRC + "; --space--md"),
            "lg": dim("32px", SRC + "; --space--lg"),
            "xl": dim("40px", SRC + "; --space--xl"),
            "2xl": dim("48px", SRC + "; --space--2xl"),
            "3xl": dim("72px", SRC + "; --space--3xl"),
            "4xl": dim("80px", SRC + "; --space--4xl"),
            "5xl": dim("112px", SRC + "; --space--5xl"),
            "6xl": dim("144px", SRC + "; --space--6xl"),
        },
        "size": {
            "button": dim("40px", SRC_EL + "; a.button--new height"),
            "button-trial": dim(
                "37px",
                SRC_EL + "; a.button--new.button--dark 'Start your free trial' on /pricing",
            ),
            "skip": dim("44px", SRC_EL + "; a.nav--keyboard-skip height"),
            "tab": dim("48px", SRC_EL + "; a.auto-tabs_tab height"),
            "chip": dim("32px", SRC_EL + "; .features--jump-item height"),
            "nav": dim("83px", SRC_EL + "; nav.nav--new height at 1169px"),
            "switch": dim("24px", SRC_EL + "; .toggle height in the marketing demo"),
            "switch-width": dim("42px", SRC_EL + "; .toggle width in the marketing demo"),
            "pricing-toggle": dim("16px", SRC_EL + "; .pricing--toggle-new height"),
            "pricing-toggle-width": dim("28px", SRC_EL + "; .pricing--toggle-new width"),
        },
        "border": {
            "chip": dim("1px", SRC_EL + "; .features--jump-item border-top-width"),
        },
        "motion": {
            "button": {
                "$type": "duration",
                "$value": "200ms",
                "$extensions": src(
                    SRC_EL + "; a.button--new transition background-color 0.2s"
                ),
            },
            "button-easing": {
                "$type": "cubicBezier",
                "$value": [0.455, 0.03, 0.515, 0.955],
                "$extensions": src(
                    SRC_EL + "; a.button--new transition-timing-function"
                ),
            },
        },
    }
    light = {
        "background": {
            "page": alias("color.white", "Derived from body background rgb(255, 255, 255)"),
            "canvas": alias("color.page", "Derived from --color--surface--page"),
            "surface": alias("color.surface", "Derived from --color--surface--default"),
            "muted": alias("color.surface-medium", "Derived from --color--surface--medium"),
            "invert": alias("color.invert", "Derived from --color--surface--invert"),
        },
        "text": {
            "primary": alias("color.text", "Derived from --color--text--default"),
            "secondary": alias("color.text-weak", "Derived from --color--text--weak"),
            "disabled": alias("color.text-disabled", "Derived from --color--text--disabled"),
            "on-invert": alias("color.text-invert", "Derived from --color--text--invert"),
            "error": alias("color.error-text", "Derived from --color--error--text"),
            "success": alias("color.success-text", "Derived from --color--success--text"),
        },
        "border": {
            "default": alias("color.border", "Derived from --color--border--default"),
            "strong": alias("color.border-active", "Derived from --color--border--active"),
            "focus": alias(
                "color.invert",
                "Derived from a:focus-visible outline-color var(--color--surface--invert)",
            ),
        },
        "button": {
            "secondary": alias(
                "color.surface-medium",
                "Derived from a.button--new background rgb(246, 246, 246)",
            ),
            "secondary-text": alias("color.text", "Derived from a.button--new color"),
            "dark": alias("color.invert", "Derived from a.button--dark background"),
            "dark-text": alias("color.text-invert", "Derived from a.button--dark color"),
        },
        "status": {
            "approve": color(
                "#e9f6ee",
                SRC_EL + "; .workflow--app-toolbarbutton-approve background rgb(233, 246, 238)",
            ),
            "approve-text": color(
                "#547e69",
                SRC_EL + "; approve badge color rgb(84, 126, 105)",
            ),
            "switch-on": color(
                "#60886f",
                SRC_EL + "; .toggle background rgb(96, 136, 111) in the marketing demo",
            ),
        },
    }
    doc = {
        "core": core,
        "light": light,
        "$themes": [
            {
                "id": "light",
                "name": "Light",
                "selectedTokenSets": {"core": "source", "light": "enabled"},
            }
        ],
    }
    unused = [k for k in VARS if k.startswith("--legacy")]
    doc["$extensions"] = {
        "notTokenised": [
            "Legacy custom properties (" + ", ".join(sorted(unused)) + ") repeat the current palette or name unused greys (#353532, #555, #797979, #e3e3e3). They are in raw/css-vars.json and are not tokens.",
            "a.nav--menu.w-button computed rgb(56, 152, 236). That is Webflow's default menu button, height 0 at 1169px, not a Workflow colour.",
            "Prices on /pricing ($16 yearly, $20 monthly) are not tokens.",
        ]
    }
    check(doc)
    out = HERE / "tokens.json"
    out.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"wrote {out}")


# ---------------------------------------------------------------- check (finding 16-6)

def _token_paths(node, path=""):
    for key, value in node.items():
        if key.startswith("$") or not isinstance(value, dict):
            continue
        if "$value" in value:
            yield f"{path}{key}", value
        else:
            yield from _token_paths(value, f"{path}{key}.")


def _aliases(value):
    if isinstance(value, str):
        return re.findall(r"\{([^{}]+)\}", value)
    if isinstance(value, dict):
        return [a for v in value.values() for a in _aliases(v)]
    if isinstance(value, list):
        return [a for v in value for a in _aliases(v)]
    return []


def _follow(flat, s, ref, seen):
    """Follow an alias chain: each name resolves in the set it is read from, then core, then the
    root (the Resolver's order). Returns a problem string for a dead alias or a repeated token,
    else None."""
    # Own set, then core, then the root, where a set-qualified name such as core.color.white.solid
    # names a token in that set. The next hop resolves from the set the target was found in.
    candidates = [(s, ref), ("core", ref)]
    if "." in ref:
        candidates.append(tuple(ref.split(".", 1)))
    found = next(((fs, fp) for fs, fp in candidates if fp in flat.get(fs, {})), None)
    if found is None:
        return f"alias {{{ref}}} resolves nowhere"
    if found in seen:
        return f"alias loop through {{{ref}}}"
    target_set, target_path = found
    for nxt in _aliases(flat[target_set][target_path]["$value"]):
        err = _follow(flat, target_set, nxt, seen | {found})
        if err:
            return err
    return None


def check(doc):
    """Refuse a token with no source, a colour that is neither #rrggbb(aa) nor one whole alias, an
    alias that resolves in neither its own set nor core (the order tools/catalog.py's Resolver
    uses), and an alias chain that comes back to a token it already passed. Raises SystemExit."""
    sets = [s for s, v in doc.items() if not s.startswith("$") and isinstance(v, dict)]
    flat = {s: dict(_token_paths(doc[s])) for s in sets}
    core = flat.get("core", {})
    problems = []
    for s in sets:
        for path, token in flat[s].items():
            where = f"{s}.{path}"
            if not token.get("$extensions", {}).get("source"):
                problems.append(f"{where}: no source")
            value = token["$value"]
            for ref in _aliases(value):
                err = _follow(flat, s, ref, {(s, path)})
                if err:
                    problems.append(f"{where}: {err}")
            if token.get("$type") == "color":
                whole_alias = isinstance(value, str) and re.fullmatch(r"\{[^{}]+\}", value)
                if not whole_alias and not (isinstance(value, str) and re.fullmatch(r"#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?", value)):
                    problems.append(f"{where}: colour {value!r} is not #rrggbb(aa) or one whole alias")
    if problems:
        raise SystemExit("token check failed:\n" + "\n".join(problems))


if __name__ == "__main__":
    main()
