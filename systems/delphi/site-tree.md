# Delphi public site tree

Captured 2026-11-21, signed out, headless Chromium, desktop 1440x900 and phone 390x844. Start URLs: `https://www.delphi.ai/` and `https://delphi.ai/` both land on `https://www.delphi.co/`. `https://www.delphi.co/` is the public home.

Nothing was typed. No form was submitted. Google, Apple, Facebook, SSO and email-continue buttons were not clicked. Branches that hit a login wall are marked and stopped.

## Two shells

| Shell | Hosts | Painted theme | Header |
|---|---|---|---|
| App | `/`, `/discover/:topic`, `/search/:slug`, `/:profile`, `/:profile/chat`, `/terms`, `/privacy` | Light by default. `prefers-color-scheme: dark` paints a dark page (`rgb(30, 30, 29)` body, measured 2026-11-21). | Logo (home), Sign In (`/auth?callbackUrl=/`), Create Your Delphi (`/onboarding?onboarding=create_cta`) |
| Marketing | `/about`, `/blog`, `/blog/:slug`, `/premium` and children, `/ask`, `/ask/:role`, `/for`, `/for/:role`, `/careers`, `/people`, `/people/:role`, `/press` | Cream (`#fdf6ee`). Dark preference does not restyle it. | Logo (home), Discover, About Delphi, Blog, Premium, Sign in (`/auth`), Sign up (`/auth`). Open menu is in the DOM at 0x0 on desktop; the links are already in the bar. |
| Help | `https://help.delphi.co/` | Cream, same marketing ink. | Search articles (focus only; nothing typed). Open chat was not used. |

## Redirects and walls

| Control or URL | Opens | Stopped |
|---|---|---|
| `https://www.delphi.ai/`, `https://delphi.ai/` | `https://www.delphi.co/` | no |
| `https://www.delphi.ai/login`, `https://www.delphi.co/login` | `https://www.delphi.co/?onboarding=discover` (public home). Sign In in the header still points at `/auth`. | yes for auth; the home itself is public |
| Header Sign In, marketing Sign in, marketing Sign up, footer equivalents | `https://www.delphi.co/auth?callbackUrl=/` which returns to `https://www.delphi.co/?onboarding=discover` | yes. No email field. |
| Header Create Your Delphi, in-page "Create a digital version…" | `https://www.delphi.co/onboarding?onboarding=create_cta` which returns to `https://www.delphi.co/?onboarding=create_cta` | yes. No onboarding form. |
| Marketing My Delphi (`/~`) | `https://www.delphi.co/auth?callbackUrl=%2F~` title Sign in. Continue with Google, Continue with Email. | yes. Login wall. Screenshot [auth-light-login-wall](screenshots/auth-light-login-wall.png). |
| Profile load (`/nireyal` and the same pattern on other profiles) | Same URL plus `?onboarding=profile_gate`, dialog "Sign in to continue with" the expert. Continue with Google, Continue with Email, close. | yes for those buttons. Page behind the scrim is public. Screenshot [profile-light-gate](screenshots/profile-light-gate.png). |

## Home (`/`)

Screenshot [home-light-default-2026-11-21](screenshots/home-light-default-2026-11-21.png), dark [home-dark-default](screenshots/home-dark-default.png), phone [mobile-home-light-default-2026-11-21](screenshots/mobile-home-light-default-2026-11-21.png).

| Control | Opens |
|---|---|
| Logo | `/` |
| Sign In | `/auth?callbackUrl=/` (bounces home; see walls) |
| Create Your Delphi | `/onboarding?onboarding=create_cta` (bounces home) |
| Topic chips (Career, Startups, Productivity, Health, Relationships, Marketing, Sales, Business, Design, Personal Growth, Family, Sports, Leadership, Finance, Parenting, Fitness, Self Esteem, Mindfulness, Social, Engineering, Technology, GTM & Revenue) | `/discover/:slug` for that topic. Career captured: [discover-career-light-default](screenshots/discover-career-light-default.png). The other slugs are the same template. |
| For You, All | Stay on `/` (filter the card row; All was the selected chip) |
| Shuffle topics, Shuffle questions, Shuffle people, Previous people, More people | In-page. They replace the visible card set. No navigation. |
| A situation card ("Ask … about …") | `/search/:slug`. One captured: `/search/family-new-baby` [search-situation-light-default](screenshots/search-situation-light-default.png). Other cards are the same template. |
| Search Delphi textarea, Say your situation, microphone, Cancel recording, Submit recording | In-page composer. Not typed, not submitted. Focus shot was not taken (the locator timed out). |
| Expert name | `/:profile?referral=…` public profile. Captured `/nireyal` and `/dara`. |
| "Ask about …" on an expert card | `/:profile/chat?handoff=…` public chat. Template captured at `/nireyal/chat`. |
| Read [Name]'s perspective | In-page flip. Back to portrait returns it. Screenshot [home-light-perspective-open](screenshots/home-light-perspective-open.png). |
| Learn more about Delphi | `/about` |
| Footer YouTube, Instagram, LinkedIn, X, TikTok | External. Not followed. |
| Footer Blog, Premium, Ask an Expert, Use Cases, Careers | The marketing routes below. |
| Footer Help Center | `https://help.delphi.co/` |
| Footer Terms, Privacy | `/terms`, `/privacy` |

## Discover and search templates

`/discover/:topic` uses the home shell with the topic chip selected. Controls are the same as home. One topic (`/discover/career`) stands for the set.

`/search/:slug` uses the home shell with the situation in the ask field. Save and expand controls, where present, were not pressed (they lead toward an account). One slug stands for the set.

## Profile and chat templates

`/:profile` is a public expert page. Load opens the sign-in dialog (profile gate). Close is present; Google and Email were not clicked. Share, suggested answers, the ask field, Add attachment, Start voice input, Call and Submit message were not used. Two profiles captured (Nir Eyal, Dara Ladjevardian). Other profile URLs linked from home, ask and people are the same template and were not each photographed.

`/:profile/chat` is a public chat: suggested questions, a message field, attachment, voice, call, submit. Nothing was typed or sent. One chat photographed at desktop and phone. The crawl confirmed the same title pattern on other chats (Guillermo Rauch, Natalie Ellis, and others) and stopped after the template was established.

## Marketing pages

Header on each: logo to `/`, Discover to `/`, About Delphi to `/about`, Blog to `/blog`, Premium to `/premium`, Sign in and Sign up to `/auth` (wall, stopped).

| Page | In-page control | Opens | Shot |
|---|---|---|---|
| `/about` | grandfather | `/akbar` (profile template, not separately shot) | [about-light-default](screenshots/about-light-default.png) |
| `/about` | Dara Ladjevardian card | `/dara` | [profile-dara-light-default](screenshots/profile-dara-light-default.png) |
| `/about` | press logos | External articles. Not followed. | |
| `/about` | See open roles | `/careers` | |
| `/blog` | All, Delphi Updates, Editorial, Featured | In-page filter. Editorial captured. | [blog-light-default](screenshots/blog-light-default.png), [blog-light-filter-editorial](screenshots/blog-light-filter-editorial.png) |
| `/blog` | A post card | `/blog/:slug`. One post captured. The index lists many more of the same template. | [blog-post-light-default](screenshots/blog-post-light-default.png) |
| `/premium` | See plans | `/premium/plans` | [premium-light-default](screenshots/premium-light-default.png) |
| `/premium` | Features | `/premium/features` | [premium-features-light-default](screenshots/premium-features-light-default.png) |
| `/premium` | Immortal | `/premium/immortal` | [premium-immortal-light-default](screenshots/premium-immortal-light-default.png) |
| `/premium/immortal` | Talk to us | `/premium/immortal/talk` (a form: name, email, radios, message, Send). Not filled, not sent. | not separately shot; URL recorded |
| `/premium/plans` | FAQ questions | In-page disclosure. Click missed the button this pass; the questions are on the page. | [premium-plans-light-default](screenshots/premium-plans-light-default.png) |
| `/ask` | Ask a founder, Ask a VC, Ask an author, Ask a researcher, Ask a professor, and the role rows | `/ask/:role`. Founders captured. Expert portraits go to `/:profile`. | [ask-light-default](screenshots/ask-light-default.png), [ask-founders-light-default](screenshots/ask-founders-light-default.png) |
| `/for` | Founders on Delphi and the other role rows | `/for/:role`. Founders captured. Portraits go to `/:profile`. | [for-light-default](screenshots/for-light-default.png), [for-founders-light-default](screenshots/for-founders-light-default.png) |
| `/people` | A role | `/people/:role`. Founders captured. The crawl confirmed 26 role pages with the same title pattern (VCs, authors, researchers, professors, athletes, faith, coaches, CEOs, speakers, doctors, lawyers, podcasters, YouTubers, writers, marketers, sales, finance, product, designers, real estate, HR, artists, public service, wellness, journalists). | [people-light-default](screenshots/people-light-default.png), [people-founders-light-default](screenshots/people-founders-light-default.png) |
| `/careers` | See open roles | Same page, plus an external Ashby board (`jobs.ashbyhq.com`). External board not followed. | [careers-light-default](screenshots/careers-light-default.png) |
| `/press` | Play Dara's Training Data episode | In-page player. Not started (a media control, not a navigation). | [press-light-default](screenshots/press-light-default.png) |
| `/terms`, `/privacy` | In-page legal text. Links to external policy sites were not followed. | | [terms-light-default](screenshots/terms-light-default.png), [privacy-light-default](screenshots/privacy-light-default.png) |

Marketing footer, repeated: Help Center (`help.delphi.co`), Immortal, People on Delphi, Ask an Expert, Use Cases, Library of Minds (`libraryofminds.com`, external, not followed), Press, social accounts (external), Terms, Privacy.

## Help center

`https://help.delphi.co/` is a separate origin, cream marketing colours, search field. Focus only. Open chat was not used. Article links inside the center were not walked; the index is the public entry. Screenshot [help-light-default](screenshots/help-light-default.png), focus [help-light-search-focus](screenshots/help-light-search-focus.png).

## Phone

390x844 at 2x. Home, about, blog, premium, premium plans, ask, discover, profile (gate still opens), chat, help, search and people. The marketing header collapses; Open menu is the control that reveals Discover, About, Blog, Premium, Sign in and Sign up. Those links go to the same URLs as desktop. Screenshots are `mobile-*-light-default.png`.

## Not walked

External press, social, Library of Minds, the Ashby careers board, and `docs.delphi.ai` (linked from legal or help copy, not from the header). Individual blog posts, people-role pages, ask-role pages, for-role pages, discover topics, search slugs, profiles and chats beyond the templates above. Each is the same control pattern as the captured example.
