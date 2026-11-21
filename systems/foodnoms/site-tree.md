# FoodNoms public site tree

Mapped 2026-11-21 from [https://foodnoms.com/](https://foodnoms.com/) in headless Chromium. Every control below records what it opens. App Store links are recorded and were not followed into a store checkout. No email, name, password or code was typed. No form was submitted. No SSO button was clicked.

The site is a Framer marketing site for the iOS app. There is no web app and no web sign-in form. [https://foodnoms.com/login](https://foodnoms.com/login) is a 404. [https://foodnoms.com/download](https://foodnoms.com/download) answers 200 and then the browser is sent to the App Store. That navigation was aborted.

## Shared chrome

Desktop header, on every Framer page:

| Control | Opens |
|---|---|
| Foodnoms (wordmark) | page `/` |
| News | page `/news` |
| Foodnoms+ | page `/plus` |
| Help | page `/help` |
| Get the App | external App Store, `id1479461686`, campaign query varies by page (`ct=web-home-header` on `/`) |

Phone header (390): the same wordmark, plus a button labelled "Open navigation menu". That button opens a menu on the same page (not a new URL). The menu holds News (`/news`), Foodnoms+ (`/plus`), Help (`/help`), Get the App (App Store, `ct=web-home-header`), and "Close navigation menu", which closes the menu.

Shared footer, on every Framer page:

| Control | Opens |
|---|---|
| Download | external App Store, campaign query varies by page |
| Foodnoms+ | page `/plus` |
| News | page `/news` |
| vs MyFitnessPal | page `/vs/myfitnesspal` |
| vs Cronometer | page `/vs/cronometer` |
| vs Lose It! | page `/vs/lose-it` |
| vs MacroFactor | page `/vs/macrofactor` |
| Help & FAQ | page `/help` |
| Email Us | external `mailto:support@foodnoms.com` (mail client, not followed) |
| Press | page `/press` |
| Instagram | external `https://www.instagram.com/foodnomsapp/` |
| Threads | external `https://threads.net/@foodnomsapp` |
| Bluesky | external `https://bsky.app/profile/foodnoms.com` |
| Mastodon | external `http://mastodon.social/@foodnoms` |
| Terms of Use | page `/terms` |
| Privacy Policy | page `/privacy` |

A second Get the App / Download the App pill in the page body also opens the App Store. Campaign query names seen: `web-home-hero`, `web-home-cta`, `web-home-footer`, and the same pattern with `web-news-`, `web-plus-`, `web-help-`, `web-login-`, `web-open-settings-account-`.

## Home `/`

| Control | Opens |
|---|---|
| Header and footer | as above |
| Download on the App Store badge | external App Store, `ct=web-home-hero` |
| Download the App | external App Store, `ct=web-home-cta` |
| Previous / Next | same page. They step the phone-screenshot carousel. They do not navigate. |

## News `/news`

| Control | Opens |
|---|---|
| Each article card | page `/news/<slug>` |
| View More | same page. Reveals older article cards. Does not navigate. After one click the list included the slugs below. |
| Email field, placeholder `name@email.com` | a field. Not typed into. Not submitted. |
| Sign Up | a submit button on the insider form. Not clicked. |

Article cards link to pages. Each article page has the shared chrome, a Back link to `/news`, and body links that leave the site. Those external links were recorded and not followed.

News slugs in the sitemap and on the page after View More:

`2026-summer-update`, `foodnoms-database-ai-improvements`, `2025-year-in-review`, `2025-holiday-update`, `ios-26-liquid-glass`, `foodnoms-cloud`, `revamped-shortcuts`, `ai-assisted-moderation`, `recipe-import-ai-meal-scanner`, `daily-summary`, `copy-all-library-tab`, `introducing-new-ask-ai-features`, `growing-foodnoms-to-10k-mrr`, `new-foodnoms-app-icon`, `carb-cycling-cheat-days-and-usability-improvements`, `introducing-ask-ai`, `foodnoms-2-launch-retrospective`, `foodnoms-2`, `march-2022-developer-update`, `january-2022-developer-update`, `april-2021-developer-update`, `crowdsourced-food-database`, `better-nutrition-label-scanner`, `moving-needles`, `making-bigger-bets`, `january-2020-status-update`, `building-a-crowdsourced-food-database`.

Body links that leave the site, on the articles that were opened:

| Page | Control | Opens |
|---|---|---|
| `/news/2026-summer-update` | express interest here | external `https://forms.gle/VfRJcWfr8rNCGJFw7` |
| `/news/foodnoms-database-ai-improvements` | stemming, CIQUAL, CoFID, MEXT, Interval, acquired and shut down in 2023 | external reference pages |
| `/news/2025-year-in-review` | person names | external personal sites |
| `/news/2025-holiday-update` | scale product names | external Amazon links |
| `/news/foodnoms-cloud` | Supabase | external `https://supabase.com/` |
| `/news/revamped-shortcuts` | iCloud link | external `https://www.icloud.com/shortcuts/...` (five shortcut links) |
| `/news/ai-assisted-moderation` | Structured Outputs, Zod, Interval | external docs |
| `/news/recipe-import-ai-meal-scanner` | Foodnoms Insiders newsletter | external `https://foodnoms.ck.page/` |
| `/news/building-a-crowdsourced-food-database` | materialized views, Open Food Facts | external docs |

## Help `/help`

| Control | Opens |
|---|---|
| Search (button, aria-label "Search Icon") | dialog on the same page, with a field placeholder `Search...` |
| Search field | filters article links inside the dialog. Typing `widgets` listed `/help/widgets`, `/help/widgets-not-appearing`, `/help/vs-myfitnesspal`, `/help/about-foodnoms`, `/help/goal-format`. The field was not submitted as a form. |
| About Foodnoms, Features & Integrations, Foodnoms+, Tips, Troubleshooting | same page. Each row expands or collapses a list of article links. |
| Each article title | page `/help/<slug>` |
| Email Us (in the help body) | external `mailto:support@foodnoms.com` |

Help article slugs the accordion listed: `about-foodnoms`, `account-and-privacy`, `widgets`, `apple-watch`, `siri-and-shortcuts`, `sharing`, `intermittent-fasting-goal`, `goal-range-types`, `create-and-edit-goals`, `track-weight`, `keto-net-carbs`, `goal-format`, `goals-and-workouts`, `calibrated-energy`, `macro-goals`, `body-profile`, `values-represent`, `recipes-vs-meals`, `duplicate-recipes`, `international-food-data`, `editing-community-database-submissions`, `generic-foods-missing-added-sugars`, `food-data-quality`, `writing-to-health`, `reading-from-health`, `mcp`, `app-not-registering-subscription`, `family-sharing`, `lifetime-purchase`, `refunds`, `manage-subscription`, `free-vs-plus`, `free-trial`, `eating-out-tips`, `water-logged-discrepancies`, `calorie-discrepancies`, `barcode-scanning`, `custom-foods`, `automatic-calorie-goal`, `edit-entries`, `missed-logging`, `active-energy-apps`, `widgets-not-appearing`, `sync-issues`, `changing-apple-account`, `sign-in-with-apple`, `android-app`, `sharing-reports`.

`/help/vs-myfitnesspal` is linked from an article, not from the footer comparison list. `/help/custom-shortcuts` is linked from a help page and returns the same 404 template as `/login`.

An article page has the shared chrome, a Back link to `/help`, and body links. Examples: Apple Shortcuts User Guide on `/help/siri-and-shortcuts`, `https://claude.ai/` on `/help/mcp`, `https://reportaproblem.apple.com/` on `/help/refunds`. Those were not followed.

## Plus `/plus` and family plan `/family-plan`

Header, footer, and App Store pills only (`ct=web-plus-header`, `web-plus-cta`, `web-plus-footer` on `/plus`). No price form. No account wall.

## Comparisons

`/vs/myfitnesspal`, `/vs/cronometer`, `/vs/lose-it`, `/vs/macrofactor`. Shared chrome plus the page's own App Store pills. No form.

## Press `/press` and `/press/<slug>`

| Control | Opens |
|---|---|
| Release cards | page `/press/2026-8-release`, `/press/ios26-release`, `/press/revamped-shortcuts`, `/press/new-ai-features` |
| App Store, Website, Mastadon, Threads, Instagram, Bluesky | same page. Each copies a link and the label changes to "Copied!". Not a navigation. |
| Download Screenshots, Download Logos, Download Promo Images | external zip on `framerusercontent.com` |
| Press kit links on a release | external zip on `framerusercontent.com` |

## Legal

`/terms` and `/privacy` are pages. Terms links to `https://foodnoms.com/` and to `https://support.apple.com/en-us/118223` and `https://www.adr.org`. Those external links were not followed.

## Open in app

`/open/settings/sign-up` and `/open/settings/account` are pages titled "Open in Foodnoms". They are not sign-in forms.

| Control | Opens |
|---|---|
| Open in Foodnoms | the anchor's `href` is `../../` (the site root). Clicking it did not leave the page in this browser. It does not show an email, password, or SSO button. |
| Get the App | external App Store |

## Login

`/login` returns HTTP 404, title "Page Not Found". No form. Return Home opens `/`. Get the App opens the App Store with `ct=web-login-header`.

## Download

`/download` returns HTTP 200 and the next document request is `https://apps.apple.com/app/apple-store/id1479461686`. That request was aborted. The store page was not captured.

## Not on the site

No checkbox, radio, switch, select, tabs, tooltip, toast, table, avatar, or badge on the public pages that were opened. The press "Copied!" label is inline button text, not a toast. Phone screenshots on the home page are marketing images, not the product.
