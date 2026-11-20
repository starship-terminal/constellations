// Measures glassnode.com's signed-out public components in every state
// reachable without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home vector contact studio-pricing auth-login research
//        research-article docs docs-metric tokenization mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// glassnode.com is five public stacks signed out. The marketing pages are a
// Next.js + SCSS-modules app on the declared --light_*/--base_* token layer,
// painted light only (dark in-page sections, no global theme).
// studio.glassnode.com is the React product shell on the declared --gds-*
// layer: /pricing, /charts/*, /dashboards/*, /market-compass, /get-listed and
// /contact are reachable signed out; a html[data-theme="dark-theme"] layer is
// declared but no public theme control exists, so only the painted light
// shell is measured. The studio "Log in" button leads to the Auth0 universal
// login at auth.glassnode.com/u/login?state=...; the auth-login pass reaches
// it through that real click and records the sanitized origin+path.
// research.glassnode.com is a Ghost publication (its dark toggle is a local
// UI control, measured at rest — the switched state is evidence from the
// screenshots pass). docs.glassnode.com is a GitBook site.
// tokenization.glassnode.com is a dark-by-default registry app. The marketing
// classes are SCSS modules (*-module-scss-module__<hash>__<name>), so specs
// select by role, aria-label, semantic attribute or text. Nothing is sent,
// bought or signed into: the only presses are local UI toggles — the
// header's Products dropdown trigger, the Vector FAQ accordions, the studio
// metric-catalog expanders and the phone's hamburger; the newsletter and
// Auth0 username fields are typed into and cleared, never submitted; "Log
// in", "Sign up", "Continue", "Continue with Google", "Send me free
// research", "Download sample" and every CTA are measured, never followed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, STUDIO_BASE, RESEARCH_BASE, DOCS_BASE, TOKENIZATION_BASE, LOGIN_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', vector: '/pricing/vector', contact: '/contact',
  'studio-pricing': STUDIO_BASE + '/pricing',
  // Reached by clicking the studio shell's own "Log in" — see authLogin().
  'auth-login': LOGIN_URL,
  research: RESEARCH_BASE + '/',
  // The current first article on the research index; resolved at run time.
  'research-article': RESEARCH_BASE + '/',
  docs: DOCS_BASE + '/', 'docs-metric': DOCS_BASE + '/data/metric-catalog',
  tokenization: TOKENIZATION_BASE + '/',
  mobile: '/',
};
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
  await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });
  if (await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
  shell: 'Marketing site chrome', home: 'Marketing home', vector: 'Vector pricing page',
  contact: 'Marketing contact page', studio: 'Studio shell (signed out)',
  auth: 'Auth0 universal login', research: 'Research publication (Ghost)',
  docs: 'Docs site (GitBook)', tokenization: 'Tokenization registry',
  mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens the marketing header's "Products" nav dropdown: a plain header
// <button> whose aria-expanded flips. On this site a pointer hover already
// opens the panel and a click toggles it, so hover is tried first, then a
// click, then Enter — a local UI toggle, never a link. Escape closes it
// afterwards.
async function openProductsMenu() {
  const btn = page.locator('header button').filter({ hasText: /^Products$/ }).first();
  if (!(await btn.count())) return 'no Products trigger';
  const open = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true';
  if (await open()) return 'the Products dropdown was already open';
  for (let i = 0; i < 3; i++) {
    await btn.hover({ timeout: 4000 }).catch(() => {});
    await page.waitForTimeout(700);
    if (await open()) return 'hovered the "Products" trigger to open the nav dropdown';
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

// Opens the mobile nav: the header hamburger button (no accessible label —
// its class name carries "hamburger"). Pointer first, then Enter.
async function openMobileMenu() {
  const b = page.locator('header button[class*="hamburger" i], header button').filter({ visible: true }).first();
  if (!(await b.count())) return 'no menu toggle';
  const open = async () => (await b.getAttribute('aria-expanded').catch(() => null)) === 'true';
  if (await open()) return 'the nav overlay was already open';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    if (await open()) return 'clicked the hamburger to open the nav overlay';
    await b.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(900);
    if (await open()) return 'focused the hamburger and pressed Enter to open the nav overlay';
  }
  return 'activated the hamburger; the overlay did not report open';
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The top bar on every marketing page: the Glassnode wordmark, the Products dropdown trigger, Pricing, Data, About and the "Launch Studio" CTA.', sel: 'header' }, { noScroll: true });
  await S('mkt-logo', q('header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Glassnode wordmark in the header, linking home.', sel: 'header a[href=/]' }, { noScroll: true });
  await S('nav-dropdown-btn', q('header button').filter({ hasText: /^Products$/ }).first(), [...B4, 'opened'], { group: g, title: 'Nav dropdown trigger', desc: 'The "Products" header button — aria-expanded flips and the dropdown panel mounts; a hover already opens it and a click toggles it. The opened state was measured after its own toggle.', sel: 'header button Products' }, { noScroll: true, noToggle: true, before: { opened: async (loc) => { await loc.hover({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(900); const e = await loc.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null); if (e !== 'true') { await loc.evaluate((el) => el.dispatchEvent(new MouseEvent('mouseover', { bubbles: true }))).catch(() => {}); await page.waitForTimeout(900); } return 'hovered the trigger to open the dropdown'; } } });
  await S('nav-menu-item', q('header a[href*="/products/"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Dropdown item', desc: 'A product entry inside the opened "Products" dropdown (Studio, Data, Research, Market Compass, Alpha Lab); measured, never followed.', sel: 'Products dropdown item' }, { open: openProductsMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('nav-link', q('header a').filter({ hasText: /^Pricing$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The "Pricing" header link; measured, never followed.', sel: 'header a Pricing' }, { noScroll: true });
  await S('nav-cta', q('header a').filter({ hasText: /^Launch Studio$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Header CTA', desc: 'The "Launch Studio" header action pointing at studio.glassnode.com; measured, never followed.', sel: 'header a Launch Studio' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', await domFind(page, /\S/, { sel: 'h1', tag: 'h1', minW: 200, minH: 20 }), ['default'], { group: h, title: 'Hero headline', desc: '"Pioneering digital asset market intelligence" — the home masthead.', sel: 'h1' }, { noScroll: true });
  await S('partner-report-link', await domFind(page, /Partner Reports/, { sel: 'a', tag: 'pr', minW: 200 }), ['default', 'hover'], { group: h, title: 'Partner report link', desc: 'The "Partner Reports" promo link under the hero ("Xapo Bank + Glassnode: Generating Yield on..."); measured, never followed.', sel: 'a Partner Reports' });
  await S('section-h2', await domFind(page, /\S{6,}/, { sel: 'h2', tag: 'h2', minW: 200, minH: 40 }), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading further down the home page ("Our flagship platform", ...) — a display-size h2, so transient microcopy never counts.', sel: 'h2 (display size)' });
  const f = G.footer;
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: f, title: 'Footer', desc: 'The page footer: the research subscribe field, the Use cases/Resources/About us/Legal columns and the Privacy settings control.', sel: 'footer' });
  await S('newsletter-field', q('input[type="email"]').filter({ visible: true }).last(), FIELD, { group: f, title: 'Newsletter field', desc: 'The "Enter your email" subscribe input; focused and typed into then cleared — never subscribed.', sel: 'input[type=email] Enter your email' }, { fillText: 'name@example.com' });
  await S('newsletter-btn', q('button, a').filter({ hasText: /^Send me free research$/ }).filter({ visible: true }).first(), B4, { group: f, title: 'Subscribe button', desc: 'The "Send me free research" subscribe button; its states were measured but the button was never clicked — nothing was submitted.', sel: 'Send me free research' });
  await S('privacy-btn', q('button').filter({ hasText: /^Privacy settings$/ }).filter({ visible: true }).first(), B4, { group: f, title: 'Privacy settings control', desc: 'The "Privacy settings" footer control that opens the consent manager; a local UI toggle — measured, never opened.', sel: 'Privacy settings' });
  await S('footer-link', q('footer a').filter({ hasText: /Case studies|The Week On-Chain/ }).filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', desc: 'A footer sitemap link; measured, never followed.', sel: 'footer link' });
  save();
}

async function vector() {
  if (!(await newPage('vector'))) return;
  await sheetsFor('vector');
  await chrome('vector');
  const g = G.vector;
  await S('vec-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Vector headline', desc: 'The /pricing/vector masthead over the Bitcoin Vector pitch.', sel: 'h1' }, { noScroll: true });
  await S('vec-billing-select', q('select').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Billing-cycle select', desc: 'The native <select> switching "Bill quarterly"/"Bill monthly" on the Vector price; measured at rest, never changed.', sel: 'select' });
  await S('vec-plan-card', await domFind(page, /\$\d/, { sel: 'div, li, article', tag: 'vpc', minW: 200, minH: 120 }), ['default'], { group: g, title: 'Plan card', desc: 'A price card on /pricing/vector — the plan name, monthly price and CTA inside a bordered card.', sel: 'plan card' });
  await S('vec-download-btn', q('button, a').filter({ hasText: /^Download sample$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Download sample button', desc: 'A "Download sample" control on the Vector page; measured, never pressed — no download was requested.', sel: 'Download sample' });
  await S('vec-faq', q('[aria-expanded], button').filter({ hasText: /^How is the Bitcoin Vector delivered\?$/ }).filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'FAQ accordion', desc: 'A question row in the Vector FAQ ("How is the Bitcoin Vector delivered?", "Can I unsubscribe at any time?", ...); the opened state was measured after its own toggle — a local UI toggle.', sel: 'Vector FAQ row' }, { noToggle: true, before: { opened: async (loc) => { for (let i = 0; i < 3; i++) { const e = await loc.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null); if (e === 'true') break; await loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.click())); await page.waitForTimeout(700); } return 'clicked the row until it reported open'; } } });
  save();
}

async function contact() {
  if (!(await newPage('contact'))) return;
  await sheetsFor('contact');
  await chrome('contact');
  const g = G.contact;
  await S('contact-h1', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact headline', desc: '"How can we connect" — the /contact masthead over the category cards.', sel: 'h1' }, { noScroll: true });
  await S('contact-category', await domFind(page, /Contact Sales|General Inquiries/, { sel: 'a, div, section', tag: 'cc', minW: 200, minH: 60 }), ['default', 'hover'], { group: g, title: 'Contact category card', desc: 'A contact-category card ("Contact Sales", "General Inquiries") that routes to the right form; measured, never followed.', sel: 'contact category card' });
  await S('contact-subscribe-btn', q('button, a').filter({ hasText: /^Send me free research$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Subscribe button (contact)', desc: 'The "Send me free research" subscribe button in the contact page\'s research band; measured, never pressed.', sel: 'Send me free research' });
  save();
}

async function studioPricing() {
  if (!(await newPage('studio-pricing', { url: STUDIO_BASE + '/pricing', wait: 14000 }))) return;
  await sheetsFor('studio-pricing');
  await chrome('studio-pricing');
  const g = G.studio;
  await S('st-navbar', q('div[class*="navbar_container"], header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Studio navbar', desc: 'The product-shell top bar on studio.glassnode.com: the wordmark, Home/Dashboards/Charts/Market Compass/Alpha Lab/Research/Tokenization nav, Resources, the search control, "Log in" and "Sign up".', sel: '.navbar_container' }, { noScroll: true });
  await S('st-nav-link', q('nav a, div[class*="navigation"] a, header a').filter({ hasText: /^Charts$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Studio nav link', desc: 'The "Charts" navbar link to /charts?a=BTC; measured, never followed.', sel: 'studio nav Charts' }, { noScroll: true });
  await S('st-login-btn', q('button').filter({ hasText: /^Log ?in$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in button', desc: 'The navbar "Log in" — navigates to the Auth0 universal login at auth.glassnode.com; measured, never pressed (the login form is captured on the auth-login pass).', sel: 'studio Log in' }, { noScroll: true });
  await S('st-signup-btn', q('div[class*="navbar"] button, header button').filter({ hasText: /^Sign up$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign up button', desc: 'The navbar "Sign up" — navigates to the Auth0 signup; measured, never pressed.', sel: 'studio Sign up' }, { noScroll: true });
  await S('st-search-btn', q('button[aria-label="search" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Search trigger', desc: 'The navbar search button that opens the metric/asset search; a local UI toggle — measured, never opened.', sel: 'studio search button' }, { noScroll: true });
  await S('st-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing headline', desc: '"Plans & Pricing" — the studio /pricing masthead.', sel: 'studio h1' }, { noScroll: true });
  await S('st-plan-card', await domFind(page, /ADVANCED/, { sel: 'div, li, article, section', tag: 'spc', minW: 200, minH: 200 }), ['default'], { group: g, title: 'Plan card', desc: 'A plan card on studio /pricing — one column of the plan grid (ADVANCED/PROFESSIONAL/...): name, price, billing copy and CTA.', sel: 'studio plan card' });
  await S('st-plan-signup-btn', q('button').filter({ hasText: /^Sign up$/ }).filter({ visible: true }).last(), B4, { group: g, title: 'Plan CTA', desc: 'A "Sign up" call-to-action inside a plan card; measured, never pressed.', sel: 'plan card Sign up' });
  await S('st-configure-btn', q('button').filter({ hasText: /^Configure$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Configure button', desc: 'The "Configure" control on the custom/enterprise plan card; measured, never pressed.', sel: 'plan card Configure' });
  await S('st-metrics-expander', q('button').filter({ hasText: /Show \d[\d,]* more metrics/ }).filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'Metric catalog expander', desc: 'A "Show N more metrics" expander in the public metric catalog on /pricing; the opened state was measured after its own toggle — a local UI toggle that reveals more catalog rows.', sel: 'Show N more metrics' });
  await S('st-faq', q('button, [aria-expanded]').filter({ hasText: /^How many assets does Glassnode/ }).filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'FAQ accordion', desc: 'A question row in the studio pricing FAQ ("How many assets does Glassnode...", "Is API access included...", ...); the opened state was measured after its own toggle — a local UI toggle.', sel: 'studio pricing FAQ' });
  save();
}

// The Auth0 universal login, reached by clicking the studio shell's own
// "Log in" button — the real signed-out path a visitor takes. The landing
// URL's volatile ?state= is not recorded; the component metadata carries the
// sanitized origin+path. The username field is typed into and cleared; the
// form is never submitted.
async function authLogin() {
  if (!(await newPage('auth-login', { url: STUDIO_BASE + '/', wait: 12000 }))) return;
  const btn = page.locator('button, a').filter({ hasText: /^Log ?in$/i }).filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! auth-login: no Log in control'); return; }
  await Promise.all([page.waitForURL(/auth\.glassnode\.com\/u\/login/, { timeout: 45000 }).catch(() => {}), btn.click({ timeout: 8000 }).catch(() => {})]);
  await page.waitForTimeout(7000);
  if (!/auth\.glassnode\.com/.test(page.url())) { log('  ! auth-login: did not reach the auth origin'); return; }
  out.components.__auth = { group: G.auth, title: 'Auth0 origin reached', page: 'auth-login', url: LOGIN_URL, desc: 'Marker: the studio shell\'s "Log in" was followed to auth.glassnode.com/u/login. Only the sanitized origin+path is recorded — the volatile ?state= parameter is never preserved.' };
  await sheetsFor('auth-login');
  await chrome('auth-login');
  const g = G.auth;
  URLS['auth-login'] = LOGIN_URL;
  const cardLoc = await domFind(page, /Email|Username|Continue/, { sel: 'form, div', tag: 'ac', minW: 200, minH: 200 });
  await S('auth-card', cardLoc, ['default'], { group: g, title: 'Login card', desc: 'The Auth0 universal-login card on auth.glassnode.com/u/login — the username/password form, "Continue", "Continue with Google", "Reset password" and "Sign up". Reached through the studio shell\'s real "Log in" button; the volatile ?state= parameter is never recorded.', sel: 'auth0 login form' }, { noScroll: true });
  await S('auth-email', q('input[name="username"], input[type="email"], input[type="text"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Username field', desc: 'The e-mail/username input on the Auth0 card; focused and typed into then cleared — never submitted.', sel: 'input[name=username]' }, { noScroll: true, fillText: 'name@example.com' });
  await S('auth-password', q('input[name="password"], input[type="password"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Password field', desc: 'The password input on the Auth0 card; focused only — nothing was typed or submitted.', sel: 'input[name=password]' }, { noScroll: true });
  await S('auth-continue', q('button[type="submit"]').filter({ hasText: /^Continue$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'The login form\'s "Continue" submit; its states were measured but the button was never clicked — no credentials were entered and nothing was submitted.', sel: 'auth0 Continue' }, { noScroll: true });
  await S('auth-google', q('button').filter({ hasText: /Continue with Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google SSO button', desc: 'The "Continue with Google" social-login submit; measured, never pressed.', sel: 'auth0 Continue with Google' }, { noScroll: true });
  await S('auth-reset', q('a').filter({ hasText: /^Reset password$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Reset password link', desc: 'The "Reset password" link to the Auth0 password-reset start; measured, never followed.', sel: 'auth0 Reset password' }, { noScroll: true });
  await S('auth-signup-link', q('a').filter({ hasText: /^Sign up$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign up link', desc: 'The "Sign up" link beside the login form; measured, never followed.', sel: 'auth0 Sign up' }, { noScroll: true });
  save();
}

async function research() {
  if (!(await newPage('research', { url: RESEARCH_BASE + '/' }))) return;
  await sheetsFor('research');
  await chrome('research');
  const g = G.research;
  await S('res-header', q('header, nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The Ghost publication header: the Glassnode apps menu, the tag nav (Week On-chain, Strategy Watch, Market Pulse, Partner Reports, Product & Research), search and the theme toggle.', sel: 'research header' }, { noScroll: true });
  await S('res-nav-link', q('header a, nav a').filter({ hasText: /^Week On-chain$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The "Week On-chain" tag link in the header nav; measured, never followed.', sel: 'research nav Week On-chain' }, { noScroll: true });
  await S('res-theme-toggle', q('button.gh-theme-toggle').filter({ visible: true }).first(), B4, { group: g, title: 'Theme toggle', desc: 'The "Switch to dark mode" Ghost theme toggle — a local UI control that removes data-theme="light" and repaints the page; measured at rest, never switched here (the dark surface is captured in the screenshots pass).', sel: '.gh-theme-toggle' }, { noScroll: true });
  await S('res-post-card', q('article').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Article card', desc: 'An article card in the research index (the current Week On-chain issue); measured, never followed.', sel: 'research article card' });
  await S('res-subscribe-field', q('input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Subscribe field', desc: 'The "Email" subscribe input on the research site; focused and typed into then cleared — never subscribed.', sel: 'research input[type=email]' }, { fillText: 'name@example.com' });
  await S('res-footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The research footer: the subscribe band, the sitemap columns and the legal links.', sel: 'research footer' });
  save();
}

async function researchArticle() {
  // Measure the current first article on the index (the week-on-chain issue).
  if (!(await newPage('research-article', { url: RESEARCH_BASE + '/' }))) return;
  const href = await page.evaluate(() => (document.querySelector('article a, .post-card a, h2 a, h3 a') || {}).href || null);
  if (!href) { log('  ! research-article: no article link'); return; }
  URLS['research-article'] = href.replace(/\?.*$/, '');
  await open(page, URLS['research-article'], { wait: 7000 });
  if (await blocked()) { log('  BLOCKED research-article'); failedPages.add('research-article'); return; }
  const g = G.research;
  await S('res-article-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article headline', desc: 'The published-article masthead on research.glassnode.com (the current Week On-chain issue); the article URL is recorded on the component.', sel: 'article h1' }, { noScroll: true });
  await S('res-article-p', q('article p, .gh-content p, main p').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article body text', desc: 'A paragraph in the article body — the Ghost theme\'s serif/sans reading measure.', sel: 'article p' });
  await S('res-article-tag', q('article a[href*="/tag/"], a[href*="/tag/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Article tag', desc: 'A tag link on the article; measured, never followed.', sel: 'article tag link' });
  save();
}

async function docs() {
  if (!(await newPage('docs', { url: DOCS_BASE + '/' }))) return;
  await sheetsFor('docs');
  const g = G.docs;
  await S('docs-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs header', desc: 'The GitBook docs header: "Glassnode Docs", the search field, the Website/Studio/Insights/Twitter links, "More" and the light/system/dark theme buttons.', sel: 'docs header' }, { noScroll: true });
  await S('docs-nav-link', q('header a').filter({ hasText: /^Studio$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Docs nav link', desc: 'The "Studio" header link out to studio.glassnode.com; measured, never followed.', sel: 'docs header link' }, { noScroll: true });
  await S('docs-theme-btn', q('button[aria-label="Switch to dark theme"]').filter({ visible: true }).first(), B4, { group: g, title: 'Theme button', desc: 'The GitBook "Switch to dark theme" button — a local UI control that flips .light/.dark on <html>; measured at rest, never switched here (the dark surface is captured in the screenshots pass).', sel: 'docs Switch to dark theme' }, { noScroll: true });
  await S('docs-search', q('input[placeholder*="Search" i], button[aria-label*="Search" i]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Search field', desc: 'The docs "Search" field — focused only; typing was not needed to read the focus ring.', sel: 'docs Search' }, { noScroll: true });
  await S('docs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Doc page headline', desc: '"Overview" — the docs landing headline on the GitBook stack.', sel: 'docs h1' }, { noScroll: true });
  await S('docs-side-link', q('aside a, nav a').filter({ hasText: /^Metric Catalog$/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Sidebar link', desc: 'A sidebar navigation link in the docs tree; measured, never followed.', sel: 'docs sidebar link' });
  await S('docs-quote-btn', q('a, button').filter({ hasText: /Request a quote/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Request a quote link', desc: 'The "Request a quote" banner link on the overview page; measured, never followed.', sel: 'docs Request a quote' });
  save();
}

async function docsMetric() {
  if (!(await newPage('docs-metric', { url: DOCS_BASE + '/data/metric-catalog' }))) return;
  await sheetsFor('docs-metric');
  const g = G.docs;
  await S('docs-metric-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Metric catalog headline', desc: '"Metric Catalog" — the API metric index page on the docs site.', sel: 'docs-metric h1' }, { noScroll: true });
  await S('docs-metric-link', q('main a, article a').filter({ hasText: /Address|Market|Network|Indicators/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Metric category link', desc: 'A metric-category link in the catalog; measured, never followed.', sel: 'docs metric category link' });
  await S('docs-code', q('pre, code').filter({ visible: true }).first(), ['default'], { group: g, title: 'Code or metric label', desc: 'A code/metric label on the catalog page — the GitBook monospace treatment.', sel: 'docs pre/code' });
  save();
}

async function tokenization() {
  if (!(await newPage('tokenization', { url: TOKENIZATION_BASE + '/', wait: 10000 }))) return;
  await sheetsFor('tokenization');
  await chrome('tokenization');
  const g = G.tokenization;
  await S('tok-shell', q('aside, nav, header').filter({ hasText: /Assets/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Registry nav', desc: 'The registry navigation on tokenization.glassnode.com: the Glassnode apps menu, search, the theme button and the Overview/Assets/Issuers/Products/Derivatives items with their live counts.', sel: 'tokenization nav' }, { noScroll: true });
  await S('tok-nav-item', q('a').filter({ hasText: /Assets/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav item', desc: 'The "Assets" nav item with its live asset count (3,727 at capture); measured, never followed.', sel: 'tokenization nav Assets' }, { noScroll: true });
  await S('tok-search-btn', q('button[aria-label="Search" i], input[placeholder*="Search" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Search control', desc: 'The "Search assets, issuers, products..." search control; a local UI toggle — measured, never opened.', sel: 'tokenization Search' }, { noScroll: true });
  await S('tok-theme-btn', q('button[aria-label="Switch to light theme"]').filter({ visible: true }).first(), B4, { group: g, title: 'Theme button', desc: 'The "Switch to light theme" control — flips [data-theme] on <html>; measured at rest on the painted dark surface, never switched here (the light surface is captured in the screenshots pass).', sel: 'tokenization Switch to light theme' }, { noScroll: true });
  await S('tok-request-btn', q('a, button').filter({ hasText: /^Request access$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Request access link', desc: 'The "Request access" nav action to /api-access; measured, never followed.', sel: 'tokenization Request access' }, { noScroll: true });
  await S('tok-stat', await domFind(page, /3,|2,|89/, { sel: 'a, div, span', tag: 'ts', minW: 40, minH: 16 }), ['default'], { group: g, title: 'Registry stat', desc: 'A live registry count (assets/issuers/products/derivatives) in the nav or hero — the dark theme\'s numeric treatment.', sel: 'registry stat' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header at 390 wide: the wordmark and the hamburger.', sel: 'mobile header' }, { noScroll: true });
  const ham = q('header button[class*="hamburger" i], header button').filter({ visible: true }).first();
  await S('m-menu-btn', ham, [...B4, 'opened'], { group: g, title: 'Mobile menu button', desc: 'The hamburger button — a local UI toggle; the opened state was measured after activating it.', sel: 'mobile hamburger' }, { noScroll: true, allowLink: true });
  await S('m-drawer', q('nav, [role="dialog"], div[class*="fixed"], div[class*="menu" i]').filter({ hasText: /Pricing/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Mobile nav overlay', desc: 'The navigation overlay opened by the hamburger (the same destinations as the desktop header); its links were never followed.', sel: 'mobile nav overlay' }, { open: openMobileMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide.', sel: 'mobile h1' });
  await S('m-newsletter-field', q('input[type="email"]').filter({ visible: true }).last(), FIELD, { group: g, title: 'Mobile newsletter field', desc: 'The "Enter your email" subscribe input at 390 wide; focused and typed into then cleared — never subscribed.', sel: 'mobile input[type=email]' }, { fillText: 'name@example.com' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the marketing site paints the declared --light_*/--base_* layer only (dark in-page sections, no global theme); studio.glassnode.com paints light signed out (its html[data-theme="dark-theme"] layer is declared but has no public control); auth.glassnode.com/u/login is the Auth0 universal login reached through the studio "Log in" (the volatile ?state= is never recorded); research/docs/tokenization paint light/light/dark respectively and each carries a real local theme control';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, vector, contact, 'studio-pricing': studioPricing, 'auth-login': authLogin, research, 'research-article': researchArticle, docs, 'docs-metric': docsMetric, tokenization, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the header CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a[href*="studio.glassnode.com"]');
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
