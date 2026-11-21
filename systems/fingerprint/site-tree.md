# Fingerprint public site tree

Captured 2026-11-21 from [https://fingerprint.com/](https://fingerprint.com/) with Playwright. Desktop viewport measured 1440 by 900 at device pixel ratio 1. Phone viewport measured 390 by 844 at device pixel ratio 2. No cookie banner appeared, so none was accepted. The walk stopped at the auth wall. `signed_in` is false. See [login-review.json](login-review.json).

The sitemap at `https://fingerprint.com/sitemap-index.xml` lists 940 apex URLs. 599 are blog posts, 150 are bot-directory entries, 101 are Smart Signals explorer entries, and 27 are case studies. Those leaves share the hub chrome. This map records every hub, every header and footer control, and the in-page controls that open a menu, dialog, or page. It does not paste 599 blog titles.

Screenshots live in [screenshots/](screenshots/). Names starting `desktop-` are 1440 by 900. Names starting `phone-` are 390 by 844.

## Header (desktop)

The sticky header is 56px tall. Buttons open a panel. Links navigate.

| Control | Opens |
|---|---|
| Logo | [https://fingerprint.com/](https://fingerprint.com/) |
| Product (button, aria-expanded) | Mega menu. Screenshot: [desktop-menu-product.png](screenshots/desktop-menu-product.png) |
| Use Cases (button) | Mega menu. Screenshot: [desktop-menu-use-cases.png](screenshots/desktop-menu-use-cases.png) |
| Resources (button) | Mega menu. Screenshot: [desktop-menu-resources.png](screenshots/desktop-menu-resources.png) |
| AI | [https://fingerprint.com/ai/](https://fingerprint.com/ai/) |
| Docs | [https://docs.fingerprint.com/](https://docs.fingerprint.com/) |
| Demo | [https://fingerprint.com/demo/](https://fingerprint.com/demo/) |
| Pricing | [https://fingerprint.com/pricing/](https://fingerprint.com/pricing/) |
| Login | [https://dashboard.fingerprint.com/login](https://dashboard.fingerprint.com/login). Auth wall. Stop. |
| Contact Sales | [https://fingerprint.com/contact-sales/](https://fingerprint.com/contact-sales/) |
| Get Started | [https://dashboard.fingerprint.com/signup](https://dashboard.fingerprint.com/signup). Signup wall. Stop. |
| Mobile Menu | Hidden at 1440. Shown at 390. |

### Product menu

| Item | Opens |
|---|---|
| Device Intelligence | [https://fingerprint.com/products/fingerprint-pro/](https://fingerprint.com/products/fingerprint-pro/) |
| Identification | [https://fingerprint.com/products/identification/](https://fingerprint.com/products/identification/) |
| Smart Signals | [https://fingerprint.com/products/smart-signals/](https://fingerprint.com/products/smart-signals/) |
| Fraud Score | [https://fingerprint.com/products/fraud-score/](https://fingerprint.com/products/fraud-score/) |
| Bot Detection | [https://fingerprint.com/products/bot-detection/](https://fingerprint.com/products/bot-detection/) |
| AI Agent Detection | [https://fingerprint.com/products/ai-agent-detection/](https://fingerprint.com/products/ai-agent-detection/) |
| What's new, Fingerprint MCP Server | [https://fingerprint.com/blog/introducing-fingerprint-mcp-server/](https://fingerprint.com/blog/introducing-fingerprint-mcp-server/) |

### Use Cases menu

| Item | Opens |
|---|---|
| Payment Fraud | [https://fingerprint.com/use-cases/payment-fraud/](https://fingerprint.com/use-cases/payment-fraud/) |
| Account Takeover | [https://fingerprint.com/use-cases/account-takeover/](https://fingerprint.com/use-cases/account-takeover/) |
| SMS Fraud | [https://fingerprint.com/use-cases/sms-fraud/](https://fingerprint.com/use-cases/sms-fraud/) |
| New Account Fraud | [https://fingerprint.com/use-cases/new-account-fraud-prevention/](https://fingerprint.com/use-cases/new-account-fraud-prevention/) |
| Device Authentication | [https://fingerprint.com/use-cases/device-authentication/](https://fingerprint.com/use-cases/device-authentication/) |
| Account Sharing Prevention | [https://fingerprint.com/use-cases/account-sharing-prevention/](https://fingerprint.com/use-cases/account-sharing-prevention/) |
| Paywall | [https://fingerprint.com/use-cases/paywall/](https://fingerprint.com/use-cases/paywall/) |
| AI Token Fraud | [https://fingerprint.com/use-cases/ai-token-fraud/](https://fingerprint.com/use-cases/ai-token-fraud/) |
| See all use cases | [https://fingerprint.com/use-cases/](https://fingerprint.com/use-cases/) |
| Fintech | [https://fingerprint.com/industries/fintech/](https://fingerprint.com/industries/fintech/) |
| E-commerce | [https://fingerprint.com/industries/e-commerce/](https://fingerprint.com/industries/e-commerce/) |
| Buy Now Pay Later | [https://fingerprint.com/industries/buy-now-pay-later/](https://fingerprint.com/industries/buy-now-pay-later/) |
| iGaming | [https://fingerprint.com/industries/igaming/](https://fingerprint.com/industries/igaming/) |
| Travel | [https://fingerprint.com/industries/travel/](https://fingerprint.com/industries/travel/) |
| Cryptocurrency | [https://fingerprint.com/industries/cryptocurrency/](https://fingerprint.com/industries/cryptocurrency/) |
| Banking | [https://fingerprint.com/industries/banking/](https://fingerprint.com/industries/banking/) |

### Resources menu

| Item | Opens |
|---|---|
| Resources | [https://fingerprint.com/resources/](https://fingerprint.com/resources/) |
| Bot Directory | [https://fingerprint.com/bot-directory/](https://fingerprint.com/bot-directory/) |
| Blog | [https://fingerprint.com/blog/](https://fingerprint.com/blog/) |
| Events & Webinars | [https://fingerprint.com/events/](https://fingerprint.com/events/) |
| Partners | [https://fingerprint.com/partners/](https://fingerprint.com/partners/) |
| Case Studies | [https://fingerprint.com/case-studies/](https://fingerprint.com/case-studies/) |
| Press | [https://fingerprint.com/resources/press/](https://fingerprint.com/resources/press/) |
| About Us | [https://fingerprint.com/about-us/](https://fingerprint.com/about-us/) |
| Support | [https://fingerprint.com/support/](https://fingerprint.com/support/) |
| Playground | [https://demo.fingerprint.com/playground/](https://demo.fingerprint.com/playground/) |
| Featured report | [https://fingerprint.com/try/device-intelligence-report-2026/](https://fingerprint.com/try/device-intelligence-report-2026/) |

## Header (phone, 390)

The Mobile Menu button opens a full-screen sheet. Screenshot: [phone-mobile-menu.png](screenshots/phone-mobile-menu.png). Close is the X.

| Control | Opens |
|---|---|
| Product | Nested sheet of the Product menu. [phone-menu-product.png](screenshots/phone-menu-product.png) |
| Use Cases | Nested sheet. [phone-menu-use-cases.png](screenshots/phone-menu-use-cases.png) |
| Resources | Nested sheet. [phone-menu-resources.png](screenshots/phone-menu-resources.png) |
| Docs | [https://docs.fingerprint.com/](https://docs.fingerprint.com/) |
| Demo | [https://fingerprint.com/demo/](https://fingerprint.com/demo/) |
| Pricing | [https://fingerprint.com/pricing/](https://fingerprint.com/pricing/) |
| Contact Sales | [https://fingerprint.com/contact-sales/](https://fingerprint.com/contact-sales/) |
| Get Started | Signup wall. Stop. |

Login is not in the phone sheet. It remains on the desktop header.

## Footer

The same footer is on marketing pages. Newsletter email field and Subscribe were not filled and not submitted.

| Column | Control | Opens |
|---|---|---|
| Product | Device Intelligence Platform | [https://fingerprint.com/products/fingerprint-pro/](https://fingerprint.com/products/fingerprint-pro/) |
| Product | Smart Signals | [https://fingerprint.com/products/smart-signals/](https://fingerprint.com/products/smart-signals/) |
| Product | AI Agent Detection | [https://fingerprint.com/products/ai-agent-detection/](https://fingerprint.com/products/ai-agent-detection/) |
| Product | Integrations | [https://fingerprint.com/integrations/](https://fingerprint.com/integrations/) |
| Product | FingerprintJS vs. Pro | [https://fingerprint.com/github/](https://fingerprint.com/github/) |
| Product | Demo | [https://fingerprint.com/demo/](https://fingerprint.com/demo/) |
| Product | Identification | [https://fingerprint.com/products/identification/](https://fingerprint.com/products/identification/) |
| Product | Pricing | [https://fingerprint.com/pricing/](https://fingerprint.com/pricing/) |
| Use cases | New Account Fraud | [https://fingerprint.com/use-cases/new-account-fraud-prevention/](https://fingerprint.com/use-cases/new-account-fraud-prevention/) |
| Use cases | Account Takeover | [https://fingerprint.com/use-cases/account-takeover/](https://fingerprint.com/use-cases/account-takeover/) |
| Use cases | Account Sharing Prevention | [https://fingerprint.com/use-cases/account-sharing-prevention/](https://fingerprint.com/use-cases/account-sharing-prevention/) |
| Use cases | SMS Fraud | [https://fingerprint.com/use-cases/sms-fraud/](https://fingerprint.com/use-cases/sms-fraud/) |
| Use cases | Payment Fraud | [https://fingerprint.com/use-cases/payment-fraud/](https://fingerprint.com/use-cases/payment-fraud/) |
| Use cases | Paywall Enforcement | [https://fingerprint.com/use-cases/paywall/](https://fingerprint.com/use-cases/paywall/) |
| Use cases | AI Token Fraud | [https://fingerprint.com/use-cases/ai-token-fraud/](https://fingerprint.com/use-cases/ai-token-fraud/) |
| Use cases | Device Authentication | [https://fingerprint.com/use-cases/device-authentication/](https://fingerprint.com/use-cases/device-authentication/) |
| Use cases | Bot Detection | [https://fingerprint.com/products/bot-detection/](https://fingerprint.com/products/bot-detection/) |
| Resources | Resource Center | [https://fingerprint.com/resources/](https://fingerprint.com/resources/) |
| Resources | Bot Directory | [https://fingerprint.com/bot-directory/](https://fingerprint.com/bot-directory/) |
| Resources | Blog | [https://fingerprint.com/blog/](https://fingerprint.com/blog/) |
| Resources | Case Studies | [https://fingerprint.com/case-studies/](https://fingerprint.com/case-studies/) |
| Resources | Guides | [https://fingerprint.com/blog/tag/guides/](https://fingerprint.com/blog/tag/guides/) which redirects to [https://fingerprint.com/guides/](https://fingerprint.com/guides/) |
| Resources | FAQ | [https://fingerprint.com/resources/frequently-asked-questions-faqs/](https://fingerprint.com/resources/frequently-asked-questions-faqs/) |
| Resources | Support Center | [https://fingerprint.com/support/](https://fingerprint.com/support/) |
| Resources | Documentation | [https://docs.fingerprint.com/](https://docs.fingerprint.com/) |
| Resources | Build with AI | [https://fingerprint.com/ai/](https://fingerprint.com/ai/) |
| Resources | Tutorials | [https://fingerprint.com/blog/tag/tutorials/](https://fingerprint.com/blog/tag/tutorials/) which redirects to [https://fingerprint.com/tutorials/](https://fingerprint.com/tutorials/) |
| Resources | SDKs and Libraries | [https://fingerprint.com/sdk-libraries/](https://fingerprint.com/sdk-libraries/) |
| Company | About us | [https://fingerprint.com/about-us/](https://fingerprint.com/about-us/) |
| Company | Careers | [https://fingerprint.com/careers/](https://fingerprint.com/careers/) |
| Company | Info for AI Bots | [https://fingerprint.com/blog/ai-info-page/](https://fingerprint.com/blog/ai-info-page/) |
| Company | Press | [https://fingerprint.com/resources/press/](https://fingerprint.com/resources/press/) |
| Company | Partners | [https://fingerprint.com/partners/](https://fingerprint.com/partners/) |
| Company | System status | [https://status.fingerprint.com/](https://status.fingerprint.com/) |
| Company | Security | [https://fingerprint.com/security/](https://fingerprint.com/security/) |
| Legal | Privacy policy | [https://docs.fingerprint.com/docs/privacy-policy](https://docs.fingerprint.com/docs/privacy-policy) |
| Legal | Terms and conditions | [https://docs.fingerprint.com/docs/terms-of-service](https://docs.fingerprint.com/docs/terms-of-service) |
| Social | Discord | [https://discord.gg/ad6R2ttHVX](https://discord.gg/ad6R2ttHVX) (external, not entered) |
| Social | LinkedIn | [https://www.linkedin.com/company/fingerprintjs/](https://www.linkedin.com/company/fingerprintjs/) (external) |
| Social | X | [https://x.com/fingerprintjs](https://x.com/fingerprintjs) (external) |
| Social | GitHub | [https://github.com/fingerprintjs/fingerprintjs/](https://github.com/fingerprintjs/fingerprintjs/) (external) |

## In-page controls on the homepage

The homepage demo paints a live visitor identifier. Those frames are not in this package.

| Control | What it does |
|---|---|
| Prompt | Opens a menu: Prompt, CLI, Skills. [desktop-prompt-menu.png](screenshots/desktop-prompt-menu.png) |
| Install Fingerprint with AI | Copies an install prompt. No form. |
| Claude Code / Codex / Cursor | External agent deep links. Not followed. |
| I'm a developer | Switch. Toggled once to reveal code, then toggled back. No submit. |
| Copy visitor ID | Copies the demo identifier. Not stored here. |
| Newer visit / Older visit | Steps the demo timeline. |
| Your current device / Try trusted device | Switches the demo device. |
| See without Fingerprint | Toggle on the demo scene. |
| Signal chips (Bot Detection, VPN, Suspect Score, and the rest of the Smart Signals list) | Select a signal card in the demo. |
| Signed / Spoofed | Variant buttons on the agent-detection card. |
| Use-case accordion | Account Takeover starts expanded. Payment Fraud, SMS Fraud, and Bot Detection expand in place. |
| Case-study tiles | Booking.com, Dropbox, JumiaPay, Trustpilot stories, plus external company sites. |
| Open the chat | Launcher present. Not submitted. |
| Subscribe to newsletter | Footer form. Not filled. |

## Other public pages reached

Each row was loaded at desktop and phone. Status 200 unless noted. Screenshot names are `desktop-apex-com-<path>.png` and `phone-apex-com-<path>.png`, with slashes turned into hyphens.

| Page | In-page control that changes the view |
|---|---|
| /pricing/ | Plan volume buttons: 20K, 100K, 200K, 500K, 1M+. Compare all features expands the table. [desktop-pricing.png](screenshots/desktop-pricing.png) |
| /bot-directory/ | Search field (placeholder "Search 131 bots") and Filters. Not submitted. [desktop-bot-directory-search.png](screenshots/desktop-bot-directory-search.png). 150 bot pages sit under this hub. |
| /blog/ | Post cards open individual posts. Tags and pagination stay on the blog. 599 posts in the sitemap. |
| /docs.fingerprint.com/ | Search button ("Search... ⌘K") opens search. [desktop-docs-search-open.png](screenshots/desktop-docs-search-open.png). Log In goes to `dashboard.fingerprint.com/mintlify_login`. Stop. Toggle dark mode is present on docs only. Get Started and Dashboard go to the auth wall. |
| /contact-sales/ and /support/ and /subscribe-newsletter/ | Forms present. Not filled. Not submitted. |
| /careers/jobs/ | Job links. No application submitted. |
| /smart-signals-explorer/ | Hub for 101 explorer entries in the sitemap. |
| /case-studies/ | Hub for 27 case studies. |
| /templates/ | Hub for 8 templates. |
| /login/ | 404 marketing page. Not a login form. |
| demo.fingerprint.com/playground | Public playground loaded. Not signed in. |
| status.fingerprint.com | Public status page. "All services are online." |

## Auth wall (branch stopped)

| Control | Result |
|---|---|
| Header Login, Get Started, Get API key, Request API key | [https://dashboard.fingerprint.com/login](https://dashboard.fingerprint.com/login) or `/signup` |
| Continue with Google | Not clicked |
| Continue with GitHub | Not clicked |
| Continue with Microsoft | Not clicked |
| Continue with email | Clicked only to reveal the fields. Email and Password appear. Nothing typed. Not submitted. |
| Forgot password | Not clicked |
| Sign up / Log in cross-links | Recorded. Not used to create an account. |

Screenshots: [desktop-login-wall.png](screenshots/desktop-login-wall.png), [desktop-login-email-form.png](screenshots/desktop-login-email-form.png), [phone-login-wall.png](screenshots/phone-login-wall.png). The signup dialog was also seen and not submitted.
