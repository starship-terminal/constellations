#!/usr/bin/env python3
"""Rename captured parts after the fact, in the readings and the screenshot names, so a review
correction does not need a new capture. Run once per rename; idempotent.

    python3 tools/capture/rename_parts.py [RAW_SHOTS_DIR]

RENAMES (PRODUCT, adapt) maps (shot, old part) to the new part name; the shot's per-part state shots
(`<shot>-<old part>-hover`, `-focus-visible`, `-pressed`) get the part renamed too, and their names with it,
in raw/components.<theme>.json, screenshots/<theme>/ and, when given, the full-colour RAW_SHOTS_DIR.
Applied on 2026-10-25 after the capture: the command menu's box was measured as `dialog`, the name the
settings modal's box has, and three settings buttons were named for a look they do not have (two are text
links, one a danger button). product.mjs now uses the new names.
"""
import json
import pathlib
import sys

PKG = pathlib.Path(__file__).resolve().parent.parent.parent
RENAMES = {  # PRODUCT (adapt)
    ("command-menu", "dialog"): "command-menu",
    ("command-menu-typed", "dialog"): "command-menu",
    ("command-menu-empty", "dialog"): "command-menu",
    ("settings-profile-detail", "button-outline"): "text-link-button",              # Edit in Notion ↗: a text link
    ("settings-conferencing-detail", "button-secondary-sm"): "text-link-button-sm",  # Configure ↗: a text link
    ("settings-conferencing-detail", "button-ghost"): "button-danger-sm",            # Disconnect: red text, hairline edge
}

STATES = ("hover", "focus-visible", "pressed")


def main(raw_shots=None):
    for theme in ("dark", "light"):
        f = PKG / "raw" / f"components.{theme}.json"
        caps = json.loads(f.read_text())
        out = {}
        for shot, d in caps.items():
            new_shot = shot
            for (s, old), new in RENAMES.items():
                # The shot itself, or one of its per-part state shots, `{shot}-{part}-{state}` (states() in product.mjs),
                # whose name carries the part and is renamed with it.
                kind = next((k for k in STATES if shot == f"{s}-{old}-{k}"), None)
                if (s == shot or kind) and old in d["parts"]:
                    d["parts"] = {(new if k == old else k): v for k, v in d["parts"].items()}
                    if kind:
                        new_shot = f"{s}-{new}-{kind}"
            if new_shot != shot:
                d["file"] = d["file"].replace(shot, new_shot)
                for folder in [PKG / "screenshots" / theme] + ([pathlib.Path(raw_shots).expanduser() / theme] if raw_shots else []):
                    src = folder / f"{shot}.png"
                    if src.exists():
                        src.rename(folder / f"{new_shot}.png")
            out[new_shot] = d
        f.write_text(json.dumps(out, indent=1) + "\n")
        if raw_shots:
            (pathlib.Path(raw_shots).expanduser() / theme / "captures.json").write_text(json.dumps(out, indent=1) + "\n")
    print("renamed")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
