# Gated surfaces

What the library has NOT captured: every surface that sits behind a sign-in,
an account, a checkout or a submission in the signed-out captures. Generated
by `python3 tools/gated.py` from `capture.gaps` and `access` in
[catalog.json](../catalog.json); do not edit by hand.

Each entry is the catalog's own words. A package appearing here is not
incomplete — the capture was scoped to public surfaces on purpose — it is
the queue for any future authenticated pass, which needs the owner's
account and a fresh capture contract (docs/CAPTURE.md, docs/RIGHTS.md).

_273 of 459 packages name gated surfaces in their gaps; 165 more mark a gate in their access text; 21 report none._

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

## [Calendly](../systems/calendly) — `calendly`
Access: signed out (every captured surface is public; the workspace, event-type editor, integrations and billing sit behind /app/login and were never reached; the invitee confirmation past a time slot was never opened)
- the signed-in workspace entirely: event types, availability, meetings, routing, workflows, contacts, integrations, analytics and billing live behind /app/login and were never reached
- /login and /signup were captured as surfaces, never filled or submitted
- the invitee confirmation past a time slot (name/email form, $53 payment step) was never reached; a day was selected but nothing was booked
- /integrations redirects to /app/login signed out

## [Calm](../systems/calm) — `calm`
Access: signed out (every captured surface is public; the product past the login card, playback, library, checkout and every signed-in surface were never reached)
- the signed-in product entirely: playback, the home feed, library, profile, check-ins and checkout live behind the login card and were never reached
- the login card was opened by its own button, measured, and never filled or submitted; the Try Calm for Free button navigates to /signup-flow, which stayed PerimeterX-blocked this run and is recorded as a boundary
- no public pricing/plans page exists signed out: plan choices sit behind /signup-flow; /family (six premium accounts, SGD 93.99/year geolocated) and /gift (Gift a Year / Gift a Lifetime) are the public purchasable surfaces

## [Canva](../systems/canva) — `canva`
Access: signed out (every captured surface is public; the editor, Brand Kit, dashboards, teams, billing and account sit behind the /login and /signup cards and were never reached; no form was submitted and no account created). Served the Singapore region: prices render S$
- the signed-in product entirely: the design editor, Brand Kit, dashboards, teams, billing and account sit behind the auth card and were never reached
- /login and /signup captured as a surface; 'Continue with email' was pressed once to reveal the username field (a local UI step, focused and sample-filled then deleted) - Continue was never pressed and no form was submitted
- Sign up, Get started, Start a free trial, Contact Sales and the OAuth providers were measured or screenshotted, never followed

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

## [Chargetrip](../systems/chargetrip) — `chargetrip`
Access: signed out (every captured surface is public: the www.chargetrip.com marketing routes, the account.chargetrip.io sign-in card, and developers/playground shells as boundaries; the routing engine, dashboard, API keys and every form submit were never crossed; the Cookie Settings card was hidden, never answered)
- the product itself: the routing engine, dashboard, API keys and the authenticated app sit behind account.chargetrip.io and were never reached; the sign-in card was measured and filled with the documented name@example.com test address, never submitted
- no form was submitted and nothing was booked: the sales form and newsletter field were focused, Book-a-demo / Plan-a-route / Contact-sales / Sign-in / Create-account / Send were never followed; the Cookie Settings card was hidden, never answered
- developers.chargetrip.com and playground.chargetrip.com were captured as boundary shells only; the credential-gated playground was never used
- the sign-in card runs a different stack (Tailwind v4, oklch) from the Framer marketing site; its tokens are marked measured, not declared

## [ClassPass](../systems/classpass) — `classpass`
Access: read-only (the marketing site, search, plans, features, how-it-works, fitness, gifts, reviews, partners, corporate-wellness, about, contact, blog and legal are fully public; /login's card and /walkthrough's carousel were measured as boundaries - nothing was signed into, searched for, booked or submitted; booking, member search results, credits and checkout sit behind sign-in or payment)
- the product itself - class booking, member search results, credits, plan checkout and account pages - sits behind sign-in or payment and was never crossed
- nav-login and nav-cta could not be given a real keyboard focus on this pass; their focus behaviour is published as unmeasured, not absent

## [Mesh](../systems/clay-earth) — `clay-earth`
Access: signed out (clay.earth 301-redirects to me.sh - the Clay product rebranded to Mesh, an Automattic product; every captured surface is public: the me.sh marketing routes and the app.me.sh sign-in card as a boundary; the app interior, plan checkout, downloads and every OAuth/sign-in action were never crossed; the sign-in e-mail field was focused and filled with placeholder text only)
- the product itself: the Mesh app interior, plan checkout, downloads (/start targets) and every account surface sit behind app.me.sh and were never reached; the sign-in card was measured and its e-mail field focused and filled with placeholder text only, never submitted
- no form was submitted, no plan purchased, no OAuth button pressed; the nav dropdowns and the mobile drawer were opened by their own toggles but nothing navigated
- the marketing site runs three skins on one product: the black marketing routes, the warm-cream /pricing route and the light app.me.sh sign-in card (SF Pro, #ff6821) - all tokenised, none toggled by the user

## [Clearful](../systems/clearful) — `clearful`
Access: signed out (the marketing routes, /library, /journal-prompts and legal are fully public; the journal app sits behind app.clearful.com sign-in - the public sign-in card was measured through the Flutter semantics overlay, never submitted; several CTA anchors point at # and were never followed)
- the journal app itself - entries, editor, settings - sits behind app.clearful.com sign-in and was never crossed; the sign-in card was measured but never submitted
- the sign-in card is a Flutter canvas: its colours cannot be read by CSSOM, so light.app.* values are pixel-sampled off the captured screenshot and labelled as such

## [Clipchamp](../systems/clipchamp) — `clipchamp`
Access: signed out (the marketing routes are fully public; the editor sits behind app.clipchamp.com sign-in - the public login card was measured at rest, the email path where the only field lives was never entered; consent and promo overlays were hidden without answering them; CTA anchors to signup/login were never followed)
- the editor itself - timeline, assets, export - sits behind app.clipchamp.com sign-in and was never crossed; the sign-in card was measured at rest but never submitted
- no credentials field renders on the sign-in card until the email path is entered; that path was never crossed, so no field was measured

## [Cofounder](../systems/cofounder) — `cofounder`
Access: signed out (the marketing routes are fully public; the Cofounder OS sits behind app.cofounder.co sign-in - the login card was measured at rest only; CTA anchors to the app were never followed; the hero copy-prompt button writes the clipboard so it was never pressed; no form was submitted and nothing was authenticated)
- the Cofounder OS - workspace, integrations, billing - sits behind app.cofounder.co sign-in and was never crossed; the login card was measured at rest but never submitted

## [Cohere](../systems/cohere) — `cohere`
Access: signed out (the marketing routes are fully public; the Cohere product sits behind dashboard.cohere.com sign-in - the welcome/login card was measured at rest only with no credentials typed and nothing submitted; nav/hero CTAs to sign-up and sales forms were never followed; no OAuth flow was started)
- the Cohere product - North, Command, the dashboard - sits behind dashboard.cohere.com sign-in and was never crossed; the login card was measured at rest but never submitted

## [Coinbase](../systems/coinbase) — `coinbase`
Access: signed out (the marketing routes are fully public; the Coinbase product sits behind login.coinbase.com - the /signin redirect's card was measured at rest only: the email field was focused once for its computed style, no text was typed, nothing submitted, and no OAuth/passkey flow was started; the OneTrust consent layer was hidden, never answered)
- the Coinbase product - portfolio, trading, wallets - sits behind login.coinbase.com sign-in and was never crossed; the sign-in card was measured at rest but never submitted
- the email field's focused border change lives on its container wrapper, not the input - the focused state records no outline change on the field itself

## [Column](../systems/column) — `column`
Access: signed out (the marketing routes are fully public; the Column product sits behind dashboard.column.com - the /login form was measured at rest only: the email field was focused once for its computed style, no text was typed, nothing submitted, and no passkey flow was started; the styled-components cookie banner was hidden, never answered)
- the Column product - dashboard, ledgers, transfers - sits behind dashboard.column.com sign-in and was never crossed; the login form was measured at rest but never submitted

## [Copy.ai](../systems/copy) — `copy`
Access: signed out (every captured surface is public; the workflows builder, GTM dashboards, chat, tables, teams, billing and account sit behind the login.copy.ai card and were never reached; the contact form's fields were focused and filled then cleared, no form was submitted and no account created)
- the signed-in product entirely: the workflows builder, GTM dashboards, chat, tables, teams, billing and account sit behind the login.copy.ai card and were never reached
- the login.copy.ai card captured as a surface; its email field was measured, never sent; both OAuth providers measured, never followed
- the hero email capture and the contact form were focused and filled then cleared, never submitted; Get a Demo, Try for free, Get started, Sign up and Contact Sales never followed

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

## [DailyArt Magazine](../systems/dailyartmagazine) — `dailyartmagazine`
Access: read-only (the magazine is fully public; Shop and Courses lead off-domain and were measured as links, never followed)
- the newsletter and Contact Form 7 fields were focused and filled with sample text then cleared - never submitted; the acceptance/checkbox native inputs are visibility:hidden/opacity:0 and the boxes are painted by their labels
- breadcrumbs exist only in JSON-LD - no breadcrumb UI paints on the article; author archives and tag indexes reuse the feed layout and were not individually captured

## [Deel](../systems/deel) — `deel`
Access: read-only (the marketing site is fully public; the product lives behind app.deel.com - an authenticated boundary never reached; Book a demo, Claim offer and Log in were measured as destinations, never followed)
- the product lives behind app.deel.com - an authenticated boundary never reached; every Log in, Book a demo and Claim offer destination was measured, never followed

## [Deezer](../systems/deezer) — `deezer`
Access: read-only (the marketing site, the public catalog pages and the account forms are fully public; everything behind account.deezer.com is an authenticated boundary never reached; Try-for-free, Sign-up, Mix, Play, queue and volume actions were measured, never followed; the login and signup forms were never submitted)
- every post-login surface (library, Flow, playlists, downloads, settings, billing) lives behind account.deezer.com - an authenticated boundary never reached
- the login and signup forms were measured as forms, never filled or submitted; validation, error and success states are absent rather than measured

## [Delphi](../systems/delphi) — `delphi`
Access: read-only (the home page, /discover/<topic> galleries, /search/<question> results, /<expert> profiles and /<expert>/chat are fully public signed out; creating a clone, saving perspectives and every post-login surface is an authenticated boundary never reached; Sign In, Continue with Google/Email, Share, Save, Expand, Personalize, suggested-question chips, the microphone and the chat send were measured, never followed or submitted)
- creating a clone, saving perspectives, personalising results and every post-login surface need an account - an authenticated boundary never reached
- the Sign-In/onboarding dialogs were measured as dialogs; Continue with Google/Email were never pressed, so the auth flow past the dialog is unmeasured

## [Descript](../systems/descript) — `descript`
Access: read-only (the marketing site is fully public; the product lives behind web.descript.com - its sign-in card was captured as a boundary, measured and never submitted; Sign in, Sign up, Get started and every plan CTA were measured as destinations, never followed)
- the product lives behind web.descript.com - the sign-in card's buttons and email field were measured and the field typed/cleared, never submitted; no authenticated page was reached
- Sign in, Sign up, Get started, Try free, Request a demo and every plan CTA were measured as outbound/form destinations, never followed

## [Designmodo](../systems/designmodo) — `designmodo`
Access: read-only (the marketing site, /pricing, /email-templates, /postcards, /slides, the /postcards/app/login form and the signed-out app shell behind the Welcome-back modal are public; the builder canvas and every post-login surface need an account - the modal was dismissed locally with Escape and every auth action measured, never submitted)
- the Postcards builder canvas, saving work and every post-login surface need an account - never reached
- the Welcome-back modal's actions (Continue with Google, email field, Login, Create Account) were measured, never submitted
- the sign-in form's fields were typed into and cleared and Login was never pressed; validation, error and success states are absent rather than measured

## [Visual (designstripe)](../systems/designstripe) — `designstripe`
Access: read-only (the home page, /assets library and /assets/<kind>/<set> galleries, /tools, /about, /contact and /blog articles are fully public signed out; the design agents, account asset downloads and every post-waitlist surface are an authenticated boundary never reached; the WAITLIST buttons, nav links, category tiles, tool cards and article links were measured, never followed or submitted)
- the design agents, account asset downloads and every post-waitlist surface need an account - an authenticated boundary never reached

## [Digg](../systems/digg) — `digg`
Access: read-only (the home feed, category feeds, story pages, /u/<source> profiles, /login, /sign-up and /privacy are fully public signed out; voting, commenting, submitting, following and settings are an authenticated boundary never reached; the vote pills, comment and source links were measured, never followed or pressed, and the Clerk fields were focused/filled, never submitted)
- voting, commenting, submitting, following sources and every account surface need an account - an authenticated boundary never reached; the digg-it pills and comment links gate on sign-in and were never pressed
- the Clerk auth fields were focused and filled at /login and /sign-up, never submitted - no validation, error, loading or success state exists in this capture

## [Discord](../systems/discord) — `discord`
Access: read-only (the marketing pages, /servers discovery + categories, /servers/<slug> details, /login and /register are public signed out; the whole client - /channels/*, joining servers, invites, messages, settings - is an authenticated boundary never reached; every button and field was measured, never submitted or followed)
- the whole Discord client needs an account - /channels/* redirects to /login; joining a server, accepting an invite, messages and settings are an authenticated boundary never reached
- the Join/Share/Nitro/submit controls were measured (hover/focus/pressed), never pressed - no account action was executed
- auth fields were focused and filled then cleared, never submitted - no validation, error, loading or success state exists in this capture
- /invite/<code> painted a dark frame but no invite card signed out in this pass - recorded as a boundary

## [District](../systems/district) — `district`
Access: signed out (booking and payment gate on the Zomato account and were never reached)
- booking, payment, sign-in and every account surface need the Zomato account - the Book/Proceed CTAs and date pills were measured at every paintable state, never pressed

## [DJI](../systems/dji) — `dji`
Access: read-only (the /sg home, /camera-drones, /handheld, /mavic-4-pro, /support, /company, /where-to-buy/* and the /sg/mobile site are fully public signed out; the store (store.dji.com), Login/Register and checkout gate on a DJI account - an authenticated boundary never reached; the Store, Buy Now, Watch Video and search controls were measured at every paintable state, never followed or pressed)
- the store (store.dji.com), Login/Register (member-service redirects) and checkout gate on a DJI account - an authenticated boundary never reached; the Store and Buy Now CTAs were measured, never followed

## [Dock](../systems/dock) — `dock`
Access: signed out (every captured surface is public; the Dock workspace sits behind auth.dock.us and was never reached; the HubSpot demo form and the auth cards were measured, never filled or submitted)
- the signed-in workspace entirely: rooms, deal portals, content library, learning paths, settings and billing live behind auth.dock.us and were never reached
- the login/signup cards and the HubSpot demo form were measured as surfaces, never filled or submitted; their Continue/submit actions were never pressed

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

## [Dona](../systems/dona) — `dona`
Access: signed out (every captured surface is public: /, /about, /privacy-policy, /terms-of-service; the product on app.dona.ai sits behind sign-in and was never reached; the newsletter was never submitted and the cookie banner never answered)
- app.dona.ai entirely: the to-do product — lists, the advertised light/dark/black UI themes, sync, accounts — lives behind sign-in and was never reached; Login and Try for free open that host and were never followed
- external links (twitter.com/getdona, the Discord invite) were never followed

## [DoorDash](../systems/doordash) — `doordash`
Access: signed out (every captured surface is public; the address gate, sign-in, ordering, cart, checkout, DashPass and merchant/Dasher onboarding were never crossed; catalog bodies that hydrate from live APIs render as the product's own loading spinner)
- the signed-in product entirely: the address gate, sign-in, ordering, cart, checkout, DashPass purchase, merchant and Dasher onboarding were never crossed; the identity.doordash.com OAuth anchors were measured, never followed
- the address-search field was focused once for measurement, never filled or submitted; the cookie banner and dormant Turnstile nodes were hidden and never answered
- icons: no standalone SVG set lifted this pass; icon.png is the site's published favicon (32 px source, the largest the site ships, upscaled to 128 px)

## [Dopper](../systems/dopper) — `dopper`
Access: signed out (every captured surface is public; the customer account, checkout and filled cart behind the login and cart cards were never reached; no form was submitted, no account created, and the Cookiebot dialog was hidden, never answered). English locale, EUR prices
- the signed-in product entirely: customer account, order history, checkout flow and the filled cart sit behind the login/cart cards and were never reached; Add to cart was measured, never really clicked
- the login fields were focused, typed into and cleared - Sign in was never pressed and no form was submitted
- the 'For Businesses' B2B portal, Digital Product Passport, Tap/Map/community apps and non-English locales are linked surfaces that were not captured

## [Doppler](../systems/doppler) — `doppler`
Access: signed out (every captured surface is public; the product — the secrets dashboard, projects, configs, service tokens, logs and billing — sits behind sign-in on dashboard.doppler.com and was never reached; the demo request form was never submitted)
- the signed-in product entirely: the secrets dashboard, projects, configs, service tokens, logs, integrations management and billing live behind sign-in on dashboard.doppler.com and were never reached; Start for Free and Sign In point off-site and were measured, never followed

## [Dribbble](../systems/dribbble) — `dribbble`
Access: signed out (every captured surface is public; posting shots, following, hiring flows, inboxes and dashboards sit behind /session/new and were never reached; the signed-out feed itself stops at one shot card plus a sign-up wall, which is where the package stops; no form was submitted and no account created)
- the signed-in product entirely: posting, following, hiring flows, inboxes and dashboards sit behind sign-in and were never reached
- /session/new and /signups/new captured as surfaces; the email field typed sample text and deleted it — nothing was submitted and no OAuth flow started; the Continue-with-Google GSI button is third-party-rendered and was hidden like every overlay, so it is a documented gap

## [Douze](../systems/drinkdouze) — `drinkdouze`
Access: signed out (every captured surface is public; checkout, a filled cart, /account past the login/register forms and subscription management were never reached — nothing was added to the cart, no form was ever submitted, and no consent or newsletter overlay was ever answered)
- checkout, a filled cart, payment, /account past the login and register forms, and subscription management were never reached — nothing was added to the cart and no submit was ever pressed
- the subscription (Appstle) purchase-option radios did not render on load signed out — they appear in the variant screenshot after a pack-size is picked, never toggled

## [Dropbox](../systems/dropbox) — `dropbox`
Access: signed out (every captured surface is public; the file dashboard, Paper/Dash/Replay/Sign workspaces, account and billing sit behind the auth cards and were never reached; dash.dropbox.com and the sign-in-embed hosts were never opened; the login/register fields were focused and sample-filled then deleted, never submitted)
- the signed-in product entirely: the file dashboard, Paper/Dash/Replay/Sign workspaces, account, billing and checkout sit behind the auth cards and were never reached
- /login and /register captured as surfaces: the email fields were focused and given sample text that was deleted; Continue, the SSO buttons and every Try-for-free/Buy-now/Get-started action were measured, never followed
- the auth cards run an older susi sheet (lucida grande stack, 4px radii) distinct from the DIG marketing system

## [Dub](../systems/dub) — `dub`
Access: signed out (every captured surface is public; the link-management workspace, analytics, domains, settings and billing sit behind /login on app.dub.co and were never reached; the login, register and contact-sales forms were measured, never filled past a deleted sample, never submitted; the docs search palette and Mintlify AI assistant were never opened)
- the signed-in workspace entirely: link management, analytics, domains, tags, webhooks, integrations, settings and billing live behind app.dub.co/login and were never reached
- /login and /register were captured as surfaces, never filled past a deleted sample or submitted
- the demo-panel under the home hero is a published dashboard mock, not the app
- hero-badge and sales-submit focus-visible recorded failed states (a real keyboard focus could not be held)

## [Editor X (Wix Studio)](../systems/editorx) — `editorx`
Access: signed out (every captured surface is public; editorx.com 301s to wix.com/studio for every path except /pricing, which served its Premium-plans error pane at capture time; the Studio editor, workspaces and checkout sit behind Log In / Start Creating and were never reached; no form was submitted and no account created)
- the signed-in product entirely: the Studio editor, workspaces, dashboards, signup and checkout sit behind Log In / Start Creating and were never reached
- the only presses were local UI toggles: the Product dropdown, the FAQ expander, the mobile menu; no form was submitted and no action followed

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

## [ElevenLabs](../systems/elevenlabs) — `elevenlabs`
Access: signed out (every captured surface is public; the Studio, agents platform, voice library, API keys, billing and account sit behind the /app/sign-in and /app/sign-up cards and were never reached; no form was submitted, no account created and the Cookiebot layer was hidden, never answered). The home TTS playground's Play was pressed once, a public affordance that generates without an account
- the signed-in product entirely: the Studio, agents platform, voice library, API keys, billing and account sit behind the auth card; /app redirects to /app/sign-in and was never entered
- /app/sign-in and /app/sign-up captured as surfaces; the email/password fields were focused and sample-filled then deleted, leaving the submits disabled and never pressed; no form was submitted
- Sign up, Subscribe, Get API key, Contact Sales and the OAuth providers (Google / Apple / SSO) were measured or screenshotted, never followed
- the home TTS playground's Play was pressed once and generated without an account; the voice-orb and sample-card play buttons were measured but not played, and the voice-chat launcher was never opened

## [ElevenMusic](../systems/elevenmusic) — `elevenmusic`
Access: signed out (every captured surface is public: /, /explore, /charts, /tracks, /genres, /genres/electronic, /sounds, /tools, an artist profile, a playlist, /blog, /pricing, /login, /sign-in; Create/Composer/Library/Chat/publish, Likes, Remixes, Shares and search itself sit behind sign-in and were never entered or submitted)
- the signed-in product entirely: Create, Composer, Chat, Library, artist-page publishing, account settings and billing need an account and were never reached; /login and /sign-in were measured as forms and never submitted
- search is gated: the rail's Search button opens the log-in dialog (captured as evidence), so a real search surface is uncaptured
- every Create button, prompt submit and Attach control was measured, never pressed — a prompt is a generation request
- the Get-Pro and Start-free CTAs were measured, never followed past the public card; checkout is uncaptured

## [ElevenReader](../systems/elevenreader) — `elevenreader`
Access: signed out (every captured surface is public: the marketing pages, one public audiobook page and the /reader sign-in/sign-up cards; the reader app - library, upload, player, settings, billing - sits behind /reader/sign-in and was never reached; the email forms were revealed by their own toggles and never submitted)
- the reader app entirely: library, upload, the reader/player, settings and billing live behind /reader/sign-in and were never reached; /reader/sign-in and /reader/sign-up were captured as boundary cards
- the OAuth buttons were never pressed; the email credential forms were revealed by their own 'with email' toggles (local UI, nothing sent), fields were focused and sample text was typed and deleted - no form was ever submitted, so error/success states are uncaptured

## [Matter](../systems/matter) — `matter`
Access: signed out (every captured surface is public: the marketing pages, one published article, the docs home and the web reader sign-in card; the reader app sits behind sign-in and was never reached; the email field was focused and never filled; Subscribe was never pressed, so that form was not submitted)
- the reader app sits behind sign-in at web.getmatter.com and was never reached; the sign-in card was captured as the boundary
- Continue with Google and Continue with Apple were never pressed; the email field was focused and never filled; the arrow was never pressed, so the form was not submitted
- the publication Subscribe control was measured and never pressed, so that form was not submitted
- Get Matter links to an App Store checkout that was never followed

## [Endel](../systems/endel) — `endel`
Access: signed out (every captured surface is public: the endel.io marketing pages plus app.endel.io's explore, player and sign-in card; the account, library, premium unlock/checkout and any form submit were never crossed; the Set Timer sheet, More flyout and mobile menu were opened by their own toggles and closed again)
- the signed-in app entirely: account, library, sync, settings, purchase and the premium unlock/checkout the timer sheet's Unlock row starts were never reached; the FREEMIUM chip, scenario pills, Unlock, Continue and the OAuth buttons were measured, never pressed for real
- no form was submitted and no account created: the footer newsletter field and the sign-in card's email field were measured, never sent; Try Today, Subscribe, Continue, Unlock and every outbound link were never followed
- the home page's mid-page newsletter row (input-email, btn-subscribe) was not on the page at capture time; the footer's own field was painted instead

## [Endless](../systems/endless) — `endless`
Access: signed out (every captured surface is public; the workspace behind sign-up on s.endless.app, auth on clerk.endless.app, was never reached; no form was submitted and no tool was run)
- the signed-in workspace entirely: chat, canvas, projects, files, MCP connections, billing and onboarding live behind s.endless.app (auth on clerk.endless.app) and were never reached
- no form was ever submitted and no tool was ever run: the contact Send button and every Generate action were measured, not pressed, so success, error, progress and result-gallery states are uncaptured
- checkout, plan purchase and localized routes were never reached

## [Endless Tools](../systems/endlesstools) — `endlesstools`
Access: signed out (every captured surface is public: / on endlesstools.io plus /login, /legal/privacy_policy and /legal/terms_of_use on app.endlesstools.io; the product editor behind sign-in was never reached; no form was submitted and the only presses were local UI toggles)
- the editor entirely: the canvas, tools, panels, library and AI features live behind sign-in on app.endlesstools.io and were never reached; Start for free, the plan CTAs and Create team open signup and were never followed
- the login card's two forms (OTP send-code and password) were measured and locally switched; neither was submitted, so the code entry, errors and signed-in redirect are uncaptured
- the newsletter form was measured and its consent checkbox toggled for the capture; it was never submitted, so its success and any error state are uncaptured

## [Enode](../systems/enode) — `enode`
Access: read-only (the marketing site and the platform login page are fully public signed out; everything behind platform.enode.com - the dashboard, docs portal, API surfaces - is an authenticated boundary never reached; the contact and login forms were measured and typed into then cleared, never submitted; every CTA and link was measured, never followed; the dormant Cookiebot layer shows no banner and was never answered)
- every post-login platform surface (dashboard, asset management, API keys) and docs.enode.com lives behind an account - an authenticated boundary never reached
- the /contact, /contact/partnerships and platform login forms were measured at rest and typed into then cleared, never submitted - validation, error, loading and success states are absent rather than measured

## [Epic Games Store](../systems/epicgames) — `epicgames`
Access: read-only (every captured surface is public: the storefront, the sign-in dialog, the support centre and the marketing home); the sign-in form and both search fields were measured, never submitted; Get, Add to Cart, Wishlist, Download, sort options and filter checkboxes were measured, never activated
- every post-login surface (library, account, billing, cart, checkout) is an authenticated boundary never reached
- the sign-in form was measured default/focused/filled, never submitted; validation, error and success states are absent rather than measured

## [Epidemic Sound](../systems/epidemicsound) — `epidemicsound`
Access: read-only (the marketing site, the public catalog, SFX and artist pages and the account forms are fully public; everything behind login.epidemicsound.com is an authenticated boundary never reached; Play, Download, Subscribe, Create-free-account and Log-in actions were measured, never followed; the login and signup forms were never submitted)
- every post-login surface (library, playlists, downloads, billing, account settings) lives behind login.epidemicsound.com - an authenticated boundary never reached
- the login and signup forms were measured at rest, never filled with real credentials or submitted; validation, error and success states are absent rather than measured

## [Equals](../systems/equals) — `equals`
Access: read-only (the marketing site, the go.equals.com sign-in card and the docs are fully public; the spreadsheet workspace and every post-login surface are an authenticated boundary never reached - app.equals.com did not answer; the sign-in and demo e-mail fields were focused and filled for measurement, then cleared, never submitted; Get-a-demo, plan and trial actions were measured, never followed)
- the authenticated product - workbook, dashboards, datasources, settings and every post-login surface - was never reached; app.equals.com did not answer during the capture
- the sign-in form and the demo e-mail captures were measured as fields, never submitted; validation, error and success states are absent rather than measured
- the mobile capture of /use-cases/arr-dashboard/ hit a security challenge; component readings fall back to the desktop measurement

## [Esquire](../systems/esquire) — `esquire`
Access: signed out (every surface captured is public; account.esquire.com sign-in and the shop.esquire.com subscription checkout are off-domain boundaries that were measured, never followed; the newsletter and search fields were typed into and cleared, never submitted)
- every signed-in surface (bookmarks, comment counts, the premium archive) lives behind Sign In on account.esquire.com - an authenticated boundary never reached
- the Join/Subscribe buttons lead to shop.esquire.com checkout - measured, never followed; purchase, payment and confirmation states are absent rather than measured

## [Exa](../systems/exa) — `exa`
Access: read-only (every captured surface is public and signed out; the dashboard, API keys and playground behind auth.exa.ai were never reached - login routes rate-limited or redirected during reconnaissance; the login and e-mail fields were focused and filled then cleared, never submitted; the home demo's Run-preview arrow, Get-started and Sign-up actions were measured, never pressed)
- every post-login surface (the dashboard, API keys, the playground, billing) sits behind auth.exa.ai - an authenticated boundary never reached; dashboard.exa.ai/login and /playground/search rate-limited (HTTP 429) during reconnaissance
- the sign-in and e-mail fields were focused and filled with test text, then cleared - never submitted; validation, error and success states are absent rather than measured
- the marketing site and sign-in card paint light only - the dark set covers the docs alone

## [Exactly.ai](../systems/exactly) — `exactly`
Access: read-only (the marketing site, pricing, showcase, case studies, industries, help center and book-a-demo are fully public; everything on threads.exactly.ai is an authenticated boundary behind a Cloudflare check never bypassed; Log in, Start for free and Book a demo were measured, never followed; the help search was typed and cleared, never submitted; the scheduler was measured at rest)
- the product itself - studio, model training, the image generator, credits, billing and every account surface - lives on threads.exactly.ai behind a Cloudflare check that was never bypassed
- the Log in, Start-for-free and Book-a-demo links were measured, never followed; the scheduler was measured at rest - no day, time or contact detail was ever picked or typed

## [Excalidraw](../systems/excalidraw) — `excalidraw`
Access: read-only (the whole editor is public signed out; nothing was drawn, opened, saved, shared, exported or generated; Open, Save, Export actions, Live collaboration, Share, the AI tools, Reset the canvas and every Sign up were measured, never pressed; Excalidraw+ needs an account and was never reached)
- Excalidraw+ (saved workspaces, cloud library, collaboration management, billing) needs an account and was never reached; no signup or login path was followed

## [Expedia](../systems/expedia) — `expedia`
Access: signed out (every captured surface is public); expedia.com answers automation with a 429 "Bot or Not?" challenge, so the DOM evidence is a Wayback snapshot served locally and painted with live travel-assets.com CSS/fonts
- anything behind sign-in: trips, account, member pricing, checkout, booking, saved items
- submitted states: search was never submitted; sort/filters never applied; only screenshot evidence for the opened sort menu

## [Explore](../systems/explore) — `explore`
Access: read-only (every public surface signed out; the site itself is offline - the product closed 2023-04-19 and the domain later lapsed - so all pages were replayed from a local Internet Archive mirror of the 2023-02-23 build, with the closure shell from the 2023-06-08 snapshot; auth forms were measured and typed into then cleared, never submitted; no backend was ever reached; member names and works on the SSR profiles are public archive records reproduced as captured)
- every signed-in member surface (network feed, composer, notifications, saved, subscriptions, settings) plus the dark member-portfolio theme lives behind accounts that closed with the product - an authenticated boundary never reached
- SPA routes whose API records were never archived (/user/*, /post/*) render signed-out shells; member profiles survive only in the three archived SSR HTML pages
- the login/register/forgot-password fields were measured at rest and typed into then cleared, never submitted - validation, error, loading and success states are absent rather than measured

## [Fable](../systems/fable) — `fable`
Access: read-only (the marketing pages, /clubs, /books, genre/club/book detail pages, /discover, /signin, /signup, /support, /blog and /community-guidelines are fully public signed out; joined clubs, discussions, the reader, lists, streaks, cart and checkout need an account - an authenticated boundary never reached; the sign-in form and SSO buttons, Join, Want to read, store badges and every CTA were measured, never submitted, pressed or followed; the Osano consent layer was hidden, never answered)
- every post-login surface (joined clubs, discussion threads, the book reader, lists, streaks and stats) needs an account - an authenticated boundary never reached
- cart, checkout and ebook purchase flows were never opened; App Store / Google Play badges and 'Get the app' CTAs were measured, never followed
- the sign-in and sign-up forms were measured at rest and typed into then cleared, never submitted - validation, error, loading and success states are absent rather than measured; 'Continue with Google/Apple' was never pressed
- 'Join the club', 'Want to read', the spoiler toggle, 'Read more' and the FAQ accordion are local UI - the disclosure toggles were opened for capture and nothing was submitted or joined

## [Factory](../systems/factory) — `factory`
Access: read-only (factory.com, docs.factory.com and the auth.factory.ai sign-in card are fully public signed out; everything behind app.factory.ai - the Droid console, missions and settings - is an authenticated boundary never reached; the /contact HubSpot form and the sign-in card were measured and typed into then cleared, never submitted; every CTA and link was measured, never followed; overlays were hidden, never answered)
- every post-login app surface (the Droid console, missions, settings) sits behind app.factory.ai - an authenticated boundary never reached; the auth.factory.ai sign-in card is a different app that does not share the marketing token layer
- the /contact HubSpot form and the sign-in card were measured at rest and typed into then cleared, never submitted - validation, error, loading and success states are absent rather than measured
- factory.com/changelog and docs.factory.com/changelog answer a Vercel-login 404 shape; the working changelog at docs.factory.com/docs/changelog/release-notes was captured instead

## [Faire](../systems/faire) — `faire`
Access: signed out (every captured surface is public; search results, product detail, cart, checkout, account and the brand portal are behind the sign-up/sign-in dialogs - a documented authenticated boundary never crossed)
- every post-auth surface - search results, product detail, cart, checkout, account and the brand portal - sits behind the sign-up/sign-in dialogs; every product tile links ?signUp=product, an authenticated boundary never crossed
- the /apply stepper's steps past 1 need a submitted first step; step 1 was filled and cleared, never sent
- the observed sign-up dialog mounts no Apple SSO button; signup-apple is recorded missing

## [fal.ai](../systems/fal) — `fal`
Access: read-only (the marketing pages, the explore catalog, the model and API pages, the docs and the login card are fully public; everything past login - dashboard, API keys, billing, deployments, sandbox, inference - is an authenticated boundary never reached; OAuth, Sign-in-to-run, Open-in-Sandbox, Download, Contact-Sales and Get-Started were measured, never followed; the prompt field was filled and cleared without running a model; the consent card was hidden, never answered)
- every post-login surface (dashboard, API keys, billing, deployments) lives behind fal's account - an authenticated boundary never reached
- inference was never run: the prompt field was filled and cleared, Sign-in-to-run links to login signed out, Open-in-Sandbox and Download were measured, never followed
- the OAuth buttons and Use-SSO were measured at rest, never followed; validation, error and success states are absent rather than measured

## [Family](../systems/family) — `family`
Access: read-only (family.co marketing pages, /docs, /support and the app.family.co login are fully public signed out; the signed-in Aave Account product and the iOS wallet are authenticated/native boundaries never reached; Log In, Get Started, Download on iOS and every Watch link were measured, never followed, and the login field and support search were typed into and cleared, never submitted)
- the signed-in Aave Account product and every post-login surface need an account - an authenticated boundary never reached
- Log In, Get Started, Download on iOS and every Watch link were measured, never followed; the login field and support search were typed into and cleared, never submitted

## [FARFETCH](../systems/farfetch) — `farfetch`
Access: signed out (every captured surface is public); www.farfetch.com answers automation with Akamai 403 and the farfetch-contents.com CDNs with 429, so the DOM evidence is Wayback SSR snapshots served locally and painted by Farfetch's own archived CSS, fonts and images with scripts stripped
- anything behind sign-in: account, wishlist contents, bag, checkout, order tracking, FARFETCH Access loyalty, private client
- submitted states: search, newsletter and filters were typed/measured but never submitted

## [FeedHive](../systems/feedhive) — `feedhive`
Access: signed out (every surface captured is public; the app.feedhive.com sign-in and sign-up cards are the only app surfaces a signed-out visitor sees - measured as forms, typed into then cleared, never submitted; everything post-login is an authenticated boundary never reached; docs.feedhive.com is a separate site; every CTA and link was measured, never followed; the dormant vanilla-cookieconsent layer mounts empty and was never answered)
- every post-login surface (composer, scheduling calendar, AI generation, analytics, account settings) lives behind app.feedhive.com - an authenticated boundary never reached
- the sign-in, sign-up and bio-generator forms were measured at rest and typed into then cleared, never submitted - validation, error, loading and success states are absent rather than measured; the bio Generate button's desaturated #b9c0f5 is its resting style, not a measured disabled state
- the app.feedhive.com values are a different design system (Chakra UI) kept as component.login.* literals, never the marketing roles

## [Fibery](../systems/fibery) — `fibery`
Access: read-only (the marketing site, fibery.io/sign-up and fibery.io/login/ are fully public signed out; everything past login - workspaces, views, the app's dark/system theme - is an authenticated boundary never reached; the sign-up prompt and login e-mail field were typed into then cleared, never submitted; the OAuth POST forms were never pressed; the wizard never advanced; every link and CTA was measured, never followed; the consent layer and Intercom widget were hidden, never answered)
- every post-login app surface - workspaces, entity views, whiteboards, automations, AI, admin - lives behind an account, an authenticated boundary never reached
- the app's dark/system theme (advertised on the login page) is behind sign-in and was not captured; the token file deliberately ships core + light only
- the sign-up wizard was never advanced past step one - 'Create workspace' and 'Start without AI' were never pressed - so steps 2+ and workspace creation are uncaptured
- the sign-up prompt and login e-mail field were typed into then cleared and never submitted, and the OAuth POST forms were never pressed - validation, error, loading and success states are absent rather than measured
- 'Book a demo' links to a scheduler that was never opened; 'Workspace SSO' was never followed

## [Figma](../systems/figma) — `figma`
Access: signed out (every captured surface is public; the editor and every post-login surface - files, boards, Dev Mode in a file, Make projects, community profiles and publish flows, admin - is an authenticated boundary never reached; the /login, /signup, /contact and /make forms were measured and typed into then cleared, never submitted; every CTA, nav item and community card was measured, never followed; the consent layer was hidden, never answered; Cloudflare challenged the automation on /dev-mode/ and /customers/ in the first pass and retries in fresh sessions succeeded - no challenge was answered by hand; the dark theme is declared only - a complete :root[data-theme="dark"] token layer the stylesheets ship but no public page painted while captured)
- the editor and every post-login surface (files, the canvas, Dev Mode in a file, Make projects, community profiles and publish flows, account, admin) sits behind an account - an authenticated boundary never reached; /login and /signup were measured as forms, never submitted, and Continue with Google / Use single sign-on were never followed
- submitted states: the /contact sales form, /make prompt, blog newsletter field, community search and the login/signup fields were typed into then cleared, never sent - validation, error, loading and success states are absent rather than measured

## [Fingerprint](../systems/fingerprint) — `fingerprint`
Access: signed out (every captured surface is public; the dashboard and every post-login surface - API keys, the events explorer, playground, billing - is an authenticated boundary never reached; the /login, /signup, contact-sales, newsletter and demo fields were measured and typed into then cleared, never submitted; every CTA, SSO button, nav item and link was measured, never followed; the 'Open the chat' launcher was never opened; the docs dark theme is the Mintlify site's own preference, captured as screenshots, while the marketing site ships only a .dark-scoped syntax redeclaration and resolved identically under an emulated dark probe; /demo and the IdentifySection panels paint the capture machine's real visitor ID, IP and geolocation, masked in committed images via tools/redact-rules/fingerprint.json)
- the dashboard and every post-login surface (API keys, events explorer, playground, billing, admin) sits behind an account - an authenticated boundary never reached; dashboard /login and /signup were measured as forms, never submitted, and Continue with Google/GitHub/Microsoft were never followed
- submitted states: the /contact-sales form, footer and blog newsletter fields, the demo fake-checkout field and the auth cards were typed into then cleared, never sent - validation, error, loading and success states are absent rather than measured

## [Fiverr](../systems/fiverr) — `fiverr`
Access: signed out (every captured surface is public; the buyer/seller account, orders, inbox, checkout and every post-login surface is an authenticated boundary never reached; the hero search, join and login fields were measured and typed into then cleared, never submitted)
- the buyer/seller account, orders, inbox, checkout and every post-login surface was never reached
- the gig card's Continue was measured, never pressed — the order/checkout flow it leads to is uncaptured
- Contact me was measured, never pressed — the message flow it fronts needs an account
- the join and login forms were typed into then cleared, never submitted; Continue-with-* was never pressed

## [Flask](../systems/flask) — `flask`
Access: signed out (every captured surface is public; the product workspace behind /home and every post-login surface is an authenticated boundary never reached; /login was measured at rest, the Google and Email buttons never followed; the pricing billing switch was toggled for the monthly shot then toggled back; the FAQ accordions and the home demo's Version chip were opened locally; every link and CTA was measured, never followed; the public site paints dark only and no theme switcher or light theme was observed)
- the product workspace behind /home and every post-login surface sits behind an account - an authenticated boundary never reached; Sign Up and Open Flask link to /home and were measured, never followed; /login was captured at rest, its Google and Email buttons never followed
- submitted states: the login form was never submitted - validation, error, loading and success states are absent rather than measured

## [FlowMapp](../systems/flowmapp) — `flowmapp`
Access: read-only (the www.flowmapp.com marketing pages, the signed-out app.flowmapp.com/signin, /signup and /restore forms, and the public /share/projects/215285 sitemap and user-flow demo viewers are fully public; every post-login app surface - the sitemap/user-flow editors, wireframes, content, estimation, dashboards, billing - is an authenticated boundary never reached; the auth and contact forms were measured and typed into then cleared, never submitted; every link and CTA was measured, never followed; no consent banner was observed on either host)
- every post-login app surface (the sitemap/user-flow editors, wireframes, content planner, estimation and invoicing, project dashboard, team settings, billing) needs an account - an authenticated boundary never reached
- the /signin, /signup, /restore and /contact-us forms were measured and typed into then cleared, never submitted - validation, error, loading and success states are absent rather than measured
- the mobile 390px pass on app.flowmapp.com/signin hit an anti-bot challenge; the desktop pass captured it - recorded as a gap, not bypassed

## [FlutterFlow](../systems/flutterflow) — `flutterflow`
Access: signed out (every surface captured is public; the app sits at app.flutterflow.io behind login)
- app.flutterflow.io and everything behind Sign in / Start building / Open Studio was never opened: the dashboard, editor canvas, AI generation flow, billing and account surfaces are signed-in and out of scope
- the prompt composer was measured, focused and typed in (then cleared) but never submitted, so the generation flow it starts is missing
- the enterprise Talk-to-sales form and the Studio application form were never submitted, so their success and painted error states are missing (the error slot is recorded as declared DOM, not painted)
- plan CTAs lead to a signed-in checkout and were not followed

## [Foodnoms](../systems/foodnoms) — `foodnoms`
Access: read-only (the marketing site, pricing, help center, news, press, articles, comparison pages and legal are fully public; the product itself is an iOS/macOS app sold through the App Store - there is no web sign-in; every Download/Get-the-App link, press-kit zip and mailto was measured, never followed; the help search and newsletter field were typed into then cleared, never submitted; /open/settings/* is a static deep-link interstitial)
- the product itself - food logging, AI scanning, widgets, the community database and subscription purchase - is an iOS/macOS app behind the App Store download, which was never installed or opened; /download is a JS redirect to apps.apple.com that was never followed
- the help search modal was opened and typed into, but result rows were never clicked; the newsletter field was typed into then cleared, never submitted

## [For Hers](../systems/forhers) — `forhers`
Access: signed out (every captured route is public marketing, catalogue, editorial or tool surface; Log in, the slide menu, the quiz/intake flow, consultations, prescriptions, orders and checkout are gated destinations measured at rest only - the BMI and lead-capture fields were clicked into and typed-then-cleared, nothing was submitted, and www.forhers.com answers this network with a Cloudflare managed challenge so the evidence is Wayback SSR, never the live origin)
- scripts are stripped from the archived SSR, so hydration-owned surfaces never open: the slide menu, the login menu, accordion expansion, carousel scrolling, the quiz/intake flow and Read more - captured closed, recorded as gaps
- sign-in, the member account, consultation/intake, prescriptions, orders and checkout were never opened; forms were measured empty, success/error/post-submit states uncaptured by design

## [Fourmula](../systems/fourmula) — `fourmula`
Access: signed out (every surface captured is public; app.fourmula.ai /start, /auth and /project/create-pdp are the only app surfaces a signed-out visitor sees - measured as forms, typed into then cleared, never submitted; uploads, the Shopify connection, generation and every post-login surface need an account and were never run; consent was never answered; every CTA and link was measured, never followed)
- every post-login surface (dashboard, asset generation, results, account settings) lives behind app.fourmula.ai's auth wall - an authenticated boundary never reached
- the auth fields, PDP uploads, Shopify Check connection and Start generation were measured at rest and typed into then cleared, never submitted - validation, error, loading and success states are absent rather than measured; the Start generation pill's dim accent/15% fill is its resting style, not a measured disabled state

## [Fourthwall](../systems/fourthwall) — `fourthwall`
Access: signed out (every captured surface is public: the marketing pages, the product catalogue and one product page, the docs and help sites in light and in their own dark themes, and the /get-started auth shell; every post-login surface - the shop dashboard, product designer, checkout/orders, promotions, account - is an authenticated boundary never reached; the auth choices (Google/Apple/email) and the PDP 'Sign in to design' were measured at rest, never pressed, no OAuth flow started; searches and fields were typed into then cleared, never submitted; nothing was bought; the Osano consent layer was hidden, never answered)
- every post-login surface (the shop dashboard, the product designer, checkout and order flow, promotions, account settings) sits behind an account - an authenticated boundary never reached
- the auth choices (Google/Apple/email provider rows) and the PDP 'Sign in to design' were measured at rest and never pressed - no OAuth flow was started and no form was submitted
- nothing was purchased; the PDP size guide and product-finder quiz are local toggles that were opened, never a checkout
- the nav 'Start now' modal navigates to /get-started on this build instead of opening; the auth shell was captured instead

## [Frame.io](../systems/frame) — `frame`
Access: signed out (every captured surface is public; the app and every post-login surface - projects, the review player, Camera to Cloud uploads, Drive and Transfer workspaces, admin, billing - is an authenticated boundary never reached; the accounts.frame.io/welcome sign-in and the /contact/form fields were measured and typed into then cleared, never submitted; every CTA, nav item, menu item and card was measured, never followed; no consent layer appeared for the en-US signed-out visitor and the cookie-preferences control was never pressed; the site ships no theme switch - every frame.io page paints the one dark theme, and accounts.frame.io/welcome is the lone light surface on a different stack)
- the app and every post-login surface (projects, the review-and-approval player, Camera to Cloud uploads, Drive and Transfer workspaces, account, admin, billing) sits behind an account - an authenticated boundary never reached; accounts.frame.io/welcome was measured as a form, never submitted
- submitted states: the /contact/form fields and the sign-in e-mail were typed into then cleared, never sent - validation, error, loading and success states are absent rather than measured

## [Framer](../systems/framer) — `framer`
Access: signed out (every captured surface is public; the dashboard, editor, CMS, publishing, workspaces and every post-login surface are an authenticated boundary never reached; /login was measured as a form, never submitted - /signup redirects to it - and Continue with Google was never followed; the pricing 'Yearly billing' switch, credits selects and every CTA/link were measured, never switched or followed; the 'We use cookies' consent card was hidden in the DOM, never answered; the public marketing stack and the community/gallery stack paint dark while /login is a separate light shell)
- the dashboard, editor, CMS, publishing, workspaces and every post-login surface sit behind an account - an authenticated boundary never reached; /login was captured at rest, its Google button and Continue submit never followed, and /signup redirects to the same shell
- submitted states: the login work-email field was never submitted and search inputs were never sent - validation, error, loading and success states are absent rather than measured
- the community/marketplace stack's own stylesheet layer was not separately harvested - its values are measured component tokens, not declared variables; the mkt-logo crop and a full-size nav-panel measurement are recorded missing/weak rather than inferred (the measured login-panel is the full 1440px shell, not a bounded card)
- prefers-reduced-motion is only partially honoured on the homepage and ignored on pricing, the gallery and login - recorded per page in raw/motion.json
- no light marketing theme or theme switcher was observed; the only light surface is the /login auth shell

## [Fresha](../systems/fresha) — `fresha`
Access: read-only (every captured surface is public: the consumer marketplace, the /user-flow and /auth sign-in shells, the partners.fresha.com professional sign-in, a public venue profile, the booking wizard at the service-selection boundary, /pricing and /for-business marketing, the legacy /lp category and browse pages, /help-center, /careers, /blog, /download-app and /cookies; every post-login surface - the customer account and the whole partner app (calendar, sales, clients, marketing) - is an authenticated boundary never reached; the sign-in fields were measured and typed into then cleared, never submitted; the booking Continue button was never pressed and no payment step was reached; no search, booking, OAuth, SSO or consent action was performed)
- every post-login surface (the customer account and the whole partner app: calendar, sales, clients, marketing, billing) needs an account - an authenticated boundary never reached
- the /auth and partner sign-in forms were measured and typed into then cleared, never submitted - validation, error, loading, success and verification-code states are absent rather than measured; no OAuth, SSO or passkey flow was started
- the booking wizard stops at service selection: Continue was never pressed, so staff, time-slot, payment and confirmation steps are absent
- venue content (staff, reviews, hours, prices) is that venue's published data, not a canonical template

## [Front](../systems/front) — `front`
Access: signed out (every captured surface is public; the workspace and every post-login surface is an authenticated boundary never reached; the demo, signup, auth and search fields were measured and typed into then cleared, never submitted; every CTA, SSO button, nav item and link was measured, never followed; the Qualified 'Quinn' widget was measured at rest, never opened; the app dark theme is the shell's own front-theme-preference mechanism, verified painted as html[data-theme=dark]; the marketing violet/light/gray sets are section themes, not a page-level switch)
- the workspace and every post-login surface (inbox, contacts, rules, analytics, settings) sits behind an account - an authenticated boundary never reached; app /signin, /signup and /forgot-password were measured as forms, never submitted, and Google/Office 365/SAML SSO was never followed
- app /signup and /forgot-password paint the same sign-in card as /signin (email, password, 'Sign in') - no dedicated signup or reset form exists signed out; recorded as painted, not inferred
- submitted states: the /request-demo and /signup forms, the auth cards and the help search were typed into then cleared, never sent - validation, error, loading and success states are absent rather than measured
- the marketing violet/light/gray sets are [data-theme] section themes of one page, not a user-selectable dark mode; the dark set is the app auth shell's own theme, a different stack
- disabled, error, loading and validation states never appear signed out - nothing was submitted

## [Fernand](../systems/getfernand) — `getfernand`
Access: read-only (the marketing site, the signed-out app.getfernand.com/auth/login and /create forms, and help.getfernand.com in light and toggled dark are fully public; every post-login app surface - the inbox workspace, settings, API keys - is an authenticated boundary never reached; the login/signup forms were measured and typed into then cleared, never submitted; the 'Book a demo' Cal.com scheduler was measured, never activated; every link and CTA was measured, never followed; no consent banner was observed on any host)
- every post-login app surface (the inbox workspace, conversation views, settings, API keys, team/AI-agent configuration) needs an account - an authenticated boundary never reached
- the /auth/login and /create forms were measured and typed into then cleared, never submitted - validation, error, loading and success states are absent rather than measured
- the 'Book a demo' action loads the Cal.com scheduler; starting a real booking flow is a side effect, so it was measured at rest and never activated

## [Gladia](../systems/gladia) — `gladia`
Access: signed out (every captured surface is public; the app console and every post-login surface - API keys, transcription playground, usage, billing - is an authenticated boundary never reached; the /demo-request, pricing-calculator, login and signup fields were measured and typed into then cleared, never submitted; every CTA, SSO button, nav item and link was measured, never followed; the mega-menu opens by hover intent or keyboard, the pricing-mode toggle and FAQ accordions are local UI toggles, and the docs dark theme is the Mintlify site's own preference)
- the app console and every post-login surface (API keys, transcription playground, usage, billing, settings) sits behind an account - an authenticated boundary never reached; app.gladia.io / and /signup were measured as forms, never submitted, and Continue-with SSO buttons were never followed
- submitted states: the /demo-request form, the pricing-calculator fields and the auth cards were typed into then cleared, never sent - validation, error, loading and success states are absent rather than measured

## [Glassnode](../systems/glassnode) — `glassnode`
Access: signed out (every captured surface is public; the signed-in Studio workbench - chart editor, saved dashboards, alerts, API keys, billing - is an authenticated boundary never reached; the newsletter, contact and Auth0 username fields were typed into then cleared, never submitted; every CTA, nav item and link was measured, never followed; the studio dark-theme layer is declared but has no public control, so dark.studio.* tokens are labelled declared-not-painted; the research, docs and registry theme controls are the sites' own toggles; the Auth0 landing URL's volatile ?state= is sanitized to origin+path in every sidecar)
- the signed-in Studio workbench - chart editor, saved dashboards, alerts, API keys, billing and every post-login surface - sits behind an account; the Auth0 card was measured as a form, never submitted, and Continue with Google was never followed
- submitted states: the newsletter, contact and Auth0 username fields were typed into then cleared - validation, error, loading and success states are absent rather than measured

## [Glorify](../systems/glorify) — `glorify`
Access: signed out (every captured surface is public; the signed-in workspace, saved files, billing and account settings are an authenticated boundary never reached; the auth and Craft fields were measured and typed into then cleared, never submitted; Login, Signup, Share, Download, Replace and 'Add to canvas' were measured, never pressed; no trial was started, no OAuth followed and nothing was purchased)
- every signed-in product surface (saved designs, workspaces, team/billing, the editor beyond the anonymous scratch file) needs an account - an authenticated boundary never reached
- the login, register and Craft fields were measured and typed into then cleared, never submitted - validation, error, loading and success states are absent rather than measured
- the anonymous editor's file content, layers and canvas tools beyond the onboarding and the Craft dialog were not exercised - the scratch file was never saved

## [GlossGenius](../systems/glossgenius) — `glossgenius`
Access: signed out (every captured surface is public); the product app behind sign-in (calendar, clients, payments, marketing tools — app.glossgenius.com/ redirects to /calendar) was never reached; the login, signup, restore and demo forms were measured and typed into then cleared, never submitted; the published booking flow was browsed read-only to its public /book date-picker — no slot confirmed, no appointment booked; every CTA measured, never followed; no consent banner was observed on any host
- everything post-login — the calendar, clients, payments, marketing and business tools behind app.glossgenius.com sign-in (the app root redirects to /calendar); an authenticated boundary never reached
- submitted states: the login, signup, forgot-password and get-demo forms were typed into then cleared, never sent — validation, error, loading and success states are absent rather than measured
- the booking flow stops at the public /book date-picker — slot confirmation, the YOUR DETAILS form and payment were never reached; 'Next' never pressed
- the booking site is one business's skin (honeyhivesalon.glossgenius.com, Organic-style layout) — other businesses re-skin the same chrome through other .tokens_glossDS__* layout classes; booking tokens are this surface's resolution, not a universal brand set
- an edge security-verification page blocked app.glossgenius.com/login on one pass; a retry in a fresh context succeeded and no challenge was answered by hand

## [GoFundMe](../systems/gofundme) — `gofundme`
Access: signed out (every captured surface is public; the account, the donation flow, checkout and every post-login surface is an authenticated boundary never reached; the wizard's postcode field and the sign-in email field were typed into then cleared, never submitted; 'Donate now', 'Share', 'Message', 'Continue', 'Sign in', 'Start a GoFundMe' were measured, never activated)
- the account, the donation flow, checkout and every post-login surface was never reached
- the /create wizard was captured at its first public step only; its category pills and 'Continue' were measured, never submitted - later wizard steps sit behind it
- the /sign-in Welcome card was measured signed-out; the email field was typed into then cleared and 'Continue'/SSO were never pressed - no account was ever touched; in some headless passes the island does not hydrate and only the empty shell records
- some measured components are missing or zero-sized where the route did not serve them in a given pass (the donations heading, the search heading, the sign-in card's buttons); gaps are recorded, not fabricated

## [Grammarly](../systems/grammarly) — `grammarly`
Access: signed out (every surface captured is public; the product sits at app.grammarly.com behind login)
- app.grammarly.com and everything behind Log in / Sign up was never opened: the editor, dashboard, documents, account, billing and admin surfaces are signed-in and out of scope
- no form was submitted (contact sales, sign-in, newsletter) and no checkout or trial started, so success and painted error states are missing
- the free tools' result views (plagiarism report, AI-detector verdict, paraphrase output) each need a submit action the kit never performs; the grammar checker's live suggestion cards render in a product overlay outside the page's light DOM and are recorded missing

## [Grok / xAI Docs](../systems/grok) — `grok`
Access: signed out (every captured surface is public docs.x.ai; grok.com's chat product never cleared the Cloudflare managed challenge and x.ai, console.x.ai, status.x.ai and accounts.x.ai returned Cloudflare 403 blocks from the capture host - blocked boundaries, never claimed as captures; nothing was signed into, typed, searched, sent, bought or submitted; the only presses were local UI toggles - theme button, Ctrl+K, sidebar chevrons, SDK tabs, the phone nav button)
- x.ai, console.x.ai, status.x.ai and accounts.x.ai returned Cloudflare 403 'Sorry, you have been blocked' from the capture host - marketing, console, auth and status surfaces were never reached
- dark-only declarations (--border, --input, --ring, --alert, --on-alert, --background-*, --content-*, --sb-*) exist in the dark token set alone and were never inferred for light

## [Grow with Google](../systems/grow) — `grow`
Access: signed out (every captured surface is public; enrolment on Coursera, Google accounts and all outbound links were measured, never followed; the footer's language select was never changed — its form posts to services.google.com; the hero YouTube embed was opened and closed, never played; no sign-in exists on grow.google)
- enrolment and accounts live off grow.google (coursera.org, Google sign-in): every CTA was measured, never followed

## [Gumroad](../systems/gumroad) — `gumroad`
Access: signed out (every captured surface is public gumroad.com or a public creator subdomain; the seller dashboard, buyer library and settings stayed behind login; the public checkout was captured empty and never submitted; nothing was signed into, typed, searched, sent, bought or submitted; the only presses were local UI toggles - the carousel arrow, the nav menu button, the Share popover, the billing-term select)
- post-login surfaces: the seller dashboard (products, sales, payouts, analytics), the buyer library and account settings were never reached - the capture was signed out end to end
- search results: the marketplace search fields were measured empty; no query was ever submitted
- checkout beyond the empty public form: payment, confirmation and post-purchase screens were never reached

## [Hashnode](../systems/hashnode) — `hashnode`
Access: signed out (every captured surface is public: hashnode.com marketing/feed/posts/profiles/product sections and townhall.hashnode.com; /login and every post-auth surface never entered; engineering.hashnode.com returned 429, help./docs./blog./api./support./changelog./weekly. subdomains do not resolve, status.hashnode.com is a Better Stack page not the product - blocked boundaries, never claimed as captures; nothing was signed into, typed, searched, sent, bought or submitted; the only presses were local UI toggles - the search dialogs, Theme/More menus, FAQ and tab rows, the sidebar toggle, the phone nav button)
- the signed-in product (/login and everything behind it - dashboard, editor, settings, the onboarding submit) is a boundary: the Sign in / Start your blog / Get Pro links were measured, never followed
- five components read as absent on this pass (the profile sticky header, the Get Pro plan CTA, the deferred onboarding field, the blog article's pre wrapper, the blog search suggestion row) - recorded as missing, not measured as absent

## [HBO Max](../systems/hbomax) — `hbomax`
Access: signed out (every captured surface is public; sign-in, plan checkout, the help centre and account surfaces were link-observed only and never opened)
- auth.hbomax.com sign-in, plan selection and checkout, help.hbomax.com and every account surface were observed as links only and never opened; no form was submitted and no trial or plan was started
- carousel-next, yearly-billing, FAQ-open, cookie-modal and mobile-nav states are local UI toggles only - nothing was accepted, purchased or submitted

## [Headspace](../systems/headspace) — `headspace`
Access: signed out (every captured surface is public); the member app behind auth.headspace.com login was never reached; the universal login/signup, newsletter, redeem-code and checkout forms were measured empty, never filled or submitted; no trial started, no plan bought, no code redeemed; every CTA measured, never followed; the OneTrust consent layer was hidden, never answered
- everything post-login - the member home, meditation player, streaks, settings and the whole signed-in app behind auth.headspace.com; an authenticated boundary never reached
- submitted states: the universal login/signup, newsletter, redeem-code and checkout forms were measured empty, never sent - validation, error, loading and success states are absent rather than measured
- /pricing answers a real 404 ('Whoops! Something's changed'); the plans live on /subscriptions - a recorded absence, not a capture
- the checkout shell's form fields, the feature/testimonial cards, the FAQ accordion, the plan cards and billing switch, the content tiles, the footer language selector and app badges, and the mobile nav sheet did not match the kit's structural selectors on this pass - recorded as absent components, not measured

## [Hello Ivy](../systems/helloivy) — `helloivy`
Access: signed out (every captured surface is public: www.helloivy.co marketing routes, app.helloivy.co/login at rest and the public share document, and the hosted /docs platform; nothing was signed into, typed, searched, sent, bought or submitted; the only presses were local UI toggles - the Framer menu overlay, the footer's real 'Change theme' control, the pricing FAQ accordion, the share page's settings popover and the phone's menu drawer; every link was measured, never followed; the workspace and every post-auth surface was never entered)
- the signed-in product (the workspace, projects, clients, files and settings behind /login) is a boundary: the login card was measured at rest, fields never typed, 'Continue' never pressed
- the app's semantic layer resolves only where its inline section.main_section theme exists - the public share route; /login carries no section so app roles there are measured, not themed

## [Hitchd](../systems/hitchd) — `hitchd`
Access: signed out (the marketing pages, content pages and demo registries are fully public; the auth forms were read at rest - nothing was focused, typed or submitted; the gift modal's Give/contribute flow and every payment step were never entered; the registry's internal routes /contributions, /payment-methods, /ask and /quick-thanks bounce the guest to / and were recorded as boundaries)
- focus/hover/pressed states on the auth controls were never forced (focusing a field is the first step of signing in)
- the registry's internal routes (/contributions, /payment-methods, /ask, /quick-thanks) bounce the signed-out guest to /

## [Homerun](../systems/homerun) — `homerun`
Access: signed out (the marketing routes and careers site are fully public; the ATS and HR apps sit behind sign-in - both public login cards were measured at rest, never submitted; the public application wizard was never advanced past its first step; consent banners were hidden without answering them; sign-up/login/apply links were never followed)
- the ATS and HR apps sit behind sign-in and were never crossed; both login cards were measured at rest and never submitted, no credentials exist in the capture
- the application wizard was never advanced past its first step: nothing was typed, uploaded or submitted, and its file input/checkbox paint through custom controls over 0x0 inputs

## [HTTPie](../systems/httpie) — `httpie`
Access: signed out (every captured surface is public: httpie.io marketing/docs/blog/legal pages and /app, the HTTPie-for-Web client that runs unsigned in its 'Incognito space'; sign-in and every account surface - named spaces, sync, shared collections - never entered; the HTTPie AI 'Try it out' action never pressed; Send never pressed on /app - issuing a request is a network side effect, so the response pane stands at its resting 'Not sent' state; the desktop/CLI binaries behind /download never fetched; /pricing 404s and is kept as the product's not-found page; /discord redirects off-site; nothing was signed into, typed, searched, sent, bought or submitted; the only presses were local UI toggles - the ThemeToggle radios, the method and Incognito-space controls, the request and environments tabs, the Cmd+K DocSearch dialog opened for icons and closed unqueried)
- the signed-in product (named spaces, sync, shared collections, the avatar and Sign-in prompts) is a boundary - measured, never entered
- HTTPie AI 'Try it out' is an account/paid generation flow - the promo dialog is evidence, the action is not
- the newsletter inputs were measured and focused, never typed or submitted - the success/mail flow is absent
- the Import/Migrate card, + Collection's Create dialog submit and 'Create environment' were never confirmed - the surfaces behind them are absent

## [Huddlekit](../systems/huddlekit) — `huddlekit`
Access: signed out (every captured surface is public: the huddlekit.com marketing site and app.huddlekit.com/login, the only surface the app serves anonymously; everything past /login 307-redirects an anonymous visitor and was never entered; Google OAuth and the email form's Continue were never submitted; try./demo./status./docs./help.huddlekit.com and app.huddlekit.io do not resolve - blocked boundaries, never claimed as captures; nothing was signed into, typed, searched, sent, bought or submitted; the only presses were local UI toggles - the consent banner's Decline, the nav menus, FAQ and tab rows, the billing switch, Show-more, the email reveal, the phone's menu button)
- the signed-in product (everything on app.huddlekit.com past /login - the annotation widget on a real site, the project dashboard, workspaces, settings, billing) is a boundary: the Sign in / Get started links were measured, never followed
- huddlekit.com has no theme control: the dark token set is the .dark re-pointed declarations the app paints under prefers-color-scheme (verified on the login), and the site's dark footer/testimonial/MCP panels are component-level surfaces, not a page theme
- no field was ever typed into (support search, contrast-checker inputs, the login email field were focused only), so validation, suggestion and error states are uncaptured; the email Continue and Google OAuth were never submitted
- prefers-reduced-motion is only partly honoured - /pricing, /features and the login ignore it and the marquee/ping loops keep running; the probe's per-page verdicts are in raw/motion.json

## [Hume AI](../systems/hume) — `hume`
Access: signed out (every captured surface is public: www.hume.ai marketing/product/blog/legal pages, the dev.hume.ai docs, the demo.hume.ai invitation gate and the app.hume.ai/log-in card; the demo playground is gated on an invitation email and was never entered, nothing past /log-in was entered, EVI/Octave TTS have no public surface post-pivot - demo.hume.ai/evi answers 404; nothing was signed into, typed, searched, sent, bought or submitted; the only presses were local UI toggles - the docs Theme menu, the home player's transport, the benchmark tabs, the blog filters and the mobile drawer)
- the signed-in platform (app.hume.ai past /log-in - dashboard, API keys, projects, billing) is the product's own boundary, never entered
- contact, newsletter and log-in fields were clicked into for the focus look only - never typed or submitted

## [Intercom](../systems/intercom) — `intercom`
Access: signed out (every captured surface is public: www.intercom.com marketing routes, the /help/en/ help center and /changes/en changelog; app.intercom.com, /signup onboarding, purchase and the contact-sales form's later steps never entered - the Log in / Start free trial / Get started / Contact sales links were measured, never followed; the Next submit was measured with forced pseudo states, never pressed; no select option was chosen and the marketing checkbox was never ticked; nothing was signed into, searched, chosen, uploaded, bought or submitted; the only presses were local UI toggles - the nav mega-menu, the billing switch, a FAQ row, the select's own listbox and the mobile menu button)
- the signed-in product (app.intercom.com - inbox, tickets, reports) is a boundary: the Log in link was measured, never followed
- trial onboarding (/signup), purchase and every conversion path past the marketing surface are boundaries, not captures
- three header components (logo, nav-login, nav-cta) were measured on one pass and preserved on a later recapture that missed them - recorded as recaptureMissed provenance

## [Jace AI](../systems/jace) — `jace`
Access: signed out (marketing routes are public; app.jace.ai/signin was measured at rest; app.jace.ai/signup was opened through the privacy notice to the Google/Outlook card; there is no email or password field; Google, Outlook and SSO were never pressed; the sales form was focused and a sample string typed then deleted, nothing submitted)
- the inbox, drafts, labels, Flows, settings and billing sit behind Google or Outlook OAuth on https://app.jace.ai/signin and https://app.jace.ai/signup; there is no email or password field, so those surfaces were not reached
- Continue with Google on sign-in and signup is an OAuth flow and was not pressed (hover, focus-visible and a DevTools-forced pressed state only)
- Continue with Outlook on sign-in and signup is an OAuth flow and was not pressed (hover, focus-visible and forced pressed on signup)
- Enterprise SSO at https://app.jace.ai/enterprise-sso (Launch the SSO portal) was not followed
- the sales form at https://jace.ai/contact/sales (Send a request) was shown at rest, focused, and a sample string typed then deleted; it was not submitted, so no posted validation error was captured
- checkout and payment sit behind sign-in and were not opened
- account deletion and settings sit behind sign-in (public docs mention them) and were not opened
- marketing home and pricing ignore prefers-reduced-motion; sign-in is partial (raw/motion.json)

## [Jasper AI](../systems/jasper) — `jasper`
Access: signed out (marketing routes on www.jasper.ai are public). Signed-in pass attempted 2026-11-18 via Continue with email on app.jasper.ai/auth/signup and /auth/login: continueWithEmail returned HTTP 401 and the page toasted 'Failed to send login link. Please contact support for further assistance.' No password field exists (passwordless). Google OAuth was not followed. No CAPTCHA, phone, payment or KYC appeared. Canvas, agents, Brand IQ and campaigns were not reached. Transcend and cookie overlays were hidden, never answered
- Product app (canvas, agents runtime, Brand IQ editor, campaigns) at https://app.jasper.ai/ was not reached. A signed-in pass on 2026-11-18 submitted Continue with email on /auth/signup and /auth/login; continueWithEmail returned HTTP 401 and the page toasted Failed to send login link. Please contact support for further assistance. No password field exists. Google OAuth was not followed. No CAPTCHA, phone, payment or KYC appeared.
- Signup and free trial at https://app.jasper.ai/auth/signup stay gated: Continue with email 401s, so no trial, onboarding or paid-plan screen was opened.
- Get a Demo form at https://www.jasper.ai/demo was measured at rest and never submitted, so no validation, error or success state was captured.

## [JetBrains](../systems/jetbrains) — `jetbrains`
Access: signed out; Continue with email opened the signup email field; reCAPTCHA blocked the signed-in account
- Signed-in JetBrains Account (profile and licenses) at https://account.jetbrains.com was not captured: Continue with email on /signup opened the email field, then Continue hit reCAPTCHA ('I'm not a robot') and capture stopped. No OAuth button was completed
- Store checkout and Buy at https://www.jetbrains.com/store/ were not followed
- Product downloads at https://www.jetbrains.com/products/ were not started; starting a download is a submit boundary and was not followed
- The cookie dialog at https://www.jetbrains.com/ was hidden and never submitted

## [Jitter](../systems/jitter) — `jitter`
Access: signed in on a free email account; marketing plus files, account, trash, brand kit, onboarding and the editor were captured; Google/SSO were never clicked; billing checkout, paid export and Invite were not opened; Superagents Upgrade now was measured at rest
- SSO at https://jitter.video/sso and Continue with Google / Continue with SSO on https://jitter.video/login/ were measured at rest and never clicked
- checkout and billing at https://jitter.video/billing and Upgrade your plan / Upgrade now were measured at rest and never followed; no card was entered
- Invite members and Send invites were measured at rest and never submitted
- the contact-sales form at https://jitter.video/contact-sales/ was measured empty and never submitted
- no validation, disabled or toast state was produced because no form was submitted after sign-in

## [Handshake](../systems/joinhandshake) — `joinhandshake`
Access: signed out (every captured surface is public: joinhandshake.com's marketing pages serve a plain load, and app.joinhandshake.com/access - the 'Log in or sign up' card - cleared its Cloudflare challenge intermittently and was captured on the loads that did; /explore, /signup, the registration flow and support.joinhandshake.com never cleared - blocked boundaries, not captures; nothing was signed into, typed, searched, sent, bought or submitted; the only presses were local UI toggles - the nav's hover-opened mega menu, segment tabs, FAQ and department accordions, the phone's 'Open menu' button)
- the consumer app's signed-in surfaces - /explore, /signup, registration, dashboards - are a blocked boundary: the Cloudflare managed challenge never cleared across fresh-context retries
- the Marketo lead forms were measured at rest; no field was filled and nothing was submitted - validation, error and success states are absent

## [Julienne](../systems/julienne) — `julienne`
Access: signed out (public pages only: home, discover, a published recipe, ingredient search, a collection, team, roadmap, shop, privacy policy, signup at rest, and the cookbook gate; nothing typed, submitted, saved, cooked or bought; the only presses were the theme toggle, a discover filter chip, the marketing Menu button, and Log in opened and closed at rest)
- the signed-in cookbook at https://withjulienne.com/cookbook is a boundary: signed out it shows Come back soon, and the account cookbook was not entered
- Save on a recipe (https://withjulienne.com/days/11_17_2026/recipes/chef_muse_20261117_soup_season_e92685c034_10) was not pressed; saving needs an account
- Cook on that recipe page was not pressed; cook mode needs an account
- Log in and https://withjulienne.com/signup were read at rest; email, password, Google, Apple and Turnstile were never used
- search was not typed or submitted; /search?ingredients=apple is a published browse link

## [Kickstarter](../systems/kickstarter) — `kickstarter`
Access: signed out (every captured surface is public; login, signup, pledge, save, checkout and the project editor past the first /start step were not entered; the email field was typed into and cleared; Continue, Next, Back this project, Save and Sign in with Apple were measured, never activated)
- https://www.kickstarter.com/login — the account after Continue, and Sign in with Apple (OAuth), were not entered. The email field was typed into and cleared. Turnstile was not solved.
- https://www.kickstarter.com/signup — redirects to /login. Account creation was not started.
- https://www.kickstarter.com/projects/shirtaloon/hwfwm — Back this project, Remind me, and the share controls were measured and not followed. Pledge and checkout are gated.
- https://www.kickstarter.com/start — the category step is public. Next was not pressed. The project editor, story, rewards, and launch sit behind an account.
- Save this project on home and Discover cards requires an account and was not activated.
- Comments, updates posting, messages, and the creator dashboard were not opened.

## [Kinhive](../systems/kinhive) — `kinhive`
Access: public site plus the join and sign-in 6-digit code step; contact, subscribe, and the hero email were not submitted; LinkedIn, store badges, template downloads, and Add to cart were not followed; the signed-in app was not opened because the code email never arrived
- the signed-in app at https://kinhive.com/home, /matches, /chat, /cowork, /profile, /settings, /notifications, /community, /posts, /team, /room, and the other paths robots.txt disallows, was not opened: join POST /api/auth/join returned ok true and sign-in POST /api/auth/sign-in returned status sent, but no Kinhive message arrived at the capture inbox, and later submits returned Too many emails sent / Too many attempts
- https://kinhive.com/join was submitted through the 6-digit code step; a wrong code and a send-rate limit were captured; the in-app onboarding after a valid code was not reached
- https://kinhive.com/sign-in Email me a sign-in code was pressed; Continue with LinkedIn was not
- https://kinhive.com/contact Send message was not submitted, so validation, error, and success states were not reached
- the hero email, the mid-page capture email, and the footer Subscribe fields were not submitted
- https://kinhive.com/shop/founders-hat Add to cart was not pressed, and checkout was not started; the cart drawer was opened empty at https://kinhive.com/shop
- template Fill in online, Copy to Google Docs, and Download as Word on https://kinhive.com/templates/nda were not followed; those are submission and account boundaries

## [Kit](../systems/kit) — `kit`
Access: signed out (the creator app behind app.kit.com login was never reached)
- the signed-in creator app at app.kit.com (dashboard, email designer, automations, subscribers, commerce) needs an account and was never reached
- the request-a-demo form at https://kit.com/request-demo sits in a Chili Piper iframe (https://kit.chilipiper.com/concierge-router/demo-request-form) and was not submitted
- password reset at https://app.kit.com/users/password/new is linked from the log-in card and was not followed
- checkout and trial links on https://kit.com/pricing point at signup with a plan query (plan=1k, plan=1k-annual, plan=kit-free) and were measured, never followed
- disabled, error, loading and validation states were not seen because no form was submitted
- the product publishes no dark theme; the dark token set is empty on purpose
- C5, V1 and V2 are not published by the product

## [Kitchen.co](../systems/kitchen) — `kitchen`
Access: signed in (free workspace after email signup; invites, creates, Upgrade, DocuMocu connect and Stripe checkout were not submitted)
- Get a demo (https://kitchen.co/get-demo): the demo request form was not submitted
- Lifetime checkout (https://kitchen.co/pricing Pay Now and Settings > Billing Buy Lifetime Access): Stripe checkout was not opened
- Workspace theme customisation is paid (Settings > Branding > Theme & Colors Upgrade)
- Invites, new folders, boards, conversations and clients were not created

## [Kitchen Stories](../systems/kitchenstories) — `kitchenstories`
Access: signed out (every captured surface is public; checkout, profile, the recipe cart and rating submit were not followed)
- Plus checkout: Jetzt kostenlos starten on https://pages.kitchenstories.com/de/plus links to https://www.kitchenstories.com/de/checkout and was not followed
- Account: https://www.kitchenstories.com/profile (Dein Kitchen Stories Konto zieht um) was not signed into. /login and /anmelden return 404
- Recipe rating submit (Abschicken / Bewerte das Rezept) on that recipe URL was not submitted
- Contact form on https://www.kitchenstories.com/kontakt was not submitted

## [Klarna](../systems/klarna) — `klarna`
Access: signed out (US marketing at www.klarna.com/us/ and the country picker at /international/ are public; the OneTrust banner was hidden and never answered; Sign in was opened once to the app.klarna.com QR interstitial and not followed; no account, checkout, search submission or purchase)
- Klarna app sign-in at https://app.klarna.com/login?market=US&locale=en-US stops at a QR interstitial (Continue securely in the Klarna app). Continue on web? was not followed, so the typed sign-in form was not captured
- Signed-in payments, purchases, portfolio, savings and account sit behind that sign-in and were not captured
- Checkout was not started. Shop now and Get the app were not followed into a purchase
- Search overlay on https://www.klarna.com/us/ was opened and not submitted, so search results were not captured
- The language and region dialog was opened. Confirm was not submitted

## [Kraken](../systems/kraken) — `kraken`
Access: signed out (trading, wallets, account and any submitted form were not entered)
- Sign-in at https://id.kraken.com/sign-in was photographed at rest. The email field was focused. Nothing was typed. Continue, Google, Apple and passkey were not followed.
- Create an account at https://www.kraken.com/sign-up was photographed at rest. Continue was not submitted and the Google and Apple buttons were not followed.
- Kraken Pro trading at https://pro.kraken.com/app/trade and the markets at https://pro.kraken.com/app/markets/spot sit behind sign-in. The /pro marketing page was captured. The app was not opened.
- The consumer app at https://app.kraken.com/ and the product routes behind /app (xstocks, borrow, onchain, auto-earn, perpetual futures, Kraken+, dollar-cost averaging, crypto card) require an account. The /app marketing page was captured.
- Portfolio, wallets, checkout, KYC and card issuance require an account and were not entered.
- The institutions contact form on https://www.kraken.com/institutions (Get in touch) was not submitted.

## [Krea](../systems/krea) — `krea`
Access: read-only (the home shell, pricing, enterprise, blog, plugins, MCP, the image tool, docs, terms and the login card are public; a Continue with Email attempt on 2026-11-18 was stopped by Cloudflare Turnstile: GET /api/auth/email-flow returned 400 captcha_failed with no visible widget, so assets, train, nodes, account, billing, API keys, checkout and generation remain behind sign-in; Sign in, Sign up, OAuth, Book a call, Get Pro and Generate were measured, never followed except that one Email continue; the prompt and email fields were filled; consent overlays were hidden, never answered)
- https://www.krea.ai/login is the auth boundary (Continue with Google, Continue with Apple, SSO, Continue with Email). Google, Apple and SSO were never followed. Continue with Email was submitted once on 2026-11-18; GET /api/auth/email-flow returned 400 captcha_failed (Cloudflare Turnstile, no visible widget). Stopped there
- https://www.krea.ai/assets redirects to /login?redirect=%2Fassets. The signed-in asset library was not captured: the email pass never got past Turnstile
- https://www.krea.ai/pricing plan buttons (Get Free, Get Basic, Get Pro, Get Max) open account or checkout and were measured, never followed
- https://www.krea.ai/ and https://www.krea.ai/image Generate and the composer submit a generation. They were measured, never clicked
- Train, Node Editor, account settings, billing and API keys sit behind sign-in and were not opened
- composer-send, image-generate, price-card, faq-item, m-sidebar and m-signin were not found as stable elements on the measurement pass

## [Krisp](../systems/krisp) — `krisp`
Access: signed-in free account (passwordless email OTP); /meetings and recordings redirect to the desktop download gate; notes, settings and billing were captured; Upgrade and calendar OAuth were not followed
- /meetings and recordings redirect to /setup (desktop app download) on this free account
- Upgrade, Download for macOS, Connect Google/Outlook, Delete account and Enable 2FA were not pressed
- Book a demo and Talk to Sales open https://krisp.ai/contact-sales/: a sales form, not submitted

## [LEGO](../systems/lego) — `lego`
Access: read-only (home, theme, bestsellers, product, offers, service, about and search are public signed out; sign-in, bag, checkout, wish list contents and membership signup were not entered)
- Sign-in at https://www.lego.com/identity/login sits behind a LEGO account and was not entered
- My Bag at https://www.lego.com/en-us/cart was not opened; Add to Bag was measured and never pressed, so the bag and checkout stay behind an account boundary
- Checkout at the bag sits behind sign-in and was not entered
- Wish list contents behind the header Wish List control sit behind a LEGO account and were not opened
- Membership signup (Become a member / Insiders) was not submitted
- The footer email subscription field was not submitted

## [Lemni](../systems/lemni) — `lemni`
Access: signed-in free account (email magic link at lemni.com/signin; Google unused). Public marketing plus the workplace app as the free trial shows it. Upgrade and payment were not followed.
- Continue with Google at https://lemni.com/signin. Email magic link was used. Google was not clicked.
- Upgrade and checkout at https://lemni.com/welcome/subscribe and the workplace sidebar Upgrade control. Captured at rest. Not pressed. No plan was bought.
- Application form at https://www.lemni.com/company/apply. Not submitted.

## [Lemon Squeezy](../systems/lemonsqueezy) — `lemonsqueezy`
Access: signed-in pass attempted (email/password). The address was not registered. New store signups are closed: business-intent submits to a Stripe Managed Payments recommendation. Get started, Google, Twitter, bank connect and payout KYC were not followed. Merchant dashboard routes bounce to login. Customer order portal login was opened and not submitted.
- the signed-in merchant dashboard at app.lemonsqueezy.com (products, orders, subscriptions, customers, discounts, affiliates, payouts, analytics, settings) was not opened: new store signups are closed, the email was not already registered, and those routes bounce to auth.lemonsqueezy.com/login
- Stripe Managed Payments onboarding behind Get started on https://auth.lemonsqueezy.com/signup/smp was stopped (Stripe onboarding / take-payments stop)
- Google and Twitter OAuth on https://auth.lemonsqueezy.com/login were measured as buttons and never followed
- the password reset form at https://auth.lemonsqueezy.com/password/reset was not opened
- the customer order portal magic-link on https://app.lemonsqueezy.com/my-orders/login was opened and not submitted
- Stripe Managed Payments signup at https://dashboard.stripe.com/register/managed_payments and https://stripe.com/managed-payments were not opened; they are a different product
- checkout and purchase are not on the public marketing pages and were not opened
- CAPTCHA, phone verify and payout KYC did not appear

## [Leonardo.Ai](../systems/leonardo) — `leonardo`
Access: read-only (marketing pages, the signed-out app shell, public Blueprints, the login card and the docs getting-started page are public; Library, account, generation, checkout, API keys and OAuth were never entered; Start now, Subscribe, Log in, Generate and the provider buttons were measured where they painted, never followed; the prompt was filled and cleared; the consent overlay was hidden, never answered)
- Library and other account routes redirect to https://app.leonardo.ai/auth/login — an authenticated boundary never reached
- Generate on the signed-out prompt composer at https://app.leonardo.ai/ was measured and not submitted
- Subscribe on https://leonardo.ai/pricing hands off to the app; checkout was not entered
- OAuth at https://app.leonardo.ai/auth/login (Canva, Apple, Google, Microsoft) and Continue with Email were measured at rest, never followed; the email form and Turnstile were not submitted
- API keys and the API console sit behind the account; https://leonardo.ai/api and the public docs page were captured, the console was not
- Contact form at https://leonardo.ai/contact-us was not submitted
- Team plans checkout at https://leonardo.ai/team-plans was not entered
- Marketing nav controls (header, Pricing, Log in, Create, Start now) and the app rail, Sign up, Sign in and featured cards are in the screenshots and were not boxed on the measurement pass

## [Limitless](../systems/limitless) — `limitless`
Access: signed-out public marketing, docs, legal, help center, and the app.limitless.ai sign-in wall; a 2026-11-18 signed-in pass submitted the email field only (never Google) and stopped at Sign Up Unavailable (Limitless is no longer accepting new users). Lifelogs, settings and account were not entered. No Pendant purchased. No CAPTCHA, phone or payment.
- app.limitless.ai/signin: submitting a new email opens Sign Up Unavailable (Limitless is no longer accepting new users); lifelogs, settings, billing and account were not entered
- Continue with Google at https://app.limitless.ai/signin starts OAuth and was not pressed
- Pendant purchase is no longer offered to new customers; the unavailable dialog tells Pendant owners to email support; no checkout was opened
- account deletion, documented at https://help.limitless.ai/en/articles/13005203-how-to-delete-your-limitless-account-and-data, was not opened
- the Slack community invite at https://www.limitless.ai/community leaves the site and was not followed

## [Maze](../systems/maze) — `maze`
Access: signed-out public marketing, pricing, the auth login card, and one published sample report. No study started. No form submitted. No purchase.
- app.maze.co past the public report redirects to sign-in; the workspace was not entered
- auth.maze.co/signup and the Starter Sign up now link were not followed
- the login form was not submitted; the password field was never filled
- the demo form and the footer newsletter were not submitted
- SSO and password reset were not opened

## [Lummi](../systems/lummi) — `lummi`
Access: signed-out public marketing, browse, a public image page, and the /login wall. Downloads, the account, generation and checkout were not entered. Continue, Download, Google and the Stripe checkout link were not pressed.
- Downloads on a public image page require sign-in and were not pressed
- https://www.lummi.ai/login is the sign-in wall; Continue and Continue with Google were not pressed, so the account was not entered
- Generation (Create image, Create video) sits behind sign-in and was not opened
- https://www.lummi.ai/pro links to a Stripe checkout and that checkout was not opened
- The email field on /login was filled with a placeholder and cleared; the form was not submitted

## [Macaw](../systems/macaw) — `macaw`
Access: signed-out public marketing, pricing, contact, one free-tool page, and legal. The product app host did not resolve. No form was submitted.
- app.macawhq.com sign-in and sign-up did not resolve (ERR_NAME_NOT_RESOLVED); the product app was not entered
- the contact form was not submitted
- Start free with Google starts a Google sign-in strategy and was not followed
- no checkout was opened

## [ManyChat](../systems/manychat) — `manychat`
Access: read-only (the marketing site is public signed out; the bot builder and the in-app template library sit behind sign-in at app.manychat.com, never entered; Log in, Get started and Start for free were measured, never followed; checkout was not submitted)
- the bot builder and the in-app template library sit behind sign-in at app.manychat.com; Log in and Get started were measured, never followed
- checkout was not submitted; Monthly and Annual were toggled locally

## [Scape](../systems/scape) — `scape`
Access: signed out. Public marketing only. Booking, payment, phone and the contact form were not entered. Cookie consent was dismissed with Reject All.
- booking, payment, phone and the HubSpot contact form were not entered

## [The Athletic](../systems/the-athletic) — `the-athletic`
Access: signed out (theathletic.com redirects to nytimes.com/athletic; home, one public article, about, the NFL league page, the subscription marketing page, the login shell, search, and a 404 were read; the login iframe was not entered; Continue to checkout was not followed; no card, account, or email was submitted)
- the login iframe is cross-origin and was not entered
- Continue to checkout was not followed, and no card was entered

## [IFTTT](../systems/ifttt) — `ifttt`
Access: signed out (every captured surface is public: ifttt.ai marketing home and ifttt.com's /explore(+services,+stories,+applets) gallery, /plans pricing, /twitter and /todoist service pages, an applet page, /connect/discord/instagram, /solutions/productivity and /solutions/smart-home, /mcp, /about, /careers, /partners, /terms and a made-up-route 404; 'Log in', 'Get started' and every /join path measured, never followed; the Applet 'Connect' install toggle measured, never pressed; the plan CTAs never followed to checkout; help.ifttt.com answers HTTP 403 to automation - a documented blocked boundary; platform.ifttt.com redirects to ifttt.ai - no separate public platform surface; the App Store/Play badges link off-site and were never followed; nothing was signed into, typed, searched, shared, bought or submitted; the only presses were local UI toggles - the detail pages' Share button (its own modal, closed with its X), the plans Monthly/Yearly billing switch, the featured category tabs, 'show more' expanders and the mobile hamburger)
- the signed-in product (Log in, Get started, /join, account surfaces) is a boundary - measured, never entered
- the Applet 'Connect' toggle and any 'Connect' action are the install control - measured at rest, never pressed (installing is an account feature)
- the plan cards' 'Get started' CTAs lead to checkout - measured, never followed
- the search and prompt fields were clicked into for the focus look only, never queried or submitted - result surfaces are uncaptured

## [Sana AI](../systems/sana-ai) — `sana-ai`
Access: signed out (public marketing page plus the email sign-in form; an AgentMail address was typed, the one-time code was not entered, Google was not clicked, and no company SSO was offered)
- Google sign-in is an iframe and was not clicked
- no company SSO was offered
- the sign-in page has no screenshot because a headless shot disagreed with the live dark page

## [Runey](../systems/runey) — `runey`
Access: signed out (public marketing page plus the /auth sign-in and sign-up views; nothing was typed, nothing was submitted, and Google was not followed)
- the product app sits behind sign-in and was not entered
- sign-up asks for a full name as well as email, so nothing was typed and nothing was submitted

## [Wrike](../systems/wrike) — `wrike`
Access: signed out. Public marketing pages and the login email step were measured. Nothing was typed or submitted. Next, Google, Apple, Office, OTP, company SSO, demo, and Contact us were not entered.
- password step, OTP, Google, Apple, Office, and company SSO were not entered
- trial submit, demo request, and Contact us were not followed

## [Coolors](../systems/coolors) — `coolors`
Access: signed in (kaichen@agentmail.to, created in the attached T3 preview browser and confirmed with the emailed color code). Pro checkout was not opened.
- Pro checkout was not opened and was not submitted
- saved palettes and account settings were not walked

## [Copperx](../systems/copperx) — `copperx`
Access: read-only (the marketing site is public; dashboard.copperx.io and payout.copperx.io are authenticated hosts named by the Log in dialog and never opened; no account, payment, KYC or wallet flow was entered)
- dashboard.copperx.io is the payment-gateway account host named by the Log in dialog; it was not opened
- payout.copperx.io is the financial-account host named by the same dialog; wallets, cards, payouts and KYC were not entered
- no account was created and no field was filled
- Contact Sales links to a Google Form and was not submitted
- the site publishes one light theme; no dark theme was captured

## [Hello Klean](../systems/helloklean) — `helloklean`
Access: signed out for every screenshot. A Shopify customer account was created by email code and the empty Orders and Profile pages were opened in the owner's browser; those screens were not saved because the preview host stopped producing frames. Checkout, payment, a filled cart and the Skio portal were not entered. Consent overlays were hidden, never clicked.
- account.helloklean.com Orders and Profile were opened after email-code signup and not saved: the preview host stopped producing screenshot frames. Orders was empty. Profile showed the capture inbox, no address and no payment method
- checkout, payment, a filled cart and address entry were not entered
- the Skio subscription portal at /a/account/login refused the inbox until an order exists

## [Hims](../systems/hims) — `hims`
Access: signed out on the marketing routes; one account created at /customer/login (email and password only) so the care portal shell could be captured. Phone, birthday, payment edit, consultation and clinician chat were not entered. Ketch consent was hidden, never clicked
- https://www.forhims.co.uk/customer/profile: Payment Methods Edit was not opened. No card was added.
- No government ID was requested on the account step. The next medical step was left closed.

## [IKEA](../systems/ikea) — `ikea`
Access: signed out (every captured surface is public on www.ikea.com/sg/en; the global country picker at www.ikea.com was captured as the page ikea.com actually serves; login, signup, the bag, checkout and payment were not entered; Add to cart, Log in and the OneTrust banner were measured or hidden, never activated)
- https://www.ikea.com/sg/en/profile/login/ — the account after Log in, and signup, were not entered. The email field was measured and not submitted.
- https://www.ikea.com/sg/en/cart/ — the bag and checkout were not opened. Add to cart was measured and never pressed. No card was entered.
- https://www.ikea.com/sg/en/favourites/ — the shopping list requires an account and was not opened.

## [Instacart](../systems/instacart) — `instacart`
Access: signed out for every committed screenshot. An email account was created in the attached preview browser and the storefront loaded with ZIP 94105; those frames could not be saved, so the package ships the public capture. No card, street address, or phone number was submitted.
- checkout, payment, order placement and a saved street address were not used
- phone OTP is an alternate login path and was not taken

## [Instagram](../systems/instagram) — `instagram`
Access: signed out (login wall, desktop email signup, password reset, about.instagram.com, help.instagram.com, the locations directory, the privacy center, and the public @instagram profile behind its signup dialog; no field was filled, Submit and Continue were never pressed, Facebook login was never followed, and the phone signup path stops at a mobile-number demand)
- logged-in app (feed, stories, reels, DMs, settings) sits behind sign-in and was never entered
- desktop signup was photographed at rest; Submit was never pressed, so validation, the confirmation code and onboarding were not reached
- Facebook login was not followed
- pressed, loading and error states were not provoked because a press submits

## [LinkedIn](../systems/linkedin) — `linkedin`
Access: signed out (guest home, public jobs search, company page, a published profile, and the user agreement load without a session; the feed, messaging, and Easy Apply sit behind sign-in and were never reached; Sign in, Join now, Apply, Follow, and Message were measured, never followed; the login form was not submitted)
- the feed, messaging, and Easy Apply sit behind sign-in and were never reached; Sign in, Join now, Apply, Follow, and Message were measured, never followed
- the /login form was captured at rest and was not submitted
- Premium redirected to the sign-in wall; the people directory returned an auth wall (HTTP 999)

## [Linktree](../systems/linktree) — `linktree`
Access: signed out (marketing pages and the official public profile load without an account; the login wall was measured and not submitted)
- the product behind sign-in: the editor, dashboard, analytics and billing were never reached; the login wall was measured and not submitted
- no form was submitted and no checkout was followed; the claim field was filled with a throwaway string and cleared, and plan Select buttons were measured but never pressed
- share and OAuth buttons on the public profile and the login wall were measured, never activated

## [Literal.club](../systems/literal) — `literal`
Access: signed out (every captured surface is public; sign-in, register, Want to read, Follow, Like, Comment, import, and supporter checkout were measured or seen and not activated; email and password were not typed)
- https://literal.club/signin: the account after Sign in was not submitted. Sign in with Apple is OAuth and was not activated. Email and password were not typed. Forgot password was not followed.
- https://literal.club/register: account creation was not submitted.
- https://literal.club/book/the-midnight-library-mrpx0: Want to read, Like, and Comment need an account and were not activated.
- https://literal.club/kikimeower: Follow needs an account and was not activated.
- https://literal.club/import/goodreads: Start importing was not submitted. Import needs an account.
- https://literal.club/supporter: checkout and payment were not followed.
- Search results were not loaded because the search form was not submitted.
- The library, writing a review, clubs, goals, messages, and the signed-in dashboard were not opened.

## [Loom](../systems/loom) — `loom`
Access: signed-out public marketing, pricing, legal, the /login wall, and one public share page. SSO, signup Continue, Contact Sales, checkout, and recording were not pressed. No CAPTCHA.
- https://www.loom.com/login is a sign-in wall: SSO and Continue were not pressed, so the library, recorder, and account were not entered
- https://www.loom.com/signup redirects to id.atlassian.com and the form was not submitted
- pricing Try for free, Sign up, and Contact Sales lead to signup or a sales form and were not followed; no checkout was opened
- the library, recording, and workspace settings sit behind sign-in. Phone home and menu shots show a Chrome Google sign-in sheet; Continue on that sheet was not pressed
- the OneTrust cookie banner was hidden and never clicked, so no consent choice was submitted

## [LottieFiles](../systems/lottiefiles) — `lottiefiles`
Access: signed out (the editor, the dashboard and checkout sit behind sign-in and were never opened)
- sign-in, Sign up, Log in and the Google one-tap sheet were seen and not used; the editor and the dashboard were not opened
- checkout and plan upgrade links on pricing go to app.lottiefiles.com and were not followed
- search was focused and not submitted

## [Lovable](../systems/lovable) — `lovable`
Access: signed out (every captured surface is public; the builder was never signed into and no form was submitted)
- the builder behind sign-in was never signed into; Log in, Get started and the docs signup link were measured, never followed
- no form was submitted: the prompt composer, the log-in email field and the enterprise demo form were not submitted, and Continue and the OAuth buttons were never pressed
- checkout was not reached; plan CTAs were measured, never followed, and the credit combobox list was not opened

## [Lulu and Georgia](../systems/luluandgeorgia) — `luluandgeorgia`
Access: signed out (every captured surface is public; account, checkout, add to cart, wishlist, and the Shop sign-in Continue were not entered; the search field and the login email were typed into and cleared)
- https://www.luluandgeorgia.com/account/login redirects to a Shop sign-in on shopify.com. Continue with shop was not clicked. The email field was typed into and cleared. Account creation was not started.
- Add to cart on the product page was measured in hover, focus, and pressed and was not clicked. Checkout was not opened.
- Wishlist, registry, and trade login sit behind an account and were not activated.
- The filter drawer's Apply was not pressed, so no filtered results were submitted.
- The Klaviyo newsletter form was not submitted.

## [Luma](../systems/luma) — `luma`
Access: signed out (marketing pages, Discover, one public event page and the sign-in card are public; the host dashboard, event editor, guest list, check-in, blasts and billing sit behind sign-in and were never reached; registration, ticket purchase and access-code entry were not submitted)
- the host dashboard, event editor, guest list, check-in, blasts and billing sit behind sign-in and were never reached
- /home redirects to sign-in signed out
- /signin was captured as a card and never submitted
- Create Your First Event links to /create, which opens a sign-in dialog, and was never followed
- registration, ticket purchase and access-code entry were not submitted
- Follow and Create Event require sign-in and were never pressed
- Get Luma Plus links to /calendar/manage/plus, which is checkout and was never opened

## [Luma AI](../systems/lumalabs) — `lumalabs`
Access: read-only (home, pricing, about, API, enterprise, Ray, news, MCP, careers, docs and the other public marketing pages are signed out; the app at app.lumalabs.ai redirects to a sign-up host and was not entered; Sign In, Try for free, Start Now, Use the API and the enterprise Submit were measured, never followed; the home prompt was filled and cleared; consent overlays were hidden, never answered)
- https://app.lumalabs.ai redirects to a WorkOS sign-up host. Sign In and Try for free were measured and never followed. Generation, account, billing and API keys sit behind sign-in and were not opened.
- https://lumalabs.ai/pricing Start Now was measured and never followed. Following it is a sign-in and a checkout.
- https://lumalabs.ai/enterprise Submit was hovered and never clicked, so the sales form was not submitted.
- The home prompt was filled and cleared. Submit prompt was measured and never clicked, so no generation was started.

## [Mailchimp](../systems/mailchimp) — `mailchimp`
Access: signed out (the account and campaign builder behind login.mailchimp.com were never reached)
- the signed-in account and campaign builder (audiences, the email designer, automations, reports, billing) need sign-in and were never reached
- signup at https://login.mailchimp.com/signup/ was not started and was not submitted
- the log-in form at https://login.mailchimp.com/ was measured; the username field was typed into and cleared; Log in was never clicked; sign-in was not started
- password reset (Forgot username, Forgot password) is linked from the log-in card and was not followed
- checkout and trial links on https://mailchimp.com/pricing/marketing/ point at /signup/ with a plan query and were measured, never followed; checkout was not started
- Request a demo and Chat with Sales are linked from pricing and were not submitted
- admin.mailchimp.com redirects to the log-in card; the account was never reached
- disabled, error, loading and validation states were not seen because no form was submitted
- the product publishes no dark theme on the public pages; a Tailwind .dark class exists in the sheets and was not painted; the dark token set is empty on purpose
- C5, V1 and V2 are not published by the product

## [Make](../systems/make) — `make`
Access: signed-out public marketing, pricing, templates, integrations, and the make.com/login sign-in wall. Scenarios and the editor sit behind sign-in and were not entered. No form was submitted. No CAPTCHA was passed. No purchase was made.
- make.com/login is a sign-in wall; email and password were focused and not submitted, and scenarios, the editor, Make Grid and account settings were not entered
- Continue with Google and Continue with SSO at https://www.make.com/login start OAuth and were not pressed
- make.com/register shows a CAPTCHA and was not submitted
- Get started on pricing links to register and was not followed into an account
- Talk to sales and Enterprise checkout were not submitted
- Opening a template into the scenario editor requires sign-in and was not done

## [Mangomint](../systems/mangomint) — `mangomint`
Access: signed out (every captured surface is public); the salon admin behind sign-in (calendar, clients, payments, checkout) was never reached; the login, forgot-password, demo and trial forms were measured and typed into then cleared, never submitted; the public booking page loaded signed out with an empty service list and Rebook was not pressed; no slot confirmed, no appointment booked
- the salon admin behind sign-in (calendar, clients, payments, checkout) was never reached; Log In was not submitted
- the login, forgot-password, demo and trial forms were measured and typed into then cleared, never submitted, so validation, error, loading and success states are absent
- the public booking page loaded signed out with an empty service list; Rebook was not pressed, so no slot and no checkout were reached
- no dark theme is painted signed out; the navy login wall is a surface, not a theme toggle

## [Mapbox](../systems/mapbox) — `mapbox`
Access: signed out (marketing, pricing, contact, and public docs). The account console and token creation sit behind sign-in and were never opened. The contact form was not submitted. The OneTrust banner was hidden, never answered.
- the account console, token creation, and Studio sit behind sign-in on account.mapbox.com and were never opened; no token was created
- the contact form was focused and its request-type list was opened, not submitted; checkout was never reached

## [Marathon](../systems/marathon) — `marathon`
Access: signed-out public archive. /sign-in and /register redirect home and were not submitted. Get Started was not used as checkout. No purchase.
- /sign-in redirects to /; the sign-in form was not submitted and no fields painted
- /register redirects to /; registration was not submitted
- Get Started links to /register and was not used as checkout; no purchase, no payment, no billing portal
- Book A Demo embeds SavvyCal and was not submitted
- app.onmarathon.com account, dashboard and workspace are behind sign-in; the agencies page shows a public demo board only

## [MasterClass](../systems/masterclass) — `masterclass`
Access: signed out (every captured surface is public); the member library, lesson player and payment sit behind sign-in or checkout and were never reached; the sign-in form and the find-my-classes quiz were measured empty and not submitted; no trial was started and no plan was bought; the OneTrust consent layer was hidden, never clicked
- the signed-in library, lesson player and account sit behind sign-in and were never reached
- checkout payment and account steps were not opened; the membership picker was viewed only and no plan was purchased
- the sign-in form at /auth/login was measured empty and not submitted
- the find-my-classes quiz was not submitted

## [Medium](../systems/medium) — `medium`
Access: signed out (home, membership, about, blog, one public staff story, plans, the sign-in card and the email step at rest, and the help center are public; Continue, Select, OAuth, Create one and checkout were not pressed; the signed-in home, editor and settings were not entered)
- signed-in home, editor, settings and checkout were not entered
- Continue, Select, OAuth and Create one were not pressed

## [Melius](../systems/melius) — `melius`
Access: signed out (marketing routes, docs.melius.com, and the app.melius.com login and signup cards; nothing submitted; Google, billing and the newsletter were not followed)
- app.melius.com past the login and signup cards was not entered
- Google OAuth was not followed
- the login and signup forms were not submitted; the password field was never filled
- the newsletter and contact forms were not submitted

## [Mercury](../systems/mercury) — `mercury`
Access: signed out (marketing pages, the login boundary at app.mercury.com/login, and the public demo at demo.mercury.com/dashboard; no signup, KYC, payment, or account)
- Sign-in at https://app.mercury.com/login was photographed at rest and with the email field focused. Nothing was typed. Log in, Continue with passkey, Forgot password and Open Account were not followed.
- Signup at https://app.mercury.com/signup, KYC, payments, cards and treasury were not opened.
- The public demo at https://demo.mercury.com/dashboard was photographed. Open account, Move money and the task list were not followed. It is a published demo, not an account.
- The blog search was focused and not submitted.

## [Meta AI](../systems/meta-ai) — `meta-ai`
Access: signed out. The product page at www.meta.ai was read in the T3 preview browser. Log in opened auth.meta.com. The email field was focused and left empty. Continue was not pressed. No message was sent.
- Auth stopped before submit. The flow offers a mobile number, which was not used.
- The product page had no light theme toggle. Light tokens are the auth card only.

## [Missive](../systems/missive) — `missive`
Access: signed-out public marketing and the mail login, signup and SSO screens. No form submitted. No demo booked. No purchase.
- the signed-in inbox was not entered; login, signup and SSO were not submitted
- password reset is not a public route: #forgot, #forgot-password and #reset redirect to login; /forgot is a 404
- Google and Apple sign-in were not clicked
- checkout, card, phone and government ID were not asked for on these routes and were not entered

## [Mocha](../systems/mocha) — `mocha`
Access: signed out. Public docs at docs.getmocha.com. Product hosts on mocha.app return 410. getmocha.com does not resolve. No signup, no login, no payment.
- app, login, auth, dashboard, studio, and build on mocha.app return the same 410 page
- signup is closed; no account was created
- no form was submitted and the search dialog was left empty

## [Modyfi](../systems/modyfi) — `modyfi`
Access: signed out. Live modyfi.com and www.modyfi.com return a Webflow 404. app.modyfi.com does not resolve. Values are from Wayback snapshots of the public pages. Login and signup were not followed.
- the signed-in editor at app.modyfi.com was never opened. Login and Sign up were measured on the marketing nav and not followed
- no payment, phone, or government ID step was reached

## [MoMA](../systems/moma) — `moma`
Access: signed out (every captured surface is public; Tickets, Donate, Join or renew, and Continue were not pressed; the login email was focused and not submitted)
- https://visit.moma.org/select Tickets was not followed. No purchase.
- https://membership.moma.org/ Join or renew and Gift it were measured and not pressed.
- https://www.moma.org/auth/login the email field was focused. Continue was not pressed. A second launch of this URL returned a Cloudflare challenge and that launch stopped.
- Search was opened and not submitted.
- /members/ is a 404. Membership marketing is membership.moma.org.

## [Monarch Money](../systems/monarch-money) — `monarch-money`
Access: signed-out public marketing on www.monarch.com, plus the app.monarch.com/login and /signup walls photographed and not submitted. No account created. No bank linked. No card, phone or government ID entered.
- app.monarch.com/login and /signup were photographed and not submitted; no account, bank link, card, phone or government ID
- Continue with Apple and Continue with Google start OAuth and were not pressed
- the signed-in app (accounts, transactions, budgets, goals, reports, advice, settings) was not entered
- the app stylesheet at static.monarch.com was not resolved on the painted sign-in page (cross-origin CSSOM)

## [monday.com](../systems/monday) — `monday`
Access: signed out (public marketing pages and auth.monday.com login and signup; no account created; forms measured and cleared, never submitted; Google and Microsoft were not followed; the contact form asks for a phone number, so that flow stopped)
- the signed-in workspace (boards, items, automations, dashboards, settings) sits behind login and was never reached
- login and signup at 390px show a desktop-or-app gate, not the form
- nothing was submitted, so validation, error, loading and success states are absent
- Google and Microsoft sign-in were not followed

## [MSCHF](../systems/mschf) — `mschf`
Access: signed out (the host has no account; the index and the Nuxt 404 are public)
- there is no account, no light theme, and no form on this host
- section.subscription is declared and not mounted

## [Mural](../systems/mural) — `mural`
Access: public marketing pages and the signed-out login and signup. No account created. No form submitted.
- the signed-in workspace was not entered
- signup and login were not submitted
- phone auth screenshots failed the viewport dimension check and are full-page 780x1688

## [MWM](../systems/mwm) — `mwm`
Access: signed out (marketing pages are public; console and create were captured at their sign-in screens and not submitted)
- signed-in console and create were not reached; provider buttons and Sign In were not activated

## [MyMind](../systems/mymind) — `mymind`
Access: signed out. Public marketing pages and the access.mymind.com sign-in panel. Google and Apple buttons were not pressed. No email field was present.
- Sign-in is Google and Apple only. The email-only signup the capture rule allows was not on the page, so AgentMail was not used.
- Checkout and plan purchase on /pricing were not opened.

## [Navia](../systems/navia) — `navia`
Access: signed out (home, blog, one article, contact, privacy, and the app.thenavia.com gate are public; contact was not filled; Sign In, Sign Up, Book a demo and checkout were not pressed)
- signed-in app was not entered; Sign In and Sign Up were not pressed
- contact form asks for a phone number and was not filled or submitted

## [New Balance](../systems/new-balance) — `new-balance`
Access: signed out (home, men's listing, one product page, customer care, login form)
- Add to Bag, login, checkout and account creation were not submitted

## [Nextdoor](../systems/nextdoor) — `nextdoor`
Access: signed out; public marketing and the login card only; address verification not entered
- signup and login: forms not submitted

## [Nike](../systems/nike) — `nike`
Access: signed out (every captured surface is public); nike.com redirects to the Singapore storefront
- accounts.nike.com returned Access Denied; sign-in form not measured
- bag, checkout, and member account not entered
- help field border visible but computed width 0

## [Onefinestay](../systems/onefinestay) — `onefinestay`
Access: signed out (public marketing only; enquire was measured empty and not submitted; no booking, card, or account)
- enquire asks for a phone number and was not filled or submitted
- no booking, availability check, account, or payment

## [OneSoil](../systems/onesoil) — `onesoil`
Access: signed out (public marketing and help center; contact form not submitted; app shell empty)
- contact form asks for a phone number and was not submitted; no validation, error, or success state
- app.onesoil.ai returned an empty page; no login form was measured and no account was created

## [Open](../systems/open) — `open`
Access: signed out. Public pages on o-p-e-n.com. Sign-in was opened through the email step and not submitted. No Apple, phone, card, or booking.
- email was not submitted; Apple and phone sign-in were not entered
- no card, credit pack, or booking

## [Orchids](../systems/orchids) — `orchids`
Access: signed out. Public docs at docs.orchids.app. orchids.app and www.orchids.app return a paused Vercel deployment. No signup, no login, no payment.
- orchids.app and www.orchids.app are a paused Vercel deployment, including login, signup, pricing, blog, and careers
- no email was entered and no account was created
- no payment, card, phone, or government ID was requested or given

## [Overflow](../systems/overflow) — `overflow`
Access: signed out (public marketing pages and the signed-out shell at /n/signin and /n/signup; forms were not submitted; Google, SSO, download, subscribe and payment were not entered)
- sign-in and sign-up forms were not submitted; Google and SSO were not clicked
- payment, desktop download and newsletter subscribe were not entered

## [Pastel](../systems/pastel) — `pastel`
Access: signed out (marketing home, plans and features are public; login and signup were measured and not submitted because both ask for a password; SSO, Google, forgot-password and checkout were not entered)
- signed-in dashboard at https://usepastel.com/home was not reached
- login and signup both require a password, so neither form was submitted
- SSO at /sso, Google sign-in, and forgot-password were not entered
- pricing checkout and Contact us were not entered

## [Patreon](../systems/patreon) — `patreon`
Access: signed out (public marketing and the login wall only; no account, no email, no pledge, no card)
- signup wall measured and not submitted

## [Peak Performance](../systems/peak-performance) — `peak-performance`
Access: signed out (home and the women's jackets collection are public; bag, checkout and account were not entered)
- product page, bag, checkout and account were not entered

## [Pedestal](../systems/pedestal) — `pedestal`
Access: signed out on www.pedestal.com; one email-only Shopify Customer Account sign-in, orders empty, no checkout
- checkout, payment, phone, and the contact form were not submitted
- Shopify Customer Account uses a different theme and is not tokenised

## [Perplexity](../systems/perplexity) — `perplexity`
Access: signed out. Product home, hub, pricing, enterprise, terms, and a 404 were read. Sign In was opened. Continue with email, Google, Apple, and SSO were not submitted. No card, phone, or Pro checkout.
- Sign-in was opened and not submitted. The form also offers Google, Apple, and SSO, so the email field was not used.
- Pro checkout, phone, and card were not entered.

## [Pi](../systems/pi) — `pi`
Access: signed out. The greeting chat and the login page were measured. No account was created. OAuth and phone were not entered.
- login offers Google, Apple, Facebook, email and phone. None was entered. Phone and payment were out of scope

## [Pinterest](../systems/pinterest) — `pinterest`
Access: signed out (public marketing and signup wall only; account was not created)
- signup wall observed and not submitted: no account, no login, no Google continue, no birthday entered
- signed-in boards, pins, and account settings not entered

## [Pitch](../systems/pitch) — `pitch`
Access: signed out (public marketing pages plus the auth.pitch.com login form; the email field was focused, nothing was typed, nothing was submitted, and Google, Apple and SSO were not followed)
- the product app sits behind auth.pitch.com and was not entered
- Google, Apple and SSO were not followed
- no email was typed and nothing was submitted, so no error, loading or signed-in state was shown

## [Play](../systems/play) — `play`
Access: signed out (public archive replays only; the live host did not resolve and no account was created)
- signed-out login iframe did not paint

## [Playbook](../systems/playbook) — `playbook`
Access: signed out (public marketing pages plus the /sign-in form; the email field was already focused, nothing was typed, nothing was submitted, and Google and Apple were not followed)
- the product app sits behind sign-in and was not entered
- no email was typed and nothing was submitted, so no error, loading or signed-in state was shown

## [Polar](../systems/polar) — `polar`
Access: signed out. Public marketing and the auth wall only. https://polar.sh/signup redirects to https://polar.sh/auth. The form was not submitted. Google, Apple and GitHub were not followed. No card, bank or KYC step was entered.
- signup wall at https://polar.sh/auth was opened and not submitted
- Google, Apple and GitHub OAuth were not followed
- signed-in dashboard was not opened

## [Pop Site](../systems/pop-site) — `pop-site`
Access: signed out. Public marketing at pop.site plus the signed-out sign-in and sign-up screens at app.pop.site. No form was submitted. Google SSO was not entered. No payment.
- signed-in app was not entered; sign-in asks for a password or Google
- sign-up was not submitted; it asks for email and a password

## [Portrait](../systems/portrait) — `portrait`
Access: public marketing plus email-only signup. Wallet, card, and payment were not entered.
- wallet connect and payment not entered

## [Preply](../systems/preply) — `preply`
Access: signed out (public marketing and login chrome; form not submitted)
- signup not entered: not email-only (student/tutor plus Google, Facebook, Apple, corporate SSO)
- login form not submitted
- no phone, booking, or card
- second headless login load hit Cloudflare; field focus not re-measured

## [Product Hunt](../systems/product-hunt) — `product-hunt`
Access: signed out (public pages only; OAuth login was not entered; the newsletter email form was submitted and the confirmation link did not complete; votes and follows were not clicked)
- https://www.producthunt.com/login is OAuth only (LinkedIn, GitHub, X, Google, Facebook, Apple). None were entered. No email field.

## [Pryzm](../systems/pryzm) — `pryzm`
Access: signed out (public marketing, gallery, lab shell, docs and the sign-in form; account was not created)
- account creation was not submitted
- Google sign-in was not clicked
- checkout was not opened

## [Raus](../systems/raus) — `raus`
Access: signed out (public marketing only; search was not submitted; no booking, card, phone, or account)
- no booking, date selection, account, card, phone, or newsletter signup

## [Relume](../systems/relume) — `relume`
Access: signed out (public marketing and the login page; no email, password, Google, or SSO was entered)
- login form requires a password and offers Google and SSO, so it was not submitted

## [Replo](../systems/replo) — `replo`
Access: signed out. Public marketing pages and the signed-out login form. Nothing typed, nothing submitted.
- login form not submitted and not screenshotted
- payment not entered

## [Resend](../systems/resend) — `resend`
Access: Public marketing and signed-out login and signup. Signup was filled with an email and a password, then cleared, and not submitted. Google and GitHub were not followed. No API key was created. No card was entered.
- signed-in dashboard was not opened
- Google and GitHub on login and signup were not followed
- signup was filled and cleared and not submitted

## [Revolut](../systems/revolut) — `revolut`
Access: signed out. Public marketing pages and the SSO sign-in wall only. The phone field was not filled. No account was created. No card, email, passkey, Google, or Apple flow was started.
- Signup, Create account, phone, email, passkey, Google and Apple were not entered. The SSO wall is the boundary.

## [Ripple](../systems/ripple) — `ripple`
Access: signed out (wallet, account, KYC and the sales form were not entered)
- Wallet connect, sign-in, account creation and KYC were not entered.
- https://ripple.com/contact/sales/ embeds a form from go.ripple.com. It was not filled and not submitted.
- Search was typed into (payments) and not submitted.

## [Rivian](../systems/rivian) — `rivian`
Access: signed out (every captured surface is public); the vehicle builder, reserve, demo-drive booking, trade-in, and account were not entered
- vehicle builder, reserve, demo-drive booking, trade-in, and checkout not entered
- sign-in form measured and not submitted; reCAPTCHA present; no account created

## [Rork](../systems/rork) — `rork`
Access: signed out (public pages and the sign-in dialog; email was not submitted and OAuth was not entered)
- T3 preview browser tools were not registered, so readings are from headless Chrome on public pages

## [ROVR](../systems/rovr) — `rovr`
Access: signed out (public home, moods, schedule, about, privacy, and the /login gate; Google and Apple buttons were not pressed; no email field was on the page)
- /login is Google and Apple only; those buttons were not pressed and /sign-up was not opened

## [SAVEE](../systems/savee) — `savee`
Access: Public marketing and signed-out login. The email field was filled, then cleared, and not submitted. Google and Apple were not followed. No card was entered.
- magic link was not submitted
- Google and Apple on login were not followed
- contact form was not submitted

## [SeatGeek](../systems/seatgeek) — `seatgeek`
Access: signed out (public marketing and browse only; login hit a DataDome interstitial and was not passed; no ticket bought, no card entered, no account created)
- /login is a DataDome interstitial and was not passed
- no ticket purchase, card, phone, or account creation

## [ShareWillow](../systems/sharewillow) — `sharewillow`
Access: signed out. Public marketing and the login form were read. Nothing was typed or submitted. Signup is a six-step password form with reCAPTCHA, so it was not filled in. Phone sign-in, payment, and the signed-in app were not entered.
- No dark theme on the marketing site or the login page.
- Phone sign-in, payment, payroll, and the signed-in app were not entered.
- Login checkbox was already checked. Unchecked fill was not read.

## [Shopify](../systems/shopify) — `shopify`
Access: signed out. Public marketing pages and the account lookup form only. Start for free was not opened (paid trial). Email, password, passkey, Google, Apple, Facebook, and WhatsApp were not submitted. No card, phone, or KYC was entered. No store was created.
- Email, password, passkey, Google, Apple, Facebook, and WhatsApp were not submitted.

## [Shuttle](../systems/shuttle) — `shuttle`
Access: Public marketing and signed-out space, login and signup. Signup and login were not submitted. Both include a Cloudflare Turnstile. No card was entered.
- signup and login were not submitted because both include a Cloudflare Turnstile

## [Skiff](../systems/skiff) — `skiff`
Access: signed-out. The home page is the Notion acquisition notice. Product marketing pages, the whitepaper and the report form were measured. No account was created. The report form was not submitted.
- No account was created. Signed-in Mail, Pages, Drive and Calendar were not entered.
- The report form at https://skiff.com/report was measured empty and not submitted.

## [Skillshare](../systems/skillshare) — `skillshare`
Access: signed out (public marketing and signed-out login chrome only; no membership, card, or email signup was started)
- Sign In opens an in-page sheet. It was not activated. Continue with Google, Facebook, Apple, and email were not clicked. No email was submitted and no card was entered.

## [SoundCloud](../systems/soundcloud) — `soundcloud`
Access: signed out (public listener home, discover, terms, company contact, and the sign-in card; no account, email, or paid plan was started)
- Feed, Library, and Upload ask for an account and were not entered.
- Sign-in Continue, OAuth, and the email field were not submitted. No card, phone, or paid plan was opened.

## [Spyglass](../systems/spyglass) — `spyglass`
Access: signed out. Public marketing pages and the signed-out /sign-in and /sign-up forms. Email was not entered. Google was not clicked. No plan CTA was followed.
- email form not submitted
- Google OAuth not entered
- plan checkout not entered

## [SSENSE](../systems/ssense) — `ssense`
Access: signed out (public marketing and storefront only; login was opened and not submitted; bag, wishlist, and checkout were not entered)
- Add to bag, wishlist, login Continue, bag, and checkout were not entered

## [Stellate](../systems/stellate) — `stellate`
Access: Public marketing and signed-out login and signup. Signup was an email field. Submitting it sent a magic link. The magic link was not opened. GitHub and GitLab were not followed. No card was entered.
- signed-in dashboard was not opened

## [Stocksy](../systems/stocksy) — `stocksy`
Access: signed out. Public browse only. Login, cart, checkout, follow, share and the business request were not submitted.
- Login, signup, cart, checkout, Add to Cart, Follow, Share and the business request were not submitted.

## [Stocktwits](../systems/stocktwits) — `stocktwits`
Access: signed out. Public home, symbol, about, widgets, subscriptions, enterprise, privacy, sign-in and signup were read. No account was created. No password, card, phone, brokerage, or KYC field was filled.
- signup was not submitted, so later account steps were not opened

## [Stripe](../systems/stripe) — `stripe`
Access: signed out (marketing pages, docs.stripe.com, and the login and register walls at dashboard.stripe.com; no signup, KYC, card, or account)
- Sign-in at https://dashboard.stripe.com/login was photographed at rest. Nothing was typed. Sign in, Google, Passkey, SSO and Forgot password were not followed.
- Register at https://dashboard.stripe.com/register was photographed and not submitted. No account was created. No card, bank, phone or government ID was entered.
- The blurred dashboard behind the register card is the wall's backdrop, not a signed-in capture.
- Menus, the country select and the newsletter form were not opened or submitted.

## [Synthesia.io](../systems/synthesia-io) — `synthesia-io`
Access: signed out. Public marketing pages only. Login wall at login.synthesia.io was loaded and not submitted. Book demo was not submitted because it asks for a phone number. No card, no paid plan.
- signup not started: login offers email and Google, and book demo requires a phone number
- no card, checkout, or paid plan

## [Tango](../systems/tango) — `tango`
Access: Public marketing plus signed-out login and signup on app.tango.us. Email was entered. Password, name, Google and Turnstile were not. No card was entered. tango.us was not captured as a separate site.
- signup name form was not submitted

## [The Dinner Ladies](../systems/the-dinner-ladies) — `the-dinner-ladies`
Access: signed out (home, about, the public menu, contact, delivery info and one product page are public; account, checkout, cart, newsletter and the suburb search were not entered)
- no order, no cart open, no email, no phone, no suburb search, no account, no checkout

## [The Leap](../systems/the-leap) — `the-leap`
Access: Public marketing and signed-out login. Signup redirected to login, so no account was created. Google and Thinkific were not followed. No card was entered.
- signup at accounts.theleap.co/signup redirected to login, so AgentMail was not used

## [Threads](../systems/threads) — `threads`
Access: signed out (public home feed, login card, signup dialog, and /login chrome only; no account created, Instagram login not followed, no phone entered, Log in not pressed)
- signup wall not entered: no account, no Instagram login, no phone number, Log in not pressed
- logged-in app (composer, messages, activity, profile, settings) not entered

## [Trip](../systems/trip) — `trip`
Access: signed out (home, hotels landing, customer support, and the email sign-in form are public; the email field was focused and not filled; Search, Continue, Google, Apple, and Facebook were not pressed; no booking, payment, phone, or account was submitted)
- search was not submitted; no results, filters, map, or empty state
- sign-in email was focused only; Continue, Google, Apple, and Facebook were not pressed; no account, phone, card, or code
- no booking, payment, or checkout

## [Tripadvisor](../systems/tripadvisor) — `tripadvisor`
Access: signed out; marketing and search only. Sign in, join, booking, tickets, and payment were not submitted. The join card had no phone field.
- Sign in and Join were opened and not submitted. Continue with Google was not followed. No phone or card field was filled.
- See tickets, Book now, and the hotel search were not submitted.

## [Trulia](../systems/trulia) — `trulia`
Access: signed out (homepage only; listing navigation hit a PerimeterX wall and was not entered)
- sign-in, phone, and agent contact were not entered

## [Uber Eats](../systems/uber-eats) — `uber-eats`
Access: signed out (public marketing only; login, signup, checkout and address entry were not opened)
- login, signup, checkout, phone, card and address entry were not opened

## [Urban Outfitters](../systems/urban-outfitters) — `urban-outfitters`
Access: signed out (public marketing pages and the sign-in dialog only; no phone, email, bag, or card was entered)
- bag, checkout, and payment were not opened

## [Vercel](../systems/vercel) — `vercel`
Access: Public marketing, Geist docs, and signed-out login. Email was not filled. Signup was not submitted. Google, GitHub, ChatGPT, SAML SSO, and Passkey were not followed. No card was entered. No paid team was created. No org SSO was accepted.
- signed-in dashboard was not opened
- signup was not submitted
- Google, GitHub, ChatGPT, SAML SSO, and Passkey were not followed
- no org SSO was accepted

## [Visitors](../systems/visitors) — `visitors`
Access: signed out. Public marketing pages plus /login and /register. The email form was not submitted because a Turnstile field is present. Google and GitHub were not clicked. Trial and checkout were not followed.
- Turnstile on login and register, so the email form was not submitted
- trial and checkout not followed

## [Weekrise](../systems/weekrise) — `weekrise`
Access: signed out (public marketing, academy, privacy, and the login and signup forms; nothing submitted)
- Signed-in app was not entered. Signup asks for a name as well as email, so no account was created.
- Google sign-in was not used.

## [West Elm](../systems/west-elm) — `west-elm`
Access: signed out (homepage, collection, product and the public account email form)
- Did not add to cart, check out, enter a card, or submit the email overlay or the account email form

## [WhatsApp](../systems/whatsapp) — `whatsapp`
Access: signed out (every captured surface is public marketing; web.whatsapp.com was not opened; no phone number was entered; no QR pairing surface was opened; Download and Log in were measured, never followed)
- Download, Log in and the Mac app link were measured, never followed

## [Wynde](../systems/wynde) — `wynde`
Access: signed out. Public home, terms, and privacy were measured. Login at app.wynde.io was opened and not submitted. No email, phone, card, or Google SSO was entered.
- email form not submitted
- Google SSO not pressed

## [X](../systems/x) — `x`
Access: signed out (login chrome, a missing-route shell, terms, privacy and about.x.com were read; no email, phone or password was typed; Continue, Google, Apple, Sign In and Log in were not pressed; no account was created and nothing was posted)
- preview_snapshot failed twice: The browser is not producing screenshot frames. Login, missing-route and about screenshots were not invented
- no email, phone, username or password was typed; Continue, Google, Apple, Sign In and Log in were not pressed

## [Xbox](../systems/xbox) — `xbox`
Access: signed out (home, games, consoles, Game Pass, search, and one product page are public; Sign in, cart, BUY, and JOIN GAME PASS were not followed)
- Sign in, Microsoft account, cart, checkout, and JOIN GAME PASS subscription form were not entered

## [Yelp](../systems/yelp) — `yelp`
Access: signed out. Homepage, public search, one business page, about, the login form (not submitted) and a 404. No password, name, ZIP, phone, card or reservation was entered.
- signup and login not submitted: the form asks for a password, a name and a ZIP

## [ZARA](../systems/zara) — `zara`
Access: signed out (location gate and US storefront, new arrivals, one product page, search, help, empty bag, logon form measured and not submitted, a made-up 404; nothing added to the bag)
- add to bag, checkout, card, phone, address, and account creation were not entered
- the logon email field was not submitted

## [Zara Home](../systems/zara-home) — `zara-home`
Access: signed out (worldwide market gate, International homepage, category, product, search, error page)
- Did not add to bag, check out, enter a card, phone or address, or create an account

## [Zellerfeld](../systems/zellerfeld) — `zellerfeld`
Access: signed out (public store, product, FAQ, reviews, creators, newsletter, policies, and the sign-in card; no purchase, size, card, phone, or email was entered)
- checkout, size selection, card, phone, Google sign-in, sign-up, and newsletter submit were not entered

## [Zendesk](../systems/zendesk) — `zendesk`
Access: signed out (www.zendesk.com marketing, /login, /pricing, /contact, /demo step 1, /register first step, support.zendesk.com/hc/en-us, and garden.zendesk.com as a separate site screenshot). No email was typed. No form was submitted. No card, phone, or company SSO was entered. The agent workspace was not opened.
- the signed-in agent workspace was not entered
- register, contact, login and demo forms were not submitted; no email was typed
- no card, phone number, or company SSO was entered
- the register error message text colour was not isolated from a script node
- the secondary View demo ring was visible in a screenshot and not isolated in computed style (border width 0)

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

### [Rows](../systems/rows) — `rows`
public marketing, signed out. Login and signup routes on rows.com 404. The Superhuman Docs handoff is company SSO plus email behind reCAPTCHA and was not entered.

### [ResearchRabbit](../systems/researchrabbit) — `researchrabbit`
signed in

### [Sentry](../systems/sentry) — `sentry`
signed-in owner account; Developer plan observed; no trial activated

### [Spotify](../systems/spotify) — `spotify`
signed in, Premium Family plan, iPhone Mirroring

### [Square](../systems/square) — `square`
signed out (marketing pages and the login email step were measured; nothing was typed or submitted; the signup wall was recorded and not entered)

### [Substack](../systems/substack) — `substack`
signed in, iPhone Mirroring

### [Supabase](../systems/supabase) — `supabase`
signed in, free account; both projects paused; public landing

### [Superset (desktop)](../systems/superset-desktop) — `superset-desktop`
signed in (the owner's organisation on the free plan); read live from the running app over its remote-debugging port

### [Teenage Engineering](../systems/teenage-engineering) — `teenage-engineering`
signed out (public marketing and store listing only; checkout, cart, and payment were not entered)

### [Telegram](../systems/telegram) — `telegram`
signed in, iPhone Mirroring

### [Tella](../systems/tella) — `tella`
signed out (marketing pages and the AuthKit sign-in; the email was not submitted)

### [TokenTracker](../systems/tokentracker) — `tokentracker`
local dashboard served by the TokenTracker CLI (v1.4.3), no account, headless Chromium

### [Typefully](../systems/typefully) — `typefully`
signed out (public marketing and the email dialog; the form was not submitted)

### [Untitled](../systems/untitled-stream) — `untitled-stream`
signed out (every surface captured is public; the app behind login was not captured)

### [YouTube](../systems/youtube) — `youtube`
signed in, free plan, iPhone Mirroring

### [Zed (desktop)](../systems/zed-desktop) — `zed-desktop`
the owner's signed-in Zed (Free plan) on a scratch folder; colours from Zed's published theme file at the v1.25.2 commit, sizes and type from 2x window pixels

### [Wiza](../systems/wiza) — `wiza`
signed out. Public marketing pages measured. Login was opened and not submitted. Signup hit Cloudflare and was not driven. No phone, card, or company SSO was entered.

### [Whereby](../systems/whereby) — `whereby`
signed out (public marketing and the login form; the email was focused and not submitted)

### [Telescope](../systems/telescope) — `telescope`
signed out (public marketing page and /login; email and Google were not submitted)

### [Slack](../systems/slack) — `slack`
signed out. Public marketing at slack.com/intl/en-sg/ and pricing. Sign-in chrome at slack.com/signin measured and not submitted. Signup, workspace URL, Google, Microsoft, Apple, company SSO and card were not entered.

### [Skyscanner](../systems/skyscanner) — `skyscanner`
signed out. Public marketing and the search form only. Cookie banner dismissed with essential only. Login modal closed. No email, booking, card or phone.

### [The New Yorker](../systems/the-new-yorker) — `the-new-yorker`
signed out (homepage, one article, the public offers page, and the email sign-in step; nothing submitted)

### [Retool](../systems/retool) — `retool`
signed out. Homepage, pricing, login, signup and docs. No email was typed. Signup was not submitted. No demo, SSO, card or database.

### [Clay](../systems/clay) — `clay`
signed out. clay.earth 301s to me.sh. Public marketing pages and the app.me.sh sign-in card were measured. No email was typed. Apple, Google, SSO, Create account, and Sign in with email were not clicked. No phone, card, or CRM import.

### [Contra](../systems/contra) — `contra`
signed out (public marketing and the empty log-in form; sign-up was not submitted)

### [Meiro](../systems/meiro) — `meiro`
signed out (public marketing pages and the signed-out app shell at app.meiro.cc; the builder and checkout were never reached; the email field was focused; a one-character probe was typed and cleared; no form was submitted)

### [Metaview](../systems/metaview) — `metaview`
signed out (marketing is public; sign-in and sign-up were opened and not submitted)

### [Microsoft Copilot](../systems/microsoft-copilot) — `microsoft-copilot`
signed out (copilot.com marketing pages are public; sign-in redirects to a Microsoft account page and was not submitted)

### [Microsoft Teams](../systems/microsoft-teams) — `microsoft-teams`
signed out (the Teams client needs a Microsoft account and was not opened)

### [Miro](../systems/miro) — `miro`
signed-out public marketing, pricing, product, templates, login and signup. Signup rejected the capture inbox. No board created. No purchase.

### [MonoDesk](../systems/monodesk) — `monodesk`
signed out (public marketing pages and app.monodesk.com/login and /create; nothing submitted)

### [n8n](../systems/n8n) — `n8n`
signed out. Marketing pages and app.n8n.cloud login/register. No email was submitted and no workflow was opened.

### [Navan](../systems/navan) — `navan`
signed out. Public marketing pages only. The identifier page was measured and left. No email, signup, SSO, booking or card.

### [Netflix](../systems/netflix) — `netflix`
signed out. Public marketing and login chrome only. No account, no card, no playback.

### [Nothing](../systems/nothing) — `nothing`
read-only public signed-out pages (home, about, nothing-os, phone-4a-pro, support centre). Account login asks for a password and was not entered. Add to bag and contact-support were not submitted.

### [Nudea](../systems/nudea) — `nudea`
signed out (public marketing only; account, checkout, payment and the fitting-room booking were not entered)

### [Officevibe](../systems/officevibe) — `officevibe`
signed out (public Workleap marketing and login.workleap.com; no company workspace, no survey, login and demo forms not submitted)

### [Oku](../systems/oku) — `oku`
public signed-out pages only; sign-in, join and reset were measured and not submitted; pricing Subscribe was not followed

### [OpenSea](../systems/opensea) — `opensea`
signed out (home, collection, activity, discover, drops, tools and terms were public; the connect dialog was opened and closed; no wallet was connected and nothing was submitted). Dark was the live theme. Light is the declared .light pair, resolved on a probe, and was not switched on.

### [Outchat](../systems/outchat) — `outchat`
signed out. Public marketing from a Wayback replay. Login form was a spinner and was not entered

### [PamPam](../systems/pampam) — `pampam`
signed out (home, pricing, about, features, blog, and /login measured; login is a Google button with no email field, so nothing was signed up for; plan buttons were not followed; no card, phone, or government ID was entered)

### [Parallel](../systems/parallel) — `parallel`
signed out (public marketing plus /login and /signup; LinkedIn not clicked; no email submitted; trial not started)

### [Parallel](../systems/parallel-ai) — `parallel-ai`
signed out; public marketing, pricing, docs, and the login form. Email, Google, and SSO were not submitted

### [Partiful](../systems/partiful) — `partiful`
signed out (login is a phone field; no email, no event created)

### [PayPal](../systems/paypal) — `paypal`
signed out (marketing pages and the login email step were measured; nothing was typed or submitted; the signup wall was recorded and not entered)

### [Peerlist](../systems/peerlist) — `peerlist`
signed out (public marketing, jobs, scroll, launchpad, search, login, and signup; signup was not submitted)

### [Pexels](../systems/pexels) — `pexels`
signed out. Public pages on pexels.com. Join and login were opened and not submitted. No card, phone, or download.

### [Pixso](../systems/pixso) — `pixso`
signed out (public marketing and the login form; no account created)

### [PlayStation](../systems/playstation) — `playstation`
signed out (the Sony account form was not entered)

### [Pocket](../systems/pocket) — `pocket`
signed out. The public site is a shutdown notice. No account was created.

### [Polaroid](../systems/polaroid) — `polaroid`
signed out (public marketing and the public log-in page; Continue and Add to Bag were measured and not submitted; no account, card, or phone)

### [Prime Video](../systems/prime-video) — `prime-video`
signed out. Public marketing and login chrome only. No account, no card, no playback.

### [Programa](../systems/programa) — `programa`
signed out (public marketing pages plus the login and register forms; no account was created and no credentials were entered)

### [Promova](../systems/promova) — `promova`
signed out (public marketing and the /sign-up form were measured; the form was not submitted)

### [Prose](../systems/prose) — `prose`
signed out. Public marketing only. The consultation quiz, checkout, and sign-in submission were not entered.

### [Quizlet](../systems/quizlet) — `quizlet`
signed out. Login and signup were opened. No email, password, birthday, phone or card was submitted

### [Rarible](../systems/rarible) — `rarible`
signed out. Public explore, one collection, drops, terms, FAQ, phone nav, search empty state, and the Login dialog. Dialog closed. No wallet, no email submit, no Buy Now, no og.rarible.com, no rwa.rarible.com.

### [Raster](../systems/raster) — `raster`
public signed out. Sign-in was opened and measured (Google and an email-link field). The email was not submitted. Google was not used. No card, phone, or checkout.

### [Reclaim AI](../systems/reclaim-ai) — `reclaim-ai`
signed out. Marketing pages and app.reclaim.ai/login measured. Login is Google, Microsoft, Dropbox and SSO only, so no email signup was attempted and no calendar OAuth was connected. Contact form measured inside its HubSpot iframe and not submitted.

### [Record Club](../systems/record-club) — `record-club`
signed out. Public marketing, browse, releases, one public album page, help, about, supporter pricing, login and register were read and not submitted. Apple and Google were not pressed. Checkout was not opened.

### [Reown](../systems/reown) — `reown`
signed out (marketing, docs, and the sign-in wall; no wallet, no API key)

### [Resume.io](../systems/resume-io) — `resume-io`
signed out (public marketing plus the sign-in email step, not submitted)

### [RevenueCat](../systems/revenuecat) — `revenuecat`
signed out (public marketing and the login/signup pages; no account created)

### [Rise](../systems/rise) — `rise`
signed out (the app shut down on 2025-03-31; login and signup 404)

### [Rive](../systems/rive) — `rive`
signed out (login and signup were measured and not submitted)

### [Riverside](../systems/riverside) — `riverside`
signed out (public marketing and the studio login and register forms; no account created)

### [Robinhood](../systems/robinhood) — `robinhood`
signed out (US marketing and login chrome only; signup stopped at the region search; no account, email, password, card, bank, or KYC)

### [Rox](../systems/rox) — `rox`
signed out (login is Auth0 with Google and Microsoft; no email was submitted)

### [Saint Laurent](../systems/saint-laurent) — `saint-laurent`
signed out; public marketing only; bag, checkout, and account not entered

### [Scale AI](../systems/scale-ai) — `scale-ai`
signed out (public marketing and the signed-out dashboard login; no account created)

### [Shop](../systems/shop) — `shop`
signed out (signup wall opened and not submitted)

### [Sketch](../systems/sketch) — `sketch`
signed out (public marketing and the signed-out sign-in and signup pages; signup was not submitted)

### [Slab](../systems/slab) — `slab`
signed out. Public marketing and the signed-out login page. Register asks for email, full name and password, so it was not submitted. Google signup was not clicked. No company SSO, card, phone or KYC step was entered.

### [Slite](../systems/slite) — `slite`
signed out (home, pricing, features, the sign-in card and the create-account card at rest are public; Google, Apple, Slack, Continue with email, Find your workspaces, Book demo, Get started, Contact Sales and checkout were not pressed)

### [Sonarworks](../systems/sonarworks) — `sonarworks`
signed out (public marketing and the login and signup forms; no account created, no card entered)

### [Soundtrap](../systems/soundtrap) — `soundtrap`
signed out (public marketing and login chrome; OAuth not followed; no card entered)

### [SpatialChat](../systems/spatial-chat) — `spatial-chat`
signed out (marketing home and /pricing measured; login at app.spatial.chat/login measured and not submitted; Buy Now, Stripe trial, Book a Demo, Google, and Apple not followed)

### [Squarespace](../systems/squarespace) — `squarespace`
signed out (public marketing and login chrome; no account, trial, or card)

### [Stable Audio](../systems/stable-audio) — `stable-audio`
signed out (public marketing home, pricing, plugin, terms and a 404 were measured; nav Sign in opened the AuthKit email form, which was focused and not submitted; no signup, Google continue, card, phone, plan checkout, newsletter submit or plugin download)

### [Stage.so](../systems/stage-so) — `stage-so`
public listing only; the Stage product and any login are gone

### [Starbucks](../systems/starbucks) — `starbucks`
signed out (public marketing only; Sign in and Join now were not followed into a form; no card, phone, or payment was entered)

### [Steel](../systems/steel) — `steel`
signed out (public marketing, docs, brand kit, and the email sign-in form; the form was filled and cleared, not submitted)

### [Suno](../systems/suno) — `suno`
signed out. Public home, careers and about were measured. Log in opened a provider dialog and was closed. No email, phone, OAuth, card or paid plan was entered.

### [Super.so](../systems/super-so) — `super-so`
signed out (public marketing plus login and signup chrome; signup was not submitted)

### [Supercut](../systems/supercut) — `supercut`
Public marketing and signed-out login and signup choice pages. Google, email, and SSO were not followed. No card, phone, or company SSO was entered.

### [Superlist](../systems/superlist) — `superlist`
signed out (public marketing plus the Flutter sign-in screen; the magic link was not sent)

### [Teachable](../systems/teachable) — `teachable`
signed out (public marketing pages plus the Teachable Accounts sign-in chrome; no account created, no password typed, no card entered)

### [Teal](../systems/teal) — `teal`
signed out (public marketing plus sign-in and sign-up; nothing submitted)

### [Tesla](../systems/tesla) — `tesla`
signed out, public marketing only (homepage, Model Y, Solar Panels, Support, About). Configurator, shop, and account were not entered

### [The New York Times](../systems/the-new-york-times) — `the-new-york-times`
signed out (homepage, public subscription offer, and email login chrome; no account, no card, no checkout)

### [The Org](../systems/the-org) — `the-org`
signed out (homepage, pricing, about, contact, a public company page, the 404, and the login and signup forms were measured; Google, Microsoft, passkey and SSO were not followed; no email was submitted; no account was created)

### [The Washington Post](../systems/the-washington-post) — `the-washington-post`
signed out (public home, Politics section, one article and the public sign-in card; Subscribe, checkout, OAuth, SSO and the email form were not submitted; no card was entered)

### [The Weather Channel](../systems/the-weather-channel) — `the-weather-channel`
signed out (public forecast and legal pages; login form was not submitted)

### [Tidal](../systems/tidal) — `tidal`
signed out; public player, download page and OAuth login chrome; no plan, card or OAuth continue

### [TikTok](../systems/tiktok) — `tiktok`
signed out. Public marketing and login chrome only. No account, no phone, no email.

### [Tilda](../systems/tilda) — `tilda`
public marketing site and signed-out login, measured in the T3 preview browser; login not submitted

### [Time2book](../systems/time2book) — `time2book`
signed out (public marketing and the email login form; no account created)

### [Todoist](../systems/todoist) — `todoist`
signed out (public marketing and the login form; signup was not submitted)

### [TravelPerk](../systems/travelperk) — `travelperk`
signed out. Public marketing pages only. travelperk.com redirected to perk.com. The login page was measured and left. No email, signup, SSO, booking or card.

### [TwelveLabs](../systems/twelvelabs) — `twelvelabs`
Public marketing plus signed-out login on auth.twelvelabs.io. Email was entered. Password was not typed. Google was not followed. HubSpot contact form and reCAPTCHA were not filled. No card was entered. No API key was created.

### [Twist](../systems/twist) — `twist`
signed out. Public home, pricing, and Why async measured. /login email field filled with an AgentMail address and submitted; the name and password step was not filled. Google, Apple, the Typeform waitlist, and checkout were not opened.

### [Twitch](../systems/twitch) — `twitch`
signed out (public home, directory, and signup wall; no account created)

### [Typeform](../systems/typeform) — `typeform`
signed out (marketing pages and the login; the email was not submitted)

### [Uber](../systems/uber) — `uber`
signed out (US ride, about, business, and drive pages measured; signup wall at auth.uber.com/v2 measured and not entered; no phone, email, card, or ride)

### [Understory](../systems/understory) — `understory`
signed out (public marketing and the backoffice login; signup was opened and not submitted)

### [Variant](../systems/variant) — `variant`
signed out. Homepage, /authentication and /terms-and-privacy measured. Email field typed only to read the enabled button, then cleared. Not submitted. Google sign-in not clicked. No payment.

### [Vectary](../systems/vectary) — `vectary`
signed out (login and signup were opened and not submitted)

### [Vevo](../systems/vevo) — `vevo`
signed out (public marketing site; no account, phone or card)

### [Vimeo](../systems/vimeo) — `vimeo`
signed out (marketing, watch feed, pricing, and the login dialog; no account created)

### [Visual Electric](../systems/visual-electric) — `visual-electric`
signed out (archived public pages; the live apex has no DNS and the login host returned Cloudflare 1014)

### [Vivid Money](../systems/vivid-money) — `vivid-money`
signed out (public marketing and the business login chrome; no email, phone, card or KYC was entered)

### [Voicenotes](../systems/voicenotes) — `voicenotes`
signed out. Login modal opened. Email and password fields were not submitted.

### [Volkshotel](../systems/volkshotel) — `volkshotel`
signed out (public marketing only; booking, gift card and the newsletter iframe were not entered)

### [VSCO](../systems/vsco) — `vsco`
signed out (public marketing and the login form; nothing submitted)

### [Walmart](../systems/walmart) — `walmart`
signed out (public marketing only; Sign in was not followed; no card, phone, or address was entered)

### [Wealthsimple](../systems/wealthsimple) — `wealthsimple`
signed out (Canada marketing and login chrome only; signup stopped at preferred name, email, and password; no account, email, password, card, bank, or KYC)

### [Weavy](../systems/weavy) — `weavy`
signed out (public marketing at weave.figma.com, the redirect from weavy.ai, plus app.weavy.ai/signin; SSO buttons were not clicked)

### [Webflow](../systems/webflow) — `webflow`
signed out (login and signup were not entered; /login is a PerimeterX hold page)

### [Weights & Biases](../systems/weights-biases) — `weights-biases`
signed out. Marketing home and privately hosted pricing were public. Forge login and signup were measured and not submitted. Signup offers Google, GitHub and Microsoft as well as email, so no account was created. No card, plan, or API key was entered.

### [Windy](../systems/windy) — `windy`
signed out (login asks for email and password plus Google, Apple, and Facebook; nothing was entered)

### [Wise](../systems/wise) — `wise`
signed out. Public marketing pages and the login wall only. Email and password fields were left empty. No account, phone, card, bank details, or KYC was entered. No transfer was started. Google, Facebook, Apple, and passkey were not clicked.

### [Wix](../systems/wix) — `wix`
signed out (homepage, pricing, and the email login; the form was not submitted)

### [Womp](../systems/womp) — `womp`
signed out (public marketing pages, the auth card, and a public print preview; the editor was never reached)

### [Workflow](../systems/workflow) — `workflow`
signed out (marketing home, features, pricing, contact; login rendered a spinner; no account created)

### [Zapier](../systems/zapier) — `zapier`
signed out. Home, pricing, login and signup were measured. Signup was not submitted. SSO was not followed.

## No gated surface recorded

`ableton`, `allbirds`, `anam`, `attio`, `gauth`, `raycast-desktop`, `refero-design`, `sora`, `sunsama`, `wittl`, `memotron`, `nomad-goods`, `on`, `ozone`, `pattern-brands`, `runway`, `savvycal`, `seed`, `spline`, `tidycal`, `unsplash`
