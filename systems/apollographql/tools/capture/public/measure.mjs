// Measures apollographql.com's public marketing components in every state
// reachable without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing customers blog contact mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// apollographql.com is a Next.js site: Tailwind utility classes plus CSS
// modules (`footer_footer__…`); selectors key off roles, text and the stable
// class part, never a hash. The site ships one theme per page — dark on
// home/pricing/customers/graphos, light on blog/contact-sales — with the
// space-named palette (eclipse midnight, satellite, regolith, solar orange).
// Nothing is sent, bought or signed into: the only press is the Products nav
// disclosure, a local menu open. The OneTrust banner is measured as found,
// never answered. The app host studio.apollographql.com is a sign-in
// boundary — never submitted.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, open, closePromo, killGeo, domClick, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/',
  pricing: '/pricing',
  customers: '/customers',
  blog: '/blog',
  contact: '/contact-sales',
};
let page, cdp, current, context, run;
const touched = new Set();

// A bot interstitial or an error page both render a minimal body: detect
// either so a blocked load is skipped, not measured.
async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /something went wrong|performing security verification|verifying you are human|just a moment|^not found$/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

// ---------- helpers ----------

async function newPage(key, { mobile = false, promo = 'close', wait = 6000 } = {}) {
  current = key;
  const b = context.browser();
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  // bot check: recorded as a boundary, not bypassed (navigator.webdriver is left as Chromium sets it)
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

// Clicks a UI toggle (accordion, menu, drawer). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign up|sign in|log in|create|buy|checkout|pay|purchase|subscribe|share|start free trial|start for free|upgrade|open|continue with|accept all|reject all|customize|get started|talk to apollo|contact us|contact sales)$/i;
async function toggle(loc) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || t.tag === 'A') throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

// ONLY=key1,key2 limits the run to those components, so a wrong selector's
// entries can be recaptured without re-measuring every control on the page.
const ONLY = new Set((process.env.ONLY || '').split(',').map((s) => s.trim()).filter(Boolean));

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
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

// Records the listed states of one component. meta: title, group, desc, sel.
async function S(key, target, list, meta = {}, opts = {}) {
  if (ONLY.size && !ONLY.has(key)) return;
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
        await (opts.fieldLoc || loc).filter({ visible: true }).first().click({ timeout: 4000 });
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 });
        await page.keyboard.type(opts.fillText || FILL, { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || FILL}", then deleted; nothing sent`;
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

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FILL = 'name@example.com';

// Transitions and animations declared in every readable sheet, by selector.
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
// ---------- page runs ----------
const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  customers: 'Customers', blog: 'Blog', contact: 'Contact sales',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  // promo:'keep' leaves the OneTrust card up so it can be measured as found.
  if (!(await newPage('home', { promo: 'keep' }))) { await page.close(); return; }
  await sheetsFor('home');
  const g = G.shell;

  // OneTrust banner, bottom-left card: measured as found, never answered.
  const ot = q('.otFloatingRoundedCorner, #onetrust-banner-sdk').filter({ visible: true }).first();
  await S('cookie-card', ot, ['default'], { group: g, title: 'Cookie consent card', desc: 'The OneTrust bottom-left card (white, 16px radius, double shadow): copy, Accept All / Decline Non-Necessary / Manage Preferences buttons.', sel: '.otFloatingRoundedCorner' }, { noScroll: true });
  await S('cookie-accept', q('button:has-text("Accept All Cookies")').filter({ visible: true }).first(), ['default'], { group: g, title: 'Cookie Accept button', desc: 'The dark pill inside the OneTrust card. Measured, never clicked.', sel: 'Accept All Cookies' }, { noScroll: true });
  await closePromo(page);

  // The Apollo Summit eyebrow strip sits above the sticky header.
  await S('eyebrow', q(M('summit-eyebrow_eyebrow') + ', ' + M('summit-eyebrow_root') + ', [class*="summit-eyebrow"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Summit eyebrow', desc: 'The "Apollo Summit 2026 keynote available / Watch keynote" strip above the nav, with its own close.', sel: 'summit-eyebrow' }, { noScroll: true });
  await S('nav-bar', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav bar', desc: 'The sticky transparent header over the dark hero: logo, Products/Solutions/Resources/Company disclosures, Pricing and Contact us links, search, Start for free pill.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a[href="/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Logo', desc: 'The Apollo wordmark, top-left of the nav.', sel: 'header logo' }, { noScroll: true });
  await S('nav-trigger', q('header button:has-text("Products")').filter({ visible: true }).first(), B4, { group: g, title: 'Nav disclosure', desc: 'A nav menu trigger (Products / Solutions / Resources / Company): 38px, 8px radius, Inter 15px 500 at 72% white.', sel: 'nav disclosure' }, { noScroll: true });
  // Products dropdown, opened (local state, then Escape).
  const openNav = async () => { const b = q('header button:has-text("Products")').first(); await b.click().catch(() => {}); await page.waitForTimeout(1200); };
  await openNav();
  await S('nav-menu', q('[role="menu"], [class*="navigation_menu"], [class*="dropdown"], header [class*="panel" i]').filter({ visible: true }).first(), ['open'], { group: g, title: 'Products menu', desc: 'The Products dropdown panel: product rows with one-line descriptions, plus the two promo links at the foot.', sel: 'products dropdown' }, { noScroll: true });
  await S('nav-menu-item', q('a[href="/graphos"]').filter({ visible: true }).first(), ['open', 'hover'], { group: g, title: 'Menu item', desc: 'A product row inside the Products dropdown.', sel: 'dropdown item' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.mouse.click(720, 700); await page.waitForTimeout(500);
  await S('nav-cta', q('header a:has-text("Start for free"), header a[href*="signup"]').filter({ visible: true }).first(), B4, { group: g, title: 'Start for free button', desc: 'The pill at the right of the nav; links to studio.apollographql.com/signup. Hovered and focused only.', sel: 'nav Start for free' }, { noScroll: true });
  await S('nav-search', q('header .aa-DetachedSearchButton, header button.aa-DetachedSearchButton').filter({ visible: true }).first(), B4, { group: g, title: 'Search button', desc: 'The Algolia detached search icon in the nav.', sel: 'search button' }, { noScroll: true });

  const h = G.home;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: '"Give AI access to the systems that run your business" — Aeonik 60px white over the dark animated hero.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', await domFind(page, /domain model for AI|helps you build yours/i, { sel: 'p', tag: 'hs', minH: 30 }), ['default'], { group: h, title: 'Hero subhead', desc: 'The 20px Aeonik lede under the hero title.', sel: 'hero subhead' }, { noScroll: true });
  await S('cta-primary', q('main a:has-text("Talk to Apollo"), a:has-text("Talk to Apollo")').filter({ visible: true }).first(), B4, { group: h, title: 'Primary CTA', desc: 'The white 999px pill "Talk to Apollo" (60px tall, Aeonik 18px 500) with a soft warm shadow.', sel: 'hero primary' }, { noScroll: true });
  await S('cta-secondary', q('a:has-text("See how it works")').filter({ visible: true }).first(), B4, { group: h, title: 'Secondary CTA', desc: 'The 1px white/35 outline pill beside the primary.', sel: 'hero secondary' }, { noScroll: true });
  await S('pause-motion', q('button:has-text("Pause motion"), ' + M('hero-depth_pause')).filter({ visible: true }).first(), B4, { group: h, title: 'Pause motion button', desc: 'The ghost chip bottom-right of the hero (80% black fill, 1px white/20 border, 4px radius).', sel: 'pause motion' }, { noScroll: true });
  await S('text-link', q('a:has-text("Read more about domain models")').filter({ visible: true }).first(), B4, { group: h, title: 'Text link', desc: 'The solar-orange inline link (Aeonik 18px 700) inside body copy.', sel: 'orange text link' });
  await S('link-pill', q('a:has-text("Explore GraphOS"), a:has-text("Explore Agent Services")').filter({ visible: true }).first(), B4, { group: h, title: 'Arrow link pill', desc: 'An orange "Explore … →" pill link between sections (Aeonik 16px 500).', sel: 'orange arrow link' });
  await S('section-title-light', await domFind(page, /Enterprise teams trust Apollo|shared foundation/i, { sel: 'h2, h3', tag: 'st', minH: 30 }), ['default'], { group: h, title: 'Section title (light)', desc: 'An Aeonik 42px heading on a light content section — the site alternates dark hero / light content bands.', sel: 'section h2' });
  await S('video-card', q('button:has-text("PLAY VIDEO"), ' + M('video')).filter({ visible: true }).first(), B4, { group: h, title: 'Video card', desc: 'The 520x293 "PLAY VIDEO" card, 24px radius on eclipse.', sel: 'video card' });
  await S('copy-row', q(M('architecture-animation_copyControl')).filter({ visible: true }).first(), B4, { group: h, title: 'Copy control row', desc: 'One of the three 416x84 copy rows in the architecture animation panel.', sel: 'copyControl row' });
  await S('carousel-arrow', q('button.h-\\[42px\\], main button[aria-label*="next" i], main button[aria-label*="previous" i], main button[aria-label*="slide" i]').filter({ visible: true }).first(), B4, { group: h, title: 'Carousel arrow', desc: 'A 42x42 white 16px-radius arrow button on the logo/customer carousel.', sel: 'carousel arrow' });
  // Footer: dark band, link columns, social icons, small Start for free pill.
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: h, title: 'Footer', desc: 'The footer band: tagline, five link columns, small orange Start for free pill, social icons.', sel: 'footer' });
  await S('footer-link', q('footer a[class*="text-body-sm"], footer li a, footer nav a, footer a:has-text("Pricing")').filter({ visible: true }).first(), B4, { group: h, title: 'Footer link', desc: 'A 14px Inter footer column link at offwhite #f8f8f8.', sel: 'footer link' });
  await S('social-link', q('footer ' + M('footer_socialLink')).filter({ visible: true }).first(), B4, { group: h, title: 'Social icon', desc: 'A 28x28 social icon in the footer row.', sel: 'social link' });
  await page.close();
}

async function pricing() {
  if (!(await newPage('pricing'))) { await page.close(); return; }
  await sheetsFor('pricing');
  const g = G.pricing;
  await S('pricing-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: '"Pricing that makes sense at any scale…" — Inter 50px 500 on the dark page.', sel: 'h1' }, { noScroll: true });
  // Plan tier + billing segments: 43px pills with a 1px white border.
  await S('tier-segment', q('button:has-text("Developer")').filter({ visible: true }).first(), B4, { group: g, title: 'Tier segment', desc: 'A plan-tier filter pill (Developer / …), 43px tall, 20px radius, 1px white border.', sel: 'tier pill' });
  await S('billing-segment', q('button:has-text("Monthly"), button:has-text("Yearly"), button:has-text("Annual")').filter({ visible: true }).first(), B4, { group: g, title: 'Billing segment', desc: 'The Monthly/Yearly billing pill beside the tier pills.', sel: 'billing pill' });
  // Request-volume pills: the held one fills solar orange.
  await S('volume-pill-on', q('button:has-text("1m")').filter({ visible: true }).first(), B4, { group: g, title: 'Volume pill (selected)', desc: 'The held request-volume pill: #fc5200 solar fill, eclipse text, 8px radius.', sel: 'volume pill on' });
  await S('volume-pill', q('button:has-text("10m")').filter({ visible: true }).first(), B4, { group: g, title: 'Volume pill', desc: 'An unheld volume pill: transparent, 1px border, 8px radius.', sel: 'volume pill' });
  await S('plan-cta', q('main a:has-text("Start for free")').filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'The orange "Start for free" pill on pricing (49px, Inter 16px 500). Links to Studio signup; hovered and focused only.', sel: 'pricing cta' });
  // The rounded-32 feature cards: dark "Trusted by" band, light FAQ band.
  await S('stats-card', q('div[class*="border-radius-32"]').filter({ hasText: /Trusted by digital leaders/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Stats band card', desc: 'The 1344x670 eclipse card ("Trusted by digital leaders"), 32px radius.', sel: 'stats card' });
  await S('faq-card', q('div[class*="border-radius-32"]').filter({ hasText: /FAQs/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ card', desc: 'The light regolith-grey FAQ card (#e3e3e3), 32px radius.', sel: 'faq card' });
  await S('faq-item', q('div[class*="border-radius-32"]').filter({ hasText: /FAQs/ }).locator('button, summary, [role="button"]').filter({ visible: true }).first(), B4, { group: g, title: 'FAQ item', desc: 'A question row inside the FAQ card.', sel: 'faq row' });
  await S('promo-banner', q(M('connectors-promo_promoBanner')).filter({ visible: true }).first(), ['default'], { group: g, title: 'Promo banner', desc: 'The "Amazing together" connectors promo card: eclipse fill, 32px radius.', sel: 'promo banner' });
  await page.close();
}

async function customers() {
  if (!(await newPage('customers'))) { await page.close(); return; }
  await sheetsFor('customers');
  const g = G.customers;
  await S('customers-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Customers title', desc: '"API Orchestration Success Stories" — Inter 50px 500.', sel: 'h1' }, { noScroll: true });
  await S('cta-orange', q('a:has-text("Talk to an expert"), a:has-text("See plans")').filter({ visible: true }).first(), B4, { group: g, title: 'Orange CTA', desc: 'The solar-orange pill "Talk to an expert" (49px, Inter 16px 500, eclipse text on orange).', sel: 'orange cta' });
  await S('cta-orange-outline', q('a:has-text("See Apollo Plans")').filter({ visible: true }).first(), B4, { group: g, title: 'Orange outline CTA', desc: 'The 1px orange-outline pill beside the filled one.', sel: 'orange outline cta' });
  await S('stats-band', q('div[class*="border-radius-32"]').filter({ hasText: /Fortune 100|monthly downloads/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Stats band', desc: 'The eclipse stats card ("0M monthly downloads / 0% of the Fortune 100…"), 32px radius.', sel: 'stats band' });
  await S('story-card', q('article' + M('customer-story-article_article') + ', ' + M('customer-story-article_article')).filter({ visible: true }).first(), B4, { group: g, title: 'Story card', desc: 'A customer-story card (432x585): white 32px-radius card with cover image, company name, title and author.', sel: 'story card' });
  await page.close();
}

async function blog() {
  // The blog index is the light sibling app: its own nav module, Aeonik 60 headings.
  if (!(await newPage('blog'))) { await page.close(); return; }
  await sheetsFor('blog');
  const g = G.blog;
  await S('blog-title', q('h1, h2').filter({ hasText: /new|insights|latest/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Blog title', desc: '"What\'s new" — Aeonik 60px on the light page.', sel: 'blog h1' }, { noScroll: true });
  await S('article-card', q('article' + M('card_theme-satellite') + ', article' + M('blog-article_article')).filter({ visible: true }).first(), B4, { group: g, title: 'Article card (satellite)', desc: 'A featured article card on the satellite grey (#cfd7d6), 32px radius: date, title, author.', sel: 'article card' });
  await S('article-card-regolith', q('article' + M('card_theme-regolith')).filter({ visible: true }).first(), B4, { group: g, title: 'Article card (regolith)', desc: 'A past-posts card on white regolith, 32px radius.', sel: 'regolith card' });
  await S('pagination', q('button' + M('pagination_pageBtn')).filter({ visible: true }).nth(1), B4, { group: g, title: 'Pagination button', desc: 'A numbered page button in the archive pagination.', sel: 'page button' });
  await S('pagination-on', q('button' + M('pagination_activePage')).filter({ visible: true }).first(), ['default'], { group: g, title: 'Pagination (active)', desc: 'The held page number in the pagination.', sel: 'page on' });
  await page.close();
}

async function contact() {
  // The contact-sales page is light; the HubSpot form sits in a dark panel.
  if (!(await newPage('contact'))) { await page.close(); return; }
  await sheetsFor('contact');
  const g = G.contact;
  await S('contact-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact title', desc: '"Contact us" — Inter 50px 500, eclipse on the light page.', sel: 'h1' }, { noScroll: true });
  const field = q('input.hs-input:not([type="hidden"]):not([type="checkbox"]):not([type="radio"])').filter({ visible: true }).first();
  await S('field', field, ['default', 'focused'], { group: g, title: 'Text field', desc: 'A HubSpot text input: 54px, 16px radius, eclipse fill, 1px white border, Inter 18px. Clicked into once; nothing typed or sent.', sel: 'input.hs-input' });
  await S('field-filled', field, ['filled'], { group: g, title: 'Text field (filled)', desc: 'The same field with text typed, then deleted before close; the form was never submitted.', sel: 'input.hs-input' }, { fieldLoc: field });
  await S('select', q('select.hs-input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Select', desc: 'A country/topic select: same 54x16 field shell, placeholder state.', sel: 'select.hs-input' });
  await S('textarea', q('textarea.hs-input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Textarea', desc: 'The 120px message textarea, same field shell.', sel: 'textarea.hs-input' });
  await S('submit', q('input.hs-button, button.hs-button').filter({ visible: true }).first(), B4, { group: g, title: 'Submit button', desc: 'The orange pill submit (50px, radius 9999, Inter 16px 500). Measured and hovered only — never clicked.', sel: '.hs-button' });
  await page.close();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true, promo: 'close' }))) { await page.close(); return; }
  const g = G.mobile;
  await S('m-nav-bar', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav bar', desc: 'The mobile header: logo left, hamburger right.', sel: 'mobile header' }, { noScroll: true });
  await S('m-burger', q('header button:has(svg), header [class*="burger" i], header button').filter({ visible: true }).last(), ['default', 'pressed'], { group: g, title: 'Hamburger', desc: 'The mobile menu button. Not opened — the menu overlays the measured content.', sel: 'burger' }, { noScroll: true });
  await S('m-hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero title', sel: 'mobile hero' }, { noScroll: true });
  await S('m-cta-primary', q('a:has-text("Talk to Apollo")').filter({ visible: true }).first(), ['default', 'pressed'], { group: g, title: 'Mobile primary CTA', desc: 'The white pill, full width on phone.', sel: 'mobile primary' }, { noScroll: true });
  await S('m-cta-secondary', q('a:has-text("See how it works")').filter({ visible: true }).first(), ['default', 'pressed'], { group: g, title: 'Mobile secondary CTA', desc: 'The outline pill under it.', sel: 'mobile secondary' }, { noScroll: true });
  await page.close();
}

const RUNNERS = { home, pricing, customers, blog, contact, mobile };
run = new Date().toISOString();
out._meta.run = run;
out._meta.product = 'apollographql.com';
const wanted = process.argv.slice(2).join(',').split(',').map((s) => s.trim()).filter(Boolean);
const lh = await launch();
({ context } = lh);
try {
  for (const [k, fn] of Object.entries(RUNNERS)) {
    if (wanted.length && !wanted.includes(k)) continue;
    try { await fn(); } catch (e) { log('PAGE FAILED', k, String(e.message).split('\n')[0]); }
    save();
  }
  // mark components from this run whose selectors matched nothing; a component
  // with recorded states (from an earlier merged run) is covered, not missing
  for (const [k, c] of Object.entries(out.components)) {
    if (!touched.has(k)) continue;
    if (Object.keys(c.states || {}).length) delete c.missing;
    else c.missing = true;
  }
  save();
  log('done ->', OUT);
} finally {
  // closing each page leaves the browser itself running; close it so the
  // documented command exits
  await lh.browser.close().catch(() => {});
}
