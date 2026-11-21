# Flighty components

Public marketing site, signed out, 2026-11-21. Crops were not cut. The screenshots in [screenshots/](../screenshots/) are the evidence.

## Button

Two homepage variants, both labeled Give Flighty a try. White is a 44px pill, radius 40px, padding 12px 18px 12px 20px, fill #ffffff, 1px border rgba(0, 0, 0, 0.12). Black is the same size with fill #000000 and a white label. Label type is 17px weight 600. See [home-light-default.png](../screenshots/home-light-default.png).

Get the app is a smaller pill: height 32px, radius 999px, padding 0 9px 0 12px, label 15px weight 500. It opens the download dialog in [home-light-get-app.png](../screenshots/home-light-get-app.png).

Try it for free on /pricing is a 40px pill, radius 50px, fill #bf59f2. See [pricing-light-default.png](../screenshots/pricing-light-default.png).

Go back home on the 404 is a pill with fill rgba(255, 255, 255, 0.08). See [login-404-light-default.png](../screenshots/login-404-light-default.png).

Hover, focus-visible, pressed, disabled, and loading were not held.

## Link

Nav links are 15px weight 500, color rgba(0, 0, 0, 0.7), letter-spacing -0.15px. They are plain anchors. None opens a menu.

## Text field

Help Center shows a search pill. The visible field was not a measured input: the only input in the DOM was a hidden button. Focus was not captured. The search was not submitted. See [help-light-default.png](../screenshots/help-light-default.png).

Gift cards show Personal and Family radios. Neither was selected. The purchase form was not submitted. See [gift-cards-light-default.png](../screenshots/gift-cards-light-default.png).

## Text area, select, checkbox, switch

Not present on the pages that were opened.

## Tabs

Pricing shows Annual, Weekly, Lifetime, and Family as a segmented control. Annual is the painted selection. The others were not clicked, so selected, hover, and pressed are not captured. See [pricing-light-default.png](../screenshots/pricing-light-default.png).

## Menu

No desktop menu. Get the app opens a dialog, not a menu. The phone hamburger was not opened: a click on the navbar trigger left the homepage. See the gaps in [login-review.json](../login-review.json).

## Tooltip

Not present.

## Dialog

Get the app opens a fixed overlay on `/`. It shows a QR code and the line "or download on Mac", which links to the App Store. That link was not followed. Clicking the page behind the overlay closes it. See [home-light-get-app.png](../screenshots/home-light-get-app.png).

The cookie banner is a second fixed layer. Reject and Accept were not clicked. It is hidden in the marketing screenshots and visible on the airports page, which is why that frame is not in the package.

## Toast

Not present.

## Card

Pricing uses a Pro card beside a feature list. Gift cards are three tilted cards. Business inquiries is a white card with a mailto pill. See [pricing-light-default.png](../screenshots/pricing-light-default.png), [gift-cards-light-default.png](../screenshots/gift-cards-light-default.png), and [business-light-default.png](../screenshots/business-light-default.png).

## List row

Help Center lists questions as rows. None was expanded. See [help-light-default.png](../screenshots/help-light-default.png).

## Table

The airports disruption table was on screen. That frame is not committed: it is a live map with airport delay figures. The component is recorded as not captured.

## Avatar

The homepage hero includes a marketing avatar in a notification card. It is product artwork, not an account avatar.

## Badge

The promo bar is a full-width strip, sampled #12128c. Pricing has a "Most popular plan" pill. Neither is a status badge component.

## Gaps

- No hover, focus-visible, pressed, disabled, or loading state was held.
- The phone menu was not opened.
- The help search field's computed style was not read from the visible input.
- The airports table was seen and not committed.
