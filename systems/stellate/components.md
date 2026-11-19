# Components

Public signed-out Stellate, measured on 2026-11-19 at a 1169 by 731 CSS viewport, devicePixelRatio 2. Screenshots were not saved. `preview_snapshot` returned "The browser is not producing screenshot frames." Values below are computed styles.

## Button

Marketing buttons are 40px tall, 8px radius, 15px / 550, padding 0 16px, TT Commons.

| State | Where | Values |
|---|---|---|
| Gray primary | Header "Get started for free" on https://stellate.co/ | background `#dbdfe7`, text `#283448`, height 40px, radius 8px, width 158px |
| Blue | "Learn more about Caching" and pricing "Contact us" | background `#608bd8`, text `#ffffff`, height 40px, radius 8px |
| Magenta | "Learn more about Metrics" | background `#ff6b8b`, text `#ffffff`, height 40px |
| Red | "Learn more about Security" and cookie "Reject All" | background `#ff7752`, text `#ffffff`, height 40px |
| Hero | Home "Get started" button | background `#608bd8`, text `#ffffff`, 18px / 550, padding 13px 15px, height 44px, radius 6px, width 120px |
| Neutral | Pricing "Get Started" | background `rgba(59, 76, 106, 0.1)`, text `#3b4c6a`, height 40px, radius 8px |
| Trial | Pricing "Start free trial" on the blue card | background `rgba(255, 255, 255, 0.9)`, text `#3e6ec1`, height 40px, radius 8px |
| Outline | Cookie "Customize" | transparent background, 1px border `rgba(59, 76, 106, 0.25)`, text `#3b4c6a`, height 40px, radius 8px |
| OAuth | "Login with GitHub" | background `#323a4d`, text `#ffffff`, 18px / 450, padding 12px 20px, height 51px, radius 6px, width 320px |
| OAuth | "Login with GitLab" | background `#9a70c2`, same size as GitHub |
| Email submit, empty | "Continue with Email" before an address | background `rgba(59, 76, 106, 0.1)`, text `#3b4c6a`, height 52px, radius 6px, disabled |
| Email submit, filled | Same button after kaichen@agentmail.to was typed | background `#608bd8`, text `#ffffff`, cursor pointer. The form was submitted and sent a magic link |

Hover, focus-visible, pressed and loading were not forced. Classes name `hover:bg-blue-110` (`#3e6ec1`), `hover:bg-magenta-110` (`#f3446a`), `hover:bg-red-110` (`#f85b30`), and `focus:ring-2`. Those states were not shown.

## Link

Nav "Pricing" is 15px / 550, `#3b4c6a`, height 27px, no radius. "Learn more" is the same type, inline. Footer links are 18px / 550 at opacity 0.6. Auth "Create your account" is 13px / 450, `rgba(59, 76, 106, 0.6)`, underlined. Docs links in dark are `#1aa3ff`. Docs links in light are `#006be6`, underlined.

## Text field

Login and signup share one email field. White background, blue text `#608bd8`, no border, radius 6px, height 48px, padding 14px 17px, 18px / 450, width 316px. Placeholder "Email Address". Focus outline computed as `none`. A visible focus ring was not shown. There is no password field on the public form.

The email was set to kaichen@agentmail.to and Continue with Email was clicked. The page went to https://stellate.co/login/submitted and said a magic link was sent. The magic link was not opened.

## Cookie banner

A fixed banner on login and signup: white background, 12px radius, 32px padding, 1px border `rgba(59, 76, 106, 0.15)`, shadow `shadow-big`, width 672px, height 216px. Accept All is the blue 40px button. Reject All is the red 40px button. Customize is the outline button. The banner uses Times for its button face in the computed font, which is the cookie widget, not TT Commons.

## Card

Pricing cards on https://stellate.co/pricing: Free is white, 344px wide, 348px tall, 32px padding, 12px radius, 1px border `rgba(59, 76, 106, 0.1)`. Business is `#608bd8`, 386px wide, 602px tall, 32px padding, 12px radius. Enterprise is `#3b4c6a`, 344px wide, 433px tall. An add-on card is white, 320px wide, 20px padding, 10px radius. Nav menus are white, 12px radius, 20px padding, `shadow-small`.

## Code

Docs quickstart `pre` is white, 6px radius, padding 16px 0, mono 14.4px, text `#314158`. A string span is `#b31d28`. A nested span is `#24292e`. Inline `code` is `oklab(0 0 0 / 0.03)` (canvas `#f7f7f7`), radius 5.4px, padding 1.728px 3.6px. The search kbd is 11px / 500, `#99a1af`, background `#18181b` in dark, radius 4px.

## Text area, select, checkbox, radio, switch, tabs, tooltip, dialog, toast, table, avatar, badge

Not present on the public pages that were opened. The cookie banner is the closest dialog. Docs search is a kbd, not a field that was typed into. Pricing FAQ headings are 29px / 550. Their answers were not expanded.

## Icon button

Not measured as its own component. Header and footer icons are inline SVG. They were not exported.
