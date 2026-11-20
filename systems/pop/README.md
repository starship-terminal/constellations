# Pop Site design reference

A token set and component reference for Pop Site's public marketing site. It was read from **https://pop.site/** on **2026-11-21**, signed out, in headless Chromium. Desktop shots are 1440 x 900 at 1x. Phone shots are 390 x 844 at 2x. The site is a Framer publish (`Framer fb64017`, published 17 Nov 2026). One light theme. No dark toggle.

Pop Site is a no-code personal-site builder. The public surface is a white page, ink `#171717` set in Satoshi, and one blue claim button: a 110-degree gradient from `#00a8f5` to `#3b82f6`, 40px tall, radius 26px. The same claim row repeats down the home page. Pricing has no plan picker. The editor, signup and sign-in live on `app.pop.site` and were not entered.

The control map is [site-tree.md](site-tree.md). Log In opens https://app.pop.site/?signin (email, password, or Google). Password was not submitted. Create Account and an empty Claim open https://app.pop.site/. Those branches stop there.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Pop Site's favicon, resized to 128 px |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the declared Framer colours that were read, the measured type roles, radii and a few sizes. `light` aliases the roles a captured control paints. `dark` is empty and is not in `$themes`. Every token carries `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Generated from [tokens.json](tokens.json) and this README. One theme, no provenance |
| [style-guide.html](style-guide.html) | Renders the measured roles and the claim button. Satoshi is not loaded |
| [components.md](components.md) | Measured controls, crops, and the gaps |
| [patterns.md](patterns.md) | How the header, claim row, FAQ, blog and footer fit together |
| [site-tree.md](site-tree.md) | Which control opens which page, wall, or same-page state |
| [components/crops/](components/crops) | Element screenshots, `{component}-{state}.png` |
| [screenshots/](screenshots) | `{page}-light-{state}.png`. Desktop 1440 x 900 at 1x. `mobile-*` is 390 x 844 at 2x. `-full` is the whole page. Three phone full pages are stitched from tiles |
| [raw/](raw) | [css-vars.json](raw/css-vars.json), [components-computed.json](raw/components-computed.json), [extra-readings.json](raw/extra-readings.json), [measurements.md](raw/measurements.md) |
| [icons/](icons) | [INDEX.tsv](icons/INDEX.tsv) only. No SVG set was lifted |
| [tools/](tools) | The builders and the capture scripts. See [Rebuild](#rebuild) |

## Brief

<!-- brief:start -->

Brief is not generated for this package. catalog.json was not edited, and `make brief` only writes a Brief for a catalog entry. The roles below are the measured ones.

Page `#ffffff`. Surface `#fafafc`. Text `#171717`. Muted `#545454`. Accent `#3b82f6`. The claim button is a gradient from `#00a8f5` to `#3b82f6`, not a flat accent. Focus outline `#005fcc` is Chromium's auto outline.

Type is Satoshi for marketing and Inter for articles, FAQ and the privacy form. Display is 69px / 500. Nav and claim labels are 15px / 500.

<!-- brief:end -->

## Health

<!-- health:start -->

Not graded. catalog.json was not edited, so this package is not in the scorecard. A later registration can run `python3 tools/grade.py --write --review pop=<grades.json>`.

Layout: `icons/` holds only INDEX.tsv. No SVG set was lifted. The wordmark and the FAQ chevron stay in the screenshots.

<!-- health:end -->

## How the values were read

Every value came off the running signed-out site in headless Chromium. Playwright lives at `~/.design-systems/pw`.

- **Tokens.** [tools/capture/public/measure-pop.mjs](tools/capture/public/measure-pop.mjs) read every stylesheet rule through the CSSOM. Framer declares colours on `body` as `--token-<uuid>`. Those values are in [raw/css-vars.json](raw/css-vars.json). Computed styles of the controls are in [raw/components-computed.json](raw/components-computed.json). The claim gradient is `backgroundImage`, saved in [raw/extra-readings.json](raw/extra-readings.json). [tools/build_tokens.py](tools/build_tokens.py) writes [tokens.json](tokens.json) from those three files.
- **Components.** The same script hovered, keyboard-focused, and forced `:active` through CDP. It did not click Claim, Log In, Create Account, or Submit. Crops are in [components/crops/](components/crops).
- **Screenshots.** [tools/capture/public/shoot.mjs](tools/capture/public/shoot.mjs) took viewport and full-page shots. [tools/capture/quantize.py](tools/capture/quantize.py) posterised them to 256 colours. Each shot has a `.capture.json` sidecar with the measured viewport. Phone full pages taller than one tile (`mobile-home`, `mobile-blog`, `mobile-sections`) were stitched. Their sidecars record the stitch.
- **Fonts.** `@font-face` names Google Sans Flex Variable, Fragment Mono, SeriouslyNostalgic Ital Regular, and Inter. Computed text on the marketing pages is Satoshi. The webfonts are not committed.

Nothing was sent, claimed, or signed into. The privacy form was not filled. Its email placeholder was painted out of the screenshots and the email crop, because the task forbids an email address in the package.

## What to distrust

- **One painted theme.** `prefers-color-scheme: dark` left the page white. The `dark` set is empty.
- **Framer token names are uuids.** `core.color` renames the declared values. The uuid and the source control are in `$extensions.source`.
- **The claim fill is a gradient.** `light.accent` is the flat end stop `#3b82f6`. The 110-degree gradient is under `light.$extensions.notTokenised`, not a colour token.
- **Focus is the browser outline.** Keyboard focus draws Chromium's `auto` outline `#005fcc`. It is not a declared token.
- **Several declared colours are unused on the captured controls.** `#478eff`, `#00276b`, `#ffed90`, `#e3e3e3`, `#dedede`, `#d2d2d7`, `#bdbdbd` and `#fdfdfd` are in the body rule and marked as not painted on a captured control.
- **The claim field has no CSS border.** The pill outline in the screenshot is not a `border` on the input or its parents. It was not tokenised.
- **Quantised screenshots.** `screenshots/` are 256-colour PNGs. Read colours from tokens or the raw JSON.
- **The privacy email placeholder was masked.** The field's placeholder text was painted over with the field fill. The crop no longer shows it.

## Fonts

Computed marketing text is **Satoshi** (nav, display, claim, footer). Articles, FAQ questions and the privacy form use **Inter**. **Fragment Mono** and **SeriouslyNostalgic Ital Regular** are declared and were not used by a captured control. **Google Sans Flex Variable** is declared. Licences were not captured. The guide uses the system sans.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Colour roles | captured | `light.page`, `light.surface`, `light.text`, `light.muted`, `light.accent`. Raised, overlay, scrim, success, warning, danger and info are not present on the public pages |
| Type | captured | `core.typography` display, body, label, button, caption, question, card-title, field |
| Spacing | partly | four measured paddings in `core.space`. No spacing scale |
| Radii, borders | partly | claim 26px, suffix 9999px, privacy submit 10px, checkbox 4px, Go home 16px. No designed border token |
| Elevation | not present | no box-shadow on the captured controls |
| Motion | not captured | durations were not read. Reduced motion was not tested |
| Sizing | captured | control height 40px, checkbox 16px, logo 24px |
| Layout | partly | 1440 and 390 widths captured. Breakpoints and z-index not captured |
| Button | captured | [claim-button-default](components/crops/claim-button-default.png), hover, focus-visible, pressed |
| Icon button | not present | the FAQ chevron is part of the question row |
| Link | captured | nav-link, nav-login, nav-create, footer-link |
| Text field | captured | claim-field, privacy-name, privacy-email. Not typed into |
| Text area, select, radio, switch | not present | none on the public pages |
| Checkbox | captured | privacy-checkbox, default only. Not toggled, because toggling is a form field |
| Tabs, menu, tooltip, dialog, toast | not present | none on the public pages |
| Card | captured | article-card |
| List row, table, avatar, badge | not present | none as components. Marketing mockups in screenshots are pictures, not the product's list UI |
| FAQ | captured | [home-light-faq](screenshots/home-light-faq.png) |
| States: default, hover, focus-visible | captured | nav, footer, claim, privacy submit |
| States: pressed | captured | CDP `:active` on nav-link, claim-suffix, claim-button. Claim was not clicked, because a click opens signup |
| States: disabled, loading, error, selected | not present | none on the captured pages |
| App shell | captured | [home-light-default](screenshots/home-light-default.png), [mobile-home-light-default](screenshots/mobile-home-light-default.png) |
| Form with a validation error | not captured | the privacy form was not submitted |
| Empty, loading | not present | marketing pages have no empty or loading state |
| Error page | captured | [notfound-light-default](screenshots/notfound-light-default.png), HTTP 404 |
| Destructive confirmation | not present | none on the public pages |
| Search and filtering | not present | none |
| Onboarding | not captured | behind https://app.pop.site/ |
| Signed-in editor | not captured | Log In is https://app.pop.site/?signin. Password was not submitted |
| Dark theme | not present | dark emulation left the page white |
| Phone width | captured | `mobile-*` shots, measured 390 x 844 at 2x |

## Do and don't

- **Do keep the page white and the type tight.** Display is 69px Satoshi at a 62.1px line height and -3.92px tracking. See [home-light-default](screenshots/home-light-default.png).
- **Do use one claim button.** It is a 110-degree gradient from `#00a8f5` to `#3b82f6`, 40px tall, radius 26px, white label. See [claim-button-default](components/crops/claim-button-default.png).
- **Do put the suffix in a quiet chip.** `.pop.site` is `#fafafc` text `#171717`, not a second accent. See [claim-suffix-default](components/crops/claim-suffix-default.png).
- **Do quiet the nav.** Links are 15px Satoshi 500, `#171717`, and go to `#6e6e73` on hover. No pills, no underline. See [nav-link-hover](components/crops/nav-link-hover.png).
- **Don't invent a dark theme.** The public site stays white under a dark colour scheme.
- **Don't style the editor from this package.** Signup and the editor are behind `app.pop.site` and were not captured.

## Rebuild

```bash
cd systems/pop
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/build_components_md.py
```

Screenshots:

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node tools/capture/public/shoot.mjs
python3 tools/capture/quantize.py ~/.design-systems/pop/raw-shots
```

`catalog.json` was not edited. `make design-md` and `make brief` only cover catalogued packages, so [DESIGN.md](DESIGN.md) was written for this package from the same mapping those commands use.
