// Measures awwwards.com's public components in every state reachable without
// voting, submitting, logging in or signing in.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home websites site collections submit mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// awwwards.com is a custom web-awards directory in one light theme, served in
// English. Selectors key off its long-lived semantic classes
// (header-main__logo, nav-filters__item, figure-rollover__link, box-score,
// button) and text. Headless Chrome is served a 200 (see lib.mjs). Nothing is
// voted on, sent or subscribed: the only presses are local UI toggles — the
// winners-grid filter dropdown and the mobile menu. Consent or promo layers
// are hidden before every measurement, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE , pickSiteDetail } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', websites: '/websites/', site: '/websites/', collections: '/collections/', submit: '/submit/' };
let page, cdp, current, context, run;
let activeCtx; // the context of the current page; closed when the next route opens
const touched = new Set();
const ranPages = new Set();  // pages that actually opened this run
const listed = new Map();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /access denied|performing security verification|verifying you are human|just a moment|edgesuite\.net/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000 } = {}) {
  current = key;
  const b = context.browser();
  // Close the previous route's context first: leaving every context and page
  // running until the whole pass ends keeps each route's scripts, images and
  // timers alive while later routes are measured.
  if (activeCtx) { await activeCtx.close().catch(() => {}); activeCtx = undefined; }
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  activeCtx = ctx;
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  const target = URLS[key];
  await open(page, /^https?:/.test(target) ? target : BASE + target, { wait });
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); activeCtx = undefined; return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await closePromo(page);
  return true;
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(250);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  let how = 'Shift+Tab, Tab';
  if (!ok) {
    await page.keyboard.press('Shift');
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el);
    how = 'keydown then focus()';
  }
  await page.waitForTimeout(350);
  return ok ? how : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(400);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

// comp() merges the spec's meta into the entry and marks it touched. The
// page/run/url provenance is only written once the target is found, so a
// re-run whose selector misses keeps the earlier evidence's own page, run and
// url instead of stamping a new date on stale readings (FIELD-NOTES).
function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

function found(c) {
  delete c.missing;
  delete c.recaptureMissed;
  Object.assign(c, { page: current, run, url: /^https?:/.test(URLS[current]) ? URLS[current] : BASE + URLS[current] });
}

async function measure(key, state, target, opts = {}) {
  const loc = target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

async function S(key, target, list, meta = {}, opts = {}) {
  const c = comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0,80)); } }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    log('  ! missing', key);
    c.missing = true;
    c.recaptureMissed = run;
    c.states = {}; // stale states from an earlier run are not current evidence
    return;
  }
  found(c);
  for (const st of list) {
    let undo, via;
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(loc);
      if (opts.before?.[st]) via = await opts.before[st](loc);
      if (st === 'hover') {
        await (opts.hoverLoc || loc).filter({ visible: true }).first().hover({ timeout: 5000 }).catch(() => (opts.hoverLoc || loc).filter({ visible: true }).first().hover({ timeout: 5000, force: true }));
        await page.waitForTimeout(450);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus((opts.focusLoc || loc).filter({ visible: true }).first());
        // a state that did not receive keyboard focus is not a captured focus
        if (via === 'focus failed') throw new Error('keyboard focus did not land on the element');
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).filter({ visible: true }).first(), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        const fld = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 });
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'picked') {
        const sel = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await sel.selectOption({ index: 1 }).catch(() => {});
        await page.waitForTimeout(500);
        undo = async () => { await sel.selectOption({ index: 0 }).catch(() => {}); };
        via = 'selectOption index 1, then restored to index 0; nothing submitted';
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'flyout held open by opts.open';
        else { await toggle(loc); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (menu, accordion, swatch). Refuses a submit button and any
// control whose text names a purchase/action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add to bag|add to cart|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|place order|continue|vote|visit)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

async function sheetsFor(key) {
  const res = await page.evaluate(() => {
    const transitions = [];
    const walk = (rules) => {
      for (const r of rules) {
        if (r.cssRules && !r.selectorText) { walk(r.cssRules); continue; }
        if (!r.style) continue;
        const t = r.style.getPropertyValue('transition');
        const a = r.style.getPropertyValue('animation');
        if (t || a) transitions.push({ selector: (r.selectorText || '').slice(0, 160), transition: t, animation: a });
      }
    };
    for (const ss of document.styleSheets) { try { walk(ss.cssRules); } catch { /* cross-origin */ } }
    return transitions;
  });
  out._meta.sheets ??= {};
  out._meta.sheets[key] = res;
}

const G = {
  shell: 'Shell and navigation', hero: 'Home', grid: 'Winners grid', site: 'Site detail',
  collections: 'Collections', submit: 'Submit gate', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

const tid = (id) => `[data-testid="${id}"]`;

async function home() {
  if (!(await newPage('home'))) return;
  ranPages.add('home');
  await sheetsFor('home');
  const g = G.shell;
  await S('header', q('header').first(), ['default'], { group: g, title: 'Header', desc: 'The top bar: wordmark, Explore/Directory/Academy/Jobs/Market nav, Log in / Sign Up / Be Pro / Submit Website.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a.header-main__logo'), ['default'], { group: g, title: 'Logo', desc: 'The wordmark link back to /. ', sel: 'a.header-main__logo' }, { noScroll: true });
  await S('nav-item', q('header a').filter({ hasText: /^\s*Directory\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A top-level nav link (Directory). Measured, never followed.', sel: 'header a:has-text("Directory")' }, { noScroll: true });
  // The auth links sit outside the <header> element in .header-main, and are
  // not rendered on every headless load; missing runs record the gap.
  await S('login-link', q('a, span, li').filter({ hasText: /^\s*log ?in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in link', desc: 'Log in in the site header. Measured, never followed — the click opens nothing headless and no login page exists signed-out.', sel: ':text("Log in")' }, { noScroll: true });
  await S('signup-link', q('a, span, li').filter({ hasText: /^\s*sign ?up\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign Up link', desc: 'Sign Up in the site header. Measured, never followed.', sel: ':text("Sign Up")' }, { noScroll: true });
  await S('bepro-link', q('a[href="/pro"]').filter({ visible: true }).first(), B4, { group: g, title: 'Be Pro link', desc: 'The Be Pro upsell button in the header. Measured, never followed.', sel: 'a[href="/pro"]' }, { noScroll: true });
  await S('submit-cta', q('header a[href*="/submit"], header a').filter({ hasText: /submit website/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Submit Website button', desc: 'The header CTA. Measured, never followed.', sel: 'header a[href*="/submit"]' }, { noScroll: true });
  for (let y = 0; y < 3000; y += 700) { await page.evaluate((yy) => scrollTo(0, yy), y); await page.waitForTimeout(220); }
  await page.evaluate(() => scrollTo(0, 0)); await page.waitForTimeout(800);
  const h = G.hero;
  // a heading element only: [class*=heading] caught the whole Site of the Day block
  await S('sotd-heading', q('h1, h2, h3').filter({ hasText: /site of the day|nominees/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: '"Site of the Day" heading over the first card.', sel: ':has-text("Site of the Day")' });
  const cardLink = q('a.figure-rollover__link').filter({ visible: true }).first();
  const cardBox = cardLink.locator('xpath=ancestor::*[self::figure or contains(@class,"item") or self::li][1]');
  await S('site-card', cardBox, ['default', 'hover'], { group: h, title: 'Site card', desc: 'A winning-site card: screenshot, title, author and rollover actions.', sel: 'ancestor of a.figure-rollover__link' });
  // The home-card hover layer (Vote Now) never materialised for headless
  // measurement; the equivalent action is measured at rest on the detail
  // page's related cards (card-action below). Recorded as a gap.
  await S('card-cta', q('.figure-rollover__hover a, .figure-rollover__center a, .figure-rollover a.button').filter({ visible: true }).first(), ['default'], { group: h, title: 'Card action', desc: 'The "Vote Now" button revealed by hovering a site card; it stayed display:none under headless hover — see card-action on the site page instead.', sel: '.figure-rollover__hover a.button' }, { noReset: true, noScroll: true, open: async () => { await cardLink.hover({ timeout: 5000 }).catch(() => cardLink.hover({ force: true, timeout: 5000 })); await page.waitForTimeout(1400); } });
  save();
}

async function websites() {
  if (!(await newPage('websites', { wait: 9000 }))) return;
  ranPages.add('websites');
  const g = G.grid;
  await S('grid-title', q('h1').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Grid title', desc: '"Winning websites. Web Design Inspiration".', sel: 'h1' }, { noScroll: true });
  const filterItem = q('.nav-filters__item.js-nav-filters-item, .nav-filters__item').filter({ visible: true }).first();
  // The item toggles: clicking it again closes the dropdown, so only click
  // when the dropdown is not already open.
  const ensureFilterOpen = async () => {
    if (await q('.nav-filters__dropdown').filter({ visible: true }).count()) return;
    await filterItem.click({ timeout: 4000 }).catch(() => filterItem.evaluate((el) => el.click()));
    await page.waitForTimeout(1500);
  };
  await S('filter-item', filterItem, ['default', 'hover'], { group: g, title: 'Filter tab', desc: 'An Awards/Category/Tag/Technology filter tab on the winners grid.', sel: '.nav-filters__item' });
  await S('filter-dropdown', q('.nav-filters__dropdown').filter({ visible: true }).first(), ['default'], { group: g, title: 'Filter dropdown', desc: 'The open sublist under a filter tab.', sel: '.nav-filters__dropdown' }, { noReset: true, open: ensureFilterOpen });
  await S('filter-option', q('.nav-filters__subitem').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Filter option', desc: 'An option row inside the open filter dropdown. Measured, never followed.', sel: '.nav-filters__subitem' }, { noReset: true, open: ensureFilterOpen });
  const cardLink = q('a.figure-rollover__link').filter({ visible: true }).first();
  const cardBox = cardLink.locator('xpath=ancestor::*[self::figure or contains(@class,"item") or self::li][1]');
  await S('grid-card', cardBox, ['default', 'hover'], { group: g, title: 'Grid card', desc: 'A winning-site card on the winners grid.', sel: 'ancestor of a.figure-rollover__link' });
  await S('grid-card-link', cardLink, ['default', 'focus-visible'], { group: g, title: 'Grid card link', desc: 'The card anchor to /sites/<slug>. Measured, never followed.', sel: 'a.figure-rollover__link' });
  save();
}

async function site() {
  if (!(await newPage('site', { wait: 9000 }))) return;
  ranPages.add('site');
  // Site of the Day winners have closed voting, so the vote button only
  // exists on some detail pages: walk up to four card links and land on the
  // first whose page still has one, else keep the first.
  const href = await pickSiteDetail(page);   // shared with public.mjs: same entry for shots and measurements
  if (href) {
    await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  }
  if (href) URLS.site = /^https?:/.test(href) ? href : BASE + href;  // component sources name the site, not the grid
  const g = G.site;
  out.components.site_url ??= { page: 'site', title: 'Site-detail URL', states: {} };
  out.components.site_url.states.default = { text: href || 'none found', via: 'first /websites/ card link whose detail page still has a Vote button (SOTD winners have closed voting)' };
  touched.add('site_url');
  await S('site-title', q('h1').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Site title', sel: 'h1' }, { noScroll: true });
  await S('score-box', q('.box-score').filter({ visible: true }).first(), ['default'], { group: g, title: 'Score box', desc: 'The jury score panel (Design/Usability/Creativity/Content).', sel: '.box-score' }, { noScroll: true });
  await S('score-note', q('.box-score__note, .c-heading-score').filter({ visible: true }).first(), ['default'], { group: g, title: 'Score note', sel: '.box-score__note' }, { noScroll: true });
  await S('vote-button', q('a, button').filter({ hasText: /vote/i }).filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Vote button', desc: 'The vote CTA; measured except a real press — voting records a score and is never clicked.', sel: '.button:has-text("Vote")' });
  await S('visit-link', q('a.toolbar-bts__item, main a[href^="http"]:not([href*="awwwards.com"])').filter({ visible: true }).first(), ['default'], { group: g, title: 'Visit link', desc: 'The external visit-site toolbar icon; the hover pass found it outside the viewport, so only the at-rest reading stands.', sel: 'a.toolbar-bts__item' });
  await S('card-action', q('.figure-rollover__bt').filter({ visible: true }).first(), B4, { group: g, title: 'Card action', desc: 'A rollover action icon on a related-site card. Measured, never clicked.', sel: '.figure-rollover__bt' });
  await S('tag-chip', q('.button--tag').filter({ visible: true }).first(), B4, { group: g, title: 'Tag chip', desc: 'A category tag (Art & Illustration…) on the site detail page. Measured, never followed.', sel: '.button--tag' });
  save();
}

async function collections() {
  if (!(await newPage('collections', { wait: 9000 }))) return;
  ranPages.add('collections');
  const g = G.collections;
  await S('coll-title', q('h1').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Collections title', sel: 'h1' }, { noScroll: true });
  // a card has an image: the first collections link was the Reset filters button
  await S('coll-card', q('a[href*="/collections/"]').filter({ has: q('img') }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Collection card', desc: 'A curated-collection card. Measured, never followed.', sel: 'a[href*="/collections/"]' });
  save();
}

async function submit() {
  if (!(await newPage('submit', { wait: 9000 }))) return;
  ranPages.add('submit');
  const g = G.submit;
  await S('submit-title', q('h1, h2, .heading-5').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Submit title', sel: 'h1, .heading-5' }, { noScroll: true });
  await S('submit-cta-2', q('main .button, main a.button, main a, main button').filter({ visible: true }).first(), B4, { group: g, title: 'Submit CTA', desc: 'The first call-to-action on /submit/. Measured, never followed.', sel: 'main .button' });
  await S('plan-card', q('[class*="plan" i], [class*="price" i], [class*="pack" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan/pricing card', desc: 'A submission plan card where the page offers one.', sel: '[class*="plan"]' });
  save();
}

async function footer() {
  if (!page || page.isClosed()) {
    if (!(await newPage('home'))) return;
  ranPages.add('home');
  } else {
    current = 'home';
    await open(page, BASE + URLS.home, {});
    if (await blocked()) { log('  BLOCKED footer'); return; }
    await closePromo(page);
    ranPages.add('home');
  }
  const g = G.footer;
  // The footer holds section links and a search-inspiration block; its links
  // lazy-load, so scroll it into view first.
  await page.evaluate(() => scrollTo(0, document.body.scrollHeight));
  await page.waitForTimeout(1800);
  // The page footer is a bare <footer> element holding .footer__menu /
  // .footer__bottom; [class*="footer"] without the tag picks up
  // card-course__footer inside the grid first, so the tag is required.
  const footerEl = q('footer').filter({ visible: true }).first();
  const fl = footerEl.locator('a').filter({ hasText: /\w{3,}/ }).filter({ visible: true }).first();
  if (await fl.count()) {
    await S('footer', footerEl, ['default'], { group: g, title: 'Footer', sel: 'footer' });
    await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a' });
    const nl = footerEl.locator('input[type="email"], input[name*="email" i]').first();
    if (await nl.count()) await S('newsletter-input', nl, ['default', 'focused'], { group: g, title: 'Newsletter field', desc: 'Focused only; never subscribed.', sel: 'footer input[type="email"]' });
  }
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  ranPages.add('home');
  const g = G.mobile;
  await S('m-header', q('header').first(), ['default'], { group: g, title: 'Mobile header', sel: 'header' }, { noScroll: true });
  const menuBtn = q('header [class*="burger" i], header [class*="trigger" i], header button, [class*="menu-mobile" i]').filter({ visible: true }).first();
  await S('m-menu-button', menuBtn, B4, { group: g, title: 'Mobile menu button', sel: 'header menu button' }, { noScroll: true });
  const drawer = q('[class*="menu-mobile" i], [id*="menu" i][class*="open" i], [class*="menu" i][class*="open" i], nav').filter({ visible: true }).last();
  await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The menu button after its own toggle; the crop is the open menu layer.', sel: 'header menu button' }, { noScroll: true, cropLoc: drawer });
  const mLink = q('header a, nav a, [class*="menu" i] a').filter({ hasText: /\w{3,}/ }).filter({ visible: true }).first();
  await S('m-nav-link', mLink, ['default'], { group: g, title: 'Mobile nav link', desc: 'A row inside the opened menu.', sel: 'nav a' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-site-card', q('a.figure-rollover__link').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile site card', desc: 'A winning-site card on mobile.', sel: 'a.figure-rollover__link' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, websites, site, collections, submit };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) await plan[k]();
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // Only a page that actually opened may lose its untouched components; a
    // blocked or thrown route keeps its earlier readings instead of erasing
    // them with an incomplete write.
    if (!touched.has(key) && !pages.length && ranPages.has(c.page)) { delete out.components[key]; continue; }
    if (!touched.has(key)) continue;
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st) && pages.length) delete c.states[st];
  }
  save();
  await browser.close().catch(() => {});
}
console.log('done ->', OUT);
