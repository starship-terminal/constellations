# Components

Measured on the public signed-out Peerlist pages on 18 November 2026. Values are computed styles. Crops are missing because the preview browser returned "The browser is not producing screenshot frames".

| Component | Where | Measured |
|---|---|---|
| Button, primary | Home nav, Create Profile | 32px tall, 6px 16px padding, 12px radius, rgb(0 170 69) fill, 1px rgb(30 135 75) border, white 14px/600 Geist, shadow-10, 75ms ease-in |
| Button, secondary | Home nav, Log in | Same size, white fill, 1px rgb(226 232 240) border, rgb(13 13 13) text, shadow-5 |
| Button, dark | Login and signup submit | 40px tall, 8px 24px padding, 16px radius, rgb(15 23 42) fill, 1px rgb(13 13 13) border, white 16px/600 |
| Button, Google | Login and signup | 40px tall, 16px radius, white fill, gray-200 border, Roboto 16px/600 |
| Link, nav | Home header | 14px/500, 6px 8px padding, 24px radius, 200ms standard easing |
| Link, muted | Forgot password, Create One | 14px or 12px, weight 600, rgb(100 116 139) |
| Text field | Login email and password | 32px tall, 6px 8px padding, 8px radius, white fill, 1px rgb(203 213 225) border, 14px Geist |
| Username field | Home | 58px tall, 16px radius, 12px 12px 12px 20px padding, max-width 446px, 20px input |
| Search field | /search | Shell 16px radius, 1px gray-200, input 14px |
| Checkbox | /search filters | 16px, 4px radius, rgb(241 245 249) fill, 1px rgb(203 213 225) border. Unchecked only |
| Card | Auth panel | max-width 380px, 24px padding, 16px radius, 1px gray-200 border |
| List row | /jobs | 72px tall, 16px 24px padding, 640px wide at 1440 |
| Post | /scroll | White, 16px 24px padding, bottom border |
| Project card | /scroll embed and launchpad | 16px radius, 1px gray-200 border on the embed |
| Avatar | Home face row | 40px circle, gray-400 fallback fill |
| Pill | Ads announcement | 36px tall, full radius, gray-900 fill |
| Header | Every page | 56px sticky bar, 6px backdrop blur |

## Gaps

- Hover, focus-visible, pressed, disabled, loading, and error were not forced. Focus is declared as `--shadow-focus` (`0 0 0 4px #e1e4e880`) and `.focus-within:border-gray-1k`.
- No select, radio, switch, tabs-as-a-control, menu, tooltip, dialog, toast, table, or textarea was on these pages.
- No crops. Screenshot frames failed.
