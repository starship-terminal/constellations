# Public route

The kit's public route was copied here and never adapted (its `public.mjs`
still targeted Gauth), so the 2026-11 audit deleted it. The one
headless Playwright probe of `https://coolors.co/` (1440x900) stayed on a
Cloudflare managed challenge (HTTP 403, title `Just a moment...`, Ray ID
`a5c833ed7a3d5f2e`). The capture stopped. No second headless launch, no
challenge bypass, no consent click.

The probe record is `raw/block.json`.
