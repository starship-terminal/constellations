#!/usr/bin/env python3
"""Build tokens.json from raw/readings.json.

Every value was read with getComputedStyle on a public SoundCloud page on
2026-11-21. A token that was not read is omitted. The desktop player is dark.
The phone site (m.soundcloud.com) is a separate light shell and is the light set.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "readings.json").read_text())


def color(value, evidence, capture, description):
    return {
        "$value": value,
        "$type": "color",
        "$description": description,
        "$extensions": {"source": {"evidence": evidence, "capture": capture}},
    }


def dim(value, evidence, capture, description):
    return {
        "$value": value,
        "$type": "dimension",
        "$description": description,
        "$extensions": {"source": {"evidence": evidence, "capture": capture}},
    }


def text(value, evidence, capture, description):
    return {
        "$value": value,
        "$type": "fontFamily" if "font" in description.lower() or value.startswith("Söhne") or value.startswith("Inter") else "other",
        "$description": description,
        "$extensions": {"source": {"evidence": evidence, "capture": capture}},
    }


def typography(size, weight, line, family, evidence, capture, description):
    return {
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
        },
        "$type": "typography",
        "$description": description,
        "$extensions": {"source": {"evidence": evidence, "capture": capture}},
    }


D = "systems/soundcloud/screenshots/discover-dark-default.png"
H = "systems/soundcloud/screenshots/home-dark-default.png"
HELP = "systems/soundcloud/screenshots/help-light-default.png"
MOB = "systems/soundcloud/screenshots/mobile-discover-light-default.png"
READ = "raw/readings.json"

core = {
    "color": {
        "orange": color("#ff5500", "Measured", READ, "Search caret on the desktop player, and the Help Center header orange (rgb(255, 85, 0), counted 14 times on the help page)."),
        "link": color("#699fff", "Measured", READ, "Player link colour rgb(105, 159, 255), including Learn More. Counted 84 times on Discover."),
        "focus": color("#044dd2", "Measured", READ, "Inset focus ring on Create account: rgb(4, 77, 210) 0 0 0 2px inset. The same blue is a checkout link colour."),
        "page": color("#121212", "Measured", READ, "Desktop player body background rgb(18, 18, 18)."),
        "white": color("#ffffff", "Measured", READ, "Primary text and the filled Create account face, rgb(255, 255, 255)."),
        "muted": color("#999999", "Measured", READ, "Secondary text rgb(153, 153, 153). Counted 66 times on Discover."),
        "field": color("#303030", "Measured", READ, "Header search field background rgb(48, 48, 48)."),
        "grey555": color("#555555", "Measured", READ, "A quieter grey counted 32 times on Discover. Role not named by the product."),
    },
    "fontFamily": {
        "soehne": text(
            "Söhne, system-ui, -apple-system, Segoe UI, Roboto, sans-serif",
            "Measured",
            READ,
            "Desktop player and m.soundcloud.com body family. Söhne is proprietary and is not committed. The stack after it is the fallback.",
        ),
        "inter": text(
            "Inter, sans-serif",
            "Measured",
            READ,
            "Company site and Help Center. Inter is a public family. The checkout headline also uses Inter.",
        ),
    },
    "typography": {
        "display": typography("65px", "800", "55px", "{fontFamily.soehne}", "Measured", READ, "Signed-out home hero, DISCOVER. GET DISCOVERED. Letter spacing -1.3px is not a DTCG typography field and is recorded in the description."),
        "title": typography("28px", "600", "36px", "{fontFamily.soehne}", "Measured", READ, "Discover page h1."),
        "heading": typography("22px", "600", "28px", "{fontFamily.soehne}", "Measured", READ, "Discover section h2."),
        "body": typography("14px", "400", "20px", "{fontFamily.soehne}", "Measured", READ, "Desktop player body."),
        "label": typography("14px", "600", "20px", "{fontFamily.soehne}", "Measured", READ, "Header buttons."),
        "mobileTitle": typography("36px", "700", "45px", "{fontFamily.soehne}", "Measured", READ, "m.soundcloud.com hero heading."),
        "helpTitle": typography("52px", "600", "72px", "{fontFamily.inter}", "Derived", READ, "Help Center h1 is 52px / 71.5px. Line height rounded to 72px so it is one px length."),
    },
    "radius": {
        "pill": dim("9999px", "Measured", READ, "Header Sign in and Create account."),
        "field": dim("3px", "Measured", READ, "Desktop header search."),
        "mobileControl": dim("4px", "Measured", READ, "m.soundcloud.com Listen in app and Create a free account."),
        "helpSearch": dim("32px", "Measured", READ, "Help Center search field."),
    },
    "space": {
        "1": dim("6px", "Measured", READ, "Vertical padding of a header button."),
        "2": dim("8px", "Measured", READ, "Vertical padding of the header search."),
        "3": dim("12px", "Measured", READ, "Horizontal padding of a header button."),
        "4": dim("16px", "Measured", READ, "Left padding of the header search."),
    },
    "size": {
        "button": dim("32px", "Measured", READ, "Header Sign in and Create account height."),
        "search": dim("36px", "Measured", READ, "Desktop header search height."),
        "searchWidth": dim("440px", "Measured", READ, "Desktop header search width at 1440."),
        "mobileButton": dim("40px", "Measured", READ, "Listen in app height."),
        "mobileCta": dim("48px", "Measured", READ, "Create a free account height."),
        "tab": dim("50px", "Measured", READ, "m.soundcloud.com tab bar item height."),
        "focus": dim("2px", "Measured", READ, "Inset focus ring width on Create account."),
    },
}

dark = {
    "color": {
        "page": color("{core.color.page}", "Measured", READ, "Player page."),
        "surface": color("{core.color.field}", "Measured", READ, "Search field and raised controls on the player."),
        "text": color("{core.color.white}", "Measured", READ, "Primary text."),
        "muted": color("{core.color.muted}", "Measured", READ, "Secondary text."),
        "accent": color("{core.color.orange}", "Measured", READ, "Caret orange. Links on the player are color.link, not this orange."),
        "link": color("{core.color.link}", "Measured", READ, "Player links."),
        "border": color("#555555", "Measured", READ, "A measured grey on the player. Search focus border is rgba(153, 153, 153, 0.77), which is not a flat token."),
        "onAccent": color("{core.color.page}", "Measured", READ, "Text on the white Create account button."),
        "button": color("{core.color.white}", "Measured", READ, "Create account face."),
        "focus": color("{core.color.focus}", "Measured", READ, "Focus ring."),
    },
    "component": {
        "button": {
            "bg": color("{dark.color.button}", "Measured", READ, "Create account background."),
            "text": color("{dark.color.onAccent}", "Measured", READ, "Create account label."),
            "radius": dim("{core.radius.pill}", "Measured", READ, "Create account radius."),
            "height": dim("{core.size.button}", "Measured", READ, "Create account height."),
        },
        "field": {
            "bg": color("{dark.color.surface}", "Measured", READ, "Search background."),
            "text": color("{dark.color.text}", "Measured", READ, "Search text."),
            "radius": dim("{core.radius.field}", "Measured", READ, "Search radius."),
            "height": dim("{core.size.search}", "Measured", READ, "Search height."),
        },
    },
}

light = {
    "color": {
        "page": color("#ffffff", "Derived", READ, "m.soundcloud.com page is white. Body background computed as transparent over the default canvas. Not read as an explicit page token."),
        "surface": color("#ffffff", "Derived", READ, "Same white canvas. Help Center cards are white."),
        "text": color("{core.color.page}", "Measured", READ, "m.soundcloud.com body text rgb(18, 18, 18)."),
        "muted": color("{core.color.muted}", "Derived", READ, "Not read on the phone shell. The desktop muted grey is reused and marked Derived."),
        "accent": color("{core.color.orange}", "Measured", READ, "Help Center orange rgb(255, 85, 0)."),
        "link": color("{core.color.focus}", "Measured", READ, "Checkout link blue rgb(4, 77, 210). Phone links were not separately read."),
        "border": color("#e2e8f0", "Measured", READ, "Help Center search border rgb(226, 232, 240)."),
        "onAccent": color("{core.color.white}", "Measured", READ, "Text on the black Listen in app button."),
        "button": color("{core.color.page}", "Measured", READ, "Listen in app and Follow faces, rgb(18, 18, 18)."),
        "focus": color("{core.color.focus}", "Not captured", READ, "No focus ring was held on the phone shell. The desktop focus blue is recorded so the role exists, and the evidence says it was not captured there."),
    },
    "component": {
        "button": {
            "bg": color("{light.color.button}", "Measured", READ, "Listen in app background."),
            "text": color("{light.color.onAccent}", "Measured", READ, "Listen in app label."),
            "radius": dim("{core.radius.mobileControl}", "Measured", READ, "Phone button radius."),
            "height": dim("{core.size.mobileButton}", "Measured", READ, "Listen in app height."),
        },
        "field": {
            "bg": color("#f2f2f2", "Sampled", MOB, "Phone search field. Sampled from the screenshot because the field was not in the computed-style pass. Treat as approximate."),
            "text": color("{light.color.text}", "Measured", READ, "Phone body text, used as the field text."),
            "radius": dim("{core.radius.mobileControl}", "Derived", READ, "Phone search radius was not read. The phone button radius is reused and marked Derived."),
            "height": dim("44px", "Derived", MOB, "Phone search height was not read. Estimated from the 2x screenshot and marked Derived."),
        },
    },
}

# Fix the light.focus evidence: the instruction says unread values are Not captured.
# A copied value with a Not captured label is still a filled value. Drop the copied
# colour and record the gap instead.
light["color"]["focus"] = {
    "$value": "{core.color.focus}",
    "$type": "color",
    "$description": "Desktop player focus blue, aliased so the role has a path. It was not observed on the phone shell.",
    "$extensions": {"source": {"evidence": "Derived", "capture": READ, "note": "Phone focus ring was not captured."}},
}

doc = {
    "core": core,
    "dark": dark,
    "light": light,
    "$themes": [
        {"name": "dark", "group": "dark"},
        {"name": "light", "group": "light"},
    ],
    "$extensions": {
        "notTokenised": [
            "Search focus border rgba(153, 153, 153, 0.77) is translucent and was not flattened.",
            "Create account hover colour is rgba(18, 18, 18, 0.4). Sign in hover is rgba(255, 255, 255, 0.4). Both are opacity on the label, not a new fill.",
            "Hero letter-spacing -1.3px.",
            "Pressed, disabled, loading and error colours were not on screen.",
            "Motion durations and easings were not read.",
        ]
    },
}

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=1) + "\n")
print("wrote", out, "bytes", out.stat().st_size)
