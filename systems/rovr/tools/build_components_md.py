#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
C = json.loads((HERE / "raw" / "components-computed.json").read_text())
comps = C["components"]

def line(name):
    c = comps[name]
    states = c.get("states", {})
    bits = []
    for st, rec in states.items():
        if rec.get("missing") or rec.get("error"):
            bits.append(f"{st}: not captured ({rec.get('error') or 'missing'})")
            continue
        crop = rec.get("crop")
        crop_bit = f" [{crop}]({crop})" if crop else ""
        bits.append(
            f"{st}{crop_bit}: {rec.get('backgroundColor')} on {rec.get('color')}, "
            f"{rec.get('fontSize')}/{rec.get('fontWeight')}, radius {rec.get('borderRadius')}, "
            f"{rec.get('rect', {}).get('w')}x{rec.get('rect', {}).get('h')}"
        )
    title = c.get("title", name)
    group = c.get("group", "")
    return f"### {title}\n\nGroup: {group}.\n\n" + "\n".join(f"- {b}" for b in bits) + "\n"

order = list(comps)
body = ["# ROVR components", "", "Measured on www.rovr.live, signed out, dark theme, 1440 px, on 2026-11-21. Crops are 2x element screenshots where the box fit the viewport.", ""]
for name in order:
    body.append(line(name))

body.append("""## Gaps

- Checkbox, radio, switch, select, text area, tooltip, toast, table, avatar and badge were not present on the public pages that were measured.
- Disabled, loading and error states of buttons were not shown, except the sign-in submit, which was captured empty and not submitted.
- Pressed states forced through CDP often match default. That is recorded as measured, not as a distinct press colour.
- The curator card selector missed. Curator cards are visible in [screenshots/curators-dark-default.png](screenshots/curators-dark-default.png).
- Drawer and dialog crops were not written: the measurement stored the open state without a crop box. The open drawer is [screenshots/home-dark-menu.png](screenshots/home-dark-menu.png). The Alexa dialog is [screenshots/home-dark-alexa.png](screenshots/home-dark-alexa.png).
- Status colours in tokens.json are derived from declared custom properties. They were not painted on a captured control.
- Signed-in states (liked tracks, saved shows, curator chat) stop at the sign-in wall.
""")
(HERE / "components.md").write_text("\n".join(body))
print("components", len(order))
