// Measures getfernand.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing updates integrations alternative feature login signup
//        help helpdark mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// getfernand.com is a Nuxt marketing site in BEM/SCSS, light-only
// (color-scheme:light, flat --white/--grey*/--black/--blue* palette on :root).
// app.getfernand.com is the Vue SPA — /auth/login and /create are reachable
// signed out and paint light on the same palette plus extra vars.
// help.getfernand.com is the Nuxt docs site on the same palette; its
// a.switch__dark link is the real "Switch to dark mode" toggle that sets
// body.dark-mode (persisted in localStorage), so the helpdark page is the
// genuinely toggled theme. Specs select by role, aria-label, BEM class or
// text. Nothing is sent, bought or signed into: the only presses are local UI
// toggles — the "Install with AI" menu button, the "Watch a 2 minute demo"
// dialog, the Fernand chat-widget launcher, the help search field and its
// popover, the alt-faq disclosures, the playground switches and the
// dark-mode link. "Book a demo" (a Cal.com scheduler link), "Start for free"
// and "Log in" are measured, never activated; the login/signup fields are
// typed into and cleared, never submitted. No consent overlay was observed;
// any that appears is hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, HELP, LOGIN_URL, SIGNUP_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing/', updates: '/updates/', integrations: '/integrations/', alternative: '/alternative/intercom/', feature: '/feature/ai-agents/', login: LOGIN_URL, signup: SIGNUP_URL, help: HELP + '/', helparticle: HELP + '/getting-started', helpdark: HELP + '/getting-started', mobile: '/' };
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
    c.states[state] = { ...s, crop: file, via: opts.via };
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
  let loc = target.filter({ visible: true }).first();
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
  // A broad selector re-resolves against the live DOM on every use, so an
  // overlay that mounts mid-run (the docs search popover) can swap the node a
  // state reads. opts.pin marks the resolved element once and every state
  // below measures that same node.
  if (opts.pin) {
    await loc.evaluate((el) => el.setAttribute('data-m-pin', '1')).catch(() => {});
    loc = page.locator('[data-m-pin="1"]').first();
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
        // A before.opened callback already toggled the control open — a second
        // generic click would close it again before the reading.
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else if (!via) { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
        const exp = await loc.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null);
        if (exp !== null) via = (via || 'opened') + (exp === 'true' ? ' (aria-expanded=true at save)' : ' (aria-expanded=false at save — the open did not hold)');
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
  if (opts.pin) await page.evaluate(() => document.querySelectorAll('[data-m-pin]').forEach((n) => n.removeAttribute('data-m-pin'))).catch(() => {});
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|continue with.*|claim this offer|try again|start for free|book a demo)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// The first element matching `sel` whose trimmed text is at least `min` chars
// (hasText cannot express a trimmed length — /\S{20,}/ means twenty
// *consecutive* non-space characters, which no normal paragraph matches).
const p20 = async (sel, min = 20) => {
  const all = q(sel).filter({ visible: true });
  const n = Math.min(await all.count(), 15);
  for (let i = 0; i < n; i++) {
    const t = ((await all.nth(i).innerText().catch(() => '')) || '').trim();
    if (t.length >= min) return all.nth(i);
  }
  return all.first();
};

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
  shell: 'Site chrome', home: 'Home', pricing: 'Pricing', updates: 'Updates',
  integrations: 'Integrations', alternative: 'Alternative page', feature: 'Feature page',
  login: 'App login', signup: 'App signup', help: 'Help center',
  helpdark: 'Help center (dark)', mobile: 'Mobile (390 wide)', footer: 'Footer',
  widget: 'Fernand widget',
};

// Opens the hero "Install with AI" menu — a real aria-haspopup="menu" button;
// activation opens the menu and flips aria-expanded. A local UI toggle whose
// items are never activated (they copy a setup prompt per agent).
async function openAiMenu() {
  const btn = page.locator('button.ai-setup__toggle').filter({ visible: true }).first();
  if (!(await btn.count())) return 'no Install-with-AI toggle';
  const open = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true';
  if (await open()) return 'the Install-with-AI menu was already open';
  for (let i = 0; i < 3; i++) {
    await toggle(btn);  // through toggle(): its NEVER list and link refusal apply to scripted clicks too
    await page.waitForTimeout(700);
    if (await open()) return 'clicked the "Install with AI" button to open its menu';
    await btn.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(700);
    if (await open()) return 'focused the "Install with AI" button and pressed Enter to open its menu';
  }
  return 'activated the "Install with AI" button; the menu did not report open';
}

// Opens the "Watch a 2 minute demo" dialog — a local UI toggle that mounts
// .demo-modal over a backdrop with a YouTube-nocookie embed; the video pauses
// while measured and Escape closes the dialog.
async function openDemoModal() {
  const btn = page.locator('button.hero-demo__btn').filter({ visible: true }).first();
  if (!(await btn.count())) return 'no demo button';
  const open = async () => !!(await page.locator('.demo-modal__dialog').filter({ visible: true }).count());
  if (await open()) return 'the demo dialog was already open';
  for (let i = 0; i < 3; i++) {
    await toggle(btn);  // through toggle(): its NEVER list and link refusal apply to scripted clicks too
    await page.waitForTimeout(1200);
    if (await open()) { await page.evaluate(() => document.querySelectorAll('.demo-modal video').forEach((v) => v.pause())).catch(() => {}); return 'clicked "Watch a 2 minute demo" to open the video dialog'; }
  }
  return 'clicked the demo button; the dialog did not report open';
}

// Opens the Fernand chat-widget launcher — the product's own embeddable widget
// on its own site. The click reveals the widget panel; no message is typed or
// sent.
async function openLauncher() {
  const el = page.locator('.fernand__launcher').filter({ visible: true }).first();
  if (!(await el.count())) return 'no launcher';
  const open = async () => {
    const bd = page.locator('.fernand__backdrop').filter({ visible: true }).first();
    const b = await bd.boundingBox().catch(() => null);
    if (!b || b.width <= 200) return false;
    // The backdrop keeps its full-size box while closed: it sits at opacity 0
    // with no content. Only a painted, populated panel counts as open.
    return bd.evaluate((el2) => {
      const cs = getComputedStyle(el2);
      if (cs.visibility === 'hidden' || parseFloat(cs.opacity) < 0.05) return false;
      return (el2.innerText || '').trim().length > 0
        || !!el2.querySelector('iframe, [class*="panel"], [class*="widget"], [class*="conversation"], [class*="message"]');
    }).catch(() => false);
  };
  if (await open()) return 'the widget panel was already open';
  for (let i = 0; i < 3; i++) {
    await toggle(el);  // through toggle(): its NEVER list applies
    await page.waitForTimeout(2000);
    if (await open()) return 'clicked the Fernand widget launcher to open its panel';
  }
  return 'clicked the launcher; the widget panel did not report open';
}

// Types into the help search field — a local filter that opens a results
// popover. The text is deleted again; nothing is sent.
async function openHelpSearch() {
  const f = page.locator('#search-field').filter({ visible: true }).first();
  if (!(await f.count())) return 'no search field';
  await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
  await page.keyboard.type('channel', { delay: 20 });
  await page.waitForTimeout(1400);
  const open = await page.evaluate(() => {
    const pop = document.querySelector('.search__popover, [class*="popover"], [class*="results"]');
    return pop && pop.getBoundingClientRect().height > 40;
  }).catch(() => false);
  return open ? 'typed "channel" into the docs search field; the results popover opened' : 'typed "channel" into the docs search field';
}

// The help site's real dark toggle: clicks a.switch__dark to set
// body.dark-mode (it persists via localStorage in this context).
async function helpDarkOn() {
  const cur = await page.evaluate(() => document.body.classList.contains('dark-mode')).catch(() => false);
  if (cur) return 'the docs page already painted dark-mode';
  const sw = page.locator('a.switch__dark').first();
  if (!(await sw.count())) return 'no dark-mode switch';
  await toggle(sw, { allowLink: true });  // the dark-mode switch is an <a>; toggle() still applies NEVER
  await page.waitForTimeout(1200);
  return 'clicked the docs site\'s own "Switch to dark mode" link — the user-facing toggle';
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The fixed top bar: wordmark, About us / Pricing / Log in nav links, the "Book a demo" Cal.com action and the "Start for free" button.', sel: 'header' }, { noScroll: true });
  await S('mkt-logo', q('header a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Fernand mark-and-wordmark in the header, linking home.', sel: 'header a:first' }, { noScroll: true });
  await S('nav-link', q('header nav a, header ul.menu a').filter({ hasText: /^About us$/ }).first(), B4, { group: g, title: 'Nav link', desc: 'A marketing header nav link (About us); measured, never followed.', sel: 'header nav a About us' }, { noScroll: true });
  await S('nav-login', q('header a').filter({ hasText: /^Log in$/ }).first(), B4, { group: g, title: 'Log in link', desc: 'The "Log in" nav link to app.getfernand.com; measured, never followed.', sel: 'header a Log in' }, { noScroll: true });
  await S('nav-demo', q('header li.button__demo a, header a[data-cal-link]').first(), B4, { group: g, title: 'Book a demo action', desc: 'The "Book a demo" header action — a Cal.com scheduler link (data-cal-link, role="button"); measured, never activated.', sel: 'header li.button__demo a' }, { noScroll: true });
  await S('nav-cta', q('header li.button__header a').filter({ hasText: /Start for free/ }).first(), B4, { group: g, title: 'Header CTA', desc: 'The "Start for free" header button linking to the signup; measured, never followed.', sel: 'header li.button__header a Start for free' }, { noScroll: true });
  const h = G.home;
  await S('hero-eyebrow', q('a.hero__eyebrow').first(), ['default', 'hover'], { group: h, title: 'Update eyebrow pill', desc: 'The dated changelog pill above the masthead ("Oct. 27 — Dodo Payments integration"); measured, never followed.', sel: 'a.hero__eyebrow' });
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: '"The free customer support platform for SaaS teams" — the 38px display heading.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('.hero__section p, .hero p').filter({ hasText: /Respond on every channel/i }).first(), ['default'], { group: h, title: 'Hero lede', desc: 'The hero standfirst under the masthead.', sel: 'hero lede' });
  await S('hero-cta', q('a.hero__cta--primary').filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The dark "Start for free" hero button (8px radius); measured, never followed.', sel: 'a.hero__cta--primary' });
  await S('hero-cta2', q('a.hero__cta--demo').filter({ visible: true }).first(), B4, { group: h, title: 'Hero demo link', desc: 'The "Book a demo" secondary action in the hero — a Cal.com link; measured, never activated.', sel: 'a.hero__cta--demo' });
  await S('hero-demo-btn', q('button.hero-demo__btn').filter({ visible: true }).first(), [...B4, 'opened'], { group: h, title: 'Demo button', desc: 'The "Watch a 2 minute demo" play button — a local UI toggle opening the video dialog. The opened state measured the dialog it mounts.', sel: 'button.hero-demo__btn' }, { before: { opened: async () => openDemoModal() } });
  await S('demo-dialog', q('.demo-modal__dialog').filter({ visible: true }).first(), ['default'], { group: h, title: 'Demo dialog', desc: 'The video dialog mounted by the demo button — a YouTube-nocookie embed over .demo-modal__backdrop; opened by its own toggle, closed with Escape.', sel: '.demo-modal__dialog' }, { open: openDemoModal, noScroll: true, noReset: true, cropLoc: q('.demo-modal__dialog') });
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(400);
  await S('ai-setup-toggle', q('button.ai-setup__toggle').filter({ visible: true }).first(), [...B4, 'opened'], { group: h, title: 'Install-with-AI menu button', desc: 'The "Install with AI" button — an aria-haspopup="menu" trigger whose menu copies a setup prompt per agent. The opened state was measured after clicking it.', sel: 'button.ai-setup__toggle' }, { before: { opened: async () => openAiMenu() } });
  await S('ai-setup-item', q('.ai-setup__item').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'AI-setup menu item', desc: 'One item in the Install-with-AI menu (an agent prompt to copy); the menu was opened by its own toggle; the item was never activated.', sel: '.ai-setup__item' }, { open: openAiMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('section-tag', q('.section__tag').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section tag pill', desc: 'The small white eyebrow pill labelling each marketing section.', sel: '.section__tag' });
  await S('channels-card', q('.channels__card').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Channel card', desc: 'A card in the "Consolidate all your support channels" carousel (300px, #f7fafc, 10px radius).', sel: '.channels__card' });
  await S('channels-arrow', q('button.channels__arrow--right').filter({ visible: true }).first(), B4, { group: h, title: 'Carousel arrow', desc: 'The channels carousel\'s "Scroll right" arrow button; measured, never used to page the carousel.', sel: 'button.channels__arrow--right' });
  await S('feat-card', q('.feat3__card, a.feat3__card').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Feature card', desc: 'A feat3 feature card in "Support finally connects with your team and product strategy" — product-mock tiles; measured, never followed.', sel: '.feat3__card' });
  await S('why-btn', await domFind(page, /View account/i, { sel: 'button, a', tag: 'whybtn' }), B4, { group: h, title: 'Product-mock button', desc: 'The "View account" primary button inside the "Build your product" product illustration — a drawn mock control, not a live action.', sel: 'product-mock View account button' });
  await S('why-ghost', await domFind(page, /Upgrade plan/i, { sel: 'button, a', tag: 'whyghost' }), B4, { group: h, title: 'Product-mock ghost button', desc: 'The "Upgrade plan" ghost button inside the same product illustration.', sel: 'product-mock Upgrade plan button' });
  await S('testimonial', q('.testimonial, .testimonial__section blockquote, .testimonial p').filter({ visible: true }).first(), ['default'], { group: h, title: 'Testimonial', desc: 'A customer quote block (22px/1.55 display copy).', sel: '.testimonial' });
  await S('trusted-card', q('.trusted__card').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Trusted-by card', desc: 'A "trusted by" customer card in the dark strip (name + company).', sel: '.trusted__card' });
  await S('int-logo', q('.int-logo').filter({ visible: true }).first(), ['default'], { group: h, title: 'Integration logo tile', desc: 'One logo tile in the "Integrates with your entire stack" grid.', sel: '.int-logo' });
  // The widget playground: an interactive demo of the embeddable chat widget —
  // real controls driving a product mock. Toggles are local UI, never sent.
  await S('wpg-playground', q('[class*="wpg-section"], .wpg, [class*="wpg__"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Widget playground', desc: 'The "Live chat and AI, embedded in your product" interactive widget playground — an in-page demo of the embeddable widget.', sel: '.wpg* playground' });
  await S('wpg-color', q('button.wpg-color').filter({ visible: true }).first(), B4, { group: h, title: 'Widget colour swatch', desc: 'A brand-colour swatch in the widget playground (the selected one carries the double ring); clicking retints the demo widget.', sel: 'button.wpg-color' });
  await S('wpg-tab', q('.wpg-tab').filter({ visible: true }).first(), B4, { group: h, title: 'Widget tab', desc: 'A tab in the playground widget preview (Home / Chat / Articles).', sel: '.wpg-tab' });
  await S('wpg-article', q('.wpg-article').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Widget article row', desc: 'A knowledge-base article row inside the playground widget preview.', sel: '.wpg-article' });
  const w = G.widget;
  await S('launcher', q('.fernand__launcher').filter({ visible: true }).first(), ['default'], { group: w, title: 'Widget launcher', desc: 'The Fernand chat-widget launcher on the marketing site — the product\'s own embeddable widget at rest (48px bubble).', sel: '.fernand__launcher' }, { noScroll: true });
  await S('launcher-panel', q('.fernand__backdrop').filter({ visible: true }).first(), ['default'], { group: w, title: 'Widget panel', desc: 'The chat-widget panel opened by its own launcher click — the product\'s public widget UI; never typed into.', sel: '.fernand__backdrop' }, { open: openLauncher, noScroll: true, noReset: true });
  const f = G.footer;
  await S('footer-cta', q('.footer-cta__section a.button, .footer-cta__section a, .footer-cta__section button').filter({ hasText: /Start|free|demo/i }).first(), B4, { group: f, title: 'Footer CTA', desc: 'The "Start free. Email included." call-to-action button in the closing section; measured, never followed.', sel: '.footer-cta__section CTA' });
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: f, title: 'Footer', desc: 'The page footer: sitemap columns, legal links, status/social links.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /^Pricing$/ }).last(), B4, { group: f, title: 'Footer link', desc: 'A footer sitemap link; measured, never followed.', sel: 'footer a Pricing' }, { noScroll: true });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  const g = G.pricing;
  await S('pricing-eyebrow', q('.pricing__eyebrow').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan eyebrow', desc: 'The blue "FREE" eyebrow over a plan price.', sel: '.pricing__eyebrow' }, { noScroll: true });
  await S('price-free', q('.pricing__col--free').filter({ visible: true }).first(), ['default'], { group: g, title: 'Free plan card', desc: 'The $0 plan card — the blue radial-gradient fill and ringed shadow variant.', sel: '.pricing__col--free' });
  await S('price-paid', q('.pricing__col:not(.pricing__col--free)').filter({ visible: true }).first(), ['default'], { group: g, title: 'Paid plan card', desc: 'The paid plan card ($29 per active human per month).', sel: '.pricing__col' });
  await S('pricing-line', q('.pricing__line').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan feature row', desc: 'One feature line inside a plan card.', sel: '.pricing__line' });
  await S('pricing-cta', q('a.button--large, .pricing__cta a, a.button').filter({ hasText: /Start for free/i }).first(), B4, { group: g, title: 'Pricing CTA', desc: 'The large "Start for free" button on the pricing hero; measured, never followed.', sel: 'pricing Start for free' });
  await S('faq-dt', q('dl.faq dt').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ question', desc: 'A question in the "Questions & answers" list (dt/dd pairs).', sel: 'dl.faq dt' });
  await S('faq-dd', q('dl.faq dd').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ answer', desc: 'An answer in the same FAQ list.', sel: 'dl.faq dd' });
  save();
}

async function updates() {
  if (!(await newPage('updates'))) return;
  await sheetsFor('updates');
  const g = G.updates;
  await S('upd-h1', q('h1, h2').filter({ hasText: /Updates/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Updates headline', desc: 'The /updates changelog masthead.', sel: 'updates h1' }, { noScroll: true });
  await S('upd-article', q('.updates li article, .updates article').filter({ visible: true }).first(), ['default'], { group: g, title: 'Update entry', desc: 'One changelog entry on /updates (title column + body).', sel: '.updates li article' });
  await S('upd-title', q('.updates__title').filter({ visible: true }).first(), ['default'], { group: g, title: 'Update title', desc: 'The sticky title cell of a changelog entry.', sel: '.updates__title' });
  save();
}

async function integrations() {
  if (!(await newPage('integrations'))) return;
  await sheetsFor('integrations');
  const g = G.integrations;
  await S('int-essential', q('a.feat3__card.essential-card, .feat3__card.essential-card').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Essential integration card', desc: 'An "Essentials" integration card with a product mock (the Stripe plan card); measured, never followed.', sel: '.feat3__card.essential-card' });
  await S('int-card', q('a.card').filter({ hasText: /Stripe|Paddle|Polar|Dodo/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Integration card', desc: 'A grid card linking to one integration page (Stripe / Paddle / Polar / Dodo); measured, never followed.', sel: 'a.card integration' });
  await S('int-eyebrow', q('[class*="eyebrow"], .u--subtle, h3, h4').filter({ hasText: /ESSENTIALS|PAYMENTS/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Group eyebrow', desc: 'An all-caps group label (ESSENTIALS / PAYMENTS / PRODUCT AND ENGINEERING).', sel: 'integrations eyebrow' });
  save();
}

async function alternative() {
  if (!(await newPage('alternative'))) return;
  await sheetsFor('alternative');
  const g = G.alternative;
  await S('alt-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Alternative headline', desc: 'The comparison page masthead ("The fast, calm Intercom alternative…").', sel: 'h1' }, { noScroll: true });
  await S('alt-table', q('table.alt-table').filter({ visible: true }).first(), ['default'], { group: g, title: 'Comparison table', desc: 'The "Intercom vs Fernand comparison" table — a real data table on the public site.', sel: 'table.alt-table' });
  await S('alt-faq', q('.alt-faq__item').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ accordion item', desc: 'One item in the comparison FAQ accordion.', sel: '.alt-faq__item' });
  await S('alt-faq-summary', q('button.alt-faq__summary').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'FAQ disclosure', desc: 'A disclosure button in the comparison FAQ; the opened state was measured after clicking it (a local UI toggle).', sel: 'button.alt-faq__summary' }, { before: { opened: async (loc) => { await loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.click())); await page.waitForTimeout(700); return 'clicked the FAQ summary to expand its answer'; } } });
  save();
}

async function feature() {
  if (!(await newPage('feature'))) return;
  await sheetsFor('feature');
  const g = G.feature;
  await S('ag-switch', q('button.ag-switch').filter({ visible: true }).first(), B4, { group: g, title: 'Permission switch', desc: 'An on/off switch in the "Every key only does what you allow" permissions demo — a local UI toggle flipping the demo.', sel: 'button.ag-switch' });
  await S('ag-replay', q('button.ag-replay').filter({ visible: true }).first(), B4, { group: g, title: 'Replay button', desc: 'The "↻ Replay" control on the agent animation demo.', sel: 'button.ag-replay' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 9000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.login;
  await S('login-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login headline', desc: '"Welcome back" — the 25px sign-in heading.', sel: 'login h1' }, { noScroll: true });
  await S('login-card', q('form, [class*="sidebar"], [class*="card"], [class*="panel"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login card', desc: 'The sign-in card on app.getfernand.com/auth/login — e-mail and password fields, the primary submit and the account links.', sel: 'login form/card' }, { noScroll: true });
  await S('login-field', q('input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (login)', desc: 'The "Your work email" input; focused and typed into then cleared — never submitted.', sel: 'input[type=email]' }, { noScroll: true, fillText: 'name@example.com' });
  await S('login-pass', q('input[type="password"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Password field (login)', desc: 'The "Your password" input; focused and typed into then cleared — never submitted.', sel: 'input[type=password]' }, { noScroll: true, fillText: 'sample-pass-123' });
  await S('login-submit', q('input[type="submit"], input.button--primary').filter({ visible: true }).first(), B4, { group: g, title: 'Login submit', desc: 'The primary "Login" submit; its states were measured but the button was never clicked — nothing was submitted.', sel: 'login input[type=submit]' }, { noScroll: true });
  await S('login-link', q('a').filter({ hasText: /Lost password|Create an account/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Login link', desc: 'The "Create an account" / "Lost password?" link beside the form; measured, never followed.', sel: 'login account link' }, { noScroll: true });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 9000 }))) return;
  await sheetsFor('signup');
  await chrome('signup');
  const g = G.signup;
  await S('create-panel', q('.wrapper__create-left, [class*="create-left"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup intro panel', desc: 'The left intro panel of /create — "Bonjour, I\'m Fernand. The better, faster and calmer helpdesk experience."', sel: '.wrapper__create-left' }, { noScroll: true });
  await S('create-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup headline', desc: 'The signup greeting heading.', sel: 'create h1' }, { noScroll: true });
  await S('create-field', q('input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (signup)', desc: 'The "Your work email" signup input; focused and typed into then cleared — never submitted.', sel: 'create input[type=email]' }, { noScroll: true, fillText: 'name@example.com' });
  await S('create-field-name', q('input[type="text"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Product name field', desc: 'The "Your product\'s name" input; focused and typed into then cleared — never submitted.', sel: 'create input[type=text]' }, { noScroll: true, fillText: 'Example Inc' });
  await S('create-checkbox', q('input[type="checkbox"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Terms checkbox', desc: 'The terms-of-service checkbox (a styled .fake__checkbox over the native input); measured, never toggled.', sel: 'create input[type=checkbox]' }, { noScroll: true });
  await S('create-tos', q('label, span, a').filter({ hasText: /terms of service/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Terms text', desc: 'The "Accept our terms of service" line; its link was never followed.', sel: 'create ToS line' }, { noScroll: true });
  await S('create-continue', q('button.button--primary').filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'The primary "Continue" submit; its states were measured but the button was never clicked — nothing was submitted.', sel: 'create button.button--primary' }, { noScroll: true });
  save();
}

async function help() {
  if (!(await newPage('help'))) return;
  await sheetsFor('help');
  await chrome('help');
  const g = G.help;
  await S('help-header', q('header.header, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs header', desc: 'The docs site header: logo, the collection nav, the search and menu toggles and the dark-mode switch.', sel: 'help header' }, { noScroll: true });
  await S('help-logo', q('header a.logo, header a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs logo', desc: 'The Fernand Docs wordmark.', sel: 'help header logo' }, { noScroll: true });
  await S('help-nav-item', q('header nav a, nav a').filter({ hasText: /^Getting started$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Docs nav item', desc: 'A collection link in the docs nav; measured, never followed.', sel: 'help nav a' }, { noScroll: true });
  await S('help-search', q('#search-field').filter({ visible: true }).first(), FIELD, { group: g, title: 'Search field', desc: 'The docs search field ("Start typing to search an article, collection…", ⌘K hint); focused and typed into — a local filter, nothing sent.', sel: '#search-field' }, { noScroll: true, fillText: 'channel' });
  await S('help-search-pop', q('.search__popover, [class*="popover"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Search popover', desc: 'The results popover the docs search opens while typing.', sel: '.search__popover' }, { open: openHelpSearch, noScroll: true, noReset: true });
  await page.evaluate(() => { const c = document.querySelector('#search-close'); if (c) c.click(); const f = document.querySelector('#search-field'); if (f) { f.value = ''; } }).catch(() => {});
  await S('help-dark-toggle', q('a.switch__dark').filter({ visible: true }).first(), B4, { group: g, title: 'Dark-mode switch', desc: 'The docs site\'s own "Switch to dark mode" link — the real user-facing toggle that sets body.dark-mode; its states were measured but it was only toggled on the helpdark pass.', sel: 'a.switch__dark' }, { noScroll: true });
  await S('help-card', q('a.card').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Collection card', desc: 'A collection card on the docs home (emoji glyph, title, article count, description); measured, never followed.', sel: 'help a.card' });
  await S('help-article-item', q('.wrapper__articles a, .wrapper__articles li a').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Article row', desc: 'An article row inside a collection (title + standfirst); measured, never followed.', sel: 'help .wrapper__articles a' });
  await S('help-goto', q('a').filter({ hasText: /Go to Fernand/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Go-to-Fernand link', desc: 'The "→ Go to Fernand" link in the sticky search bar; measured, never followed.', sel: 'help Go to Fernand' }, { noScroll: true });
  save();
}

async function helparticle() {
  if (!(await newPage('helparticle'))) return;
  const g = G.help;
  await S('help-h1', q('main h1, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article headline', desc: 'The article title on a docs page ("Getting started").', sel: 'help h1' }, { noScroll: true });
  await S('help-prose', await p20('main p, .article p, article p'), ['default'], { group: g, title: 'Article body', desc: 'A body paragraph in a docs article.', sel: 'help article p' });
  await S('help-content-link', q('main a, article a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Article link', desc: 'An in-content link inside a docs article; measured, never followed.', sel: 'help article a' }, { pin: true });
  save();
}

async function helpdark() {
  if (!(await newPage('helpdark'))) return;
  const g = G.helpdark;
  const via = await helpDarkOn();
  log('  dark toggle:', via);
  const dark = await page.evaluate(() => document.body.classList.contains('dark-mode')).catch(() => false);
  if (!dark) { log('  ! body.dark-mode never painted; skipping dark measurements'); return; }
  await S('hd-page', q('main, .wrapper__page').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs page (dark)', desc: 'The docs article surface under body.dark-mode — reached through the site\'s own "Switch to dark mode" link, not a reconstruction.', sel: 'help main (dark)' }, { noScroll: true });
  await S('hd-h1', q('main h1, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article headline (dark)', desc: 'The article title under dark-mode.', sel: 'help h1 (dark)' }, { noScroll: true });
  await S('hd-nav-item', q('header nav a, nav a').filter({ hasText: /Getting started/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs nav item (dark)', desc: 'A collection link in the docs nav under dark-mode.', sel: 'help nav a (dark)' }, { noScroll: true });
  await S('hd-search', q('#search-field').filter({ visible: true }).first(), ['default'], { group: g, title: 'Search field (dark)', desc: 'The docs search field under dark-mode.', sel: '#search-field (dark)' }, { noScroll: true });
  await S('hd-card', q('a.card').filter({ visible: true }).first(), ['default'], { group: g, title: 'Collection card (dark)', desc: 'A collection card under dark-mode.', sel: 'help a.card (dark)' });
  await S('hd-prose', await p20('main p, .article p, article p'), ['default'], { group: g, title: 'Article body (dark)', desc: 'A body paragraph in a docs article under dark-mode.', sel: 'help article p (dark)' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header: Fernand mark, nav links and "Start for free" (Book a demo hides at this width).', sel: 'mobile header' }, { noScroll: true });
  await S('m-cta', q('header a').filter({ hasText: /Start for free/ }).first(), B4, { group: g, title: 'Mobile header CTA', desc: 'The header "Start for free" button at 390 wide; measured never followed.', sel: 'mobile Start for free' }, { noScroll: true });
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide — the 38px display heading drops to 26px.', sel: 'mobile h1' });
  await S('m-hero-cta', q('a.hero__cta--primary').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile hero CTA', desc: 'The hero "Start for free" button at 390 wide; measured never followed.', sel: 'mobile hero CTA' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); getfernand.com + app.getfernand.com paint light only; help.getfernand.com paints light, and dark via its own switch__dark toggle (the helpdark group)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, updates, integrations, alternative, feature, login, signup, help, helparticle, helpdark, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the header CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header li.button__header a');
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
