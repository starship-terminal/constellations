"""Tests for scripts/deploy_trigger.py. Run with `make test`."""
import importlib.util
import json
import os
import stat
import subprocess
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path
from unittest import mock

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "deploy_trigger.py"
TOKEN = "test-token-not-a-secret"


def load(env=None):
    """A fresh copy of the trigger module, read under the given environment."""
    clean = {k: v for k, v in os.environ.items() if not k.startswith("DEPLOY_TRIGGER_")}
    clean.update(env or {})
    with mock.patch.dict(os.environ, clean, clear=True):
        spec = importlib.util.spec_from_file_location("deploy_trigger_under_test", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    return module


def good_headers(**extra):
    headers = {"X-Deploy-Token": TOKEN, "Sec-Fetch-Site": "same-origin", "X-Designs-Redeploy": "1"}
    headers.update(extra)
    return headers


class Defaults(unittest.TestCase):
    def test_binds_loopback_and_has_no_token_by_default(self):
        trigger = load()
        self.assertEqual(trigger.HOST, "127.0.0.1")
        self.assertEqual(trigger.TOKEN, "")

    def test_host_and_token_come_from_the_environment(self):
        trigger = load({"DEPLOY_TRIGGER_HOST": "172.17.0.1", "DEPLOY_TRIGGER_TOKEN": TOKEN})
        self.assertEqual(trigger.HOST, "172.17.0.1")
        self.assertEqual(trigger.TOKEN, TOKEN)


class Authorize(unittest.TestCase):
    def setUp(self):
        self.trigger = load()

    def code(self, headers, token=TOKEN):
        with mock.patch("builtins.print"):
            refusal = self.trigger.authorize(headers, token)
        return refusal and refusal[0]

    def test_unset_token_fails_closed(self):
        self.assertEqual(self.code(good_headers(), token=""), 503)

    def test_missing_or_wrong_token_is_refused(self):
        headers = good_headers()
        del headers["X-Deploy-Token"]
        self.assertEqual(self.code(headers), 403)
        self.assertEqual(self.code(good_headers(**{"X-Deploy-Token": "nope"})), 403)

    def test_cross_site_browser_post_is_refused(self):
        self.assertEqual(self.code(good_headers(**{"Sec-Fetch-Site": "cross-site"})), 403)
        self.assertEqual(self.code(good_headers(**{"Sec-Fetch-Site": "same-site"})), 403)

    def test_post_without_the_button_header_is_refused(self):
        headers = good_headers()
        del headers["X-Designs-Redeploy"]
        self.assertEqual(self.code(headers), 403)

    def test_same_origin_post_with_token_passes(self):
        self.assertIsNone(self.code(good_headers()))
        headers = good_headers()
        del headers["Sec-Fetch-Site"]  # curl on the host, or an older browser
        self.assertIsNone(self.code(headers))


class Queue(unittest.TestCase):
    def setUp(self):
        self.trigger = load({"DEPLOY_TRIGGER_COOLDOWN": "60"})

    def test_a_second_post_inside_the_cooldown_coalesces(self):
        with mock.patch.object(self.trigger, "_run", return_value=(202, {})) as run:
            self.assertEqual(self.trigger.queue()[0], 202)
            self.assertEqual(self.trigger.queue()[0], 429)
        self.assertEqual(run.call_count, 1)

    def test_overlapping_posts_run_once(self):
        started = threading.Event()
        release = threading.Event()

        def slow_run():
            started.set()
            release.wait(5)
            return 202, {}

        codes = []
        with mock.patch.object(self.trigger, "_run", side_effect=slow_run) as run:
            first = threading.Thread(target=lambda: codes.append(self.trigger.queue()[0]))
            first.start()
            started.wait(5)
            second = threading.Thread(target=lambda: codes.append(self.trigger.queue()[0]))
            second.start()
            second.join(0.2)
            self.assertTrue(second.is_alive())  # held on the lock while the first runs
            release.set()
            first.join(5)
            second.join(5)
        self.assertEqual(run.call_count, 1)
        self.assertEqual(sorted(codes), [202, 429])

    def test_another_deploy_is_allowed_after_the_cooldown(self):
        clock = [1000.0]
        with mock.patch.object(self.trigger.time, "monotonic", side_effect=lambda: clock[0]), \
                mock.patch.object(self.trigger, "_run", return_value=(202, {})) as run:
            self.assertEqual(self.trigger.queue()[0], 202)
            clock[0] += 59
            self.assertEqual(self.trigger.queue()[0], 429)
            clock[0] += 2
            self.assertEqual(self.trigger.queue()[0], 202)
        self.assertEqual(run.call_count, 2)

    def test_a_failed_queue_does_not_start_the_cooldown(self):
        with mock.patch.object(self.trigger, "_run", return_value=(409, {})) as run:
            self.trigger.queue()
            self.trigger.queue()
        self.assertEqual(run.call_count, 2)


class RunErrors(unittest.TestCase):
    """systemd-run's output names unit files, paths and the user session: it
    goes to the service log, and the client gets fixed text."""

    def setUp(self):
        self.trigger = load()

    def run_with(self, **kw):
        done = subprocess.CompletedProcess([], kw.pop("returncode", 1), stdout="", stderr=kw.pop("stderr", ""))
        with mock.patch.object(self.trigger.subprocess, "run", return_value=done, **kw), \
                mock.patch("builtins.print") as log:
            code, body = self.trigger._run()
        return code, body, " ".join(str(c) for c in log.call_args_list)

    def test_busy_unit_is_409_with_fixed_text(self):
        err = "Failed to start transient service unit: Unit designs-manual-redeploy.service already exists."
        code, body, log = self.run_with(stderr=err)
        self.assertEqual((code, body), (409, {"error": "a redeploy is already running"}))
        self.assertIn("already exists", log)

    def test_other_failure_keeps_detail_in_the_log(self):
        err = "Failed to connect to bus: /run/user/1000/bus: No such file or directory"
        code, body, log = self.run_with(stderr=err)
        self.assertEqual(code, 500)
        self.assertNotIn("/run/user", json.dumps(body))
        self.assertIn("/run/user/1000/bus", log)

    def test_missing_systemd_run_is_fixed_text(self):
        with mock.patch.object(self.trigger.subprocess, "run",
                               side_effect=FileNotFoundError(2, "No such file", "/usr/bin/systemd-run")), \
                mock.patch("builtins.print"):
            code, body = self.trigger._run()
        self.assertEqual((code, body), (500, {"error": "systemd-run unavailable on the host"}))


class Command(unittest.TestCase):
    def test_paths_are_arguments_not_script_text(self):
        trigger = load()
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            marker = tmp / "pwned"
            repo = f"{tmp}/repo dir; touch {marker}"
            log = tmp / "log"
            bindir = tmp / "bin"
            bindir.mkdir()
            git = bindir / "git"
            git.write_text(f'#!/bin/sh\nprintf "git:%s\\n" "$@" >> "{log}"\n')
            deploy = tmp / "deploy $(touch pwned).sh"
            deploy.write_text(f'#!/bin/sh\nprintf "deploy:%s\\n" "$@" >> "{log}"\n')
            for f in (git, deploy):
                f.chmod(f.stat().st_mode | stat.S_IXUSR)

            argv = trigger.command(repo=repo, deploy=str(deploy))
            self.assertEqual(argv[:5], ["systemd-run", "--user", "--collect", "--unit", trigger.UNIT])
            shell = argv[5:]  # what systemd-run would exec
            self.assertNotIn(repo, shell[2])
            env = dict(os.environ, PATH=f"{bindir}:{os.environ.get('PATH', '')}")
            subprocess.run(shell, check=True, cwd=tmp, env=env)

            self.assertFalse(marker.exists())
            self.assertFalse((tmp / "pwned").exists())
            lines = log.read_text().splitlines()
            self.assertIn(f"git:{repo}", lines)
            self.assertIn("deploy:--force", lines)


class Http(unittest.TestCase):
    def setUp(self):
        self.trigger = load()
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), self.trigger.Handler)
        self.server.RequestHandlerClass.log_message = lambda *a: None
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.server.server_address[1]}/api/redeploy"

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()

    def post(self, headers):
        req = urllib.request.Request(self.url, method="POST", headers=headers, data=b"")
        try:
            with urllib.request.urlopen(req) as r:
                return r.status
        except urllib.error.HTTPError as e:
            with e:
                return e.code

    def test_post_without_token_never_runs_systemd(self):
        with mock.patch.object(self.trigger, "TOKEN", TOKEN), \
                mock.patch.object(self.trigger.subprocess, "run") as run:
            self.assertEqual(self.post({"X-Designs-Redeploy": "1"}), 403)
        run.assert_not_called()

    def test_post_with_token_queues(self):
        done = subprocess.CompletedProcess([], 0, "", "")
        with mock.patch.object(self.trigger, "TOKEN", TOKEN), \
                mock.patch.object(self.trigger.subprocess, "run", return_value=done) as run:
            self.assertEqual(self.post(good_headers()), 202)
        run.assert_called_once()

    def test_get_still_answers_without_a_token(self):
        with mock.patch.object(self.trigger, "STATE", "/nonexistent/built-sha"):
            with urllib.request.urlopen(self.url) as r:
                self.assertEqual(json.load(r), {"ok": True, "sha": None, "at": None})


if __name__ == "__main__":
    unittest.main()
