"""A partial tile set is rejected before it can replace the published image."""
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
source = (HERE / "quantize.py").read_text()
start = source.index("def complete_tile_set")
end = source.index("def stitched_sidecar")
namespace = {}
exec(source[start:end], namespace)
complete_tile_set = namespace["complete_tile_set"]


class PartialTileTest(unittest.TestCase):
    def test_a_lone_first_tile_is_not_a_complete_set(self):
        # The recorded page is 14642px. The one remaining tile covers 14000.
        # Rejecting it is what stops the stitcher from overwriting the full image.
        lone = [{"capture": {"clip": {"x": 0, "y": 0, "width": 1440, "height": 14000}},
                 "actual": {"documentSize": {"height": 14642}}}]
        self.assertFalse(complete_tile_set([(0, "part0")], lone))

    def test_a_gap_is_rejected_and_contiguous_tiles_are_accepted(self):
        gapped = [
            {"capture": {"clip": {"x": 0, "y": 0, "width": 10, "height": 8}}},
            {"capture": {"clip": {"x": 0, "y": 20, "width": 10, "height": 8}}},
        ]
        whole = [
            {"capture": {"clip": {"x": 0, "y": 0, "width": 10, "height": 8}}},
            {"capture": {"clip": {"x": 0, "y": 8, "width": 10, "height": 6}}},
        ]
        self.assertFalse(complete_tile_set([(0, "a"), (1, "b")], gapped))
        self.assertTrue(complete_tile_set([(0, "a"), (1, "b")], whole))
        self.assertFalse(complete_tile_set([(0, "a"), (2, "b")], whole))
        self.assertFalse(complete_tile_set([(1, "b")], whole[1:]))
        recorded = [{**m, "actual": {"documentSize": {"height": 14}}} for m in whole]
        self.assertTrue(complete_tile_set([(0, "a"), (1, "b")], recorded))
        short = [{**m, "actual": {"documentSize": {"height": 20}}} for m in whole]
        self.assertFalse(complete_tile_set([(0, "a"), (1, "b")], short))


if __name__ == "__main__":
    unittest.main()
