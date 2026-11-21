#!/usr/bin/env python3
"""Copy the Runway style-guide template to style-guide.html. Values are the measured tokens."""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
(HERE.parent / "style-guide.html").write_text((HERE / "style-guide.template.html").read_text())
print("wrote style-guide.html")
