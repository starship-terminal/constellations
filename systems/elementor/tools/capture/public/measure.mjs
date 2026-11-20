// Measures elementor.com's public components in every state reachable without
// signing in, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing contact faq mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// elementor.com is a WordPress site built with Elementor: an Elementor header
// template (nav.e-n-menu mega-menu), dsm-* components on a :root token layer
// (--Kernel-Black, --Grey-*, --Neon-Loop, --s*/--sm*/--md*/--lg* spacing) and
// .dark-mode islands that re-bind the same vars. Nothing is sent, bought or
// signed into: the only presses are local UI toggles — the Products mega-menu
// trigger, an FAQ accordion header, the mobile menu and the acceptance
// checkbox (checked, then unchecked again; nothing submitted). The Cookiebot dialog,
// the accessibility launcher and the Angie FAB are hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing/', contact: '/contact/', faq: '/faq/' };
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
  const cleared = await open(page, url || BASE + URLS[key], { wait, promo });  // false: the bot check did not clear (lib.mjs)
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
  out._meta.page ??= {};
  out._meta.page[key] = await page.evaluate(() => ({
    html: getComputedStyle(document.documentElement).backgroundColor,
    body: getComputedStyle(document.body).backgroundColor,
    bodyColor: getComputedStyle(document.body).color,
  })).catch(() => null);
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
        const h = (opts.hoverLoc || loc).filter({ visible: true }).first();
        await h.hover({ timeout: 5000 }).catch(async () => {
          // The header pill auto-hides when an auto-scroll nudges the page;
          // return to the top and try again before forcing.
          await page.evaluate(() => scrollTo(0, 0));
          await page.waitForTimeout(900);
          await h.hover({ timeout: 5000 }).catch(() => h.hover({ timeout: 5000, force: true }));
        });
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
      if (via === 'focus failed') {
        // A keyboard focus that never landed is not a measurement: record the
        // failure as the state instead of publishing at-rest styles under a
        // focus label (the generated docs must not count it as a captured
        // focus-visible).
        out.components[key].states[st] = { via, error: 'keyboard focus could not be landed on the target' };
        log('  !', key, st, 'focus failed');
      } else {
        await measure(key, st, loc, { ...opts, via });
      }
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, accordion, checkbox). Refuses a submit
// button and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|buy now|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|continue|claim this offer|try again|next|confirm|schedule event|i understand|decline)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// The native checkbox input is measured as the toggle target, but on
// elementor.com it paints at opacity 0 — the box a user sees is the sibling
// label's ::before. Record that visible box (and the real checked flag, so a
// published `selected` spec is verified) into each state's `extra`.
async function checkboxExtra(input) {
  return input.evaluate((el) => {
    // url() values can be signed URLs: record them as url(…), keeping data:
    // and #fragment references (the same noUrl styleOf uses; each browser
    // callback needs its own copy — it runs in the page, not this module).
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
    const lab = (el.id && document.querySelector(`label[for="${el.id}"]`)) || (el.parentElement && el.parentElement.querySelector('label')) || el.nextElementSibling;
    const out = { checked: el.checked };
    if (!lab) return out;
    const b = getComputedStyle(lab, '::before');
    const bw = ['Top', 'Right', 'Bottom', 'Left'].map((sd) => parseFloat(b[`border${sd}Width`]) > 0 && b[`border${sd}Style`] !== 'none' ? `${b[`border${sd}Width`]} ${b[`border${sd}Style`]} ${b[`border${sd}Color`]}` : '').filter(Boolean);
    const bgi = noUrl(b.backgroundImage);
    out.box = {
      node: 'label::before',
      size: `${b.width} x ${b.height}`,
      backgroundColor: b.backgroundColor,
      backgroundImage: bgi === 'none' ? 'none' : (bgi.includes('svg') ? 'check glyph (data-URI svg)' : bgi.slice(0, 120)),
      border: bw.join(' | ') || 'none',
      radius: b.borderRadius,
      position: `${b.position} ${b.top} ${b.left}`,
      color: b.color,
    };
    return out;
  }).catch(() => null);
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

// Marks the first painted descendant of rootSel matching the size bounds —
// for containers whose own box is 0-height (the fixed header pill is a
// descendant of a 0-height <header>) or that paint nothing themselves.
async function paintChild(rootSel, tag, { minW = 0, maxW = 99999, minH = 0, maxH = 99999, nth = 0 } = {}) {
  const ok = await page.evaluate(([s, t, w0, w1, h0, h1, i]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const root = document.querySelector(s);
    if (!root) return false;
    const els = [...root.querySelectorAll('*')].filter((n) => {
      const r = n.getBoundingClientRect();
      const cs = getComputedStyle(n);
      return r.width >= w0 && r.width <= w1 && r.height >= h0 && r.height <= h1
        && (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none' || cs.boxShadow !== 'none');
    });
    if (!els[i]) return false;
    els[i].setAttribute('data-m-mark', t);
    return true;
  }, [rootSel, tag, minW, maxW, minH, maxH, nth]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : null;
}

// Marks the nearest ancestor of the element matching sel that paints a fill
// or a background image, or falls back to marking a painted descendant.
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
  shell: 'Shell and navigation', hero: 'Home hero', home: 'Home', pricing: 'Pricing',
  contact: 'Contact form', faq: 'FAQ', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  // The <header> element itself is 0-high; the pill bar is a painted descendant.
  const bar = await paintChild('header.elementor-location-header', 'm-header-bar', { minW: 600, minH: 40, maxH: 120 });
  await S('header', bar || q('header.elementor-location-header .e-con').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The floating pill header: Elementor logo, the Products mega-menu trigger, Agency/Enterprise/Pricing/App-Builder links, the En language selector, Log in and the black Get-started pill.', sel: 'painted bar inside header.elementor-location-header' }, { noScroll: true });
  await S('logo', q('header a[href*="elementor.com"], header a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Elementor wordmark anchor.', sel: 'header a:first' }, { noScroll: true });
  await S('nav-trigger', q('.e-n-menu-title.e-click').filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Products menu trigger that opens the mega-menu; toggled, never followed.', sel: '.e-n-menu-title.e-click "Products"' }, { noScroll: true });
  await S('nav-link', q('.e-n-menu-title-container.e-focus.e-link, .e-n-menu-title a').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The plain Pricing header link.', sel: 'e-n-menu "Pricing" link' }, { noScroll: true });
  await S('nav-login', q('header a.dsm-link-wrapper-st, header a').filter({ hasText: /^\s*Log in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Login link', desc: 'The Log-in header action; measured never followed (it points at my.elementor.com).', sel: 'header a "Log in"' }, { noScroll: true });
  await S('nav-cta', q('header a.dsm-btn-wrapper-st, header a').filter({ hasText: /^\s*Get started\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The black Get-started pill (dsm-button-primary-st); measured never followed (points at my.elementor.com/signup).', sel: 'header a.dsm-btn-wrapper-st "Get started"' }, { noScroll: true });
  // The Products trigger opens the mega-menu on hover/click; keep the pointer
  // put while the panel and one of its links are read (noReset), then Escape.
  try {
    const t = q('.e-n-menu-title.e-click, .e-n-menu-dropdown-icon').filter({ visible: true }).first();
    if (await t.count()) { await t.hover({ timeout: 5000 }).catch(() => {}); await page.waitForTimeout(600); await t.click({ timeout: 4000 }).catch(() => t.evaluate((el) => el.click())); await page.waitForTimeout(1400); }
  } catch (e) { log('  ! dropdown open failed', String(e.message).split('\n')[0]); }
  const panel = q('#e-n-menu-content-9381, .e-n-menu-content').filter({ visible: true }).first();
  await S('nav-dropdown', panel, ['default'], { group: g, title: 'Nav dropdown', desc: 'The Products mega-menu panel, opened by its own trigger.', sel: '#e-n-menu-content-9381 (open)' }, { noScroll: true, noReset: true });
  await S('menu-feature', q('[id^="e-n-menu-content"] a, .e-n-menu-content a').filter({ hasText: /Builder|AI|MCP|hosting|domain|mail/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Menu feature tile', desc: 'The large featured tile inside the mega-menu (the Agent Ready Scanner promo).', sel: 'mega-menu featured tile' }, { noScroll: true,
    open: async () => { const t = q('.e-n-menu-title.e-click, .e-n-menu-dropdown-icon').filter({ visible: true }).first(); if (await t.count()) { await t.hover({ timeout: 5000 }).catch(() => {}); await page.waitForTimeout(800); } } });
  await S('menu-link', q('[id^="e-n-menu-content"] a, .e-n-menu-content a').filter({ hasText: /Optimize images|Host your website|Build with AI Editor/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A product link inside the opened mega-menu columns.', sel: 'mega-menu content a' }, { noScroll: true,
    open: async () => { const t = q('.e-n-menu-title.e-click, .e-n-menu-dropdown-icon').filter({ visible: true }).first(); if (await t.count()) { await t.hover({ timeout: 5000 }).catch(() => {}); await page.waitForTimeout(800); } } });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  const h = G.hero;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The 88px Roobert white display headline over the photo hero (a .dark-mode island).', sel: 'h1' }, { noScroll: true });
  await S('hero-lede', q('h1 + p, h1 ~ p, p').filter({ hasText: /AI how you want it|WordPress/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The lede under the hero headline.', sel: 'hero lede' });
  await S('hero-cta', q('section.dark-mode a, section.dark-mode button').filter({ hasText: /^\s*Get started\s*$/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The white Get-started pill in the dark hero (dsm-button-primary inverted by the .dark-mode scope); measured never followed.', sel: 'section.dark-mode a "Get started"' });
  await S('cta-dark', q('.dark-mode ~ * a.dsm-btn-wrapper, section:not(.dark-mode) a.dsm-btn-wrapper').filter({ hasText: /Get started|Get Elementor|Learn more/i }).filter({ visible: true }).first(), B4, { group: G.home, title: 'Dark CTA', desc: 'A black dsm-button-primary pill on a light section; measured never followed.', sel: 'light-section a.dsm-btn-wrapper' });
  await S('hero-stage', q('section.dark-mode').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero stage', desc: 'The full-viewport video hero (the first .dark-mode island) behind the headline; its paint is the hosted <video> plus the swap overlay, not a background.', sel: 'section.dark-mode (first)' }, { crop: false, noScroll: true });
  const s = G.home;
  await S('h2-section', q('h2').filter({ visible: true }).first(), ['default'], { group: s, title: 'Section heading', desc: 'A Roobert section heading in the page body.', sel: 'h2' });
  await S('card', q('.dsm-card-wrapper').filter({ visible: true }).first(), ['default'], { group: s, title: 'Card', desc: 'A dsm card tile (1rem radius, white fill).', sel: '.dsm-card-wrapper' });
  await S('icon-item', q('.dsm-icon-list-item, .elementor-icon-list-item').filter({ visible: true }).first(), ['default'], { group: s, title: 'Icon list item', desc: 'A dsm icon-list row (glyph + label).', sel: '.dsm-icon-list-item' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 12000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pricing-h1', q('h1, h2').filter({ hasText: /pricing|plan/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The pricing page heading.', sel: 'h1/h2 on /pricing' }, { noScroll: true });
  await S('plan-name', q('h2, h3, h4, .elementor-heading-title').filter({ hasText: /^\s*(Essential|Advanced|Expert|Agency|One)\b/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan name', desc: 'A plan card name (Essential/Advanced Solo/Advanced).', sel: 'plan name heading' });
  await S('plan-price', q('[data-price], .price, [class*="price" i]').filter({ hasText: /\d/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'A plan card price figure.', sel: 'plan price' });
  await S('plan-cta', q('a, button').filter({ hasText: /^\s*Buy now\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card Buy-now action; measured never followed (it would open checkout).', sel: '"Buy now"' });
  await S('plan-card', q('.e-loop-item').filter({ hasText: /Essential|Advanced|Expert|One/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card: white 8px-radius tile holding the plan name, price, Buy-now action, the variant toggle and the feature list.', sel: '.e-loop-item' });
  await S('plan-toggle', q('button.plan-toggle').filter({ visible: true }).first(), B4, { group: g, title: 'Billing toggle', desc: 'A plan variant toggle inside a plan card (Advanced/Expert, One/One Agency); measured, never switched into a purchase.', sel: 'button.plan-toggle' });
  await S('feature-row', q('li.plan__features__item').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature row', desc: 'A plan feature row with its included/not-included marker.', sel: 'li.plan__features__item' });
  save();
}

async function contact() {
  if (!(await newPage('contact', { wait: 11000 }))) return;
  await sheetsFor('contact');
  await chrome('contact');
  const g = G.contact;
  await S('contact-h1', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact title', desc: 'The Contact-us page heading.', sel: 'h1/h2 on /contact' }, { noScroll: true });
  await S('contact-card', q('[data-action-link*="popup%3Aopen"]').filter({ visible: true }).first(), B4, { group: g, title: 'Contact card', desc: 'A contact-option card (Legal department inquiries form): its own toggle opens the Elementor popup holding the form.', sel: '[data-action-link*=popup:open]' });
  // Open the Legal department popup — the form widget inside is what the
  // field specs measure. Local UI toggle; the form is never submitted.
  try {
    const card = q('[data-action-link*="popup%3Aopen"]').filter({ visible: true }).first();
    if (await card.count()) { await card.click({ timeout: 5000 }).catch(() => card.evaluate((el) => el.click())); await page.waitForTimeout(1600); }
  } catch (e) { log('  ! contact popup failed', String(e.message).split('\n')[0]); }
  await S('form-popup', q('[data-elementor-type="popup"].elementor-location-popup').filter({ visible: true }).first(), ['default'], { group: g, title: 'Form popup', desc: 'The Elementor popup dialog holding the contact form, opened by its card.', sel: '[data-elementor-type=popup] (open)' });
  await S('field-name', q('input#form-field-full_name, input[name*="full_name" i], input[type="text"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Name field', desc: 'The full-name text input; sample text typed and deleted, nothing sent.', sel: 'input#form-field-full_name' });
  await S('field-email', q('input#form-field-email, input[type="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Email field', desc: 'The email input; focused only, never filled or sent.', sel: 'input#form-field-email' });
  await S('field-message', q('textarea.elementor-field, textarea').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Message area', desc: 'The message textarea; focused only.', sel: 'textarea.elementor-field' });
  await S('field-select', q('select.elementor-field, select').filter({ visible: true }).first(), B4, { group: g, title: 'Department select', desc: 'The department select; measured, never changed.', sel: 'select.elementor-field' });
  // The input is the toggle target but paints at opacity 0: checkboxExtra
  // also reads the visible box (the label's ::before) and the checked flag.
  await S('checkbox', q('input[type="checkbox"].elementor-field, input#form-field-acceptance').filter({ visible: true }).first(), B4.concat(['selected']), { group: g, title: 'Acceptance checkbox', desc: 'The acceptance checkbox; checked for the selected state and unchecked again (local UI state) — the form was never submitted.', sel: 'input#form-field-acceptance' }, {
    extra: checkboxExtra,
    // The input paints at opacity 0, so pressed is forced on the label the user presses.
    pressLoc: q('label[for="form-field-acceptance"]'),
    // Uncheck after the selected reading so the form is left as it was found.
    after: { selected: async (l) => { if (await l.isChecked().catch(() => false)) await toggle(l); } },
  });
  await S('submit-btn', q('button[type="submit"], button.elementor-button').filter({ visible: true }).first(), B4, { group: g, title: 'Submit button', desc: 'The form submit; measured, never pressed (a real press would send the form).', sel: 'button[type=submit]' });
  save();
}

async function faq() {
  if (!(await newPage('faq', { wait: 11000 }))) return;
  await sheetsFor('faq');
  await chrome('faq');
  const g = G.faq;
  await S('faq-h1', q('h1, h2').filter({ hasText: /Frequently Asked|FAQ/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ title', desc: 'The Frequently-Asked-Questions heading.', sel: 'FAQ heading' }, { noScroll: true });
  await S('faq-item', q('.dsm-faq--title[aria-expanded]').filter({ visible: true }).first(), B4, { group: g, title: 'FAQ item (closed)', desc: 'A question row of the FAQ accordion (aria-expanded toggle).', sel: '.dsm-faq--title' });
  // Open the first item with its own toggle (local UI state) and re-read; the
  // header row swallows the pointer click, so dispatch on the element.
  try {
    const t = q('.dsm-faq--title[aria-expanded]').filter({ visible: true }).first();
    if (await t.count()) {
      await t.evaluate((el) => el.click()); await page.waitForTimeout(1200);
      const now = await t.getAttribute('aria-expanded').catch(() => '?');
      log('  faq toggle ->', now);
      if (now !== 'true') { await page.evaluate(() => { const n = document.querySelector('.dsm-faq--title'); n && n.click(); }); await page.waitForTimeout(1200); }
    }
  } catch (e) { log('  ! faq toggle failed', String(e.message).split('\n')[0]); }
  await S('faq-item-open', q('.dsm-faq--title[aria-expanded="true"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ item (open)', desc: 'The same question row after its own toggle opened it.', sel: '.dsm-faq--title[aria-expanded=true]' });
  await S('faq-answer', q('.dsm-faq--faq-content[aria-hidden="false"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ answer', desc: 'The revealed answer panel.', sel: '.dsm-faq--faq-content[aria-hidden=false]' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 7000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1800);
  await S('footer', q('footer, .dsm-footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The dsm-footer (a .dark-mode island): link columns, social icons and legal on black.', sel: '.dsm-footer' }, { noScroll: true });
  await S('footer-link', q('footer a, .dsm-footer a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('social-icon', q('footer .elementor-social-icon, .dsm-footer .elementor-social-icon, footer a[class*="icon" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Social icon', desc: 'A footer social-icon link (icon button).', sel: 'footer .elementor-social-icon' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  const mbar = await paintChild('header.elementor-location-header', 'm-mheader-bar', { minW: 200, minH: 30, maxH: 120 });
  await S('m-header', mbar || q('header.elementor-location-header .e-con').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'painted bar inside header at 390' }, { noScroll: true });
  const menu = q('button.e-n-menu-toggle').filter({ visible: true }).first();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The header hamburger toggle (e-n-menu-toggle).', sel: 'button.e-n-menu-toggle' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1600); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await S('m-menu-open', q('#menubar-938, .e-n-menu-wrapper').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The header menu panel opened by its own toggle.', sel: '#menubar-938 open' }, { noScroll: true });
  await S('m-nav-item', q('#menubar-938 .e-n-menu-title, #menubar-938 a, .e-n-menu-wrapper .e-n-menu-title').filter({ hasText: /Products|Agency|Enterprise|Pricing/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'An item inside the opened header menu.', sel: 'mobile menu item' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
const pages = process.argv.slice(2);
// The read stamp is the date the whole set was measured: a partial re-run
// re-dates only the components it touched (each carries `run`), recorded
// under _meta.recaptured so earlier pages keep their original provenance.
if (pages.length) (out._meta.recaptured ??= {})[pages.join(',')] = run;
else out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the page paints light with .dark-mode islands (photo hero, dark sections, footer) re-binding the same named vars';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const plan = { home, pricing, contact, faq, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
let finished = false;
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (the dsm button
  // background transition), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '.dsm-btn-wrapper');
  finished = true;
} finally {
  // Prune only a completed run: when the loop aborts on a page error, the
  // pages never reached are absent from `touched` and pruning here would
  // delete their earlier readings. An edge-blocked route likewise keeps its
  // earlier readings under their original provenance.
  if (finished) for (const [key, c] of Object.entries(out.components)) {
    if (!touched.has(key) && !pages.length && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
