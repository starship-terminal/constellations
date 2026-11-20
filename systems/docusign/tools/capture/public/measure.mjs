// Measures docusign.com's public components in every state reachable without
// signing in, buying, submitting or consenting to anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home esignature trial signgen stories company pricing login mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/;
// raw/measurements.md is built by build-measurements.mjs.
//
// docusign.com is three surfaces signed out: the Next.js/Emotion marketing
// site on www.docusign.com (no custom properties — every value is a measured
// computed style), the plan storefront on ecom.docusign.com (geo-redirects to
// /en-SG/, captured as served) and the public sign-in form apps.docusign.com
// lands on (account.docusign.com's OAuth page — measured, never filled or
// submitted). Nothing is sent, bought or signed into: the only presses are
// local UI toggles — the Products mega-menu trigger, an FAQ accordion row, a
// customer-story video's Expand button, the signature generator's Type tab
// and colour swatches, the Monthly billing toggle and the mobile hamburger.
// The OneTrust banner, Sierra chat, Guideflow player and locale nudge are
// hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, CY, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', esignature: '/products/electronic-signature', trial: '/free-trial',
  signgen: '/signature-generator', stories: '/customer-stories', company: '/company',
  pricing: 'https://ecom.docusign.com/plans-and-pricing/esignature',
  login: 'https://apps.docusign.com/send',
};
const urlFor = (key) => URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key];
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes the edge gates this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
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
  const cleared = await open(page, url || urlFor(key), { wait, promo });  // false: the bot check did not clear (lib.mjs)
  if (!cleared || (await blocked())) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
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
  Object.assign(c, { page: current, run, url: URLS[current] && urlFor(current) }, meta);
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
      } else if (st === 'selected') {
        if (opts.noToggle) via = 'held selected by an earlier toggle';
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

// Clicks a UI toggle (dropdown, menu, radio, day). Refuses a submit button and
// any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|continue|claim this offer|try again|next|confirm|schedule event|i understand|decline)$/i;
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
    await p.goto(BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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

// Marks the nearest ancestor of the element matching sel that paints a fill
// or a background image (the hero island paints a gradient), or falls back to
// marking a painted descendant: the hero card is a sibling layer, not an
// ancestor, so for it we mark the painted element inside its section instead.
async function markPainted(sel, tag, { maxUp = 8, minW = 100, minH = 60, descend = false } = {}) {
  const ok = await page.evaluate(([s, t, up, w, h, desc]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const el = [...document.querySelectorAll(s)].find((n) => { const r = n.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    if (!el) return false;
    const paints = (cs) => cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none';
    if (!desc) for (let n = el, i = 0; n && i < up; n = n.parentElement, i++) {
      const cs = getComputedStyle(n);
      const r = n.getBoundingClientRect();
      if (r.width >= w && r.height >= h && paints(cs)) { n.setAttribute('data-m-mark', t); return true; }
    }
    if (desc) {
      // The painted layer sits beside the content, not above it: find the
      // biggest painted element under the element's own section.
      const sec = el.closest('section') || el.parentElement;
      const cands = [...(sec || el).querySelectorAll('*')].filter((n) => {
        const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
        return r.width >= w && r.height >= h && paints(cs);
      }).sort((a, b) => b.getBoundingClientRect().width * b.getBoundingClientRect().height - a.getBoundingClientRect().width * a.getBoundingClientRect().height);
      if (cands[0]) { cands[0].setAttribute('data-m-mark', t); return true; }
    }
    return false;
  }, [sel, tag, maxUp, minW, minH, descend]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}


const G = {
  shell: 'Shell and navigation', hero: 'Home hero', home: 'Home',
  esig: 'eSignature page', trial: 'Free trial', signgen: 'Signature generator',
  stories: 'Customer stories', pricing: 'Pricing storefront (ecom)',
  auth: 'Log in', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('utilitynav', q('nav[data-cy="utilitynav"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Utility bar', desc: 'The top strip over the main nav: the announcement link, sales phone, Search, Support, Access Documents and Log In.', sel: 'nav[data-cy=utilitynav]' }, { noScroll: true });
  await S('header', q('nav[data-cy="navbar"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The primary nav inside the sticky chrome: wordmark, the Products/Solutions/Resources dropdown triggers, Enterprise and Plans & Pricing links, and the Contact-sales/Buy-now/Try-for-free actions.', sel: 'nav[data-cy=navbar]' }, { noScroll: true });
  await S('logo', q('nav[data-cy="navbar"] a[aria-label="Docusign"], a[aria-label="Docusign"]').filter({ visible: true }).first(), B4, { group: g, title: 'Logo', desc: 'The Docusign wordmark anchor (aria-label "Docusign").', sel: 'navbar a[aria-label=Docusign]' }, { noScroll: true });
  await S('nav-trigger', q('nav[data-cy="navbar"] button').filter({ hasText: /^\s*Products\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Products button that opens the full-width mega-menu; toggled, never followed.', sel: 'navbar button "Products"' }, { noScroll: true });
  await S('nav-link', q('nav[data-cy="navbar"] a').filter({ hasText: /^\s*Plans & Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The plain Plans-&-Pricing header link.', sel: 'navbar a "Plans & Pricing"' }, { noScroll: true });
  await S('nav-contact', q('nav[data-cy="navbar"] a').filter({ hasText: /^\s*CONTACT SALES\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Contact-sales link', desc: 'The uppercase Contact-sales text action; measured never followed.', sel: 'navbar a "CONTACT SALES"' }, { noScroll: true });
  await S('nav-buy', q('nav[data-cy="navbar"] a').filter({ hasText: /^\s*BUY NOW\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Buy-now link', desc: 'The uppercase Buy-now text action; measured never followed.', sel: 'navbar a "BUY NOW"' }, { noScroll: true });
  await S('nav-cta', q('nav[data-cy="navbar"] a, nav[data-cy="navbar"] button').filter({ hasText: /^\s*TRY FOR FREE\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Try-for-free CTA', desc: 'The filled purple Try-for-free pill; measured never followed.', sel: 'navbar "TRY FOR FREE"' }, { noScroll: true });
  await S('nav-search', q('nav[data-cy="utilitynav"] button, [data-cy="searchopen"], button[aria-label*="search" i]').filter({ hasText: /search|^\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Search button', desc: 'The Search button in the utility bar.', sel: 'utilitybar Search' }, { noScroll: true });
  await S('login-link', q('nav[data-cy="utilitynav"] a').filter({ hasText: /^\s*Log In\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log-in link', desc: 'The utility-bar Log In link; measured never followed.', sel: 'utilitynav a "Log In"' }, { noScroll: true });
  // The Products trigger opens the mega-menu on click (aria-expanded); keep it
  // open while the panel and one of its links are read, then Escape.
  const openMenu = async () => {
    const link = q('nav[data-cy="navbar"] a[href*="products/electronic-signature"]').first();
    if (await link.isVisible().catch(() => false)) return;
    const t = q('nav[data-cy="navbar"] button').filter({ hasText: /^\s*Products\s*$/ }).filter({ visible: true }).first();
    if (await t.count()) {
      await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click()));
      await page.waitForTimeout(1400);
    }
  };
  try { await openMenu(); } catch (e) { log('  ! dropdown open failed', String(e.message).split('\n')[0]); }
  const panelMark = await markPainted('nav[data-cy="navbar"] a[href*="products/electronic-signature"]', 'm-panel', { minW: 400, minH: 200, descend: true }).catch(() => null);
  const panel = (panelMark && (await panelMark.count())) ? panelMark : q('nav[data-cy="navbar"] a[href*="products/electronic-signature"]').filter({ visible: true }).first().locator('xpath=ancestor::div[4]');
  await S('nav-dropdown', panel, ['default'], { group: g, title: 'Nav dropdown', desc: 'The Products mega-menu panel, opened by its own trigger (a full-width white sheet).', sel: 'mega-menu panel' }, { noScroll: true, noReset: true, open: openMenu });
  await S('menu-link', q('nav[data-cy="navbar"] a[href*="products/electronic-signature"], nav[data-cy="navbar"] a[href*="products/web-forms"]').filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A product link inside the opened mega-menu (bold label over a grey description).', sel: 'mega-menu product link' }, { noScroll: true, open: openMenu, before: { hover: openMenu, 'focus-visible': openMenu, pressed: openMenu } });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  const h = G.hero;
  const heroMark = await markPainted('h1', 'm-hero', { minW: 800, minH: 200 }).catch(() => null);
  await S('hero-section', (heroMark && (await heroMark.count())) ? heroMark : q('section').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero section', desc: 'The painted #26065d deep-purple hero band.', sel: 'first painted ancestor of h1' });
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The 80px DSIndigo-300 white headline on the purple band.', sel: 'h1' }, { noScroll: true });
  await S('hero-lede', q('h1 ~ p, h1 + p, main p, [role="main"] p, p').filter({ hasText: /agree|signature|contract|business/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The lede under the hero headline.', sel: 'hero lede' });
  await S('hero-cta', q('button, a').filter({ hasText: /^\s*Get Started\s*$/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The filled Get-Started pill in the hero; measured never followed.', sel: '"Get Started"' });
  await S('hero-link', q('a').filter({ hasText: /Explore Docusign IAM|Explore eSignature/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero link', desc: 'The Explore-Docusign-IAM arrow link under the hero CTA; measured never followed.', sel: '"Explore Docusign IAM"' });
  await S('hero-field', q('input[name="workEmail"], input[type="email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: h, title: 'Hero email field', desc: 'The hero work-email input on the purple band; sample text was typed and deleted, nothing sent.', sel: 'input[name=workEmail]' }, { fillText: 'alex@example.com' });
  await S('hero-checkbox', q('input[type="checkbox"]').filter({ visible: true }).first().locator('xpath=..'), B4, { group: h, title: 'Hero consent checkbox', desc: 'The painted square of the marketing-opt-in checkbox on the purple band (the real input is a 1x1 inside it); measured, never toggled on this surface.', sel: 'hero checkbox painted square' });
  await S('hero-country', q('label').filter({ has: q('select') }).filter({ visible: true }).first(), B4, { group: h, title: 'Country picker', desc: 'The Country/region labelled control under the hero form (a native select at opacity 0 inside its painted label; reads Singapore on this vantage); measured, never opened.', sel: 'label:has(select)' });
  const s = G.home;
  await S('h2-section', q('h2').filter({ visible: true }).first(), ['default'], { group: s, title: 'Section heading', desc: 'A marketing section h2 (DSIndigo).', sel: 'first h2' });
  await S('blog-card', q('a').filter({ hasText: /Momentum|blog|report|workflow|agreement/i }).filter({ visible: true }).last(), B4, { group: s, title: 'Card link', desc: 'A marketing card link (blog-teaser or resource card); measured never followed.', sel: 'card link' });
  await S('assistant', q('button, a').filter({ hasText: /Docusign Assistant/i }).filter({ visible: true }).first(), B4, { group: s, title: 'Assistant launcher', desc: 'The floating Docusign-Assistant chat pill; measured, never opened.', sel: '"Docusign Assistant"' });
  save();
}

async function esignature() {
  if (!(await newPage('esignature', { wait: 9000 }))) return;
  await sheetsFor('esignature');
  await chrome('esignature');
  const g = G.esig;
  await S('e-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'eSignature title', desc: 'The product page display heading.', sel: 'h1 on /products/electronic-signature' }, { noScroll: true });
  await S('e-cta', q('button, a').filter({ hasText: /^\s*(Get Started|Try for Free|Free Trial)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'eSignature CTA', desc: 'A plan/trial call to action; measured never followed.', sel: 'page CTA' });
  await S('video-expand', q('button[aria-label*="Expand Customer Story Video" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Video expand button', desc: 'An expand-video icon button on a customer-story tile; one was pressed to open the dialog below.', sel: 'button[aria-label="Expand Customer Story Video"]' });
  // Open a customer-story video dialog (its own expand button; Escape closes)
  // and measure the painted dialog and scrim.
  try {
    const v = q('button[aria-label*="Expand Customer Story Video" i]').filter({ visible: true }).first();
    if (await v.count()) { await v.click({ timeout: 5000 }).catch(() => v.evaluate((el) => el.click())); await page.waitForTimeout(2500); }
  } catch (e) { log('  ! video dialog failed', String(e.message).split('\n')[0]); }
  await S('video-dialog', q('[data-cy="modal_scrim"], [role="dialog"], [class*="modal" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Video dialog', desc: 'The modal a video Expand button opens (scrim + framed player); opened and closed with the product\'s own controls.', sel: 'dialog / modal_scrim' }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(600);
  const x = q('button, [role="button"]').filter({ hasText: /close|dismiss/i }).filter({ visible: true }).first();
  if (await x.count()) await x.click().catch(() => {});
  await S('faq-button', q('button').filter({ hasText: /Is eSignature built for|Does eSignature integrate|eSignature easy/i }).filter({ visible: true }).first(), B4, { group: g, title: 'FAQ row', desc: 'A collapsed FAQ accordion row in the page footer; toggled open once for the panel below.', sel: 'FAQ accordion button' });
  try {
    const f = q('button').filter({ hasText: /Is eSignature built for/i }).filter({ visible: true }).first();
    if (await f.count()) { await f.click({ timeout: 5000 }).catch(() => f.evaluate((el) => el.click())); await page.waitForTimeout(900); }
  } catch (e) { log('  ! faq open failed', String(e.message).split('\n')[0]); }
  await S('faq-open', q('button[aria-expanded="true"], button').filter({ hasText: /Is eSignature built for/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ row, open', desc: 'The same accordion row after its own toggle (aria-expanded).', sel: 'FAQ button open' });
  await S('faq-panel', q('[role="region"], div').filter({ hasText: /eSignature is built for|built for high-volume/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'FAQ panel', desc: 'The answer text revealed under an open FAQ row.', sel: 'FAQ answer region' });
  save();
}

async function trial() {
  if (!(await newPage('trial', { wait: 9000 }))) return;
  await sheetsFor('trial');
  await chrome('trial');
  const g = G.trial;
  const card = await markPainted('input, h1', 'm-trial', { minW: 250, minH: 200 }).catch(() => null);
  await S('trial-card', (card && (await card.count())) ? card : q('input').filter({ visible: true }).first().locator('xpath=ancestor::section[1]'), ['default'], { group: g, title: 'Trial form band', desc: 'The painted free-trial form band; never submitted.', sel: 'trial form section' });
  await S('trial-field', q('input[name="workEmail"], input[type="email"], input[type="text"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Work-email field', desc: 'The work-email input; sample text was typed and deleted, nothing sent.', sel: 'input[name=workEmail]' }, { fillText: 'alex@example.com' });
  await S('trial-checkbox', q('input[type="checkbox"]').filter({ visible: true }).first().locator('xpath=..'), B4, { group: g, title: 'Consent checkbox', desc: 'The painted square of the opt-in marketing checkbox (the real input is a 1x1 inside it); measured, never toggled.', sel: 'trial checkbox painted square' });
  await S('trial-cta', q('button').filter({ hasText: /^\s*Get Started\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Trial submit', desc: 'The Get-Started submit button; measured, never pressed (a press submits the form).', sel: 'button "Get Started"' });
  await S('help-button', q('button').filter({ hasText: /^\s*Help\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Help button', desc: 'The floating Help launcher; measured, never opened.', sel: 'button "Help"' });
  save();
}

async function signgen() {
  if (!(await newPage('signgen', { wait: 9000 }))) return;
  await sheetsFor('signgen');
  await chrome('signgen');
  const g = G.signgen;
  await S('sg-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Generator title', desc: 'The signature-generator display heading.', sel: 'h1 on /signature-generator' }, { noScroll: true });
  await S('sg-tab-draw', q('button').filter({ hasText: /^\s*Draw\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Draw tab', desc: 'The Draw half of the Draw/Type mode toggle.', sel: 'button "Draw"' });
  await S('sg-tab-type', q('button').filter({ hasText: /^\s*Type\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Type tab', desc: 'The Type half of the mode toggle; its own click revealed the name field below.', sel: 'button "Type"' });
  await S('sg-canvas', q('canvas, [class*="canvas" i], [class*="signature" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Signature canvas', desc: 'The signature preview surface in Draw mode.', sel: 'signature canvas' });
  await S('sg-color', page.getByRole('button', { name: /^\s*Cobalt\s*$/i }), B4, { group: g, title: 'Colour swatch', desc: 'A signature colour swatch button (Cobalt), read at rest, hovered, focused and pressed; never selected here.', sel: 'button "Cobalt"' }, { open: async () => { const d = q('button').filter({ hasText: /^\s*Draw\s*$/ }).filter({ visible: true }).first(); if (await d.count()) { await d.click().catch(() => d.evaluate((el) => el.click())); await page.waitForTimeout(500); } } });
  await S('sg-clear', q('button').filter({ hasText: /^\s*Clear\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Clear button', desc: 'The Clear action on the draw canvas.', sel: 'button "Clear"' });
  await S('sg-download', q('button').filter({ hasText: /Download as PNG/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Download button', desc: 'The Download-as-PNG action; measured, never pressed (a press downloads a file).', sel: 'button "Download as PNG"' });
  // Type mode: the tab's own click reveals the name field and the script-face
  // picker; a sample name is typed and left in the field (local only).
  try {
    const t = q('button').filter({ hasText: /^\s*Type\s*$/ }).filter({ visible: true }).first();
    if (await t.count()) { await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click())); await page.waitForTimeout(1200); }
    const f = q('input#signature-name').first();
    if (await f.count()) { await f.click(); await page.keyboard.type('Alex Sample', { delay: 20 }); await page.waitForTimeout(1200); }
  } catch (e) { log('  ! type mode failed', String(e.message).split('\n')[0]); }
  await S('sg-field', q('input#signature-name').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Name field', desc: 'The "Your name" input in Type mode; a sample name (Alex Sample) was typed to render the script previews, nothing sent.', sel: 'input#signature-name' });
  await S('sg-font', q('button').filter({ hasText: /The Curator|The Letter Writer|The Overachiever/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Script-face option', desc: 'A signature script-face picker option (The Curator et al.); toggled, which re-renders the preview.', sel: 'script face option' });
  save();
}

async function stories() {
  if (!(await newPage('stories', { wait: 9000 }))) return;
  await sheetsFor('stories');
  await chrome('stories');
  const g = G.stories;
  await S('st-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Stories title', desc: 'The customer-stories page heading.', sel: 'h1 on /customer-stories' }, { noScroll: true });
  await S('filter-button', q('button, [role="button"], [role="combobox"]').filter({ hasText: /^\s*(Products used|Industry|Department)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Filter dropdown', desc: 'A stories filter dropdown trigger (Products used/Industry/Department); measured, never opened.', sel: 'stories filter button' }, { noScroll: true });
  const storyMark = await domFind(page, /customer story|read the|case study|learn more/i, { sel: 'a, article, [class*="card" i]', tag: 'm-story', up: 'article, [class*="card" i]', minW: 200, minH: 120 }).catch(() => null);
  await S('story-card', (storyMark && (await storyMark.count())) ? storyMark : q('a[href*="/customer-stories/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Story card', desc: 'A customer-story card link; measured never followed.', sel: 'story card link' });
  await S('story-logo', q('img[alt]').filter({ visible: true }).nth(2), ['default'], { group: g, title: 'Story logo', desc: 'A customer logo tile on the stories page.', sel: 'story logo img' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 11000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('ec-header', q('header, nav, [class*="header" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Storefront header', desc: 'The ecom storefront chrome (its own header, Log In).', sel: 'ecom header' }, { noScroll: true });
  await S('ec-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The storefront page heading.', sel: 'h1 on ecom pricing' }, { noScroll: true });
  await S('ec-billing-annual', q('button').filter({ hasText: /^\s*Annual\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Annual toggle', desc: 'The Annual half of the billing-period toggle.', sel: 'button "Annual"' }, { noScroll: true });
  await S('ec-billing-monthly', q('button').filter({ hasText: /^\s*Monthly\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Monthly toggle', desc: 'The Monthly half of the billing toggle, read unselected; the monthly screenshot comes from the screenshot pass.', sel: 'button "Monthly"' }, { noScroll: true });
  await S('plan-name', q('h2, h3, [class*="title" i], [class*="name" i]').filter({ hasText: /^\s*(Personal|Standard|Business Pro|Enhanced|Enterprise)\s*$/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan name', desc: 'A plan card\'s name.', sel: 'plan name' });
  await S('plan-price', q('span, div, p').filter({ hasText: /^(US\$|\$|S\$|SGD)\s*\d+/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'A plan card\'s price figure (SGD on the /en-SG/ route).', sel: 'plan price' });
  const planCard = await markPainted('a[class], button', 'm-plan', { minW: 200, minH: 300, maxUp: 10 }).catch(() => null);
  await S('plan-card', (planCard && (await planCard.count())) ? planCard : q('a, button').filter({ hasText: /^\s*Buy now\s*$/i }).filter({ visible: true }).first().locator('xpath=ancestor::section[1]'), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (the painted section ancestor of a Buy-now action).', sel: 'plan card section' });
  await S('buy-now', q('a, button').filter({ hasText: /^\s*Buy Now\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Buy-now CTA', desc: 'A plan\'s Buy-Now action; measured never followed.', sel: '"Buy Now"' });
  await S('contact-sales', q('a, button').filter({ hasText: /^\s*Contact Sales\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Contact-sales CTA', desc: 'The enterprise plan\'s Contact-Sales action; measured never followed.', sel: '"Contact Sales"' });
  await S('feature-row', q('button').filter({ hasText: /Send \d+ envelopes|Securely store|reusable templates/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Feature row', desc: 'An expandable feature row on a plan card, read at rest, hovered, focused and pressed; never expanded here.', sel: 'feature accordion row' });
  await S('see-all', q('button, a').filter({ hasText: /See All Features/i }).filter({ visible: true }).first(), B4, { group: g, title: 'See-all-features', desc: 'The See-All-Features expander; measured, never expanded.', sel: '"See All Features"' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 9000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.auth;
  const card = await markPainted('input[type="email"], input[name="email"], h1', 'm-login', { minW: 250, minH: 200 }).catch(() => null);
  await S('auth-card', (card && (await card.count())) ? card : q('main, form, section, [class*="card" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login card', desc: 'The centred OAuth login card on account.docusign.com; never filled or submitted.', sel: 'login card' });
  await S('auth-field', q('input[type="email"], input[name="email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The Enter-email input; sample text was typed and deleted, nothing sent.', sel: 'input[type=email]' }, { fillText: 'alex@example.com' });
  await S('auth-next', q('button').filter({ hasText: /^\s*Next\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Next button', desc: 'The Next submit; measured, never pressed (a press continues sign-in).', sel: 'button "Next"' });
  await S('auth-lang', q('button').filter({ hasText: /English \(US\)|English/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Language picker', desc: 'The English-(US) language menu trigger; measured, never opened.', sel: 'language button' });
  await S('auth-signup', q('a').filter({ hasText: /Sign Up for Free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Signup link', desc: 'The Sign-Up-for-Free link under the card; measured never followed.', sel: '"Sign Up for Free"' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1800);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The marketing footer: link columns, locale selector, legal and social.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('locale-button', q('footer button').filter({ hasText: /United States|Show more locales/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Locale button', desc: 'The United-States locale menu trigger; measured, never opened.', sel: 'footer locale button' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('nav[data-cy="navbar"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'navbar at 390' }, { noScroll: true });
  const menu = q('[data-cy="mobilenavhamburgermenu"] button, button[data-cy="mobilenavhamburgermenu"]').filter({ visible: true }).first();
  const menuBtn = (await menu.count()) ? menu : q('nav[data-cy="navbar"] button').filter({ visible: true }).last();
  await S('m-menu-button', menuBtn, B4, { group: g, title: 'Menu button', desc: 'The header hamburger toggle.', sel: 'hamburger' }, { noScroll: true });
  try {
    if (await menuBtn.count()) { await menuBtn.click({ timeout: 5000 }).catch(() => menuBtn.evaluate((el) => el.click())); await page.waitForTimeout(1500); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await S('m-menu-open', q('[data-cy="dropdown"], [role="dialog"], [class*="menu" i], nav').filter({ hasText: /Products|Solutions/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The header menu opened by its own toggle.', sel: 'mobile menu panel' }, { noScroll: true, noReset: true });
  await S('m-nav-item', q('[role="dialog"] a, [role="dialog"] button, nav a, nav button, body a, body button').filter({ hasText: /^\s*(Products|Solutions|Resources|Plans & Pricing)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'An item inside the opened header menu.', sel: 'mobile menu item' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  await S('m-cta', q('button, a').filter({ hasText: /^\s*(Get Started|TRY FOR FREE|Try for Free)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile CTA', desc: 'The hero call to action at phone width.', sel: 'mobile hero CTA' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every captured surface paints light — the #26065d hero/footer bands are painted sections, not a theme; the ecom storefront geo-redirected to /en-SG/ and is captured as served';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, esignature, trial, signgen, stories, pricing, login, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (the sticky chrome), so
  // the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'nav[data-cy="navbar"]');
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
