#!/bin/bash
# Render every page copy listed in shots.tsv into $SNAPS/renders/: a -dark- copy in both themes, any other once.
#   PLAYWRIGHT=/path/to/playwright/index.mjs SNAPS=<dir of page copies> tools/capture/signed-in/render-all.sh [label ...]
# then: python3 tools/capture/quantize.py $SNAPS/renders
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
: "${SNAPS:?set SNAPS to the directory of page copies}"
OUT="$SNAPS/renders"; mkdir -p "$OUT"
grep -v '^#' "$HERE/shots.tsv" | while IFS=$'\t' read -r label flags; do
  [ -z "$label" ] && continue
  if [ $# -gt 0 ] && ! printf '%s\n' "$@" | grep -qx "$label"; then continue; fi
  node "$HERE/render.mjs" "$SNAPS" "$label" $flags || { echo "render failed: $label" >&2; exit 1; }
  # A copy taken in dark renders in light as well (the body class swap in lib.mjs).
  if [[ "$label" =~ -dark(-|$) ]]; then node "$HERE/render.mjs" "$SNAPS" "$label" $flags light || { echo "render failed: $label light" >&2; exit 1; }; fi
done
mv "$SNAPS"/*.png "$OUT"/ 2>/dev/null || true
echo "renders in $OUT"
