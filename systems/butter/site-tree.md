# Butter public site tree

Walked signed out on 2026-11-21 from [https://usebutter.com/](https://usebutter.com/) (HTTP 200). That origin redirects to [https://www.butter.video/](https://www.butter.video/). Desktop viewport 1440. Phone viewport 390. iubenda requests were blocked. The consent banner was hidden, not accepted or rejected. No page-level theme switch was found. Marketing pages paint light. The explore, blocks, and templates shell paints dark. They are not a toggle.

Opened means the control was used and the result was photographed or the destination loaded. Linked means the href was read and the page was not opened in this pass. A prior capture (2026-11-11) already has screenshots for many of those destinations. This file records this pass.

Query strings are stripped. Cursor badge paints only for real pointer input and was left hidden.

## Header, desktop

The logo (aria-label "Butter home") links to `/`. Login links to `/login` and was opened. See the login wall below. Try for free links to `/explore` and was opened as the public dark shell, not a checkout.

Co-Create is a button (`aria-expanded`, `aria-controls`). Clicking it keeps the URL on `/` and opens a panel. Photographed in [home-light-cocreate.png](screenshots/home-light-cocreate.png).

| Control | Opens |
|---|---|
| MCP | `/mcp`. Subtitle: Create with Butter in ChatGPT, Claude & more. |

The colon is `button[aria-label="Toggle menu"]`. It keeps the URL on `/` and opens a panel. Photographed in [home-light-menu.png](screenshots/home-light-menu.png). Close is the same control once open.

| Control | Opens |
|---|---|
| Product | `/product`. Subtitle: Explore features. |
| Blocks | `/blocks`. Subtitle: Browse 1000s of butter blocks. |
| Templates | `/templates`. Subtitle: Start with a template. |
| Pricing | `/pricing`. Subtitle: Compare our plans. |
| MCP | `/mcp` |
| Instagram | `https://www.instagram.com/_butterstudio` |
| YouTube | `https://www.youtube.com/@buttervideoapp` |
| X | `https://x.com/_butterstudio` |
| Blog | `/blog` |

Skip to content links to `/#main`.

## Header, phone (390)

The island collapses to the logo and Toggle menu. Opened in [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). Same destinations as the desktop overflow panel: Product, Blocks, Templates, Pricing, MCP, Instagram, YouTube, X, Blog. Close is the same toggle. Login and Try for free were not in the drawer.

## Homepage body

URL stays `/` unless noted. Prior capture: [home-light-default.png](screenshots/home-light-default.png).

| Control | Result |
|---|---|
| Get Started | `/explore` |
| View All Features | `/product` |
| Browse All Templates | `https://app.butter.video/templates`, which redirects to `https://www.butter.video/templates` (HTTP 200, public shell) |
| Learn more (two cards) | `/product` |
| Open Justified in Butter | `https://app.butter.video/justified-studio`, which redirects to `https://www.butter.video/@justified-studio` (HTTP 200, public studio page) |
| All Blocks & Templates | `/blocks` |
| Template cards (Fit for Any Forecast and seven others) | `https://app.butter.video/templates/<id>`, which redirects to `https://www.butter.video/templates/<id>`. One id was opened (Fit for Any Forecast, HTTP 200, public template page). The other ids were linked, not opened. |

Remix, Describe, and Code are buttons (`aria-expanded`). Clicking one keeps the URL on `/` and swaps an in-page panel. Remix was expanded in this pass. Describe and Code were expanded the same way. Not a navigation.

Justified, Dedcool, and Sad Wild Thing are buttons (`aria-expanded`). Clicking one keeps the URL on `/` and swaps the case-study panel. Not a navigation.

Show performance panel is a vendor widget button. Not used.

No homepage search. No locale switch. No theme switch.

## Dark shell (explore, blocks, templates)

`/explore`, `/blocks`, and `/templates` loaded HTTP 200 signed out. Prior captures: [explore-dark-default.png](screenshots/explore-dark-default.png), [blocks-dark-default.png](screenshots/blocks-dark-default.png), [templates-dark-default.png](screenshots/templates-dark-default.png).

Shared sidebar, opened by loading each route:

| Control | Opens |
|---|---|
| Logo | `/` |
| Collapse sidebar | in-page. URL stays. |
| Explore | `/explore` |
| Templates | `/templates` |
| Blocks | `/blocks` |
| Blog | `/blog` |
| Pricing | `/pricing` |
| Learn More | `/` |
| Log in | `/login`. Wall. Branch stopped. |
| Sign up | `/register`. Wall. Branch stopped. |

Create is a button with no href. On `/explore` it opens a dialog titled "Create a free account" on the same URL. Fields seen and left empty: Name, Work Email, Password. Actions seen and not used: Continue with Google, Sign Up, Already have an account? Login, close. Stopped. Not typed. Not submitted. Not photographed into the package, because the dialog is a signup wall.

Carousel arrows (What's New, Featured Blocks, Latest Templates) stay on the same URL. Share stays on the same URL. Neither was followed into a new page.

### Explore cards

| Control | Opens |
|---|---|
| Butter for Figma | `https://www.figma.com/community/plugin/1631607918823712421/figma-to-butter` |
| ilovecreatives × Butter | `/@ilovecreatives` |
| Explore more (blocks) | `/blocks` |
| Explore more (templates) | `/templates` |
| Studio names (Justified Studio, ilovecreatives, Studio Size, Studio Kiln, The Brand Identity, Savee, Kiel Danger, Melivan Colas, Clemens Mako) | `/@justified-studio`, `/@ilovecreatives`, `/@studio-size`, `/@studio-kiln`, `/@thebrandidentity`, `/@letsavee`, `/@kiel-d-m`, `/@melivan-colas`, `/@clemensmako`. Justified Studio was opened (HTTP 200). The others were linked. |

### Blocks

All Blocks is a button. URL stays `/blocks`. Section carousels (Featured Blocks, Kinetic Type, and further rows below the fold) use arrow buttons on the same URL.

A composer sits lower on the page. Placeholder "What do you want to create?". Prompt chips (Apple-style text animation, Nokia 3310 effect, Browser frame, Glass text, AI search bar, Figma-style lower third intro) write into that field and do not navigate. One chip was clicked to confirm the field filled. Nothing was submitted. Attach images, PDFs, or text was not used. Open the code editor was not used. Read the docs links to `/docs`. Get in touch! is a mailto on the same page. Not sent. The address is not recorded.

### Templates

Search field placeholder starts "Search". Not typed.

Filter opens a panel on the same URL. Photographed in [templates-dark-filter.png](screenshots/templates-dark-filter.png). Groups and options seen, none applied:

| Group | Options |
|---|---|
| Industry | Apparel, Beauty, Food and Beverage, Health & Wellness, Home, Jewelry, Kids, Outdoor and Sports, Pets, Software / Apps, Tech, Travel |
| Style | Digital, Grids, Multiple Products, Simple, Single Product, Splitscreens, Text |
| Theme | Back in Stock, Introductory, Press, Sale, TikTok Hooks, UGC |
| Format | 9:16 (Story), 1:1 (Square), 4:5 (Portrait), 16:9 (Landscape), 2:3 (Short Portrait) |

Unmute previews stays on the page. Not used as a navigation.

## Product

`/product` loaded HTTP 200. Prior capture: [product-light-default.png](screenshots/product-light-default.png).

Get started links to `https://app.butter.video/register`, which redirects to `https://www.butter.video/register`. Wall. Branch stopped.

Blocks & Templates, Format & Exports, and Power of Butter are buttons. Each click keeps the URL on `/product` and swaps an in-page panel.

## Pricing

`/pricing` loaded HTTP 200. Prior capture: [pricing-light-default.png](screenshots/pricing-light-default.png).

Monthly and Annually are buttons. Clicking Monthly keeps the URL on `/pricing`. Photographed in [pricing-light-monthly.png](screenshots/pricing-light-monthly.png). Prices read on that pass: Free; Basic $25 struck, $10 per month; Pro $38 struck, $15.20 per month (Most popular); Business $70 struck, $28 per month. Sale chips: −60%.

| Control | Opens |
|---|---|
| Get started for Free | `https://app.butter.video/register`, redirects to `/register`. Wall. Not followed from this card. |
| Choose Basic, Choose Pro, Choose Business | `https://app.butter.video/team/subscription`, which redirects to `https://www.butter.video/login`. Wall. Opened once from a direct load, then stopped. |
| Contact Sales, Contact us | `/contact` |
| Contact Us (a second card) | `https://app.butter.video/team/subscription`, same login redirect. Not followed a second time. |

Features, Assets, and Support & Success are buttons (`aria-expanded`). Clicking one keeps the URL on `/pricing` and swaps the comparison table. Assets and Support & Success were opened.

FAQ. "Can I cancel my subscription anytime?" was opened. Photographed in [pricing-light-faq.png](screenshots/pricing-light-faq.png). Other titles visible and not opened: Is Butter just for short-form videos?, How does the money-back guarantee work?, What payment options are available?, Are subscriptions billed monthly or annually?, Can I change my subscription plan?, How does AI auto-captioning count toward my plan?

## MCP

`/mcp` loaded HTTP 200. `/cocreate` redirects there (HTTP 200). Prior capture: [mcp-light-default.png](screenshots/mcp-light-default.png).

ChatGPT, Claude, and Other MCP Agents are buttons. URL stays `/mcp`. Claude was opened. Photographed in [mcp-light-claude.png](screenshots/mcp-light-claude.png). On Claude the primary action reads Add connector. On ChatGPT it reads Install the plugin and links to chatgpt.com (query string stripped, not followed).

See it in Action links to `/mcp#prompts`. Download ChatGPT links to `https://chatgpt.com/download`. Not followed. Choose a prompt links to `#prompts`.

A button copies `https://ai.butter.video/mcp`. Not followed. Copy prompt and Try in ChatGPT were visible and not used. Prompt chips (Every Monday, Meta ads library, social posts, customer reviews, reference video, last 30 days) stay on the page. Not submitted.

## Blog

`/blog` loaded HTTP 200. Prior capture: [blog-light-default.png](screenshots/blog-light-default.png).

| Control | Opens |
|---|---|
| Component Breakdown: AI Search Bar | `/blog/component-breakdown-ai-search-bar` (opened, HTTP 200) |
| Recipes for 3D Materials | `/blog/3d-material-recipes` |
| Animation Principles for Motion Graphics | `/blog/animation-principles-for-motion-graphics` |
| A Creative Tool for Everyone | `/blog/creative-tool-for-everyone` |
| Engineering | `/blog/category/engineering` (opened, HTTP 200) |
| Get updates via RSS | `/blog/rss.xml` |

## Contact

`/contact` loaded HTTP 200. Empty form photographed in [contact-light-empty.png](screenshots/contact-light-empty.png). Fields seen and left empty: First Name, Last Name, Email Address, Company Name, How can we help?. Send Message was not clicked.

FAQ titles visible and not opened: Is Butter just for short-form videos?, Can I cancel my subscription any time?, How does the money-back guarantee work?, What payment options are available?, Can I change my subscription plan?

Contact us lower on the page is a mailto. Not sent. The address is not recorded.

## Docs

`/docs` loaded HTTP 200. Title: Butter Documentation.

External: p5 2.x and p5 2.x docs both link to `https://beta.p5js.org`. Not followed.

Example and reference links stay on this host. Opened: `/docs/gettingStarted` (HTTP 200). Linked, not opened: lookingGlass, glowText, logoDrop, smokeText, twistSlideshow, bubble, stackedLayers, filterShaders, animatingFields, variableFonts, createCanvas, canvasPadding, orbitControl, drawParentToCanvas, totalFrames, drawTransparent, drawTwoSided, load, loadImageOrVideo, loadImages, loadImagesOrVideos, createVideos, origWidth, origHeight, empty, updatesSize, componentResized, previousFrameState, defaultFrameRate, sizeNormalization.

## Comparisons and tools

Footer links. Each comparison and tool page loaded HTTP 200. `/comparisons` and `/tools` with no slug return HTTP 404.

| Control | Opens |
|---|---|
| After Effects | `/comparisons/after-effects` |
| Remotion | `/comparisons/remotion` |
| HeyGen | `/comparisons/heygen` |
| URL to video | `/tools/url-to-video-ad` |
| Image to layers | `/tools/image-to-layers` |
| Claude to layers | `/tools/claude-motion-graphics` |

On each tool page, HOME links to `/`, TOOLS links to `/tools` (404), Start creating links to `/explore`, Compare plans links to `/pricing`. A comparison card on the URL-to-video page links to `/comparisons/heygen`.

## Other public routes

Sitemap (`/sitemap.xml`, HTTP 200) also lists `/explore`, `/blocks`, about 1,099 `/templates/<id>` paths, `/docs` plus the doc slugs above, ten `/cocreate/<slug>` paths, `/spotify-wrapped-2024-generator`, `/spotify-wrapped-2025-generator`, and public `/@<studio>` pages. One cocreate slug (`/cocreate/product-launch`) returned HTTP 200 with the text "RESOURCE NOT FOUND". Wrapped 2025 loaded HTTP 200 with a Share button and a loading state. Share was not used. Those slugs were not walked one by one.

## Footer

Collected from the homepage. Not opened in this pass unless a row above already says opened.

| Label | Href |
|---|---|
| Product | `/product` |
| Pricing | `/pricing` |
| Get in touch | `/contact` |
| Instagram | `https://instagram.com/_butterstudio` |
| Youtube | `https://www.youtube.com/@buttervideohq` |
| X | `https://x.com/buttervideohq` |
| LinkedIn | `https://www.linkedin.com/company/buttervideohq/` |
| Pinterest | `https://pinterest.com/buttervideohq` |
| Figma Plugin | `https://www.figma.com/community/plugin/1631607918823712421/figma-to-butter` |
| Privacy Policy | `https://www.iubenda.com/privacy-policy/82204341` |
| Cookie Policy | `https://www.iubenda.com/privacy-policy/82204341/cookie-policy` |
| Terms of Service | `/terms-of-service` (opened, HTTP 200) |
| After Effects | `/comparisons/after-effects` |
| Remotion | `/comparisons/remotion` |
| HeyGen | `/comparisons/heygen` |
| URL to video | `/tools/url-to-video-ad` |
| Image to layers | `/tools/image-to-layers` |
| Claude to layers | `/tools/claude-motion-graphics` |
| Logo | `/` |

Header overflow socials use different handles (`_butterstudio`, `@buttervideoapp`) from the footer (`_butterstudio` on Instagram, `@buttervideohq` elsewhere). Both sets were read as published hrefs.

A chat control ("Open chat") sits on several pages. It was not opened.

## Login and signup walls

Login in the header, Log in in the dark shell, and `https://app.butter.video/team/subscription` open `https://www.butter.video/login` (HTTP 200). Empty form photographed and the branch stopped. See [login-review.json](login-review.json).

| Shot | Theme | Width |
|---|---|---|
| [login-light-empty.png](screenshots/login-light-empty.png) | light | 1440 |
| [mobile-login-light-empty.png](screenshots/mobile-login-light-empty.png) | light | 390 |

Wall offers: Email Address, Password, Log In, Continue with Google, Don't have an account? Sign up, Forgot password?, Show password. Nothing was typed. Google was not clicked.

Sign up on that wall opens `https://www.butter.video/register` (HTTP 200). Empty form photographed in [register-light-empty.png](screenshots/register-light-empty.png), then the branch stopped. Fields seen and left empty: Name, Work Email, Password. Continue with Google, Sign Up, and Already have an account? Login were visible and not used. `https://app.butter.video/register` redirects to the same page.

Forgot password? opens `https://www.butter.video/forgot` (HTTP 200). Empty form photographed in [forgot-light-empty.png](screenshots/forgot-light-empty.png), then stopped. Field seen and left empty: Email Address. Email me a recovery link was not clicked. Back to login was not followed from this page.

No dark theme was offered on these walls.

## Not opened this pass

- Continue with Google, on login, register, and the Create dialog.
- Sign Up, Log In, and Email me a recovery link submits.
- Contact Send Message.
- Choose Basic, Choose Pro, and Choose Business past the login redirect.
- Remaining pricing FAQ rows.
- Template filter apply, templates search typing, blocks composer submit.
- Remaining template ids, studio handles, doc slugs, and blog posts.
- ChatGPT plugin, Claude connector, and chatgpt.com links.
- Footer social, legal, and Figma destinations not already named as opened.
- Any signed-in workspace. Editor, projects, exports, billing, and settings were not entered.
