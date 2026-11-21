# Measurements

Public www.masterclass.com, 2026-11-21, signed out, headless Chromium.

Stylesheets were read from the homepage responses and stored outside the repo. `tools/extract_css_vars.py` wrote `css-vars.json` (572 unique custom properties). The public site paints one dark theme. Body background computed to `rgb(0, 0, 0)`. Body font computed to `Sohne, Helvetica, Arial, sans-serif`.

The Get MasterClass link, the visible desktop one, computed to background `rgb(227, 38, 82)` (`#e32652`, `--mc-color-pink-500`), color white, radius 8px, padding 12px 24px, font-weight 600, font-size 16px, line-height 20px, letter-spacing 0.16px, text-transform capitalize. Search `#searchInput` computed to height 44px.

Viewport shots were requested at 1440x900 (desktop, deviceScaleFactor 1) and 390x844 (phone, deviceScaleFactor 2). Each PNG has a `.png.capture.json` sidecar in the scratch folder `~/.design-systems/masterclass/raw-shots/`. The committed screenshots are 256-colour quantizations of those files.

The quiz option "Become a better chef" was below the first viewport and was not cropped in the second pass. Its control is visible in `screenshots/home-dark-default.png`.
