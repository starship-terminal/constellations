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

The port listens on all interfaces because the nginx container reaches the
host over its docker gateway (docker-compose override: extra_hosts
host-gateway). It only ever queues the one fixed command: no arguments,
no output streaming, so tailnet exposure is harmless.

Environment overrides: DESIGNS_REPO (working clone), DESIGNS_DEPLOY
(deploy.sh), DESIGNS_STATE (built-sha file), DESIGNS_TRIGGER_PORT
(default 8189).
"""

from __future__ import annotations

import json
import os
import subprocess
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

REPO = os.environ.get("DESIGNS_REPO", os.path.expanduser("~/dev/design-systems"))
DEPLOY = os.environ.get("DESIGNS_DEPLOY",
                        os.path.expanduser("~/services/design-systems/bin/deploy.sh"))
STATE = os.environ.get("DESIGNS_STATE",
                       os.path.expanduser("~/services/design-systems/state/built-sha"))
PORT = int(os.environ.get("DESIGNS_TRIGGER_PORT", "8189"))


def queue() -> tuple[int, dict]:
    unit = "designs-manual-redeploy"
    cmd = f"git -C {REPO} pull --ff-only --quiet && {DEPLOY} --force"
    try:
        p = subprocess.run(
            ["systemd-run", "--user", "--collect", "--unit", unit,
             "/bin/sh", "-c", cmd],
            capture_output=True, text=True, timeout=30)
    except OSError as ex:
        return 500, {"error": f"systemd-run unavailable: {ex}"}
    except subprocess.TimeoutExpired:
        return 500, {"error": "systemd-run timed out"}
    if p.returncode == 0:
        return 202, {"queued": "redeploy", "unit": unit}
    detail = (p.stderr or p.stdout).strip()
    busy = "already" in detail.lower() or "exists" in detail.lower()
    return (409 if busy else 500), {"error": detail or "systemd-run failed"}


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
            code, body = queue()
            self._json(code, body)
        else:
            self._json(404, {"error": "unknown action"})

    def log_message(self, fmt: str, *args) -> None:
        print(f"[trigger] {self.address_string()} {fmt % args}", flush=True)


def main() -> int:
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"[trigger] POST /api/redeploy on :{PORT}", flush=True)
    server.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
