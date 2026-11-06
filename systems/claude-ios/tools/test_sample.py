"""Tests for capture/native/sample.py: packed palette PNGs and boxes outside the image.
Run: python3 -m unittest discover -s tools."""
import pathlib
import struct
import sys
import tempfile
import unittest
import zlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "capture" / "native"))
import sample  # noqa: E402


def chunk(kind, data):
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))


def packed_png(path, indices, palette, depth):
    """Write rows of palette indices as a `depth`-bit palette PNG, every row with the Sub filter."""
    width, per = len(indices[0]), 8 // depth
    raw = b""
    for row in indices:
        line = bytearray((width * depth + 7) // 8)
        for x, v in enumerate(row):
            line[x // per] |= v << (8 - depth * (x % per + 1))
        sub = bytes((line[i] - (line[i - 1] if i else 0)) & 255 for i in range(len(line)))
        raw += b"\x01" + sub
    plte = b"".join(bytes(c) for c in palette)
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", width, len(indices), depth, 3, 0, 0, 0))
                + chunk(b"PLTE", plte) + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b""))


class SampleTest(unittest.TestCase):
    def test_reads_sub_byte_palette(self):
        palette = [(i * 16, 255 - i * 16, i * 8) for i in range(16)]
        for depth in (1, 2, 4):
            top = (1 << depth) - 1
            indices = [[(x * 3 + y) & top for x in range(7)] for y in range(3)]
            with tempfile.TemporaryDirectory() as d:
                path = pathlib.Path(d) / "p.png"
                packed_png(path, indices, palette[:top + 1], depth)
                width, height, rows = sample.read_png(path)
            self.assertEqual((width, height), (7, 3))
            self.assertEqual(rows, [[palette[v] + (255,) for v in row] for row in indices], depth)

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


if __name__ == "__main__":
    unittest.main()
