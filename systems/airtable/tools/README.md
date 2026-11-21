# Airtable tools

The builders that produce this package and the capture kit that read it from
www.airtable.com's public marketing pages. The public screenshots and
css-vars were refreshed on 2026-11-21. Everything is
deterministic: edit the raw inputs or the scripts, never the generated files.

Builders (run from `systems/airtable/`):

```bash
python3 tools/build_tokens.py        # raw/component-tokens.json -> tokens.json
python3 tools/build_style_guide.py   # tokens.json + style-guide.template.html -> style-guide.html
python3 tools/build_components_md.py # raw readings + tokens.json -> components.md
python3 tools/token_checks.py        # token sanity checks
```

Capture kit (`tools/capture/`, Playwright + Pillow; `PLAYWRIGHT` points at a
Playwright install's `index.mjs`, `PYTHON` at the venv interpreter):

```bash
PLAYWRIGHT=... node tools/capture/public/public.mjs       # screenshots -> scratch dir
python3 tools/capture/quantize.py <dir>                    # -> screenshots/ (256 colours)
PLAYWRIGHT=... node tools/capture/public/measure.mjs       # full component pass
PLAYWRIGHT=... node tools/capture/public/remeasure.mjs     # gap-fill pass over the same JSON
node tools/capture/public/build-measurements.mjs           # -> raw/measurements.md
PLAYWRIGHT=... node tools/capture/vars.mjs                 # -> raw/css-vars.json
PLAYWRIGHT=... node tools/capture/icons.mjs                # -> icons/ + icons/INDEX.tsv
```

`lib.mjs` holds the shared helpers: the browser launch, promo/consent dismissal,
and the sweep that hides the Qualified "Riley" widget and Google One Tap before
every shot. `measure.mjs` captures states with real hover, real keyboard focus
and a DevTools-forced :active; `remeasure.mjs` re-reads only the components it
is pointed at and merges them into `raw/components-computed.json`.
