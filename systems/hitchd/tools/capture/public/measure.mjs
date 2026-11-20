// Measures hitchd.com's signed-out public components at 1440px and 390px and
// writes raw/component-measurements.json (the "measured" provenance for
// tokens.json and components.md); crops each one into components/crops/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/public/measure.mjs [component,component,...]
//
// Everything below is a real element on a signed-out page, located by its
// class or tag — never by its text, so renames cannot silently relocate the
// measurement. Auth surfaces (/login, /signup, /forgot-password) are read at
// rest only: nothing is typed or submitted. The registry's internal routes
// (contributions/payment-methods/ask/quick-thanks) bounce the guest to / —
// measured and recorded as that boundary. The gift modal is opened by the
// card's own tap and read at rest; its Give flow is never entered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, open as openPage, openRegistry, closePromo, styleOf, crop, centre, RAW, domFind, slug, patch } from './lib.mjs';
// open() returns false on a blocked load and leaves the tab on about:blank;
// every reading here runs inside run(), so throwing records it as failed
// instead of measuring the blank tab as the product (2026-11 audit, 20-4)
const open = async (page, url, opts) => { if (!(await openPage(page, url, opts))) throw new Error(`BLOCKED ${url}: the page never loaded, nothing measured`); };
import { safeUrl } from '../safe-url.mjs';

const only = (process.argv[2] || '').split(',').filter(Boolean);
const out = {};
const { browser } = await launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
await patch(ctx);
const mctx = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
await patch(mctx);
const p = await ctx.newPage();
const pm = await mctx.newPage();
const safeCrop = async (page, locator, name) => { try { return await crop(page, locator, name); } catch { return null; } };
const run = async (name, fn) => { if (only.length && !only.includes(name)) return; try { out[name] = await fn(); console.log('ok', name); } catch (e) { out[name] = { error: String(e).split('\n')[0] }; console.log('FAIL', name, out[name].error); } };

// The registry wait lives in lib.mjs (openRegistry): it polls for a painted,
// nonzero-size .giftz tile — the element can exist at 0px while the app is
// still booting — reloads once on a stall, then hides the popups. layout.mjs
// and public.mjs share the same wait.

// ---- marketing surface ----------------------------------------------------

await run('marketing-nav', async () => {
  await open(p, BASE + '/');
  const header = p.locator('.closure-header, header').first();
  const logo = p.locator('.closure-header .logo a, .closure-header a:has(img), header a:has(img)').first();
  const login = p.locator('.closure-header a, header a').filter({ hasText: /log in/i }).first();
  return {
    header: await styleOf(header),
    logo: await styleOf(logo), logoBox: await centre(logo),
    loginLink: await styleOf(login),
    crop: await safeCrop(p, header, 'nav'),
  };
});

await run('announcement-banner', async () => {
  await open(p, BASE + '/');
  const el = p.locator('.top-banner, [class*="announce" i], .top-strip, .alert-bar').first();
  let banner = el;
  if (!(await el.count())) banner = p.locator('header').first();
  // the closure strip is the first full-width bar above the header; fall back
  // to the element containing the closure line
  const byText = p.locator('div, section, header').filter({ hasText: /closing on 31 December 2026/i }).last();
  if (await byText.count()) banner = byText;
  return { banner: await styleOf(banner), text: await styleOf(banner.locator('p, span, div').first()), crop: await crop(p, banner, 'announcement') };
});

await run('hero', async () => {
  await open(p, BASE + '/');
  const h1 = p.locator('h1').first();
  return { h1: await styleOf(h1), h1Box: await centre(h1), lead: await styleOf(h1.locator('xpath=following::p[1]').first()), crop: await crop(p, h1.locator('xpath=ancestor::section[1] | ancestor::header[1] | ancestor::div[1]').last(), 'hero') };
});

await run('marketing-h2', async () => {
  // the closure home page carries no h2/footer — those live on the content pages
  await open(p, BASE + '/trips/australia');
  const h2 = p.locator('h2:visible').first();
  return { h2: await styleOf(h2), crop: await safeCrop(p, h2, 'h2') };
});

await run('marketing-footer', async () => {
  await open(p, BASE + '/trips/australia');
  const f = p.locator('footer').first();
  return { footer: await styleOf(f), link: await styleOf(f.locator('a').first()), crop: await safeCrop(p, f, 'footer') };
});

await run('blog-card', async () => {
  await open(p, BASE + '/blog');
  // section.blog-post wraps the whole index (its h2 is "Articles"); one card
  // is an <article> tile inside its .grid-container
  const card = p.locator('section.blog-post article:visible').first();
  return { card: await styleOf(card), title: await styleOf(card.locator('h1, h2, h3, h4').first()), crop: await safeCrop(p, card, 'blog-card') };
});

await run('article-type', async () => {
  await open(p, BASE + '/blog/what-is-a-honeymoon-registry', { wait: 10000 });
  const body = p.locator('.blog-post p:visible, article p:visible, [class*="content" i] p:visible, main p:visible').first();
  return { h1: await styleOf(p.locator('h1').first()), body: await styleOf(body), link: await styleOf(p.locator('article a, main a').first()) };
});

await run('prose-h2', async () => {
  await open(p, BASE + '/terms');
  const h2 = p.locator('h2:visible, h3:visible').first();
  return { h2: await styleOf(h2), body: await styleOf(p.locator('main p:visible, article p:visible, p:visible').first()) };
});

// ---- couple app (auth forms at rest) --------------------------------------

await run('auth-layout', async () => {
  await open(p, BASE + '/login');
  return { h1: await styleOf(p.locator('h1').first()), card: await styleOf(p.locator('form').first()), page: await styleOf(p.locator('body')), crop: await crop(p, p.locator('form').first(), 'auth-card') };
});

await run('auth-field', async () => {
  await open(p, BASE + '/login');
  const input = p.locator('input[type="email"]:visible, input[type="text"]:visible, input:visible').first();
  return { input: await styleOf(input), label: await styleOf(input.locator('xpath=preceding::label[1]').first()) };
});

await run('auth-button', async () => {
  await open(p, BASE + '/login');
  const btn = p.locator('button[type="submit"]:visible, button:visible').first();
  return { button: await styleOf(btn), disabled: await btn.isDisabled().catch(() => null), crop: await crop(p, btn, 'auth-button') };
});

await run('auth-link', async () => {
  await open(p, BASE + '/login');
  const a = p.locator('a').filter({ hasText: /forgot|sign up|create/i }).first();
  return { link: await styleOf(a), muted: await styleOf(p.locator('[class*="helper" i]:visible, [class*="muted" i]:visible, p:visible').first()) };
});

// ---- guest registry app ----------------------------------------------------

await run('registry-hero', async () => {
  await openRegistry(p);
  const h = p.locator('h1.classic:not(.proxy):visible, h1:visible').first();
  const names = p.locator('.couple-intro, [class*="couple" i]').first();
  return { heading: await styleOf(h), names: await styleOf(names), crop: await safeCrop(p, names, 'registry-hero') };
});

await run('registry-nav', async () => {
  await openRegistry(p);
  const bar = p.locator('.top-registry-sample-banner:visible').first();
  // the banner renders two a.direct copies — a .show-for-small-only one for the
  // phone and a .hide-for-small-only one for the desktop; only the one that
  // paints at this width may be measured (the other reads 0px with stale
  // styles)
  const cta = bar.locator('a.direct:visible').filter({ hasText: /try it free/i }).first();
  return { bar: await styleOf(bar), cta: await styleOf(cta), hashtag: await styleOf(p.locator('.hashtag-link:visible').first()), crop: await safeCrop(p, bar, 'registry-nav') };
});

await run('gift-card', async () => {
  if (!(await openRegistry(p))) throw new Error('gift list never painted');
  // ol.gift-list holds .giftz tiles; the first is the couple's showcase pick
  const card = p.locator('ol.gift-list .giftz:visible').first();
  const info = card.locator('.showcasegift-info:visible, [class*="info" i]:visible').first();
  const title = card.locator('h1:visible, h2:visible, h3:visible, h4:visible, h5:visible').first();
  const price = card.locator('[class*="pric" i]:visible, [class*="amount" i]:visible, .currency:visible').first();
  const r = { card: await styleOf(card), title: await styleOf(title), crop: await safeCrop(p, card, 'gift-card') };
  // the showcase tile carries .bottompricing; non-showcase tiles may not
  if (await price.count()) r.price = await styleOf(price);
  if (await info.count()) r.info = await styleOf(info);
  return r;
});

await run('sort-filter', async () => {
  if (!(await openRegistry(p))) throw new Error('gift list never painted');
  await p.locator('select').first().waitFor({ state: 'attached', timeout: 20000 }).catch(() => {});
  // two stacked variants are rendered; only one paints at this width
  const sel = p.locator('select:visible').first();
  const dd = sel.locator('xpath=ancestor::*[contains(@class,"toggle-dd") or contains(@class,"filter") or contains(@class,"sort")][1]').first();
  const wrap = (await dd.count()) ? dd : sel.locator('xpath=..').first();
  return { control: await styleOf(wrap), select: await styleOf(sel), crop: await safeCrop(p, wrap, 'sort-filter') };
});

await run('gift-modal', async () => {
  if (!(await openRegistry(p))) throw new Error('gift list never painted');
  const card = p.locator('ol.gift-list .giftz:visible').first();
  await card.scrollIntoViewIfNeeded();
  // the tile's own .click-space / .view-gift hit target navigates to
  // /<couple>/<gift-slug>, which paints the modal — a bare div click can land
  // on a child that swallows the event
  await card.locator('.click-space, .view-gift').first().click({ timeout: 8000 }).catch(() => {});
  await p.waitForTimeout(5000);
  const modal = p.locator('.gift-modal:visible, .modalDialog:visible, app-gift-modal [class*="modal" i]:visible').first();
  if (!(await modal.count())) return { notes: { boundary: 'gift modal did not open from the card tap' } };
  const give = modal.locator('button, a').filter({ hasText: /give|contribute/i }).first();
  // the pill's fill paints on its .pay wrapper, not the <a>
  const giveWrap = give.locator('xpath=ancestor::*[contains(@class,"pay")][1]').first();
  const r = { modal: await styleOf(modal), title: await styleOf(modal.locator('h1, h2, h3').first()), give: await styleOf(give), crop: await safeCrop(p, modal, 'gift-modal') };
  if (await giveWrap.count()) r.giveWrap = await styleOf(giveWrap);
  await p.goBack({ waitUntil: 'domcontentloaded' }).catch(() => {});
  return r;
});

await run('mobile-menu', async () => {
  await openRegistry(pm);
  // the demo registry ships a .mobile-menu drawer (with links, for the
  // registry owner's signed-in view) but no guest-facing control opens it —
  // it stays mobile-menu-hidden, so it is measured at rest as the boundary
  const menu = pm.locator('.mobile-menu').first();
  if (!(await menu.count())) return { notes: { boundary: 'no .mobile-menu element exists on the public demo registry at 390px' } };
  const hidden = await menu.evaluate((el) => el.classList.contains('mobile-menu-hidden')).catch(() => null);
  const links = await menu.locator('a').count();
  return { menu: await styleOf(menu), notes: { hidden, linkCount: links, boundary: 'no guest-facing hamburger control exists on the public demo registry — the drawer stays hidden for signed-out visitors' } };
});

await run('mobile-gift-card', async () => {
  if (!(await openRegistry(pm))) throw new Error('gift list never painted');
  const card = pm.locator('ol.gift-list .giftz:visible').first();
  return { card: await styleOf(card), crop: await safeCrop(pm, card, 'mobile-gift-card') };
});

// ---- boundaries ------------------------------------------------------------

await run('internal-route-bounces', async () => {
  await openRegistry(p);
  const res = {};
  for (const sub of ['contributions', 'payment-methods', 'ask', 'quick-thanks']) {
    await p.goto(`${BASE}/zoeandnoah/${sub}`, { waitUntil: 'domcontentloaded', timeout: 60000 }).catch(() => {});
    // the SPA's bounce is client-side and takes a few seconds after load
    await p.waitForTimeout(12000);
    const u = new URL(p.url());
    res[sub] = { landedUrl: safeUrl(p.url()), bouncedToHome: u.pathname === '/' || u.pathname === '' };
  }
  return res;
});

// build-measurements.mjs reads raw/components-computed.json: one entry per
// component, `states` a map of label -> a styleOf reading. Each measured part
// above (input, label, button…) becomes one column of the component's table.
// Keys whose value is not a reading (a bool, a boundary object) are dropped
// from the table but kept under `notes`.
const META = {
  'marketing-nav': ['Chrome', 'Marketing nav', 'the home header bar and its logo + Log In link', BASE + '/'],
  'announcement-banner': ['Chrome', 'Closure announcement banner', 'the full-width "Hitchd is closing on 31 December 2026" strip above the header', BASE + '/'],
  hero: ['Type', 'Hero heading', 'the home hero — "Tie the knot, without tangles." set in DDNR', BASE + '/'],
  'marketing-h2': ['Type', 'Marketing H2', 'a section heading on the marketing surface (the closure home carries no h2, so this was read on the destination page)', BASE + '/trips/australia'],
  'marketing-footer': ['Chrome', 'Footer', 'the marketing footer and its links (the closure home has no footer; read on the destination page)', BASE + '/trips/australia'],
  'blog-card': ['Cards', 'Blog index card', 'a post row on /blog', BASE + '/blog'],
  'article-type': ['Type', 'Article type', 'the blog post H1, body copy and inline link', BASE + '/blog/what-is-a-honeymoon-registry'],
  'prose-h2': ['Type', 'Legal prose', 'a terms page heading and paragraph', BASE + '/terms'],
  'auth-layout': ['Forms', 'Auth form card', 'the /login form container and heading, at rest', BASE + '/login'],
  'auth-field': ['Forms', 'Auth text field', 'the email input and its label, at rest', BASE + '/login'],
  'auth-button': ['Forms', 'Auth submit button', 'the Continue button in its disabled-at-rest state', BASE + '/login'],
  'auth-link': ['Forms', 'Auth links', 'the forgot-password link and helper copy', BASE + '/login'],
  'registry-hero': ['Type', 'Registry hero', 'the demo registry heading and couple names', BASE + '/zoeandnoah'],
  'registry-nav': ['Chrome', 'Registry nav', 'the registry top bar, #hashtag link and Try It Free CTA', BASE + '/zoeandnoah'],
  'gift-card': ['Cards', 'Gift card', 'a gift tile in the registry list', BASE + '/zoeandnoah'],
  'sort-filter': ['Controls', 'Sort filter', 'the "Sort by" select in the registry header', BASE + '/zoeandnoah'],
  'gift-modal': ['Dialogs', 'Gift modal', 'a gift card\'s modal, opened by its own tap and read at rest; the Give flow is never entered', BASE + '/zoeandnoah/<gift-slug>'],
  'mobile-menu': ['Controls', 'Mobile menu', 'the registry .mobile-menu drawer at 390px — it exists (with owner links) but no guest-facing control opens it, so it was measured hidden at rest', BASE + '/zoeandnoah'],
  'mobile-gift-card': ['Cards', 'Gift card (mobile)', 'a gift tile at 390 x 844', BASE + '/zoeandnoah'],
  'internal-route-bounces': ['Boundaries', 'Registry internal routes', 'contributions / payment-methods / ask / quick-thanks each bounce the signed-out guest back to /', BASE + '/zoeandnoah'],
};

// A filtered re-run (node measure.mjs marketing-nav,marketing-h2) merges into
// the existing file instead of replacing it, so one bad selector can be fixed
// and re-measured without repeating the whole sweep.
const prev = fs.existsSync(path.join(RAW, 'components-computed.json'))
  ? JSON.parse(fs.readFileSync(path.join(RAW, 'components-computed.json'), 'utf8')).components || {}
  : {};
const components = { ...prev };
for (const [k, v] of Object.entries(out)) {
  const [group, title, desc, page] = META[k] || ['General', k, '', ''];
  const states = {};
  const notes = {};
  if (v && v.error) { components[k] = { group, title, desc, page, selector: '', states: { rest: { error: v.error } } }; continue; }
  for (const [sk, sv] of Object.entries(v || {})) {
    if (sv && typeof sv === 'object' && sv.style && sv.rect) states[sk] = sv;
    else notes[sk] = sv;
  }
  // a crop path belongs on the first reading, where build-measurements looks
  // for it; genuine notes (disabled flags, boundary maps) stay top-level
  if (typeof notes.crop === 'string') { const k0 = Object.keys(states)[0]; if (k0) states[k0].crop = notes.crop; delete notes.crop; }
  if (!Object.keys(states).length) states.rest = { error: Object.keys(notes).length ? JSON.stringify(notes) : 'no readings returned' };
  components[k] = { group, title, desc, page, selector: 'see tools/capture/public/measure.mjs', states, ...(Object.keys(notes).length ? { notes } : {}) };
}

fs.mkdirSync(RAW, { recursive: true });
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify({
  _meta: {
    read: new Date().toLocaleDateString('en-CA'),
    source: 'computed styles + getBoundingClientRect read in live Chromium at 1440 x 900 and 390 x 844 on the signed-out public pages named per component; crops in components/crops/; auth forms read at rest, the gift modal opened by its own card and read at rest',
    sheets: {},
  },
  components,
}, null, 1) + '\n');
console.log('components-computed.json:', Object.keys(components).length, 'components');
await browser.close();
