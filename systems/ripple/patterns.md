# Patterns

Public pages on ripple.com, captured 2026-11-19. Desktop shots are 1440 CSS pixels wide. The phone shot is 390 CSS pixels wide at devicePixelRatio 2, so the PNG is 780 pixels wide.

## Home

White header, 80px, over a white hero and alternating white and `#fafafa` bands. The closing band and the footer are `#141a1f`. Content column max-width is 1152px. The header container max-width is 1480px.

![Home](screenshots/home-light-default.png)

![Home, phone](screenshots/home-light-phone.png)

## Navigation

Six header menus (Products, Solutions, Customers, Developers, Resources, Company) open a full-width panel. On a 390px width those items move into a white drawer under an Open menu button. Contact Sales stays a pill in the header on desktop.

![Menu](screenshots/home-light-menu.png)

![Phone menu](screenshots/home-light-phone-menu.png)

## Search

A 700x434 white dialog on a scrim `rgba(16, 19, 21, 0.47)`. The field is focused on open. Nothing was submitted.

![Search](screenshots/home-light-search.png)

## Product and company

Product pages lead with a clipped gradient headline (computed on `/company/` and `/products/stablecoin/`: `linear-gradient(92deg, #0052b6, #33a3ff 66.48%, #0067e5 97.37%)`). The primary button repeats.

![Stablecoin](screenshots/stablecoin-light-default.png)

![Company](screenshots/company-light-default.png)

## Customers and insights

Customer logos sit in a marquee on `#fafafa`. Insight cards are image plus title plus date, in the 1152px grid.

![Customers](screenshots/customers-light-default.png)

![Insights](screenshots/insights-light-default.png)

## FAQ

One column of questions on `#fafafa`. Opening a question keeps the gray header and reveals the answer under it.

![FAQ](screenshots/faq-light-default.png)

![FAQ open](screenshots/faq-light-open.png)

## Legal

A 1152px grid. The title is a 16px heading in the side column. Section headings are 22px. Links are `#008cff`.

![Privacy](screenshots/privacy-light-default.png)

## Contact

`/contact/sales/` describes the conversation, then embeds a form from go.ripple.com. The form was not filled and not submitted.

![Contact sales](screenshots/contact-sales-light-default.png)

## Not captured

Signed-in app, wallet connect, checkout, KYC, and any submitted form. The Osano cookie banner was hidden in screenshots and was not accepted or denied.
