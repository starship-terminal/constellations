# Cofounder public site tree

Mapped on 2026-11-21 from https://cofounder.co/ in headless Chromium at 1440×900, plus the phone header at 390×844. Every control below was seen. A control that opens the app was followed only far enough to record the login wall. Google, GitHub and Email were not clicked.

The marketing host is https://cofounder.co. The app host is https://app.cofounder.co. Docs live at https://docs.cofounder.co and are a separate Mintlify tree, listed at the end.

## Header (desktop)

The header is `header.site-header`, fixed, 91px tall. "How to" is a span, not a link (`pointer-events-none`).

| Control | Opens |
|---|---|
| Wordmark "Home" | https://cofounder.co/ |
| How to | nothing (label only) |
| Start | https://cofounder.co/how-to/start |
| Build | https://cofounder.co/how-to/build |
| Sell | https://cofounder.co/how-to/sell |
| Scale | https://cofounder.co/how-to/scale |
| Resources | https://cofounder.co/resources |
| Pricing | https://cofounder.co/pricing |
| Run a company | https://app.cofounder.co/os, which redirects to the login wall |

## Header (phone)

"Open menu" is in the header and hidden at 1440. At 390 it opens an overlay and its label becomes "Close menu".

| Control | Opens |
|---|---|
| Open menu | full-screen nav overlay on the same page |
| Close menu | closes that overlay |
| Run a company (in the overlay) | https://app.cofounder.co/os, login wall |
| How to | nothing (label only) |
| Start, Build, Sell, Scale | the four `/how-to/*` chapters |
| Resources | https://cofounder.co/resources |
| Pricing | https://cofounder.co/pricing |
| X | https://x.com/intelligenceco |
| LinkedIn | https://www.linkedin.com/company/the-general-intelligence-company-of-new-york/ |

Screenshot: [screenshots/mobile-home-light-menu-open.png](screenshots/mobile-home-light-menu-open.png).

## Footer

Present on marketing pages. The grass illustration is decoration, not a control.

| Control | Opens |
|---|---|
| How to start | https://cofounder.co/how-to/start |
| How to build | https://cofounder.co/how-to/build |
| How to sell | https://cofounder.co/how-to/sell |
| How to scale | https://cofounder.co/how-to/scale |
| Homepage | https://cofounder.co/ |
| Resources | https://cofounder.co/resources |
| Pricing | https://cofounder.co/pricing |
| Careers | https://generalintelligencecompany.com/careers |
| Privacy Policy | https://cofounder.co/privacy-policy |
| Terms of Service | https://cofounder.co/terms |
| Docs | https://docs.cofounder.co/cli, which redirects to https://docs.cofounder.co/introduction |
| Support | https://cofounder.co/support |
| X | https://x.com/intelligenceco |
| LinkedIn | https://www.linkedin.com/company/the-general-intelligence-company-of-new-york/ |
| Altalogy | https://www.altalogy.com/?rel=gic-cofounder |
| Run a company | https://app.cofounder.co/os, login wall |

## Home, https://cofounder.co/

| Control | Opens |
|---|---|
| Run a company (hero and later sections) | https://app.cofounder.co/os, login wall |
| Copy Setup Prompt | copies a setup prompt to the clipboard. Stays on the page. No dialog and no toast were found. |
| View Cofounder case studies | https://cofounder.co/resources |
| LearnPath, Valence OS | https://cofounder.co/resources (case-study anchors on that index) |
| Start in Cofounder | https://app.cofounder.co/os, login wall |
| Put the guide to work | https://app.cofounder.co/os, login wall |
| Chapter cards (I to IV) | `/how-to/start`, `/how-to/build`, `/how-to/sell`, `/how-to/scale` |
| Download full guide | https://cofounder.co/guides/cofounder-founder-guide.pdf |
| 1.1 Business positioning through 3.4 Recurring workflows | a `[role=dialog]` on the same page. Close control: "Close capability details". |
| Dialog link "Do this in Cofounder" | https://app.cofounder.co/os, login wall |
| Dialog link on 3.1 "Read the Cofounder + Ramp announcement" | https://cofounder.co/resources/cofounder-partners-with-ramp-to-offer-incorporation |
| View details | in-page detail for the email preview. No navigation. |
| You stay in control… / Run multiple tasks… / Customize agents… | in-page tabs (`aria-pressed`). No navigation. |
| Enrich contacts, Research contacts, Send Outreach Emails, Campaigns | in-page workflow tabs. No navigation. |
| Previous, Next | in-page carousel. No navigation. |
| Previous campaign, Next campaign | in-page campaign carousel. No navigation. |

Capability buttons seen: 1.1 Business positioning, 1.2 Brand identity, 1.3 Marketing website, 1.4 Launch content, 2.1 Customer research, 2.2 Prospect discovery, 2.3 Email outreach, 2.4 Marketing and Newsletters, 3.1 LLC incorporation, 3.2 Product analytics, 3.3 Customer support, 3.4 Recurring workflows.

## Pricing, https://cofounder.co/pricing

| Control | Opens |
|---|---|
| Plan card "Get started" | https://app.cofounder.co/, login wall |
| FAQ buttons | expand the answer on the page. Questions: What does the subscription include?, Do unused credits roll over?, Will I need more than $40/month in credits?, Is my AI agent subscription included?, What can I spend credits on?, Does hosting have an ongoing cost?, Can I use Cofounder with an existing codebase? |

## Resources, https://cofounder.co/resources

Article cards open these posts. No other in-page controls.

| Card | Opens |
|---|---|
| Cofounder and Ramp bring incorporation to founders | https://cofounder.co/resources/cofounder-partners-with-ramp-to-offer-incorporation |
| Yohei Nakajima is building ActiveGraph with Cofounder | https://cofounder.co/resources/yohei-nakajima-activegraph-cofounder |
| Daria Ansh, Founder of Veery | https://cofounder.co/resources/daria-ansh-veery-safer-cosmetic-dentistry |
| Announcing Cofounder 2 | https://cofounder.co/resources/introducing-cofounder-2 |
| An Update on Cofounder 1 | https://cofounder.co/resources/an-update-on-cofounder-1 |
| Agent-Native Engineering | https://cofounder.co/resources/agent-native-engineering |
| Announcing Cofounder 1.5 | https://cofounder.co/resources/cofounder-1-5-seed-round |
| A Day in the Life of the World's Most AI Forward Company | https://cofounder.co/resources/a-day-in-the-life-of-the-worlds-most-ai-forward-company |

That last post is hosted as a page on the General Intelligence Company site (header links go to generalintelligencecompany.com). It was not walked past the first paint.

## How-to chapters

https://cofounder.co/how-to redirects to https://cofounder.co/how-to/start. Each chapter has the same chrome plus a contents list of buttons that scroll within the chapter, and "Download guide" to https://cofounder.co/guides/cofounder-founder-guide.pdf. "Run a company" in the chapter header opens the login wall.

Contents buttons on Start: Introduction, Should You Start a Company?, How to Come Up With Startup Ideas, Evaluate Startup Ideas, Pick a Wedge Market, Pick a Name and Domain, Take the Leap, Come up with a spec, and further section buttons (40 buttons on the page, including the shared chrome).

Build also links out to GitHub's getting-started docs, Vercel, Stripe, Postmark and Sentry. Those are external references in the chapter text.

## Students, https://cofounder.co/students

| Control | Opens |
|---|---|
| Run a company, Start building, Read the guide, View pricing, both plan cards | https://app.cofounder.co/edu, login wall |
| FAQ buttons | expand on the page: Do I need to know how to code?, Can I use Cofounder with a student team?, Is this only for software startups?, What should I start with? |

## Incorporation, https://cofounder.co/incorporation

| Control | Opens |
|---|---|
| Start incorporating | https://app.cofounder.co/, login wall |
| View Ramp offer | https://ramp.com/partners/cofounder |
| Read the announcement | the Ramp resource post above |
| FAQ buttons | expand on the page |

## Support, privacy, terms

| Page | Controls beyond the shell |
|---|---|
| https://cofounder.co/support | a mailto link to the published support address, and a link to docs.cofounder.co. No form. |
| https://cofounder.co/privacy-policy | shell only |
| https://cofounder.co/terms | shell only |

## Alternatives

Fourteen pages under https://cofounder.co/alternatives/, all in the sitemap. Each uses the same shell. In-page links:

| Control | Opens |
|---|---|
| Run a company (header and footer) | https://app.cofounder.co/os with utm params, login wall |
| Hero, comparison and final CTAs (Try Cofounder, Get Cofounder, Add Cofounder, Get started) | https://app.cofounder.co/ with utm params, login wall |
| Setup guide | https://docs.cofounder.co/cli/get-started/connect-an-agent |
| Sibling alternative pages | other `/alternatives/cofounder-vs-*` URLs |
| Competitor pricing links | the other product's public site |

Slugs: polsia, lovable, replit, flutterflow, bolt, v0, claude-code, cursor, codex, ai-sdr, ai-cmo, base44, locus, naive.

## Login wall

https://app.cofounder.co/os, https://app.cofounder.co/, and https://app.cofounder.co/edu all redirect to https://app.cofounder.co/os/login (the first adds `?next=%2F`).

Seen, not clicked:

| Control | Asks for |
|---|---|
| Continue with Google | Google. Not opened. |
| Continue with GitHub | GitHub. Not opened. |
| Continue with Email | an email step that is not on screen until clicked. Not opened. No email field is visible. |
| Privacy Policy | https://cofounder.co/privacy-policy |
| Terms of Service | https://cofounder.co/terms |
| CofounderOS wordmark | stays on the login page |

Recorded in [login-review.json](login-review.json). Screenshots: [screenshots/login-light-default.png](screenshots/login-light-default.png), [screenshots/mobile-login-light-default.png](screenshots/mobile-login-light-default.png).

## Docs, https://docs.cofounder.co

Footer "Docs" lands on https://docs.cofounder.co/introduction. This tree was listed, not captured as the design system. Visible chrome: search ("Search documentation…"), light/dark switch ("Switch to dark mode"), a copy button on code samples, and a sidebar of guide, reference, cookbook and dashboard links. "Dashboard" and any link to https://app.cofounder.co/os are the login wall. The sidebar also has a mailto to the published support address.

## Not in the tree

No newsletter form, no onboarding, no account creation form, and no email field on the first login screen. Signed-in product UI was not entered.
