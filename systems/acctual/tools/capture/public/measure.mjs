// Measures acctual.com's public marketing components in every state reachable
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
// acctual.com is a Framer site: components carry data-framer-name
// attributes and colours live in --token-* custom properties. Nothing is
// sent or submitted: the Book-a-demo form is measured at rest and focus
// only, the Log-in link and app.acctual.com are never opened, and the
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
  pricing: '/pricing',
  teams: '/teams',
  about: '/about',
  blog: '/blog',
  'blog-post': '/blog/acctual-joins-altitude',
  altitude: '/altitude',
  'freelancer-invoicing': '/freelancer-invoicing',
  'stablecoin-invoicing': '/stablecoin-invoicing',
  location: '/locations/us-to-japan',
  terms: '/terms',
  privacy: '/privacy',
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
const NEVER = /^(send|submit|sign up|sign in|log in|register|create|buy|buy now|checkout|pay|purchase|add to cart|download|subscribe|share|accept|close|more info|start free trial|try|upgrade|open|continue|get started|get in touch|save my preferences|reject|customize)$/i;
async function toggle(loc) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || t.tag === 'A') throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

// The first Playwright-visible element that also paints: computed opacity
// above zero and a box not parked outside the document. getBoundingClientRect
// is viewport-relative, so a real element above the fold reads a negative y
// once the page has scrolled; only document position separates it from the
// ghost copies Framer parks offscreen (hence + scrollY/scrollX). Elements
// below the fold always qualify; they scroll in via centre().
async function pickVisible(target) {
  const n = await target.count();
  for (let i = 0; i < n; i++) {
    const el = target.nth(i);
    if (!(await el.isVisible().catch(() => false))) continue;
    const ok = await el.evaluate((e) => {
      const r = e.getBoundingClientRect();
      const cs = getComputedStyle(e);
      if (parseFloat(cs.opacity) === 0) return false;
      return r.bottom + window.scrollY > -2 && r.right + window.scrollX > -2;
    }).catch(() => false);
    if (ok) return el;
  }
  return page.locator('[data-m-none]'); // matches nothing -> the component reads missing
}

// ONLY=key1,key2 limits the run to those components, so a wrong selector's
// entries can be recaptured without re-measuring every control on the page.
const ONLY = new Set((process.env.ONLY || '').split(',').map((s) => s.trim()).filter(Boolean));

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
  if (ONLY.size && !ONLY.has(key)) return;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  delete out.components[key].missing;
  if (opts.open) { await reset(); await opts.open(); }
  const loc = await pickVisible(target);
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
        // a focus the keyboard never reached is not a captured state: record
        // it as an error so builders do not count it among real focuses
        if (via === 'focus failed') {
          out.components[key].states[st] = { error: 'keyboard focus never reached the control', via: 'focus failed' };
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
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  company: 'Company and content pages', landing: 'Landing pages (programmatic)',
  legal: 'Legal text', mobile: 'Mobile (390 wide)',
};

async function shell(ctxPage = 'home') {
  const g = G.shell;
  const nav = q('[data-framer-name="Navigation/Topbar"], [data-framer-name="Desktop"], header, nav').filter({ visible: true }).first();
  await S('nav-bar', nav, ['default'], { group: g, title: 'Top navigation bar', desc: 'The top bar: wordmark, Freelancer / Agency / Pricing / Blog links, Log in and the Sign-up pill.', sel: 'nav topbar' }, { noScroll: true });
  await S('nav-logo', q('[data-framer-name="Desktop"] a[href="./"], [data-framer-name="Navigation/Topbar"] a[href="./"], nav a[href="./"], header a[href="./"]').filter({ visible: true }).first(), B4, { group: g, title: 'Logo', desc: 'The Acctual wordmark linking home.', sel: 'nav logo a' }, { noScroll: true });
  await S('nav-link', q('a').filter({ hasText: 'Pricing' }).first(), B4, { group: g, title: 'Nav link', desc: 'A section link in the top bar.', sel: 'nav a' }, { noScroll: true });
  await S('nav-cta', q('a').filter({ hasText: 'Sign up for free' }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The "Sign up for free" pill. Hovered and focused only; app.acctual.com is never opened.', sel: 'nav cta' }, { noScroll: true });
  await S('nav-login', q('a').filter({ hasText: 'Log in' }).first(), B4, { group: g, title: 'Log-in link', desc: 'The plain Log-in link beside the CTA. app.acctual.com is never opened.', sel: 'nav login' }, { noScroll: true });
  await S('announcement', q('a').filter({ hasText: /joining Altitude|funding/i }).first(), B4, { group: g, title: 'Announcement banner', desc: 'The "Acctual is joining Altitude" strip above the nav, linking to /altitude.', sel: 'announcement a' }, { noScroll: true });
  await S('footer', await domFind(page, /Create the world|from NYC|Smooth sailing|©/, { sel: 'div,section,footer,[data-framer-name]', tag: 'ft', minW: 600, minH: 120 }), ['default'], { group: g, title: 'Footer', desc: 'The footer band: the "Create the world\u2019s most flexible invoice" heading, link columns and the "from NYC" credit.', sel: 'footer band' });
  await S('footer-heading', await domFind(page, /Create the world/, { sel: 'h1,h2,h3,h4,p,div,span', tag: 'fh', minW: 40 }), ['default'], { group: g, title: 'Footer heading', desc: 'The sign-off heading in the footer.', sel: 'footer heading' });
  await S('footer-link', q('a').filter({ hasText: /Privacy|Terms|Blog|Pricing|Guides|Help/ }).last(), B4, { group: g, title: 'Footer link', sel: 'footer a' });
}

async function home() {
  if (!(await newPage('home'))) { await page.close(); return; }
  await sheetsFor('home');
  await shell('home');
  const h = G.home;
  // q('h1') un-sliced: pickVisible takes the first on-page one (ghost copies
  // parked outside the document are skipped).
  await S('hero-title', q('h1'), ['default'], { group: h, title: 'Hero title', desc: '"Small business invoices: Get paid on time" — the display headline.', sel: 'h1' });
  await S('invoice-demo', await domFind(page, /PAYMENT METHOD|Amount|USD/, { sel: '[data-framer-name]', tag: 'id', up: '[data-framer-name="hero"], [data-framer-name]', minW: 300, minH: 200 }), ['default'], { group: h, title: 'Invoice demo', desc: 'The interactive invoice mock in the hero (a marketing demo, not a live product): payment-method dropdown, amount and currency fields.', sel: 'invoice demo' });
  // acctual.com emits no h2: every heading is an h1, so the section title is
  // found by its text.
  await S('section-title', await domFind(page, /works harder for your business/i, { sel: 'h1, h2', tag: 'st', minW: 300, minH: 30 }), ['default'], { group: h, title: 'Section title', desc: 'A section heading ("We designed an invoice that works harder for your business").', sel: 'h1 (section)' });
  await S('fee-item', q('[data-framer-name="1% bank transfer fee"], [data-framer-name="2.7% card fee"]'), ['default'], { group: h, title: 'Fee item', desc: 'A fee-comparison row (1% bank transfer / 2.7% card / 1% stablecoin).', sel: 'fee item' });
  await S('persona-card', await domFind(page, /Contractors|Get paid on the job/, { sel: 'a, [data-framer-name]', tag: 'pc', minW: 200, minH: 80 }), ['default', 'hover'], { group: h, title: 'Persona card', desc: 'A who-it-is-for card (Contractors).', sel: 'persona card' });
  await S('security-item', await domFind(page, /PCI standards|SSL encryption/i, { sel: '[data-framer-name] *, div, p', tag: 'sc', minW: 100, minH: 30 }), ['default'], { group: h, title: 'Security item', desc: 'A trust row (PCI standards / SSL encryption & tokenization).', sel: 'security item' });
  // The FAQ rows are [data-framer-name="Closed"] toggles; a real click flips
  // the row to "Opened" (a plain el.click() does not trigger Framer).
  const faqRow = q('[data-framer-name="Closed"]');
  await S('faq-item', faqRow, ['default'], { group: h, title: 'FAQ item', desc: 'An accordion question in the FAQs section; toggled open once (a local disclosure).', sel: 'faq Closed row' });
  {
    const closed = await pickVisible(faqRow);
    if (await closed.count()) {
      await centre(closed);
      await toggle(closed).catch((e) => log('  ! faq toggle', String(e.message).slice(0, 80)));
      await page.waitForTimeout(900);
      const opened = await pickVisible(q('[data-framer-name="Opened"], [data-framer-name="Open"]'));
      if (await opened.count()) await measure('faq-item', 'open', opened, { via: 'question pressed once (a local accordion disclosure)' });
    }
  }
  await page.close();
}

async function pricing() {
  if (!(await newPage('pricing'))) { await page.close(); return; }
  await sheetsFor('pricing');
  const g = G.pricing;
  await S('pricing-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', sel: 'h1' }, { noScroll: true });
  await S('fee-row', await domFind(page, /Bank Transfer|Card Payment|Currencies|Payout/, { sel: '[data-framer-name], tr, div', tag: 'pr', minW: 200, minH: 24 }), ['default'], { group: g, title: 'Fee comparison row', desc: 'A comparison row on the pricing page (payment method, currencies, payout).', sel: 'fee row' });
  await S('plan-cta', q('a, button').filter({ hasText: /Sign up|Get started|Start free|Try/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Page CTA', sel: 'page cta' });
  await page.close();
}

async function company(key) {
  if (!(await newPage(key))) { await page.close(); return; }
  const g = G.company;
  await S(key + '-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', sel: 'h1,h2' }, { noScroll: true });
  await S(key + '-body', await domFind(page, /./, { sel: 'main p, article p, [data-framer-name="ContentWrapper"] p, p', tag: 'cb', minW: 250, minH: 20 }), ['default'], { group: g, title: 'Body text', sel: 'body p' });
  if (key === 'blog') {
    await S('blog-item', await domFind(page, /2026|2025|Read|min/, { sel: 'a[data-framer-name*="Blog" i], [data-framer-name*="Blog Item" i], article, a', tag: 'bi', minW: 200, minH: 30 }), ['default', 'hover'], { group: g, title: 'Blog item', desc: 'A post row or card on the blog index.', sel: 'blog item' });
  }
  if (key === 'blog-post' || key === 'altitude') {
    await S(key + '-link', q('a').filter({ hasText: /back|Blog|Home/ }).first(), B4, { group: g, title: 'Back link', desc: 'The link returning to the index.', sel: 'back link' });
  }
  await page.close();
}

async function landing(key) {
  if (!(await newPage(key))) { await page.close(); return; }
  const g = G.landing;
  await S(key + '-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', sel: 'h1' }, { noScroll: true });
  await S(key + '-cta', q('a, button').filter({ hasText: /Sign up|Get started|Start|Send an invoice|Try/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Page CTA', sel: 'page cta' });
  // Most landing pages carry an h2 for the first section; pages that emit
  // h1s only (freelancer-invoicing) fall back to the second heading.
  const sec = (await q('h2').count()) ? q('h2') : q('h1, h2').nth(1);
  await S(key + '-section', sec, ['default'], { group: g, title: 'Section title', sel: 'h2 (or second heading)' });
  await page.close();
}

async function legal(key) {
  if (!(await newPage(key))) { await page.close(); return; }
  const g = G.legal;
  await S(key + '-title', q('h1, h2, h3').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', sel: 'h1-h3' }, { noScroll: true });
  await S(key + '-body', await domFind(page, /Last updated|agreement|information|may|shall/, { sel: 'p, div, span, li', tag: 'lb', minW: 250, minH: 20 }), ['default'], { group: g, title: 'Body text', sel: 'legal p' });
  await page.close();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) { await page.close(); return; }
  const g = G.mobile;
  await closePromo(page);
  await page.evaluate(() => {
    const t = document.querySelector('[data-framer-name="navtrigger"], [data-framer-name*="navtrigger" i]');
    for (let n = t; n; n = n.parentElement) {
      const cs = getComputedStyle(n); const r = n.getBoundingClientRect();
      if ((cs.position === 'fixed' || cs.position === 'sticky') && r.width > 300 && r.height < 200) { n.setAttribute('data-m-mark', 'mnb'); break; }
      if (r.width > 300 && r.height >= 40 && r.height <= 200 && n.parentElement === document.body) { n.setAttribute('data-m-mark', 'mnb'); break; }
    }
  }).catch(() => {});
  await S('m-nav-bar', q('[data-m-mark="mnb"], [data-framer-name="Navigation/Topbar"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The mobile header: logo left, menu trigger right.', sel: 'mobile nav' }, { noScroll: true });
  // The menu trigger carries no data-framer-name on this build: tag the small
  // icon box on the right of the top bar (the outermost svg holder) so the
  // selector below can find it.
  await page.evaluate(() => {
    const bar = document.querySelector('[data-framer-name="Navigation/Topbar"], [data-m-mark="mnb"]');
    if (!bar) return;
    const small = [...bar.querySelectorAll('div,button,a')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width >= 10 && r.width <= 90 && r.height <= 80 && r.x > window.innerWidth - 140 && e.querySelector('svg');
    });
    const el = small.find((e) => !small.some((o) => o !== e && o.contains(e))) || small[0];
    if (el) el.setAttribute('data-m-mark', 'mtr');
  }).catch(() => {});
  const trg = q('[data-m-mark="mtr"], [data-framer-name="navtrigger"], [aria-label*="menu" i], [data-framer-name*="nav" i] button');
  await S('m-menu-trigger', trg, B4, { group: g, title: 'Mobile menu trigger', desc: 'The menu button (the 24px icon box at the right of the top bar). Pressed once below to open the menu; a local disclosure.', sel: 'nav icon box' }, { noScroll: true });
  const trgPick = await pickVisible(trg);
  if (await trgPick.count()) {
    await trgPick.click().catch(() => trgPick.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    await page.evaluate(() => {
      const link = [...document.querySelectorAll('a')].find((a) => /Pricing|Blog|Freelancer/.test(a.innerText || '') && a.getBoundingClientRect().top > 60);
      if (link) for (let n = link; n; n = n.parentElement) { const r = n.getBoundingClientRect(); const cs = getComputedStyle(n); if (r.width > 200 && r.height > 200 && (cs.position === 'fixed' || cs.position === 'absolute')) { n.setAttribute('data-m-mark', 'mnp'); break; } }
    }).catch(() => {});
    await S('m-nav-panel', q('[data-m-mark="mnp"], [data-framer-name*="menu" i]').filter({ visible: true }).first(), ['open'], { group: g, title: 'Mobile menu (open)', desc: 'The opened mobile menu panel; pressed once, nothing navigated.', sel: 'mobile menu open' }, { noScroll: true, via: 'menu trigger pressed once' });
    await page.keyboard.press('Escape').catch(() => {});
    await page.waitForTimeout(400);
  }
  await S('m-hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero title', sel: 'h1' }, { noScroll: true });
  await page.close();
}

const RUNNERS = {
  home, pricing,
  teams: () => company('teams'), about: () => company('about'),
  blog: () => company('blog'), 'blog-post': () => company('blog-post'), altitude: () => company('altitude'),
  'freelancer-invoicing': () => landing('freelancer-invoicing'),
  'stablecoin-invoicing': () => landing('stablecoin-invoicing'),
  location: () => landing('location'),
  terms: () => legal('terms'), privacy: () => legal('privacy'), mobile,
};
run = new Date().toISOString();
out._meta.run = run;
out._meta.product = 'acctual.com';
const wanted = process.argv.slice(2).join(',').split(',').map((s) => s.trim()).filter(Boolean);
const launched = await launch();
context = launched.context;
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
  await launched.browser.close();
}
