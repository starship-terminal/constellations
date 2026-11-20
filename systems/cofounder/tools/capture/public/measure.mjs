// Measures cofounder.co's public components in every state reachable
// without signing in, paying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing howto signin mobile (the footer group also runs
// on home). Writes raw/components-computed.json (merged) and one crop per
// component and state into components/crops/; raw/measurements.md is
// built by build-measurements.mjs.
//
// cofounder.co is a Next.js/Tailwind v4 build in one LIGHT theme: semantic
// utility classes (site-header, nav-link, glass-hero-btn, cta-btn-dark,
// btn-light-surface, pricing-card-group, footer-link) plus data-analytics-*
// instrumentation and aria-labels carry the selectors.
// app.cofounder.co/os/login is the product's sign-in boundary: its card is
// measured, never submitted. The only presses are local UI toggles — the
// tools-section tab buttons (aria-pressed), carousel arrows and the mobile
// menu button. Every CTA links to app.cofounder.co/os — measured, never
// followed. The hero "copy setup prompt" button is never pressed (it would
// write the clipboard): only rest/hover/focus/CDP-forced states.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', howto: '/how-to/start', signin: 'https://app.cofounder.co/os/login' };
let page, cdp, current, view, context, run;
const touched = new Set();
const listed = new Map();
// Page+viewport visits that actually loaded this run (not blocked): readings
// may only be pruned for components of one of these — a blocked mobile visit
// must not erase evidence the desktop visit of the same route kept.
const opened = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || /just a moment/i.test(document.title) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, dsf } = {}) {
  current = key;
  view = mobile ? 'mobile' : 'desktop';
  const b = context.browser();
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: dsf ?? 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, /^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key], { wait });
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  opened.add(key + '|' + view);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await closePromo(page);
  return true;
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
  Object.assign(c, { page: current, view, run, url: URLS[current] && new URL(URLS[current], BASE).href }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

async function measure(key, state, target, opts = {}) {
  const loc = target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    const prev = c.states[state];
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    // A failed crop keeps the previous state's image link rather than
    // dropping it; the style reading is fresh, the crop is last good.
    c.states[state] = { ...s, crop: file ?? (prev && prev.crop), via: opts.via, run };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    // A failed state capture must not erase a previous reading: keep it under
    // its own provenance and record the error beside it.
    const prev = c.states[state];
    c.states[state] = prev && !prev.error
      ? { ...prev, recaptureError: String(e.message || e).slice(0, 200) }
      : { error: String(e.message || e).slice(0, 200) };
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
        if (opts.noToggle) via = 'menu held open by opts.open';
        else { await toggle(loc); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      out.components[key].states[st] = prev && !prev.error
        ? { ...prev, recaptureError: String(e.message || e).slice(0, 200) }
        : { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (nav menu, mobile menu). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|start|get started|claim|share|export|select|continue|book|request)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Marks the shallowest ancestor of a text leaf whose subtree paints a fill of
// colour `want` (Framer draws a button's fill on a sibling layer, so the
// anchor alone reads transparent). `minY` skips same-text copies in the
// header. Falls back to the leaf. Returns whether anything was marked.
const markFillParent = async (textRe, want, attr, { minY = 0 } = {}) => page.evaluate(([src, flags, a, w, miny]) => {
  const re = new RegExp(src, flags);
  const texts = [...document.querySelectorAll('a,button,div,p,span')].filter((n) => {
    const t = (n.innerText || '').trim();
    const r = n.getBoundingClientRect();
    return re.test(t) && t.length < 60 && r.width > 0 && r.y >= miny;
  });
  const leaf = texts.find((n) => !texts.some((o) => o !== n && n.contains(o))) || texts[0];
  if (!leaf) return false;
  const paints = (n) => getComputedStyle(n).backgroundColor === w;
  for (let n = leaf, i = 0; n && i < 8; i++, n = n.parentElement) {
    if (n.getBoundingClientRect().width > 700) break;
    if (paints(n) || [...n.children].some((k) => paints(k) && k.getBoundingClientRect().width >= 80)) {
      n.setAttribute(a, '1');
      return true;
    }
  }
  leaf.setAttribute(a, '1');
  return true;
}, [textRe.source, textRe.flags, attr, want, minY]);

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

const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  howto: 'How-to guides', signin: 'App sign-in (boundary)',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  // The fixed top bar (site-header): transparent at the top, gains a
  // border/shadow on scroll; logo left, flat nav-link row centre, the
  // "Run a company" pill right.
  await S('header', q('header.site-header, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav bar', desc: 'The fixed site header (position:fixed, transparent at top, border+shadow on scroll): logo, flat nav links, Run-a-company CTA.', sel: 'header.site-header' }, { noScroll: true });
  await S('logo', q('header a[aria-label="Home"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Cofounder mark+wordmark home anchor in the header.', sel: 'header a[aria-label=Home]' }, { noScroll: true });
  await S('nav-item', q('header a.nav-link, nav a.nav-link').filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A flat nav link (nav-link, 15px/410 weight, text-surface-raised): Start/Build/Sell/Scale/Resources/Pricing.', sel: 'a.nav-link' }, { noScroll: true });
  await S('nav-cta', q('header a[data-analytics-location="site_nav"], header a[data-analytics-location="site_header"]').filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The header "Run a company" pill linking to app.cofounder.co/os; measured never followed.', sel: 'a[data-analytics-location=site_nav|site_header]' }, { noScroll: true });
  const h = G.home;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: '"Cofounder lets you run an entire company with AI" — the hero headline (hero-gradient-text, 46px/108%).', sel: 'h1' }, { noScroll: true });
  await S('hero-cta', q('a[data-analytics-location="hero"]').filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The hero "Run a company" anchor linking to app.cofounder.co/os; measured never followed.', sel: 'a[data-analytics-location=hero]' }, { noScroll: true });
  // The copy-setup-prompt button writes the clipboard on press — measured
  // at rest/hover/focus/forced only, never clicked.
  await S('hero-prompt-btn', q('button[data-analytics-cta="copy_setup_prompt"]').filter({ visible: true }).first(), B4, { group: h, title: 'Prompt button', desc: 'The glass "copy the setup prompt" hero button (glass-hero-btn, backdrop-blur 24px); never pressed — it writes the clipboard. Hover/focus/forced states only.', sel: 'button[data-analytics-cta=copy_setup_prompt]' }, { noScroll: true });
  await S('cta-dark', q('a.cta-btn-dark, button.cta-btn-dark').filter({ visible: true }).first(), B4, { group: h, title: 'Dark CTA', desc: 'A cta-btn-dark control — the dark button style used for mid-page actions.', sel: '.cta-btn-dark' });
  await S('cta-light', q('a.btn-light-surface, button.btn-light-surface').filter({ visible: true }).first(), B4, { group: h, title: 'Light CTA', desc: 'A btn-light-surface control — the light pill button style.', sel: '.btn-light-surface' });
  // The "All the tools and systems" band paints #1a6fd1 and holds
  // aria-pressed tab buttons that switch the tool diagram.
  await S('blue-section', q('section[aria-label*="tools and systems"], section.bg-\\[\\#1a6fd1\\]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Tools band', desc: 'The #1a6fd1 "All the tools and systems" band with the tools diagram and tab toggles.', sel: 'section.bg-[#1a6fd1]' });
  // The band rotates its selected tab by itself, so a locator that re-resolves aria-pressed for every state
  // reads whichever button is selected at that moment (tool-tab focus-visible was another button, and
  // tool-tab-off was the first button after it rotated off). Mark one button of each kind once, then
  // measure those. The rotation itself is not paused, so a state read late can still find its button
  // flipped; the via and text of each reading show which.
  await page.evaluate(() => {
    const band = document.querySelector('section[aria-label*="tools and systems"]') || document;
    band.querySelector('button[aria-pressed="true"]')?.setAttribute('data-m-tab', 'on');
    band.querySelector('button[aria-pressed="false"]')?.setAttribute('data-m-tab', 'off');
  });
  await S('tool-tab', q('[data-m-tab="on"]').filter({ visible: true }).first(), ['default', 'focus-visible'], { group: h, title: 'Tools tab (selected)', desc: 'The selected aria-pressed tab in the tools band (text-white selected).', sel: 'button[aria-pressed=true] in tools band' });
  await S('tool-tab-off', q('[data-m-tab="off"]').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: h, title: 'Tools tab (unselected)', desc: 'An unselected aria-pressed tab (text-white/40, hover white/60); never pressed — it swaps the diagram.', sel: 'button[aria-pressed=false] in tools band' });
  await S('tool-button', q('button.rounded-\\[10px\\].border, section button[class*="border-black"]').filter({ visible: true }).first(), B4, { group: h, title: 'Tool button', desc: 'A tool/agent picker button (border-black/10 bg-white/60 rounded-[10px], hover white-fill swap).', sel: 'button.border-black/10' });
  await S('case-study', q('a[aria-label="View Cofounder case studies"]').filter({ visible: true }).first(), B4, { group: h, title: 'Case study card', desc: 'A case-study card anchor.', sel: 'a[aria-label="View Cofounder case studies"]' });
  await S('carousel-prev', q('button[aria-label="Previous campaign"], button[aria-label="Previous"]').filter({ visible: true }).first(), B4, { group: h, title: 'Carousel arrow', desc: 'A campaign-carousel arrow button.', sel: 'button[aria-label="Previous campaign"]' });
  await S('logo-tile', q('.logo-tile').filter({ visible: true }).first(), ['default'], { group: h, title: 'Logo tile', desc: 'A customer logo tile (170x84) in the social-proof row.', sel: '.logo-tile' });
  await S('logo-pill', q('.logo-pill').filter({ visible: true }).first(), ['default'], { group: h, title: 'Tool logo pill', desc: 'An agent-tool logo pill (ChatGPT/Claude/Cursor/Codex icons in /agent-icons/).', sel: '.logo-pill' });
  await S('section-title', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section title', desc: 'A section heading under the hero (Neoris, 28-40px responsive).', sel: 'first h2' });
  await S('page-ground', q('body'), ['default'], { group: h, title: 'Page ground', desc: 'The body element painted fill — the page ground (--background #f5f5f2).', sel: 'document.body' }, { noScroll: true, crop: false });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  // The pricing h1 is sr-only; the visible headline is the first h2.
  await S('pricing-title', q('h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The visible pricing headline (the h1 is sr-only).', sel: 'first visible h2' }, { noScroll: true });
  await S('plan-card', q('a.pricing-card-group').filter({ visible: true }).first(), B4, { group: g, title: 'Plan card', desc: 'A whole-card plan anchor (pricing-card-group -> pricing-card): border-border-card bg-surface-raised rounded-2xl, hover reveals the hidden CTA chip (no lift transition — the anchor computes 0s). Links to app.cofounder.co; never followed.', sel: 'a.pricing-card-group' });
  await S('plan-name', q('a.pricing-card-group span.text-ink-muted').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan name', desc: 'The plan label row inside a pricing card (15px ink-muted).', sel: '.pricing-card-group .text-ink-muted' });
  // The whole-card anchor IS the plan CTA (aria-label "Get started for
  // Cofounder"); inside it a cta-btn-dark chip exists only while the card is
  // hovered — held open by the card's own hover, never followed.
  const planCard = q('a.pricing-card-group').filter({ visible: true }).first();
  await S('plan-cta', q('a.pricing-card-group .cta-btn-dark:not(.absolute)').filter({ visible: true }).first(), ['default', 'pressed'], { group: g, title: 'Revealed CTA chip', desc: 'The "Get started" cta-btn-dark chip a plan card reveals on hover; exists only while the card is hovered — held open by the card\'s own hover, never followed.', sel: '.pricing-card-group .cta-btn-dark' }, { noReset: true, open: async () => { await planCard.hover(); await page.waitForTimeout(700); } });
  save();
}

async function howto() {
  if (!(await newPage('howto'))) return;
  const g = G.howto;
  // The guide renders a hidden heading set first in DOM (a prerender/SEO
  // copy); the real content is last — .last() lands on it regardless of how
  // the engine judges the hidden copy.
  await S('howto-title', q('h1').last(), ['default'], { group: g, title: 'Guide title', desc: 'The how-to guide headline (40px Neoris at 1440).', sel: 'h1' }, { noScroll: true });
  await S('howto-section', q('main').filter({ visible: true }).first(), ['default'], { group: g, title: 'Guide section', desc: 'The how-to guide content column.', sel: 'main' });
  await S('howto-heading', q('h2').last(), ['default'], { group: g, title: 'Guide heading', desc: 'A section heading inside the guide (24px/530).', sel: 'h2' });
  await S('howto-card-title', q('h3').last(), ['default'], { group: g, title: 'Card title', desc: 'A step/card title inside the guide (15px/530).', sel: 'h3' });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 18000 }))) return;
  const g = G.signin;
  // app.cofounder.co/os/login is the product's sign-in surface: the card and
  // its Continue-with buttons are measured; nothing is pressed or sent.
  await S('signin-card', q('main, [class*="login" i], [class*="auth" i], form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in card', desc: 'The app.cofounder.co/os login surface: the sign-in card the app paints. Measured at rest, never submitted.', sel: 'main/first visible login container' }, { noScroll: true });
  await S('signin-button', q('button, a[class*="btn" i], a[class*="button" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'A "Continue with" OAuth button on the sign-in card; measured never pressed.', sel: 'first visible button' }, { noScroll: true });
  await S('signin-back', q('a[aria-label="Back to Cofounder"]').filter({ visible: true }).first(), B4, { group: g, title: 'Back link', desc: 'The "Back to Cofounder" link returning to the marketing site.', sel: 'a[aria-label="Back to Cofounder"]' }, { noScroll: true });
  save();
}

async function footer() {
  if (!(await newPage('home'))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1600);
  await page.evaluate(() => {
    const f = document.querySelector('footer, [role="contentinfo"]');
    if (f) f.setAttribute('data-m-footer', '1');
  });
  await S('footer', q('[data-m-footer="1"]'), ['default'], { group: g, title: 'Footer', desc: 'The footer band (footer-bg): the Run-a-company CTA card, link columns, social icons and legal row.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('[data-m-footer="1"] a.footer-link[href="/pricing"]').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A link in a footer link column (footer-link) — the md:hidden mobile CTA copy is skipped.', sel: 'footer a.footer-link' }, { noScroll: true });
  await S('footer-social', q('[data-m-footer="1"] a[aria-label="X"], [data-m-footer="1"] a[aria-label="LinkedIn"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A footer social icon link (X/LinkedIn).', sel: 'footer a[aria-label=X|LinkedIn]' }, { noScroll: true });
  await S('footer-cta', q('[data-m-footer="1"] a[data-analytics-location="footer_card"]:visible').filter({ visible: true }).first(), B4, { group: g, title: 'Footer CTA', desc: 'The footer CTA card "Run a company" button (btn-light-surface) linking to app.cofounder.co/os; measured never followed.', sel: 'footer a[data-analytics-location=footer_card]' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  // At 390 the nav collapses to the bar plus the Open-menu toggle; the menu
  // opens on the button's own press.
  await S('m-header', q('header.site-header, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile bar', desc: 'The 390 mobile header bar: logo + menu toggle.', sel: 'header.site-header at 390' }, { noScroll: true });
  await S('m-menu-button', q('button[aria-label="Open menu"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Menu button', desc: 'The hamburger (aria-label="Open menu", 41x41 rounded-8); its own press opens the menu.', sel: 'button[aria-label="Open menu"]' }, { noScroll: true });
  const menuBtn = q('button[aria-label="Open menu"]').filter({ visible: true }).first();
  if (await menuBtn.count()) {
    try { await menuBtn.click({ timeout: 5000 }); await page.waitForTimeout(1500); } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  }
  // The open menu is a fixed full-screen overlay holding the big link list;
  // tag whatever fills the viewport and contains the "How to" section.
  await page.evaluate(() => {
    const p = [...document.querySelectorAll('body *')].find((e) => {
      const cs = getComputedStyle(e);
      const r = e.getBoundingClientRect();
      return (cs.position === 'fixed' || cs.position === 'absolute') && r.height > 500 && r.width > 300 && e.querySelector('a[href="/how-to/start"], a[href="/pricing"]');
    });
    if (p) p.setAttribute('data-m-panel', '1');
  }).catch(() => {});
  await S('m-menu-open', q('[data-m-panel="1"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The full-screen menu overlay after the hamburger press.', sel: 'opened mobile menu overlay' }, { noScroll: true });
  await S('m-menu-link', q('[data-m-panel="1"] a').filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A link row inside the open mobile menu.', sel: 'first link inside the open menu' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The hero headline at 390.', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme (app.cofounder.co/os/login is the sign-in boundary)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, howto, signin, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // Prune only components whose page+viewport visit actually opened this
    // run: a blocked route (or a blocked mobile pass of a route the desktop
    // pass captured) keeps its earlier readings. Components saved before the
    // view field existed fall back to the m- prefix for their variant.
    if (!touched.has(key) && !pages.length) {
      const cview = c.view || (key.startsWith('m-') ? 'mobile' : 'desktop');
      if (opened.has(c.page + '|' + cview)) delete out.components[key];
      continue;
    }
    if (!touched.has(key)) continue;
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st) && pages.length) delete c.states[st];
  }
  save();
  await browser.close().catch(() => {});
}
console.log('done ->', OUT);
