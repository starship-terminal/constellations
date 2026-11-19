"""Tests for tools/refero/coverage.py's root-domain matching. Pure functions;
nothing is read or written. Run with `make test`."""
import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS / "refero"))
import coverage  # noqa: E402


class RootDomainTest(unittest.TestCase):
    def test_two_labels_by_default_three_under_a_ccsld(self):
        cases = {"www.linear.app": "linear.app", "app.linear.app": "linear.app",
                 "www.forhims.co.uk": "forhims.co.uk", "shop.example.com.tw": "example.com.tw",
                 "www.example.co.id": "example.co.id", "a.b.example.co.il": "example.co.il",
                 "example.com.my": "example.com.my", "localhost": "localhost", "": ""}
        for host, root in cases.items():
            self.assertEqual(coverage.root_domain(host), root, host)

    def test_a_host_on_its_own_tld_is_its_own_root(self):
        # Not folded under google.com, whatever an older docstring said.
        self.assertEqual(coverage.root_domain("gemini.google"), "gemini.google")

    def test_host_of_accepts_a_bare_domain(self):
        self.assertEqual(coverage.host_of("acme.example/path"), "acme.example")
        self.assertEqual(coverage.host_of("https://www.acme.example/"), "www.acme.example")
        self.assertEqual(coverage.host_of(None), "")


if __name__ == "__main__":
    unittest.main()
