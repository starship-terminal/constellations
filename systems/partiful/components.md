# Components

Measured on the public signed-out pages on 2026-11-19. No crops: the preview browser did not produce screenshot frames.

## Button

Marketing controls are links. The painted face is an inner `div.framer-1g6fwu5`, not the anchor. Label is TWK Lausanne Pan 600, 16px / 19.2px, weight 600, padding 16px 24px, height 51px.

| State | Fill | Text | Radius | Where |
|---|---|---|---|---|
| Primary pill (Create an invite) | `#111111` | `#fdfdfb` | 200px | Home nav |
| Secondary pill (Log in) | `#fdfdfb` | `#000000` | 200px | Home nav |
| Hero solid (Create event) | `#fdfdfb` | `#000000` | 4px | Home hero |
| Hero ghost (Get the app) | `#111111` | `#fdfdfb` | 4px | Home hero, on the black hero |
| App outline (Get the app, Explore events) | `rgba(255, 255, 255, 0.05)` | `#ffffff` | 800px | Login. 1px `rgba(255, 255, 255, 0.4)` border. Heights 40px and 32px |
| App solid (Create a free event) | `#ffffff` | `#000000` | 800px | Login footer. 14px weight 600, height 32px, padding 0 12px |
| Hover, pressed, disabled, loading | Gap | Gap | Gap | Not painted. Preview snapshot could not force hover |

## Link

Marketing inline link (Learn more) is TWK Lausanne Pan 300, 19.2px / 23.04px, weight 300, letter-spacing -0.384px, `#111111`.

App inline link (Get the app under the phone field) is Lausanne 16px weight 600, `#9ccfff`, no underline.

App footer links (Help, Blog, Careers, About) are Lausanne 18px weight 600, `#ffffff`, no underline.

## Text field

Login phone field is `input[type=tel]`, placeholder "Phone number". The wrap is 400 by 52, fill `rgba(255, 255, 255, 0.05)`, 1px `rgba(255, 255, 255, 0.1)`, radius 4px. The input is 314 by 50, Lausanne 18px / 25.2px, weight 400, `#ffffff`, padding 1px 12px, no border of its own. The country button is 80 by 52, same fill and border, radius 4px, 18px. I did not type a number.

Programmatic focus did not paint an outline. Computed outline stayed `none 3px`.

## Icon button

Social marks on the login footer are 28 by 28 anchors with `aria-label` Instagram, X, and TikTok. No separate chrome was sampled.

## Card

Explore posters are about 181 by 181, radius 4px, shadow `rgba(0, 0, 0, 0.2) 0px 0px 8px 8px`. The phone demo on the home hero is 329 by 443, fill `rgba(255, 255, 255, 0.06)`, radius 16.4px. That demo is a public illustration, not a signed-in event.

## Tabs, menu, tooltip, dialog, toast, checkbox, radio, switch, select, text area

Not captured. Login has a country button and a language button (English). I did not open them. No cookie dialog was present.

## Gaps

Hover, pressed, disabled, loading, focus-visible, form error, empty, and toast were not painted. Create-event was not entered. Checkbox, radio, switch, select, and text area were not on the pages I opened.
