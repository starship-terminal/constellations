# Reown site tree

Mapped on 2026-11-21 from the public homepage at https://reown.com/ in headless Chromium (Playwright), desktop 1440×900 and phone 390×844. No form was submitted. No password, code, or newsletter field was filled. Login and signup branches stop at the wall.

The marketing site is one Next.js app. Docs, the AppKit demo, status, and the dashboard are separate hosts. The homepage nav and the footer are the source of reachable pages. The sitemap (https://reown.com/sitemap.xml, 165 URLs, lastmod 2026-10-12) also lists older solution URLs that the live nav no longer links.

| Mark | Meaning |
|---|---|
| [x] | Opened. Children listed. |
| [auth] | Opens a login or signup wall. URL recorded. Branch stopped. |
| [form] | A form. Listed. Not submitted. Fields not filled. |
| [external] | Leaves the Reown product hosts. Listed. Not opened. |
| [same] | Opens a page already in this tree. |

## Tree

- [x] Home https://reown.com/ (200, "Infrastructure for blockchain app development")
  - Header (fixed, about 64px). Desktop shows the logo, Navigation Toggle, Learn, Docs, Demo, Log in. Phone shows the logo and Navigation Toggle only. Learn, Docs, Demo, Log in and Pricing sit inside the overlay.
  - [x] Navigation Toggle (button, aria-label "Navigation Toggle") opens the nav overlay on the same URL. Same control at 390.
    - [x] Solutions (button, aria-expanded) opens an in-overlay list
      - [x] Analytics → /solutions/analytics
      - [x] Authentication → /solutions/authentication
      - [x] Transactions → /solutions/transactions
    - [x] Use Cases (button) opens an in-overlay list
      - [x] DeFi → /use-cases/defi
      - [x] Marketplaces → /use-cases/marketplaces
      - [x] Gaming → /use-cases/gaming
      - [x] Social → /use-cases/social
    - [x] Pricing → /pricing
    - [x] Company (button) opens an in-overlay list
      - [x] About Us → /about-reown
      - [x] Blog → /blog
      - [x] Careers → /careers
    - [x] Learn → /learn
    - [x] Docs → https://docs.reown.com/ (other host)
    - [x] Demo → https://demo.reown.com/ (other host)
    - [auth] Log in → https://cloud.reown.com/sign-in, which redirects to https://dashboard.reown.com/sign-in. Email and password fields, Continue with Google, Sign In. Stopped. Not filled. Google not clicked.
  - [x] Hero
    - [auth] Start building → https://cloud.reown.com/sign-up (signup wall). Stopped.
    - [x] Explore Plans → /pricing
  - [x] Announcement bar ("State of DeFi 2026")
    - [x] Download now → /state-of-defi-2026
    - [x] Close announcement (button, aria-label "Close announcement") dismisses the bar on this page. Not a form.
  - [x] Solution cards
    - [x] Explore Authentication → /solutions/authentication
    - [x] Explore Payments → /solutions/transactions
    - [x] Explore Analytics → /solutions/analytics
  - [x] Use-case cards
    - [x] Learn more → /use-cases/defi, /use-cases/social, /use-cases/marketplaces, /use-cases/gaming
  - [external] WalletConnect "Learn More" → https://walletconnect.network/
  - [x] Article cards (three posts) and More articles → /blog and individual posts
  - [auth] Bottom Start building → https://cloud.reown.com/sign-up. Stopped.
  - [x] Contact sales (button) opens a HubSpot contact dialog on the same URL (name, email, telegram, company-size radios, message, newsletter checkbox, submit). [form] Not filled. Not submitted.
  - [form] Footer "Subscribe to our newsletter" (email placeholder "Mail", submit). Not filled. Not submitted. The same field appears on the /login 404.
  - Footer links, same host: Dashboard [auth], Docs, Learn, Status, Bug Bounty (/security), FAQ, Analytics, Authentication, Transactions, Compliance, DeFi, Gaming, Marketplaces, Social, Terms, Privacy, Cookie Policy, About Us, Pricing, Blog, Careers, Contact, logo → /reown-sdk
  - [external] Footer: GitHub (github.com/reown-com), X, LinkedIn, YouTube, Farcaster, Media Kit (Google Drive), walletconnect.com privacy

- [x] Pricing https://reown.com/pricing (200)
  - Plan cards. [auth] "Build with starter" → https://dashboard.reown.com (redirects to /sign-in). Stopped.
  - [external] Contact sales link → https://share.hsforms.com/... (HubSpot). The in-page Contact sales button is the same dialog as home. [form] Not submitted.
  - [x] FAQ accordions (switch plans, MAU, RPC limits, billing, annual discounts). See all FAQs → /faq
  - Docs links to Reown Auth on docs.reown.com

- [x] Learn https://reown.com/learn (200, h1 "Reown Learn")
  - [x] Filter chips: All, Tron Ecosystem, Solana Ecosystem, Reown Tools, How to build, EVM Ecosystem, Bitcoin Ecosystem, About Blockchain App Development. Local filter. Not a form submit.
  - [x] Load more reveals more cards on the same page.
  - [x] Article cards → /learn/<slug> (example: /learn/what-are-erc-token-standards)

- [x] Solutions
  - [x] /solutions/analytics (h1 Analytics). FAQ accordions. Contact sales [form].
  - [x] /solutions/authentication (h1 Authentication). FAQ accordions. Contact sales [form].
  - [x] /solutions/transactions (h1 Transactions). FAQ accordions. Contact sales [form].
  - [x] /solutions/compliance (footer only, not in the nav overlay). Contact sales [form].
  - Sitemap-only, not in the live nav (still 200 if requested): /solutions/defi, /solutions/payments, /solutions/gaming, /solutions/marketplaces, /solutions/social, /solutions/reown-sdk. The live site points those topics at /use-cases/* and /reown-sdk.

- [x] Use cases
  - [x] /use-cases/defi (h1 DeFi App Development). FAQ accordions. Announcement bar. Contact sales [form].
  - [x] /use-cases/marketplaces
  - [x] /use-cases/gaming
  - [x] /use-cases/social

- [x] Company
  - [x] /about-reown (h1 "The future of finance is onchain")
  - [x] /blog. Filter chips: All, Reports, Product Updates, Partnership, Industry, Events, Company update, Case Study. Load more. Cards → /blog/<slug>
  - [x] /careers. [external] Open roles and Apply now → https://apply.workable.com/walletconnect/. Not opened.
  - [x] /contact (footer). Contact sales button opens the same HubSpot dialog. [form] Not submitted. No other fields on the page itself besides the footer newsletter.

- [x] Other marketing pages linked from home or footer
  - [x] /faq. Long accordion list.
  - [x] /security (Bug Bounty). [external] Submit Report leaves the page (security report). Not submitted.
  - [x] /reown-sdk (footer logo). Contact sales [form].
  - [x] /state-of-defi-2026. Download now is a file/download control on that page. Not treated as a form submit.
  - [x] /privacy-policy, /terms-of-service, /cookie-policy
  - [x] /login is a 404 ("Sorry, we can't find the page you're looking for") with the footer newsletter email field. Known probe. [form] Not submitted.

- [x] Docs https://docs.reown.com/ (200, Mintlify, h1 Quickstart). Separate product chrome. Theme menu: System, Light, Dark. Default observed: light.
  - [x] Search button ("Search... ⌘K") opens a search dialog. Not submitted.
  - [x] Ask Assistant (⌘I) opens an assistant panel with an "Ask a question..." field and Send. [form] Not sent.
  - [x] Change theme preference opens a menu (System / Light / Dark). Selecting Light or Dark is a theme switch, not a form.
  - [x] Sidebar groups (collapsed buttons): AppKit, Pricing Plans, Authentication, Smart Accounts, Fund wallets, EVM Chains, Solana, Bitcoin, Other Network Settings, Security, and more. Expanding a group reveals doc links on docs.reown.com.
  - [x] On this page: table of contents, Open in ChatGPT, More actions, Yes/No feedback. Feedback not submitted.
  - [auth] Reown Dashboard link → https://dashboard.reown.com/ (sign-in). Stopped.
  - [same] AppKit Demo → https://demo.reown.com/
  - [external] System Status → https://status.walletconnect.com/
  - [x] One inner page captured for component states: /appkit/overview

- [x] Demo https://demo.reown.com/ (200, dark page, "Reown Demo"). Public AppKit playground. Not a signed-in dashboard.
  - [x] Tabs: Auth, Features, Design
  - [x] Auth: connect-option checkboxes (Email, Social, Wallet), Layout "Collapse wallets", Chains "Open networks" (opens a network list on the page)
  - [x] Features tab: feature toggles on the same page
  - [x] Design tab: Mode Light/Dark, Font choices (Inter, Noto Sans, Domine, EB Garamond, Bree Serif, Bellota), Radius steps (S, M, L, XL), Accent, Background. Local preview controls.
  - [x] Share and Reset are local demo controls. Share was not used to post anywhere.
  - [x] Get started opens the AppKit connect modal on the demo page (wallet list). Not a Reown account form. No wallet connected. Google and Apple not clicked.
  - [x] Read our docs → docs.reown.com

- [x] Status https://status.reown.com/ (200, "Reown Status")
  - [form] Subscribe to updates opens an email and OTP dialog. Not filled. Not submitted.
  - Component "?" buttons expand status details on the page.

- [auth] Dashboard https://dashboard.reown.com/ and https://cloud.reown.com/sign-in both land on https://dashboard.reown.com/sign-in. Cookie banner (Cookie Policy, Preferences, Accept) was not clicked. Continue with Google not clicked. Sign In not clicked. Branch stopped.

## Themes and widths

| Surface | Themes observed | Widths |
|---|---|---|
| reown.com marketing | One theme. Section skins (`theme--blue`, `theme--white`, `theme--black`, `theme--grey*`, `theme--orange`, `theme--green`) recolor a block. `prefers-color-scheme: dark` did not change the page. | 1440×900 and 390×844 |
| docs.reown.com | Light (default), Dark, System, from the theme menu | 1440×900 and 390×844 |
| demo.reown.com | Dark page. Design tab can preview Light or Dark inside the widget | 1440×900 and 390×844 |
| status.reown.com | One light status theme | 1440×900 |
| dashboard.reown.com | Sign-in only. Not captured past the wall | not captured |
