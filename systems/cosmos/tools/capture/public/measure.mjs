// Measures cosmos.so's public components in every state reachable without
// signing in, checking out or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home explore sequence login mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// cosmos.so is a Next.js app on Tailwind utilities with a real
// --light-*/--dark-* semantic var layer; the public surface locks
// data-theme="light". Specs select by role, aria-label, text or structure
// (utility classes are too dense to name). Save/follow/search are product
// actions and never used; the login form's fields are filled then cleared —
// the Next button is measured disabled and again enabled — never pressed.
// The only presses are local UI toggles: the mobile nav button.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };
const URLS = { home: '/', explore: '/explore', sequence: '/sequence', login: '/login' };
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
  await open(page, url || (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]), { wait, promo });
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|order( free)?( sample)?|add to cart|go to the platform|get a demo|get demo|contact sales|send message)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
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

// Marks the opened mobile navigation overlay: the container holding the
// Home/Explore/Sequence/Careers rows and the Sign up action.
async function markMobileMenu() {
  await page.evaluate(() => {
    const cand = [...document.querySelectorAll('div,nav,aside,section,[role="dialog"]')].filter((el) => {
      const r = el.getBoundingClientRect();
      const t = el.innerText || '';
      return r.height > innerHeight * 0.5 && r.width > innerWidth * 0.6
        && /Sign up/i.test(t) && /Explore|Sequence/i.test(t) && t.length < 4000;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'mmenu');
  });
}

// Marks the auth panel on /login: the smallest visible ancestor of the first
// field that also holds the heading and the Next action.
async function markAuthCard() {
  await page.evaluate(() => {
    const fld = [...document.querySelectorAll('input')].find((e) => e.getBoundingClientRect().width > 100);
    if (!fld) return;
    let n = fld;
    for (let i = 0; i < 12 && n.parentElement; i++) {
      n = n.parentElement;
      const t = n.innerText || '';
      const r = n.getBoundingClientRect();
      if (/Welcome back|credentials|Next/i.test(t) && /password/i.test(t) && t.length < 1500 && r.height > 250 && r.width < 800) {
        n.setAttribute('data-m-mark', 'authcard');
        return;
      }
    }
    fld.closest('form, main, section, div').setAttribute('data-m-mark', 'authcard');
  });
}

// Marks a "Selected by Cosmos" carousel card on /explore: the smallest link
// holding a title and an "@handle · N elements" meta line.
async function markSelCard() {
  await page.evaluate(() => {
    const a = [...document.querySelectorAll('main a')].find((e) => {
      const t = e.innerText || '';
      const r = e.getBoundingClientRect();
      return /elements|Edition/i.test(t) && r.width > 200 && r.height > 150 && r.top > 0;
    });
    if (a) a.setAttribute('data-m-mark', 'selcard');
  });
}

// Fills both login fields and leaves them (a state hook): the submit's
// enabled reading is real product behaviour. Cleared by the after hook.
async function fillAuth() {
  const user = q('input').filter({ visible: true }).first();
  const pass = q('input[type="password"]').filter({ visible: true }).first();
  if (!(await user.count())) return 'no field';
  await user.click({ timeout: 4000 });
  await page.keyboard.type('name@example.com', { delay: 10 });
  if (await pass.count()) { await pass.click({ timeout: 4000 }); await page.keyboard.type('sample-pass', { delay: 10 }); }
  await page.waitForTimeout(600);
  return 'both fields typed (name@example.com, sample-pass), never submitted';
}
async function clearAuth() {
  for (const sel of ['input[type="password"]', 'input']) {
    const f = q(sel).filter({ visible: true }).first();
    if (await f.count()) { await f.click({ timeout: 3000 }).catch(() => {}); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); }
  }
  await page.waitForTimeout(400);
}

const G = {
  shell: 'Shell and navigation', home: 'Home', explore: 'Explore and search',
  sequence: 'Sequence', login: 'Login', footer: 'Footer',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The sticky app header (hidden until painted): the flower mark, Explore / Sequence / Shop links, the search pill, Log in and Sign up.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Cosmos flower mark anchor.', sel: 'header a[href="/"]' }, { noScroll: true });
  await S('nav-link', q('header a').filter({ hasText: /^\s*(Explore|Sequence|Shop)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A header nav link (Explore / Sequence / Shop); measured, never followed.', sel: 'header a Explore' }, { noScroll: true });
  await S('signup-cta', q('header a, header button').filter({ hasText: /^\s*Sign up\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up pill', desc: 'The black "Sign up" header pill; measured, never followed.', sel: 'header Sign up' }, { noScroll: true });
  await S('login-link', q('header a, header button').filter({ hasText: /^\s*Log in\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Log-in pill', desc: 'The light "Log in" header pill; measured, never followed.', sel: 'header Log in' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The 72px display ("Find your next go-to outfit" — the object word rotates through saved categories).', sel: 'h1.text-display' });
  await S('hero-search', q('main div.rounded-full, main [class*="rounded-full"][class*="border"]').filter({ visible: true }).first(), B4, { group: h, title: 'Hero search', desc: 'The hero search pill ("Search for outfits"); measured, never used — it would open the search surface.', sel: 'hero search pill' });
  await S('join-cta', q('a, button').filter({ hasText: /Join Cosmos for free/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Join CTA', desc: 'The black "Join Cosmos for free" pill; measured, never followed.', sel: 'Join Cosmos for free' });
  await S('qr-card', q('a, div, aside').filter({ hasText: /Get the app/ }).filter({ visible: true }).last(), ['default'], { group: h, title: 'Get-the-app card', desc: 'The "Get the app" QR card fixed bottom-right.', sel: 'Get the app card' });
}

async function explore() {
  if (!(await newPage('explore'))) return;
  await sheetsFor('explore');
  await chrome('explore');
  await lazyLoad();
  const g = G.explore;
  await S('search-pill', q('header div.rounded-full, header [class*="rounded-full"][class*="border"]').filter({ visible: true }).first(), B4, { group: g, title: 'Search field', desc: 'The header search field (a suggested query in the placeholder); focused, never searched.', sel: 'header search input' }, { noScroll: true });
  await S('cat-tab', q('main a, nav a, main button, nav button, [role="tab"]').filter({ hasText: /^\s*(Fashion|Interiors|Graphic Design|Art|Branding)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Category tab', desc: 'A category chip in the explore rail (Fashion/Interiors/...); measured, never followed.', sel: 'category chip' }, { noScroll: true });
  await S('section-h2', q('h2, h3').filter({ hasText: /Explore elements|Selected by Cosmos/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Section heading', desc: 'A section heading on /explore ("Selected by Cosmos" / "Explore elements").', sel: 'explore section heading' });
  await markSelCard();
  await S('selected-card', q('[data-m-mark="selcard"]').filter({ visible: true }).first(), B4, { group: g, title: 'Selected card', desc: 'A "Selected by Cosmos" carousel card (artwork, title, @handle and element count); measured, never followed.', sel: 'selected carousel card' });
  await S('element-tile', q('main .rounded-element, main [class*="rounded-element"]').filter({ visible: true }).first(), B4, { group: g, title: 'Element tile', desc: 'A masonry tile in the Explore elements grid (rounded-element corners over the image); measured, never followed — opening it goes to the element.', sel: '.rounded-element tile' });
}

async function sequence() {
  if (!(await newPage('sequence'))) return;
  await chrome('sequence');
  const g = G.sequence;
  await S('seq-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sequence title', desc: 'The "Sequence" page heading.', sel: 'h1' }, { noScroll: true });
  await S('seq-card', q('main a').filter({ visible: true }).first(), B4, { group: g, title: 'Sequence card', desc: 'An article card in the Sequence editorial list; measured, never followed.', sel: 'main a' });
}

async function login() {
  if (!(await newPage('login'))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.login;
  await markAuthCard();
  await S('auth-card', q('[data-m-mark="authcard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Auth panel', desc: 'The "Welcome back" sign-in panel (username/email + password fields, the disabled-then-enabled Next, Forgot password, the sign up link) over the image collage; captured, never used.', sel: 'auth panel' }, { noScroll: true });
  await S('auth-input', q('input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Username field', desc: 'The "Username or email" input; focused and given sample text that was deleted again — nothing sent.', sel: 'Username or email' }, { noScroll: true });
  await S('auth-pass', q('input[type="password"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Password field', desc: 'The Password input (with the reveal-eye button); focused and given sample text that was deleted again — nothing sent.', sel: 'input[type=password]' }, { noScroll: true });
  await S('auth-next', q('button').filter({ hasText: /^\s*Next\s*$/ }).filter({ visible: true }).first(), ['default', 'enabled', 'focus-visible', 'pressed'], { group: g, title: 'Next button', desc: 'The "Next" submit — greyed and disabled until both fields hold text (the enabled state is measured with the fields filled); never pressed.', sel: 'Next button' }, { noScroll: true, before: { enabled: fillAuth }, after: { enabled: clearAuth } });
  await S('forgot-link', q('a, button').filter({ hasText: /Forgot password/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Forgot-password link', desc: 'The "Forgot password?" link; measured, never followed.', sel: 'Forgot password' }, { noScroll: true });
  await S('auth-signup', q('a, button').filter({ hasText: /^\s*sign up\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up link', desc: 'The "sign up" link on the auth panel; measured, never followed.', sel: 'sign up link' }, { noScroll: true });
}

async function footer() {
  if (!(await newPage('explore'))) return;
  await chrome('explore-footer');
  const g = G.footer;
  const ft = q('footer').filter({ visible: true }).last();
  await ft.scrollIntoViewIfNeeded().catch(() => {});
  await S('footer', ft, ['default'], { group: g, title: 'Footer', desc: 'The footer (force-light): Discover links, the app badges, Follow-us socials and the Info legal row.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer link (Download app / Careers / Terms); measured, never followed.', sel: 'footer a' }, { noScroll: true });
  await S('social-icon', q('footer a[href*="instagram"], footer a[href*="tiktok"], footer a[href*="x.com"], footer a[href*="twitter"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A social link in the footer (Instagram/TikTok/X).', sel: 'footer social a' }, { noScroll: true });
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('header button').filter({ visible: true }).first();
  await S('m-menu-button', menu, B4, { group: g, title: 'Menu button', desc: 'The header menu button (xl:hidden) that opens the full overlay.', sel: 'header menu button' }, { noScroll: true });
  if (await menu.count()) {
    try {
      await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click()));
      await page.waitForTimeout(1600);
      await markMobileMenu();
    } catch (e) { log('  ! menu open failed', String(e.message).slice(0, 80)); }
  }
  await S('m-menu-open', q('[data-m-mark="mmenu"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The opened nav overlay: the Home / Explore / Sequence / Careers rows over the page with the Sign up pill at the foot.', sel: 'opened mobile menu' }, { noScroll: true });
  await S('m-nav-item', q('[data-m-mark="mmenu"] a, [data-m-mark="mmenu"] button').filter({ hasText: /^\s*(Home|Explore|Sequence|Careers)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile menu row', desc: 'A row inside the opened nav overlay.', sel: 'mobile menu row' }, { noScroll: true });
  await S('m-signup', q('[data-m-mark="mmenu"] a, [data-m-mark="mmenu"] button').filter({ hasText: /Sign up/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile sign-up', desc: 'The Sign up pill inside the mobile menu; measured, never followed.', sel: 'mobile menu Sign up' }, { noScroll: true });
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); cosmos.so locks data-theme=light on the public surface (a --dark-* semantic layer exists in the CSS but nothing here paints it)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, explore, sequence, login, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually transitions (a nav
  // dropdown trigger), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a');
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
