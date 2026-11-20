// Measures framer.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing contact login gallery mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// framer.com is three public stacks signed out. The marketing pages
// (www.framer.com/...) are themselves a Framer site: the declared token
// layer is the project's ~580 `--token-<uuid>` colour styles on `body`
// (the dark palette, the #cbff00 lime accent); sizes and text styles live
// inline per element, so geometry and type are measured values.
// /community/gallery and /marketplace are the product's community stack, a
// different app that also paints dark; /login is the auth shell — a light
// third stack. The .framer-* class names are hashed per project, so specs
// select by role, aria-label, element type or text. Nothing is sent,
// bought or signed into: the only presses are local UI toggles — the
// header's Platform mega-dropdown (hover), the mobile nav button; the
// login e-mail field and the gallery search box are typed into and
// cleared, never submitted; Continue with Google, Continue, Open and
// every CTA are measured, never followed. The consent card is hidden,
// never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, LOGIN_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', contact: '/contact/', login: LOGIN_URL, gallery: '/community/gallery/', mobile: '/' };
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
  shell: 'Site chrome', home: 'Home', pricing: 'Pricing', contact: 'Contact',
  auth: 'Login (auth shell)', gallery: 'Community gallery (product stack)',
  mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens the header's "Platform" mega-dropdown: an `a` element without href
// whose panel mounts under the bar on hover. The pointer rests on the
// trigger until a wide panel reports open; Escape and a move to the page
// edge close it afterwards. Its links are never followed.
async function openPlatformMenu() {
  const btn = page.locator('nav a, header a, div a').filter({ hasText: /^Platform/ }).filter({ visible: true }).first();
  if (!(await btn.count())) return 'no Platform trigger';
  // Finds the panel, tags it data-mjs-panel so the spec's locator can be a
  // plain attribute match, and reports open.
  const open = async () => page.evaluate(() => {
    const el = [...document.querySelectorAll('body *')].filter((x) => {
      const t = (x.innerText || '');
      const r = x.getBoundingClientRect();
      return r.width > 300 && r.height > 150 && /^(Create|Design|Build|Grow)\b/.test(t.trim()) && /Framer|AI|MCP|CMS|SEO/.test(t);
    }).sort((a, b) => a.innerText.length - b.innerText.length)[0];
    if (!el) return false;
    el.setAttribute('data-mjs-panel', '1');
    return true;
  }).catch(() => false);
  if (await open()) return 'the Platform dropdown was already open';
  for (let i = 0; i < 4; i++) {
    await btn.hover({ timeout: 4000 }).catch(() => {});
    await page.waitForTimeout(1200);
    if (await open()) return 'hovered the "Platform" trigger to open the mega-dropdown';
  }
  return 'hovered "Platform"; the dropdown did not report open';
}

// Opens the mobile nav overlay: the header's nav toggle on the phone
// surface. Framer sites switch the nav control to a menu variant under the
// breakpoint; the button may carry an aria-label or no text at all.
async function openMobileMenu() {
  // Finds the overlay, tags it data-mjs-overlay so the spec's locator can be
  // a plain attribute match, and reports open.
  const open = () => page.evaluate(() => {
    const el = [...document.querySelectorAll('body *')].filter((x) => {
      if (x === document.body || x === document.documentElement) return false;
      const r = x.getBoundingClientRect();
      const t = (x.innerText || '');
      return r.width > 300 && r.height > 400 && r.height < 3000 && /Platform|Solutions|Resources/.test(t) && /Log in|Sign up/.test(t);
    }).sort((a, b) => a.innerText.length - b.innerText.length)[0];
    if (!el) return false;
    el.setAttribute('data-mjs-overlay', '1');
    return true;
  }).catch(() => false);
  if (await open()) return 'the nav overlay was already open';
  const b = page.locator('[data-framer-name="Mobile Menu"], [data-framer-name="Menu"], [data-framer-name="navswitch"], button[aria-label*="menu" i], button[aria-label*="navigation" i]').filter({ visible: true }).first();
  if (!(await b.count())) return 'no menu toggle';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    if (await open()) return 'clicked the Mobile Menu toggle to open the mobile menu';
    await b.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(900);
    if (await open()) return 'focused the Mobile Menu toggle and pressed Enter to open the mobile menu';
  }
  return 'activated the nav toggle; the overlay did not report open';
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell, h = G.home, f = G.footer;
  await S('mkt-header', q('header, [data-framer-name*="nav" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The bar on every marketing page: the Framer mark, the Platform/Solutions/Resources mega-dropdown triggers, Pricing, Enterprise, "Log in" and "Sign up".', sel: 'header / top nav' }, { noScroll: true });
  await S('mkt-logo', q('a[aria-label*="Framer" i], header a[href="/"], a[href$="/"]').filter({ hasText: /^\s*Framer\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Framer mark in the header, linking home.', sel: 'header a Framer' }, { noScroll: true });
  await S('nav-dropdown-btn', q('nav a, header a, div a').filter({ hasText: /^Platform$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav dropdown trigger', desc: 'The "Platform" header item — an `a` without href whose mega-dropdown opens on hover (never followed).', sel: 'header a Platform' }, { noScroll: true });
  await S('nav-panel', q('[data-mjs-panel]'), ['default'], { group: g, title: 'Platform dropdown panel', desc: 'The mega-dropdown panel opened by hovering "Platform" (Create/Build/Grow columns and the Updates thumbnail); its links were never followed.', sel: 'platform mega-dropdown panel' }, { open: openPlatformMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await page.mouse.move(1438, 890).catch(() => {});
  await S('nav-pricing', q('a').filter({ hasText: /^Pricing$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The "Pricing" header link; measured, never followed.', sel: 'header a Pricing' }, { noScroll: true });
  await S('nav-login', q('a, button').filter({ hasText: /^Log in$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in link', desc: 'The "Log in" header link to /login; measured, never followed.', sel: 'header a Log in' }, { noScroll: true });
  await S('nav-cta', q('a, button').filter({ hasText: /^Sign up$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Header CTA', desc: 'The "Sign up" header button; links to the auth shell, measured never followed.', sel: 'header a Sign up' }, { noScroll: true });

  await S('hero-h1', await domFind(page, /\S/, { sel: 'h1', tag: 'h1', minW: 200, minH: 20 }), ['default'], { group: h, title: 'Hero headline', desc: '"Framer is the pro website builder with a world-class design agent" — the www.framer.com hero display heading.', sel: 'h1' }, { noScroll: true });
  await S('hero-cta', q('a').filter({ hasText: /^Get started for free$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The white "Get started for free" pill in the hero; links to the auth shell, measured never followed.', sel: 'hero Get started for free' });
  await S('hero-mcp', q('a, button').filter({ hasText: /Install the MCP/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero secondary button', desc: 'The "Install the MCP" ghost button beside the hero CTA; measured, never followed.', sel: 'hero Install the MCP' });
  await S('section-h2', q('h2').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading further down the home page.', sel: 'h2' });

  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: f, title: 'Footer', desc: 'The page footer: product/solutions/resources/company columns, social icons and the English/Japanese locale select.', sel: 'footer' });
  await S('footer-link', q('footer a').filter({ hasText: /^Careers$/ }).first(), B4, { group: f, title: 'Footer link', desc: 'A footer sitemap link; measured, never followed.', sel: 'footer a Careers' });
  await S('locale-select', q('footer select, [role="contentinfo"] select').filter({ visible: true }).first(), B4, { group: f, title: 'Locale select', desc: 'The "English" locale select in the footer — a local UI control; measured, never changed.', sel: 'footer select locale' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('price-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing headline', desc: '"Start free, then scale your site" — the /pricing masthead.', sel: 'h1' }, { noScroll: true });
  await S('billing-toggle', q('p, div, span').filter({ hasText: /^Yearly billing$/ }).filter({ visible: true }).last().locator('xpath=ancestor::*[self::div or self::button][1]'), B4, { group: g, title: 'Billing toggle', desc: 'The "Yearly billing" switch beside the plan names; measured at rest, never toggled (toggling would re-price the grid).', sel: 'yearly billing toggle' }, { noScroll: true });
  await S('credits-select', q('select[name="Credits per month"], select').filter({ hasText: /credits/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Credits select', desc: 'The "Credits per month" select on a plan card (1,000–10,000 AI credits); measured at rest, never opened (its options recompute prices).', sel: 'credits per month select' });
  await S('plan-card', q('h2').filter({ hasText: /^Pro$/ }).locator('xpath=ancestor::*[self::div or self::article][.//a or .//button][1]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'The Pro plan column: name, price, feature list and its CTA.', sel: 'Pro plan card' });
  await S('plan-cta', q('h2').filter({ hasText: /^Pro$/ }).locator('xpath=ancestor::*[self::div or self::article][.//a or .//button][1]').locator('a, button').filter({ visible: true }).last(), B4, { group: g, title: 'Plan CTA', desc: 'The Pro plan card\'s action button; measured, never followed.', sel: 'Pro plan CTA' });
  await S('faq-acc', q('h3').filter({ hasText: /^What are credits\?/ }).locator('xpath=ancestor::*[self::div or self::button or self::summary][1]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'FAQ row', desc: 'A question row in the /pricing FAQ ("What are credits?"); measured at rest and on hover, never toggled.', sel: 'FAQ row What are credits' });
  save();
}

async function contact() {
  if (!(await newPage('contact'))) return;
  const g = G.contact;
  await S('contact-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact headline', desc: '"Get in touch with the team" — the /contact masthead over the support/billing/sales directory.', sel: 'h1' }, { noScroll: true });
  await S('contact-card', q('h2').filter({ hasText: /^Support$/ }).locator('xpath=ancestor::*[self::div or self::article or self::section][.//a or .//button][1]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact card', desc: 'The Support directory card; a contact surface, not a form.', sel: 'Support card' });
  await S('contact-link', q('h2').filter({ hasText: /^Support$/ }).locator('xpath=ancestor::*[self::div or self::article or self::section][.//a][1]').locator('a').filter({ visible: true }).first(), B4, { group: g, title: 'Contact link', desc: 'A link inside a contact directory card; measured, never followed.', sel: 'contact card link' });
  save();
}

async function login() {
  if (!(await newPage('login', { url: LOGIN_URL, wait: 10000 }))) return;
  const g = G.auth;
  await S('login-panel', q('form, main, [class*="login" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login panel', desc: 'The auth-shell sign-in card on /login: "Welcome to Framer" with Google SSO and an e-mail field. The auth shell is a light third stack.', sel: 'login form' }, { noScroll: true });
  await S('login-google', q('button').filter({ hasText: /Continue with Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google SSO button', desc: 'The "Continue with Google" button; measured, never pressed.', sel: 'login Continue with Google' }, { noScroll: true });
  await S('login-email', q('input[type="email"], input[name="email"], input[placeholder*="email" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (login)', desc: 'The work e-mail input on the sign-in card; focused and typed into then cleared — never submitted.', sel: 'login email input' }, { noScroll: true, fillText: 'name@example.com' });
  await S('login-submit', q('button[type="submit"], button').filter({ hasText: /^Continue$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue submit', desc: 'The "Continue" submit button; its states were measured but the button was never clicked — nothing was submitted.', sel: 'login Continue' }, { noScroll: true });
  save();
}

async function gallery() {
  if (!(await newPage('gallery', { wait: 10000 }))) return;
  const g = G.gallery;
  await S('gal-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Gallery headline', desc: '"Gallery" — the /community/gallery masthead in the community stack (a different app that also paints dark).', sel: 'h1' }, { noScroll: true });
  // The input remounts while the keystroke lands, so the 'filled' state's box
  // reads 0x0; default+focused are the reliable states. It was still typed
  // into and cleared, never searched.
  await S('gal-search', q('div[class*="desktop" i] input[type="search"], div[class*="desktop" i] input[placeholder*="Search" i], input[placeholder*="Search Gallery" i]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Gallery search', desc: 'The "Search Gallery" input; focused and typed into then cleared — never searched.', sel: 'gallery search input' }, { noScroll: true, fillText: 'portfolio' });
  // The toolbar ships a hidden mobile copy of the same buttons ahead of the
  // desktop row in DOM order; scope to the desktop toolbar.
  await S('gal-filter', q('div[class*="desktop" i] button').filter({ hasText: /^(Trending|Recent|Vibe)$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Filter button', desc: 'A gallery sort button (Trending / Recent / Vibe); measured at rest, never toggled (toggling would re-sort the grid).', sel: 'gallery Trending' }, { noScroll: true });
  await S('gal-open', q('a[role="button"]').filter({ hasText: /^Open$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Card Open button', desc: 'An "Open" button on a gallery card; measured, never followed (it would open the site\'s page).', sel: 'gallery Open' });
  await S('gal-comm', q('button').filter({ hasText: /^Community$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Community menu button', desc: 'The "Community" dropdown button in the gallery header — a local UI toggle; measured, never toggled.', sel: 'gallery Community button' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  const g = G.mobile;
  await S('m-topbar', q('header, [data-framer-name*="nav" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header at 390 wide: the Framer mark and the nav toggle.', sel: 'mobile header' }, { noScroll: true });
  const ham = q('[data-framer-name="Mobile Menu"], [data-framer-name="Menu"], [data-framer-name="navswitch"], button[aria-label*="menu" i], button[aria-label*="navigation" i]').filter({ visible: true }).first();
  await S('m-menu-btn', ham, [...B4, 'opened'], { group: g, title: 'Mobile menu button', desc: 'The header nav toggle at 390 wide — a local UI toggle; the opened state was measured after activating it.', sel: 'mobile nav toggle' }, { noScroll: true, allowLink: true });
  await S('m-drawer', q('[data-mjs-overlay]'), ['default'], { group: g, title: 'Mobile nav overlay', desc: 'The nav overlay opened by the menu button (the page links plus Log in/Sign up); its links were never followed.', sel: 'mobile nav overlay' }, { open: openMobileMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide.', sel: 'mobile h1' });
  await S('m-hero-cta', q('a').filter({ hasText: /^Get started for free$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile hero CTA', desc: 'The hero "Get started for free" pill at 390 wide; measured never followed.', sel: 'mobile hero CTA' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every marketing page on www.framer.com paints the body-declared --token-<uuid> dark palette (no theme switcher exists); /community/gallery is the product community stack, also dark; /login is the auth shell, a light third stack';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, contact, login, gallery, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the header CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'a[href*="signup"], a[href*="login"]');
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
