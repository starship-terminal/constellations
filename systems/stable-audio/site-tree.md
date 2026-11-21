# Stable Audio site tree

Mapped from the live public site on 2026-11-21, before screenshots, in headless Chromium at 1440x900. Origin is `https://stableaudio.com/` (www redirects here). Cookie consent is a OneTrust banner. It was hidden in CSS and never clicked. No form was submitted. No email was typed. AuthKit was not continued past the recorded URL.

## Pages that load signed out

| Control | Opens | What it is |
|---|---|---|
| Logo, "Stable Audio home" | `/` | Homepage mix surface |
| Nav "How it works" | `/#how-it-works` | Same page, section |
| Nav "Plugin", "Download the plugin" | `/plugin` | Plugin download page |
| Nav "Pricing", "Compare plans" | `/pricing` | Plan cards and billing FAQ |
| Footer / guide "Read the manual" | `/docs/manual` | Public manual, own chrome |
| `/guide`, `/docs`, `/user-guide`, `/user-guide/text-to-audio` | `/guide` | Public how-to guide |
| Footer terms mark | `/terms` | Stability AI terms, in the marketing chrome |
| `/account` | `/account` | Signed-out wall: "Sign in to see your account" |
| `/about` | `/` | Redirects home |
| `/workspace` | `/workspace-next` | Signed-out wall, then stop |

## Homepage controls that stay on the page

| Control | Opens |
|---|---|
| "Presets" (`aria-haspopup="menu"`) | Menu "START FROM A PRESET" (Midnight Drive, Sunday Coffee, Catwalk, Glacier, Storm Trailer, Rainy Window, Arcade Heart, Desert Road, Golden Hour, and the rest the menu lists) |
| A mad-lib word ("explosive, energy. Tap to change.") | Cycles that slot. No listbox or dialog mounted |
| "Roll the dice" | Replaces the prompt with another published preset. Local only |
| Bowl / "Play …" | Plays the published demo track already on the page |
| FAQ `summary.HomeFaq_question` | Expands that answer in place |
| Help (`aria-label="Help"`) | Region "Help is on: hover or tap a ? …" plus a Done button. Not a link menu |
| "Your Privacy Choices" | OneTrust preference center (`#onetrust-pc-sdk`). Not submitted |
| Plugin page "Mac" / "Windows" | Toggles the download target on `/plugin` |
| "Play the plug-in demo" | Plays the published plugin demo on `/plugin` |
| Guide and manual in-page links | Anchors on the same document |

## Controls that open a signup dialog, then stop

These stay on `https://stableaudio.com/` and mount a dialog. The dialog's "Sign up free" is the next step toward AuthKit and was not followed. "Not now" closes it.

| Control | Dialog copy |
|---|---|
| "Make my mix" | "Sign up to make it yours" |
| "Download" | "Sign up to download your take" |
| "Save" | "Sign up to save your mix" |

## Controls that leave for a login wall, then stop

Recorded URL, branch stopped. No email typed, no password, no Google or Apple, no account created.

| Control | Lands on |
|---|---|
| "Sign in", "Log in", logo "Open Stable Audio", `/login`, `/workspace`, `/workspace-next` | `https://generous-milk-49.authkit.app/` (WorkOS AuthKit, intent login). Workspace title before the hop: "Sign in to your Workspace" |
| "Start free", "Sign up" | `https://generous-milk-49.authkit.app/sign-up` (intent signup) |
| "Open Sampler" | AuthKit, `returnTo` `/workspace-next/apps/sampler` |
| "Try it in Labs" | AuthKit, `returnTo` `/workspace-next/labs` |
| "Open studio", guide session link | `/workspace-next/apps/sessions/new` then AuthKit |
| "Generate" | `/workspace-next/apps/generate` then AuthKit |
| Pricing "Get Solo", "Get Session", "Get Producer", "Get Studio" | Checkout / AuthKit. Not followed |
| Account page "Sign in" | AuthKit. Not followed |

Known probe, already recorded and not repeated as a typed flow: homepage Sign in opened AuthKit, Continue with email, then a password step. Password was not submitted. This capture does not type an email into that step.

## Off-site links, not captured as this product

| Control | URL |
|---|---|
| Nav "API" | `https://platform.stability.ai/` |
| "here" (model family) | `https://stability.ai/stable-audio` |
| "Contact us", footer Contact | `https://kb.stability.ai/knowledge-base/kb-tickets/new` |
| Help and support | `https://kb.stability.ai/knowledge-base` |
| Terms of Service (footer text link) | `https://stability.ai/terms-of-service` |
| Privacy Policy | `https://stability.ai/privacypolicy` |
| Stability AI | `https://stability.ai/` |
| X, Discord, Instagram | social profiles |
| Plugin "Download for Mac" / model packs | `https://assets.stableaudio.com/plugin/...` file downloads. Not downloaded |
| Newsletter "Subscribe" | Form. Not filled, not submitted |

## Routes that do not exist

404 on 2026-11-21: `/signup`, `/sign-in`, `/sign-up`, `/blog`, `/faq`, `/models`, `/labs`, `/sampler`, `/app`, `/changelog`, `/privacy`, `/legal`, `/support`, `/help`, `/status`, `/careers`, `/enterprise`, `/api`, `/download`, `/sitemap.xml`, `/robots.txt`, `/plugin/download`. `/generate` returned 403.

## Theme

No theme toggle on the public pages. The marketing chrome is one dark surface. Light is not a public state.
