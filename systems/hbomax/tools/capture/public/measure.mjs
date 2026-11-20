// Measures www.hbomax.com's components on its public marketing pages, in every
// state that can be reached without signing in or submitting anything.
//
//   xvfb-run -a env PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [group ...]
//
// Groups: home plans faq detail legal consent mobile. Writes
// raw/components-computed.json (merged, so a subset of groups can be re-run)
// and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 500ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or button can fire
//   opened         a resting state reached by the component's own toggle: an FAQ
//                  item's chevron, the carousel's own Next arrow, the language
//                  selector's list, the phone's menu button
// Nothing is typed, sent, bought or signed into — Sign In / Choose plan /
// Start Subscription links are only hovered and focused, never pressed. HBO Max
// paints a single dark theme (html data-theme="max"), so there are no
// dark-state passes; setTheme no-ops. Headed under xvfb (Akamai 403s headless).
import fs from 'node:fs';
import path from 'node:path';
import { chromium, BASE, LOCALE, M, open, closePromo, setTheme, paintedTheme, styleOf, crop, centre, domFind, patch, UA, UA_MOBILE, RAW } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: LOCALE,
  show: LOCALE + '/show/e6e7bad9-d48d-4434-b334-7c651ffc4bdf',
  movie: LOCALE + '/movie/710798da-f811-40be-9ed9-3a7443e36278',
  movies: LOCALE + '/movies',
  privacy: '/privacy',
};

let page, cdp, context, current;

// ---------- state drivers ----------

async function reset() {
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
// 'pressed' | 'focused' | {name, via, fn} | (loc, page) => Promise<void>.
const via = { 'hover': 'mouse hover over the element', 'focus-visible': 'keyboard focus (Shift+Tab, Tab)', 'pressed': 'CDP CSS.forcePseudoState(:active:hover) — no real press' };

// The fixed navbar: HBO Max wordmark, the nav links, Sign In.
const CHROME = [
  { key: 'header-bar', group: 'Site chrome', title: 'Fixed navigation bar',
    desc: 'The translucent gradient bar over every page: HBO Max wordmark, nav links and the Sign In button.',
    sel: 'header nav, nav[class*="Navbar"], nav', find: (p) => p.locator('header nav, nav').filter({ visible: true }).first(), states: ['default'] },
  { key: 'header-logo', group: 'Site chrome', title: 'HBO Max wordmark',
    desc: 'The wordmark link at the left of the navbar.',
    sel: 'nav a[aria-label*="home" i], nav a svg', find: (p) => p.locator('nav a[aria-label*="home" i], header a').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'header-nav-link', group: 'Site chrome', title: 'Navbar link',
    desc: 'A section link in the navbar (Browse, Series, Movies — whichever renders).',
    sel: 'nav a', find: (p) => p.locator('nav a').filter({ visible: true }).nth(1), states: ['default', 'hover', 'focus-visible'] },
  { key: 'header-signin', group: 'Site chrome', title: '"Sign In" button',
    desc: 'The pill button that leads to auth.hbomax.com — hovered and focused only, never pressed (pressing would leave the public site).',
    sel: 'a (text Sign In)', find: async (p) => await domFind(p, /sign in/i, { sel: 'nav a, header a', tag: 'si', minW: 60, minH: 20 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
];

// The hero autoplay carousel (Bootstrap markup) and the CTA inside its slide.
const HERO = [
  { key: 'hero-carousel', group: 'Hero', title: 'Hero carousel',
    desc: 'The full-bleed autoplay carousel under the navbar — backdrop art, title treatment, a "Start Subscription" CTA per slide.',
    sel: '.carousel, [class*="carousel"], [class*="Carousel"]', find: (p) => p.locator('.carousel, [class*="carousel"], [class*="Carousel"]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'hero-slide', group: 'Hero', title: 'Active carousel slide',
    desc: 'The currently painted slide: backdrop image, title and meta row.',
    // Scoped to the Bootstrap hero carousel: a bare [class*="active"] also
    // matches the language dropdown's li.active, which is not the slide.
    sel: '.carousel .carousel-item.active', find: (p) => p.locator('.carousel .carousel-item.active').filter({ visible: true }).first(), states: ['default'] },
  { key: 'hero-cta', group: 'Hero', title: 'Slide CTA ("Start Subscription")',
    desc: 'The white pill call-to-action in the active slide — an auth.hbomax.com link, hovered and focused but never pressed.',
    sel: 'a (text Start Subscription|Subscribe|Sign Up)', find: async (p) => await domFind(p, /start subscription|subscribe|sign up/i, { sel: 'a', tag: 'hc', minW: 60, minH: 24 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'hero-next', group: 'Hero', title: 'Carousel "Next" control',
    desc: 'The arrow that advances the hero — "opened" is the slide reached by its own press (a local UI toggle).',
    sel: '.carousel-control-next, [class*="carousel"] [aria-label*="next" i], [class*="carousel"] button:last-of-type',
    find: (p) => p.locator('.carousel-control-next, [aria-label*="next" i]').filter({ visible: true }).first(),
    states: ['default', 'hover', { name: 'opened', via: 'the carousel Next arrow\'s own press — the slide advanced one step', fn: async (loc) => { await loc.click({ timeout: 5000, force: true }); await page.waitForTimeout(1400); } }] },
  { key: 'hero-indicator', group: 'Hero', title: 'Carousel indicator',
    desc: 'A slide indicator tab under the hero.',
    sel: '.carousel-indicators [data-bs-target], .carousel-indicators li, .carousel-indicators button', find: (p) => p.locator('.carousel-indicators li, .carousel-indicators button, [data-bs-target]').filter({ visible: true }).first(), states: ['default', 'hover'] },
];

// The subscription plan section: tier cards, the monthly/yearly switch, the
// per-tier Choose buttons (measured, never pressed).
const PLANS = [
  { key: 'plan-section', group: 'Plans', title: 'Plans section',
    desc: 'The "Choose your plan" section: billing toggle plus the tier cards.',
    sel: '[class*="plan" i], section:has-text("plan")', find: async (p) => { const s = p.locator('[class*="plan" i], [class*="Plan"]').filter({ visible: true }); return await s.count() ? s.first() : p.locator('section').filter({ hasText: /plan/i }).first(); }, states: ['default'] },
  { key: 'plan-card', group: 'Plans', title: 'Plan tier card',
    desc: 'One subscription tier card: name, price, feature list and its Choose button.',
    sel: '[class*="plan-card" i], [class*="tier" i], [class*="PlanCard"]', find: (p) => p.locator('[class*="plan-card" i], [class*="PlanCard"], [class*="tier" i]').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'plan-toggle', group: 'Plans', title: 'Billing period toggle',
    desc: 'The monthly/yearly switch above the cards. "opened" is the prices repainted by its own press — the plan-yearly screenshot shows the result.',
    sel: '[class*="toggle" i] button, [role="switch"], [class*="billing" i] button',
    find: (p) => p.locator('[role="switch"], [class*="toggle" i] button, [class*="billing" i] button').filter({ visible: true }).first(),
    states: ['default', 'hover', { name: 'opened', via: 'the billing toggle\'s own press — the card prices repainted', fn: async (loc) => { await loc.click({ timeout: 5000, force: true }); await page.waitForTimeout(900); } }] },
  { key: 'plan-choose', group: 'Plans', title: '"Choose" plan button',
    desc: 'The button on a tier card that leads to checkout — hovered and focused only, never pressed.',
    sel: 'button|a (text Choose|Select|Continue)', find: async (p) => await domFind(p, /choose|select|get started/i, { sel: 'button, a', tag: 'ch', minW: 60, minH: 24 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
];

// The FAQ accordion near the foot of the home page.
const FAQ = [
  { key: 'faq-section', group: 'FAQ', title: 'FAQ section',
    desc: 'The "Questions" accordion near the foot of the home page.',
    sel: '.max-section-faq, [class*="faq" i]', find: (p) => p.locator('.max-section-faq, [class*="faq" i]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'faq-item', group: 'FAQ', title: 'FAQ accordion item',
    desc: 'One question row. "opened" is its own chevron press revealing the answer.',
    sel: '.max-section-faq button, [class*="faq" i] button',
    find: (p) => p.locator('.max-section-faq button, [class*="faq" i] button').filter({ visible: true }).first(),
    states: ['default', 'hover', 'focus-visible', { name: 'opened', via: 'the item\'s own press — the answer expanded', fn: async (loc) => { await loc.click({ timeout: 5000, force: true }); await page.waitForTimeout(900); } }] },
];

// A title card inside a "Discover" rail and the rail itself.
const RAIL = [
  { key: 'rail-section', group: 'Content rails', title: 'Content rail',
    desc: 'A horizontal "Discover" row of title cards.',
    sel: '[class*="shelf" i], [class*="rail" i], [class*="carousel" i]:below(:text("Discover"))', find: (p) => p.locator('section').filter({ hasText: /discover|trending|popular/i }).first(), states: ['default'] },
  { key: 'rail-card', group: 'Content rails', title: 'Title card link',
    desc: 'A poster card in a rail — a link to the title\'s detail page.',
    // Poster cards are the links into /show/… and /movie/… detail pages;
    // a bare a:has(img) also matches the navbar's a.navbar-brand logo link.
    sel: 'main a[href*="/show/"], main a[href*="/movie/"]', find: (p) => p.locator('main a[href*="/show/"], main a[href*="/movie/"]').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
];

// The footer: link columns, legal row, the language selector.
const FOOTER = [
  { key: 'footer', group: 'Footer', title: 'Site footer',
    desc: 'The footer: link columns, the legal row and the language selector.',
    sel: 'footer', find: (p) => p.locator('footer').filter({ visible: true }).first(), states: ['default'] },
  { key: 'footer-link', group: 'Footer', title: 'Footer link',
    desc: 'A link in the footer columns.',
    sel: 'footer a', find: (p) => p.locator('footer a').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'footer-legal-link', group: 'Footer', title: 'Legal link',
    desc: 'A link in the footer\'s legal row (Privacy Policy, Terms of Use).',
    sel: 'footer a (text Privacy|Terms)', find: async (p) => await domFind(p, /privacy|terms of use/i, { sel: 'footer a', tag: 'lg', minW: 40, minH: 10 }), states: ['default', 'hover'] },
  { key: 'lang-selector', group: 'Footer', title: 'Language selector',
    desc: 'The "English" selector in the footer. "opened" is its own press listing the locales — a local UI toggle, no locale is switched.',
    sel: '[class*="language" i] button, footer button:has-text("English")',
    find: (p) => p.locator('[class*="language" i] button, footer button').filter({ hasText: /english/i }).filter({ visible: true }).first(),
    states: ['default', 'hover', { name: 'opened', via: 'the selector\'s own press — the locale list opened, nothing chosen', fn: async (loc) => { await loc.click({ timeout: 5000, force: true }); await page.waitForTimeout(1100); } }] },
];

// Detail-page parts: the backdrop hero, the title, the meta row, the CTA.
const DETAIL = [
  { key: 'detail-hero', group: 'Title detail', title: 'Detail backdrop hero',
    desc: 'The full-bleed backdrop area on a title detail page.',
    sel: '[class*="hero" i], [class*="backdrop" i], [class*="detail" i]:has(img)', find: (p) => p.locator('[class*="hero" i], [class*="backdrop" i]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'detail-title', group: 'Title detail', title: 'Title heading',
    desc: 'The title\'s display heading on the detail page.',
    sel: 'h1', find: (p) => p.locator('h1').filter({ visible: true }).first(), states: ['default'] },
  { key: 'detail-meta', group: 'Title detail', title: 'Meta row',
    desc: 'The year · rating · runtime/seasons line under the title.',
    sel: '[class*="meta" i], h1 ~ *', find: (p) => p.locator('[class*="meta" i]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'detail-cta', group: 'Title detail', title: 'Detail "Start Subscription" CTA',
    desc: 'The subscribe call-to-action on a title page — an auth link, hovered and focused only.',
    sel: 'a (text Start Subscription|Subscribe)', find: async (p) => await domFind(p, /start subscription|subscribe now|sign up/i, { sel: 'a, button', tag: 'dc', minW: 60, minH: 24 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
];

// The legal surface (privacy page): heading, paragraph, inline link.
const LEGAL = [
  { key: 'legal-h1', page: 'privacy', group: 'Legal prose', title: 'Legal page title',
    desc: 'The "Privacy Policy" heading.', sel: 'main h1, h1', find: (p) => p.locator('main h1, h1').filter({ visible: true }).first(), states: ['default'] },
  { key: 'legal-p', page: 'privacy', group: 'Legal prose', title: 'Legal paragraph',
    desc: 'A body paragraph of the policy.', sel: 'main p, article p, p', find: (p) => p.locator('main p, article p, p').filter({ visible: true }).first(), states: ['default'] },
  { key: 'legal-link', page: 'privacy', group: 'Legal prose', title: 'Legal inline link',
    desc: 'A link inside the policy prose.', sel: 'main p a, article a', find: (p) => p.locator('main p a, article a, main a').filter({ visible: true }).first(), states: ['default', 'hover'] },
];

// The consent modal is measured against a fresh, uncontested load — the
// dialog is left up on purpose and its buttons are never pressed.
const CONSENT_SETUP = async (p) => { await p.waitForTimeout(4000); };
const CONSENT = [
  { key: 'consent-dialog', group: 'Cookie consent', title: 'Consent modal',
    desc: 'The cookie-preferences modal that opens over a fresh visit — measured as loaded, never accepted or rejected (closePromo hides it for the other groups).',
    // The Bootstrap .modal is the dialog itself; a bare [class*="consent" i]
    // first matches inner containers (consent-description-container).
    sel: '.modal, [role="dialog"], [class*="consent" i][class*="modal" i]', find: (p) => p.locator('.modal, [role="dialog"], [class*="consent" i][class*="modal" i]').filter({ visible: true }).last(), states: ['default'] },
  { key: 'consent-accept', group: 'Cookie consent', title: '"Accept All Cookies" button',
    desc: 'The primary consent button — styles only, never pressed.',
    sel: 'button (text Accept)', find: async (p) => await domFind(p, /accept/i, { sel: 'button', tag: 'ac', minW: 60, minH: 24 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'consent-manage', group: 'Cookie consent', title: '"Manage" / "Reject" control',
    desc: 'A secondary consent control — styles only, never pressed.',
    sel: 'button (text Manage|Reject|Settings)', find: async (p) => await domFind(p, /manage|reject|settings/i, { sel: 'button, a', tag: 'mg', minW: 60, minH: 20 }), states: ['default', 'hover'] },
];

// The consent group must run with promo left open.
const MOBILE = [
  { key: 'm-header', group: 'Site chrome (mobile)', title: 'Mobile navbar',
    desc: 'The navbar at 390px: wordmark, menu button, Sign In.', sel: 'header nav, nav',
    find: (p) => p.locator('header nav, nav').filter({ visible: true }).first(), states: ['default'] },
  { key: 'm-menu-button', group: 'Site chrome (mobile)', title: 'Mobile menu button',
    desc: 'The button that opens the nav at 390px.', sel: 'nav button, header button',
    find: (p) => p.locator('nav button, header button').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'm-nav-open', group: 'Site chrome (mobile)', title: 'Mobile nav (open)',
    desc: 'The navigation opened by the menu button\'s own press.',
    sel: '[class*="drawer" i], [class*="menu" i][class*="open" i], nav ul', find: async (p) => {
      const btn = p.locator('nav button, header button').filter({ visible: true }).first();
      await btn.click({ timeout: 5000 }).catch(() => {});
      await p.waitForTimeout(1300);
      return p.locator('[class*="drawer" i], [class*="open" i], nav ul').filter({ visible: true }).first();
    }, states: [{ name: 'opened', via: 'the mobile menu button\'s own press', fn: async () => {} }] },
  { key: 'm-hero-cta', group: 'Site chrome (mobile)', title: 'Slide CTA at 390px',
    desc: 'The "Start Subscription" pill under the hero at phone width.',
    sel: 'a (text Start Subscription)', find: async (p) => await domFind(p, /start subscription|subscribe/i, { sel: 'a', tag: 'mh', minW: 60, minH: 24 }), states: ['default'] },
];

const GROUPS = {
  home: { page: 'home', specs: [...CHROME, ...HERO, ...PLANS, ...FAQ, ...RAIL, ...FOOTER] },
  detail: { page: 'show', specs: DETAIL },
  // The movie group gets its own key prefix — sharing detail-* keys would let
  // a failed movie rerun leave the earlier show readings under the movie's
  // page/url, and a successful one would overwrite the show's evidence.
  'detail-movie': { page: 'movie', specs: DETAIL.map((s) => ({ ...s, key: 'movie-' + s.key })) },
  movies: { page: 'movies', specs: RAIL.map((s) => ({ ...s, key: 'browse-' + s.key, desc: s.desc.replace('rail', 'browse row') })) },
  legal: { page: 'privacy', specs: LEGAL },
  consent: { page: 'home', promo: 'keep', setup: CONSENT_SETUP, specs: CONSENT },
  mobile: { page: 'home', mobile: true, specs: MOBILE },
};

// ---------- runner ----------

const b = await chromium.launch({ headless: process.env.HEADLESS === '1' });
context = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
await patch(context);
const mobCtx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
await patch(mobCtx);

const wanted = process.argv.slice(2);
out._meta.read = new Date().toLocaleDateString('en-CA');
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); www.hbomax.com paints a single dark theme (html data-theme="max") — there is no light surface to measure';
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
  const url = BASE + URLS[g.page];
  log('open', key, g.mobile ? '(mobile)' : '', url);
  if (!(await open(page, url, { wait: 7000, promo: g.promo ?? 'close' }))) { log('  group skipped: the page never loaded'); await page.close().catch(() => {}); continue; }
  // A Chromium network-error page must never be measured: it paints its own
  // h1/p ("Your connection was interrupted", "A network change was detected")
  // which would be committed as the site's legal prose. Reload once; if the
  // error persists the group's specs are left absent, not filled with the
  // error page's text.
  const ERR_TEXT = /your connection was interrupted|a network change was detected|this site can.t be reached/i;
  if (ERR_TEXT.test(await page.evaluate(() => document.body?.innerText || '').catch(() => ''))) {
    log('  error page detected — reloading', url);
    await page.reload({ waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await page.waitForTimeout(7000);
    if (ERR_TEXT.test(await page.evaluate(() => document.body?.innerText || '').catch(() => ''))) {
      log('  error page persists — group skipped');
      await page.close().catch(() => {});
      continue;
    }
  }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  if (g.setup) await g.setup(page).catch((e) => log('  setup failed:', e.message));
  // the readable sheets' transition declarations, for measurements.md
  out._meta.sheets[URLS[g.page]] = await page.evaluate(() => {
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
    comp.page = URLS[g.page];
    comp.url = safeUrl(url);
    comp.run = new Date().toISOString();
    comp.states ??= {};
    let loc;
    // A lookup miss must not erase states a previous run already measured —
    // only a component with no good readings at all counts as missing.
    const hasStates = () => Object.values(comp.states ?? {}).some((s) => s && s.style);
    try { loc = await spec.find(page); } catch (e) {
      log(' ', spec.key, 'find failed:', e.message.split('\n')[0]);
      if (hasStates()) comp.recaptureMissed = e.message.split('\n')[0]; else comp.missing = true;
      continue;
    }
    if (!(await loc.count()) || !(await loc.first().isVisible().catch(() => false))) {
      log(' ', spec.key, 'absent');
      if (hasStates()) comp.recaptureMissed = 'absent on this run'; else comp.missing = true;
      continue;
    }
    delete comp.missing;
    delete comp.recaptureMissed;
    loc = loc.first();
    for (const st of spec.states) {
      const name = typeof st === 'string' ? st : (st.name || 'opened');
      // pressed/dark are cleared in finally so a failed read can never leak
      // the forced state into the next measurement.
      let pressed = null;
      let darkOn = false;
      try {
        await reset();
        let viaText = 'resting state';
        if (st === 'hover') { await hover(loc); viaText = via.hover; }
        else if (st === 'focus-visible') {
          await kbFocus(loc);
          // A reading is only a focus state if the keyboard pass actually
          // landed on the target — otherwise it is recorded as a failed
          // attempt (build_components_md treats 'focus failed' as not a
          // state, so a miss can never read as a measured absence).
          const focused = await loc.evaluate((el) => el === document.activeElement || el.contains(document.activeElement)).catch(() => false);
          viaText = focused ? via['focus-visible'] : 'focus failed';
        }
        else if (st === 'focused') { await loc.click({ timeout: 3000 }).catch(() => loc.evaluate((el) => el.focus())); await page.waitForTimeout(400); viaText = 'the field clicked into'; }
        else if (st === 'pressed') { pressed = await pressOn(loc); viaText = via.pressed; }
        else if (st === 'dark') { if (!(await setTheme(page, 'dark'))) { log(' ', spec.key, name, 'dark never painted — skipped'); continue; } darkOn = true; viaText = via.dark; }
        else if (st && typeof st === 'object' && st.fn) { await st.fn(loc); viaText = st.via || 'reached by the component\'s own UI toggle'; }
        else if (typeof st === 'function') { await st(loc); viaText = 'reached by the component\'s own UI toggle'; }
        await centre(loc).catch(() => {});
        const v = await styleOf(loc);
        v.via = viaText;
        v.crop = await crop(page, loc, `${spec.key}-${name}`).catch((e) => { log('  crop failed', spec.key, name, e.message.split('\n')[0]); return undefined; });
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
        if (darkOn) await setTheme(page, 'light').catch(() => {});
      }
    }
    save();
  }
  if (g.teardown) await g.teardown(page).catch(() => {});
  await setTheme(page, 'light').catch(() => {});
  await page.close();
}
await b.close();
log('done ->', OUT);
