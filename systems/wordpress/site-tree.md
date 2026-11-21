# WordPress.com public site tree

Mapped on 2026-11-22 from the public homepage, https://wordpress.com/. Title: "WordPress.com: Everything You Need to Build Your Website". The page is a live marketing site. It is not parked and it is not a captcha wall. The homepage painted light, then a blue hosting hero after a few seconds. `theme-color` was not set.

Desktop shots are 1440 by 900 CSS pixels at device pixel ratio 2 (PNG 2880 by 1800). Phone shots are 390 by 844 CSS pixels at device pixel ratio 2 (PNG 780 by 1688). Screenshots are 256-colour PNGs.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. No site was created. No checkout was started. `login-extracted` stays not-started. catalog.json and webapps-manifest.json were left alone.

This package is WordPress.com, the hosted product. wordpress.org was not captured.

## Header

Desktop, left to right: WordPress.com wordmark, Products, Resources, Support, Pricing, Log in, Get started. Products and Resources are menu buttons. Support, Pricing, Log in, and Get started are links. A dark promo bar sits above the header: "Build and run your site from ChatGPT, free through November".

At 390 the row is the wordmark and a Menu button. The drawer lists Products, Resources, Support, and Pricing, then Log in and Get started.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Wordmark | link | https://wordpress.com/ | photographed |
| Products | menu button | listed below | photographed |
| Resources | menu button | listed below | photographed |
| Support | link | https://wordpress.com/support/ | photographed. Clicking the label navigates. It does not open a menu on desktop |
| Pricing | link | https://wordpress.com/pricing/ | photographed, desktop and phone |
| Log in | link | https://wordpress.com/log-in/ | empty wall, photographed. Not submitted |
| Get started | link | https://wordpress.com/setup/onboarding/?ref=logged-out-homepage-lp | empty signup wall, photographed. Not submitted |
| Promo bar | link | https://wp.me/chatgpt | followed the redirect to chatgpt.com and discarded the shot. ChatGPT showed a bot check. Not a WordPress.com page |

Products menu.

| Item | Destination | This pass |
|---|---|---|
| Website | https://wordpress.com/website-builder/ | photographed |
| Ecommerce | https://wordpress.com/ecommerce/ | photographed |
| AI website builder | https://wordpress.com/ai-website-builder/ | photographed |
| Blog | https://wordpress.com/create-blog/ | photographed |
| Newsletter | https://wordpress.com/newsletter/ | photographed |
| Managed hosting | https://wordpress.com/hosting/ | photographed |
| Agency hosting | https://wordpress.com/for-agencies/ | photographed |
| Site migration | https://wordpress.com/move/ | photographed |
| WordPress VIP | https://wpvip.com/ | off-domain. Not photographed |
| Find a domain | https://wordpress.com/domains/ | photographed |
| Transfer a domain | https://wordpress.com/setup/domain-transfer | intro photographed. Checkout step not opened |
| Professional email | https://wordpress.com/professional-email/ | photographed |
| Affiliate program | https://wordpress.com/affiliates/ | photographed |
| AI tools | https://wordpress.com/ai/ | photographed |
| MCP | https://wordpress.com/ai/mcp/ | photographed |
| WordPress Agent | https://wordpress.com/ai/wordpress-agent/ | photographed |
| WordPress Studio | https://developer.wordpress.com/studio/ | off-domain developer site. Not photographed |

Resources menu.

| Item | Destination | This pass |
|---|---|---|
| Business name generator | https://wordpress.com/business-name-generator/ | photographed |
| Logo generator | https://wordpress.com/logo-maker/ | photographed |
| Hire an expert | https://wordpress.com/website-design-service/ | photographed |
| Site profiler | https://wordpress.com/site-profiler | photographed. URL field not typed |
| Newspack | https://newspack.com/ | off-domain. Not photographed |
| Developer tools | https://developer.wordpress.com/docs/developer-tools/ | off-domain. Not photographed |
| Developer blog | https://wordpress.com/blog/category/development/ | not opened separately. Blog index photographed |
| Rest API | https://developer.wordpress.com/docs/api/ | off-domain. Not photographed |
| Docs | https://developer.wordpress.com/docs/ | off-domain. Not photographed |
| Studio | https://developer.wordpress.com/studio/ | off-domain. Not photographed |
| Themes | https://wordpress.com/themes | index photographed. Theme detail and start-with-theme not opened |
| Plugins | https://wordpress.com/plugins | photographed |
| Patterns | https://wordpress.com/patterns | photographed |
| View all features | https://wordpress.com/features/ | photographed |
| Latest news | https://wordpress.com/blog/ | photographed |
| Browse blogs | https://wordpress.com/discover | photographed. Subscribe and comment not used |

## Footer

The homepage footer is a section, not a `footer` element. Columns:

| Column | Links |
|---|---|
| Products | Websites, Blog, AI website builder, Newsletter, Ecommerce, Managed hosting, Agency hosting, WordPress VIP, Domains, Site migration, Affiliate program, Professional email |
| AI | AI tools, MCP, WordPress Agent, WordPress Studio |
| Features | Themes, Plugins, Patterns |
| Resources | Latest news, Browse blogs, Business name generator, Logo generator, Hire an expert, Developer resources (https://developer.wordpress.com/) |
| Support | Support center, Guides, Courses, Forums, Contact |
| Company | About, Accessibility, Sitemap, Compare, Careers (https://automattic.com/work-with-us/), Press |

Also in the footer: a language list (Deutsch through English), app store badges, Facebook, X, Instagram, YouTube, Terms of service and Privacy policy on automattic.com, and "An Automattic contraption".

Language homepages, app stores, social profiles, automattic.com, developer.wordpress.com, wpvip.com, and newspack.com were not photographed. They are other sites or other locales.

Support destinations that were photographed: https://wordpress.com/support/, https://wordpress.com/support/guides/, https://wordpress.com/support/courses/, https://wordpress.com/forums/, https://wordpress.com/support/contact/. Contact is a card index. It does not print a street address or a phone number. The cards were not followed into a chat or a charge lookup.

Company pages photographed: https://wordpress.com/about/, https://wordpress.com/accessibility/, https://wordpress.com/sitemap/, https://wordpress.com/compare/, https://wordpress.com/press/.

## Auth walls

Photographed empty. Stopped there.

| Control | Opens | Action |
|---|---|---|
| Log in | https://wordpress.com/log-in/ | "Log in to WordPress.com". Empty email or username field. Continue with Google, Apple, and GitHub were not clicked. "Email me a login link" was not opened. "Lost your password?" was not opened. Continue was not clicked. |
| Get started | https://wordpress.com/setup/onboarding/user?ref=logged-out-homepage-lp | "Create your account" at 1440, "Welcome to WordPress.com" at 390. Empty email. Continue is disabled. Identity buttons were not clicked. |
| Domain transfer "Get Started" | would continue the transfer flow toward checkout | Not clicked. The intro page was photographed. |
| Pricing plan cards | would start a paid plan | Not clicked. "start with our free plan" was not followed. |
| Discover Subscribe | would subscribe to a public blog | Not clicked. |

Headless Chromium received a "Confirm you are human" interstitial on `/log-in/` (HTTP 403). That shot was discarded. The empty login wall above was photographed in the shared preview browser, signed out, and nothing was typed.

## Phone

390 by 844. Homepage, pricing, the menu drawer, and the signup wall. The homepage at this width paints the blue hosting hero. The drawer does not list footer columns.
