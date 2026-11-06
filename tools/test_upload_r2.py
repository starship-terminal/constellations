"""Tests for tools/refero/upload_r2.py: the SigV4 signer, the retrying PUT and
main()'s job list, dry run and exit status. No network: urlopen and upload are
patched, the media root is a temp folder and the credentials are invented.
Run with `make test`."""
import contextlib
import datetime
import hashlib
import hmac
import importlib.util
import io
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("upload_r2", HERE / "refero" / "upload_r2.py")
r2 = importlib.util.module_from_spec(_spec)
_path = list(sys.path)
_spec.loader.exec_module(r2)
sys.path[:] = _path  # it puts tools/refero/ first, whose check.py and fetch.py would shadow

NOW = datetime.datetime(2026, 1, 2, 3, 4, 5, tzinfo=datetime.timezone.utc)
CREDS = ("TESTKEYID", "test-secret")
ENV = {"R2_ACCOUNT_ID": "acct", "R2_ACCESS_KEY_ID": CREDS[0], "R2_SECRET_ACCESS_KEY": CREDS[1],
       "R2_BUCKET": "bucket", "PATH": os.environ.get("PATH", "")}


class SignerTest(unittest.TestCase):
    def test_signing_key_chain_matches_the_aws_published_example(self):
        # docs.aws.amazon.com "Examples of how to derive a signing key for Signature Version 4".
        h = r2._hmac
        key = h(h(h(h(b"AWS4wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY", "20120215"), "us-east-1"), "iam"),
                "aws4_request")
        self.assertEqual(key.hex(), "f4780e2d9f65fa895f9c67b32ce1baf0b0d8a43505a000a1a9e090d414db404d")

    def test_put_signature_over_the_canonical_request(self):
        got = r2.signed_headers("PUT", "acct.r2.cloudflarestorage.com", "/bucket/shots/a b.jpg", *CREDS, NOW)
        # The canonical request written out by hand: path segments percent-encoded once,
        # headers lower-case and sorted, the payload left unsigned.
        canonical = "\n".join([
            "PUT", "/bucket/shots/a%20b.jpg", "",
            "host:acct.r2.cloudflarestorage.com\nx-amz-content-sha256:UNSIGNED-PAYLOAD\n"
            "x-amz-date:20260102T030405Z\n",
            "host;x-amz-content-sha256;x-amz-date", "UNSIGNED-PAYLOAD"])
        scope = "20260102/auto/s3/aws4_request"
        to_sign = "\n".join(["AWS4-HMAC-SHA256", "20260102T030405Z", scope,
                             hashlib.sha256(canonical.encode()).hexdigest()])
        h = r2._hmac
        key = h(h(h(h(b"AWS4test-secret", "20260102"), "auto"), "s3"), "aws4_request")
        sig = hmac.new(key, to_sign.encode(), hashlib.sha256).hexdigest()
        self.assertEqual(got["Authorization"],
                         f"AWS4-HMAC-SHA256 Credential=TESTKEYID/{scope}, "
                         f"SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature={sig}")
        self.assertEqual((got["x-amz-date"], got["x-amz-content-sha256"]), ("20260102T030405Z", "UNSIGNED-PAYLOAD"))
        self.assertNotIn("test-secret", repr(got))


class UploadTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.file = Path(self.tmp.name) / "a b.jpg"
        self.file.write_bytes(b"jpeg bytes")
        sleep = mock.patch.object(r2.time, "sleep")
        self.sleep = sleep.start()
        self.addCleanup(sleep.stop)

    def response(self, status=200):
        r = mock.MagicMock(status=status)
        r.__enter__.return_value = r
        return r

    def test_put_carries_type_length_and_quoted_key(self):
        with mock.patch.object(r2.urllib.request, "urlopen", return_value=self.response()) as urlopen:
            r2.upload("https://acct.r2.cloudflarestorage.com", "bucket", "refero-media/shots/a b.jpg",
                      self.file, CREDS)
        req = urlopen.call_args[0][0]
        self.assertEqual((req.method, req.full_url),
                         ("PUT", "https://acct.r2.cloudflarestorage.com/bucket/refero-media/shots/a%20b.jpg"))
        self.assertEqual(req.data, b"jpeg bytes")
        self.assertEqual(req.get_header("Content-type"), "image/jpeg")
        self.assertEqual(req.get_header("Content-length"), "10")
        self.assertTrue(req.get_header("Authorization").startswith("AWS4-HMAC-SHA256 Credential=TESTKEYID/"))

    def test_retries_then_gives_up(self):
        with mock.patch.object(r2.urllib.request, "urlopen",
                               side_effect=[OSError("reset"), self.response()]) as urlopen:
            r2.upload("https://h", "b", "k", self.file, CREDS)
        self.assertEqual(urlopen.call_count, 2)
        with mock.patch.object(r2.urllib.request, "urlopen", return_value=self.response(500)):
            with self.assertRaisesRegex(ValueError, "http 500"):
                r2.upload("https://h", "b", "k", self.file, CREDS)
        self.assertEqual([c.args[0] for c in self.sleep.call_args_list], [1, 1, 2, 4])


class MainTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in ("one.jpg", "two.jpg", "skip.png", "half.jpg.partial", "x.compress.jpg"):
            (self.root / "shots").mkdir(exist_ok=True)
            (self.root / "shots" / name).write_bytes(b"x" * 10)
        (self.root / "videos").mkdir()
        (self.root / "videos" / "v.mp4").write_bytes(b"v")
        load_env = mock.patch.object(r2.refero_media, "load_env")
        load_env.start()
        self.addCleanup(load_env.stop)

    def main(self, *argv, env=ENV):
        out, err = io.StringIO(), io.StringIO()
        with mock.patch.dict(os.environ, env, clear=True), \
                mock.patch.object(sys, "argv", ["upload_r2.py", "--media-root", str(self.root), *argv]), \
                contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                r2.main()
                code = 0
            except SystemExit as e:
                code = e.code
        return code, out.getvalue(), err.getvalue()

    def test_dry_run_lists_only_finished_files_of_the_chosen_kinds(self):
        with mock.patch.object(r2, "upload") as upload:
            code, out, _ = self.main("--dry-run", "--only", "shots")
        upload.assert_not_called()
        self.assertEqual(code, 0)
        self.assertIn("2 objects -> bucket/refero-media/", out)
        self.assertIn("refero-media/shots/one.jpg", out)
        self.assertNotIn("half", out)
        self.assertNotIn("compress", out)

    def test_bad_only_kind_and_empty_root(self):
        self.assertEqual(self.main("--only", "shots,nope")[0], 2)
        code = self.main("--only", "favicons")[0]
        self.assertIn("nothing to upload", code)

    def test_missing_credentials_send_nothing(self):
        with mock.patch.object(r2, "upload") as upload:
            code, _, _ = self.main(env={"R2_BUCKET": "bucket"})
        self.assertIn("set R2_ACCOUNT_ID", code)
        upload.assert_not_called()

    def test_uploads_every_job_and_fails_the_run_when_one_fails(self):
        sent = []

        def fake(endpoint, bucket, key, path, creds):
            sent.append((endpoint, bucket, key, creds))
            if key.endswith("two.jpg"):
                raise ValueError("http 403")
        with mock.patch.object(r2, "upload", side_effect=fake):
            code, out, err = self.main("--prefix", "p", "--workers", "2")
        self.assertEqual(sorted(k for _, _, k, _ in sent), ["p/shots/one.jpg", "p/shots/two.jpg", "p/videos/v.mp4"])
        self.assertEqual({(e, b, c) for e, b, _, c in sent},
                         {("https://acct.r2.cloudflarestorage.com", "bucket", CREDS)})
        self.assertIn("uploaded 2; 1 failed", out)
        self.assertIn("FAIL shots/two.jpg: http 403", err)
        self.assertEqual(code, 1)
        with mock.patch.object(r2, "upload"):
            self.assertEqual(self.main()[0], 0)


if __name__ == "__main__":
    unittest.main()
