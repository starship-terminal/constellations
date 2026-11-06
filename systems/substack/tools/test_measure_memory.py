"""run() decodes each capture once and releases it before decoding the next, so a run holds one
image (several hundred MB as Python tuples) at a time. Run: python3 -m unittest discover -s tools."""
import gc
import pathlib
import sys
import tempfile
import unittest
import weakref
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import measure  # noqa: E402


class Rows(list):
    """A stand-in for a decoded capture that a weakref can watch."""


class MemoryTest(unittest.TestCase):
    def test_one_capture_alive_at_a_time_each_decoded_once(self):
        decoded, alive = [], []

        def decode(key):
            gc.collect()
            self.assertTrue(all(ref() is None for ref in alive), f"a capture was still held when {key} was decoded")
            self.assertNotIn(key, decoded, f"{key} decoded twice")
            decoded.append(key)
            rows = Rows()
            alive.append(weakref.ref(rows))
            return rows

        ops = {n: (lambda *a, **k: {"value": "x", "evidence": "Sampled"}) for n in dir(measure) if n.startswith("op_")}
        with tempfile.TemporaryDirectory() as d:
            raw = pathlib.Path(d)
            for theme in ("dark", "light"):
                (raw / theme).mkdir()
            names = set()
            for entry in measure.R.values():
                for e in entry if isinstance(entry, list) else [entry]:
                    if isinstance(e, dict):
                        names |= {e[t][0] for t in ("dark", "light") if t in e}
                    else:
                        names.add(e[0].split("/")[-1])
            for theme in ("dark", "light"):
                for name in names:
                    (raw / theme / f"{name}.png").write_bytes(b"")
            if hasattr(measure, "load"):
                patch = mock.patch.object(measure, "load", lambda raw, theme, name: decode(f"{theme}/{name}"))
            else:
                patch = mock.patch.object(measure.sample, "read_png",
                                          lambda png: (0, 0, decode(f"{png.parent.name}/{png.stem}")))
            with patch, mock.patch.multiple(measure, **ops):
                out = measure.run(raw)
        self.assertTrue(out)
        self.assertEqual(len(decoded), len(set(decoded)))


if __name__ == "__main__":
    unittest.main()
