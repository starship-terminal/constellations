#!/usr/bin/env bash
# Private Linux service releases. Never changes Tailscale publishing itself.
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
SERVICE="${DESIGN_RESEARCH_SERVICE_HOME:-$HOME/services/design-research}"
MODE="${1:-stage}"
REV="${2:-HEAD}"
case "$MODE" in stage|activate|update|install) ;; *) echo 'usage: studio-deploy.sh stage|activate [revision] | install | update' >&2; exit 2 ;; esac
[ "$(id -u)" -ne 0 ] || { echo 'Run as the service user, not root.' >&2; exit 1; }
[ "$(uname -s)" = Linux ] || { echo 'This systemd installer requires Linux.' >&2; exit 1; }
mkdir -p "$SERVICE/releases" "$SERVICE/backups"
chmod 700 "$SERVICE"
# A lock prevents a timer and a manual build switching the same service.
exec 9>"$SERVICE/.deploy.lock"
flock -n 9 || { echo 'Studio deployment already running.' >&2; exit 1; }
if [ "$MODE" = install ]; then
  [ -f "$SERVICE/runtime.env" ] || { echo "Configure $SERVICE/runtime.env first (see app/docs/DEPLOYMENT.md)." >&2; exit 1; }
  NODE="$(command -v node)"
  mkdir -p "$HOME/.config/systemd/user"
  # systemd paths with whitespace need escaping; reject instead of producing a broken unit.
  for path in "$SERVICE" "$REPO" "$NODE"; do
    [[ "$path" != *[[:space:]%\\\"]* ]] || { echo 'Service paths must not contain whitespace, %, backslashes or quotes.' >&2; exit 1; }
  done
  UNIT="$HOME/.config/systemd/user/design-research.service"
  if [ -f "$UNIT" ]; then cp "$UNIT" "$SERVICE/backups/service-$(date -u +%Y%m%dT%H%M%SZ).unit"; fi
  cat > "$UNIT" <<UNIT
[Unit]
Description=Studio private design research
After=network.target
[Service]
WorkingDirectory=$SERVICE/current/app
ExecStart=$NODE $SERVICE/current/app/node_modules/next/dist/bin/next start -H 127.0.0.1 -p 8845
EnvironmentFile=$SERVICE/runtime.env
Environment=HOME=$HOME
Environment=PATH=$(dirname "$NODE"):/usr/local/bin:/usr/bin:/bin
Restart=always
RestartSec=3
UMask=0077
[Install]
WantedBy=default.target
UNIT
  cat > "$HOME/.config/systemd/user/design-research-update.service" <<UNIT
[Unit]
Description=Update Studio from the private main branch
[Service]
Type=oneshot
ExecStart=/bin/bash $REPO/scripts/studio-deploy.sh update
Environment=HOME=$HOME
Environment=DESIGN_RESEARCH_SERVICE_HOME=$SERVICE
Environment=PATH=$(dirname "$NODE"):$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin
UNIT
  cat > "$HOME/.config/systemd/user/design-research-update.timer" <<'UNIT'
[Unit]
Description=Check for Studio updates
[Timer]
OnBootSec=5min
OnUnitActiveSec=5min
Persistent=true
[Install]
WantedBy=timers.target
UNIT
  systemctl --user daemon-reload
  systemctl --user enable design-research.service
  # Enable the timer only after the operator accepts the first cutover.
  echo 'Installed user service and disabled update timer. Stage and activate before enabling it.'
  exit 0
fi
if [ "$MODE" = update ]; then
  export GIT_TERMINAL_PROMPT=0
  git -C "$REPO" fetch --quiet origin main
  SHA="$(git -C "$REPO" rev-parse origin/main)"
  if [ "$(cat "$SERVICE/deployed-sha" 2>/dev/null || true)" = "$SHA" ]; then exit 0; fi
  # Refuse divergence or tracked edits. Leave unrelated untracked evidence alone.
  [ -z "$(git -C "$REPO" status --porcelain --untracked-files=no)" ] || { echo 'Tracked checkout edits block automatic deployment.' >&2; exit 1; }
  [ "$(git -C "$REPO" branch --show-current)" = main ] || { echo 'Automatic deployment requires main.' >&2; exit 1; }
  git -C "$REPO" merge --ff-only "$SHA"
  REV="$SHA"
fi
SHA="$(git -C "$REPO" rev-parse --verify "$REV^{commit}")"
RELEASE="$SERVICE/releases/$SHA"
if [ "$MODE" != activate ]; then
  if [ ! -f "$RELEASE/.ready" ]; then
    mkdir -p "$RELEASE"
    git -C "$REPO" archive "$SHA" app catalog.json | tar -x -C "$RELEASE"
    (cd "$RELEASE/app" && corepack pnpm install --frozen-lockfile && corepack pnpm build)
    printf '%s\n' "$SHA" > "$RELEASE/.ready"
  fi
  echo "Staged $SHA"
  [ "$MODE" = update ] || exit 0
fi
[ -f "$RELEASE/.ready" ] || { echo 'Stage this release before activation.' >&2; exit 1; }
PREVIOUS="$(readlink "$SERVICE/current" 2>/dev/null || true)"
ln -s "$RELEASE" "$SERVICE/current.next"
mv -Tf "$SERVICE/current.next" "$SERVICE/current"
if systemctl --user restart design-research.service; then
for attempt in $(seq 1 30); do
  if curl --fail --silent --max-time 3 http://127.0.0.1:8845/api/settings >/dev/null; then
    printf '%s\n' "$SHA" > "$SERVICE/deployed-sha"
    printf '%s\n' "$PREVIOUS" > "$SERVICE/previous-release"
    echo "Activated $SHA"
    exit 0
  fi
  sleep 1
done
fi
if [ -n "$PREVIOUS" ]; then
  ln -s "$PREVIOUS" "$SERVICE/current.next"
  mv -Tf "$SERVICE/current.next" "$SERVICE/current"
  systemctl --user restart design-research.service
else
  systemctl --user stop design-research.service
fi
echo 'Studio health check failed; restored the previous service release when available.' >&2
exit 1
