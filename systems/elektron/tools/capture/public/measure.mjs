// Measures elektron.se's public components in every state reachable without
// signing in, checking out or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home shop product-digitakt product-accessory explore support about
// contact cart my-account store-locator mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// elektron.se is WordPress + WooCommerce on the thedock child theme: classes
// are readable (block-button, block-input, is-modal-section) but the
// per-element .td<hex>-<n> utility classes are generated, so specs select by
// role, text or stable class names, never a td* hash. The site paints one
// dark theme — there is no light variant.
// Nothing is sent, bought or signed into: the only presses are local UI
// toggles — the header's Search / Catalog / Account modal triggers, the cart
// drawer, a product accordion and the mobile menu. The #thedock-cookie-banner
// consent modal is hidden, never answered; ADD TO CART, SUBMIT, the magic-
// login Send me a code and every checkout action are measured, never pressed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', shop: '/shop', 'product-digitakt': '/product/digitakt-ii',
  'product-accessory': '/product/pl-2-protective-lid', explore: '/explore',
  support: '/support-downloads', about: '/who-we-are', contact: '/contact-us',
  cart: '/cart', 'my-account': '/my-account', 'store-locator': '/store-locator',
};
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes blocked this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /client challenge|performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access|a required part of this site/i.test(t + ' ' + document.title) || t.trim().length < 40;
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
  await loc.waitFor({ state: 'visible', timeout: 6000 }).catch(() => {});
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
        else {
          await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle';
          // Close it again after the reading: a menu left open holds focus, so every later
          // focus-visible on the page records 'focus failed'. Escape closes a menu; an
          // accordion still reporting aria-expanded=true is toggled back.
          undo = async () => {
            await page.keyboard.press('Escape'); await page.waitForTimeout(300);
            const l = loc.filter({ visible: true }).first();
            if ((await l.getAttribute('aria-expanded').catch(() => null)) === 'true') { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(600); }
          };
        }
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

// Clicks a UI toggle (dropdown, menu, accordion trigger). Refuses a submit
// button and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|order( free)?( sample)?|add to cart|go to the platform|create new account|send me a code|proceed to checkout)$/i;
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

// The header's Search / Account anchors open .is-modal-section panels
// (dropdown / drawer-right). A click toggles them; the desktop bar is
// .is-main-menu (the mobile copy is .is-main-menu-mobile). Catalog is a plain
// link to /explore, not a modal. hasText is a substring match: the anchors'
// textContent carries the injected icon <style> text, so an anchored label
// match fails.
const navTrigger = (text) => q('.is-main-menu a').filter({ hasText: new RegExp(text) }).filter({ visible: true }).first();

async function openModal(text) {
  const t = navTrigger(text);
  if (!(await t.count())) return false;
  await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click()));
  await page.waitForTimeout(1600);
  return true;
}

// Marks an opened modal panel: a visible .is-modal-section (the Search
// dropdown is a thin bar, so the floor is 60px tall).
async function markModal(tag) {
  await page.evaluate((tag) => {
    document.querySelectorAll(`[data-m-mark="${tag}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const cand = [...document.querySelectorAll('.is-modal-section, [class*="modal-layout"]')].filter((el) => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      return r.height > 60 && r.width > 200 && cs.visibility !== 'hidden' && cs.opacity !== '0' && cs.display !== 'none' && r.top < innerHeight && r.bottom > 0;
    });
    if (cand[0]) cand[0].setAttribute('data-m-mark', tag);
  }, tag);
}

const G = {
  shell: 'Shell and navigation', shop: 'Shop', product: 'Product pages',
  explore: 'Explore', support: 'Support and downloads', about: 'About',
  contact: 'Contact', account: 'Account and cart', footer: 'Footer',
  overlay: 'Dialogs and overlays', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('.header-section-wrapper.is-main-menu').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The 56px transparent top bar over the page: Catalog / Shop / Kulture / Search on the left, the Elektron mark centre, Support / Account / Cart on the right — Neue Haas Grotesk Text 14px labels with small icons.', sel: '.header-section-wrapper.is-main-menu' }, { noScroll: true });
  await S('logo', q('.is-main-menu a[href="https://www.elektron.se"], .is-main-menu a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Elektron wordmark anchor at the centre of the header.', sel: 'header logo anchor' }, { noScroll: true });
  await S('nav-link', navTrigger('Shop'), B4, { group: g, title: 'Nav link', desc: 'A header destination anchor (Catalog / Shop / Kulture): a .block-button.button-small_text row 28px tall, icon left of a 14px label. Measured, never followed.', sel: 'header .block-button.button-small_text' }, { noScroll: true });
  await S('nav-icon-link', navTrigger('Cart'), B4, { group: g, title: 'Nav icon link', desc: 'A right-side header action (Support / Account / Cart): label left of a small icon. Cart opens the mini-cart drawer — measured, never followed to checkout.', sel: 'header Cart anchor' }, { noScroll: true });
  // Header modals: Search dropdown, Account drawer. The Search panel is a
  // header section, not an .is-modal-section — mark the visible panel that
  // contains the live search-field instead.
  if (await openModal('Search')) {
    await page.evaluate(() => {
      const i = [...document.querySelectorAll('input.search-field')].find((e) => e.getBoundingClientRect().width > 0);
      let n = i;
      // the dropdown panel is the nearest wrapper sized like a bar (60-400px)
      while (n && n !== document.body && !(n.getBoundingClientRect().height > 60 && n.getBoundingClientRect().height < 400 && n.getBoundingClientRect().width > 400)) n = n.parentElement;
      if (n && n !== document.body) n.setAttribute('data-m-mark', 'searchmodal');
    });
    await S('search-modal', q('[data-m-mark="searchmodal"]').filter({ visible: true }).first(), ['opened'], { group: G.overlay, title: 'Search dropdown', desc: 'The header Search dropdown: a large search-field row under the header.', sel: 'opened Search modal' }, { noScroll: true, noReset: true, noToggle: true });
    await S('search-field', q('.is-modal-section input[type="search"], input.search-field').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: G.overlay, title: 'Search field', desc: 'The big search input inside the Search dropdown ("Type and press enter to search"). Sample text was typed and deleted; the query was never submitted.', sel: 'search modal input.search-field' }, { noScroll: true, noReset: true, fillText: 'digitakt' });
    await page.keyboard.press('Escape').catch(() => {});
    const x = q('.modal-close').filter({ visible: true }).first();
    if (await x.count()) await x.click().catch(() => {});
    await page.waitForTimeout(900);
  }
  if (await openModal('Account')) {
    await markModal('accountmodal');
    await S('account-modal', q('[data-m-mark="accountmodal"]').filter({ visible: true }).first(), ['opened'], { group: G.overlay, title: 'Account drawer', desc: 'The header Account modal (modal-layout-drawer-right): the magic-login panel — a Log in step (Email field, Send me a code) and Create New Account. Measured, never used.', sel: 'opened Account modal' }, { noScroll: true, noReset: true, noToggle: true });
    // The drawer's Log in row expands the magic-login form (local UI toggle);
    // it is a heading row, not an anchor.
    // Only the h2 heading row: an anchor or button named "Log in" would be a real sign-in, which toggle()'s NEVER list refuses.
    const step = q('[data-m-mark="accountmodal"] h2').filter({ hasText: /^\s*Log in/ }).filter({ visible: true }).first();
    if (await step.count()) { await step.click().catch(() => {}); await page.waitForTimeout(1200); }
    await S('magic-email', q('[data-m-mark="accountmodal"] input[type="email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: G.overlay, title: 'Magic-login email field', desc: 'The Email input of the magic-login drawer: a 42px block-input field. Sample text was typed and deleted; no code was ever requested.', sel: 'account drawer email input' }, { noScroll: true, noReset: true });
    await S('magic-send', q('[data-m-mark="accountmodal"] button').filter({ hasText: /Send me a code/ }).filter({ visible: true }).first(), B4, { group: G.overlay, title: 'Send me a code button', desc: 'The magic-login submit: a full-width secondary-variant block-button (grey fill, dark label, digi one v2). Measured, never pressed.', sel: 'account drawer Send me a code' }, { noScroll: true, noReset: true });
    await page.keyboard.press('Escape').catch(() => {});
    const x = q('.modal-close').filter({ visible: true }).first();
    if (await x.count()) await x.click().catch(() => {});
    await page.waitForTimeout(900);
  }
  const h = G.about;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Page title', desc: 'The home page heading.', sel: 'first h1' });
  await S('section-h2', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A section heading below the fold.', sel: 'first h2' });
  save();
}

async function shop() {
  if (!(await newPage('shop'))) return;
  await sheetsFor('shop');
  await chrome('shop');
  const g = G.shop;
  // /shop has no h1: the grid is the page. A product cell is a
  // .group-content holding the product h2, a one-line descriptor h2 and a
  // .price paragraph — products are block links (a.background-link overlays),
  // not wrapped anchors.
  const card = q('p.price').filter({ visible: true }).first().locator('xpath=ancestor::div[contains(@class,"group-content")][1]');
  await S('product-card', card, B4, { group: g, title: 'Product card', desc: 'A shop-grid product block: product name (18px Neue Haas Text), a one-line descriptor and the price in $. Measured, never followed.', sel: 'shop product group-content' });
  await S('product-card-title', q('.wp-block-heading.has-medium-font-size').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product card title', sel: 'shop product h2' });
  await S('product-card-sub', q('.wp-block-heading.has-normal-font-size').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product card subtitle', sel: 'shop product descriptor' });
  await S('price', q('.price, p.price').filter({ visible: true }).first(), ['default'], { group: g, title: 'Price', desc: 'A product price figure ("349 $").', sel: '.price' });
  save();
}

async function product() {
  if (!(await newPage('product-digitakt'))) return;
  await sheetsFor('product-digitakt');
  await chrome('product-digitakt');
  const g = G.product;
  await S('pdp-title', q('h1').filter({ hasText: /Digitakt/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Product title', desc: 'The product name on the detail page, 18px Neue Haas Text.', sel: 'product h1' });
  await S('pdp-price', q('.price, p.price').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product price', desc: 'The product price figure ("1149 $").', sel: 'product .price' });
  await S('pdp-explore', q('.block-button').filter({ hasText: /EXPLORE/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Explore button', desc: 'The full-width outline action on the product page (EXPLORE DIGITAKT II): a .block-button.button-outline, 2px #eeeef2 border, transparent fill, digi one v2 14px caps at 46px tall. Measured, never followed.', sel: '.block-button.button-outline EXPLORE' });
  await S('accordion', q('.block-button').filter({ hasText: /Key Features/ }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Key Features accordion', desc: 'A 24px Neue Haas Grotesk Display block row with a right icon that expands the feature section — a local UI toggle.', sel: '.block-button Key Features' }, {
    before: { opened: async (l) => { await toggle(l, { allowLink: true }); await page.waitForTimeout(1000); return 'clicked (a UI toggle)'; } },
    after: { opened: async () => { const x = q('.block-button').filter({ hasText: /Key Features/ }).filter({ visible: true }).first(); await x.click({ timeout: 3000 }).catch(() => {}); } },
  });
  save();

  if (!(await newPage('product-accessory'))) return;
  await S('pdp-title-accessory', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product title (accessory)', sel: 'product h1 on /product/pl-2-protective-lid' });
  await S('add-to-cart', q('.single_add_to_cart_button, button[name="add-to-cart"]').filter({ visible: true }).first(), B4, { group: g, title: 'Add to cart button', desc: 'The in-stock product action: a 2px #eeeef2 outline block-button, digi one v2 14px caps, 46px tall. Measured, never pressed — nothing was added to the cart.', sel: '.single_add_to_cart_button' });
  save();
}

async function explore() {
  if (!(await newPage('explore'))) return;
  await sheetsFor('explore');
  const g = G.explore;
  await S('explore-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Explore title', sel: 'first h1 on /explore' });
  await S('explore-link', q('main a, article a, .grid-content a').filter({ hasText: /Analog|Digit|Syntakt|Tonverk|Octatrack/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Explore product link', desc: 'A product-name row in the Explore index; measured, never followed.', sel: 'explore product link' });
  save();
}

async function support() {
  if (!(await newPage('support'))) return;
  await sheetsFor('support');
  const g = G.support;
  await S('support-title', q('h2').filter({ hasText: /Support/ }).filter({ visible: true }).first().or(q('h1').filter({ visible: true }).first()), ['default'], { group: g, title: 'Support title', desc: 'The 64px Neue Haas Grotesk Display page title.', sel: 'support h1/h2' });
  // Page links are .background-link overlays or .block-button.button-text
  // rows; measure the first visible text action under main.
  await S('download-row', q('a.block-button.button-text, main a').filter({ visible: true }).first(), B4, { group: g, title: 'Support action link', desc: 'A support/downloads action row (a .block-button.button-text link with a right icon) in the page content. Measured, never followed.', sel: 'support action link' });
  save();
}

async function about() {
  if (!(await newPage('about'))) return;
  await sheetsFor('about');
  const g = G.about;
  await S('about-title', q('h1, h2').filter({ hasText: /Elektron|Who|We/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'About title', sel: 'who-we-are heading' });
  save();
}

async function contact() {
  if (!(await newPage('contact'))) return;
  await sheetsFor('contact');
  const g = G.contact;
  await S('contact-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact title', desc: 'The 64px Neue Haas Grotesk Display Pro 500 page title.', sel: 'contact h1' });
  const field = q('input.block-input, input[class*="block-input"]').filter({ visible: true }).first();
  await S('text-field', field, ['default', 'focused', 'filled'], { group: g, title: 'Text field', desc: 'A 42px block-input: #eeeef2 field, #151515 text, Neue Haas Text 14px, square corners. Sample text was typed and deleted; the form was never submitted.', sel: '.block-input input', fillText: 'Test name' }, { fillText: 'Test name' });
  await S('select-field', q('select.block-input, select[class*="block-input"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Select field', desc: 'The Category select: same 42px field treatment; never changed.', sel: 'select.block-input' });
  await S('textarea-field', q('textarea.block-input, textarea[class*="block-input"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Text area', desc: 'The Message area: a taller #eeeef2 field. Focused only; nothing typed was sent.', sel: 'textarea.block-input' });
  await S('submit-button', q('button, input[type="submit"]').filter({ hasText: /submit/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Submit button', desc: 'The contact form SUBMIT: a 2px #eeeef2 outline block-button, digi one v2 14px caps, 46px tall. Measured, never pressed — the form was never sent.', sel: 'contact Submit button' });
  save();
}

async function cart() {
  if (!(await newPage('cart'))) return;
  await sheetsFor('cart');
  const g = G.account;
  await S('cart-drawer', q('dialog.tdc-cart, .tdc-cart__panel, [class*="tdc-cart"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mini-cart drawer', desc: 'The cart side drawer (a 392px right drawer, dialog.tdc-cart): "Your cart is empty." with a CONTINUE SHOPPING action. Nothing was ever added.', sel: 'dialog.tdc-cart' }, { noScroll: true });
  await S('cart-continue', q('a, button').filter({ hasText: /continue shopping|back to shop|start shopping/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue shopping action', desc: 'The empty-cart action row; measured, never followed.', sel: 'cart continue action' }, { noScroll: true });
  save();
}

async function myAccount() {
  if (!(await newPage('my-account'))) return;
  await sheetsFor('my-account');
  const g = G.account;
  await S('login-panel', q('main, [class*="login"], form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login panel', desc: 'The /my-account magic-login surface (the same Send me a code form as the header drawer). Captured, never used.', sel: 'my-account form' }, { crop: false });
  await S('login-email', q('input[type="email"], input.block-input, input[name*="email" i]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Login email field', desc: 'The Email input of the magic-login form. Sample text was typed and deleted; no code was ever requested.', sel: 'my-account email input' });
  await S('login-send', q('button').filter({ hasText: /Send me a code/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Send me a code button', desc: 'The full-width secondary-variant block-button (grey #cccccc fill, #151515 digi label). Measured, never pressed.', sel: 'my-account Send me a code' });
  await S('login-create', q('button, a').filter({ hasText: /Create New Account/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Create account button', desc: 'The secondary account action; measured, never pressed.', sel: 'my-account Create New Account' });
  save();
}

async function storeLocator() {
  if (!(await newPage('store-locator', { wait: 12000 }))) return;
  await sheetsFor('store-locator');
  const g = G.support;
  await S('locator-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Store locator title', sel: 'store-locator heading' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 7000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1800);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The footer: the Elektron wordmark, the Navigation / Shop / Support / Resources columns of 24px Neue Haas Display links, legal row and the cookie-settings reopen link.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a.block-button, footer a[class*="button"]').filter({ hasText: /Shop|Support|Press|Store Locator/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer column link: 24px Neue Haas Grotesk Display 450, measured, never followed.', sel: 'footer .block-button' }, { noScroll: true });
  await S('footer-wordmark', q('footer a.block-icon, footer a[class*="svg-icon"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer wordmark', desc: 'The Elektron logo link at the foot of the page.', sel: 'footer wordmark' }, { noScroll: true });
  await S('social-icon', q('footer a[href*="instagram"], footer a[href*="facebook"], footer a[href*="youtube"], footer a[href*="discord"], footer a[href*="x.com"], footer a[aria-label*="Instagram" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A social link in the footer.', sel: 'footer social a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('.header-section-wrapper').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('a[href="#menu-trigger"]').filter({ visible: true }).first();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The burger anchor that toggles the mobile menu panel.', sel: 'a[href=#menu-trigger]' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1600); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  // The mobile menu is the header itself: a[href="#menu-trigger"] expands
  // header#menu-trigger.header-mobile to fill the viewport.
  await page.evaluate(() => {
    const h = document.querySelector('#menu-trigger, header.header-mobile');
    if (h && h.getBoundingClientRect().height > 200) h.setAttribute('data-m-mark', 'mmenu');
  });
  await S('m-menu-open', q('[data-m-mark="mmenu"]').filter({ visible: true }).first(), ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The opened mobile navigation panel: the header expands to a fullscreen menu with a search row and Catalog / Shop / Kulture / Support / Account links.', sel: 'opened mobile menu header' }, { noScroll: true, noReset: true, noToggle: true });
  await S('m-nav-item', q('#menu-trigger a, .header-mobile a').filter({ hasText: /Catalog|Shop|Kulture|Support|Account/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A row inside the opened mobile menu.', sel: 'mobile menu row' }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile heading', sel: 'first heading at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the public surface paints one dark theme — #151515 field, #eeeef2 text — with no light variant';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
// Keys are the page names the header lists (product() reads both product pages).
const plan = { home, shop, 'product-digitakt': product, explore, support, about, contact, cart, 'my-account': myAccount, 'store-locator': storeLocator };
const known = new Set([...Object.keys(plan), 'product-accessory', 'mobile']);
const unknown = pages.filter((p) => !known.has(p));
if (unknown.length) throw new Error(`unknown page ${unknown.join(', ')}; pages: ${[...known].join(' ')}`);
if (pages.includes('product-accessory') && !pages.includes('product-digitakt')) pages.push('product-digitakt');
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) await plan[k]();
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await mobile();
  // Reduced-motion check on an element that actually transitions (a header
  // nav link), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '.is-main-menu a');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    if (!touched.has(key) && !pages.length && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
