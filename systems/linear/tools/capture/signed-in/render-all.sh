#!/bin/bash
# Render every page copy listed in shots.tsv, once each in the theme it was taken in, into $SNAPS/renders/.
#   PLAYWRIGHT=/path/to/playwright/index.mjs SNAPS=<dir of page copies> tools/capture/signed-in/render-all.sh [label ...]
# then: python3 tools/capture/quantize.py $SNAPS/renders
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
: "${SNAPS:?set SNAPS to the directory of page copies}"
OUT="$SNAPS/renders"; mkdir -p "$OUT"
grep -v '^#' "$HERE/shots.tsv" | while IFS=$'\t' read -r label flags; do
  [ -z "$label" ] && continue
  if [ $# -gt 0 ] && ! printf '%s\n' "$@" | grep -qx "$label"; then continue; fi
  # Linear copies keep the theme they were taken in, so each renders once, as captured.
  node "$HERE/render.mjs" "$SNAPS" "$label" $flags || { echo "render failed: $label" >&2; exit 1; }
done
mv "$SNAPS"/*.png "$OUT"/ 2>/dev/null || true
echo "renders in $OUT"
