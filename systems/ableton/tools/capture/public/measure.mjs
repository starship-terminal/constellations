// Measures ableton.com's public marketing components in every state reachable
// without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home live push move note link packs shop trial blog about help jobs
// login mobile. Writes raw/components-computed.json (merged, so a subset of
// pages can be re-run) and one crop per component and state into
// components/crops/. raw/measurements.md is then built from the JSON by
// build-measurements.mjs.
//
// ableton.com is a server-rendered site with stable BEM classes
// (.main-nav__*, .abl-button, .blog-teaser, .product-teaser). Nothing is sent,
// bought, downloaded or signed into: the only presses are local UI toggles —
// the nav's "More" disclosure and a "Discover more" collapse. The consent
// bar is re-shown for measurement after being hidden, never answered; the
// login/register forms and newsletter form are measured at rest and focused
// only (no submit); shop's Add-to-cart, trial's Download and the packs'
// Download buttons are measured, never followed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, open, closePromo, killGeo, domClick, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/en/',
  live: '/en/live/',
  push: '/en/push/',
  move: '/en/move/',
  note: '/en/note/',
  link: '/en/link/',
  packs: '/en/packs/',
  shop: '/en/shop/',
  trial: '/en/trial/',
  blog: '/en/blog/',
  about: '/en/about/',
  help: '/en/help/',
  jobs: '/en/jobs/',
  login: '/en/login/',
};
let page, cdp, current, context, run;
const touched = new Set();

// A bot interstitial or an error body renders a minimal page: detect either
// so a blocked load is skipped, not measured.
async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /something went wrong|performing security verification|verifying you are human|just a moment|^not found$/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

// ---------- helpers ----------

async function newPage(key, { mobile = false, promo = 'close', wait = 6000 } = {}) {
  current = key;
  const b = context.browser();
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  // bot check: recorded as a boundary, not bypassed (navigator.webdriver is left as Chromium sets it)
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  page.setDefaultTimeout(8000);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '');
  for (let attempt = 0; attempt < 3; attempt++) {
    await open(page, URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { wait, promo });
    if (!(await blocked())) break;
    log('  blocked pass', attempt + 1, '- reloading');
  }
  if (await blocked()) { log('  BLOCKED', key); return false; }
  if (promo === 'close') await killGeo(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
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

// Clicks a UI toggle (disclosure, collapse). Refuses a submit button, a link,
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign up|sign in|log in|register|create|buy|buy now|checkout|pay|purchase|add to cart|download|subscribe|share|accept|close|more info|start free trial|try|upgrade|open|continue|get started)$/i;
async function toggle(loc) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || t.tag === 'A') throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, run, url: URLS[current] && (URLS[current].startsWith('http') ? URLS[current] : BASE + URLS[current]) }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
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

// Records the listed states of one component. meta: title, group, desc, sel.
async function S(key, target, list, meta = {}, opts = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  delete out.components[key].missing;
  if (opts.open) { await reset(); await opts.open(); }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
    if (!has) out.components[key].missing = true;
    return;
  }
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
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).filter({ visible: true }).first(), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await (opts.fieldLoc || loc).filter({ visible: true }).first().click({ timeout: 4000 });
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'open') {
        // A resting state the page itself can be put in: a disclosure opened
        // once by its own button (opts.open) or already open.
        via = opts.via || 'resting state after a local toggle';
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

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Transitions and animations declared in every readable sheet, by selector.
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

// Re-shows the consent bar for measurement (it is hidden by the tour sweep),
// then returns; callers hide it again afterwards.
async function showCookie() {
  await page.evaluate(() => { const el = document.querySelector('#biscuits-overlay'); if (el) { el.style.display = ''; el.scrollIntoView(); } });
  await page.waitForTimeout(400);
}
async function hideCookie() {
  await page.evaluate(() => { const el = document.querySelector('#biscuits-overlay'); if (el) el.style.display = 'none'; });
}

// ---------- page runs ----------
const G = {
  shell: 'Shell and navigation', consent: 'Consent overlay', home: 'Home',
  live: 'Live page', trial: 'Trial page', shop: 'Shop', packs: 'Packs',
  blog: 'Blog', login: 'Log in / register (resting only)',
  misc: 'Content pages', mobile: 'Mobile (390 wide)',
};

async function shell(ctxPage = 'home') {
  const g = G.shell;
  await S('nav-bar', q('header.main-nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Top navigation bar', desc: 'The white top bar: the Ableton logo (the grid mark), product links (Live / Push / Move / Note / Link / Shop / Packs / Help), the "More" disclosure, "Try Live 12 for free" in blue and "Log in or register".', sel: 'header.main-nav' }, { noScroll: true });
  await S('nav-logo', q('.main-nav__logo a, a.main-nav__logo').filter({ visible: true }).first(), B4, { group: g, title: 'Logo', desc: 'The Ableton grid-mark wordmark linking home.', sel: '.main-nav__logo' }, { noScroll: true });
  await S('nav-link', q('.main-nav__link-list__item a:has-text("Live"), .main-nav__link-list__link:has-text("Live"), .main-nav a:has-text("Push")').filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A product link in the top bar.', sel: '.main-nav__link-list__link' }, { noScroll: true });
  await S('nav-more', q('.js-main-nav-more-button').filter({ visible: true }).first(), B4, { group: g, title: 'More button', desc: 'The "More +" disclosure button opening the extended menu.', sel: '.js-main-nav-more-button' }, { noScroll: true });
  // open the More menu, measure the panel, then a link inside it
  const more = q('.js-main-nav-more-button').filter({ visible: true }).first();
  if (await more.count()) {
    await more.click().catch(() => {});
    await page.waitForTimeout(900);
    await S('nav-more-panel', q('.main-nav__more').filter({ visible: true }).first(), ['open'], { group: g, title: 'More menu panel', desc: 'The expanded "More" menu: "More on Ableton.com" link row plus "More from Ableton" cards (Ableton Learn, Learning Synths, Making Music).', sel: '.main-nav__more' }, { noScroll: true, via: 'More button pressed; local disclosure, nothing navigated' });
    await S('nav-more-link', q('.main-nav__more a').filter({ hasText: 'Blog' }).first(), ['open', 'hover'], { group: g, title: 'More menu link', desc: 'A link inside the expanded More menu.', sel: '.main-nav__more a' }, { noScroll: true, via: 'menu open' });
    await more.click().catch(() => {});
    await page.waitForTimeout(400);
  }
  await S('nav-trial-cta', q('a').filter({ hasText: 'Try Live 12 for free' }).first(), B4, { group: g, title: 'Trial CTA link', desc: 'The blue "Try Live 12 for free" link at the right end of the top bar; links to /en/trial/. Hovered and focused only.', sel: 'nav trial link' }, { noScroll: true });
  await S('nav-login', q('a').filter({ hasText: 'Log in or register' }).first(), B4, { group: g, title: 'Log in link', desc: '"Log in or register" in the top bar; links to /en/login/. Hovered and focused only.', sel: 'nav login link' }, { noScroll: true });
}

async function home() {
  if (!(await newPage('home'))) { await page.close(); return; }
  await sheetsFor('home');
  await shell('home');
  const h = G.home;
  await S('hero-teaser', q('.homepage-teaser').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero teaser', desc: 'The lead tile of the home grid: a photo/video cell with a large white headline and a "See what\'s new" link.', sel: '.homepage-teaser' }, { noScroll: true });
  await S('hero-title', q('.homepage-teaser__primary-headline').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The white display headline over the hero media.', sel: '.homepage-teaser__primary-headline' }, { noScroll: true });
  await S('hero-cta', q('.homepage-teaser__cta, .homepage-teaser a.has-arrow').filter({ visible: true }).first(), B4, { group: h, title: 'Hero link', desc: '"See what\'s new" — the arrow link under the hero headline.', sel: '.homepage-teaser__cta' }, { noScroll: true });
  await S('home-cell', q('.homepage-grid .cell, .cell').filter({ visible: true }).first(), ['default'], { group: h, title: 'Grid cell', desc: 'One tile of the loose homepage grid: the layout mixes image cells and text-on-white cells.', sel: '.cell' });
  await S('home-promo-card', await domFind(page, /rent-to-own|spread the cost/i, { sel: '.cell, .homepage-teaser, [class*="cell"]', tag: 'hp', leaf: false, minW: 200, minH: 100 }), ['default'], { group: h, title: 'Promo card', desc: 'A text-on-tint promo cell in the grid (the rent-to-own card on lime stripes).', sel: 'promo cell' });
  await S('scroll-down', q('.homepage-grid__anchor, .js-homepage-grid-anchor').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Scroll-down button', desc: 'The blue chevron button pinned under the first screen; an in-page anchor, measured at rest.', sel: '.homepage-grid__anchor' });
  await S('panel-title', q('.panel-blog-teasers__headline').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section headline', desc: 'A section headline over a blog-teaser row ("From the blog" and friends).', sel: '.panel-blog-teasers__headline' });
  await S('blog-teaser', q('.blog-teaser').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Blog teaser card', desc: 'An article teaser in the home/blog rows: media cell, category tag and headline.', sel: '.blog-teaser' });
  await S('blog-teaser-title', q('.blog-teaser__headline').filter({ visible: true }).first(), ['default'], { group: h, title: 'Blog teaser headline', sel: '.blog-teaser__headline' });
  await S('blog-teaser-tag', q('.blog-teaser__category').filter({ visible: true }).first(), ['default'], { group: h, title: 'Blog teaser category', sel: '.blog-teaser__category' });
  await S('panel-cat-link', q('.panel-blog-teasers__link, .panel-blog-categories__item a').filter({ visible: true }).first(), B4, { group: h, title: 'Category link', desc: 'A blog category filter link under a teasers panel.', sel: '.panel-blog-teasers__link' });
  await footer();
  await cookie();
  await page.close();
}

async function footer() {
  const g = G.shell;
  await S('footer', q('footer.main-footer, .main-footer').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer', desc: 'The page footer: link columns, the newsletter form, social buttons, the language and location selectors and the legal row.', sel: '.main-footer' });
  await S('footer-heading', q('.main-footer__h3').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer column heading', sel: '.main-footer__h3' });
  await S('footer-link', q('.main-footer__secondary__link-list__item a, .main-footer__list a').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: '.main-footer a' });
  await S('footer-social', q('.main-footer__social-button').filter({ visible: true }).first(), B4, { group: g, title: 'Social icon link', desc: 'One of the social-icon links (Facebook, X, YouTube, Instagram, TikTok, Discord).', sel: '.main-footer__social-button' });
  await S('newsletter-field', q('.main-footer__newsletter__form input[type="email"], form[action*="subscribe"] input[type="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Newsletter email field', desc: 'The email field of the footer newsletter form; clicked into, nothing typed or sent.', sel: '.main-footer__newsletter__form input[type=email]' });
  await S('newsletter-submit', q('.main-footer__button, form[action*="subscribe"] [type="submit"]').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Newsletter sign-up button', desc: 'The "Sign up" button of the footer newsletter form. Measured, never pressed.', sel: '.main-footer__button' });
  await S('footer-locale', q('.main-footer__secondary__select, form[action*="set-language"] select').filter({ visible: true }).first(), ['default'], { group: g, title: 'Language selector', desc: 'The footer language <select>.', sel: '.main-footer__secondary__select' });
}

async function cookie() {
  const g = G.consent;
  await showCookie();
  await S('cookie-bar', q('#biscuits-overlay .bg-black, #biscuits-overlay [class*="bg-"]').filter({ visible: true }).first(), ['open'], { group: g, title: 'Cookie consent card', desc: 'The black consent card fixed at the bottom left: "Clicking Accept means you consent…" copy with Accept (blue), Close and More info buttons. Re-shown for the measurement, never answered.', sel: '#biscuits-overlay .bg-black' }, { noScroll: true, via: 're-shown after the sweep hid it' });
  await S('cookie-accept', q('#biscuits-accept-button').filter({ visible: true }).first(), B4, { group: g, title: 'Accept button', desc: 'The blue "Accept" button of the consent card. Measured in every state — never pressed (it would post consent).', sel: '#biscuits-accept-button' }, { noScroll: true });
  await S('cookie-close', q('#biscuits-overlay .abl-button--outline').filter({ hasText: 'Close' }).first(), B4, { group: g, title: 'Close button', desc: 'The outline "Close" button, which denies consent. Measured, never pressed.', sel: '#biscuits-overlay .abl-button--outline' }, { noScroll: true });
  await S('cookie-more-info', q('#biscuits-overlay a').filter({ hasText: 'More info' }).first(), B4, { group: g, title: 'More info link', desc: '"More info" — the outline link to /en/cookie-settings/. Hovered and focused only.', sel: '#biscuits-overlay a' }, { noScroll: true });
  await hideCookie();
}

async function live() {
  if (!(await newPage('live'))) { await page.close(); return; }
  await sheetsFor('live');
  const g = G.live;
  await S('live-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', desc: '"Find … in Ableton Live" — the product page title in the largest abl-type step.', sel: 'h1' }, { noScroll: true });
  await S('live-section-title', q('h1.abl-type-30, h1[class*="abl-type-60"], h1[class*="abl-type-90"]').filter({ visible: true }).nth(1), ['default'], { group: g, title: 'Section title', desc: 'A big section heading ("Play freely with ideas").', sel: 'h1.abl-type-*' });
  await S('btn-try', q('a.boxed-btn').filter({ hasText: 'Try Live 12 for free' }).first(), B4, { group: g, title: 'Try-for-free button', desc: 'The boxed "Try Live 12 for free" button on the product page; links to /en/trial/. Hovered and focused only.', sel: 'a.boxed-btn' });
  await S('btn-buy', q('a.boxed-btn').filter({ hasText: 'Buy now' }).first(), B4, { group: g, title: 'Buy now button', desc: 'The boxed "Buy now" button; links to the shop. Hovered and focused only.', sel: 'a.boxed-btn' });
  await S('btn-video', q('a.abl-button.abl-cl-white, .abl-button.abl-bg-overlay-button').filter({ hasText: /Play/i }).first(), ['default', 'hover'], { group: g, title: 'Video play button', desc: 'The "Play: VIDEO" overlay button on a demo clip. Hovered only — pressing plays the video.', sel: '.abl-bg-overlay-button' });
  await S('btn-audio', q('.js-simple-audio-play-button').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Audio play button', desc: 'A "Play: <sound>" button on an audio example. Hovered only — pressing plays audio.', sel: '.js-simple-audio-play-button' });
  await S('anchor-link', q('.nav-anchor-link').filter({ visible: true }).first(), B4, { group: g, title: 'Anchor link', desc: 'An in-page anchor link in the feature navigation row.', sel: '.nav-anchor-link' });
  // The "Discover more … sounds" collapse is a local expander.
  const col = q('.nav-button-link.collapsed, a.nav-button-link[data-toggle], a[data-toggle="collapse"]').filter({ hasText: /Discover more/i }).first();
  await S('collapse-toggle', col, ['default', 'hover'], { group: g, title: 'Discover-more collapse', desc: 'A "Discover more … sounds" collapsed-content toggle.', sel: '.nav-button-link.collapsed' });
  if (await col.count()) {
    await col.click().catch(() => col.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    await S('collapse-toggle-open', col, ['open'], { group: g, title: 'Discover-more collapse (open)', desc: 'The same toggle after being pressed once; client-side expand, nothing sent.', sel: '.nav-button-link' }, { via: 'pressed once to expand' });
  }
  await page.close();
}

async function product(key) {
  if (!(await newPage(key))) { await page.close(); return; }
  await sheetsFor(key);
  const g = G.misc;
  await S(`${key}-title`, q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: `${key[0].toUpperCase() + key.slice(1)} page title`, sel: 'h1' }, { noScroll: true });
  await S(`${key}-cta`, q('a.boxed-btn, a.abl-button--primary, a.has-arrow').filter({ visible: true }).first(), B4, { group: g, title: `${key} primary CTA`, desc: 'The page\'s main call-to-action (a boxed button, or an arrow link on Link).', sel: 'a.boxed-btn / a.has-arrow' });
  await page.close();
}

async function trial() {
  if (!(await newPage('trial'))) { await page.close(); return; }
  await sheetsFor('trial');
  const g = G.trial;
  await S('trial-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Trial page title', desc: '"Start your free trial of Ableton Live" in the heading_l style.', sel: 'h1' }, { noScroll: true });
  await S('trial-download', q('.test-download-lite-button, a.abl-button--primary').filter({ hasText: 'Download' }).first(), B4, { group: g, title: 'Download button', desc: 'A "Download" button for a trial edition. Measured, never pressed — the download would start.', sel: '.test-download-lite-button' });
  await S('trial-edition-card', await domFind(page, /live 12 (suite|standard|intro)|edition/i, { sel: 'div, section, [class*="card"], [class*="edition"], [class*="panel"]', tag: 'te', leaf: true, minW: 200, minH: 80 }), ['default'], { group: g, title: 'Trial edition panel', desc: 'A panel choosing between the Live editions for the trial.', sel: 'edition panel' });
  await page.close();
}

async function shop() {
  if (!(await newPage('shop'))) { await page.close(); return; }
  await sheetsFor('shop');
  const g = G.shop;
  await S('shop-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Shop page title', sel: 'h1' }, { noScroll: true });
  await S('product-card', q('.product-teaser').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Product teaser card', desc: 'A product tile in the shop grid (Live editions, Push, merchandise).', sel: '.product-teaser' });
  await S('product-price', q('.price').filter({ visible: true }).first(), ['default'], { group: g, title: 'Price', desc: 'A product price in the shop.', sel: '.price' });
  await S('add-to-cart', q('.add_to_cart, a.btn').filter({ visible: true }).first(), B4, { group: g, title: 'Add-to-cart button', desc: 'The buy control on a shop tile. Measured, never pressed — pressing carts a product.', sel: '.add_to_cart' });
  await page.close();
}

async function packs() {
  if (!(await newPage('packs'))) { await page.close(); return; }
  await sheetsFor('packs');
  const g = G.packs;
  await S('packs-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Packs page title', sel: 'h1' }, { noScroll: true });
  await S('pack-card', await domFind(page, /pack|bundle|live 12/i, { sel: '[class*="pack"], [class*="teaser"], [class*="card"], .cell', tag: 'pc', leaf: true, minW: 150, minH: 120 }), ['default', 'hover'], { group: g, title: 'Pack card', desc: 'A Pack tile in the catalogue grid.', sel: 'pack teaser' });
  await S('pack-download', q('.test-pack-download').filter({ visible: true }).first(), B4, { group: g, title: 'Pack download button', desc: 'A "Download" button on a Pack row; links to /en/login/ (the download needs an account). Measured, never followed.', sel: '.test-pack-download' });
  await page.close();
}

async function blog() {
  if (!(await newPage('blog'))) { await page.close(); return; }
  await sheetsFor('blog');
  const g = G.blog;
  await S('blog-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Blog page title', sel: 'h1' }, { noScroll: true });
  await S('blog-row', q('.blog-teaser, article, [class*="blog-list"] > *, [class*="teaser"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Article teaser', desc: 'An article row in the blog index.', sel: '.blog-teaser' });
  await S('blog-category-badge', q('.abl-entry-category-badge').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Entry category badge', desc: 'The coloured category badge on a blog index row (Artists / Downloads / Tutorials).', sel: '.abl-entry-category-badge' });
  await page.close();
}

async function misc(key) {
  if (!(await newPage(key))) { await page.close(); return; }
  await sheetsFor(key);
  const g = G.misc;
  await S(`${key}-title`, q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: `${key[0].toUpperCase() + key.slice(1)} title`, sel: 'h1' }, { noScroll: true });
  await S(`${key}-body`, await domFind(page, /./, { sel: 'main p, [class*="body-text"], p', tag: 'bd', minH: 30, minW: 200 }), ['default'], { group: g, title: `${key} body text`, sel: 'body p' });
  await page.close();
}

async function login() {
  if (!(await newPage('login'))) { await page.close(); return; }
  await sheetsFor('login');
  const g = G.login;
  await S('login-title', q('h1.section__headline').filter({ hasText: 'Log in' }).first(), ['default'], { group: g, title: 'Log in title', sel: 'h1.section__headline' }, { noScroll: true });
  await S('login-form', q('form.test-login-form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Log in form', desc: 'The Log in card: username and password fields plus the submit. Measured at rest — nothing typed, nothing submitted.', sel: 'form.test-login-form' });
  await S('login-field', q('form.test-login-form input[name="username"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Username field', desc: 'The username text field. Clicked into for the focus style; nothing typed.', sel: 'input[name=username]' });
  await S('login-submit', q('form.test-login-form [type="submit"], form.test-login-form button').filter({ visible: true }).first(), B4, { group: g, title: 'Log in button', desc: 'The form\'s submit. Measured in every state — never pressed.', sel: 'login submit' });
  await S('register-form', q('form.test-registration-form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Register form', desc: 'The Register card beside Log in: email, password, names, country select and a newsletter checkbox. Measured at rest.', sel: 'form.test-registration-form' });
  await S('register-field', q('form.test-registration-form input[type="email"], form.test-registration-form input[name="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Register email field', desc: 'The email field of the register form. Clicked into only.', sel: 'register email' });
  await S('register-select', q('form.test-registration-form select[name="country"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Country select', sel: 'select[name=country]' });
  await S('register-checkbox', q('form.test-registration-form input[type="checkbox"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Newsletter checkbox', sel: 'register checkbox' });
  await page.close();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) { await page.close(); return; }
  const g = G.mobile;
  await closePromo(page);
  await S('m-nav-bar', q('header.main-nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The mobile header: logo left, menu trigger right.', sel: 'header.main-nav' }, { noScroll: true });
  await S('m-menu-trigger', q('.main-nav__trigger-label, [class*="trigger" i], button').filter({ visible: true }).first(), ['default', 'pressed'], { group: g, title: 'Mobile menu trigger', desc: 'The mobile menu button. Measured, not opened.', sel: 'menu trigger' }, { noScroll: true });
  await S('m-hero-title', q('.homepage-teaser__primary-headline, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', sel: '.homepage-teaser__primary-headline' }, { noScroll: true });
  await S('m-trial-cta', q('a').filter({ hasText: 'Try Live 12 for free' }).first(), ['default', 'pressed'], { group: g, title: 'Mobile trial CTA', sel: 'mobile trial cta' }, { noScroll: true });
  await page.close();
}

const RUNNERS = { home, live, push: () => product('push'), move: () => product('move'), note: () => product('note'), link: () => product('link'), trial, shop, packs, blog, about: () => misc('about'), help: () => misc('help'), jobs: () => misc('jobs'), login, mobile };
run = new Date().toISOString();
out._meta.run = run;
out._meta.product = 'ableton.com';
const wanted = process.argv.slice(2).join(',').split(',').map((s) => s.trim()).filter(Boolean);
({ context } = await launch());
for (const [k, fn] of Object.entries(RUNNERS)) {
  if (wanted.length && !wanted.includes(k)) continue;
  try { await fn(); } catch (e) { log('PAGE FAILED', k, String(e.message).split('\n')[0]); }
  save();
}
// mark components from this run whose selectors matched nothing; a component
// with recorded states (from an earlier merged run) is covered, not missing
for (const [k, c] of Object.entries(out.components)) {
  if (!touched.has(k)) continue;
  if (Object.keys(c.states || {}).length) delete c.missing;
  else c.missing = true;
}
save();
log('done ->', OUT);
