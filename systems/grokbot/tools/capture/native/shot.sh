#!/bin/sh
# shot.sh <theme> <name>: capture the iPhone Mirroring window alone and convert it to sRGB.
# Writes ~/.design-systems/grokbot/raw-shots/<theme>/<name>.png and <name>.raw.png (the Display P3
# original). winid.swift is the helper beside this script.
HERE=$(cd "$(dirname "$0")" && pwd)
dir=~/.design-systems/grokbot/raw-shots/$1; mkdir -p "$dir"
id=$(swift "$HERE/winid.swift" "iPhone Mirroring")
screencapture -o -x -l "$id" "$dir/$2.raw.png" &&
sips --matchTo "/System/Library/ColorSync/Profiles/sRGB Profile.icc" "$dir/$2.raw.png" --out "$dir/$2.png" >/dev/null && echo "$dir/$2.png"
