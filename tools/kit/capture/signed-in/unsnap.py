#!/usr/bin/env python3
"""Write one snapshot from snapshot.js to <outdir>/<label>.html and <label>.json.

Usage: python3 unsnap.py <file holding the SNAPSTART...SNAPEND string> <outdir>
The input may be the raw string or a tool-result JSON array of {text} parts wrapping it.

Refuses the snapshot, writing nothing, if any pattern in the redaction file still matches or
any URL still carries a signing parameter (the list in signed-params.json beside this script).
The redaction file names the learner, so it lives outside the repository: $SNAP_REDACT,
normally ~/.design-systems/<slug>-redact.json, shaped like redact.example.json beside this script.
"""
import json, os, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent


def signed_url_pattern(spec):
    """A regex whose one group is the name of a credential-carrying URL parameter, built from
    signed-params.json: after ?, &, &amp;, # or their %-encodings, case-insensitive."""
    names = [re.escape(p) + r"[A-Za-z0-9-]*" for p in spec["prefixes"]] + [re.escape(p) for p in spec["params"]]
    return re.compile(r"(?:[?&#]|%3F|%26|%23)(?:amp;)?(" + "|".join(names) + r")(?:=|%3D)", re.I)


SIGNED = signed_url_pattern(json.loads((HERE / "signed-params.json").read_text()))


def leaks_in(checked, redact):
    """What survived in the copy: redaction patterns by number, signing parameters by name."""
    leaks = []
    for pattern, flags, _ in redact["replace"]:
        if re.search(pattern, checked, re.I if "i" in flags else 0):
            leaks.append(f"redaction pattern {len(leaks) + 1}")
    return leaks + sorted(set(m.lower() for m in SIGNED.findall(checked)))


def main(src, outdir):
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
    leaks = leaks_in(html + json.dumps(meta), redact)
    if leaks:
        sys.exit(f"LEAK {leaks}")

    os.makedirs(outdir, exist_ok=True)
    open(f"{outdir}/{meta['label']}.html", "w").write(html)
    json.dump(meta, open(f"{outdir}/{meta['label']}.json", "w"), indent=1)
    print(meta["label"], len(html), meta)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
