#!/usr/bin/env python3
"""Apply icon-names.tsv to icons/ and icons/INDEX.tsv without the page copies.

    python3 tools/capture/name_icons.py

icons.mjs names each glyph from icon-names.tsv when it lifts the icons out of the page copies. The
2026-10-04 copies no longer exist, so on the 2026-10-17 refresh the glyphs it had left as
icon-<hash8> were named by role (from the words beside them in INDEX.tsv's `role` column and from
looking at each one) in icon-names.tsv, and this script renames those files and their INDEX rows to
match. A future icons.mjs run reads the same file and gives the same names. Idempotent; refuses to
overwrite an existing file. Brand marks of other companies are named brand-*; they are those
companies' property, kept only because Manus shows them.
"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ICONS = HERE.parents[1] / "icons"
names = {}
for line in (HERE / "icon-names.tsv").read_text().splitlines()[1:]:
    if "\t" in line:
        h, n = line.split("\t")[:2]
        names[h] = n
rows = (ICONS / "INDEX.tsv").read_text().rstrip("\n").split("\n")
# The ninth column holds the words either side of the glyph on the page, not a role; it was headed
# `role` until 2026-10-17.
out, renamed = [rows[0].replace("\tcount\trole\tnote", "\tcount\tcontext\tnote")], 0
for r in rows[1:]:
    c = r.split("\t")
    stem = c[0][:-4]
    if stem.startswith("icon-") and c[2] in names:
        new = names[c[2]]
        src, dst = ICONS / c[0], ICONS / f"{new}.svg"
        if dst.exists():
            sys.exit(f"{dst.name} exists; pick another name for {c[2]}")
        src.rename(dst)
        c[0], c[1] = f"{new}.svg", new
        renamed += 1
    if len(c) > 9 and c[9] == "unnamed fallback" and c[2] in names:
        c[9] = "named by role on 2026-10-17 (icon-names.tsv)"
    out.append("\t".join(c))
(ICONS / "INDEX.tsv").write_text("\n".join(out) + "\n")
left = sum(1 for r in out[1:] if r.startswith("icon-"))
print(f"renamed {renamed}; {left} still named by hash")
