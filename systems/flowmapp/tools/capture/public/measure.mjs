// Measures flowmapp.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing feature contact login signup restore sharesitemap
//        shareuserflow mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// www.flowmapp.com is a Webflow marketing site (BEM-ish classes: .nav__link,
// .nav__btn, .p-tabs__btn, .faq__q-wrap), light-only — no theme toggle, no
// dark media query. app.flowmapp.com is a React/Ant Design SPA under CSS
// modules (hashed names like button--PGwt3, input--LVdIP, ant-dropdown-
// trigger): /signin, /signup and /restore paint the auth shell, and
// /share/projects/215285 publishes a real read-only demo project with
// sitemap and userflow viewers behind a "Log In or Sign Up" nudge.
//
// Nothing is sent, bought or signed into: the only activations are local UI
// toggles — the nav Features flyout (hover), the pricing billing tabs, a
// pricing FAQ disclosure, the mobile burger, the share-viewer "Demo Project"
// dropdown and its Structure/Estimation tabs. The auth fields are typed into
// and cleared, never submitted; "Log In", "Sign Up", "Try for free" and
// "Start planning" are measured, never activated. No consent overlay was
// observed; any that appears is hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, LOGIN_URL, SIGNUP_URL, RESTORE_URL, SHARE, SHARE_SITEMAP, SHARE_USERFLOW, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', pricing: '/pricing', feature: '/features/sitemap', contact: '/contact-us',
  login: LOGIN_URL, signup: SIGNUP_URL, restore: RESTORE_URL,
  sharesitemap: SHARE_SITEMAP, shareuserflow: SHARE_USERFLOW, mobile: '/',
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
const NEVER = /^(send|send message|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|continue with.*|claim this offer|try again|start for free|try for free|book a demo|start planning|restore|send reset|reset password)$/i;
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
  shell: 'Site chrome', home: 'Home', pricing: 'Pricing', feature: 'Feature page',
  contact: 'Contact', login: 'App sign-in', signup: 'App sign-up', restore: 'App restore',
  share: 'Shared demo project', mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens the nav "Features" flyout — a hover-driven .nav__pop-wrap dropdown on
// the Webflow navbar. A local UI toggle; its links are measured, never
// followed.
async function openFeatures() {
  const btn = q('.nav__link.pop__is-br-8, .nav__link').filter({ hasText: /features/i }).filter({ visible: true }).first();
  if (!(await btn.count())) return 'no Features nav trigger';
  const pop = q('.nav__pop-wrap').filter({ visible: true }).first();
  const open = async () => (await pop.count()) && (await pop.boundingBox().catch(() => null))?.height > 40;
  if (await open()) return 'the Features flyout was already open';
  for (let i = 0; i < 3; i++) {
    await btn.hover({ timeout: 4000 }).catch(() => btn.evaluate((el) => el.dispatchEvent(new MouseEvent('mouseover', { bubbles: true }))));
    await page.waitForTimeout(900);
    if (await open()) return 'hovered the "Features" nav trigger to open its flyout';
  }
  return 'hovered the "Features" nav trigger; the flyout did not report open';
}

// Opens the share viewer's "Demo Project" dropdown — an ant-dropdown-trigger
// button whose menu lists the published project's boards. A local UI toggle;
// its items are never activated.
async function openProjectMenu() {
  const btn = q('button.ant-dropdown-trigger').filter({ hasText: /demo project|project/i }).filter({ visible: true }).first();
  if (!(await btn.count())) return 'no Demo Project dropdown';
  const open = async () => !!(await q('.ant-dropdown:not(.ant-dropdown-hidden), [class*="dropdown"][class*="open"]').filter({ visible: true }).count());
  if (await open()) return 'the project dropdown was already open';
  for (let i = 0; i < 3; i++) {
    await btn.click({ timeout: 4000 }).catch(() => btn.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    if (await open()) return 'clicked the "Demo Project" button to open its dropdown';
  }
  return 'clicked the "Demo Project" button; the dropdown did not report open';
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('header, .navbar, .nav.w-nav, [class*="navbar"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The marketing top bar: wordmark, "Try Demo Project", Features and Use cases dropdowns, Pricing, Help, Blog, "Log in" and the "Try for free" pill.', sel: 'header / .navbar' }, { noScroll: true });
  await S('mkt-logo', q('header a, .navbar a, .nav a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The FlowMapp wordmark in the header, linking home.', sel: 'header first a' }, { noScroll: true });
  await S('nav-link', q('.nav__link, header a').filter({ hasText: /^Pricing$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A marketing header nav link (Pricing); measured, never followed.', sel: '.nav__link Pricing' }, { noScroll: true });
  await S('nav-features', q('.nav__link').filter({ hasText: /features/i }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Features nav trigger', desc: 'The "Features" nav item that opens the .nav__pop-wrap flyout on hover (Sitemap, User flow, Wireframes, Content, Estimation & invoice…).', sel: 'nav Features trigger' }, { noScroll: true, before: { opened: openFeatures } });
  await S('nav-pop-item', q('.nav__pop-link').filter({ visible: true }).first(), ['default'], { group: g, title: 'Features flyout item', desc: 'A row inside the opened Features flyout (icon, name, one-line description); measured while the flyout was held open by hover.', sel: '.nav__pop-link' }, { noScroll: true, open: openFeatures, noReset: true });
  await S('nav-demo', q('a, button').filter({ hasText: /try demo/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Try Demo Project link', desc: 'The header link to the published read-only demo project on app.flowmapp.com; measured, never followed.', sel: 'header Try Demo Project' }, { noScroll: true });
  await S('nav-login', q('header a, .nav__btn').filter({ hasText: /^Log ?in$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in link', desc: 'The "Log in" nav action to app.flowmapp.com/signin; measured, never followed.', sel: 'header Log in' }, { noScroll: true });
  await S('nav-cta', q('header a, .nav__btn').filter({ hasText: /try for free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Try for free pill', desc: 'The black "Try for free" header pill to app.flowmapp.com/signup; measured, never followed.', sel: 'header Try for free' }, { noScroll: true });
  await S('hero-eyebrow', q('.text-12-main, [class*="eyebrow"], h1 ~ *').filter({ hasText: /400,?000|users/i }).filter({ visible: true }).first(), ['default'], { group: G.home, title: 'Hero eyebrow', desc: 'The "Over 400,000 users" trust line above the hero heading.', sel: 'hero trust line' }, { noScroll: true });
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: G.home, title: 'Hero headline', desc: '"Visual platform for planning UX and pitching web design" — the display heading.', sel: 'home h1' }, { noScroll: true });
  await S('hero-cta', q('a.btn, a').filter({ hasText: /start planning/i }).filter({ visible: true }).first(), B4, { group: G.home, title: 'Hero CTA', desc: 'The hero "Start planning" button (blue pill with the squiggle arrow); measured, never followed.', sel: 'hero Start planning' }, { noScroll: true });
  await S('hero-avatars', q('.ava-container, [class*="avatar"]').filter({ visible: true }).first(), ['default'], { group: G.home, title: 'Avatar cluster', desc: 'The stacked-user avatar cluster beside the trust line.', sel: '.ava-container' }, { noScroll: true });
  await S('trusted-mark', q('.header__logo, [class*="logo"]').filter({ visible: true }).nth(1), ['default'], { group: G.home, title: 'Client mark', desc: 'One of the "Win more clients" brand marks under the hero CTA (Webflow, Framer, WordPress…).', sel: 'home client logos' }, { noScroll: true });
  await S('home-h2', q('h2').filter({ visible: true }).first(), ['default'], { group: G.home, title: 'Section heading', desc: 'A section heading on the marketing home.', sel: 'home h2' });
  await S('home-prose', await p20('main p, section p, p', 40), ['default'], { group: G.home, title: 'Body paragraph', desc: 'A body paragraph on the marketing home.', sel: 'home p' });
  await S('home-card', await p20('[class*="card"], [class*="tile"]'), ['default', 'hover'], { group: G.home, title: 'Home card', desc: 'A feature/benefit card on the marketing home.', sel: 'home [class*=card]' }, { pin: true });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  const g = G.pricing;
  await S('ptab-monthly', q('.p-tabs__btn').filter({ hasText: /monthly/i }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Billing tab (monthly)', desc: 'The "Billed monthly" toggle in the pricing switcher; opened is the selected state after clicking (a local UI toggle).', sel: '.p-tabs__btn monthly' }, { noScroll: true, before: { opened: async (loc) => { await loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.click())); await page.waitForTimeout(700); return 'clicked "Billed monthly" to select monthly prices'; } } });
  await S('ptab-annual', q('.p-tabs__btn').filter({ hasText: /annual/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Billing tab (annual)', desc: 'The "Billed annually" toggle carrying the "45% off" badge.', sel: '.p-tabs__btn annual' }, { noScroll: true });
  await S('plan-card', q('.p-tabs__card').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (Free: $0 forever, features list, CTA).', sel: '.p-tabs__card:first' });
  await S('plan-card-paid', q('.p-tabs__card').filter({ hasText: /\$35|\$19/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Paid plan card', desc: 'A paid pricing card ($35/mo monthly, $19.25/mo annual); hover is a pointer hover, never clicked through.', sel: '.p-tabs__card paid' }, { pin: true });
  await S('plan-price', q('.p-tabs__card [class*="price"], .p-tabs__price-wrap').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'The price block inside a plan card.', sel: '.p-tabs__card price' });
  await S('plan-cta', q('.p-tabs__card a, .p-tabs__card button').filter({ hasText: /sign up free|start free trial/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s action button/link; its states were measured but it was never followed — no checkout.', sel: '.p-tabs__card action' });
  await S('plan-row', await p20('.p-tabs__card li, .p-tabs__card [class*="feature"], .p-tabs__card [class*="item"]', 8), ['default'], { group: g, title: 'Plan feature row', desc: 'A feature row inside a plan card.', sel: '.p-tabs__card feature row' });
  await S('faq-q', q('.faq__q-wrap, .faq__item').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'FAQ disclosure', desc: 'A pricing FAQ disclosure row ("Can I cancel a subscription at any time?"); opened was measured after clicking it (a local UI toggle).', sel: '.faq__q-wrap' }, { before: { opened: async (loc) => { await loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.click())); await page.waitForTimeout(700); return 'clicked the FAQ row to expand its answer'; } } });
  await S('faq-a', await p20('.faq__item, .faq__a-wrap, [class*="faq"] p', 30), ['default'], { group: g, title: 'FAQ answer', desc: 'An expanded pricing FAQ answer paragraph.', sel: 'faq answer' });
  save();
}

async function feature() {
  if (!(await newPage('feature'))) return;
  await sheetsFor('feature');
  const g = G.feature;
  await S('feat-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature headline', desc: 'The /features/sitemap page heading.', sel: 'feature h1' }, { noScroll: true });
  await S('feat-cta', q('a.btn, a.button, a').filter({ hasText: /start|try for free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Feature CTA', desc: 'The feature page\'s primary action; measured, never followed.', sel: 'feature CTA' });
  await S('feat-card', await p20('[class*="card"], [class*="tile"], [class*="feature"]', 15), ['default', 'hover'], { group: g, title: 'Feature card', desc: 'A capability card on the sitemap feature page.', sel: 'feature [class*=card]' }, { pin: true });
  await S('feat-prose', await p20('main p, section p, p', 40), ['default'], { group: g, title: 'Feature paragraph', desc: 'A body paragraph on the feature page.', sel: 'feature p' });
  save();
}

async function contact() {
  if (!(await newPage('contact'))) return;
  const g = G.contact;
  await S('contact-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact headline', desc: 'The contact page heading.', sel: 'contact h1' }, { noScroll: true });
  await S('contact-field', q('.form__field input, input[type="text"], input').filter({ visible: true }).first(), FIELD, { group: g, title: 'Contact field', desc: 'A text input in the contact form; focused and typed into then cleared — the form was never submitted.', sel: 'contact input' }, { fillText: 'Example name' });
  await S('contact-area', q('textarea, input[placeholder*="message" i], input[name*="message" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Contact message area', desc: 'The message textarea; focused and typed into then cleared — never sent.', sel: 'contact textarea' }, { fillText: 'Hello' });
  await S('contact-submit', q('.form__submit, input[type="submit"], button[type="submit"], button').filter({ hasText: /send|submit/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Contact submit', desc: 'The contact form\'s send button; its states were measured but it was never clicked — nothing was sent.', sel: 'contact submit' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 10000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.login;
  await S('login-h1', q('h1, h2, [class*="title"], [class*="Title"]').filter({ hasText: /log ?in|sign ?in|welcome/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in headline', desc: 'The app sign-in heading on app.flowmapp.com/signin.', sel: 'signin heading' }, { noScroll: true });
  await S('login-card', q('form, [class*="card"], [class*="Card"], [class*="form"], [class*="Form"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in card', desc: 'The sign-in form card — e-mail and password fields, the primary submit and OAuth buttons.', sel: 'signin form/card' }, { noScroll: true });
  await S('login-field', q('input[type="email"], input[name*="mail" i], input[placeholder*="mail" i], input[type="text"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (sign-in)', desc: 'The sign-in e-mail input; focused and typed into then cleared — never submitted.', sel: 'signin email input' }, { noScroll: true, fillText: 'name@example.com' });
  await S('login-pass', q('input[type="password"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Password field (sign-in)', desc: 'The sign-in password input; focused and typed into then cleared — never submitted.', sel: 'signin password input' }, { noScroll: true, fillText: 'sample-pass-123' });
  await S('login-submit', q('button').filter({ hasText: /^(sign ?in|log ?in)$/i }).filter({ visible: true }).first(), [...B4, 'enabled'], { group: g, title: 'Sign-in submit', desc: 'The primary "Log In" submit; every state was measured but the button was never clicked — nothing was submitted. Disabled at rest until both fields validate; `enabled` is the fill it paints once sample text sits in both fields.', sel: 'signin submit button' }, { noScroll: true, before: { enabled: async () => {
    const em = q('input[type="email"], input[name*="mail" i], input[type="text"]').filter({ visible: true }).first();
    const pw = q('input[type="password"]').filter({ visible: true }).first();
    await em.click({ timeout: 4000 }).catch(() => em.evaluate((el) => el.focus())); await page.keyboard.type('name@example.com', { delay: 8 });
    await pw.click({ timeout: 4000 }).catch(() => pw.evaluate((el) => el.focus())); await page.keyboard.type('sample-pass-123', { delay: 8 });
    await page.waitForTimeout(500);
    return 'typed sample text into both fields so the submit enabled — still never clicked';
  } }, after: { enabled: async () => {
    for (const sel of ['input[type="email"], input[type="text"]', 'input[type="password"]']) {
      const f = q(sel).filter({ visible: true }).first();
      await f.click({ timeout: 2000 }).catch(() => f.evaluate((el) => el.focus()));
      await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace');
    }
    await page.waitForTimeout(300);
  } } });
  await S('login-google', q('button, a').filter({ hasText: /google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google OAuth button', desc: 'The "Sign in with Google" OAuth button; measured, never activated.', sel: 'signin Google button' }, { noScroll: true });
  await S('login-forgot', q('a, button, span').filter({ hasText: /forgot|restore/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Forgot-password link', desc: 'The "Forgot password?" link to /restore; measured, never followed.', sel: 'signin forgot link' }, { noScroll: true });
  await S('login-signup', q('a, button, span').filter({ hasText: /sign ?up|create.*account/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up link', desc: 'The "Sign Up" link beside the sign-in form; measured, never followed.', sel: 'signin signup link' }, { noScroll: true });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 10000 }))) return;
  const g = G.signup;
  await S('signup-h1', q('h1, h2, [class*="title"], [class*="Title"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-up headline', desc: 'The app sign-up heading on app.flowmapp.com/signup.', sel: 'signup heading' }, { noScroll: true });
  await S('signup-field', q('input[type="email"], input[name*="mail" i], input[placeholder*="mail" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (sign-up)', desc: 'The sign-up e-mail input; focused and typed into then cleared — never submitted.', sel: 'signup email input' }, { noScroll: true, fillText: 'name@example.com' });
  await S('signup-name', q('input[type="text"], input[name*="name" i], input[placeholder*="name" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Name field (sign-up)', desc: 'The sign-up name input; focused and typed into then cleared — never submitted.', sel: 'signup name input' }, { noScroll: true, fillText: 'Example User' });
  await S('signup-pass', q('input[type="password"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Password field (sign-up)', desc: 'The sign-up password input; focused and typed into then cleared — never submitted.', sel: 'signup password input' }, { noScroll: true, fillText: 'sample-pass-123' });
  await S('signup-submit', q('button').filter({ hasText: /sign ?up|create|continue|get started/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up submit', desc: 'The primary sign-up submit; its states were measured but the button was never clicked — no account was created.', sel: 'signup submit button' }, { noScroll: true });
  await S('signup-google', q('button, a').filter({ hasText: /google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google OAuth button (sign-up)', desc: 'The "Sign up with Google" button; measured, never activated.', sel: 'signup Google button' }, { noScroll: true });
  await S('signup-terms', q('a, span, p').filter({ hasText: /terms|privacy/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Terms line', desc: 'The terms/privacy line under the sign-up form; its links were never followed.', sel: 'signup terms line' }, { noScroll: true });
  save();
}

async function restore() {
  if (!(await newPage('restore', { wait: 10000 }))) return;
  const g = G.restore;
  await S('restore-h1', q('h1, h2, [class*="title"], [class*="Title"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Restore headline', desc: 'The password-restore heading on app.flowmapp.com/restore.', sel: 'restore heading' }, { noScroll: true });
  await S('restore-field', q('input[type="email"], input[name*="mail" i], input[type="text"], input').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (restore)', desc: 'The restore e-mail input; focused and typed into then cleared — never submitted.', sel: 'restore email input' }, { noScroll: true, fillText: 'name@example.com' });
  await S('restore-send', q('button').filter({ hasText: /send|restore|reset|continue/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Restore submit', desc: 'The restore submit; its states were measured but the button was never clicked — no reset e-mail was sent.', sel: 'restore submit button' }, { noScroll: true });
  await S('restore-back', q('a, button, span').filter({ hasText: /back|log ?in|sign ?in/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Back-to-login link', desc: 'The link back to the sign-in form; measured, never followed.', sel: 'restore back link' }, { noScroll: true });
  save();
}

async function sharesitemap() {
  if (!(await newPage('sharesitemap', { wait: 12000 }))) return;
  await sheetsFor('sharesitemap');
  await chrome('sharesitemap');
  const g = G.share;
  await S('sh-menu', q('button.ant-dropdown-trigger, button').filter({ hasText: /demo project/i }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Project dropdown', desc: 'The "Demo Project" dropdown in the share viewer header listing the published project\'s boards; opened was measured after clicking it — a local UI toggle whose items were never activated.', sel: 'share .ant-dropdown-trigger' }, { noScroll: true, before: { opened: openProjectMenu } });
  await S('sh-tab-structure', q('button').filter({ hasText: /^Structure$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Structure tab', desc: 'The "Structure" toolbar tab in the share viewer.', sel: 'share Structure tab' }, { noScroll: true });
  await S('sh-tab-estimation', q('button').filter({ hasText: /^Estimation$/ }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Estimation tab', desc: 'The "Estimation" toolbar tab; opened was measured after clicking it — a local UI toggle switching the viewer pane.', sel: 'share Estimation tab' }, { noScroll: true, before: { opened: async (loc) => { await loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.click())); await page.waitForTimeout(900); return 'clicked the "Estimation" tab'; } } });
  await S('sh-login-btn', q('button').filter({ hasText: /^Log ?In$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Share Log In button', desc: 'The "Log In" header button in the share viewer; measured, never clicked — the viewer stays signed out.', sel: 'share Log In button' }, { noScroll: true });
  await S('sh-signup-btn', q('button').filter({ hasText: /^Sign ?Up$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Share Sign Up button', desc: 'The "Sign Up" header button in the share viewer; measured, never clicked.', sel: 'share Sign Up button' }, { noScroll: true });
  await S('sh-popup', q('[class*="popup"]').filter({ hasText: /log ?in|sign ?up/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-up nudge', desc: 'The "Hi, Log In or Sign Up to start planning amazing websites!" toast pinned over the viewer (dismissable, left in place for the reading).', sel: 'share [class*=popup]' }, { noScroll: true });
  await S('sh-card', q('[class*="card--"], [class*="Card--"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Sitemap page card', desc: 'A page card on the published sitemap canvas (title, mini-map of sections); read-only.', sel: 'share [class*=card--]' }, { pin: true });
  await S('sh-blocks', q('[class*="blocks--"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sitemap card blocks', desc: 'The section list inside a sitemap page card (Menu, Header, Featured Services…).', sel: 'share [class*=blocks--]' });
  await S('sh-toolbar-btn', q('button[class*="dark--"]').filter({ visible: true }).first(), B4, { group: g, title: 'Canvas toolbar button', desc: 'An icon button on the share viewer\'s bottom toolbar panel.', sel: 'share toolbar button' }, { noScroll: true });
  await S('sh-toolbar-disabled', q('button[class*="disabled"], button[disabled]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Disabled toolbar button', desc: 'A disabled icon button on the share viewer\'s bottom toolbar.', sel: 'share disabled toolbar button' }, { noScroll: true });
  await S('sh-zoom', q('button').filter({ hasText: /%$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Zoom button', desc: 'The zoom-percentage button on the share viewer toolbar; measured, never toggled.', sel: 'share zoom button' }, { noScroll: true });
  await S('sh-help', q('button[class*="helpBtn"], [class*="helpBtn"]').filter({ visible: true }).first(), B4, { group: g, title: 'Help button', desc: 'The "?" help button on the share viewer chrome.', sel: 'share help button' }, { noScroll: true });
  save();
}

async function shareuserflow() {
  if (!(await newPage('shareuserflow', { wait: 12000 }))) return;
  const g = G.share;
  await S('uf-card', q('[class*="card--"], [class*="Card--"], [class*="node"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'User-flow card', desc: 'A screen/flow card on the published user-flow canvas; read-only.', sel: 'userflow [class*=card--]' }, { pin: true });
  await S('uf-tag', q('[class*="tag"], [class*="Tag"], [class*="badge"], [class*="status"], [class*="Status"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Status tag', desc: 'A status pill on the user-flow canvas (NEW / IN PROGRESS / DONE…).', sel: 'userflow status tag' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('header, .navbar, .nav.w-nav, [class*="navbar"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header at 390 wide: wordmark, the burger and the actions that survive the width.', sel: 'mobile header' }, { noScroll: true });
  await S('m-burger', q('.w-nav-button, [class*="burger"], [class*="menu-btn"], button').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Mobile burger', desc: 'The nav burger at 390 wide; opened was measured after tapping it (a local UI toggle opening the mobile menu).', sel: 'mobile burger' }, { noScroll: true, before: { opened: async (loc) => { await loc.tap({ timeout: 4000 }).catch(() => loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.click()))); await page.waitForTimeout(900); return 'tapped the nav burger to open the mobile menu'; } } });
  await S('m-menu-link', q('.w-nav-menu a, .nav__pop-wrap a, [class*="menu"] a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu link', desc: 'A link inside the opened mobile nav menu.', sel: 'mobile menu link' }, { noScroll: true });
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The hero display heading at 390 wide.', sel: 'mobile h1' });
  await S('m-hero-cta', q('a.btn').filter({ hasText: /start planning|try for free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile hero CTA', desc: 'The hero action at 390 wide; measured never followed.', sel: 'mobile hero CTA' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); www.flowmapp.com and app.flowmapp.com paint light only — no theme toggle or dark media query observed on any signed-out route';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, feature, contact, login, signup, restore, sharesitemap, shareuserflow, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the nav link's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a, .nav__link');
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
