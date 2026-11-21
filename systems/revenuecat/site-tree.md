# RevenueCat public site tree

Mapped on 2026-11-21 from https://www.revenuecat.com/ in headless Chromium at 1440×900, before screenshots. The homepage returned HTTP 200. Controls were opened by hover or click. No form was submitted. No email was typed. Cookie, newsletter, sales and contact controls were recorded and not activated when activation would accept, reject or send data.

The marketing site is a light-only Next.js app on Vercel (`body` is white `#ffffff`, text `rgb(31, 31, 71)`). Docs at `/docs` are a separate public surface with their own theme toggle. The signed-in product at `app.revenuecat.com` stops at a login or signup wall.

## Shell (every marketing page)

| Control | Opens | Stop? |
|---|---|---|
| Logo, "Back to the RevenueCat homepage" | https://www.revenuecat.com/ | No |
| Why RevenueCat? (button, `aria-expanded` false until click) | Header mega-menu. See below. Escape closes it. | No |
| Solutions (button) | Header mega-menu. See below. | No |
| Developers (button) | Header mega-menu. See below. | No |
| Resources (button) | Header mega-menu. See below. | No |
| Pricing | https://www.revenuecat.com/pricing | No |
| Log in | https://app.revenuecat.com/login | Yes. Email field, then a password field after an email is entered. Do not type an email. |
| Contact sales | https://www.revenuecat.com/talk-to-sales | Page is public. Its form is a wall: do not fill or submit. |
| Sign up | https://app.revenuecat.com/signup | Yes. Name, email, password, referral, marketing checkbox. Do not type or submit. |
| English / Eng (header and footer) | Locale menu: English (current), 日本語 → `/jp`, 한국어 → `/ko`, Català → `/cat` | Locale copies of the same marketing site. Captured as the menu, not as a second product. |
| Menu (present in the header button list; the desktop bar already shows the links) | Mobile sheet at 390. Same destinations as the desktop menus plus Log in, Contact sales, Sign up, Pricing. | No, unless the destination is a login or signup URL. |
| iubenda cookie banner (`#iubenda-cs-banner`) | "We use third-party cookies…" Customize, Reject, Accept | Hide only. Never click Reject, Accept or Customize (Customize opens a preference dialog that can POST). |
| Footer social: Github, X, Mastodon | github.com/RevenueCat, x.com/revenuecat, mastodon.social/@revenuecat | External. Not captured. |
| Footer store badges | Google Play `com.revenuecat.mobile`, App Store RevenueCat Mobile | External store listings. Not captured. |

Footer columns repeat the same public pages as the menus, plus legal: Terms (`/terms`), Privacy (`/privacy`), Cookies (`/cookie-policy`), GDPR (`/gdpr`), Security (`/security-and-compliance`), Fair billing (`/fair-billing`).

## Why RevenueCat? menu

| Item | Opens |
|---|---|
| Get started | https://www.revenuecat.com/feature/paywalls |
| Migrate | https://www.revenuecat.com/migration-implementation-case |
| Customer stories | https://www.revenuecat.com/testimonials |
| State of Subscription Apps card | https://www.revenuecat.com/state-of-subscription-apps |
| App Growth Annual 2026 card | https://www.revenuecat.com/blog/company/app-growth-annual-2026 |
| Start for free | https://app.revenuecat.com/signup (stop) |

The same menu also surfaces, from the homepage footer and body, `/why-revenuecat`, `/build-vs-buy`, `/build-on-revenuecat`, `/press-kit`. Careers leaves the site for `jobs.ashbyhq.com/revenuecat` (external, not captured).

## Solutions menu

| Item | Opens |
|---|---|
| Explore Rico | `/feature/ai-agent` |
| Subscriptions | `/feature/infrastructure` |
| In-app currency | `/feature/in-app-currency` |
| Web | `/feature/web` |
| Outage protection | `/feature/reliability` |
| Ad Monetization | `/feature/ad-monetization` |
| Paywalls | `/feature/paywalls` |
| Web-to-app funnels | `/feature/funnels` |
| A/B/n testing | `/feature/experiments` |
| Early Payouts | `/early-payouts` |
| Customer support tools | `/feature/customer-management` |
| Self-serve support UI | `/feature/customer-center` |
| Refund request handling | `/feature/refund-control` |
| Win-back campaigns | `/win-back` |
| Analytics | `/feature/charts` |
| Native integrations | `/integrations` |
| Alerts & app health | `/feature/alerts-app-health` |
| Start for free | signup wall (stop) |

Homepage body and footer add audience pages that this menu does not list: `/for-developers`, `/for-marketing`, `/for-product`, `/support-teams`, `/data-teams`, `/indies`, `/for-startups`, `/for-enterprise`, `/partners`, `/streaming`, `/billing`, `/web-purchase-button`, `/feature/targeting`, `/feature/retention-messaging`.

## Developers menu

| Item | Opens | Stop? |
|---|---|---|
| API reference | `/docs/api-v1` | No. Public docs. |
| Migration guide | `/docs/migrating-to-revenuecat/migration-paths` | No |
| GitHub | https://github.com/RevenueCat | External |
| System status | https://status.revenuecat.com/ | Public status page. Subscribe form is a wall: do not submit. |
| Technical community | https://community.revenuecat.com/ | Public index. Cookie banner hidden, not clicked. Login/signup inside the community is a wall. |
| Sample apps | `/docs/platform-resources/sample-apps` | No |
| SDK install links (iOS, Android, Flutter, React Native, Unity, Roku, Capacitor, macOS, Cordova, Kotlin Multiplatform, All SDKs) | `/docs/getting-started/installation/...` | No |
| RevenueCat Web Billing | `/docs/web/overview` | No |
| Stripe Billing | `/docs/web/integrations/stripe` | No |
| Paddle | `/integrations/revenuecat-paddle` | No |
| All docs / Quickstart | `/docs`, `/docs/welcome/overview` | No |
| Start for free | signup wall | Yes |

Docs chrome, seen on `/docs` (public, separate from the marketing header):

| Control | Opens | Stop? |
|---|---|---|
| Search the docs or ask AI / ⌘K | Search dialog | Open the empty dialog only. Do not type a query that submits, and do not send an AI prompt. |
| Toggle navigation bar | Docs sidebar | No |
| Switch between dark and light mode | Docs theme. Marketing pages have no equivalent. | No. A theme toggle, not an account setting. |
| Sidebar links | Other `/docs/...` pages | No |

## Resources menu

| Item | Opens | Stop? |
|---|---|---|
| Product tutorials | YouTube playlist | External |
| Attend office hours / Office Hours card | https://app.livestorm.co/revenuecat/live-revenuecat-demo?type=detailed | External registration. Do not register. |
| Agency support | `/partners/agency` | No |
| Case studies | `/testimonials` | No |
| Blog | `/blog` | Index is public. Newsletter email field is a wall: do not type or subscribe. |
| Sub Club podcast | https://subclub.com/episodes | External |
| StartApp School | https://www.startapp.school/ | External |
| State of Subscription Apps | `/state-of-subscription-apps` | No |
| Events | `/events` | No |
| App Growth Annual conference | https://appgrowthannual.com/ | External |
| Become a partner | `/partners/technology-partner-program` | Page may contain an application form. Do not fill or submit. |
| Shipaton | https://www.shipaton.com/ | External |
| Start for free | signup wall | Yes |

Footer adds `/glossary`, `/app-store-fee-calculator`, `/reactivation-calculator`, `/app-store-revenue-calculator`, `/contact`. Help center is the community host above.

## Homepage interactions (not navigation)

| Control | Opens |
|---|---|
| Start for free (hero and repeated CTAs) | signup wall (stop) |
| Talk to sales | `/talk-to-sales` (form wall) |
| See the docs | `/docs` |
| Case-study cards (OpenAI, VSCO, Ladder, Runna, Pixery Labs, Pixelcut, Holy Water, PhotoRoom, CardPointers, The Tapping Solution) | `/customers/<slug>` |
| "Go to … testimonial" carousel buttons | Switches the on-page testimonial. Does not navigate. |
| Audience cards (Engineering, Marketing, Product, Support, Data) | The audience pages listed under Solutions |
| Feature links in the lower page (Paywalls, Experiments, Targeting, Charts, Customer center, and the rest of the footer feature list) | The feature URLs above |

No dialog, toast, select, checkbox, radio or switch was on the homepage besides the cookie banner and the nav menus. The homepage has no search field.

## Page families reached from the shell

Captured as representatives, not as every sitemap URL. The sitemap index (`/sitemap.xml`) points at `sitemap-next.xml` (1,254 URLs) and `sitemap-gatsby.xml` (25 URLs). About 807 of those are `/blog` posts and about 267 are `/jp`, `/ko` or `/cat` locale copies.

| Family | Representative | Interactions to open |
|---|---|---|
| Home | `/` | Menus, locale menu, testimonial carousel, mobile menu |
| Why / compare | `/why-revenuecat`, `/build-vs-buy` | In-page anchors if present |
| Audience | `/for-developers`, `/for-enterprise`, `/indies` | Same shell |
| Feature | `/feature/paywalls`, `/feature/charts`, `/feature/experiments` | Same shell |
| Pricing | `/pricing` | In-page tabs: Growth Tools, All features, Testimonials, Certifications, FAQs |
| Sales and contact | `/talk-to-sales`, `/contact` | Record empty fields. Do not type or submit. "What would you like to discuss?" is a select: open it, do not choose a value that submits. |
| Stories | `/testimonials`, one `/customers/openai` | Story cards navigate; do not open external "read on" hosts beyond the first hop if it leaves revenuecat.com |
| Integrations | `/integrations`, one `/integrations/stripe` | Filter or search if it filters locally. Do not submit a partner form. |
| Blog | `/blog` | Search control if it filters the public index without posting an email. Newsletter fields stay empty. |
| Docs | `/docs`, `/docs/welcome/overview` | Search dialog (empty), nav toggle, light and dark |
| Calculators | `/app-store-fee-calculator` | Local controls only. Do not enter an email. |
| Legal | `/terms`, `/privacy` | Static |
| Status | https://status.revenuecat.com/ | Public board. Subscribe is a wall. |
| Changelog | `/changelog` | If the URL 404s, record that and stop. |

## Walls (recorded, branch stopped)

| URL | What it asked for |
|---|---|
| https://app.revenuecat.com/login | An email field with the product's own placeholder, then a password field after an email is entered. Button: Log in. Not typed. |
| https://app.revenuecat.com/signup | Name, email, password, "How did you hear about us?", marketing checkbox. Not typed. |
| https://www.revenuecat.com/talk-to-sales | First name, last name, email, company website, "Tell us more", a discussion select. Not filled. |
| https://www.revenuecat.com/contact | First name, last name, work email, company name, "How can we help?". Not filled. |
| https://www.revenuecat.com/blog (and other pages with the same footer block) | Newsletter email. Not typed. |
| https://status.revenuecat.com/ subscribe | Email plus an OTP field in the page. Not typed. |
| External: Ashby careers, Livestorm office hours, YouTube, Sub Club, StartApp School, App Growth Annual, Shipaton, GitHub, X, Mastodon, App Store, Google Play | Left the product. Not captured. |

## Not a second product

`/jp`, `/ko` and `/cat` are locale copies of the marketing site. The English site is the capture. The locale menu is captured open so the control is evidenced. Docs dark mode is a docs-only theme, not a marketing theme.
