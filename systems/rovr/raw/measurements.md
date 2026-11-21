# ROVR measurements

Read on 2026-11-21 from https://www.rovr.live/ in headless Chromium, signed out.

Desktop viewport: innerWidth 1440, innerHeight 900, devicePixelRatio 1. Phone viewport: innerWidth 390, innerHeight 844, devicePixelRatio 2. PNG sizes match those CSS viewports (phone PNGs are 780x1688). Sidecars live beside the full-colour shots in `~/.design-systems/rovr/raw-shots/` and are not committed.

html class is `dark`. color-scheme is `dark`. Body background `rgb(0, 0, 0)`, body color `rgb(250, 250, 250)`, body font `kernStandard, "kernStandard Fallback", system-ui, sans-serif` at 16px.

The painted chrome yellow is `rgb(255, 240, 87)` on the MENU pill, play button, and track strip. The computed `--primary` channel paints `rgb(255, 255, 87)`. Both are recorded. They are not the same value.

Component readings are in [components-computed.json](components-computed.json). Declared custom properties are in [css-vars.json](css-vars.json). The stylesheet harvest resolved names on a blank probe, so those resolved values are the light defaults. Dark role tokens use the live-page paint in components-computed.json.
