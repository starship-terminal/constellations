#!/usr/bin/env python3
"""Write one snapshot from snapshot.js to <outdir>/<label>.html and <label>.json.

Usage: python3 unsnap.py <file holding the SNAPSTART...SNAPEND string> <outdir>
The input may be the raw string or a tool-result JSON array of {text} parts wrapping it.

Refuses the snapshot, writing nothing, if any pattern in the redaction file still matches or
any URL still carries a signing parameter. The redaction file names the learner, so it lives
outside the repository: $SNAP_REDACT, normally ~/.design-systems/<slug>-redact.json, shaped like
redact.example.json beside this script.
"""
import json, os, pathlib, re, sys

src, outdir = sys.argv[1], sys.argv[2]
if not os.environ.get("SNAP_REDACT"):
    sys.exit("set SNAP_REDACT to this capture's redaction file, e.g. ~/.design-systems/<slug>-redact.json")
redact_path = pathlib.Path(os.environ["SNAP_REDACT"]).expanduser()
redact = json.loads(redact_path.read_text())

raw = open(src).read()
try:
    text = "".join(x.get("text", "") for x in json.loads(raw))
except Exception:
    text = raw
if text.startswith('"'):
    text = json.JSONDecoder().raw_decode(text)[0]
m = re.search(r"SNAPSTART(.*?)SNAPMETA(.*)SNAPEND", text, re.S)
meta, html = json.loads(m.group(1)), m.group(2)
# The page title is usually the conversation or document name, so it is not kept.
meta.pop("title", None)
# NotebookLM (adapt): the page is called with an empty `replace` list, so the account's literals
# never pass through the browser tool; they are applied here, from the redaction file, to the
# copy and its URL before the check below.
for pattern, flags, rep in redact["replace"]:
    rx = re.compile(pattern, re.I if "i" in flags else 0)
    py_rep = re.sub(r"\$(\d)", r"\\\1", rep)
    html = rx.sub(py_rep, html)
    meta["url"] = rx.sub(py_rep, meta.get("url", ""))
checked = html + json.dumps(meta)

leaks = []
for pattern, flags, _ in redact["replace"]:
    if re.search(pattern, checked, re.I if "i" in flags else 0):
        leaks.append(f"redaction pattern {len(leaks) + 1}")
leaks += sorted(set(re.findall(r"[?&](?:amp;)?(X-Amz-Signature|X-Amz-Security-Token|Key-Pair-Id|Signature)=", checked)))
if leaks:
    sys.exit(f"LEAK {leaks}")

# NotebookLM (adapt): the copy has no charset of its own once scripts and metas are cut, and a
# file:// page without one is read as Windows-1252, so emoji and dots came out garbled.
html = re.sub(r"<head([^>]*)>", r'<head\1><meta charset="utf-8">', html, count=1)
os.makedirs(outdir, exist_ok=True)
open(f"{outdir}/{meta['label']}.html", "w").write(html)
json.dump(meta, open(f"{outdir}/{meta['label']}.json", "w"), indent=1)
print(meta["label"], len(html), meta)
