// Measures blog.blueapron.com's public components in every state reachable
// without signing in, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home category article faq cart mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// blog.blueapron.com is a Squarespace 7.1 site ("Extra Helpings"): classes are
// stable semantic names (blog-item, header-nav-item, sqs-button-element--*).
// www.blueapron.com hard-blocks this client at the Cloudflare edge, so the
// blog is the whole capturable surface. Nothing is sent, bought or signed
// into: the only presses are local UI toggles — the comments toggle and the
// mobile burger menu. The cookie banner is disabled sitewide; a promo popup
// is hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const ARTICLE = '/guides/15-budget-friendly-quick-dinner-ideas-for-busy-weeknights';
const URLS = { home: '/', category: '/guides/category/Recipes', article: ARTICLE, faq: '/guides/membership-autoship-faq', cart: '/cart' };
let page, cdp, current, context, run;
const touched = new Set();
const listed = new Map();
// Routes PerimeterX gates this run: components last measured on them keep their
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
  const b = context.browser();
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, url || BASE + URLS[key], { wait, promo });
  if (await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
  // meta is the entry's description only; an option placed here (fillText, cropLoc,
  // noToggle...) would be silently ignored, so refuse it
  for (const k of Object.keys(meta)) if (!['group', 'title', 'desc', 'sel'].includes(k)) throw new Error(`S(${key}): '${k}' is an option; pass it in opts`);
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
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again)$/i;
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

const G = {
  shell: 'Shell and navigation', home: 'Blog home and cards', category: 'Category list',
  article: 'Article page', cart: 'Cart', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  // --- chrome ---
  await S('announcement-bar', q('.sqs-announcement-bar, .header-announcement-bar-wrapper, [class*="announcement-bar" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Announcement bar', desc: 'The thin promo strip above the header; its close is a UI toggle, measured never pressed.', sel: '.sqs-announcement-bar' }, { noScroll: true });
  await S('announcement-close', q('.sqs-announcement-bar-close, [class*="announcement-bar" i] button').filter({ visible: true }).first(), B4, { group: g, title: 'Announcement close', sel: '.sqs-announcement-bar-close' }, { noScroll: true });
  await S('header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The header bar: logo wordmark, nav, cart and the CTA.', sel: 'header' }, { noScroll: true });
  await S('logo', q('.header-title-logo a, .header-title a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', sel: '.header-title-logo a' }, { noScroll: true });
  await S('nav-link', q('.header-nav-item a').filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A header nav item (Guides, the Blue Apron shop links).', sel: '.header-nav-item a' }, { noScroll: true });
  await S('header-cta', q('.header-actions-action--cta .btn, .header-actions .btn, .header-actions a[class*="btn" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Header CTA', desc: 'The button in the header actions (join/shop); links off the blog host, measured and never followed.', sel: '.header-actions-action--cta .btn' }, { noScroll: true });
  await S('cart-icon', q('.floating-cart, .header-actions [class*="cart" i], a[href="/cart"]').filter({ visible: true }).first(), B4, { group: g, title: 'Cart icon', desc: 'The Squarespace commerce cart control (the cart stays empty).', sel: '.floating-cart / .icon--cart' }, { noScroll: true });
  // --- blog list ---
  const h = G.home;
  await S('search-field', q('.sqs-block-search input, input.search-input, input[type="search"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: h, title: 'Search field', desc: 'The blog search input; focused and filled with sample text that was deleted, never submitted.', sel: '.sqs-block-search input' }, { noScroll: true, fillText: 'dinner ideas' });
  await S('search-button', q('.sqs-block-search button, [class*="search" i] button[type="submit"], .sqs-search-ui-button-wrapper button').filter({ visible: true }).first(), B4, { group: h, title: 'Search button', desc: 'The search submit; measured at rest, never pressed (it would run a search).', sel: '.sqs-block-search button' }, { noScroll: true });
  await S('blog-card', q('.blog-item').filter({ visible: true }).first(), ['default'], { group: h, title: 'Blog card', desc: 'One post summary in the masonry list: image, categories, title, excerpt, meta.', sel: '.blog-item' });
  await S('card-image', q('.blog-item .blog-image-wrapper').filter({ visible: true }).first(), ['default'], { group: h, title: 'Card image', desc: 'The post thumbnail frame.', sel: '.blog-item .blog-image-wrapper' });
  await S('card-title', q('.blog-item .blog-title, .blog-item .blog-title a').filter({ visible: true }).first(), B4, { group: h, title: 'Card title', desc: 'The post title link; measured, never followed.', sel: '.blog-item .blog-title' });
  await S('card-category', q('.blog-item .blog-categories a, .blog-item .blog-categories-list a').filter({ visible: true }).first(), B4, { group: h, title: 'Category link', desc: 'A category link on the card meta row.', sel: '.blog-categories a' });
  await S('card-excerpt', q('.blog-item .blog-excerpt').filter({ visible: true }).first(), ['default'], { group: h, title: 'Card excerpt', desc: 'The summary paragraph under the title.', sel: '.blog-excerpt' });
  await S('card-more', q('.blog-item .blog-more-link').filter({ visible: true }).first(), B4, { group: h, title: 'Read-more link', sel: '.blog-more-link' });
  await S('card-meta', q('.blog-item .blog-meta-section, .blog-item .blog-meta-primary').filter({ visible: true }).first(), ['default'], { group: h, title: 'Card meta', desc: 'The date/author row under the excerpt.', sel: '.blog-meta-section' });
  await S('pagination', q('.blog-list-pagination').filter({ visible: true }).first(), ['default'], { group: h, title: 'List pagination', desc: 'The older/newer posts pager under the list.', sel: '.blog-list-pagination' });
  await S('pagination-link', q('.blog-list-pagination a').filter({ visible: true }).first(), B4, { group: h, title: 'Pagination link', sel: '.blog-list-pagination a' });
  // --- content blocks on the page ---
  await S('button-primary', q('.sqs-button-element--primary, a.sqs-block-button-element--primary').filter({ visible: true }).first(), B4, { group: h, title: 'Primary button', desc: 'A primary Squarespace button block on the page.', sel: '.sqs-button-element--primary' });
  await S('button-secondary', q('.sqs-button-element--secondary, a.sqs-block-button-element--secondary').filter({ visible: true }).first(), B4, { group: h, title: 'Secondary button', desc: 'A secondary (border) Squarespace button block.', sel: '.sqs-button-element--secondary' });
  await S('content-image', q('.sqs-block-image .image-wrapper, .sqs-block-image img').filter({ visible: true }).first(), ['default'], { group: h, title: 'Content image', desc: 'An image block inside a content section.', sel: '.sqs-block-image' });
  save();
}

async function category() {
  if (!(await newPage('category'))) return;
  await sheetsFor('category');
  const g = G.category;
  await S('cat-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Category heading', desc: 'The Recipes category listing heading.', sel: 'h1/h2 on the category page' }, { noScroll: true });
  await S('cat-card', q('.blog-item, .blog-masonry .entry').filter({ visible: true }).nth(2), ['default'], { group: g, title: 'Category card', desc: 'A post card on the category listing.', sel: '.blog-item on /guides/category' });
  save();
}

async function article() {
  if (!(await newPage('article', { wait: 9000 }))) return;
  await sheetsFor('article');
  await chrome('article');
  const g = G.article;
  await S('article-title', q('h1.entry-title, .blog-item-title').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article title', desc: 'The guide headline in Ivory.', sel: 'h1.entry-title' }, { noScroll: true });
  await S('article-meta', q('.blog-item-meta-wrapper, .blog-item-author-date-wrapper').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article meta', desc: 'The author/date row under the title.', sel: '.blog-item-meta-wrapper' }, { noScroll: true });
  await S('article-body', q('.blog-item-content p, .sqs-html-content p').filter({ visible: true }).first(), ['default'], { group: g, title: 'Body paragraph', desc: 'A body-text paragraph in the guide.', sel: '.blog-item-content p' });
  await S('article-lede', q('.blog-item-content img, .blog-item-content .image-wrapper').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article image', desc: 'The lede/inline image in the guide body.', sel: '.blog-item-content img' });
  await S('body-link', q('.blog-item-content p a, .sqs-html-content p a').filter({ visible: true }).first(), B4, { group: g, title: 'Body link', desc: 'An inline link inside body text; measured, never followed.', sel: '.blog-item-content p a' });
  const pg = q('.item-pagination--prev-next .item-pagination-link, .item-pagination-link--next, .item-pagination-link--prev').filter({ visible: true });
  await S('article-pager', pg.first(), B4, { group: g, title: 'Article pager', desc: 'The older/newer guide pager under the article.', sel: '.item-pagination-link' });
  const tog = q('.blog-item-comments-toggle-wrapper, [class*="comments-toggle"]').filter({ visible: true }).first();
  await S('comments-toggle', tog, B4, { group: g, title: 'Comments toggle', desc: 'The comments header; a UI toggle measured in all states.', sel: '.blog-item-comments-toggle-wrapper' });
  await S('comments-open', tog, ['opened'], { group: g, title: 'Comments toggle, open', desc: 'After its own toggle; the opened comments list shows in the crop of the comments area.', sel: '.blog-item-comments-toggle-wrapper' }, { cropLoc: q('.blog-item-comments').first() });
  // The captured guide ends at the older/newer pager — no related grid on
  // this article template.
  save();
}

async function faq() {
  if (!(await newPage('faq'))) return;
  const g = G.article;
  await S('faq-title', q('h1.entry-title, .blog-item-title, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ title', desc: 'The membership/Autoship FAQ headline.', sel: 'h1 on the FAQ guide' }, { noScroll: true });
  await S('faq-heading', q('.blog-item-content h2, .blog-item-content h3, .sqs-html-content h2, .sqs-html-content h3').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ heading', desc: 'A question heading inside the FAQ body.', sel: '.blog-item-content h2/h3' });
  await S('faq-body', q('.blog-item-content p, .sqs-html-content p').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ paragraph', sel: '.blog-item-content p on the FAQ guide' });
  save();
}

async function cart() {
  if (!(await newPage('cart'))) return;
  const g = G.cart;
  await S('cart-page', q('.Cart-inner, [class*="Cart" i], main').filter({ visible: true }).first(), ['default'], { group: g, title: 'Cart page', desc: 'The Squarespace commerce cart, empty as this client sees it — nothing was ever added.', sel: '.Cart-inner' }, { noScroll: true });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The dark-bold footer sections: sitemap links, social icons, legal.', sel: 'footer#footer-sections' }, { noScroll: true });
  const fl = q('footer a').filter({ visible: true }).first();
  await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('social-icon', q('footer .sqs-svg-icon--social, footer [class*="social" i] a, .sqs-svg-icon--social').filter({ visible: true }).first(), B4, { group: g, title: 'Social icon', desc: 'A social link icon in the footer.', sel: '.sqs-svg-icon--social' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('.header-burger-btn, button[class*="burger" i], .header-menu-toggle').filter({ visible: true }).first();
  await S('m-menu-button', menu, B4, { group: g, title: 'Burger button', desc: 'The hamburger that opens the mobile menu.', sel: '.header-burger-btn' }, { noScroll: true });
  await S('m-menu-open', menu, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The burger after its own toggle; the opened menu overlay shows in the crop of the whole menu panel.', sel: '.header-burger-btn' }, { noScroll: true, cropLoc: q('.header-menu').first() });
  // The menu is still open after m-menu-open's own toggle: read a nav item
  // while it is held open — the items mount only while the overlay is up, and
  // clicking the burger again would close it, so no further toggle here.
  await S('m-nav-item', q('.header-menu-nav-item a, .header-menu-nav-list a').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A nav link inside the opened menu overlay.', sel: '.header-menu-nav-item a' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-blog-card', q('.blog-item').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile blog card', sel: '.blog-item at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, category, article, faq, cart, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '.blog-item');
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
