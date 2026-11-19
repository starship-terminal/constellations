# Vercel components

Measured on 2026-11-19 from a T3 preview tab at CSS viewport 1169 by 731, devicePixelRatio 2. Pages: https://vercel.com/, https://vercel.com/login, https://vercel.com/pricing, https://vercel.com/geist/button, and https://vercel.com/docs. No screenshot frames were produced, so there are no crops.

## Button

Header "Sign Up" on https://vercel.com/ is an anchor. Background `rgb(237, 237, 237)`, text `rgb(10, 10, 10)`, height 32px, padding `0 6px`, radius 6px, font GeistSans 14px weight 500, line-height 21px, shadow none.

Header "Log In" and "Get a Demo" use background `rgb(10, 10, 10)`, text `rgb(237, 237, 237)`, the same 32px height and 6px radius, and a 1px ring `rgb(46, 46, 46)`.

Hero "Deploy now" is the light face at 40px height, padding `0 12px`, 16px type, and a pill radius (`1.67772e+07px`). "Talk to sales" is the dark ringed face at the same size.

Login "Continue with Email" is a button, 40px height, padding `0 14px`, radius 8px, background `rgb(237, 237, 237)`, text `rgb(10, 10, 10)`. "Continue with Google", GitHub, ChatGPT, SAML SSO, and Passkey share the dark face, 8px radius, and the `rgb(46, 46, 46)` ring.

Geist docs at https://vercel.com/geist/button show three sizes of "Upload": 32px (padding `0 6px`, radius 6px), 36px (padding `0 10px`, radius 6px), and 40px (padding `0 14px`, radius 8px). Default is the light face. Error is `oklch(0.5801 0.227 25.12)` with white text, canvas sRGB `#e2162a`. Warning is `oklch(0.7721 0.1991 64.28)` with `rgb(10, 10, 10)` text, canvas sRGB `#ff9300`. Secondary is the dark ringed face. Tertiary is transparent with `rgb(237, 237, 237)` text.

Disabled and loading "Upload" on that page compute background `rgb(26, 26, 26)`, text `rgb(143, 143, 143)`, opacity 1, cursor `not-allowed`. Hover, focus-visible, and pressed were not shown.

## Link

Login "Sign Up" under the form is `oklch(0.717 0.1648 250.794)`, canvas sRGB `#47a8ff`, 16px, weight 400. Footer "Terms" and "Privacy Policy" are `rgb(135, 135, 135)` at 12px. Skip-to-content uses the same link colour.

## Text field

Login email input is `input[name=email]`, placeholder "Email Address", 320 by 40 CSS pixels, background `rgb(10, 10, 10)`, color `rgb(255, 255, 255)`, 16px weight 400. The input itself has radius 0. The wrap has radius 8px and a 1px shadow `rgba(255, 255, 255, 0.14)`. The wrap class includes `duration-150`. The field was not filled and the form was not submitted. Focus, error, and disabled field states were not shown.

## Text area, select, checkbox, radio, switch

Not present on the public pages that were opened. Geist lists Checkbox in its nav. That page was not opened, so those controls are not captured.

## Tabs, menu, tooltip, dialog, toast

Not opened. Login "Show other options" is a button and was not clicked. Docs search is a button labelled "Search Docs", 264 by 36, radius 6px, 14px, color `rgb(161, 161, 161)`. The search dialog was not opened.

## Card

Pricing plan columns on https://vercel.com/pricing were not given a separate card measurement. Plan actions were measured: "Start deploying" is a dark pill, 36px, 14px weight 500. "Start a free trial" and "Start a free Pro trial" are light pills at the same size. "Contact Sales" is a dark pill. Those links were not followed. "Popular" on the Pro plan was visible in the page text. Its box was not isolated.

## Table, list row, avatar, badge

Pricing comparison text is on the page. Individual table cells were not measured. No avatar or badge component was isolated. Geist lists Avatar and Badge. Those pages were not opened.

## Code

Docs `pre` on https://vercel.com/docs computes Geist Mono at 16px, background `rgb(10, 10, 10)`, color `rgb(237, 237, 237)`, bottom radius 8px. A code sample on https://vercel.com/geist/button computes Geist Mono at 13.7143px, background `rgb(26, 26, 26)`, color `rgb(161, 161, 161)`.

## Gaps

- Hover, focus-visible, and pressed were not shown.
- The login email field was not filled. Signup was not submitted.
- Google, GitHub, ChatGPT, SAML SSO, and Passkey were not followed.
- No card, paid team, or org SSO was entered.
- No screenshots or crops. `preview_snapshot` returned "The browser is not producing screenshot frames".
