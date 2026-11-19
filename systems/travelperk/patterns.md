# Patterns

Public pages on perk.com. travelperk.com redirected there. No screenshots: the preview browser returned "The browser is not producing screenshot frames".

## Shell

The header is fixed, full width. At the 1169 homepage read it was 66px and `rgb(245, 245, 235)`, shadow none. At 1440 on `/platform/` it was 80px and transparent. At 390 on `/platform/` it was 66px and off-white again. Nav labels are 16/24 OTSono. Actions in the bar are Book a demo, Get started, and Log in.

## Hero

The homepage h1 is "Automate travel, expenses, and policies in one platform", 80/72, weight 500, tracking -2.4px, colour `rgb(20, 20, 15)`, width 1073 at innerWidth 1169. The primary action is the lime pill. The second action is an outlined pill. Body copy under the hero is 18/24 `rgb(110, 110, 100)`.

On `/platform/` at 1440 the h1 is 60/60. At 390 the same heading is 36/38, width 324, and the lime button grows to 48px.

## Pricing

`/pricing/` redirects to `?tab=Travel+and+Spend&region=nam`. The h1 "Pick your plan" matches the homepage display size, with 80px top padding. Two plan cards were visible: Premium at `$6 /month` and Pro at `$8 /month`, both 60px OTSono. Cards are off-white, 28px radius, 32px padding. Starter and a `$99 /month` price were in the DOM at height 0.

Region tabs (North America, Europe) and product tabs (Travel and Spend, Travel, Spend) sit in a sticky tab list. Selected state was an attribute, not a filled chip.

## Footer

The footer computed a transparent background and black text. A dark band utility `.bg-brand-dark` exists. The only off-black element found in that search was a mobile submenu at height 0. A painted dark footer was not confirmed.

## Sign-in boundary

Log in goes to `https://app.perk.com/login`. The page is white, 384px form, Perk Sans. Title "Sign in" is 20/24 at the wide read and 18px at 390. The email field was left empty. An error line was already visible in `#d20f46`. SSO, Google, and the Yokoy link were not opened. Signup was not opened.
