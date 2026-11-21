# Vercel public site tree

Mapped on 2026-11-21 from the live public site at `https://vercel.com/`.
Official domain confirmed by the page title "Agentic Infrastructure - Vercel"
and the h1 "Agentic Infrastructure". Headless Playwright, signed out.
Nothing was typed. No identity provider was clicked. No form was submitted.

Default theme is light (`color-scheme: light`, body background `rgb(250, 250, 250)`,
body text `rgb(23, 23, 23)`). The footer has labels `system`, `light`, and `dark`.
Clicking the `dark` label adds `dark-theme` to `html`, sets `color-scheme: dark`,
and paints the page black. Login and signup stay light. They were not switched.

`login-extracted` stays `not-started`.

Auth walls, photographed empty and not entered:

| Control | Opens | Action |
|---|---|---|
| Header "Log In", mobile drawer "Log In" | `https://vercel.com/login` | Photographed empty. Email placeholder "Email Address", value empty. Buttons: Continue with Email, Google, GitHub, ChatGPT, SAML SSO, Passkey, Show other options. Did not type. Did not click a provider. Did not submit. |
| Header "Sign Up", hero "Deploy now", mobile drawer "Sign Up" | `https://vercel.com/signup` | Photographed empty. No email field on the first screen. Buttons: Continue with Google, GitHub, ChatGPT, Apple, Show other options. Did not click a provider. Did not submit. |
| Signup "Show other options" | stays on `https://vercel.com/signup` | Clicked only to see the other labels. The buttons stayed Google, GitHub, ChatGPT, and Apple. A "Continue with Email" link appeared. Did not follow it. Did not type. |
| Header "Get a Demo", mobile drawer "Get a Demo" | `https://vercel.com/contact/sales` | Public sales page, title "Talk to our Sales team". Not submitted. |

## Shell

Desktop header (1440): triangle mark to `/home`, then Products (button,
`aria-controls="nav-panel-products"`), Resources (button,
`aria-controls="nav-panel-resources"`), Enterprise (`/enterprise`), Pricing
(`/pricing`), then Get a Demo (`/contact/sales`), Log In (`/login`), Sign Up
(`/signup`).

Products and Resources open a dialog labelled "Navigation menu". Click opens
it. Escape closes it. Both panels are in the same dialog, so opening either
one shows both sets of links.

Phone header (390): the only header control is a button labelled "Open menu"
(`aria-label="Open menu"`, `aria-expanded` starts false). It opens a
full-screen dialog. The dialog lists Products and Resources as collapsed
rows, then Enterprise, Pricing, Get a Demo, Log In, and Sign Up. A close
control sits at the top right.

## Desktop dialog links

### Products

| Group | Item | Opens |
|---|---|---|
| Agent Stack | AI SDK | `/ai-sdk` |
| Agent Stack | AI Gateway | `/ai-gateway` |
| Agent Stack | Sandbox | `/sandbox` |
| Agent Stack | Passport | `/passport` |
| Agent Stack | Connect | `/connect` |
| Agent Stack | eve | `/eve` |
| Core Platform | Build and deploy | `/products/previews` |
| Core Platform | Vercel CI | `/ci` |
| Core Platform | Fluid Compute | `/fluid` |
| Core Platform | Content Delivery | `/cdn` |
| Core Platform | Observability | `/products/observability` |
| Core Platform | Workflows | `/workflows` |
| Core Platform | Security | `/security` |
| Tools | Next.js | `/frameworks/nextjs` |
| Tools | Vercel Agent | `/agent` |
| Tools | Vercel Plugin | `/plugin` |
| Tools | Open Source | `/oss` |
| Tools | Domains | `https://vercel.com/domains` |
| Tools | v0 | `https://v0.app` |

### Resources

| Group | Item | Opens |
|---|---|---|
| Learn | Docs | `/docs` |
| Learn | About | `/about` |
| Learn | Blog | `/blog` |
| Learn | Changelog | `/changelog` |
| Learn | Knowledge Base | `/kb` |
| Build | AI Apps | `/ai` |
| Build | Web Apps | `/for/web-apps` |
| Build | Marketing Sites | `/for/marketing-sites` |
| Build | Platforms | `/for/platforms` |
| Build | Commerce | `/for/retail` |
| Explore | Customers | `/customers` |
| Explore | Marketplace | `/marketplace` |
| Explore | Partner Finder | `/partners/solution-partners` |
| Explore | AWS | `/partners/aws` |
| Explore | Community | `https://community.vercel.com/` |

## Footer

Footer groups on the homepage: Agent Stack, Core Platform, Security, Tools,
Frameworks, SDKs, Build, Learn, Explore, Company, Legal & Trust, Social.
A status link goes to `https://www.vercel-status.com`. Theme labels sit at
the bottom: system, light, dark. "Cookie Preferences" is a button. It was
not used as a consent POST.

Extra footer links that are not in the header dialog: Nuxt, SvelteKit,
Nitro, Turborepo, TanStack Start, FastAPI, All frameworks, Vercel SDK,
Flags SDK, Chat SDK, Queues SDK, Streamdown (`https://streamdown.ai`),
Platform Engineers, Design Engineers, Academy, Articles, Is Agentic
(`https://is-agentic.com`), Templates, Careers, Press, Events, Startups,
Shipped on Vercel, Open Source Program, Help, the legal documents, Trust
Center (`https://security.vercel.com`), and the social marks (GitHub, X,
LinkedIn, YouTube, Instagram).

## Pages confirmed public

| Path | Title | Stopped? |
|---|---|---|
| `/` | Agentic Infrastructure - Vercel | Captured |
| `/pricing` | Vercel Pricing: Hobby, Pro, and Enterprise plans | Captured |
| `/enterprise` | Enterprise | Captured |
| `/docs` | Vercel Documentation | Captured, landing only |
| `/geist/colors` | Geist Design System | Captured, light |
| `/design` | Vercel Design | Public, not framed |
| `/blog` | Blog - Vercel | Public, not framed |
| `/customers` | Customer stories | Public, not framed |
| `/changelog` | Changelog - Vercel | Public, not framed |
| `/about` | About Us | Public, not framed |
| `/security` | Security - Vercel | Public, not framed |
| `/templates` | Templates - Vercel | Public, not framed |
| `/marketplace` | Vercel Marketplace | Public, not framed |
| `/contact/sales` | Contact Sales - Vercel | Public form. Not filled. |
| `/login` | Login – Vercel | Empty wall. Stopped. |
| `/signup` | Sign Up – Vercel | Empty wall. Stopped. |
