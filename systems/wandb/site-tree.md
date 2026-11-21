# Weights & Biases public site tree

Mapped on 2026-11-21 with headless Playwright, signed out. No email, name, password, or code was typed. No identity provider was clicked. No form was submitted.

The public marketing site is [https://wandb.ai/site](https://wandb.ai/site). The app host is a login wall.

## Roots

| Request | Landed | What happened |
|---|---|---|
| https://wandb.ai/ | https://id.coreweave.com/ | Redirected to a CoreWeave Forge shell. The page title was Forge. No form had painted after 2.5 seconds. Branch stopped. |
| https://wandb.ai/home | https://id.coreweave.com/ | Same redirect. Title Forge. Body text was "W&B". Branch stopped. |
| https://wandb.ai/site | https://wandb.ai/site | Marketing home loaded. Status 200. Dark page, body background rgb(26, 28, 31). |

## Homepage controls

The page has two bars. A CoreWeave bar sits above the Weights & Biases header.

| Control | Opens |
|---|---|
| Logo | https://wandb.ai/site |
| Weave (hover) | Menu. Traces, Evaluations, Playground, Monitors. See [screenshots/home-dark-menu-weave.png](screenshots/home-dark-menu-weave.png). |
| Solutions (hover) | Menu. Use cases, industries, and case studies. See [screenshots/home-dark-menu-solutions.png](screenshots/home-dark-menu-solutions.png). |
| Enterprise (hover) | Menu. Security, Deployment, Performance, Partners, Support. See [screenshots/home-dark-menu-enterprise.png](screenshots/home-dark-menu-enterprise.png). |
| Resources (hover) | Menu. AI SideQuest, Blog, Articles, Podcast, Whitepapers, Events & Webinars, Press. See [screenshots/home-dark-menu-resources.png](screenshots/home-dark-menu-resources.png). |
| Docs | https://docs.wandb.ai/ which redirected to https://docs.coreweave.com/forge-home |
| Pricing | https://wandb.ai/site/pricing-privately-hosted/ (the live href). The older /site/privately-hosted-pricing/ path redirects there. |
| CONTACT | https://wandb.ai/site/contact/ |
| LOG IN | https://id.coreweave.com/login. Login wall. Branch stopped. |
| SIGN UP | https://id.coreweave.com/signup. Signup wall. Branch stopped. |
| GET STARTED WITH WEAVE | https://wandb.ai/site/weave/ |
| REQUEST DEMO | https://wandb.ai/site/contact |
| Announcement close | Dismisses the "sign-in now lives in CoreWeave Forge" dialog. Does not navigate. |
| Sign in to CoreWeave Forge | Login wall. Not followed. |
| Learn more (in the announcement) | Not followed. |
| Contact sales | CoreWeave top bar. The href was not measured. Not followed. |

An announcement dialog covers the hero on first paint. Its close control was clicked. The dialog is public marketing copy, not a credential form.

## Menu destinations

Weave:

- Traces: https://wandb.ai/site/traces/
- Evaluations: https://wandb.ai/site/evaluations/
- Playground: https://wandb.ai/site/playground
- Monitors: https://wandb.ai/site/online-evaluations
- Get started: https://wandb.ai/site/weave/

Solutions, from the open menu and the header markup:

- AI governance, Computer vision, Contact centers, Evaluations, Fine-tune LLMs, Physical AI, RAG, Train LLMs, Quant trading
- Industries: Autonomous Vehicles, Communications, Financial Services, Healthcare & Life Sciences, Public Sector, Scientific Research
- Case studies: https://wandb.ai/site/customers

Enterprise:

- Security: https://wandb.ai/site/security
- Deployment: https://wandb.ai/site/for-enterprise/deployment-options/
- Performance: https://wandb.ai/site/models-performance
- Partners: https://wandb.ai/site/partners
- Support: https://wandb.ai/site/support

Resources:

- AI SideQuest: https://wandb.ai/site/ai-sidequest
- Blog: https://forge.coreweave.com/forge-reports
- Articles: https://wandb.ai/site/articles/
- Podcast: https://wandb.ai/site/resources/podcast/
- Whitepapers: https://wandb.ai/site/resources/whitepapers
- Events & Webinars: https://wandb.ai/site/resources/events/
- Press: https://wandb.ai/site/press-releases/

Footer also links About (https://wandb.ai/site/company/about-us/), Careers, Brand guide (https://wandb.ai/site/brand-identity/), Legal, and language variants at /site/ja/, /site/ko/, and /site/de/.

## Pages photographed

| Page | URL | Width |
|---|---|---|
| Home | https://wandb.ai/site | 1440 and 390 |
| Pricing | https://wandb.ai/site/pricing-privately-hosted/ | 1440 and 390 |
| Contact | https://wandb.ai/site/contact/ | 1440 |
| Weave | https://wandb.ai/site/weave/ | 1440 |
| About | https://wandb.ai/site/company/about-us/ | 1440 |
| Careers | https://wandb.ai/site/careers/ | 1440 |
| Brand guide | https://wandb.ai/site/brand-identity/ | 1440 |
| Security | https://wandb.ai/site/security/ | 1440 |
| Docs | https://docs.coreweave.com/forge-home | 1440 |
| Login wall | https://id.coreweave.com/login | 1440 |
| Signup wall | https://id.coreweave.com/signup | 1440 |

## Phone width

At 390 the marketing header did not expose a named menu button in the accessibility tree. A coordinate click opened the announcement dialog full-screen, not the site nav. The phone nav is not captured. The home and pricing pages were photographed at 390.

## Stopped branches

Login and signup walls are recorded in [login-review.json](login-review.json). Identity providers were visible and were not clicked. The contact form was photographed empty and was not submitted. GET STARTED on the pricing page points at the signup wall and was not followed.
