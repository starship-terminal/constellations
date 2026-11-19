#!/usr/bin/env python3
"""Redact private regions in a package's PNGs, and check that none are left.

Signed-in captures show the owner's own content: task and notebook titles, file names, chat text, an
email. This tool paints those regions out of the finished images when no page copy survives to
recapture from. A rules file lists rectangles per screenshot family; an OCR pass over every output
finds anything the rectangles missed, using the same detection patterns as `tools/catalog.py scan`.

    python3 tools/redact_images.py apply systems/manus --rules tools/redact-rules/manus.json \
        --patterns ~/.design-systems/cleanup-redact.json
    python3 tools/redact_images.py check systems/manus --patterns ~/.design-systems/cleanup-redact.json
    python3 tools/redact_images.py lines systems/manus/screenshots/home-dark.png   # author a rules file

`check` never lets a rules file switch a detector off (its ocr.emails or ocr.net), and an email_allow
entry must match a whole part of an address (see email_allowed). `check` reads every image file under the package that git does not ignore (any folder, every frame;
a file of an image type it cannot read fails the check), and the package's own rules file, tools/redact-rules/<slug>.json, when one exists (its ocr
block: email_allow, wrap_ignore) and prints which file it loaded; `--rules` names another one instead.
`apply` never guesses: it edits files, so its `--rules` stays required.

`apply` edits files in place (they are Git LFS objects, so git has the originals until you commit).
Run it on a clean checkout of the package; to redo it after changing a rule, `git checkout` the
package's images first, because a painted-over image no longer holds the pixels a rule was written
against. Needs Pillow and numpy, and `tesseract` on PATH. Only Pillow, numpy and the
patterns file are read; no private value is ever written by this tool, and none belongs in a rules file:
`check` fails when a rules file's own text (its notes, family names, keep lists) holds an email address
its email_allow does not pass or a phone-number-shaped string. Say what a family hides, not the value.

Rules file (JSON, committed, coordinates and generic UI words only):

    {
      "families": [
        {"name": "sidebar task list",
         "files": ["screenshots/*-dark*.png"],          globs under the package; any match applies
         "skip":  ["screenshots/*collapsed*"],          globs removed from the match
         "size":  [[2880, 1800]],                       optional: only images of exactly this size
                                                        ([w, null] or [null, h] match one side)
         "rects": [[96, 790, 556, 870],                 x0, y0, x1, y1 in pixels; a negative number
                   [96, 990, 556, 1560, "rows"],        counts from the right or bottom edge
                   [600, 300, 900, 600, "pixelate:48"]],  optional 5th item: the fill mode
         "ocr_lines": [{"rect": [700, 190, 2200, -1],   paint out every OCR text line centred in this
                        "keep": ["^Today$"]}]}          rectangle unless it matches a keep regex
      ],
      "delete_stems": ["file-row", "doc-h1"],           crops of these components are deleted, every
                                                        state and theme (file-row-title is another one)
      "delete": ["components/crops/one-more-*.png"],    plain globs
      "ocr": {"net": true,                              paint out OCR words that match a pattern
              "emails": true, "email_allow": ["@example\\.com$"],
              "keep": ["^New task$"],                   keep regexes for every ocr_lines region
              "boost": ["screenshots/*.png"],           also read a contrast-flattened copy, which
                                                        finds text dimmed behind a modal backdrop
              "delete_if_covered": 0.3,                 a crop with this share painted out is deleted
              "wrap_ignore": ["screenshots/one.png"]}   `check --rules` does not flag a pattern that spans two
                                                        unrelated OCR lines of these images (a logo word next
                                                        to a heading); look at each one before listing it
    }

Fill modes: "rows" (default) takes the colour at the rectangle's left and right edge on every pixel
row and blends across, so list rows, hover fills and gradients survive; "cols" does the same top to
bottom; "solid" uses the one most common colour on the rectangle's ring (use it where one side of the
rectangle touches something bright, such as a modal's edge); "pixelate:N" averages N-pixel blocks, for
photographs, where a flat fill would look like a hole. N below 16 is refused: a pixelated title is
still a title.

Every output is requantized to 256 colours with the call the kit's quantize.py makes (median cut, no
dither), so untouched pixels keep their exact colour and the files stay small. A pattern that spans
two OCR lines is reported, not painted; add a rectangle for it.
"""
import argparse
import csv
import fnmatch
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import warnings
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter, ImageSequence

sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalog import IMAGE_EXT, read_json_object, read_redaction, redaction_patterns, tool_env  # noqa: E402

Image.MAX_IMAGE_PIXELS = None
warnings.simplefilter("ignore", Image.DecompressionBombWarning)

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
EDGE_GAP, EDGE_W = 2, 4          # sample the rectangle's neighbours this far out, this wide
PAD = 6                          # OCR boxes grow by this many pixels before filling
BOOST_CONF = 50                  # flattened copies read noise as text; trust only confident words
TILE, OVERLAP = 2400, 160        # tall images are read in strips of this height


# ---------------------------------------------------------------- patterns and rules

RULES_DIR = Path(__file__).resolve().parent / "redact-rules"


def package_rules(pkg, explicit=None):
    """The rules file `check` reads: the explicit --rules path, else RULES_DIR/<slug>.json for a
    package folder systems/<slug> when that file exists, else None."""
    if explicit:
        return Path(explicit)
    own = RULES_DIR / f"{Path(pkg).resolve().name}.json"
    return own if own.is_file() else None


def load_patterns(paths):
    """Compiled regexes from catalog-style redaction files: {"replace": [[pattern, ...], ...]}, read by
    catalog.py's shared loader; always case-insensitive here, and a row that is not a valid regex
    matches literally."""
    return redaction_patterns(read_redaction(paths), ignorecase=True)


def load_email_allow(paths):
    """The `email_allow` regexes of the same files: addresses an image may show (the owner's own,
    which AGENTS.md allows). Merged with a rules file's ocr.email_allow."""
    return read_redaction(paths)["email_allow"]


# Crop files are named {component}-{state}.png, with "light" added for the light theme.
STATES = "default|hover|focus-visible|active|selected|checked|open|typed|second|disabled|pressed"


def stem_files(pkg, stems):
    """Crop files of whole components: 'file-row' matches file-row-hover.png and file-row-light-hover.png
    but not file-row-title-hover.png, which belongs to the component 'file-row-title'. Subfolders of
    components/crops (coursera's signed-in/) are searched too."""
    out = set()
    for stem in stems:
        rx = re.compile(rf"{re.escape(stem)}-(light-)?({STATES}|light)(-({STATES}))?\.png$")
        out.update(f for f in (pkg / "components/crops").rglob(f"{stem}-*.png") if rx.fullmatch(f.name))
    return out


def package_images(pkg, subdirs=("screenshots", "components/crops", "components", "boards", "thumbnails", "previews")):
    seen, out = set(), []
    for sub in subdirs:
        for f in sorted((pkg / sub).rglob("*")) if (pkg / sub).is_dir() else []:
            if f.suffix.lower() in (".png", ".jpg", ".jpeg") and f not in seen:
                seen.add(f)
                out.append(f)
    return out


# `check` reads every image a package holds, wherever it sits (icons/, raw/, the top-level icon.png),
# in each format catalog.py lists a package image under. A file of any other image type cannot be
# read for text here, so `check` fails on it rather than pass it unread.
OTHER_IMAGE_EXT = {".ico", ".bmp", ".tif", ".tiff", ".avif", ".heic", ".heif", ".jxl", ".apng", ".jp2", ".psd"}
SKIP_DIRS = {".git", "node_modules", "__pycache__"}


def _is_image(f):
    """By extension, or by content for a file whose name does not say (an extensionless dump, a
    renamed .psd): Pillow recognises the format from the header."""
    ext = f.suffix.lower()
    if ext in IMAGE_EXT or ext in OTHER_IMAGE_EXT:
        return True
    try:
        with open(f, "rb") as fh:
            head = fh.read(16)
    except OSError:
        return False
    if head.startswith((b"8BPS", b"\xff\x0a", b"\x00\x00\x00\x0cJXL ", b"\x00\x00\x00\x0cjP  ")) or (
            head[4:8] == b"ftyp" and head[8:12] in (b"avif", b"avis", b"heic", b"heix", b"mif1", b"msf1")):
        return True
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            with Image.open(f):
                return True
    except Exception:
        return False


def _git_ignored(paths):
    """The paths git ignores (a package's local fonts/, capture dumps/): never committed, so not checked.
    Outside a git checkout, or without git, nothing counts as ignored. NUL-separated both ways, so a
    non-ASCII name comes back as itself rather than quoted."""
    if not paths:
        return set()
    try:
        out = subprocess.run(["git", "-C", str(paths[0].parent), "check-ignore", "-z", "--stdin"],
                             capture_output=True, input=b"\0".join(os.fsencode(p.resolve()) for p in paths),
                             timeout=60)
    except (OSError, subprocess.SubprocessError):
        return set()
    if out.returncode not in (0, 1):
        return set()
    return {Path(os.fsdecode(p)) for p in out.stdout.split(b"\0") if p}


def check_images(pkg):
    """(images `check` reads, image files it cannot read): every image file anywhere under the package
    that git does not ignore, in any folder."""
    found = []
    for root, dirs, files in os.walk(pkg):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        found += [Path(root) / n for n in sorted(files) if _is_image(Path(root) / n)]
    ignored = _git_ignored(found)
    found = [f for f in found if f.resolve() not in ignored]
    readable = [f for f in found if f.suffix.lower() in IMAGE_EXT]
    return readable, [f for f in found if f.suffix.lower() not in IMAGE_EXT]


def frames(f):
    """Every frame of an image as RGB, one at a time: an animated GIF or WebP can hide text in a later
    frame, and holding every decoded frame of a long one would exhaust memory."""
    with Image.open(f) as im:
        for fr in ImageSequence.Iterator(im):
            yield fr.convert("RGB")


def size_matches(sizes, wh):
    if not sizes:
        return True
    return any((s[0] is None or s[0] == wh[0]) and (s[1] is None or s[1] == wh[1]) for s in sizes)


def _abs(r, wh):
    x0, y0, x1, y1 = (v + (wh[i % 2] if v < 0 else 0) for i, v in enumerate(r[:4]))
    return max(0, x0), max(0, y0), min(wh[0], x1), min(wh[1], y1)


def rules_for(rules, rel, wh):
    """What applies to one image: rectangles (x0, y0, x1, y1, mode) and OCR-line regions
    (x0, y0, x1, y1, keep-regexes), all in pixels."""
    rects, regions = [], []
    for fam in rules.get("families", []):
        if not any(fnmatch.fnmatch(rel, g) for g in fam["files"]):
            continue
        if any(fnmatch.fnmatch(rel, g) for g in fam.get("skip", [])):
            continue
        if not size_matches(fam.get("size"), wh):
            continue
        for r in fam.get("rects", []):
            x0, y0, x1, y1 = _abs(r, wh)
            if x1 > x0 and y1 > y0:
                rects.append((x0, y0, x1, y1, r[4] if len(r) > 4 else "rows"))
        for r in fam.get("ocr_lines", []):
            x0, y0, x1, y1 = _abs(r["rect"], wh)
            if x1 > x0 and y1 > y0:
                regions.append((x0, y0, x1, y1, [re.compile(k, re.I) for k in r.get("keep", [])]))
    return rects, regions


# ---------------------------------------------------------------- filling

def _strip_median(a, x0, x1, y0, y1):
    """Median colour of a[y0:y1, x0:x1] per pixel row, shape (y1 - y0, 3), or None if empty."""
    if x1 <= x0 or y1 <= y0:
        return None
    return np.median(a[y0:y1, x0:x1].astype(np.float32), axis=1)


def _smooth(c, k=7):
    """Running median down the rows, so one row of text touching the edge sample cannot streak."""
    if len(c) < k:
        return c
    pad = np.pad(c, ((k // 2, k // 2), (0, 0)), mode="edge")
    return np.median(np.stack([pad[i:i + len(c)] for i in range(k)]), axis=0)


def fill_rows(a, x0, y0, x1, y1):
    h, w = a.shape[:2]
    left = _strip_median(a, max(0, x0 - EDGE_GAP - EDGE_W), x0 - EDGE_GAP, y0, y1)
    right = _strip_median(a, x1 + EDGE_GAP, min(w, x1 + EDGE_GAP + EDGE_W), y0, y1)
    if left is None and right is None:
        return fill_solid(a, x0, y0, x1, y1)
    left = _smooth(left if left is not None else right)
    right = _smooth(right if right is not None else left)
    t = np.linspace(0, 1, x1 - x0, dtype=np.float32)[None, :, None]
    a[y0:y1, x0:x1] = np.rint(left[:, None, :] * (1 - t) + right[:, None, :] * t).astype(np.uint8)


def fill_cols(a, x0, y0, x1, y1):
    h, w = a.shape[:2]
    top = _strip_median(a.transpose(1, 0, 2), max(0, y0 - EDGE_GAP - EDGE_W), y0 - EDGE_GAP, x0, x1)
    bot = _strip_median(a.transpose(1, 0, 2), y1 + EDGE_GAP, min(h, y1 + EDGE_GAP + EDGE_W), x0, x1)
    if top is None and bot is None:
        return fill_solid(a, x0, y0, x1, y1)
    top = _smooth(top if top is not None else bot)
    bot = _smooth(bot if bot is not None else top)
    t = np.linspace(0, 1, y1 - y0, dtype=np.float32)[:, None, None]
    a[y0:y1, x0:x1] = np.rint(top[None, :, :] * (1 - t) + bot[None, :, :] * t).astype(np.uint8)


def fill_solid(a, x0, y0, x1, y1):
    h, w = a.shape[:2]
    X0, Y0, X1, Y1 = max(0, x0 - 3), max(0, y0 - 3), min(w, x1 + 3), min(h, y1 + 3)
    mask = np.ones((Y1 - Y0, X1 - X0), bool)
    mask[y0 - Y0:y1 - Y0, x0 - X0:x1 - X0] = False
    px = a[Y0:Y1, X0:X1][mask]
    if len(px) == 0:
        return
    vals, counts = np.unique(px.reshape(-1, 3), axis=0, return_counts=True)
    a[y0:y1, x0:x1] = vals[counts.argmax()]


def pixelate(a, x0, y0, x1, y1, n):
    block = a[y0:y1, x0:x1].astype(np.float32)
    h, w = block.shape[:2]
    ph, pw = -h % n, -w % n
    padded = np.pad(block, ((0, ph), (0, pw), (0, 0)), mode="edge")
    small = padded.reshape(padded.shape[0] // n, n, padded.shape[1] // n, n, 3).mean(axis=(1, 3))
    big = np.repeat(np.repeat(small, n, axis=0), n, axis=1)[:h, :w]
    a[y0:y1, x0:x1] = np.rint(big).astype(np.uint8)


def paint(a, rect):
    x0, y0, x1, y1, mode = rect
    if mode == "rows":
        fill_rows(a, x0, y0, x1, y1)
    elif mode == "cols":
        fill_cols(a, x0, y0, x1, y1)
    elif mode == "solid":
        fill_solid(a, x0, y0, x1, y1)
    elif mode.startswith("pixelate:"):
        n = int(mode.split(":")[1])
        if n < 16:
            sys.exit(f"pixelate:{n} is too fine to hide text; use 16 or more")
        pixelate(a, x0, y0, x1, y1, n)
    else:
        sys.exit(f"unknown fill mode {mode!r}")


# ---------------------------------------------------------------- OCR

def _tesseract_words(im, psm=11, min_conf=0):
    """Word boxes [(text, x, y, w, h, line_key)] of one RGB image, in its own pixels."""
    with tempfile.TemporaryDirectory() as d:
        src = Path(d) / "in.png"
        im.save(src)
        env = tool_env(OMP_THREAD_LIMIT="1")
        try:
            # errors="replace": a failed read can echo the image's own bytes on
            # stderr, which must reach the message below, not a UnicodeDecodeError.
            res = subprocess.run(["tesseract", str(src), "stdout", "--psm", str(psm), "tsv"],
                                 capture_output=True, text=True, errors="replace", env=env)
        except FileNotFoundError:
            sys.exit("tesseract is not on PATH; install it (brew install tesseract)")
    if res.returncode != 0:
        # an empty word list from a failed read would let `check` pass without reading anything
        sys.exit(f"tesseract failed (exit {res.returncode}): {res.stderr.strip()[:300]}")
    words = []
    for row in csv.DictReader(io.StringIO(res.stdout), delimiter="\t", quoting=csv.QUOTE_NONE):
        if row.get("level") != "5" or not (row.get("text") or "").strip():
            continue
        if float(row.get("conf") or -1) < min_conf:
            continue
        key = (row["block_num"], row["par_num"], row["line_num"])
        words.append((row["text"], int(row["left"]), int(row["top"]), int(row["width"]), int(row["height"]), key))
    return words


def flatten(im):
    """Local contrast stretch, so text dimmed by a modal backdrop reads like normal text."""
    g = np.array(im.convert("L"), dtype=np.float32)
    bg = np.array(Image.fromarray(g.astype(np.uint8)).filter(ImageFilter.GaussianBlur(20)), dtype=np.float32)
    return Image.fromarray(np.clip(128 + (g - bg) * 4, 0, 255).astype(np.uint8)).convert("RGB")


def ocr_scale(width):
    """How much a strip is enlarged before OCR, from the image's width alone: text size follows the
    width, and tall images are read in TILE-high strips anyway, so a 390-wide mobile capture
    thousands of pixels tall still gets the enlargement its small text needs."""
    return 3 if width < 500 else 2 if width < 1000 else 1


def ocr_words(im, boost=False):
    """Word boxes for a whole image: small ones enlarged, tall ones read in strips. `boost` reads a
    contrast-flattened copy, which finds dimmed text that plain OCR skips."""
    if boost:
        im = flatten(im)
    w, h = im.size
    scale = ocr_scale(w)
    words = []
    y = 0
    while True:
        strip = im.crop((0, y, w, min(h, y + TILE)))
        if scale != 1:
            strip = strip.resize((strip.width * scale, strip.height * scale), Image.LANCZOS)
        for t, x0, y0, bw, bh, key in _tesseract_words(strip, min_conf=BOOST_CONF if boost else 0):
            words.append((t, x0 // scale, y + y0 // scale, max(1, bw // scale), max(1, bh // scale), (boost, y) + key))
        if y + TILE >= h:
            break
        y += TILE - OVERLAP
    return words


def group_lines(words):
    """[(text, (x0, y0, x1, y1))] one entry per OCR text line."""
    lines = {}
    for wd in words:
        lines.setdefault(wd[5], []).append(wd)
    out = []
    for ws in lines.values():
        ws.sort(key=lambda r: r[1])
        out.append((" ".join(w[0] for w in ws),
                    (min(w[1] for w in ws), min(w[2] for w in ws),
                     max(w[1] + w[3] for w in ws), max(w[2] + w[4] for w in ws))))
    return out


def region_boxes(words, regions, global_keep):
    """Boxes of every OCR line whose centre is in a region and that matches none of its keep regexes."""
    boxes = []
    for text, (x0, y0, x1, y1) in group_lines(words):
        if sum(c.isalnum() for c in text) < 3:
            continue                      # an icon or a glyph, not a name
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        for rx0, ry0, rx1, ry1, keep in regions:
            if rx0 <= cx < rx1 and ry0 <= cy < ry1 and not any(k.search(text.strip()) for k in keep + global_keep):
                boxes.append((x0, y0, x1, y1))
                break
    return boxes


def email_allowed(addr, allow):
    """Whether an allow regex passes an address. An entry has to match a whole part of it, never a
    piece: the address, its local part (with or without the @), its @domain, or a whole-label
    suffix of the domain (`\\.example$`). So `@example\\.com?\\b` passes x@example.co and
    x@example.com but not x@example.co.evil.test. An entry that starts with ^ may also match the
    start of the local part (an OCR read that cut the owner's own address short). A trailing full
    stop, the end of a sentence, is not part of the address."""
    addr = addr.rstrip(".")
    local, _, domain = addr.partition("@")
    labels = domain.split(".")
    parts = [addr, local, local + "@", "@" + domain] + ["." + ".".join(labels[i:]) for i in range(1, len(labels))]
    for a in allow:
        rx = re.compile(a, re.I)
        if any(rx.fullmatch(p) for p in parts) or (a.startswith("^") and rx.match(local)):
            return True
    return False


# A rules file is committed, so it must never hold the values it paints out: a note names the kind of
# value and where it sits, never the value. These find what slipped in anyway.
PHONE = re.compile(r"(?<![\w.])\+?\(?\d[\d ().-]{6,}\d(?!\w)")
RESERVED_DOMAIN = re.compile(r"(^|\.)(example(\.(com|org|net))?|test|invalid|localhost)$", re.I)


def _rule_strings(o, path=""):
    """(JSON path, string) for every string in a rules file except its own ocr.email_allow list."""
    if isinstance(o, dict):
        for k, v in o.items():
            if path == "ocr" and k == "email_allow":
                continue
            yield from _rule_strings(v, f"{path}.{k}" if path else k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from _rule_strings(v, f"{path}[{i}]")
    elif isinstance(o, str):
        yield path, o


def rules_text_leaks(rules):
    """Where a rules file's own text holds a private-looking value: an email address that neither its
    ocr.email_allow nor a reserved test domain (example.com, .test, .example, .invalid) passes, or a
    phone-number-shaped string (9 to 15 digits with a separator). Returns "path: kind" lines, never
    the value, so the report itself leaks nothing."""
    ocr = rules.get("ocr") if isinstance(rules, dict) else None
    allow = ocr.get("email_allow", []) if isinstance(ocr, dict) else []
    out = []
    for path, s in _rule_strings(rules):
        for m in EMAIL.finditer(s):
            addr = m.group().rstrip(".")
            if not RESERVED_DOMAIN.search(addr.partition("@")[2]) and not email_allowed(addr, allow):
                out.append(f"{path}: an email address its email_allow does not pass")
        for m in PHONE.finditer(s):
            if 9 <= sum(c.isdigit() for c in m.group()) <= 15 and re.search(r"[ ().-]", m.group()):
                out.append(f"{path}: a phone-number-shaped string")
    return out


def find_private(words, patterns, emails, email_allow):
    """Boxes (x0, y0, x1, y1) of OCR words that fall inside a pattern or email match, per line."""
    lines = {}
    for wd in words:
        lines.setdefault(wd[5], []).append(wd)
    boxes = []
    for ws in lines.values():
        ws.sort(key=lambda r: r[1])
        text, spans = "", []
        for t, x, y, bw, bh, _ in ws:
            if text:
                text += " "
            spans.append((len(text), len(text) + len(t), (x, y, x + bw, y + bh)))
            text += t
        rx = list(patterns)
        hits = [m.span() for p in rx for m in p.finditer(text)]
        if emails:
            hits += [m.span() for m in EMAIL.finditer(text)
                     if not email_allowed(m.group(), email_allow)]
        for s, e in hits:
            for a, b, box in spans:
                if a < e and b > s:
                    boxes.append(box)
    return boxes


def ocr_hits(patterns, ocr_cfg, reads):
    """(boxes of matching words, whether a pattern matched only across a line break). `reads` is a list
    of word lists, one per OCR pass; the line-break test runs on each pass alone, because two passes
    over the same title interleave their words."""
    found, wrapped = [], False
    for words in reads:
        found += find_private(words, patterns, ocr_cfg.get("emails", True), ocr_cfg.get("email_allow", []))
        flat = re.sub(r"\s+", " ", " ".join(w[0] for w in sorted(words, key=lambda r: (r[2] // 20, r[1]))))
        wrapped = wrapped or any(p.search(flat) for p in patterns)
    return found, wrapped and not found


# ---------------------------------------------------------------- commands

def open_rgb(f):
    return Image.open(f).convert("RGB")


def save_256(im, f):
    """The kit's quantize.py call: sRGB, 256 colours, median cut, no dither."""
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)


def cmd_apply(args):
    pkg = Path(args.package)
    rules = read_json_object(args.rules, "rules file")
    ocr_cfg = dict(rules.get("ocr", {}))
    patterns = load_patterns(args.patterns) if args.patterns else []
    ocr_cfg["email_allow"] = ocr_cfg.get("email_allow", []) + load_email_allow(args.patterns)
    global_keep = [re.compile(k, re.I) for k in ocr_cfg.get("keep", [])]
    only = args.only
    deleted, edited, flagged = set(), 0, []

    for g in rules.get("delete", []):
        deleted.update(pkg.glob(g))
    deleted |= stem_files(pkg, rules.get("delete_stems", []))
    if only:                                    # --only limits deletions as well as edits
        deleted = {f for f in deleted if any(fnmatch.fnmatch(f.relative_to(pkg).as_posix(), g) for g in only)}

    for f in package_images(pkg):
        rel = f.relative_to(pkg).as_posix()
        if f in deleted or (only and not any(fnmatch.fnmatch(rel, g) for g in only)):
            continue
        im = open_rgb(f)
        rects, regions = rules_for(rules, rel, im.size)
        a = np.array(im)
        orig = a.copy()
        for r in rects:
            paint(a, r)
        boxes, wrapped = [], False
        if regions or (ocr_cfg.get("net", True) and (patterns or ocr_cfg.get("emails", True))):
            reads = [ocr_words(Image.fromarray(a))]
            if any(fnmatch.fnmatch(rel, g) for g in ocr_cfg.get("boost", [])):
                reads.append(ocr_words(Image.fromarray(a), boost=True))
            boxes = [b for words in reads for b in region_boxes(words, regions, global_keep)]
            if ocr_cfg.get("net", True):
                found, wrapped = ocr_hits(patterns, ocr_cfg, reads)
                boxes += found
        covered = np.zeros(a.shape[:2], bool)       # union of the painted boxes, so overlaps count once
        for x0, y0, x1, y1 in boxes:
            r = (max(0, x0 - PAD), max(0, y0 - PAD), min(im.width, x1 + PAD), min(im.height, y1 + PAD), "rows")
            covered[r[1]:r[3], r[0]:r[2]] = True
            paint(a, r)
        if boxes and "components/crops/" in rel and covered.mean() >= ocr_cfg.get("delete_if_covered", 0.3):
            deleted.add(f)
            continue
        if wrapped:
            flagged.append(rel)
        if not np.array_equal(a, orig):
            edited += 1
            print(("would edit " if args.dry_run else "edited ") + rel, flush=True)
            if not args.dry_run:
                save_256(Image.fromarray(a), f)

    # A delete glob ("../x", a symlinked folder) must never reach a file outside the package.
    # unlink removes the directory entry, so the folder holding it is what must sit in the package
    # (a symlink beside the package pointing in still counts as outside), and so must its target.
    root = pkg.resolve()
    outside = sorted(f for f in deleted if root not in f.resolve().parents
                     or not (f.parent.resolve() == root or root in f.parent.resolve().parents))
    if outside:
        sys.exit("refusing to delete outside the package: " + ", ".join(str(f) for f in outside))
    for f in sorted(deleted):
        print(("would delete " if args.dry_run else "deleted ") + f.relative_to(pkg).as_posix())
        if not args.dry_run:
            f.unlink()
    print(f"{edited} edited, {len(deleted)} deleted, {len(flagged)} with a pattern spanning lines (add rectangles):")
    for rel in flagged:
        print("  ", rel)
    return 0


def cmd_check(args):
    pkg = Path(args.package)
    if not pkg.is_dir():
        sys.exit(f"{pkg} is not a directory")
    patterns = load_patterns(args.patterns)
    if not patterns:
        sys.exit("no patterns read; a check against nothing proves nothing")
    rules_file = package_rules(pkg, args.rules)
    cfg, leaks = {}, []
    if rules_file:
        rules = read_json_object(rules_file, "rules file")
        cfg = dict(rules.get("ocr", {}))
        print(f"rules: {rules_file if args.rules else 'tools/redact-rules/' + rules_file.name}"
              + ("" if args.rules else " (loaded for this package)"), flush=True)
        # The rules file is committed too: it may describe what it hides, never hold it.
        leaks = rules_text_leaks(rules)
        for leak in leaks:
            print(f"LEAK {rules_file.name} {leak}; describe the value instead of writing it", flush=True)
        # A rules file steers `apply`; it never switches a detector off in the check that guards a commit.
        for key in ("emails", "net"):
            if cfg.get(key, True) is not True:
                print(f"warning: {rules_file.name} sets ocr.{key} to {json.dumps(cfg[key])}; check ignores that "
                      f"and reads {'every email' if key == 'emails' else 'every pattern'}", flush=True)
        cfg["emails"] = cfg["net"] = True
    cfg["email_allow"] = cfg.get("email_allow", []) + load_email_allow(args.patterns)
    bad = 0
    if args.files:
        targets = [Path(p) for p in args.files]
        unreadable = [f for f in targets if f.suffix.lower() not in IMAGE_EXT]
        targets = [f for f in targets if f not in unreadable]
    else:
        targets, unreadable = check_images(pkg)
    for f in unreadable:
        bad += 1
        print(f"UNREADABLE {f.relative_to(pkg) if pkg in f.parents else f}: {f.suffix or 'this'} image type "
              f"is not one check reads ({', '.join(sorted(IMAGE_EXT))}); convert it or remove it")
    if not targets and not unreadable:
        sys.exit(f"no images found under {pkg}")
    for f in targets:
        found, wrapped = [], False
        for im in frames(f):
            reads = [ocr_words(im)]
            if max(im.size) >= 400:
                reads.append(ocr_words(im, boost=True))
            hit, wrap = ocr_hits(patterns, cfg, reads)
            found += hit
            wrapped = wrapped or wrap
        rel = f.relative_to(pkg).as_posix() if pkg in f.parents else f.as_posix()
        if wrapped and not found and any(fnmatch.fnmatch(rel, g) for g in cfg.get("wrap_ignore", [])):
            wrapped = False               # a pattern that matches two unrelated lines, reviewed by hand
        if found or wrapped:
            bad += 1
            print(f"HIT {f.relative_to(pkg) if pkg in f.parents else f}: {len(found)} match boxes" + (" (spans lines)" if wrapped else ""))
    print(f"{len(targets)} images read, {bad} with a match" + (f" or unreadable ({len(unreadable)})" if unreadable else "")
          + (f"; {len(leaks)} private-looking values in the rules file" if leaks else ""))
    return 1 if bad or leaks else 0


def cmd_lines(args):
    """OCR text lines with boxes, to pick rectangles from."""
    for f in args.files:
        im = open_rgb(f)
        lines = {}
        for t, x, y, bw, bh, key in ocr_words(im):
            lines.setdefault(key, []).append((t, x, y, bw, bh))
        print(f"# {f}  {im.width}x{im.height}")
        for ws in sorted(lines.values(), key=lambda ws: (min(w[2] for w in ws), min(w[1] for w in ws))):
            x0, y0 = min(w[1] for w in ws), min(w[2] for w in ws)
            x1, y1 = max(w[1] + w[3] for w in ws), max(w[2] + w[4] for w in ws)
            print(f"[{x0}, {y0}, {x1}, {y1}]  {' '.join(w[0] for w in sorted(ws, key=lambda r: r[1]))}")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("apply", help="paint the rules' rectangles and OCR matches, quantize, delete title-only crops")
    p.add_argument("package")
    p.add_argument("--rules", required=True)
    p.add_argument("--patterns", action="append", help="catalog-style redaction file; read, never written; repeat for more")
    p.add_argument("--only", action="append", help="glob under the package; repeat; default every image")
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(fn=cmd_apply)
    p = sub.add_parser("check", help="OCR every image; exit 1 if any matches a pattern or shows an email")
    p.add_argument("package")
    p.add_argument("--patterns", action="append", required=True)
    p.add_argument("--rules", help="reads the ocr block (email allow list); default tools/redact-rules/<slug>.json if it exists")
    p.add_argument("files", nargs="*", help="check only these images")
    p.set_defaults(fn=cmd_check)
    p = sub.add_parser("lines", help="print OCR text lines with [x0, y0, x1, y1] boxes")
    p.add_argument("files", nargs="+")
    p.set_defaults(fn=cmd_lines)
    # argv entries may be Paths (tests build them with pathlib); argparse on
    # Python >=3.12 indexes args[0], so coerce to str first. parse_known_args
    # because a nargs="*" positional after an optional (check's trailing file
    # list) comes back in extras on affected argparse versions.
    args, extra = ap.parse_known_args(None if argv is None else [str(a) for a in argv])
    if extra:
        # Extras argparse could not place are legit trailing files only when
        # none looks like an option. A dash-prefixed extra is an unknown flag
        # (a misspelt --rules used to be checked as an image path, silently
        # skipping the whole-package scan).
        if getattr(args, "files", None) is not None and not any(a.startswith("-") for a in extra):
            args.files.extend(extra)
        else:
            ap.error("unrecognized arguments: %s" % " ".join(extra))
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
