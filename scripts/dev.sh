#!/usr/bin/env bash
# Run the library's Next.js app in dev mode, then open the gallery and the
# scorecard in the browser. `make dev` and the `design` shell alias call this.
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: scripts/dev.sh [--port N] [--no-open]

Runs the Next.js app (web/) in dev mode on 127.0.0.1, and opens two tabs:
the gallery (every package, section by section) and the scorecard (how far
each package has got). Ctrl-C stops it.

If the app is already being served on that port, it only opens the tabs.

Options:
  --port N    port to serve on (default: $PORT, else 8800)
  --no-open   serve without opening the browser
  -h, --help  show this help
EOF
}

die() { printf 'dev.sh: %s\n' "$*" >&2; exit 1; }
warn() { printf '  ! %s\n' "$*" >&2; }

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PORT="${PORT:-8800}"
OPEN=1
while [ $# -gt 0 ]; do
  case "$1" in
    --port) [ $# -ge 2 ] || die "--port needs a number"; PORT="$2"; shift 2 ;;
    --no-open) OPEN=0; shift ;;
    -h|--help) usage; exit 0 ;;
    *) die "unknown option $1 (see --help)" ;;
  esac
done
case "$PORT" in ''|*[!0-9]*) die "port must be a number, got '$PORT'" ;; esac
cd "$ROOT"

BASE="http://127.0.0.1:$PORT"
open_tabs() {
  [ "$OPEN" = 1 ] || return 0
  command -v open >/dev/null 2>&1 || { printf 'open %s/gallery/ and %s/scorecard/\n' "$BASE" "$BASE"; return 0; }
  open "$BASE/gallery/"
  open "$BASE/scorecard/"
}
answers() { curl -fsS -o /dev/null --max-time 2 "$BASE/gallery/" 2>/dev/null; }

# Already running: just bring the pages up.
if answers; then
  printf 'design-systems is already served at %s/\n' "$BASE"
  open_tabs
  exit 0
fi
if lsof -nP -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  die "port $PORT is taken by something else; pass --port N"
fi

# What the app needs.
command -v pnpm >/dev/null 2>&1 || die "pnpm is not on PATH"
if [ ! -d web/node_modules ]; then
  printf 'first run: installing the app dependencies\n'
  pnpm --dir web install
fi
if command -v python3 >/dev/null 2>&1; then
  cover="$(python3 -c 'import json; print(json.load(open("catalog.json"))["systems"][0]["preview"]["cover"])' 2>/dev/null || true)"
  if head -c 64 "$cover" 2>/dev/null | grep -q '^version https://git-lfs'; then
    warn "screenshots are Git LFS pointers, so the gallery will show no images; run: git lfs install && git lfs pull"
  fi
fi

# Open the tabs once the server answers, while it runs in the foreground.
if [ "$OPEN" = 1 ]; then
  (
    for _ in $(seq 1 120); do
      if answers; then open_tabs; exit 0; fi
      sleep 1
    done
    warn "the app did not answer within 2 minutes; open $BASE/gallery/ yourself"
  ) &
fi

cd "$ROOT/web"
exec pnpm exec next dev -p "$PORT"
