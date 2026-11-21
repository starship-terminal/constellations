# Pryzm public site tree

Mapped 2026-11-21 from https://pryzm.design/ with headless Playwright (Chromium), before screenshots. Official site confirmed: title "Pryzm | Background & Visual Studio for Designers", Vercel, sitemap at https://pryzm.design/sitemap.xml (77 URLs). No password was typed, no email was typed, no form was submitted, and Google was not clicked.

Theme: the public pages paint one dark canvas. `prefers-color-scheme: light` and `dark` were checked later in the capture; no theme switch exists on the public pages.

## Shells

Two shells. Marketing pages share a top nav and a footer. The studio apps share a left rail.

| Shell | Where | Controls |
|---|---|---|
| Marketing nav | `/`, `/blog`, `/about`, `/support`, `/privacy`, `/terms`, and the home `#pricing` anchor | Inspiration, Lab, Pricing, Open studio, Sign in. At 390 px a Menu button opens a dialog. |
| Marketing footer | Same pages | Logo, Studio, Inspiration, Flow, Blog, Pricing, About, Docs, Support, Privacy, Terms, Framer templates (external), X / Twitter (external), Ava Thiery (external), newsletter email plus Subscribe |
| App rail | `/studio`, `/lab`, `/flow`, `/gallery`, `/gallery/<slug>`, `/docs` | Logo, Studio, Lab, Flow, Inspiration, My work, Documentation, Give Feedback (mailto), Collapse / Expand, Sign in |

## Marketing nav (desktop 1440)

| Control | Opens |
|---|---|
| Logo | `/` |
| Inspiration | `/gallery` |
| Lab | `/lab` |
| Pricing | `/#pricing` (same page, pricing section) |
| Open studio | `/studio` |
| Sign in | `/signin?next=<path>` (login wall: email, password, Continue with Google, Sign up, Reset password). Branch stopped. Password was not submitted. |

## Marketing nav (phone 390)

| Control | Opens |
|---|---|
| Menu | Dialog titled Menu: Inspiration, Lab, Pricing, Open studio, Close. Does not navigate until a link is chosen. |
| Sign in | Same login wall as desktop. Branch stopped. |

## Home `/`

| Control | Opens |
|---|---|
| Hero marquee tiles | Not links. Labels only (look name and effect names). |
| Open studio, Try the Studio, Try it in the studio | `/studio` |
| Browse inspiration | `/gallery` |
| Open Flow | `/flow` |
| Look cards (Ink Facet, Undergrowth, Pewter Fade, and the rest of the row) | `/gallery/<slug>` |
| Monthly / Yearly tabs | Same page. Switches the pricing interval. Yearly shows "3 months free". No navigation. |
| Get Pryzm Pro | `/api/checkout?interval=month`, which redirects to a Polar checkout (`polar.sh/checkout/...`). Payment wall. Branch stopped. No form filled. |
| See pricing | `/#pricing` |
| FAQ questions | Same page. Accordions under "Good questions, answered." No navigation. |
| Newsletter email + Subscribe | Form. Not typed, not submitted. |
| Footer links | See Marketing footer. |

## Gallery `/gallery`

| Control | Opens |
|---|---|
| All | `/gallery` |
| Gradient | `/gallery?category=gradient` |
| Photographic | `/gallery?category=photographic` |
| Halftone, Dither, ASCII, Glass, Grain | `/gallery?tag=<Tag>` |
| Look card | `/gallery/<slug>` |
| Load more | `/gallery?page=3` (further pages exist; the index is paged) |
| Collapse | Same page. Rail label changes to Expand. |
| My work | `/my-work`, which redirects to `/signin?next=%2Fmy-work`. Login wall. Branch stopped. |
| Give Feedback | mailto to the product's published support address (external mail). Not opened. |

One representative look page was mapped: `/gallery/ink-facet-280dcf`.

| Control | Opens |
|---|---|
| Gallery | `/gallery` |
| Remix | Dialog: "Pryzm Pro" paywall ("This look uses a Pro gallery asset"). Unlock link goes toward checkout. Branch stopped. No purchase. |
| More looks cards | Other `/gallery/<slug>` pages |

The sitemap lists 46 look pages plus 7 filtered gallery URLs. They share this page. Captured states use one look plus the filters, not all 46.

## Studio `/studio`

Public without an account. Left rail as above, then a canvas and an inspector.

| Control | Opens |
|---|---|
| Effect chips (Gradients, Patterns, Light, Glass, Optics, Blobs, Waves, Pixelate, Dither, Halftone, Plaid, ASCII, Grain) | Same page. Expands that effect's props in the inspector. Grain starts expanded. |
| Image, Pattern, Gradient (layer rows) | Same page. Expands that layer. |
| Randomize, Reset the studio, Animate, Undo, Redo, Full, Square, Portrait (3:4), Landscape (4:3) | Same page. Local canvas state. |
| 1.0× | Menu of animation speeds. |
| More aspect ratios | Dialog: Fill, Square, Landscape ratios, Portrait ratios. |
| Share | Dialog: "Save this look first." Save look is the next step and needs an account. Dialog recorded. Save look not followed into a wall. |
| Save | Account wall if followed through. Not submitted. |
| Export | Dialog: aspect ratios plus "Free PNG export is capped at Preview size". Export button stays inside the dialog. Not submitted. |
| Color picker, hex, numeric props | Fields. Not filled with personal data. |

## Lab `/lab`

Public. Title "Lab: multipass". Stacked layers (Grain, Glass, Gradient by default) plus props.

| Control | Opens |
|---|---|
| Add a layer | Same page. Layer picker (Image, Gradient, effect names). |
| Reorder / Hide / Lock / Delete layer | Same page. Local stack. Delete is a destructive control on a local unsaved layer, not account data. |
| Randomize, Reset the Lab, Animate, aspect buttons, Undo, Redo | Same page. |
| More aspect ratios | Same dialog as Studio. |
| Share | Dialog: "Save this stack first." Not followed into an account save. |
| Export | Same export dialog as Studio. Not submitted. |
| Blend combobox | List of blend modes (Additive is the default). |
| Speed menu | Animation speed. |

## Flow `/flow`

Public node canvas. Default graph: Gradient, Glass, Grain, Base 1.

| Control | Opens |
|---|---|
| Preset chips (Graphite, Sakura Grid, Neon Dream, and the rest) | Same page. Applies a preset to the selected node. |
| Options (per node) | Same page. Expands that node's props. |
| Color stops, Remove color stop | Same page. |
| Add node | Dialog: Base, Image, Pattern, Router, and effect types. |
| Import look | Dialog: "No looks yet. Save one from a base node." Empty state. |
| Import from gallery | Dialog: "IMPORT FROM GALLERY". |
| Embed as code | Dialog: Pro embed sheet (Framer steps). Copy actions not taken. |
| Share | Dialog: "Save this project first." Not followed into an account save. |
| Export | Dialog: "Resolution Preview" and "Unlock Pryzm Pro". Unlock not followed (checkout wall). |
| Save / Save look | Account save. Not submitted. |
| Fill, Animate, speed, zoom, Undo, Redo | Same page. |
| My work (in the canvas chrome) | `/my-work?type=flow`, which redirects to sign-in. Login wall. Branch stopped. |

## Docs `/docs`

| Control | Opens |
|---|---|
| Sidebar section buttons (What is Pryzm?, Quick start, The interface, Inspiration, Flow, Lab, Keyboard shortcuts, layer and effect sections, export, embed, save) | Same page, hash anchors such as `#quick-start`. No navigation off the docs. |
| Open studio | `/studio` |

## Blog

| Control | Opens |
|---|---|
| Tag chips | `/blog/tag/<tag>` (backgrounds, css, dither, effects, export, glass, gradients, inspiration, tutorials) |
| Post cards | `/blog/<slug>` (6 posts in the sitemap) |
| In-post "the studio" / "Open the studio" | `/studio` |
| In-post Subscribe | Newsletter form. Not submitted. |

## Other marketing pages

| Page | Controls beyond the shared shell |
|---|---|
| `/about` | Framer templates (external), Open the studio (`/studio`) |
| `/support` | Read the docs (`/docs`), Read the FAQ (`/#faq`), Email support (mailto). Not opened as a compose window. |
| `/privacy` | External links: Supabase, Polar, Resend, Vercel, Sentry, Ahrefs, DataFast, Google privacy, Google My Ad Center. Not followed. |
| `/terms` | Polar (external), mailto support. Not followed. |

## Auth and payment walls (recorded, then stopped)

| URL | What it asks | Action |
|---|---|---|
| https://pryzm.design/login | 404 "This page was not found". Links: Open studio, Back home. | Known wall. Not a form. |
| https://pryzm.design/signin | Email, password, Continue with Google, Continue, Sign up, Reset password. | Stopped. No email typed. Password not submitted. Google not clicked. |
| https://pryzm.design/my-work | Redirects to `/signin?next=%2Fmy-work`. | Stopped. |
| https://pryzm.design/api/checkout?interval=month | Redirects to Polar checkout for Pryzm Pro. | Stopped. No card, no discount code. |

## External (not captured)

Framer templates, X / Twitter, avathiery.com, mailto links, and the privacy-page vendors. They leave pryzm.design.
