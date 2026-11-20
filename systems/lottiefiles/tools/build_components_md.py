#!/usr/bin/env python3
"""Write components.md from the measured component readings."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "components-computed.json").read_text())
lines = [
    "# Components",
    "",
    "Public controls on lottiefiles.com, measured 2026-11-21 from computed styles. Crops are 2x screenshots of the element. A missing state is listed under Gaps.",
    "",
]
for name, states in RAW["components"].items():
    lines.append(f"## {name}")
    lines.append("")
    for state, data in states.items():
        if data.get("missing"):
            lines.append(f"- {state}: not captured ({data.get('via')})")
            continue
        crop = HERE / "components" / "crops" / f"{name}-{state}.png"
        shot = f"[{name}-{state}.png](components/crops/{name}-{state}.png)" if crop.exists() else "no crop"
        lines.append(f"- {state}: {shot}. bg `{data.get('backgroundColor')}`, text `{data.get('color')}`, {data.get('fontSize')}/{data.get('fontWeight')}, radius `{data.get('borderRadius')}`, height `{data.get('height')}`. Via {data.get('via')}.")
    lines.append("")
lines += [
    "## Gaps",
    "",
    "- Checkbox, radio, switch, tabs, tooltip, toast, table, avatar, select: not present as product controls on the captured public pages. Pricing has a hire-status switch that is an account control, not a theme switch.",
    "- Disabled, loading, error, pressed: not shown on the public pages. Pressed was not forced.",
    "- Focus ring: keyboard Tab did not land on the hero CTA in the probe. The search button carries a 1px border-coloured outline. Focus ring token is not captured as a measured focus-visible ring.",
    "- Dark theme: not present. `--color-*-inverse` tokens exist and paint inverse sections, not a second theme.",
    "- Signed-in app components: behind login.lottiefiles.com. Not captured.",
    "",
]
(HERE / "components.md").write_text("\n".join(lines))
print("wrote components.md")
