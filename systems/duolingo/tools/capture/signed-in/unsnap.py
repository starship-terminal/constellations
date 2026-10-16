#!/usr/bin/env python3
"""Write one snapshot from snapshot.js to <outdir>/<label>.html and <label>.json.

Usage: python3 unsnap.py <file holding the SNAPSTART...SNAPEND string> <outdir>
The input may be the raw string or a tool-result JSON array of {text} parts wrapping it.

Duolingo (adapt): the page is snapshotted with only the DOM rules of the redaction file (scrub,
badges), and the text replacements run here, so the 200 patterns never have to be pasted into
the page. Then it refuses the snapshot, writing nothing, if any pattern in the redaction file still matches or
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
def pyrep(rep):
    return re.sub(r"\$(\d)", r"\\\1", rep)
for pattern, flags, rep in redact["replace"]:
    rx = re.compile(pattern, re.I if "i" in flags else 0)
    html = rx.sub(pyrep(rep), html)
    meta["url"] = rx.sub(pyrep(rep), meta.get("url", ""))
checked = html + json.dumps(meta)

leaks = []
for pattern, flags, _ in redact["replace"]:
    if re.search(pattern, checked, re.I if "i" in flags else 0):
        leaks.append(f"redaction pattern {len(leaks) + 1}")
leaks += sorted(set(re.findall(r"[?&](?:amp;)?(X-Amz-Signature|X-Amz-Security-Token|Key-Pair-Id|Signature)=", checked)))
if leaks:
    sys.exit(f"LEAK {leaks}")

os.makedirs(outdir, exist_ok=True)
open(f"{outdir}/{meta['label']}.html", "w").write(html)
json.dump(meta, open(f"{outdir}/{meta['label']}.json", "w"), indent=1)
print(meta["label"], len(html), meta)
