# Public route

Copied from `tools/kit/capture/public` and left unadapted.

`public.mjs` still targets Gauth. It was not pointed at coolors.co. The one
headless Playwright probe of `https://coolors.co/` (1440x900) stayed on a
Cloudflare managed challenge (HTTP 403, title `Just a moment...`, Ray ID
`a5c833ed7a3d5f2e`). The capture stopped. No second headless launch, no
challenge bypass, no consent click.

The probe record is `raw/block.json`.
