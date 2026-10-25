#!/usr/bin/env python3
"""Rename captured parts after the fact, in the readings and the screenshot names, so a review
correction does not need a new capture. Run once per rename; idempotent.

    python3 tools/capture/rename_parts.py [RAW_SHOTS_DIR]

RENAMES (PRODUCT, adapt) maps (shot, old part) to the new part name; a shot whose name contains
the old part (a per-part state shot such as settings-button-secondary-hover) is renamed with it,
in raw/components.<theme>.json, screenshots/<theme>/ and, when given, the full-colour RAW_SHOTS_DIR.
Applied on 2026-10-25 after the capture (the disabled Create project button) and after review in PR 111 (parts named
for the wrong look, two readings of the wrong element, which DROPS removes).
"""
import json
import pathlib
import sys

PKG = pathlib.Path(__file__).resolve().parent.parent.parent
RENAMES = {  # PRODUCT (adapt)
    # The Create project button is disabled until the dialog has a name; the default shot shows that.
    ("create-project-dialog", "button-primary"): "button-primary-disabled",
    # After review (PR 111): parts named for the wrong look, so one name mixed controls across states.
    ("pages", "button-outline"): "button-primary-sm",                       # Create with AI: ink, 32px
    ("pages-button-outline-sm-hover", "button-outline-sm"): "button-primary-sm",
    ("pages-button-outline-sm-focus-visible", "button-outline-sm"): "button-primary-sm",
    ("pages-button-outline-sm-pressed", "button-outline-sm"): "button-primary-sm",
    ("settings-terminal", "button-outline-sm"): "button-primary-sm",        # Add script: ink
    ("settings-account", "button-secondary"): "button-primary-sm",          # Save profile: ink
    ("settings-account", "button-ghost-sm"): "button-secondary-lg",         # Sign out: outlined, 36px
    ("automations-pro", "button-ghost"): "button-secondary-lg",             # Cancel: outlined, 36px
    ("settings-keyboard", "button-ghost-sm"): "button-secondary",           # Reset: outlined, 32px
    ("settings-integrations", "button-ghost-sm"): "button-secondary",       # Connect: outlined, 32px
    ("delete-confirmation", "button-ghost"): "button-ghost-sm",             # Cancel: ghost, 28px
    ("settings-appearance", "select-trigger"): "select-trigger-sm",         # the theme select, 32px
    ("settings-teams", "button-primary-sm"): "button-primary",              # Create team: 36px
    ("workspace-default", "terminal"): "terminal-offscreen",                # an off-screen .xterm (-9999px)
}
# Readings of the wrong element, removed (PR 111): the selector matched something else.
DROPS = {
    ("workspaces", "sidebar-row-selected"),   # matched the New Workspace button, not the Workspaces row
    ("workspaces", "workspace-card"),         # matched the board's content area, not a card
}


def main(raw_shots=None):
    for theme in ("dark", "light"):
        f = PKG / "raw" / f"components.{theme}.json"
        caps = json.loads(f.read_text())
        out = {}
        for shot, d in caps.items():
            for s_, part in DROPS:
                if s_ == shot:
                    d["parts"].pop(part, None)
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
