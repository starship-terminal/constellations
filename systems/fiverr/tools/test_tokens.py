#!/usr/bin/env python3
"""Package checks for the blocked Fiverr capture."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent


def test_builders():
    for name in ("build_tokens.py", "build_style_guide.py"):
        subprocess.check_call([sys.executable, str(HERE / name)], cwd=PKG)


def test_login_review():
    data = json.loads((PKG / "login-review.json").read_text())
    assert data["signed_in"] is False
    assert data["formSubmitted"] is False
    assert data["ssoClicked"] is False
    assert "Signed-in app was not captured." in data["gaps"]
    text = json.dumps(data)
    assert "Not captured" in text or "not captured" in text.lower() or "Unread token values are Not captured." in data["gaps"]


def test_no_private_strings():
    import re
    email = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
    ip = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")
    for path in PKG.rglob("*"):
        if not path.is_file() or path.suffix.lower() == ".png":
            continue
        text = path.read_text(errors="replace")
        if email.search(text):
            raise AssertionError(f"email-like string in {path.name}")
        if ip.search(text):
            raise AssertionError(f"ip-like string in {path.name}")


if __name__ == "__main__":
    test_builders()
    test_login_review()
    test_no_private_strings()
    print("fiverr package checks ok")
