#!/usr/bin/env python3
"""Build tokens.json from the Macaw public capture.

Macaw's marketing site is Webflow. Colour roles are custom properties in
macaw-prod.webflow.*.min.css (--gray*, --primary*, --error*, --warning*,
--success*). Component colours were also read as computed styles on
2026-11-18. The public site paints one theme (light). There is no dark set.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))

MOTION = json.loads((RAW / "motion.json").read_text()) if (RAW / "motion.json").exists() else None

CSS = "Authored in macaw-prod.webflow.7735a213d.min.css, fetched 2026-11-18 from cdn.prod.website-files.com"
M = "Measured computed style, public macawhq.com, 2026-11-18, light, 1440"
D = "Derived from the Webflow custom properties and the computed styles on the same capture"


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def shadow(value, source):
    """A computed box-shadow ("0px 1px 2px 0px rgba(...)") as the DTCG shadow object list."""
    m = re.fullmatch(r"(inset )?(-?[\d.]+px) (-?[\d.]+px) ([\d.]+px) (-?[\d.]+px) (#[0-9a-f]{6}|rgba?\([^)]*\))", value)
    if not m:
        raise SystemExit(f"shadow not understood: {value!r}")
    layer = {"color": m.group(6), "offsetX": m.group(2), "offsetY": m.group(3), "blur": m.group(4), "spread": m.group(5)}
    if m.group(1):
        layer["inset"] = True
    return {"$value": [layer], "$type": "shadow", "$extensions": {"source": source}}


# For a value no file in raw/ holds: typed in at capture time (docs/EVIDENCE.md, Reconstruction).
HAND = "Reconstruction: entered by hand at capture time; no file in raw/ holds this reading. Capture note"


def ramp(prefix, steps, note):
    return {step: color(value, f"{CSS}: {prefix}{step} {note}") for step, value in steps.items()}


core = {
    "color": {
        "page": color("#fffdf9", f"{M}: body background-color rgb(255, 253, 249). Not a --gray token."),
        "gray": ramp("--gray", {
            "25": "#fcfcfd",
            "50": "#f9fafb",
            "100": "#f2f4f7",
            "200": "#eaecf0",
            "300": "#d0d5dd",
            "400": "#98a2b3",
            "500": "#667085",
            "600": "#475467",
            "700": "#344054",
            "800": "#1d2939",
            "900": "#101828",
        }, "Webflow gray ramp"),
        "primary": ramp("--primary", {
            "25": "#fff8f8",
            "50": "#fff3f2",
            "100": "#ffe1df",
            "200": "#fbbdb7",
            "300": "#faa29a",
            "400": "#f8887e",
            "500": "#f7786c",
            "600": "#f66658",
            "700": "#de4f30",
            "800": "#cf3e1e",
            "900": "#bc2504",
        }, "coral accent ramp"),
        "error": ramp("--error", {
            "25": "#fffbfa", "50": "#fef3f2", "100": "#fee4e2", "200": "#fecdca",
            "300": "#fda29b", "400": "#f97066", "500": "#f04438", "600": "#d92d20",
            "700": "#b42318", "800": "#912018", "900": "#7a271a",
        }, "error ramp, authored, not painted on the captured pages"),
        "warning": ramp("--warning", {
            "25": "#fffcf5", "50": "#fffaeb", "100": "#fef0c7", "200": "#fedf89",
            "300": "#fec84b", "400": "#fdb022", "500": "#f79009", "600": "#dc6803",
            "700": "#b54708", "800": "#93370d", "900": "#7a2e0e",
        }, "warning ramp, authored, not painted on the captured pages"),
        "success": ramp("--success", {
            "25": "#f6fef9", "50": "#ecfdf3", "100": "#d1fadf", "200": "#a6f4c5",
            "300": "#6ce9a6", "400": "#32d583", "500": "#12b76a", "600": "#039855",
            "700": "#027a48", "800": "#05603a", "900": "#054f31",
        }, "success ramp, authored, not painted on the captured pages"),
        "white": color("#ffffff", f"{CSS}: --white"),
        "nav": color("rgba(255, 253, 249, 0.3)", f"{M}: .navbar_component background-color; the sheet writes #fffdf94d"),
        "examples": color("#e3eeff", f"{M}: home Writing Examples section background"),
        "plan": {
            "starter": color("#f6e2ff", f"{M}: .pricing07_top-row-content.purple"),
            "pro": color("#ffe8e2", f"{M}: .pricing07_top-row-content.orange"),
            "scale": color("#e3eeff", f"{M}: .pricing07_top-row-content.blue"),
        },
        "focusRing": color("#005fcc", "Observed. Chromium's default focus ring (-webkit-focus-ring-color), not a Macaw colour: the focus-visible outline on links and buttons reads rgb(0, 95, 204). Macaw's own focus cue is the 4px focusHalo"),
        "focusHalo": color("#ffe1df", f"{M}: 4px box-shadow ring on focused button and field, same as --primary100"),
    },
    "font": {
        "family": {
            "sans": font("Inter, sans-serif", f"{M}: body, h1, buttons and fields. Google Fonts Inter is linked from the page."),
            "open-sans": font('"Open Sans", sans-serif', f"{CSS}: a custom property named --1 holds this stack. Computed body text is Inter, not Open Sans."),
        },
        "weight": {
            "regular": num(400, f"{M}: body copy", "fontWeight"),
            "medium": num(500, f"{M}: field label", "fontWeight"),
            "semibold": num(600, f"{M}: nav links and buttons", "fontWeight"),
            "bold": num(700, f"{M}: h1 and section headings", "fontWeight"),
        },
        "size": {
            "label": dim("14px", f"{M}: .field-label"),
            "button": dim("14.8px", f"{M}: primary and secondary buttons"),
            "body": dim("16px", f"{M}: body"),
            "section": dim("27.2px", f"{HAND}: article h2 on the home examples"),
            "heading": dim("36px", f"{M}: example card h3"),
            "display": dim("53.6px", f"{M}: h1"),
            "privacy-h2": dim("60px", f"{HAND}: privacy page h2"),
        },
        "lineHeight": {
            "display": dim("64.32px", f"{M}: h1 computed line-height (display, pricing-heading and the other h1s in raw/components-computed.json)"),
            "heading": dim("43.2px", f"{HAND}: example card h3"),
            "section": dim("32.64px", f"{HAND}: article h2"),
            "body": dim("24px", f"{D}: 16px body at 1.5, the form-input line-height in the sheet"),
            "button": dim("22px", f"{D}: 14.8px button label at the sheet's 1.5 line"),
        },
        "tracking": {
            "display": dim("-1.608px", f"{M}: home h1 letter-spacing"),
            "heading": dim("-0.72px", f"{HAND}: example card h3 letter-spacing"),
            "section": dim("-0.544px", f"{HAND}: article h2 letter-spacing"),
        },
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.display}",
                "fontWeight": "{font.weight.bold}",
                "lineHeight": "{font.lineHeight.display}",
                "letterSpacing": "{font.tracking.display}",
            },
            "$extensions": {"source": f"{M}: h1, letter-spacing -1.608px"},
        },
        "heading": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.heading}",
                "fontWeight": "{font.weight.bold}",
                "lineHeight": "{font.lineHeight.heading}",
                "letterSpacing": "{font.tracking.heading}",
            },
            "$extensions": {"source": f"{M}: example card h3"},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.body}",
                "fontWeight": "{font.weight.regular}",
                "lineHeight": "{font.lineHeight.body}",
            },
            "$extensions": {"source": f"{M}: body"},
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.button}",
                "fontWeight": "{font.weight.semibold}",
                "lineHeight": "{font.lineHeight.button}",
            },
            "$extensions": {"source": f"{M}: buttons and nav links"},
        },
        "caption": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.label}",
                "fontWeight": "{font.weight.medium}",
                "lineHeight": "21px",
            },
            "$extensions": {"source": f"{M}: field label, 14px / 500, 21px tall"},
        },
    },
    "space": {
        "2": dim("8px", f"{M}: field vertical padding"),
        "3": dim("12px", f"{M}: text area vertical padding"),
        "4": dim("16px", f"{M}: plan card padding-bottom, the 1rem step"),
        "6": dim("24px", f"{D}: FAQ question padding-top and padding-bottom, 1.5rem in .faq01_question"),
        "5": dim("18px", f"{M}: button horizontal padding"),
        "8": dim("32px", f"{M}: navbar padding-left and padding-right, 2rem"),
        "10": dim("40px", f"{M}: plan card padding-top"),
    },
    "radius": {
        "control": dim("8px", f"{M}: buttons, fields and billing toggle, 0.5rem"),
        "plan": dim("12px", f"{M}: plan cards"),
    },
    "border": {
        "width": dim("1px", f"{M}: button, field and secondary button border"),
    },
    "elevation": {
        "control": shadow("0px 1px 2px 0px rgba(16, 24, 40, 0.05)", f"{M}: button and field box-shadow"),
        "focus": shadow("0px 0px 0px 4px #ffe1df", f"{M}: focus halo on the primary button and the text field"),
    },
    "size": {
        "nav": dim("80px", f"{M}: desktop navbar height"),
        "nav-mobile": dim("72px", f"{M}: phone navbar height at 390"),
        "button": dim("46px", f"{M}: primary, secondary and send buttons"),
        "field": dim("44px", f"{M}: text field, min-height 2.75rem"),
        "area": dim("112px", f"{M}: message text area"),
        "menu-button": dim("40px", f"{M}: phone menu button width"),
        "focus": dim("1px", f"{M}: focus-visible outline width"),
        "focus-halo": dim("4px", f"{M}: focus box-shadow spread"),
    },
    "layout": {
        "desktop": dim("1440px", f"{M}: desktop capture viewport"),
        "phone": dim("390px", f"{M}: phone capture viewport"),
        "content": dim("1024px", f"{M}: pricing h1 width, the content column"),
        "prose": dim("768px", f"{M}: FAQ question width"),
        "form": dim("450px", f"{M}: contact text area and send button width"),
    },
}

light = {
    "page": color("{color.page}", f"{M}: page"),
    "surface": color("{color.white}", f"{M}: cards, fields, secondary button"),
    "surfaceMuted": color("{color.examples}", f"{M}: Writing Examples band"),
    "text": color("{color.gray.900}", f"{M}: h1 ink rgb(16, 24, 40)"),
    "textBody": color("{color.gray.600}", f"{M}: body ink rgb(71, 84, 103)"),
    "textMuted": color("{color.gray.700}", f"{M}: secondary button and field label rgb(52, 64, 84)"),
    "textOnAccent": color("{color.white}", f"{M}: primary button label"),
    "link": color("{color.primary.600}", f"{M}: nav link hover ink"),
    "border": color("{color.gray.300}", f"{CSS}: field and secondary button border --gray300"),
    "borderFocus": color("{color.primary.300}", f"{M}: autofocused name field border rgb(250, 162, 154)"),
    "accent": color("{color.primary.600}", f"{M}: primary button fill"),
    "accentHover": color("{color.primary.700}", f"{M}: primary button hover and forced :active"),
    "focus": color("{color.focusRing}", f"{M}: keyboard focus outline"),
    "success": color("{color.success.600}", f"{CSS}: --success600, authored, not painted on the captured pages"),
    "warning": color("{color.warning.600}", f"{CSS}: --warning600, authored, not painted on the captured pages"),
    "danger": color("{color.error.600}", f"{CSS}: --error600, authored, not painted on the captured pages"),
    "info": color("#2e90fa", f"{CSS}: --blue500, authored, not painted as a status on the captured pages"),
}

tokens = {
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}

if MOTION:
    # The package's own motion.py (copy it from tools/kit/build/ before running the probe):
    # build() returns the token group and what DTCG cannot carry.
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import motion
    core["motion"], not_tokenised = motion.build(MOTION)
    if not_tokenised:
        core.setdefault("$extensions", {})["notTokenised"] = not_tokenised


def leaves(node, path=""):
    for k, v in node.items():
        if k.startswith("$") or not isinstance(v, dict):
            continue
        here = f"{path}.{k}" if path else k
        if "$value" in v:
            yield here, v
        else:
            yield from leaves(v, here)


CHANNEL = r"\s*\d{1,3}\s*"
COLOR = (r"#[0-9a-f]{6}([0-9a-f]{2})?"
         rf"|rgb\({CHANNEL},{CHANNEL},{CHANNEL}\)|rgba\({CHANNEL},{CHANNEL},{CHANNEL},\s*(0|1|0?\.\d+)\s*\)")
DIMENSION = r"-?\d*\.?\d+(px|rem)"
# The $type an alias inside a composite must point at, by member name.
MEMBER = {"fontFamily": {"fontFamily"}, "fontSize": {"dimension"}, "fontWeight": {"fontWeight", "number"},
          "lineHeight": {"dimension", "number"}, "letterSpacing": {"dimension"}, "color": {"color"},
          "offsetX": {"dimension"}, "offsetY": {"dimension"}, "blur": {"dimension"}, "spread": {"dimension"}}


def check(doc):
    """The kit's guards, which this fork had dropped: every alias resolves (the set, then core) to a
    token of the right $type, every leaf has a source, and colours, dimensions and shadow layers have
    DTCG shapes."""
    core_types = {p: t["$type"] for p, t in leaves(doc["core"])}
    for setname in ("core", "light"):
        types = {**core_types, **{p: t["$type"] for p, t in leaves(doc[setname])}}

        def check_value(where, v, want):
            if isinstance(v, str) and re.fullmatch(r"\{([^{}]+)\}", v):
                ref = v[1:-1]
                if ref not in types:
                    raise SystemExit(f"{where}: alias {{{ref}}} resolves to nothing")
                if types[ref] not in want:
                    raise SystemExit(f"{where}: alias {{{ref}}} is a {types[ref]}, not a {'/'.join(sorted(want))}")
                return
            if "color" in want and not (isinstance(v, str) and re.fullmatch(COLOR, v)):
                raise SystemExit(f"{where}: colour {v!r}")
            if want == {"dimension"} and not (isinstance(v, str) and re.fullmatch(DIMENSION, v)):
                raise SystemExit(f"{where}: dimension {v!r}")

        for path, tok in leaves(doc[setname]):
            where = f"{setname}.{path}"
            if not tok.get("$extensions", {}).get("source"):
                raise SystemExit(f"{where}: no source")
            v, ty = tok["$value"], tok["$type"]
            if ty in ("typography",):
                for member, mv in v.items():
                    check_value(f"{where}.{member}", mv, MEMBER.get(member, {ty}))
            elif ty == "shadow":
                if not isinstance(v, list):
                    raise SystemExit(f"{where}: shadow must be a list of layers")
                for layer in v:
                    for member, mv in layer.items():
                        if member != "inset":
                            check_value(f"{where}.{member}", mv, MEMBER[member])
            else:
                check_value(where, v, {ty} | ({"number"} if ty == "fontWeight" else set()))


check(tokens)

if __name__ == "__main__":
    (HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
    print("wrote", HERE / "tokens.json")
