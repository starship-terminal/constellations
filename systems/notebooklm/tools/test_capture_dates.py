"""capture/signed-in/measure.mjs merges into the committed components file. Its _meta.read must
keep the earlier date until a state is read, and every state carries its own read date, so a rerun
that fails throughout never redates old readings. The script drives a browser, so this checks its
source rather than running it."""
import pathlib
import unittest

SRC = (pathlib.Path(__file__).resolve().parent / "capture" / "signed-in" / "measure.mjs").read_text()


class CaptureDatesTest(unittest.TestCase):
    def test_run_date_moves_only_on_a_reading(self):
        self.assertIn("read: PRIOR_READ || RUN,", SRC)
        self.assertIn("lastAttempt: RUN,", SRC)
        self.assertNotIn("read: new Date()", SRC)
        self.assertIn("...s, via, read: RUN };\n        out._meta.read = RUN;", SRC)

    def test_kept_readings_keep_their_date(self):
        self.assertIn("recaptureError: error, recaptureRun: RUN", SRC)
        self.assertIn("!st.read && PRIOR_READ) st.read = PRIOR_READ", SRC)


if __name__ == "__main__":
    unittest.main()
