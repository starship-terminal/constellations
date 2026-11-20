# Programa capture tools

`build_tokens.py` checks [tokens.json](../tokens.json) against the evidence
labels and against [raw/](../raw/): a Measured, Declared or Derived value must
appear in a raw reading once `raw_check.py` normalises both sides. Values read
in the preview browser but not saved to raw/ are labelled Reconstruction. It
does not invent colours or write tokens.json. `test_build_tokens.py` runs that
check.

The values were read in the T3 preview browser with `preview_evaluate` on
19 November 2026. Screenshots of the public marketing pages were taken with
headless Playwright because `preview_snapshot` returned "The browser is not
producing screenshot frames." Login and register returned 403 in that
headless browser, so those pages were measured in the preview browser only.
