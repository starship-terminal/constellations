#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json, raw/components-computed.json, and raw/motion.json.

Pop Site has two surfaces. Marketing (pop.site) is a Framer page. Auth (app.pop.site)
is a separate app with Radix-style ramps. Values here are the ones those readings
measured. A colour that was declared and not painted is left out of the semantic sets.
"""
import copy
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import motion  # noqa: E402

RAW = ROOT / "raw"
CSS = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components-computed.json").read_text())


def color(value, evidence, capture):
    return {
        "$type": "color",
        "$value": value,
        "$extensions": {"source": {"evidence": evidence, "capture": capture}},
    }


def dim(value, evidence, capture):
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": {"evidence": evidence, "capture": capture}},
    }


def text(value, evidence, capture):
    """A font-family stack."""
    return {
        "$type": "fontFamily",
        "$value": value,
        "$extensions": {"source": {"evidence": evidence, "capture": capture}},
    }


def ramp(steps, evidence, capture):
    return {str(i): color(hex_, evidence, capture) for i, hex_ in steps.items()}


M = "raw/components-computed.json marketing"
A = "raw/components-computed.json auth"
V = "raw/css-vars.json"

app = CSS["app"]["light"]
marketing_tokens = CSS["marketing"]["tokens"]

core = {
    "color": {
        "marketing": {
            "ink": color("#171717", "Measured", V + " body --token-4da5a6b8"),
            "ink-soft": color("#545454", "Measured", V + " body --token-66b6d7ff"),
            "muted": color("#6e6e73", "Measured", V + " body --token-66acd1d2"),
            "page": color("#ffffff", "Measured", V + " body --token-15ca1af0"),
            "field": color("#fafafc", "Measured", V + " body --token-fa705767"),
            "line": color("#e3e3e3", "Measured", V + " body --token-a1f53698"),
            "line-strong": color("#d2d2d7", "Measured", V + " body --token-29dd526f"),
            "blue": color("#3b82f6", "Measured", V + " body --token-0b12ad74"),
            "blue-bright": color("#478eff", "Measured", V + " body --token-51154332"),
            "cyan": color("#00a8f5", "Measured", V + " body --token-271ffd78"),
            "navy": color("#00276b", "Measured", V + " body --token-57da7360"),
            "highlight": color("#ffed90", "Measured", V + " body --token-a8970b24"),
        },
        "blue": ramp(app["blue"], "Measured", V + " app light --blue"),
        "slate": ramp(app["slate"], "Measured", V + " app light --slate"),
        "grass": ramp(app["grass"], "Measured", V + " app light --grass"),
        "amber": ramp(app["amber"], "Measured", V + " app light --amber"),
        "red": ramp(app["red"], "Measured", V + " app light --red"),
    },
    "font": {
        "family": {
            "display": text(
                'Satoshi, "Satoshi Placeholder", sans-serif',
                "Measured",
                M + " h1.fontFamily",
            ),
            "ui": text(
                'satoshi, -apple-system, system-ui, sans-serif',
                "Measured",
                A + " bodyFont",
            ),
        }
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "Satoshi, sans-serif",
                "fontSize": "51px",
                "fontWeight": 500,
                "lineHeight": "51px",
                "letterSpacing": "-3.82px",
            },
            "$extensions": {"source": {"evidence": "Measured", "capture": M + " h1"}},
        },
        "title": {
            "$type": "typography",
            "$value": {
                "fontFamily": "Satoshi, sans-serif",
                "fontSize": "19px",
                "fontWeight": 500,
                "lineHeight": "26.6px",
                "letterSpacing": "-0.57px",
            },
            "$extensions": {"source": {"evidence": "Measured", "capture": M + " body19"}},
        },
        "nav": {
            "$type": "typography",
            "$value": {
                "fontFamily": "Satoshi, sans-serif",
                "fontSize": "15px",
                "fontWeight": 500,
                "lineHeight": "19.5px",
                "letterSpacing": "-0.45px",
            },
            "$extensions": {"source": {"evidence": "Measured", "capture": M + " navLink"}},
        },
        "auth-title": {
            "$type": "typography",
            "$value": {
                "fontFamily": "satoshi, sans-serif",
                "fontSize": "18px",
                "fontWeight": 700,
                "lineHeight": "27px",
            },
            "$extensions": {"source": {"evidence": "Measured", "capture": A + " title"}},
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "satoshi, sans-serif",
                "fontSize": "14px",
                "fontWeight": 500,
                "lineHeight": "21px",
            },
            "$extensions": {"source": {"evidence": "Measured", "capture": A + " label"}},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "satoshi, sans-serif",
                "fontSize": "16px",
                "fontWeight": 400,
                "lineHeight": "24px",
            },
            "$extensions": {"source": {"evidence": "Measured", "capture": A + " field"}},
        },
    },
    "space": {
        "4": dim("4px", "Measured", M + " eyebrowPill padding top"),
        "8": dim("8px", "Measured", A + " field padding top"),
        "10": dim("10px", "Measured", A + " shell padding"),
        "12": dim("12px", "Measured", A + " field padding left"),
        "16": dim("16px", "Measured", M + " claimButton padding top"),
        "20": dim("20px", "Measured", M + " sectionCard padding"),
        "24": dim("24px", "Measured", M + " claimButton padding inline"),
        "72": dim("72px", "Measured", M + " header height"),
        "80": dim("80px", "Measured", "hero section padding 80px 0, computed on the home hero wrapper"),
    },
    "radius": {
        "field": dim("6px", "Measured", A + " field.borderRadius"),
        "sm": dim("8px", "Measured", M + " radiiSeen"),
        "card": dim("10px", "Measured", M + " sectionCard.borderRadius"),
        "md": dim("12px", "Measured", M + " radiiSeen"),
        "shell": dim("20px", "Measured", A + " shell.borderRadius"),
        "phone": dim("22px", "Measured", M + " radiiSeen, phone-mock frames"),
        "claim": dim("26px", "Measured", M + " claimButton.borderRadius"),
        "pill": dim("999px", "Measured", M + " claimField inputRadius"),
    },
    "layout": {
        "content": dim("1000px", "Measured", M + " contentWidth"),
        "header": dim("72px", "Measured", M + " header.height"),
        "claim-height": dim("40px", "Measured", M + " claimButton.height"),
        "auth-shell": dim("420px", "Measured", A + " shell.width"),
        "auth-field": dim("357px", "Measured", A + " field.width"),
        "signin-height": dim("36px", "Measured", A + " signin.height"),
    },
}

light = {
    "page": color("#ffffff", "Measured", M + " page.backgroundColor"),
    "surface": color("#ffffff", "Measured", M + " sectionCard.backgroundColor"),
    "text": color("#171717", "Measured", M + " h1.color"),
    "muted": color("#545454", "Measured", M + " body19.color"),
    "accent": color("#3b82f6", "Measured", M + " linkBlue.color and claim gradient end"),
    "border": color("#e3e3e3", "Measured", V + " marketing line"),
    "focus": color("#3b82f6", "Measured", A + " fieldFocus ring is oklch(0.623 0.214 259.815), the same blue"),
    "on-accent": color("#ffffff", "Measured", M + " claimButton label color"),
    "field": color("#fafafc", "Measured", M + " claimField.suffixBackground"),
    "auth-page": color("#f3f3f3", "Measured", A + " htmlBackground"),
    "auth-text": color("#1e293b", "Measured", A + " title.color"),
    "auth-muted": color("#64748b", "Measured", A + " label.color"),
    "auth-border": color("#e5e5e5", "Measured", A + " field.border"),
    "auth-link": color("#2563eb", "Measured", A + " link.color"),
    "auth-shell-border": color("#e2e8f0", "Measured", A + " shell.border"),
    "component": {
        "claim": {
            "background": color("#3b82f6", "Measured", M + " claim gradient ends at #3b82f6; start is #00a8f5"),
            "text": color("#ffffff", "Measured", M + " claim label"),
            "radius": dim("26px", "Measured", M + " claimButton.borderRadius"),
            "height": dim("40px", "Measured", M + " claimButton.height"),
            "padding": dim("16px", "Measured", M + " claimButton padding block"),
        },
        "signin": {
            "background": color("#1e293b", "Measured", A + " signin gradient start"),
            "text": color("#ffffff", "Measured", A + " signin.color"),
            "radius": dim("999px", "Measured", A + " signin.borderRadius is the pill keyword"),
            "height": dim("36px", "Measured", A + " signin.height"),
        },
        "field": {
            "background": color("#ffffff", "Measured", "auth field backgroundColor is transparent over the white card"),
            "text": color("#1e293b", "Measured", A + " field.color"),
            "radius": dim("6px", "Measured", A + " field.borderRadius"),
            "height": dim("38px", "Measured", A + " field.height"),
        },
    },
}

def build():
    """The token document, built in memory from raw/. Writes nothing."""
    doc_core = copy.deepcopy(core)
    tokens = {
        "core": doc_core,
        "light": copy.deepcopy(light),
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}
        ],
    }
    motion_path = RAW / "motion.json"
    if motion_path.exists():
        group, not_tokenised = motion.build(json.loads(motion_path.read_text()))
        if group:
            doc_core["motion"] = group
        if not_tokenised:
            doc_core.setdefault("$extensions", {})["notTokenised"] = not_tokenised
    return tokens


def main():
    tokens = build()
    (ROOT / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
    print("tokens.json", len(json.dumps(tokens)))


if __name__ == "__main__":
    main()
