# Hashnode patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

Two surfaces carry the one system: **hashnode.com** (the app shell — marketing, feed, posts, profiles, product sections) and **townhall.hashnode.com** (the official blog on the hosted blog engine). They share the same custom-property layer — the same names resolve to the same values — while the blog adds prose roles (`--reading-text`, `--code-block`, `--tw-prose-*`).

## The app shell (light by default)

Every hashnode.com page is a viewport-high shell — the document never scrolls; the content panes do. A left **sidebar** (`app-sidebar`, `div[class*="bg-sidebar"]`) carries the wordmark, the primary nav rows (`a.peer/menu-button` — Home, Feed, Hashnode Pro, For Agents, Hackathons, Changelog; the active page paints `--sidebar-accent`), then the utility menu buttons (`button.peer/menu-button`): **Search** with its ⌘K hint, **Theme** opening Light / Dark / System, **More** (with a "New" badge) opening the overflow nav, and **Toggle Sidebar** collapsing the rail to icons. The rail's footer holds the resource links, a **Sign in** link to /login and the solid pill CTA — "Start your blog, free" on `--primary` ink — measured, never followed. On the phone the rail collapses to a header hamburger whose "Open menu" press slides the nav sheet (`m-app-drawer`).

## The feed and the post card

Home and /feed are streams of **post cards** (`post-card`, `article.group/card` rows separated by `--border` hairlines): an author row (avatar + handle link), the title link (hover shifts colour toward the link role), an excerpt in `--muted-foreground`, a cover thumbnail, and the action row — **Upvote**, **comment count**, **bookmark** (`post-upvote`, `post-comments-link`, `post-bookmark`, ghost icon buttons) — plus share. The stream grows on scroll: "Load more" exists but was never pressed (it would extend the stream or need an account), and `-full` screenshots are bounded at eight chunks with the boundary in the sidecar. A **Trending** aside (`feed-trending`) rides beside the column at desktop width.

## The public post and its discussion

/post pages re-cast the card grammar as an article: author header, title, cover, body prose, then the discussion — the **"Share your thoughts"** textarea (`comment-box`, an `--input`-bordered field that lifts the `--ring` focus outline when clicked into — measured, never typed in), its **Comment** submit (measured, never pressed), per-comment **Reply** and **More options** actions, and the share icon button (`post-share`).

## Product sections

- **/pro** is the marketing pattern: plan cards on `--card` with the Pro gold scene palette (`pro.*`, `--pro-button` #e8b543 on `--pro-button-foreground` ink), the "Get Pro" CTA that links to /login, and a **FAQ accordion** (`faq-question`) whose question row expands the answer by its own press — captured `pro-light-faq-open`.
- **/changelog** is a list behind a **category tablist** (`changelog-tablist`): All / Features / Improvements / Fixes / Deprecated `[role="tab"]` rows — activating one is a local toggle that re-filters (captured `changelog-light-tab-features`).
- **/agents** is the install page: the same tablist grammar switches MCP server / Agent skill / CLI snippets (`agents-tab`, captured `agents-light-tab-cli`), each beside a **copy-to-clipboard** icon button (`agents-copy`) — pressed only via forced pseudo-state.
- **/brand** is the palette page: named swatch buttons (`brand-swatch`, the Graphite ramp) that copy values.
- **/onboard** is the one form: text input, combobox, tagline textarea, upload-photo button and a "Next" submit — **measured at rest only**: nothing was typed, no suggestion list fetched, and the submit never pressed.
- **/@handle** is the public profile: a sticky header (avatar, name, Share button) over the sections nav (`profile-header`, `profile-nav`, `profile-share`).

## The ⌘K search dialogs

Both surfaces open a command dialog from their own control — the sidebar **Search** button or Ctrl+K on hashnode.com (`app-search-dialog`, `app-search-input`, `app-search-item`), the header search button on the blog (`th-search-*`). The dialog was opened, its resting suggestion rows measured, and closed with Escape — **no query was ever typed**, so result lists stay uncaptured. The app dialog's dark reading closes the dialog, repaints via the Theme menu, and reopens it.

## The blog engine (townhall.hashnode.com)

The hosted blog paints a sticky **header** (`th-header`, `border-b` over `backdrop-blur`): wordmark, a centred **pill nav** (`th-nav`, `bg-surface` `rounded-full` border links — the "News 📰" section items), the Search ⌘K button, a "Toggle theme" button and the More menu. The index is a column of **post cards** (`th-post-card`: cover thumb, title, excerpt, author + date) ending in "Load more posts" (measured, never pressed) beside the **About the publication** aside (`th-about`); the **archive** page adds `nav[aria-label="Pagination"]` Previous/Next (`th-pagination`, `th-page-prev`). The article page is the prose layer: `h1.text-article-title` (`th-prose-h1`), `h2` sections, `text-reading` body (`th-prose-p`) with `--link` underlined links (`th-prose-link`), fenced **`--code-block` panels** (`th-code-block`, tinted dark in both themes — #15171c on the light page), and a right-rail **"On this page"** table of contents (`th-toc`, `th-toc-link`).

## Mobile (390px)

The app shell compresses to a header bar (`m-app-header`) with the "Open menu" hamburger (`m-app-menu-button`) that opens the nav sheet (`m-app-drawer`), plus search. The blog compresses to its compact header (`m-th-header`).

## Motion and focus

Transitions are the Tailwind defaults — `--default-transition-duration` on `--default-transition-timing-function`, `--ease-in-out`/`-out` curves, `--animate-pulse`/`-spin`/`-ping`/`-bounce` keyframes for loaders and live badges. Hover washes settle inside that window (nav rows, menu buttons, ghost buttons). Focus is a real keyboard focus ring — the `--ring` token (#2962ff light / #6293ff dark) — verified on buttons, links and fields. The reduced-motion probe (`raw/motion.json`) records what `prefers-reduced-motion` changes per page.

## Theme architecture

Both surfaces boot `html.light`. hashnode.com's sidebar **Theme menu** (Light / Dark / System) flips `html.dark` and `.dark`/`:root.dark` re-points the roles — `--background` #ffffff→#0d0f14, `--foreground` #13161c→#e6e8eb, `--brand`/`--link`/`--ring` #2962ff→#6293ff, `--primary` inverts (dark button on white → light button on dark), `--code-block` stays dark (#15171c→#0a0c10), and the scene palettes (`--pro-*`, `--tod-*`, `--landing-*`, `--ai-*`, `--buildful*`) re-point to their dark stops. `--command` is declared under `.dark` only. On the blog engine the same repaint follows `prefers-color-scheme` — its own "Toggle theme" button produced no repaint headless, so blog dark evidence is the OS-preference path, recorded as such.

## The boundary beyond the signed-out surface

This package documents the public product, not the account. **/login** and everything behind it (dashboard, editor, settings) was never entered; **engineering.hashnode.com** answered 429; the docs/help/api/support/blog. subdomains do not resolve; **status.hashnode.com** is a Better Stack page, not the product. Those are boundaries — no pixel, token or component in this package claims to describe them.
