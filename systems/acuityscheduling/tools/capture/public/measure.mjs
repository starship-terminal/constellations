// Measures acuityscheduling.com's public components in every state reachable
// without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing getstarted login mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// acuityscheduling.com is Squarespace's scheduling marketing site: server-
// rendered pages with BEM-ish classes (menu-container, dropdown__,
// frontsite-footer, phase2-plan-*). Nothing is sent, bought or signed into:
// the only presses are local UI toggles (nav dropdowns, the pricing FAQ
// accordion, the mobile hamburger menu). The Log in / Get started pages are
// Squarespace's public auth gate — photographed and state-forced, never
// submitted. Consent banners are hidden remove-only.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, killGeo, domClick, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/',
  pricing: '/pricing',
  getstarted: '/get-started?type=professional',
  login: 'https://secure.acuityscheduling.com/login?nav=1',
  mobile: '/',
};
let page, cdp, current, context, run;
const touched = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /something went wrong|performing security verification|verifying you are human|just a moment|page cannot be found/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

// ---------- helpers ----------

async function newPage(key, { mobile = false, promo = 'close', wait = 6000 } = {}) {
  current = key;
  const b = context.browser();
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  page.setDefaultTimeout(8000);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '');
  for (let attempt = 0; attempt < 3; attempt++) {
    await open(page, URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { wait, promo });
    if (!(await blocked())) break;
    log('  blocked pass', attempt + 1, '- reloading');
  }
  if (await blocked()) { log('  BLOCKED', key); return false; }
  if (promo === 'close') await killGeo(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
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

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FILL = ""; // never type into login or signup

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
    let s;
    try {
      s = await styleOf(loc);
    } catch (e) {
      await page.waitForTimeout(1500);
      s = await styleOf(target.filter({ visible: true }).first());
    }
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
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  delete out.components[key].missing;
  if (opts.open) { await reset(); await opts.open(); }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
    if (!has) out.components[key].missing = true;
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
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.keyboard.type(opts.fillText || FILL, { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || FILL}", then deleted; nothing sent`;
      } else via = via || 'at rest';
      if (via === 'focus failed') {
        // The element never took focus: a resting read labelled focus-visible is
        // not a captured focus, so the attempt is recorded as an error instead.
        out.components[key].states[st] = { error: 'keyboard focus could not reach the element', via };
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
  save();
}

// ---------- page runs ----------
const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  gate: 'Auth gate (Squarespace)', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

const openDropdown = async (label) => {
  const t = q('button.dropdown__trigger-link').filter({ hasText: new RegExp(label, 'i') }).filter({ visible: true }).first();
  if (!(await t.count())) return false;
  await t.hover(); await page.waitForTimeout(1300); return true;
};

async function shell() {
  const g = G.shell;
  await S('header', q('.menu-container.frontsite-hero-nav, header').first(), ['default'], { group: g, title: 'Header', desc: 'The fixed top bar at 80px: the Acuity wordmark left; How It Works plus the Solutions / Product / Resources dropdown triggers, Pricing and Log in; the Get started CTA right. Transparent over the hero, opaque after scroll.', sel: '.menu-container.frontsite-hero-nav' }, { noScroll: true });
  await S('logo', q('.menu-container a.navlogo--no-animation, .menu-container a.navlogo__container').filter({ visible: true }).first(), ['default'], { group: g, title: 'Wordmark', desc: 'The Acuity logotype in the header, an SVG lockup that links home.', sel: '.navlogo a svg' }, { noScroll: true });
  await S('nav-link', q('.menu-container a').filter({ hasText: /how it works/i }).first(), B4, { group: g, title: 'Nav link', desc: 'A direct header link (How It Works, Pricing).', sel: 'header a "How It Works"' }, { noScroll: true });
  await S('nav-trigger', q('button.dropdown__trigger-link').filter({ hasText: /solutions/i }).first(), B4, { group: g, title: 'Nav dropdown trigger', desc: 'A hoverable dropdown trigger (Solutions, Product, Resources): a nav item that opens a mega-menu of industry / feature links.', sel: 'button.dropdown__trigger-link' }, { noScroll: true });
  // The mega-menu only exists while the pointer rests on the trigger, and
  // reset() parks the pointer in the corner, so each state re-hovers first.
  const rehover = async () => { await openDropdown('Solutions'); };
  await S('nav-dropdown', q('.dropdown__content').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav dropdown', desc: 'The Solutions mega-menu under the header: a padded card grid of industry links (Beauty, Business Services, Wellness, Fitness, Visual and Performing Arts, Education).', sel: '.dropdown__content' }, { noScroll: true, open: rehover, before: { default: rehover } });
  await S('dropdown-item', q('.dropdown__content a.solutions-grid__item, .dropdown__content a').filter({ visible: true }).first(), B4, { group: g, title: 'Dropdown item', desc: 'An industry link inside the mega-menu: a bold name with a grey one-line description.', sel: '.dropdown__content a' }, { noScroll: true, open: rehover, before: { default: rehover, hover: rehover, 'focus-visible': rehover, pressed: rehover } });
  await S('login-link', q('.menu-container a').filter({ hasText: /log in/i }).first(), B4, { group: g, title: 'Log in link', desc: 'The Log in entry in the header, an <a> to the Squarespace sign-in gate. Hovered and focused, never followed.', sel: 'header "Log in"' }, { noScroll: true });
  await S('nav-cta', await domFind(page, /^get started$/i, { sel: '.menu-container a, .menu-container button', tag: 'nc', minH: 20 }), B4, { group: g, title: 'Nav CTA', desc: 'The Get started button in the header: the signup CTA.', sel: 'header "Get started"' }, { noScroll: true });
}

async function footerRun() {
  const g = G.footer;
  await S('footer', q('footer.frontsite-footer, footer').first(), ['default'], { group: g, title: 'Footer', desc: 'The page foot: a Squarespace logo mark, link columns under collapsible headings (Get Started, Features, Solutions, Resources), social icons and legal links.', sel: 'footer.frontsite-footer' });
  await S('footer-col-title', q('footer button.footer-link-title').first(), B4, { group: g, title: 'Footer column title', desc: 'A footer column heading (Get Started, Features, Solutions, Resources): a button that expands the column on narrow screens.', sel: 'button.footer-link-title' });
  await S('footer-link', q('footer a').filter({ hasText: /pricing|online booking|about us/i }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer column link (Home, About Us, Pricing, Online Booking).', sel: 'footer a' });
  const social = q('footer a[href*="instagram.com"], footer a[href*="facebook.com"]').first();
  await S('social-link', social, B4, { group: g, title: 'Social link', desc: 'A social icon link in the footer (Instagram, Pinterest, Facebook, LinkedIn, YouTube): the mark is painted as a background image, not an inline SVG.', sel: 'footer a[href*=instagram.com]' });
  await S('footer-legal', q('footer a').filter({ hasText: /terms|privacy/i }).first(), B4, { group: g, title: 'Legal link', desc: 'A legal foot link (Terms of Service, Privacy Policy).', sel: 'footer legal a' });
}

async function home() {
  if (!(await newPage('home'))) { await page.context().close(); return; }
  await sheetsFor('home');
  await shell();
  const h = G.home;
  await S('hero', q('section.hero-block').first(), ['default'], { group: h, title: 'Hero', desc: 'The opening band: the 40px "Scheduling software to power exceptional client experiences" headline, the signup pair and a product booking-page mock. Measured at rest.', sel: 'section.hero-block' });
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: 'The 40px Clarkson headline.', sel: 'hero h1' });
  await S('hero-sub', q('section.hero-block p, section.hero-block [class*=sub]').filter({ hasText: /book appointments/i }).first(), ['default'], { group: h, title: 'Hero sub', desc: 'The supporting line under the title ("Book appointments, take payments, and automate the busywork…").', sel: 'hero sub' });
  await S('hero-cta-email', q('a.hero-cta-email').first(), B4, { group: h, title: 'Sign up with email', desc: 'The hero signup button: a 56px 12px-radius control, followed to the account gate only in captures — never pressed here.', sel: 'a.hero-cta-email' });
  await S('hero-cta-google', q('a.hero-cta-google').first(), B4, { group: h, title: 'Sign up with Google', desc: 'The Google signup button beside the email one, with the G glyph.', sel: 'a.hero-cta-google' });
  await S('hero-terms', q('p.hero-cta-terms').first(), ['default'], { group: h, title: 'Signup legal line', desc: 'The "By creating an account, you agree to our Terms of Service…" line under the buttons.', sel: 'p.hero-cta-terms' });
  await S('vertical-card', q('a.verticals-section__card').first(), B4, { group: h, title: 'Industry card', desc: 'A tile in "Acuity is for anyone in the business of time" (Beauty, Business Services, Wellness, Fitness, Visual and Performing Arts, Education): a named card with an image and a one-line descriptor, linking the industry page.', sel: 'a.verticals-section__card' });
  await S('vertical-cta', q('.verticals-section__cta').first(), B4, { group: h, title: 'Industries CTA', desc: '"Explore all industries" under the grid.', sel: '.verticals-section__cta' });
  const fcard = await page.evaluate(() => {
    const el = [...document.querySelectorAll('.feature-area-card, [class*=feature-area] > *')].filter((n) => {
      const r = n.getBoundingClientRect(); return r.height > 200 && r.height < 700 && /feature/i.test(n.className || '') && n.querySelector('h3, .feature-area-card__header');
    })[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'fc'); return true;
  });
  await S('feature-card', fcard ? q('[data-m-mark="fc"]') : q('.feature-area-card').first(), ['default', 'hover'], { group: h, title: 'Feature card', desc: 'A card in "Everything you need to run your business" (Book beautifully 24/7, Reduce no-shows, Automate your day, Boost your earnings): an image, a 24px header and body text.', sel: '.feature-area-card' });
  await S('feature-card-title', q('.feature-area-card__header').first(), ['default'], { group: h, title: 'Feature card title', desc: 'A 24px feature card header.', sel: '.feature-area-card__header' });
  const tcard = await page.evaluate(() => {
    const el = [...document.querySelectorAll('.testimonials-carousel *')].filter((n) => {
      const r = n.getBoundingClientRect(); return r.height > 150 && r.height < 600 && /card|slide|item|testimonial/i.test(n.className || '') && (n.innerText || '').length > 60;
    })[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'tc'); return true;
  });
  await S('testimonial-card', tcard ? q('[data-m-mark="tc"]') : q('.testimonials-carousel').first(), ['default'], { group: h, title: 'Testimonial card', desc: 'A quote card in "Real results from professionals just like you".', sel: 'testimonial card' });
  await S('carousel-dots', q('.testimonial-card__dots').filter({ visible: true }).first(), ['default'], { group: h, title: 'Carousel dots', desc: 'The testimonials carousel has no arrows: a .testimonial-card__dots row of thin dash indicators (the active one wider) marks position while slides auto-play.', sel: '.testimonial-card__dots' });
  // A partner mark only: an <img>/<svg> inside the integrations section, never
  // the "View integrations" text link (which matched the earlier any-link probe).
  const integ = await page.evaluate(() => {
    const el = [...document.querySelectorAll('.integrations-v2 img, .integrations-v2 svg, .integrations-v2 [class*=logo] img, .integrations-v2 [class*=logo] svg')]
      .filter((n) => n.getBoundingClientRect().width > 30 && n.getBoundingClientRect().height > 20)[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'ig'); return true;
  });
  await S('integration-logo', integ ? q('[data-m-mark="ig"]') : q('.integrations-v2 img').first(), ['default'], { group: h, title: 'Integration logo', desc: 'A partner mark in "Connect your calendar and so much more" (Google, Outlook, Stripe…).', sel: '.integrations-v2 img' });
  await S('bottom-cta', q('section.bottom-cta').first(), ['default'], { group: h, title: 'Bottom CTA', desc: 'The closing "Get started for free" band before the footer.', sel: 'section.bottom-cta' });
  await footerRun();
  await page.context().close();
}

async function pricing() {
  if (!(await newPage('pricing'))) { await page.context().close(); return; }
  await sheetsFor('pricing');
  const g = G.pricing;
  await S('pricing-hero', q('.pricing-hero-plans-wrapper').first(), ['default'], { group: g, title: 'Pricing plans block', desc: 'The plan cards row: three or four tiers each with a name, blurb, monthly price, feature list and a CTA.', sel: '.pricing-hero-plans-wrapper' });
  await S('plan-card', q('.plan.phase2-plan').first(), ['default', 'hover'], { group: g, title: 'Plan card', desc: 'A pricing tier card (~447x436): name, price, feature list with tooltip markers, Start free trial CTA.', sel: '.plan.phase2-plan' });
  await S('plan-name', q('.phase2-plan-title').first(), ['default'], { group: g, title: 'Plan name', desc: 'The tier name on a plan card (Starter, Emerging, Growing, Powerhouse), a .phase2-plan-title div.', sel: '.phase2-plan-title' });
  await S('plan-price', q('.phase2-plan-price').first(), ['default'], { group: g, title: 'Plan price', desc: 'The monthly price figure on a tier card.', sel: '.phase2-plan-price' });
  await S('plan-cta', q('a.phase2-cta.cta-desktop').first(), B4, { group: g, title: 'Plan CTA', desc: 'The "Start free trial" button on a tier card: measured and state-forced, never followed.', sel: 'a.phase2-cta' });
  await S('plan-feature', q('.plan.phase2-plan .feature').first(), ['default', 'hover'], { group: g, title: 'Plan feature row', desc: 'A feature line in a plan card; the marker holds a tooltip on hover.', sel: '.phase2-plan .feature' });
  await S('faq-accordion', q('.faq-accordion-container').first(), ['default'], { group: g, title: 'FAQ accordion', desc: 'The pricing FAQ: button.accordion-title questions expanding .accordion-panel answers.', sel: '.faq-accordion-container' });
  await S('accordion-title', q('button.accordion-title').first(), B4, { group: g, title: 'FAQ question', desc: 'An accordion question row; pressing it is a local toggle that reveals the answer.', sel: 'button.accordion-title' });
  // Press the first question — a local expand toggle — then measure the open panel.
  const at = q('button.accordion-title').filter({ visible: true }).first();
  if (await at.count()) {
    await at.scrollIntoViewIfNeeded();
    await at.click({ timeout: 5000 }).catch(() => at.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    const expanded = await page.evaluate(() => {
      const el = [...document.querySelectorAll('.accordion-panel')].find((n) => n.getBoundingClientRect().height > 20);
      if (!el) return false; el.setAttribute('data-m-mark', 'ap'); return true;
    });
    await S('accordion-panel', expanded ? q('[data-m-mark="ap"]') : q('.accordion-panel').first(), ['default'], { group: g, title: 'FAQ answer', desc: 'An expanded accordion answer, opened through its own question toggle.', sel: '.accordion-panel open' });
    await S('accordion-title-open', q('button.accordion-title.accordion-active, button.accordion-title[aria-expanded="true"]').first(), ['default'], { group: g, title: 'FAQ question, open', desc: 'The question in its expanded state (accordion-active / aria-expanded).', sel: 'button.accordion-title.open' });
  }
  await footerRun();
  await page.context().close();
}

async function getstarted() {
  // The Squarespace "Create your account" dialog /get-started lands on.
  if (!(await newPage('getstarted'))) { await page.context().close(); return; }
  const g = G.gate;
  await S('gate-card', q('[class*=Dialog-container], [role=dialog], main').first(), ['default'], { group: g, title: 'Create-account card', desc: 'The Squarespace account gate "Create your account": a centred ~540px card with provider buttons and legal links — the start of the signup flow, never submitted.', sel: 'dialog card' });
  await S('gate-google', await domFind(page, /continue with google/i, { sel: 'button, a', tag: 'gg', minH: 30 }), B4, { group: g, title: 'Continue with Google', desc: 'The Google OAuth row on the create-account card. Measured, never pressed.', sel: '"Continue with Google" button' });
  await S('gate-apple', await domFind(page, /continue with apple/i, { sel: 'button, a', tag: 'ga', minH: 30 }), B4, { group: g, title: 'Continue with Apple', desc: 'The Apple OAuth row. Measured, never pressed.', sel: '"Continue with Apple" button' });
  await S('gate-email', await domFind(page, /continue with email/i, { sel: 'button, a', tag: 'ge', minH: 30 }), B4, { group: g, title: 'Continue with Email', desc: 'The email signup row — leads to an email field on the next step, which is not reached.', sel: '"Continue with Email" button' });
  const mo = await domFind(page, /more options/i, { sel: 'button, a', tag: 'mo', minH: 20 });
  await S('more-options', mo, B4, { group: g, title: 'More options expander', desc: 'The "MORE OPTIONS" text expander revealing further providers — a local toggle.', sel: '"MORE OPTIONS" button' });
  // Press it (a local toggle) and measure the revealed provider list.
  if (await mo.count()) {
    await mo.first().click({ timeout: 4000 }).catch(() => mo.first().evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    const extra = await page.evaluate(() => {
      const el = [...document.querySelectorAll('button, a')].filter((n) => /microsoft|facebook|other/i.test(n.innerText || '') && n.getBoundingClientRect().height > 20)[0];
      if (!el) return false; el.setAttribute('data-m-mark', 'xp'); return true;
    });
    await S('more-options-open', extra ? q('[data-m-mark="xp"]') : mo.first(), ['default'], { group: g, title: 'Extra provider, revealed', desc: 'A provider row revealed by MORE OPTIONS.', sel: 'extra provider' });
  }
  await page.context().close();
}

async function login() {
  if (!(await newPage('login'))) { await page.context().close(); return; }
  const g = G.gate;
  const lcard = await page.evaluate(() => {
    const inp = document.querySelector('input[type=email], input[type=password]');
    if (!inp) return false;
    for (let n = inp; n; n = n.parentElement) {
      const r = n.getBoundingClientRect();
      if (r.width > 250 && r.width < 1200 && r.height > 250) { n.setAttribute('data-m-mark', 'lc'); return true; }
    }
    return false;
  });
  await S('login-card', lcard ? q('[data-m-mark="lc"]') : q('main').first(), ['default'], { group: g, title: 'Sign-in card', desc: 'The Squarespace "Log into Acuity Scheduling with your Squarespace account" card (styled-components css-* classes): email and password fields, LOG IN, OR divider, OAuth rows — the gate for the app, never submitted.', sel: 'login card' });
  await S('login-email', q('input[type=email], input[name=email]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The EMAIL ADDRESS field; typed and deleted, never submitted.', sel: 'input[name=email]' });
  await S('login-password', q('input[type=password]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Password field', desc: 'The PASSWORD field; focused only, never typed.', sel: 'input[type=password]' });
  await S('login-submit', await domFind(page, /^log in$/i, { sel: 'button, [type=submit]', tag: 'ls', minH: 30 }), B4, { group: g, title: 'Log in button', desc: 'The LOG IN submit. Measured, never pressed.', sel: 'LOG IN button' });
  await S('oauth-google', await domFind(page, /continue with google/i, { sel: 'button, a', tag: 'og', minH: 30 }), B4, { group: g, title: 'OAuth Google', desc: 'The Google OAuth row on the sign-in card. Measured, never pressed.', sel: '"Continue with Google"' });
  await S('oauth-apple', await domFind(page, /continue with apple/i, { sel: 'button, a', tag: 'oa', minH: 30 }), B4, { group: g, title: 'OAuth Apple', desc: 'The Apple OAuth row.', sel: '"Continue with Apple"' });
  await S('oauth-facebook', await domFind(page, /continue with facebook/i, { sel: 'button, a', tag: 'of', minH: 30 }), B4, { group: g, title: 'OAuth Facebook', desc: 'The Facebook OAuth row.', sel: '"Continue with Facebook"' });
  await S('cant-login', await domFind(page, /can.?t log in/i, { sel: 'a, button', tag: 'cl', minH: 10 }), B4, { group: g, title: "Can't log in link", desc: 'The recovery link under the OAuth rows.', sel: '"CAN\'T LOG IN?"' });
  await S('create-account-link', await domFind(page, /create account/i, { sel: 'a, button', tag: 'ca', minH: 10 }), B4, { group: g, title: 'Create account link', desc: 'The CREATE ACCOUNT tab beside LOG IN on the gate.', sel: '"CREATE ACCOUNT" link' });
  await page.context().close();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true }))) { await page.context().close(); return; }
  const g = G.mobile;
  await S('m-header', q('.menu-container.frontsite-hero-nav, header').first(), ['default'], { group: g, title: 'Mobile header', desc: 'The bar at 390: 55px, wordmark and a hamburger.', sel: '.menu-container' }, { noScroll: true });
  await S('m-hamburger', q('button.hamburger-icon').filter({ visible: true }).first(), B4, { group: g, title: 'Hamburger button', desc: 'The menu trigger; opens the full-screen menu.', sel: 'button.hamburger-icon' }, { noScroll: true });
  // The hamburger has no innerText, so domClick's text match cannot fire:
  // click the first visible .hamburger-icon element directly.
  const opened = await page.evaluate(() => { const b = [...document.querySelectorAll('button.hamburger-icon')].find((n) => n.getBoundingClientRect().width > 0); if (!b) return false; b.click(); return true; }).catch(() => false);
  await page.waitForTimeout(1200);
  const menu = await page.evaluate(() => {
    const el = [...document.querySelectorAll('.mobile-menu-container, nav, [class*=menu]')].filter((n) => {
      const r = n.getBoundingClientRect(); return r.width > 200 && r.height > 300 && /how it works|solutions|pricing/i.test(n.innerText || '');
    })[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'mm'); return true;
  });
  await S('m-menu', menu ? q('[data-m-mark="mm"]') : q('.mobile-menu-container').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu', desc: 'The full-height menu the hamburger opens (.mobile-menu-container): primary links stacked.', sel: '.mobile-menu-container' }, { noScroll: true });
  // Keep the union narrow: the menu header's .logo anchor precedes the links in
  // DOM order, so falling back to `[data-m-mark="mm"] a` measured the wordmark.
  await S('m-menu-link', q('[data-m-mark="mm"] a.mobile-link').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile menu link', desc: 'A primary link in the mobile menu.', sel: '.mobile-menu-primary a.mobile-link' }, { noScroll: true });
  await S('m-hero', q('section.hero-block').first(), ['default'], { group: g, title: 'Mobile hero', desc: 'The hero at 390.', sel: 'section.hero-block' }, { open: async () => { await page.keyboard.press('Escape').catch(() => {}); await page.evaluate(() => { document.querySelectorAll('.mobile-menu-container').forEach((n) => { n.style.display = 'none'; }); }); await page.waitForTimeout(500); } });
  await page.context().close();
}

run = new Date().toISOString();
const which = process.argv.slice(2).flatMap((a) => a.split(',')).filter(Boolean);
const ALL = { home, pricing, getstarted, login, mobile };
let browser;
({ browser, context } = await launch());
for (const [k, fn] of Object.entries(ALL)) {
  if (which.length && !which.includes(k)) continue;
  for (let attempt = 0; attempt < 3; attempt++) {
    try { await fn(); break; } catch (e) {
      log('RUN FAILED', k, e.message);
      if (!/closed|crash|Terminated|target/i.test(e.message) || attempt === 2) break;
      try { await browser.close(); } catch {}
      ({ browser, context } = await launch());
      log('  relaunched browser, retrying', k);
    }
  }
  save();
}
save();
console.log('components:', Object.keys(out.components).length);
await browser.close();
