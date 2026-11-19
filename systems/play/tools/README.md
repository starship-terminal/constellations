# Play tools

`build_tokens.py` checks [tokens.json](../tokens.json). It refuses a token whose source is empty, a colour that is not hex, and a dimension that is not one px length. It does not rebuild tokens from a dump: the live host did not resolve, so the tokens were written from the archive readings in [raw/capture.json](../raw/capture.json).

```bash
python3 tools/build_tokens.py
```

`test_build_tokens.py` runs that check. `python3 tools/package_tests.py play` from the repo root runs it.
