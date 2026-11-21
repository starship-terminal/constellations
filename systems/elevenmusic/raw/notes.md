# Readings

[readings.json](readings.json) is the Playwright `getComputedStyle` dump from 2026-11-21.

- homeDark: https://elevenmusic.io/ at 1440×900, default dark (`html` class includes `dark`).
- homeLight: same URL after adding `light`, setting `data-theme=light`, and clicking the footer Light theme control.
- loginDialog: Sign in dialog, not submitted.
- mobile: 390×844, deviceScaleFactor 2.

Colours arrived as CSS `lab()`. tokens.json stores the sRGB conversion. Pill radii arrived as `3.35544e+07px` and are stored as `9999px`.

The page did not declare a product token layer. The 466 custom properties harvested were Tailwind internals (`--tw-*`) and were not promoted to tokens.

`meta name=theme-color` was `#030303`. Body background in dark computed as `lab(0 0 0)`, stored as `#000000`.
