# Dribbble patterns

How the measured components combine on dribbble.com's public signed-out
surface, read from the screenshots and the component entries in
[components.md](components.md). dribbble.com paints one light surface in
three CSS eras — the Rails-era mini-master bundle (Mona Sans, hardcoded
values), Vite/Shoelace components with the `--sl-*` token layer re-bound to
the Dribbble pink `#ea4c89`, and Algolia/intl-tel-input vendor styles.
Values are the measured light-set roles unless marked.

## The site header

Every page carries the same chrome
([header](components/crops/header-default.png), `div.site-nav` — 1440 x 92,
transparent on the white page, Mona Sans): the script wordmark
([logo](components/crops/logo-default.png), 89 x 25), a search strip on
feeds, the `Explore`, `Hire Talent`, `Get Hired` and `Community` dropdown
triggers ([nav-trigger](components/crops/nav-trigger-default.png),
Mona Sans 14/30 600 ink `#060318`, 16px side padding), a plain `Sign up`
([signup-link](components/crops/signup-link-default.png), 14/17 700) and
the dark `Log in` pill ([login-btn](components/crops/login-btn-default.png),
89 x 48, ink `#0d0c22` fill, white 14px text, full pill radius, 24px
padding). Hovering `Explore` opens a 230 x 479 white panel
([nav-dropdown](components/crops/nav-dropdown-default.png), 8px radius,
1px `#e7e7e9` @ 0.5 border, `0 15px 50px rgba(27,32,50,.1)` shadow, 24px
padding) listing `Popular`, `New and Noteworthy` and the category links
([menu-link](components/crops/menu-link-default.png), 180 x 32, 14/17 600);
see [home-light-menu](screenshots/home-light-menu.png). Keyboard focus
draws a 2px solid `#f3afe4` pink outline offset 1px on the interactive
items. At 390 wide the header collapses to a 58px bar with the burger
toggle ([m-header](components/crops/m-header-default.png),
[m-menu-button](components/crops/m-menu-button-default.png)), whose own
press opens the 390 x 319 overlay menu
([m-menu-open](components/crops/m-menu-open-default.png),
[mobile-home-light-menu](screenshots/mobile-home-light-menu.png)).

## The home hero and search strip

The home page opens under a `WELCOME20` offer strip
([promo-banner](components/crops/promo-banner-default.png), 1440 x 62,
page content — never clicked): then the hero
([home-light-default](screenshots/home-light-default.png)) pairs a 618 x
125 `Work with the world's best` headline in Mona Sans 52/62.4 600
([hero-title](components/crops/hero-title-default.png)) — one rotating
word paints the pink ([hero-accent](components/crops/hero-accent-default.png),
`#ea4c89`) — with a pink-check bullet list
([hero-check](components/crops/hero-check-default.png)), the dark
`Start Your Project Brief` pill ([hero-cta](components/crops/hero-cta-default.png),
230 x 49, 24px padding, full radius) and the animated designer-work card
beside it ([hero-media](components/crops/hero-media-default.png), 614 x
430). Below, the Shots/Designers/Services segmented control
([view-tab](components/crops/view-tab-default.png), 100 x 40 — a `<label>`,
not a button) sits over the 1234 x 54 `What type of design are you
interested in?` field ([home-search](components/crops/home-search-default.png),
12px radius) with the pink circle Go button
([search-go](components/crops/search-go-default.png), 40 x 40 at 50%
radius) and the popular-tag chips under it
([tag-chip](components/crops/tag-chip-default.png)).

## The shots feed and the sign-up wall

`/shots/popular` ([shots-light-default](screenshots/shots-light-default.png))
leads with the header search field
([search-input](components/crops/search-input-default.png)) and the
`Shots` scope select ([scope-select](components/crops/scope-select-default.png)),
then a grid of shot cards ([shot-card](components/crops/shot-card-default.png),
297 x 255: a thumbnail, then author, like and view counts
[stat-count](components/crops/stat-count-default.png)) — the PRO+ badge
([pro-badge](components/crops/pro-badge-default.png), 40 x 20 dark chip)
rides on selected authors. The signed-out feed is a teaser: after the
first card the page paints a Sign-up-to-continue wall whose dark CTA
([wall-cta](components/crops/wall-cta-default.png)) was measured, never
followed — see the boundary in
[shots-light-full](screenshots/shots-light-full.png). A category strip
([category-tile](components/crops/category-tile-default.png)) and the
`Popular` sort control ([sort-select](components/crops/sort-select-default.png))
bookend the grid.

## The shot detail

A shot page ([shot-light-default](screenshots/shot-light-default.png))
centres the 1024px-wide media figure
([shot-media](components/crops/shot-media-default.png), 8px radius) under
the title row ([shot-detail-title](components/crops/shot-detail-title-default.png))
and the author line: a 48px round avatar
([shot-author](components/crops/shot-author-default.png)), a Follow text
action ([shot-follow](components/crops/shot-follow-default.png)), the dark
hire pill ([shot-cta](components/crops/shot-cta-default.png), 117 x 40)
and a round like/save icon button
([shot-icon-btn](components/crops/shot-icon-btn-default.png), 40 x 40,
white fill, 1px `#e7e7e9` border, 50% radius). The rail carries matching
40px circle controls ([rail-btn](components/crops/rail-btn-default.png)).

## The designer profile and directory

A profile page ([designer-light-default](screenshots/designer-light-default.png))
opens a `profile-masthead`: the 80px avatar
([profile-avatar](components/crops/profile-avatar-default.png)), the name
at 32/38 700 ([profile-name](components/crops/profile-name-default.png)),
the tagline at 48/56 700 up to 600px wide
([profile-headline](components/crops/profile-headline-default.png)), a
`masthead-stats` row of follower counts in muted `#6e6d7a`
([profile-stat](components/crops/profile-stat-default.png), 16px), then
the actions — the dark `Get in touch` pill
([profile-cta](components/crops/profile-cta-default.png), 132 x 48), the
white-bordered `Follow` pill
([profile-follow](components/crops/profile-follow-default.png), 93 x 48,
1px `#e7e7e9` border) and an icon-only round action
([profile-icon-btn](components/crops/profile-icon-btn-default.png), 48 x
48). A Work/Services/Reviews tab bar follows
([profile-tab](components/crops/profile-tab-default.png), pill, `#f8f7f4`
fill when active) with the `Recent Shots` sort
([profile-sort](components/crops/profile-sort-default.png)) over the work
grid ([profile-shot-card](components/crops/profile-shot-card-default.png)).

`/designers` ([designers-light-default](screenshots/designers-light-default.png))
lists freelancer `resume-user-card` rows
([designer-card](components/crops/designer-card-default.png), 1296 x 416,
white, 1px `#f3f3f4` border, 8px radius, 28px padding, a faint
`0 1px 10px rgba(18,22,25,.02)` shadow): name with PRO+/SELECT badge
([designer-name](components/crops/designer-name-default.png),
[badge-select](components/crops/badge-select-default.png)), the star
rating figure ([rating](components/crops/rating-default.png), 14px 600),
meta items ([designer-meta](components/crops/designer-meta-default.png)),
the `Promoted` disclosure in 12px 700 grey
([promoted-tag](components/crops/promoted-tag-default.png)), the dark
contact pill ([designer-cta](components/crops/designer-cta-default.png)),
a round bookmark button
([bookmark-btn](components/crops/bookmark-btn-default.png)), a work strip
and skill chips ([skill-chip](components/crops/skill-chip-default.png),
white pill, 1px `#e7e7e9` border). Topic chips
([topic-chip](components/crops/topic-chip-default.png)) and a filter
select ([filter-select](components/crops/filter-select-default.png)) sit
above the list.

## Jobs, search and stories

`/jobs` ([jobs-light-default](screenshots/jobs-light-default.png)) is the
one serif surface: its h1 sets Source Serif Pro at 72/76 400
([jobs-h1](components/crops/jobs-h1-default.png)). Job rows are 912 x 104
white cards ([job-card](components/crops/job-card-default.png), 1px
`#f1f1f1` border, 8px radius, 24px padding) with the title
([job-title](components/crops/job-title-default.png)), a tag
([job-tag](components/crops/job-tag-default.png)) and a white-bordered
`Apply` pill ([job-apply](components/crops/job-apply-default.png)) —
measured, never followed.

`/search` ([search-light-default](screenshots/search-light-default.png))
leads with a 32/38 700 h1
([search-h1](components/crops/search-h1-default.png)) and description
([search-desc](components/crops/search-desc-default.png)), then the
filter grammar: pill tabs ([filter-tab](components/crops/filter-tab-default.png),
`#f8f7f4` fill), the sort control
([filter-sort](components/crops/filter-sort-default.png)) and a Filters
button ([filters-btn](components/crops/filters-btn-default.png)) over the
shot grid ([grid-shot-card](components/crops/grid-shot-card-default.png)).

`/stories` ([stories-light-default](screenshots/stories-light-default.png))
is editorial: a big display h1
([stories-h1](components/crops/stories-h1-default.png)) over wide article
rows ([story-card](components/crops/story-card-default.png), 809 x 86,
36px/43.2 500 titles at -1.08px tracking) with topic tags
([story-tag](components/crops/story-tag-default.png)).

## Sign up and log in

The auth pages are a split layout — a 400 x 900 painted art panel
([auth-art](components/crops/auth-art-default.png)) beside the form card
([login-card](components/crops/login-card-default.png),
[signup-card](components/crops/signup-card-default.png), the
`auth-layout__content` section, 1024 x 804 at 48px side padding):
`Welcome back` in 24/29 700, the 310 x 47 email field
([email-field](components/crops/email-field-default.png), white, 1px
`#dbda`de @ 0.9 border, 8px radius; the `filled` state typed sample text
and deleted it — nothing was sent), the dark `Continue` pill
([continue-btn](components/crops/continue-btn-default.png), 310 x 48) and
small auth links ([auth-link](components/crops/auth-link-default.png)).
See [login-light-default](screenshots/login-light-default.png) and
[signup-light-default](screenshots/signup-light-default.png). The
Continue-with-Google action is a Google-rendered GSI element — hidden as
a third-party prompt, never answered, so it is a documented gap.

## The footer

Every page ends in the 1440 x 508 footer
([footer](components/crops/footer-default.png)): a horizontally
scrollable row of category cards, then the bottom bar — the script
wordmark, text links ([footer-link](components/crops/footer-link-default.png),
14px 500 ink) and 18px social icons
([social-icon](components/crops/social-icon-default.png)).
