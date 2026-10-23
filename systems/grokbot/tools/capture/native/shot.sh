#!/bin/sh
# shot.sh <theme> <name>: capture the iPhone Mirroring window alone and convert to sRGB.
LIB="${DESIGN_SYSTEMS_HOME:-/Users/kaichen/Desktop/Personal/Internal/Projects/ai-engineering/design/design-systems}"
dir=~/.design-systems/grokbot/raw-shots/$1; mkdir -p "$dir"
id=$(swift "$LIB/tools/kit/capture/native/winid.swift" "iPhone Mirroring")
screencapture -o -x -l "$id" "$dir/$2.raw.png" &&
sips --matchTo "/System/Library/ColorSync/Profiles/sRGB Profile.icc" "$dir/$2.raw.png" --out "$dir/$2.png" >/dev/null && echo "$dir/$2.png"
