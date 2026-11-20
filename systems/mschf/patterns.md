# Patterns

The public site is one page. These are the layouts that page uses.

## Drop index

[home-dark-default.png](screenshots/home-dark-default.png) is the top of the index at 1440x900. [home-dark-full.png](screenshots/home-dark-full.png) is the whole page, 8148px tall.

A fixed header sits at the top right: shop link, then the gold logo button, inset 10px. The index is a `main` with 10px of left padding. Each section has a 3px left rule.

| Section | Rule | Role |
|---|---|---|
| `.projects-previous` | `rgba(168, 145, 65, 0.3)`, padding-top 14px | released drops, numbered |
| `.projects-new` | same gold rule | the latest drop |
| `.projects-upcoming-and-links` | `border-image` from `#f00007` to `#000000` | gold `///` links, then red unreleased rows of question marks |

The three link rows are not one colour. Applied MSCHF is `#ffc700`. GSCT is `#40aaff`. Made by MSCHF is `#f00007`. The unreleased question-mark rows are the same grey as the index, `#84898e`. `.row.project-tbd` is declared `#f00007` and was not in the DOM.

## Hover and focus

[home-dark-link-hover.png](screenshots/home-dark-link-hover.png) shows a title gone white. [home-dark-logo-hover.png](screenshots/home-dark-logo-hover.png) shows the gold button gone clear. [home-dark-shop-focus.png](screenshots/home-dark-shop-focus.png) shows the browser focus ring on Shop.

## Upcoming

[home-dark-upcoming.png](screenshots/home-dark-upcoming.png) is the bottom of the index: the gold link group and the red placeholder rows.

## Phone

[mobile-home-dark-default.png](screenshots/mobile-home-dark-default.png) and [mobile-home-dark-upcoming.png](screenshots/mobile-home-dark-upcoming.png) are the same page at 390x844, device pixel ratio 2. The shop link is hidden. Body type is 30.16px / 29.12px with letter-spacing -0.905px. The left rule is 3px. The page is 4231px tall.

## Not found

[not-found-dark-default.png](screenshots/not-found-dark-default.png) is `https://mschf.com/missing-page`. Nuxt's default 404: "Page not found: /missing-page" and "Go back home". It does not use the index type or the gold rule. The sitemap lists only `/`.

## Not on this site

No app shell beyond the fixed header. No search, no filter, no onboarding, no confirmation, no toast, no table, no signed-in empty state. `/shop` redirects to store.mschf.com, which is a different theme and was not packaged.
