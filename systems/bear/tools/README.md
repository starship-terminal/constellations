# Bear builders

`build_tokens.py` reads [raw/elements.json](../raw/elements.json) and writes [tokens.json](../tokens.json). Every colour and length in the token file is taken from that reading. The script converts computed rgb to hex. It does not keep a second copy of the numbers.

`build_style_guide.py` reads `tokens.json` and writes [style-guide.html](../style-guide.html).

```sh
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

The live measure script is not in this folder. It ran once, headless Chromium, no clicks and no typing, and its readings are in `raw/elements.json`.
