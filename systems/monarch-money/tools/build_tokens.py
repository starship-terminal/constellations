#!/usr/bin/env python3
"""Build tokens.json from the Monarch Money public capture.

The marketing site (www.monarch.com) declares a Radix-style ramp and semantic
roles on :root in its Next stylesheet. The page does not set data-brand, so
the default :root wins. A second :root:where([data-brand="refresh"]) exists
and is not applied; those values are recorded under core.brand.refresh and
are not the painted theme.

app.monarch.com/login paints the same page ground and an Oracle stack, but
its stylesheet is cross-origin, so its custom properties were not resolved
in the page. The sign-in controls are measured in raw/components-computed.json.

There is no dark set. The public site does not paint one.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))

VARS = json.loads((RAW / "css-vars.json").read_text())
RES = VARS["home"]["resolved"]
DATE = VARS.get("readAt", "2026-11-19")
M = f"Measured computed custom property on www.monarch.com :root, {DATE}, light, 1440. data-brand was unset, so the default :root wins"
D = "Derived from a measured custom property on the same capture"

HUES = ["orange", "gray", "blue", "green", "red", "yellow", "pink", "purple", "indigo"]


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def typography(value, source):
    return {"$value": value, "$type": "typography", "$extensions": {"source": source}}


def need(name):
    if name not in RES or not RES[name]:
        raise SystemExit(f"missing resolved {name}")
    return RES[name]


core = {"color": {}, "font": {"family": {}, "weight": {}, "size": {}, "lineHeight": {}, "tracking": {}}, "radius": {}, "space": {}}

for hue in HUES:
    steps = {}
    for i in range(1, 13):
        name = f"--{hue}-{i}"
        if name in RES and RES[name].startswith("#"):
            steps[str(i)] = color(RES[name], f"{M}: {name}")
    if steps:
        core["color"][hue] = steps

brand_literals = {
    "orange": "--monarch-orange",
    "persimmon": "--persimmon",
    "charcoal": "--charcoal",
    "parchment": "--parchment",
    "wheat": "--wheat",
    "walnut": "--walnut",
    "evergreen": "--evergreen",
    "mahogany": "--mahogany",
    "goldenrod": "--goldenrod",
    "milkweed": "--milkweed",
    "pool-blue": "--pool-blue",
    "sky": "--sky",
    "aster": "--aster",
    "daisy": "--daisy",
    "sunbeam": "--sunbeam",
    "dark-grey": "--dark-grey",
    "secondary-grey": "--secondary-grey",
    "tertiary-grey": "--tertiary-grey",
}
pigments = {}
for key, name in brand_literals.items():
    if name in RES and RES[name].startswith("#"):
        pigments[key] = color(RES[name], f"{M}: {name}. A named pigment. Not the painted page role unless a semantic token aliases it.")
core["color"]["pigment"] = pigments

# The unused refresh brand, recorded so it is not mistaken for the live theme.
refresh = {
    "page": color("#fdf8ed", f"{D}: --parchment, the value :root:where([data-brand=refresh]) assigns to --background. The captured pages did not set data-brand, so this was not painted."),
    "text": color("#22201d", f"{D}: --charcoal under data-brand=refresh. Not painted on the captured pages."),
    "accent": color("#f35b16", f"{D}: --monarch-orange under data-brand=refresh. Not painted as --primary on the captured pages."),
    "accentHover": color("#e64818", f"{D}: --persimmon under data-brand=refresh. Not painted."),
    "displaySize": dim("75px", f"Declared --type-display-size on :root:where([data-brand=refresh]) at min-width 768px. Not painted. The live display size is 48px."),
}
core["color"]["refresh"] = {k: v for k, v in refresh.items() if k != "displaySize"}
core["color"]["refresh"]["$description"] = "The data-brand=refresh palette. The captured pages left data-brand unset, so these colours were not the painted theme."

core["font"]["family"]["primary"] = font(need("--font-primary"), f"{M}: --font-primary. ABC Oracle is a licensed face. The files are not in this package.")
core["font"]["family"]["secondary"] = font(need("--font-secondary"), f"{M}: --font-secondary. Copernicus is a licensed face. The files are not in this package.")
core["font"]["family"]["display"] = font(need("--font-display"), f"{M}: --font-display. ABC Otto is a licensed face. The files are not in this package. The home hero computed Copernicus; pricing headings computed ABC Otto.")
core["font"]["family"]["accent"] = font(need("--font-accent"), f"{M}: --font-accent. Beltram Mono is a licensed face. The files are not in this package.")

core["font"]["weight"]["book"] = num(350, f"{M}: --type-body-weight and --type-heading-1-weight are 350", "fontWeight")
core["font"]["weight"]["regular"] = num(400, f"{D}: the sign-in field computed font-weight 400. The marketing type roles use 350.", "fontWeight")
core["font"]["weight"]["medium"] = num(500, f"{M}: --type-eyebrow-weight is 500. Pricing trial links and FAQ summaries computed 500.", "fontWeight")

# Desktop type roles (min-width 768px). The capture viewport is 1440, so these are the painted sizes.
TYPE = ["display", "heading-1", "heading-2", "heading-3", "heading-4", "heading-5", "heading-6", "body", "small", "extra-small", "eyebrow"]
# Every role reads its four custom properties from raw/css-vars.json; a missing one fails the build
# (the TYPE literals used to stand in under the measured source). rem is converted at the 16px
# root, and an em tracking at the role's own size, since a DTCG dimension is px or rem.
def rem_px(v):
    return "%gpx" % (float(v[:-3]) * 16) if v.endswith("rem") else v


for role in TYPE:
    size_name = f"--type-{role}-size"
    size = rem_px(need(size_name))
    core["font"]["size"][role] = dim(size, f"{M}: {size_name} at min-width 768px (the 1440 capture). Phone (under 768px) declares a smaller step in the same stylesheet.")
    core["font"]["lineHeight"][role] = num(float(need(f"--type-{role}-leading")), f"{M}: --type-{role}-leading", "number")
    track = need(f"--type-{role}-tracking")
    if track.endswith("em") and not track.endswith("rem"):
        px = float(track[:-2]) * float(size[:-2])
        core["font"]["tracking"][role] = dim("%gpx" % round(px, 3), f"{M}: --type-{role}-tracking {track}, at the {size} size")
    else:
        core["font"]["tracking"][role] = dim(rem_px(track), f"{M}: --type-{role}-tracking")

core["typography"] = {}
for role, fam in (
    ("display", "{font.family.display}"),
    ("heading-1", "{font.family.display}"),
    ("heading-2", "{font.family.display}"),
    ("heading-3", "{font.family.secondary}"),
    ("body", "{font.family.primary}"),
    ("small", "{font.family.primary}"),
    ("eyebrow", "{font.family.primary}"),
    ("label", "{font.family.primary}"),
):
    size_role = "small" if role == "label" else role
    weight = "{font.weight.medium}" if role in ("eyebrow", "label") else "{font.weight.book}"
    core["typography"][role] = typography(
        {
            "fontFamily": fam,
            "fontSize": "{font.size.%s}" % size_role,
            "fontWeight": weight,
            "lineHeight": "{font.lineHeight.%s}" % size_role,
            "letterSpacing": "{font.tracking.%s}" % size_role,
        },
        f"{M}: --type-{size_role}-* at the desktop breakpoint. Family is the role the marketing CSS assigns.",
    )

core["radius"] = {
    "sm": dim("8px", "Measured on the sign-in field and the Continue with Apple button, app.monarch.com/login, 2026-11-19. border-radius 8px."),
    "control": dim("8px", "Measured on the sign-in submit, 2026-11-19."),
    "pill": dim("9999px", f"{M}: nav links, Sign in and Sign up compute border-radius 9999px."),
    "none": dim("0px", f"{M}: the page and the hero title have no radius."),
}
core["space"] = {
    "1": dim("4px", f"{D}: a 4px step. The sign-in label gap uses a 2xs step in the app class names."),
    "2": dim("8px", "Measured nav link padding-top 8px, 2026-11-19."),
    "3": dim("12px", "Measured nav link padding-inline 12px, 2026-11-19."),
    "4": dim("16px", "Measured Sign in and Sign up padding-inline 16px, 2026-11-19."),
    "5": dim("20px", "Measured plan trial link padding-inline 20px, 2026-11-19."),
    "6": dim("24px", "Measured footer call-to-action padding-inline 24px, 2026-11-19."),
    "8": dim("32px", f"{D}: the announcement bar height is 32px (--announcement-bar-height on html)."),
    "9": dim("36px", "Measured nav link and Sign up height 36px, 2026-11-19."),
    "10": dim("40px", "Measured Continue with Apple height 40px, 2026-11-19."),
    "12": dim("48px", "Measured email field and footer call-to-action height 48px, 2026-11-19."),
}
core["layout"] = {
    "desktop": dim("1440px", "The desktop capture viewport, window.innerWidth 1440."),
    "phone": dim("390px", "The phone capture viewport, window.innerWidth 390."),
    "nav": dim("36px", "Measured nav link height."),
    "announcement": dim("32px", "html style --announcement-bar-height, measured 32px."),
    "field": dim("48px", "Measured sign-in email field height."),
}

if (RAW / "motion.json").exists():
    import motion as motion_mod
    core["motion"], motion_not = motion_mod.build(json.loads((RAW / "motion.json").read_text()))
    # The values DTCG cannot carry are listed, as the kit does, not dropped.
    if motion_not:
        core.setdefault("$extensions", {}).setdefault("notTokenised", []).extend(motion_not)

light = {
    "page": color("{color.gray.2}", f"{M}: --background is var(--gray-2). Computed #f6f5f3."),
    "surface": color("#ffffff", f"{M}: --card and --secondary are #fff. Computed on the Sign in pill."),
    "surfaceMuted": color("{color.gray.3}", f"{M}: --muted is var(--gray-3). Computed #efecea."),
    "text": color("{color.gray.12}", f"{M}: --foreground is var(--gray-12). Computed #22201d."),
    "textMuted": color("{color.gray.11}", f"{M}: --muted-foreground is var(--gray-11). Computed #777573."),
    "textSubtle": color("{color.gray.9}", f"{M}: --subtle and --dark-grey compute #8f8c8a."),
    "textOnAccent": color("#fefcfb", f"{M}: --primary-foreground is var(--orange-1). The Sign up pill computed rgb(254, 252, 251)."),
    "accent": color("{color.orange.9}", f"{M}: --primary is var(--orange-9). Computed #ff692d on the Sign up pill."),
    "accentHover": color("{color.orange.10}", f"{M}: --primary-hover is var(--orange-10). Computed #f35b16."),
    "accentPressed": color("{color.pigment.orange}", f"{M}: --monarch-orange #f35b16. The pricing trial link computed rgb(243, 91, 22), the same orange."),
    "border": color("{color.gray.6}", f"{M}: --border and --input are var(--gray-6). Computed #dcd9d6."),
    "focus": color("{color.gray.12}", f"{M}: --ring is var(--gray-12)."),
    "link": color("#0797b9", "Measured on the Forgot password and Sign up links at app.monarch.com/login, 2026-11-19. rgb(7, 151, 185)."),
    "danger": color("#e5484d", f"{M}: --destructive computes #e5484d. Not painted as a form error on the captured pages."),
    "dangerForeground": color("#ffffff", f"{M}: --destructive-foreground is #fff."),
    "success": color("#e6f6eb", f"{M}: --success computes #e6f6eb."),
    "successForeground": color("#218358", f"{M}: --success-foreground computes #218358."),
    "warning": color("#fff7c2", f"{M}: --warning computes #fff7c2."),
    "warningForeground": color("#ab6400", f"{M}: --warning-foreground computes #ab6400."),
    "info": color("#def7f9", f"{M}: --info computes #def7f9."),
    "infoForeground": color("#107d98", f"{M}: --info-foreground computes #107d98."),
    "errorSurface": color("#fdebec", f"{M}: --error computes #fdebec."),
    "errorText": color("#e5484d", f"{M}: --error-foreground computes #e5484d."),
}
light["$description"] = "The painted marketing theme. data-brand was unset. Status colours are declared on :root and were not shown as form errors on the captured pages."

doc = {
    "$schema": "https://tr.designtokens.org/format/",
    "core": core,
    "light": light,
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$extensions": {"how": "www.monarch.com leaves data-brand unset. The default :root semantic tokens paint the page. No dark theme was published on the captured surfaces."},
        }
    ],
    "$extensions": {
        "source": VARS.get("source"),
        "notPainted": "core.color.refresh is the data-brand=refresh palette. It was declared and not applied.",
    },
}

TEXT = json.dumps(doc, indent=2) + "\n"

if __name__ == "__main__":
    (HERE / "tokens.json").write_text(TEXT)
    print("wrote", HERE / "tokens.json")
