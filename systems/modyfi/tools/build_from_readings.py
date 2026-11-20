#!/usr/bin/env python3
"""Rebuild components-computed.json and css-vars.json from readings.json.

The capture walks every page and the last page must not overwrite a control
that only the homepage paints. Homepage wins for shared controls.
"""
import json
import pathlib

RAW = pathlib.Path(__file__).resolve().parent.parent / "raw"
readings = json.loads((RAW / "readings.json").read_text())
# tools/capture/crops.mjs read every control with the pointer away first, then the signup hover.
# The old homepage pass read its rest styles with the pointer still on the signup control, so the
# crop reading repairs its defaults (default_row below); a pass marked readAtRest is not repaired.
CROPS = json.loads((RAW / "crops-measured.json").read_text())
home = readings["home"]
CROP_SRC = "computed style read with the pointer away, Wayback 20250219221151 https://www.modyfi.com/, raw/crops-measured.json"


def default_row(name, row, home, crops):
    """The control's default. The old capture (2026-11-19) read the homepage's rest styles with the
    pointer still on the signup control, so its crop pass is the default there. A capture from the
    current run.mjs reads them at rest and marks the pass `readAtRest`; its readings are kept whole,
    so a recapture without a crop pass never mixes fresh readings with the old crop defaults."""
    default = {
        **row,
        "page": "home",
        "source": "computed style on %s at %spx, Wayback 20250219221151 https://www.modyfi.com/" % (row.get("sel"), home.get("innerWidth")),
    }
    rest = None if home.get("readAtRest") else crops.get(f"{name}-default")
    if rest:
        default.update({k: v for k, v in rest.items() if k != "text"})
        default["source"] = f"{CROP_SRC} ({name}-default); other fields from the homepage pass"
    return default


components = {}
for name, row in home["components"].items():
    if row.get("missing"):
        continue
    components[name] = {"states": {"default": default_row(name, row, home, CROPS)}}

# Hover: a state run.mjs saved in readings.json, else the crop pass's hover reading.
states = home.get("states") or {}
signup = components.get("signup-button")
if signup:
    hover = states.get("hover") or CROPS.get("signup-button-hover")
    if not hover:
        raise SystemExit("no signup hover reading in readings.json or crops-measured.json")
    signup["states"]["hover"] = {
        **{k: v for k, v in hover.items() if k not in ("component", "source")},
        "page": "home",
        "sel": "a.rl_navbar2_button.w-button:not(.loginbutton)",
        "source": hover.get("source") or "computed style read after signup.hover() in tools/capture/crops.mjs, Wayback 20250219221151 https://www.modyfi.com/, raw/crops-measured.json (signup-button-hover)",
        "evidence": "Measured",
    }


def cta_focus(states):
    """The CTA's focus-visible row: a saved reading is Measured; without one, the hand-entered row is
    Reconstruction."""
    focus = states.get("focus-visible")
    if focus:
        return {**{k: v for k, v in focus.items() if k != "component"}, "page": "home", "evidence": "Measured"}
    # No saved reading holds this state: the values were entered by hand here. run.mjs could not
    # force :focus-visible then (a point lookup found no node), so the state came from a
    # programmatic focus(), and its outline is the browser's own ring, not a Modyfi style.
    return {
        "color": "rgb(0, 0, 0)",
        "backgroundColor": "rgb(255, 255, 255)",
        "borderTopColor": "rgb(0, 0, 0)",
        "borderRadius": "15px",
        "outline": "rgb(153, 200, 255) auto 1px",
        "boxShadow": "none",
        "page": "home",
        "sel": "a.rl-button",
        "source": "entered by hand in tools/build_from_readings.py; no saved reading backs it. A programmatic focus() shows the browser's default ring, not a Modyfi style",
        "evidence": "Reconstruction",
    }


cta = components.get("cta-button")
if cta:
    cta["states"]["focus-visible"] = cta_focus(states)

COMPONENTS_TEXT = json.dumps({
    "source": "getComputedStyle on the Wayback replay of https://www.modyfi.com/ snapshot 20250219221151, 1440x900, 2026-11-19. Live site is a Webflow 404.",
    "viewport": {"width": home.get("innerWidth"), "height": home.get("innerHeight")},
    "components": components,
}, indent=2) + "\n"
VARS_TEXT = json.dumps({
    "source": "computed custom properties on :root of Wayback 20250219221151 https://www.modyfi.com/",
    "resolved": home.get("vars") or {},
    "body": home.get("body") or {},
    "title": home.get("title") or "",
}, indent=2) + "\n"

if __name__ == "__main__":
    (RAW / "components-computed.json").write_text(COMPONENTS_TEXT)
    (RAW / "css-vars.json").write_text(VARS_TEXT)
    print("components", list(components))
    print("signup bg", components["signup-button"]["states"]["default"]["backgroundColor"])
    print("vars", len(home.get("vars") or {}))
