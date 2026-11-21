#!/usr/bin/env python3
"""Build tokens.json from raw/readings.json.

Public marketing site only, measured 2026-11-21 from https://makersite.io/.
The site paints one light theme. Values are computed styles and declared
custom properties. Nothing is filled from memory.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "readings.json").read_text())
PAGE = RAW["page"]
RUN = RAW["captured"]


def src(note, prop, file="raw/readings.json"):
    return {
        "label": "Measured",
        "file": file,
        "property": prop,
        "page": PAGE,
        "run": RUN,
        "note": note,
    }


def color(value, note, prop):
    return {"$type": "color", "$value": value, "$extensions": {"source": src(note, prop)}}


def dim(value, note, prop):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": src(note, prop)}}


def font(value, note, prop):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": src(note, prop)}}


def weight(value, note, prop):
    return {"$type": "fontWeight", "$value": value, "$extensions": {"source": src(note, prop)}}


c = RAW["computed"]
tokens = {
    "core": {
        "font": {
            "display": font("ArboriaMedium", "Painted h1 and h2 family.", "computed.h1.fontFamily"),
            "body": font("ArboriaMedium", "Painted body family.", "computed.body.fontFamily"),
            "bold": font("ArboriaBold", "Painted button family.", "computed.bookADemo.fontFamily"),
            "book": font("ArboriaBook", "Declared @font-face. Not sampled on a role.", "fontFaces"),
        },
        "fontSize": {
            "display": dim("64px", "Homepage h1.", "computed.h1.fontSize"),
            "heading": dim("44px", "First h2 on the homepage.", "computed.h2.fontSize"),
            "body": dim("16px", "Body.", "computed.body.fontSize"),
            "button": dim("16px", "Book a Demo.", "computed.bookADemo.fontSize"),
        },
        "lineHeight": {
            "display": dim("69px", "Homepage h1.", "computed.h1.lineHeight"),
            "heading": dim("53px", "First h2.", "computed.h2.lineHeight"),
            "body": dim("24px", "Body.", "computed.body.lineHeight"),
            "button": dim("18px", "Book a Demo.", "computed.bookADemo.lineHeight"),
        },
        "fontWeight": {
            "display": weight("500", "Homepage h1.", "computed.h1.fontWeight"),
            "body": weight("400", "Body.", "computed.body.fontWeight"),
            "button": weight("700", "Book a Demo.", "computed.bookADemo.fontWeight"),
        },
        "space": {
            "button-x": dim("32px", "Book a Demo horizontal padding.", "computed.bookADemo.padding"),
            "button-y": dim("16px", "Book a Demo vertical padding.", "computed.bookADemo.padding"),
        },
        "radius": {
            "button": dim("0px", "Book a Demo. Square corners.", "computed.bookADemo.borderRadius"),
            "content-blocker": dim("4px", "Borlabs content-blocker radius.", "computed.contentBlocker.radius"),
        },
        "borderWidth": {
            "button": dim("1px", "Book a Demo border.", "computed.bookADemo.border"),
        },
    },
    "light": {
        "color": {
            "page": color("#ffffff", "Body background rgb(255, 255, 255).", "computed.body.backgroundColor"),
            "surface": color("#003c4f", "Hero stage and footer rgb(0, 60, 79). Also the favicon fill.", "computed.stage.backgroundColor"),
            "text": color("#404040", "Body text rgb(64, 64, 64).", "computed.body.color"),
            "text-on-accent": color("#ffffff", "Hero h1 rgb(255, 255, 255).", "computed.h1.color"),
            "accent": color("#003c4f", "Button label and heading rgb(0, 60, 79).", "computed.bookADemo.color"),
            "accent-hover": color("#00747a", "Content-blocker button hover custom property. Not a homepage button hover.", "computed.contentBlocker.buttonHover"),
            "announce": color("#deff00", "Announcement bar rgb(222, 255, 0).", "computed.announcement.backgroundColor"),
            "button-fill": color("#f0f3f4", "Left stop of the Book a Demo gradient rgb(240, 243, 244).", "computed.bookADemo.backgroundImage"),
            "focus": color("#e2e9eb", "Focus outline on Book a Demo rgb(226, 233, 235).", "computed.bookADemo.focusOutline"),
            "border-on-hero": color("#ffffff", "Button border on the hero.", "computed.bookADemo.border"),
        }
    },
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}],
}

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1) + "\n")
print("wrote", HERE / "tokens.json")
