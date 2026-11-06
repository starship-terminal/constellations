#!/bin/sh
# shot.sh <slug> <theme> <name>: capture the iPhone Mirroring window alone and convert it to sRGB.
# Writes ~/.design-systems/<slug>/raw-shots/<theme>/<name>.png and <name>.raw.png (the Display P3
# original). winid.swift is the helper beside this script.
HERE=$(cd "$(dirname "$0")" && pwd)
dir=~/.design-systems/$1/raw-shots/$2; mkdir -p "$dir"
id=$(swift "$HERE/winid.swift" "iPhone Mirroring")
# An empty id would make screencapture grab the whole screen, so stop before it does.
case $id in
  ''|*[!0-9]*) echo "shot.sh: no iPhone Mirroring window found (got '$id'); open it and retry" >&2; exit 1 ;;
esac
screencapture -o -x -l "$id" "$dir/$3.raw.png" &&
sips --matchTo "/System/Library/ColorSync/Profiles/sRGB Profile.icc" "$dir/$3.raw.png" --out "$dir/$3.png" >/dev/null && echo "$dir/$3.png"
