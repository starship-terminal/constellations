// Measures doctronic.ai's components on its public pages, in every state that
// can be reached without signing in, submitting a form or starting a chat.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home chat signin symptom blog telehealth authors resource wall dark mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be re-run)
// and one crop per component and state into components/crops/. raw/measurements.md
// is then built from the JSON by build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 450ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or submit button can fire
//   focused        the field clicked into (a text field only)
//   filled         sample text typed into a field, measured, then deleted; Enter is never pressed
//   anything else  a resting state reached by the page itself or by a UI toggle (the site
//                  menu drawer, the chat sidebar's own Expand button); nothing that sends
//                  a message, submits symptoms, signs in or navigates away is ever pressed
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, open, closePromo, domFind, styleOf, crop, centre, RAW } from './lib.mjs';
import { prefer } from './prefer.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: '/',
  chat: '/chat/',
  signin: '/?modal=signin',
  symptom: '/symptom-checker/',
  blog: '/blog/',
  telehealth: '/telehealth/',
  authors: '/authors/',
  resource: '/resource-center/',
  wall: '/wall-of-love/',
  dark: '/',
};
const THEME = { dark: 'dark' };   // every other run is the default light theme

let page, cdp, current, context, run;
const touched = new Set();
const listed = new Map(); // component -> the states this run's specs list for it

// ---------- helpers ----------

async function newPage(key, { mobile = false, promo = 'close', wait = 6000 } = {}) {
  current = key;
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '');
  // a page whose bot check does not clear fails here; the run loop keeps that page's earlier readings
  if (!(await open(page, BASE + URLS[key], { wait, promo }))) throw new Error('blocked: the bot check did not clear on ' + key);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
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

// Clicks a UI toggle (tab, menu, show more). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|send message|submit|sign in|log in|log in with email|sign up|sign up for free|create( an account)?|continue with .+|generate|upload|start chat|get started|check my symptoms|try doctronic.*|talk to|see (a |the )?doctor|find care|get care|book|refill|start free trial|upgrade|open|explore now|share|export pdf)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
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

const FILL = 'I have a mild fever since yesterday';

// Records the listed states of one component. meta: title, group, desc, sel.
async function S(key, target, list, meta = {}, opts = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  if (opts.open) { await reset(); await opts.open(); }
  // A target that only exists once opts.open has run is passed as a function and resolved here.
  const loc = (typeof target === 'function' ? await target() : target).filter({ visible: true }).first();
  if (!(await loc.count())) { log('  ! missing', key); out.components[key].missing = true; return; }
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
        const f0 = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f0.click({ timeout: 4000 }).catch(() => f0.evaluate((el) => { el.focus(); el.click(); }));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => { el.focus(); el.click(); }));
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
// Locator.or() is a union resolved in DOM order: `preferred.or(fallback)` picks whichever node comes
// first in the document, so a fallback earlier in the DOM wins over a preferred match. prefer()
// (prefer.mjs) takes the first candidate with a visible match, in the order given.

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
        if (t || a) transitions.push({ selector: (r.selectorText || '').replace(/__[A-Za-z0-9_-]{5,6}/g, '').slice(0, 160), transition: t, animation: a });
      }
    };
    for (const ss of document.styleSheets) { try { walk(ss.cssRules); } catch { /* cross-origin, read by vars.mjs */ } }
    return transitions;
  });
  out._meta.sheets ??= {};
  out._meta.sheets[key] = res;
}



// ---------- groups ----------
const G = {
  shell: 'Shell and navigation', home: 'Home: hero and marketing', chat: 'Chat surface',
  symptom: 'Symptom checker', content: 'Marketing and content pages', overlay: 'Dialogs and overlays',
  dark: 'Dark theme (data-theme="dark")', mobile: 'Mobile (390 wide)',
};

// ---------- home ----------

async function home() {
  await newPage('home');
  await sheetsFor('home');
  const g = G.shell;
  // The top bar is a div (class _header _marketingHeader), not a <header> tag:
  // wordmark link, Log in (secondary), Sign up (primary) and the menu button.
  const header = await prefer(q(M('marketingHeader')).first(), q(M('header')).first(), q('header').first());
  await S('header', header, ['default'], { group: g, title: 'Marketing top bar', desc: 'The bar over the home page: wordmark, Log in, Sign up and the menu button that opens the site-menu drawer.', sel: M('marketingHeader') }, { noScroll: true });
  await S('signup-button', await prefer(header.getByRole('button', { name: /sign up/i }).first(), header.locator('a,button').filter({ hasText: /sign up/i }).first()), B4, { group: g, title: 'Sign up button', desc: 'The dark pill at the right of the top bar. Measured, never pressed.', sel: 'top bar "Sign up"' }, { noScroll: true });
  await S('login-button', await prefer(header.getByRole('button', { name: /log in/i }).first(), header.locator('a,button').filter({ hasText: /log in/i }).first()), B4, { group: g, title: 'Log in button', desc: 'The quiet secondary button beside Sign up. Measured, never pressed.', sel: 'top bar "Log in"' }, { noScroll: true });
  const menuBtn = await prefer(q(M('expandHitArea')).first(), header.locator('button[aria-label]').first(), header.locator('button').last());
  await S('menu-button', menuBtn, B4, { group: g, title: 'Site-menu button', desc: 'aria-label "open sidebar": opens the site-menu drawer. The drawer was opened and measured below, then dismissed with Escape.', sel: M('expandHitArea') }, { noScroll: true });
  await S('logo', await prefer(header.locator('a[href="/"]').first(), q(M('logo')).first()), ['default'], { group: g, title: 'Wordmark', sel: 'top bar home link' }, { noScroll: true });
  // The site-menu drawer — opened by the header's own "open sidebar" button.
  await S('menu-drawer', () => prefer(q('section[class*="_dialog"]').first(), q('[role="dialog"]').first()), ['default'], { group: g, title: 'Site-menu drawer', desc: 'The left drawer the menu button opens: Dashboard links (New chat, Explore, Health record, Health information), then a Company group (About us, Careers, Partnerships, …).', sel: 'section[class*="_dialog"]' }, { noScroll: true, open: async () => { const b2 = menuBtn.filter({ visible: true }).first(); await b2.click({ timeout: 4000 }).catch(() => b2.evaluate((el) => el.click())); await page.waitForTimeout(1400); } });
  await S('menu-item', q(`${M('menuItem')}:not(${M('menuItemButton')})`).first(), B4, { group: g, title: 'Menu drawer item', desc: 'A row in the site-menu drawer. Measured while the drawer was open; links were never followed.', sel: M('menuItem') }, { noScroll: true });
  await S('menu-item-expand', q(M('menuItemButton')).first(), ['default', 'hover'], { group: g, title: 'Menu drawer expandable', desc: 'A submenu row (About Chat / Health information) with a chevron. Measured, never expanded.', sel: M('menuItemButton') }, { noScroll: true });
  await page.keyboard.press('Escape');
  await page.waitForTimeout(700);

  const h = G.home;
  // The hero band is the smallest ancestor of the textarea that also holds
  // an h1 (the first h1 in the DOM is the wordmark inside the top bar, so the
  // anchor must be the textarea itself).
  const heroTa = await prefer(q('textarea[placeholder*="symptom" i]').first(), q('textarea[placeholder]').first());
  const heroEl = heroTa.locator('xpath=ancestor::*[.//h1][1]');
  await S('hero', heroEl, ['default'], { group: h, title: 'Home hero', desc: 'The first band: the Fraunces display headline, the "What brings you in?" prompt and the chat input card.', sel: 'textarea ancestor holding h1' });
  await S('hero-title', await prefer(heroEl.locator('h1').first(), q('h1').filter({ hasText: /doctronic/i }).last()), ['default'], { group: h, title: 'Hero headline', desc: '"Hi, I\'m Doctronic" in the Fraunces display face with the dashed underline.', sel: 'hero h1' });
  await S('anon-label', await prefer(q(M('anonymousLabel')).first(), await domFind(page, /^anonymous$/i, { sel: 'span,div,button', tag: 'm-anon', leaf: true })), ['default'], { group: h, title: 'Anonymous label', desc: 'The "Anonymous" session badge inside the chat field.', sel: '"Anonymous" badge' });
  await S('hero-input-card', await prefer(q(M('inputContainer')).first(), q(M('heroInputWrapper')), q(M('inputCard')), heroTa.locator('xpath=ancestor::*[self::div or self::form][position()<=3]').last()), ['default', 'hover'], { group: h, title: 'Hero chat field', desc: 'The input card the page is built around: raised white surface, soft border, the textarea and the Start chat button. Measured, never submitted.', sel: M('inputContainer') });
  await S('hero-textarea', heroTa, ['default', 'focused', 'filled'], { group: h, title: 'Hero textarea', desc: '"Describe symptom or ask any health questions…" — text was typed and deleted; nothing was sent.', sel: 'textarea' }, { fillText: 'I have a headache since this morning' });
  await S('start-chat-button', await prefer(q(M('submitButton')).first(), await domFind(page, /^start chat$/i, { tag: 'm-sc' })), B4, { group: h, title: 'Start chat button', desc: 'The accent-blue submit control. Measured, never pressed — pressing would start a chat.', sel: M('submitButton') });
  await S('brings-pill', await prefer(q(M('pill')).first(), await domFind(page, /what brings you in/i, { sel: 'span,p,div', tag: 'm-pill', leaf: true })), ['default'], { group: h, title: '"What brings you in?" pill', sel: M('pill') });
  await S('hipaa-badge', await prefer(q(M('hipaaBadge')).first(), await domFind(page, /hipaa/i, { sel: 'span,div,a', tag: 'm-hipaa', leaf: true })), ['default'], { group: h, title: 'HIPAA badge', sel: M('hipaaBadge') });
  await S('feature-card', await prefer(q(M('featureCardBlock')).first(), q(M('card')).filter({ hasNot: q('blockquote') }).first()), ['default', 'hover'], { group: h, title: 'Feature card', sel: M('featureCardBlock') });
  await S('pricing-card', await prefer(q(M('card')).filter({ hasText: /\$\s?\d/ }).first(), q(M('cardWrapper')).filter({ hasText: /\$\s?\d/ }).first()), ['default'], { group: h, title: 'Pricing card', desc: 'The plan card with the $ price and the highlighted callout.', sel: M('card') + ' with $' });
  await S('price', await prefer(q(M('price')).first(), q(M('pricingHighlight')).first()), ['default'], { group: h, title: 'Price figure', sel: M('price') });
  await S('testimonial-arrow', await prefer(q(M('arrow')).first(), q(M('arrowsWrapper')).locator('button').first()), B4, { group: h, title: 'Testimonial arrow', sel: M('arrow') });
  await S('watch-button', await prefer(q(M('secondary')).filter({ hasText: /watch/i }).first(), await domFind(page, /^watch/i, { tag: 'm-watch' })), B4, { group: h, title: 'Watch testimonial button', desc: 'Measured, never pressed.', sel: M('secondary') + ' "Watch…"' });
  await S('oath-band', q(M('oathSection')).first(), ['default'], { group: h, title: 'Hippocratic oath band', sel: M('oathSection') });
  await S('quote-card', await prefer(q(M('quote')).first(), q(M('card')).filter({ hasText: /"/ }).first()), ['default'], { group: h, title: 'Testimonial card', sel: M('quote') });
  await S('rating-group', q(M('ratingGroup')).first(), ['default'], { group: h, title: 'Trustpilot rating block', sel: M('ratingGroup') });
  await S('condensed-form', q(M('condensedForm')).first(), ['default'], { group: h, title: 'Condensed chat form', desc: 'The slim repeat of the chat field near the footer: one textarea and a Get started button.', sel: M('condensedForm') });
  await S('condensed-button', await prefer(q(M('condensedButton')).first(), await domFind(page, /^get started$/i, { tag: 'm-gs' })), B4, { group: h, title: 'Get started button', desc: 'Measured, never pressed.', sel: M('condensedButton') });
  await S('pause-control', await prefer(q('button[aria-label*="pause" i]').first(), q('button[aria-label*="animation" i]'), q('button[aria-label*="motion" i]')), B4, { group: h, title: 'Animation pause control', desc: 'The round control pinned bottom-right that pauses the page\'s motion. Measured, never pressed.', sel: 'button[aria-label*="pause"]' }, { noScroll: true });
  // The page footer is the LAST footer element; earlier <footer>s are card
  // footers inside sections.
  const pageFooter = await prefer(q('footer').last(), q(M('footer')).last());
  await S('footer', pageFooter, ['default'], { group: h, title: 'Footer', desc: 'The deep page footer: link columns, legal row and the "Made in" note.', sel: 'last footer' });
  await S('footer-social-icon', await prefer(pageFooter.locator('a').filter({ hasText: / on (instagram|x|twitter|linkedin|facebook|tiktok|youtube)\b/i }).first(), pageFooter.locator('a').first()), B4, { group: h, title: 'Footer social icon link', desc: 'An aria-labelled icon link in the footer\'s social row (e.g. "Doctronic on Instagram"). Measured, never followed.', sel: 'footer a' });
  await S('footer-legal-link', await domFind(page, /privacy policy|terms of service/i, { sel: 'footer a, footer button, footer [role="link"]', tag: 'm-fll' }), B4, { group: h, title: 'Footer legal link', desc: 'Privacy Policy / Terms of Service in the legal row. Measured, never followed.', sel: 'footer legal link' });
  await S('footer-legal', await prefer(q(M('legal')).first(), q(M('legalText')).first()), ['default'], { group: h, title: 'Legal line', sel: M('legal') });
}

// ---------- chat (/chat/) ----------

async function chat() {
  await newPage('chat', { wait: 8000 });
  await sheetsFor('chat');
  const g = G.chat;
  await S('chat-sidebar', q(M('sidebar')).first(), ['default'], { group: g, title: 'Chat sidebar (collapsed)', desc: 'The left rail as a signed-out visitor first sees it: collapsed to the logo and toggle.', sel: M('sidebar') }, { noScroll: true });
  const toggleB = await prefer(page.getByRole('button', { name: /expand sidebar|collapse sidebar/i }).first(), q(M('toggleButton')));
  await S('sidebar-toggle', toggleB, B4, { group: g, title: 'Sidebar expand button', sel: 'button "Expand sidebar"' }, { noScroll: true });
  // Expand the drawer — the sidebar's own toggle, a local presentation state.
  await toggleB.click().catch(() => {});
  await page.waitForTimeout(900);
  await S('chat-sidebar-open', q(M('sidebar')).first(), ['default'], { group: g, title: 'Chat sidebar (expanded)', desc: 'Opened with the sidebar\'s own Expand button: New chat highlighted at the top, Health record / Appointments / Prescriptions below, then Sign up and Log in pinned at the bottom.', sel: M('sidebar') + ' expanded' }, { noScroll: true });
  await S('nav-link-current', await prefer(q(M('wrapper')).filter({ hasText: /new chat/i }).first(), q('a[class*="_highlighted"]')), ['default'], { group: g, title: 'Sidebar link, current', desc: 'New chat: the highlighted row in the expanded rail.', sel: M('wrapper') + ' highlighted' }, { noScroll: true });
  await S('nav-link', await prefer(q(M('wrapper')).filter({ hasText: /health record/i }).first(), q(M('wrapper')).filter({ hasNotText: /new chat/i }).first()), B4, { group: g, title: 'Sidebar link', sel: M('wrapper') }, { noScroll: true });
  await S('signup-free', page.getByRole('button', { name: /sign up for free/i }).first(), B4, { group: g, title: 'Sign up for free button', desc: 'The blue primary button pinned at the bottom of the expanded rail. Measured, never pressed.', sel: 'button "Sign up for free"' }, { noScroll: true });
  await S('sidebar-login', await prefer(q(M('sidebar')).getByRole('button', { name: /log in/i }).first(), page.getByRole('button', { name: /^log in$/i }).first()), B4, { group: g, title: 'Sidebar log in button', desc: 'The secondary button beside Sign up for free. Measured, never pressed.', sel: 'button "Log in"' }, { noScroll: true });
  await S('anon-badge', await prefer(q(M('badgeButton')).first(), page.getByRole('button', { name: /anonymous/i })), ['default', 'hover'], { group: g, title: 'Anonymous badge', desc: 'The "Anonymous" session chip. Pressing it is a sign-in path, so it was hovered and measured only.', sel: M('badgeButton') }, { noScroll: true });
  await S('support-link', q('a[href^="mailto:"]').first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Support mail link', sel: 'a[href^="mailto:"]' }, { noScroll: true });
  // The legal row's anchors are picked by destination, never by position:
  // the footer's first <a> is the support@ mailto (already support-link).
  await S('legal-link', await prefer(q(M('footer')).locator('a[href*="privacy" i], a[href*="terms" i]').first(), await domFind(page, /terms of service|privacy policy/i, { sel: 'footer a, [class*="_footer"] a', tag: 'm-tos' })), B4, { group: g, title: 'Legal link', desc: 'The Terms of Service / Privacy Policy link in the chat footer. Measured, never followed.', sel: 'footer a[href*="privacy"|"terms"]' }, { noScroll: true });
  await S('recent-chats', await domFind(page, /view recent chats/i, { tag: 'm-recent' }), ['default', 'hover'], { group: g, title: 'View recent chats', desc: 'Link to the (signed-in) chat list; measured only.', sel: '"View recent chats"' }, { noScroll: true });

  await S('chat-hero', await prefer(q('h1').filter({ hasText: /chat for free/i }).first().locator('xpath=ancestor::*[.//textarea][1]'), q('main').first()), ['default'], { group: g, title: 'Chat hero', desc: 'The centered empty-state: the Fraunces greeting and the large input card.', sel: 'h1 ancestor holding textarea' });
  await S('chat-greeting', await prefer(q('main h1').first(), q('h1').first(), q(M('display40')).first()), ['default'], { group: g, title: 'Chat greeting', sel: 'h1' });
  // The painted card is the <form> itself; the _inputCard match higher up is
  // the transparent .wrapper.chatInput that also carries the disclaimer line.
  await S('input-card', await prefer(q('form[class*="_inputCard"]').first(), q(M('inputCard'))), ['default', 'hover'], { group: g, title: 'Chat input card', desc: 'The large raised card holding the textarea and the round Send button; expands when focused.', sel: 'form[class*="_inputCard"]' });
  await S('chat-textarea', q('textarea[placeholder]').first(), ['default', 'focused', 'filled'], { group: g, title: 'Chat textarea', desc: '"Ask a question about your health…" — text was typed and deleted, Enter never pressed.', sel: 'textarea' }, { fillText: 'I have a headache since this morning' });
  await S('send-button', await prefer(page.getByRole('button', { name: /send message/i }).first(), q(M('submitButton'))), B4, { group: g, title: 'Send message button', desc: 'The condensed dark submit control inside the card. Measured, never pressed — pressing would send a message.', sel: M('submitButton') });
  await S('starter', q(M('starter')).first(), B4, { group: g, title: 'Starter chip', desc: '"Check my symptoms" — a conversation starter under the card. Measured, never pressed.', sel: M('starter') });
  await S('disclaimer', await prefer(q(M('disclaimer')).first(), await domFind(page, /not a substitute|doctronic is not/i, { sel: 'p,div,span', tag: 'm-disc', leaf: true })), ['default'], { group: g, title: 'Medical disclaimer', sel: M('disclaimer') });
  await page.close();
}

// ---------- sign-in dialog (/?modal=signin) ----------

async function signin() {
  await newPage('signin', { wait: 8000 });
  const g = G.overlay;
  // [role="dialog"] is the transparent inner section; the card that paints the
  // surface (24px radius, raised canvas, the lg shadow) is its div.modal parent.
  const dlg = await prefer(q('div[class*="_modal"]').first(), q('[role="dialog"]').first(), q(M('dialog')).first());
  await S('signin-dialog', dlg, ['default'], { group: g, title: 'Sign-in dialog', desc: 'Reached by the public ?modal=signin URL: a centered raised card over a dimmed page. Nothing inside it was pressed.', sel: 'div[class*="_modal"] (the [role="dialog"] card\'s painted parent)' }, { noScroll: true });
  await S('signin-title', dlg.locator('h1, h2, [class*="display"], [class*="heading"]').first(), ['default'], { group: g, title: 'Sign-in title', sel: 'dialog heading' }, { noScroll: true });
  await S('email-login-button', await prefer(dlg.getByRole('button', { name: /log in with email|email/i }).first(), dlg.locator(M('primary')).first()), B4, { group: g, title: 'Log in with email button', desc: 'The primary action inside the dialog. Measured, never pressed.', sel: 'dialog button "Log in with email"' }, { noScroll: true });
  await S('oauth-button', await prefer(dlg.getByRole('button', { name: /continue with|google|apple/i }).first(), dlg.locator(M('secondary')).first()), B4, { group: g, title: 'OAuth button', desc: 'A Continue-with provider button. Measured, never pressed.', sel: 'dialog OAuth button' }, { noScroll: true });
  await S('create-account-link', await prefer(dlg.getByRole('link', { name: /create an account|sign up/i }).first(), dlg.getByRole('button', { name: /create an account/i })), B4, { group: g, title: 'Create an account link', desc: 'Measured, never followed.', sel: 'dialog "Create an account"' }, { noScroll: true });
  await S('dialog-close', await prefer(dlg.getByRole('button', { name: /close|dismiss/i }).first(), dlg.locator(M('close')).first()), B4, { group: g, title: 'Dialog close button', sel: 'dialog close button' }, { noScroll: true });
  out._meta.signinBackdrop = await page.evaluate(() => {
    const d = document.querySelector('[role="dialog"]');
    const res = [];
    for (let n = d && d.parentElement; n && res.length < 4; n = n.parentElement) {
      const c = getComputedStyle(n);
      if (c.backgroundColor !== 'rgba(0, 0, 0, 0)' || c.backdropFilter !== 'none') res.push({ node: (n.className || '').toString().slice(0, 80), bg: c.backgroundColor, backdrop: c.backdropFilter });
    }
    return res;
  });
  await page.close();
}

// ---------- symptom checker ----------

async function symptom() {
  await newPage('symptom', { wait: 8000 });
  const g = G.symptom;
  await S('symptom-title', await prefer(q('main h1').first(), q('h1').first()), ['default'], { group: g, title: 'Symptom-checker headline', desc: '"…your private and personal AI symptom checker" in the Fraunces display face.', sel: 'h1' });
  const ta = q('textarea[placeholder]').first();
  await S('symptom-input-card', await prefer(ta.locator('xpath=ancestor::*[self::div or self::form][position()<=3]').last(), ta), ['default', 'hover'], { group: g, title: 'Symptom input card', desc: 'The raised card holding the symptoms textarea and the Check button.', sel: 'textarea ancestor card' });
  await S('symptom-textarea', ta, ['default', 'focused', 'filled'], { group: g, title: 'Symptoms textarea', desc: '"Describe your symptoms…" — text was typed and deleted, never submitted.', sel: 'textarea' }, { fillText: 'I have a headache since this morning' });
  await S('check-button', await prefer(page.getByRole('button', { name: /check my symptoms/i }).first(), await domFind(page, /check my symptoms/i, { tag: 'm-chk' })), B4, { group: g, title: 'Check My Symptoms button', desc: 'Measured, never pressed — pressing would submit symptoms.', sel: '"Check My Symptoms"' });
  await S('brings-pill', await domFind(page, /what brings you in/i, { sel: 'span,p,div,a,button', tag: 'm-pill2', leaf: true }), ['default'], { group: g, title: '"What brings you in?" pill', sel: '"What brings you in?"' });
  await page.close();
}

// ---------- content pages (Tailwind utilities) ----------

async function marketingChrome(g) {
  // Content pages (blog, telehealth, …) carry the link-row top bar: wordmark,
  // About/FAQ/Blog/Online Treatment/Wall of Love/LegitScript and the
  // "Try Doctronic For Free" pill. It may be a <header> or a _header div.
  const header = await prefer(q('header').first(), q(M('marketingHeader')).first(), q(M('header')).first());
  await S('mkt-header', header, ['default'], { group: g, title: 'Marketing top bar', desc: 'The pill-link bar shared by the content pages: wordmark, About/FAQ/Blog/Online Treatment/Wall of Love, "Try Doctronic For Free" and Sign up.', sel: 'header' }, { noScroll: true });
  await S('mkt-nav-pill', await prefer(header.locator('a').filter({ hasText: /^Blog$/ }).first(), header.locator('a').nth(2)), B4, { group: g, title: 'Marketing pill link', sel: 'header a' }, { noScroll: true });
  await S('try-button', await prefer(header.locator('a').filter({ hasText: /try doctronic/i }).first(), await domFind(page, /try doctronic for free/i, { tag: 'm-try' })), B4, { group: g, title: 'Try Doctronic button', desc: 'The dark rounded-full CTA link in the top bar. Measured, never followed.', sel: 'header a "Try Doctronic For Free"' }, { noScroll: true });
  await S('mkt-signup', await prefer(header.getByRole('button', { name: /sign up/i }).first(), header.locator('a').filter({ hasText: /sign up/i }).first()), B4, { group: g, title: 'Marketing sign up', desc: 'Measured, never pressed.', sel: 'header "Sign up"' }, { noScroll: true });
  const mFooter = q('footer').last();
  await S('mkt-footer', mFooter, ['default'], { group: g, title: 'Marketing footer', desc: 'The link-column footer shared by the content pages.', sel: 'last footer' });
  await S('mkt-footer-link', await prefer(mFooter.locator('a').filter({ hasText: /privacy|terms/i }).first(), mFooter.locator('a').first()), B4, { group: g, title: 'Marketing footer link', desc: 'A link in the content-page footer (a social icon link if the legal row has no text links). Measured, never followed.', sel: 'footer a' });
}

async function blog() {
  await newPage('blog', { wait: 8000 });
  const g = G.content;
  await marketingChrome(g);
  await S('blog-title', await prefer(q('main h1').first(), q('h1').first()), ['default'], { group: g, title: 'Blog title', sel: 'h1' });
  await S('blog-search', await prefer(q('input[type="search"]').first(), q('input[placeholder*="earch" i]')), ['default', 'focused', 'filled'], { group: g, title: 'Blog search field', desc: 'Text was typed and deleted; search was never submitted.', sel: 'input[type="search"]' }, { fillText: 'prescription' });
  // Article cards are Tailwind divs (rounded-[14px] border) with a gradient
  // thumbnail; category chips are rounded-full links above the grid.
  const card = await prefer(q('main a').filter({ has: q('h3') }).first(), q('main [class*="rounded-[14px]"]').first());
  await S('category-chip', await prefer(q('main a[class*="rounded-full"]').filter({ hasText: /allergies|medicine|health/i }).first(), q('main a[class*="rounded-full"]').first()), B4, { group: g, title: 'Category chip', desc: 'A tinted pill filtering the article grid ("Allergies", "Mental Health", …). Measured, never followed.', sel: 'main a.rounded-full' });
  await S('article-card', card, ['default', 'hover', 'focus-visible'], { group: g, title: 'Article card', desc: 'A post card: gradient thumbnail with a centred glyph, category/date line and title; the whole card is one link.', sel: 'main [class*="rounded-[14px]"]' });
  await S('article-card-title', await prefer(card.locator('h2, h3').first(), card.locator('[class*="font-"], p').last()), ['default'], { group: g, title: 'Article card title', sel: 'card title' }, { crop: false });
  await S('body-h2', q('main h2').first(), ['default'], { group: g, title: 'Content h2', sel: 'h2' });
  await page.close();
}

async function telehealth() {
  await newPage('telehealth', { wait: 8000 });
  const g = G.content;
  await S('telehealth-title', await prefer(q('main h1').first(), q('h1').first()), ['default'], { group: g, title: 'Telehealth headline', sel: 'h1' });
  await S('telehealth-lede', await prefer(q('main h1').locator('xpath=following::*[self::p or self::div][1]').first(), q('main p').first()), ['default'], { group: g, title: 'Telehealth lede', sel: 'first p after h1' }, { crop: false });
  await S('telehealth-cta', await prefer(await domFind(page, /get started|start (a |your )?(visit|chat)|talk to|see (a |the )?doctor|try doctronic/i, { sel: 'main a, main button', tag: 'm-cta', leaf: true }), await domFind(page, /try doctronic for free/i, { tag: 'm-cta2' })), B4, { group: g, title: 'Telehealth CTA', desc: 'The page\'s primary call to action — the dark "Try Doctronic For Free" pill shared with the top bar. Measured, never pressed.', sel: 'first CTA in main' });
  await S('step-block', q('main h2').first(), ['default'], { group: g, title: 'Telehealth section heading', sel: 'h2' });
  await page.close();
}

async function authors() {
  await newPage('authors', { wait: 8000 });
  const g = G.content;
  await S('authors-title', await prefer(q('main h1').first(), q('h1').first()), ['default'], { group: g, title: 'Authors headline', sel: 'h1' });
  // Author cards are <li> rows in the reviewers grid (the first <li> in main
  // is a breadcrumb, so the portrait is the discriminant); the whole card is
  // one "group" link holding the portrait.
  const card = await prefer(q('main li').filter({ has: q('img') }).first(), q('main a').filter({ has: q('img') }).first());
  await S('author-card', card, ['default', 'hover'], { group: g, title: 'Author card', desc: 'A reviewer card: portrait, name and medical credential line, with a "View profile" link.', sel: 'main li' });
  await page.close();
}

async function resource() {
  await newPage('resource', { wait: 8000 });
  const g = G.content;
  await S('resource-title', await prefer(q('main h1').first(), q('h1').first()), ['default'], { group: g, title: 'Resource center headline', sel: 'h1' });
  // /resource-center/ is one long prose sheet (a white rounded-2xl card).
  const sheet = await prefer(q('main [class*="prose"]').first(), q('main [class*="rounded-2xl"]').first());
  await S('resource-sheet', sheet, ['default'], { group: g, title: 'Resource article sheet', desc: 'The long-form white card the Resource Center is typeset into.', sel: 'main [class*="prose"]' });
  await S('body-copy', q('main p').first(), ['default'], { group: g, title: 'Body copy', sel: 'main p' }, { crop: false });
  await page.close();
}

async function wall() {
  await newPage('wall', { wait: 8000 });
  const g = G.content;
  await S('wall-title', await prefer(q('main h1').first(), q('h1').first()), ['default'], { group: g, title: 'Wall of Love headline', sel: 'h1' });
  // Review cards are .break-inside-avoid tiles in a CSS-columns masonry.
  const card = await prefer(q('main [class*="break-inside-avoid"]').first(), q('main [class*="rounded-[24px]"]').first());
  await S('love-card', card, ['default', 'hover'], { group: g, title: 'Testimonial card', desc: 'A review card on the Wall of Love: avatar, first name, quote and the Love/Reply footer row.', sel: 'main [class*="break-inside-avoid"]' });
  await page.close();
}

// ---------- dark theme ----------

async function dark() {
  await newPage('dark');
  const g = G.dark;
  out._meta.darkApplied = await page.evaluate(() => ({ theme: document.documentElement.getAttribute('data-theme'), bg: getComputedStyle(document.body).backgroundColor }));
  const dHeader = await prefer(q(M('marketingHeader')).first(), q(M('header')).first(), q('header').first());
  await S('d-header', dHeader, ['default'], { group: g, title: 'Top bar, dark', desc: 'The same bar under data-theme="dark": sunken dark ground, light text.', sel: M('marketingHeader') }, { noScroll: true });
  await S('d-signup-button', await prefer(dHeader.getByRole('button', { name: /sign up/i }).first(), dHeader.locator('a,button').filter({ hasText: /sign up/i }).first()), B4, { group: g, title: 'Sign up button, dark', sel: 'top bar "Sign up"' }, { noScroll: true });
  const dHero = q('textarea[placeholder]').first().locator('xpath=ancestor::*[.//h1][1]');
  await S('d-hero', dHero, ['default'], { group: g, title: 'Hero, dark', sel: 'textarea ancestor holding h1' });
  await S('d-hero-title', await prefer(dHero.locator('h1').first(), q('h1').filter({ hasText: /doctronic/i }).last()), ['default'], { group: g, title: 'Hero headline, dark', sel: 'hero h1' });
  await S('d-input-card', await prefer(q(M('inputContainer')).first(), q(M('heroInputWrapper')), q(M('inputCard'))), ['default'], { group: g, title: 'Chat field, dark', sel: M('inputContainer') });
  await S('d-start-button', await prefer(q(M('submitButton')).first(), await domFind(page, /^start chat$/i, { tag: 'm-dsc' })), ['default'], { group: g, title: 'Start chat button, dark', sel: M('submitButton') });
  await S('d-pill', await prefer(q(M('pill')).first(), await domFind(page, /what brings you in/i, { sel: 'span,p,div', tag: 'm-dpill', leaf: true })), ['default'], { group: g, title: 'Prompt pill, dark', sel: M('pill') });
  await S('d-footer', await prefer(q('footer').last(), q(M('footer')).last()), ['default'], { group: g, title: 'Footer, dark', sel: 'last footer' });
  await page.close();
}

// ---------- mobile ----------

async function mobile() {
  const g = G.mobile;
  await newPage('home', { mobile: true });
  const header = await prefer(q(M('marketingHeader')).first(), q(M('header')).first(), q('header').first());
  await S('m-header', header, ['default'], { group: g, title: 'Top bar (mobile)', desc: 'The 390px header: wordmark, Sign up and the menu button (Log in is dropped at this width).', sel: M('marketingHeader') }, { noScroll: true });
  await S('m-menu-button', await prefer(q(M('expandHitArea')).first(), header.locator('button[aria-label]').first(), header.locator('button').last()), ['default'], { group: g, title: 'Mobile menu button', sel: 'menu button' }, { noScroll: true });
  const mHero = q('textarea[placeholder]').first().locator('xpath=ancestor::*[.//h1][1]');
  await S('m-hero', mHero, ['default'], { group: g, title: 'Hero (mobile)', sel: 'textarea ancestor holding h1' });
  await S('m-hero-title', await prefer(mHero.locator('h1').first(), q('h1').filter({ hasText: /doctronic/i }).last()), ['default'], { group: g, title: 'Hero headline (mobile)', sel: 'hero h1' });
  await S('m-input-card', await prefer(q(M('inputContainer')).first(), q(M('heroInputWrapper')), q(M('inputCard'))), ['default'], { group: g, title: 'Chat field (mobile)', sel: M('inputContainer') });
  await S('m-start-button', await prefer(q(M('submitButton')).first(), await domFind(page, /^start chat$/i, { tag: 'm-msb' })), ['default'], { group: g, title: 'Start chat button (mobile)', sel: M('submitButton') });
  await S('m-footer', await prefer(q('footer').last(), q(M('footer')).last()), ['default'], { group: g, title: 'Footer (mobile)', sel: 'last footer' });
  await page.close();
  await newPage('chat', { mobile: true, wait: 8000 });
  await S('m-chat-header', await prefer(q(M('mobileHeader')).first(), q(M('header')).first(), q('header').first()), ['default'], { group: g, title: 'Chat top bar (mobile)', sel: M('mobileHeader') }, { noScroll: true });
  await S('m-input-card-chat', await prefer(q('form[class*="_inputCard"]').first(), q(M('inputCard'))), ['default'], { group: g, title: 'Chat input card (mobile)', sel: 'form[class*="_inputCard"]' });
  await S('m-starter', q(M('starter')).first(), ['default'], { group: g, title: 'Starter chip (mobile)', sel: M('starter') });
  await page.close();
}

const PAGES = { home, chat, signin, symptom, blog, telehealth, authors, resource, wall, dark, mobile };
const want = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(PAGES);
const done = new Set(); // pages whose capture ran to the end
for (const k of want) {
  const l = await launch({ mobile: k === 'mobile', theme: THEME[k] || 'light' });
  context = l.context;
  run = k;
  try { await PAGES[k](); done.add(k); } catch (e) { log('PAGE FAILED', k, String(e.message).split('\n')[0]); }
  out._meta.read = new Date().toLocaleDateString('en-CA'); // the local date of the capture
  save();
  await l.browser.close();
}
// a component a page no longer produces is dropped, so a re-run cannot leave stale entries; a page that
// failed partway keeps its earlier entries, since what it did not reach is not known to be gone
for (const [key, c] of Object.entries(out.components)) if (done.has(c.run) && !touched.has(key)) { delete out.components[key]; log('dropped stale', key); }
// the same for states: a state an earlier run recorded that this finished run's spec no longer lists goes
for (const [key, c] of Object.entries(out.components)) {
  if (!done.has(c.run) || !listed.has(key)) continue;
  for (const st of Object.keys(c.states || {})) if (!listed.get(key).has(st)) { delete c.states[st]; log('dropped stale state', key, st); }
}
save();
log('done ->', OUT);
