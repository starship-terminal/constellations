"""capture/signed-in/neutralise.py's filler: placeholder text of about the length it replaces, never an
IndexError for a text node that is only its prefix ("You said:", "Claude responded:")."""
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("neutralise_under_test", HERE / "capture" / "signed-in" / "neutralise.py")
neutralise = importlib.util.module_from_spec(spec)
spec.loader.exec_module(neutralise)


class FillerTest(unittest.TestCase):
    def test_length_follows_the_text_it_replaces(self):
        for n in (4, 12, 40):
            s = neutralise.filler(n, 3)
            self.assertLessEqual(len(s), n)
            self.assertTrue(s[0].isupper())

    def test_a_prefix_only_node_gets_a_short_filler(self):
        for n in (-1, 0, 1):
            s = neutralise.filler(n, 0)
            self.assertTrue(s)
            self.assertLessEqual(len(s), 4)


if __name__ == "__main__":
    unittest.main()
