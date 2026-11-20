# Patterns

## Marketing home

[screenshots/home-light-default.png](screenshots/home-light-default.png)

A white page, a fixed 64px header, a centred Inter Tight headline, a soft prompt card with a solid pill, then a mono eyebrow and a horizontal row of template cards. The footer is the dark theme.

At 390px the header keeps the wordmark and a menu button. The headline stacks and the prompt card goes full width. [screenshots/home-light-phone.png](screenshots/home-light-phone.png)

## Nav menu

[screenshots/home-light-menu.png](screenshots/home-light-menu.png)

Opening 3D Printing reveals a panel of image cards under small mono section labels. The header stays put. The page behind is dimmed in the capture.

## Pricing

[screenshots/pricing-light-default.png](screenshots/pricing-light-default.png)

Same header. A mono "PRICING" eyebrow, a 64px headline, a Monthly / Annual control, then four plan cards. Pro is raised. A comparison table follows. FAQ rows are full-width buttons with 24px vertical padding. Opening one was measured. The answer panel was not a sibling element, so its type is a gap.

## Store and docs

[screenshots/store-light-default.png](screenshots/store-light-default.png) uses the same header over a filter row and a product grid. [screenshots/docs-light-default.png](screenshots/docs-light-default.png) is a separate docs chrome (sidebar plus article) and was not measured control by control.

## Auth boundary

`https://beta.womp.com/` and `https://beta.womp.com/auth` show the same signed-out card: Inter Tight heading, a soft Google button, an email field, a solid Continue button, and a ghost SSO button. The email field was focused and left empty. Google and SSO were not pressed. A public print preview at `beta.womp.com/preview/...` shows the same solid pill ("Join Womp to remix this 3d print") over a white page, still signed out.

## Contact sales

[screenshots/contact-light-default.png](screenshots/contact-light-default.png)

A sales form: name, email, company, company-size cards, a topic select, a message box, and Send message. It asks for a company name and a company size, and it includes a reCAPTCHA field. It was not submitted.
