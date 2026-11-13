# DailyArt Magazine patterns

How the measured components combine on dailyartmagazine.com's public
surface, read from the screenshots and the component entries in
[components.md](components.md). Everything paints one theme: a white
editorial field crossed by `#19191c` near-black bands — the top nav, the
home hero and the mid-page donation/long-read sections. Values are from
the single `light` set; there is no theme toggle.

## The chrome: a 65px dark bar over a white mega-menu

Every page sits under the fixed `#19191c` bar
([nav-bar](components/crops/nav-bar-default.png), 1440 x 65): the
DailyArt wordmark ([nav-logo](components/crops/nav-logo-default.png),
111 x 30) centred, `Stories` / `Shop` / `Courses` links in 14px/600 white
Basier ([nav-link](components/crops/nav-link-default.png)) on the left,
social glyphs and the Search ghost button
([search-btn](components/crops/search-btn-default.png), 87.5 x 38 —
transparent with a 1px `#c6002f` border and white text; hover and pressed
fill `#c6002f`). `Shop` and `Courses` are outbound links
([nav-outbound](components/crops/nav-outbound-default.png)) — measured,
never followed. The hamburger
([hamburger](components/crops/hamburger-default.png), 20 x 15) drops the
full-width white mega-menu (1440 x 633 under a
`rgba(0,0,0,.25) 0 16px 48px` shadow — see
[home-light-menu](screenshots/home-light-menu.png)): five link columns
(Art Movements, Art Forms, Regions, Special, Article Types) of 298 x 59
rows in 16px/600 RoslindaleNarrow
([cat-nav-item](components/crops/cat-nav-item-default.png)) on `#2e2e32`
hairlines, with submenu items
([cat-nav-sub](components/crops/cat-nav-sub-opened.png)) painting under a
hovered parent. Keyboard focus draws the browser's dotted outline in the
element's own colour — no custom ring.

## The home hero: a dark magazine cover

The home page opens on a ~799px `#19191c` band
([home-light-default](screenshots/home-light-default.png),
[hero-block](components/crops/hero-block-default.png)): a `FEATURED STORY`
chip ([hero-tag](components/crops/hero-tag-default.png), 93 x 20 —
`#c6002f` fill, 10px/700 white uppercase Basier, flanked by two 41 x 1
`#2e2e32` rules drawn by its ::before/::after) over the 56px/500
RoslindaleCondensed headline
([hero-h1](components/crops/hero-h1-default.png), 900 x 60, white), then a
grid of 275.5 x 292.75 vertical cards
([hero-card](components/crops/hero-card-default.png)) — artwork image,
20px/700 RoslindaleNarrow title, crimson uppercase author line.

## The feed: tabs, horizontal cards, ghost Load more

Below the hero the page turns white. Section headings set at 32px/500
RoslindaleCondensed
([section-heading](components/crops/section-heading-default.png)) beside
28px feed tabs ([feed-tab](components/crops/feed-tab-default.png); the
active tab measures identically — the marker is not a computed-style
difference) and a `Browse all` link
([browse-link](components/crops/browse-link-default.png)). The Latest
list runs 760 x 194 horizontal cards
([post-card-h](components/crops/post-card-h-default.png)): a 260 x 177
thumbnail ([post-card-img](components/crops/post-card-img-default.png)),
a crimson category chip
([post-card-cat](components/crops/post-card-cat-default.png),
119 x 20 — the same chip as the hero tag), a 20px/700 RoslindaleNarrow
title ([post-card-title](components/crops/post-card-title-default.png)),
a #4d5761 excerpt
([post-card-excerpt](components/crops/post-card-excerpt-default.png))
and 15px author/date meta
([post-card-author](components/crops/post-card-author-default.png),
[post-card-date](components/crops/post-card-date-default.png)).
Vertical cards
([post-card-v](components/crops/post-card-v-default.png), 275.5 x 292.75)
fill the rails. The list ends on the 760 x 38 `Load more` ghost button
([load-more](components/crops/load-more-default.png)) — the same
transparent + 1px `#c6002f` border that fills crimson on hover/pressed —
and a 760 x 98 third-party ad slot (`ad-slot` in
[components.md](components.md) — a layout slot only, no crop). Mid-page, a
`#19191c` donation band
([donation](components/crops/donation-default.png), 760 x 385.56)
repeats the hero's dark language.

## The newsletter: inline form and a slide-down modal

Newsletter signups appear three ways, all measured, none submitted: the
inline form ([nl-form](components/crops/nl-form-default.png), 368 x 180)
with a 368 x 40 white email field
([nl-email](components/crops/nl-email-default.png)) — focused and filled
states recorded — a painted 16px checkbox box (white, 1px #989da7, 2px
radius) drawn by the label's ::after over a 13px input at opacity 0
([nl-checkbox](components/crops/nl-checkbox-default.png)) and the 368 x 38
[nl-checkbox](components/crops/nl-checkbox-default.png)) and the 368 x 38
`Send` ghost button
([nl-send](components/crops/nl-send-default.png)); a matching form under
each article
([nl-form-article](components/crops/nl-form-article-default.png)); and
the 720 x 157 top slide-down modal
([nl-modal](components/crops/nl-modal-default.png)) opened with the
site's own `.modal-r--show` class — 16px/21.6 Basier copy on white.

## The article: a 648px column inside a 1152px header

A single post
([article-light-default](screenshots/article-light-default.png)) opens
with a 1152px header row — category chip
([art-cat](components/crops/art-cat-default.png)), 56px/500
RoslindaleCondensed headline
([art-h1](components/crops/art-h1-default.png)) and meta
([art-meta](components/crops/art-meta-default.png)) — then narrows to
the 648px text column: 18px/400 Basier paragraphs in `#4d5761`
([art-para](components/crops/art-para-default.png)) with `#f3003a`
inline links
([art-inline-link](components/crops/art-inline-link-default.png)), 648px
figures ([art-figure](components/crops/art-figure-default.png)) with
captions ([art-caption](components/crops/art-caption-default.png)),
10 x 18 share glyphs
([share-btn](components/crops/share-btn-default.png)), crimson tag chips
([art-tag](components/crops/art-tag-default.png)), the author box
([author-box](components/crops/author-box-default.png)) and 337 x 107
related cards
([related-card](components/crops/related-card-default.png)). The full
page stitches to 16,608px
([article-light-full](screenshots/article-light-full.png)).

## Indexes, about, contact, search

`/latest/` ([latest-light-default](screenshots/latest-light-default.png))
and `/category/art-movements/impressionism/`
([category-light-default](screenshots/category-light-default.png)) reuse
the feed-card layout under a display heading
([latest-h1](components/crops/latest-h1-default.png),
[cat-h1](components/crops/cat-h1-default.png),
[cat-card](components/crops/cat-card-default.png)).
`/about-dailyart-magazine/` sets the same 60px-class heading over a text
column ([about-h1](components/crops/about-h1-default.png)).
`/contact/` runs a 669px Contact Form 7 form
([cf7-form](components/crops/cf7-form-default.png)): half-width 319.5 x 40
name/email fields ([cf7-name](components/crops/cf7-name-default.png)),
the 669 x 202 message area
([cf7-message](components/crops/cf7-message-default.png)), the acceptance
control — its native input is `visibility:hidden`, the box painted by the
label's ::before ([cf7-accept](components/crops/cf7-accept-default.png))
— and a 669 x 46 black Send with a 1px `#989da7` border
([cf7-send](components/crops/cf7-send-default.png)). All fields were
focused and filled with sample text, then cleared — never submitted.
The search page `/?s=van+gogh`
([search-light-default](screenshots/search-light-default.png)) returns
result cards ([search-card](components/crops/search-card-default.png))
under the display heading.

## The footer

Every page ends on the 842px footer
([footer](components/crops/footer-default.png)): link columns in
`#c6002f` crimson ([footer-link](components/crops/footer-link-default.png))
and 10 x 18 social glyphs
([social-link](components/crops/social-link-default.png)) — outbound,
never followed.

## Mobile at 390

At phone width the bar condenses to the wordmark plus the hamburger
([m-nav-bar](components/crops/m-nav-bar-default.png),
[m-hamburger](components/crops/m-hamburger-default.png)), the menu opens
full-screen
([mobile-home-light-menu](screenshots/mobile-home-light-menu.png)), and
the feed stacks to full-width 366px cards
([m-post-card](components/crops/m-post-card-default.png)) with the
356px newsletter field
([m-nl-email](components/crops/m-nl-email-default.png)).
[mobile-article-light-full](screenshots/mobile-article-light-full.png)
stitches the article to 37,010px under the shooter's cap.
