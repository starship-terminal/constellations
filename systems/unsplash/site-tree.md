# Unsplash public site tree

Mapped from https://unsplash.com/ on 2026-11-21 in headed Chromium (1440 x 900) before screenshots. Headless Chromium stops on `https://unsplash.com/.within.website` ("Checking your browser before accessing unsplash.com", HTTP 401). Headed Chromium clears that check and loads the public site. No form was submitted. No email was typed. Login and join were opened only to record the wall, then that branch stopped.

OneTrust's Privacy Preference Center is mounted on every page. It was hidden with CSS and never clicked (Allow all, Reject, cookie search, Apply).

## Header (every public page)

| Control | Opens |
|---|---|
| Logo | https://unsplash.com/ |
| Photos | https://unsplash.com/ |
| Illustrations | https://unsplash.com/illustrations |
| Explore (link) | https://unsplash.com/explore |
| Collections (button) | Login wall. Recorded, not followed. |
| Download History (button) | Login wall. Recorded, not followed. |
| Bookmarks (button) | Login wall. Recorded, not followed. |
| Language (button, `aria-haspopup=menu`) | Language menu. Lists Deutsch, English, Español, Français, Bahasa Indonesia, Italiano, 日本語, 한국어 and more. Not switched. |
| Menu (button, `aria-haspopup=dialog`) | Company and product dialog. See below. |
| Search field (`searchKeyword`, placeholder "Search photos and illustrations") | Focus opens a suggestion listbox: trending searches, trending topics, trending collections. Typed text was not submitted. |
| Visual Search (button, `aria-haspopup=dialog`) | Dialog: drop or upload a file, paste an image or link, try an example. No file uploaded. Help link goes to the Help Center article and was not followed as a signed-in flow. |
| Get Unsplash+ | https://unsplash.com/plus (public pricing page) |
| Log in | https://unsplash.com/login (email and password; not submitted; no Google or Apple button seen) |
| Submit an image (button) | Login wall. Recorded, not followed. |

## Menu dialog

Company: About (`/about`), Advertise (`/advertise`), Join the team (`/hiring`), Blog (`/blog`), Press (`/press`), Contact us (`/contact-us`), Help Center (help.unsplash.com, external). Social: Twitter, Facebook, Instagram (external; not captured).

Product: Get Unsplash+ (`/plus`), Developers/API (`/developers`), Unsplash Dataset (`/data`), Unsplash for iOS (App Store, external), Apps & Plugins (`/apps`), Unsplash Studio (`/studio`), Product Placement Ads (`/advertise/product-placement`).

Community: Become a Contributor (`/community`), Collections (`/collections`), Unsplash Awards (`/awards`), Stats (`/stats`).

## Home topic row

Featured (`/`), New Fall (`/t/Fall`), Wallpapers (`/t/wallpapers`), Nature (`/t/nature`), 3D Renders (`/t/3d-renders`), Experimental (`/t/experimental`), Film (`/t/film`), Street Photography (`/t/street-photography`), Architecture (`/t/architecture-interior`), Textures (`/t/textures-patterns`), Travel (`/t/travel`), People (`/t/people`).

A photo card opens `/photos/<slug>`. A collection card opens `/collections/<id>`. A photographer credit opens `/@<handle>` (a public profile). The awards banner opens `/awards/2026/winners`.

## Explore page

The Explore control navigates to `/explore` (it is a link as well as a menu button). The page lists stock landing pages (`/images/stock` and children such as royalty-free, public-domain, creative-commons) and topic searches (`/s/photos/<topic>`). Those search URLs are public result grids. This capture does not submit a typed query. One published topic search is recorded as a reachable public grid.

Footer menu on the explore page: Today (`/today`), Images (`/images`), Backgrounds (`/backgrounds`), Wallpapers (`/wallpapers`).

## Login and join (walls)

| URL | What it shows | Action |
|---|---|---|
| https://unsplash.com/login | Email and password fields, Forgot your password?, Login submit, Join link. No Google button. | Stop. Nothing typed. Nothing submitted. |
| https://unsplash.com/join | Join Unsplash signup. | Stop. No account created. No profile, birthday, plan, survey, or newsletter field filled. |
| https://unsplash.com/users/password/new | Linked as Forgot your password? | Not opened. No reset requested. |

## Public pages captured as the shot list

Home, illustrations, explore, one topic (`/t/nature`), one photo, one collection, plus, about, license, developers, images, login (fields visible, empty). Phone width: home, menu, search focus, photo.

## Not captured (boundary)

Signed-in collections, download history, bookmarks, submit, account settings, downloads that require an account, newsletter signup, language switch, visual-search upload, any form submit, external social and App Store pages, the Help Center host, and every `/s/photos/` grid beyond the one public topic search noted above.
