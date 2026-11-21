# Gumroad public site tree

Mapped on 2026-11-21 from `https://gumroad.com/` with headless Playwright at a requested 1440×900 viewport, before screenshots. A control is recorded only when it was opened or its `href` was read. Branches that land on a log-in or sign-up wall stop there. No form was submitted. No password was typed. Apple, Google, X, Stripe, and passkey were not clicked.

The marketing shell (`/`, `/blog`, `/pricing`, `/features`, `/about`, `/gumclaw`, `/small-bets`, `/mcp`, `/terms`, `/privacy`, `/prohibited`, `/dpa`, `/api`) and the marketplace shell (`/discover` and category pages) both follow `prefers-color-scheme`. Light paints a `#f4f4f0` page. Dark paints `#242423`. There is no on-page theme switch. The log-in and sign-up pages stay light.

## Header (marketing shell)

Present on the home page and the marketing, legal, and feature pages listed above.

| Control | Opens |
|---|---|
| Wordmark | `https://gumroad.com/` |
| GitHub star count (10.1K) | `https://github.com/antiwork/gumroad` (external). Not captured as product UI. |
| Discover | `https://gumroad.com/discover` |
| Blog | `https://gumroad.com/blog` |
| Pricing | `https://gumroad.com/pricing` |
| Features | `https://gumroad.com/features` |
| About | `https://gumroad.com/about` |
| Gumclaw | `https://gumroad.com/gumclaw` |
| Log in | Log-in wall: `https://gumroad.com/login`. Stop. Known probe: email and password, or Apple, Google, X, Stripe, or a passkey. |
| Start selling | Sign-up wall: `https://gumroad.com/signup`. Stop. Email, password, Google, X. Not filled. |

At 390×844 the same links sit behind a hamburger (`button[data-toggle="mobile-menu"]`). It opens an in-page menu, not a new URL.

## Home (`/`)

| Control | Opens |
|---|---|
| Start selling (hero and elsewhere) | Sign-up wall: `https://gumroad.com/signup`. Stop. |
| Search marketplace (text field) + Search | Stays on the page until submitted. A public query goes to Discover search. Not a personal form. |
| GitHub (contribute or fork) | `https://github.com/antiwork/gumroad` |
| Find out how | `https://gumroad.com/features` |
| Category chips (blender, meditation, comic, notion template, textures, procreate, and the rest of the chip grid) | A public category or tag page, for example `https://gumroad.com/3d?tags=blender`, `https://gumroad.com/design?tags=font` |
| Footer email field + arrow | Newsletter. Not typed. Not submitted. |
| Small Bets | `https://gumroad.com/small-bets` |
| Gumroad MCP | `https://gumroad.com/mcp` |
| Help | `https://gumroad.com/help` |
| Board meetings | `https://www.youtube.com/playlist?list=PL_DfN-mKCGNuswqERc6sIA8urYAKARc6s` (external). Not captured. |
| Terms of Service | `https://gumroad.com/terms` |
| Privacy Policy | `https://gumroad.com/privacy` |
| X, YouTube, Instagram, Facebook, Pinterest marks | External social profiles. Not captured as product UI. |

## Discover (`/discover`)

Marketplace shell. Header is the wordmark (links to `/discover`), Log in, and Start selling.

| Control | Opens |
|---|---|
| Search products | Public search on the marketplace. Not a personal form. |
| Category bar: All | `https://gumroad.com/discover` |
| Drawing & Painting (the link) | `https://gumroad.com/drawing-and-painting` |
| Drawing & Painting (the dialog trigger, hover) | Dialog on the page: All, Drawing & Painting, Artwork & Commissions, Digital Illustration, Traditional Art. |
| 3D, Design, Music & Sound Design, Self Improvement, Gaming, Films, Education, Software Development | The matching category URL (`/3d`, `/design`, `/music-and-sound-design`, `/self-improvement`, `/gaming`, `/films`, `/education`, `/software-development`). Each trigger also opens a subcategory dialog. |
| More | Dialog on the page: Business & Money, Photography, Comics & Graphic Novels, Writing & Publishing, Fitness & Health, Fiction Books, Recorded Music, Audio, Other. The `href` is `https://gumroad.com/discover#`. |
| Trending, Best Sellers, Hot & New | Sort tabs. Stay on Discover (query changes the sort). |
| Filters (tags, file type, price, rating) | Local filter controls on the page. Checkboxes, price fields, rating radios. Not submitted as a form POST. |
| Currency select | Local display currency. Not an account setting. |
| A product card | Public product page on a creator subdomain, for example `https://tejujangid.gumroad.com/l/Thickimpastobrushes` |
| A creator name | Public creator profile on that subdomain |
| Follow | Log-in wall: `https://gumroad.com/login?next=…`. Stop. |
| Load more | More public cards on the same page. |
| I want this! on a product page | Checkout: `https://gumroad.com/checkout?product=…`. Not followed. No purchase. |

## Blog (`/blog`)

Index of public posts. A post title opens `https://gumroad.com/blog/p/<slug>`. One post is enough to show the article template. The rest are the same template.

## Pricing, features, about, Gumclaw, Small Bets

Marketing pages on the same shell. Pricing links "here" to `https://gumroad.com/prohibited` and a PDF reseller certificate. Features links public creator profiles. Gumclaw links `https://antiwork.com/` (external). Small Bets "Join Small Bets" goes to `https://smallbets.com/join` (external). Not captured as product UI.

## Gumroad MCP (`/mcp`) and connector pages

| Control | Opens |
|---|---|
| Set up the connector | `https://gumroad.com/mcp#connect` (same page) |
| Read the technical details | `https://gumroad.com/muse` |
| Set up Gumroad MCP (Claude, Cursor, Antigravity, ChatGPT) | `https://gumroad.com/claude`, `/cursor`, `/antigravity`, `/chatgpt` |
| Connecting AI assistants | Help article `https://gumroad.com/help/article/355-connect-ai-assistants-to-gumroad` |
| Settings > Applications | `https://gumroad.com/settings/authorized_applications`. Account settings. Not opened. Stop. |
| API docs | `https://gumroad.com/api` |
| MCP discovery | `https://gumroad.com/.well-known/mcp.json` (a JSON file, not a page) |

## Help (`/help`)

Public help center. Search field is local. Article links open `https://gumroad.com/help/article/<id>-<slug>`. "Email support" is a `mailto:` link. Not used. "Contact support" was not submitted.

## Log in and sign up (walls)

| URL | What it asks | Stop |
|---|---|---|
| `https://gumroad.com/login` | Email, password, Show password, Login, Log in with a passkey, Apple, Google, X, Stripe, Forgot your password?, Sign up | Recorded. Not filled. Not clicked past the wall. |
| `https://gumroad.com/signup` | Email, password, Google, X, Create account, Terms of Use, Privacy Policy, Log in | Recorded. Not filled. |
| `https://gumroad.com/users/forgot_password/new` | Email to send reset instructions, plus Apple, Google, X, Stripe | Recorded. Not filled. |

## Legal

| Control | Opens |
|---|---|
| Terms of Service | `https://gumroad.com/terms` |
| Privacy Policy | `https://gumroad.com/privacy` |
| Prohibited products | `https://gumroad.com/prohibited` |
| Data processing addendum | `https://gumroad.com/dpa` |

External legal hosts named inside those pages (Stripe, PayPal, Google, OpenAI, Anthropic) were not opened.

## Stopped branches

- Log in, Start selling, Follow, and any control that redirects to `/login` or `/signup`.
- Forgot password, passkey, Apple, Google, X, Stripe.
- Checkout (`I want this!`).
- Account settings (`/settings/authorized_applications`).
- Newsletter email field.
- External sites: GitHub, YouTube, X, Instagram, Facebook, Pinterest, antiwork.com, smallbets.com.
