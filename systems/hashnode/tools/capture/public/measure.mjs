// Measures hashnode.com's signed-out components on its public pages, in
// every state that can be reached without signing in or submitting
// anything — plus the matching components on townhall.hashnode.com, the
// official blog on the hosted blog engine (the `th-*` specs).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home feed post profile pro changelog agents brand alt-medium
// onboard th-home th-post th-archive search th-search mobile. Writes
// raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by
// build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 500ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or button can fire
//   dark           the same element after the header's own Theme menu
//                  (Light / Dark / System) repaints html.dark, verified by the
//                  painted surface — setTheme in lib.mjs
//   dark           on th-* pages: prefers-color-scheme emulated + reload —
//                  the signal the blog engine honours; its "Toggle theme"
//                  button produced no repaint headless (lib.mjs setBlogTheme)
//   opened         a resting state reached by the component's own toggle:
//                  the Ctrl+K search dialog, the header's More and Theme
//                  menus, a FAQ accordion, a changelog/agents tab, the
//                  phone's "Open menu" button
//   focused        the comment/search field clicked into — nothing is typed
// Nothing is typed, sent, bought or signed into. The only presses are local
// UI toggles the page's own chrome provides. The /onboard form's fields are
// measured at rest only: nothing is entered and "Next" is never pressed.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, BASE, BLOG, M, open, closePromo, setTheme, setBlogTheme, paintedTheme, styleOf, crop, centre, domFind, patch, UA, UA_MOBILE, RAW } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';
import { toggleBefore, toggleOpen, toggleRestore } from './toggle.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: '/',
  feed: '/feed',
  post: '/posts/i-used-to-be-a-magician/6afadee8cd8f659889f399ed',
  profile: '/@anish78',
  pro: '/pro',
  changelog: '/changelog',
  agents: '/agents',
  brand: '/brand',
  'alt-medium': '/alternatives/medium',
  hackathons: '/hackathons',
  onboard: '/onboard',
  'th-home': { blog: '/' },
  'th-post': { blog: '/why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps' },
  'th-archive': { blog: '/archive' },
};
const urlOf = (key) => typeof URLS[key] === 'string' ? BASE + URLS[key] : BLOG + URLS[key].blog;
const pathOf = (key) => typeof URLS[key] === 'string' ? URLS[key] : URLS[key].blog;
const isBlog = (key) => typeof URLS[key] !== 'string';

let page, cdp, context, current;

// ---------- state drivers ----------

async function reset() {
  // open() leaves the tab on about:blank when a reload was blocked; every
  // state after that fails here, so the saved readings are kept
  if (page.url() === 'about:blank') throw new Error('the page was lost to a blocked reload; saved readings kept');
  await page.keyboard.press('Escape').catch(() => {});
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(300);
}

async function hover(loc) {
  await centre(loc);
  const b = await loc.boundingBox();
  if (b) { await page.mouse.move(b.x + b.width / 2, b.y + b.height / 2); await page.waitForTimeout(600); }
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  await page.waitForTimeout(400);
  // The attempt is only evidence when focus really came back to the element
  // and paints the :focus-visible ring — anything else is a resting reading,
  // recorded under the "focus failed" via rather than claimed as a state.
  return await loc.evaluate((el) => {
    const ae = document.activeElement;
    const held = ae === el || el.contains(ae);
    let ring = false;
    try { ring = Boolean((ae && ae.matches(':focus-visible')) || el.matches(':focus-visible')); } catch { /* unpierceable */ }
    return { held, ring };
  }).catch(() => ({ held: false, ring: false }));
}

// Pick one element out of a selector's matches inside the page — marks the
// winner with data-m-mark="<tag>" and returns a locator for it. score(el, r,
// cs) returns a number, lowest wins; return Infinity to skip a match.
async function pick(p, sel, score, tag = 'pk') {
  const ok = await p.evaluate(([s, t, src]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const fn = new Function('el', 'r', 'cs', `return (${src})(el, r, cs)`);
    let best = null, bestV = Infinity;
    for (const el of document.querySelectorAll(s)) {
      const r = el.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      const cs = getComputedStyle(el);
      if (cs.visibility === 'hidden' || cs.opacity === '0') continue;
      const v = fn(el, r, cs);
      if (v < bestV) { bestV = v; best = el; }
    }
    if (!best) return false;
    best.setAttribute('data-m-mark', t);
    return true;
  }, [sel, tag, score.toString()]);
  return ok ? p.locator(`[data-m-mark="${tag}"]`) : p.locator('[data-m-mark="__none__"]');
}

// CSS.forcePseudoState through CDP: the press never happens, so no link can
// navigate and no button can fire.
async function pressOn(loc) {
  // Force :active:hover on the component element itself, never the topmost
  // node at its centre (a text span or an svg), so the component's own
  // :active rule applies (2026-11 audit, finding 12-6; not run since).
  await cdp.send('DOM.getDocument').catch(() => {});
  await loc.evaluate((el) => el.setAttribute('data-press-target', '1'));
  try {
    const { result } = await cdp.send('Runtime.evaluate', { expression: `document.querySelector('[data-press-target]')`, returnByValue: false });
    // an unresolved target throws, so the state records an error instead of
    // a resting reading labelled pressed
    if (!result || !result.objectId) throw new Error('press target not resolvable');
    const { nodeId } = await cdp.send('DOM.requestNode', { objectId: result.objectId });
    if (!nodeId) throw new Error('press target has no DOM node');
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['active', 'hover'] });
    await page.waitForTimeout(400);
    return nodeId;
  } finally {
    await loc.evaluate((el) => el.removeAttribute('data-press-target')).catch(() => {});
  }
}
const pressOff = (id) => id == null ? null : cdp.send('CSS.forcePseudoState', { nodeId: id, forcedPseudoClasses: [] }).catch(() => {});

// ---------- the component specs ----------
// find: page -> Locator. states: name -> 'hover' | 'focus-visible' |
// 'pressed' | 'dark' | 'opened:label' | (loc, page) => Promise<void>.
const via = { 'hover': 'mouse hover over the element', 'focus-visible': 'keyboard focus (Shift+Tab, Tab)', 'pressed': 'CDP CSS.forcePseudoState(:active:hover) — no real press', 'dark': 'same element after the header Theme menu repaints html.dark', 'darkblog': 'same element after prefers-color-scheme repaints html.dark (the signal the blog engine honours; its own toggle produced no repaint headless)' };

// The shadcn sidebar: .bg-sidebar inside .group.peer.text-sidebar-foreground,
// with nav links and menu buttons as .peer/menu-button.
const SIDEBAR = 'div[class*="bg-sidebar"]';
const MENU_BTN = 'button[class*="peer/menu-button"]';
const MENU_LINK = 'a[class*="peer/menu-button"]';
// The sidebar's open state: the shadcn wrapper's data-state when present,
// else the rail's width (the collapsed rail is 64px), for the toggle restore.
const sidebarState = () => page.evaluate((sel) => {
  const w = document.querySelector('[data-state="expanded"], [data-state="collapsed"]');
  if (w) return w.getAttribute('data-state');
  const s = document.querySelector(sel);
  return s ? (s.getBoundingClientRect().width > 100 ? 'expanded' : 'collapsed') : null;
}, SIDEBAR);

const CHROME = [
  { key: 'app-sidebar', group: 'App chrome', title: 'App sidebar',
    desc: 'The left sidebar (bg-sidebar): logo, Home/Feed/Pro/Agents nav links, the Search / Theme / More menu buttons, sidebar footer with the resource links and the Sign-in link.',
    sel: SIDEBAR, find: (p) => p.locator('div[class~="bg-sidebar"]').first(), states: ['default', 'dark'] },
  { key: 'app-nav-link', group: 'App chrome', title: 'Sidebar nav link',
    desc: 'A primary nav link in the sidebar ("Feed"), a peer/menu-button row.',
    sel: MENU_LINK, find: (p) => p.locator(MENU_LINK).filter({ hasText: /feed/i }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'app-nav-active', group: 'App chrome', title: 'Sidebar active nav link',
    desc: 'The link for the page being read ("Home"), painted with the active style.',
    sel: MENU_LINK, find: (p) => p.locator(MENU_LINK).filter({ hasText: /home/i }).first(), states: ['default'] },
  { key: 'app-sidebar-toggle', group: 'App chrome', title: '"Toggle Sidebar" button',
    desc: 'The sidebar footer control that collapses the rail — a local UI toggle. "opened" is its own press (the rail collapsed), restored afterwards.',
    sel: 'button (text Toggle Sidebar)', find: async (p) => await domFind(p, /toggle sidebar/i, { sel: 'button', tag: 'st', minW: 40 }), states: ['default', 'hover',
      { name: 'opened', via: 'the "Toggle Sidebar" button\'s own press (sidebar collapsed; pressed again to restore)',
        stateOf: sidebarState,
        fn: async (loc) => { await loc.click({ timeout: 4000 }); await page.waitForTimeout(900); },
        restore: async (loc) => { await loc.click({ timeout: 4000 }); await page.waitForTimeout(900); } },
    ] },
  { key: 'app-search-button', group: 'App chrome', title: 'Search button (Ctrl K)',
    desc: 'The sidebar "Search" menu-button carrying the ⌘K hint; opens the command search dialog.',
    sel: `${MENU_BTN} (text Search)`, find: async (p) => await domFind(p, /^search/i, { sel: MENU_BTN, tag: 'sb', minW: 60 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'app-theme-button', group: 'App chrome', title: 'Theme menu button',
    desc: 'The "Theme" menu-button that opens Light / Dark / System. "opened" is its own press; the menu is then closed with Escape.',
    sel: `${MENU_BTN} (text Theme)`, find: async (p) => await domFind(p, /^theme$/i, { sel: MENU_BTN, tag: 'tb', minW: 60 }), states: ['default',
      { name: 'opened', via: 'the "Theme" button\'s own press (menu open; Escape restores)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(900);
      } },
      { name: 'opened-menu', via: 'the open Light / Dark / System menu — Theme pressed, the painted [role="menu"] itself read; reset closes it with Escape', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(900);
        const m = page.locator('[role="menu"], [role="listbox"]').filter({ visible: true }).last();
        return (await m.count()) ? m : null;
      } },
    ] },
  { key: 'app-more-menu', group: 'App chrome', title: '"More" menu button',
    desc: 'The "More" menu-button (carries a "New" badge) opening the overflow nav menu. "opened" is its own press, closed with Escape.',
    sel: `${MENU_BTN} (text More)`, find: async (p) => await domFind(p, /^more/i, { sel: MENU_BTN, tag: 'mm', minW: 50 }), states: ['default', 'hover',
      { name: 'opened', via: 'the "More" button\'s own press (menu open; Escape restores)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(900);
      } },
    ] },
  { key: 'app-cta', group: 'App chrome', title: '"Start your blog, free" CTA',
    desc: 'The solid sign-up call-to-action in the sidebar footer (bg-primary text-primary-foreground, rounded-full). Links to /login — measured, never followed.',
    sel: 'a[href="/login"] (text Start your blog)', find: async (p) => await domFind(p, /start your blog/i, { sel: 'a[href^="/login"]', tag: 'cta', minW: 80 }), states: ['default', 'hover', 'focus-visible', 'pressed', 'dark'] },
  { key: 'app-signin', group: 'App chrome', title: '"Sign in" link',
    desc: 'The quiet sign-in link in the sidebar footer — measured, never followed.',
    sel: 'a[href="/login"] (text Sign in)', find: async (p) => await domFind(p, /^sign in$/i, { sel: 'a[href^="/login"]', tag: 'si', minW: 40 }), states: ['default', 'hover'] },
];

const FEED = [
  { key: 'post-card', group: 'Feed', title: 'Feed post card',
    desc: 'A post row in the feed (article.group/card, border-b separator): author avatar + name, time, title, excerpt, cover thumb, upvote/comments/bookmark actions.',
    sel: 'article', find: (p) => p.locator('article').filter({ visible: true }).first(), states: ['default', 'dark'] },
  { key: 'post-title-link', group: 'Feed', title: 'Post title link',
    desc: 'The post\'s title inside a feed card — the card\'s main link.',
    sel: 'article a (title)', find: async (p) => await pick(p, 'article:first-of-type a', (el) => {
      const href = el.getAttribute('href') || '';
      if (href.startsWith('/@') || href.startsWith('#')) return Infinity;
      const t = (el.innerText || '').trim();
      return t.length >= 8 ? -t.length : Infinity;   // the longest non-author link is the title
    }, 'ptl'), states: ['default', 'hover', 'focus-visible'] },
  { key: 'post-upvote', group: 'Feed', title: 'Upvote button',
    desc: 'The upvote action under a feed card (aria-label "Upvote"): count + arrow icon — measured, never pressed.',
    sel: 'article button[aria-label*="Upvote" i]', find: (p) => p.locator('article button[aria-label*="Upvote" i]').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'post-bookmark', group: 'Feed', title: 'Bookmark icon button',
    desc: 'The bookmark action under a feed card (aria-label "Bookmark this post") — an icon-only ghost button.',
    sel: 'article button[aria-label*="Bookmark" i]', find: (p) => p.locator('article button[aria-label*="Bookmark" i]').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'post-comments-link', group: 'Feed', title: 'Comments link',
    desc: 'The comments-count link under a feed card, pointing at the post\'s discussion page.',
    sel: 'article a[aria-label*="comment" i]', find: (p) => p.locator('article a[aria-label*="comment" i]').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'post-author', group: 'Feed', title: 'Author link + avatar',
    desc: 'The author row on a feed card: avatar image and profile link.',
    sel: 'article a[href^="/@"]', find: (p) => p.locator('article a[href^="/@"]').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'feed-load-more', group: 'Feed', title: '"Load more" button',
    desc: 'The feed\'s pagination button — measured, never pressed (it would grow the stream).',
    sel: 'button[aria-label*="Load more" i]', find: (p) => p.locator('button[aria-label*="Load more" i]').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'feed-trending', group: 'Feed', title: 'Trending aside',
    desc: 'The "Trending" rail beside the feed column (aria-label "Trending").',
    sel: 'aside[aria-label*="Trending" i]', find: (p) => p.locator('aside[aria-label*="Trending" i]').first(), states: ['default'] },
];

const POST = [
  { key: 'comment-box', group: 'Discussion', title: 'Comment textarea',
    desc: 'The "Share your thoughts…" textarea on a discussion page. "focused" is the field clicked into — nothing is typed.',
    sel: 'textarea[placeholder*="Share your thoughts" i]', find: (p) => p.locator('textarea').filter({ visible: true }).first(), states: ['default', 'focused', 'dark'] },
  { key: 'comment-submit', group: 'Discussion', title: '"Comment" button',
    desc: 'The submit under the comment box — measured, never pressed.',
    sel: 'button (text Comment)', find: async (p) => await domFind(p, /^comment$/i, { sel: 'button', tag: 'cm', minW: 50 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'post-share', group: 'Discussion', title: 'Share icon button',
    desc: 'The "Share this post" icon button — measured, never pressed.',
    sel: 'button[aria-label*="Share" i]', find: (p) => p.locator('button[aria-label*="Share" i]').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'post-more-options', group: 'Discussion', title: '"More options" icon button',
    desc: 'The overflow action on a comment row (aria-label "More options") — measured, never pressed.',
    sel: 'button[aria-label*="More options" i]', find: (p) => p.locator('button[aria-label*="More options" i]').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'comment-reply', group: 'Discussion', title: '"Reply" button',
    desc: 'The reply action under a comment — measured, never pressed.',
    sel: 'button (text Reply)', find: async (p) => await domFind(p, /^reply$/i, { sel: 'button', tag: 'rp', minW: 30 }), states: ['default', 'hover'] },
];

const PROFILE = [
  { key: 'profile-header', group: 'Profile', title: 'Profile header',
    desc: 'The sticky profile bar (avatar, name, handle, Share button) above the sections nav.',
    sel: 'header.sticky', find: (p) => p.locator('header').filter({ visible: true }).first(), states: ['default'] },
  { key: 'profile-nav', group: 'Profile', title: 'Profile sections nav',
    desc: 'The "Profile sections" tab-like nav (Posts / Series / …) under the header.',
    sel: 'nav[aria-label*="Profile sections" i]', find: (p) => p.locator('nav[aria-label*="Profile sections" i]').first(), states: ['default'] },
  { key: 'profile-share', group: 'Profile', title: 'Profile "Share" button',
    desc: 'The outlined Share action in the profile header — measured, never pressed.',
    sel: 'button (text Share)', find: async (p) => await domFind(p, /^share$/i, { sel: 'button', tag: 'ps', minW: 50 }), states: ['default', 'hover', 'focus-visible'] },
];

const PRO = [
  { key: 'pro-plan-card', group: 'Pro', title: 'Plan card',
    desc: 'A Pro / Growth pricing card on /pro.',
    sel: 'main box (priced plan)', find: async (p) => await pick(p, 'main div, main section, main article', (el, r) => {
      if (r.width < 200 || r.width > 720) return Infinity;
      const t = el.innerText || '';
      if (!/\$\s*\d/.test(t) || !/mo(?:nth)?\b|year/i.test(t)) return Infinity;
      return el.querySelectorAll('*').length;   // the smallest box holding a price is the card, not the page or a nav link
    }, 'ppc'), states: ['default'] },
  { key: 'pro-cta', group: 'Pro', title: '"Get Pro" CTA',
    desc: 'A plan call-to-action ("Get Pro, $5 a month") — links to /login, measured never followed.',
    sel: 'a (text Get Pro)', find: async (p) => await domFind(p, /get pro/i, { sel: 'a', tag: 'pc', minW: 80 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'faq-question', group: 'Pro', title: 'FAQ accordion question',
    desc: 'A question row in the /pro FAQ accordion. "opened" is its own press revealing the answer.',
    sel: 'button (text What do I get with Pro)', find: async (p) => await domFind(p, /what do i get with pro/i, { sel: 'button', tag: 'fq', minW: 100 }), states: ['default', 'hover', 'focus-visible',
      { name: 'opened', via: 'the question row\'s own press (answer visible; pressed again to close)',
      stateOf: async (loc) => (await loc.getAttribute('aria-expanded')) ?? (await loc.getAttribute('data-state')),
      fn: async (loc) => {
        await loc.click({ timeout: 4000 });
        await page.waitForTimeout(700);
      }, restore: async (loc) => { await loc.click({ timeout: 4000 }); await page.waitForTimeout(700); } },
    ] },
];

const CHANGELOG = [
  { key: 'changelog-tablist', group: 'Changelog', title: 'Category tablist',
    desc: 'The All / Features / Improvements / Fixes / Deprecated tablist.',
    sel: '[role="tablist"], [class*="tabs-list"]', find: (p) => p.locator('[role="tablist"], [class*="tabs-list"]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'changelog-tab', group: 'Changelog', title: 'Category tab',
    desc: 'One category tab. "selected" is the tab\'s own activation — a local UI toggle that re-filters the list.',
    sel: '[role="tab"]', find: (p) => p.locator('[role="tab"]').filter({ hasText: /features/i }).filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible',
      { name: 'selected', via: 'the tab\'s own activation (aria-selected)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(800);
      } },
    ] },
];

const AGENTS = [
  { key: 'agents-tab', group: 'Agents', title: 'Install-method tab',
    desc: 'One of the MCP server / Agent skill / CLI tabs. "selected" is its own activation.',
    sel: '[role="tab"]', find: (p) => p.locator('[role="tab"]').filter({ hasText: /cli/i }).filter({ visible: true }).first(), states: ['default', 'hover',
      { name: 'selected', via: 'the tab\'s own activation (aria-selected)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(800);
      } },
    ] },
  { key: 'agents-copy', group: 'Agents', title: '"Copy to clipboard" button',
    desc: 'The copy icon-button beside an install command — pressed only with forcePseudoState.',
    sel: 'button[aria-label*="Copy" i]', find: (p) => p.locator('button[aria-label*="Copy" i]').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible', 'pressed'] },
];

const ONBOARD = [
  { key: 'onboard-input', group: 'Onboarding form', title: 'Text input (name)',
    desc: 'The "Alex Johnson" placeholder name field — measured at rest; nothing is entered.',
    sel: 'input', find: (p) => p.locator('input').filter({ visible: true }).first(), states: ['default', 'focus-visible', 'dark'] },
  { key: 'onboard-combobox', group: 'Onboarding form', title: 'Combobox (city)',
    desc: 'The "City, Country" location combobox — measured at rest, never opened (it would fetch suggestions).',
    sel: '[role="combobox"]', find: (p) => p.locator('[role="combobox"]').filter({ visible: true }).first(), states: ['default', 'focus-visible'] },
  { key: 'onboard-textarea', group: 'Onboarding form', title: 'Tagline textarea',
    desc: 'The bio/tagline textarea — measured at rest.',
    sel: 'textarea', find: (p) => p.locator('textarea').filter({ visible: true }).first(), states: ['default', 'focus-visible'] },
  { key: 'onboard-upload', group: 'Onboarding form', title: '"Upload photo" button',
    desc: 'The avatar upload control — measured, never pressed (it opens a file dialog).',
    sel: 'button (text Upload photo)', find: async (p) => await domFind(p, /upload photo/i, { sel: 'button', tag: 'up', minW: 60 }), states: ['default', 'hover'] },
  { key: 'onboard-next', group: 'Onboarding form', title: '"Next" button',
    desc: 'The form\'s primary action — measured, never pressed (it would submit).',
    sel: 'button (text Next)', find: async (p) => await domFind(p, /^next$/i, { sel: 'button', tag: 'nx', minW: 50 }), states: ['default', 'hover', 'focus-visible'] },
];

const BRAND = [
  { key: 'brand-swatch', group: 'Brand', title: 'Palette swatch button',
    desc: 'A named colour swatch on /brand (Graphite 500) — a button that copies the value.',
    sel: 'button (text Graphite 500)', find: async (p) => await domFind(p, /graphite 500/i, { sel: 'button', tag: 'sw', minW: 60 }), states: ['default', 'hover'] },
];

// ---- townhall.hashnode.com (the hosted blog engine) ----
const TH_CHROME = [
  { key: 'th-header', group: 'Blog chrome', title: 'Blog header bar',
    desc: 'The sticky blog header (border-b, backdrop blur): wordmark, the pill main nav, Search (Ctrl K) and Toggle theme buttons.',
    sel: 'header', find: (p) => p.locator('header').first(), states: ['default', 'dark'] },
  { key: 'th-nav', group: 'Blog chrome', title: 'Main navigation pill',
    desc: 'The centred pill nav (bg-surface, rounded-full border) holding the publication\'s nav links.',
    sel: 'nav[aria-label="Main navigation"] [class*="rounded-full"]', find: (p) => p.locator('nav[aria-label="Main navigation"] [class*="rounded-full"], nav[aria-label="Main navigation"] [class*="bg-surface"]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'th-nav-link', group: 'Blog chrome', title: 'Nav link',
    desc: 'A nav item in the pill ("News 📰"), hover:bg-background.',
    sel: 'nav[aria-label="Main navigation"] a', find: (p) => p.locator('nav[aria-label="Main navigation"] a').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'th-search-button', group: 'Blog chrome', title: 'Search button (Ctrl K)',
    desc: 'The header search button (aria-label "Open search (press Control or Command and K)") carrying the ⌘K hint.',
    sel: 'button[aria-label*="Open search" i]', find: (p) => p.locator('button[aria-label*="Open search" i]').first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'th-theme-toggle', group: 'Blog chrome', title: '"Toggle theme" button',
    desc: 'The header theme toggle. Pressed headless it produced no repaint and no menu (verified 2026-11-17) — measured at rest and after the prefers-color-scheme repaint, which is how the engine shows dark.',
    sel: 'button[aria-label*="theme" i], button:has-text("Toggle theme")', find: (p) => p.locator('button[aria-label*="theme" i], button:has-text("Toggle theme")').filter({ visible: true }).first(), states: ['default', 'darkblog'] },
  { key: 'th-more-menu', group: 'Blog chrome', title: '"More" menu button',
    desc: 'The header overflow menu. "opened" is its own press, closed with Escape.',
    sel: 'button (text More)', find: async (p) => await domFind(p, /^more$/i, { sel: 'button', tag: 'tm', minW: 40 }), states: ['default', 'hover',
      { name: 'opened', via: 'the "More" button\'s own press (menu open; Escape restores)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(900);
      } },
    ] },
  { key: 'th-about', group: 'Blog chrome', title: 'About-the-publication aside',
    desc: 'The "About the publication" sidebar card on the index.',
    sel: 'aside[aria-label*="About the publication" i]', find: (p) => p.locator('aside[aria-label*="About the publication" i]').first(), states: ['default'] },
  { key: 'th-footer', group: 'Blog chrome', title: 'Blog footer',
    desc: 'The footer (aria-label "Footer") with the publication\'s footer nav and "Powered by Hashnode" link.',
    sel: 'footer', find: (p) => p.locator('footer').first(), states: ['default', 'dark'] },
];

const TH_FEED = [
  { key: 'th-post-card', group: 'Blog feed', title: 'Post card',
    desc: 'A post row on the blog index (li > article): cover thumb, title, excerpt, author + date.',
    sel: 'li article, li[class*="py-5"]', find: (p) => p.locator('main article, main li').filter({ visible: true }).filter({ hasText: /\w{6}/ }).first(), states: ['default', 'dark'] },
  { key: 'th-post-title', group: 'Blog feed', title: 'Post title link',
    desc: 'The title link inside an index card.',
    sel: 'article a, li a', find: (p) => p.locator('main article a, main li a').filter({ visible: true }).filter({ hasText: /\w{8}/ }).first(), states: ['default', 'hover'] },
  { key: 'th-load-more', group: 'Blog feed', title: '"Load more posts" button',
    desc: 'The index pagination button — measured, never pressed.',
    sel: 'button[aria-label*="Load more" i]', find: (p) => p.locator('button[aria-label*="Load more" i]').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
];

const TH_PROSE = [
  { key: 'th-article-header', group: 'Blog prose', title: 'Article header',
    desc: 'The page-frame article header: title (text-article-title), meta, cover.',
    sel: 'header.page-frame, header', find: (p) => p.locator('header.page-frame, main header').filter({ visible: true }).first(), states: ['default', 'dark'] },
  { key: 'th-prose-h1', group: 'Blog prose', title: 'Article title (h1)',
    desc: 'The post title, text-article-title.', sel: 'main h1', find: (p) => p.locator('main h1, h1').first(), states: ['default', 'dark'] },
  { key: 'th-prose-h2', group: 'Blog prose', title: 'Section heading (h2)',
    desc: 'An in-article heading.', sel: 'main h2', find: (p) => p.locator('main h2').filter({ visible: true }).first(), states: ['default'] },
  { key: 'th-prose-p', group: 'Blog prose', title: 'Body paragraph',
    desc: 'A paragraph of article prose (text-reading).', sel: 'main p (sentence)', find: (p) => p.locator('main p').filter({ visible: true }).filter({ hasText: /\S+(\s+\S+){7,}/ }).first(), states: ['default', 'dark'] },
  { key: 'th-prose-link', group: 'Blog prose', title: 'Prose link',
    desc: 'A body-text link inside the article.', sel: 'main p a, main li a', find: (p) => p.locator('main :is(p,li) a').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'th-code-block', group: 'Blog prose', title: 'Code block',
    desc: 'A fenced code block in the article (bg-code-block, tinted dark in both themes).',
    sel: 'main pre, [class*="code"]', find: (p) => p.locator('main pre, main [class*="code-block"]').filter({ visible: true }).first(), states: ['default', 'dark'] },
  { key: 'th-toc', group: 'Blog prose', title: '"On this page" TOC',
    desc: 'The article\'s table-of-contents rail (aria-label "On this page").',
    sel: 'nav[aria-label*="On this page" i]', find: (p) => p.locator('nav[aria-label*="On this page" i]').first(), states: ['default'] },
  { key: 'th-toc-link', group: 'Blog prose', title: 'TOC link',
    desc: 'One entry in the table of contents.', sel: 'nav[aria-label*="On this page" i] a', find: (p) => p.locator('nav[aria-label*="On this page" i] a').filter({ visible: true }).first(), states: ['default', 'hover'] },
];

const TH_ARCHIVE = [
  { key: 'th-pagination', group: 'Blog archive', title: 'Pagination nav',
    desc: 'The archive\'s Previous / Next pagination (aria-label "Pagination").',
    sel: 'nav[aria-label*="Pagination" i]', find: (p) => p.locator('nav[aria-label*="Pagination" i]').first(), states: ['default'] },
  { key: 'th-page-prev', group: 'Blog archive', title: '"Previous" button',
    desc: 'The previous-page control — measured, never pressed.',
    sel: 'button (text Previous)', find: async (p) => await domFind(p, /previous/i, { sel: 'button, a', tag: 'pv', minW: 50 }), states: ['default', 'hover'] },
];

// The Ctrl+K search dialog is measured open: setup() opens it, the specs
// inside read its parts, teardown() closes it.
const SEARCH_SETUP = async (p) => {
  const btn = p.locator('button').filter({ hasText: /search/i }).filter({ visible: true }).first();
  if (await btn.count()) await btn.click({ timeout: 4000 }).catch(() => p.keyboard.press('Control+k'));
  else await p.keyboard.press('Control+k');
  await p.waitForTimeout(1600);
};
const SEARCH_DOWN = async (p) => { await p.keyboard.press('Escape'); await p.waitForTimeout(500); };
const searchSpecs = (prefix, group) => [
  { key: `${prefix}-search-input`, group, title: 'Search input',
    desc: 'The command field in the open dialog; "focused" is the field clicked into — nothing is typed.',
    sel: '[role="dialog"] input, [cmdk-input], input[type="search"]', find: (p) => p.locator('[role="dialog"] input, [cmdk-input], input').filter({ visible: true }).first(), states: ['default', 'focused'] },
  { key: `${prefix}-search-item`, group, title: 'Suggestion row',
    desc: 'A suggestion row in the open menu.',
    sel: '[cmdk-item], [role="option"], [role="dialog"] li', find: (p) => p.locator('[cmdk-item], [role="option"], [role="dialog"] li').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: `${prefix}-search-dialog`, group, title: 'Search dialog',
    desc: 'The ⌘K command dialog, painted by the page\'s own shortcut.',
    sel: '[role="dialog"], [cmdk-root]', find: (p) => p.locator('[role="dialog"], [cmdk-root]').filter({ visible: true }).first(), states: ['default',
      { name: 'dark', via: 'the dialog was closed, the Theme menu repainted html.dark, and the dialog was reopened',
        fn: async () => {
          await page.keyboard.press('Escape');
          await page.waitForTimeout(500);
          if (!(await setTheme(page, 'dark'))) throw new Error('dark never painted');
          await SEARCH_SETUP(page);
        } }] },
];

const MOBILE = [
  { key: 'm-app-header', group: 'App chrome (mobile)', title: 'Mobile header',
    desc: 'The sticky bar at 390px (md:hidden): menu button, logo, search.',
    sel: 'header', find: (p) => p.locator('header').first(), states: ['default'] },
  { key: 'm-app-menu-button', group: 'App chrome (mobile)', title: '"Open menu" button',
    desc: 'The hamburger that opens the nav sheet.',
    sel: 'header button[aria-label*="menu" i]', find: (p) => p.locator('header button[aria-label*="menu" i]').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'm-app-drawer', group: 'App chrome (mobile)', title: 'Nav sheet (open)',
    desc: 'The opened navigation sheet — an overlay panel over the page. The "Open menu" press happens in find().',
    sel: '[role="dialog"], aside', find: async (p) => {
      const ham = p.locator('header button[aria-label*="menu" i]').filter({ visible: true }).first();
      await ham.click({ timeout: 5000 }).catch(() => {});
      await p.waitForTimeout(1300);
      return p.locator('[role="dialog"], aside').filter({ visible: true }).first();
    }, states: [{ name: 'opened', via: 'the "Open menu" button\'s own press', fn: async () => {} }] },
];

const MOBILE_BLOG = [
  { key: 'm-th-header', group: 'Blog chrome (mobile)', title: 'Mobile blog header',
    desc: 'The sticky blog bar at 390px: wordmark, More, search and theme icons.', sel: 'header',
    find: (p) => p.locator('header').first(), states: ['default'] },
];

const GROUPS = {
  home: { page: 'home', specs: [...CHROME, ...FEED.filter((w) => !['feed-load-more','feed-trending'].includes(w.key))] },
  feed: { page: 'feed', specs: FEED.filter((w) => ['feed-load-more','feed-trending'].includes(w.key)) },
  post: { page: 'post', specs: POST },
  profile: { page: 'profile', specs: PROFILE },
  pro: { page: 'pro', specs: PRO },
  changelog: { page: 'changelog', specs: CHANGELOG },
  agents: { page: 'agents', specs: AGENTS },
  onboard: { page: 'onboard', specs: ONBOARD },
  brand: { page: 'brand', specs: BRAND },
  'th-home': { page: 'th-home', specs: [...TH_CHROME, ...TH_FEED] },
  'th-post': { page: 'th-post', specs: TH_PROSE },
  'th-archive': { page: 'th-archive', specs: TH_ARCHIVE },
  search: { page: 'home', setup: SEARCH_SETUP, teardown: SEARCH_DOWN, specs: searchSpecs('app', 'App search') },
  'th-search': { page: 'th-home', setup: SEARCH_SETUP, teardown: SEARCH_DOWN, specs: searchSpecs('th', 'Blog search').map((s) => s.key === 'th-search-dialog' ? { ...s, states: s.states.filter((st) => st === 'default' || (typeof st === 'object' && st.name !== 'dark')) } : s) },
  mobile: { page: 'home', mobile: true, specs: MOBILE },
  'mobile-blog': { page: 'th-home', mobile: true, specs: MOBILE_BLOG },
};

// ---------- runner ----------

const b = await chromium.launch();
context = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
await patch(context);
const mobCtx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
await patch(mobCtx);

const wanted = process.argv.slice(2);
out._meta.read = new Date().toLocaleDateString('en-CA');
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); hashnode.com paints html.light by default and html.dark after the header Theme menu (Light / Dark / System) — `dark` states are measured on the painted dark surface; th-* blog pages paint html.dark on prefers-color-scheme (emulated + reloaded, their own toggle produced no repaint headless)';
out._meta.tool = 'tools/capture/public/measure.mjs';
out._meta.sheets ??= {};

for (const [key, g] of Object.entries(GROUPS)) {
  if (wanted.length && !wanted.includes(key)) continue;
  const ctx = g.mobile ? mobCtx : context;
  page = await ctx.newPage();
  page.setDefaultTimeout(8000);
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  const darkFn = isBlog(g.page) ? setBlogTheme : setTheme;
  const url = urlOf(g.page);
  log('open', key, g.mobile ? '(mobile)' : '', url);
  if (!(await open(page, url, { wait: 7000 }))) { log('  group skipped: the page never loaded'); await page.close().catch(() => {}); continue; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  if (g.setup) await g.setup(page).catch((e) => log('  setup failed:', e.message));
  // the readable sheets' transition declarations, for measurements.md
  out._meta.sheets[pathOf(g.page)] = await page.evaluate(() => {
    const found = [];
    for (const ss of document.styleSheets) {
      try {
        for (const r of ss.cssRules) {
          if (r.style && r.style.transition && r.style.transition !== 'all 0s') found.push({ transition: r.style.transition.slice(0, 90) });
        }
      } catch { /* cross-origin sheet */ }
    }
    return found.slice(0, 30);
  }).catch(() => []);

  for (const spec of g.specs) {
    const comp = out.components[spec.key] ??= {};
    comp.group = spec.group;
    comp.title = spec.title;
    comp.desc = spec.desc;
    comp.selector = spec.sel;
    comp.page = pathOf(g.page);
    comp.url = safeUrl(url);
    comp.run = new Date().toISOString();
    comp.states ??= {};
    let loc;
    // A lookup miss must not erase states a previous run already measured —
    // only a component with no good readings at all counts as missing.
    const hasStates = () => Object.values(comp.states ?? {}).some((s) => s && s.style);
    try { loc = await spec.find(page); } catch (e) {
      log(' ', spec.key, 'find failed:', e.message.split('\n')[0]);
      if (hasStates()) comp.rerunMiss = e.message.split('\n')[0]; else comp.missing = true;
      continue;
    }
    if (!(await loc.count()) || !(await loc.first().isVisible().catch(() => false))) {
      log(' ', spec.key, 'absent');
      if (hasStates()) comp.rerunMiss = 'absent on this run'; else comp.missing = true;
      continue;
    }
    delete comp.missing;
    delete comp.rerunMiss;
    loc = loc.first();
    for (const st of spec.states) {
      const name = typeof st === 'string' ? st : (st.name || 'opened');
      // pressed/dark are cleared in finally so a failed read can never leak
      // the forced state into the next measurement.
      let pressed = null;
      let darkOn = false;
      let toggle = null;  // a toggled state's press and its state before, for the restore
      try {
        await reset();
        let viaText = 'resting state';
        let readLoc = loc;
        if (st === 'hover') { await hover(readLoc); viaText = via.hover; }
        else if (st === 'focus-visible') { const f = await kbFocus(readLoc); viaText = f && (f.held || f.ring) ? via['focus-visible'] : 'focus failed'; }
        else if (st === 'focused') { await readLoc.click({ timeout: 3000 }).catch(() => readLoc.evaluate((el) => el.focus())); await page.waitForTimeout(400); viaText = 'the field clicked into'; }
        else if (st === 'pressed') { pressed = await pressOn(readLoc); viaText = via.pressed; }
        else if (st === 'dark') { if (!(await darkFn(page, 'dark'))) { log(' ', spec.key, name, 'dark never painted — skipped'); continue; } darkOn = true; viaText = isBlog(g.page) ? via.darkblog : via.dark; }
        else if (st === 'darkblog') { if (!(await setBlogTheme(page, 'dark'))) { log(' ', spec.key, name, 'dark never painted — skipped'); continue; } darkOn = true; viaText = via.darkblog; }
        else if (st && typeof st === 'object' && st.fn) { toggle = await toggleBefore(st, readLoc); const alt = await toggleOpen(st, toggle); if (alt && typeof alt.count === 'function' && await alt.count()) readLoc = alt; viaText = st.via || 'reached by the component\'s own UI toggle'; }
        else if (typeof st === 'function') { await st(readLoc); viaText = 'reached by the component\'s own UI toggle'; }
        await centre(readLoc).catch(() => {});
        const v = await styleOf(readLoc);
        v.via = viaText;
        v.crop = await crop(page, readLoc, `${spec.key}-${name}`).catch((e) => { log('  crop failed', spec.key, name, e.message.split('\n')[0]); return undefined; });
        v.run = new Date().toISOString();
        comp.states[name] = v;
        log(' ', spec.key, name, 'ok');
      } catch (e) {
        // A failed rerun records the error beside the last good reading, not
        // over it — a good saved state outlives a transient failure.
        const prev = comp.states[name];
        comp.states[name] = (prev && prev.style)
          ? { ...prev, rerunError: e.message.split('\n')[0] }
          : { error: e.message.split('\n')[0] };
        log(' ', spec.key, name, 'FAILED', e.message.split('\n')[0]);
      } finally {
        if (pressed != null) await pressOff(pressed).catch(() => {});
        // A toggled state puts the page back to the state it had before its
        // press, even when the reading failed: without it every later
        // component was measured in the toggled layout (the collapsed
        // sidebar, an open FAQ row). A press that never landed leaves
        // nothing to undo; a stale control is found again (toggle.mjs).
        if (toggle && st.restore) {
          const refind = async () => { const a = await spec.find(page).catch(() => null); return a && await a.count() ? a.first() : null; };
          await toggleRestore(st, toggle, refind).catch((e) => log(' ', spec.key, name, 'restore failed', e.message.split('\n')[0]));
        }
        if (darkOn) {
          let back = await darkFn(page, 'light').catch(() => false);
          if (!back) back = await darkFn(page, 'light').catch(() => false);
          if (!back) {
            // A failed reset must never leak dark paint into the next
            // default reading: reload, which restores the html.light boot,
            // and re-find the element so later states measure the live page.
            log(' ', spec.key, 'light reset failed — reloading to the light boot');
            await open(page, url, { wait: 7000 }).catch(() => {});
            await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
            if (g.setup) await g.setup(page).catch(() => {});
            const refound = await spec.find(page).catch(() => null);
            if (refound && await refound.count()) loc = refound.first();
          }
        }
      }
    }
    save();
  }
  if (g.teardown) await g.teardown(page).catch(() => {});
  await darkFn(page, 'light').catch(() => {});
  await page.close();
}
await b.close();
log('done ->', OUT);
