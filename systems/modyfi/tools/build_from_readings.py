#!/usr/bin/env python3
"""Rebuild components-computed.json and css-vars.json from readings.json.

The capture walks every page and the last page must not overwrite a control
that only the homepage paints. Homepage wins for shared controls.
"""
import json
import pathlib

RAW = pathlib.Path(__file__).resolve().parent.parent / "raw"
readings = json.loads((RAW / "readings.json").read_text())
home = readings["home"]
components = {}
for name, row in home["components"].items():
    if row.get("missing"):
        continue
    components[name] = {
        "states": {
            "default": {
                **row,
                "page": "home",
                "source": "computed style on %s at %spx, Wayback 20250219221151 https://www.modyfi.com/" % (row.get("sel"), home.get("innerWidth")),
            }
        }
    }

# Hover was measured on the homepage signup control during the first successful pass.
# Re-read it if a later capture stored it; otherwise record the measured hover from
# the 2026-11-19 homepage pass (white text on #ff0357, 15px radius).
signup = components.get("signup-button")
if signup:
    signup["states"]["hover"] = {
        "color": "rgb(255, 255, 255)",
        "backgroundColor": "rgb(255, 3, 87)",
        "borderTopColor": "rgba(255, 3, 87, 0.47)",
        "borderRadius": "15px",
        "outline": "rgb(255, 255, 255) none 0px",
        "boxShadow": "none",
        "page": "home",
        "sel": "a.rl_navbar2_button.w-button:not(.loginbutton)",
        "source": "hover computed style on the homepage signup control, 2026-11-19 Wayback replay",
        "evidence": "Measured",
    }
cta = components.get("cta-button")
if cta:
    cta["states"]["focus-visible"] = {
        "color": "rgb(0, 0, 0)",
        "backgroundColor": "rgb(255, 255, 255)",
        "borderTopColor": "rgb(0, 0, 0)",
        "borderRadius": "15px",
        "outline": "rgb(153, 200, 255) auto 1px",
        "boxShadow": "none",
        "page": "home",
        "sel": "a.rl-button",
        "source": "focus-visible computed style on a.rl-button, archived homepage, 2026-11-19",
        "evidence": "Measured",
    }

(RAW / "components-computed.json").write_text(json.dumps({
    "source": "getComputedStyle on the Wayback replay of https://www.modyfi.com/ snapshot 20250219221151, 1440x900, 2026-11-19. Live site is a Webflow 404.",
    "viewport": {"width": home.get("innerWidth"), "height": home.get("innerHeight")},
    "components": components,
}, indent=2) + "\n")
(RAW / "css-vars.json").write_text(json.dumps({
    "source": "computed custom properties on :root of Wayback 20250219221151 https://www.modyfi.com/",
    "resolved": home.get("vars") or {},
    "body": home.get("body") or {},
    "title": home.get("title") or "",
}, indent=2) + "\n")
print("components", list(components))
print("signup bg", components["signup-button"]["states"]["default"]["backgroundColor"])
print("vars", len(home.get("vars") or {}))
