"""set_mode.py dark|light|system: change only theme.mode in ~/.config/zed/settings.json, by text replacement.
Prints nothing from the file. Verifies that the parsed document differs only in theme.mode. Zed allows
comments and trailing commas in its settings, so the check parses the same way read_settings.py does;
the edit itself is a text replacement inside the "theme" object, so the file's comments survive.

Every check is explicit (they hold under `python3 -O` too) and stops before the file is touched. The old
file is kept beside it as settings.json.bak, and the new one is written to a temporary file in the same
folder and moved into place, so an interrupted write never leaves a half-written settings file."""
import json
import os
import pathlib
import re
import shutil
import sys
import tempfile

MODES = ("dark", "light", "system")


def strip_jsonc(text):
    text = re.sub(r"(?m)^\s*//.*$", "", text)
    return re.sub(r",(\s*[}\]])", r"\1", text)


def edit(text, mode):
    """The settings text with theme.mode set to `mode`; SystemExit when that is not the only change."""
    if mode not in MODES:
        sys.exit(f"mode must be one of {', '.join(MODES)}, not {mode!r}")
    try:
        before = json.loads(strip_jsonc(text))
    except ValueError as e:
        sys.exit(f"settings.json does not parse: {e}")
    m = re.search(r'"theme"\s*:\s*\{[^{}]*\}', text)
    if not m:
        sys.exit("no theme object in settings.json")
    seg, n = re.subn(r'("mode"\s*:\s*)"(system|dark|light)"', lambda g: g.group(1) + '"' + mode + '"', m.group(0))
    if n != 1:
        sys.exit(f"expected one theme.mode in the theme object, found {n}")
    out = text[:m.start()] + seg + text[m.end():]
    after = json.loads(strip_jsonc(out))
    if not isinstance(before.get("theme"), dict) or after.get("theme", {}).get("mode") != mode:
        sys.exit("theme.mode did not change as expected")
    want = dict(before)
    want["theme"] = {**before["theme"], "mode": mode}
    if after != want:
        sys.exit("something else changed")
    return out


def write(path, text):
    """Keep the old file as <name>.bak beside `path`, then replace the file in one move. A symlinked settings
    file (a managed dotfile) stays a link: the file it points at is the one replaced."""
    target = path.resolve()
    shutil.copy2(target, path.with_name(path.name + ".bak"))
    fd, tmp = tempfile.mkstemp(dir=target.parent, prefix=target.name + ".")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(text)
        shutil.copymode(target, tmp)
        os.replace(tmp, target)
    except BaseException:
        pathlib.Path(tmp).unlink(missing_ok=True)
        raise


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: set_mode.py dark|light|system")
    mode = sys.argv[1]
    p = pathlib.Path.home() / ".config/zed/settings.json"
    write(p, edit(p.read_text(), mode))
    print("theme.mode =", mode)


if __name__ == "__main__":
    main()
