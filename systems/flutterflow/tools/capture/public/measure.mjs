// Measures flutterflow.io's components on its public pages, in every state
// that can be reached without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing enterprise product studio mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// flutterflow.io ships two generations of its marketing skin: the home page
// carries the older module set (.composer/.cmp-*, .pbtn, .pg-*, .apps), and
// every other public page carries the new ff-* component layer (.ff-btn,
// .ff-fld, .ff-snav, .ff-acc, .ff-seg, .ff-tsw, .ff-tbs). Both are measured.
//
// States:
//   hover          real mouse hover, 450ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or submit button can fire
//   focused        the field clicked into (a text field only)
//   filled         sample text typed into a field, measured, then deleted; Enter is never pressed
//   open/selected  a resting state reached by the page's own UI toggles — a
//                  snav menu button, the billing segmented control, a tab,
//                  an accordion summary, the mobile sheet's Open button
//   dark           the same component measured again with the site's own
//                  theme switch flipped to Dark (data-theme="dark", the
//                  ff-theme localStorage key); restored afterwards
//   anything else  a resting state reached by the page itself; nothing that
//                  submits a form, signs in or starts building is ever pressed
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, open, patch, setTheme, styleOf, crop, centre, RAW } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: '/',
  pricing: '/pricing',
  enterprise: '/enterprise',
  product: '/product',
  studio: '/studio',
  showcase: '/studio/showcase',
};

let page, cdp, current, context, run;
const touched = new Set();

// ---------- helpers ----------

async function newPage(key, { mobile = false, theme = null, wait = 6000 } = {}) {
  current = key;
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '', theme ? `(${theme})` : '');
  if (!(await open(page, BASE + URLS[key], { wait }))) throw new Error(`BLOCKED ${key}: the page never loaded, nothing measured`);
  if (theme) await setTheme(page, theme);
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

// Clicks a UI toggle (tab, segment, accordion summary, menu button). Refuses
// a submit button and any control whose text names an action this kit must
// never take.
const NEVER = /^(send|submit|sign in|log in|create|generate|upload|start building|start free|apply|open studio|talk to sales|book|subscribe|request|resend|continue)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

function comp(key, meta) {
  const c = (out.components[key] ??= {});
  // A rerun replaces the component's evidence wholesale: old states from a list
  // the current run no longer measures would otherwise linger, and a `missing`
  // flag from an earlier failed run would survive a successful recapture.
  c.states = {};
  delete c.missing;
  Object.assign(c, { page: current, run, url: URLS[current] && BASE + URLS[current] }, meta);
  touched.add(key);
  return c;
}

async function measure(key, state, target, opts = {}) {
  // opts.hidden targets an element that is in the DOM but unpainted (display:
  // none) — filtering it visible again would make its declared slot unreadable.
  const loc = opts.hidden ? target.first() : target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false && !opts.hidden) {
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

const FILL = 'A habit tracker for two people';

// Records the listed states of one component. meta: title, group, desc, sel.
async function S(key, target, list, meta = {}, opts = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (opts.open) { await reset(); await opts.open(); }
  const loc = opts.hidden ? target.first() : target.filter({ visible: true }).first();
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
      } else if (st === 'dark') {
        undo = 'theme';
        await setTheme(page, 'dark');
        await page.waitForTimeout(300);
        via = 'footer theme switch set to Dark (data-theme="dark"), restored after';
      } else if (opts.stateOpen?.[st]) {
        await opts.stateOpen[st](loc);
        via = via || 'the page\'s own control';
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo === 'theme') { await setTheme(page, 'light'); await page.waitForTimeout(300); }
    else if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const B5 = [...B4, 'dark'];

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
    for (const ss of document.styleSheets) { try { walk(ss.cssRules); } catch { /* cross-origin, read by vars.mjs */ } }
    return transitions;
  });
  out._meta.sheets ??= {};
  out._meta.sheets[key] = res;
}

// ---------- groups ----------
const G = {
  shell: 'Shell and navigation', home: 'Home (earlier skin)', composer: 'Prompt composer',
  pricing: 'Pricing', form: 'Enterprise contact form', tabs: 'Tabs and disclosure',
  footer: 'Footer', overlay: 'Dialogs and overlays', content: 'Content pages', mobile: 'Mobile (390 wide)',
};

// ---------- shell + pricing (the ff-* layer) ----------
async function pricing() {
  await newPage('pricing');
  await sheetsFor('pricing');
  const g = G.shell;
  await S('skip-link', q('.ff-page-skip'), ['default'], { group: g, title: 'Skip to content link', desc: 'The first tab stop on every page: a visually-hidden link that paints when focused.', sel: '.ff-page-skip' }, { noScroll: true });
  await S('announcement', q('.ff-ban'), ['default', 'dark'], { group: g, title: 'Announcement banner', desc: 'The slim bar above the header ("FlutterFlow for Web is here"): the accent line colour, a "What\'s changing" link and a Dismiss icon button. Shown, never dismissed.', sel: '.ff-ban' }, { noScroll: true });
  await S('banner-dismiss', q('.ff-ban .ff-ibtn').first(), B4, { group: g, title: 'Banner dismiss button', desc: 'The small square icon button that closes the announcement bar. Measured, never pressed.', sel: '.ff-ban .ff-ibtn' }, { noScroll: true });
  await S('header', q('.ff-snav'), ['default', 'dark'], { group: g, title: 'Top nav', desc: 'The floating bar over every page: brand lockup, the Product/Studio/Resources menu buttons, Pricing and Enterprise links, Sign in and the Start building pill.', sel: '.ff-snav' }, { noScroll: true });
  await S('nav-menu-button', q('.ff-snav-menu').first(), B5, { group: g, title: 'Nav menu button', desc: 'A top-level menu trigger (Product): 14px nav text with a chevron; opens the snav panel.', sel: '.ff-snav-menu' }, { noScroll: true });
  await S('nav-panel', q('.ff-snav-panel').first(), ['default'], { group: g, title: 'Nav dropdown panel', desc: 'The Product flyout: a card-radius floating panel with lead link, column headings and item rows.', sel: '.ff-snav-panel' }, { noScroll: true, open: async () => { await toggle(q('.ff-snav-menu').first()); await page.waitForTimeout(900); } });
  await S('nav-panel-item', q('.ff-snav-col a, .ff-snav-panel a').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Nav dropdown item', sel: '.ff-snav-panel a' }, { noScroll: true, open: async () => { await toggle(q('.ff-snav-menu').first()); await page.waitForTimeout(900); } });
  await S('nav-link', q('.ff-snav-lk').filter({ hasText: 'Pricing' }).first(), B5, { group: g, title: 'Nav link', desc: 'The plain text links in the bar (Pricing, Enterprise).', sel: '.ff-snav-lk' }, { noScroll: true });
  await S('nav-signin', q('.ff-snav-signin').first(), B4, { group: g, title: 'Sign in link', desc: 'The secondary text link in the nav end. Measured, never followed.', sel: '.ff-snav-signin' }, { noScroll: true });
  await S('btn-primary-sm', q('.ff-snav .ff-btn-primary').first(), B5, { group: g, title: 'Start building (nav, small)', desc: 'The small contrast pill in the nav: --ff-color-contrast fill, --ff-color-contrast-ink text, radius pill. Measured, never followed.', sel: '.ff-btn.ff-btn-primary.ff-btn-sm' }, { noScroll: true });
  await S('brand', q('.ff-lkp').first(), ['default'], { group: g, title: 'Brand lockup', desc: 'The FlutterFlow mark + wordmark link; the mark is a filtered image (--ff-theme-logo-filter) so it inverts in dark.', sel: '.ff-lkp' }, { noScroll: true });

  const pr = G.pricing;
  await S('plan-grid', q('.ff-plg'), ['default'], { group: pr, title: 'Plan grid', desc: 'The plans list: a carded grid of plan columns under the billing toggle.', sel: '.ff-plg' });
  await S('plan-card', q('.ff-plg > li, .ff-plg [class*="plan"]').filter({ visible: true }).first(), ['default'], { group: pr, title: 'Plan card', desc: 'One plan column: name, price, feature rows and its CTA.', sel: '.ff-plg > li' });
  await S('billing-seg', q('.ff-seg').first(), ['default', 'selected'], { group: pr, title: 'Billing period segmented control', desc: 'A two-option radiogroup (Monthly/Yearly) with a sliding badge: role=radiogroup, each option a role=radio button; the pill slides via --ff-seg-x/width vars.', sel: '.ff-seg' }, { stateOpen: { selected: async (loc) => { const y = loc.locator('[data-ff-value="yearly"]').first(); await y.click(); await page.waitForTimeout(600); } } });
  await S('billing-seg-option', q('.ff-seg [data-ff-value="monthly"]').first(), B4, { group: pr, title: 'Segmented control option', sel: '.ff-seg [role="radio"], .ff-seg [data-ff-value]' });
  await S('plan-cta', q('.ff-btn-secondary').filter({ hasText: 'Start free' }).first(), B5, { group: pr, title: 'Plan CTA (secondary)', desc: 'The secondary button: --ff-color-card fill with the hairline rule and resting shadow. Measured, never followed.', sel: '.ff-btn.ff-btn-secondary' });
  await S('plan-cta-primary', q('.ff-btn-primary').filter({ hasText: /Start|Apply|Contact/ }).first(), B4, { group: pr, title: 'Plan CTA (primary)', desc: 'A contrast-fill call to action in the plan grid. Measured, never followed.', sel: '.ff-btn.ff-btn-primary' });
  const item = q('.ff-acc-item').first();
  await S('accordion-item', item, ['default'], { group: pr, title: 'FAQ accordion item', desc: 'A details/summary row in the questions list: hairline-separated, a plus/cross marker that turns on open. The first item ships open, so this resting reading is the open look.', sel: '.ff-acc-item' });
  // The first FAQ ships open: toggle the summary only when the item is closed, and
  // verify it opened — a blind click would close it and save the wrong state.
  const openDetails = async () => {
    await centre(item);
    const isOpen = await item.evaluate((el) => el.open ?? el.hasAttribute('open'));
    if (!isOpen) {
      await item.locator('summary, .ff-acc-x, .ff-acc-a').first().click();
      await page.waitForTimeout(700);
    }
    const nowOpen = await item.evaluate((el) => el.open ?? el.hasAttribute('open'));
    if (!nowOpen) throw new Error('accordion item is not open after its own toggle');
    return isOpen ? 'already open at rest (verified, not toggled)' : 'opened by the page\'s own summary';
  };
  const closeDetails = async () => {
    await centre(item);
    const wasOpen = await item.evaluate((el) => el.open ?? el.hasAttribute('open'));
    if (wasOpen) {
      await item.locator('summary, .ff-acc-x, .ff-acc-a').first().click();
      await page.waitForTimeout(700);
    }
    const nowOpen = await item.evaluate((el) => el.open ?? el.hasAttribute('open'));
    if (nowOpen) throw new Error('accordion item is still open after its own toggle');
    return wasOpen ? 'closed by the page\'s own summary' : 'already closed at rest (verified, not toggled)';
  };
  await S('accordion-open', item, ['default'], { group: pr, title: 'FAQ accordion, open', desc: 'The same details element measured open; the summary is clicked only when the item is closed.', sel: '.ff-acc-item' }, { before: { default: openDetails } });
  await S('accordion-closed', item, ['default'], { group: pr, title: 'FAQ accordion, closed', desc: 'The same details element measured closed; the summary is clicked only when the item is open.', sel: '.ff-acc-item' }, { before: { default: closeDetails } });
  await S('link-go', q('.ff-go').first(), B4, { group: pr, title: 'Arrow link', desc: 'The text link with a trailing arrow ("Contact us", question rows): --ff-lnk. Measured, never followed.', sel: '.ff-go' });
  // the ff-cmp composer on pricing = the new-generation prompt field
  const cp = G.composer;
  await S('ff-composer', q('.ff-cmp').first(), ['default', 'hover'], { group: cp, title: 'Prompt composer (new skin)', desc: 'The "What should your app do?" field on inner pages: a rounded field (radius-field) with the prompt textarea, idea nav and the send button.', sel: '.ff-cmp' });
  await S('ff-composer-field', q('.ff-cmp-field').first(), ['default', 'focused', 'filled'], { group: cp, title: 'Composer field', desc: 'The single-line prompt textarea. Text was typed and deleted; nothing was sent.', sel: '.ff-cmp-field' }, { fieldLoc: q('.ff-cmp-field').first() });
  await S('ff-composer-go', q('.ff-cmp-go').first(), B4, { group: cp, title: 'Composer send button', desc: 'The round submit arrow (type=submit). Measured, never pressed.', sel: '.ff-cmp-go' });
  await S('ff-composer-key', q('.ff-cmp-key').first(), B4, { group: cp, title: 'Idea key chip', desc: 'The "Use this idea" suggestion chip inside the composer.', sel: '.ff-cmp-key' });

  const f = G.footer;
  await S('footer', q('footer, .ff-ftr-site-foot').first(), ['default'], { group: f, title: 'Footer', desc: 'The site foot: brand lockup, link columns, the legal bar, the theme switch and the privacy-choices button.', sel: '.ff-ftr-site-foot' });
  await S('footer-link', q('.ff-ftr-site-foot a, footer a').filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', sel: 'footer a' });
  await S('theme-switch', q('.ff-tsw').first(), ['default', 'dark'], { group: f, title: 'Theme switch', desc: 'The footer Light/Dark/"Match your system" radiogroup (data-ff-tsw; writes ff-theme to localStorage). The dark reading is measured with the switch on Dark.', sel: '.ff-tsw' });
  await S('theme-switch-pick', q('.ff-tsw [data-ff-tsw-pick="dark"]').first(), B4, { group: f, title: 'Theme switch option', desc: 'A role=radio button in the switch; the checked one carries aria-checked=true.', sel: '.ff-tsw [data-ff-tsw-pick]' });
  await S('cookie-button', q('.ft-cookie').first(), ['default'], { group: f, title: 'Privacy choices button', desc: 'The "Your Privacy Choices" footer button (hidden outside banner regions). Measured at rest.', sel: '.ft-cookie' });
  await page.close();
}

// ---------- enterprise: the form ----------
async function enterprise() {
  await newPage('enterprise');
  const g = G.form;
  await S('contact-form', q('form').filter({ has: q('.ff-fld-i') }).first(), ['default'], { group: g, title: 'Contact form', desc: 'The enterprise inquiry form: a carded column of labelled fields, topic radios, two custom selects, a textarea and the submit button. Measured and shot; never submitted.', sel: 'form' });
  await S('field', q('.ff-fld').first(), ['default'], { group: g, title: 'Field wrapper', desc: 'One form row: label (.ff-fld-l), the control (.ff-fld-i), an optional hint and the alert slot (.ff-fld-e).', sel: '.ff-fld' });
  await S('field-label', q('.ff-fld-l').first(), ['default'], { group: g, title: 'Field label', sel: '.ff-fld-l' }, { crop: false });
  const first = q('#contact-first');
  await S('text-field', first, ['default', 'hover', 'focused', 'filled'], { group: g, title: 'Text field', desc: 'A .ff-fld-i input: --ff-color-card fill, hairline border, radius-field-tall, --ff-shadow-field; focus paints --ff-shadow-field-focus. Text was typed and deleted; the form was never submitted.', sel: '.ff-fld-i' }, { fieldLoc: first });
  await S('textarea', q('#contact-msg'), ['default', 'focused'], { group: g, title: 'Text area', sel: 'textarea.ff-fld-i' }, { fieldLoc: q('#contact-msg') });
  const topic = q('input[name="topic"]').first();
  await S('radio', topic, ['default'], { group: g, title: 'Topic radio', desc: 'A native radio in the topic list; the checked state is the accent dot.', sel: 'input[name="topic"]' });
  await S('radio-checked', topic, ['default'], { group: g, title: 'Topic radio, checked', sel: 'input[name="topic"]' }, { open: async () => { await topic.check().catch(() => topic.evaluate((el) => { el.checked = true; el.dispatchEvent(new Event('change', { bubbles: true })); })); await page.waitForTimeout(300); } });
  const selT = q('button.ff-sel-t').first();
  await S('select', selT, B4, { group: g, title: 'Select (custom combobox)', desc: 'A role=combobox button styled as a field (.ff-fld-i.ff-sel-t); opens .ff-sel-p listbox of .ff-sel-o options. The native select behind it is kept at 1x1 off screen.', sel: 'button.ff-sel-t' });
  await S('select-popup', q('.ff-sel-p').first(), ['default'], { group: g, title: 'Custom select listbox', desc: 'The option popup: role=listbox card with option rows and the floating shadow.', sel: '.ff-sel-p' }, { noReset: true, noScroll: true, open: async () => { await selT.click(); await page.waitForTimeout(600); } });
  await S('select-option', q('.ff-sel-o').filter({ hasText: /\S/ }).first(), ['default', 'hover'], { group: g, title: 'Custom select option', sel: '.ff-sel-o' }, { noReset: true, noScroll: true, open: async () => { await selT.click(); await page.waitForTimeout(600); } });
  await S('field-error', q('.ff-fld-e').filter({ hasText: /\S/ }).first(), ['default'], { group: g, title: 'Field error text', desc: 'The alert slot under a field ("Pick the topic that best fits."): role=alert, --ff-color-danger text. Rendered in the DOM at rest but not painted until validation, so this is the declared style of the slot, not an observed error.', sel: '.ff-fld-e' }, { hidden: true });
  await S('submit', q('button[data-ff-submit]'), B4, { group: g, title: 'Submit button', desc: 'The primary submit ("Submit"). Measured, never pressed — the form was never sent.', sel: 'button[data-ff-submit]' });
  const cells = G.content;
  await S('cells-grid', q('.ff-cells-grid').first(), ['default'], { group: cells, title: 'Feature cells grid', desc: 'The bordered feature grid on the studio/enterprise pages: hairline cells with an icon, a title and a line each.', sel: '.ff-cells-grid' });
  await S('cells-item', q('.ff-cells-grid > *').filter({ visible: true }).first(), ['default'], { group: cells, title: 'Feature cell', sel: '.ff-cells-grid > *' });
  await page.close();
}

// ---------- product: tabs + accordion ----------
async function product() {
  await newPage('product');
  const g = G.tabs;
  await S('tablist', q('.ff-tbs-tabs').first(), ['default'], { group: g, title: 'Tab list', desc: 'A vertical tablist ("Parts of the backend"): role=tab rows over tabpanels; the selected tab is filled.', sel: '.ff-tbs-tabs' });
  const tab1 = q('#backend-t0');
  await S('tab-selected', tab1, B4, { group: g, title: 'Tab, selected', desc: 'The aria-selected tab: filled with the tint wash.', sel: '[role="tab"]' });
  const tab2 = q('#backend-t1');
  await S('tab', tab2, B4, { group: g, title: 'Tab', desc: 'An unselected tab row. The selected state was reached by clicking it (a UI toggle).', sel: '[role="tab"]' });
  await S('tab-after-click', tab2, ['default'], { group: g, title: 'Tab after selection', desc: 'The same tab after the page\'s own click selected it.', sel: '[role="tab"]' }, { open: async () => { await tab2.click(); await page.waitForTimeout(500); } });
  await S('accordion-item-product', q('.ff-acc-item').first(), ['default'], { group: g, title: 'FAQ accordion item (product)', sel: '.ff-acc-item' });
  const pbtn = G.home;
  await S('replay-btn', q('.ff-pbtn').first(), B4, { group: pbtn, title: 'Replay button', desc: 'The small outline "Replay" control on the demo panels (.ff-pbtn-outline).', sel: '.ff-pbtn' });
  await page.close();
}

// ---------- home: the earlier skin ----------
async function home() {
  await newPage('home');
  await sheetsFor('home');
  const g = G.home;
  await S('home-hero', q('.hx-cmp, .composer').first().locator('xpath=ancestor::*[self::section or self::div][1]'), ['default'], { group: g, title: 'Home hero', desc: 'The first band: the two-line display headline, the lede, the prompt composer and the check line, over the page ground with its grain texture.', sel: '.composer' }, { noScroll: true });
  await S('home-title', q('h1').first(), ['default', 'dark'], { group: g, title: 'Hero display', desc: '"Build an app by describing it" in the --ff-text-display size.', sel: 'h1' }, { noScroll: true });
  const cp = G.composer;
  await S('composer', q('.composer').first(), ['default', 'hover', 'dark'], { group: cp, title: 'Prompt composer (home skin)', desc: 'The hero prompt field: a large rounded card with the ghost idea text, the Tab hint and the round send button.', sel: '.composer' });
  await S('composer-field', q('#describe-hero'), ['default', 'focused', 'filled'], { group: cp, title: 'Composer textarea', desc: 'The prompt textarea; text was typed and deleted, nothing sent.', sel: '.cmp-field' }, { fieldLoc: q('#describe-hero') });
  await S('composer-ghost', q('.cmp-ghost-t').first(), ['default'], { group: cp, title: 'Composer ghost idea', desc: 'The suggested prompt painted as placeholder ghost text.', sel: '.cmp-ghost-t' });
  await S('composer-nav', q('.cmp-nav').first(), ['default', 'hover'], { group: cp, title: 'Idea nav button', desc: 'The previous/next idea arrows in the composer.', sel: '.cmp-nav' });
  await S('composer-key', q('.cmp-key').filter({ visible: true }).first(), ['default'], { group: cp, title: 'Idea key chip', desc: 'The "Use this idea" chip under the ghost text (home skin); only painted in the dock composer on this page.', sel: '.cmp-key' }, { hidden: true });
  await S('composer-go', q('.composer .cmp-go, .cmp-go').first(), B4, { group: cp, title: 'Send button', desc: 'The round submit arrow in the composer (type=submit). Measured, never pressed.', sel: '.cmp-go' });
  await S('btn-contrast', q('.btn-contrast').first(), B5, { group: g, title: 'Contrast button (footer band)', desc: 'The "Talk to sales" pill in the closing band: the old skin\'s contrast fill.', sel: '.btn.btn-contrast' });
  await S('btn-quiet', q('.btn-quiet').first(), B4, { group: g, title: 'Quiet button', desc: 'The secondary pill next to it.', sel: '.btn.btn-quiet' });
  await S('replay-btn-home', q('.pbtn.outline').first(), ['default'], { group: g, title: 'Replay button (home skin)', desc: 'The small outline Replay on the demo modules; never painted at rest on this page, so this is the hidden DOM slot\'s declared style, not a painted reading.', sel: '.pbtn.outline' }, { hidden: true });
  await S('app-card', q('.apps [class*="app"], .apps > *').filter({ visible: true }).first(), ['default'], { group: g, title: 'Generated app card', desc: 'A generated-app tile in the demo reel.', sel: '.apps' });
  const f = G.footer;
  await S('theme-switch-home', q('.ft-theme, .ff-tsw').first(), ['default'], { group: f, title: 'Theme switch (home skin)', sel: '.ft-theme' });
  await page.close();
}

// ---------- studio + showcase: content pages ----------
async function studio() {
  await newPage('studio');
  const g = G.content;
  await S('studio-hero', q('main h1').first(), ['default'], { group: g, title: 'Studio page display', sel: 'main h1' }, { noScroll: true });
  await S('ptag-studio', q('.ff-ptag').first(), ['default'], { group: g, title: 'Studio product tag', desc: 'The tinted product tag (.ff-ptag-studio): --ff-color-studio-tint ground, --ff-color-studio-ink label.', sel: '.ff-ptag' });
  await page.close();
}
async function showcase() {
  await newPage('showcase');
  const g = G.content;
  await S('showcase-card', q('main a, .ff-slot, [class*="card"]').filter({ visible: true }).nth(2), ['default', 'hover'], { group: g, title: 'Showcase card', desc: 'A published-app card in the Studio showcase grid. Hovered only; never opened.', sel: 'main a' });
  await page.close();
}

// ---------- mobile ----------
async function mobile() {
  await newPage('home', { mobile: true });
  const g = G.mobile;
  await S('m-nav', q('.ff-snav'), ['default'], { group: g, title: 'Top nav (390)', desc: 'The 390-wide bar: brand, the Open menu icon button.', sel: '.ff-snav' }, { noScroll: true });
  await S('m-open-menu', q('.ff-ibtn[aria-label="Open menu"]'), B4, { group: g, title: 'Open menu button', sel: '.ff-ibtn[aria-label="Open menu"]' }, { noScroll: true });
  await S('m-menu-dialog', q('.ff-snav-ms'), ['default'], { group: G.overlay, title: 'Mobile menu sheet', desc: 'The full-screen dialog.ff-snav-ms opened by the menu button: nav links, the lead card and the sign-in row.', sel: '.ff-snav-ms' }, { noScroll: true, open: async () => { await toggle(q('.ff-ibtn[aria-label="Open menu"]').first()); await page.waitForTimeout(1200); } });
  await S('m-menu-close', q('.ff-ibtn[aria-label="Close menu"]'), B4, { group: g, title: 'Close menu button', sel: '.ff-ibtn[aria-label="Close menu"]' }, { noScroll: true, open: async () => { await toggle(q('.ff-ibtn[aria-label="Open menu"]').first()); await page.waitForTimeout(1200); } });
  await S('m-composer', q('.composer, .ff-cmp').first(), ['default'], { group: g, title: 'Composer (390)', sel: '.composer' });
  await S('m-hero-title', q('h1').first(), ['default'], { group: g, title: 'Hero display (390)', sel: 'h1' }, { noScroll: true });
  await page.close();
}

const RUNS = { pricing, enterprise, product, home, studio, showcase, mobile };
const which = process.argv.slice(2);
const { browser } = await launch();
for (const name of which.length ? which : Object.keys(RUNS)) {
  if (!RUNS[name]) { log('unknown page', name); continue; }
  run = name;
  try {
    context = await browser.newContext(name === 'mobile'
      ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1', isMobile: true, hasTouch: true, locale: 'en-US' }
      : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36', locale: 'en-US', reducedMotion: 'no-preference' });
    await patch(context, { theme: 'light' });
    await RUNS[name]();
    save();
  } catch (e) {
    log('PAGE FAILED', name, String(e.message).split('\n')[0]);
    save();
  }
  await context.close();
}
out._meta.captured = new Date().toISOString();
out._meta.base = BASE;
save();
console.log('done ->', OUT);
await browser.close();
