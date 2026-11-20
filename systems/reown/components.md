# Components

Values are computed styles from the live signed-out pages on 2026-11-19. Crops are from a later headless Playwright pass of the public marketing page, which loaded without a Cloudflare challenge. The T3 preview snapshot returned "The browser is not producing screenshot frames", so the crops are not from that tab.

## Button

Marketing buttons use KHTeka Mono, weight 400, letter-spacing -0.8px at 16px, and 16px radius.

| Variant | Where | Fill | Text | Size |
|---|---|---|---|---|
| Primary | "Start building" on https://reown.com/ | `#379def` | `#202020` | 16px, padding 13px 15px, height 44px |
| Outline | "Explore Plans" | transparent, 1px `#ffffff` | `#ffffff` | 16px, height 44px |
| White | "Log in" | `#ffffff` | `#202020` | 22px, radius 14px, padding 11px 23px 13px, height 48px |
| Blue nav | "Learn", "Docs", "Demo" | `#379def` | `#202020` | 22px, radius 14px, height 48px |
| Black | "Download now" | `#202020` | `#ffffff` | 16px, radius 16px, height 44px |
| Grey | "Explore Payments" | `#dedede` | `#202020` | 16px, radius 16px |
| Text | footer "Dashboard" | none | `#202020` | 14px |

Crops: [button-primary-hero.png](components/crops/button-primary-hero.png), [button-outline-default.png](components/crops/button-outline-default.png), [button-login-default.png](components/crops/button-login-default.png).

Focus on "Start building" after `focus()` drew `outline: rgb(229, 151, 0) auto 1px` with offset 1px. Hover, pressed, disabled and loading were not shown. Stylesheet hover rules for `.button` did not set a background.

## Link

FAQ answer links are `#0988f0` and underlined. Blog body links are `#383838` and underlined. Docs active nav is `#008847` on a green oklab wash. Docs idle nav is `#9ea2a0` in dark.

## Text field

The newsletter field on the home footer is `#363636` fill, `#e9e9e9` text, KHTeka Mono 48px, radius 32px, height 96px, padding `0px 13px 0px 30px`. It was not submitted.

The sign-in email and password wraps at https://dashboard.reown.com/sign-in are `#252525`, 1px `#363636`, radius 16px, height 60px, width 400px. Placeholder text is white 16px KHTeka. The form was not submitted.

Text area, select, checkbox, radio and switch were not on the pages opened.

## Accordion

FAQ rows are `#202020`, radius 16px, height 60px closed and 103px open. The question is white 16px KHTeka. The open answer is `#6c6c6c` 16px. Opened by clicking "How do I implement Reown?".

## Card

Home content cards are `#202020`, `#379def`, `#f4624a`, `#18ac65` and `#e9e9e9`, radius 16px or 64px. The hero is `#202020` with radius 160px. Pricing plan cards are `#202020` with radius 32px, inside a `#0988f0` or `#18ac65` ring of radius 40px.

## Code block

Docs code on https://docs.reown.com/appkit/overview is `#0b0c0e`, text `#d4d4d4`, Paper Mono 14px, radius 16px, padding 14px 16px, border 1px at about 10% white.

## Tabs, menu, tooltip, dialog, toast, table, avatar, badge

Not present as product components on the public pages opened. The docs theme control is a menu with System, Light and Dark. The phone mock on the home hero is a marketing image, not a captured wallet modal. The cookie bar on the dashboard sign-in page is Termly chrome, not a Reown component.

## Gaps

- Wallet connect, transaction signing, and API key creation were not entered.
- The sign-in form at https://dashboard.reown.com/sign-in was measured and not submitted. No Google continue, no password, no signup.
- Button hover, pressed, disabled and loading were not shown.
- Checkbox, radio, switch, select, text area, toast, dialog, table, avatar and badge were not on the public pages.
- Preview screenshot frames failed. Crops are from headless Playwright of the public marketing page only.
