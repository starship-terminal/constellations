// Measures forhers.com's public components in every state reachable without
// signing in, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home weight-loss hair-loss skin-care mental-health birth-control
// product anti-aging wegovy-pill labs benefits quality blog blog-post
// bmi-calculator drugs-info mhome mwl mbmi mproduct mblogpost.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// www.forhers.com answers every request from this network with a Cloudflare
// managed challenge, so the DOM evidence is Wayback Machine SSR snapshots
// served locally by lib.mjs's servePages — the marketing stack's inline
// styled-components sheets and the /shop stack's archived CSS bundles paint
// statically with all scripts stripped. The site paints one light theme.
// Specs select by data-testid hooks, role, aria-label or the semantic
// CSS-module/styled-components class prefixes, never by copy. Because no
// script runs, opens and toggles hydration owns (the slide menu, the Log-in
// menu, accordion panels, the A-Z browse jump, quiz starts) cannot paint:
// those states are recorded as gaps, not faked. Hover is a real pointer
// hover, focus-visible a real keyboard focus, pressed is forced with
// DevTools CSS.forcePseudoState so no link or button ever fired, filled is
// text typed into a field and deleted again — never submitted. The
// regional-redirect card is measured as the dialog it is, then hidden.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, servePages, launch, open, closePromo, patch, domFind, styleOf, crop, centre, RAW, SCRATCH, PAGES, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
let page, cdp, current, srv, port, browser, run, liveCtx;
const touched = new Set();
const listed = new Map();
const failedPages = new Set();
const URLS = Object.fromEntries(Object.entries(PAGES).map(([k, v]) => [k, v.url]));

// Mobile passes reuse a desktop page file; name the map instead of stripping an "m".
const PAGE_OF = { mhome: 'home', mwl: 'weight-loss', mbmi: 'bmi-calculator', mproduct: 'product', mblogpost: 'blog-post' };

async function newPage(key, { mobile = false, wait = 7000 } = {}) {
  current = PAGE_OF[key] || key;
  if (!PAGES[current]) throw new Error(`no page file for ${key}`);
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = browser;
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(9000);
  log('open', key, mobile ? '(mobile)' : '');
  await page.goto(`http://127.0.0.1:${port}/pages/${current}.html`, { waitUntil: 'load', timeout: 120000 }).catch(() => {});
  await page.waitForFunction(() => document.fonts && document.fonts.status === 'loaded', undefined, { timeout: 20000 }).catch(() => {});
  await page.waitForTimeout(wait);
  await closePromo(page);
  const body = await page.evaluate(() => (document.body && document.body.innerText || '').length).catch(() => 0);
  if (body < 200) { log('  EMPTY', key); failedPages.add(key); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return true;
}

// Fixed/sticky chrome with paint order: the z-index map of the page's bars.
async function chrome(key) {
  if (KEYS) return;
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
  Object.assign(c, { page: current, run, url: URLS[current] }, meta);
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
    // Keep the page this state was actually read on. comp() already rewrote the
    // entry's page/url/run for the current pass; a later failed state must not
    // inherit that rewrite.
    c.states[state] = { ...s, crop: file, via: opts.via, page: current, url: URLS[current], run };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    // A failed re-read must not erase an earlier successful one, and must not
    // leave that earlier reading labelled as this page's evidence.
    const prev = c.states[state];
    if (prev && prev.style) {
      prev.rerunError = String(e.message || e).slice(0, 200);
      c.states[state] = { ...prev, excluded: 'failed replacement; earlier reading kept, not republished as this page' };
    } else c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

// KEYS=hero,type-title limits a run to those components.
const KEYS = process.env.KEYS ? new Set(process.env.KEYS.split(',')) : null;

async function S(key, target, list, meta = {}, opts = {}) {
  if (KEYS && !KEYS.has(key)) return;
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
    if (opts.dropPrior) {
      out.components[key].states = {};
      out.components[key].missing = true;
      delete out.components[key].recaptureMissed;
    } else if (!has) out.components[key].missing = true;
    else { Object.assign(out.components[key], keep); out.components[key].recaptureMissed = run; }
    return;
  }
  delete out.components[key].recaptureMissed;
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
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) {
        prev.rerunError = String(e.message || e).slice(0, 200);
        out.components[key].states[st] = { ...prev, excluded: 'failed replacement; earlier reading kept, not republished as this page' };
      } else out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  // A listed state that failed its re-read kept the earlier evidence under
  // rerunError. Restore the entry's page/run/url so that kept reading is not
  // published as this pass.
  if (keep && list.some((st) => out.components[key].states[st]?.rerunError || out.components[key].states[st]?.excluded)) {
    Object.assign(out.components[key], keep);
    out.components[key].recaptureMissed = run;
  }
  await reset();
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FIELD = ['default', 'focused', 'filled'];

const G = {
  shell: 'Header and site chrome',
  home: 'Home page (marketing stack)',
  shop: 'Shop pages (weight-loss, hair, skin, mental-health, birth-control, product, labs, benefits)',
  form: 'Forms and tools (bmi-calculator, lead capture)',
  content: 'Content pages (blog, article, quality, drugs-info)',
  footer: 'Footer',
  mobile: 'Mobile (390 wide)',
};

// ---------------------------------------------------------------- chrome

// The /shop stack chrome: navigation-mast promo bar + nav row, fineprint footer.
// The marketing stack chrome: GlobalNavigation + FooterLink columns.
async function header() {
  const g = G.shell;
  await S('header', q('nav[data-testid="navigation-mast"], [data-testid="navigation-top-bar"], [class*="GlobalNavigation"], header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The top chrome: promo bar over the nav row (wordmark, category links, Log in, hamburger).', sel: 'navigation-mast / GlobalNavigation' }, { noScroll: true });
  await S('promo-bar', q('[data-navigation-banner="true"], [data-testid="navigation-content"], [class*="PromoBar"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Promo bar', desc: 'The lime announcement strip ("Peptides+ is coming soon" / "The GLP-1 pill is here") with a tertiary CTA link.', sel: 'data-navigation-banner' }, { noScroll: true });
  await S('logo', q('a[aria-label*="homepage" i]:has(svg), [class*="Logo"], [class*="_logo"]').filter({ visible: true }).first(), B4, { group: g, title: 'Wordmark', desc: 'The "hers" serif wordmark linking home; measured, never followed.', sel: 'nav logo link' }, { noScroll: true });
  await S('nav-link', q('[data-testid="navigation-mast"] a:visible, nav a[href*="/weight-loss"], nav a[href*="/labs"], [class*="GlobalNavigationItem"] a').filter({ hasText: /weight|treatment|membership|hair|skin|labs|science|blog/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A category link in the nav row; measured, never followed.', sel: 'nav link' }, { noScroll: true });
  await S('login-button', q('button[data-testid="GlobalNavigationLogin"], [class*="GlobalNavigationItemButton"], a:has-text("Log in")').filter({ visible: true }).first(), B4, { group: g, title: 'Log in control', desc: 'The "Log in" button/link; measured, never pressed — its menu and the account are hydration- and auth-gated.', sel: 'GlobalNavigationLogin / Log in link' }, { noScroll: true });
  await S('menu-toggle', q('button[data-testid="GlobalNavigationButton"], button[aria-label*="Slide Menu" i], button[aria-label*="menu" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Menu toggle', desc: 'The hamburger that opens the slide menu; measured, never toggled (the drawer needs hydration).', sel: 'GlobalNavigationButton' }, { noScroll: true });
}

async function footer() {
  const f = G.footer;
  const foot = q('footer').filter({ visible: true }).last();
  await S('footer', foot, ['default'], { group: f, title: 'Footer', desc: 'The site footer: link columns, social icons, legal fineprint row.', sel: 'footer' });
  await S('footer-link', foot.locator('a').filter({ hasText: /Privacy|Terms|Sitemap|About|Blog|Help|Careers/i }).filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', desc: 'A footer column link; measured, never followed.', sel: 'footer a' });
  await S('footer-fineprint', foot.locator('a[class*="fineprint-link"], a').filter({ hasText: /privacy choices|telehealth consent|consumer health/i }).filter({ visible: true }).first(), B4, { group: f, title: 'Fineprint link', desc: 'A legal fineprint link in the footer\'s last row; measured, never followed.', sel: 'fineprint-link' });
  await S('footer-social', foot.locator('a:has(svg)').filter({ visible: true }).first(), B4, { group: f, title: 'Social icon link', desc: 'A social icon link in the footer; measured, never followed.', sel: 'footer a:has(svg)' });
}

// ---------------------------------------------------------------- shared shop components

async function shopChrome() {
  const g = G.shop;
  await S('page-heading', q('h1, h5[data-testid="page-section-headings"] h5, [data-testid="page-section-headings"] h5').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page heading', desc: 'The serif section heading ("Weight loss that works" / "Lose weight the way you want").', sel: 'first h1/section headings' }, { noScroll: true });
  await S('page-dek', q('[data-testid="page-section-remaining"] p, [class*="header_component_remaining"] p').filter({ visible: true }).first(), ['default'], { group: g, title: 'Section dek', desc: 'The body copy beside the section heading.', sel: 'page-section-remaining p' }, { noScroll: true });
  await S('cta-primary', q('a[data-variant="primary"], a[class*="_format-primary-"], button[class*="_format-primary-"]').filter({ visible: true }).first(), B4, { group: g, title: 'Primary CTA', desc: 'The dark-green pill primary action ("Start losing weight" / "Go to membership"); measured, never followed.', sel: 'data-variant=primary / _format-primary-*' });
  await S('cta-secondary', q('main a[class*="_format-secondary-"], main button[class*="_format-secondary-"], [data-testid="card"] a[class*="_format-secondary-"], article a[class*="_format-secondary-"]').filter({ visible: true }).first(), B4, { group: g, title: 'Secondary CTA', desc: 'The outlined secondary action ("Get started"); measured, never followed.', sel: '_format-secondary-* inside main/card' });
  await S('cta-tertiary', q('a[class*="_format-tertiary-"], button[class*="_format-tertiary-"]').filter({ visible: true }).first(), B4, { group: g, title: 'Tertiary CTA', desc: 'The quiet tertiary action ("View details"); measured, never followed.', sel: '_format-tertiary-*' });
  await S('cta-underlined', q('a[class*="_format-underlined-"]').filter({ visible: true }).first(), B4, { group: g, title: 'Underlined link', desc: 'The underlined "Important safety information" action; measured, never followed.', sel: '_format-underlined-*' });
  await S('content-card', q('article[data-content*="contentcard" i], [data-testid="card"] article, article[class*="media-first_component"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Content card', desc: 'A rounded media-first content card in the rails (gradient surface, image, heading, CTA stack).', sel: 'data-content=componentngcontentcard' });
  await S('treatment-card', q('[class*="treatment-card_treatment-card"], [class*="wl-sidekick-style__ProductCard"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Treatment card', desc: 'A medication treatment card (name, drug, price "From $149/mo", CTA stack).', sel: 'treatment-card / ProductCard' });
  await S('card-price', q('[class*="treatment-card"] [class*="price" i], [class*="ProductCard"] [class*="Price"], [class*="ProductCard"] [class*="price"]').filter({ hasText: /from \$|\/mo/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Price line', desc: 'The "From $149/mo †" price line on a treatment/product card.', sel: 'price text inside a card' });
  await S('accordion', q('[class*="accordion_"], [class*="AccordionWrapper"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Accordion', desc: 'The FAQ accordion block; the first panel ships open in SSR, toggles need hydration.', sel: 'accordion_* / AccordionWrapper' });
  await S('accordion-toggle', q('[class*="accordion_heading-container"] button, [class*="accordion_heading-container"], [class*="AccordionTitle"] button, [class*="AccordionTitle"]').filter({ visible: true }).first(), B4, { group: g, title: 'Accordion toggle', desc: 'An accordion row toggle (title + icon); measured, never toggled.', sel: 'accordion heading/title' });
  await S('disclaimer', q('[class*="disclaimer_frame"], [class*="DisclaimerWrapper"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Disclaimer', desc: 'The collapsed legal disclaimer block (grey text, expandable).', sel: 'disclaimer_frame / DisclaimerWrapper' });
  await S('read-more', q('button[class*="DisclaimerToggle"], button[class*="ReadMore_button"], button:has-text("Read more")').filter({ visible: true }).first(), B4, { group: g, title: 'Read more toggle', desc: 'The "Read more" disclaimer toggle; measured, never toggled.', sel: 'DisclaimerToggle / ReadMore_button' });
  await S('carousel-arrow', q('[class*="carousel-controls"] button, [class*="CarouselWrapper"] button, button[aria-label*="next" i], button[aria-label*="previous" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Carousel arrow', desc: 'A carousel next/previous control; measured, never pressed.', sel: 'carousel-controls button' });
  await S('slide-dot', q('[class*="SlideIndicatorDot"], [class*="SlideIndicator"] *, [role="tab"]').filter({ visible: true }).first(), B4, { group: g, title: 'Slide indicator', desc: 'A carousel position dot; measured, never pressed.', sel: 'SlideIndicatorDot' });
}

// ---------------------------------------------------------------- home (marketing stack)

async function home() {
  await header();
  const g = G.home;
  await S('hero-heading', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Hero headline', desc: '"The care you\u2019ve always deserved" — the IvarSoft serif hero.', sel: 'first h1' }, { noScroll: true });
  await S('bento-card', q('[class*="BentoContentCard"], [class*="Bento"] article').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Bento card', desc: 'A hero bento tile (category card: headline, image, arrow); measured, never followed.', sel: 'BentoContentCard' });
  await S('tile-card', q('[class*="homepage-image-style"], [class*="tile" i] a, section a:has(img)').filter({ hasText: /hair|menopause|health|begin/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Category tile', desc: 'A category entry tile ("Grow fuller hair" / "Treat menopause"); measured, never followed.', sel: 'category tile link' });
  await S('quiz-tile', q('a').filter({ hasText: /unsure where to begin|start here/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Quiz entry tile', desc: 'The "Unsure where to begin? Start here" quiz entry tile; measured, never followed (the quiz is a client app).', sel: 'tile with Start here' });
  await S('product-card', q('[class*="wl-sidekick-style__ProductCard"], [class*="ProductCard"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Product card', desc: 'A GLP-1 product card in the lineup rail (image, name, drug, price, CTA).', sel: 'wl-sidekick ProductCard' });
  await S('fda-badge', q('[class*="FdaBadge"], [class*="BadgeContainer"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'FDA badge', desc: 'The "FDA-approved" badge on a product card.', sel: 'FdaBadge' });
  await S('testimonial', q('[class*="TestimonialCard"], [class*="SlideItem"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Testimonial card', desc: 'A testimonial slide (quote, user photo, name) in the carousel.', sel: 'TestimonialCard/SlideItem' });
  await S('app-cta', q('a, button').filter({ hasText: /meet the app|learn more|get the science/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Section CTA', desc: 'A mid-page secondary CTA ("Meet the app" / "Learn more"); measured, never followed.', sel: 'section CTA' });
  await shopChrome();
  await footer();
  save();
}

// ---------------------------------------------------------------- shop pages

async function shopPage() {
  await header();
  await shopChrome();
  await footer();
  save();
}

// ---------------------------------------------------------------- content pages (blog, article, quality, drugs-info, bmi)

async function contentPage(key) {
  const g = G.content;
  await header();
  if (key === 'bmi-calculator') {
    const f = G.form;
    await S('bmi-form', q('form').filter({ visible: true }).first(), ['default'], { group: f, title: 'BMI form', desc: 'The calculator form: height feet/inches and weight number fields plus the submit.', sel: 'form' });
    await S('text-field', q('input[type="number"], input[class*="TextInputElement"]').filter({ visible: true }).first(), FIELD, { group: f, title: 'Number field', desc: 'A labelled number input ("feet"/"inches"/"pounds"); focused and typed into then cleared — never submitted.', sel: 'TextInputElement input' }, { fillText: '150' });
    await S('email-field', q('input[type="email"]').filter({ visible: true }).first(), FIELD, { group: f, title: 'Email field', desc: 'The lead-capture email input; focused and typed into then cleared — never submitted.', sel: 'input[type=email]' }, { fillText: 'name@example.com' });
    await S('form-submit', q('form button[class*="StyledButton"], form button[class*="ButtonVariant"], form button[type="submit"], form button').filter({ visible: true }).first(), B4, { group: f, title: 'Form submit', desc: 'The form\'s dark pill submit; measured, never pressed.', sel: 'form button' });
    await S('disabled-button', q('button[disabled]').filter({ visible: true }).first(), ['default'], { group: f, title: 'Disabled button', desc: 'A disabled pagination/option button in the tool (resting disabled state, SSR).', sel: 'button[disabled]' });
    await S('bmi-dial', q('[class*="BmiDialWrapper"], [class*="BmiDial"]').filter({ visible: true }).first(), ['default'], { group: f, title: 'BMI dial', desc: 'The result dial gauge beside the form.', sel: 'BmiDialWrapper' });
    await S('lead-capture', q('[class*="LeadCaptureBlockWrapper"], [class*="lead-capture"]').filter({ visible: true }).first(), ['default'], { group: f, title: 'Lead capture block', desc: 'The email sign-up block (input + submit + privacy disclosure).', sel: 'LeadCaptureBlockWrapper' });
    await S('privacy-note', q('[class*="PrivacyDisclosure"], [class*="privacy" i]').filter({ visible: true }).first(), ['default'], { group: f, title: 'Privacy disclosure', desc: 'The fine-print privacy disclosure under the lead capture.', sel: 'PrivacyDisclosure' });
  }
  if (key === 'drugs-info') {
    await S('az-chip', q('a[href*="#"], [class*="az" i] a, [class*="letter" i] a').filter({ hasText: /^[A-Z]$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'A-Z chip', desc: 'A grey circular letter chip in "Browse A-Z"; measured, never followed.', sel: 'A-Z letter link' });
    await S('drug-link', q('a').filter({ hasText: /bupropion|metformin|adapalene|minoxidil/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Drug link', desc: 'A medication link in the "Popular Medications" list; measured, never followed.', sel: 'drug name link' });
    await S('page-lede', q('h1, [class*="Typography"] h1, h1 ~ p, [class*="BmiDescription"], [class*="Description"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page lede', desc: 'The page heading/dek block.', sel: 'h1 + description' });
    await S('topic-tab', q('nav a, [role="tab"], header a').filter({ hasText: /weight loss|menopause|mental health|hair|skin|news/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Topic link', desc: 'A topic link in the drugs index sub-nav (All / Weight Loss / …).', sel: 'sub-nav topic link' });
  }
  if (key === 'blog') {
    await S('article-card', q('article, a[class*="card" i], a:has(img), [class*="PictureWrapper"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Article card', desc: 'An article card on the blog index; measured, never followed.', sel: 'article/card link' });
    await S('blog-topic', q('a').filter({ hasText: /hair|skin|mental|weight|news/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Topic link', desc: 'A blog topic/category link; measured, never followed.', sel: 'topic link' });
  }
  if (key === 'blog-post') {
    await S('article-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article title', desc: 'The article H1.', sel: 'h1' }, { noScroll: true });
    await S('prose-p', q('article p, [class*="MarkdownMediaQueryWrapper"] p, main article p').filter({ visible: true }).first(), ['default'], { group: g, title: 'Body paragraph', desc: 'A body paragraph in the article prose.', sel: 'article p' });
    await S('prose-h2', q('article h2, main h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Section heading', desc: 'An in-article section heading.', sel: 'article h2' });
    await S('prose-link', q('article p a, main p a').filter({ visible: true }).first(), B4, { group: g, title: 'Inline link', desc: 'An inline link inside the article body; measured, never followed.', sel: 'article p a' });
    await S('prose-list', q('article li, main li, [class*="OrderedList"] li').filter({ visible: true }).first(), ['default'], { group: g, title: 'List item', desc: 'A list item in the article body.', sel: 'article li' });
    await S('byline', q('[class*="author" i], [class*="byline" i], [class*="Caption"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Byline block', desc: 'The author/reviewer byline under the title.', sel: 'author/byline/caption' });
  }
  if (key === 'quality') {
    await S('prose-h', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Heading', desc: 'A heading on the quality/safety page.', sel: 'h1/h2' }, { noScroll: true });
    await S('prose-body', q('main p, article p').filter({ visible: true }).first(), ['default'], { group: g, title: 'Body text', desc: 'A body paragraph.', sel: 'main p' });
  }
  // The regional-redirect card is mounted visible on these SSR pages; newPage's
  // closePromo hid it, so undo that hiding (SSR markup, not hydration), measure
  // it as the dialog it is, then hide it again (never answered).
  await page.evaluate(() => {
    document.querySelectorAll('[class*="regional-redirect" i], [id*="regional-redirect" i], [class*="RegionalRedirectPopupWrapper"]').forEach((x) => { if (x.style.display === 'none' || x.style.getPropertyPriority('display')) x.style.removeProperty('display'); });
  }).catch(() => {});
  await S('region-dialog', q('[class*="RegionalRedirectPopupWrapper"], [class*="regional-redirect-popup"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Regional redirect card', desc: 'The "It looks like you\u2019re visiting from Canada" redirect card, the one dialog the signed-out SSR paints. Its CTA was measured, never followed; the card was hidden, never answered.', sel: 'RegionalRedirectPopupWrapper' });
  await S('region-cta', q('[class*="RegionalRedirectPopupWrapper"] a, [class*="RegionalRedirectLink"]').filter({ visible: true }).first(), B4, { group: g, title: 'Redirect CTA', desc: 'The "Go to forhers.ca" pill button inside the redirect card; measured, never followed.', sel: 'RegionalRedirectLink' });
  await closePromo(page);
  await shopChrome();
  await footer();
  save();
}

// ---------------------------------------------------------------- mobile

async function mobile(key) {
  const g = G.mobile;
  await S('m-header', q('nav[data-testid="navigation-mast"], [class*="GlobalNavigation"], header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The top chrome at 390: promo bar, wordmark, hamburger (the slide menu needs hydration).', sel: 'navigation-mast / GlobalNavigation' }, { noScroll: true });
  await S('m-menu-toggle', q('button[data-testid="GlobalNavigationButton"], button[aria-label*="menu" i], [class*="menu" i] button').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu toggle', desc: 'The hamburger at phone width; measured, never toggled.', sel: 'menu button' }, { noScroll: true });
  await S('m-logo', q('a[aria-label*="homepage" i]:has(svg), [class*="_logo"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile wordmark', desc: 'The "hers" wordmark at phone width.', sel: 'logo link' }, { noScroll: true });
  if (key === 'weight-loss' || key === 'product') {
    await S('m-cta-primary', q('a[data-variant="primary"], a[class*="_format-primary-"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile primary CTA', desc: 'The primary pill action at phone width.', sel: 'data-variant=primary' });
    await S('m-content-card', q('article[data-content*="contentcard" i], [data-testid="card"] article').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile content card', desc: 'A content card at phone width.', sel: 'content card' });
  }
  if (key === 'home') {
    await S('m-bento-card', q('[class*="BentoContentCard"], [class*="Bento"] article').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile bento card', desc: 'A bento tile at phone width.', sel: 'BentoContentCard' });
  }
  if (key === 'bmi-calculator') {
    await S('m-text-field', q('input[type="number"], input[class*="TextInputElement"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile number field', desc: 'The number input at phone width.', sel: 'TextInputElement input' });
  }
  save();
}

// ---------------------------------------------------------------------------

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.sources = 'Wayback SSR snapshots of forhers.com (live site answers a Cloudflare managed challenge to this network), served locally with scripts stripped; states: at rest, real hover, real keyboard focus, CDP-forced :active, typed-then-cleared fields';
({ srv, port } = await servePages(`${SCRATCH}/pages`, `${SCRATCH}/assets`));
browser = await chromium.launch();
const only = (process.argv[2] || '').split(',').filter(Boolean);
const want = (k) => !only.length || only.includes(k);
try {
  if (want('home') && await newPage('home', { wait: 9000 })) { await chrome('home'); await home(); }
  for (const k of ['weight-loss', 'hair-loss', 'skin-care', 'mental-health', 'birth-control', 'product', 'anti-aging', 'wegovy-pill', 'labs', 'benefits']) {
    if (want(k) && await newPage(k, { wait: 8000 })) { await chrome(k); await shopPage(); }
  }
  for (const k of ['blog', 'blog-post', 'quality', 'bmi-calculator', 'drugs-info']) {
    if (want(k) && await newPage(k, { wait: 8000 })) { await chrome(k); await contentPage(k); }
  }
  if (want('mhome') && await newPage('mhome', { mobile: true })) await mobile('home');
  if (want('mwl') && await newPage('mwl', { mobile: true })) await mobile('weight-loss');
  if (want('mproduct') && await newPage('mproduct', { mobile: true })) await mobile('product');
  if (want('mbmi') && await newPage('mbmi', { mobile: true })) await mobile('bmi-calculator');
  if (want('mblogpost') && await newPage('mblogpost', { mobile: true })) await mobile('blog-post');
} finally {
  save();
  await browser.close();
  srv.close();
}
log('done ->', OUT);
