// Measures homerun.co's public components in every state reachable
// without signing in, paying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing ats careers apply signin signinhr mobile (the footer
// group also runs on home). Writes raw/components-computed.json (merged)
// and one crop per component and state into components/crops/;
// raw/measurements.md is built by build-measurements.mjs.
//
// homerun.co is a Webflow build in one LIGHT theme: classes are plain
// authored names (nav-primary, btn-primary_new, w-dropdown). The nav
// dropdowns open on hover (data-hover). jobs.homerun.co is the employer
// careers site the product publishes; app.homerun.co/login and
// app.homerun.hr/Account/Logon are sign-in boundaries measured at rest,
// never submitted. The only presses are local UI toggles — the nav
// dropdown hovers, FAQ accordion toggles, the pricing job-slot stepper
// and the mobile menu button. Log-in/sign-up/apply links are measured,
// never followed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, JOBS, APP, APPHR, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', pricing: '/pricing', ats: '/ats',
  careers: JOBS + '/', job: JOBS + '/open/en', apply: JOBS + '/open/en/apply',
  signin: APP + '/login', signinhr: APPHR + '/Account/Logon',
};
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
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || /just a moment/i.test(document.title) || t.trim().length < 20;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, dsf, promo = 'close' } = {}) {
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
  const loaded = await open(page, /^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key], { wait, promo });
  if (!loaded || await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  opened.add(key + '|' + view);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return true;
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  await page.keyboard.press('Escape').catch(() => {});
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

// Clicks a UI toggle (nav menu, mobile menu, an accordion). Refuses a submit
// button and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|start|get started|claim|share|export|select|continue|book|request|apply now|next)/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Hover-holds a Webflow data-hover dropdown open on the desktop nav; returns
// whether the list painted. The panel stays open only while the pointer is
// on the trigger or the panel — move onto the panel to keep it held. The
// marker attributes are cleared first so a second dropdown never matches
// two elements, and the pointer moves with real mouse.move calls to the
// element centre (locator.hover() actionability waits proved flaky on the
// sticky nav while a previous dropdown was closing).
async function holdNavDropdown(which) {
  const box = await page.evaluate((w) => {
    for (const e of document.querySelectorAll('[data-m-nd]')) e.removeAttribute('data-m-nd');
    for (const e of document.querySelectorAll('[data-m-nd-panel]')) e.removeAttribute('data-m-nd-panel');
    const el = [...document.querySelectorAll('.nav-new.is-desktop .w-dropdown-toggle')].find((e) => (e.innerText || '').trim().toLowerCase().startsWith(w));
    if (!el) return false;
    el.setAttribute('data-m-nd', '1');
    const r = el.getBoundingClientRect();
    return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
  }, which);
  if (!box) return false;
  await page.mouse.move(box.x, box.y, { steps: 8 });
  await page.waitForTimeout(1400);
  // Move onto the panel itself so the open state survives subsequent reads.
  const moved = await page.evaluate(() => {
    const t = document.querySelector('[data-m-nd="1"]');
    const dd = t && t.closest('.w-dropdown');
    const list = dd && dd.querySelector('.w-dropdown-list');
    if (!list) return false;
    const r = list.getBoundingClientRect();
    if (!r.width || getComputedStyle(list).display === 'none') return false;
    list.setAttribute('data-m-nd-panel', '1');
    return { x: r.x + r.width / 2, y: r.y + Math.min(r.height - 4, 30) };
  });
  if (moved) { await page.mouse.move(moved.x, moved.y, { steps: 6 }).catch(() => {}); await page.waitForTimeout(400); return true; }
  // The panel never painted: try a click as a last resort (some Webflow
  // builds open on both), then leave the pointer on the trigger either way.
  await page.click('[data-m-nd="1"]', { timeout: 3000 }).catch(() => {});
  await page.waitForTimeout(800);
  return page.evaluate(() => {
    const t = document.querySelector('[data-m-nd="1"]');
    const list = t && t.closest('.w-dropdown') && t.closest('.w-dropdown').querySelector('.w-dropdown-list');
    return !!(list && list.getBoundingClientRect().width && getComputedStyle(list).display !== 'none');
  });
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

const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  ats: 'ATS page', careers: 'Careers site (jobs.homerun.co)',
  apply: 'Application form', signin: 'ATS sign-in (boundary)',
  signinhr: 'HR sign-in (boundary)', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  // The sticky top bar: HOMERUN wordmark left, ATS/HR pill links,
  // Pricing/Customers/Partnership/Resources centre, Log in + Book a demo +
  // Start free trial right.
  await S('header', q('.nav-new.is-v2.is-desktop, .nav-primary').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav bar', desc: 'The sticky 1440 top nav (position:sticky): logo, product pills, dropdown menus, Log-in/Book-a-demo/Start-free-trial actions.', sel: '.nav-new.is-desktop' }, { noScroll: true });
  await S('logo', q('a.new-nav_brand').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The HOMERUN logotype anchor (wordmark image).', sel: 'a.new-nav_brand' }, { noScroll: true });
  await S('nav-link', q('.nav-new.is-desktop a.nav_link-new.w-nav-link').filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A text nav link (Pricing) in the top bar.', sel: 'a.nav_link-new' }, { noScroll: true });
  await S('nav-product-pill', q('.nav-new.is-desktop a.nav_link-new.is-icon').filter({ visible: true }).first(), B4, { group: g, title: 'Nav product pill', desc: 'The "ATS Organise your hiring" pill — an icon-bearing product link that tints its icon on hover.', sel: 'a.nav_link-new.is-icon[data-nav-menu]' }, { noScroll: true });
  await S('nav-resources', q('.nav-new.is-desktop .nav_link-new.is-dropdown-v2 .w-dropdown-toggle').filter({ visible: true }).first(), ['default', 'hover', 'opened'], { group: g, title: 'Resources dropdown', desc: 'The Resources nav dropdown trigger — a hover-open w-dropdown whose panel links Blog/Guides/Templates/Integrations/Help center and Product updates/Careers/Refer/About.', sel: '.nav_link-new.is-dropdown-v2 .w-dropdown-toggle' }, { noScroll: true, noToggle: true, before: { opened: holdNavDropdown.bind(null, 'resources') } });
  await S('nav-resources-panel', q('.nav-new.is-desktop .nav_dropdown-list-v2.resources, .nav-new.is-desktop .nav_resources-update').filter({ visible: true }).first(), ['default'], { group: g, title: 'Resources panel', desc: 'The open Resources mega-panel (nav_resources-update): two link columns, rounded + shadowed card.', sel: '.nav_dropdown-list-v2.resources' }, { noScroll: true, noReset: true, open: holdNavDropdown.bind(null, 'resources') });
  await S('nav-resources-link', q('.nav-new.is-desktop a.nav_resources-link').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Resources link', desc: 'A link row inside the open Resources panel; focus/pressed are unreachable while the panel is hover-held.', sel: 'a.nav_resources-link' }, { noScroll: true, noReset: true, open: holdNavDropdown.bind(null, 'resources') });
  await S('nav-login', q('.nav-new.is-desktop .nav_cta-dropdown .w-dropdown-toggle').filter({ visible: true }).first(), ['default', 'hover', 'opened'], { group: g, title: 'Log-in dropdown', desc: 'The "Log in" ghost-button dropdown — opens the ATS/HR sign-in menu on hover.', sel: '.nav_cta-dropdown .w-dropdown-toggle' }, { noScroll: true, noToggle: true, before: { opened: holdNavDropdown.bind(null, 'log') } });
  await S('nav-login-panel', q('.nav-new.is-desktop .nav_cta-dropdown-list-outer, .nav-new.is-desktop .nav_cta-dropdown .w-dropdown-list').filter({ visible: true }).first(), ['default'], { group: g, title: 'Log-in panel', desc: 'The open Log-in menu: "ATS Organise your hiring" and "HR Manage your team" sign-in links, measured never followed.', sel: '.nav_cta-dropdown-list-outer' }, { noScroll: true, noReset: true, open: holdNavDropdown.bind(null, 'log') });
  await S('nav-login-link', q('.nav-new.is-desktop .nav_cta-dropdown a.nav-cta_dropdown-link, .nav-new.is-desktop .nav_cta-dropdown-list-outer a').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Log-in menu link', desc: 'A sign-in link inside the open Log-in menu (to app.homerun.co/login); measured never followed.', sel: '.nav_cta-dropdown a' }, { noScroll: true, noReset: true, open: holdNavDropdown.bind(null, 'log') });
  await reset();
  await S('nav-demo', q('.nav-new.is-desktop a.btn-black_new').filter({ visible: true }).first(), B4, { group: g, title: 'Book-a-demo button', desc: 'The dark "Book a demo" button in the top bar; links to a HubSpot meeting page, never followed.', sel: 'nav a.btn-black_new' }, { noScroll: true });
  await S('nav-trial', q('.nav-new.is-desktop a.btn-primary_new').filter({ visible: true }).first(), B4, { group: g, title: 'Start-trial button', desc: 'The blue "Start free trial" button in the top bar; links to /trial, never followed.', sel: 'nav a.btn-primary_new' }, { noScroll: true });
  const h = G.home;
  await S('hero-title', q('h1.new-home-h1, h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: '"Beautiful HR tools for modern teams." — the hero display headline.', sel: 'h1.new-home-h1' }, { noScroll: true });
  await S('hero-sub', q('.new-home-h1').first().locator('xpath=following::p[1]'), ['default'], { group: h, title: 'Hero subline', desc: 'The hero supporting paragraph under the headline.', sel: 'p after h1' }, { noScroll: true });
  await S('hero-cta', q('a.btn-primary_new.is-icon.is-large').filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: '"Try free for 15 days" — the large primary button with an arrow icon under the hero copy; links to /trial, never followed.', sel: 'a.btn-primary_new.is-icon.is-large' }, { noScroll: true });
  await S('hero-demo', q('.h-new-hero_left a.btn-secondary_new').filter({ visible: true }).first(), B4, { group: h, title: 'Hero secondary', desc: 'The "Book a demo" bordered button beside the hero CTA.', sel: '.h-new-hero_left a.btn-secondary_new' }, { noScroll: true });
  await S('rating-row', q('.home-new-hero_stats, .btn-container.no-margin').filter({ visible: true }).first(), ['default'], { group: h, title: 'Rating row', desc: 'The social-proof row under the hero CTAs (Capterra rating, satisfaction, team count).', sel: '.home-new-hero_stats' });
  await S('section-h2', q('h2.new-h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section title', desc: 'The first section heading under the hero.', sel: 'first h2.new-h2' });
  await S('feature-accordion', q('.h-new_features-item.w-dropdown').filter({ visible: true }).first(), ['default', 'opened'], { group: h, title: 'Feature accordion', desc: 'A feature accordion row (h-new_features-item w-dropdown): summary bar + expanding body; opened with its own toggle.', sel: '.h-new_features-item.w-dropdown' }, { noScroll: true, before: { opened: async (loc) => { await toggle(loc.locator('.w-dropdown-toggle').first()); await page.waitForTimeout(1000); return 'own w-dropdown-toggle'; } } });
  await S('feature-accordion-body', q('.h-new_features-item .h-new_features-item-bot').filter({ visible: true }).first(), ['default'], { group: h, title: 'Accordion body', desc: 'The body text region of an opened feature accordion.', sel: '.h-new_features-item-bot after open' }, { noScroll: true, noReset: true, open: async () => { const t = q('.h-new_features-item.w-dropdown .w-dropdown-toggle').first(); if (await t.count()) await t.click().catch(() => {}); await page.waitForTimeout(1000); } });
  await S('testimonial-card', q('.land-new_testi-item').filter({ visible: true }).first(), ['default'], { group: h, title: 'Testimonial card', desc: 'A customer testimonial card (land-new_testi-item): quote, avatar, name, role.', sel: '.land-new_testi-item' });
  await S('marquee-item', q('.land-marquee_company-item').filter({ visible: true }).first(), ['default'], { group: h, title: 'Logo marquee item', desc: 'A company logo cell in the scrolling customer marquee (CSS marquee animation).', sel: '.land-marquee_company-item' });
  await S('cta-band', q('.h-new_cta').filter({ visible: true }).last(), ['default'], { group: h, title: 'CTA band', desc: 'The closing call-to-action band before the footer (h-new_cta: label, headline, demo + trial buttons).', sel: '.h-new_cta' });
  await S('page-ground', q('body'), ['default'], { group: h, title: 'Page ground', desc: 'The body element\'s painted fill — the page ground.', sel: 'document.body' }, { noScroll: true, crop: false });
  save();
}

async function footer() {
  if (!(await newPage('home'))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1600);
  await page.evaluate(() => {
    const f = document.querySelector('footer, .footer_component, [role="contentinfo"], [class*="footer" i]');
    if (f) f.setAttribute('data-m-footer', '1');
  });
  await S('footer', q('[data-m-footer="1"]'), ['default'], { group: g, title: 'Footer', desc: 'The footer band: link columns, newsletter form, social icons and legal subfooter.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('[data-m-footer="1"] a.footer-link').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A link in a footer link column.', sel: 'footer a.footer-link' }, { noScroll: true });
  await S('footer-heading', q('[data-m-footer="1"] .footer-heading').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer heading', desc: 'A column heading in the footer.', sel: '.footer-heading' }, { noScroll: true });
  await S('newsletter-field', q('input.newsletter-text-white-2, input[type="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Newsletter field', desc: 'The footer newsletter email input; focused locally, never submitted.', sel: 'input.newsletter-text-white-2' }, { noScroll: true });
  await S('newsletter-button', q('.newsletter-white, input.newsletter-white').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Newsletter button', desc: 'The newsletter subscribe submit; measured never pressed (a submit control).', sel: '.newsletter-white' }, { noScroll: true });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: '"Choose the right plan for your team." — the pricing headline.', sel: 'h1' }, { noScroll: true });
  await S('plan-card', q('.new-pricing_plan-card').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A plan card (new-pricing_plan-card): plan name, description, price, job-slot stepper and feature list.', sel: '.new-pricing_plan-card' }, { noScroll: true });
  await S('plan-stepper-plus', q('.new-pricing_plan-card [job-slots-plus]').filter({ visible: true }).first(), ['default', 'hover', 'pressed'], { group: g, title: 'Job-slot stepper', desc: 'The plus icon in a plan card\'s job-slot stepper — a local stepper that changes the quoted price; measured, and the minus side paints .disabled.', sel: '[job-slots-plus]' }, { noScroll: true });
  await S('plan-stepper-minus', q('.new-pricing_plan-card [job-slots-minus]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Job-slot minus (disabled)', desc: 'The minus icon at the stepper\'s floor — painted with a .disabled class.', sel: '[job-slots-minus].disabled' }, { noScroll: true });
  await S('plan-button', q('a.new-pricing_button, a.pricing_button').filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A "Start free trial" button inside a plan card; links to /trial, never followed.', sel: 'a.new-pricing_button' }, { noScroll: true });
  await S('plan-feature', q('.new-pricing_plan-feature-wrap, .new-pricing_plan-feature-tab').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan feature row', desc: 'A feature row inside a plan card (icon + text).', sel: '.new-pricing_plan-feature-tab' }, { noScroll: true });
  // The "Compare plans" table sits in .section_compare.is-hide — the public
  // page keeps it display:none, so the honest reading is "present in the
  // DOM, painted hidden"; the selector only matches inside a shown section.
  await S('pricing-table', q('.section_compare:not(.is-hide) .pricing_table-block').filter({ visible: true }).first(), ['default'], { group: g, title: 'Comparison table', desc: 'The plan comparison table lives in .section_compare.is-hide — the public page paints the section hidden, so nothing is measured.', sel: '.section_compare:not(.is-hide) .pricing_table-block' });
  await S('pricing-table-head', q('.section_compare:not(.is-hide) .pricing_table-block-heading').filter({ visible: true }).first(), ['default'], { group: g, title: 'Table header cell', desc: 'A header cell in the comparison table — unreachable while the section is hidden.', sel: '.section_compare:not(.is-hide) .pricing_table-block-heading' });
  await S('pricing-table-row', q('.section_compare:not(.is-hide) .pricing_table-row').filter({ visible: true }).first(), ['default'], { group: g, title: 'Table row', desc: 'A feature row in the comparison table — unreachable while the section is hidden.', sel: '.section_compare:not(.is-hide) .pricing_table-row' });
  await S('faq-item', q('.faq .h-new_features-item, .pricing_faq-block .h-new_features-item, .h-new_features-item.w-dropdown').filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'FAQ item', desc: 'A pricing FAQ accordion item; opened with its own toggle.', sel: '.h-new_features-item' }, { noScroll: true, before: { opened: async (loc) => { await toggle(loc.locator('.w-dropdown-toggle').first()); await page.waitForTimeout(1000); return 'own w-dropdown-toggle'; } } });
  await S('faq-answer', q('.faq_rich').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ answer', desc: 'The rich-text body of an opened FAQ item.', sel: '.faq_rich after open' }, { noScroll: true, noReset: true, open: async () => { const t = q('.faq .h-new_features-item .w-dropdown-toggle, .pricing_faq-block .w-dropdown-toggle, .h-new_features-item.w-dropdown .w-dropdown-toggle').first(); if (await t.count()) await t.click().catch(() => {}); await page.waitForTimeout(1000); } });
  await S('pricing-cta', q('a.pricing_button.on-cta, a.btn-primary_new.is-icon.is-large').filter({ visible: true }).first(), B4, { group: g, title: 'Pricing CTA', desc: 'The closing trial CTA on the pricing page.', sel: 'a.pricing_button.on-cta' });
  save();
}

async function ats() {
  if (!(await newPage('ats'))) return;
  const g = G.ats;
  await S('ats-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'ATS title', desc: 'The /ats product page headline.', sel: 'h1' }, { noScroll: true });
  await S('ats-card', q('.new-ats_card').filter({ visible: true }).first(), ['default'], { group: g, title: 'ATS card', desc: 'A product card on the ATS page (new-ats_card: heading, image, bottom text).', sel: '.new-ats_card' });
  await S('ats-feature-item', q('.new-ats_feature-item').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature item', desc: 'A feature row on the ATS product page (new-ats_feature-item).', sel: '.new-ats_feature-item' });
  // Bind every state to the same component type: the bare `a` branch could
  // pick a classless "Learn more" link on a re-resolve, mixing one control's
  // default with another's hover.
  await S('ats-tab', q('.new-ats_features-body a.new-ats_feature-item').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'ATS feature link', desc: 'A feature-item link inside the ATS features body; the tab script paints the inactive copies display:none.', sel: '.new-ats_features-body a.new-ats_feature-item' });
  await S('ats-integrate-card', q('.new-ats_integrate-card').filter({ visible: true }).first(), ['default'], { group: g, title: 'Integration card', desc: 'An integrations card on the ATS page (new-ats_integrate-card).', sel: '.new-ats_integrate-card' });
  save();
}

async function careers() {
  if (!(await newPage('careers', { wait: 10000, promo: 'keep' }))) return;
  const g = G.careers;
  // The careers site's own cookie banner, measured at rest before closePromo
  // hides it — never answered.
  await S('cookie-banner', q('[class*="CookieBanner"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Cookie banner', desc: 'The careers site\'s consent banner (CookieBanner), measured at rest then hidden for every other reading — never answered.', sel: '[class*=CookieBanner]' }, { noScroll: true });
  await closePromo(page);
  await S('careers-header', q('.career-site-header, .job-blocks').filter({ visible: true }).first(), ['default'], { group: g, title: 'Careers header', desc: 'The careers site header block (job-blocks career-site-header): company intro and share links.', sel: '.career-site-header' }, { noScroll: true });
  await S('careers-logo', q('a.company-logo-link').filter({ visible: true }).first(), ['default'], { group: g, title: 'Careers logo', desc: 'The company logo link at the top of the careers site.', sel: 'a.company-logo-link' }, { noScroll: true });
  await S('careers-share', q('a.social-icon-btn, a[href^="javascript:"]').filter({ visible: true }).first(), B4, { group: g, title: 'Share button', desc: 'A share-this-site social icon button in the careers header; measured never pressed.', sel: 'a.social-icon-btn' }, { noScroll: true });
  await S('careers-all-jobs', q('a.btn-all-jobs, a.button').filter({ visible: true }).first(), B4, { group: g, title: 'See-all-jobs button', desc: 'The "See all jobs" button — scrolls to the job list.', sel: 'a.btn-all-jobs' }, { noScroll: true });
  await S('careers-filter', q('button[class*="BaseButton__button"]').filter({ visible: true }).first(), B4, { group: g, title: 'Filter button', desc: 'A job-list filter pill (Department/Location/Job type) — opens a filter popover.', sel: 'button[class*=BaseButton__button]' }, { noScroll: true });
  await S('careers-job-card', q('a[class*="JobListItems__listItem"]').filter({ visible: true }).first(), B4, { group: g, title: 'Job card', desc: 'A job listing row (title + location + department); links to the job page, never followed.', sel: 'a[class*=JobListItems__listItem]' });
  await S('careers-carousel', q('button.control.next').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Carousel control', desc: 'The next-arrow of the careers photo carousel (local UI control).', sel: 'button.control.next' });
  save();
}

async function job() {
  if (!(await newPage('job', { wait: 9000 }))) return;
  const g = G.careers;
  await S('job-title', q('h1, .job-header-title').filter({ visible: true }).first(), ['default'], { group: g, title: 'Job title', desc: 'The open-application page heading (jobs.homerun.co/open/en).', sel: 'h1' }, { noScroll: true });
  await S('job-apply', q('a.btn-apply, a.button').filter({ hasText: /apply/i }).first(), B4, { group: g, title: 'Apply button', desc: 'The "Apply now" button on a job page; links to the application form, measured never followed.', sel: 'a.btn-apply' }, { noScroll: true });
  await S('job-prose', q('.vacancy-text, article').filter({ visible: true }).first(), ['default'], { group: g, title: 'Job body', desc: 'The job description prose block (vacancy-text).', sel: '.vacancy-text' });
  await S('job-share', q('.share-job a, a.social-icon-btn').filter({ visible: true }).first(), B4, { group: g, title: 'Share link', desc: 'A share-this-job link (X/LinkedIn); measured never followed.', sel: '.share-job a' }, { noScroll: true });
  await S('job-back', q('a.back-to-career-site').filter({ visible: true }).first(), B4, { group: g, title: 'Back link', desc: 'The back-to-career-site link at the job page top; measured never followed.', sel: 'a.back-to-career-site' }, { noScroll: true });
  save();
}

async function apply() {
  if (!(await newPage('apply', { wait: 10000 }))) return;
  const g = G.apply;
  // The public open-application form, at rest: measured never submitted.
  await S('apply-steps', q('nav.progressbar ul.nav-tabs, nav.progressbar, ul.nav-tabs').filter({ visible: true }).first(), ['default'], { group: g, title: 'Form steps', desc: 'The 4-step indicator (Your details / Questions / Preview / Submit).', sel: 'nav.progressbar ul.nav-tabs' }, { noScroll: true });
  await S('apply-field', q('input[name="first_name"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Text field', desc: 'A text input in the application form; focused locally, never submitted.', sel: 'input[name=first_name]' }, { noScroll: true });
  await S('apply-email', q('input[name="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Email field', desc: 'The email input in the application form; focused locally, never submitted.', sel: 'input[name=email]' }, { noScroll: true });
  await S('apply-file', q('.file-drop').filter({ visible: true }).first(), ['default'], { group: g, title: 'File dropzone', desc: 'The resume upload dropzone (.file-drop wraps the hidden native file input); measured at rest, nothing uploaded.', sel: '.file-drop' }, { noScroll: true });
  await S('apply-checkbox', q('label.checkbox-container').filter({ visible: true }).first(), ['default'], { group: g, title: 'Consent checkbox', desc: 'A data-consent checkbox row (label.checkbox-container paints the custom box around the hidden input); never ticked.', sel: 'label.checkbox-container' }, { noScroll: true });
  await S('apply-next', q('button.tab-control').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Next-step button', desc: 'The "Next: Questions" control — measured never pressed (it advances the wizard; the final Submit is never reached).', sel: 'button.tab-control.next' }, { noScroll: true });
  await S('apply-back', q('a[class*="btn-back"]').filter({ visible: true }).first(), B4, { group: g, title: 'Back link', desc: 'The back-to-job link in the application bar; measured never followed.', sel: 'a.btn-back' }, { noScroll: true });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 16000 }))) return;
  const g = G.signin;
  // app.homerun.co/login is the ATS sign-in surface: the card, SSO buttons
  // and the email/password fields are measured; nothing is typed or sent.
  await S('signin-card', q('[class*="Login__container"], [class*="public__form-container"], .auth-login').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in card', desc: 'The app.homerun.co login card the Angular SPA paints (ATS/HR variant tabs, SSO buttons, email/password). Measured at rest, never submitted.', sel: '[class*=Login__container]' }, { noScroll: true });
  await S('signin-tab', q('a[class*="Login__platform-button"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Product tab', desc: 'The ATS/HR product tab at the card top (the HR variant links to app.homerun.hr; measured never followed).', sel: 'a[class*=Login__platform-button]' }, { noScroll: true });
  await S('signin-sso', q('button[class*="sso-button"]').filter({ visible: true }).first(), B4, { group: g, title: 'SSO button', desc: '"Log in with Google" — an SSO button on the card; measured never pressed.', sel: 'button[class*=sso-button]' }, { noScroll: true });
  await S('signin-email', q('input[type="email"], input[name="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Email field', desc: 'The email input on the sign-in card; focused locally, never submitted.', sel: 'input[type=email]' }, { noScroll: true });
  await S('signin-password', q('input[type="password"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Password field', desc: 'The password input; measured at rest, never typed.', sel: 'input[type=password]' }, { noScroll: true });
  await S('signin-button', q('button.h-button').filter({ hasText: /log in/i }).first(), B4, { group: g, title: 'Log-in button', desc: 'The "Log in" submit-style button (h-button-secondary); measured never pressed.', sel: 'button.h-button-secondary' }, { noScroll: true });
  await S('signin-link', q('a.h-button-link').filter({ visible: true }).first(), B4, { group: g, title: 'Account link', desc: '"I don\'t have an account" / "Forgot your password?" — link-styled controls; measured never followed.', sel: 'a.h-button-link' }, { noScroll: true });
  save();
}

async function signinhr() {
  if (!(await newPage('signinhr', { wait: 12000 }))) return;
  const g = G.signinhr;
  // app.homerun.hr/Account/Logon is the .NET HR sign-in: the server-rendered
  // form is measured; nothing is typed or sent.
  await S('hr-card', q('xpath=//input[@type="password"]/ancestor::*[contains(@class,"form") or self::form][last()]').filter({ visible: true }).first(), ['default'], { group: g, title: 'HR sign-in card', desc: 'The app.homerun.hr logon card (the outermost form container). Measured at rest, never submitted.', sel: 'outermost form ancestor of the password input' }, { noScroll: true });
  await S('hr-field', q('input.public-form__input[type="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'HR email field', desc: 'The email input (public-form__input); focused locally, never submitted.', sel: 'input.public-form__input[type=email]' }, { noScroll: true });
  await S('hr-password', q('input.public-form__input[type="password"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'HR password field', desc: 'The password input; measured at rest, never typed.', sel: 'input.public-form__input[type=password]' }, { noScroll: true });
  await S('hr-button', q('button.public-form__button').filter({ visible: true }).first(), B4, { group: g, title: 'HR log-in button', desc: 'The "Log in" button (public-form__button); measured never pressed.', sel: 'button.public-form__button' }, { noScroll: true });
  await S('hr-link', q('a.public-form__button--link, a[href*="forgottenpassword"]').filter({ visible: true }).first(), B4, { group: g, title: 'HR account link', desc: '"I don\'t have an account" / "Forgot your password?" — measured never followed.', sel: 'a.public-form__button--link' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('.nav-new.is-v2.is-mobile, .nav-primary, .w-nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile bar', desc: 'The 390 mobile nav bar: logo + hamburger + trial button.', sel: '.nav-new.is-mobile at 390' }, { noScroll: true });
  // The hamburger exists twice in the DOM — the painted copy gets a marker.
  await page.evaluate(() => {
    const e = [...document.querySelectorAll('.w-nav-button')].find((x) => x.offsetParent && x.getBoundingClientRect().width > 0);
    if (e) e.setAttribute('data-m-menu', '1');
  });
  await S('m-menu-button', q('[data-m-menu="1"]'), ['default'], { group: g, title: 'Menu button', desc: 'The hamburger (the painted w-nav-button copy); its own press opens the menu sheet.', sel: 'visible .w-nav-button' }, { noScroll: true });
  // The hamburger is a local toggle (never a link). A synthetic el.click()
  // is the only press that reaches it through the nav's pointer-event
  // layering, and the open is verified — a failed or double toggle is
  // retried rather than trusting the one shot.
  const menuIsOpen = () => page.evaluate(() => [...document.querySelectorAll('.nav_menu-new.is-mobile, .w-nav-menu')].some((e) => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 40; })).catch(() => false);
  const openMenu = async () => {
    for (let i = 0; i < 4; i++) {
      if (await menuIsOpen()) return true;
      await page.evaluate(() => { const e = document.querySelector('[data-m-menu="1"]') || [...document.querySelectorAll('.w-nav-button')].find((x) => x.offsetParent && x.getBoundingClientRect().width > 0); if (e) e.click(); }).catch(() => {});
      await page.waitForTimeout(1100);
    }
    return menuIsOpen();
  };
  await S('m-menu-open', q('.nav_menu-new.is-mobile, .w-nav-menu.w--open'), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The opened mobile menu sheet after the hamburger press.', sel: '.nav_menu-new.is-mobile after toggle press' }, { noScroll: true, noReset: true, open: openMenu });
  await S('m-menu-link', q('.nav_menu-new.is-mobile a, .w-nav-menu.w--open a'), B4, { group: g, title: 'Menu link', desc: 'A link row inside the open mobile menu.', sel: 'first link inside the open menu' }, { noScroll: true, noReset: true, open: openMenu });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The hero headline at 390.', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme (app.homerun.co/login and app.homerun.hr/Account/Logon are sign-in boundaries)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, ats, careers, job, apply, signin, signinhr, mobile };
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
