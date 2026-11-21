# Patterns

Signed-out pages. Color-scheme dark. The 2026-11-19 readings used a 1169 by 731 viewport and had no frames. The 2026-11-20 frames measured 1440 by 900 and 390 by 844. See [screenshots/README.md](screenshots/README.md) and [site-tree.md](site-tree.md).

## Marketing home

`https://suno.com/`, title "Suno | AI Music Generator".

The page background is `#101012`. A top nav holds Products, Resources, Pricing and Careers as pills, then a transparent "Log in" pill and a cream "Join Suno for free" pill. The hero is a rotating prompt headline in Neue Montreal at 72px, weight 500, white, letter-spacing -0.96px, over a textarea whose placeholder reads "Chat to make music". A black "Create" pill sits with that prompt.

Below the hero, song tiles show public track titles, artist names and Remix chips. Those tiles are a public demo, not the signed-in library. Feature sections use Editorial New at 66px, weight 300, for lines such as "Mind blowing song quality". Feature titles under them are Neue Montreal 18px weight 500.

## Pricing

The same home page, `#pricing-section`. Headline "Start making music for free" in Editorial New. A Monthly / Yearly pill sits above four cards: Free ($0), Pro ($8 a month, billed $96 a year, "Most Popular"), Premier ($24 a month, billed $288 a year, "Best Value") and Platinum. Yearly was selected when the section was read. Plan buttons read "Join Suno for free", "Get Pro", "Get Premier" and "Get Platinum". None of the paid buttons were followed.

## Sign-in dialog

Opened from "Log in" on the home page, still at `https://suno.com/`. A 400px dialog, radius 32px, on a 60% black overlay. Title "Welcome to Suno". Providers: Google, Apple, Phone, Discord, Facebook, Microsoft. No email field. Closed without continuing.

## Careers

`https://suno.com/careers`, title "Careers | Suno". Same dark page and nav. The h1 "We make music more possible." is Editorial New, 96px, weight 300, letter-spacing not re-read on this page (the about h1 at the same size measured -2.88px). A large cream pill reads "See open positions". Roles link out to Ashby. Those applications were not opened.

## About

`https://suno.com/about`, title "About | Suno". Same shell. The h1 "Music is who we are." is Editorial New, 96px, weight 300, line-height 104px, letter-spacing -2.88px, color `#f7f4ef`.

## Gaps

- No phone-width layout. The viewport was not resized.
- No light theme layout. The pages stayed dark.
- No signed-in app shell, empty library, generation progress, or error toast.
- No checkout, no payment form, no destructive confirmation.
- No screenshot of any of these patterns.


## Logged-out app shell, 2026-11-20

`/discover`, `/explore`, `/labs` and `/pricing` share a left sidebar: Home, Explore, Create, Studio, Library, Log in, Earn credits, Labs, More. Create, Library and Earn credits redirected to sign-in. Studio redirected to the public studio welcome page. See [discover-desktop.png](screenshots/discover-desktop.png).

## Phone, 2026-11-20

The marketing header collapses to Open menu, Log in and Open App. The menu lists V6, Studio, Visuals, MCP, Bridge, Voices, Stem Separation, Remix, Custom Models, Pricing and Careers. See [home-phone-menu.png](screenshots/home-phone-menu.png).
