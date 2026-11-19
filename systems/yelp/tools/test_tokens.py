"""The committed tokens.json matches the raw variable dump."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent


def hex_of(triplet):
    parts = [int(p) for p in triplet.split(",")]
    return "#{:02X}{:02X}{:02X}".format(*parts)


class TokensTest(unittest.TestCase):
    def test_brand_text_and_page_match_the_dump(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        rows = {}
        for line in (HERE / "raw" / "css-vars.tsv").read_text().splitlines():
            name, val = line.split("\t", 1)
            rows[name] = val
        self.assertEqual(tokens["light"]["color"]["bg"]["default"]["$value"], hex_of(rows["--sem-color-bg-default"]))
        self.assertEqual(tokens["light"]["color"]["text"]["default"]["$value"], hex_of(rows["--sem-color-text-default"]))
        self.assertEqual(
            tokens["light"]["color"]["bg"]["brandPrimary"]["strong"]["default"]["$value"],
            hex_of(rows["--sem-color-bg-brandPrimary-strong-default"]),
        )
        self.assertEqual(tokens["light"]["color"]["border"]["default"]["$value"], hex_of(rows["--sem-color-border-default"]))
        self.assertEqual(tokens["core"]["color"]["rating"]["five"]["$value"], hex_of(rows["--sem-color-bg-rating-five"]))
        self.assertNotIn("dark", tokens)


if __name__ == "__main__":
    unittest.main()
