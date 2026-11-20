// Measures flask.do's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing mcp about security video-collaboration frame-io-alternative login mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// flask.do is one public surface signed out: a React-Router app on the
// declared --ds-* token layer, all painted in the dark `default` theme; no
// light variant or toggle exists. The class names are semantic utilities
// (button-primary, bg-surface-1, text-fg-1, element-border), so specs select
// by role, aria-label, class or text. The hero on / ships an interactive
// marketing demo of the product built from the same classes; its controls are
// measured as painted, and only its own "Version" chip is toggled. Nothing is
// sent, bought or signed into: the only presses are local UI toggles — a
// /pricing FAQ accordion and the "Billed quarterly"
// switch (toggled off, measured, then toggled back); the login e-mail field is
// typed into and cleared, never submitted; Log in, Continue-with-*, Book
// Demo/Call and every CTA are measured, never followed. The Add-to-Cursor MCP
// install link is external and never opened.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, LOGIN_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', mcp: '/mcp', about: '/about', security: '/security', 'video-collaboration': '/video-collaboration', 'frame-io-alternative': '/frame-io-alternative', login: LOGIN_URL, mobile: '/' };
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
  shell: 'Site chrome', home: 'Home and landing pages', demo: 'Marketing demo (pre-rendered product UI)',
  pricing: 'Pricing', docs: 'Docs and about', legal: 'Security and legal',
  auth: 'Login (signed-out)', mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens the mobile nav overlay: the icon-only `button[aria-label="Open menu"]`
// hamburger (md:hidden — it exists only at 390 wide, outside <header>).
// Pointer activation first, then keyboard Enter.
async function openMobileMenu() {
  const open = () => page.evaluate(() => {
    const b = document.querySelector('button[aria-label="Open menu"]');
    return !!b && (b.getAttribute('aria-expanded') === 'true' || !!document.querySelector('[role="dialog"]'));
  }).catch(() => false);
  if (await open()) return 'the nav overlay was already open';
  const b = page.locator('button[aria-label="Open menu"]').filter({ visible: true }).first();
  if (!(await b.count())) return 'no menu toggle';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    if (await open()) return 'clicked "Open menu" to open the nav overlay';
    await b.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(900);
    if (await open()) return 'focused "Open menu" and pressed Enter to open the nav overlay';
  }
  return 'activated "Open menu"; the overlay did not report open';
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home', { wait: 8000 }))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('div[class*="top-0"][class*="z-50"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The sticky top bar on every page (a div, not <header>): the Flask mark, the Pricing/Features nav links and the "Sign Up" CTA (which links to /home — the login boundary).', sel: 'div.top-0.z-50' }, { noScroll: true });
  await S('mkt-logo', q('a[aria-label="Flask"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Flask mark (aria-label="Flask") in the top bar, linking home.', sel: 'a[aria-label=Flask]' }, { noScroll: true });
  await S('nav-pricing', q('header a, nav a').filter({ hasText: /^Pricing$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The "Pricing" header link; measured, never followed.', sel: 'header a Pricing' }, { noScroll: true });
  await S('nav-features', q('header a, nav a').filter({ hasText: /^Features$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Features nav link', desc: 'The "Features" header link; measured, never followed. The header offers no Log in link — /login is reached through Sign Up.', sel: 'header a Features' }, { noScroll: true });
  await S('nav-cta', await domFind(page, /^Sign Up$/, { sel: 'a', tag: 'ncta' }), B4, { group: g, title: 'Header CTA', desc: 'The "Sign Up" CTA in the top bar — it links to /home, which redirects to /login; measured, never followed.', sel: 'nav "Sign Up" link' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', await domFind(page, /\S/, { sel: 'h1', tag: 'h1', minW: 200, minH: 20 }), ['default'], { group: h, title: 'Hero headline', desc: '"The world\'s fastest way to review video." — the flask.do hero display heading.', sel: 'h1' }, { noScroll: true });
  await S('hero-cta', q('main a, main button').filter({ hasText: /^(Open Flask|Get Started|Book a Demo|Try Flask)$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The hero\'s "Open Flask" pill — the primary call to action; measured, never followed.', sel: 'hero "Open Flask" button' });
  await S('hero-copy-prompt', await domFind(page, /^Copy Prompt$/, { sel: 'button, a', tag: 'hcp' }), B4, { group: h, title: 'Hero "Copy Prompt" button', desc: 'The hero\'s secondary "Copy Prompt" pill; measured, never pressed.', sel: 'hero "Copy Prompt" button' });
  const d = G.demo;
  await S('demo-breadcrumb', await domFind(page, /^ACME Studios$/, { sel: 'span, button', tag: 'dbr' }), B4, { group: d, title: 'Demo breadcrumb chip', desc: 'The demo mock\'s "ACME Studios" breadcrumb chip in the workspace bar; measured as painted.', sel: 'demo "ACME Studios" breadcrumb' });
  await S('demo-tab-context', await domFind(page, /v2\s*Context/i, { sel: 'button, [role="tab"]', tag: 'dtc' }), B4, { group: d, title: 'Demo context tab', desc: 'The demo\'s "v2 / Context" tab, painted as the active tab; measured as painted.', sel: 'demo "v2 Context" tab' });
  await S('demo-tab-feedback', await domFind(page, /Feedback\s*\|?\s*0/i, { sel: 'button, [role="tab"]', tag: 'dtf' }), B4, { group: d, title: 'Demo feedback tab', desc: 'The demo\'s "Feedback / 0" tab, painted as inactive; measured as painted.', sel: 'demo "Feedback 0" tab' });
  await S('demo-feedback-field', await domFind(page, /Leave Feedback/i, { sel: 'div, [contenteditable], input, textarea, span', tag: 'dff' }), ['default'], { group: d, title: 'Demo feedback composer', desc: 'The demo\'s "00:00 / Leave Feedback.." composer field, painted with a timestamp chip; measured as painted.', sel: 'demo "Leave Feedback" composer' });
  await S('demo-version-chip', await domFind(page, /^Version 3$/, { sel: 'button, [role="combobox"], [role="button"], div, span', tag: 'dvc' }), B4, { group: d, title: 'Demo version chip', desc: 'The demo\'s "Version 3" chip — the mock asset switcher; measured as painted, toggled once during screenshot capture.', sel: 'demo "Version 3" chip' });
  await S('demo-copy-link', await domFind(page, /Copy Link to Folder|Copy Link/i, { sel: 'button, [role="button"], a', tag: 'dcl' }), B4, { group: d, title: 'Demo "Copy Link" button', desc: 'The demo\'s "Copy Link to Folder" / "Copy Link" control; measured, never pressed.', sel: 'demo "Copy Link" button' });
  await S('demo-th', await domFind(page, /Latest Activity/i, { sel: 'th, button, [role="columnheader"], div, span', tag: 'dth' }), ['default', 'hover'], { group: d, title: 'Demo table header', desc: 'The demo file list\'s "Latest Activity" column header; measured as painted.', sel: 'demo "Latest Activity" header' });
  await S('demo-acme-btn', await domFind(page, /^ACME Studios$/, { sel: 'button', tag: 'dab' }), B4, { group: d, title: 'Demo "ACME Studios" share button', desc: 'The "ACME Studios" button in the demo\'s rendered share popover ("Who can edit"); measured, never pressed.', sel: 'demo share "ACME Studios" button' });
  await S('demo-share-scope', await domFind(page, /Anyone with Link/i, { sel: 'button, [role="button"], [role="combobox"], div, span', tag: 'dss' }), ['default', 'hover', 'focus-visible'], { group: d, title: 'Demo share-scope control', desc: 'The demo\'s "Anyone with Link" share-scope control; measured as painted, never opened (an earlier pointer attempt was intercepted by the mock overlay).', sel: 'demo "Anyone with Link" control' });
  await S('demo-share-popover', await domFind(page, /Who can view|Who can edit/i, { sel: 'div', tag: 'dsp', minW: 200 }), ['default'], { group: d, title: 'Demo share popover', desc: 'The demo mock\'s painted share popover (bg-surface-3, element-border, shadow-popover): "Who can view / Anyone with Link / Who can edit" — a painted mock state, measured as painted.', sel: 'demo share popover' });
  await S('demo-close', await domFind(page, /^Close$/, { sel: 'button, [role="button"]', tag: 'dx' }), B4, { group: d, title: 'Demo "Close" button', desc: 'A "Close" button in the demo mock\'s dialog surface; measured, never pressed.', sel: 'demo "Close" button' });
  await S('section-h2', q('main h2').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading further down the home page ("Talk, Draw, Show", "Share, Organize and Compare", …).', sel: 'main h2' });
  await S('cta-book-demo', q('main a, main button').filter({ hasText: /^Book a Demo$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Book a Demo CTA', desc: 'A "Book a Demo" CTA in the marketing page body; measured, never followed.', sel: 'main "Book a Demo" button' });
  const f = G.footer;
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: f, title: 'Footer', desc: 'The page footer: product/company/legal columns and social links.', sel: 'footer' });
  await S('footer-link', q('footer a').filter({ hasText: /^(Privacy Policy|Privacy|Security|About|MCP)$/ }).filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', desc: 'A footer sitemap link; measured, never followed.', sel: 'footer link' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 8000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('price-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing headline', desc: '"Pricing" — the /pricing masthead.', sel: 'h1' }, { noScroll: true });
  await S('billing-switch', q('[role="switch"]').filter({ visible: true }).last(), [...B4, 'off'], { group: g, title: 'Billing switch', desc: 'The plan billing switch beside the plan cards — labelled "Billed yearly" when on ($15/member/mo) and "Billed quarterly" when off ($35/member/mo); the off state was measured after toggling it — a local UI toggle — then toggled back.', sel: '[role=switch] billing' }, {
    before: { off: async (loc) => { const v = await loc.getAttribute('aria-checked').catch(() => null); if (v !== 'false') { await loc.evaluate((el) => el.click()); await page.waitForTimeout(900); } return 'own toggle (aria-checked true→false)'; } },
    after: { off: async (loc) => { const v = await loc.getAttribute('aria-checked').catch(() => null); if (v === 'false') { await loc.evaluate((el) => el.click()); await page.waitForTimeout(600); } } },
  });
  await S('plan-cta', q('a, button').filter({ hasText: /^Get Started$/ }).filter({ visible: true }).last(), B4, { group: g, title: 'Get Started button', desc: 'A plan card\'s "Get Started" button; measured, never followed (it would start a sign-up flow).', sel: '"Get Started" button' });
  await S('book-call', q('a, button').filter({ hasText: /^Book Call$/ }).filter({ visible: true }).last(), B4, { group: g, title: 'Book Call button', desc: 'A plan card\'s "Book Call" button; measured, never followed (external scheduler).', sel: '"Book Call" button' });
  await S('faq-acc', q('button').filter({ hasText: /storage limit/i }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'FAQ accordion', desc: 'A question row in the /pricing FAQs accordion ("What is the storage limit and what are download windows?"); the opened state was measured after its own toggle — aria-expanded had to stay true.', sel: 'pricing FAQ button' });
  await page.keyboard.press('Escape').catch(() => {});
  save();
}

async function mcp() {
  if (!(await newPage('mcp'))) return;
  await sheetsFor('mcp');
  const g = G.docs;
  await S('docs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs headline', desc: '"Flask MCP Server" — the /mcp documentation masthead.', sel: 'h1' }, { noScroll: true });
  await S('docs-code', q('pre, code').filter({ hasText: /claude|npx|mcp/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Code block', desc: 'A command/code block in the MCP docs (install and tool snippets); measured as painted, never run.', sel: 'docs code block' });
  await S('docs-cursor', q('a').filter({ hasText: /Add to Cursor/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Add to Cursor link', desc: 'The "Add to Cursor" MCP-install link; an external install URL, measured, never followed.', sel: '"Add to Cursor" link' });
  await S('docs-anchor', q('a').filter({ hasText: /^Quick start$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Docs anchor link', desc: 'An in-page anchor link in the MCP docs; measured, never followed.', sel: 'docs anchor link' });
  save();
}

async function about() {
  if (!(await newPage('about'))) return;
  await sheetsFor('about');
  const g = G.docs;
  await S('about-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'About headline', desc: '"About" — the /about masthead.', sel: 'h1' }, { noScroll: true });
  await S('about-link', q('a[href^="mailto:"], a').filter({ hasText: /YouTube|DMs|hello@flask/i }).filter({ visible: true }).first(), B4, { group: g, title: 'About link', desc: 'An external/social link on /about (YouTube show, DMs, hello@flask.do); measured, never followed.', sel: 'about link' });
  save();
}

async function security() {
  if (!(await newPage('security'))) return;
  await sheetsFor('security');
  const g = G.legal;
  await S('sec-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Security headline', desc: '"Security" — the /security masthead ("Security: How Flask Protects Your Data").', sel: 'h1' }, { noScroll: true });
  save();
}

async function vidCollab() {
  if (!(await newPage('video-collaboration'))) return;
  await sheetsFor('video-collaboration');
  const g = G.home;
  await S('seo-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'SEO page headline', desc: 'The /video-collaboration landing-page masthead — one of the SEO/landing surfaces sharing the marketing shell.', sel: 'h1' }, { noScroll: true });
  await S('seo-cta', q('main a, main button').filter({ hasText: /^(Get Started|Book a Demo|Open Flask|Try Flask( Free)?|See pricing)$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'SEO page CTA', desc: 'The landing page\'s CTA; measured, never followed.', sel: 'seo page CTA' });
  save();
}

async function frameIo() {
  if (!(await newPage('frame-io-alternative'))) return;
  const g = G.home;
  await S('seo2-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Alternative page headline', desc: 'The /frame-io-alternative landing-page masthead.', sel: 'h1' }, { noScroll: true });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 8000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.auth;
  await S('login-panel', q('div').filter({ has: q('input[type="email"], input[name="email"]') }).filter({ hasText: /Sign in to Flask|Continue with Google/i }).last(), ['default'], { group: g, title: 'Login panel', desc: 'The sign-in card on /login: "Sign in to Flask" with Continue with Google and Continue with Email plus the e-mail field. Nothing was submitted.', sel: 'login panel' }, { noScroll: true });
  await S('login-google', q('button, a').filter({ hasText: /Continue with Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google SSO button', desc: 'The "Continue with Google" button; measured, never pressed (it would leave for Google SSO).', sel: 'login "Continue with Google"' }, { noScroll: true });
  await S('login-email-btn', q('button').filter({ hasText: /Continue with Email/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue with Email button', desc: 'The "Continue with Email" submit button; its states were measured but the button was never clicked — nothing was submitted.', sel: 'login "Continue with Email"' }, { noScroll: true });
  await S('login-email', q('input[type="email"], input[name="email"], input[type="text"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (login)', desc: 'The e-mail input on the sign-in card (placeholder "han@solo.com"); focused and typed into then cleared — never submitted.', sel: 'login email input' }, { noScroll: true, fillText: 'name@example.com' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/', wait: 8000 }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('body').locator('a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top chrome', desc: 'The phone top chrome at 390 wide: the Flask logo link plus the hamburger — the page mounts no <header> element at this width.', sel: 'mobile logo link' }, { noScroll: true });
  const ham = q('button[aria-label="Open menu"]').filter({ visible: true }).first();
  await S('m-menu-btn', ham, [...B4, 'opened'], { group: g, title: 'Mobile menu button', desc: 'The icon-only "Open menu" hamburger (md:hidden — mobile only) — a local UI toggle; the opened state was measured after activating it.', sel: 'button[aria-label=Open menu]' }, { noScroll: true });
  await S('m-drawer', q('[role="dialog"], [role="menu"], [class*="popover" i]').filter({ hasText: /Pricing|Features|About|MCP|Sign Up/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav overlay', desc: 'The nav layer opened by the "Open menu" button; its links were never followed.', sel: 'mobile nav overlay' }, { open: openMobileMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide.', sel: 'mobile h1' });
  await S('m-hero-cta', q('main a, main button').filter({ hasText: /^(Open Flask|Get Started|Book a Demo|Try Flask)$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile hero CTA', desc: 'The hero CTA at 390 wide; measured, never followed.', sel: 'mobile hero CTA' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every public flask.do page paints the dark `default` theme — the only --ds-* layer the bundle declares; no light variant or theme toggle exists';
out._meta.tool = 'tools/capture/public/measure.mjs';
let { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, mcp, about, security, 'video-collaboration': vidCollab, 'frame-io-alternative': frameIo, login, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
const crashed = [];
async function runPage(k) {
  try { await plan[k](); finishedPages.add(k); }
  catch (e) {
    log('  ! page', k, 'crashed:', String(e.message || e).slice(0, 100));
    crashed.push(k);
  }
}
try {
  for (const k of order) { if (k !== 'mobile') await runPage(k); }
  if (!pages.length || pages.includes('mobile')) await runPage('mobile');
  // One retry per crashed page in a fresh context: a renderer crash (heavy
  // crop, OOM) must not cost the page's remaining components. A dead browser
  // is relaunched first.
  for (const k of crashed.splice(0)) {
    log('retry', k);
    if (!browser.isConnected()) {
      log('relaunching browser');
      ({ browser, context } = await launch());
    }
    await runPage(k);
  }
  // Reduced-motion check on an element that transitions (the header CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a');
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
