// Measures 1Password's public marketing components in every state reachable
// without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing product download developer contact signin mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// States: hover, focus-visible, pressed (CDP forcePseudoState), focused,
// filled (typed then deleted), open (a resting state via a UI toggle).
// Nothing is sent, bought or signed into: the only presses are consent
// dismissal, the Business nav flyout button, the plan selector and FAQ
// accordions. The vault is credential-gated; start.1password.com gates
// headless browsers to /unsupported, which is measured as the boundary.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, open, closePromo, killGeo, domClick, domFind, styleOf, crop, centre, RAW, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/',
  pricing: '/pricing',
  product: '/product/enterprise-password-manager',
  download: '/downloads/mac',
  developer: '/developer-security',
  contact: '/contact-sales',
  signin: 'https://start.1password.com/unsupported?l=en',
};
let page, cdp, current, context, contextMobile, run;
const touched = new Set();

// ---------- helpers ----------

async function newPage(key, { mobile = false, promo = 'close', wait = 6000 } = {}) {
  current = key;
  if (!contextMobile) {
    const b = context.browser();
    contextMobile = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
  }
  const ctx = mobile ? contextMobile : context;
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  page.setDefaultTimeout(8000);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { wait, promo });
  if (promo === 'close') await killGeo(page);
  // 1password's CSP forbids inline <style>; the caret nicety is optional.
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
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
const NEVER = /^(send|submit|sign up|sign in|log in|create|buy|checkout|pay|purchase|subscribe|share|start free trial|upgrade|open)$/i;
async function toggle(loc) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || t.tag === 'A') throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
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
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

// Records the listed states of one component. meta: title, group, desc, sel.
async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  delete out.components[key].missing;
  if (opts.open) { await reset(); await opts.open(); }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
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
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing', product: 'Product page',
  download: 'Downloads', developer: 'Developer', overlay: 'Dialogs and overlays',
  form: 'Forms', mobile: 'Mobile (390 wide)', signin: 'Sign-in boundary',
};

async function home() {
  await newPage('home');
  await sheetsFor('home');
  const g = G.shell;
  const strip = await domFind(page, /1Password for Agents/i, { sel: 'a, p, div', tag: 'strip' });
  await S('promo-strip', strip, ['default'], { group: g, title: 'Announcement strip', desc: 'The tan strip above the header: "1Password for Agents" copy with a Learn more link and a Sign in link at the far right.', sel: 'top strip' }, { noScroll: true });
  await S('promo-link', q('a:has-text("Learn more")').filter({ visible: true }).first(), B4, { group: g, title: 'Announcement link', sel: 'strip Learn more' }, { noScroll: true });
  await S('signin-link', q('a:has-text("Sign in")').filter({ visible: true }).first(), B4, { group: g, title: 'Sign in link', desc: 'The sign-in link at the strip\'s far right; points at my.1password.com.', sel: 'a Sign in' }, { noScroll: true });
  const hdr = q('[class*="header-navigation"]').filter({ visible: true }).first();
  await S('header', hdr, ['default'], { group: g, title: 'Header', desc: 'The white sticky bar (header-navigation): wordmark, Business/Personal/Developers/Partners/Resources flyout buttons, Pricing link, then Talk to sales and the blue Get started free pill.', sel: 'header.header-navigation' }, { noScroll: true });
  await S('logo', q('[class*="logo-container"], header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Wordmark', sel: 'header logo' }, { noScroll: true });
  const biz = await domFind(page, /^Business$/, { sel: 'button, a', tag: 'biz' });
  await S('nav-flyout-button', biz, B4, { group: g, title: 'Nav flyout button', desc: 'A group/nav-item button (Business, Personal, Developers, Partners, Resources); opens the mega flyout on hover.', sel: 'button.group/nav-item' }, { noScroll: true });
  await S('nav-flyout', q('[class*="header-navigation__dropdown" i]').filter({ visible: true }).first(), ['open'], { group: g, title: 'Nav flyout', desc: 'The mega panel a nav group opens on click (Business, Personal, ...): product and feature links in columns.', sel: 'header-navigation__dropdown' }, { noScroll: true, open: async () => { await biz.click().catch(() => biz.evaluate((el) => el.click())); await page.waitForTimeout(1600); } });
  await S('nav-link', q('a[class*="nav-item"]:has-text("Pricing")').filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A plain text nav item (Pricing).', sel: 'header a Pricing' }, { noScroll: true });
  await S('cta-header-primary', hdr.locator('a:has-text("Get started"), a[class*="cta" i]').filter({ visible: true }).last(), B4, { group: g, title: 'Header primary CTA', desc: 'The blue cta-btn pill at the header\'s far right ("Get started free").', sel: 'header .cta-btn' }, { noScroll: true });
  await S('cta-header-sales', hdr.locator('a:has-text("Talk to sales")').filter({ visible: true }).first(), B4, { group: g, title: 'Header sales link', sel: 'header a Talk to sales' }, { noScroll: true });

  const h = G.home;
  const hero = q('h1').filter({ visible: true }).first().locator('xpath=ancestor::*[contains(@class,"hero") or contains(@class,"gradient")][1]');
  await S('hero', hero, ['default'], { group: h, title: 'Hero', desc: 'The opening band on bg-hero-gradient-blue: oversized display headline, sub copy and the CTA row on a dark field above the product collage.', sel: 'section.bg-hero-gradient-blue' });
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: 'Display copy in agileSans, ~88px light.', sel: 'h1' });
  const heroBox = hero.filter({ visible: true }).first();
  await S('cta-hero-primary', heroBox.locator('a:has-text("Talk to sales"), a[class*="cta" i]').filter({ visible: true }).first(), B4, { group: h, title: 'Hero primary CTA', desc: 'The white cta-btn pill in the hero ("Talk to sales").', sel: 'hero .cta-btn' });
  await S('cta-hero-secondary', heroBox.locator('a:has-text("View plans")').filter({ visible: true }).first(), B4, { group: h, title: 'Hero secondary CTA', desc: 'The bordered outline pill beside the primary ("View plans").', sel: 'hero secondary cta' });
  await S('video-embed', q('iframe[src*="vimeo"], iframe[src*="player"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Video embed', desc: 'The hero product video: a cross-origin Vimeo iframe. The element\'s box and style were measured; its contents are unreachable (cross-origin), so nothing inside is claimed.', sel: 'iframe[src*=vimeo]' });
  await S('section-title', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section title', sel: 'h2' });
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer', desc: 'The footer: link columns, legal row, social icons.', sel: 'footer' });
  await page.close();
}

async function pricing() {
  await newPage('pricing');
  await sheetsFor('pricing');
  const g = G.pricing;
  await S('pricing-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', sel: 'h1' });
  const plan = q('[class*="segment-selector" i], [class*="segment" i][role]').filter({ visible: true }).first();
  await S('plan-selector', plan, B4, { group: g, title: 'Plan selector', desc: 'The large bordered pill beside the h1 that switches the grid between Enterprise / Business / Individual & Family.', sel: 'plan pill' });
  const epm = await domFind(page, /Enterprise Password Manager/, { sel: 'h2, h3, p, div', tag: 'epm' });
  const col = epm.locator('xpath=ancestor::*[self::li or self::td or self::div][contains(@class,"p-") or contains(@class,"border") or contains(@class,"flex")][1]');
  await S('product-column', col, ['default'], { group: g, title: 'Product column', desc: 'One column of the platform/product pricing grid: kicker, product name, blurb, CTA pill and a feature list.', sel: 'pricing grid column' });
  await S('product-name', epm, ['default'], { group: g, title: 'Product name', sel: 'column product name' });
  await S('cta-quote', q('a:has-text("Request a quote"), button:has-text("Request a quote")').filter({ visible: true }).first(), B4, { group: g, title: 'Request a quote CTA', sel: 'Request a quote' });
  // The FAQ block's toggles are the "Answer to '…'" chevron buttons; a
  // page-wide aria-expanded query hits the header's nav buttons first.
  const acc = q('button[aria-label^="Answer to"][aria-expanded="false"]').filter({ visible: true }).first();
  const accRow = acc.locator('xpath=ancestor::div[contains(@class,"relative") and contains(@class,"flex")][1]');
  await S('faq-row', accRow, B4, { group: g, title: 'FAQ row', desc: 'A collapsible question row in the dark FAQ band; focus lands on its "Answer to" toggle.', sel: 'faq row' }, { focusLoc: acc });
  if (await acc.count()) {
    await toggle(acc).catch(() => {});
    await page.waitForTimeout(900);
    await S('faq-answer', acc.locator('xpath=ancestor::div[contains(@class,"border")][1]/div[@role="region"]'), ['open'], { group: g, title: 'FAQ answer', desc: 'The expanded answer body under a FAQ row.', sel: 'faq region' }, { noScroll: true });
  }
  await page.close();
}

async function product() {
  await newPage('product');
  await sheetsFor('product');
  const g = G.product;
  await S('product-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product title', sel: 'h1' });
  await S('cta-product-primary', q('a:has-text("Get started free"), a[class*="cta" i]:has-text("Get started")').filter({ visible: true }).first(), B4, { group: g, title: 'Product primary CTA', sel: 'Get started free' });
  await S('cta-marketplace', q('a:has-text("Marketplace"), a[href*="marketplace"]').filter({ visible: true }).first(), B4, { group: g, title: 'Marketplace link', desc: 'The link to the 1Password Marketplace (marketplace.1password.com) on the product page.', sel: 'a Marketplace' });
  const card = await domFind(page, /password|credential|vault/i, { sel: '[class*="card" i], article, li:has(h3), section [class*="rounded"]', tag: 'fc', leaf: false, minW: 200, minH: 80 });
  await S('feature-card', card, ['default', 'hover'], { group: g, title: 'Feature card', desc: 'A product-feature card on the marketing page.', sel: 'feature card' });
  await page.close();
}

async function download() {
  await newPage('download');
  const g = G.download;
  const dtitle = await domFind(page, /Download 1Password for/i, { sel: 'h1, h2, p, div', tag: 'dt', leaf: true, minW: 250 });
  await S('download-title', dtitle, ['default'], { group: g, title: 'Download title', desc: 'The display heading "Download 1Password for macOS": the h1 itself is sr-only, so the styled text block was measured instead.', sel: 'download heading block' });
  await S('platform-pill', q('button:has-text("macOS"), [class*="segment" i]:has-text("macOS"), [role="combobox"]:has-text("macOS")').filter({ visible: true }).first(), B4, { group: g, title: 'Platform pill', desc: 'The macOS platform selector under the title, same segment-selector control as the pricing plan pill.', sel: 'macOS pill' });
  await S('download-button', q('a:has-text("Download"), button:has-text("Download"), a[class*="download" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Download button', sel: 'Download' });
  await S('platform-link', q('a:has-text("Windows"), a:has-text("iOS"), a:has-text("Android"), a:has-text("Linux")').filter({ visible: true }).first(), B4, { group: g, title: 'Platform link', desc: 'A link to another platform\'s download page.', sel: 'platform link' });
  await page.close();
}

async function developer() {
  await newPage('developer');
  const g = G.developer;
  await S('dev-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Developer title', sel: 'h1' });
  await S('dev-card', q('[class*="card" i], section [class*="rounded" i][class*="border" i], li:has(h3)').filter({ visible: true }).first(), ['default'], { group: g, title: 'Developer card', desc: 'A feature/link card on the developer page.', sel: 'developer card' });
  await S('dev-cta', q('a:has-text("Get started"), a:has-text("Docs"), a:has-text("documentation")').filter({ visible: true }).first(), B4, { group: g, title: 'Developer CTA', sel: 'developer cta' });
  await page.close();
}

async function contact() {
  await newPage('contact');
  const f = G.form;
  await S('contact-title', q('h1').filter({ visible: true }).first(), ['default'], { group: f, title: 'Contact title', sel: 'h1' });
  await S('form-embed', q('iframe[src*="marketo"], iframe[src*="integrations.1passwordservices"]').filter({ visible: true }).first(), ['default'], { group: f, title: 'Sales form embed', desc: 'The contact form is a Marketo iframe hosted on integrations.1passwordservices.com. The element box was measured; the fields inside are cross-origin and were neither introspected nor submitted.', sel: 'iframe[src*=marketo]' });
  await page.close();
}

async function signin() {
  await newPage('signin', { wait: 10000 });
  const g = G.signin;
  await S('unsupported-card', q('main, [role="main"], body > div').filter({ visible: true }).first(), ['default'], { group: g, title: 'Unsupported-browser page', desc: 'start.1password.com gates headless/unsupported browsers here instead of the sign-in form. Measured as the honest edge of the public surface; the vault itself is credential-gated and out of scope.', sel: 'unsupported main' }, { noScroll: true });
  await S('unsupported-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Unsupported title', sel: 'unsupported heading' }, { noScroll: true });
  await page.close();
}

async function mobile() {
  await newPage('home', { mobile: true });
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The 390-wide header bar.', sel: 'mobile header' }, { noScroll: true });
  const ham = q('button[aria-label*="menu" i], button[aria-expanded], [class*="header-navigation"] button, [class*="header"] button').filter({ visible: true }).last();
  await S('m-menu-button', ham, ['default', 'pressed'], { group: g, title: 'Mobile menu button', desc: 'Opens the mobile nav drawer.', sel: 'mobile menu button' }, { noScroll: true });
  if (await ham.count()) { await toggle(ham).catch(() => {}); await page.waitForTimeout(1600); }
  const drawer = await domFind(page, /business|personal|pricing|sign in/i, { sel: '[role="dialog"], [class*="drawer" i], [class*="mobile" i], nav, [class*="fixed"]', tag: 'mdr', leaf: false, minW: 250, minH: 300 });
  await S('m-nav-drawer', drawer, ['open'], { group: g, title: 'Mobile nav drawer', desc: 'The sheet the menu button opens.', sel: 'mobile nav drawer' }, { noScroll: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero title', sel: 'mobile h1' });
  await page.close();
}

const RUNNERS = { home, pricing, product, download, developer, contact, signin, mobile };
run = new Date().toISOString();
out._meta.run = run;
out._meta.product = '1password.com';
const wanted = process.argv.slice(2).join(',').split(',').map((s) => s.trim()).filter((s) => s && s !== 'all');
({ context } = await launch());
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
await context.browser().close();
