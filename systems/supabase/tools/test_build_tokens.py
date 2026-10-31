import unittest
from build_tokens import token

class ColorEvidenceTests(unittest.TestCase):
    def test_srgb_reference_neutrals(self):
        for css, expected in [('oklch(1 0 0)', '#ffffff'),
                              ('oklch(0 0 0)', '#000000'),
                              ('oklch(0.5 0 0)', '#636363')]:
            with self.subTest(css=css):
                self.assertEqual(token(css, 'color', 'fixture')['$value'], expected)

    def test_alpha_and_original_evidence_survive_conversion(self):
        css='oklch(1 0 0 / 0.075125)'
        result=token(css, 'color', 'fixture')
        self.assertEqual(result['$value'], 'rgba(255, 255, 255, 0.075125)')
        self.assertEqual(result['$extensions']['measuredCss'], css)
        self.assertTrue(result['$extensions']['source'].startswith('Derived:'))

    def test_unresolved_expression_is_rejected(self):
        with self.assertRaises(ValueError):
            token('oklch(from var(--page) l c h)', 'color', 'fixture')

if __name__ == '__main__': unittest.main()
