#!/usr/bin/env python3
"""Write one snapshot from snapshot.js to <outdir>/<label>.html and <label>.json.

Usage: python3 unsnap.py <file holding the SNAPSTART...SNAPEND string> <outdir>
The input may be the raw string or a tool-result JSON array of {text} parts wrapping it.

Refuses the snapshot, writing nothing, if any pattern in the redaction file still matches or
any URL still carries a signing parameter (the list in signed-params.json beside this script).
The redaction file names the learner, so it lives outside the repository: $SNAP_REDACT,
normally ~/.design-systems/<slug>-redact.json, shaped like redact.example.json beside this script.
"""
import html, html.parser, json, os, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent


def signed_url_pattern(spec):
    """A regex whose one group is the name of a credential-carrying URL parameter, built from
    signed-params.json: after ?, &, &amp;, # or their %-encodings, case-insensitive."""
    names = [re.escape(p) + r"[A-Za-z0-9-]*" for p in spec["prefixes"]] + [re.escape(p) for p in spec["params"]]
    return re.compile(r"(?:[?&#]|%3F|%26|%23)(?:amp;)?(" + "|".join(names) + r")(?:=|%3D)", re.I)


SIGNED = signed_url_pattern(json.loads((HERE / "signed-params.json").read_text()))


class _Text(html.parser.HTMLParser):
    """The text an HTML parser reads out of a page, entities decoded, so a tag whose quoted
    attribute holds a > cannot leave markup between the halves of a name."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def readings(checked):
    """The forms a redaction pattern is tried on: the serialised copy as written, with its entities
    decoded (&nbsp;, &#74;), and as page text with the tags taken out, both joined (a name split
    across <span>s) and spaced; each with non-breaking spaces read as plain spaces too."""
    parser = _Text()
    parser.feed(checked)
    parser.close()
    forms = [checked, html.unescape(checked), "".join(parser.parts), " ".join(parser.parts)]
    return forms + [f.replace("\xa0", " ") for f in forms[1:]]


def leaks_in(checked, redact):
    """What survived in the copy: redaction patterns by number, signing parameters by name."""
    forms = readings(checked)
    leaks = []
    for n, (pattern, flags, _) in enumerate(redact["replace"], 1):
        rx = re.compile(pattern, re.I if "i" in flags else 0)
        if any(rx.search(f) for f in forms):
            leaks.append(f"redaction pattern {n}")
    return leaks + sorted(set(m.lower() for f in forms[:2] for m in SIGNED.findall(f)))


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
    if not m:
        sys.exit(f"{src}: no SNAPSTART...SNAPMETA...SNAPEND snapshot in it (paste the whole string __snap returned)")
    meta, page = json.loads(m.group(1)), m.group(2)
    # The label names the two files written; anything but a plain name (a / or ..) could write elsewhere.
    if not isinstance(meta.get("label"), str) or not re.fullmatch(r"[\w.-]+", meta["label"]) or meta["label"].strip(".") == "":
        # the value is not printed: a label can hold the very text the redaction file exists to keep out
        sys.exit("the snapshot label is not a plain name (letters, digits, _ . -); rename it in the paste")
    # The page title is usually the conversation or document name, so it is not kept.
    meta.pop("title", None)
    leaks = leaks_in(page + json.dumps(meta, ensure_ascii=False), redact)   # an accented name stays as written
    if leaks:
        sys.exit(f"LEAK {leaks}")

    os.makedirs(outdir, exist_ok=True)
    open(f"{outdir}/{meta['label']}.html", "w").write(page)
    json.dump(meta, open(f"{outdir}/{meta['label']}.json", "w"), indent=1)
    print(meta["label"], len(page), meta)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
