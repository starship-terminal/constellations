# Patterns

Public pages opened on 19 November 2026, signed out. No vehicle was configured, no card was entered, and no account was created.

## Home

[https://www.tesla.com/](https://www.tesla.com/) is a stack of full-bleed product bands. Each band is a photograph with a display title, a promo link, and a pair of buttons: Order Now and Learn More. The header is 56px and transparent over the first band. A sticky bar offers "Schedule a Drive Today". The footer is a single row of legal links.

A location card ("Confirm Your Location", United States / Singapore) and a cookie banner sit on first load. Both were dismissed. Reject was used for cookies.

## Product page

[https://www.tesla.com/modely](https://www.tesla.com/modely) repeats the band pattern. The title is "Model Y Premium" at 48px display, weight 500, white. Order Now links to `/modely/design`. That configurator was not opened.

[https://www.tesla.com/solarpanels](https://www.tesla.com/solarpanels) uses the same pair, with "Schedule a Consultation" as the second button. The title is 56px / 64px.

## Support

[https://www.tesla.com/support](https://www.tesla.com/support) is a light page. The title "Tesla Support" is 40px / 48px, #171a20. Under it is one search field, placeholder "Search Support". A search was not submitted.

## About

[https://www.tesla.com/about](https://www.tesla.com/about) opens with "About Us" at 40px display, white, over a dark band.

## Menu

The header Menu control opens a full-window white dialog. Rows are 56px and 17px. Shop leaves the site for shop.tesla.com. That shop was not opened.

## Widths

The attached preview measured 1169 by 731 CSS pixels at device pixel ratio 2. A 1440 desktop frame and a 390 phone frame were not captured: headless Playwright, which would have set those viewports, received HTTP 403.

## Gaps

| Pattern | Status |
|---|---|
| Vehicle configurator | Not entered. The rule forbids configuring a vehicle for purchase. |
| Account, phone, payment | Not entered. |
| Shop | Not entered. shop.tesla.com is a separate checkout surface. |
| Empty, loading, error | Not captured. The public pages did not show them. |
| Dark marketing theme | Not present. The site has no theme toggle. |
| Phone width | Not captured. See Widths. |
| Screenshots | Not captured. Preview frames failed and headless Playwright was denied. |
