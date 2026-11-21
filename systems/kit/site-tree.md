# Kit public site tree

Mapped on 2026-11-21 from the live public site in headless Chromium, desktop 1440 and phone 390. Start URL is https://kit.com/. A bare https://kit.com/ request without a browser user agent returned HTTP 403 from Cloudflare ("Are you a robot?"). The same URL with a Chrome user agent returned 200 and rendered the marketing home. https://www.kit.com/ redirects to https://kit.com/. https://convertkit.com/ also lands on https://kit.com/.

Nothing on this tree was submitted. No email, password, phone, or code was typed. Identity-provider buttons were not present on the walls that rendered, and none were clicked. Cookie banners were not accepted. The one overlay found was hidden in CSS by the capture scripts, never answered.

Kit publishes no theme switch and no locale switch on the pages opened. `color-scheme` on the home document was `normal`. Emulating dark mode was not treated as a second theme.

## Home

URL: https://kit.com/

| Control | What it opens |
|---|---|
| Claim Black Friday deal (top strip) | https://app.kit.com/users/signup?promo_code=50BFCM26. Not followed. Signup on that host stopped at a Cloudflare human-check (HTTP 403, title "Just a moment...", vendor Cloudflare). |
| Kit wordmark | https://kit.com/ |
| Features (button, aria-expanded false until clicked) | Opens the Features column of the mega menu in place. Does not navigate. Escape closes it. Photographed as [home-light-menu-features.png](screenshots/home-light-menu-features.png). |
| Pricing (link) | https://kit.com/pricing |
| Use Cases (button) | Opens the Use Cases column of the same mega menu. Photographed as [home-light-menu-use-cases.png](screenshots/home-light-menu-use-cases.png). |
| Resources (button) | Opens the Resources column of the same mega menu. Photographed as [home-light-menu-resources.png](screenshots/home-light-menu-resources.png). |
| Log in | https://app.kit.com/users/login. Empty wall. See below. |
| Request a demo | https://kit.com/request-demo. Page rendered. The Chili Piper form inside it was not entered and not submitted. |
| Start free trial | https://app.kit.com/users/signup?plan=1k. Stopped at Cloudflare HTTP 403. Not photographed as a product screen. |
| Request demo (hero) | https://kit.com/request-demo |
| Previous slide / Next slide | Local carousel on the home page. Next slide was clicked and photographed as [home-light-carousel-next.png](screenshots/home-light-carousel-next.png). No navigation. |
| Toggle mobile menu (390 only) | Opens the phone drawer in place. Photographed as [mobile-home-light-drawer.png](screenshots/mobile-home-light-drawer.png). Links inside were not followed. |

There is no search field on the home page.

### Features menu column

Opened from the Features button. Each row is a link. None of these were followed past recording the href, except the pages named in "Pages opened" below.

| Label | Href |
|---|---|
| See all features | /features |
| Pro | /pro |
| Kit + AI | /ai |
| Advertisers | /advertisers |
| Analytics | /features/analytics |
| Subscriber Signals | /features/signals |
| Recommendations | /features/recommendations |
| Landing pages | /features/landing-pages |
| Forms | /features/forms |
| Email designer | /features/email-designer |
| Email marketing | /features/email-marketing |
| Deliverability | /features/deliverability |
| Visual Automations | /features/automations |
| Kit App Store | /apps |
| Kit MCP | /ai/mcp |
| Commerce | /features/commerce |
| Paid Recommendations | /features/paid-recommendations |
| Paid newsletter | /features/commerce/paid-newsletter |
| Newsletter sponsorships | /features/newsletter-sponsorships |
| Request demo (panel) | /request-demo |
| See all case studies | /resources/blog/category/case-study |
| Start free trial (panel) | https://app.kit.com/users/signup?plan=1k (Cloudflare 403 if followed) |

The same panel also lists the Use Cases and Resources columns. Clicking Features, Use Cases, or Resources changes which column is in view. It does not change the URL.

### Use Cases menu column

| Label | Href |
|---|---|
| Artists | /use-cases/artists |
| Authors | /use-cases/authors |
| Bloggers | /use-cases/bloggers |
| Coaches | /use-cases/coaches |
| Course creators | /use-cases/course-memberships |
| Marketers | /use-cases/marketers |
| Musicians | /use-cases/musicians |
| Newsletter creators | /use-cases/newsletter-creators |
| Podcasters | /use-cases/podcasters |
| YouTubers | /use-cases/youtubers |

Feature cards in the same open panel: Email marketing (/features/email-marketing), Run a paid newsletter (/features/commerce/paid-newsletter), Automate your marketing (/features/automations), Sell digital products (/features/commerce).

### Resources menu column

| Label | Href |
|---|---|
| Get support | /support |
| Hire a Kit Expert | /experts |
| Free migrations | /migrations (Cloudflare HTTP 403 when opened) |
| Email templates | /marketplace |
| Latest report | /reports/creator-economy-2024 |
| Kit University | https://learn.kit.com (separate host, not opened) |
| Podcasts | /resources/podcasts |
| Blog | /resources |
| Kit Studios | /studios |
| I Am A Creator | /resources/creator-stories |
| Rebranding in Public | /rebranding-in-public |
| See all resources | /resources |

## Pricing

URL: https://kit.com/pricing

| Control | What it opens |
|---|---|
| Plan trial links ("Start 14-day free trial", "Sign up free") | Signup URLs with a plan query. Not followed. Signup is the Cloudflare wall. |
| Yearly billing switch | A switch on the page. Not toggled on this refresh. Resting state is in [pricing-light-default.png](screenshots/pricing-light-default.png). |
| FAQ summary "How many emails" | Opens that answer in place. Photographed as [pricing-light-faq-open.png](screenshots/pricing-light-faq-open.png). |
| Subscriber count control | A slider, not a select. Not dragged. |

## Features

URL: https://kit.com/features

| Control | What it opens |
|---|---|
| Feature explorer search (`#feature-explorer-search`) | Filters the explorer in place. Focused, not typed into, not submitted. [features-light-search-focused.png](screenshots/features-light-search-focused.png). |
| Feature rows | Links to /features/* pages. Email marketing was opened. The other feature URLs are listed in the Features menu. |

## Resources

URL: https://kit.com/resources

| Control | What it opens |
|---|---|
| Articles | Stays on /resources |
| Case Studies | /resources/blog/category/case-study |
| Creator Stories | /resources/creator-stories |
| Search | A button in the blog header, not a text field on the index. Not clicked, so the search panel it opens was not seen. The button is in [resources-light-default.png](screenshots/resources-light-default.png). |

## App store

URL: https://kit.com/apps

| Control | What it opens |
|---|---|
| Category buttons (All categories, Advertisements, Affiliate Management, Analytics, CRM, Content, Email Verification, Events, Giveaways, Lead Capture, Memberships & Courses, Scheduling, Surveys & Quizzes, Webinar Services, Website Platforms, Workflows, e-Commerce, Legacy integrations) | Filters the card grid in place. URL stays https://kit.com/apps. Analytics was clicked. Photograph: [apps-light-filter.png](screenshots/apps-light-filter.png). |
| Sort by | Opens a menu: Popular, Newest, Name: A-Z, Name: Z-A. Photographed open as [apps-light-sort.png](screenshots/apps-light-sort.png). No option was chosen. |
| Install | Not clicked. Would leave the public page. |
| Learn more | Not followed. |
| Explore Kit API | Not followed. |
| Request an app | Not followed. |

## Support

URL: https://kit.com/support

| Control | What it opens |
|---|---|
| Search field ("What do you need help with?") | A text field. Not typed into. Not submitted. Visible in [support-light-default.png](screenshots/support-light-default.png). |
| Topic links (Getting started, Switching to Kit, Growing, Earning, Something else) | In-page sections. Not each opened. |
| Log in (contact row) | https://app.kit.com/users/login. Not clicked from this page. The empty wall was photographed from the header link. |
| Go to Knowledge Base | https://help.kit.com/en. Opened separately. |

## Footer

Present on https://kit.com/. Column links, recorded from the live footer. Mailto and social links were not activated.

Product and plans: Pricing (/pricing), Free migrations (/migrations, Cloudflare 403), Request a demo (/request-demo), Start free trial (signup, Cloudflare 403).

Use cases: the same ten /use-cases/* links as the Use Cases menu.

Product: Product overview (/features), Pro (/pro), What's new (https://updates.kit.com, not opened), Kit + AI (/ai), compare links (Mailchimp, ActiveCampaign, Mailerlite, Beehiiv, Substack, Aweber, Flodesk, and /compare).

Features: the same /features/* and /apps and /ai/mcp links as the Features menu.

Learn: Blog (/resources), Rebranding in Public (/rebranding-in-public), Email template marketplace (/marketplace), Podcasts (/resources/podcasts), Kit University (https://learn.kit.com, not opened), Hire a Kit Expert (/experts), Get support (/support), Report spam (/report-spam), Knowledge base (https://help.kit.com/en/, opened), Subscribe to our newsletter (https://newsletter.kit.com/, not opened), Sitemap (/sitemap, opened).

Company: About (/about), Kit Studios (/studios), Press (/news), Careers (/careers), Brand assets (/brand), Developer docs (https://developers.kit.com/api-reference/overview, not opened), Affiliate program (/affiliate), ConvertKit is now Kit (/resources/blog/convertkit-is-now-kit).

Contact: a mailto link. Not activated. The address is not copied here.

Social: YouTube, X, Facebook, Instagram, LinkedIn. Not opened. These are profile links, not identity-provider login buttons.

Legal: Privacy (/privacy, opened, view only), Terms (/terms), GDPR (/gdpr), Imprint (/imprint).

## Login wall

URL: https://app.kit.com/users/login

Reached from the header Log in link and from https://app.kit.com/ (which redirects here). HTTP 200. Title "Log In - Kit". Empty form. Email and password values were length 0. Nothing was typed. Log in was not clicked. Create account was not clicked. Show password was not clicked. The remember-me checkbox was not toggled.

| Control | What it would open | This capture |
|---|---|---|
| Log in tab | Stays on /users/login | Photographed at rest |
| Create account | https://app.kit.com/users/signup?plan=1k | Not clicked. Direct navigation returned HTTP 403, Cloudflare "Are you a robot?" |
| Email field | Text input, placeholder only | Empty. Not typed. |
| Password field | Password input, placeholder dots | Empty. Not typed. |
| Show password | Toggles the field type | Not clicked |
| Keep me logged in on this device | Checkbox | Not toggled |
| Log in (submit) | Would submit the form | Not clicked |
| I forgot my password | https://app.kit.com/users/password/new | Not clicked from this page. The URL was opened separately as its own empty wall. |

No Google, Apple, Facebook, Microsoft, GitHub, or SSO button was on this wall.

Photographs: [login-light-default.png](screenshots/login-light-default.png), [mobile-login-light-default.png](screenshots/mobile-login-light-default.png).

## Password reset wall

URL: https://app.kit.com/users/password/new

HTTP 200. Title "Reset your password - Kit". Empty email field (value length 0). "Send me a reset link" was not clicked. "Back to log in" returns to /users/login and was not clicked. Photograph: [password-reset-light-default.png](screenshots/password-reset-light-default.png).

## Pages opened

These rendered and were photographed or read. A page not in this list was recorded from a menu or the sitemap and not opened.

| Page | URL | Notes |
|---|---|---|
| Home | https://kit.com/ | Menus, carousel, phone drawer |
| Pricing | https://kit.com/pricing | FAQ opened |
| Features | https://kit.com/features | Search focused, not typed |
| Email marketing | https://kit.com/features/email-marketing | |
| Request a demo | https://kit.com/request-demo | Form iframe not entered |
| Mailchimp compare | https://kit.com/compare/mailchimp | Table |
| Brand | https://kit.com/brand | |
| About | https://kit.com/about | |
| Privacy | https://kit.com/privacy | View only |
| Resources | https://kit.com/resources | Search at rest |
| App store | https://kit.com/apps | Analytics filter and Sort by menu opened |
| Support | https://kit.com/support | |
| Sitemap | https://kit.com/sitemap | Link list |
| Help center | https://help.kit.com/en | Search control present, not typed. Separate host. |
| Log in | https://app.kit.com/users/login | Empty wall |
| Password reset | https://app.kit.com/users/password/new | Empty wall |

## Stopped branches

| URL | Result |
|---|---|
| https://app.kit.com/users/signup?plan=1k | HTTP 403. Cloudflare. Title "Just a moment...". Body asks to confirm you are not a robot. No product screenshot stored. |
| https://kit.com/migrations | HTTP 403. Same Cloudflare human-check. |
| https://app.kit.com/ after login | Not entered. The redirect stops at the empty login wall. |
| https://learn.kit.com | Not opened. |
| https://developers.kit.com | Not opened. |
| https://updates.kit.com | Not opened. |
| https://newsletter.kit.com/ | Not opened. Newsletter signup was not filled. |
| https://creatorsessions.kit.com | Listed on the sitemap. Not opened. |

The sitemap at https://kit.com/sitemap also lists careers, studios, testimonials, mission, news, affiliate, report spam, terms, GDPR, imprint, compare variants, use-case pages, blog categories, and two creator-economy reports. Those share the marketing chrome already captured. They were not each opened on this refresh.
