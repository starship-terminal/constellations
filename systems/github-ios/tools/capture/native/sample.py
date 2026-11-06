#!/usr/bin/env python3
"""Read colours out of a screenshot of a native app, the way the hevy package was measured.

    sample.py fill shot.png X Y W H              the region's dominant colour and its share
    sample.py text shot.png X Y W H [--dark]     the text colour: the pixel furthest from the fill
    sample.py pick shot.png X Y                  one pixel
    sample.py edges shot.png --row Y | --col X   where the colour changes along a line (sizes)
    sample.py mask shot.png X,Y,W,H [...] [-o out.png]   paint regions over with their own fill

Coordinates are image pixels. A native app has no CSS, so these are the evidence: a flat fill
is exact ("Sampled"); a text colour is the darkest anti-aliased pixel on a light fill (or the
lightest with --dark), so the true value is the same or slightly further from the fill
("Sampled (text)"); a radius or a font size read off pixels is "Derived" (docs/EVIDENCE.md).

Standard library only. Reads 8-bit PNGs: RGB, RGBA, grey and palette (the repo's quantised
screenshots).
"""
import argparse
import struct
import sys
import zlib
from collections import Counter


def read_png(path):
    """Return (width, height, rows) where rows[y][x] is an (r, g, b, a) tuple."""
    with open(path, "rb") as f:
        data = f.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path} is not a PNG")
    pos, idat, palette, trns = 8, b"", None, None
    while pos < len(data):
        length, kind = struct.unpack(">I4s", data[pos:pos + 8])
        chunk = data[pos + 8:pos + 8 + length]
        pos += 12 + length
        if kind == b"IHDR":
            width, height, depth, colour, _, _, interlace = struct.unpack(">IIBBBBB", chunk)
        elif kind == b"PLTE":
            palette = [tuple(chunk[i:i + 3]) for i in range(0, len(chunk), 3)]
        elif kind == b"tRNS":
            trns = chunk
        elif kind == b"IDAT":
            idat += chunk
        elif kind == b"IEND":
            break
    if depth != 8 or interlace:
        raise ValueError(f"{path}: only 8-bit, non-interlaced PNGs are supported")
    channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[colour]
    stride = width * channels
    raw = zlib.decompress(idat)
    rows, prev = [], bytearray(stride)
    for y in range(height):
        f = raw[y * (stride + 1)]
        line = bytearray(raw[y * (stride + 1) + 1:(y + 1) * (stride + 1)])
        for i in range(stride):
            a = line[i - channels] if i >= channels else 0
            b = prev[i]
            c = prev[i - channels] if i >= channels else 0
            if f == 1:
                line[i] = (line[i] + a) & 255
            elif f == 2:
                line[i] = (line[i] + b) & 255
            elif f == 3:
                line[i] = (line[i] + (a + b) // 2) & 255
            elif f == 4:
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                line[i] = (line[i] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        prev = line
        px = []
        for x in range(width):
            v = line[x * channels:(x + 1) * channels]
            if colour == 2:
                px.append((v[0], v[1], v[2], 255))
            elif colour == 6:
                px.append(tuple(v))
            elif colour == 0:
                px.append((v[0], v[0], v[0], 255))
            elif colour == 4:
                px.append((v[0], v[0], v[0], v[1]))
            else:
                r, g, b = palette[v[0]]
                px.append((r, g, b, trns[v[0]] if trns and v[0] < len(trns) else 255))
        rows.append(px)
    return width, height, rows


def write_png(path, rows):
    """Write rows of (r, g, b, a) as an 8-bit RGBA PNG."""
    h, w = len(rows), len(rows[0])
    raw = b"".join(b"\x00" + bytes(v for px in row for v in px) for row in rows)
    chunk = lambda k, d: struct.pack(">I", len(d)) + k + d + struct.pack(">I", zlib.crc32(k + d))
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
                + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


def mask(rows, boxes):
    """Paint each (x, y, w, h) box with the most common colour on its one-pixel border, so a
    name or title disappears into the surface it sat on. Returns the colours used."""
    height, width = len(rows), len(rows[0])
    used = []
    for x, y, w, h in boxes:
        x0, y0, x1, y1 = max(x, 0), max(y, 0), min(x + w, width), min(y + h, height)
        ring = [rows[j][i] for j in (max(y0 - 1, 0), min(y1, height - 1)) for i in range(x0, x1)]
        ring += [rows[j][i] for i in (max(x0 - 1, 0), min(x1, width - 1)) for j in range(y0, y1)]
        colour = Counter(ring).most_common(1)[0][0]
        for j in range(y0, y1):
            for i in range(x0, x1):
                rows[j][i] = colour
        used.append(colour)
    return used


def hexof(p):
    return "#{:02X}{:02X}{:02X}".format(*p[:3]) + ("" if p[3] == 255 else f"{p[3]:02X}")


def region(rows, x, y, w, h):
    return [rows[j][i] for j in range(y, y + h) for i in range(x, x + w)]


def fill(rows, x, y, w, h):
    counts = Counter(region(rows, x, y, w, h))
    colour, n = counts.most_common(1)[0]
    return colour, n / sum(counts.values())


def text(rows, x, y, w, h, dark=False):
    """The pixel furthest from the region's fill: darkest on a light fill, lightest on a dark one."""
    px = region(rows, x, y, w, h)
    lum = lambda p: 0.2126 * p[0] + 0.7152 * p[1] + 0.0722 * p[2]
    return (max if dark else min)(px, key=lum)


def edges(rows, row=None, col=None):
    line = rows[row] if row is not None else [r[col] for r in rows]
    out, start = [], 0
    for i in range(1, len(line) + 1):
        if i == len(line) or line[i] != line[start]:
            out.append((start, i - start, line[start]))
            start = i
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("fill", "text"):
        p = sub.add_parser(name)
        p.add_argument("png")
        for k in "xywh":
            p.add_argument(k, type=int)
        if name == "text":
            p.add_argument("--dark", action="store_true", help="light text on a dark fill")
    p = sub.add_parser("pick")
    p.add_argument("png")
    p.add_argument("x", type=int)
    p.add_argument("y", type=int)
    p = sub.add_parser("edges")
    p.add_argument("png")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--row", type=int)
    g.add_argument("--col", type=int)
    p.add_argument("--min", type=int, default=2, help="hide runs shorter than this many pixels")
    p = sub.add_parser("mask", help="paint regions holding private text with their own fill")
    p.add_argument("png")
    p.add_argument("boxes", nargs="+", help="X,Y,W,H in image pixels")
    p.add_argument("-o", "--out", help="write here instead of over the input")
    a = ap.parse_args()

    width, height, rows = read_png(a.png)
    if a.cmd == "fill":
        colour, share = fill(rows, a.x, a.y, a.w, a.h)
        print(f"{hexof(colour)}  {share:.0%} of {a.w}x{a.h} px{'' if share > 0.9 else '  (not flat: narrow the region)'}")
    elif a.cmd == "text":
        print(hexof(text(rows, a.x, a.y, a.w, a.h, a.dark)))
    elif a.cmd == "mask":
        boxes = [tuple(int(v) for v in b.split(",")) for b in a.boxes]
        if any(len(b) != 4 for b in boxes):
            sys.exit("each box is X,Y,W,H")
        used = mask(rows, boxes)
        write_png(a.out or a.png, rows)
        print(f"masked {len(boxes)} region(s) in {a.out or a.png} with {', '.join(hexof(c) for c in used)}")
    elif a.cmd == "pick":
        print(hexof(rows[a.y][a.x]))
    else:
        for start, length, colour in edges(rows, a.row, a.col):
            if length >= a.min:
                print(f"{start:>5} +{length:<5} {hexof(colour)}")


if __name__ == "__main__":
    sys.exit(main())
