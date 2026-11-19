#!/bin/bash
# Render every page copy listed in shots.tsv, dark and light, into $SNAPS/renders/.
#   PLAYWRIGHT=/path/to/playwright/index.mjs SNAPS=<dir of page copies> tools/capture/signed-in/render-all.sh [label ...]
# then: python3 tools/capture/quantize.py $SNAPS/renders
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
: "${SNAPS:?set SNAPS to the directory of page copies}"
OUT="$SNAPS/renders"; mkdir -p "$OUT"
grep -v '^#' "$HERE/shots.tsv" | while IFS=$'\t' read -r label flags; do
  [ -z "$label" ] && continue
  if [ $# -gt 0 ] && ! printf '%s\n' "$@" | grep -qx "$label"; then continue; fi
  # A copy taken in dark (label contains -dark) renders both themes, the light one under the
  # -light name; any other copy renders once, as captured, so two renders never share a file.
  # Full-page shots are taken of the dark copy only, as in the Manus reference.
  node "$HERE/render.mjs" "$SNAPS" "$label" $flags & dark=$!
  light=""
  if printf '%s' "$label" | grep -Eq -- '-dark(-|$)'; then
    node "$HERE/render.mjs" "$SNAPS" "$label" $(echo $flags | sed 's/full//') light & light=$!
  fi
  ok=0
  wait "$dark" || { echo "render failed: $label" >&2; ok=1; }
  [ -z "$light" ] || wait "$light" || { echo "render failed: $label light" >&2; ok=1; }
  [ "$ok" -eq 0 ] || exit 1
done
for image in "$SNAPS"/*.png; do
  [ -f "$image" ] || continue
  mv "$image" "$OUT/"
  [ ! -f "$image.capture.json" ] || mv "$image.capture.json" "$OUT/"
done
echo "renders in $OUT"
