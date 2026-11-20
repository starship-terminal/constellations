#!/usr/bin/env python3
"""Render style-guide.html from tokens.json and tools/style-guide.template.html."""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())
template = (HERE / "tools" / "style-guide.template.html").read_text()


def block(theme):
    lines = []
    for name, token in T[theme].items():
        lines.append(f"  --{name}: {token['$value']};")
    return "\n".join(lines)


html = template.replace("/*LIGHT*/", "\n" + block("light") + "\n").replace("/*DARK*/", "\n" + block("dark") + "\n")
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
