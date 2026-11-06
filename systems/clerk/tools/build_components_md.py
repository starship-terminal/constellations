#!/usr/bin/env python3
"""Build the component inventory from raw/components-manifest.json.

Manifest: {components:[{id,title,description,states:[{name,reading,
elementIndex,crop,screenshot}]}], gaps:[...]}.
An entry may put reading/elementIndex directly on itself for one default state.
The reading value is the filename under raw/readings/. This script deliberately
does not derive component labels from account text in the live readings.
"""
import json
import re
from pathlib import Path

from build_tokens import COMPONENT_PROPS, read_all

HERE = Path(__file__).resolve().parent.parent


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def build():
    path = HERE / "raw" / "components-manifest.json"
    if not path.exists():
        raise SystemExit("Need raw/components-manifest.json; no component names inferred from account text")
    manifest = json.loads(path.read_text())
    readings = {p.name: (p, data, theme) for p, data, theme in read_all()}
    lines = ["# Clerk dashboard components", "",
             "Measured values come from live computed styles. Images linked below are observed product captures. The style guide's token specimens are reconstructions, not captured components.", "",
             "Measured input, checkbox and switch readings may refer to an unpainted native helper. The screenshots show the visible control; helper dimensions and colours do not establish the painted wrapper's geometry or state styles.", "",
             "## Inventory", ""]
    for component in manifest["components"]:
        lines.extend([f"### {component.get('title', component['id'])}", "",
                      component.get("description", ""), ""])
        if component.get("status") == "not-captured":
            lines.extend(["**Not captured.** " + component.get("gap", "No corresponding state was captured."), ""])
            continue
        states = component.get("states") or [{"name": "default", **component}]
        for state in states:
            filename = state.get("reading", component.get("reading"))
            index = state.get("elementIndex", component.get("elementIndex"))
            name = state.get("name", "default")
            observed_only = state.get("observedOnly", component.get("observedOnly"))
            if observed_only:
                lines.extend([f"**{name}. Observed only.** No computed-style value is assigned to this visible component.", ""])
            else:
                reading_path, data, theme = readings[filename]
                element = next(e for e in data["elements"] if e["index"] == index)
                lines.extend([f"**{name}, {theme}.** Measured on element {index} (`{element['tag']}`), {data['width']} x {data['height']} CSS px. [Reading]({reading_path.relative_to(HERE).as_posix()}).", ""])
            if state.get("note"):
                lines.extend([state["note"], ""])
            for key in ("crop", "screenshot"):
                if state.get(key):
                    asset = state[key]
                    if not (HERE / asset).is_file():
                        raise SystemExit(f"Missing {key}: {asset}")
                    if key == "crop":
                        lines.extend([f"![{cell(component.get('title', component['id']))}, {name}]({asset})", ""])
                    else:
                        lines.extend([f"[Whole screenshot, {cell(name)}]({asset}).", ""])
            if observed_only:
                continue
            lines.extend(["| Property | Measured value | Token |", "|---|---|---|"])
            for prop, value in sorted(element["styles"].items()):
                state_key = re.sub(r"[^a-zA-Z0-9_-]", "-", name)
                token_path = f"{theme}.component.{component['id']}.{state_key}.{COMPONENT_PROPS.get(prop, prop)}"
                has_token = prop in COMPONENT_PROPS and value not in ("normal", "auto", "none", "")
                lines.append(f"| {prop} | `{cell(value)}` | {f'`{token_path}`' if has_token else 'Raw reading only'} |")
            lines.append("")
    lines.extend(["## Gaps", ""])
    lines.extend(f"- {gap}" for gap in manifest.get("gaps", ["Only listed states were captured. Other component states remain not captured."]))
    lines.append("")
    (HERE / "components.md").write_text("\n".join(lines))
    print(f"components.md: {len(manifest['components'])} named components")


if __name__ == "__main__":
    build()
