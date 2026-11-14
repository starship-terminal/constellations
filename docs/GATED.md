# Gated surfaces

What the library has NOT captured: every surface that sits behind a sign-in,
an account, a checkout or a submission in the signed-out captures. Generated
by `python3 tools/gated.py` from `capture.gaps` and `access` in
[catalog.json](../catalog.json); do not edit by hand.

Each entry is the catalog's own words. A package appearing here is not
incomplete — the capture was scoped to public surfaces on purpose — it is
the queue for any future authenticated pass, which needs the owner's
account and a fresh capture contract (docs/CAPTURE.md, docs/RIGHTS.md).

_85 of 143 packages name gated surfaces in their gaps; 51 more mark a gate in their access text; 7 report none._

## [aaply](../systems/aaply) — `aaply`
Access: signed out (every surface captured is public; the app host go.aaply.app returned "Not found" on every route and was not captured)
- go.aaply.app returned "Not found" on /login, /sign, /signup and /workspace/demo: the authenticated product is unreachable to this client, so only the marketing site is measured

## [Acne Studios](../systems/acnestudios) — `acnestudios`
Access: signed out (every captured surface is public); Singapore storefront /sg/en, OneTrust consent SDK network-blocked
- Bag drawer, checkout, account area, store stock check, size-guide drawer and search results need a cart item, account, purchase or form submit — not captured

## [Acuity Scheduling](../systems/acuityscheduling) — `acuityscheduling`
Access: signed out (every captured surface is public); the Squarespace account gate was measured and state-forced, never submitted
- the scheduling app itself sits behind a Squarespace account and was never entered; the create-account gate and sign-in card were measured at rest and state-forced only

## [adidas](../systems/adidas) — `adidas`
Access: signed out (every captured surface is public); China flagship storefront adidas.com.cn
- add-to-cart captured in its disabled state (grey text/border); enabled purchase bar not captured
- nothing submitted, bought or signed into; sign-in area and checkout untouched

## [Aesop](../systems/aesop) — `aesop`
Access: signed out (every captured surface is public); US storefront Sites-aesop-us-Site, OneTrust consent SDK network-blocked
- sign-in beyond the form, account area, checkout and purchases deliberately uncaptured (nothing submitted)

## [Airbnb](../systems/airbnb) — `airbnb`
Access: signed out; www.airbnb.com geo-redirected to www.airbnb.com.sg from this network (same system on the regional mirror)
- sign-in and everything behind the account: wishlist save, promo claim, host onboarding, booking and payment
- search submission: the Where panel was opened and measured, never submitted

## [Alo Yoga](../systems/aloyoga) — `aloyoga`
Access: signed out (every captured surface is public; checkout, the bag drawer and account behind sign-in were never reached)
- checkout, the bag drawer and everything behind sign-in

## [Amie](../systems/amie) — `amie`
Access: signed out (every captured surface is public; the app behind login and the download were never reached)
- the app behind login: calendar, inbox, notes, recording
- downloads were measured, never pressed; the contact form was never submitted

## [Appwrite](../systems/appwrite) — `appwrite`
Access: signed out (every captured surface is public; the console behind sign-in was never reached)
- the console app behind sign-in: projects, dashboards, account
- form submission: sign-in fields were typed into and cleared, never sent

## [Arcade](../systems/arcade) — `arcade`
Access: signed out (every captured surface is public; the app behind sign-in was never reached; the Finsweet consent banner and Intercom launcher were hidden, never answered)
- the app behind sign-up/sign-in: demo editor, agents, dashboard
- no form was submitted, no prompt was sent, no plan or signup CTA was followed

## [ARKET](../systems/arket) — `arket`
Access: signed out (every captured surface is public; the cookie-consent card and the 'Please confirm your location' dialog were measured as they arrive, then hidden, never answered; Akamai blocks headless Chromium and every /en-ww/product/* URL, so the capture ran in headed real Chrome and no PDP was reached)
- the account behind the Login/Signup gate, checkout and the filled cart were never reached
- no consent or location answer was given, nothing was added to the bag, no form was submitted

## [Artboard Studio](../systems/artboardstudio) — `artboardstudio`
Access: signed out (every captured surface is public; the editor on app.artboard.studio sits behind sign-in and was never reached; no consent overlay appeared)
- the editor on app.artboard.studio sits behind sign-in; no account was created, no canvas, plugin UI or download reached

## [Asana](../systems/asana) — `asana`
Access: signed out (every captured surface is public; the app on app.asana.com sits behind sign-in and was never reached; OneTrust consent banner was dismissed; the dark token set is declared in the shipped CSS but unbound on the captured routes)
- the product on app.asana.com sits behind sign-in; no workspace, task or Launch Asana surface was reached; Log in, Get started, plan CTAs and both forms were measured, never followed or submitted
- the create-account gate heading did not measure (gate-title missing); the field, continue CTA and SSO buttons did

## [ASOS](../systems/asos) — `asos`
Access: signed out (every captured surface is public; checkout and account behind sign-in were never reached)
- checkout and everything behind sign-in (nothing was added to the bag)

## [Avnier](../systems/avnier) — `avnier`
Access: signed out (every captured surface is public; checkout and account behind sign-in were never reached)
- checkout and everything behind sign-in (nothing was added to the cart)
- the login email's filled state is an error record: the fill click did not land in time

## [Awwwards](../systems/awwwards) — `awwwards`
Access: signed out (every captured surface is public; voting, submission and account areas were never performed or reached)
- Log in / Sign Up did not render on the captured headless loads; no public login page exists signed-out (/session/login 404s)
- voting and /submit/ were never performed (a vote records a score); account, jury and Pro areas are behind sign-in
- submit-cta-2 is a recorded miss: no measurable CTA rendered on /submit/ headless

## [B150](../systems/b150) — `b150`
Access: signed out (every captured surface is public; app.b150.ai login/signup rate-limits non-browser clients with HTTP 429 and was never reached)
- app.b150.ai (LOGIN / SIGN UP / auth gate) returns HTTP 429 to non-browser clients and was never reached
- the contact form was measured and focused, never submitted

## [Ballpark](../systems/ballpark) — `ballpark`
Access: signed out (every captured surface is public; the app behind /sign-in was never reached and no form was submitted)
- the product behind /sign-in: surveys, participants, reports and billing were never reached
- no form was submitted and no link followed off-site; sign-in fields were focused/filled then cleared

## [Base44](../systems/base44) — `base44`
Access: signed out (every captured surface is public; the app behind app.base44.com was never signed into and no form was submitted)
- the product behind app.base44.com: the builder, dashboards, billing and templates were never signed into
- no form was submitted and no OAuth button was pressed; the email field was focused/filled then cleared; the prompt composer was never sent

## [Bezi](../systems/bezi) — `bezi`
Access: signed out (every captured surface is public; the product is a desktop download and no sign-in surface, form or checkout was reached)
- the product itself: Bezi is a desktop app download and no sign-in, account or app surface was reached
- no link was followed, download started or form submitted; TRY FOR FREE, the plan CTAs, the billing toggle and outbound links (Docs, Discord, socials) were measured only

## [Bio Sites](../systems/biosites) — `biosites`
Access: signed out (every captured surface is public; the editor redirects to a claim screen that was measured but never submitted, and no account was created)
- the product behind sign-in: the editor, dashboard, analytics and billing were never reached; only the signed-out claim screen was measured
- no form was submitted and no link followed; the username field was filled with a throwaway string and cleared, the circular submit measured but never pressed

## [Bloomberg](../systems/bloomberg) — `bloomberg`
Access: signed out (every captured surface is public; the article paywall, sign-in, checkout and the gated live stream were never crossed)
- the article body past the paywall, comments and everything behind sign-in (portfolio, watchlist, account) were never reached
- the sign-in sheet mounts /account/iframe/login which renders the PerimeterX verification card for this client
- the live stream and video playback need a subscription; the gated player was measured at rest
- checkout and purchase flows were never followed

## [Blue Apron](../systems/blueapron) — `blueapron`
Access: signed out (every captured surface is public; the shop, sign-in and checkout on www.blueapron.com are edge-blocked for this client and were never reached)
- www.blueapron.com entirely: the shop front end, menu, membership, gifts, cookbook, sign-in, checkout and account are behind the Cloudflare edge block; nothing there was measured
- the cart was captured empty; checkout was never reached

## [Boords](../systems/boords) — `boords`
Access: signed out (every captured surface is public; the product on app.boords.com sits behind login and was never reached)
- app.boords.com entirely: storyboards, animatics, shot lists, the script editor, projects, exports and every account surface are behind login and were never reached
- /login renders its shell; no form fields mount for this client
- the script timer textarea was filled with a sample script and cleared; nothing was submitted

## [Busuu](../systems/busuu) — `busuu`
Access: signed out (every captured surface is public; the product on app.busuu.com, register step 2+ and checkout sit behind login and were never reached)
- app.busuu.com entirely: lessons, review, streaks, the profile and every account surface are behind login and were never reached
- register stops at step 1 (the language picker): choosing a language starts the account, so later steps are unmeasured
- checkout was never followed; the Get Premium CTAs were measured only
- the paywall X close button was never pressed; its destination is unrecorded

## [Butter](../systems/butter) — `butter`
Access: signed out (every captured surface is public; the editor workspace, projects, exports, billing and checkout sit behind /login and were never reached)
- the signed-in workspace entirely: the editor, projects, exports, billing and API-key flows live behind /login and were never reached
- /login was captured as a surface, never filled or submitted
- checkout and signup were never followed; every Try-for-free, Get-Started and Choose-plan action was measured only

## [Cake Equity](../systems/cakeequity) — `cakeequity`
Access: signed out (every captured surface is public; the equity-management workspace, cap table, grants, documents, billing and checkout sit behind app.cakeequity.com and were never reached)
- the signed-in workspace entirely: the equity app, cap table, grants, scenario models, documents, stakeholders, reports, billing and checkout live behind app.cakeequity.com and were never reached
- the login card (Kinde hosted) was captured as a surface, never filled or submitted
- signup and checkout were never followed; every Get-started-free, Start-free and Book-a-demo action was measured only; the HubSpot demo form is a cross-origin iframe captured as a region

## [Cal.com](../systems/cal) — `cal`
Access: signed out (every captured surface is public; the product — scheduler, event types, availability, bookings, workflows, insights, settings — sits behind app.cal.com login and was never reached; no booking was created)
- the signed-in product entirely: the scheduler, event-type editor, availability, bookings, workflows, insights and settings live behind app.cal.com login and were never reached
- the login and signup cards were captured as surfaces, never filled or submitted
- no booking was created: the booker's day cells, slot list and guest-details form were toggled as local state and Confirm was never pressed
- signup, SSO and checkout were never followed; every Get-started/Sign-up-with/Continue action was measured only
- booking pages vary per host: this capture is cal.com/peer's event type with its #292929 brand paint

## [Dock](../systems/dock) — `dock`
Access: signed out (every captured surface is public; the Dock workspace sits behind auth.dock.us and was never reached; the HubSpot demo form and the auth cards were measured, never filled or submitted)
- the signed-in workspace entirely: rooms, deal portals, content library, learning paths, settings and billing live behind auth.dock.us and were never reached
- the login/signup cards and the HubSpot demo form were measured as surfaces, never filled or submitted; their Continue/submit actions were never pressed

## [Buy Me a Coffee](../systems/buymeacoffee) — `buymeacoffee`
Access: signed out (every captured surface is public; the creator dashboard, shop/membership/extras managers, payouts, analytics and settings sit behind /login, the Stripe checkout behind Support was never opened, and the password step behind Continue-with-email was never submitted)
- the signed-in dashboard entirely: the page editor, membership/shop/extras managers, payouts, analytics and settings live behind /login and were never reached
- the Stripe checkout behind the Support and Join buttons was never opened; both are submits, measured never pressed
- /login and /signup were captured as cards, never submitted; the password input lives in a second step behind Continue-with-email and was never reached

## [BYBORRE](../systems/byborre) — `byborre`
Access: signed out (every captured surface is public; the Design Studio, dashboard, saved designs, ordering, checkout and account sit behind the /login panel and were never reached)
- the signed-in product entirely: the Design Studio, dashboard, saved designs, ordering, checkout and account sit behind the 'Log in to continue' panel and were never reached
- /login was captured open as a surface, never filled or submitted
- order, cart, Get-in-touch and every external link (help-center, news, the pcon catalogue, careers, socials) were measured or screenshotted, never followed

## [Calendly](../systems/calendly) — `calendly`
Access: signed out (every captured surface is public; the workspace, event-type editor, integrations and billing sit behind /app/login and were never reached; the invitee confirmation past a time slot was never opened)
- the signed-in workspace entirely: event types, availability, meetings, routing, workflows, contacts, integrations, analytics and billing live behind /app/login and were never reached
- /login and /signup were captured as surfaces, never filled or submitted
- the invitee confirmation past a time slot (name/email form, $53 payment step) was never reached; a day was selected but nothing was booked
- /integrations redirects to /app/login signed out

## [Canva](../systems/canva) — `canva`
Access: signed out (every captured surface is public; the editor, Brand Kit, dashboards, teams, billing and account sit behind the /login and /signup cards and were never reached; no form was submitted and no account created). Served the Singapore region: prices render S$
- the signed-in product entirely: the design editor, Brand Kit, dashboards, teams, billing and account sit behind the auth card and were never reached
- /login and /signup captured as a surface; 'Continue with email' was pressed once to reveal the username field (a local UI step, focused and sample-filled then deleted) - Continue was never pressed and no form was submitted
- Sign up, Get started, Start a free trial, Contact Sales and the OAuth providers were measured or screenshotted, never followed

## [DoorDash](../systems/doordash) — `doordash`
Access: signed out (every captured surface is public; the address gate, sign-in, ordering, cart, checkout, DashPass and merchant/Dasher onboarding were never crossed; catalog bodies that hydrate from live APIs render as the product's own loading spinner)
- the signed-in product entirely: the address gate, sign-in, ordering, cart, checkout, DashPass purchase, merchant and Dasher onboarding were never crossed; the identity.doordash.com OAuth anchors were measured, never followed
- the address-search field was focused once for measurement, never filled or submitted; the cookie banner and dormant Turnstile nodes were hidden and never answered
- icons: no standalone SVG set lifted this pass; icon.png is the site's published favicon (32 px source, the largest the site ships, upscaled to 128 px)

## [Dona](../systems/dona) — `dona`
Access: signed out (every captured surface is public: /, /about, /privacy-policy, /terms-of-service; the product on app.dona.ai sits behind sign-in and was never reached; the newsletter was never submitted and the cookie banner never answered)
- app.dona.ai entirely: the to-do product — lists, the advertised light/dark/black UI themes, sync, accounts — lives behind sign-in and was never reached; Login and Try for free open that host and were never followed
- external links (twitter.com/getdona, the Discord invite) were never followed

## [Douze](../systems/drinkdouze) — `drinkdouze`
Access: signed out (every captured surface is public; checkout, a filled cart, /account past the login/register forms and subscription management were never reached — nothing was added to the cart, no form was ever submitted, and no consent or newsletter overlay was ever answered)
- checkout, a filled cart, payment, /account past the login and register forms, and subscription management were never reached — nothing was added to the cart and no submit was ever pressed
- the subscription (Appstle) purchase-option radios did not render on load signed out — they appear in the variant screenshot after a pack-size is picked, never toggled

## [Doctronic](../systems/doctronic) — `doctronic`
Access: signed out (every captured surface is public; the chat product's threads, health record, prescriptions, appointments, account and billing sit behind the sign-in card and were never reached)
- the signed-in product entirely: chat threads, health record, prescriptions, appointments, account and billing sit behind the sign-in card and were never reached
- the ?modal=signin card was rendered from its public URL and measured; Log in with email, the OAuth buttons and Create an account were never pressed
- Start chat, Send message, Check My Symptoms, the starter chips and the Anonymous badge were measured, never pressed — each would start a session or submit text
- site-menu drawer and footer links to account surfaces were measured, never followed

## [DocuSign](../systems/docusign) — `docusign`
Access: signed out (every captured surface is public; the apps.docusign.com workspace, envelopes, templates and billing sit behind account.docusign.com and were never reached; no form was submitted, no plan purchased, no consent control answered)
- the signed-in product entirely: envelopes, templates, CLM, workflows, billing and admin live behind account.docusign.com and were never reached
- the trial, hero and sign-in forms were measured with sample text typed and deleted, never submitted
- no plan was purchased and no Buy-now/Contact-sales/ Try-for-free CTA was followed past its public landing

## [Doppler](../systems/doppler) — `doppler`
Access: signed out (every captured surface is public; the product — the secrets dashboard, projects, configs, service tokens, logs and billing — sits behind sign-in on dashboard.doppler.com and was never reached; the demo request form was never submitted)
- the signed-in product entirely: the secrets dashboard, projects, configs, service tokens, logs, integrations management and billing live behind sign-in on dashboard.doppler.com and were never reached; Start for Free and Sign In point off-site and were measured, never followed

## [Dropbox](../systems/dropbox) — `dropbox`
Access: signed out (every captured surface is public; the file dashboard, Paper/Dash/Replay/Sign workspaces, account and billing sit behind the auth cards and were never reached; dash.dropbox.com and the sign-in-embed hosts were never opened; the login/register fields were focused and sample-filled then deleted, never submitted)
- the signed-in product entirely: the file dashboard, Paper/Dash/Replay/Sign workspaces, account, billing and checkout sit behind the auth cards and were never reached
- /login and /register captured as surfaces: the email fields were focused and given sample text that was deleted; Continue, the SSO buttons and every Try-for-free/Buy-now/Get-started action were measured, never followed
- the auth cards run an older susi sheet (lucida grande stack, 4px radii) distinct from the DIG marketing system

## [DailyArt Magazine](../systems/dailyartmagazine) — `dailyartmagazine`
Access: read-only (the magazine is fully public; Shop and Courses lead off-domain and were measured as links, never followed)
- the newsletter and Contact Form 7 fields were focused and filled with sample text then cleared - never submitted; the acceptance/checkbox native inputs are visibility:hidden/opacity:0 and the boxes are painted by their labels
- breadcrumbs exist only in JSON-LD - no breadcrumb UI paints on the article; author archives and tag indexes reuse the feed layout and were not individually captured

## [Deel](../systems/deel) — `deel`
Access: read-only (the marketing site is fully public; the product lives behind app.deel.com - an authenticated boundary never reached; Book a demo, Claim offer and Log in were measured as destinations, never followed)
- the product lives behind app.deel.com - an authenticated boundary never reached; every Log in, Book a demo and Claim offer destination was measured, never followed

## [Care.com](../systems/care) — `care`
Access: signed out (every captured surface is public; the member dashboard, messaging, bookings, payments, applications and plan checkout sit behind /vis/auth/login and were never reached; the login and get-started shells were measured as boundary cards, never filled)
- the signed-in member product entirely: dashboard, messaging, bookings, payments, job applications and full caregiver profiles live behind auth and were never reached
- the login email step and the get-started chooser were captured as boundary cards, never filled or submitted; the password step and two-factor screens were never reached
- search, booking and checkout were never followed; every ZIP Search, City/State, Filter, provider link, Join-now and Get-started action was measured only

## [Cartesia](../systems/cartesia) — `cartesia`
Access: signed out (the marketing pages, the Clerk sign-in/sign-up cards and the Mintlify docs are public; the voice playground, console, cloning, agents, API keys and billing sit behind sign-in on play.cartesia.ai and were never reached; the live-agent calls were never started)
- the signed-in playground entirely: the voice console, cloning, agents, files, API keys and billing live behind sign-in on play.cartesia.ai and were never reached
- the sign-in/sign-up cards were measured as forms, never filled or submitted
- checkout and onboarding were never followed; every Try Cartesia, Talk to Sales and plan CTA was measured only

## [Copy.ai](../systems/copy) — `copy`
Access: signed out (every captured surface is public; the workflows builder, GTM dashboards, chat, tables, teams, billing and account sit behind the login.copy.ai card and were never reached; the contact form's fields were focused and filled then cleared, no form was submitted and no account created)
- the signed-in product entirely: the workflows builder, GTM dashboards, chat, tables, teams, billing and account sit behind the login.copy.ai card and were never reached
- the login.copy.ai card captured as a surface; its email field was measured, never sent; both OAuth providers measured, never followed
- the hero email capture and the contact form were focused and filled then cleared, never submitted; Get a Demo, Try for free, Get started, Sign up and Contact Sales never followed

## [Dopper](../systems/dopper) — `dopper`
Access: signed out (every captured surface is public; the customer account, checkout and filled cart behind the login and cart cards were never reached; no form was submitted, no account created, and the Cookiebot dialog was hidden, never answered). English locale, EUR prices
- the signed-in product entirely: customer account, order history, checkout flow and the filled cart sit behind the login/cart cards and were never reached; Add to cart was measured, never really clicked
- the login fields were focused, typed into and cleared - Sign in was never pressed and no form was submitted
- the 'For Businesses' B2B portal, Digital Product Passport, Tap/Map/community apps and non-English locales are linked surfaces that were not captured

## [Cosmos](../systems/cosmos) — `cosmos`
Access: signed out (every captured surface is public; the saved-element feed, boards, clusters and settings sit behind the /login card and were never reached; the login fields were focused and sample-filled then cleared, never submitted; no account created).
- the signed-in product entirely: the feed, boards, clusters and settings sit behind the /login card and were never reached
- /login captured as a surface; fields were focused and sample-filled then cleared - Next was never pressed and no form was submitted
- Join Cosmos for free, Sign up and /start were measured or screenshotted, never followed past the first step; no account was created

## [Craft](../systems/craft) — `craft`
Access: signed out (every captured surface is public; there is no auth card on www.craft.do - Log in links out to docs.craft.do and was never followed; Try Craft Free and the platform buttons lead to /download and were never used; the billing toggle was flipped locally and flipped back, nothing purchased). Served the Singapore region: prices render SGD.
- the product entirely: the docs editor, tasks, calendar and app surfaces live in the apps; www.craft.do has no auth card (Log in links out to docs.craft.do, never followed)
- Try Craft Free, the platform download buttons, plan CTAs and Get Started were measured or screenshotted, never followed - nothing downloaded or purchased

## [Craftwork](../systems/craftwork) — `craftwork`
Access: signed out (every captured surface is public; the account, cart/checkout, asset downloads, the Pro purchase and the author dashboard sit behind the /login OTP card - Send code was never pressed and no form was submitted). The fixed cookie notice was hidden, never answered.
- the signed-in product entirely: the account, cart/checkout, asset downloads, the Pro purchase and the sell/author dashboard sit behind the OTP card and were never reached
- /login captured as a surface; the email field was filled with a placeholder and cleared - Send code and Log in with Google were never pressed
- Get full access, Connect agent, every plan CTA and the deal's purchase CTA were measured or screenshotted, never followed

## [Creative Market](../systems/creativemarket) — `creativemarket`
Access: signed out (every captured surface is public; the account dashboard, purchases, downloads, checkout and the sell studio sit behind the /sign-in card and were never reached; no form was submitted, nothing was added to the cart and no consent button was pressed)
- the signed-in product entirely: the dashboard, purchases, downloads, cart checkout and the sell studio sit behind /sign-in and were never reached
- /sign-in captured as a surface; the username field was filled with a placeholder and cleared - Log In and the SSO buttons were never pressed and no form was submitted
- Add to cart, Buy now, license radios, bundle checkboxes, every membership CTA, Save 25% and FOLLOW were measured or screenshotted, never followed

## [Cron](../systems/cron) — `cron`
Access: signed out (every captured surface is public; the Cron app, its Notion Calendar successor, docs and the demo sit behind Login/Sign up and outbound links, none of which was followed; nothing was submitted)
- the signed-in product entirely: the Cron app (calendar.cron.com) and the Notion Calendar successor it redirects to sit behind Login/Sign up and were never reached
- Login, Sign up, the Notion Calendar banner link, Docs and the see-the-demo link were measured or screenshotted, never followed

## [Dribbble](../systems/dribbble) — `dribbble`
Access: signed out (every captured surface is public; posting shots, following, hiring flows, inboxes and dashboards sit behind /session/new and were never reached; the signed-out feed itself stops at one shot card plus a sign-up wall, which is where the package stops; no form was submitted and no account created)
- the signed-in product entirely: posting, following, hiring flows, inboxes and dashboards sit behind sign-in and were never reached
- /session/new and /signups/new captured as surfaces; the email field typed sample text and deleted it — nothing was submitted and no OAuth flow started; the Continue-with-Google GSI button is third-party-rendered and was hidden like every overlay, so it is a documented gap

## [Curater](../systems/curater) — `curater`
Access: signed out (every captured surface is public; creating curations, the TasteScope questionnaire, saving items and settings sit behind 'Log in or sign up' / the Google SSO button and were never reached; nothing was submitted and no account created)
- the signed-in product entirely: creating curations, the TasteScope questionnaire, saving items and settings sit behind 'Log in or sign up' / Google SSO and were never reached
- the search field collapses when the pointer leaves the toggle area; it was opened locally and left open, nothing typed or submitted

## [Cushion](../systems/cushion) — `cushion`
Access: signed out (every captured surface is public; the real app sits behind Log in / Sign up / Get started and was never reached; the 'Acme Inc' inbox on the home page is a marketing mock, not the authenticated product; no form was submitted and nothing was downloaded).
- the signed-in product entirely: real inboxes, posting, check-ins, settings and the desktop download sit behind Log in / Sign up / Get started and were never reached
- the 'Acme Inc' inbox on the home page is a rendered marketing mock, measured as DOM but not the authenticated app
- Log in, Sign up, Get started, Talk to a human and the download/store links were measured or screenshotted, never followed
- the FAQ accordion was toggled locally to measure its opened state; nothing was typed or submitted anywhere

## [Dub](../systems/dub) — `dub`
Access: signed out (every captured surface is public; the link-management workspace, analytics, domains, settings and billing sit behind /login on app.dub.co and were never reached; the login, register and contact-sales forms were measured, never filled past a deleted sample, never submitted; the docs search palette and Mintlify AI assistant were never opened)
- the signed-in workspace entirely: link management, analytics, domains, tags, webhooks, integrations, settings and billing live behind app.dub.co/login and were never reached
- /login and /register were captured as surfaces, never filled past a deleted sample or submitted
- the demo-panel under the home hero is a published dashboard mock, not the app
- hero-badge and sales-submit focus-visible recorded failed states (a real keyboard focus could not be held)

## [ElevenLabs](../systems/elevenlabs) — `elevenlabs`
Access: signed out (every captured surface is public; the Studio, agents platform, voice library, API keys, billing and account sit behind the /app/sign-in and /app/sign-up cards and were never reached; no form was submitted, no account created and the Cookiebot layer was hidden, never answered). The home TTS playground's Play was pressed once, a public affordance that generates without an account
- the signed-in product entirely: the Studio, agents platform, voice library, API keys, billing and account sit behind the auth card; /app redirects to /app/sign-in and was never entered
- /app/sign-in and /app/sign-up captured as surfaces; the email/password fields were focused and sample-filled then deleted, leaving the submits disabled and never pressed; no form was submitted
- Sign up, Subscribe, Get API key, Contact Sales and the OAuth providers (Google / Apple / SSO) were measured or screenshotted, never followed
- the home TTS playground's Play was pressed once and generated without an account; the voice-orb and sample-card play buttons were measured but not played, and the voice-chat launcher was never opened

## [Elektron](../systems/elektron) — `elektron`
Access: signed out (every captured surface is public; the account dashboard, order history, serial-registered downloads and checkout sit behind the /my-account magic-login card and were never reached; no code was requested, no form submitted, nothing added to the cart and no account created)
- the signed-in product entirely: the account dashboard, orders, registered machines and serial downloads sit behind the magic-login card and were never reached; no code was requested
- ADD TO CART, EXPLORE, SUBMIT, CONTINUE SHOPPING, Send me a code and Create New Account were measured across their states, never pressed; the cart stayed empty and no checkout surface was reached
- field states were typed sample text that was deleted again; nothing was submitted

## [Elementor](../systems/elementor) — `elementor`
Access: signed out (every captured surface is public; the Elementor editor, the my.elementor.com dashboard, hosting, billing and account sit behind Log in/Get started and were never reached; the contact form was never submitted, Buy now never pressed, and the Cookiebot consent dialog was hidden rather than answered)
- the signed-in product entirely: the Elementor editor, the my.elementor.com dashboard, hosting, billing and account sit behind Log in/Get started and were never reached
- /contact captured as a surface: the popup form was opened by its card, the name field sample-filled and deleted, the checkbox toggled locally - submit was never pressed and nothing was sent
- Buy now, Get started, Log in and every signup action were measured or screenshotted, never followed (they open checkout or my.elementor.com)

## [Endel](../systems/endel) — `endel`
Access: signed out (every captured surface is public: the endel.io marketing pages plus app.endel.io's explore, player and sign-in card; the account, library, premium unlock/checkout and any form submit were never crossed; the Set Timer sheet, More flyout and mobile menu were opened by their own toggles and closed again)
- the signed-in app entirely: account, library, sync, settings, purchase and the premium unlock/checkout the timer sheet's Unlock row starts were never reached; the FREEMIUM chip, scenario pills, Unlock, Continue and the OAuth buttons were measured, never pressed for real
- no form was submitted and no account created: the footer newsletter field and the sign-in card's email field were measured, never sent; Try Today, Subscribe, Continue, Unlock and every outbound link were never followed
- the home page's mid-page newsletter row (input-email, btn-subscribe) was not on the page at capture time; the footer's own field was painted instead

## [Editor X (Wix Studio)](../systems/editorx) — `editorx`
Access: signed out (every captured surface is public; editorx.com 301s to wix.com/studio for every path except /pricing, which served its Premium-plans error pane at capture time; the Studio editor, workspaces and checkout sit behind Log In / Start Creating and were never reached; no form was submitted and no account created)
- the signed-in product entirely: the Studio editor, workspaces, dashboards, signup and checkout sit behind Log In / Start Creating and were never reached
- the only presses were local UI toggles: the Product dropdown, the FAQ expander, the mobile menu; no form was submitted and no action followed

## [Endless Tools](../systems/endlesstools) — `endlesstools`
Access: signed out (every captured surface is public: / on endlesstools.io plus /login, /legal/privacy_policy and /legal/terms_of_use on app.endlesstools.io; the product editor behind sign-in was never reached; no form was submitted and the only presses were local UI toggles)
- the editor entirely: the canvas, tools, panels, library and AI features live behind sign-in on app.endlesstools.io and were never reached; Start for free, the plan CTAs and Create team open signup and were never followed
- the login card's two forms (OTP send-code and password) were measured and locally switched; neither was submitted, so the code entry, errors and signed-in redirect are uncaptured
- the newsletter form was measured and its consent checkbox toggled for the capture; it was never submitted, so its success and any error state are uncaptured

## [ElevenReader](../systems/elevenreader) — `elevenreader`
Access: signed out (every captured surface is public: the marketing pages, one public audiobook page and the /reader sign-in/sign-up cards; the reader app - library, upload, player, settings, billing - sits behind /reader/sign-in and was never reached; the email forms were revealed by their own toggles and never submitted)
- the reader app entirely: library, upload, the reader/player, settings and billing live behind /reader/sign-in and were never reached; /reader/sign-in and /reader/sign-up were captured as boundary cards
- the OAuth buttons were never pressed; the email credential forms were revealed by their own 'with email' toggles (local UI, nothing sent), fields were focused and sample text was typed and deleted - no form was ever submitted, so error/success states are uncaptured

## [Endless](../systems/endless) — `endless`
Access: signed out (every captured surface is public; the workspace behind sign-up on s.endless.app, auth on clerk.endless.app, was never reached; no form was submitted and no tool was run)
- the signed-in workspace entirely: chat, canvas, projects, files, MCP connections, billing and onboarding live behind s.endless.app (auth on clerk.endless.app) and were never reached
- no form was ever submitted and no tool was ever run: the contact Send button and every Generate action were measured, not pressed, so success, error, progress and result-gallery states are uncaptured
- checkout, plan purchase and localized routes were never reached

## [ElevenMusic](../systems/elevenmusic) — `elevenmusic`
Access: signed out (every captured surface is public: /, /explore, /charts, /tracks, /genres, /genres/electronic, /sounds, /tools, an artist profile, a playlist, /blog, /pricing, /login, /sign-in; Create/Composer/Library/Chat/publish, Likes, Remixes, Shares and search itself sit behind sign-in and were never entered or submitted)
- the signed-in product entirely: Create, Composer, Chat, Library, artist-page publishing, account settings and billing need an account and were never reached; /login and /sign-in were measured as forms and never submitted
- search is gated: the rail's Search button opens the log-in dialog (captured as evidence), so a real search surface is uncaptured
- every Create button, prompt submit and Attach control was measured, never pressed — a prompt is a generation request
- the Get-Pro and Start-free CTAs were measured, never followed past the public card; checkout is uncaptured

## [Deezer](../systems/deezer) — `deezer`
Access: read-only (the marketing site, the public catalog pages and the account forms are fully public; everything behind account.deezer.com is an authenticated boundary never reached; Try-for-free, Sign-up, Mix, Play, queue and volume actions were measured, never followed; the login and signup forms were never submitted)
- every post-login surface (library, Flow, playlists, downloads, settings, billing) lives behind account.deezer.com - an authenticated boundary never reached
- the login and signup forms were measured as forms, never filled or submitted; validation, error and success states are absent rather than measured

## [Epidemic Sound](../systems/epidemicsound) — `epidemicsound`
Access: read-only (the marketing site, the public catalog, SFX and artist pages and the account forms are fully public; everything behind login.epidemicsound.com is an authenticated boundary never reached; Play, Download, Subscribe, Create-free-account and Log-in actions were measured, never followed; the login and signup forms were never submitted)
- every post-login surface (library, playlists, downloads, billing, account settings) lives behind login.epidemicsound.com - an authenticated boundary never reached
- the login and signup forms were measured at rest, never filled with real credentials or submitted; validation, error and success states are absent rather than measured

## [Enode](../systems/enode) — `enode`
Access: read-only (the marketing site and the platform login page are fully public signed out; everything behind platform.enode.com - the dashboard, docs portal, API surfaces - is an authenticated boundary never reached; the contact and login forms were measured and typed into then cleared, never submitted; every CTA and link was measured, never followed; the dormant Cookiebot layer shows no banner and was never answered)
- every post-login platform surface (dashboard, asset management, API keys) and docs.enode.com lives behind an account - an authenticated boundary never reached
- the /contact, /contact/partnerships and platform login forms were measured at rest and typed into then cleared, never submitted - validation, error, loading and success states are absent rather than measured

## [Delphi](../systems/delphi) — `delphi`
Access: read-only (the home page, /discover/<topic> galleries, /search/<question> results, /<expert> profiles and /<expert>/chat are fully public signed out; creating a clone, saving perspectives and every post-login surface is an authenticated boundary never reached; Sign In, Continue with Google/Email, Share, Save, Expand, Personalize, suggested-question chips, the microphone and the chat send were measured, never followed or submitted)
- creating a clone, saving perspectives, personalising results and every post-login surface need an account - an authenticated boundary never reached
- the Sign-In/onboarding dialogs were measured as dialogs; Continue with Google/Email were never pressed, so the auth flow past the dialog is unmeasured

## [Esquire](../systems/esquire) — `esquire`
Access: signed out (every surface captured is public; account.esquire.com sign-in and the shop.esquire.com subscription checkout are off-domain boundaries that were measured, never followed; the newsletter and search fields were typed into and cleared, never submitted)
- every signed-in surface (bookmarks, comment counts, the premium archive) lives behind Sign In on account.esquire.com - an authenticated boundary never reached
- the Join/Subscribe buttons lead to shop.esquire.com checkout - measured, never followed; purchase, payment and confirmation states are absent rather than measured

## [Descript](../systems/descript) — `descript`
Access: read-only (the marketing site is fully public; the product lives behind web.descript.com - its sign-in card was captured as a boundary, measured and never submitted; Sign in, Sign up, Get started and every plan CTA were measured as destinations, never followed)
- the product lives behind web.descript.com - the sign-in card's buttons and email field were measured and the field typed/cleared, never submitted; no authenticated page was reached
- Sign in, Sign up, Get started, Try free, Request a demo and every plan CTA were measured as outbound/form destinations, never followed

## [Exa](../systems/exa) — `exa`
Access: read-only (every captured surface is public and signed out; the dashboard, API keys and playground behind auth.exa.ai were never reached - login routes rate-limited or redirected during reconnaissance; the login and e-mail fields were focused and filled then cleared, never submitted; the home demo's Run-preview arrow, Get-started and Sign-up actions were measured, never pressed)
- every post-login surface (the dashboard, API keys, the playground, billing) sits behind auth.exa.ai - an authenticated boundary never reached; dashboard.exa.ai/login and /playground/search rate-limited (HTTP 429) during reconnaissance
- the sign-in and e-mail fields were focused and filled with test text, then cleared - never submitted; validation, error and success states are absent rather than measured
- the marketing site and sign-in card paint light only - the dark set covers the docs alone

## [Exactly.ai](../systems/exactly) — `exactly`
Access: read-only (the marketing site, pricing, showcase, case studies, industries, help center and book-a-demo are fully public; everything on threads.exactly.ai is an authenticated boundary behind a Cloudflare check never bypassed; Log in, Start for free and Book a demo were measured, never followed; the help search was typed and cleared, never submitted; the scheduler was measured at rest)
- the product itself - studio, model training, the image generator, credits, billing and every account surface - lives on threads.exactly.ai behind a Cloudflare check that was never bypassed
- the Log in, Start-for-free and Book-a-demo links were measured, never followed; the scheduler was measured at rest - no day, time or contact detail was ever picked or typed

## [Equals](../systems/equals) — `equals`
Access: read-only (the marketing site, the go.equals.com sign-in card and the docs are fully public; the spreadsheet workspace and every post-login surface are an authenticated boundary never reached - app.equals.com did not answer; the sign-in and demo e-mail fields were focused and filled for measurement, then cleared, never submitted; Get-a-demo, plan and trial actions were measured, never followed)
- the authenticated product - workbook, dashboards, datasources, settings and every post-login surface - was never reached; app.equals.com did not answer during the capture
- the sign-in form and the demo e-mail captures were measured as fields, never submitted; validation, error and success states are absent rather than measured
- the mobile capture of /use-cases/arr-dashboard/ hit a security challenge; component readings fall back to the desktop measurement

## [Epic Games Store](../systems/epicgames) — `epicgames`
Access: read-only (every captured surface is public: the storefront, the sign-in dialog, the support centre and the marketing home); the sign-in form and both search fields were measured, never submitted; Get, Add to Cart, Wishlist, Download, sort options and filter checkboxes were measured, never activated
- every post-login surface (library, account, billing, cart, checkout) is an authenticated boundary never reached
- the sign-in form was measured default/focused/filled, never submitted; validation, error and success states are absent rather than measured

## [Excalidraw](../systems/excalidraw) — `excalidraw`
Access: read-only (the whole editor is public signed out; nothing was drawn, opened, saved, shared, exported or generated; Open, Save, Export actions, Live collaboration, Share, the AI tools, Reset the canvas and every Sign up were measured, never pressed; Excalidraw+ needs an account and was never reached)
- Excalidraw+ (saved workspaces, cloud library, collaboration management, billing) needs an account and was never reached; no signup or login path was followed

## [Expedia](../systems/expedia) — `expedia`
Access: signed out (every captured surface is public); expedia.com answers automation with a 429 "Bot or Not?" challenge, so the DOM evidence is a Wayback snapshot served locally and painted with live travel-assets.com CSS/fonts
- anything behind sign-in: trips, account, member pricing, checkout, booking, saved items
- submitted states: search was never submitted; sort/filters never applied; only screenshot evidence for the opened sort menu

## [Fable](../systems/fable) — `fable`
Access: read-only (the marketing pages, /clubs, /books, genre/club/book detail pages, /discover, /signin, /signup, /support, /blog and /community-guidelines are fully public signed out; joined clubs, discussions, the reader, lists, streaks, cart and checkout need an account - an authenticated boundary never reached; the sign-in form and SSO buttons, Join, Want to read, store badges and every CTA were measured, never submitted, pressed or followed; the Osano consent layer was hidden, never answered)
- every post-login surface (joined clubs, discussion threads, the book reader, lists, streaks and stats) needs an account - an authenticated boundary never reached
- cart, checkout and ebook purchase flows were never opened; App Store / Google Play badges and 'Get the app' CTAs were measured, never followed
- the sign-in and sign-up forms were measured at rest and typed into then cleared, never submitted - validation, error, loading and success states are absent rather than measured; 'Continue with Google/Apple' was never pressed
- 'Join the club', 'Want to read', the spoiler toggle, 'Read more' and the FAQ accordion are local UI - the disclosure toggles were opened for capture and nothing was submitted or joined

## [Faire](../systems/faire) — `faire`
Access: signed out (every captured surface is public; search results, product detail, cart, checkout, account and the brand portal are behind the sign-up/sign-in dialogs - a documented authenticated boundary never crossed)
- every post-auth surface - search results, product detail, cart, checkout, account and the brand portal - sits behind the sign-up/sign-in dialogs; every product tile links ?signUp=product, an authenticated boundary never crossed
- the /apply stepper's steps past 1 need a submitted first step; step 1 was filled and cleared, never sent
- the observed sign-up dialog mounts no Apple SSO button; signup-apple is recorded missing

## [Explore](../systems/explore) — `explore`
Access: read-only (every public surface signed out; the site itself is offline - the product closed 2023-04-19 and the domain later lapsed - so all pages were replayed from a local Internet Archive mirror of the 2023-02-23 build, with the closure shell from the 2023-06-08 snapshot; auth forms were measured and typed into then cleared, never submitted; no backend was ever reached; member names and works on the SSR profiles are public archive records reproduced as captured)
- every signed-in member surface (network feed, composer, notifications, saved, subscriptions, settings) plus the dark member-portfolio theme lives behind accounts that closed with the product - an authenticated boundary never reached
- SPA routes whose API records were never archived (/user/*, /post/*) render signed-out shells; member profiles survive only in the three archived SSR HTML pages
- the login/register/forgot-password fields were measured at rest and typed into then cleared, never submitted - validation, error, loading and success states are absent rather than measured

## [Factory](../systems/factory) — `factory`
Access: read-only (factory.com, docs.factory.com and the auth.factory.ai sign-in card are fully public signed out; everything behind app.factory.ai - the Droid console, missions and settings - is an authenticated boundary never reached; the /contact HubSpot form and the sign-in card were measured and typed into then cleared, never submitted; every CTA and link was measured, never followed; overlays were hidden, never answered)
- every post-login app surface (the Droid console, missions, settings) sits behind app.factory.ai - an authenticated boundary never reached; the auth.factory.ai sign-in card is a different app that does not share the marketing token layer
- the /contact HubSpot form and the sign-in card were measured at rest and typed into then cleared, never submitted - validation, error, loading and success states are absent rather than measured
- factory.com/changelog and docs.factory.com/changelog answer a Vercel-login 404 shape; the working changelog at docs.factory.com/docs/changelog/release-notes was captured instead

## [Visual (designstripe)](../systems/designstripe) — `designstripe`
Access: read-only (the home page, /assets library and /assets/<kind>/<set> galleries, /tools, /about, /contact and /blog articles are fully public signed out; the design agents, account asset downloads and every post-waitlist surface are an authenticated boundary never reached; the WAITLIST buttons, nav links, category tiles, tool cards and article links were measured, never followed or submitted)
- the design agents, account asset downloads and every post-waitlist surface need an account - an authenticated boundary never reached

## [Family](../systems/family) — `family`
Access: read-only (family.co marketing pages, /docs, /support and the app.family.co login are fully public signed out; the signed-in Aave Account product and the iOS wallet are authenticated/native boundaries never reached; Log In, Get Started, Download on iOS and every Watch link were measured, never followed, and the login field and support search were typed into and cleared, never submitted)
- the signed-in Aave Account product and every post-login surface need an account - an authenticated boundary never reached
- Log In, Get Started, Download on iOS and every Watch link were measured, never followed; the login field and support search were typed into and cleared, never submitted

## [Fibery](../systems/fibery) — `fibery`
Access: read-only (the marketing site, fibery.io/sign-up and fibery.io/login/ are fully public signed out; everything past login - workspaces, views, the app's dark/system theme - is an authenticated boundary never reached; the sign-up prompt and login e-mail field were typed into then cleared, never submitted; the OAuth POST forms were never pressed; the wizard never advanced; every link and CTA was measured, never followed; the consent layer and Intercom widget were hidden, never answered)
- every post-login app surface - workspaces, entity views, whiteboards, automations, AI, admin - lives behind an account, an authenticated boundary never reached
- the app's dark/system theme (advertised on the login page) is behind sign-in and was not captured; the token file deliberately ships core + light only
- the sign-up wizard was never advanced past step one - 'Create workspace' and 'Start without AI' were never pressed - so steps 2+ and workspace creation are uncaptured
- the sign-up prompt and login e-mail field were typed into then cleared and never submitted, and the OAuth POST forms were never pressed - validation, error, loading and success states are absent rather than measured
- 'Book a demo' links to a scheduler that was never opened; 'Workspace SSO' was never followed

## [fal.ai](../systems/fal) — `fal`
Access: read-only (the marketing pages, the explore catalog, the model and API pages, the docs and the login card are fully public; everything past login - dashboard, API keys, billing, deployments, sandbox, inference - is an authenticated boundary never reached; OAuth, Sign-in-to-run, Open-in-Sandbox, Download, Contact-Sales and Get-Started were measured, never followed; the prompt field was filled and cleared without running a model; the consent card was hidden, never answered)
- every post-login surface (dashboard, API keys, billing, deployments) lives behind fal's account - an authenticated boundary never reached
- inference was never run: the prompt field was filled and cleared, Sign-in-to-run links to login signed out, Open-in-Sandbox and Download were measured, never followed
- the OAuth buttons and Use-SSO were measured at rest, never followed; validation, error and success states are absent rather than measured

## [FARFETCH](../systems/farfetch) — `farfetch`
Access: signed out (every captured surface is public); www.farfetch.com answers automation with Akamai 403 and the farfetch-contents.com CDNs with 429, so the DOM evidence is Wayback SSR snapshots served locally and painted by Farfetch's own archived CSS, fonts and images with scripts stripped
- anything behind sign-in: account, wishlist contents, bag, checkout, order tracking, FARFETCH Access loyalty, private client
- submitted states: search, newsletter and filters were typed/measured but never submitted

## Gate noted in access text only

### [1Password](../systems/1password) — `1password`
signed out (the vault is credential-gated and was never reached)

### [Aboard](../systems/aboard) — `aboard`
signed out (every captured surface is public); newsletter signup measured at rest and focus only, never submitted; the CookieYes consent strip never rendered headless

### [Aboard HR](../systems/aboardhr) — `aboardhr`
signed out (every captured surface is public); the book-a-demo form measured at rest and focus only, never submitted; app.aboardhr.com sign-in never opened

### [Acctual](../systems/acctual) — `acctual`
signed out (every captured surface is public); app.acctual.com sign-in never opened

### [Airtable](../systems/airtable) — `airtable`
signed out (every captured surface is public); the contact-sales form measured and focused but never submitted; the Qualified chat widget and Google One Tap swept out of every shot

### [Anthropic](../systems/anthropic) — `anthropic`
public marketing surface only; signed out; nothing submitted or signed into

### [Apollo GraphQL](../systems/apollographql) — `apollographql`
signed out (every captured surface is public); the OneTrust card was captured but never answered; studio.apollographql.com login/signup captured at rest, never submitted

### [Arc Search](../systems/arcsearch) — `arcsearch`
not signed in, iPhone Mirroring

### [Brilliant](../systems/brilliant) — `brilliant`
signed in, free account

### [Capy (desktop)](../systems/capy-desktop) — `capy-desktop`
the owner's signed-in account (personal workspace, no plan); read live from the running app over its remote-debugging port, plus Capy's component gallery at capy://app/design on fixture data, and a real agent run (Capy 0.5.0, Claude Code) in a project made for the capture on a scratch folder, run on the paired Mac

### [ChatGPT](../systems/chatgpt) — `chatgpt`
signed in, Free plan

### [ChatGPT for iOS](../systems/chatgpt-ios) — `chatgpt-ios`
signed in, workspace seat, iPhone Mirroring

### [Claude](../systems/claude) — `claude`
signed in, Max plan (2026-10-04; refreshed 2026-10-17 for forms, feedback and states)

### [Claude for iOS](../systems/claude-ios) — `claude-ios`
signed in, Max plan, iPhone Mirroring (dark 2026-10-23, light 2026-10-24)

### [Clerk](../systems/clerk) — `clerk`
signed-in Hobby workspace, development instance; public marketing landing page

### [Cloudflare](../systems/cloudflare) — `cloudflare`
Signed-in owner free-plan dashboard; public landing page separately labelled

### [Codex (desktop)](../systems/codex-desktop) — `codex-desktop`
signed in (the owner's second Codex account, Codex 2.app); read live from the running app over its remote-debugging port

### [Conductor (desktop)](../systems/conductor-desktop) — `conductor-desktop`
the owner's signed-in account on the Free plan; read live from the app's WKWebView through Safari's Web Inspector, on a scratch repository the capture added

### [Coursera](../systems/coursera) — `coursera`
public pages signed out, learner pages signed in

### [Cursor (desktop)](../systems/cursor-desktop) — `cursor-desktop`
signed in (the owner's Team plan); read live from the running app over its remote-debugging port

### [Cursor for iOS](../systems/cursor-ios) — `cursor-ios`
signed in, iPhone Mirroring

### [Devin (desktop)](../systems/devin-desktop) — `devin-desktop`
signed in (the owner's cortexairobot organisation); read live from the running app over its remote-debugging port

### [Duolingo](../systems/duolingo) — `duolingo`
signed in, free account

### [Gemini](../systems/gemini) — `gemini`
signed in, Google AI Pro, iPhone Mirroring

### [GitHub Mobile](../systems/github-ios) — `github-ios`
signed in, Copilot Pro, iPhone Mirroring

### [Grab](../systems/grab) — `grab`
signed in, iPhone Mirroring

### [Grok Bot](../systems/grokbot) — `grokbot`
signed in, paid plan, iPhone Mirroring

### [Grok Bot (desktop)](../systems/grokbot-desktop) — `grokbot-desktop`
signed in (the owner's account); read live from the running app over its remote-debugging port

### [Hevy](../systems/hevy) — `hevy`
signed in, free account, iPhone Mirroring

### [Linear](../systems/linear) — `linear`
public site measured signed out (2026-09-23); signed-in app measured from redacted page copies on the free plan (2026-10-17), owner signed in

### [Luma](../systems/luma-ios) — `luma-ios`
signed in, iPhone Mirroring

### [Manus](../systems/manus) — `manus`
signed in

### [Metabase (Edumation demo)](../systems/metabase) — `metabase`
Official public interactive Edumation demo; automatically supplied persona; unsaved navigation/form inspection; authorized Dark appearance restored to Light

### [Gemini Notebook (NotebookLM)](../systems/notebooklm) — `notebooklm`
signed in

### [Notion Calendar (desktop)](../systems/notion-calendar-desktop) — `notion-calendar-desktop`
signed in (the owner's account, two Google calendar accounts and four Notion workspaces); read live from the running app over its remote-debugging port

### [Notion (desktop)](../systems/notion-desktop) — `notion-desktop`
signed in (the owner's account and workspace); read live from the running app over its remote-debugging port, editing only a scratch page the capture created

### [Notion for iOS](../systems/notion-ios) — `notion-ios`
signed in, iPhone Mirroring

### [OpenCode (desktop)](../systems/opencode-desktop) — `opencode-desktop`
signed in (the owner's providers already connected); read live from the running app over its remote-debugging port

### [Orca (desktop)](../systems/orca-desktop) — `orca-desktop`
not signed in to an Orca account (not needed); read live from the running app over its remote-debugging port, on a scratch project the capture added and removed

### [Shopify Polaris (React archive)](../systems/polaris) — `polaris`
published packages and the archive repo at a pinned commit (2026-09-25); gallery re-shot and ramps, focus states and patterns added in headless Chromium (2026-10-17)

### [ResearchRabbit](../systems/researchrabbit) — `researchrabbit`
signed in

### [Sentry](../systems/sentry) — `sentry`
signed-in owner account; Developer plan observed; no trial activated

### [Spotify](../systems/spotify) — `spotify`
signed in, Premium Family plan, iPhone Mirroring

### [Substack](../systems/substack) — `substack`
signed in, iPhone Mirroring

### [Supabase](../systems/supabase) — `supabase`
signed in, free account; both projects paused; public landing

### [Superset (desktop)](../systems/superset-desktop) — `superset-desktop`
signed in (the owner's organisation on the free plan); read live from the running app over its remote-debugging port

### [Telegram](../systems/telegram) — `telegram`
signed in, iPhone Mirroring

### [TokenTracker](../systems/tokentracker) — `tokentracker`
local dashboard served by the TokenTracker CLI (v1.4.3), no account, headless Chromium

### [Untitled](../systems/untitled-stream) — `untitled-stream`
signed out (every surface captured is public; the app behind login was not captured)

### [YouTube](../systems/youtube) — `youtube`
signed in, free plan, iPhone Mirroring

### [Zed (desktop)](../systems/zed-desktop) — `zed-desktop`
the owner's signed-in Zed (Free plan) on a scratch folder; colours from Zed's published theme file at the v1.25.2 commit, sizes and type from 2x window pixels

## No gated surface recorded

`ableton`, `allbirds`, `anam`, `attio`, `gauth`, `raycast-desktop`, `refero-design`
