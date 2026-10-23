#!/bin/sh
# shot.sh <slug> <theme> <name>: capture the iPhone Mirroring window alone and convert it to sRGB.
# Writes ~/.design-systems/<slug>/raw-shots/<theme>/<name>.png and <name>.raw.png (the Display P3
# original). winid.swift is the helper beside this script.
HERE=$(cd "$(dirname "$0")" && pwd)
dir=~/.design-systems/$1/raw-shots/$2; mkdir -p "$dir"
id=$(swift "$HERE/winid.swift" "iPhone Mirroring")
screencapture -o -x -l "$id" "$dir/$3.raw.png" &&
sips --matchTo "/System/Library/ColorSync/Profiles/sRGB Profile.icc" "$dir/$3.raw.png" --out "$dir/$3.png" >/dev/null && echo "$dir/$3.png"
