# Sentry public landing evidence

Captured 2026-10-31 in Codex's visible in-app browser at https://sentry.io/welcome/.
This folder contains public marketing evidence only. Embedded diagnostic, replay and trace images do not establish signed-in component coverage.

## Captures

- Desktop hero: 1440 x 1000 CSS pixels and native image pixels.
- Desktop full page: 1440 x 8804 native pixels, captured after scrolling to load the marketing images.
- Desktop Platform menu: 1440 x 1000, fully visible and inspected.
- Mobile hero and navigation menu: 390 x 844 each, fully inspected. The hero illustration extends beyond the mobile viewport in the product itself.

Screenshots live in ../../screenshots/public/. Each PNG has dimension metadata. The browser supplied JPEGs; these were converted to 256-colour PNGs, not treated as colour measurements. Original files remain outside git in ~/.design-systems/sentry/raw-shots/public/.

## Measurements

Each reading records URL, time, actual viewport, device pixel ratio, visual viewport, root theme class, 170 root CSS custom properties, computed component styles and value occurrence counts. Counts include rendered elements below the fold; they are not a semantic-use ranking. The observed root class is dark. Marketing Mode was left unchanged. No alternate public theme was inferred.

The reader is ../../tools/capture/read-public.js, run through the in-app browser's read-only evaluation API. ../../tools/build_public_tokens.py rebuilds tokens.json from these readings. The token subset preserves declared hex colours and single dimensions, plus measured hero typography. Complex CSS and other values remain in the readings; no ramps or app roles were invented. Public tokens are separate from the signed-in app tokens at ../../tokens.json.

## App evidence

Signed-in app capture is complete within the available account data. See ../../README.md and ../coverage.json for captured states and explicit gaps. The app includes trace samples, span attributes, a waterfall, filters, menus and dialogs in both themes; issue lists were empty across all statuses over 30 days. Public demo images remain marketing evidence only. Shared skills and capture documentation were left unchanged.
