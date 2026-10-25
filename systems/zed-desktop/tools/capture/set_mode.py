"""set_mode.py dark|light: change only theme.mode in ~/.config/zed/settings.json, by text replacement.
Prints nothing from the file. Verifies that the parsed document differs only in theme.mode. Zed allows
comments and trailing commas in its settings, so the check parses the same way read_settings.py does;
the edit itself is a text replacement inside the "theme" object, so the file's comments survive."""
import json, pathlib, re, sys


def strip_jsonc(text):
    text = re.sub(r"(?m)^\s*//.*$", "", text)
    return re.sub(r",(\s*[}\]])", r"\1", text)


mode = sys.argv[1]
assert mode in ("dark", "light", "system")
p = pathlib.Path.home() / ".config/zed/settings.json"
t = p.read_text()
before = json.loads(strip_jsonc(t))
m = re.search(r'"theme"\s*:\s*\{[^{}]*\}', t)
assert m, "no theme object"
seg = m.group(0)
new_seg, n = re.subn(r'("mode"\s*:\s*)"(system|dark|light)"', lambda g: g.group(1) + '"' + mode + '"', seg)
assert n == 1, n
t2 = t[:m.start()] + new_seg + t[m.end():]
after = json.loads(strip_jsonc(t2))
b2 = dict(before); a2 = dict(after)
assert a2["theme"]["mode"] == mode
b2["theme"] = dict(b2["theme"]); b2["theme"]["mode"] = mode
assert a2 == b2, "something else changed"
p.write_text(t2)
print("theme.mode =", mode)
