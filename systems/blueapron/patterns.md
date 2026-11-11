# Blue Apron patterns

How the measured components combine on blog.blueapron.com's public surface,
read from the screenshots and the component entries in
[components.md](components.md). The site paints one light theme over a cream
field; the footer is a dark-bold section style, not a second theme. All values
are from the light set unless noted.

## The promo + header stack

Two bands sit at the top of every page
([home-light-default](screenshots/home-light-default.png)): a 44px navy
`#002856` announcement strip ([announcement-bar](components/crops/announcement-bar-default.png))
carrying the offer copy ("Get $25 off your first 2 orders…") with a white
close on the right, then the cream header ([header](components/crops/header-default.png)):
the navy Blue Apron wordmark ([logo](components/crops/logo-default.png)),
plain-text nav links in Almarai ([nav-link](components/crops/nav-link-default.png))
— Blog · Blue Apron+ · Subscribe & Save — and a 65px `#2959e0` pill
Shop Now CTA ([header-cta](components/crops/header-cta-default.png)). The
nav links point off the blog host at the shop, which is edge-blocked for this
client — measured, never followed.

## The masonry blog grid

The home body is a masonry list of guide cards
([home-light-full](screenshots/home-light-full.png)): each
[blog-card](components/crops/blog-card-default.png) holds a square-cornered
photo ([card-image](components/crops/card-image-default.png)), a category
link ([card-category](components/crops/card-category-default.png)), a blue
serif title link in Ovo ~37px
([card-title](components/crops/card-title-default.png)), a short excerpt in
Almarai ~14px ([card-excerpt](components/crops/card-excerpt-default.png)) and
a date/author meta row ([card-meta](components/crops/card-meta-default.png)),
ending in an older/newer pager
([pagination](components/crops/pagination-default.png)). There are no card
fills — the cream field shows through and type does the grouping. A search
field ([search-field](components/crops/search-field-default.png)) with a 1px
`#aaa` hairline sits above the grid; it was focused and filled, never run.

## The guide page

An article centres a ~66ch column on the same cream field
([article-light-full](screenshots/article-light-full.png)): a small date,
then a large blue `#2959e0` serif headline in Ovo ~68px
([article-title](components/crops/article-title-default.png)), the
author/date meta row ([article-meta](components/crops/article-meta-default.png)),
black Almarai body text ([article-body](components/crops/article-body-default.png))
with blue inline links ([body-link](components/crops/body-link-default.png)),
blue section headings inside the body, and an older/newer guide pager at the
foot ([article-pager](components/crops/article-pager-default.png)). This guide
is text-only — no lede image — and the site mounts no comments, so both specs
are recorded missing.

## The navy footer

Every page ends in a navy `#002856` dark-bold section
([footer](components/crops/footer-default.png)): a white Blue Apron wordmark,
two sitemap columns in blue link text
([footer-link](components/crops/footer-link-default.png)) — Menu · Blue
Apron+ · Autoship & Save · About Us · Gift Cards · Recipes · Careers ·
Affiliates and Help Center & FAQ · Supply Chains Act · Terms · Privacy — a
social icon row ([social-icon](components/crops/social-icon-default.png)) and
a copyright line.

## The mobile menu

At 390 the header collapses to the burger
([m-menu-button](components/crops/m-menu-button-default.png)); its own toggle
opens a full-cream overlay ([mobile-home-light-menu](screenshots/mobile-home-light-menu.png)):
an X close, the centred navy wordmark, large centred nav items
([m-nav-item](components/crops/m-nav-item-default.png)) and the same blue pill
Shop Now CTA at the bottom.

## The cart

`/cart` renders the Squarespace commerce shell — the same header and an empty
cart area ([cart-light-default](screenshots/cart-light-default.png)). Nothing
was ever added; the checkout was never reached.
