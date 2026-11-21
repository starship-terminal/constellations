# Riverside patterns

How the measured components sit on riverside.com's public pages. Values are in [tokens.json](tokens.json) and [components.md](components.md). Screenshots are in [screenshots/](screenshots). The control map is [site-tree.md](site-tree.md).

## App shell

The desktop bar is 64px (`core.layout.header-height`) on a white field. It holds the wordmark, three Webflow dropdowns (Platform, Solutions, Resources), For Business, Pricing, Contact Sales, Login, and a black pill (`light.ink`, white label, `core.radius.pill`). The home hero behind it is a dark photograph, not a second theme.

At 390 the same links sit behind `.w-nav-button`. The open menu is a white sheet: Platform, Solutions and Resources as rows with chevrons, then outlined Contact Sales and Login, then a black Start for Free pill ([mobile-home-light-menu](screenshots/mobile-home-light-menu.png)). A Google One Tap sheet can mount over the phone page. It was not clicked.

## Hero

The home hero is white Sharp Grotesk 60px (`core.typography.display`) over a dark photograph, with an Instrument Sans subline. Under that, translucent pill chips (Podcasts, Interviews, Webinars, Live streams, Social clips, Video marketing, Transcriptions) and a purple Start for Free button (`light.accent`). A product still sits below the fold. It is a public demo, not the signed-in studio ([home-light-default](screenshots/home-light-default.png)).

## Pricing

https://riverside.com/pricing opens on "There's a plan for every story." A Monthly / Yearly control sits above four cards (Pro, Grow, Webinar, Business). Yearly is the default. Grow carries a lavender Best Value badge and a purple outline. Trial and Book a demo buttons were measured in screenshots and not followed ([pricing-light-default](screenshots/pricing-light-default.png)).

## Login wall

https://riverside.com/login is a split screen: a dark form panel and a photograph. The form shows email and password, a purple Log in button, and Google, Apple and Spotify buttons, plus an SSO link. Password was not submitted. SSO was not clicked ([login-light-wall](screenshots/login-light-wall.png)). The panel uses Inter and a `#222222` field, which is not the marketing theme.

## Blog and FAQ

The blog index is a list of published posts with an email field. The field was focused and not submitted. FAQ is a short accordion page. Opening a question is a local toggle.

## Footer

The footer is a dark band with light grey links (`light.footer-muted`) and social icons. Terms, Privacy and Cookies are public pages. Social profiles were left.
