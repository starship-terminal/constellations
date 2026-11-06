"""Tests for tools/kit/capture/native/sample.py. Run with `make test`."""
import struct
import sys
import tempfile
import unittest
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "kit" / "capture" / "native"))
import sample  # noqa: E402


def _paeth(a, b, c):
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    return a if pa <= pb and pa <= pc else b if pb <= pc else c


def write_png(path, rows, filt=0):
    """A minimal 8-bit RGBA PNG; filt sets every row's filter type (0 none, 1 sub, 2 up,
    3 average, 4 Paeth), encoded the way the PNG spec defines so the decoder is checked."""
    h, w = len(rows), len(rows[0])
    raw, prev = b"", bytes(w * 4)
    for row in rows:
        flat = bytes(v for px in row for v in px)
        left = lambda i: flat[i - 4] if i >= 4 else 0
        upleft = lambda i: prev[i - 4] if i >= 4 else 0
        enc = {0: lambda i: flat[i], 1: lambda i: flat[i] - left(i), 2: lambda i: flat[i] - prev[i],
               3: lambda i: flat[i] - (left(i) + prev[i]) // 2,
               4: lambda i: flat[i] - _paeth(left(i), prev[i], upleft(i))}[filt]
        raw += bytes([filt]) + bytes(enc(i) & 255 for i in range(len(flat)))
        prev = flat
    chunk = lambda k, d: struct.pack(">I", len(d)) + k + d + struct.pack(">I", zlib.crc32(k + d))
    Path(path).write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
                          + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b""))


class SampleTest(unittest.TestCase):
    WHITE, INK, GREY = (255, 255, 255, 255), (17, 17, 17, 255), (120, 120, 120, 255)

    def png(self, filt=0):
        rows = [[self.WHITE] * 6 for _ in range(4)]
        rows[1][2], rows[1][3], rows[2][2] = self.INK, self.GREY, self.GREY
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            path = f.name
        write_png(path, rows, filt)
        return sample.read_png(path)

    def test_every_filter_type_decodes_to_the_same_pixels(self):
        expected = self.png(0)[2]
        for filt in (1, 2, 3, 4):
            self.assertEqual(self.png(filt)[2], expected, f"filter {filt}")

    def test_fill_text_and_edges(self):
        _, _, rows = self.png(1)
        colour, share = sample.fill(rows, 0, 0, 6, 4)
        self.assertEqual((colour, round(share, 2)), (self.WHITE, 0.88))
        self.assertEqual(sample.text(rows, 0, 0, 6, 4), self.INK)
        self.assertEqual(sample.edges(rows, row=1), [(0, 2, self.WHITE), (2, 1, self.INK), (3, 1, self.GREY), (4, 2, self.WHITE)])

    def test_mask_paints_text_with_the_surrounding_fill_and_round_trips(self):
        _, _, rows = self.png(1)
        self.assertEqual(sample.mask(rows, [(2, 1, 2, 2)]), [self.WHITE])
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            out = f.name
        sample.write_png(out, rows)
        _, _, back = sample.read_png(out)
        self.assertTrue(all(px == self.WHITE for row in back for px in row))

    def test_reads_a_quantised_package_screenshot(self):
        shot = HERE.parent / "systems/claude/screenshots/home-light.png"
        _, _, rows = sample.read_png(shot)
        self.assertEqual(sample.hexof(sample.fill(rows, 1500, 100, 200, 40)[0]), "#FCFCFB")


if __name__ == "__main__":
    unittest.main()
