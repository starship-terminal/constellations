# Linktree patterns

How the measured components combine on linktr.ee's public surface, read from the screenshots and the component entries in [components.md](components.md). The site paints one light theme. Values below are from the light set.

## The shell

The marketing nav is a `nav` that measures 1440 x 138, including the promo strip above the bar ([home-light-default](screenshots/home-light-default.png)). The visible bar is a child layer: 1296 x 90, white, 1px `rgba(0,0,0,0.08)` border, 9999px radius, and a `0 24px 60px` shadow. Inside it: text links (Pricing, 86 x 48, Linksans 16/400, `#1e2330`), Log in (102 x 62), and Sign up free (152 x 62, fill `#1e2330`, white text, 9999px radius). Solutions opens a menu; the Musicians item measured 319 x 48 once the menu was open ([nav-menu-panel-opened](components/crops/nav-menu-panel-opened.png)).

At 390 the bar is 390 x 89. A 48px Toggle menu button opens a panel. Opening Solutions in that panel shows the audience list ([mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png)). Sign up free shrinks to 110 x 46. The phone homepage full-page shot was not committed: a row of public profile cards shows usernames.

## The hero and claim field

The home hero sits on chartreuse `#d2e823` (`light.hero`). The title "A link in bio built for you." is Linksans 80px/800, `#254f1a`, 616 x 171 ([hero-title-default](components/crops/hero-title-default.png)). Get started for free is a 300 x 60 forest pill (`#254f1a`, 9999px radius). CDP-forced press scales it to 291 x 58.2. The claim field is a separate 290 x 60 white control with an 8px radius. Its accessible name is "Claim your Linktree username". The default value already starts with `linktr.ee/`. It was filled and cleared, never submitted. Claim your Linktree is a second 300 x 60 pill beside it.

## Pricing

`/s/pricing` is a public page, 1440 wide and about 19048 tall ([pricing-light-full](screenshots/pricing-light-full.png)). The title "Pick your plan. Make it yours." measures 706 x 53. The Pro name is a 65 x 36 heading, not a card. The plan actions are anchors: Try free for 7 days (336 x 48, `#7f22fe`, white text, 9999px radius) and Get started (336 x 48, white, hairline). Both lead toward checkout. They were measured and not followed.

## The public profile

`/linktr.ee` loads signed out ([profile-light-default](screenshots/profile-light-default.png)). The title is Link Sans Product 24/600, 95 x 33. Share profile is a 40 x 40 button with an accessible name and no visible text. Links and Shop are 94 x 48 tabs. The first social button is 48 x 48 and grows to 52 x 52 on hover. A profile link row is 395 x 64. Verified is a 62 x 24 badge in `rgba(0,0,0,0.75)`. Social and share buttons leave the page or open a share sheet. They were not activated.

## The login wall

`/login` redirects to `/universal-login#/login`. On 2026-11-21 the wall offered an email or username field, Continue, Continue with Google, Continue with Apple, Forgot password, and Forgot username. Nothing was typed. Google and Apple were not clicked. The wall was not photographed. `/register` lands on the signup half of the same wall. This is a signed-out wall, not the product. The control map is [site-tree.md](site-tree.md).

## The footer

The footer is a 1440 x 1667 dahlia band, `#502274`, with Linksans display type in `#e9c0e9`. Footer links, including About, are `#676b5f`. Keyboard focus on About draws the browser's 1px `#005fcc` ring.
