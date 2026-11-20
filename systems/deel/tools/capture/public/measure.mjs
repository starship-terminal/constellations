// Measures deel.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs PYTHON=<venv python3> node measure.mjs [page ...]
//
// Pages: home pricing hr payroll about mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// deel.com is a Next.js + MUI + Tailwind marketing site; the page paints one
// light theme. Specs select by mui class fragments, role, aria-label or text.
// Log in, Book a demo, Claim offer and every product/store link are measured,
// never followed; nav dropdowns and the MUI FAQ accordions are local UI
// toggles; no form is ever submitted and app.deel.com is never reached.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, styleOfSelector, crop, cropSelector, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };
const URLS = { home: '/', pricing: '/pricing/', hr: '/hr/', payroll: '/global-payroll/', about: '/about-us/' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes blocked this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /client challenge|performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access|a required part of this site/i.test(t + ' ' + document.title) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null } = {}) {
  current = key;
  // Close the previous page's context before opening the next: leaving them
  // alive keeps every captured page (and its animations) running in the
  // background for the rest of the run.
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = context.browser();
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  // Cloudflare Turnstile can greet a route: wait it out, then one retry on a
  // fresh context before recording the route as blocked this run.
  let ok = false;
  for (let tries = 0; tries < 2 && !ok; tries++) {
    ok = (await open(page, url || (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]), { wait, promo })) && !(await blocked());  // open() is false when the bot check did not clear
    if (!ok && tries === 0) { log('  challenge, one reload', key); }
  }
  if (!ok) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); liveCtx = null; return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return true;
}

// Fixed/sticky chrome with paint order: the z-index map of the page's bars and
// overlays. Recorded per page into _meta.chrome.
async function chrome(key) {
  const z = await page.evaluate(() => {
    const els = [...document.querySelectorAll('body *')];
    const seen = [];
    for (const el of els) {
      const cs = getComputedStyle(el);
      if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
      const r = el.getBoundingClientRect();
      if (r.width < 40 || r.height < 10) continue;
      seen.push({ node: el.tagName.toLowerCase() + '.' + String(el.className).split(' ')[0].slice(0, 60), z: cs.zIndex, pos: cs.position, rect: `${r.width | 0}x${r.height | 0}@${r.x | 0},${r.y | 0}`, text: (el.innerText || '').slice(0, 40).replace(/\n/g, '|') });
    }
    return seen.sort((a, b) => (parseInt(b.z) || 0) - (parseInt(a.z) || 0)).slice(0, 20);
  }).catch(() => []);
  out._meta.chrome ??= {};
  out._meta.chrome[key] = z;
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

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, run, url: /^https?:/.test(URLS[current] || '') ? URLS[current] : BASE + (URLS[current] || '') }, meta);
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

async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); } }
  const loc = target.filter({ visible: true }).first();
  await loc.waitFor({ state: 'visible', timeout: 6000 }).catch(() => {});
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
    // Keep earlier evidence under its own provenance: the states stay but the
    // entry keeps its original page/run/url and records the miss, so a re-run
    // never republishes old readings under a new date.
    if (!has) out.components[key].missing = true;
    else { Object.assign(out.components[key], keep); out.components[key].recaptureMissed = run; }
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
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
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

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|order( free)?( sample)?|add to cart|buy now|buy font|go to the platform|get a demo|get demo|contact sales|send message)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

// Variant of S() for routes whose Playwright locators never resolve.
// curater.org/taste client-side redirected to /taste/soon and the navigation
// never settles: locators count matches, but every resolve dies with the
// execution context. Measuring the default state through the main world
// (same styleOf reader + clip crop) instead of locators.
async function SJ(key, sel, meta = {}, opts = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: sel });
  delete out.components[key].missing;
  const found = await page.evaluate((pick) => !!eval(pick), sel.startsWith('js:') ? sel.slice(3) : `document.querySelector(${JSON.stringify(sel)})`);
  if (!found) { out.components[key].missing = true; log('  ! missing', key); return; }
  try {
    const s = await styleOfSelector(page, sel);
    if (!s) throw new Error('element not found');
    let file;
    if (opts.crop !== false) {
      try { file = await cropSelector(page, sel, `${key}-default`, opts.pad ?? 8); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    out.components[key].states.default = { ...s, crop: file, via: 'main-world query (locators never settle on this route)' };
    log('  ', key, 'default', s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    out.components[key].states.default = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, 'default', String(e.message).slice(0, 120));
  }
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Scrolls the page down in steps and back to the top: lazy-mounted sections
// only enter the DOM once scrolled into view.
async function lazyLoad() {
  await page.evaluate(async () => {
    const h = document.documentElement.scrollHeight;
    for (let y = 0; y <= h; y += 800) { scrollTo(0, y); await new Promise((r) => setTimeout(r, 120)); }
    scrollTo(0, 0);
  });
  await page.waitForTimeout(1600);
}

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

// Whether the page paints a different transition under prefers-reduced-motion:
// the same component re-read in a context with reduce on.
async function reducedMotion(key, sel) {
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(URLS[key] ? (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]) : BASE, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(7000);
    await closePromo(p);
    const v = await p.evaluate((s) => {
      const el = document.querySelector(s);
      if (!el) return null;
      const cs = getComputedStyle(el);
      return { transition: cs.transition, animation: cs.animation, scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior };
    }, sel).catch(() => null);
    out._meta.reducedMotion[key] = { selector: sel, reduce: v };
    await ctx.close();
  } catch (e) { out._meta.reducedMotion[key] = { selector: sel, error: String(e).slice(0, 120) }; }
}

const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  hr: 'Deel HR', payroll: 'Global Payroll', about: 'About',
  mobile: 'Mobile (390 wide)',
};

// Opens the Solutions mega dropdown: the nav item is a button that opens its
// panel on click (a local UI toggle, never a link). "Solutions" is not a
// submit/link, so the click is the panel's own trigger.
async function openSolutions() {
  const open = () => page.evaluate(() => [...document.querySelectorAll('a')].some((a) => /deel payroll overview/i.test(a.textContent) && a.getBoundingClientRect().width > 0));
  if (await open()) return 'the mega dropdown was already open';
  const item = page.locator('nav button, nav a').filter({ hasText: /^Solutions/ }).filter({ visible: true }).first();
  if (!(await item.count())) return 'no Solutions trigger';
  await item.click({ timeout: 4000 }).catch(() => item.evaluate((el) => el.click()));
  await page.waitForTimeout(1600);
  return (await open()) ? 'clicked Solutions to open the mega dropdown' : 'clicked Solutions; the panel did not report open';
}

// The FAQ accordions are MUI MuiAccordion items: clicking the summary toggles
// the details — a local UI toggle, never a submission.
async function firstFaqSummary() {
  return page.locator('[class*="MuiAccordionSummary"], [class*="product-faqs"] [role="button"], [class*="accordion" i] button').filter({ visible: true }).first();
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('promo-banner', q('#top-banner, .banners').filter({ visible: true }).first(), ['default'], { group: g, title: 'Promo banner', desc: 'The "Special Offer" strip above the nav ("Get 3 months free of PEO" + Claim offer + close); a dismissible banner, never dismissed.', sel: '#top-banner' }, { noScroll: true });
  await S('promo-cta', q('#top-banner button, .banners button').filter({ hasText: /claim/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Promo CTA', desc: '"Claim offer" — the banner button; measured, never followed.', sel: '#top-banner button' }, { noScroll: true });
  await S('header-nav', q('header nav, header .mui-8qiahu').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header nav', desc: 'The sticky nav inside the header: logo, Solutions/Use cases/Who we serve/Resources, Pricing, EN, Log in, Book a demo.', sel: 'header nav' }, { noScroll: true });
  await S('nav-logo', q('a#navbar-logo-link, nav a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Deel wordmark in the nav.', sel: '#navbar-logo-link' }, { noScroll: true });
  await S('nav-link', q('nav a, nav button').filter({ hasText: /^Solutions/ }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Nav item (dropdown)', desc: '"Solutions" — a dropdown nav item; measured, never followed.', sel: 'nav .mui-1fo3fxi' }, { noScroll: true });
  await S('nav-plain-link', q('nav a').filter({ hasText: /^Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: '"Pricing" — a plain nav link; measured, never followed.', sel: 'nav .mui-1moi9ht' }, { noScroll: true });
  await S('nav-locale', q('nav a, nav button').filter({ hasText: /^EN/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Locale switch', desc: 'The "EN" language/locale switch in the nav; measured, never changed.', sel: 'nav a, nav button' }, { noScroll: true });
  await S('nav-login', q('nav a').filter({ hasText: /log ?in/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in link', desc: '"Log in" — outbound to app.deel.com; measured, never followed.', sel: 'nav a[href*="app.deel.com"]' }, { noScroll: true });
  await S('nav-demo', q('header a, header button, nav a, nav button').filter({ hasText: /book a demo/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Book a demo CTA', desc: 'The nav "Book a demo" button; measured, never followed.', sel: 'nav .mui-1wshw4o' }, { noScroll: true });
  await S('menu-item', q('a').filter({ hasText: /pay teams locally|deel hire/i }).filter({ visible: true }).first(), ['default', 'focus-visible'], { group: g, title: 'Mega-menu item', desc: '"Deel Payroll - Pay teams locally or globally" — a link inside the Solutions mega dropdown; measured after clicking the nav item open, never followed.', sel: 'menu a' }, { open: openSolutions, noScroll: true });
  await openSolutions();
  await SJ('menu-panel', 'js:[...document.querySelectorAll("a")].find((a) => /deel payroll overview/i.test(a.textContent))?.parentElement', { group: g, title: 'Mega-menu panel', desc: 'The Solutions mega dropdown container (1241x629) opened by the nav item click; measured open, its links never followed.', sel: 'js: menu panel' });
  const h = G.home;
  await S('hero-block', q('h1').filter({ visible: true }).first().locator('xpath=ancestor::*[self::section or contains(@class,"hero")][1]'), ['default'], { group: h, title: 'Hero block', desc: 'The dark hero section ("Hire, manage, pay, & equip anyone, anywhere." on a dark field).', sel: 'hero section' }, { noScroll: true });
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero heading', desc: '"Hire, manage, pay, & equip anyone, anywhere." — the BagossCondensed hero title.', sel: 'h1' }, { noScroll: true });
  await S('hero-tile', q('h1').filter({ visible: true }).first().locator('xpath=ancestor::*[self::section or contains(@class,"hero")][1]').locator('button.group, button[class*="flex-1"]').filter({ hasText: /hire anywhere/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero action tile', desc: '"Hire anywhere" — a quick-action tile under the hero title; measured, never followed.', sel: 'a.group' });
  await S('hero-demo', q('a, button').filter({ hasText: /^Book a demo$/ }).filter({ visible: true }).nth(1), B4, { group: h, title: 'Hero demo button', desc: 'The hero "Book a demo" pill (375x51 rounded-full); measured, never followed.', sel: 'main a, main button' });
  await S('section-heading', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A big Bagoss section heading ("The global people platform").', sel: 'h2' });
  await S('product-card', q('a.group[class*="bg-surface"], a.group[class*="rounded"]').filter({ hasText: /deel payroll/i }).filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: h, title: 'Product card', desc: 'A "Deel Payroll" product card in the global-people-platform grid; measured, never followed.', sel: 'section a' });
  await S('review-band', q('[class*="video-carousel"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Reviews band', desc: 'The "Our customer reviews" video-carousel band (1440x1206).', sel: 'reviews section' });
  await S('review-card', q('[class*="video-carousel"] a').filter({ hasText: /read case study/i }).filter({ visible: true }).first().locator('xpath=ancestor::div[contains(@class,"gap-md")][1]'), ['default'], { group: h, title: 'Review card', desc: 'A customer-review slide inside the video-carousel band (the ~840x638 video card plus caption and case-study link); its link measured, never followed.', sel: 'video-carousel slide' });
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The footer band: product/company/resource columns, social icons, legal links.', sel: 'footer' });
  await S('footer-heading', q('footer h3, footer [class*="heading" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer column heading', desc: 'A footer column heading ("Solutions"/"Deel Platform"/"Resources").', sel: 'footer h3' });
  await S('footer-link', q('footer a').filter({ hasText: /about us/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: '"About us" — a footer menu link; measured, never followed.', sel: 'footer a' });
  await S('social-link', q('footer a[href*="linkedin"], footer a[href*="twitter"], footer a[href*="x.com"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social icon link', desc: 'A social icon link in the footer; measured, never followed.', sel: 'footer a[href*="linkedin"]' });
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('price-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing heading', desc: '"Transparent and fair pricing that grows with your business".', sel: 'h1' }, { noScroll: true });
  await S('price-card', q('div[class*="shadow-elevation-2dp"], div[class*="elevation"]').filter({ hasText: /\$\s?\d/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Price card', desc: 'A pricing tier card (Find talent / Hire contractors / Hire employees).', sel: 'div[class*="elevation"]' });
  await S('price-cta', q('div[class*="shadow-elevation-2dp"], div[class*="elevation"]').filter({ hasText: /\$\s?\d/ }).first().locator('a, button').filter({ hasText: /book a demo|get started/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Price CTA', desc: 'The "Book a demo"/"Get started" button inside a pricing tier card (395x51); measured, never followed.', sel: 'tier card a, tier card button' });
  const faq = await firstFaqSummary();
  await S('faq-item', faq, ['default', 'opened', 'focus-visible'], { group: g, title: 'FAQ accordion', desc: 'A product-faqs MUI accordion summary; opened via its own click toggle.', sel: '[class*="MuiAccordionSummary"]' }, { allowLink: true });
}

async function hr() {
  if (!(await newPage('hr'))) return;
  await sheetsFor('hr');
  await chrome('hr');
  const g = G.hr;
  await S('hr-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product heading', desc: 'The Deel HR page hero heading.', sel: 'h1' }, { noScroll: true });
  await S('hr-cta', q('main a, main button').filter({ hasText: /book a demo|get started|see deel/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Product CTA', desc: 'A product-page CTA; measured, never followed.', sel: 'main a, main button' });
}

async function payroll() {
  if (!(await newPage('payroll'))) return;
  await sheetsFor('payroll');
  await chrome('payroll');
  const g = G.payroll;
  await S('payroll-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Payroll heading', desc: 'The Global Payroll page hero heading.', sel: 'h1' }, { noScroll: true });
}

async function about() {
  if (!(await newPage('about'))) return;
  await sheetsFor('about');
  await chrome('about');
  const g = G.about;
  await S('about-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'About heading', desc: 'The About page heading.', sel: 'h1' }, { noScroll: true });
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-nav-bar', q('header nav, nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav', sel: 'nav at 390' }, { noScroll: true });
  await S('m-logo', q('a#navbar-logo-link, nav a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile logo', sel: '#navbar-logo-link at 390' }, { noScroll: true });
  await S('m-hamburger', q('header button[aria-label*="menu" i], header button[aria-label*="navigation" i], header button').last(), ['default', 'pressed'], { group: g, title: 'Mobile hamburger', desc: 'The hamburger/drawer trigger at 390px.', sel: 'header button' }, { noScroll: true });
  await S('m-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero heading', desc: 'The hero h1 at 390px.', sel: 'h1' });
  await S('m-demo', q('a, button').filter({ hasText: /^Book a demo$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile demo CTA', desc: 'A Book a demo button at 390px; measured, never followed.', sel: 'main a, main button' });
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); deel.com paints a single light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, hr, payroll, about, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (a nav link's hover),
  // so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'nav a');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only when its page was not blocked this
    // run: an edge-blocked route keeps its earlier readings under their
    // original provenance instead of being erased and republished.
    if (!touched.has(key) && !pages.length && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
