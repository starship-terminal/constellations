#!/usr/bin/env bash
# Redeploy the docs site by hand: pull the clone, then deploy.sh --force —
# the same thing the footer Redeploy button queues through the
# designs-trigger endpoint. For running on kai-home-server.
#
#   scripts/redeploy.sh
#
# DESIGNS_DEPLOY overrides the deploy.sh path.
set -euo pipefail

cd "$(dirname "$0")/.."
DEPLOY="${DESIGNS_DEPLOY:-$HOME/services/design-systems/bin/deploy.sh}"

# Nothing else writes this tree, so there is no fetch lock to take;
# deploy.sh serialises deploys itself via ~/services/design-systems/.deploy.lock.
git pull --ff-only --quiet
"$DEPLOY" --force
