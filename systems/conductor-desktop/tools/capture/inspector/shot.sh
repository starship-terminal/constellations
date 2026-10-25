#!/bin/sh
# shot.sh <theme> <name>: capture Conductor's main window alone (no shadow) while it is frontmost and
# uncovered, keep the Display P3 original as <name>.raw.png and write an sRGB copy as <name>.png, in
# ~/.design-systems/conductor-desktop/raw-shots/<theme>/ (outside the repository).
HERE=$(cd "$(dirname "$0")" && pwd)
dir=${RAW:-$HOME/.design-systems/conductor-desktop/raw-shots}/$1; mkdir -p "$dir"
front=$(osascript -e 'tell application "System Events" to get name of first process whose frontmost is true')
if [ "$front" != conductor ]; then
  osascript -e 'tell application "Conductor" to activate' >/dev/null; sleep 0.6
  front=$(osascript -e 'tell application "System Events" to get name of first process whose frontmost is true')
  [ "$front" = conductor ] || { echo "shot.sh: $front is frontmost, not Conductor" >&2; exit 1; }
fi
id=$(swift "$HERE/winid.swift" "Conductor") || exit 1
screencapture -o -x -l "$id" "$dir/$2.raw.png" &&
sips --matchTo "/System/Library/ColorSync/Profiles/sRGB Profile.icc" "$dir/$2.raw.png" --out "$dir/$2.png" >/dev/null &&
echo "$dir/$2.png"
