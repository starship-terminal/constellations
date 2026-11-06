"""Tests for capture/native/sample.py and shot.sh: packed PNGs, boxes outside the image, a missing
window. Run: python3 -m unittest discover -s tools."""
import os
import pathlib
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib

NATIVE = pathlib.Path(__file__).resolve().parent / "capture" / "native"
sys.path.insert(0, str(NATIVE))
import sample  # noqa: E402


def chunk(kind, data):
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))


def paeth(a, b, c):
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    return a if pa <= pb and pa <= pc else b if pb <= pc else c


def packed_png(path, samples, depth, colour=3, palette=None, trns=None, filters=(1,)):
    """Write rows of samples (palette indices or grey levels) as a `depth`-bit PNG; row y uses
    filters[y % len(filters)], so a multi-row image exercises the filters that read the row above."""
    width, per = len(samples[0]), 8 // depth
    raw, prev = b"", bytearray((width * depth + 7) // 8)
    for y, row in enumerate(samples):
        line = bytearray(len(prev))
        for x, v in enumerate(row):
            line[x // per] |= v << (8 - depth * (x % per + 1))
        f = filters[y % len(filters)]
        out = bytearray(len(line))
        for i, v in enumerate(line):
            a, b, c = (line[i - 1] if i else 0), prev[i], (prev[i - 1] if i else 0)
            pred = (0, a, b, (a + b) // 2, paeth(a, b, c))[f]
            out[i] = (v - pred) & 255
        raw += bytes([f]) + bytes(out)
        prev = line
    body = chunk(b"IHDR", struct.pack(">IIBBBBB", width, len(samples), depth, colour, 0, 0, 0))
    if palette:
        body += chunk(b"PLTE", b"".join(bytes(c) for c in palette))
    if trns is not None:
        body += chunk(b"tRNS", trns)
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n" + body + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b""))


def decode(**kw):
    with tempfile.TemporaryDirectory() as d:
        path = pathlib.Path(d) / "p.png"
        packed_png(path, **kw)
        return sample.read_png(path)


class ReadPngTest(unittest.TestCase):
    def test_reads_sub_byte_palette_with_every_filter(self):
        palette = [(i * 16, 255 - i * 16, i * 8) for i in range(16)]
        for depth in (1, 2, 4):
            top = (1 << depth) - 1
            samples = [[(x * 3 + y * 5) & top for x in range(7)] for y in range(10)]
            width, height, rows = decode(samples=samples, depth=depth, palette=palette[:top + 1],
                                         filters=(0, 1, 2, 3, 4))
            self.assertEqual((width, height), (7, 10))
            self.assertEqual(rows, [[palette[v] + (255,) for v in row] for row in samples], depth)

    def test_reads_sub_byte_grey_with_its_transparent_level(self):
        for depth in (1, 2, 4):
            top = (1 << depth) - 1
            samples = [[(x + y) & top for x in range(9)] for y in range(4)]
            _, _, rows = decode(samples=samples, depth=depth, colour=0, trns=struct.pack(">H", 0),
                                filters=(2, 3, 4, 1))
            want = [[(v * 255 // top,) * 3 + (0 if v == 0 else 255,) for v in row] for row in samples]
            self.assertEqual(rows, want, depth)


class BoxTest(unittest.TestCase):
    def test_region_outside_image_raises(self):
        rows = [[(x, y, 0, 255) for x in range(4)] for y in range(4)]
        self.assertEqual(sample.fill(rows, 1, 1, 2, 2)[1], 0.25)
        for box in ((-1, 0, 2, 2), (3, 3, 2, 2), (0, 0, 0, 2)):
            with self.assertRaises(ValueError, msg=box):
                sample.region(rows, *box)

    def test_mask_outside_image_raises(self):
        rows = [[(9, 9, 9, 255)] * 4 for _ in range(4)]
        with self.assertRaises(ValueError):
            sample.mask(rows, [(10, 10, 2, 2)])
        self.assertEqual(sample.mask(rows, [(-1, -1, 3, 3)]), [(9, 9, 9, 255)])


@unittest.skipUnless(shutil.which("sh"), "needs a POSIX sh")
class ShotTest(unittest.TestCase):
    """shot.sh with stub swift, screencapture and sips on PATH and a scratch HOME."""

    def shot(self, winid):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / "bin").mkdir()
            log = d / "calls"
            stubs = {"swift": f"printf '%s' '{winid}'; [ -n '{winid}' ]",
                     "screencapture": f"echo screencapture >> '{log}'",
                     "sips": f"echo sips >> '{log}'"}
            for name, body in stubs.items():
                (d / "bin" / name).write_text(f"#!/bin/sh\n{body}\n")
                (d / "bin" / name).chmod(0o755)
            env = dict(os.environ, HOME=str(d), PATH=f"{d / 'bin'}:{os.environ['PATH']}")
            args = ["sh", str(NATIVE / "shot.sh")]
            args += ["light", "t"] if "~/.design-systems/$1/" not in (NATIVE / "shot.sh").read_text() else ["x", "light", "t"]
            done = subprocess.run(args, env=env, capture_output=True, text=True)
            return done.returncode, (log.read_text().split() if log.exists() else [])

    def test_no_window_stops_before_capturing(self):
        for winid in ("", "no window"):
            code, calls = self.shot(winid)
            self.assertEqual((code, calls), (1, []), repr(winid))

    def test_a_window_id_reaches_capture(self):
        self.assertEqual(self.shot("4242"), (0, ["screencapture", "sips"]))


if __name__ == "__main__":
    unittest.main()
