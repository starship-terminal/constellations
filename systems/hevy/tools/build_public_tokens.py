#!/usr/bin/env python3
"""Merge a public-web token set into the existing iOS tokens.json.

Reads systems/hevy/raw/home-computed.json and raw/public-computed.json.
Does not invent a value the readers did not record. Existing light and
dark sets stay as the iOS capture wrote them.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = ROOT / "tokens.json"
HOME = ROOT / "raw" / "home-computed.json"
PUBLIC = ROOT / "raw" / "public-computed.json"


def token(value, type_, evidence, capture, description):
    return {
        "$value": value,
        "$type": type_,
        "$description": description,
        "$extensions": {
            "source": {"evidence": evidence, "capture": capture},
        },
    }


def main():
    home = json.loads(HOME.read_text())
    public = json.loads(PUBLIC.read_text())
    data = json.loads(TOKENS.read_text())

    body = home["body"]
    h1 = home["h1"]
    login = home["login"]
    signup = home["signup"]
    accent = next(row for row in public["accent"] if row.get("text") == "Get Stronger")
    menu = public["menuStyle"][0]
    search = public["search"]["input"]
    search_button = public["search"]["button"]

    web = {
        "color": {
            "page": token(
                body["backgroundColor"], "color", "Measured",
                "raw/home-computed.json",
                "body backgroundColor on https://www.hevyapp.com/ at 1440.",
            ),
            "text": token(
                body["color"], "color", "Measured",
                "raw/home-computed.json",
                "body color on the homepage.",
            ),
            "heading": token(
                h1["color"], "color", "Measured",
                "raw/home-computed.json",
                "h1 color, the black hero line.",
            ),
            "accent": token(
                accent["color"], "color", "Measured",
                "raw/public-computed.json",
                "Computed color of the hero line Get Stronger.",
            ),
            "link": token(
                login["color"], "color", "Measured",
                "raw/home-computed.json",
                "Log in link color. Same rgb as the hero accent.",
            ),
            "linkHover": token(
                "rgb(29, 131, 234)", "color", "Measured",
                "raw/public-computed.json",
                "A second blue on in-page links such as How to Get Started.",
            ),
            "onAccent": token(
                signup["color"], "color", "Measured",
                "raw/home-computed.json",
                "Sign Up label color.",
            ),
            "menu": token(
                menu["bg"], "color", "Measured",
                "raw/public-computed.json",
                "Product dropdown background.",
            ),
            "searchButton": token(
                search_button["backgroundColor"], "color", "Measured",
                "raw/public-computed.json",
                "Exercise library search button. A third blue, not the hero accent.",
            ),
        },
        "font": {
            "family": token(
                body["fontFamily"], "fontFamily", "Measured",
                "raw/home-computed.json",
                "Computed font-family on body. The webfont file is not in the repo.",
            ),
            "bodySize": token(body["fontSize"], "dimension", "Measured", "raw/home-computed.json", "body font-size."),
            "bodyWeight": token(body["fontWeight"], "fontWeight", "Measured", "raw/home-computed.json", "body font-weight."),
            "bodyLineHeight": token(body["lineHeight"], "dimension", "Measured", "raw/home-computed.json", "body line-height."),
            "displaySize": token(h1["fontSize"], "dimension", "Measured", "raw/home-computed.json", "h1 font-size."),
            "displayWeight": token(h1["fontWeight"], "fontWeight", "Measured", "raw/home-computed.json", "h1 font-weight."),
            "displayLineHeight": token(h1["lineHeight"], "dimension", "Measured", "raw/home-computed.json", "h1 line-height."),
            "navSize": token(login["fontSize"], "dimension", "Measured", "raw/home-computed.json", "Log in font-size."),
            "navWeight": token(login["fontWeight"], "fontWeight", "Measured", "raw/home-computed.json", "Log in font-weight."),
        },
        "radius": {
            "signup": token(
                signup["borderRadius"], "dimension", "Measured",
                "raw/home-computed.json",
                "Sign Up computed border-radius. The painted corner reads as 12px; the computed value is 11.3213px.",
            ),
            "menu": token(menu["radius"], "dimension", "Measured", "raw/public-computed.json", "Product dropdown border-radius."),
        },
        "size": {
            "signup": token(
                {"width": f"{signup['w']}px", "height": f"{signup['h']}px"},
                "dimension", "Measured", "raw/home-computed.json",
                "Sign Up bounding box at 1440.",
            ),
            "search": token(
                {"width": f"{search['w']}px", "height": f"{search['h']}px"},
                "dimension", "Measured", "raw/public-computed.json",
                "Exercise library search field bounding box. Width is the field, not a token.",
            ),
            "menu": token(
                {"width": f"{menu['w']}px"},
                "dimension", "Measured", "raw/public-computed.json",
                "Product dropdown width.",
            ),
        },
        "elevation": {
            "menu": token(
                menu["shadow"], "shadow", "Measured",
                "raw/public-computed.json",
                "Product dropdown box-shadow.",
            ),
        },
    }
    data["public-web"] = web
    order = data.setdefault("$metadata", {}).get("tokenSetOrder")
    if isinstance(order, list) and "public-web" not in order:
        order.append("public-web")
    TOKENS.write_text(json.dumps(data, indent=2) + "\n")
    print("wrote public-web set")


if __name__ == "__main__":
    main()
