"""capture/drive.py checks a target's accessibility text before pressing Return on a launcher result or clicking
a Settings sidebar row. The readings below are invented in the shape ax.swift prints (seen live on 2026-11-07);
nothing is sent to Raycast."""
import importlib.util
import pathlib
import unittest
from unittest import mock

spec = importlib.util.spec_from_file_location("raycast_drive", pathlib.Path(__file__).resolve().parent / "capture" / "drive.py")
drive = importlib.util.module_from_spec(spec)
spec.loader.exec_module(drive)

RESULTS = [["h", "Results"], ["t", "Search Emoji & Symbols"], ["t", "Raycast"], ["t", "Command"],
           ["h", "Files"], ["t", "emoji"], ["t", "emoji.json"]]


class FirstResultTest(unittest.TestCase):
    def test_first_text_after_the_first_header(self):
        self.assertEqual(drive.first_result(RESULTS), "Search Emoji & Symbols")

    def test_text_before_any_header_is_not_a_result(self):
        self.assertEqual(drive.first_result([["t", "Search for apps"], ["h", "Results"], ["t", "Calculator"]]), "Calculator")

    def test_no_results(self):
        self.assertIsNone(drive.first_result([]))
        self.assertIsNone(drive.first_result([["h", "Results"]]))


class RowMatchesTest(unittest.TestCase):
    def test_the_row_with_its_label(self):
        self.assertTrue(drive.row_matches({"owner": "Raycast", "texts": ["General"]}, "General"))
        self.assertTrue(drive.row_matches({"owner": "Raycast", "texts": ["AI", "Pro"]}, "AI"))
        self.assertTrue(drive.row_matches({"owner": "Raycast", "texts": ["Someone", "Account"]}, "Account"))

    def test_another_row_or_app_or_the_whole_sidebar(self):
        self.assertFalse(drive.row_matches({"owner": "Raycast", "texts": ["General"]}, "Launcher"))
        self.assertFalse(drive.row_matches({"owner": "Finder", "texts": ["General"]}, "General"))
        self.assertFalse(drive.row_matches({"owner": "Raycast", "texts": ["General", "Launcher", "Shortcuts", "Keyboard"]}, "General"))
        self.assertFalse(drive.row_matches({"owner": "Raycast", "texts": []}, "General"))


class ExpectTest(unittest.TestCase):
    def test_top_result_passes_and_stops(self):
        with mock.patch.object(drive, "ax", return_value={"query": "emoji", "items": RESULTS}):
            drive.expect_top_result("emoji", "Search Emoji & Symbols")
            with self.assertRaises(SystemExit):
                drive.expect_top_result("emoji", "Clipboard History")
            with self.assertRaises(SystemExit):
                drive.expect_top_result("emo", "Search Emoji & Symbols")

    def test_row_passes_and_stops(self):
        with mock.patch.object(drive, "ax", return_value={"owner": "Raycast", "texts": ["General"]}):
            drive.expect_row(77, 250, "General")
            with self.assertRaises(SystemExit):
                drive.expect_row(77, 250, "Launcher")

    def test_every_settings_step_names_its_row(self):
        for name, (_, _, label, _) in drive.SETTINGS.items():
            self.assertTrue(label, name)


class ClickGuardTest(unittest.TestCase):
    def test_theme_select_reads_a_theme_name(self):
        self.assertTrue(drive.theme_select(["Raycast Dark"]))
        self.assertTrue(drive.theme_select(["Theme", "Raycast Light"]))

    def test_theme_guard_rejects_the_appearance_checkbox_and_nothing(self):
        self.assertFalse(drive.theme_select(["Follow System Appearance"]))
        self.assertFalse(drive.theme_select(["Dark", "Light"]))
        self.assertFalse(drive.theme_select([]))

    def test_footer_menu_button_reads_the_footer(self):
        self.assertTrue(drive.footer_menu_button(["Open Command", "Actions"]))
        self.assertTrue(drive.footer_menu_button(["Open Command", "\u21b5", "Actions", "\u2318", "K"]))

    def test_footer_guard_rejects_empty_and_unrelated_readings(self):
        self.assertFalse(drive.footer_menu_button([]))
        self.assertFalse(drive.footer_menu_button(["Search for apps and commands..."]))
        self.assertFalse(drive.footer_menu_button(["Calculator", "Command"]))
        self.assertFalse(drive.footer_menu_button(["Results", "Actions", "a", "b", "c", "d", "e"]))

    def test_guards_stop_before_a_click(self):
        with mock.patch.object(drive, "ax", return_value={"owner": "Raycast", "texts": ["Follow System Appearance"]}):
            with self.assertRaises(SystemExit):
                drive.expect_at(700, 315, "the General theme select", drive.theme_select)
        with mock.patch.object(drive, "ax", return_value={"owner": "Raycast", "texts": []}):
            with self.assertRaises(SystemExit):
                drive.expect_at(25, 448, "the footer menu button", drive.footer_menu_button)


if __name__ == "__main__":
    unittest.main()
