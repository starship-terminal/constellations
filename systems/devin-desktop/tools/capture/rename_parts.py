#!/usr/bin/env python3
"""Rename captured parts after the fact, in the readings and the screenshot names, so a review
correction does not need a new capture. Run once per rename; idempotent.

    python3 tools/capture/rename_parts.py [RAW_SHOTS_DIR]

RENAMES (PRODUCT, adapt) maps (shot, old part) to the new part name; a shot whose name contains
the old part (a per-part state shot such as settings-button-secondary-hover) is renamed with it,
in raw/components.<theme>.json, screenshots/<theme>/ and, when given, the full-colour RAW_SHOTS_DIR.
Applied on 2026-10-25 after review: the search field's hover and focus-visible shots had measured its
input under the group's name (`settings-search`), so the states looked like a different box.
"""
import json
import pathlib
import sys

PKG = pathlib.Path(__file__).resolve().parent.parent.parent
RENAMES = {  # PRODUCT (adapt)
    ("settings-settings-search-hover", "settings-search"): "settings-search-input",
    ("settings-settings-search-focus-visible", "settings-search"): "settings-search-input",
}


def main(raw_shots=None):
    for theme in ("dark", "light"):
        f = PKG / "raw" / f"components.{theme}.json"
        caps = json.loads(f.read_text())
        out = {}
        for shot, d in caps.items():
            new_shot = shot
            for (s, old), new in RENAMES.items():
                if s == shot and old in d["parts"]:
                    d["parts"] = {(new if k == old else k): v for k, v in d["parts"].items()}
                    if old in shot:
                        new_shot = shot.replace(old, new)
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
