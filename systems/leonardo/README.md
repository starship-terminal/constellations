# Leonardo.Ai design reference

A token set and component reference for the public marketing site of Leonardo.Ai, the generative image and video platform. Captured on 2026-11-21 from https://leonardo.ai/, signed out, in headless Chromium at 1440×900 and 390×844. One theme: the site paints black. No theme toggle was found on the public pages.

The site is worth a capture because the marketing system is unusually graphic. A black page, one violet (`#6e60ee`) used as poster type and as the subscribe pill, white pills for Log in and Start now, and plan names in yellow, green and red. UI text is Canva Sans. Headlines are Ufficio Display. The giant hero words are Leo Sans.

Boundary: the product itself is behind login. https://leonardo.ai/login is a 404 ("This page is not found"). https://app.leonardo.ai/auth/login asks for email and password, or Canva, Apple, Google, or Microsoft. That branch was stopped. No form was submitted. No account was created.

The control map is [site-tree.md](site-tree.md).

| File | What it is |
|---|---|
| [site-tree.md](site-tree.md) | Which header, footer and in-page control opens which page, menu or auth wall |
| [icon.png](icon.png) | Site icon, 128 px, from https://leonardo.ai/images/leonardo_favicon.png |
| [tokens.json](tokens.json) | DTCG tokens: `core` and `dark`. No light set. Every token has `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Generated export. One theme, no provenance. Take values from tokens.json |
| [style-guide.html](style-guide.html) | Renders the measured colours, pills, tabs and plan names |
| [components.md](components.md) | Checklist components, with crops where a control was measured |
| [patterns.md](patterns.md) | Shell, hero, pricing, contact, news, 404 |
| [components/crops/](components/crops) | 26 element crops |
| [icons/](icons) | Index only. Brand SVGs were not extracted |
| [screenshots/](screenshots) | 31 captures, desktop 1440×900 and phone 390×844 at 2x, quantised to 256 colours |
| [raw/](raw) | Logged computed styles and the `:root` custom properties read on the first probe |
| [tools/](tools) | Capture scripts and `build_tokens.py` |

## Brief

<!-- brief:start -->
Read this before designing in this style. Take every value from [tokens.json](tokens.json). The screenshots are 256-colour and are not measurements.

### Principles

1. Do paint the page black and spend violet on the poster type.
2. Do use a white pill for the account action and a violet pill for subscribe.
3. Do keep menus in a near-black panel, not a light sheet.
4. Do colour plan names (yellow, green, red) and leave prices light grey.
5. Don't treat the shadcn `:root` variables as the brand palette.
6. Don't style the signed-in generator from this package.

Each rule links a screenshot under [Do and don't](#do-and-dont).

### Using tokens

| Role | dark |
|---|---|
| page | #000000 `dark.page` |
| surface | #111111 `dark.surface` |
| text | #ffffff `dark.text` |
| muted | #ededed `dark.muted` |
| accent | #6e60ee `dark.accent` |
| border | rgba(255, 255, 255, 0.16) `dark.border` |

Fonts: `core.font.sans` is canvaSans; `core.font.display` is ufficioDisplay; `core.font.poster` is leoSans. All three are proprietary. The style guide uses the system sans.

### Using components

Read [components.md](components.md) and [patterns.md](patterns.md). 26 crops in [components/crops/](components/crops). [style-guide.html](style-guide.html) renders the tokens.

### Accessibility

White on black is the body pair. Violet `#6e60ee` on black is the poster pair. White text on the violet subscribe pill was measured. A full contrast table was not generated because this package is not in catalog.json.

<!-- brief:end -->

## Health

<!-- health:start -->
Not graded. This capture was asked not to edit catalog.json, so `make grade` was not run for this package. A catalog entry would be rejected on this PR.

<!-- health:end -->

## How the values were read

Headless Playwright opened https://leonardo.ai/ and the public pages linked from the header, footer and home body. Desktop viewport 1440×900 at 1x. Phone viewport 390×844 at 2x. The measured inner sizes matched those requests.

Computed styles were read on the live elements: Log in, Start now, Tutorial, pricing tabs, billing toggle, Subscribe, the price, the headline. Violet `#6e60ee` is `rgb(110, 96, 238)` on the selected pricing tab and the Subscribe button, and the same flat fill in the hero poster and the 404, sampled from the raw PNG before quantise. Menu `#111111`, contact green `#03e65b`, plan yellow `#f8c030` and plan red `#f85848` were sampled from raw screenshots before quantise.

`:root` custom properties were read from the homepage CSSOM on the first probe. They are a shadcn set (`--background: #000`, `--primary: oklch(20.5% 0 0)`, light card and popover). The painted brand violet is not one of those variables. Tokens use the painted values and say so.

Cookie overlays were hidden, not clicked. No form was submitted. Auth links were not followed past recording the URL.

## What to distrust

- **shadcn variables are not the brand.** `--primary`, `--card` and `--accent` on `:root` are light-theme defaults. The page paints black and violet. Do not copy those oklch values as Leonardo's accent.
- **Pill radius.** Computed `border-radius` on the pills came back as about 3.3e7 px. The token records `9999px` as Derived from that expansion.
- **Hover often matches default.** Log in, Subscribe and the idle tab did not change computed fill on hover. No hover colour was invented.
- **Border token is Observed.** The hairline on plan cards was not isolated as a computed style. `dark.border` is a visible white alpha, labelled in the token source.
- **Contact fields.** A later pass hit a Turnstile widget. Field metrics are Not captured. The screenshot shows the fields.
- **Fonts are proprietary.** Canva Sans, Ufficio Display and Leo Sans (Leo Renaisans in the preload) are not in this package.
- **Screenshots are 256-colour.** Read colours from tokens.json.
- **Full-page shots are capped at 7200 px.** Home, API and the image generator are taller. The cap is recorded in the capture log.
- **css-vars.json is a partial harvest.** The full stylesheet dump did not finish writing. The `:root` names in that file are from the first probe, not a complete sheet walk.

## Fonts

- **Canva Sans** (Regular, Medium, Bold) is the UI face. Proprietary. Not redistributed. Tokens name it; the style guide falls back to the system sans.
- **Ufficio Display** is the headline face (h1, 34.425 px, weight 500, uppercase, tight tracking). Proprietary.
- **Leo Sans** (preloaded as Leo Renaisans Bold) is the giant violet poster, 76 px, weight 900. Proprietary.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Page, surface, text, muted, accent | captured | `dark.page`, `dark.surface`, `dark.text`, `dark.muted`, `dark.accent` |
| Raised, overlay, scrim | not present | No overlay token on the public pages. The menu is a surface panel |
| Text secondary | captured | billing toggle at 70% white, `core.color.text-secondary` |
| Text disabled, on-accent, link | partly | On-accent is white on the violet pill. Disabled and a separate link colour were not isolated |
| Border default, strong, focus | not captured | Hairline observed only. Focus ring did not paint on the controls that were focused |
| Accent hover, pressed | not captured | Computed fill did not change |
| Success, warning, danger, info | partly | Plan yellow, green and red are labels, not a status system. No info colour |
| Light theme | not present | Public site is black only |
| Type families | captured | canvaSans, ufficioDisplay, leoSans |
| Type scale, line heights, named roles | partly | Five measured sizes. No caption or code role on the pages shot |
| Spacing scale | not captured | No spacing custom properties were isolated |
| Radii | captured | Pill, and 0 on the headline |
| Elevation | not present | Flat page. Menu is a fill, not a shadow |
| Motion | not captured | Durations were not isolated |
| Control heights | captured | Login 35 px, subscribe 48 px, tab 61 px |
| Breakpoints | captured as widths | 1440 and 390. No token for the breakpoint itself |
| Button | captured | [components.md](components.md), login and subscribe crops |
| Icon button | observed | Phone menu mark in [mobile-home-dark-menu.png](screenshots/mobile-home-dark-menu.png). No crop |
| Link | captured | Nav and menu crops |
| Text field, text area | observed | [contact-dark-default.png](screenshots/contact-dark-default.png). Metrics Not captured |
| Select | not captured | Enterprise form not opened |
| Checkbox, radio, switch | not present | |
| Tabs | captured | Pricing SOLO / TEAM / API |
| Menu | captured | Desktop Create menu and phone drawer |
| Tooltip, dialog, toast | not present | |
| Card | captured | Pricing cards in [pricing-dark-default.png](screenshots/pricing-dark-default.png) |
| List row | observed | Phone drawer rows |
| Table | not present | |
| Avatar | not present | Marketing photos are not an account avatar |
| Badge | observed | Best Offer and the green billing badge. Metrics Not captured |
| App shell | captured | Header and phone drawer |
| Form with validation error | not captured | Forms were not submitted |
| Empty, loading, error | partly | 404 captured. Empty and loading are behind login |
| Destructive confirmation | not present | |
| Search | observed | Learn has a search field. Not submitted. Metrics Not captured |
| Onboarding | not captured | Behind login. Not filled |
| Desktop 1440 and phone 390 | captured | Sidecars in the scratch folder recorded innerWidth 1440 and 390 |

## Do and don't

- **Do paint the page black and spend violet on the poster type.** The hero and the 404 are black fields of `#6e60ee` lettering. See [home-dark-default.png](screenshots/home-dark-default.png).
- **Do use a white pill for the account action and a violet pill for subscribe.** Log in is white. Subscribe is `#6e60ee`. See [pricing-dark-default.png](screenshots/pricing-dark-default.png).
- **Do keep menus in a near-black panel, not a light sheet.** The Create menu is `#111111` over the violet poster. See [home-dark-create-menu.png](screenshots/home-dark-create-menu.png).
- **Do colour plan names and leave prices light grey.** Essential is yellow, Premium green, Ultimate red. Prices are `#ededed`. See [pricing-dark-default.png](screenshots/pricing-dark-default.png).
- **Don't treat the shadcn `:root` variables as the brand palette.** `--primary` on `:root` is a dark grey oklch, not the violet. See [raw/css-vars.json](raw/css-vars.json).
- **Don't style the signed-in generator from this package.** Login stops at https://app.leonardo.ai/auth/login. See [not-found-dark-default.png](screenshots/not-found-dark-default.png) for the public 404 at /login.

## Rebuild

```bash
python3 systems/leonardo/tools/build_tokens.py
```

Screenshots were quantised from `~/.design-systems/leonardo/raw-shots` after the Playwright run. Re-capture with:

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node systems/leonardo/tools/capture/run.mjs
```

`catalog.json` was not edited. `make design-md` and `make grade` need a catalog entry, so DESIGN.md in this package was written to match the generator's shape without registering the package.
