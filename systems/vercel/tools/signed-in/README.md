# Signed-in walk builders

`build_login_review.py` writes `login-review.json` from the 2026-11-21 notes.

`build_tokens.py`, `build_style_guide.py` and `build_components_md.py` rebuild a dashboard-only token set from `raw/css-vars.json`. They are not the package builders. The public `tokens.json` stays the 2026-11-19 reading. Do not run these three from `tools/` or they will replace that file.
