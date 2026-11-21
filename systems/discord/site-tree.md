# Discord public site tree

Mapped signed out from [https://discord.com/](https://discord.com/) on 2026-11-21 with headless Playwright. A control that opens a login, signup, request, or invite wall is recorded and that branch stops. No password, code, phone number, identity provider, or form was submitted.

The marketing site is Webflow. Nav items with a menu open on hover (desktop) as a `.nav_dd_list` overlay. They are not separate pages. Phone width replaces that bar with a Menu button.

## Home, desktop 1440

| Control | Opens |
|---|---|
| Wordmark | [https://discord.com/](https://discord.com/) |
| Download | [https://discord.com/download](https://discord.com/download) |
| Nitro | [https://discord.com/nitro](https://discord.com/nitro) |
| Discover (hover) | Menu overlay. Title link goes to [https://discord.com/servers](https://discord.com/servers). Items: Server Directory ([https://discord.com/servers](https://discord.com/servers)), Trending Games ([https://discord.com/trending-games](https://discord.com/trending-games)) |
| Safety (hover) | Menu overlay. Title link [https://discord.com/safety](https://discord.com/safety). Family Center, Safety Library, Safety News, Teen Charter, Discord Player's Guide, Parent Hub, Policy Hub, Privacy Hub, Transparency Hub, Wellbeing Hub (paths `/safety-family-center`, `/safety-library`, `/safety-news`, `/safety-teen-charter`, `/safety-players-guide`, `/safety-parents`, `/safety-policies`, `/safety-privacy`, `/safety-transparency`, `/safety-wellbeing`) |
| Quests (hover) | Menu overlay. Title [https://discord.com/ads/quests](https://discord.com/ads/quests). Advertising, Success Stories (`/ads/quests-success-stories`), Quests FAQ (`/ads/quests-faq`) |
| Support (hover) | Menu overlay. Help Center ([https://support.discord.com/hc](https://support.discord.com/hc)). Feedback and Submit a Request open support request forms: wall, branch stopped |
| Blog (hover) | Menu overlay. Featured [https://discord.com/blog](https://discord.com/blog). Categories: `/category/community`, `/category/company`, `/category/engineering`, `/category/how-to-discord`, `/category/safety`, `/category/product` |
| Developers (hover) | Menu overlay. Title [https://discord.com/developers](https://discord.com/developers). Integration (`/developers/social-sdk`), Social Commerce (`/developers/social-commerce`), Apps and Activities (`/developers/build`), Developer Newsletter (`/developers/developer-newsletter`), Developer Case Studies (`/developers/success-stories`), Official Game Communities (`/community`), Developer Portal (`/developers/home`), Documentation (`/developers/docs/intro`), Developer Help Center ([https://support-dev.discord.com/hc/en-us](https://support-dev.discord.com/hc/en-us)) |
| Careers | [https://discord.com/careers](https://discord.com/careers) |
| Log In | Wall. [https://discord.com/login](https://discord.com/login). Asks for email or phone and a password, or a QR code or passkey. Branch stopped |
| Download for Mac | Installer URL under `/api/downloads/`. Not followed |
| Open Discord in your browser | Button on the hero. Not followed: the app path redirects to the login wall |

## Home, phone 390

| Control | Opens |
|---|---|
| Menu | Full-screen nav overlay with the same destinations as the desktop bar, nested under Discover, Safety, Quests, Support, Blog, Developers |
| Log In | Same login wall |

## Footer

| Control | Opens |
|---|---|
| Language (English) | Menu overlay of locale names. Choosing a locale was not done |
| Product: Download, Nitro, Status, App Directory, Gift Cards | `/download`, `/nitro`, [https://discordstatus.com/](https://discordstatus.com/) (external), `/application-directory` (redirects to `/discovery/applications`, public app shell, no h1), `/gift-cards` |
| Company: About, Jobs, Brand, Newsroom | `/company`, `/careers`, `/branding`, `/newsroom` |
| Resources: Support, Safety, Blog, Creators, Community, Developers, Quests, Official 3rd Party Merch, Feedback | Support and Safety and Blog and Developers as above. Creators `/creators`. Community `/community`. Merch `discordmerch.com` (external). Feedback is a support request wall |
| Policies: Terms, Privacy, Cookie Settings, Guidelines, Acknowledgements, Licenses, Company Information | `/terms`, `/privacy`, cookie dialog (not opened: a consent control, not clicked), `/guidelines`, `/acknowledgements`, `/licenses`, `/company-information` |
| Social icons | External profiles on X, Instagram, Facebook, YouTube, TikTok. Not identity-provider login buttons |

## Walls (branch stopped)

| Control | URL | What it asked |
|---|---|---|
| Log In, Open in browser, `/app` | [https://discord.com/login](https://discord.com/login) | Email or phone, password, QR code, passkey |
| Sign up (Teen Charter and other CTAs) | [https://discord.com/register](https://discord.com/register) | Create an account: email, display name, username, password |
| Nitro Subscribe, View All Questions | `https://discord.com/login?redirect_to=…` | Same login wall, with a redirect |
| Join the DDevs Server | [https://discord.com/invite/discord-developers](https://discord.com/invite/discord-developers) | Invite wall |
| Feedback, Submit a Request, other "notify us" links | `support.discord.com` and `support-dev.discord.com` `/requests/new` | Support request form. Not submitted |
| Identity provider buttons on the login wall | Google, Apple, and any other provider on that page | Not clicked |

## Pages reached, not photographed as a separate layout

Safety hub children, quest success stories and FAQ, blog categories, developer subpages, one blog post sample, Nitro Rewards (`/nitrorewards`), acknowledgements, licenses, guidelines, privacy, company information. They share the marketing header and footer. Two blog posts were opened as a sample. Further blog posts and server-listing URLs were capped so the crawl would not walk every article.

The signed-in app (channels, settings, store) was not entered.
