"""style-guide.html is hand-written from tokens.json.

Run from the package: python3 tools/build_style_guide.py
"""
import pathlib

html = (pathlib.Path(__file__).resolve().parents[1] / "style-guide.html").read_text()
for needle in ("#0b57d0", "#16171a", "#f8f9fa", "#1a0dab"):
    if needle not in html:
        raise SystemExit(f"style guide missing {needle}")
print("style-guide.html has the measured swatches")
