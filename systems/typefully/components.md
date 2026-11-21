# Typefully components

Public marketing controls, measured on 2026-11-21 from https://typefully.com/pricing and the homepage login dialog, signed out. Values are token names. The readings are in [raw/components-computed.json](raw/components-computed.json). Element crops were not cut; the states live in the page screenshots named below.

## Discovery list

| Page | What was on screen |
|---|---|
| `/` | Marketing dialog over a non-interactive product-shell illustration. Log in and Sign up open a second dialog. |
| `/pricing` | Header, plan cards, primary and secondary buttons, comparison disclosures, social-set menu, footer. |
| `/docs/api` | Scalar API reference: sidebar groups, method rows, search, token field (not filled). |
| `/tools/fake-tweet-generator` | Local composer, advanced options, focused textarea. Nothing typed, nothing submitted. |
| `/social-media-glossary` | Index, search field focused, one term page. |
| Auth dialog | Provider buttons and an email field. Providers not clicked. Field not submitted. |

## Shared values

| Role | Token | Measured |
|---|---|---|
| Page | `light.color.bg.page` | `#ffffff` (`--color-typ-bg0`) |
| Text | `light.color.text.primary` | `#000000` (`--color-typ-c1`) |
| Secondary text | `light.color.text.secondary` | `#354450` (`--color-typ-c2`) |
| Muted text | `light.color.text.muted` | `#5c6d7a` (`--color-typ-c3`) |
| Accent | `light.color.accent.default` | `#199af5` (`--color-typ-accent`) |
| Border | `light.color.border.default` | `#e6e8ea` |
| Field border | `light.color.border.subtle` | `#eef0f1` |
| Font | `core.fontFamily.inter` | Inter, then system UI |
| Motion | `core.motion.base` | 150ms, cubic-bezier(0.4, 0, 0.2, 1) |

## Components

### Header

Marketing pages, not the homepage modal. Logo, Pricing, Blog, Changelog, Jobs, Help, and a pill CTA. Phone 390 on pricing showed logo and CTA only. Jobs on phone showed a menu icon that was not opened.

Screenshot: [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png), [screenshots/mobile-pricing-light-default.png](screenshots/mobile-pricing-light-default.png).

| State | Values |
|---|---|
| Nav link, default | `core.typography.nav`, color `light.color.text.link`, padding `core.space.1` by 10px, radius about `core.radius.md` |
| Nav link, focus | Background a muted oklab wash at 0.1 alpha. Colour of that wash: Not captured as a hex. |
| CTA, default | Height 26px, padding `core.space.4`, radius `core.radius.pill`, background `light.color.accent.default`, text `light.color.text.onAccent`, Inter 13.5px / 600, transition `core.motion.fast` |

### Primary button

"Get started" on the Business plan. Height `core.size.button` (32px), padding left `core.space.3`, radius `core.radius.button` (9.6px), background `light.color.accent.default`, text `light.color.text.onAccent`, Inter 14px / 600 / 18.2px.

| State | What changed |
|---|---|
| Default | No shadow. |
| Hover | Background stayed `rgb(25, 154, 245)`. Distinct hover colour: Not captured. |
| Focus | Box-shadow: 1px white ring plus a 4px oklab accent ring at 0.2 alpha. The ring is not one colour token. |

Screenshot: [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png).

### Secondary button

"Get started" on the Free plan. Same height and padding. 1px border `rgb(230, 232, 234)`, radius 12px (`core.radius.card`), background white, text `light.color.text.secondary`, weight 500. Shadow: `rgba(0, 0, 0, 0.04) 0 1px 3px -1px` and `0 1px 4px -1px`.

### Auth button

Login dialog. Google, X, LinkedIn, and Email share one style. Height about 38px (`core.size.buttonAuth`), padding left `core.space.5`, hairline border, pill radius, white background, text `light.color.text.secondary`, Inter 15px / 500, transition `core.motion.slow`. Providers were not clicked.

Screenshot: [screenshots/home-light-login-dialog.png](screenshots/home-light-login-dialog.png).

### Text field

Shown after Email is clicked. Not submitted. 32px tall, padding 8px 12px, 1px border `rgb(238, 240, 241)`, radius 9.6px, white background, Inter 14px / 400 / 20px. A focus ring was already present when measured. Placeholder text is the product's sample, not a typed address.

Screenshot: [screenshots/home-light-login-email.png](screenshots/home-light-login-email.png).

### Menu

"1 social set" on pricing opens a short explanation menu. Comparison rows are `aria-expanded` disclosures. Phone comparison uses Free, Creator, and Business tabs. Those phone tabs are not a separate screenshot.

Screenshot: [screenshots/pricing-light-social-set-menu.png](screenshots/pricing-light-social-set-menu.png), [screenshots/pricing-light-comparison-open.png](screenshots/pricing-light-comparison-open.png).

### Dialog

Homepage is itself a full-viewport dialog with no Close. Log in and Sign up open a second dialog on `/`. Close dismisses the second dialog only.

### Docs chrome

Scalar sidebar, method badges, search control, and an API client panel. The token field was not filled. A separate search-overlay screenshot was not written.

Screenshot: [screenshots/docs-light-default.png](screenshots/docs-light-default.png).

## Gaps

| Missing | Why |
|---|---|
| Checkbox, radio, switch, toast, table, avatar, destructive confirm | Not on the public pages that were measured. |
| Disabled, pressed, and a distinct hover fill | Hover did not change the primary background. No disabled control was on screen. `light.color.text.disabled` is the `--color-typ-c4` name, not a measured disabled control. |
| Signed-in empty, loading, and error | Login wall. Stopped. |
| Element crops | Not cut. States are in the page screenshots. |
| Icons as SVG | Not extracted. `icons/` is absent. The site icon is [icon.png](icon.png). |
| Dark component set | A dark class changed no resolved CSS variable. No dark set was written. |
