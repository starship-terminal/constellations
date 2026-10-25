#!/bin/sh
# shot.sh <theme> <name> [<window title part>]: capture Zed's main window alone (no shadow), convert Display P3 to sRGB.
# Writes ~/.design-systems/zed-desktop/raw-shots/<theme>/<name>.png and <name>.raw.png.
# Refuses when Zed is not frontmost (zwin exits non-zero).
HERE=$(cd "$(dirname "$0")" && pwd)
dir="$HOME/.design-systems/zed-desktop/raw-shots/$1"; mkdir -p "$dir"
id=$("$HERE/zwin" $3) || { echo "not captured: Zed window not frontmost" >&2; exit 1; }
screencapture -o -x -l "$id" "$dir/$2.raw.png" &&
sips --matchTo "/System/Library/ColorSync/Profiles/sRGB Profile.icc" "$dir/$2.raw.png" --out "$dir/$2.png" >/dev/null && echo "$dir/$2.png"
