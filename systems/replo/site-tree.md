# Replo public site tree

Mapped on 2026-11-21 from https://www.replo.app/ in headless Chromium (Playwright), desktop 1440×900, before screenshots. Phone shots at 390×844 were taken after this map. The homepage loaded (HTTP 200, title "Replo: AI website builder to launch and grow a business"). `replo.app` redirects to `www.replo.app`. The painted surface is one dark theme: `color-scheme: dark`, body background `rgb(0, 0, 0)`, `<meta name="theme-color" content="#000000">`. No theme toggle was found.

Nothing in this map was submitted. Login and signup URLs were opened only to record the wall, then the branch stopped. No password, code, Google, or Apple control was used. No newsletter, profile, birthday, plan, survey, or onboarding field was filled.

## Chrome that repeats on every marketing page

| Control | Opens |
|---|---|
| Logo "Home" | https://www.replo.app/ |
| Nav link "Customers" | https://www.replo.app/case-studies |
| Nav link "Pricing" | https://www.replo.app/pricing |
| Nav button "Product" (`aria-expanded`, popup) | Product menu, listed below. Escape closes it. |
| Nav button "Solutions" | Solutions menu, listed below. Escape closes it. |
| Nav button "Resources" | Resources menu, listed below. Escape closes it. |
| Header link "Log in" | https://dashboard.replo.app/ (redirects to signup). Auth wall. Branch stops. |
| Header link "Start for free" | https://dashboard.replo.app/auth/signup. Auth wall. Branch stops. |
| Header link "Book a demo" | https://www.replo.app/contact |
| Phone control `aria-label="Open menu"` | Same three menus plus the header links, as a drawer. |
| Footer columns | Repeat the resource, product, legal, and social links below. |

## Product menu

| Item | Opens |
|---|---|
| Website Builder | https://www.replo.app/website-builder |
| Landing Page Builder | https://www.replo.app/landing-page-builder |
| Import from Figma | https://www.replo.app/figma-to-website |
| Heatmaps | https://www.replo.app/heatmaps |
| A/B Testing | https://www.replo.app/ab-testing |
| Industry Benchmarks | https://www.replo.app/analytics/ecommerce |
| Ad Library | https://www.replo.app/ad-library |
| AI Ad Builder | https://www.replo.app/examples/ads |
| Competitive Analysis | https://www.replo.app/competitor-analysis |
| Global Business Leaderboard | https://www.replo.app/reports/top-brands |
| Daily Analytics Report | https://www.replo.app/automated-reports |
| Daily CRO Report | https://www.replo.app/ai-analyst |
| Daily Competitor Watch | https://www.replo.app/automations |
| Claude | https://www.replo.app/claude |
| ChatGPT | https://www.replo.app/chatgpt |
| Codex | https://www.replo.app/codex |
| All products | https://www.replo.app/products |
| Preview card (analytics demo) | https://www.replo.app/analytics |
| Preview card (ad research) | https://www.replo.app/ad-library |

## Solutions menu

| Item | Opens |
|---|---|
| Brands | https://www.replo.app/partners/brands |
| Agencies | https://www.replo.app/partners/agencies |
| Performance marketers | https://www.replo.app/partners/performance-marketing |
| CRO teams | https://www.replo.app/partners/cro |
| Shopify Partners | https://www.replo.app/partners/shopify |
| Online stores | https://www.replo.app/ai-store-builder |
| Software and SaaS | https://www.replo.app/solutions/saas |
| Apps | https://www.replo.app/solutions/apps |
| Digital products | https://www.replo.app/solutions/digital-products |
| Service businesses | https://www.replo.app/solutions |
| Book a demo | https://www.replo.app/contact |
| Customer stories | https://www.replo.app/case-studies |

## Resources menu

| Item | Opens |
|---|---|
| Docs | https://docs.replo.app/ (external docs host; linked, not walked as the marketing tree) |
| Blog | https://www.replo.app/blog |
| Guides | https://www.replo.app/guides |
| ChatGPT ads | https://www.replo.app/guides/chatgpt-ads |
| Compare platforms | https://www.replo.app/compare |
| Glossary | https://www.replo.app/glossary |
| Templates | https://www.replo.app/templates |
| Use cases | https://www.replo.app/use-cases |
| Integrations | https://www.replo.app/integrations |
| Free tools | https://www.replo.app/tools |
| Experts | https://www.replo.app/experts |
| Reports | https://www.replo.app/reports |
| Top brands | https://www.replo.app/reports/top-brands |
| Brand ads | https://www.replo.app/examples/ads |
| Landing page examples | https://www.replo.app/examples/landing-pages |
| UGC ads | https://www.replo.app/examples/ugc-ads |

## Homepage interactions (local, no navigation)

| Control | What it does |
|---|---|
| Prompt chips (Build websites, Build landing pages, Sell products, Launch ads, Track analytics, Research competitors, Manage branding, Manage orders, Automate reports) | Fill the on-page prompt. Not submitted. |
| "Add to ChatGPT / Claude" | Closed button on the hero. Not opened into an account flow. |
| Replo / ChatGPT / Claude segment | Local tab on the hero demo. |
| Accordions ("Build from anything you have", "Copy any website on the internet", "Buy a domain directly in Replo", and the research/experiment groups) | Expand a panel in place. "Learn more" inside a panel is a normal page link (website-builder, pricing, research, analytics, ab-testing, integrations, and the use-case pages). |
| "Get started for free" | https://dashboard.replo.app/auth/signup. Auth wall. Branch stops. |

## Auth walls (recorded, then stopped)

| Request | Result |
|---|---|
| https://www.replo.app/login | HTTP 404. Title "404 \| Page Not Found". Marketing chrome still paints. Known probe confirmed. |
| https://replo.app/login | Redirects to the same 404. |
| https://dashboard.replo.app/auth/login | HTTP 200. Title "Dashboard - Replo". Heading "Welcome back to Replo". Email field, password field, "Forgot password?", "Sign in", "Continue with Google", link to sign up. Branch stops. Not filled. Google not clicked. |
| https://dashboard.replo.app/ | Redirects to https://dashboard.replo.app/auth/signup. Heading "Let's create your account". Email, password, "Continue", "Continue with Google", link to sign in. Branch stops. |
| https://dashboard.replo.app/auth/signup | Same signup wall. Branch stops. |

## Sitemap shape

https://www.replo.app/sitemap.xml listed 587 URLs on 2026-11-21 (lastmod 2026-11-20). Counts by first path segment: guides 122, examples 89, blog 70, tools 67, integrations 33, compare 31, reports 30, template 24, glossary 20, case-study 19, use-cases 11, claude 11, experts 8, solutions 8, plus the product and legal pages. Article, integration, case-study, and tool leaves share the marketing shell. The capture visits one of each family at 1440×900 and at 390×844, not every leaf. Product, Solutions, and Resources menus were opened on desktop. The phone drawer was opened on the home page.

Legal and company pages linked from the footer and sitemap: `/privacy`, `/terms`, `/partner-terms`, `/careers`, `/engineering`, `/site-map`, `/dpa.pdf`, `/subprocessors.pdf`.

## External links (not walked)

Twitter, LinkedIn, YouTube, a Pocket Casts episode, Facebook Ads Library, Triple Whale, and `mailto:` support. Docs live at https://docs.replo.app/.
