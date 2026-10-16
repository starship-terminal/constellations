#!/usr/bin/env python3
"""Write one snapshot from snapshot.js to <outdir>/<label>.html and <label>.json.

Usage: python3 unsnap.py <file holding the SNAPSTART...SNAPEND string> <outdir>
The input may be the raw string or a tool-result JSON array of {text} parts wrapping it.

Refuses the snapshot, writing nothing, if any pattern in the redaction file still matches or
any URL still carries a signing parameter. The redaction file names the learner, so it lives
outside the repository: $SNAP_REDACT, default ~/.design-systems/chatgpt-redact.json, shaped like
redact.example.json beside this script.
"""
import json, os, pathlib, re, sys

src, outdir = sys.argv[1], sys.argv[2]
redact_path = pathlib.Path(os.environ.get("SNAP_REDACT", "~/.design-systems/chatgpt-redact.json")).expanduser()
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

leaks = []
for pattern, flags, _ in redact["replace"]:
    if re.search(pattern, html, re.I if "i" in flags else 0):
        leaks.append(f"redaction pattern {len(leaks) + 1}")
# The account photo is served from estuary/public_content; a copy that still points at it would
# load the photo again whenever it is rendered.
if re.search(r"<img[^>]*backend-api/estuary/public_content/", html):
    leaks.append("account photo URL (backend-api/estuary/public_content)")
# Chat, project, account and user ids (snapshot.js cuts them; a survivor means it was bypassed).
if re.search(r"\b(?!00000000-)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", html):
    leaks.append("a chat or account uuid")
if re.search(r"\bg-p-(?!sample)[0-9a-f]{32}|\b(?:user|account)-(?!sample)[A-Za-z0-9]{16,}|\blibfile_(?!sample)[0-9a-f]{16,}|\bfile[-_](?!sample)[A-Za-z0-9]{16,}", html):
    leaks.append("a project, file, user or account id")
leaks += sorted(set(re.findall(r"[?&](?:amp;)?(X-Amz-Signature|X-Amz-Security-Token|Key-Pair-Id|Signature|sig)=", html)))
if leaks:
    sys.exit(f"LEAK {leaks}")

os.makedirs(outdir, exist_ok=True)
open(f"{outdir}/{meta['label']}.html", "w").write(html)
json.dump(meta, open(f"{outdir}/{meta['label']}.json", "w"), indent=1)
print(meta["label"], len(html), meta)
