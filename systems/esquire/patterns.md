# Esquire patterns

How the components in [components.md](components.md) combine on each captured surface. Everything below is the public, signed-out surface of esquire.com painted in its single light theme; read exact values from [tokens.json](tokens.json).

## Chrome that wraps every page

- **Red utility strip (32px):** edition switcher (US) on the left, Newsletter on the right. On the phone it collapses to Newsletter / Subscribe.
- **Main bar (~75px):** 211px search field (left), the 296px Esquire wordmark (centre), Sign In + red Subscribe pill (right). On the phone this is hamburger + wordmark + search icon.
- **Category strip (.megaMenu, ~53px):** Entertainment · What to Buy · Style · Lifestyle · News and Politics · Video · Food and Drinks · More. Per-item chevron buttons open subsection flyouts; the More toggle drops the overflow panel (Sports, Member Exclusives, For You). On the phone the same sections become a horizontally scrolling link strip; full subsections live in the side panel.
- **Side panel (nav#sidepanel):** the hamburger's drawer — Subscribe + My Bookmarks, the full section list with per-section accordion chevrons, social row and the footer menu clone; closes on its own Close button or Escape. Hidden until toggled; its links were never followed.
- **Footer:** wordmark + social icon buttons, the Newsletter/About Us/Media Kit/Press Room/Contact Us link columns, then the Hearst legal line ("A Part of Hearst Digital Media", commission disclosure, © Hearst Magazine Media).

## Home

`[screenshots/home-light-*]`

The 32px strip + bar + megamenu sit over a leaderboard ad slot (blank — ad requests aborted) and the content column:

1. **The Latest** — left rail: 80px-thumbnail story rows (18px Lausanne headline, BY-line, "N min read"), ~46px row height per line of title.
2. **Cover hero** — centre column: 56px PlayFair headline over a lede paragraph, photo above; the one story painted at display size.
3. **MAN AT HIS BEST rail** — right column: repeated eyebrow + 20px headline + 14px muted dek + thumbnail cards.
4. Then stacked **section bands** — Most Read, Entertainment, Watches, Politics With Charles P. Pierce, Our Cover Stars, The Endorsement, "For Our Premium Subscribers Only:", Food & Drinks, Esquire Classics — each a 32px Lausanne h2 over its own card grid; premium-only cards carry the lock treatment.
5. **Newsletter band** — the 846px block ("Real journalism and real style, direct to your inbox daily." 28px) with the email field, red Sign Up button and the terms microcopy. The same band appears mid-feed; a second instance closes the page.
6. **Pagination** — the 1 | 2 | 3 strip at the foot of the story feed.

## Section front (Style, Entertainment, News & Politics, Food & Drinks)

`[screenshots/style-light-*, entertainment-light-*, politics-light-*, food-light-*]`

- Section title (PlayFair, ~64px on Style's 205x85 box) + a muted standfirst describing the desk.
- A lead story block, then the standard card grid — eyebrow over 40px-Lausanne titles with muted deks and byline/readtime rows, thumbnails above.
- **"Advertisement - Continue Reading Below"** furniture at intervals down the page, each over a blank slot (requests aborted).
- Ends on the red-outline **See More** ghost button (~101x38), newsletter band, footer.

## Article (cover interview)

`[screenshots/article-light-*, essay-light-*, mobile-article-light-*]`

- **RELATED strip** pinned under the chrome: the RELATED bullet + outlined pill links to sibling stories.
- Full-bleed hero photograph with the caption/credit row (Lora ~16px).
- Content header: breadcrumb (Entertainment › Movies) → PlayFair headline (64px on the interview) → Lausanne standfirst (~21px muted) → byline row with the author's photo and "By <name>" link.
- The ~628px text column: lede paragraph with a painted drop cap, Lora 18px body, inline links, mid-story block headings ("readers also read" + card rows), pull quotes, the Advertisement furniture between blocks.
- Tail: related-story cards, newsletter band, footer.
- The phone article runs 56,109px and was captured to the kit's 8-chunk bound (the boundary is recorded on the shot's sidecar); desktop fit at 37,921px.

## Membership offers (/offers/premium-membership/)

`[screenshots/offers-light-*]`

- "The only place you'll find real journalism and real style" strap → **Choose a Plan**.
- Three **plan cards** (~390px): Premium $50/year flagged **Best Value**, Print + Digital $30/year, Digital Only $25/year — struck list price in #cc2828 over the current price, a perk list with green #088153 checks (included) vs #575757 dashes (excluded), and a red **Join** pill each. Never pressed — they leave for checkout on shop.esquire.com.
- "Cancel anytime…" fine print, the **Compare** table (features × plan columns of checks), **Membership Perks** icon grid, the **FAQ accordion** (56px collapsible-header-button rows), and the red-outline **GIVE A GIFT SUBSCRIPTION** CTA.

## Premium hub (/esq-premium-exclusive/)

`[screenshots/premium-light-*]`

- A hub front in the same grid language as the section fronts, carrying member-exclusive stories (locked/registered variants are labelled in-page); measured at rest, gated interiors not opened.

## Search (/search/?q=suits)

`[screenshots/search-light-*]`

- The 1115x48 results-page search field with the round red submit; "1857 results for keyword suits" count; the **Sort By: Relevance** popover trigger (measured, not opened).
- Result cards: thumbnail over eyebrow + 40px-Lausanne title + muted dek + byline row; **See More** ghost button at the foot.

## About

`[screenshots/about-light-*]`

- A text page: About Us heading + paragraphs in the same Lausanne content styles.

## Mobile (390 wide)

`[screenshots/mobile-home-light-*, mobile-style-light-*]`

- ~154px chrome: red strip (Newsletter · Subscribe), bar (hamburger, wordmark, search icon), the horizontally scrolling category strip.
- The feed collapses to single-column story cards (eyebrow → PlayFair headline → dek → BY-line + readtime), the newsletter band and the footer stack vertically.
- The hamburger opens the **side panel** (nav#sidepanel) over the page; Escape or Close dismisses it.

## Boundaries kept honest

- Consent: the OneTrust layer is hidden with CSS/DOM only, never answered.
- Ads/trackers: third-party ad requests aborted; the site's own "Advertisement" furniture stays over the blank slots.
- Purchase/account: Sign In, Subscribe, Join, gift CTA and every story link are shown at rest only.
- Gated stories: premium content past the public lede was not opened.
- The 8-chunk capture bound: only the phone article hit it (56,000px of 56,109px kept).
