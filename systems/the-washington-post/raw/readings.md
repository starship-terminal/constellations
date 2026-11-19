# Readings

Live computed styles from the T3 preview browser on 2026-11-19.

Screenshot attempt: `preview_snapshot` returned "The browser is not producing screenshot frames. For a desktop tab, show or restore the T3 Code window and try again." No PNG was written.

Pages opened, signed out:

- https://www.washingtonpost.com/
- https://www.washingtonpost.com/entertainment/video-games/2026/11/18/grand-theft-auto-vi-is-an-astonishing-american-epic/
- https://www.washingtonpost.com/subscribe/signin/
- https://www.washingtonpost.com/politics/

Not entered: Subscribe, checkout, card, phone, account creation, OAuth, SSO, email submit.

The root exposed 577 computed custom properties. Static hue ramps (`--wpds-colors-*-static`) were read in the browser and are not all copied into `computed-vars.json`. The semantic, type, space, radius, shadow and motion names used by `tools/build_tokens.py` are in that file. Component boxes are in `components-computed.json`.
