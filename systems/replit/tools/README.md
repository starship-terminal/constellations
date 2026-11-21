The builders write [tokens.json](../tokens.json) and [style-guide.html](../style-guide.html) from [raw/readings.json](../raw/readings.json).

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

The readings were taken in the preview browser on 22 November 2026 from the signed-out public site. The scripts do not fetch the site. To refresh a value, read it again from computed style, replace the matching field in the readings file, and run both scripts.
