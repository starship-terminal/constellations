// Measures enode.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home overview enterprise updates contact login mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// enode.com is a light-only marketing site signed out (`data-mode="light"
// data-ink="alpha"` on <html>); some inner showcase sections paint
// `[data-mode="dark"]` inside the light page. There is no user theme toggle.
// platform.enode.com/login is a separate app that paints a dark sign-in over
// a dimmed product screenshot. The Tailwind utility classes are stable but
// verbose, so specs select by role, aria-label, token-named classes
// (nav-pill, text-masthead, chrome-glass) or text. Nothing is sent, bought
// or signed into: the only presses are local UI toggles — the header's
// "Platform" mega-menu button (an aria-haspopup="dialog" panel) and the
// mobile hamburger; the contact and login fields are typed into and cleared,
// never submitted; Sign in, Talk-to-our-team, Explore-our-platform and every
// form submit are measured, never followed. The dormant Cookiebot script
// shows no banner; any consent overlay is hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, LOGIN_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', overview: '/platform/overview', enterprise: '/enterprise', updates: '/updates', contact: '/contact', login: LOGIN_URL, mobile: '/' };
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
  const cleared = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });  // false: the bot check did not clear (lib.mjs)
  if (!cleared || (await blocked())) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
        // A `before.opened` hook has already opened it (and says how): toggling
        // again would close it and overwrite that provenance.
        if (opts.before?.[st] && via) { /* opened by the hook */ }
        else if (opts.noToggle) via = 'held open by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
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
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|continue with.*|claim this offer|try again)$/i;
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
  shell: 'Site chrome', home: 'Home', overview: 'Platform pages', updates: 'Updates',
  enterprise: 'Enterprise', contact: 'Contact form', login: 'Platform login (dark)',
  mobile: 'Mobile (390 wide)', footer: 'Footer', dark: 'Dark showcase sections',
};

// Opens the header's "Platform" mega-menu: the button is an
// aria-haspopup="dialog" trigger that opens on activation — pointer clicks do
// not flip it in headless Chromium, so it is focused and opened with the
// keyboard (Enter), a local UI toggle, never a link. The panel stays open so
// it and one item can be measured; Escape closes it afterwards.
async function openPlatformMenu() {
  const btn = page.locator('header button[aria-haspopup="dialog"]').filter({ hasText: /^Platform$/ }).first();
  if (!(await btn.count())) return 'no Platform trigger';
  const open = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true';
  if (await open()) return 'the mega-menu was already open';
  for (let i = 0; i < 3; i++) {
    await btn.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(700);
    if (await open()) return 'focused the "Platform" button and pressed Enter to open the mega-menu panel';
  }
  return 'pressed Enter on "Platform"; the panel did not report open';
}

// Opens the mobile nav overlay: the icon-only round button in the header.
// Tries a pointer activation first, then keyboard Enter (the desktop
// mega-menus only respond to the keyboard path in headless Chromium).
async function openMobileMenu() {
  const open = () => page.evaluate(() => {
    const el = [...document.querySelectorAll('body > div, body > nav, [role="dialog"]')].find((x) => {
      const r = x.getBoundingClientRect();
      const cs = getComputedStyle(x);
      return r.height > 300 && /\S/.test(x.textContent || '') && cs.position === 'fixed' && cs.visibility !== 'hidden' && cs.opacity !== '0';
    });
    return !!el;
  }).catch(() => false);
  if (await open()) return 'the nav overlay was already open';
  const b = page.locator('header button').filter({ visible: true }).last();
  if (!(await b.count())) return 'no menu toggle';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    if (await open()) return 'clicked the menu button to open the nav overlay';
    await page.waitForTimeout(500);
    await b.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(700);
    if (await open()) return 'focused the menu button and pressed Enter to open the nav overlay';
  }
  return 'activated the menu button; the overlay did not report open';
}

const FIELD = ['default', 'focused', 'filled'];
const CTABTN = 'a[class*="rounded-full"], button[class*="rounded-full"]';

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The fixed glass top bar: wordmark, Platform/Resources mega-menu buttons, Enterprise/Updates/Company nav pills, Sign in and the "Talk to our team" pill.', sel: 'header' }, { noScroll: true });
  await S('mkt-logo', q('header a[aria-label*="Enode" i], header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Enode mark-and-wordmark in the header, linking home.', sel: 'header a[aria-label*=Enode]' }, { noScroll: true });
  await S('nav-menu-btn', q('header button[aria-haspopup="dialog"]').filter({ hasText: /^Platform$/ }).first(), [...B4, 'opened'], { group: g, title: 'Mega-menu trigger', desc: 'The "Platform" header button — an aria-haspopup="dialog" trigger for the product mega-menu. The opened state was measured after focusing it and pressing Enter.', sel: 'header button[aria-haspopup=dialog] Platform' }, { noScroll: true, before: { opened: async (loc) => { await loc.focus(); await page.keyboard.press('Enter'); await page.waitForTimeout(800); return 'focused the button and pressed Enter to open the mega-menu'; } } });
  await S('nav-panel', q('header div.absolute.top-full, header [class*="top-full"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mega-menu panel', desc: 'The dark glass mega-menu panel opened by its own trigger; its links were never followed.', sel: 'mega-menu panel (top-full absolute)' }, { open: openPlatformMenu, noScroll: true, noReset: true });
  await S('nav-menu-item', q('header div.absolute.top-full a, header [class*="top-full"] a').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Mega-menu item', desc: 'A link inside the opened mega-menu panel; measured, never followed.', sel: 'mega-menu panel a' }, { open: openPlatformMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('nav-link', q('header a.nav-pill').filter({ hasText: /^Enterprise$/ }).first(), B4, { group: g, title: 'Nav link', desc: 'A marketing header nav pill (Enterprise); measured, never followed.', sel: 'header a.nav-pill' }, { noScroll: true });
  await S('nav-signin', q('header a.nav-pill').filter({ hasText: /^Sign in$/ }).first(), B4, { group: g, title: 'Sign in link', desc: 'The "Sign in" nav pill linking to platform.enode.com; measured, never followed.', sel: 'header a.nav-pill Sign in' }, { noScroll: true });
  await S('nav-cta', q('header ' + CTABTN).filter({ hasText: /Talk to our team/i }).first(), B4, { group: g, title: 'Header CTA', desc: 'The dark "Talk to our team" pill in the header; links to /contact, measured never followed.', sel: 'header Talk to our team' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: '"Orchestrating energy for the next grid" — the text-masthead display heading.', sel: 'h1.text-masthead' }, { noScroll: true });
  await S('hero-cta', q(CTABTN).filter({ hasText: /^\s*Talk to our team\s*$/i }).filter({ visible: true }).nth(1), B4, { group: h, title: 'Hero CTA', desc: 'The dark "Talk to our team" pill in the hero; measured never followed.', sel: 'hero Talk to our team' });
  await S('hero-cta2', q(CTABTN).filter({ hasText: /^\s*Explore our platform\s*$/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero secondary CTA', desc: 'The outlined "Explore our platform" pill beside it; measured never followed.', sel: 'hero Explore our platform' });
  const d = G.dark;
  // Scoped to <main>: the header mega-menu panel is itself a
  // [data-mode="dark"] surface, so a page-wide selector hits the menu.
  await S('dark-showcase', q('main [data-mode="dark"]').filter({ visible: true }).first(), ['default'], { group: d, title: 'Dark showcase panel', desc: 'A scoped [data-mode="dark"] section inside the light page — the hero media/showcase panel painting the dark semantic layer.', sel: 'main [data-mode=dark]' });
  await S('demo-card', q('main [data-mode="dark"] div, main [data-mode="dark"] section').filter({ hasText: /kW|MW|PRODUCING|CHARGING|BALANCING|SCHEDULE/i }).filter({ visible: true }).first(), ['default'], { group: d, title: 'Product demo card', desc: 'A product-UI demo tile inside the dark showcase (the live energy diagram/charging numbers); a public demo, not the signed-in product.', sel: 'main [data-mode=dark] demo tile' });
  await S('stat-card', q('div, section').filter({ hasText: /device models supported|Connected households|Controllable load/i }).filter({ visible: true }).last(), ['default'], { group: h, title: 'Stat card', desc: 'A metric card ("960+ Energy device models supported" / "1.6M+ Connected households" / "4,799+ MW").', sel: 'stat card' });
  await S('section-h2', q('h2').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading (text-h2) further down the home page.', sel: 'h2' });
  const f = G.footer;
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: f, title: 'Footer', desc: 'The page footer: sitemap columns, legal links, social icons.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /^Customers$/ }).first(), B4, { group: f, title: 'Footer link', desc: 'A footer sitemap link; measured, never followed.', sel: 'footer a' }, { noScroll: true });
  save();
}

async function overview() {
  if (!(await newPage('overview'))) return;
  await sheetsFor('overview');
  await chrome('overview');
  const g = G.overview;
  await S('ov-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page headline', desc: '"Connect. Coordinate. Shape." — the platform overview masthead.', sel: 'h1' }, { noScroll: true });
  await S('ov-lede', q('p, h2, [class*="lede" i]').filter({ hasText: /energy|platform|device/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Platform card copy', desc: 'The 15px muted feature-card description ("One API for 1,000+ device models…").', sel: 'platform card copy' }, { noScroll: true });
  await S('section-h2-ov', q('h2').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Section heading (platform)', desc: 'A platform page section heading.', sel: 'platform h2' });
  await S('feature-row', q('section, div, li').filter({ hasText: /connectivity|coordination|flexibility|intelligence/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Platform section nav item', desc: 'One item in the sticky product-area nav (Asset connectivity / Home energy coordination / Residential flexibility / Intelligence layer).', sel: 'platform nav li' });
  await S('visual-frame', q('main .visual-frame').filter({ hasText: /platform\.enode\.com|Client|Users|Assets/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Visual frame (product mock)', desc: 'A .visual-frame demo tile holding a platform product mock (the browser-framed "platform.enode.com — Client / Users / Assets" screenshot).', sel: 'main .visual-frame' });
  await S('code-frame', q('main .visual-frame').filter({ hasText: /import |kubectl|\$ /i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Visual frame (code)', desc: 'A .visual-frame demo tile holding a code/terminal mock ("import …", "kubectl logs").', sel: 'main .visual-frame code tile' });
  save();
}

async function enterprise() {
  if (!(await newPage('enterprise'))) return;
  await sheetsFor('enterprise');
  const g = G.enterprise;
  await S('ent-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Enterprise headline', desc: 'The /enterprise masthead.', sel: 'h1' }, { noScroll: true });
  await S('ent-cta', q(CTABTN).filter({ hasText: /talk|team|contact|demo|book/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Enterprise CTA', desc: 'The enterprise contact/demo pill; measured never followed.', sel: 'enterprise CTA' });
  await S('quote-card', q('section, div, ul').filter({ hasText: /Vattenfall|BMW|Tibber|Resideo|Easee/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Partner quote card', desc: 'The enterprise partner quote card ("We’re partnering with Easee…").', sel: 'enterprise quote card' });
  save();
}

async function updates() {
  if (!(await newPage('updates'))) return;
  await sheetsFor('updates');
  const g = G.updates;
  await S('upd-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Updates headline', desc: '"Product news, insights, and stories…" — the /updates masthead.', sel: 'h1' }, { noScroll: true });
  await S('upd-card', q('a').filter({ hasText: /Enode|energy|flexibility|charging|platform/i }).filter({ visible: true }).nth(2), ['default', 'hover'], { group: g, title: 'Article card', desc: 'An article card on the updates index (image, tag, title, date); measured, never followed.', sel: 'updates article card' });
  await S('upd-link', q('a').filter({ hasText: /follow enode/i }).first(), B4, { group: g, title: 'Follow link', desc: 'The "Follow Enode on LinkedIn" social pill; measured, never followed.', sel: 'Follow Enode' }, { noScroll: true });
  save();
}

async function contact() {
  if (!(await newPage('contact'))) return;
  await sheetsFor('contact');
  await chrome('contact');
  const g = G.contact;
  await S('contact-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact headline', desc: 'The /contact masthead over the inquiry form.', sel: 'h1' }, { noScroll: true });
  await S('field-firstname', q('input[name="firstName"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'First name field', desc: 'The First name text input; focused and typed into then cleared — never submitted.', sel: 'input[name=firstName]' }, { noScroll: true, fillText: 'Ada' });
  await S('field-email', q('input[type="email"], input[name="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field', desc: 'The work-email input; focused and typed into then cleared — never submitted.', sel: 'input[type=email]' }, { noScroll: true, fillText: 'name@example.com' });
  await S('field-phone', q('input[type="tel"], input[name="phone"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Phone field', desc: 'The optional phone input; focused and typed into then cleared — never submitted.', sel: 'input[type=tel]' }, { noScroll: true, fillText: '+47 000 00 000' });
  await S('field-inquiry', q('textarea[name="inquiryDetail"], textarea').filter({ visible: true }).first(), FIELD, { group: g, title: 'Message textarea', desc: 'The inquiry-detail textarea; focused and typed into then cleared — never submitted.', sel: 'textarea' }, { noScroll: true, fillText: 'A short question about the API.' });
  await S('radio-inquiry', q('label, [role="radio"], [role="radiogroup"] *').filter({ hasText: /sales|support|partnership|general|other/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Inquiry radio', desc: 'One option of the inquiry-type radio group (sr-only inputs behind styled labels); measured, never toggled.', sel: 'inquiry radio label' });
  await S('send-btn', q('button').filter({ hasText: /send message/i }).first(), B4, { group: g, title: 'Send message button', desc: 'The form\'s dark "Send message" pill; its states were measured but the button was never clicked — nothing was submitted.', sel: 'contact Send message' }, { noScroll: true });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 9000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.login;
  await S('login-panel', q('form, [class*="panel" i], [class*="card" i], main').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login panel', desc: 'The dark sign-in panel over a dimmed product screenshot: "Sign in to Enode Platform".', sel: 'login form' }, { noScroll: true });
  await S('login-field', q('input[name="email_address"], input[type="email"], input[type="text"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (login)', desc: 'The e-mail input on the platform login; focused and typed into then cleared — never submitted.', sel: 'input[name=email_address]' }, { noScroll: true, fillText: 'name@example.com' });
  await S('login-submit', q('button[type="submit"], button.enode-button, button').filter({ hasText: /^\s*Log in\s*$/i }).first(), B4, { group: g, title: 'Log in submit', desc: 'The login submit button; its states were measured but the button was never clicked — nothing was submitted.', sel: 'login Log in' }, { noScroll: true });
  await S('login-sso', q('a, button').filter({ hasText: /saml|sso/i }).filter({ visible: true }).first(), B4, { group: g, title: 'SAML SSO link', desc: 'The "Continue with SAML SSO" action; measured, never followed.', sel: 'login SAML SSO' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header: Enode mark, the round menu button and the "Talk to our team" pill.', sel: 'mobile header' }, { noScroll: true });
  await S('m-cta', q('header ' + CTABTN).filter({ hasText: /Talk/i }).first(), B4, { group: g, title: 'Mobile header CTA', desc: 'The header "Talk to our team" pill at 390 wide; measured never followed.', sel: 'mobile Talk to our team' }, { noScroll: true });
  const ham = q('header button').filter({ visible: true }).last();
  await S('m-menu-btn', ham, [...B4, 'opened'], { group: g, title: 'Mobile menu button', desc: 'The icon-only round button that opens the phone nav overlay — a local UI toggle; the opened state was measured after clicking it.', sel: 'mobile header menu button' }, { noScroll: true, allowLink: true });
  await S('m-drawer', q('body > div, body > nav, [role="dialog"]').filter({ hasText: /Platform|Enterprise|Company/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Mobile nav overlay', desc: 'The nav overlay opened by the menu button; its links were never followed.', sel: 'mobile nav overlay' }, { open: openMobileMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide.', sel: 'mobile h1' });
  await S('m-hero-cta', q(CTABTN).filter({ hasText: /^\s*Talk to our team\s*$/i }).filter({ visible: true }).nth(1), B4, { group: g, title: 'Mobile hero CTA', desc: 'The hero "Talk to our team" pill at 390 wide; measured never followed.', sel: 'mobile hero CTA' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every enode.com page paints data-mode="light" data-ink="alpha" with scoped [data-mode="dark"] showcase sections; platform.enode.com/login paints dark';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, overview, enterprise, updates, contact, login, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the header CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a[class*="rounded-full"]');
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
