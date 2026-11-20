// Measures care.com's public components in every state reachable without
// signing in, joining, booking or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home childcare listing login join pricing footer mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// care.com is a Next.js app over an MUI component layer (CareHeaderContainer,
// MegaMenu, MuiButtonBase/MuiPaper/CareTag/MuiTypography classes). The public
// surface includes the /babysitters provider listing — real caregivers' first
// names, photos and bios, which the repo's privacy policy allows (no contact
// details appear on it). DataDome gates the edge, so ONE context per viewport
// stays alive for the whole run and navigations are paced (PACE env). Nothing
// is sent, bought or signed into: the only presses are local UI toggles — the
// "Find care" mega-menu trigger, the mobile menu, a listing FAQ question and
// the fields' own focus. The cookie banner and the "Join Care.com" signup-gate
// modal are hidden after their own measurement, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', childcare: '/child-care', listing: '/babysitters', login: '/vis/auth/login', join: '/app/vhp/get-started', pricing: '/app/vhp/plans-and-pricing', safety: '/about/safety/' };
let page, cdp, current, context, run;
const ctxs = {};
const touched = new Set();
const listed = new Map();
// Routes blocked this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();
const PACE = +(process.env.PACE || 20000); // ms between routes; DataDome rate-limits

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /challenge validation|confirm you are a person|performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access/i.test(t)
      || /challenge validation/i.test(document.title)
      || t.trim().length < 40;
  }).catch(() => true);
}

// One context per viewport class, reused for every route so the DataDome
// clearance cookie carries across navigations; routes are paced by PACE.
async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null } = {}) {
  current = key;
  const cls = mobile ? 'm' : 'd';
  const b = context.browser();
  if (!ctxs[cls]) {
    const ctx = ctxs[cls] = await b.newContext(mobile
      ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
      : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
    await patch(ctx);
  }
  page = await ctxs[cls].newPage();
  cdp = await ctxs[cls].newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, url || BASE + URLS[key], { wait, promo });
  if (await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return true;
}

async function endPage() { await page.close().catch(() => {}); await new Promise((r) => setTimeout(r, PACE)); }

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
    ok = await loc.evaluate((el) => el === document.activeElement);
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
  Object.assign(c, { page: current, run, url: URLS[current] && BASE + URLS[current] }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

async function measure(key, state, target, opts = {}) {
  const loc = target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let shot;
    if (opts.crop !== false) {
      try {
        shot = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: shot?.file, cropScale: shot?.scale, cropPixels: shot?.pixels, via: opts.via };
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
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|join now|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|search|find|book|hire|contact|post a job|sign up|upgrade)$/i;
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

// The "Find care" header trigger opens the mega menu. Click is a local UI
// toggle — the panel stays painted while it is read and cropped.
async function openMegaMenu() {
  const t = q('header button').filter({ hasText: /^\s*Find care/ }).filter({ visible: true }).first();
  if (!(await t.count())) return false;
  await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click()));
  await page.waitForTimeout(1200);
  return true;
}

// The listing pages mount a "Join Care.com" signup-gate dialog over the
// results. It is a real painted surface: measured open first, then hidden
// (never answered) so the results behind it can be read.
async function hideGate() {
  await page.evaluate(() => {
    document.querySelectorAll('.MuiModal-root, .MuiDialog-root, [role="dialog"]').forEach((x) => {
      const t = x.innerText || '';
      if (/join care\.com|sign up to|create (a|your) (free )?account/i.test(t) && !/use cookies/i.test(t)) {
        x.style.setProperty('display', 'none', 'important');
      }
    });
    document.querySelectorAll('.MuiBackdrop-root').forEach((x) => x.style.setProperty('display', 'none', 'important'));
    document.body && document.body.style.removeProperty('overflow');
  }).catch(() => {});
}

const G = {
  shell: 'Shell and navigation', home: 'Home', childcare: 'Category page',
  listing: 'Provider listing', login: 'Login page', join: 'Join page',
  pricing: 'Pricing', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('header[class*="CareHeaderContainer"], header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The fixed header: wordmark, the Find care / Find jobs / List your business / Resources mega-menu triggers, Log in and the Join-now pill.', sel: 'header.CareHeaderContainer-root' }, { noScroll: true });
  await S('logo', q('header a[href="https://www.care.com"], header a[href="/"], header a:has(svg)').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Care.com wordmark anchor.', sel: 'header logo a' }, { noScroll: true });
  await S('nav-trigger', q('header button').filter({ hasText: /^\s*Find care/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The "Find care" button that opens the mega menu; toggled, never followed.', sel: 'header button Find care' }, { noScroll: true });
  await S('login-link', q('header a').filter({ hasText: /^\s*Log in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log-in link', desc: 'The header Log-in action; measured, never followed.', sel: 'header a Log in' }, { noScroll: true });
  await S('join-cta', q('header a, header button').filter({ hasText: /^\s*Join now\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Join CTA', desc: 'The green Join-now header action; measured, never followed.', sel: 'header Join now' }, { noScroll: true });
  try { await openMegaMenu(); } catch (e) { log('  ! mega menu failed', String(e.message).split('\n')[0]); }
  await S('nav-dropdown', q('nav[class*="MegaMenu" i], [class*="MegaMenu" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mega menu', desc: 'The Find-care mega menu panel, opened by its own trigger.', sel: 'nav.MegaMenu--root' }, { noScroll: true, noReset: true });
  await S('menu-item', q('[class*="MegaMenu" i] button, .MegaMenu--item').filter({ visible: true }).first(), B4, { group: g, title: 'Mega-menu tab', desc: 'A category tab inside the mega menu (Child care active by default).', sel: 'button.MegaMenu--item' }, { noScroll: true, noReset: true });
  await S('menu-link', q('[class*="NavLinkList" i] a, [class*="MegaMenu" i] a').filter({ hasText: /Babysitters|Nannies|Child care/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A link inside the opened mega menu.', sel: 'mega menu a' }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  const h = G.home;
  // The hero headline is an h1 some loads and mounts late on others: mark
  // the biggest display-size text in the top fold instead of guessing a tag.
  await page.evaluate(() => {
    let best = null;
    document.querySelectorAll('h1,h2,p,span,div').forEach((x) => {
      const r = x.getBoundingClientRect();
      const fs = parseFloat(getComputedStyle(x).fontSize);
      if (r.top < 550 && r.top > -50 && fs >= 40 && (x.innerText || '').trim().length > 10 && (!best || fs > best.fs)) best = { el: x, fs };
    });
    if (best) best.el.setAttribute('data-m-mark', 'hero');
  });
  await S('hero-title', q('[data-m-mark="hero"]'), ['default'], { group: h, title: 'Hero headline', desc: 'The hero display headline over the photo ("Connecting families with quality, local caregivers"); the testimonial-name accentHeadline1 h1s are excluded.', sel: 'largest display text in the hero fold' }, { noScroll: true });
  await S('zip-field', q('input[placeholder*="ZIP" i], input[placeholder*="zip" i]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: h, title: 'ZIP field', desc: 'The hero ZIP-code search input; focused and given a sample ZIP that was deleted again — never searched.', sel: 'input[placeholder=ZIP code]' }, { fillText: '90210' });
  await S('search-cta', q('button.MuiButton-contained, button').filter({ hasText: /^\s*Search\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Search CTA', desc: 'The green Search action under the ZIP field; measured, never pressed.', sel: 'button.MuiButton-contained Search' }, { noScroll: true });
  await S('category-card', q('a.MuiLink-root').filter({ hasText: /^\s*Child care\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Category card', desc: 'A "One membership" category card (Child care, Senior care, Pet care ...); measured, never followed.', sel: 'a.MuiLink-root category card' });
  await S('section-h2', q('h2, [class*="display2" i]').filter({ hasText: /membership|season|stress|families/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A section display heading ("One membership for every season of life").', sel: 'h2.display2' });
  save();
  await endPage();
}

async function childcare() {
  if (!(await newPage('childcare', { wait: 9000 }))) return;
  await sheetsFor('childcare');
  const g = G.childcare;
  await S('cat-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Category title', desc: 'The category page display title ("Find child care on your terms").', sel: 'h1' }, { noScroll: true });
  await S('service-card', q('.MuiPaper-root[class*="elevation" i], .MuiPaper-root').filter({ hasText: /Nannies|Babysitters|Daycares/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Service card', desc: 'A service-card panel (Nannies / Babysitters / Daycares ...) in the services grid.', sel: '.MuiPaper-root service card' });
  await S('service-cta', q('.MuiCardActions-root a, .MuiCardActions-root button').filter({ hasText: /Find/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Service CTA', desc: 'A card action ("Find babysitters"); measured, never followed.', sel: 'service card action' });
  await S('review-card', q('.MuiCard-root').filter({ hasText: /“|"/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Testimonial card', desc: 'A member-quote card ("Trusted by families like yours").', sel: 'testimonial .MuiCard-root' });
  await S('cat-faq', q('.MuiAccordion-root button, .MuiAccordionSummary-root, button').filter({ hasText: /\?\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'FAQ question', desc: 'A question row in the category FAQ block; measured closed.', sel: 'FAQ accordion row' });
  save();
  await endPage();
}

async function listing() {
  if (!(await newPage('listing', { wait: 11000 }))) return;
  await sheetsFor('listing');
  await chrome('listing');
  const g = G.listing;
  await S('listing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Listing title', desc: 'The listing display title ("Find Local Babysitters").', sel: 'h1' }, { noScroll: true });
  await S('city-button', q('button').filter({ hasText: /City,?\s*State/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Location button', desc: 'The outlined "City, State" location trigger on the listing toolbar; measured, never opened.', sel: 'button.MuiButton-outlined City State' });
  await S('filter-button', q('button').filter({ hasText: /^\s*Filter\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Filter button', desc: 'The outlined Filter action on the listing toolbar; measured, never opened.', sel: 'button.MuiButton-outlined Filter' });
  // The signup gate mounts on scroll: scroll to wake it, measure it open,
  // then hide it (never answered) so the cards behind it read clean.
  // The gate mounts on real scroll engagement: wheel down in steps (real
  // input events, not scrollTo) then poll for the dialog up to ~40s. It is
  // frequency-capped server-side, so a run where it stays absent records
  // the dialog missing rather than fabricating one.
  await page.mouse.move(720, 450);
  for (let i = 0; i < 14; i++) { await page.mouse.wheel(0, 700); await page.waitForTimeout(700); }
  await page.waitForSelector('.MuiDialog-root .MuiPaper-root, [role="dialog"].MuiPaper-root', { timeout: 30000 }).catch(() => {});
  await page.waitForTimeout(800);
  await S('gate-dialog', q('.MuiDialog-root .MuiPaper-root, .MuiModal-root .MuiPaper-root, [role="dialog"]').filter({ hasText: /Join Care\.com/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup-gate dialog', desc: 'The "Join Care.com" modal the listing mounts over the results once they are scrolled to: measured open, then hidden, never answered or submitted.', sel: 'join gate dialog' }, { noScroll: true });
  await S('gate-cta', q('.MuiDialog-root a, .MuiDialog-root button, [role="dialog"] a, [role="dialog"] button').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Gate CTA', desc: 'The gate dialog\'s primary action; measured, never pressed.', sel: 'gate dialog action' }, { noScroll: true });
  await hideGate();
  await page.evaluate(() => scrollTo(0, 0));
  await page.waitForTimeout(800);
  // The provider row is a MUI Grid, not a Paper card: mark the smallest
  // ancestor of the first name h2 that holds the whole row (photo + body).
  await page.evaluate(() => {
    const h = [...document.querySelectorAll('h2.MuiTypography-h2')].find((x) => x.closest('a') || /^[A-Z][a-z]+ [A-Z]\./.test(x.innerText || ''));
    if (!h) return;
    let n = h.parentElement, best = null;
    while (n && n !== document.body) {
      const r = n.getBoundingClientRect();
      if (r.height >= 140 && r.height <= 460 && r.width >= 500) { best = n; break; }
      n = n.parentElement;
    }
    (best || h.closest('a') || h).setAttribute('data-m-mark', 'prov');
  });
  await S('provider-card', q('[data-m-mark="prov"]'), B4, { group: g, title: 'Provider card', desc: 'A caregiver listing row (first name + initial, photo, rate, tags, review count) — a real person\'s public profile summary; structure only, measured, never followed.', sel: 'provider grid row' });
  await S('care-tag', q('[class*="CareTag" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Care tag', desc: 'A service chip on the provider card (light cleaning, meal prep, travel ...).', sel: '.CareTag chip' });
  await S('read-more', q('button, a').filter({ hasText: /^\s*read more\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Read-more link', desc: 'The bio expander on a provider card.', sel: 'button read more' });
  await S('pagination', q('nav[class*="Pagination" i], .MuiPagination-root').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pagination', desc: 'The results pager (1 2 3 4 5 ... N).', sel: 'nav.MuiPagination-root' });
  await S('page-item', q('.MuiPaginationItem-root, nav[class*="Pagination" i] a, nav[class*="Pagination" i] button').filter({ hasText: /^\s*2\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Page item', desc: 'A page-number item in the pager.', sel: '.MuiPaginationItem-root 2' });
  await S('learn-more', q('button.MuiButton-text, a').filter({ hasText: /^\s*Learn more\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Learn-more link', desc: 'A text-button link on the listing page.', sel: 'button.MuiButton-text Learn more' });
  await S('list-faq', q('.MuiAccordion-root button, .MuiAccordionSummary-root, button, summary').filter({ hasText: /\?\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'FAQ question', desc: 'A question row in the "FAQs for finding a babysitter" block; measured closed.', sel: 'listing FAQ row' });
  save();
  await endPage();
}

// Marks the login card (the smallest ancestor of the email input that holds
// the whole form) so it can be located and cropped without a class-name guess.
// Marks the login card (the smallest ancestor of the form-control input that
// holds the Continue button) so it can be located and cropped without a
// class-name guess.
async function markLogin() {
  await page.evaluate(() => {
    const inp = [...document.querySelectorAll('input.form-control, input[type="email"], input[name="email"]')].find((x) => x.getBoundingClientRect().width > 100);
    if (!inp) return;
    const vw = innerWidth, vh = innerHeight;
    let n = inp.parentElement;
    while (n && n !== document.body) {
      const r = n.getBoundingClientRect();
      if (r.width > 280 && r.height > 150 && r.width < vw * 0.9 && r.height < vh * 0.98) {
        const hasBtn = [...n.querySelectorAll('button, [role="button"], input[type="submit"], a')].some((x) => /log ?in|sign ?in|continue/i.test(x.innerText || x.value || ''));
        if (hasBtn) { n.setAttribute('data-m-mark', 'dlg'); return; }
      }
      n = n.parentElement;
    }
  });
}

async function login() {
  if (!(await newPage('login', { wait: 10000 }))) return;
  await sheetsFor('login');
  const g = G.login;
  await markLogin();
  await S('login-card', q('[data-m-mark="dlg"]'), ['default'], { group: g, title: 'Login card', desc: 'The sign-in card on /vis/auth/login (redirects to /vis/lcp/login, a legacy form — not the MUI layer): captured as a boundary surface, never filled or submitted.', sel: 'login form card' }, { noScroll: true });
  await S('login-email', q('input.form-control, input[type="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Email field', desc: 'The login email input (input.form-control); focused only, never typed into. The password step sits behind Continue, never reached.', sel: 'input.form-control' });
  await S('login-button', q('button, input[type="submit"]').filter({ hasText: /^\s*(Log ?in|Sign ?in|Continue)\s*$/i }).filter({ visible: true }).last(), B4, { group: g, title: 'Login button', desc: 'The Continue action; measured, never pressed — the password step and the account sit behind it.', sel: 'button.btn-primary-2 Continue' });
  await S('passwordless-link', q('a, button').filter({ hasText: /without a password|forgot/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Passwordless link', desc: 'The "Log in without a password" link; measured, never followed.', sel: 'passwordless link' });
  save();
  await endPage();
}

async function join() {
  if (!(await newPage('join', { wait: 10000 }))) return;
  await sheetsFor('join');
  const g = G.join;
  await S('join-card', q('.MuiPaper-root').filter({ hasText: /I need a caregiver|I want a care job/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Join card', desc: 'A chooser card on /app/vhp/get-started ("I need a caregiver" / "I want a care job"); captured as a boundary, never followed.', sel: 'get-started .MuiPaper-root' }, { noScroll: true });
  await S('join-option', q('.MuiPaper-root button, .MuiPaper-root a').filter({ hasText: /^\s*(Find care|Find jobs)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Join option', desc: 'The Find-care/Find-jobs action inside a chooser card; measured, never pressed.', sel: 'chooser card button' });
  save();
  await endPage();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 10000 }))) return;
  await sheetsFor('pricing');
  const g = G.pricing;
  await S('pricing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The "Flexible plans that fit your life" title.', sel: 'h1' }, { noScroll: true });
  // The plan column is not a MuiPaper card: mark the smallest ancestor of
  // the "Premium monthly" heading that holds a whole column.
  await page.evaluate(() => {
    const h = [...document.querySelectorAll('h1,h2,h3')].find((x) => /^\s*Premium\s+(monthly|quarterly|annual)/i.test(x.innerText || ''));
    if (!h) return;
    let n = h.parentElement, best = null;
    while (n && n !== document.body) {
      const r = n.getBoundingClientRect();
      if (r.height >= 200 && r.height <= 800 && r.width <= 620) { best = n; break; }
      n = n.parentElement;
    }
    (best || h.parentElement || h).setAttribute('data-m-mark', 'plan');
  });
  await S('plan-card', q('[data-m-mark="plan"]'), ['default'], { group: g, title: 'Plan card', desc: 'A Premium plan column (monthly/quarterly/annual); measured, never checked out.', sel: 'premium plan column' });
  await S('plan-price', q('h2, h3, [class*="price" i]').filter({ hasText: /^\s*\$[\d.]+\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'A plan price figure ($39.99 monthly / $25.99 quarterly / $13.99 annual).', sel: 'plan price h2' });
  await S('plan-cta', q('button.MuiButton-contained, button').filter({ hasText: /^\s*(Get started|Join now)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan Get-started action; measured, never pressed.', sel: 'button.MuiButton-contained Get started' });
  await S('plan-alt', q('button.MuiButton-outlined, a.MuiButton-outlined').filter({ hasText: /Why join|See senior care/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan alt', desc: 'An outlined secondary action (Why join?); measured, never pressed.', sel: 'button.MuiButton-outlined' });
  await S('addon-card', q('.MuiPaper-contrast').filter({ hasText: /\$[\d.]+|Price varies/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Add-on card', desc: 'An add-on product card (Feature your job post, Social Media Check, Hiring Helper).', sel: '.MuiPaper-contrast add-on' });
  await S('pricing-faq', q('.MuiAccordionSummary-root, .MuiAccordion-root').filter({ hasText: /\?/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Pricing FAQ', desc: 'A billing FAQ row (How do I pay the caregiver once hired?); measured closed.', sel: 'pricing FAQ accordion' });
  save();
  await endPage();
}

async function footer() {
  if (!(await newPage('home', { wait: 7000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer[class*="GlobalFooter" i], footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The inverse (dark) GlobalFooter: link columns, legal and the social row.', sel: 'footer.GlobalFooter' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('social-icon', q('footer a[href*="facebook"], footer a[href*="instagram"], footer a[href*="linkedin"], footer a[href*="twitter"], footer a[href*="x.com"], footer a[aria-label]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A social link/icon in the footer.', sel: 'footer social a' }, { noScroll: true });
  save();
  await endPage();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('header button[aria-label="Open menu"], header [class*="TouchMenuButton" i]').filter({ visible: true }).first();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The "Open menu" touch toggle at phone width.', sel: 'button[aria-label=Open menu]' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1800); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await hideGate();
  await S('m-menu-open', q('[class*="CareMobileDrawer" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The CareMobileDrawer panel opened by the header toggle at 390 (full-screen).', sel: 'div.CareMobileDrawer--root' }, { noScroll: true });
  await S('m-nav-item', q('[class*="CareMobileDrawer" i] a, [class*="CareMobileDrawer" i] button').filter({ hasText: /Child care|Find care|Log in|Join|Find jobs/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A link inside the opened mobile drawer.', sel: 'CareMobileDrawer a' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(600);
  await page.evaluate(() => {
    let best = null;
    document.querySelectorAll('h1,h2,p,span,div').forEach((x) => {
      const r = x.getBoundingClientRect();
      const fs = parseFloat(getComputedStyle(x).fontSize);
      if (r.top < 550 && r.top > -50 && fs >= 28 && (x.innerText || '').trim().length > 10 && (!best || fs > best.fs)) best = { el: x, fs };
    });
    if (best) best.el.setAttribute('data-m-mark', 'mhero');
  });
  await S('m-hero', q('[data-m-mark="mhero"]'), ['default'], { group: g, title: 'Mobile headline', sel: 'largest display text in the hero fold at 390' });
  save();
  await endPage();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the public surface paints light throughout';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, childcare, listing, login, join, pricing, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header button');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only when its page was not blocked this
    // run: an edge-blocked route keeps its earlier readings under their
    // original provenance instead of being erased and republished.
    // Never prune in a run that measured nothing: a fully edge-blocked pass
    // must leave every earlier reading untouched.
    if (!touched.has(key) && !pages.length && !failedPages.has(c.page) && touched.size) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
