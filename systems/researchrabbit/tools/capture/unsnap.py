#!/usr/bin/env python3
"""Write each snapshot from snapshot.js to <outdir>/<label>.html and <label>.json.

Usage: python3 unsnap.py <file holding the SNAPSTART...SNAPEND string> <outdir>
The input may be the raw string, a JSON string literal of it, or a tool-result JSON array of
{text} parts wrapping either (a browser_batch result holds one part per action).

Stops at the first snapshot that leaks, writing nothing for it.
Refuses the snapshot, writing nothing, if any pattern in the redaction file still matches the copy
or its metadata (as written, entity-decoded, or as text with the tags out), or any URL still carries
a signing parameter (the list in signed-params.json beside this script). The redaction file names
the account, so it lives outside the repository: $SNAP_REDACT, normally
~/.design-systems/<slug>-redact.json, shaped like redact.example.json beside this script.
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


def load_redact():
    if not os.environ.get("SNAP_REDACT"):
        sys.exit("set SNAP_REDACT to this capture's redaction file, e.g. ~/.design-systems/<slug>-redact.json")
    return json.loads(pathlib.Path(os.environ["SNAP_REDACT"]).expanduser().read_text())


def read_text(src):
    raw = open(src).read()
    try:
        return "".join(x.get("text", "") for x in json.loads(raw))
    except Exception:
        return raw


def main(src, outdir):
    redact = load_redact()
    text = read_text(src)
    # A browser_batch result prints each snapshot as a JSON string literal after a label, so
    # decode from the quote that opens each one. One file may hold several snapshots.
    snaps = []
    for m in re.finditer(r'"SNAPSTART', text):
        snaps.append(json.JSONDecoder().raw_decode(text[m.start():])[0])
    if not snaps:
        snaps = [text]

    os.makedirs(outdir, exist_ok=True)
    for snap in snaps:
        m = re.search(r"SNAPSTART(.*?)SNAPMETA(.*)SNAPEND", snap, re.S)
        meta, page = json.loads(m.group(1)), m.group(2)
        # The page title is usually the conversation or document name, so it is not kept.
        meta.pop("title", None)
        leaks = leaks_in(page + json.dumps(meta), redact)
        if leaks:
            sys.exit(f"LEAK in {meta['label']}: {leaks}")

        open(f"{outdir}/{meta['label']}.html", "w").write(page)
        json.dump(meta, open(f"{outdir}/{meta['label']}.json", "w"), indent=1)
        print(meta["label"], len(page))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
