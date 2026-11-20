// Measures aboard.com's public marketing components in every state reachable
// without signing in, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home how-we-work case-studies case-study foundry perspectives
// newsletter podcast podcast-episode events media about faq careers security
// aboard-sign mobile. Writes raw/components-computed.json (merged, so a subset
// of pages can be re-run) and one crop per component and state into
// components/crops/. raw/measurements.md is then built from the JSON by
// build-measurements.mjs.
//
// aboard.com is WordPress with Tailwind-style utilities plus .rd-* theme
// classes. Nothing is sent or submitted: the only presses are local UI
// toggles — the FAQ accordion headings and the mobile menu trigger. The
// CookieYes consent strip is re-shown for measurement after being hidden,
// never answered; the newsletter signup forms are measured at rest and
// focused only (no address typed, no submit).
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
  home: '/',
  'how-we-work': '/how-we-work/',
  'case-studies': '/case-studies/',
  'case-study': '/case-studies/city-of-boston-scheduling-app/',
  foundry: '/foundry/',
  perspectives: '/perspectives/',
  newsletter: '/newsletter/',
  podcast: '/podcast/',
  'podcast-episode': '/podcast/jason-goldman-from-vc-pitches-to-ai-kill-switches/',
  events: '/events/',
  media: '/media/',
  about: '/about/',
  faq: '/faq/',
  careers: '/careers/',
  security: '/security/',
  'aboard-sign': '/meet-aboard-sign/',
};
let page, cdp, current, context, run;
const tempContexts = [];
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
  tempContexts.push(ctx);
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

// Waits out the element's declared transitions instead of a fixed ms: the
// longest transition-duration + delay on the element, its pseudo-elements and
// its children, plus a buffer. A fixed 400-450ms reads mid-transition values —
// nav-cta changes over 500ms, the feed movement over 600ms.
async function settle(loc, { floor = 400, cap = 3000 } = {}) {
  const ms = await loc.evaluate((el) => {
    const maxOf = (n, pe) => {
      const c = getComputedStyle(n, pe);
      const durs = c.transitionDuration.split(',').map((x) => parseFloat(x) || 0);
      const dels = c.transitionDelay.split(',').map((x) => parseFloat(x) || 0);
      return Math.max(0, ...durs.map((d, i) => d + (dels[i % dels.length] || 0)));
    };
    let m = Math.max(maxOf(el), maxOf(el, '::before'), maxOf(el, '::after'));
    for (const n of el.querySelectorAll('*')) m = Math.max(m, maxOf(n));
    return m * 1000;
  }).catch(() => 0);
  await page.waitForTimeout(Math.max(floor, Math.min(cap, ms + 150)));
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await settle(loc);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

// Clicks a UI toggle (disclosure, collapse). Refuses a submit button, a link,
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign up|sign in|log in|register|create|buy|buy now|checkout|pay|purchase|add to cart|download|subscribe|share|accept|close|more info|start free trial|try|upgrade|open|continue|get started|get in touch|save my preferences|reject|customize)$/i;
async function toggle(loc) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || t.tag === 'A') throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, url: URLS[current] && (URLS[current].startsWith('http') ? URLS[current] : BASE + URLS[current]) }, meta);
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
    // A state actually measured gets this run's timestamp; a component whose
    // states are only kept from an earlier run keeps its original one.
    c.run = run;
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
        await settle(loc);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus((opts.focusLoc || loc).filter({ visible: true }).first());
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).filter({ visible: true }).first(), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await (opts.fieldLoc || loc).filter({ visible: true }).first().click({ timeout: 4000 });
        await settle(loc);
        via = 'clicked into the field';
      } else if (st === 'open') {
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

// Re-shows the consent strip for measurement (it is hidden by the tour
// sweep), then returns; callers hide it again afterwards.
async function showCookie() {
  await page.evaluate(() => {
    document.querySelectorAll('.cky-consent-container').forEach((el) => {
      for (let n = el; n && n !== document.body; n = n.parentElement) {
        if (n.style.display === 'none') n.style.display = '';
        if (n.style.visibility === 'hidden') n.style.visibility = '';
      }
    });
    const bar = document.querySelector('.cky-consent-container');
    if (bar) bar.scrollIntoView();
  });
  await page.waitForTimeout(400);
}
async function hideCookie() {
  await page.evaluate(() => {
    document.querySelectorAll('.cky-consent-container, .cky-modal').forEach((el) => { el.style.display = 'none'; });
  });
}

// ---------- page runs ----------
const G = {
  shell: 'Shell and navigation', consent: 'Consent overlay', home: 'Home',
  hww: 'How We Work', cases: 'Case studies', foundry: 'Foundry',
  feeds: 'Feeds: perspectives, newsletter, events, media', pod: 'Podcast',
  article: 'Article page', forms: 'Newsletter signup (resting only)',
  misc: 'About, careers, security', mobile: 'Mobile (390 wide)',
};

async function shell(ctxPage = 'home') {
  const g = G.shell;
  await S('nav-bar', q('header.site-header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Top navigation bar', desc: 'The fixed 78px header: the Aboard wordmark, the section links (How We Work / Case Studies / Foundry / Perspectives / About) and the boxed "Get in Touch" CTA.', sel: 'header.site-header' }, { noScroll: true });
  await S('nav-logo', q('a.aboard-logo, a.rd-nav-logo').filter({ visible: true }).first(), B4, { group: g, title: 'Logo', desc: 'The Aboard wordmark linking home.', sel: 'a.aboard-logo' }, { noScroll: true });
  await S('nav-link', q('nav.rd-nav a, .rd-nav-row a').filter({ hasText: 'How We Work' }).first(), B4, { group: g, title: 'Nav link', desc: 'A section link in the top bar.', sel: 'nav.rd-nav a' }, { noScroll: true });
  await S('nav-cta', q('a.rd-nav-cta').filter({ visible: true }).first(), B4, { group: g, title: 'Get-in-touch CTA', desc: 'The boxed "Get in Touch" button at the right of the nav; jumps to the contact section. Hovered and focused only.', sel: 'a.rd-nav-cta' }, { noScroll: true });
  await S('skip-link', q('a.rd-skip-link').filter({ visible: true }).first(), ['default'], { group: g, title: 'Skip link', desc: 'The fixed "Skip to content" link, offscreen until focused.', sel: 'a.rd-skip-link' }, { noScroll: true, crop: false });
  await S('footer', q('footer.rd').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer', desc: 'The bright-citrus footer: "We Can Help" display heading, the newsletter-signup iframe, link columns, the legal row and the social links.', sel: 'footer.rd' });
  await S('footer-heading', q('h2.text-rd-footer-h, footer h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer heading', desc: '"We Can Help" — the serif display heading of the citrus footer.', sel: 'h2.text-rd-footer-h' });
  await S('footer-link', q('footer a').filter({ hasText: 'How We Work' }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' });
  await S('footer-social', q('footer a').filter({ hasText: /LinkedIn|Youtube|Instagram|Facebook|X\b/ }).first(), B4, { group: g, title: 'Social link', desc: 'A social link in the footer column (LinkedIn New York / Lebanon, YouTube, Instagram, Facebook, X).', sel: 'footer social link' });
}

async function home() {
  if (!(await newPage('home'))) { await page.close(); return; }
  await sheetsFor('home');
  await shell('home');
  const h = G.home;
  await S('hero-title', q('h1.rd-words, h1.text-rd-display, h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: '"Your partner for the big AI leap" — the display headline, per-word animated (rd-words).', sel: 'h1.rd-words' }, { noScroll: true });
  await S('eyebrow', q('p.rd-eyebrow').filter({ visible: true }).first(), ['default'], { group: h, title: 'Eyebrow label', desc: 'A small caps section label ("WHAT WE DO", "PERSPECTIVES").', sel: 'p.rd-eyebrow' });
  await S('section-title', q('h2.text-rd-h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section title', desc: 'A section heading ("Your roadmap, realized", "We\'ve got opinions").', sel: 'h2.text-rd-h2' });
  await S('feed-row', q('a.rd-feed-row').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Feed row', desc: 'A content row in the home feed: kind tag, title and date in a three-column grid (EVENT / NEWSLETTER / PODCAST).', sel: 'a.rd-feed-row' });
  await S('feed-row-tag', await domFind(page, /EVENT|NEWSLETTER|PODCAST|MEDIA/i, { sel: 'a.rd-feed-row *', tag: 'ft', leaf: true, minW: 20 }), ['default'], { group: h, title: 'Feed row kind tag', desc: 'The small caps kind label on a feed row.', sel: 'rd-feed-row kind' });
  await S('carousel-tick', q('button.cc-tick').filter({ visible: true }).first(), B4, { group: h, title: 'Carousel tick', desc: 'A pagination tick of the home media carousel (cc-*); is-on marks the current one.', sel: 'button.cc-tick' });
  await S('carousel-pause', q('button.cc-pause').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Carousel pause', desc: 'The carousel\'s pause control.', sel: 'button.cc-pause' });
  await S('contact-iframe', q('iframe[src*="contact-form"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Contact iframe', desc: 'The embedded form frame in the contact section (same-origin newsletter signup). Measured as a frame; the fields inside live under Newsletter signup.', sel: 'iframe[src*=contact-form]' });
  await cookie();
  await page.close();
}

async function cookie() {
  const g = G.consent;
  await showCookie();
  await S('cookie-bar', q('.cky-consent-container').filter({ visible: true }).first(), ['open'], { group: g, title: 'Cookie consent strip', desc: 'The CookieYes strip pinned at the bottom: "We use cookies..." copy with Customize and Accept All. Re-shown for the measurement, never answered.', sel: '.cky-consent-container' }, { noScroll: true, via: 're-shown after the sweep hid it' });
  await S('cookie-accept', q('button.cky-btn-accept').filter({ visible: true }).first(), B4, { group: g, title: 'Accept-all button', desc: 'The "Accept All" button of the consent strip. Measured in every state — never pressed (it would post consent).', sel: 'button.cky-btn-accept' }, { noScroll: true });
  await S('cookie-customize', q('button.cky-btn-customize').filter({ visible: true }).first(), B4, { group: g, title: 'Customize button', desc: 'The "Customize" button, which opens the preferences modal. Measured, never pressed.', sel: 'button.cky-btn-customize' }, { noScroll: true });
  await S('cookie-close', q('button.cky-btn-close').filter({ visible: true }).first(), B4, { group: g, title: 'Consent close button', desc: 'The small close control of the consent strip. Measured, never pressed.', sel: 'button.cky-btn-close' }, { noScroll: true });
  await hideCookie();
}

async function howWeWork() {
  if (!(await newPage('how-we-work'))) { await page.close(); return; }
  await sheetsFor('how-we-work');
  const g = G.hww;
  await S('hww-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', desc: '"95% of AI software initiatives fail. Why do ours ship?" — the interior display headline.', sel: 'h1' }, { noScroll: true });
  await S('hww-card', q('h3.text-rd-card').filter({ visible: true }).first(), ['default'], { group: g, title: 'Principle card heading', desc: 'A principle card heading ("We evolved the process").', sel: 'h3.text-rd-card' });
  await S('hww-step', q('h3').filter({ hasText: /Landscape|Audit|Blueprint|Architecture|Migrate/ }).first(), ['default'], { group: g, title: 'Process step', desc: 'A step of the Landscape → Audit → Blueprint → Architecture → Migrate process row.', sel: 'h3 process step' });
  await S('hww-body', await domFind(page, /./, { sel: 'main p, [class*="article"] p, p', tag: 'hw', minH: 30, minW: 200 }), ['default'], { group: g, title: 'Body text', sel: 'body p' });
  await page.close();
}

async function caseStudies() {
  if (!(await newPage('case-studies'))) { await page.close(); return; }
  await sheetsFor('case-studies');
  const g = G.cases;
  await S('cases-title', q('h1, h2.entry-title').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', sel: 'h1' }, { noScroll: true });
  await S('case-card-feature', q('a.rd-case.rd-case-feature').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Featured case card', desc: 'The lead case-study card (the full-width SageSure feature).', sel: 'a.rd-case-feature' });
  await S('case-card', q('a.rd-case:not(.rd-case-feature)').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Case card', desc: 'A case-study card in the grid: industry tag, title, client.', sel: 'a.rd-case' });
  await S('case-tag', await domFind(page, /INSURANCE|HEALTH|TRAVEL|GOVERNMENT|CULTURE/i, { sel: 'a.rd-case *', tag: 'ct', leaf: true, minW: 20 }), ['default'], { group: g, title: 'Case industry tag', desc: 'The small caps industry label on a case card.', sel: 'rd-case tag' });
  await page.close();
}

async function caseStudy() {
  if (!(await newPage('case-study'))) { await page.close(); return; }
  await sheetsFor('case-study');
  const g = G.cases;
  await S('cs-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Case study title', desc: '"City of Boston" detail page title.', sel: 'h1' }, { noScroll: true });
  await S('cs-body', await domFind(page, /./, { sel: 'main p, article p, [class*="article"] p, p', tag: 'cb', minH: 30, minW: 200 }), ['default'], { group: g, title: 'Case study body', sel: 'article p' });
  await S('cs-meta', await domFind(page, /client|sector|deliverable|industry|year|platform/i, { sel: '[class*="meta"] *, [class*="detail"] *, li, dt, dd, span', tag: 'cm', leaf: true, minW: 40 }), ['default'], { group: g, title: 'Case study meta', desc: 'The detail page\'s fact labels (client, sector, platform).', sel: 'case meta' });
  await page.close();
}

async function foundry() {
  if (!(await newPage('foundry'))) { await page.close(); return; }
  await sheetsFor('foundry');
  const g = G.foundry;
  await S('foundry-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', desc: '"Software we build for ourselves" — the Foundry page title.', sel: 'h1' }, { noScroll: true });
  await S('foundry-card', q('.rd-fd-name').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Foundry product header', desc: 'A Foundry product header block: the product name, its date and the "Try …" link (Aboard Sign, TinyLittleOffice).', sel: '.rd-fd-name' });
  await S('foundry-figure', q('.rd-fd-shots figure, section figure').filter({ visible: true }).first(), ['default'], { group: g, title: 'Foundry figure', desc: 'A product feature figure with caption.', sel: '.rd-fd-shots figure' });
  await page.close();
}

async function feeds(key) {
  if (!(await newPage(key))) { await page.close(); return; }
  await sheetsFor(key);
  const g = G.feeds;
  await S(`${key}-title`, q('h1, h2.entry-title').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', sel: 'h1' }, { noScroll: true });
  const rowSel = key === 'events' ? 'li.rd-ev-item' : key === 'media' ? 'a.rd-media-link' : 'a.rd-feed-row, a.rd-nl-row, a.rd-nl-card, a[class*="row"]';
  await S(`${key}-row`, q(rowSel).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Index row', desc: 'A content row/card on the index (date, title, thumbnail).', sel: rowSel });
  await S(`${key}-row-title`, q('h3.rd-nl-row-title, h3.rd-nl-card-title, .rd-feed-row h3, .rd-ev-item h3, .rd-media-link h3, h3').filter({ visible: true }).first(), ['default'], { group: g, title: 'Row title', sel: 'row title' });
  if (key === 'newsletter') {
    const f = G.forms;
    await S('nl-form', q('form.rd-nl-form').filter({ visible: true }).first(), ['default'], { group: f, title: 'Newsletter form', desc: 'The "Email address + Subscribe" signup (dark variant on the newsletter page). Posts to /wp-json/aboard/v1/newsletter-signups — measured at rest, never submitted.', sel: 'form.rd-nl-form' });
    await S('nl-field', q('form.rd-nl-form input[type="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: f, title: 'Newsletter email field', desc: 'The email input. Clicked into for the focus style; nothing typed.', sel: 'input[type=email]' });
    await S('nl-submit', q('form.rd-nl-form [type="submit"], form.rd-nl-form button').filter({ visible: true }).first(), B4, { group: f, title: 'Subscribe button', desc: 'The Subscribe submit. Measured in every state — never pressed.', sel: 'newsletter submit' });
    await S('nl-latest-title', q('.rd-nl-latest-title').filter({ visible: true }).first(), ['default'], { group: f, title: 'Latest issue title', desc: '"Meet Aboard Sign" — the latest-issue headline.', sel: '.rd-nl-latest-title' });
  }
  if (key === 'events') {
    await S('ev-tag', await domFind(page, /OFFICE HOURS/i, { sel: 'li.rd-ev-item *', tag: 'et', leaf: true, minW: 20 }), ['default'], { group: g, title: 'Event kind tag', desc: 'The "OFFICE HOURS" caps tag on an event card.', sel: 'event tag' });
    const f = G.forms;
    await S('ev-field', q('input[type="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: f, title: 'Events email field', desc: 'The email field of the events signup row; clicked into, nothing typed.', sel: 'events input[type=email]' });
    await S('ev-submit', q('button.rd-ev-submit').filter({ visible: true }).first(), B4, { group: f, title: 'Events submit button', desc: 'The events signup submit. Measured in every state, never pressed.', sel: 'button.rd-ev-submit' });
  }
  if (key === 'media') {
    await S('media-show', q('button.rd-media-show').filter({ visible: true }).first(), B4, { group: g, title: 'Media show-more button', desc: 'A "show" toggle on a media row. Measured, not pressed.', sel: 'button.rd-media-show' });
  }
  await page.close();
}

async function podcast() {
  if (!(await newPage('podcast'))) { await page.close(); return; }
  await sheetsFor('podcast');
  const g = G.pod;
  await S('pod-title', q('h1, h2.rd-pd-latest-title').filter({ visible: true }).first(), ['default'], { group: g, title: 'Podcast title', desc: 'The latest-episode headline in cream on the dark podcast section.', sel: 'h1 / .rd-pd-latest-title' }, { noScroll: true });
  await S('pod-ep-title', q('h3.rd-pd-ep-title').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Episode title', desc: 'An episode row title ("Allison Fine: Making AI-Driven Change Less Scary").', sel: 'h3.rd-pd-ep-title' });
  await S('pod-ep-row', q('li.rd-pd-ep').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Episode row', desc: 'An episode row in the index.', sel: 'li.rd-pd-ep' });
  await S('pod-seek', q('input.rd-pd-dock-seek').filter({ visible: true }).first(), ['default'], { group: g, title: 'Player seek bar', desc: 'The range input of the podcast dock player. Measured at rest, never dragged.', sel: 'input.rd-pd-dock-seek' });
  await S('pod-play', q('.rd-pd-ep button, button[class*="pd"], button[class*="play" i], .rd-pd-dock button').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Player button', desc: 'A player transport button. Measured, never pressed (it would play).', sel: 'player button' });
  await page.close();
}

async function podcastEpisode() {
  if (!(await newPage('podcast-episode'))) { await page.close(); return; }
  await sheetsFor('podcast-episode');
  const g = G.pod;
  await S('pe-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Episode page title', sel: 'h1' }, { noScroll: true });
  await S('pe-body', await domFind(page, /./, { sel: 'main p, article p', tag: 'pe', minH: 30, minW: 200 }), ['default'], { group: g, title: 'Episode body', sel: 'article p' });
  await page.close();
}

async function faq() {
  if (!(await newPage('faq'))) { await page.close(); return; }
  await sheetsFor('faq');
  const g = G.misc;
  await S('faq-title', q('h1, h2.entry-title').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ title', sel: 'h1' }, { noScroll: true });
  await S('faq-cat', q('h2.text-rd-h2-sm, h2').filter({ hasText: /What Aboard is|AI consulting/i }).first(), ['default'], { group: g, title: 'FAQ category', desc: 'A category heading inside the FAQ ("AI consulting, strategy & managed services").', sel: 'h2.text-rd-h2-sm' });
  const qHead = q('h3.faq-q-heading').filter({ visible: true }).first();
  await S('faq-q', qHead, ['default', 'hover'], { group: g, title: 'FAQ question', desc: 'A question row of the FAQ accordion.', sel: 'h3.faq-q-heading' });
  if (await qHead.count()) {
    await qHead.click().catch(() => qHead.evaluate((el) => el.click()));
    await page.waitForTimeout(700);
    await S('faq-panel-open', q('div.accordion-content.faq-panel').filter({ visible: true }).first(), ['open'], { group: g, title: 'FAQ panel (open)', desc: 'The answer panel after its question was pressed; a local disclosure, nothing sent.', sel: 'div.faq-panel' }, { via: 'question pressed once to expand' });
    await S('faq-q-open', qHead, ['open'], { group: g, title: 'FAQ question (open)', desc: 'The question row after being pressed once.', sel: 'h3.faq-q-heading' }, { via: 'pressed once to expand' });
    await qHead.click().catch(() => qHead.evaluate((el) => el.click()));
    await page.waitForTimeout(400);
  }
  await page.close();
}

async function misc(key) {
  if (!(await newPage(key))) { await page.close(); return; }
  await sheetsFor(key);
  const g = G.misc;
  await S(`${key}-title`, q('h1, h2.entry-title').filter({ visible: true }).first(), ['default'], { group: g, title: `${key[0].toUpperCase() + key.slice(1)} title`, sel: 'h1' }, { noScroll: true });
  await S(`${key}-body`, await domFind(page, /./, { sel: 'main p, article p, p', tag: 'bd', minH: 30, minW: 200 }), ['default'], { group: g, title: `${key} body text`, sel: 'body p' });
  if (key === 'about') {
    await S('about-person', await domFind(page, /./, { sel: '[class*="person"], [class*="team"], [class*="member"], figure', tag: 'ap', minW: 100, minH: 100 }), ['default'], { group: g, title: 'Team member', desc: 'A person card/photo on the about page.', sel: 'team member' });
  }
  if (key === 'careers') {
    await S('job-row', await domFind(page, /engineer|designer|manager|developer|director/i, { sel: 'a, li, [class*="job"], [class*="role"]', tag: 'jr', minW: 200, minH: 30 }), ['default', 'hover'], { group: g, title: 'Job row', desc: 'An opening on the careers page.', sel: 'job row' });
  }
  await page.close();
}

async function aboardSign() {
  if (!(await newPage('aboard-sign'))) { await page.close(); return; }
  await sheetsFor('aboard-sign');
  const g = G.article;
  await S('art-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article title', desc: '"Meet Aboard Sign…" — a long-form piece in the article layout.', sel: 'h1' }, { noScroll: true });
  await S('art-body', q('div.rd-article p, article p').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article body', desc: 'A paragraph in the article column (rd-article, centred at columns 4-11).', sel: '.rd-article p' });
  await S('art-share', q('div.rd-nl-rail, [class*="share" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Share rail', desc: 'The SHARE rail beside the article (copy-link, never pressed).', sel: '.rd-nl-rail' });
  await S('art-nl-card', q('a.rd-nl-card').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Newsletter card', desc: 'A "More from the newsletter" card (date, title, thumbnail).', sel: 'a.rd-nl-card' });
  const f = G.forms;
  await S('nl-form-card', q('form.rd-nl-form.is-card, form.rd-nl-form').filter({ visible: true }).first(), ['default'], { group: f, title: 'Newsletter card form', desc: 'The boxed variant of the signup (is-card) under the article.', sel: 'form.rd-nl-form.is-card' });
  await page.close();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) { await page.close(); return; }
  const g = G.mobile;
  await closePromo(page);
  await S('m-nav-bar', q('header.site-header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The mobile header: wordmark left, menu trigger right.', sel: 'header.site-header' }, { noScroll: true });
  const trg = q('button.rd-nav-toggle').filter({ visible: true }).first();
  await S('m-menu-trigger', trg, B4, { group: g, title: 'Mobile menu trigger', desc: 'The "Open menu" button. Pressed once below to open the menu; a local disclosure.', sel: 'button.rd-nav-toggle' }, { noScroll: true });
  if (await trg.count()) {
    await trg.click().catch(() => trg.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    await S('m-nav-panel', q('nav.rd-nav, .rd-nav-row, [class*="menu" i][class*="open" i]').filter({ visible: true }).first(), ['open'], { group: g, title: 'Mobile menu (open)', desc: 'The opened mobile menu panel; pressed once, nothing navigated.', sel: 'nav.rd-nav open' }, { noScroll: true, via: 'menu trigger pressed once' });
    await trg.click().catch(() => {});
    await page.waitForTimeout(400);
  }
  await S('m-hero-title', q('h1.rd-words, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero title', sel: 'h1' }, { noScroll: true });
  await S('m-feed-row', q('a.rd-feed-row').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile feed row', sel: 'a.rd-feed-row' });
  await page.close();
}

const RUNNERS = {
  home, 'how-we-work': howWeWork, 'case-studies': caseStudies, 'case-study': caseStudy,
  foundry, perspectives: () => feeds('perspectives'), newsletter: () => feeds('newsletter'),
  podcast, 'podcast-episode': podcastEpisode, events: () => feeds('events'), media: () => feeds('media'),
  about: () => misc('about'), faq, careers: () => misc('careers'), security: () => misc('security'),
  'aboard-sign': aboardSign, mobile,
};
run = new Date().toISOString();
out._meta.run = run;
out._meta.product = 'aboard.com';
const wanted = process.argv.slice(2).join(',').split(',').map((s) => s.trim()).filter(Boolean);
const { browser, context: launchContext } = await launch();
context = launchContext;
try {
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
} finally {
  for (const c of tempContexts) await c.close().catch(() => {});
  await context.close().catch(() => {});
  await browser.close().catch(() => {});
}
