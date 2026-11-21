# Tools

`build_tokens.py` writes [tokens.json](../tokens.json) from [raw/readings.json](../raw/readings.json). `build_style_guide.py` writes [style-guide.html](../style-guide.html) from that token file. Neither script opens the site.

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```
