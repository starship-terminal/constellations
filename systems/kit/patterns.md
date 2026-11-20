# Kit patterns

How the measured components combine on the captured surfaces. Values are in [tokens.json](tokens.json). Components are in [components.md](components.md). Page evidence is in [screenshots/](screenshots).

## Marketing chrome

A 48px announcement strip sits above a fixed 58px nav. The strip is `--color-blue-500` (`#44b1ff`) with 16px Libre Franklin in soft-black, and a dark pill for the current offer. The nav (`#mega-nav`, z-index 50) is transparent over the soft-black hero on the home page, so its links paint warm white `#f2efe9` at 14px/600. On interior pages the same nav sits on the warm page field and the links paint soft-black.

The left side is the Kit wordmark, then Features, Pricing, Use Cases and Resources. Features and Use Cases are `aria-haspopup` buttons. Opening one drops a white panel (about 1440 x 288) with a two-layer shadow: `rgba(0, 0, 0, 0.1) 0px 10px 15px -3px` and `0px 4px 6px -4px`. The right side is Log in, an outlined Request a demo, and the blue Start free trial pill (about 116 x 32, 8px radius, soft-black type on `#44b1ff`).

See [home-light-default](screenshots/home-light-default.png) and [home-light-menu-features](screenshots/home-light-menu-features.png).

## Home

The hero is a soft-black band. The masthead is KitSansFont 80px/500, white, line box 152px tall, centred: "Turn your audience insights into revenue." The lede is warm white. The primary action repeats the trial pill. The secondary action is an outlined warm-white pill on the same ink. Below the fold the page returns to white and warm sections, then a tall footer.

See [hero-h1](components/crops/hero-h1-default.png) and [home-light-full](screenshots/home-light-full.png).

## Pricing

`/pricing` keeps the chrome and switches the field to warm white. The masthead is KitSansFont 64px/500 in soft-black. Three plan cards sit in a row: Free, Creator and Pro. Free and Creator use a pale wash and an 8% soft-black button (12px radius, 48px tall). Pro inverts to a dark card with a blue Start 14-day free trial button. A yearly billing switch sits at the top right, resting on yearly. FAQ rows are disclosure summaries, 752px wide. Opening one is a local toggle.

Plan buttons link to signup with a plan query. They were measured and never followed.

See [pricing-light-default](screenshots/pricing-light-default.png) and [pricing-light-faq-open](screenshots/pricing-light-faq-open.png).

## Features and compare

`/features` opens on a dark band with a 64px KitSansFont masthead, then a search field (976 x 45, 8px radius, `#f7f7f7` fill, 1px border). The field was focused and filled, then cleared. Search was not submitted.

`/compare/mailchimp` is a long comparison table under the same 64px masthead. The table itself is the list pattern: rows of feature names against Kit and Mailchimp columns, sticky header included.

See [feat-search](components/crops/feat-search-default.png) and [compare-table](components/crops/compare-table-default.png).

## Request a demo and brand

`/request-demo` is a short marketing page. The form lives in a Chili Piper iframe and was not submitted. `/brand` and `/about` are editorial pages on the same chrome. `/privacy` was viewed and not interacted with.

## Log-in card

`app.kit.com/users/login` is a separate signed-out surface. The page field is warm white `#f9f7f4`. The form column is left. A published portrait fills the right half on desktop and drops away on the phone.

The form uses Inter at 14px. Email and password fields are 40px tall. The email field has a 10px radius and an inset `#d4d4d4` ring. The submit is 470 x 48, 12px radius, soft-black fill, white type. Forgot password and Create account are links. They were measured and not followed. The fields were typed into and cleared before the stored screenshot. Log in was never clicked.

See [login-light-default](screenshots/login-light-default.png) and [mobile-login-light-default](screenshots/mobile-login-light-default.png).

## Phone

At 390 wide the announcement wraps to two lines and grows to about 80px. The nav is 60px, with the wordmark and a 36px menu button (`aria-label="Toggle mobile menu"`). Opening it replaces the page with a white sheet: Features, Pricing, Use Cases, Resources, then a full-width trial pill, an outlined Request a demo, and Log in. The hero drops to KitSansFont 48px/500.

See [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png) and [m-hero](components/crops/m-hero-default.png).

## Motion and focus

Marketing controls declare a 150ms transition with `cubic-bezier(0.4, 0, 0.2, 1)`. Hover on the trial pill does not swap the blue for another fill in the readings taken here. Keyboard focus is a thin ring rather than a fill change. Where a component recorded no visible outline change, that is written in its entry rather than invented.

Reduced motion is recorded in `raw/motion.json` when the probe has run. A verdict of ignores, if that is what the probe returns, stays as a finding.
