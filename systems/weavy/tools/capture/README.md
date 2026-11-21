# Capture scripts

Public marketing pages were read with headless Playwright against `https://www.weavy.ai/` (redirects to `https://weave.figma.com/`). Screenshots and readings stayed in `~/.design-systems/weavy/` and were not committed. `quantize.py` writes the 256-colour PNGs into `screenshots/`.

The signed-in route was not used. `https://app.weavy.ai/signin` is a login wall. Figma, Google, Microsoft and Apple controls were not clicked. No form was submitted.

Shared kit files (`screenshot.mjs`, `quantize.py`, `css-colour.mjs`, `safe-url.mjs`) are the repo kit. `public/lib.mjs` sets the product base URL. Product-specific page lists live in the capture notes, not in a second product's scripts.
