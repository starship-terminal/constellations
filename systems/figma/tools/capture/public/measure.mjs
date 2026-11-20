// Measures figma.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing contact login signup community make downloads faq blog careers mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// figma.com is two public stacks signed out. The marketing pages
// (www.figma.com/...) are a Next.js + Emotion app on the declared --fig-*
// token layer, all painted light — a :root[data-theme='dark'] layer ships in
// the CSS but no public page carried the attribute. /community, /login and
// /signup are the product app shell (data-product-locale on <html>), a
// different stack that also paints light. The Emotion class names are hashed,
// so specs select by role, aria-label, semantic attribute
// (data-nav-dropdown-trigger, [name=...]) or text. Nothing is sent, bought or
// signed into: the only presses are local UI toggles — the header's
// Products/Solutions dropdown triggers, the pricing feature accordions, the
// mobile nav button; the contact, prompt, login and signup fields are typed
// into and cleared, never submitted; Submit, Log in, Continue-with-* and every
// CTA are measured, never followed. The consent dialog is hidden, never
// answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, LOGIN_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing/', contact: '/contact/', login: LOGIN_URL, signup: '/signup', community: '/community', make: '/make/', downloads: '/downloads/', faq: '/design-systems/', blog: '/blog/', careers: '/careers/', mobile: '/' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes an edge block gates this run: components last measured on them keep
// their earlier readings instead of being pruned below (a blocked pass must
// never erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 9000, promo = 'close', url = null } = {}) {
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
  const loaded = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });
  if (!loaded || await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
    c.states[state] = { ...s, crop: file, via: opts.via, run };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    // A failed re-read must not erase an earlier successful one: keep the
    // saved style and record the failed attempt beside it.
    const prev = c.states[state];
    if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
    else c.states[state] = { error: String(e.message || e).slice(0, 200) };
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
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else {
          await toggle(loc, { allowLink: opts.allowLink });
          await page.waitForTimeout(900);
          // A collapsible that reports expansion must still be open when its
          // "opened" reading is taken; a control without the attribute is
          // trusted (some toggles expose no state).
          const expanded = await loc.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null);
          if (expanded === 'false') throw new Error('the opened state measured closed (aria-expanded="false" after the toggle)');
          via = 'own toggle';
        }
      } else if (st === 'closed') {
        await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle';
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  // A listed state that failed its re-read kept the earlier evidence under
  // rerunError (and its own earlier `run`); the entry then republishes under
  // the earlier run's page/run/url and records the miss, so retained readings
  // never carry the new run's date.
  if (keep && list.some((st) => out.components[key].states[st]?.rerunError)) {
    Object.assign(out.components[key], keep);
    out.components[key].recaptureMissed = run;
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, accordion, sheet trigger). Refuses a
// submit button and any control whose text names an action this kit must
// never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|sign up|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|get started for free|claim|share|export|select|continue|continue with.*|claim this offer|try again)$/i;
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

// Whether the page paints a different transition under prefers-reduced-motion:
// the same component re-read in a context with reduce on.
async function reducedMotion(key, sel) {
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(8000);
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
  shell: 'Site chrome', home: 'Home', pricing: 'Pricing', contact: 'Contact sales form',
  auth: 'Login and signup (product shell)', community: 'Community (product shell)',
  prompt: 'Prompt surfaces', resources: 'Blog, downloads and careers',
  faq: 'FAQ accordions', mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens the header's "Products" nav-dropdown: a
// button[data-nav-dropdown-trigger] whose panel mounts beside it. A pointer
// click flips aria-expanded; keyboard Enter is the fallback — a local UI
// toggle, never a link. Escape closes it afterwards.
async function openProductsMenu() {
  const btn = page.locator('button[data-nav-dropdown-trigger]').filter({ hasText: /^Products$/ }).first();
  if (!(await btn.count())) return 'no Products trigger';
  const open = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true';
  if (await open()) return 'the Products dropdown was already open';
  for (let i = 0; i < 3; i++) {
    await btn.click({ timeout: 4000 }).catch(() => {});
    await page.waitForTimeout(700);
    if (await open()) return 'clicked the "Products" trigger to open the nav dropdown';
    await btn.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(700);
    if (await open()) return 'focused the "Products" trigger and pressed Enter to open the nav dropdown';
  }
  return 'activated "Products"; the dropdown did not report open';
}

// Opens the mobile nav overlay: the "Open navigation menu" button. Pointer
// activation first, then keyboard Enter.
async function openMobileMenu() {
  // The hamburger flips aria-expanded; the overlay div mounts beside it.
  const open = () => page.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find((x) => /navigation menu/i.test(x.getAttribute('aria-label') || ''));
    return !!b && b.getAttribute('aria-expanded') === 'true';
  }).catch(() => false);
  if (await open()) return 'the nav overlay was already open';
  const b = page.locator('button[aria-label*="navigation menu"]').filter({ visible: true }).first();
  if (!(await b.count())) return 'no menu toggle';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    if (await open()) return 'clicked "Open navigation menu" to open the nav overlay';
    await b.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(900);
    if (await open()) return 'focused "Open navigation menu" and pressed Enter to open the nav overlay';
  }
  return 'activated "Open navigation menu"; the overlay did not report open';
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The fixed top bar on every marketing page: the Figma mark, Products/Solutions/Community/Resources dropdown triggers, Pricing, Log in, Contact sales and the "Get started for free" CTA.', sel: 'header' }, { noScroll: true });
  await S('mkt-logo', q('header a[href="/"], header a[href="https://www.figma.com/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Figma mark in the header, linking home.', sel: 'header a[href=/]' }, { noScroll: true });
  await S('nav-dropdown-btn', q('button[data-nav-dropdown-trigger]').filter({ hasText: /^Products$/ }).first(), [...B4, 'opened'], { group: g, title: 'Nav dropdown trigger', desc: 'The "Products" header button — a data-nav-dropdown-trigger that opens the products dropdown. The opened state was measured after its own toggle click; aria-expanded had to stay true.', sel: 'button[data-nav-dropdown-trigger] Products' }, { noScroll: true });
  await S('nav-panel', q('button[data-nav-dropdown-trigger][aria-expanded="true"]').locator('xpath=ancestor::li[1]/following-sibling::li[1]//nav[1]/ancestor::div[2]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Products dropdown panel', desc: 'The dropdown panel opened by the "Products" trigger (Figma Design, Make, Weave, Dev Mode, Motion, Specs, FigJam, Slides, Draw, Sites, Buzz, AI workflows, Release notes, Downloads); its links were never followed.', sel: 'products dropdown panel' }, { open: openProductsMenu, noScroll: true, noReset: true });
  await S('nav-menu-item', q('button[data-nav-dropdown-trigger][aria-expanded="true"]').locator('xpath=ancestor::li[1]/following-sibling::li[1]').locator('a').filter({ hasText: /^Figma Design/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Dropdown item', desc: 'The "Figma Design" item inside the opened products dropdown; measured, never followed.', sel: 'products dropdown item' }, { open: openProductsMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('nav-pricing', q('header a, nav a').filter({ hasText: /^Pricing$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The "Pricing" header link; measured, never followed.', sel: 'header a Pricing' }, { noScroll: true });
  await S('nav-login', q('header a, nav a').filter({ hasText: /^Log in$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in link', desc: 'The "Log in" header link to /login; measured, never followed.', sel: 'header a Log in' }, { noScroll: true });
  await S('nav-cta', q('header a, nav a').filter({ hasText: /^Get started for free$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Header CTA', desc: 'The dark "Get started for free" header pill; links to /signup, measured never followed.', sel: 'header a Get started for free' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', await domFind(page, /\S/, { sel: 'h1', tag: 'h1', minW: 200, minH: 20 }), ['default'], { group: h, title: 'Hero headline', desc: '"The full-stack creative canvas" — the figma.com hero display heading.', sel: 'h1' }, { noScroll: true });
  await S('hero-cta', q('main a').filter({ hasText: /^Get started/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The dark "Get started" pill in the hero; links to /signup, measured never followed.', sel: 'hero Get started' }, { noScroll: true });
  await S('play-btn', q('main button').filter({ hasText: /^\s*Play\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Demo play button', desc: 'A "Play" control on a hero/section product demo video; a local media toggle, measured not held.', sel: 'main button Play' });
  await S('section-h2', q('main h2').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading further down the home page.', sel: 'main h2' });
  const f = G.footer;
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: f, title: 'Footer', desc: 'The page footer: product/use-case/resource columns, social icons and the locale button.', sel: 'footer' });
  await S('footer-link', q('footer a').filter({ hasText: /^Careers$/ }).first(), B4, { group: f, title: 'Footer link', desc: 'A footer sitemap link; measured, never followed.', sel: 'footer a Careers' });
  await S('locale-btn', q('footer button, [role="contentinfo"] button').filter({ hasText: /^English$/ }).filter({ visible: true }).first(), B4, { group: f, title: 'Locale button', desc: 'The "English" locale button in the footer — a local UI toggle for the locale list; measured, never toggled.', sel: 'footer button English' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('price-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing headline', desc: '"Pick your plan, choose your seats" — the /pricing masthead.', sel: 'h1' }, { noScroll: true });
  await S('price-toggle', q('button').filter({ hasText: /^Monthly\s*Annual$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Billing toggle', desc: 'The Monthly/Annual segmented control; measured at rest, never toggled (toggling would re-price the grid).', sel: 'billing Monthly/Annual toggle' }, { noScroll: true });
  await S('seat-combo', q('button[role="combobox"], [role="combobox"]').filter({ hasText: /seat/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Seat combobox', desc: 'The "Full seat" role combobox that re-prices the grid; measured at rest, never opened (its options recompute prices).', sel: 'seat combobox' });
  await S('feature-switch', q('[role="switch"], button[aria-checked]').filter({ hasText: /features/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Feature switch', desc: 'The "All features / Key features" switch (role=switch); measured at rest, never toggled.', sel: 'features switch' });
  await S('plan-card', q('button').filter({ hasText: /^Why choose Professional\?/ }).locator('xpath=ancestor::article[1]').first(), ['default'], { group: g, title: 'Plan card', desc: 'The Professional plan column: name, price, seat copy and its CTA.', sel: 'plan card' });
  await S('plan-cta', q('article').locator('a, button').filter({ hasText: /^(Get started|Contact sales|Try for free|Upgrade)/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s action (Get started / Contact sales), scoped to a plan article so the header\'s "Contact sales" link cannot match first; measured, never followed.', sel: 'plan card CTA' });
  await S('feature-acc', q('button').filter({ hasText: /^(Components|Auto layout|Styles|Variables)$/ }).filter({ visible: true }).first(), ['default', 'opened', 'hover'], { group: g, title: 'Feature accordion', desc: 'A feature-list accordion in the comparison grid ("Components", "Auto layout", ...); the opened state was measured after clicking it — a local UI toggle.', sel: 'feature accordion button' });
  save();
}

async function contact() {
  if (!(await newPage('contact'))) return;
  await sheetsFor('contact');
  await chrome('contact');
  const g = G.contact;
  await S('contact-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact headline', desc: 'The /contact masthead over the sales form.', sel: 'h1' }, { noScroll: true });
  await S('field-email', q('input[name="email"], input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field', desc: 'The work-email input; focused and typed into then cleared — never submitted.', sel: 'input[name=email]' }, { noScroll: true, fillText: 'name@example.com' });
  await S('field-firstname', q('input[name="firstName"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'First name field', desc: 'The first-name input; focused and typed into then cleared — never submitted.', sel: 'input[name=firstName]' }, { noScroll: true, fillText: 'Ada' });
  await S('field-lastname', q('input[name="lastName"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Last name field', desc: 'The last-name input; focused and typed into then cleared — never submitted.', sel: 'input[name=lastName]' }, { noScroll: true, fillText: 'Lovelace' });
  await S('field-topic', q('form').locator('input:not([name]):not([type])').filter({ visible: true }).first(), FIELD, { group: g, title: 'Free-text field', desc: 'The unnamed free-text input on the sales form\'s first step (the name=topic twin is a display:none honeypot); focused and typed into then cleared — never submitted.', sel: 'contact unnamed text input' }, { noScroll: true, fillText: 'A product question' });
  await S('next-btn', q('button[type="submit"], button').filter({ hasText: /^Next step$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Next step button', desc: 'The multi-step form\'s "Next step" button; its states were measured but the button was never clicked — the form never advanced.', sel: 'contact Next step' }, { noScroll: true });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 10000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.auth;
  await S('login-panel', q('form, [class*="login" i], main').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login panel', desc: 'The product-shell sign-in card on /login: "Sign in to Figma" with Google SSO, e-mail and password.', sel: 'login form' }, { noScroll: true });
  await S('login-google', q('button').filter({ hasText: /Continue with Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google SSO button', desc: 'The "Continue with Google" button; measured, never pressed.', sel: 'login Continue with Google' }, { noScroll: true });
  await S('login-email', q('input[type="email"], input[name="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (login)', desc: 'The e-mail input on the sign-in card; focused and typed into then cleared — never submitted.', sel: 'login input[type=email]' }, { noScroll: true, fillText: 'name@example.com' });
  await S('login-password', q('input[type="password"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Password field (login)', desc: 'The password input on the sign-in card; focused and typed into then cleared — never submitted.', sel: 'login input[type=password]' }, { noScroll: true, fillText: 'not-a-real-password' });
  await S('login-submit', q('button[type="submit"], button').filter({ hasText: /^Log in$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in submit', desc: 'The "Log in" submit button; its states were measured but the button was never clicked — nothing was submitted.', sel: 'login Log in' }, { noScroll: true });
  await S('login-sso', q('a').filter({ hasText: /single sign-on|sso/i }).filter({ visible: true }).first(), B4, { group: g, title: 'SSO link', desc: 'The "Use single sign-on" link; measured, never followed.', sel: 'login Use single sign-on' }, { noScroll: true });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 10000 }))) return;
  await sheetsFor('signup');
  await chrome('signup');
  const g = G.auth;
  await S('signup-panel', q('form, [class*="signup" i], [class*="register" i], main').filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup panel', desc: 'The product-shell sign-up card on /signup: "Welcome to Figma" with Google SSO and an e-mail field.', sel: 'signup form' }, { noScroll: true });
  await S('signup-google', q('button').filter({ hasText: /Continue with Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google SSO button (signup)', desc: 'The "Continue with Google" button on /signup; measured, never pressed.', sel: 'signup Continue with Google' }, { noScroll: true });
  await S('signup-email', q('input[type="email"], input[name="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (signup)', desc: 'The e-mail input on the sign-up card; focused and typed into then cleared — never submitted.', sel: 'signup input[type=email]' }, { noScroll: true, fillText: 'name@example.com' });
  await S('signup-continue', q('button').filter({ hasText: /Continue with email/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue with email', desc: 'The "Continue with email" button; its states were measured but the button was never clicked — nothing was submitted.', sel: 'signup Continue with email' }, { noScroll: true });
  save();
}

async function community() {
  if (!(await newPage('community', { wait: 10000 }))) return;
  await sheetsFor('community');
  await chrome('community');
  const g = G.community;
  await S('comm-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Community headline', desc: '"Discover community-made libraries, plugins, icon sets, and more" — the /community masthead in the product shell.', sel: 'h1' }, { noScroll: true });
  await S('comm-search', q('input[type="text"], input[type="search"], input[placeholder]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Community search', desc: 'The "Search for resources like …" input; focused and typed into then cleared — never searched.', sel: 'community search input' }, { noScroll: true, fillText: 'portfolio' });
  await S('comm-cat', q('button').filter({ hasText: /^Design resources$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Category button', desc: 'A category filter button (Design resources / Websites / Extensions / Whiteboarding / Presentations); measured at rest, never toggled.', sel: 'community category button' }, { noScroll: true });
  await S('comm-login', q('button').filter({ hasText: /^Log in$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Community Log in', desc: 'The product-shell "Log in" button; measured, never pressed.', sel: 'community Log in' }, { noScroll: true });
  await S('comm-signup', q('button').filter({ hasText: /^Sign up$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Community Sign up', desc: 'The product-shell "Sign up" button; measured, never pressed.', sel: 'community Sign up' }, { noScroll: true });
  await S('comm-banner-nav', q('button[aria-label="Next banner"]').filter({ visible: true }).first(), B4, { group: g, title: 'Banner carousel control', desc: 'The hero banner carousel\'s "Next banner" control — a local UI toggle; measured, never cycled.', sel: 'community Next banner' }, { noScroll: true });
  await S('comm-card', q('button[aria-label^="Riff:"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Resource card', desc: 'A community "Riff" card (thumbnail, title, author, like count); measured, never followed.', sel: 'community Riff card' });
  await S('comm-like', q('button[aria-label^="Like"]').filter({ visible: true }).first(), B4, { group: g, title: 'Like button', desc: 'A resource card\'s like button; measured, never pressed (a like would write to an account).', sel: 'community like button' });
  save();
}

async function make() {
  if (!(await newPage('make'))) return;
  await sheetsFor('make');
  const g = G.prompt;
  await S('prompt-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Make headline', desc: 'The /make masthead — "Figma Make".', sel: 'h1' }, { noScroll: true });
  await S('prompt-textarea', q('textarea').filter({ visible: true }).first(), FIELD, { group: g, title: 'Prompt textarea', desc: 'The "What do you want to make?" prompt box on /make; focused and typed into then cleared — never submitted.', sel: 'make textarea' }, { noScroll: true, fillText: 'A landing page for a coffee roaster' });
  await S('prompt-submit', q('textarea').locator('xpath=following::button[@type="submit"][1]').filter({ visible: true }).first(), B4, { group: g, title: 'Prompt submit', desc: 'The prompt box\'s icon-only submit button; its states were measured but the button was never clicked — nothing was sent.', sel: 'make submit button' }, { noScroll: true });
  save();
}

async function downloads() {
  if (!(await newPage('downloads'))) return;
  await sheetsFor('downloads');
  const g = G.resources;
  await S('dl-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Downloads headline', desc: 'The /downloads masthead — "Figma downloads".', sel: 'h1' }, { noScroll: true });
  await S('dl-btn', q('main a').filter({ hasText: /^Desktop app for macOS$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Download link', desc: 'The "Desktop app for macOS" download link (desktop apps, mobile apps, font installers, the Chrome extension); measured, never followed.', sel: 'downloads platform link' });
  save();
}

async function faq() {
  if (!(await newPage('faq'))) return;
  await sheetsFor('faq');
  const g = G.faq;
  await S('faq-acc', q('button').filter({ hasText: /^(What is Figma\?|What is a design system\?)$/ }).filter({ visible: true }).first(), ['default', 'closed'], { group: g, title: 'FAQ accordion', desc: 'A question row in the /design-systems FAQ (all accordions mount open); the closed state was measured after clicking the row — a local UI toggle.', sel: 'FAQ accordion button' });
  save();
}

async function blog() {
  if (!(await newPage('blog'))) return;
  await sheetsFor('blog');
  const g = G.resources;
  await S('blog-topics', q('button').filter({ hasText: /^Topics$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Topics button', desc: 'The blog index\'s "Topics" filter button — a local UI toggle; measured, never toggled.', sel: 'blog Topics' }, { noScroll: true });
  await S('blog-search', q('button[aria-label="Search"], button:has-text("Search")').filter({ visible: true }).first(), B4, { group: g, title: 'Search button', desc: 'The blog index\'s "Search" button — a local UI toggle; measured, never toggled.', sel: 'blog Search' }, { noScroll: true });
  await S('blog-subscribe', q('input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Newsletter field', desc: 'The editorial-newsletter e-mail input in the blog rail; focused and typed into then cleared — never subscribed.', sel: 'blog newsletter input' }, { fillText: 'name@example.com' });
  save();
}

async function careers() {
  if (!(await newPage('careers'))) return;
  await sheetsFor('careers');
  const g = G.resources;
  await S('careers-cta', q('a').filter({ hasText: /See open positions/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Careers CTA', desc: 'The "See open positions" link on /careers; measured, never followed.', sel: 'careers See open positions' }, { noScroll: true });
  await S('job-link', q('main a').filter({ hasText: /Engineer|Designer|Manager|Director/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Job link', desc: 'An open-position link in the careers list; measured, never followed.', sel: 'careers job link' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('header').filter({ has: q('button[aria-label*="navigation menu"]') }).filter({ has: q('a[href*="/signup"]') }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header at 390 wide: the Figma mark, "Get started for free", the nav button and the locale button.', sel: 'mobile header' }, { noScroll: true });
  await S('m-cta', q('header a[href="/signup"], header a[href="https://www.figma.com/signup"]').filter({ visible: true }).last(), B4, { group: g, title: 'Mobile header CTA', desc: 'The header "Get started for free" pill at 390 wide; measured never followed.', sel: 'mobile header Get started for free' }, { noScroll: true });
  const ham = q('button[aria-label="Open navigation menu"]').filter({ visible: true }).first();
  await S('m-menu-btn', ham, [...B4, 'opened'], { group: g, title: 'Mobile menu button', desc: 'The "Open navigation menu" button — a local UI toggle; the opened state was measured after activating it.', sel: 'button[aria-label=Open navigation menu]' }, { noScroll: true, allowLink: true });
  await S('m-drawer', q('button[aria-label="Close navigation menu"]').locator('xpath=following::*[self::ul or self::nav or self::ol][.//button[normalize-space(.)="Products"]][1]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav overlay', desc: 'The accordion nav inside the nav overlay opened by the menu button (Products/Solutions/Community/Resources accordions plus the page links); its links were never followed.', sel: 'mobile nav overlay accordion' }, { open: openMobileMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide.', sel: 'mobile h1' });
  await S('m-hero-cta', q('main a').filter({ hasText: /^Get started/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile hero CTA', desc: 'The hero "Get started" pill at 390 wide; measured never followed.', sel: 'mobile hero Get started' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every marketing page on www.figma.com paints the :root light token layer (a :root[data-theme="dark"] layer is declared but never painted publicly); /community, /login and /signup are the product app shell, a different stack that also paints light';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, contact, login, signup, community, make, downloads, faq, blog, careers, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the header CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a[href="/signup"], header a[href="https://www.figma.com/signup"]');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only when its page finished this run: a
    // page the run never reached, and an edge-blocked route, keeps its earlier
    // readings under their original provenance instead of being erased and
    // republished.
    if (!touched.has(key) && !pages.length && finishedPages.has(c.page) && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
