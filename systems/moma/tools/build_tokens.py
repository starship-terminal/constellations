#!/usr/bin/env python3
"""Build systems/moma/tokens.json from raw/css-vars.json.

MoMA publishes one light theme. Colours are the :root custom properties in
sol.css, confirmed computed on www.moma.org. Type sizes are the
$typography/size classes times --rem-conversion (0.1rem) at a 10px root,
confirmed on the live Welcome heading (60px, weight 900, tracking -1.2px).
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
ROOT = RAW["root"]
MOTION = RAW["motion"]
SHEET = "sol.css :root"


def color(value, source, evidence="Measured"):
    return {
        "$type": "color",
        "$value": value,
        "$extensions": {"source": f"{evidence}. {source}"},
    }


def dim(value, source, evidence="Measured"):
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": f"{evidence}. {source}"},
    }


def duration(value, source):
    """A time is a DTCG duration, not a dimension (consumers that expect one length drop it)."""
    return {
        "$type": "duration",
        "$value": value,
        "$extensions": {"source": f"Measured. {source}"},
    }


def font(value, source, derived=False):
    return {
        "$type": "fontFamily",
        "$value": value,
        "$extensions": {"source": ("Derived. " if derived else "Measured. ") + source},
    }


def number(value, source):
    return {
        "$type": "number",
        "$value": value,
        "$extensions": {"source": f"Measured. {source}"},
    }


def typography(size, weight, line, tracking, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": "{font.family.sans}",
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
            "letterSpacing": tracking,
        },
        "$extensions": {"source": f"Measured. {source}"},
    }


core_color = {}
for key, value in ROOT.items():
    if not key.startswith("--color--"):
        continue
    if key.endswith("--rgb") or value.startswith("var("):
        continue
    parts = key.replace("--color--", "").split("--")
    node = core_color
    for part in parts[:-1]:
        node = node.setdefault(part, {})
    node[parts[-1]] = color(value, f"{SHEET} {key}")

sizes = {
    "display": ("60px", "60px", "-1.2px", "h1 Welcome, class $typography/size:extra-extra-large, computed 1440px"),
    "title": ("40px", "40px", "-0.8px", "h2 Exhibitions, class $typography/size:extra-large, computed"),
    "card-title": ("30px", "30px", "-0.6px", "exhibition card title, class $typography/size:medium-large, computed"),
    "body": ("18px", "18px", "normal", "body copy 'The museum is open', weight 400, computed"),
    "ui": ("16px", "18px", "normal", "$typography/size:medium is --typography--size 16 times 0.1rem; line-height measured 18px on truncated card text"),
    "nav": ("13.333px", "normal", "normal", "Visit button, computed font-size 13.3333px, weight 400"),
    "chrome": ("10px", "10px", "normal", "Tickets and Donate links, computed 10px. Matches html font-size from --typography--size 10"),
}

core = {
    "color": core_color,
    "font": {
        "family": {
            "sans": font(
                "MoMA Sans, Helvetica, sans-serif",
                'computed font-family on body: "MoMA Sans", "MoMA Sans", Helvetica, sans-serif. @font-face src is /dist/dist/moma-sans/*.woff2. Proprietary. Token stack drops the duplicate family name.',
                derived=True,
            ),
            "sans-condensed": font(
                "MoMA Sans Condensed, Helvetica, sans-serif",
                "@font-face in sol.css. Not the computed body family on the captured pages.",
            ),
        }
    },
    "typography": {
        name: typography(size, 900 if name in ("display", "title", "card-title") else 400, line, tracking, source)
        for name, (size, line, tracking, source) in sizes.items()
    },
    "spacing": {
        "page": dim("32px", "computed --page-spacing 3.2rem at 10px root on www.moma.org 1440px"),
        "page-fixed": dim("48px", "computed --page-spacing--fixed 4.8rem at 10px root"),
        "header": dim("166px", "computed --header-height 16.6rem and header.getBoundingClientRect().height 166"),
        "focus": dim("2px", "--focus-thickness 0.2rem"),
        "control-pad": dim("8px", "computed padding 8px on Visit, Tickets, Donate"),
    },
    "radius": {
        "none": dim("0px", "computed border-radius 0px on header, cards, Tickets, Donate, Join"),
        "focus": dim("4px", "--focus-radius 0.4rem"),
        "pill": dim("999px", "A stand-in for a full pill: the Help chip on the login card is one. No radius was read for it.", evidence="Reconstruction"),
    },
    "motion": {
        "duration": {
            "100": duration("100ms", f"{SHEET} {MOTION['--motion--transition--duration']} via --motion--transition--duration"),
            "200": duration("200ms", "--motion--transition--color--duration and --motion--transition--transform--duration"),
            "4000": duration("4000ms", "--motion--animation--duration"),
        },
        "easing": {
            "in": {"$type": "cubicBezier", "$value": [0.42, 0, 1, 1], "$extensions": {"source": "Derived. --motion--transition--curve ease-in expanded to control points."}},
            "in-out": {"$type": "cubicBezier", "$value": [0.42, 0, 0.58, 1], "$extensions": {"source": "Derived. --motion--transition--transform--curve ease-in-out."}},
        },
    },
}

# fix motion duration sources to name the property
core["motion"]["duration"]["100"]["$extensions"]["source"] = "Measured. sol.css --motion--transition--duration 100ms"
core["motion"]["duration"]["200"]["$extensions"]["source"] = "Measured. sol.css --motion--transition--color--duration 200ms"
core["motion"]["duration"]["4000"]["$extensions"]["source"] = "Measured. sol.css --motion--animation--duration 4000ms"

light = {
    "color": {
        "page": color("#ffffff", "computed body background is transparent over the white page; --color--white #fff. Tickets text is rgb(0,0,0) on the brand-10 fill."),
        "surface": color("#eeeeee", "--color--gray--eee. Donate carries $color/background:gray:eee."),
        "text": color("#000000", "computed color rgb(0, 0, 0) on h1 and body. --color--black #000"),
        "muted": color("#767676", "computed color rgb(118, 118, 118) on exhibition dates, class $color/gray:767. --color--gray--767"),
        "accent": color("#00b7f2", "--color--brand--10. Tickets carries $color/background:brand:10. Session colour also aliases this step when html is $color/session:10."),
        "border": color("#000000", "1px solid black on the login card, seen in login-light-default.png; no computed reading of the card border is saved. Focus colour --color--focus resolves to --color--black.", evidence="Observed"),
        "danger": color("#e42d00", "--color--red. 'Error 404' on the /members/ miss paints this red."),
        "footer": color("#444444", "computed footer background rgb(68, 68, 68). --color--gray--444"),
        "brand": {
            str(i): color(ROOT[f"--color--brand--{i}"], f"--color--brand--{i}")
            for i in range(1, 13)
        },
        "membership": {
            str(i): color(ROOT[f"--color--membership--{i}"], f"--color--membership--{i}. Access card fill measured rgb(213, 250, 234) = membership 6. Explore card fill measured rgb(246, 193, 230) = membership 15.")
            for i in range(1, 19)
        },
    }
}

doc = {
    "$description": "MoMA public site tokens. One light theme. Colours from sol.css :root, confirmed computed on www.moma.org and membership.moma.org on 2026-11-19.",
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

TEXT = json.dumps(doc, indent=2) + "\n"

if __name__ == "__main__":
    out = HERE / "tokens.json"
    out.write_text(TEXT)
    print("wrote", out, "bytes", out.stat().st_size)
