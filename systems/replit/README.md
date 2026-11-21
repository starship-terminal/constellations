# Replit

Replit is an AI app and website builder. This package records the public signed-out site at https://replit.com/, measured on 22 November 2026. The homepage and pricing were read at innerWidth 1169. The empty login wall at https://replit.com/login was read and not filled. `color-scheme` was light. `prefers-color-scheme` was dark, and the page stayed light. There is no public theme toggle.

A site-tree walk on the same day mapped the header, footer, and the public pages those controls open. That walk photographed the pages. This pass did not recapture them. The map is [site-tree.md](site-tree.md).

Nothing was typed. Login, signup, checkout, and subscribe were not followed. Identity providers were not clicked. No repl was started. The cookie control was not accepted or rejected.

| File or Path | What it holds | How many |
|---|---|---|
| [README.md](README.md) | This file | 1 |
| [icon.png](icon.png) | The site favicon, resized to 128 px from the 192 px PNG at `/public/icons/favicon-prompt-192-rebrand.png` | 1 |
| [tokens.json](tokens.json) | Tokens Studio sets: `core` and `light`. No dark set. Every colour is a hex from computed style. | 129 tokens |
| [style-guide.html](style-guide.html) | The tokens rendered as a page | 1 |
| [site-tree.md](site-tree.md) | The public site tree from the earlier photograph pass | 1 |
| [screenshots/](screenshots) | Viewport shots from the site-tree pass. Not recaptured here. | 50 PNG |
| [raw/](raw) | [readings.json](raw/readings.json), the computed-style dump the builders read | 1 |
| [tools/](tools) | [build_tokens.py](tools/build_tokens.py) and [build_style_guide.py](tools/build_style_guide.py) | 2 scripts |

## Brief

The Brief is written by `tools/brief.py` after a catalog entry exists. This package has no catalog entry yet. catalog.json was left alone.

## Health

The Health section is written by `tools/health.py` after grades exist. None exist yet.

## How the values were read

Every colour came from computed style in the preview browser, signed out, on 22 November 2026.

- Named colours are custom properties on `documentElement` at https://replit.com/. Each declared colour was assigned to a probe element's `color`, and the computed `rgb` was converted to hex. Those hex values are in [raw/readings.json](raw/readings.json).
- Painted colours are `getComputedStyle` on the body, header, footer, the home h1, Sign up, the composer card, Start, the pricing CTAs, the empty login fields, and the Home link. Nothing was typed into a field.
- Type, radius, and spacing are the same computed styles, plus the `--font-*`, `--radius-*`, and `--spacing-*` custom properties.
- [tools/build_tokens.py](tools/build_tokens.py) writes [tokens.json](tokens.json) from the readings. [tools/build_style_guide.py](tools/build_style_guide.py) writes the guide from the token file.

No colour was read off a screenshot.

## What to distrust

- The public site paints one light theme. The stylesheet contains `._sdz_dark` rules. They were not applied on the homepage, pricing, or the login wall. There is no dark set in [tokens.json](tokens.json).
- `--background-default` is `#fcfcfc`. The marketing body paints `#f6f5f4`. Both are recorded. The page role uses the painted body colour.
- Accent ramps (`--accent-blue-dimmer` and the rest) are declared on the page. Most of them were not the computed colour of a measured control. The painted orange is `#ff3c00` on Sign up, which is not `--accent-orange-default` (`#d96d00`).
- Pricing paints a second orange, `#f03800` on Try now, and a blue, `#1b8dff` on Upgrade to Pro. The header Sign up is `#ff3c00`. The disabled Log In button is `#ff3b00`.
- Footer links computed `#4b5563`. `--foreground-dimmest` is `#5c5f66`. The muted role points at the named token.
- Screenshots are from the earlier site-tree pass. Read colours from [tokens.json](tokens.json).
- Login, signup, checkout, the editor, and a signed-in workspace were not entered.

## Fonts

The public pages use **Replit Diatype** for text and **Replit Diatype Mono** for the small template label. Both were loaded on the homepage. The package does not include the font files. The style guide falls back to Segoe UI.

`--font-weight-medium` is 460 and `--font-weight-bold` is 560. The Sign up label computed 500. Footer column titles computed 600.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Colour roles | captured | `light.*` over measured `core.color.*` |
| Type | captured | `core.typography` from the home h1, a section heading, body, nav, and Sign up |
| Radius and spacing | captured | `--radius-*` and `--spacing-*`, plus the composer radius 20px |
| Dark theme | not captured | stylesheet has `._sdz_dark`. No public page painted it. |
| Login and signup | stopped | empty walls. Fields were not filled. Identity providers were not clicked. |
| Checkout and subscribe | not opened | pricing CTAs were measured and not followed |
| Cookie dialog | not opened | Your privacy choices was not clicked |
| Screenshots | already present | 50 PNG files from the site-tree pass. Not recaptured. |

## Do and don't

1. **Do paint the page cream.** Body background is `#f6f5f4`. The header is `#faf6f1`. The footer is `#faf5f0`. See [home-light-1440.png](screenshots/home-light-1440.png).
2. **Do use orange for the one marketing action.** Sign up and Start are `#ff3c00` with white type and an 8px radius. See [home-light-1440.png](screenshots/home-light-1440.png).
3. **Do set display type at 64px with a tight line.** The home h1 is 64px, weight 400, line-height 64px, letter-spacing -3.84px, colour `#37383c`. See [home-light-1440.png](screenshots/home-light-1440.png).
4. **Don't invent a dark marketing theme.** The public pages stayed light while the OS preferred dark. See [pricing-light-1440.png](screenshots/pricing-light-1440.png).
5. **Don't follow Sign up from this package.** The signup wall was left empty. See [signup-empty-light-1440.png](screenshots/signup-empty-light-1440.png).

## Rebuild

From this folder:

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

The scripts read [raw/readings.json](raw/readings.json). They do not open the site.
