// Measures aboardhr.com's public marketing components in every state reachable
// without signing in, booking or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home everyday-hr growth-feedback team-culture pricing whats-new
// book-demo dataprotection terms mobile. Writes raw/components-computed.json
// (merged, so a subset of pages can be re-run) and one crop per component
// and state into components/crops/. raw/measurements.md is then built from
// the JSON by build-measurements.mjs.
//
// aboardhr.com is a Framer site: components carry data-framer-name
// attributes and colours live in --token-* custom properties. Nothing is
// sent or submitted: the Book-a-demo form is measured at rest and focus
// only, the Sign-in link and app.aboardhr.com are never opened, and the
// only press is the mobile nav trigger (a local disclosure).
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
  'everyday-hr': '/everyday-hr',
  'growth-feedback': '/growth-feedback',
  'team-culture': '/team-culture',
  pricing: '/pricing',
  'whats-new': '/whats-new',
  'release': '/whats-new/june-2026',
  'book-demo': '/book-demo',
  teamtailor: '/teamtailor-and-aboard',
  dataprotection: '/dataprotection',
  terms: '/terms',
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
        await page.waitForTimeout(450);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus((opts.focusLoc || loc).filter({ visible: true }).first());
        if (via === 'focus failed') {
          // The element never took keyboard focus: record the failure instead
          // of saving a resting-style capture under the focus-visible name.
          out.components[key].states[st] = { error: 'keyboard focus failed' };
          log('  !', key, st, 'focus failed');
          continue;
        }
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).filter({ visible: true }).first(), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await (opts.fieldLoc || loc).filter({ visible: true }).first().click({ timeout: 4000 });
        await page.waitForTimeout(400);
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
  shell: 'Shell and navigation', home: 'Home', product: 'Product pages',
  pricing: 'Pricing', demo: 'Book a demo (resting only)', news: "What's new",
  partner: 'Teamtailor partner page', legal: 'Legal text', mobile: 'Mobile (390 wide)',
};

async function shell(ctxPage = 'home') {
  const g = G.shell;
  const nav = q('[data-framer-name="Desktop"], header').filter({ visible: true }).first();
  await S('nav-bar', nav, ['default'], { group: g, title: 'Top navigation bar', desc: 'The floating nav: logo, Product / Price / Resources links and the Sign-in / Book-a-demo actions.', sel: '[data-framer-name=Desktop]' }, { noScroll: true });
  await S('nav-logo', q('a').filter({ has: page.locator('[data-framer-name="Logo"], svg, img') }).first(), B4, { group: g, title: 'Logo', desc: 'The Aboard wordmark linking home.', sel: 'nav logo a' }, { noScroll: true });
  await S('nav-link', q('a').filter({ hasText: 'Product' }).first(), B4, { group: g, title: 'Nav link', desc: 'A section link in the top bar.', sel: 'nav a' }, { noScroll: true });
  // inside the nav only: the page repeats Book a demo in the hero and the footer
  await S('nav-cta', q('header a, nav a').filter({ hasText: /Book a demo|Sign in/ }).filter({ visible: true }).last(), B4, { group: g, title: 'Nav CTA', desc: 'The boxed action at the right of the nav (Sign in / Book a demo). Hovered and focused only; app.aboardhr.com is never opened.', sel: 'nav cta' }, { noScroll: true });
  await S('footer', await domFind(page, /© Teamtailor|Smooth sailing/, { sel: 'div,section,[data-framer-name]', tag: 'ft', minW: 600, minH: 120 }), ['default'], { group: g, title: 'Footer', desc: 'The "Smooth sailing" footer band: link columns (Price / What\'s new / Help center / legal) and the Teamtailor credit row.', sel: 'footer band' });
  await S('footer-heading', await domFind(page, /Smooth sailing/, { sel: 'h1,h2,h3,h4,p,div,span', tag: 'fh', minW: 40 }), ['default'], { group: g, title: 'Footer heading', desc: 'The "Smooth sailing." sign-off heading in the footer.', sel: 'footer heading' });
  await S('footer-link', q('a').filter({ hasText: /Help center|Privacy policy|Terms and conditions|What's new/ }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' });
}

async function home() {
  if (!(await newPage('home'))) { await page.close(); return; }
  await sheetsFor('home');
  await shell('home');
  const h = G.home;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: '"Run people operations. With clarity." — the display headline.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', await domFind(page, /Bring all your people data/, { sel: 'p, div, h2, h3, span', tag: 'hs', leaf: true, minW: 200 }), ['default'], { group: h, title: 'Hero subtitle', desc: 'The paragraph under the hero title.', sel: 'hero p' }, { noScroll: true });
  await S('cta-demo', q('a, button').filter({ hasText: 'Book a demo' }).filter({ visible: true }).first(), B4, { group: h, title: 'Primary CTA', desc: 'The "Book a demo" button under the hero. Hovered and focused only.', sel: 'Book a demo' });
  await S('cta-try', q('a, button').filter({ hasText: 'Try for free' }).filter({ visible: true }).first(), B4, { group: h, title: 'Secondary CTA', desc: 'The "Try for free" button. Hovered and focused only.', sel: 'Try for free' });
  await S('copilot-demo', await domFind(page, /Ask me anything/, { sel: 'p,div,span,input,label', tag: 'cp', up: '[data-framer-name]', minW: 60 }), ['default'], { group: h, title: 'Co-pilot demo panel', desc: 'The animated AI-assistant chat mock in the hero (a marketing demo, not a live product): the "Ask me anything" prompt inside the chat panel.', sel: 'copilot prompt' });
  await S('section-title', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section title', desc: 'A section heading ("Built for people, not just the process").', sel: 'h2' });
  await S('feature-card', q('[data-framer-name="Feature Card"], [data-framer-name*="card" i]').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Feature card', desc: 'A product-area card (Everyday HR / Team culture / Growth & feedback).', sel: 'feature card' });
  await S('feature-item', await domFind(page, /People directory|Time off|Contracts|Onboarding/, { sel: '[data-framer-name], li, div, a', tag: 'fi', minW: 80, minH: 20 }), ['default', 'hover'], { group: h, title: 'Feature list item', desc: 'A feature row inside a product card (People directory, Time off, Contracts & documents).', sel: 'feature item' });
  await S('learn-more', q('a').filter({ hasText: 'Learn more' }).first(), B4, { group: h, title: 'Learn-more link', desc: 'The text link inside a feature card.', sel: 'Learn more' });
  await page.close();
}

async function product(key) {
  if (!(await newPage(key))) { await page.close(); return; }
  await sheetsFor(key);
  const g = G.product;
  await S(key + '-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', sel: 'h1' }, { noScroll: true });
  await S(key + '-section', q('h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Section title', sel: 'h2' });
  await S(key + '-card', q('[data-framer-name="Feature Card"], [data-framer-name*="card" i]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Feature card', sel: 'feature card' });
  const itemRe = { 'everyday-hr': /People directory|Time off|Contracts|Onboarding|Expenses/i, 'growth-feedback': /review|goal|1:1|feedback|performance|survey|development/i, 'team-culture': /Posts|Events|Celebrate|Photo library|Employee portal|updates/i }[key] || /./;
  await S(key + '-item', await domFind(page, itemRe, { sel: '[data-framer-name] *, li, p, span, div', tag: 'pi', minW: 60, minH: 14 }), ['default'], { group: g, title: 'Feature item', desc: 'A feature row inside a product card.', sel: 'feature item' });
  await S(key + '-cta', q('a, button').filter({ hasText: /Book a demo|Try for free|Learn more|Get started/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Page CTA', sel: 'page cta' });
  await page.close();
}

async function pricing() {
  if (!(await newPage('pricing'))) { await page.close(); return; }
  await sheetsFor('pricing');
  const g = G.pricing;
  await S('pricing-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', sel: 'h1' }, { noScroll: true });
  await S('price-card', await domFind(page, /month|year|employee|seat|user|Free|Essential|Premium/, { sel: '[data-framer-name], div, section', tag: 'pc', minW: 200, minH: 200 }), ['default', 'hover'], { group: g, title: 'Plan card', desc: 'A pricing plan card.', sel: 'plan card' });
  await S('price-amount', await domFind(page, /80\s*kr|User \/ month/, { sel: 'h1,h2,h3,p,span,div', tag: 'pa', leaf: true, minW: 20 }), ['default'], { group: g, title: 'Plan price', desc: 'The "80 kr / user / month" price figure.', sel: 'price amount' });
  await S('plan-cta', q('a, button').filter({ hasText: /Book a demo|Try for free|Get started|Choose|Start/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', sel: 'plan cta' });
  await S('billing-toggle', await domFind(page, /monthly|yearly|annual/, { sel: 'button, [role="switch"], [role="tab"], label, a', tag: 'bt', minW: 30, minH: 16 }), ['default'], { group: g, title: 'Billing toggle', desc: 'The monthly/yearly switch, if rendered (never toggled).', sel: 'billing toggle' });
  await page.close();
}

async function bookDemo() {
  if (!(await newPage('book-demo'))) { await page.close(); return; }
  await sheetsFor('book-demo');
  const g = G.demo;
  await S('demo-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', desc: '"Request a demo" — the form page heading.', sel: 'h1,h2' }, { noScroll: true });
  await S('demo-form', q('form, iframe[src*="cal"], [data-framer-name*="form" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Demo form', desc: 'The book-a-demo form or scheduler embed. Measured at rest; nothing typed or sent.', sel: 'form' });
  await S('demo-field', q('input, textarea, select').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Demo field', desc: 'A text field of the demo form. Clicked into for the focus style; nothing typed.', sel: 'form field' });
  await S('demo-submit', q('button[type="submit"], button, a').filter({ hasText: /Let.?s talk|Submit|Send|Request|Schedule|Confirm/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Demo submit', desc: 'The "Let’s talk" form submit button. Measured in every state, never pressed.', sel: 'form submit' });
  await page.close();
}

async function whatsNew() {
  if (!(await newPage('whats-new'))) { await page.close(); return; }
  await sheetsFor('whats-new');
  const g = G.news;
  await S('whatsnew-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', sel: 'h1' }, { noScroll: true });
  await S('release-row', await domFind(page, /January|February|March|April|May|June|July|August|September|October|November|December|2025|2026/, { sel: '[data-framer-name] *, article, li, div, a', tag: 'rn', minW: 200, minH: 30 }), ['default', 'hover'], { group: g, title: 'Release row', desc: 'A dated changelog entry on the Whats-new page.', sel: 'release row' });
  await page.close();
}

async function legal(key) {
  if (!(await newPage(key))) { await page.close(); return; }
  const g = G.legal;
  await S(key + '-title', q('h1, h2, h3').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', sel: 'h1-h3' }, { noScroll: true });
  await S(key + '-body', await domFind(page, /Last updated|means|shall|GDPR|Customer/, { sel: 'p, div, span', tag: 'lb', minW: 250, minH: 20 }), ['default'], { group: g, title: 'Body text', sel: 'legal p' });
  await page.close();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) { await page.close(); return; }
  const g = G.mobile;
  await closePromo(page);
  await page.evaluate(() => {
    const t = document.querySelector('[data-framer-name="navtrigger"]');
    for (let n = t; n; n = n.parentElement) {
      const cs = getComputedStyle(n); const r = n.getBoundingClientRect();
      if ((cs.position === 'fixed' || cs.position === 'sticky') && r.width > 300 && r.height < 200) { n.setAttribute('data-m-mark', 'mnb'); break; }
      if (r.width > 300 && r.height >= 40 && r.height <= 200 && n.parentElement === document.body) { n.setAttribute('data-m-mark', 'mnb'); break; }
    }
  }).catch(() => {});
  await S('m-nav-bar', q('[data-m-mark="mnb"]'), ['default'], { group: g, title: 'Mobile top bar', desc: 'The mobile header: logo left, menu trigger right.', sel: 'mobile nav' }, { noScroll: true });
  const trg = q('[data-framer-name="navtrigger"], [aria-label*="menu" i], [data-framer-name*="nav" i] button').filter({ visible: true }).first();
  await S('m-menu-trigger', trg, B4, { group: g, title: 'Mobile menu trigger', desc: 'The menu button. Pressed once below to open the menu; a local disclosure.', sel: 'navtrigger' }, { noScroll: true });
  if (await trg.count()) {
    await trg.click().catch(() => trg.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    // The menu is open only when a nav link sits inside a large fixed/absolute
    // panel below the header band; an empty nav or the ordinary header is not.
    const opened = await page.evaluate(() => {
      const link = [...document.querySelectorAll('a')].find((a) => /Product|Price|Resources/.test(a.innerText || '') && a.getBoundingClientRect().top > 60);
      if (!link) return false;
      for (let n = link; n; n = n.parentElement) {
        const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
        if (r.width > 200 && r.height > 200 && (cs.position === 'fixed' || cs.position === 'absolute')) { n.setAttribute('data-m-mark', 'mnp'); return true; }
      }
      return false;
    }).catch(() => false);
    if (opened) {
      await S('m-nav-panel', q('[data-m-mark="mnp"]').filter({ visible: true }).first(), ['open'], { group: g, title: 'Mobile menu (open)', desc: 'The opened mobile menu panel; pressed once, nothing navigated.', sel: 'mobile menu open' }, { noScroll: true, via: 'menu trigger pressed once' });
    } else {
      // The trigger did not open a menu: record the state as unavailable rather
      // than saving the header as if it were the menu panel.
      const c = comp('m-nav-panel', { title: 'Mobile menu (open)', group: g, desc: 'The opened mobile menu panel; pressed once, nothing navigated.', selector: 'mobile menu open' });
      delete c.states.open;
      c.missing = true;
      log('  ! m-nav-panel: menu did not open; recorded unavailable');
    }
    await page.keyboard.press('Escape').catch(() => {});
    await page.waitForTimeout(400);
  }
  await S('m-hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero title', sel: 'h1' }, { noScroll: true });
  await page.close();
}

async function release() {
  if (!(await newPage('release'))) { await page.close(); return; }
  const g = G.news;
  await S('release-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Release title', desc: 'The dated headline of a changelog detail page (June 2026).', sel: 'h1' }, { noScroll: true });
  await S('release-back', q('a').filter({ hasText: /back|what.?s new/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Back link', desc: 'The "Link back" anchor returning to the What\'s new index.', sel: 'back link' });
  await S('release-post', q('[data-framer-name="Post"], [data-framer-name="Content"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Release body', desc: 'The changelog post body on a detail page.', sel: 'release post' });
  await page.close();
}

async function teamtailor() {
  if (!(await newPage('teamtailor'))) { await page.close(); return; }
  await sheetsFor('teamtailor');
  const g = G.partner;
  await S('teamtailor-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', desc: '"The best candidate experience deserves an equally great employee experience."', sel: 'h1' }, { noScroll: true });
  await S('teamtailor-card', q('[data-framer-name="Card Primary"], [data-framer-name*="card" i]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Partner card', sel: 'partner card' });
  await S('teamtailor-cta', q('a, button').filter({ hasText: /Book a demo|Try for free|Learn more|Get started/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Page CTA', sel: 'page cta' });
  await page.close();
}

const RUNNERS = {
  home, 'everyday-hr': () => product('everyday-hr'), 'growth-feedback': () => product('growth-feedback'),
  'team-culture': () => product('team-culture'), pricing, 'book-demo': bookDemo,
  'whats-new': whatsNew, release, teamtailor, dataprotection: () => legal('dataprotection'), terms: () => legal('terms'), mobile,
};
run = new Date().toISOString();
out._meta.run = run;
out._meta.product = 'aboardhr.com';
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
