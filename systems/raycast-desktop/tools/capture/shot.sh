#!/bin/sh
# shot.sh <theme> <name> [<window title part>]: capture one Raycast window alone (no shadow), convert Display P3 to sRGB.
# Writes ~/.design-systems/raycast-desktop/raw-shots/<theme>/<name>.png (sRGB) and <name>.raw.png (as captured).
# Refuses unless Raycast is frontmost (rwin exits non-zero). RWIN is the compiled rwin.swift.
RWIN=${RWIN:-$HOME/.design-systems/raycast-desktop/bin/rwin}
dir="$HOME/.design-systems/raycast-desktop/raw-shots/$1"; mkdir -p "$dir"
id=$("$RWIN" $3) || { echo "not captured: Raycast window not frontmost" >&2; exit 1; }
screencapture -o -x -l "$id" "$dir/$2.raw.png" &&
sips --matchTo "/System/Library/ColorSync/Profiles/sRGB Profile.icc" "$dir/$2.raw.png" --out "$dir/$2.png" >/dev/null && echo "$dir/$2.png"
