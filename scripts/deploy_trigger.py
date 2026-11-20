#!/usr/bin/env python3
"""Manual-redeploy endpoint for the design-systems docs site.

The site is static files, so the footer's Redeploy button POSTs here and
this queues the deploy through the user manager (`systemd-run --user`),
unit `designs-manual-redeploy`. Runs on kai-home-server as a plain user
service; no root.

    POST /api/redeploy   -> git pull --ff-only && deploy.sh --force
    GET  /api/redeploy   -> {"sha", "at"} of the last deploy (the footer
                            bar's "Last redeploy" label reads this)

deploy.sh pulls inside its own .deploy.lock and builds whatever HEAD it
finds; the explicit pull here is only so a diverged or offline clone fails
loudly instead of deploying a stale HEAD.

A click while a run is active gets 409: systemd-run refuses the duplicate
unit name, and deploy.sh's .deploy.lock is the second line of defence.
POSTs are also serialised here, and one within DEPLOY_TRIGGER_COOLDOWN
seconds of the last queued run gets 429, so a burst of clicks coalesces
into one deploy.

Who may POST:

- The socket binds DEPLOY_TRIGGER_HOST (default 127.0.0.1), never every
  interface. The nginx container reaches the host over its docker gateway
  (docker-compose override: extra_hosts host-gateway), so on
  kai-home-server set it to that gateway's address (usually 172.17.0.1,
  the docker0 bridge), which LAN hosts cannot reach.
- Every POST must carry DEPLOY_TRIGGER_TOKEN in the X-Deploy-Token header.
  nginx adds it (proxy_set_header in the /api/redeploy location), so the
  token never reaches a browser. With the variable unset, every POST is
  refused with 503 (fail closed); GET keeps working.
- A browser POST must be same-origin: one whose Sec-Fetch-Site says
  cross-site or same-site is refused, and the footer button sends an
  X-Designs-Redeploy header that a cross-site form or simple fetch cannot
  send without a CORS preflight, which this server never grants.

The trust boundary is therefore network reach, not the token. Because nginx
adds the token to every request it proxies, the token only keeps out a
client that reaches the trigger's port directly; any non-browser client that
can reach the site through nginx (it sends no Sec-Fetch-Site and can set
X-Designs-Redeploy itself) can queue a redeploy. That is accepted because the
site is meant to be reachable only from the owner's private network, and the
worst it can do is pull and rebuild the current branch once per
DEPLOY_TRIGGER_COOLDOWN. A site reachable from anywhere wider needs an auth
layer in nginx in front of /api/redeploy. Refusals and failures answer with
fixed text; the systemd-run output goes to this service's log, never to the
client.

Environment overrides: DESIGNS_REPO (working clone), DESIGNS_DEPLOY
(deploy.sh), DESIGNS_STATE (built-sha file), DESIGNS_TRIGGER_PORT
(default 8189), DEPLOY_TRIGGER_HOST (default 127.0.0.1),
DEPLOY_TRIGGER_TOKEN (required for POST), DEPLOY_TRIGGER_COOLDOWN
(default 30 seconds).
"""

from __future__ import annotations

import hmac
import json
import os
import subprocess
import threading
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

REPO = os.environ.get("DESIGNS_REPO", os.path.expanduser("~/dev/constellations"))
DEPLOY = os.environ.get("DESIGNS_DEPLOY",
                        os.path.expanduser("~/services/design-systems/bin/deploy.sh"))
STATE = os.environ.get("DESIGNS_STATE",
                       os.path.expanduser("~/services/design-systems/state/built-sha"))
PORT = int(os.environ.get("DESIGNS_TRIGGER_PORT", "8189"))
HOST = os.environ.get("DEPLOY_TRIGGER_HOST", "127.0.0.1")
TOKEN = os.environ.get("DEPLOY_TRIGGER_TOKEN", "")
COOLDOWN = float(os.environ.get("DEPLOY_TRIGGER_COOLDOWN", "30"))

UNIT = "designs-manual-redeploy"
# The paths travel as positional parameters ($1, $2), never spliced into the
# script text, so a space or shell metacharacter in either stays a path.
SCRIPT = 'git -C "$1" pull --ff-only --quiet && "$2" --force'

_lock = threading.Lock()
_last_queued = 0.0


def command(repo: str | None = None, deploy: str | None = None) -> list[str]:
    return ["systemd-run", "--user", "--collect", "--unit", UNIT,
            "/bin/sh", "-c", SCRIPT, "sh",
            REPO if repo is None else repo,
            DEPLOY if deploy is None else deploy]


def authorize(headers, token: str | None = None) -> tuple[int, dict] | None:
    """None when this POST may queue a deploy, else the (status, body) refusal."""
    token = TOKEN if token is None else token
    if not token:
        print("[trigger] refused POST: DEPLOY_TRIGGER_TOKEN is not set", flush=True)
        return 503, {"error": "redeploy is disabled: DEPLOY_TRIGGER_TOKEN is not set on the host"}
    sent = headers.get("X-Deploy-Token") or ""
    if not hmac.compare_digest(sent.encode(), token.encode()):
        return 403, {"error": "bad or missing deploy token"}
    site = (headers.get("Sec-Fetch-Site") or "").lower()
    if site and site not in ("same-origin", "none"):
        return 403, {"error": "cross-site redeploy refused"}
    if not headers.get("X-Designs-Redeploy"):
        return 403, {"error": "missing X-Designs-Redeploy header"}
    return None


def queue() -> tuple[int, dict]:
    global _last_queued
    with _lock:
        if _last_queued and time.monotonic() - _last_queued < COOLDOWN:
            return 429, {"error": "a redeploy was just queued; try again shortly"}
        code, body = _run()
        if code == 202:
            _last_queued = time.monotonic()
        return code, body


def _run() -> tuple[int, dict]:
    try:
        p = subprocess.run(command(), capture_output=True, text=True, timeout=30)
    except OSError as ex:
        print(f"[trigger] systemd-run unavailable: {ex}", flush=True)
        return 500, {"error": "systemd-run unavailable on the host"}
    except subprocess.TimeoutExpired:
        return 500, {"error": "systemd-run timed out"}
    if p.returncode == 0:
        return 202, {"queued": "redeploy", "unit": UNIT}
    # The output names unit files, paths and the user's session; it stays in
    # this service's log.
    detail = (p.stderr or p.stdout).strip()
    print(f"[trigger] systemd-run exited {p.returncode}: {detail}", flush=True)
    if "already" in detail.lower() or "exists" in detail.lower():
        return 409, {"error": "a redeploy is already running"}
    return 500, {"error": "systemd-run failed; see the trigger's log on the host"}


def info() -> dict:
    # built-sha is written at the end of every deploy.sh run, so its mtime
    # is the last redeploy whether the timer, the button or a hand run did it.
    try:
        sha = open(STATE).read().strip() or None
        at = datetime.fromtimestamp(os.path.getmtime(STATE), timezone.utc)
    except OSError:
        return {"ok": True, "sha": None, "at": None}
    return {"ok": True, "sha": sha, "at": at.isoformat()}


class Handler(BaseHTTPRequestHandler):
    server_version = "designs-trigger/1"

    def _json(self, code: int, obj: dict) -> None:
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/api/redeploy":
            self._json(200, info())
        else:
            self._json(404, {"error": "not found"})

    def do_POST(self) -> None:
        if self.path == "/api/redeploy":
            refusal = authorize(self.headers)
            code, body = refusal or queue()
            self._json(code, body)
        else:
            self._json(404, {"error": "unknown action"})

    def log_message(self, fmt: str, *args) -> None:
        print(f"[trigger] {self.address_string()} {fmt % args}", flush=True)


def main() -> int:
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"[trigger] POST /api/redeploy on {HOST}:{PORT}", flush=True)
    if not TOKEN:
        print("[trigger] DEPLOY_TRIGGER_TOKEN is not set: every POST will be "
              "refused until it is", flush=True)
    server.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
