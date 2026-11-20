#!/usr/bin/env python3
"""Build tokens.json from the SeatGeek stylesheet readings in raw/declared-tokens.json.

The readings are the :root and [data-theme=dark] custom properties fetched from
the live seatgeek.com stylesheets on 2026-11-19 (chunks 0cki_b1y~_ibz.css and
0gwmdb80dmu1h.css). Computed styles on the painted public pages confirm the
light theme tokens. Dark semantic aliases are declared, not a live paint.
"""
from __future__ import annotations

import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
SRC = json.loads((RAW / "declared-tokens.json").read_text())

MEASURED = (
    "Measured: declared custom property fetched from the live seatgeek.com "
    "stylesheet on 2026-11-19, confirmed by getComputedStyle where the public "
    "page paints the value"
)
DECLARED = (
    "Measured: declared custom property in the live seatgeek.com stylesheet "
    "fetched 2026-11-19 (not a painted computed style on this capture)"
)
DERIVED = "Derived: alias resolved against the palette declared in the same :root block"


def colour(value: str) -> dict:
    return {"$type": "color", "$value": value}


def dim(value: str) -> dict:
    return {"$type": "dimension", "$value": value}


def num(value) -> dict:
    return {"$type": "number", "$value": value}


def font(value: str) -> dict:
    return {"$type": "fontFamily", "$value": value}


def shadow(value: str) -> dict:
    return {"$type": "shadow", "$value": value}


def src(label: str, name: str, selector: str) -> dict:
    return {"source": f"{label}. {selector} {name}"}


def nest(tree: dict, parts: list[str], token: dict) -> None:
    node = tree
    for part in parts[:-1]:
        node = node.setdefault(part, {})
    node[parts[-1]] = token


def parse_block(css: str) -> dict[str, str]:
    body = css[css.find("{") + 1: css.rfind("}")]
    out = {}
    for match in re.finditer(r"(--[\w-]+)\s*:\s*([^;]+)", body):
        out[match.group(1)] = match.group(2).strip()
    return out


def resolve(name: str, table: dict[str, str], seen: set[str] | None = None) -> str:
    seen = seen or set()
    value = table[name]
    match = re.fullmatch(r"var\((--[\w-]+)\)", value)
    if not match:
        return value
    nxt = match.group(1)
    if nxt in seen or nxt not in table:
        return value
    return resolve(nxt, table, seen | {name})


def expand_hex(value: str) -> str:
    value = value.strip().lower()
    if re.fullmatch(r"#[0-9a-f]{3}", value):
        return "#" + "".join(ch * 2 for ch in value[1:])
    if value == "#eee":
        return "#eeeeee"
    if value == "#fff6":
        return "#ffffff66"
    if value == "#fffc":
        return "#ffffffcc"
    if value == "#000c":
        return "#000000cc"
    return value


def tokenise_colour(name: str, raw: str, table: dict[str, str], selector: str) -> dict:
    resolved = expand_hex(resolve(name, table))
    alias = re.fullmatch(r"var\((--[\w-]+)\)", raw.strip())
    if alias and alias.group(1) in table:
        target = alias.group(1)
        # palette lives in core.color
        if target.startswith("--sg-color-palette-"):
            parts = target.removeprefix("--sg-color-palette-").split("-")
            path = "{color." + ".".join(parts) + "}"
        else:
            path = None
        token = colour(path or resolved)
        token["$extensions"] = src(DERIVED if path else DECLARED, name, selector)
        if path:
            token["$extensions"]["resolved"] = resolved
        return token
    token = colour(resolved)
    token["$extensions"] = src(DECLARED, name, selector)
    return token


def build() -> dict:
    theme = parse_block(SRC["theme"])
    sg = parse_block(SRC["sgLight"])
    dark = parse_block(SRC["sgDark"])
    # dark block only overrides; inherit the rest from light
    dark_full = dict(sg)
    dark_full.update(dark)

    core: dict = {
        "font": {
            "family": {
                "ui": font("RoobertVF, 'RoobertVF Fallback', 'Helvetica Neue', Arial, Helvetica, sans-serif"),
                "compressed": font("Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif"),
            },
            "weight": {
                "light": num(300),
                "regular": num(400),
                "medium": num(500),
                "semi-bold": num(650),
                "bold": num(700),
                "heavy": num(750),
                "black": num(900),
                "sg-regular": num(420),
                "sg-medium": num(600),
                "sg-bold": num(640),
            },
        },
        "color": {},
        "radius": {},
        "spacing": {},
        "border": {},
        "typography": {},
        "shadow": {},
        "motion": {
            "duration": {
                "fast": {"$type": "duration", "$value": "120ms"},
                "quick": {"$type": "duration", "$value": "160ms"},
                "base": {"$type": "duration", "$value": "200ms"},
                "drawer": {"$type": "duration", "$value": "450ms"},
            },
            "easing": {
                "out": {"$type": "cubicBezier", "$value": [0, 0, 0.2, 1]},
                "in-out": {"$type": "cubicBezier", "$value": [0.4, 0, 0.2, 1]},
                "drawer": {"$type": "cubicBezier", "$value": [0.32, 0.72, 0, 1]},
                "tooltip": {"$type": "cubicBezier", "$value": [0.23, 1, 0.32, 1]},
            },
        },
    }
    core["font"]["family"]["ui"]["$extensions"] = {
        "source": "Measured: computed font-family on body, h1 and buttons at seatgeek.com/ on 2026-11-19. :root --font-family and @font-face RoobertVF in 0cki_b1y~_ibz.css"
    }
    core["font"]["family"]["compressed"]["$extensions"] = {
        "source": "Measured: [data-density=compressed] --sg-typography-font-family-body in 0gwmdb80dmu1h.css. Not the density the public pages paint"
    }
    for key, note in {
        "light": "Measured: :root --font-weight-light: 300",
        "regular": "Measured: :root --font-weight-regular: 400. Computed weight on Sports nav link and Sign in",
        "medium": "Measured: computed font-weight 500 on the home subtitle 'The best tickets at the best prices'",
        "semi-bold": "Measured: :root --font-weight-semi-bold: 650. Computed on the empty-state line and the Get updates button",
        "bold": "Measured: computed font-weight 700 on the home h1 and event titles",
        "heavy": "Measured: computed font-weight 750 on the NFL Tickets h1",
        "black": "Measured: :root --font-weight-heavy: 900. Help h1 computed 800, recorded as a component reading, not this token",
        "sg-regular": "Measured: :root --sg-typography-font-weight-regular: 420",
        "sg-medium": "Measured: :root --sg-typography-font-weight-medium: 600",
        "sg-bold": "Measured: :root --sg-typography-font-weight-bold: 640",
    }.items():
        core["font"]["weight"][key]["$extensions"] = {"source": note}

    for name, value in sg.items():
        if name.startswith("--sg-color-palette-"):
            parts = name.removeprefix("--sg-color-palette-").split("-")
            token = colour(expand_hex(value))
            token["$extensions"] = src(DECLARED, name, ":root")
            nest(core["color"], parts, token)
        elif name.startswith("--sg-border-radius-"):
            step = name.removeprefix("--sg-border-radius-")
            token = dim(value)
            token["$extensions"] = src(DECLARED, name, ":root")
            core["radius"][step] = token
        elif name.startswith("--sg-spacing-"):
            step = name.removeprefix("--sg-spacing-")
            token = dim(value)
            token["$extensions"] = src(DECLARED, name, ":root")
            core["spacing"][step] = token
        elif name.startswith("--sg-border-width-"):
            step = name.removeprefix("--sg-border-width-")
            token = dim(value)
            token["$extensions"] = src(DECLARED, name, ":root")
            core["border"][step] = token
        elif name.startswith("--sg-shadow-"):
            step = name.removeprefix("--sg-shadow-").replace("-", "_")
            token = shadow(value)
            token["$extensions"] = src(DECLARED, name, ":root")
            core["shadow"][step] = token

    # Type roles from the declared scale, plus the sizes actually painted.
    type_roles = {
        "caption": ("1", "1", "regular", "2"),
        "body": ("4", "3", "regular", "2"),
        "body-strong": ("5", "3", "bold", "2"),
        "label": ("3", "3", "medium", "2"),
        "heading": ("7", "6", "bold", "2"),
        "title": ("10", "9", "bold", "1"),
        "display": ("11", "11", "bold", "1"),
    }
    for role, (size, line, weight, tracking) in type_roles.items():
        core["typography"][role] = {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.ui}",
                "fontSize": sg[f"--sg-typography-font-size-{size}"],
                "fontWeight": sg[f"--sg-typography-font-weight-{weight}"],
                "lineHeight": sg[f"--sg-typography-line-height-{line}"],
                "letterSpacing": sg[f"--sg-typography-letter-spacing-{tracking}"],
            },
            "$extensions": {
                "source": f"Measured: :root --sg-typography-font-size-{size}, line-height-{line}, font-weight-{weight}, letter-spacing-{tracking}"
            },
        }
    core["typography"]["hero"] = {
        "$type": "typography",
        "$value": {
            "fontFamily": "{font.family.ui}",
            "fontSize": "32px",
            "fontWeight": "700",
            "lineHeight": "46px",
            "letterSpacing": "-0.32px",
        },
        "$extensions": {
            "source": "Measured: computed style on the home h1 'Be good at seats' at 1169px"
        },
    }
    core["typography"]["page-title"] = {
        "$type": "typography",
        "$value": {
            "fontFamily": "{font.family.ui}",
            "fontSize": "48px",
            "fontWeight": "750",
            "lineHeight": "56px",
            "letterSpacing": "-0.32px",
        },
        "$extensions": {
            "source": "Measured: computed style on the NFL Tickets and About h1 at 1169px. About weight was 700; NFL weight was 750"
        },
    }
    for key, token in core["motion"]["duration"].items():
        token["$extensions"] = {
            "source": "Measured: transition-duration in the live stylesheets (button .12s, tooltip .16s, toggle .2s, drawer .45s cubic-bezier(.32,.72,0,1))"
        }
    for key, token in core["motion"]["easing"].items():
        token["$extensions"] = {
            "source": "Derived: keyword or cubic-bezier() from the live stylesheet transition-timing-function list"
        }
    core["motion"]["$extensions"] = {
        "reducedMotion": "The stylesheets contain 41 prefers-reduced-motion mentions. A reduced-motion emulation was not run, so the honour verdict is a gap",
        "incomplete": "Motion was read from stylesheet text, not from a computed-style probe of every element",
    }

    def semantic(table: dict[str, str], selector: str) -> dict:
        out: dict = {"color": {}, "component": {}}
        for name, raw in table.items():
            if not name.startswith("--sg-color-semantic-"):
                continue
            parts = name.removeprefix("--sg-color-semantic-").split("-")
            nest(out["color"], parts, tokenise_colour(name, raw, table, selector))
        return out

    light = semantic(sg, ":root")
    dark = semantic(dark_full, "[data-theme=dark], .dark")

    # Painted roles, so the catalog swatches and DESIGN.md have a surface/text/accent.
    light["surface"] = {
        "page": colour("#ffffff"),
        "card": colour("#f5f5f4"),
        "hero": colour("#120100"),
        "inverse": colour("#181818"),
        "footer": colour("#ffffff"),
    }
    light["surface"]["page"]["$extensions"] = {
        "source": "Measured: computed background on header (about, help) and footer at seatgeek.com. Matches --theme-background-color-primary #fff and --sg-color-semantic-background-screen"
    }
    light["surface"]["card"]["$extensions"] = {
        "source": "Measured: :root --theme-background-color-secondary #f5f5f4, and the computed background of an open nav row"
    }
    light["surface"]["hero"]["$extensions"] = {
        "source": "Measured: computed background-color rgb(18, 1, 0) on the home hero ancestor, under a radial-gradient of rgb(58, 5, 4)"
    }
    light["surface"]["inverse"]["$extensions"] = {
        "source": "Measured: computed background rgb(24, 24, 24) on the price pill 'From $42'. Matches --theme-text-color-primary"
    }
    light["surface"]["footer"]["$extensions"] = {
        "source": "Measured: computed background rgb(255, 255, 255) on footer, padding 60px, shadow rgba(0, 0, 0, 0.08) 0px -1px 0px 0px"
    }
    light["text"] = {
        "primary": colour("#181818"),
        "secondary": colour("#525252"),
        "muted": colour("#767575"),
        "on-hero": colour("#ffffff"),
        "on-hero-muted": colour("#ffffff8f"),
        "on-inverse": colour("#ffffff"),
        "brand": colour("#ff5b49"),
        "link": colour("#1c71ef"),
        "success": colour("#0b6f46"),
        "danger": colour("#ba2626"),
        "warning": colour("#b84d00"),
        "disabled": colour("#76757599"),
    }
    notes = {
        "primary": "Measured: computed color rgb(24, 24, 24) on body text, nav and event titles. :root --theme-text-color-primary #181818",
        "secondary": "Measured: computed color rgb(82, 82, 82) on the About lede. :root --theme-text-color-secondary #525252",
        "muted": "Measured: computed color rgb(118, 117, 117) on event time 'Thu · 7:15pm'. :root --theme-text-color-tertiary #767575",
        "on-hero": "Measured: computed color rgb(255, 255, 255) on the home h1 and the category h1s",
        "on-hero-muted": "Measured: computed color rgba(255, 255, 255, 0.56) on the home subtitle",
        "on-inverse": "Measured: computed color rgb(255, 255, 255) on the price pill",
        "brand": "Measured: computed color rgb(255, 91, 73) on the logo link and suggestion chips. :root --theme-brand-color-base #ff5b49 and --sg-color-palette-brand-600",
        "link": "Measured: :root --sg-color-semantic-action-legal-link aliases --sg-color-palette-blue-600 #1c71ef. Not confirmed as a painted link colour on the pages visited",
        "success": "Measured: :root --theme-text-color-success #0b6f46",
        "danger": "Measured: :root --theme-text-color-critical #ba2626",
        "warning": "Measured: :root --theme-text-color-warning #b84d00",
        "disabled": "Measured: :root --theme-text-color-disabled #76757599",
    }
    for key, note in notes.items():
        light["text"][key]["$extensions"] = {"source": note}
    light["accent"] = colour("#ff5b49")
    light["accent"]["$extensions"] = {
        "source": "Measured: computed color rgb(255, 91, 73) on the wordmark and suggestion chips; help 'Chat with us' background. :root --theme-brand-color-base"
    }
    light["border"] = {
        "default": colour("#dedddb"),
        "subtle": colour("#00000014"),
        "strong": colour("#181818"),
        "focus": colour("#000000"),
        "glass": colour("#ffffff14"),
    }
    light["border"]["default"]["$extensions"] = {
        "source": "Measured: computed border-color rgb(222, 221, 219) on Location and Filter by date. :root --theme-border-color-primary #dedddb"
    }
    light["border"]["subtle"]["$extensions"] = {
        "source": "Measured: :root --theme-divider-color #00000014. Footer shadow uses rgba(0, 0, 0, 0.08)"
    }
    light["border"]["strong"]["$extensions"] = {
        "source": "Measured: :root --theme-border-color-keyboard-focus #000 and --theme-border-color-primarySelected #000"
    }
    light["border"]["focus"]["$extensions"] = {
        "source": "Measured: stylesheet focus ring 0 0 0 2px var(--theme-border-color-primary-alt), 0 0 0 4px var(--theme-border-color-keyboard-focus). Keyboard focus was not held on a live control"
    }
    light["border"]["glass"]["$extensions"] = {
        "source": "Measured: computed border rgba(255, 255, 255, 0.08) on the hero search wrap and Sign in"
    }

    # Component tokens the public pages actually painted.
    light["component"] = {
        "button-primary": {
            "bg": colour("#000000"),
            "text": colour("#ffffff"),
            "radius": dim("8px"),
            "height": dim("56px"),
            "padding": dim("16px"),
        },
        "button-brand": {
            "bg": colour("#ff5b49"),
            "text": colour("#ffffff"),
            "radius": dim("12px"),
            "height": dim("44px"),
        },
        "button-glass": {
            "bg": colour("#ffffff1f"),
            "text": colour("#ffffff"),
            "radius": dim("100px"),
            "height": dim("40px"),
        },
        "chip": {
            "bg": colour("#ffffff"),
            "text": colour("#181818"),
            "radius": dim("100px"),
            "height": dim("32px"),
        },
        "chip-selected": {
            "bg": colour("#181818"),
            "text": colour("#ffffff"),
            "radius": dim("100px"),
            "height": dim("32px"),
        },
        "field": {
            "bg": colour("#ffffff"),
            "text": colour("#181818"),
            "radius": dim("20px"),
            "height": dim("46px"),
        },
        "price": {
            "bg": colour("#181818"),
            "text": colour("#ffffff"),
            "radius": dim("6px"),
            "height": dim("36px"),
        },
        "card": {
            "bg": colour("#ffffff"),
            "text": colour("#181818"),
            "radius": dim("12px"),
        },
        "nav": {
            "bg": colour("#ffffff"),
            "text": colour("#181818"),
            "height": dim("80px"),
        },
    }
    comps = {
        "button-primary": "Measured: Get updates button, computed background rgb(0, 0, 0), color rgb(255, 255, 255), radius 8px, height 56px, padding 16px 24px, weight 650. Seen before the email modal was dismissed",
        "button-brand": "Measured: Help 'Chat with us', computed background rgb(255, 91, 73), color rgb(255, 255, 255), radius 12px, height 44px, shadow rgba(255, 91, 73, 0.3) 0px 6px 16px 0px",
        "button-glass": "Measured: Sign in on the dark hero, computed background rgba(255, 255, 255, 0.12), border 0.5px rgba(255, 255, 255, 0.08), radius 100px, height 40px",
        "chip": "Measured: Location and Filter by date, computed background rgb(255, 255, 255), border 1px rgb(222, 221, 219), radius 100px, height 32px, padding 0 15px",
        "chip-selected": "Measured: location chip 'Singapore, 00' on /nfl-tickets, computed background rgb(24, 24, 24), color rgb(255, 255, 255), border 1px rgb(222, 221, 219), radius 100px, height 32px",
        "field": "Measured: home search wrap, computed background rgba(255, 255, 255, 0.12), radius 100px, height 46px. Help textarea wrap is white, radius 20px, border 2px rgb(222, 221, 219). The token mixes the two: white and 20px from the Help textarea wrap, 46px from the home search wrap",
        "price": "Measured: 'From $42' pill, computed background rgb(24, 24, 24), color rgb(255, 255, 255), radius 6px, height 36px, padding 0 16px, weight 650",
        "card": "Measured: team row radius 12px; trust card border 0.5px rgb(222, 221, 219), radius 12px, padding 20px 24px",
        "nav": "Measured: header height 80px at 1169px and 68px at 390px. About and Help paint the header white; category pages paint it transparent over the hero",
    }
    # raw/declared-tokens.json's `computed` block holds the Sign in button (button-glass) and the
    # price pill (price). The other components' styles were read in the preview and typed in here,
    # so they carry the hand-entered label rather than Measured.
    in_raw = {"button-glass": "computed.signIn", "price": "computed.pricePill"}
    for key, note in comps.items():
        if key in in_raw:
            note = f"{note}. Reading: raw/declared-tokens.json {in_raw[key]}"
        else:
            note = ("Reconstruction: entered by hand at capture time from the computed style read in the "
                    f"preview ({note.removeprefix('Measured: ')}); no raw/ file holds this reading")
        for child in light["component"][key].values():
            child["$extensions"] = {"source": note}

    dark["surface"] = {
        "page": colour("#0a0a0a"),
        "card": colour("#1d1d1d"),
        "hero": colour("#0a0a0a"),
        "inverse": colour("#ffffff"),
        "footer": colour("#0a0a0a"),
    }
    dark["text"] = {
        "primary": colour("#ffffff"),
        "secondary": colour("#b6b6b6"),
        "muted": colour("#939393"),
        "on-hero": colour("#ffffff"),
        "on-hero-muted": colour("#ffffff8f"),
        "on-inverse": colour("#2a2a2a"),
        "brand": colour("#ff5b49"),
        "link": colour("#4796f3"),
        "success": colour("#35c182"),
        "danger": colour("#dd3c3c"),
        "warning": colour("#f48731"),
        "disabled": colour("#939393"),
    }
    dark["accent"] = colour("#ff5b49")
    dark["border"] = {
        "default": colour("#4a4a4a"),
        "subtle": colour("#ffffff14"),
        "strong": colour("#ffffff"),
        "focus": colour("#b6b6b6"),
        "glass": colour("#ffffff29"),
    }
    dark_note = (
        "Declared, not painted: [data-theme=dark], .dark overrides in 0gwmdb80dmu1h.css. "
        "The public pages did not expose a theme switch. prefers-color-scheme was dark in "
        "the browser and the marketing pages still painted the light content surfaces"
    )
    for group in ("surface", "text", "border"):
        for token in dark[group].values():
            token["$extensions"] = {"source": dark_note}
    dark["accent"]["$extensions"] = {
        "source": "Declared: --sg-color-semantic-action-accent stays --sg-color-palette-brand-600 #ff5b49 in the dark block (hover moves to brand-500)"
    }
    dark["$extensions"] = {
        "notPainted": "Dark semantic colours are the stylesheet's [data-theme=dark] overrides. No public page was observed in that theme"
    }

    doc = {
        "$schema": "https://design-tokens.github.io/community-group/format/",
        "core": core,
        "light": light,
        "dark": dark,
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
        ],
        "$extensions": {
            "source": "seatgeek.com public signed-out pages, 2026-11-19. Stylesheets fetched from the live page: 0cki_b1y~_ibz.css and 0gwmdb80dmu1h.css",
            "gaps": SRC["gaps"],
        },
    }
    return doc


def render() -> str:
    """tokens.json's exact text; nothing is written."""
    return json.dumps(build(), indent=2) + "\n"


if __name__ == "__main__":
    (HERE / "tokens.json").write_text(render())
    print("tokens.json written")
