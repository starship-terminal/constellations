# Krea public site tree

Mapped from https://www.krea.ai/ on 2026-11-21, signed out, in headless Chromium at 1440×900. The painted theme is `html.dark`. There is no separate marketing host. Sign up and Sign in open an empty auth dialog on the home shell. `/login` is the same wall as a page. Nothing was typed. No identity provider was clicked. No form was submitted. A control that opens that wall is recorded and that branch stops.

`/signup`, `/sign-up`, `/register` and `/auth/login` return the public 404 ("The page you're looking for can't be found"). Signup is the Sign up button, not a route.

## Shell

The home page is the signed-out app shell: a left rail, a tool list, a composer, a public feed, and a footer. Promo dialogs (a limited-time Seedance offer) were hidden, never answered.

| Control | Opens | Stop? |
|---|---|---|
| Toggle Sidebar | Folds the left rail on the same page | |
| Krea | `/app` | public shell, same chrome |
| Bots | `/bots` | public empty gallery |
| Agent | `/agent` | public composer; do not send |
| Node Editor | `/nodes` | public overview |
| Train Lora | `/train` | public overview |
| Files | `/login?redirect=%2Ffiles` | yes, login wall |
| API | `/app/api` | public API marketing page |
| Home | `/` | |
| Image | `/image` | public tool shell |
| Image More | Unpin Tool menu | |
| Video | `/video` | public tool shell |
| Video More | Unpin Tool menu | |
| Enhancer | `/enhancer` | public tool shell |
| Enhancer More | Unpin Tool menu | |
| Ad Studio | `/ad-studio` | public tool shell |
| Ad Studio More | Unpin Tool menu | |
| Edit | `/edit` | public tool shell |
| Edit More | Unpin Tool menu | |
| More | Tools menu (see below) | |
| Pricing | `/pricing` | |
| Enterprise | `/enterprise` | |
| MCP | MCP client menu (see below) | |
| Sign up | Auth dialog on `/` | yes, signup wall |
| Sign in | Same auth dialog on `/` | yes, login wall |
| Search | Command palette dialog, empty | do not type a query |
| Claim offer, See plans | `/pricing` | do not start checkout |
| Close (promo) | Hides the offer dialog | hidden, never clicked |

## More menu

The last More button in the tool list (`aria-haspopup="menu"`). Escape closes it. The earlier More buttons on pinned tools only offer Unpin Tool.

| Item | Opens | Stop? |
|---|---|---|
| Realtime | `/realtime` | public canvas shell; do not generate |
| Pin Tool: Realtime | Pins the row in the rail | local |
| Nano Banana | `/nano-banana` | public model page |
| Audio | `/audio` | public tool shell |
| Seedance Studio | `/seedance-studio` | public tool shell |
| Video Lipsync | `/lipsync` | public tool shell |
| 3D Objects | `/3d` | public tool shell |
| Drama Studio | `/drama-studio` | public tool shell |

## MCP menu

| Item | Opens |
|---|---|
| ChatGPT | `/mcp?tab=chatgpt` |
| Claude | `/mcp?tab=claude` |
| Claude Code | `/mcp?tab=claude-code` |
| Cursor | `/mcp?tab=cursor` |
| Grok Bot | `/mcp?tab=grok-bot` |
| CLI | `/mcp?tab=cli` |

## Search dialog

Search opens a dialog titled with jump links (Home, Account, theme toggle, Agent, Image, Video, and more). The field placeholder is "Search tools, models, chats, and files...". It was opened empty and closed with Escape. Account goes to settings and was not followed. The theme row says the page is currently dark. It was not switched.

## Auth walls

Photographed empty. Continue with Google, Continue with Apple, Single Sign-On, and Continue with Email were not clicked. The email field was left empty.

| Control | Opens | What it shows |
|---|---|---|
| Sign up (home) | Dialog on `/` | "Sign up to generate for free". Google, Apple, SSO, email. No card required. |
| Sign in (home) | Same dialog | Same providers. |
| `/login` | Page | "Log in or sign up". Google, Apple, SSO, Continue with Email. |
| Files, and other gated routes | `/login?redirect=…` | Same page. The redirect query is the stop, not a signed-in URL. |

`/app`, `/bots`, `/agent`, `/nodes`, `/train`, `/image`, `/video`, `/enhancer`, `/ad-studio`, `/edit`, `/realtime` and `/feed` stay on their own URLs signed out. They are public shells. Generation, training, and file upload were not started.

## Footer

The footer is on the home page. Groups below are the labels as painted. One sample of each template was photographed. The rest are mapped and not each shot.

| Group | Items |
|---|---|
| Generate | AI Image Generator `/features/ai-image-generator`, AI Video Generator `/features/ai-video-generator`, Image to Video `/apps/image-to-video`, AI Drama Generator `/apps/ai-drama-generator`, Krea Agent `/krea-agent`, Ad Studio `/ad-studio`, Sketch to Image, AI Character Generator, 3D Model Generator, T-Shirt Design Maker, Polaroid Photo Generator |
| Video models | Seedance 2.5, Kling 4, Kling AI, Veo 3.1, MiniMax H3, MiniMax H3 Max, Wan 3.0, Runway `/video/runway`, All Video Models `/video` |
| Edit | AI Image Editor, Image to Image, AI Hairstyle Changer, AI Clothes Changer, Face Swap, Video Face Swap, Remove Text, Object Remover, Photo to Cartoon, Change Lighting, Motion Transfer, Lip Sync |
| Image models | Krea 3 `/krea-3`, Krea 2 `/krea-2`, Nano Banana Pro, ChatGPT Images 2, FLUX 3, Seedream 5.0 Pro, All Image Models `/image` |
| Enhance | Photo Enhancer, Image Upscaler, Video Upscaler, Background Remover, AI Vectorizer, Unblur Image, Colorize Photo, All AI Apps `/apps` |
| Solutions | Architecture, Interior Design, Gaming, All Solutions `/solutions` |
| Product | Pricing, Enterprise, All Models `/models`, API `/features/api`, MCP, Plugins |
| Learn | Blog, Guides, Academy `/enterprise/academy`, Customer Stories, Krea Alternatives, Release Notes `/docs/changelog` |
| Ask | ChatGPT, Claude, Gemini, Perplexity, Grok (external) |
| Legal | Terms `/terms`, Privacy `/privacy`, Security `/security`, Subprocessors `https://trust.krea.ai` |
| Company | Careers (Ashby), Press `/press`, Documentation `/docs` |
| Social | X, LinkedIn, Instagram, Reddit, YouTube, Discord |

## Home interactions that stay on `/`

| Control | Opens | Stop? |
|---|---|---|
| Claim offer, See plans | `/pricing` | |
| Try Video Swap, Try Video 2.0, Open Ad Studio, Try Krea 3, model try buttons | Tool or model routes | do not generate |
| Sign up to the Waitlist | Waitlist control | not submitted |
| View announcement | Announcement | not followed into an account |
| Add image | Upload / Select asset menu | not used |
| Previous slide, Next slide | Feed carousel | local |
| Composer, Generate | Would start a generation | not typed, not submitted |

## Phone

At 390px the same shell collapses. Toggle Sidebar opens the rail. Home and one inner page (`/feed`, the public gallery) were photographed at that width. Login was photographed at that width and left empty.

## Not entered

Signed-in `/app` chrome, settings, account menu, billing, generation, waitlist submit, Book a call, Get Pro, and any OAuth redirect. `login-extracted` stays `not-started`.
