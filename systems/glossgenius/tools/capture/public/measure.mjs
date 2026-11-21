// Measures glossgenius.com's public components in every state reachable
// without signing in, booking or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing feature demo login signup forgot bookservices mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// glossgenius.com is a Webflow marketing site (BEM-ish classes: .header_new,
// .btn_new, .link_new, .card-main, .accordion-item, .dropdown_new,
// .toggle_new), light-only — no theme toggle, no dark media query.
// app.glossgenius.com is a Next.js SPA under CSS modules (BaseInput_input__*,
// Button_root__*, Checkbox_input__*, TextAction_root__*): /login, /signup and
// /forgot-password paint the signed-out auth forms.
// bookings.glossgenius.com is a published booking website (every
// business gets a public booking site): the service list and the empty
// date-picker are reachable without an account. Select and BOOK are never
// pressed.
//
// Nothing is sent, bought, booked or signed into. The only activations are
// local UI toggles: the "How it works" nav mega-menu, the pricing
// Monthly/Annual switch, the pricing tier dropdown, a FAQ details row, the
// mobile burger, and the booking site's professional select (opened, never
// chosen). Auth and demo fields are photographed empty. Focus uses the
// keyboard. Nothing is typed. "Log in", "Sign up", "Send reset link",
// "Book a demo", "Select" and "BOOK n SERVICE" are measured, never activated.
// No consent overlay was observed; any that appears is hidden, never
// answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, LOGIN_URL, SIGNUP_URL, FORGOT_URL, BOOK_HOME, BOOK_SERVICES, BOOK_BOOK, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', pricing: '/pricing', feature: '/online-booking', demo: '/get-demo',
  login: LOGIN_URL, signup: SIGNUP_URL, forgot: FORGOT_URL,
  bookhome: BOOK_HOME, bookservices: BOOK_SERVICES, bookflow: BOOK_BOOK, mobile: '/',
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
  // overlay that mounts mid-run can swap the node a state reads. opts.pin
  // marks the resolved element once and every state below measures that same
  // node.
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
        if (opts.focusInner) {
          // A control whose label click toggles it (a checkbox) focuses its
          // inner input directly — never clicked, never toggled.
          await fld.evaluate((el) => {
            const t = el.matches('input,textarea,select') ? el : (el.querySelector('input,textarea,select') || el);
            t.focus();
          });
          await page.waitForTimeout(400);
          via = 'focused the inner input via .focus() — never clicked (a label click would check the box)';
        } else {
          await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
          await page.waitForTimeout(400);
          via = 'clicked into the field';
        }
      } else if (st === 'filled') {
        throw new Error('filled refused: do not type into a field');
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
const NEVER = /^(send|send message|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|continue with.*|claim this offer|try again|start for free|try for free|book a demo|start free trial|start planning|restore|send reset|reset password|send reset link|next|book \d+ service.*|book now)$/i;
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
  demo: 'Demo form', login: 'App sign-in', signup: 'App sign-up', forgot: 'App restore',
  book: 'Published booking site', mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens the "How it works" header mega-menu — a CSS-hover driven Webflow
// w-dropdown (the list flips visibility hidden->visible; no w--open class).
// The pointer is parked on the opened list to hold it during the reading. A
// local UI toggle; its links are measured, never followed.
async function openHiw() {
  const dd = q('.dropdown_new--header').filter({ hasText: /how it works/i }).first();
  if (!(await dd.count())) return 'no "How it works" dropdown';
  const btn = dd.locator('.w-dropdown-toggle').first();
  const open = async () => await page.evaluate(() => {
    for (const dd of document.querySelectorAll('.dropdown_new--header')) {
      if (!dd.innerText || !/how it works/i.test(dd.innerText)) continue;
      const l = dd.querySelector('.dropdown_new__list');
      if (l && getComputedStyle(l).visibility === 'visible') return true;
    }
    return false;
  }).catch(() => false);
  if (await open()) return 'the "How it works" menu was already open';
  for (let i = 0; i < 4; i++) {
    await btn.hover({ timeout: 4000 }).catch(() => dd.hover({ timeout: 4000 }).catch(() => {}));
    await page.waitForTimeout(1200);
    if (await open()) break;
  }
  if (!(await open())) return 'hovered the "How it works" trigger; the menu did not report open';
  const list = dd.locator('.dropdown_new__list').first();
  const box = await list.boundingBox().catch(() => null);
  if (box) { await page.mouse.move(box.x + Math.min(200, box.width / 2), box.y + 40); await page.waitForTimeout(500); }
  return 'hovered the "How it works" trigger; the CSS-hover mega-menu is held open by the parked pointer';
}

// The pricing "Beauty & Wellness / Medspa & Aesthetics" tier picker — a
// Webflow w-dropdown whose list toggles display:none->block on click (no
// w--open class). Opens it; its options are never activated.
async function openTier() {
  const t = q('.dropdown_new--pricing-tiers .w-dropdown-toggle').filter({ visible: true }).first();
  if (!(await t.count())) return 'no pricing tier dropdown';
  const open = async () => await page.evaluate(() => {
    for (const dd of document.querySelectorAll('.dropdown_new--pricing-tiers')) {
      const l = dd.querySelector('.w-dropdown-list');
      if (l && getComputedStyle(l).display !== 'none') return true;
    }
    return false;
  }).catch(() => false);
  if (await open()) return 'the tier dropdown was already open';
  for (let i = 0; i < 3; i++) {
    await t.click({ timeout: 4000 }).catch(() => t.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    if (await open()) return 'clicked the tier dropdown to list "Beauty & Wellness / Medspa & Aesthetics"';
  }
  return 'clicked the tier dropdown; it did not report open';
}

// On the booking site: the "Select a Professional" react-select — opens the
// gg-dropdown menu. A local UI toggle; the options are never chosen.
async function openPro() {
  const t = q('[class*="selectOuterContainer"], .gg-dropdown__control').filter({ visible: true }).first();
  if (!(await t.count())) return 'no professional select';
  const open = async () => !!(await q('.gg-dropdown__menu').count());
  if (await open()) return 'the professional menu was already open';
  for (let i = 0; i < 3; i++) {
    await t.click({ timeout: 4000 }).catch(() => t.evaluate((el) => el.click()));
    await page.waitForTimeout(1000);
    if (await open()) return 'clicked "Any Professional" to open the react-select menu';
  }
  return 'clicked the professional select; the menu did not report open';
}

// Empty-wall rule: never type an email, phone, name, password or code.
// Empty-wall rule: never type an email, phone, name, password or code.
const FIELD = ['default', 'focused'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('.header_new, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The marketing top bar: the GlossGenius wordmark, the "How it works" / "Businesses" / "Resources" mega-menus, Pricing, "Log in" and the "Book a demo" pill.', sel: '.header_new' }, { noScroll: true });
  await S('mkt-logo', q('.header_new__logo, .header_new a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The GlossGenius wordmark in the header, linking home.', sel: '.header_new__logo' }, { noScroll: true });
  await S('nav-link', q('.header_new a, .nav-link').filter({ hasText: /^Pricing$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A marketing header nav link (Pricing); measured, never followed.', sel: 'header Pricing link' }, { noScroll: true });
  await S('nav-hiw', q('.dropdown_new .nav-link, .w-dropdown-toggle').filter({ hasText: /how it works/i }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'How-it-works menu trigger', desc: 'The "How it works" nav item that opens the feature mega-menu (Agents, Booking & Scheduling, Marketing & CRM, Payments & POS, Staff & Business, EMR rails).', sel: 'nav How it works trigger' }, { noScroll: true, before: { opened: openHiw } });
  await S('nav-drop-item', q('.dropdown_new--header .nav-list--dropdown a, .dropdown_new--header .dropdown_new__list a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mega-menu item', desc: 'A feature link inside the opened "How it works" mega-menu; measured while the CSS-hover menu was held open by the parked pointer, never followed.', sel: '.nav-list--dropdown a' }, { noScroll: true, open: openHiw, noReset: true });
  // The header and hero CTAs have hidden 0x0 duplicates earlier in the DOM
  // (mobile-menu/template copies), so each is pinned by domFind — a DOM-level
  // non-zero-rect + computed-visibility check — not a bare locator filter.
  await S('nav-login', await domFind(page, /^Log ?in$/i, { sel: '.header_new a, .btn_new', tag: 'nlg', minW: 20, minH: 10 }), B4, { group: g, title: 'Log in button', desc: 'The header "Log in" button to app.glossgenius.com; measured, never followed.', sel: 'header Log in' }, { noScroll: true });
  await S('nav-demo', await domFind(page, /book a demo/i, { sel: '.header_new a, .btn_new', tag: 'nd', minW: 60, minH: 20 }), B4, { group: g, title: 'Book a demo pill', desc: 'The header "Book a demo" pill to /get-demo; measured, never followed.', sel: 'header Book a demo' }, { noScroll: true });
  await S('hero-eyebrow', q('.eyebrow_new, [class*="eyebrow"]').filter({ visible: true }).first(), ['default'], { group: G.home, title: 'Hero eyebrow', desc: 'The eyebrow line above the hero heading.', sel: '.eyebrow_new' }, { noScroll: true });
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: G.home, title: 'Hero headline', desc: '"Scheduling, payments, and admin. Handled." — the display heading.', sel: 'home h1' }, { noScroll: true });
  await S('hero-cta', await domFind(page, /start free trial/i, { sel: '.button-group_new.u-sm-w-100 a, .button-group_new.u-sm-w-100 .btn_new', tag: 'hc', minW: 60, minH: 20 }), B4, { group: G.home, title: 'Hero CTA', desc: 'The hero "Start free trial" button to /free-trial (the u-sm-w-100 button group — the header and mobile-nav button groups are excluded); measured, never followed.', sel: 'hero Start free trial' }, { noScroll: true });
  await S('hero-demo', q('a.btn_new, a').filter({ hasText: /get a demo|book a demo/i }).filter({ visible: true }).first(), B4, { group: G.home, title: 'Hero demo link', desc: 'The hero "Get a demo" action; measured, never followed.', sel: 'hero Get a demo' }, { noScroll: true });
  await S('gg-support', q('.gg-support-btn').filter({ visible: true }).first(), B4, { group: g, title: 'Support bubble', desc: 'The fixed support/chat launcher pinned to the corner of every marketing page; measured, never opened.', sel: '.gg-support-btn' }, { noScroll: true });
  await S('home-h2', q('h2').filter({ visible: true }).first(), ['default'], { group: G.home, title: 'Section heading', desc: 'A section heading on the marketing home.', sel: 'home h2' });
  await S('home-prose', await p20('main p, section p, .paragraph-body, p', 40), ['default'], { group: G.home, title: 'Body paragraph', desc: 'A body paragraph on the marketing home.', sel: 'home p' });
  await S('home-card', await p20('[class*="card"], [class*="tile"], [class*="feature"]', 15), ['default', 'hover'], { group: G.home, title: 'Home card', desc: 'A feature/benefit card on the marketing home.', sel: 'home [class*=card]' }, { pin: true });
  await S('home-footer', q('footer, [class*="footer"]').filter({ visible: true }).last(), ['default'], { group: G.footer, title: 'Footer', desc: 'The marketing footer: closing CTA, link columns, legal links and social marks.', sel: 'footer' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  const g = G.pricing;
  await S('ptoggle', q('.toggle_new').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Billing toggle', desc: 'The Monthly/Annual ("save up to 14%") switch above the plan cards — a checkbox-backed .toggle_new that loads annual-checked; opened was measured after clicking its input to select Monthly (a local UI toggle).', sel: '.toggle_new' }, { before: { opened: async (loc) => { const i = loc.locator('input[type="checkbox"], input').first(); if (await i.count()) await i.click({ timeout: 4000, force: true }).catch(() => i.evaluate((el) => el.click())); else await loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.click())); await page.waitForTimeout(900); return 'clicked the Monthly/Annual switch input to show monthly prices (annual is the default)'; } } });
  await S('ptier', q('.dropdown_new--pricing-tiers .dropdown_new__toggle, .dropdown_new--pricing-tiers .w-dropdown-toggle').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Plan tier dropdown', desc: 'The "Beauty & Wellness / Medspa & Aesthetics" plan-tier picker; opened was measured after clicking it — a local UI toggle whose options were never activated.', sel: '.dropdown_new--pricing-tiers toggle' }, { before: { opened: openTier } });
  await openTier(); // domFind resolves eagerly, so the list is opened before it runs
  await S('ptier-option', await domFind(page, /medspa/i, { sel: '.dropdown_new--pricing-tiers a', tag: 'po' }), ['default'], { group: g, title: 'Tier option', desc: 'The "Medspa & Aesthetics" option row inside the opened tier dropdown (the current option, "Beauty & Wellness", is display:none); measured while the list was held open, never activated.', sel: 'pricing tier option' }, { open: openTier, noReset: true });
  await S('plan-card', q('.card-main').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (Standard: $28/mo monthly, $24/mo annual — "Essential tools for businesses just starting out").', sel: '.card-main:first' });
  await S('plan-card-popular', q('.card_new').filter({ hasText: /most popular/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Popular plan card', desc: 'The "Most popular" Gold plan card ($56/$48 monthly) — the .card_new--pricing-small column carrying the amber tag; hover is a pointer hover, never clicked through.', sel: '.card_new popular' }, { pin: true });
  await S('plan-price', q('.card_new-price').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'The struck/full price block inside a plan card.', sel: '.card_new-price' });
  await S('plan-cta', q('.card-main a, .card-main button').filter({ hasText: /get started|start|sign up|try/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s action button/link; its states were measured but it was never followed — no checkout.', sel: '.card-main action' });
  await S('plan-row', await p20('.card-main li, .card-main [class*="feature"], .card-main [class*="item"], .pricing-table-row', 8), ['default'], { group: g, title: 'Plan feature row', desc: 'A feature/comparison row inside the pricing block (rate or feature line).', sel: 'plan feature row' });
  await S('ptab-nav', q('.pricing-table-nav__plan').filter({ visible: true }).first(), B4, { group: g, title: 'Compare-table plan nav', desc: 'A plan chip in the "Compare plans" table navigator.', sel: '.pricing-table-nav__plan' });
  await S('faq-item', q('details.accordion-item, .accordion-item').filter({ visible: true }).first(), ['default', 'hover', 'opened'], { group: g, title: 'FAQ accordion', desc: 'A native <details>/<summary> disclosure in the pricing "Included in every plan" list; opened was measured after clicking the summary row (a local UI toggle).', sel: 'details.accordion-item' }, { before: { opened: async (loc) => { const s = loc.locator('summary').first(); await s.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => { el.open = true; })); await page.waitForTimeout(700); return 'clicked the accordion summary to expand its answer'; } } });
  await S('faq-answer', await p20('.accordion-content, .accordion-item [class*="content"]', 20), ['default'], { group: g, title: 'Accordion content', desc: 'An expanded accordion\'s answer block (plan feature rows).', sel: '.accordion-content' });
  save();
}

async function feature() {
  if (!(await newPage('feature'))) return;
  await sheetsFor('feature');
  const g = G.feature;
  // The feature page's display heading is an h2.h1_new — its only h1 is the
  // small eyebrow line ("Online Booking System", measured separately below).
  await S('feat-h1', await domFind(page, /\S/, { sel: 'h2.h1_new, .h1_new, h1:not(.eyebrow_new)', tag: 'fh', minW: 200, minH: 40 }), ['default'], { group: g, title: 'Feature headline', desc: 'The /online-booking display heading ("Book more clients fast", h2.h1_new).', sel: 'feature h2.h1_new' }, { noScroll: true });
  await S('feat-cta', await domFind(page, /get started for free/i, { sel: 'a.btn_new, .btn_new', tag: 'fc', minW: 100, minH: 30 }), B4, { group: g, title: 'Feature CTA', desc: 'The feature page\'s "Get started for free" hero action; measured, never followed.', sel: 'feature CTA' });
  await S('feat-card', await p20('[class*="card"], [class*="tile"], [class*="feature"]', 15), ['default', 'hover'], { group: g, title: 'Feature card', desc: 'A capability card on the online-booking feature page.', sel: 'feature [class*=card]' }, { pin: true });
  await S('feat-prose', await p20('main p, section p, .paragraph-body, p', 40), ['default'], { group: g, title: 'Feature paragraph', desc: 'A body paragraph on the feature page.', sel: 'feature p' });
  save();
}

async function demo() {
  if (!(await newPage('demo'))) return;
  const g = G.demo;
  // The demo form is two steps: step 1 (#email-form, visible) is the
  // team-size radio pills plus a "Get a demo" link; step 2 is the real
  // HubSpot form inside .get-demo-form-step-2 (display:none until the link
  // runs). To measure step 2's declared styles the wrapper's display:none is
  // cleared inline — the "Get a demo" link itself is never activated, no
  // step transition is run and nothing is ever submitted.
  // Step 2 asks for a name, email and phone. Leave it hidden. Do not unhide it and do not type.
  await S('demo-h1', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Demo headline', desc: 'The /get-demo page heading ("See how GlossGenius works").', sel: 'demo h1' }, { noScroll: true });
  await S('demo-card', q('.card-main').filter({ visible: true }).first(), ['default'], { group: g, title: 'Demo form card', desc: 'The .card-main card holding the two-step demo form on the right of the heading.', sel: 'demo .card-main' });
  await S('demo-radio', q('#email-form label.radio_new').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Team-size radio pill', desc: 'A step-1 "How big is your team?" pill (Just me / 2-4 / 5-9 / 10+) — a label.radio_new tab; measured at rest and hovered, never chosen.', sel: '#email-form label.radio_new' });
  await S('demo-step-cta', q('#email-form a.btn_new, #email-form a').filter({ hasText: /get a demo/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Step-1 continue', desc: 'The "Get a demo" link that reveals step 2; its states were measured but it was never activated — step 2 was read with its wrapper unhidden instead.', sel: 'demo Get a demo' });
  // Step 2 (name, email, phone, selects, submit) stays hidden. Those controls are a form, not a local toggle.
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 10000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.login;
  await S('login-h1', await domFind(page, /welcome|log ?in|sign ?in/i, { sel: 'h1, h2, [class*="title"], [class*="Title"]', tag: 'lh', minW: 60, minH: 14 }), ['default'], { group: g, title: 'Sign-in headline', desc: 'The "Welcome back!" sign-in heading on app.glossgenius.com/login; pinned by size because a 1px hidden heading also matches.', sel: 'login heading' }, { noScroll: true });
  await S('login-card', q('form, [class*="card"], [class*="Card"], [class*="form"], [class*="Form"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in card', desc: 'The sign-in form card — e-mail and password fields, the primary "Log in" submit and the forgot-password link.', sel: 'login form/card' }, { noScroll: true });
  await S('login-field', q('input[type="email"], input[name*="mail" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (sign-in)', desc: 'The empty sign-in e-mail input. Focused with the keyboard, never typed into, never submitted.', sel: 'login email input' }, { noScroll: true });
  await S('login-pass', q('input[type="password"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Password field (sign-in)', desc: 'The empty sign-in password input. Focused with the keyboard, never typed into, never submitted.', sel: 'login password input' }, { noScroll: true });
  await S('login-submit', q('button').filter({ hasText: /^Log ?in$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in submit', desc: 'The primary "Log in" submit; its states were measured but the button was never clicked — nothing was submitted.', sel: 'login submit button' }, { noScroll: true });
  await S('login-forgot', q('a, button').filter({ hasText: /forgot/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Forgot-password link', desc: 'The "Forgot Password?" link to /forgot-password; measured, never followed.', sel: 'login forgot link' }, { noScroll: true });
  await S('login-signup', q('a, button').filter({ hasText: /sign up|free trial/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up link', desc: 'The "Sign up for free trial" link beside the sign-in form; measured, never followed.', sel: 'login signup link' }, { noScroll: true });
  await S('login-footer', await domFind(page, /about|careers|terms|privacy|contact/i, { sel: 'footer, [class*="Footer"], [class*="footer"]', tag: 'lf', leaf: false, minW: 300, minH: 30 }), ['default'], { group: g, title: 'App footer', desc: 'The app\'s public footer band (About, Careers, Terms, Privacy, Contact, social icons); pinned by width because a 24px footer-classed icon also matches.', sel: 'app footer' });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 10000 }))) return;
  const g = G.signup;
  await S('signup-h1', q('h1, h2, [class*="title"], [class*="Title"]').filter({ hasText: /get started|sign ?up|control/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-up headline', desc: 'The "Let\'s get started" sign-up heading on app.glossgenius.com/signup.', sel: 'signup heading' }, { noScroll: true });
  await S('signup-name', q('input[name="first_name"], input[id*="name" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Name field (sign-up)', desc: 'The empty sign-up first-name input. Focused, never typed into, never submitted.', sel: 'signup first_name input' }, { noScroll: true });
  await S('signup-email', q('input[type="email"], input[name*="mail" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (sign-up)', desc: 'The empty sign-up e-mail input. Focused, never typed into, never submitted.', sel: 'signup email input' }, { noScroll: true });
  await S('signup-pass', q('input[type="password"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Password field (sign-up)', desc: 'The empty sign-up password input. Focused, never typed into, never submitted.', sel: 'signup password input' }, { noScroll: true });
  await S('signup-phone', q('input[type="tel"], input[name*="phone" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Phone field (sign-up)', desc: 'The empty sign-up phone input. Focused, never typed into, never submitted.', sel: 'signup phone input' }, { noScroll: true });
  await S('signup-checkbox', q('input[type="checkbox"], [class*="Checkbox"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Professional checkbox', desc: 'The "I confirm that I\'m a professional or business owner" checkbox; focused via .focus() on its inner input — never clicked, never checked.', sel: 'signup checkbox' }, { noScroll: true, focusInner: true });
  await S('signup-promo', q('button, a').filter({ hasText: /promo/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Promo-code button', desc: 'The "Add Promo Code" secondary button; measured, never activated.', sel: 'signup promo button' }, { noScroll: true });
  await S('signup-submit', q('button').filter({ hasText: /sign ?up|get started|create|continue/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up submit', desc: 'The primary sign-up submit; its states were measured but the button was never clicked — no account was created.', sel: 'signup submit button' }, { noScroll: true });
  save();
}

async function forgot() {
  if (!(await newPage('forgot', { wait: 10000 }))) return;
  const g = G.forgot;
  await S('forgot-h1', q('h1, h2, [class*="title"], [class*="Title"]').filter({ hasText: /recover|forgot|password/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Restore headline', desc: 'The "Password recovery" heading on app.glossgenius.com/forgot-password.', sel: 'forgot heading' }, { noScroll: true });
  await S('forgot-field', q('input[type="email"], input').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (restore)', desc: 'The empty restore e-mail input. Focused, never typed into, never submitted.', sel: 'forgot email input' }, { noScroll: true });
  await S('forgot-send', q('button').filter({ hasText: /send|reset|continue/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Restore submit', desc: 'The "Send reset link" submit; its states were measured but the button was never clicked — no reset e-mail was sent.', sel: 'forgot submit button' }, { noScroll: true });
  await S('forgot-back', q('a, button').filter({ hasText: /back|log ?in|sign ?in/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Back-to-login link', desc: 'The "Back to login" link; measured, never followed.', sel: 'forgot back link' }, { noScroll: true });
  save();
}

async function bookhome() {
  if (!(await newPage('bookhome', { wait: 10000 }))) return;
  await sheetsFor('bookhome');
  await chrome('bookhome');
  const g = G.book;
  await S('bk-nav', q('nav, [class*="Navigation_nav"], header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Booking-site nav', desc: 'The published booking website\'s top nav (About, Our Team, Services, Portfolio, Shop, Contact, BOOK NOW).', sel: 'booking nav' }, { noScroll: true });
  await S('bk-nav-item', q('nav a, [class*="Navigation"] a').filter({ hasText: /services/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Booking nav link', desc: 'A nav link on the booking site; measured, never followed.', sel: 'booking nav link' }, { noScroll: true });
  await S('bk-book-cta', q('a, button').filter({ hasText: /book now/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Book Now button', desc: 'The booking site\'s "BOOK NOW" nav button to the service list; measured, never followed.', sel: 'booking BOOK NOW' }, { noScroll: true });
  await S('bk-title', await domFind(page, /\S/, { sel: 'h1', tag: 'bt', minW: 80, minH: 20 }), ['default'], { group: g, title: 'Booking title', desc: 'The business-name display heading on the published booking site.', sel: 'booking h1' }, { noScroll: true });
  await S('bk-badge', q('a, div, span').filter({ hasText: /powered by/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Powered-by badge', desc: 'The "powered by GLOSSGENIUS" badge on the published site.', sel: 'booking powered-by' });
  save();
}

async function bookservices() {
  if (!(await newPage('bookservices', { wait: 10000 }))) return;
  await sheetsFor('bookservices');
  const g = G.book;
  await S('bk-pro-select', q('[class*="selectOuterContainer"], [class*="Select_select"], .gg-dropdown__control').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Professional select', desc: 'The "Select a Professional" react-select on the service list (Any Professional, the business\'s pros); opened was measured with its .gg-dropdown__menu held open — an option was never chosen.', sel: 'booking professional select' }, { before: { opened: openPro } });
  await S('bk-pro-option', q('.gg-dropdown__option, [class*="option"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Professional option', desc: 'An option row inside the opened professional menu; measured while the menu was held open, never chosen.', sel: '.gg-dropdown__option' }, { open: openPro, noReset: true });
  await S('bk-service-card', q('[class*="ClassicService_root"], [class*="ClassicService_card"], [class*="service"]').filter({ hasText: /\$|min/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Service card', desc: 'A service card on the published list (category, name, description, price, duration, Select).', sel: 'booking service card' }, { pin: true });
  await S('bk-service-select', q('button').filter({ hasText: /^Select$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Service Select button', desc: 'A service row\'s "Select" button. Measured at rest, hover, focus-visible and forced pressed. Never clicked: selecting a service starts a booking.', sel: 'booking Select button' });
  await S('bk-book-btn', q('button, a').filter({ hasText: /book \d+ service/i }).filter({ visible: true }).first(), B4, { group: g, title: 'BOOK bar button', desc: 'The "BOOK n SERVICE" header bar at rest (BOOK 0 SERVICE). Never pressed.', sel: 'booking BOOK button' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('.header_new, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header at 390 wide: wordmark, the burger and the actions that survive the width.', sel: 'mobile header' }, { noScroll: true });
  // The hero is measured BEFORE the burger opens the nav menu: the opened
  // menu reveals hidden desktop-width copies (~5205 px) that share the hero
  // text and would otherwise win a text match.
  await S('m-hero-h1', await domFind(page, /scheduling|payments|handled/i, { sel: 'h1', tag: 'mh', minW: 100, minH: 24 }), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The hero display heading ("Scheduling, payments, and admin. Handled.") at 390 wide, measured before the nav menu opens.', sel: 'mobile h1' });
  await S('m-hero-cta', q('.btn_new').filter({ hasText: /start free trial|get started|book a demo/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile hero CTA', desc: 'The hero action at 390 wide; measured never followed.', sel: 'mobile hero CTA' });
  await S('m-burger', q('.header_new__m-menu-btn, .w-nav-button, [class*="menu-btn"], button').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Mobile burger', desc: 'The nav burger at 390 wide; opened was measured after tapping it (a local UI toggle opening the mobile menu).', sel: 'mobile burger' }, { noScroll: true, before: { opened: async (loc) => { await loc.tap({ timeout: 4000 }).catch(() => loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.click()))); await page.waitForTimeout(900); return 'tapped the nav burger to open the mobile menu'; } } });
  await S('m-menu-link', q('.w-nav-menu a, [class*="menu"] a, .header_new a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu link', desc: 'A link inside the opened mobile nav menu.', sel: 'mobile menu link' }, { noScroll: true });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); glossgenius.com, app.glossgenius.com and bookings.glossgenius.com paint light only — no theme toggle or dark media query observed on any signed-out route';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
// The public date-picker at /booking-flow is photographed empty. Choosing a
// professional or a service category starts a booking, so those selects are
// not opened here.
const plan = { home, pricing, feature, demo, login, signup, forgot, bookhome, bookservices, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (a header button's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '.btn_new, .link_new, .header_new a');
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
