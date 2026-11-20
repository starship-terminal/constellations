// Measures docs.x.ai's components on its public pages, in every state that
// can be reached without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home quickstart pricing faq generate-text apiref grok grok-bot
// build x-subscription mobile. Writes raw/components-computed.json (merged,
// so a subset of pages can be re-run) and one crop per component and state
// into components/crops/. raw/measurements.md is then built from the JSON
// by build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 500ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or button can fire
//   dark           the same element after the header's own theme button repaints
//                  html.dark (setTheme verifies the painted surface; the theme is
//                  switched back afterwards)
//   opened         a resting state reached by the component's own toggle: the
//                  Ctrl+K search dialog, the product switcher menu, a sidebar
//                  group's chevron, the phone's "Open navigation menu"
//   focused        the search field inside the opened dialog
// Nothing is typed, sent, bought or signed into. The only presses are local
// UI toggles the page's own chrome provides.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, BASE, M, open, closePromo, setTheme, paintedTheme, styleOf, crop, centre, domFind, patch, UA, UA_MOBILE, RAW } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: '/overview',
  quickstart: '/developers/quickstart',
  'generate-text': '/developers/model-capabilities/text/generate-text',
  pricing: '/developers/pricing',
  'rate-limits': '/developers/rate-limits',
  faq: '/developers/faq/general',
  apiref: '/developers/rest-api-reference/inference',
  'release-notes': '/developers/release-notes',
  cookbook: '/cookbook',
  grok: '/grok/overview',
  'grok-faq': '/grok/faq',
  'grok-guide': '/grok/user-guide',
  'grok-bot': '/grok-bot/overview',
  build: '/build/overview',
  'x-subscription': '/x-subscription/overview',
};

let page, cdp, context, current;

// ---------- state drivers ----------

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(300);
}

async function hover(loc) {
  await centre(loc);
  const b = await loc.boundingBox();
  if (b) { await page.mouse.move(b.x + b.width / 2, b.y + b.height / 2); await page.waitForTimeout(600); }
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  await page.waitForTimeout(400);
}

// CSS.forcePseudoState through CDP: the press never happens, so no link can
// navigate and no button can fire.
async function pressOn(loc) {
  const b = await loc.boundingBox();
  if (!b) return null;
  // Force the component's own node. The topmost node at its centre (DOM.getNodeForLocation) is a
  // text span or an svg, whose :active never triggers the component's own :active rule. Any marker a
  // failed earlier press left is cleared first, and this one is always removed.
  await page.evaluate(() => document.querySelectorAll('[data-m-press]').forEach((el) => el.removeAttribute('data-m-press')));
  let nodeId;
  try {
    await loc.evaluate((el) => el.setAttribute('data-m-press', '1'));
    const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
    ({ nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-press]' }));
  } finally {
    await loc.evaluate((el) => el.removeAttribute('data-m-press')).catch(() => {});
  }
  if (!nodeId) return null;
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['active', 'hover'] });
  await page.waitForTimeout(400);
  return nodeId;
}
const pressOff = (id) => id == null ? null : cdp.send('CSS.forcePseudoState', { nodeId: id, forcedPseudoClasses: [] }).catch(() => {});

// ---------- the component specs ----------
// find: page -> Locator. states: name -> 'hover' | 'focus-visible' |
// 'pressed' | 'dark' | 'opened:label' | (loc, page) => Promise<void>.
const via = { 'hover': 'mouse hover over the element', 'focus-visible': 'keyboard focus (Shift+Tab, Tab)', 'pressed': 'CDP CSS.forcePseudoState(:active:hover) — no real press', 'dark': 'same element after the header theme button repaints html.dark' };

const CHROME = [
  { key: 'docs-header', group: 'Docs chrome', title: 'Fixed header bar',
    desc: 'The 80px bar fixed over every page: wordmark, product switcher, section links, the ⌘K search pill, theme button and GitHub link.',
    sel: 'header', find: (p) => p.locator('header').first(), states: ['default', 'dark'] },
  { key: 'docs-logo', group: 'Docs chrome', title: 'Wordmark link',
    desc: 'The svg wordmark in the header, coloured by the primary foreground role.',
    sel: 'header a[aria-label*="home"]', find: (p) => p.locator('header a[aria-label*="home" i]').first(), states: ['default'] },
  { key: 'docs-section-link', group: 'Docs chrome', title: 'Header section link',
    desc: 'A product-section link in the header nav ("Grok Bot" — an inactive pill-shaped label).',
    sel: 'header nav a', find: (p) => p.locator('header nav a').filter({ hasText: /Grok Bot/ }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'docs-search-pill', group: 'Docs chrome', title: 'Search pill (⌘K)',
    desc: 'The rounded search field in the header that opens the cmdk dialog; carries the ⌘K hint.',
    sel: 'header button (text Search)', find: async (p) => await domFind(p, /^search/i, { sel: 'header button', tag: 'sp', minW: 80, minH: 24 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'docs-theme-button', group: 'Docs chrome', title: 'Theme button',
    desc: 'The round icon button that switches html.light/html.dark. "dark" shows it after its own press repaints the page.',
    sel: 'header button[aria-label*="theme"]', find: (p) => p.locator('header button[aria-label*="theme" i]').first(), states: ['default', 'dark'] },
  { key: 'docs-sidebar', group: 'Docs chrome', title: 'Section sidebar',
    desc: 'The left nav column: product links, the collapsible page groups and the active-page marker.',
    sel: 'aside', find: (p) => p.locator('aside').first(), states: ['default', 'dark'] },
  { key: 'docs-sidebar-link', group: 'Docs chrome', title: 'Sidebar page link',
    desc: 'A single page link in the sidebar nav.',
    sel: 'aside a', find: (p) => p.locator('aside a').filter({ visible: true }).nth(1), states: ['default', 'hover', 'focus-visible'] },
  { key: 'docs-sidebar-active', group: 'Docs chrome', title: 'Sidebar active link',
    desc: 'The link for the page being read, painted with the active style.',
    sel: 'aside a (first)', find: (p) => p.locator('aside a').filter({ visible: true }).first(), states: ['default'] },
  { key: 'docs-sidebar-group', group: 'Docs chrome', title: 'Sidebar collapsible group',
    desc: 'A collapsible group row; "opened" is reached by its own chevron press.',
    sel: 'aside button[class*="peer/menu-button"]', find: (p) => p.locator('aside button[class*="peer/menu-button"]').filter({ visible: true }).first(), states: ['default',
      async (loc) => { await loc.click({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(700); }] },
];

// The sticky footer bar only mounts on article pages (the overview has none):
// these specs run on quickstart.
const FOOTER = [
  { key: 'docs-page-footer', group: 'Docs chrome', title: 'Page footer bar',
    desc: 'The sticky bottom bar (bg-base, border-border-l1) with the page actions.',
    sel: 'footer', find: (p) => p.locator('footer').first(), states: ['default'] },
  { key: 'docs-footer-button', group: 'Docs chrome', title: '"Share feedback" button',
    desc: 'A footer action button in the sticky bar — measured, never pressed (it may open a feedback form).',
    sel: 'footer button (text Share feedback)', find: async (p) => await domFind(p, /share feedback/i, { sel: 'footer button', tag: 'nx', minW: 60, minH: 20 }), states: ['default', 'hover'] },
  { key: 'docs-markdown-link', group: 'Docs chrome', title: '"View as Markdown" link',
    desc: 'The small muted link that serves the page\'s raw markdown.',
    sel: 'a (text Markdown)', find: async (p) => await domFind(p, /markdown/i, { sel: 'main a', tag: 'md', minW: 60, minH: 10 }), states: ['default', 'hover'] },
];

const PROSE = [
  { key: 'prose-h1', page: 'quickstart', group: 'Docs prose', title: 'Page title (h1)',
    desc: 'The article title in font-display.', sel: 'main h1', find: (p) => p.locator('main h1').first(), states: ['default', 'dark'] },
  { key: 'prose-h2', page: 'quickstart', group: 'Docs prose', title: 'Section heading (h2)',
    desc: 'A numbered step heading.', sel: 'main h2', find: (p) => p.locator('main h2').first(), states: ['default'] },
  { key: 'prose-p', page: 'quickstart', group: 'Docs prose', title: 'Body paragraph',
    desc: 'A paragraph of the quickstart.', sel: 'main p', find: (p) => p.locator('main p').first(), states: ['default'] },
  { key: 'prose-inline-code', page: 'quickstart', group: 'Docs prose', title: 'Inline code span',
    desc: 'A `code` span inside prose, tinted by the solar accent.', sel: 'main p code, main li code', find: (p) => p.locator('main :is(p,li,td) code').filter({ visible: true }).first(), states: ['default'] },
  { key: 'prose-link', page: 'grok', group: 'Docs prose', title: 'Prose link',
    desc: 'A body-text link (the "Connectors" link on the Grok help page), underlined with the dotted solar decoration for code spans.',
    sel: 'main p a, main li a', find: (p) => p.locator('main :is(p,li) a').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'prose-copy-llm', page: 'faq', group: 'Docs prose', title: '"Copy for LLM" button',
    desc: 'The small muted button that copies the page for an LLM — a local clipboard action, pressed only with forcePseudoState.',
    sel: 'main button (text Copy for LLM)', find: async (p) => await domFind(p, /copy for llm/i, { sel: 'main button', tag: 'cl', minW: 40 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'faq-question', page: 'faq', group: 'Docs prose', title: 'FAQ question (h3)',
    desc: 'A question heading on the FAQ page — the FAQ lists plain headings, no accordion.',
    sel: 'main h3', find: (p) => p.locator('main h3').first(), states: ['default'] },
];

const WIDGETS = [
  { key: 'docs-code-block', page: 'home', group: 'Docs widgets', title: 'Code block (shiki)',
    desc: 'The shiki-highlighted sample under the hero: a dark-tinted panel even in the light theme.',
    sel: 'pre.shiki', find: (p) => p.locator('pre.shiki').first(), states: ['default', 'dark'] },
  { key: 'docs-code-tabs', page: 'quickstart', group: 'Docs widgets', title: 'SDK tabs',
    desc: 'The language picker above a code sample ("Python", "TypeScript", "cURL", ...): a Radix tablist.',
    sel: '[role="tablist"]', find: (p) => p.locator('[role="tablist"]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'docs-code-tab', page: 'quickstart', group: 'Docs widgets', title: 'SDK tab',
    desc: 'One tab in the picker. "selected" is the tab\'s own activation — a local UI toggle that swaps the published snippet.',
    sel: '[role="tab"]', find: (p) => p.locator('[role="tab"]').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'docs-next-card', page: 'quickstart', group: 'Docs widgets', title: 'Nav card',
    desc: 'A filled card link at the foot of a docs page (bg-card, hover:bg-card-hover).',
    sel: 'main a.bg-card, main a[class*="bg-card"]', find: (p) => p.locator('main a[class*="bg-card"]').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'docs-cta', page: 'home', group: 'Docs widgets', title: 'Primary CTA link',
    desc: 'A solid call-to-action in the hero ("Get Started" / "Create API key") — primary bg, primary-foreground text.',
    sel: 'main a (text Get Started|Create API key|View model)', find: async (p) => await domFind(p, /get started|create api key|view model/i, { sel: 'main a', tag: 'cta', minW: 60, minH: 24 }), states: ['default', 'hover', 'focus-visible', 'pressed', 'dark'] },
  { key: 'docs-text-link', page: 'home', group: 'Docs widgets', title: 'Inline feature link',
    desc: 'A small underlined link inside a feature row (decoration-primary/30).',
    sel: 'main a (text Configurable|Learn more|Read more)', find: async (p) => await domFind(p, /configurable|learn more|read more|explore/i, { sel: 'main a', tag: 'tl', minW: 30, minH: 10 }), states: ['default', 'hover'] },
  { key: 'pricing-table', page: 'pricing', group: 'Docs widgets', title: 'Pricing table',
    desc: 'A token-pricing table: header row with a bottom border, dense cells.',
    sel: 'table', find: (p) => p.locator('table').filter({ visible: true }).first(), states: ['default', 'dark'] },
  { key: 'pricing-th', page: 'pricing', group: 'Docs widgets', title: 'Table header cell',
    desc: 'A th in the pricing table.', sel: 'th', find: (p) => p.locator('th').filter({ visible: true }).first(), states: ['default'] },
  { key: 'pricing-td', page: 'pricing', group: 'Docs widgets', title: 'Table cell',
    desc: 'A td in the pricing table.', sel: 'td', find: (p) => p.locator('td').filter({ visible: true }).first(), states: ['default'] },
  { key: 'gbm-panel', page: 'grok-bot', group: 'Docs widgets', title: 'Grok Bot phone panel',
    desc: 'The phone-shaped routine panel (.gbm-panel) on the Grok Bot page — the product\'s illustrative mock.',
    sel: 'section.gbm-panel, [class*="gbm-panel"]', find: (p) => p.locator('.gbm-panel, [class*="gbm-panel"]').filter({ visible: true }).first(), states: ['default', 'dark'] },
];

// The Ctrl+K dialog is measured open: setup() opens it, the specs inside read
// its parts, teardown() closes it.
const SEARCH_SETUP = async (p) => { await p.keyboard.press('Control+k'); await p.waitForTimeout(1600); };
const SEARCH_DOWN = async (p) => { await p.keyboard.press('Escape'); await p.waitForTimeout(500); };
const SEARCH = [
  { key: 'docs-search-input', group: 'Docs search', title: 'Search input',
    desc: 'The command field; "focused" is the field clicked into — nothing is typed.',
    sel: '.docs-search-modal input, [cmdk-input]', find: (p) => p.locator('.docs-search-modal input, [cmdk-input], [role="dialog"] input').filter({ visible: true }).first(), states: ['default', 'focused'] },
  { key: 'docs-search-item', group: 'Docs search', title: 'Suggestion row',
    desc: 'A suggestion row in the open menu ("Ask Grok anything", "Quickstart", ...).',
    sel: '[cmdk-item], [role="option"]', find: (p) => p.locator('[cmdk-item], [role="option"], .docs-search-modal [class*="cursor-pointer"]').filter({ visible: true }).first(), states: ['default', 'hover'] },
  // The dialog spec runs last: its 'dark' state closes the dialog, repaints
  // via the header's own theme button (which the open dialog occludes), then
  // reopens the dialog with Ctrl+K for the dark measurement.
  { key: 'docs-search-dialog', group: 'Docs search', title: 'Search dialog (cmdk)',
    desc: 'The ⌘K command menu: "Ask Grok" plus page suggestions, painted by the page\'s own shortcut.',
    sel: '.docs-search-modal, [cmdk-root]', find: (p) => p.locator('.docs-search-modal, [cmdk-root], [role="dialog"]').filter({ visible: true }).first(), states: ['default',
      { name: 'dark', via: 'the dialog was closed, the header theme button repainted html.dark, and Ctrl+K reopened it',
        fn: async () => {
          await page.keyboard.press('Escape');
          await page.waitForTimeout(500);
          if (!(await setTheme(page, 'dark'))) throw new Error('dark never painted');
          await page.keyboard.press('Control+k');
          await page.waitForTimeout(1400);
        } }] },
];

const MOBILE = [
  { key: 'm-docs-topbar', group: 'Docs chrome (mobile)', title: 'Mobile header',
    desc: 'The fixed bar at 390px: hamburger, wordmark, search and theme icons.', sel: 'header',
    find: (p) => p.locator('header').first(), states: ['default'] },
  { key: 'm-docs-hamburger', group: 'Docs chrome (mobile)', title: '"Open navigation menu" button',
    desc: 'The hamburger that opens the nav sheet.', sel: 'header button[aria-label*="navigation" i], header button[aria-label*="menu" i]',
    find: (p) => p.locator('header button[aria-label*="navigation" i], header button[aria-label*="menu" i]').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'm-docs-drawer', group: 'Docs chrome (mobile)', title: 'Nav sheet (open)',
    desc: 'The opened navigation sheet — a full-screen fixed aside over the page. The "Open navigation menu" press happens in find(): the sheet is only visible once open, so the state itself is a no-op.',
    sel: 'aside.fixed.inset-0', find: async (p) => {
      const ham = p.locator('header button[aria-label*="navigation" i], header button[aria-label*="menu" i]').filter({ visible: true }).first();
      await ham.click({ timeout: 5000 }).catch(() => {});
      await p.waitForTimeout(1300);
      return p.locator('aside[class*="fixed"], aside[class*="inset-0"]').first();
    }, states: [{ name: 'opened', via: 'the "Open navigation menu" button\'s own press', fn: async () => {} }] },
];

const GROUPS = {
  home: { page: 'home', specs: [...CHROME, ...WIDGETS.filter((w) => w.page === 'home')] },
  quickstart: { page: 'quickstart', specs: [...FOOTER, ...PROSE.filter((w) => w.page === 'quickstart'), ...WIDGETS.filter((w) => w.page === 'quickstart')] },
  pricing: { page: 'pricing', specs: WIDGETS.filter((w) => w.page === 'pricing') },
  faq: { page: 'faq', specs: PROSE.filter((w) => w.page === 'faq') },
  grok: { page: 'grok', specs: PROSE.filter((w) => w.page === 'grok') },
  'grok-bot': { page: 'grok-bot', specs: WIDGETS.filter((w) => w.page === 'grok-bot') },
  search: { page: 'home', setup: SEARCH_SETUP, teardown: SEARCH_DOWN, specs: SEARCH },
  mobile: { page: 'home', mobile: true, specs: MOBILE },
};

// ---------- runner ----------

const b = await chromium.launch();
context = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
await patch(context);
const mobCtx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
await patch(mobCtx);

const wanted = process.argv.slice(2);
out._meta.read = new Date().toLocaleDateString('en-CA');
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); docs.x.ai paints html.light by default and html.dark after the header theme button — `dark` states are measured on the painted dark surface';
out._meta.tool = 'tools/capture/public/measure.mjs';
out._meta.sheets ??= {};

for (const [key, g] of Object.entries(GROUPS)) {
  if (wanted.length && !wanted.includes(key)) continue;
  const ctx = g.mobile ? mobCtx : context;
  page = await ctx.newPage();
  page.setDefaultTimeout(8000);
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  const url = BASE + URLS[g.page];
  log('open', key, g.mobile ? '(mobile)' : '', url);
  if (!(await open(page, url, { wait: 7000 }))) {
    // not reached, or a bot check that never cleared: a boundary, never measured as the product
    log('  ! not reached or bot-checked: recorded as a boundary', key);
    await page.close().catch(() => {});
    continue;
  }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  if (g.setup) await g.setup(page).catch((e) => log('  setup failed:', e.message));
  // the readable sheets' transition declarations, for measurements.md
  out._meta.sheets[URLS[g.page]] = await page.evaluate(() => {
    const found = [];
    for (const ss of document.styleSheets) {
      try {
        for (const r of ss.cssRules) {
          if (r.style && r.style.transition && r.style.transition !== 'all 0s') found.push({ transition: r.style.transition.slice(0, 90) });
        }
      } catch { /* cross-origin sheet */ }
    }
    return found.slice(0, 30);
  }).catch(() => []);

  for (const spec of g.specs) {
    const comp = out.components[spec.key] ??= {};
    comp.group = spec.group;
    comp.title = spec.title;
    comp.desc = spec.desc;
    comp.selector = spec.sel;
    comp.page = URLS[g.page];
    comp.url = safeUrl(url);
    comp.run = new Date().toISOString();
    comp.states ??= {};
    let loc;
    // A lookup miss must not erase states a previous run already measured —
    // only a component with no good readings at all counts as missing.
    const hasStates = () => Object.values(comp.states ?? {}).some((s) => s && s.style);
    try { loc = await spec.find(page); } catch (e) {
      log(' ', spec.key, 'find failed:', e.message.split('\n')[0]);
      if (hasStates()) comp.rerunMiss = e.message.split('\n')[0]; else comp.missing = true;
      continue;
    }
    if (!(await loc.count()) || !(await loc.first().isVisible().catch(() => false))) {
      log(' ', spec.key, 'absent');
      if (hasStates()) comp.rerunMiss = 'absent on this run'; else comp.missing = true;
      continue;
    }
    delete comp.missing;
    delete comp.rerunMiss;
    loc = loc.first();
    for (const st of spec.states) {
      const name = typeof st === 'string' ? st : (st.name || 'opened');
      // pressed/dark are cleared in finally so a failed read can never leak
      // the forced state into the next measurement.
      let pressed = null;
      let darkOn = false;
      try {
        await reset();
        let viaText = 'resting state';
        if (st === 'hover') { await hover(loc); viaText = via.hover; }
        else if (st === 'focus-visible') { await kbFocus(loc); viaText = via['focus-visible']; }
        else if (st === 'focused') { await loc.click({ timeout: 3000 }).catch(() => loc.evaluate((el) => el.focus())); await page.waitForTimeout(400); viaText = 'the field clicked into'; }
        else if (st === 'pressed') { pressed = await pressOn(loc); viaText = via.pressed; }
        else if (st === 'dark') { if (!(await setTheme(page, 'dark'))) { log(' ', spec.key, name, 'dark never painted — skipped'); continue; } darkOn = true; viaText = via.dark; }
        else if (st && typeof st === 'object' && st.fn) { await st.fn(loc); viaText = st.via || 'reached by the component\'s own UI toggle'; }
        else if (typeof st === 'function') { await st(loc); viaText = 'reached by the component\'s own UI toggle'; }
        await centre(loc).catch(() => {});
        const v = await styleOf(loc);
        v.via = viaText;
        v.crop = await crop(page, loc, `${spec.key}-${name}`).catch((e) => { log('  crop failed', spec.key, name, e.message.split('\n')[0]); return undefined; });
        v.run = new Date().toISOString();
        comp.states[name] = v;
        log(' ', spec.key, name, 'ok');
      } catch (e) {
        // A failed rerun records the error beside the last good reading, not
        // over it — a good saved state outlives a transient failure.
        const prev = comp.states[name];
        comp.states[name] = (prev && prev.style)
          ? { ...prev, rerunError: e.message.split('\n')[0] }
          : { error: e.message.split('\n')[0] };
        log(' ', spec.key, name, 'FAILED', e.message.split('\n')[0]);
      } finally {
        if (pressed != null) await pressOff(pressed).catch(() => {});
        if (darkOn) await setTheme(page, 'light').catch(() => {});
      }
    }
    save();
  }
  if (g.teardown) await g.teardown(page).catch(() => {});
  await setTheme(page, 'light').catch(() => {});
  await page.close();
}
await b.close();
log('done ->', OUT);
