"""The wrong-element corrections apply to the old readings only, never to a recapture."""
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from wrong_element import corrected  # noqa: E402

C = json.loads((ROOT / "raw" / "components-computed.json").read_text())["components"]


def reading(classes, paint=None):
    return {"title": "Fresh title", "desc": "Fresh description.",
            "states": {"default": {"classes": classes, "paint": paint or []}}}


class WrongElement(unittest.TestCase):
    def test_the_committed_readings_are_corrected(self):
        out = corrected(C)
        self.assertEqual(out["content-block-dark"]["title"], "Dark band heading")
        self.assertEqual(out["plan-head"]["title"], "Plan header icon")
        self.assertIn("tooltip closed", out["feature-tooltip"]["desc"])

    def test_a_recapture_of_the_right_element_keeps_its_own_description(self):
        fresh = {
            "content-block-dark": reading("x_ContentBlockDark"),
            "plan-head": reading("x_HeaderCell"),
            "feature-tooltip": reading("x_Cell x_CellTooltip",
                                       [{"node": "div.fui-Tooltip__content", "size": "180.0x32.0"}]),
        }
        out = corrected(fresh)
        for key in fresh:
            self.assertEqual(out[key]["title"], "Fresh title", key)
            self.assertEqual(out[key]["desc"], "Fresh description.", key)

    def test_the_raw_readings_are_not_changed(self):
        before = json.dumps(C, sort_keys=True)
        corrected(C)
        self.assertEqual(json.dumps(C, sort_keys=True), before)


if __name__ == "__main__":
    unittest.main()
