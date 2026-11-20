# Patterns

How the public archive combines the components in [components.md](components.md). Screenshots are in [screenshots/](screenshots).

## Archive shell

Every public page except the 404 stacks three bands: a lime banner, a 56px white header, then the page. The banner is one line and an arrow. The header is the wordmark, three text links, Sign In, and one black pill. At 390 the three links and Sign In collapse into the Open menu button.

![Home at 1440](screenshots/home-light-default.png)

![Home at 390 with the menu open](screenshots/mobile-home-light-menu-open.png)

## Letter page

The homepage is a letter. The h1 is graphik, near 81px, black, centred. Body copy is a narrow column in muted grey. A name and a studio line close it. There is no card grid on this page.

![Home, full page](screenshots/home-light-full.png)

## Pricing

A centred "Pricing" heading, then a two-part pill toggle, then two cards. Free is white. Pro is the same lime as the banner, with a black Popular badge. Pay Monthly changes the Pro price in place ($49 billed annually, $59 billed monthly). Get Started on a plan redirects home.

![Pricing, annual](screenshots/pricing-light-default.png)

![Pricing, monthly](screenshots/pricing-light-monthly.png)

## Book a demo

A heading and an embedded scheduler. The embed was still loading in the viewport shot (a spinner). It is a booking form and was not filled. The page is recorded as the shell plus an unloaded third-party widget.

![Demo](screenshots/demo-light-default.png)

## Curated

A heading, one line of muted text, and one published video card with a caption. No outbound design gallery was on the page.

![Curated](screenshots/curated-light-default.png)

## Missing page

`/changelog` and the other unlinked probes render a centred 404: a large numeral, one muted line, and a black pill back to home. No header, no banner.

![404](screenshots/notfound-light-default.png)

## Footer

A studio line, a link to the studio site, a copyright line, then columns. "More" is a heading. Demo and Curated live here, not in the header. Careers, Privacy and Terms leave the site.

Not present on the public archive: a form with a validation error, an empty app state, a loading skeleton, a destructive confirmation, search, a data table, and onboarding.
