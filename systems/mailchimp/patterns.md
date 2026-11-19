# Mailchimp patterns

How the measured components combine on the captured surfaces. Values are in [tokens.json](tokens.json). Components are in [components.md](components.md). Page evidence is in [screenshots/](screenshots).

## Marketing chrome

The header is `header.iaGlobalNav`. On the home page the wordmark sits under a dark announcement strip. The strip's "Start today." link measured 64.83 x 16, white Tally 13px/400. The strip itself (`aside.freeTrial--banner`) measured 1440 x 41.55 with a caviar background `#231e15`. That aside is not the nav.

The left side is the wordmark (`a[aria-label="Mailchimp Home"]`, 162.45 x 46). Then Industries and Solutions, Integrations and Resources, each a `button.iaNav__cta[aria-haspopup]`. Opening Resources drops `section.iaNav__panel.expanded`, 1440 x 507.5, transparent on the section itself. The right side is a Pricing link (58.95 x 30.3), Search, an outlined Log In pill (85.56 x 43.5, transparent fill, 1px caviar stroke) and the yellow Start Free Trial pill (140.36 x 43.5, `#ffe01b`, caviar type 13px/700, 1px caviar stroke).

See [home-light-default](screenshots/home-light-default.png) and [home-light-menu-resources](screenshots/home-light-menu-resources.png).

## Home

The hero is a dark band. The masthead is Means Web 64px/400, white, letter-spacing -1.2px, line box 153.59px tall, 960px wide, centred: "Turn ideas into emails that connect." The primary action is a yellow Start Free Trial button, 343 x 48, caviar type 15px/600 on `#ffe01b`, with a 1px caviar stroke. It points at pricing. It was measured and never followed. The secondary action under the photo band is "See all demos", white Tally 16px/400, 136.72 x 32. It was measured and never followed.

Below the fold the page returns to light sections, then a gold footer `#e7b75f`, 1440 x 1041.78. A sitemap link, "Why Mailchimp?", measured 90.34 x 15 in caviar 13px/400.

See [hero-h1](components/crops/hero-h1-default.png) and [home-light-full](screenshots/home-light-full.png).

## Pricing

`/pricing/marketing/` keeps the chrome. The Standard plan cell (`.singlePlan__planCardCell`) measured 370 x 508.25. Its root paints transparent; the white card look is in the children. Inside it, the contacts select (`select[name="Number of Contacts"]`) measured 214 x 44 at rest, and a trial-or-discount radio measured 20 x 20. Neither was changed. Nothing was submitted.

The Standard Start Free Trial link (`a.ctaBuyNow`) measured 338 x 43.5, yellow `#ffe01b`, radius 26px, caviar type. It points at `/signup/` with a plan query. It was measured and never followed. Signup was not started. Checkout was not started.

See [pricing-light-default](screenshots/pricing-light-default.png) and [price-cta](components/crops/price-cta-default.png).

## Features and about

`/features/` opens with a caviar Means Web masthead at 48px/400, letter-spacing -1px, line box 96px: "Powerful marketing features that help your business grow faster." `/about/` is a public page that loads signed out. Its masthead is the same 48px Means Web: "About Mailchimp."

See [features-light-default](screenshots/features-light-default.png) and [about-light-default](screenshots/about-light-default.png).

## Log-in card

`login.mailchimp.com` is a separate signed-out surface. The form `#unified-login-form` measured 422 x 453. It uses Graphik Web, ink `#21262a`, not the marketing Tally stack. The heading reads "Log in to Mailchimp".

The username field is 422 x 46, white fill, 17px/400. It was focused, typed into with a placeholder, then cleared. The submit is 422 x 36, teal `#017e89`, white type 14px/500. It was never clicked. Sign-in was not started. Forgot username and Create an account are links. They were measured and not followed. Signup was not started.

See [login-light-default](screenshots/login-light-default.png) and [mobile-login-light-default](screenshots/mobile-login-light-default.png).

## Phone

At 390 wide the nav bar measured 390 x 60. The Main Menu button (`button.iaNav__menuOpen`) measured 46 x 39.3. Opening it is a local toggle. Links were never followed. The hero drops to Means Web 36px/400, line box 93.59px, 343px wide, still white.

See [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) and [m-hero](components/crops/m-hero-default.png).

## Motion and focus

Marketing nav links measured a 150ms `ease` background-color transition. The trial pills measured a 0.3s transition on box-shadow and transform with `cubic-bezier(0.5, 2.5, 0.7, 0.7)`. Keyboard focus on marketing controls is a 2px `#4bc4c2` outline. The log-in submit draws its focus as a shadow. Hover on the yellow pill did not swap `#ffe01b` for another fill in the readings taken here. The declared `--ease-*` curves belong to the embedded Navattic demo and are not Mailchimp tokens.

`raw/motion.json` covers home, pricing and the log-in card. Reduced-motion behaviour is `partial`: some transitions shorten, some stay.
