# Components

Values are token paths. Take the numbers from [tokens.json](tokens.json). Crops are cut from the 256-colour screenshots, so they show layout and state, not exact colour.

## Header

The shared header is 72 px tall in the older home rule and paints a 1 px bottom line. The live controls sit inside it at 32 px tall, 8 px radius, 13 px Inter.

| Control | Tokens | Shot |
|---|---|---|
| Products, Resources | `dark.component.nav-fg`, `dark.component.nav-height`, `core.typography.nav` | [screenshots/home-dark-products-menu.png](screenshots/home-dark-products-menu.png) |
| Open MWM Console | `dark.component.button-secondary-bg`, `dark.component.button-secondary-fg` | [screenshots/home-dark-default.png](screenshots/home-dark-default.png) |
| Build your app | `dark.component.button-primary-bg`, `dark.component.button-primary-fg`, `dark.component.button-primary-radius` | same |
| Phone drawer | Observed. Opens from "Open navigation". | [screenshots/mobile-home-dark-nav-open.png](screenshots/mobile-home-dark-nav-open.png) |

Hover and pressed styles of these controls are not captured. `CSS.forcePseudoState` could not address the nodes, and the public sheets declare no `:hover` rule for them.

## Composer

The home prompt is a panel under the display heading. The textarea measured 16 px Inter, 48 px tall, transparent background. The Agent chip measured 40 px tall, 8 px radius, fill `rgba(255, 255, 255, 0.05)`.

| Control | State | Evidence |
|---|---|---|
| Textarea | default, focused | [screenshots/home-dark-prompt-focused.png](screenshots/home-dark-prompt-focused.png). Focus did not change the textarea's computed colour, radius, or outline. |
| Agent menu | open | [screenshots/home-dark-agent-menu.png](screenshots/home-dark-agent-menu.png). The lower options clip at the 900 px viewport. |
| Platform menu | open | [screenshots/home-dark-platform-menu.png](screenshots/home-dark-platform-menu.png) |
| Model menu | open | [screenshots/home-dark-model-menu.png](screenshots/home-dark-model-menu.png). Later models clip. |
| Send | disabled | Observed. Declared fill `#fff3` until a prompt exists. The prompt was not typed, so the ready and hover states were not captured. |
| Attachment, voice | present | Not used. |

Declared composer focus ring: `core.shadow.composer-focus` (`0 0 0 2px #ffffff2e`) on icon buttons, menu options, send, and tool pills. Not measured via a forced pseudo-state.

## Buttons elsewhere

| Control | Measured | Shot |
|---|---|---|
| Get MWM AI Pro | white fill, black label, 44 px, 8 px radius | [screenshots/pricing-dark-default.png](screenshots/pricing-dark-default.png) |
| Submit Dispute, empty form | fill `#2a2a2a`, label `#616161`, 48 px | [screenshots/ip-dispute-dark-default.png](screenshots/ip-dispute-dark-default.png) |
| FAQ trigger | 14 px Inter, transparent. Open and closed computed styles matched on the trigger itself. | [screenshots/pricing-dark-faq-open.png](screenshots/pricing-dark-faq-open.png) |

The pricing and console CTAs navigate to login walls. Those walls were not entered and are not screenshotted.

## Fields

The IP dispute form was left empty.

| Control | Default | Focused |
|---|---|---|
| Text field | fill `#141414`, border `#1a1a1a`, 8 px radius, 12.25 px Inter, padding 10 px by 16 px | fill `#1c1c1c`, border `#3a3a3a` |
| Textarea | same fill and border, taller | not separately measured |
| Select | same fill, border, and type | not opened |
| Checkbox | 18 px, fill `#141414` | not toggled |

Shot: [screenshots/ip-dispute-dark-field-focused.png](screenshots/ip-dispute-dark-field-focused.png).

## Cards and filters

The glossary category card measured fill `#181818`, radius 16 px, padding 18 px. After the ASO card was clicked, fill became `#1d1d1d` and the box shadow became an inset 1 px ring of `rgba(255, 83, 1, 0.32)`, which matches `--mwm-orange-data-border-strong`.

Shot: [screenshots/glossary-dark-filter-aso.png](screenshots/glossary-dark-filter-aso.png).

Directory search measured fill `#0c0c0c`, height 48 px, radius 8 px.

## Type

| Style | Size | Weight | Line height | Tracking | Where |
|---|---|---|---|---|---|
| Display | 72 px | 600 | 76 px | -2.88 px | Home h1, white. Pricing h1 is `#f7f8f8`. |
| Lede | 16 px | 400 | 24 px | -0.32 px | Home paragraph, white at 70%. |
| Nav | 13 px | 400 | 16 px | -0.26 px | Products button. |
| Button | 13 px | 600 | 16 px | -0.26 px | Header CTAs. |
| Chip | 14 px | 500 | 16 px | -0.07 px | Agent chip. |
| Field | 12.25 px | 400 | 18.375 px | 0 | IP form. |

All of these computed to Inter. The declared display stack names Modern Gothic first. That face was not loaded.

## Gaps

- Header button hover, focus-visible, and active: not captured.
- Pricing CTA hover and active: not captured.
- Submit Dispute hover, and the enabled submit after a valid form: not captured. The form was not filled.
- Light theme: not present.
- Signed-in Console and Create App: login walls, not entered.
- Radio, switch, tooltip, toast, dialog: not present on the captured public pages.
- Agent details were opened for one agent (Theo). Mira and Cody use the same panel. Coming-soon agents do not open.
- One FAQ item was opened on pricing, MWM AI, Console, Publishing, the ASO tool, the glossary term, and the ranking chart. The other items were not each expanded.
- Guide "On this page" is a phone control. Desktop click found a 0-size summary. Phone shot: [screenshots/mobile-guide-dark-on-this-page.png](screenshots/mobile-guide-dark-on-this-page.png).
- Phone coverage is a subset: home (default, full, nav open), pricing (default, full), MWM AI, Console, Studio, articles, apps, glossary, rankings, and the guide contents. Other pages are desktop only.
- Locale mirrors, careers, and external product sites: not captured.
