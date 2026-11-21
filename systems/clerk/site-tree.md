# Clerk public site tree

Mapped from https://clerk.com/ on 2026-11-22, signed out, in headless Chromium at 1440×900 and 390×844. The homepage returned 200. The title was "Clerk | Authentication and User Management". The first heading was "Everything you need for authentication". This is a live marketing site, not a parked domain.

The painted marketing theme is light on the homepage (`color-scheme: normal`, body `#f7f7f8`). Pricing and the company page paint a dark field (`#131316`). Docs paint a white field. There is no theme switch on the public site.

Nothing was typed. No password was typed. No phone number was typed. No address was typed. No form was submitted. No identity provider was clicked. No captcha was solved. The dashboard was not entered. `login-extracted` stays `not-started`.

The homepage hero includes an animated product demo. That demo types a placeholder address on its own. It is a marketing animation, not a form this pass filled. Shots of the homepage and the open nav still show that animation. The login and signup walls were photographed empty, on their own URLs, and those fields were not filled.

## Shared chrome

A black strip sits above the nav: "Configure Clerk with your agent" and "Install the MCP". The nav is a rounded bar: wordmark, five menus, Pricing, Sign in, Sign up.

| Control | Opens | Stop? |
|---|---|---|
| Clerk wordmark | `/` | |
| Products | Dropdown on the same page | |
| Docs | Dropdown on the same page | |
| Changelog | Dropdown on the same page | |
| Company | Dropdown on the same page | |
| AI | Dropdown on the same page | |
| Pricing | `/pricing` | |
| Configure Clerk with your agent | `/mcp` | |
| Install the MCP | `/mcp` | |
| Sign in | `https://dashboard.clerk.com/sign-in` | Stop. Empty wall only |
| Sign up | `https://dashboard.clerk.com/sign-up` | Stop. Empty wall only |
| Open navigation (phone) | Drawer `#mobile-navigation` on the same page | |

On a 390-wide viewport the text menus hide. The hamburger opens the drawer. Sign in and Sign up stay in the bar.

## Products menu

Opened from the Products button. The panel label is PRODUCTS. Escape closes it.

| Item | Opens |
|---|---|
| User Authentication | `/user-authentication` |
| Enterprise Authentication | `/enterprise-authentication` |
| Multi-tenancy | `/multi-tenancy` |
| Protect | `/protect` |
| Billing | `/billing` |
| Platform | `/platform` |

The phone drawer adds Waitlist (`/waitlist`) and component links (`/components/sign-up`, `/components/sign-in`, `/components/user-button`, `/components/user-profile`, `/components/organization-profile`, `/components/organization-switcher`, `/components/create-organization`, `/components/organization-list`, `/components/pricing-table`, `/components/checkout-button`). Those were mapped from the open drawer and not each photographed.

## Docs menu

| Column | Item | Opens |
|---|---|---|
| Top SDKs | Next.js | `/docs/nextjs/getting-started/quickstart` |
| Top SDKs | React | `/docs/react/getting-started/quickstart` |
| Top SDKs | Expo | `/docs/expo/getting-started/quickstart` |
| Top SDKs | TanStack | `/docs/tanstack-react-start/getting-started/quickstart` |
| Top SDKs | React Router | `/docs/react-router/getting-started/quickstart` |
| Top SDKs | Express | `/docs/expressjs/getting-started/quickstart` |
| Top SDKs | Astro | `/docs/astro/getting-started/quickstart` |
| Top SDKs | Chrome | `/docs/chrome-extension/getting-started/quickstart` |
| Top SDKs | Go to Clerk Docs | `/docs` |
| Featured docs | Quickstarts & Tutorials | `/docs` |
| Featured docs | Authentication | `/docs/guides/configure/auth-strategies/sign-up-sign-in-options` |
| Featured docs | Multi-tenancy | `/docs/guides/organizations/overview` |
| Featured docs | Billing | `/docs/guides/billing/overview` |
| Featured docs | Component customization | `/docs/guides/customizing-clerk/overview` |

## Changelog menu

The four dates are what the menu showed on 2026-11-22.

| Item | Opens |
|---|---|
| Nov 20, 2026 Protect your MCP server with Clerk | `/changelog/2026-11-20-mcp-tools-1-0` |
| Nov 12, 2026 View organizations and update users with the Clerk MCP server | `/changelog/2026-11-12-mcp-organization-and-user-tools` |
| Nov 6, 2026 Browser sessions for agents | `/changelog/2026-11-06-agent-browser-sessions` |
| Nov 6, 2026 Set custom session limits per user or device | `/changelog/2026-11-06-custom-session-limits` |
| Go to Changelog | `/changelog` |

## Company menu

| Item | Opens |
|---|---|
| About | `/company` |
| Blog | `/blog` |
| Careers | `/careers` |
| Contact | `/contact` |

## AI menu

| Item | Opens |
|---|---|
| MCP server | `/mcp` |
| CLI | `/cli` |
| Agents | `/agents` |

## Homepage

| Control | Opens | Stop? |
|---|---|---|
| Copy prompt | Copies a prompt. Stays on `/` | Not used as a submit |
| User Authentication, Multi-tenancy, Enterprise Authentication, Agent Authentication | Tabs on the same page. They swap the hero demo | |
| Explore user authentication | `/user-authentication` | |
| Explore Multi-tenancy | `/multi-tenancy` | |
| Explore the MCP server | `/mcp` | |
| Explore the CLI | `/cli` | |
| Explore Clerk for agents | `/agents` | |
| Framework chips (Next.js, React, Expo, React Router, TanStack, Astro) | Matching `/docs/<sdk>/getting-started/quickstart` | |
| FAQ "What is Clerk?" and the other questions | Accordion on the same page | |
| Do Not Sell or Share My Personal Information | Cookie preference control | Not clicked |
| Cookie manager | Cookie preference control | Not clicked |
| Support | Support control in the corner | Not followed into an account |

## Docs landing

`/docs` is public. Title: "Welcome to Clerk Docs". The left rail lists Guides, Reference, and feature groups (Getting started, Authentication flows, User management, and more). Search documentation opens an empty search dialog. Nothing was typed into it. Sign Up in the docs header goes to the signup wall and was not followed from that button.

## Footer

Groups are the labels as painted. One sample of each template was photographed. The rest are mapped.

| Group | Items |
|---|---|
| Product | Authentication `/user-authentication`, Multi-tenancy `/multi-tenancy`, Billing `/billing`, MCP server `/mcp`, CLI `/cli`, Agents `/agents` |
| SDKs | React `/react-authentication`, Next.js `/nextjs-authentication`, Expo `/expo-authentication`, View all `/docs#explore-by-frontend-framework` |
| Resources | Documentation `/docs`, Changelog `/changelog`, Glossary `/glossary`, Feature requests `https://feedback.clerk.com/roadmap`, Startups `/startups`, Students `/github-student-developer-pack`, LLM Leaderboard `/llm-leaderboard` |
| Company | About `/company`, Careers `/careers`, Blog `/blog`, Contact `/contact`, Brand assets `/brand-assets`, Articles `/articles` |
| Legal | Terms and conditions `/legal/standard-terms`, Privacy policy `/legal/privacy`, Website terms of use `/legal/website-terms`, Security `/security`, Legal Resources `/legal` |
| Social | X `https://x.com/clerk`, LinkedIn, Discord `/discord`, GitHub `https://github.com/clerk`, YouTube |

## Auth walls

Photographed empty. Continue with ChatGPT, Continue with GitHub, and Continue with Google were not clicked. Email and password fields were left empty. Continue was not clicked.

| Control | Opens | What it shows |
|---|---|---|
| Sign in (nav) | `https://dashboard.clerk.com/sign-in` | "Sign in to Clerk". ChatGPT, GitHub, Google, then an empty email field and Continue. |
| Sign up (nav) | `https://dashboard.clerk.com/sign-up` | "Create your account". Same providers, empty email, empty password, Continue. |
| Sign up (on the login card) | `/sign-up` | Same signup wall. Not followed after the empty shot. |
| Sign in (on the signup card) | `/sign-in` | Same login wall. Not followed after the empty shot. |

## Empty and missing

| Control | Opens | Stop? |
|---|---|---|
| Search documentation | Empty search dialog on `/docs` | Nothing typed |
| Unknown path | `/this-page-does-not-exist-capture-2026` returns 404, "Sorry, we can't find the page you're looking for." | |
| Go to homepage (on the 404) | `/` | |
| FAQ accordion | Opens on the homepage. The rest stay collapsed | |

## Phone

At 390px the homepage and `/pricing` were photographed. Open navigation opens a drawer of Products, Docs, Changelog, Company, AI, and Pricing. Products was expanded in that drawer. Sign in and Sign up in the drawer bar go to the same walls and were not followed.

## Not entered

`dashboard.clerk.com` past the empty sign-in and sign-up cards. Identity providers. Talk to sales, Submit a ticket, and any contact form. Cookie choices. Subscribe to RSS was not needed. The dashboard from the 2026-10-30 capture was not reopened.
