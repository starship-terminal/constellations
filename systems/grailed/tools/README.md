# How this package was produced

The public shop was read on 2026-11-22 from [https://www.grailed.com](https://www.grailed.com) in headed Google Chrome, driven by Playwright 1.55.0. The T3 preview tab loaded the homepage, then failed twice on screenshots:

`Preview automation snapshot failed: The browser is not producing screenshot frames. For a desktop tab, show or restore the T3 Code window and try again.`

After that, the capture switched to Chrome. The viewport was 1440 by 900 CSS pixels at `devicePixelRatio` 1, then 390 by 844 at `devicePixelRatio` 2. Nothing was typed. No identity provider was clicked. No captcha appeared.

Colours in [tokens.json](../tokens.json) come from `getComputedStyle` and from declared custom properties and rules in the site's CSS. They were not sampled from the PNGs.

[build_style_guide.py](build_style_guide.py) reads [tokens.json](../tokens.json) and writes [style-guide.html](../style-guide.html). Run it from the package:

```bash
python3 tools/build_style_guide.py
```

[icon.png](../icon.png) is [https://www.grailed.com/images/favicon@4x.png](https://www.grailed.com/images/favicon@4x.png), 139 px, resized to 128 px with `sips -z 128 128`.
