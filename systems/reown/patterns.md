# Reown patterns

How the public surfaces combine. Screenshots are in [screenshots/](screenshots). The control map is [site-tree.md](site-tree.md).

## Marketing shell

The home page is a dark rounded hero inside a grey page. A fixed header holds the logo, a round Navigation Toggle, and four pill buttons (Learn, Docs, Demo, Log in). The toggle opens a second row of pills (Solutions, Use Cases, Pricing, Company) and drops a short list under the open one.

[screenshots/home-light-default.png](screenshots/home-light-default.png), [screenshots/home-light-nav-solutions.png](screenshots/home-light-nav-solutions.png).

At 390 the header keeps the logo and the toggle. The pills wrap and clip. [screenshots/mobile-home-light-nav.png](screenshots/mobile-home-light-nav.png).

## Hero and announcement

The hero is a large rounded panel with a phone mock of the AppKit connect sheet, a white headline, a blue Start building button, and an outline Explore Plans button. An orange announcement bar sits under the hero and links to the State of DeFi report. Close announcement dismisses it.

[screenshots/home-light-announcement.png](screenshots/home-light-announcement.png).

## Section themes

Blocks carry `theme--blue`, `theme--white`, `theme--black`, `theme--grey*`, `theme--orange`, or `theme--green`. Each recolors surface, button, and text for that block. The page itself stays grey.

## Pricing and FAQ

Pricing is a stack of plan cards plus an FAQ accordion. Opening a question expands the answer in place. See all FAQs goes to /faq, which is the same accordion at full length.

[screenshots/pricing-light-default.png](screenshots/pricing-light-default.png), [screenshots/faq-light-accordion.png](screenshots/faq-light-accordion.png).

## Lists

Learn and Blog are filter chips plus cards. A chip filters the list on the same page. Load more appends cards. [screenshots/learn-light-filter.png](screenshots/learn-light-filter.png), [screenshots/blog-light-default.png](screenshots/blog-light-default.png).

## Contact dialog

Contact sales opens a HubSpot dialog on the marketing page. It was opened and closed. It was not filled and not submitted. [screenshots/home-light-contact-dialog.png](screenshots/home-light-contact-dialog.png).

## Docs chrome

docs.reown.com is Mintlify: a sticky top bar (search, assistant, dashboard, demo, theme), a sidebar of groups, a content column, and an on-this-page list. Light is the default. Dark is a menu choice. [screenshots/docs-light-default.png](screenshots/docs-light-default.png), [screenshots/docs-dark-default.png](screenshots/docs-dark-default.png).

## Demo

demo.reown.com is a dark playground with Auth, Features, and Design tabs. Design previews mode, font, radius, and accent inside the widget. Get started opens the AppKit connect modal. No wallet was connected. [screenshots/demo-dark-design.png](screenshots/demo-dark-design.png), [screenshots/demo-dark-connect-modal.png](screenshots/demo-dark-connect-modal.png).

## Sign-in wall

Log in leaves reown.com for https://dashboard.reown.com/sign-in. The branch stopped there. [screenshots/dashboard-signin-light-wall.png](screenshots/dashboard-signin-light-wall.png).

## Empty, loading, error, destructive, onboarding

Not present on the public pages. The /login URL is a 404 with the footer newsletter, not a sign-in. [screenshots/login-404-light-default.png](screenshots/login-404-light-default.png).
