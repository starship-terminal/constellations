# Programa capture tools

`build_tokens.py` checks [tokens.json](../tokens.json) against the evidence
labels. It does not invent colours. `test_build_tokens.py` runs that check.

The values were read in the T3 preview browser with `preview_evaluate` on
19 November 2026. Screenshots of the public marketing pages were taken with
headless Playwright because `preview_snapshot` returned "The browser is not
producing screenshot frames." Login and register returned 403 in that
headless browser, so those pages were measured in the preview browser only.
