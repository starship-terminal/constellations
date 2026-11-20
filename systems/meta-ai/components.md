# Meta AI components

Measured on the signed-out product page at `https://www.meta.ai/` and the signed-out auth card at `auth.meta.com` on 2026-11-19. Desktop readings use innerWidth 1440 and innerHeight 900. Phone readings use innerWidth 390 and innerHeight 844. Device pixel ratio was 2 in both. Nothing was typed into a field and nothing was submitted.

Crops are absent. The preview browser returned page text and computed styles, and `preview_snapshot` failed four times with "The browser is not producing screenshot frames." Headless Playwright was not launched: a plain request to `https://www.meta.ai/` returned HTTP 403.

## Button

Header `Log in`: 67 by 36 px, padding `0 14px`, transparent background, white text, 14 px medium, radius 9999 px.

Header `Download app`: 121 by 36 px, same type, background `rgba(255, 255, 255, 0.12)`.

Section `Edit a photo`: 106 by 36 px, transparent, white, 14 px weight 500, radius 9999 px. Hover did not change background, colour, or transform. Focus set outline colour `#1793ff`, outline style `none`, width 2 px, offset 2 px. No ring was painted.

`Learn more`: height 40 px, padding `0 12px 0 14px`, background `rgba(56, 56, 56, 0.8)`, radius 9999 px, backdrop-filter `blur(36px)`.

Icon buttons (`Open sidebar`, `Add attachment`, `Send`, `Settings`): 32 by 32 px. `Open sidebar` uses radius 12 px and page background `#181819`. `Send` is disabled at rest, opacity 0.5.

Sidebar `Sign up`: 72 by 32 px, background `rgba(255, 255, 255, 0.12)`, radius 9999 px, padding `0 12px`, 14 px.

## Text field

Composer input, accessible name "Ask Meta AI": width 728 px at 1440, height 27 px, 18 px / 27 px optimisticAI, white text, transparent background. Placeholder colour `rgba(241, 246, 255, 0.38)`, which matches `--text-tertiary` `#f1f6ff61`.

The shell around it is 768 by 107 px, background `rgba(56, 56, 56, 0.8)`, radius 32 px, padding `0 12px 12px`. That 768 px is `--container-conversation` (48 rem).

Auth field on `auth.meta.com`: label "Mobile number or email address", box 560 by 60 px, radius 16 px, border `1px solid rgb(104, 106, 110)`, padding `10px 16px`. Input text is 15 px weight 500, colour `rgb(17, 17, 18)`. Label colour `rgb(104, 106, 110)`. The field was focused and left empty.

## Link

Footer `Muse` and `AI Learning Hub`: colour `rgba(242, 247, 255, 0.53)`, 16 px weight 600, no underline. They point at `https://muse.ai/` and `https://meta.ai/learn/`.

Auth footer links (`Privacy`, `Cookie Policy`, `Terms`): 13 px weight 700, colour `rgb(104, 106, 110)`, family Optimistic.

## Sidebar

Collapsed width 56 px, expanded width 256 px, height 900 px, background `#181819`. Expanding is a click on the button labelled "Open sidebar". Rows `New chat` and `Vibes` are 232 by 32 px, radius 12 px, padding `6px 12px 6px 4px`, 14 px white.

The settings control has `aria-haspopup="menu"` and `aria-expanded="false"`. A click and a hover did not open a menu in this session, so menu items were not measured.

## Hero and section title

Desktop h1: 48 px, computed line-height 51.84 px (token `--text-lg-title-1--line-height` is 52 px), weight 400, white, width 720 px. Class `text-lg-title-1`.

Phone h1 at 390 px: 28.08 px, line-height 30.33 px, width 342 px. Same weight and colour.

Section h2 "Edit photos with ease": 30 px / 34 px, weight 400, white. Class `text-title-1`.

## Chat bubble

Demo bubble in the photo section: "Change the background to a neutral blue", 277 by 44 px, background `rgba(255, 255, 255, 0.12)`, radius 22 px, padding `10px 16px`, 16 px / 24 px white. This is published marketing copy on the public page, not a signed-in thread.

## Auth card

Host `auth.meta.com`. Page background `#ffffff`. Heading "Log in or create an account" is 17 px weight 600, colour `rgb(17, 17, 18)`, family Optimistic.

`Continue with Facebook` and `Continue with Instagram`: 560 by 54 px, white face, border `1px solid rgb(224, 226, 228)`, radius 16 px.

The email step heading is 24 px / 28 px, weight 600, colour `rgb(17, 17, 18)`. Continue was not pressed. The flow also offers a mobile number, which this capture did not use.

## Shared values

| Role | Value | Where |
|---|---|---|
| Page | `#181819` | body, sidebar, `--background-primary` |
| Raised | `#28292b` | `--fill-primary`, `--color-fill-primary` |
| Elevated fill | `#ffffff1f` | Download app, Sign up, demo bubble |
| Text | `#ffffff` | headings, buttons, composer |
| Muted | `#f2f7ff87` | footer links, `--text-secondary` |
| Link and focus colour | `#1793ff` | `--accent-dark`, `--text-primary-link` |
| Declared accent | `#0064d4` | `--accent`, not the painted focus colour |
| Pill radius | `9999px` | header and section buttons |
| Composer radius | `32px` | composer shell |
| Fast motion | `150ms` cubic-bezier(0.4, 0, 0.2, 1) | button transition |

## Gaps

- No crops. Screenshot capture failed. See the README coverage table.
- No hover colour change was observed on the section button. Pressed, loading, error, and disabled states of text buttons were not shown, except Send, which is disabled until the composer has text.
- Checkbox, radio, switch, tabs, select, tooltip, toast, table, avatar, and badge were not on the signed-out page.
- The settings menu did not open.
- Signed-in chat, history, and settings were not entered. Auth stopped at the empty email field because the next step asks for a mobile number or an email submission.
- `--btn-primary-bg` (a blue-to-indigo gradient) and `--btn-destructive-bg` are declared and were not painted on these pages.
- Light theme of the product page was not found. `html` carried the class `dark` and there was no theme toggle on the signed-out surface. The light values in `tokens.json` are the auth card only.
