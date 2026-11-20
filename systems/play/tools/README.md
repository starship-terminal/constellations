# Play tools

`build_tokens.py` checks [tokens.json](../tokens.json). It refuses a token whose source has no evidence label, a Measured, Declared or Derived value that no file in [raw/](../raw/) holds, a colour that is not hex, and a dimension that is not one px length. It does not rebuild tokens from a dump: the live host did not resolve, and the archive readings the tokens were typed from were not saved, so every token is labelled Reconstruction. [raw/capture.json](../raw/capture.json) holds the capture notes.

```bash
python3 tools/build_tokens.py
```

`test_build_tokens.py` runs that check. `python3 tools/package_tests.py play` from the repo root runs it.
