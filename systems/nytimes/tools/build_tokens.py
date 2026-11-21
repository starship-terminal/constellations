#!/usr/bin/env python3
"""Build tokens.json for the New York Times signed-in account capture.

Source: raw/component-tokens.json, values read live from www.nytimes.com/account
on 2026-11-21 (computed custom properties, light theme). The site declares dark
counterparts in the same sheets; this account had no theme control, so the
package is light only.

Every token carries $extensions.source. Deterministic: same input, same bytes.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "component-tokens.json").read_text())


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def number(value, source):
    return {"$type": "number", "$value": value, "$extensions": {"source": source}}


C = RAW["colors"]
T = RAW["type"]
S = RAW["space"]
G = RAW["geometry"]

core = {
    "color": {
        "ink": color(C["content-primary"]["$value"], C["content-primary"]["source"]),
        "body": color(C["content-primary-dim"]["$value"], C["content-primary-dim"]["source"]),
        "secondary": color(C["content-secondary"]["$value"], C["content-secondary"]["source"]),
        "muted": color(C["content-secondary-dim"]["$value"], C["content-secondary-dim"]["source"]),
        "placeholder": color(C["content-placeholder"]["$value"], C["content-placeholder"]["source"]),
        "paper": color("#ffffff", C["background-primary"]["source"]),
        "surface": color(C["background-secondary"]["$value"], C["background-secondary"]["source"]),
        "surface-tertiary": color(C["background-tertiary"]["$value"], C["background-tertiary"]["source"]),
        "highlight": color(C["background-highlight"]["$value"], C["background-highlight"]["source"]),
        "scrim": color(C["background-scrim"]["$value"], C["background-scrim"]["source"]),
        "hairline": color(C["stroke-tertiary"]["$value"], C["stroke-tertiary"]["source"]),
        "stroke": color(C["stroke-secondary"]["$value"], C["stroke-secondary"]["source"]),
        "rule": color(C["stroke-primary"]["$value"], C["stroke-primary"]["source"]),
        "link": color(C["content-accent"]["$value"], C["content-accent"]["source"]),
        "editorial": color(C["signal-editorial"]["$value"], C["signal-editorial"]["source"]),
        "positive": color(C["content-positive"]["$value"], C["content-positive"]["source"]),
        "negative": color(C["content-negative"]["$value"], C["content-negative"]["source"]),
        "breaking": color(C["content-breaking"]["$value"], C["content-breaking"]["source"]),
        "developing": color(C["signal-developing"]["$value"], C["signal-developing"]["source"]),
        "signal-accent": color(C["signal-accent"]["$value"], C["signal-accent"]["source"]),
        "emphasis": color(C["button-emphasis-bg"]["$value"], C["button-emphasis-bg"]["source"]),
        "emphasis-fg": color(C["button-emphasis-fg"]["$value"], C["button-emphasis-fg"]["source"]),
        "go": color(C["search-go"]["$value"], C["search-go"]["source"]),
        "go-border": color(C["search-go-border"]["$value"], C["search-go-border"]["source"]),
    },
    "font": {
        "franklin": font(T["franklin"]["$value"], T["franklin"]["source"]),
        "cheltenham": font(T["cheltenham"]["$value"], T["cheltenham"]["source"]),
        "imperial": font(T["imperial"]["$value"], T["imperial"]["source"]),
        "karnak": font(T["karnak"]["$value"], T["karnak"]["source"]),
    },
    "typography": {
        "greeting": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.franklin}",
                "fontSize": T["account-greeting"]["fontSize"],
                "fontWeight": int(T["account-greeting"]["fontWeight"]),
                "lineHeight": T["account-greeting"]["lineHeight"],
            },
            "$extensions": {"source": T["account-greeting"]["source"]},
        },
        "nav": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.franklin}",
                "fontSize": T["account-nav"]["fontSize"],
                "fontWeight": int(T["account-nav"]["fontWeight"]),
                "lineHeight": T["account-nav"]["lineHeight"],
            },
            "$extensions": {"source": T["account-nav"]["source"]},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.franklin}",
                "fontSize": T["update-link"]["fontSize"],
                "fontWeight": int(T["update-link"]["fontWeight"]),
                "lineHeight": T["update-link"]["lineHeight"],
            },
            "$extensions": {"source": T["update-link"]["source"]},
        },
    },
    "spacing": {k: dim(S[k], S["source"]) for k in ("1", "2", "3", "4", "5", "6", "8")},
    "radius": {
        "dialog": dim(G["dialog-radius"], G["source"]),
        "tile": dim(G["tile-radius"], G["source"]),
        "search": dim(T["search-input"]["radius"], T["search-input"]["source"]),
    },
}

light = {
    "page": color("{color.paper}", "alias of core.color.paper, the account page background"),
    "surface": color("{color.surface}", "alias of core.color.surface"),
    "text": color("{color.ink}", "alias of core.color.ink"),
    "muted": color("{color.body}", "alias of core.color.body, body text on the account page"),
    "accent": color("{color.link}", "alias of core.color.link"),
    "border": color("{color.hairline}", "alias of core.color.hairline"),
    "component": {
        "button-emphasis-bg": color("{color.emphasis}", "Connect and emphasis buttons"),
        "button-emphasis-text": color("{color.emphasis-fg}", "text on emphasis buttons"),
        "button-bg": color("{color.paper}", "outlined Disconnect button face"),
        "button-text": color("{color.ink}", "outlined button label"),
        "button-border": color("{color.rule}", "outlined button border"),
        "link-text": color("{color.ink}", "Update, Create, Manage links"),
        "nav-selected-text": color("{color.ink}", "selected account nav item"),
        "search-go-bg": color("{color.go}", "enabled masthead Go button"),
    },
}

doc = {
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}
    ],
}

def main():
    out = HERE / "tokens.json"
    out.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"wrote {out.relative_to(HERE)} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
