#!/usr/bin/env python3
"""Fetch Zed's published theme file and default settings at the v1.25.2 release commit.

    python3 tools/capture/fetch_upstream.py [OUT]

Writes one.json and one.LICENSE (assets/themes/one/, MIT, copyright GitHub Inc.) and default.json
(assets/settings/default.json) to OUT, ~/.design-systems/zed-desktop/upstream by default, and prints
each file's SHA-256. The package keeps a copy of one.json and its licence in raw/; default.json
stays outside the repo (only the font values in raw/settings-fonts.json come from it).
Standard library only.
"""
import hashlib
import pathlib
import sys
import urllib.request

TAG = "v1.25.2"
SHA = "d25fa01ccd788d812f236810b71af4feff6b2e38"   # refs/tags/v1.25.2 in zed-industries/zed
BASE = "https://raw.githubusercontent.com/zed-industries/zed/" + SHA + "/"
FILES = [("assets/themes/one/one.json", "one.json"), ("assets/themes/one/LICENSE", "one.LICENSE"),
         ("assets/settings/default.json", "default.json")]

if __name__ == "__main__":
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "~/.design-systems/zed-desktop/upstream").expanduser()
    out.mkdir(parents=True, exist_ok=True)
    for src, dst in FILES:
        data = urllib.request.urlopen(BASE + src).read()
        (out / dst).write_bytes(data)
        print(dst, len(data), hashlib.sha256(data).hexdigest())
