#!/usr/bin/env python3
"""Build Memotron tokens.json, components.md, patterns.md and a style-guide
template from the live readings. Run from anywhere:

    python3 tools/build_memotron.py
"""
from __future__ import annotations

import json
import pathlib
import re
import shutil

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
RULES = json.loads((RAW / "css-rules.json").read_text())
LIVE = json.loads((RAW / "live-readings.json").read_text())
TYPE = json.loads((RAW / "type-scale.json").read_text())
SIGNUP = json.loads((RAW / "signup-components.json").read_text())

SRC_CSS = "declared on the theme class in memotron.app/_app/immutable/assets/0.CH5IVgSX.css, fetched 2026-11-19"
SRC_COMPUTED = "computed style on https://memotron.app/ and https://web.memotron.app/signup, 1440x900, 2026-11-19"


def rgb_triplet(raw: str) -> str:
    parts = [float(x.strip()) for x in raw.split(",")]
    rgb = [max(0, min(255, round(p))) for p in parts[:3]]
    return "#" + "".join(f"{v:02x}" for v in rgb)


def tok(value, typ, source):
    return {"$value": value, "$type": typ, "$extensions": {"source": source}}


def theme_props(selector: str) -> dict:
    for sheet in RULES["sheets"]:
        for rule in sheet.get("rules", []):
            if rule["selector"].strip() == selector:
                return rule["properties"]
    raise SystemExit(f"missing selector {selector}")


ROLE = {
    "aps1": ("accent", "primary"),
    "aps2": ("accent", "secondary"),
    "aps3": ("accent", "tertiary"),
    "ass1": ("accent", "support"),
    "ass2": ("accent", "support-soft"),
    "ars1": ("status", "danger"),
    "ars2": ("status", "danger-soft"),
    "ars3": ("status", "danger-softer"),
    "ags1": ("status", "success"),
    "ags2": ("status", "success-soft"),
    "bgs1": ("background", "surface"),
    "bgs2": ("background", "page"),
    "bgs3": ("background", "raised"),
    "bgs4": ("background", "raised-2"),
    "bgs5": ("background", "raised-3"),
    "bgs6": ("background", "raised-4"),
    "brs1": ("border", "subtle"),
    "brs2": ("border", "default"),
    "brs3": ("border", "strong"),
    "brs4": ("border", "stronger"),
    "fgs1": ("text", "primary"),
    "fgs2": ("text", "secondary"),
    "fgs3": ("text", "muted"),
    "fgs4": ("text", "faint"),
    "bgg1": ("background", "glow"),
}


def semantic(selector: str) -> dict:
    props = theme_props(selector)
    tree: dict = {}
    for name, raw in props.items():
        if not name.startswith("--colors-"):
            continue
        key = name[len("--colors-"):]
        if key not in ROLE:
            continue
        group, leaf = ROLE[key]
        tree.setdefault(group, {})[leaf] = tok(rgb_triplet(raw), "color", f"{SRC_CSS}; {selector} {name}")
    return tree


def nest(path, value):
    node = {}
    cur = node
    parts = path.split(".")
    for p in parts[:-1]:
        cur = cur.setdefault(p, {})
    cur[parts[-1]] = value
    return node


def merge(dst, src):
    for k, v in src.items():
        if isinstance(v, dict) and "$value" not in v and isinstance(dst.get(k), dict):
            merge(dst[k], v)
        else:
            dst[k] = v


# Type roles measured by applying the class on a probe inside .cs_tidigit_dark_blue.
# The root font-size is 16.702px (html 104.3875%), so a utility of 1rem resolves
# slightly above 16px. Record the computed px.
TYPE_ROLES = {
    "display": ("text-h1", "Display / h1 utility"),
    "title": ("text-h2", "Title / h2 utility"),
    "heading": ("text-h3", "Heading / h3 utility, wordmark and signup title"),
    "subheading": ("text-h4", "Subheading / h4 utility, feature card titles"),
    "body": ("text-base", "Body"),
    "body-small": ("text-b2", "Nav links and secondary body"),
    "caption": ("text-b3", "Caption, footer links on the signup page"),
}

core = {
    "fontFamily": {
        "sans": tok(
            "Twenty One Native, Sen, Sen, Sen Variable, Space Grotesk, Hanken Grotesk, Hanken Grotesk Variable, Nunito, Teachers, Montserrat, Proxima Nova, Poppins, Noto Sans, sans-serif",
            "fontFamily",
            "computed font-family on body of https://memotron.app/, 2026-11-19. Twenty One Native is the product face and is not shipped here; Sen and Space Grotesk are the Google Fonts faces the page loads",
        ),
        "serif": tok("Merriweather, serif", "fontFamily", "declared --fontFamily-serif-0 on :root in the same stylesheet; not used by the marketing pages"),
    },
    "typography": {},
    "radius": {
        "none": tok("0px", "dimension", "computed border-radius on feature cards' text"),
        "sm": tok("6px", "dimension", "rounded-md on the signup offline card (computed 6.26px at the page's 16.702px root, authored as 0.375rem)"),
        "md": tok("12px", "dimension", "rounded-xl on home feature cards (computed 12.58px, authored 0.75rem)"),
        "full": tok("9999px", "dimension", "rounded-full on nav links, Go to web app, Download for Mac, and the signup provider buttons"),
    },
    "spacing": {
        "1": tok("4px", "dimension", "gap-1 on the wordmark row (computed 4.19px)"),
        "2": tok("8px", "dimension", "py-2 on the watch-video link"),
        "3": tok("12px", "dimension", "px-3 on nav links and the signup card padding"),
        "4": tok("16px", "dimension", "px-4 on the watch-video link and the sidebar rail padding"),
        "6": tok("24px", "dimension", "p-6 / pl-6 on feature cards"),
        "8": tok("32px", "dimension", "px-8 on the home content column"),
    },
    "size": {
        "button-sm": tok("32px", "dimension", "h-8 on Go to web app (computed 33.39px)"),
        "button-md": tok("48px", "dimension", "h-12 on Continue with Google (computed 50.10px)"),
        "header": tok("76px", "dimension", "computed height of the marketing header at 1440"),
        "rail": tok("100px", "dimension", "w-[100px] product rail on the marketing shell"),
        "content": tok("1240px", "dimension", "max-w-[1240px] on the home content column"),
    },
}

def add_type(role, family, size, weight, line, note):
    # Flat tokens. catalog.py design-md joins `-{font-size}` style suffixes into one style.
    core["typography"][role + "-font-family"] = tok(family, "fontFamily", note)
    core["typography"][role + "-font-size"] = tok(size, "dimension", note)
    core["typography"][role + "-font-weight"] = tok(weight, "number", note)
    core["typography"][role + "-font-line-height"] = tok(line, "dimension", note)
    core["typography"][role + "-font-letter-spacing"] = tok("0px", "dimension", note + "; letter-spacing computed as normal")


for role, (cls, note) in TYPE_ROLES.items():
    row = TYPE[cls]
    add_type(
        role,
        "{fontFamily.sans}",
        row["fontSize"],
        int(float(row["fontWeight"])),
        row["lineHeight"],
        f"computed {cls} on a probe inside .cs_tidigit_dark_blue at 1440; {note}",
    )

add_type(
    "hero",
    "{fontFamily.sans}",
    "44px",
    500,
    "66px",
    "computed on the home h2 'Exceptional throughout' (class text-[44px] font-medium)",
)

light = semantic(".cs_tidigit_light_blue")
dark = semantic(".cs_tidigit_dark_blue")
# Page ground on the marketing site is bgs2, cards are bgs1. Keep that naming
# in both themes so the catalog swatches resolve.
for tree, sel in ((light, ".cs_tidigit_light_blue"), (dark, ".cs_tidigit_dark_blue")):
    tree["$description"] = f"Semantic colours from {sel}, the tidigit blue theme. The marketing site and the signed-out web app paint .cs_tidigit_dark_blue."

tokens = {
    "$schema": "https://tr.designtokens.org/format/",
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("tokens", sum(1 for _ in json.dumps(tokens)))

# components.md
home = LIVE.get("components", {}).get("home", {})


def hex_of(rgb):
    m = re.match(r"rgba?\((\d+),\s*(\d+),\s*(\d+)", rgb or "")
    if not m:
        return rgb
    return "#" + "".join(f"{int(g):02x}" for g in m.groups())


def comp_block(name, states):
    lines = [f"### {name}", ""]
    for state, row in states.items():
        if not row:
            continue
        style = row.get("style") or row.get("rest") or row
        if not isinstance(style, dict):
            continue
        bits = []
        for key in ("color", "backgroundColor", "borderRadius", "fontSize", "fontWeight", "padding", "height", "border"):
            if style.get(key):
                val = style[key]
                if "color" in key.lower() or key in ("color", "backgroundColor"):
                    val = f"{hex_of(val)} ({val})"
                bits.append(f"{key} {val}")
        text = style.get("text") or ""
        lines.append(f"- **{state}.** {text}. " + "; ".join(bits) + ".")
    lines.append("")
    return "\n".join(lines)


components = f"""# Memotron components

Measured on the public marketing site and the signed-out web app on 2026-11-19.
Crops are in [components/crops/](components/crops). Values are computed styles.
A colour written as hex is the rounded sRGB of the computed `rgb()`.

## Inventory

| Checklist | In the product | Evidence |
|---|---|---|
| Button | yes | Go to web app, Download for Mac, Continue with Google, Continue with Apple, Continue offline |
| Icon button | yes | Discord mark in the header, a circle with a 1px fgs2 border |
| Link | yes | Nav links, Terms of Service, Docs |
| Text field | not on these pages | Signup has no email field. Google, Apple, or offline only |
| Text area | not present signed out | |
| Select | not present | Billing period is a segmented control, not a select |
| Checkbox | not present | |
| Radio | not present | |
| Switch | not present | |
| Tabs | partial | Pricing Monthly / Yearly / Lifetime is a segmented control |
| Menu | yes | Resources menu: Features, Tutorials, FAQs, Changelog, Roadmap |
| Tooltip | not captured | none opened on the public pages |
| Dialog | not present signed out | no promo dialog on the marketing site |
| Toast | not present | |
| Card | yes | Feature cards on the home page, plan cards on pricing |
| List row | partial | Plan feature rows |
| Table | not present | Compare is a card layout, not a table, in the first viewport |
| Avatar | not present | |
| Badge | partial | "20% off" sits inside the Yearly segment label |

## Button

Primary filled pill. Go to web app uses `bg-fgs1` text `text-bgs1`, height 33px, radius 9999px, padding 0 12.5px, type body-small.

{comp_block("Go to web app", {"default": {"style": home.get("cta-web-app", {}).get("rest")}, "hover": {"style": home.get("cta-web-app", {}).get("hover")}})}

Download for Mac is the same filled pill at body size, height 33px, padding 0 16.6px.

Signup provider buttons (Continue with Google, Continue with Apple) are a quieter fill, computed background `#252837` (between bgs2 and bgs3), text fgs1, height 50px, radius 9999px, padding 16.7px 25px.

Continue offline is a tall card-button: background bgs1, top border brs3, radius 6px on the bottom corners only, padding 12.5px.

## Link

Nav link at rest is text fgs1, transparent, radius 9999px, padding 4px 12.5px, type body-small. Hover turns the text accent primary (`#2c70dd`) and the fill raised (`#252837`, bgs3).

Terms of Service on the signup page is caption size, text secondary, dotted underline.

## Card

Home feature card: background bgs1 (`#151823`), radius 12.6px (rounded-xl), padding 25px 0 0 25px, gap 34px, min height 268px. Title is h4 at 18.9px weight 600. Body is text secondary.

Pricing plan card: border 1px brs3, radius about 12px, icon, title, price, feature list.

## Menu

Resources opens a panel of five tiles (Features, Tutorials, FAQs, Changelog, Roadmap) under the nav. Captured in [screenshots/home-dark-resources-menu.png](screenshots/home-dark-resources-menu.png).

## Segmented control

Pricing billing period: Monthly, Yearly (20% off), Lifetime. The selected segment is a darker pill inside a raised track. Monthly was clicked and recaptured.

## Wordmark

Hexagon mark plus "Memotron" in the h3 utility (21.9px / 32.9px, weight 400) on the marketing header. On signup the same mark sits alone in the left pane.

## Gaps

- No text field, checkbox, radio, switch, dialog, toast, tooltip, table or avatar on the signed-out surfaces.
- Focus-visible was not forced. The pages do not show a custom focus ring in the resting CSS that was read.
- Pressed and disabled were not captured. Nothing was submitted.
- Loading and error states sit behind signup.
- Light theme classes exist (`.cs_tidigit_light_blue` and the other tidigit accents) and are tokenised. The public pages paint dark only. No control on the marketing site or the signup page switches theme.
- The product rail ("21n", "Products") is marketing chrome, not the signed-in app shell.
"""
(HERE / "components.md").write_text(components)

patterns = """# Memotron patterns

Public surfaces only. The signed-in app was not opened: signup offers Google, Apple, or Continue offline, and offline was not taken because it starts a local-only workspace this capture does not keep.

## Marketing shell

A 100px rail on the left ("21n") and a matching rail on the right ("Products"), with the page scrolling in the centre column (`overflow-y-auto`, about 8076px on the home page). The header is sticky inside that column: wordmark, Resources, Pricing, Compare, Extension, Discord, a Discord icon button, and Go to web app.

Screenshot: [screenshots/home-dark-default.png](screenshots/home-dark-default.png).

## Hero

Centred. "Your memory atlas" at an authored 44px is below the first viewport of the text dump and visible in the default shot as the display line. Subcopy at 17px. One filled pill, Download for Mac. A line of muted availability text. Then a product demo image with a play button. The demo is a public marketing render, not the signed-in app.

## Feature grid

Cards in a wrapping grid. Each card is an anchor, bgs1, radius xl, an icon, an h4, muted body. Some cards list small feature chips (Open source, On-device AI).

Screenshot: [screenshots/home-dark-slice2.png](screenshots/home-dark-slice2.png).

## Pricing

Three plan cards under a billing segmented control. Offline is $0. Memotron sync is $60 yearly. Nucleus is $144 yearly. An early-adopter banner uses the accent blue. No card was entered. No payment step was opened.

Screenshot: [screenshots/pricing-dark-default.png](screenshots/pricing-dark-default.png).

## Signup

Two panes. Left is bgs1 with the hexagon wordmark. Right is the page ground with "Welcome to Memotron", two provider pills, and a tall offline card. Footer links: Terms, Privacy, Pricing, Docs, Discord. No email field, no card field, no phone field.

Screenshot: [screenshots/signup-dark-default.png](screenshots/signup-dark-default.png).

## Legal

Privacy, terms and refund are long text pages in the same shell. Captured as viewports only.

## Not captured

Signed-in app shell, empty library, search, a note editor, destructive confirmation, toasts, and onboarding after offline continue. Those need an account session this capture did not start.
"""
(HERE / "patterns.md").write_text(patterns)
print("wrote components.md patterns.md tokens.json")
