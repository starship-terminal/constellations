# Claude public site tree

Mapped on 2026-11-22 from [https://claude.ai](https://claude.ai) and [https://claude.com](https://claude.com), logged out, in an incognito tab. `https://claude.ai/` redirects to `https://claude.ai/login`. That page is both the empty sign-in wall and the public homepage: a hero, plan cards, an FAQ, and a footer. The marketing site lives on `claude.com`.

`document.documentElement` on claude.ai had `data-mode="system"` and `data-theme="claude"`, and the page painted dark (`color-scheme: dark`). claude.com had `color-scheme: normal` and a near-black page (`rgb(20, 20, 19)`).

A cookie banner exists in the claude.ai DOM (Customize, Reject all cookies, Accept all cookies). It was not on screen. Accept all was not clicked. No account setting was changed.

Nothing was typed. Google and Apple were not clicked. Continue with email and Continue with SSO were not clicked. No form was submitted. No captcha was solved. Try Claude, Login, and plan checkout links were not followed into a signed-in thread. Contact sales was not submitted.

Desktop CSS viewport measured `innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 2. Phone CSS viewport measured `innerWidth` 390, `innerHeight` 844, `devicePixelRatio` 2.

## claude.ai homepage (the login wall)

Present on [https://claude.ai/login](https://claude.ai/login). There is no separate signup URL. Sign up and log in are the same empty wall.

| Control | Opens |
|---|---|
| Claude wordmark | https://claude.ai/ (returns to this page) |
| Continue with Google | An identity provider. Not clicked. |
| Continue with Apple | An identity provider. Not clicked. |
| Email field | Empty. Placeholder `Enter your email`. Nothing typed. |
| Continue with email | Would start the email step. Not clicked. |
| Continue with SSO | Present in the DOM, not on screen at 1440. Not clicked. |
| Privacy Policy | https://www.anthropic.com/legal/archive/baeb68ac-c81c-4931-9539-58f46b6f090c (off the product host). Not followed. |
| Download desktop app | A download control on the page. Not clicked, so no installer started. The public download page was opened from the footer instead. |
| Plan type, Individual / Team and Enterprise | A radio group on the same page. Individual was already selected. Team and Enterprise was not switched. |
| Try Claude, on a plan card | Stays a button on this page. Not clicked. |
| FAQ rows | What is Claude and how does it work, What should I use Claude for, How much does it cost to use. Left closed. |

## claude.com header, desktop

Present on pricing, download, and the product overview.

| Control | Opens |
|---|---|
| Claude wordmark | https://claude.com/ |
| Product | A menu: Claude, Claude Code, Claude Cowork, Claude Duet, Claude Platform, Claude Tag, Claude Security, Claude Science, Artifacts, Design, Connectors, Plugins, Skills, Claude in Chrome, Claude for Google Workspace, Claude for Microsoft 365, Mythos (including Fable), Opus, Sonnet, Haiku, Import to Claude. |
| Developers | A menu: Claude Code, Claude Platform, Code Review, Managed Agents, Claude Academy, Community, Developer blog, plus docs and Console. |
| Enterprise | A menu: Overview, Claude Code for Enterprise, Claude Platform, AI Agents, Coding, Commerce, Customer support, Cybersecurity, Legal, Sales, and industry pages (Financial advisors, Financial services, Government, Healthcare, Higher education, K-12 teachers, Life sciences, Nonprofits). |
| Resources | A menu that includes Resources, plus Customers, the marketplace, and Contact sales. |
| Pricing | A menu: the pricing page, and an API anchor (`/pricing#api`). |
| Login | A redirect on claude.ai whose URL carries a tracking id (`/redirect/claude_com.v1.…/login`). Not clicked. The clean login URL was opened instead. |
| Contact sales | https://claude.com/contact-sales. Not opened. No form was submitted. |
| Try Claude | A redirect into claude.ai. Not clicked. |
| Explore here | A breadcrumb control under the header. Not used to start an account. |

## Phone

At 390, claude.ai still shows the login wall, stacked: wordmark, headline, Google, Apple, empty email, Continue with email, then plan cards. claude.com hides the desktop menus behind one control.

| Control | Opens |
|---|---|
| Toggle menu | A full-screen drawer: Product, Developers, Enterprise, Resources, Pricing (each with a plus), Login, Contact sales, Try Claude. Closed with the X. |
| Explore here | The same breadcrumb control, on the pricing page. |

## Walls this pass does not enter

| Control | Why it stops |
|---|---|
| Continue with Google | Identity provider. Not clicked. |
| Continue with Apple | Identity provider. Not clicked. |
| Continue with email | The email field was empty. The button was not clicked, so no password or code step appeared. |
| Continue with SSO | Not clicked. |
| Login on claude.com | Its href is a redirect URL with a tracking id. Not clicked. The wall was photographed at https://claude.ai/login. |
| Try Claude | Leads toward an account. Not clicked. |
| Contact sales | A form. Not opened and not submitted. |
| Download for macOS / Windows | Installer links on the download page. Not clicked. |

## Pages opened from the tree

| Control | Landed | Shot |
|---|---|---|
| Homepage | https://claude.ai/login | screenshots/public/home-dark-desktop.png |
| Same page, the empty wall | https://claude.ai/login | screenshots/public/login-wall-dark-desktop.png |
| Pricing, from the footer | https://claude.com/pricing | screenshots/public/pricing-dark-desktop.png |
| Download app, from the footer | https://claude.com/download | screenshots/public/download-dark-desktop.png |
| Claude, from the footer Products column | https://claude.com/product/overview | screenshots/public/product-dark-desktop.png |
| Phone homepage | https://claude.ai/login at 390 | screenshots/public/home-dark-phone.png |
| Phone pricing | https://claude.com/pricing at 390 | screenshots/public/pricing-dark-phone.png |
| Phone menu | same pricing page, drawer open | screenshots/public/menu-dark-phone.png |
