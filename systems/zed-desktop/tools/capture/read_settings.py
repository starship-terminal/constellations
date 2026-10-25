#!/usr/bin/env python3
"""Write raw/settings-fonts.json: the font and theme values Zed ran with during the capture.

    python3 tools/capture/read_settings.py [UPSTREAM_DIR]

Two sources. The owner's ~/.config/zed/settings.json holds other keys, including credentials, so
this script parses it and keeps only an allow-list of display keys (`theme`, `ui_font_*`,
`buffer_font_*`, `agent_ui_font_size`, `markdown_preview_font_size`, `buffer_line_height`); it never
prints the file or writes any other key. Zed's assets/settings/default.json at the v1.25.2 commit
(fetched by fetch_upstream.py) gives the defaults for the keys the owner leaves unset, with the line
each came from, and the comments that name what `.ZedSans`, `.ZedMono` and the line-height words mean.
Run it once at capture time; the committed JSON is the record. Standard library only.
"""
import json
import pathlib
import re
import sys

PKG = pathlib.Path(__file__).resolve().parent.parent.parent
ALLOW = re.compile(r"^(theme|ui_font_\w+|buffer_font_\w+|agent_ui_font_size|agent_buffer_font_size|"
                   r"markdown_preview_font_size|buffer_line_height)$")
DEFAULT_KEYS = ["ui_font_family", "ui_font_size", "ui_font_weight", "buffer_font_family", "buffer_font_size",
                "buffer_font_weight", "buffer_line_height", "agent_ui_font_size", "agent_buffer_font_size"]
COMMENTS = [r'"\.ZedMono" currently aliases to (\w+)', r'"\.ZedSans" currently aliases to "([^"]+)"',
            r"comfortable for reading \(([\d.]+)\)", r"standard line height, \(([\d.]+)\)"]


def strip_jsonc(text):
    text = re.sub(r"(?m)^\s*//.*$", "", text)
    return re.sub(r",(\s*[}\]])", r"\1", text)


if __name__ == "__main__":
    up = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "~/.design-systems/zed-desktop/upstream").expanduser()
    user = json.loads(strip_jsonc((pathlib.Path.home() / ".config/zed/settings.json").read_text()))
    owner = {k: v for k, v in user.items() if ALLOW.match(k)}
    lines = (up / "default.json").read_text().splitlines()
    defaults = {}
    for key in DEFAULT_KEYS:
        n = next(i for i, l in enumerate(lines) if re.match(rf'\s*"{key}"\s*:', l))
        defaults[key] = {"value": json.loads(strip_jsonc("{" + lines[n].strip().rstrip(",") + "}"))[key], "line": n + 1}
    notes = {}
    text = "\n".join(lines)
    for pat, name in zip(COMMENTS, ["ZedMono", "ZedSans", "comfortable", "standard"]):
        m = re.search(pat, text)
        notes[name] = {"value": m.group(1), "line": text[:m.start()].count("\n") + 1}
    doc = {
        "owner": {"file": "~/.config/zed/settings.json (the owner's; only these keys were read)", "keys": owner},
        "defaults": {"file": "assets/settings/default.json", "repo": "zed-industries/zed", "tag": "v1.25.2",
                     "commit": "d25fa01ccd788d812f236810b71af4feff6b2e38", "keys": defaults, "comments": notes},
    }
    (PKG / "raw" / "settings-fonts.json").write_text(json.dumps(doc, indent=1, sort_keys=True) + "\n")
    print("raw/settings-fonts.json:", sorted(owner), "and", len(defaults), "defaults")
