// Measures httpie.io's signed-out components on its public pages, in every
// state that can be reached without signing in or submitting anything —
// the marketing surface plus /app, the HTTPie-for-Web client that runs
// signed out in its "Incognito space".
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home desktop-page cli ai docs docs-desktop docs-cli jobs blog
// blog-post download about terms privacy notfound app app-tabs app-env
// mobile. Writes raw/components-computed.json (merged, so a
// subset of pages can be re-run) and one crop per component and state into
// components/crops/. raw/measurements.md is then built from the JSON by
// build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 500ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or button can fire
//   light          the same element after the footer's own ThemeToggle
//                  radios (LIGHT MODE / AUTO / DARK MODE) repaint html.light —
//                  httpie.io boots html.dark, so dark is the resting read
//                  and light the switched state (setTheme in lib.mjs)
//   opened         a resting state reached by the component's own toggle:
//                  the /app method menu and the Incognito-space side menu,
//                  the Environments selector, a request panel tab
//   focused        a field clicked into — nothing is typed
// Nothing else is typed, sent, bought or signed into. Send is never
// pressed on /app — issuing a request is a network side effect, so the
// response surface is measured only at its resting "Not sent" state and
// the sent surface is a documented boundary. The newsletter forms are
// measured at rest and focused only — never submitted.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, BASE, M, open, closePromo, setTheme, paintedTheme, styleOf, crop, centre, domFind, patch, UA, UA_MOBILE, RAW, openApp, dismissAppPromo } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: '/',
  'desktop-page': '/desktop',
  cli: '/cli',
  ai: '/ai',
  docs: '/docs',
  'docs-desktop': '/docs/desktop',
  'docs-cli': '/docs/cli',
  jobs: '/jobs',
  blog: '/blog',
  'blog-post': '/blog/changelog-0027',
  download: '/download',
  about: '/about',
  terms: '/terms',
  privacy: '/privacy',
  notfound: '/pricing',
  app: '/app',
};
const urlOf = (key) => BASE + (URLS[key] || '/');
const pathOf = (key) => URLS[key] || '/';
const isApp = (key) => URLS[key] === '/app';

let page, cdp, context, current;

// ---------- state drivers ----------

async function reset() {
  // open() leaves the tab on about:blank when a reload was blocked; every
  // state after that fails here, so the saved readings are kept
  if (page.url() === 'about:blank') throw new Error('the page was lost to a blocked reload; saved readings kept');
  await page.keyboard.press('Escape').catch(() => {});
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
  // The attempt is only evidence when focus really came back to the element
  // and paints the :focus-visible ring — anything else is a resting reading,
  // recorded under the "focus failed" via rather than claimed as a state.
  return await loc.evaluate((el) => {
    const ae = document.activeElement;
    const held = ae === el || el.contains(ae);
    let ring = false;
    try { ring = Boolean((ae && ae.matches(':focus-visible')) || el.matches(':focus-visible')); } catch { /* unpierceable */ }
    return { held, ring };
  }).catch(() => ({ held: false, ring: false }));
}

// Pick one element out of a selector's matches inside the page — marks the
// winner with data-m-mark="<tag>" and returns a locator for it. score(el, r,
// cs) returns a number, lowest wins; return Infinity to skip a match.
async function pick(p, sel, score, tag = 'pk') {
  const ok = await p.evaluate(([s, t, src]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const fn = new Function('el', 'r', 'cs', `return (${src})(el, r, cs)`);
    let best = null, bestV = Infinity;
    for (const el of document.querySelectorAll(s)) {
      const r = el.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      const cs = getComputedStyle(el);
      if (cs.visibility === 'hidden' || cs.opacity === '0') continue;
      const v = fn(el, r, cs);
      if (v < bestV) { bestV = v; best = el; }
    }
    if (!best) return false;
    best.setAttribute('data-m-mark', t);
    return true;
  }, [sel, tag, score.toString()]);
  return ok ? p.locator(`[data-m-mark="${tag}"]`) : p.locator('[data-m-mark="__none__"]');
}

// CSS.forcePseudoState through CDP: the press never happens, so no link can
// navigate and no button can fire.
async function pressOn(loc) {
  // Force :active:hover on the component element itself, never the topmost
  // node at its centre (a text span or an svg), so the component's own
  // :active rule applies (2026-11 audit, finding 12-6; not run since).
  await cdp.send('DOM.getDocument').catch(() => {});
  await loc.evaluate((el) => el.setAttribute('data-press-target', '1'));
  try {
    const { result } = await cdp.send('Runtime.evaluate', { expression: `document.querySelector('[data-press-target]')`, returnByValue: false });
    // an unresolved target throws, so the state records an error instead of
    // a resting reading labelled pressed
    if (!result || !result.objectId) throw new Error('press target not resolvable');
    const { nodeId } = await cdp.send('DOM.requestNode', { objectId: result.objectId });
    if (!nodeId) throw new Error('press target has no DOM node');
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['active', 'hover'] });
    await page.waitForTimeout(400);
    return nodeId;
  } finally {
    await loc.evaluate((el) => el.removeAttribute('data-press-target')).catch(() => {});
  }
}
const pressOff = (id) => id == null ? null : cdp.send('CSS.forcePseudoState', { nodeId: id, forcedPseudoClasses: [] }).catch(() => {});

// ---------- the component specs ----------
// find: page -> Locator. states: name -> 'hover' | 'focus-visible' |
// 'pressed' | 'light' | 'focused' | (loc, page) => Promise<void>.
const via = { 'hover': 'mouse hover over the element', 'focus-visible': 'keyboard focus (Shift+Tab, Tab)', 'pressed': 'CDP CSS.forcePseudoState(:active:hover) — no real press', 'light': 'same element after the footer\'s own LIGHT MODE radio repaints html.light (the site boots html.dark, so light is the switched state)' };

const BTN = 'button[class*="Button_button"], a[class*="Button_button"]';

const CHROME = [
  { key: 'site-nav', group: 'Site chrome', title: 'Site navigation bar',
    desc: 'The top nav (Navigation_navigation): wordmark, Desktop / Terminal / AI / Docs / Jobs / Blog links and the "Go to App →" primary button.',
    sel: 'nav[class*="Navigation_navigation"]', find: (p) => p.locator('nav').filter({ visible: true }).first(), states: ['default', 'light'] },
  { key: 'nav-link', group: 'Site chrome', title: 'Nav link',
    desc: 'A primary nav link ("Terminal").',
    sel: 'nav a', find: async (p) => await domFind(p, /^terminal$/i, { sel: 'nav a', tag: 'nl', minW: 40 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'nav-cta', group: 'Site chrome', title: '"Go to App →" button',
    desc: 'The solid primary button in the nav — links to /app, measured never followed.',
    sel: `${BTN} (text Go to App)`, find: async (p) => await domFind(p, /go to app/i, { sel: BTN, tag: 'cta', minW: 80 }), states: ['default', 'hover', 'focus-visible', 'pressed', 'light'] },
  { key: 'site-footer', group: 'Site chrome', title: 'Site footer',
    desc: 'The page footer (Footer_footer): link columns, the social icons, and the LIGHT MODE / AUTO / DARK MODE theme control.',
    sel: 'footer[class*="Footer_footer"]', find: (p) => p.locator('[class*="Footer_footer"], footer').filter({ visible: true }).last(), states: ['default'] },
  { key: 'theme-toggle', group: 'Site chrome', title: 'Theme toggle (LIGHT / AUTO / DARK)',
    desc: 'The footer\'s three-segment ThemeToggle radio stack — the product\'s real theme control. "light" is its own LIGHT MODE press, restored to DARK after.',
    sel: '[class*="ThemeToggle_wrapper"]', find: async (p) => await pick(p, '[class*="ThemeToggle_wrapper"]', (el, r) => r.width > 30 ? r.y : Infinity, 'tt'), states: ['default', 'light'] },
  { key: 'social-button', group: 'Site chrome', title: 'Social button',
    desc: 'A footer social action ("Discord") — a Button_secondary with an icon.',
    sel: `${BTN} (text Discord)`, find: async (p) => await domFind(p, /^discord$/i, { sel: BTN, tag: 'dc', minW: 60 }), states: ['default', 'hover'] },
];

const BUTTONS = [
  { key: 'button-secondary', group: 'Buttons and links', title: 'Secondary button',
    desc: 'An outlined action ("Read blog post" on the changelog banner).',
    sel: `${BTN} (text Read blog post)`, find: async (p) => await domFind(p, /read blog post/i, { sel: BTN, tag: 'sec', minW: 80 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'button-counter', group: 'Buttons and links', title: 'Counter button ("Star on GitHub")',
    desc: 'The GitHub star button carrying its live count — Button_counter.',
    sel: `${BTN} (text Star on GitHub)`, find: async (p) => await domFind(p, /star on github/i, { sel: BTN, tag: 'gh', minW: 80 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'button-share', group: 'Buttons and links', title: 'Share button',
    desc: '"Share on Twitter" in the testimonial wall footer — Button_share.',
    sel: `${BTN} (text Share on Twitter)`, find: async (p) => await domFind(p, /share on twitter/i, { sel: BTN, tag: 'sh', minW: 80 }), states: ['default', 'hover'] },
  { key: 'text-link', group: 'Buttons and links', title: 'Text link',
    desc: 'A Link_link in page content.',
    sel: 'a[class*="Link_link"]', find: (p) => p.locator('a[class*="Link_link"]').filter({ visible: true }).first(), states: ['default', 'hover'] },
];

const HOME = [
  { key: 'hero-headline', group: 'Home', title: 'Hero headline',
    desc: 'The home hero h1 "FLOW THROUGH APIs" — Pie Headline (FK Screamer).',
    sel: 'h1', find: (p) => p.locator('h1').first(), states: ['default', 'light'] },
  { key: 'testimonial-card', group: 'Home', title: 'Testimonial card',
    desc: 'A tweet card in the community wall (TestimonialCard_tweet): avatar, name, handle, body, timestamp.',
    sel: '[class*="TestimonialCard_tweet"]', find: (p) => p.locator('[class*="TestimonialCard"]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'newsletter-input', group: 'Home', title: 'Newsletter email input',
    desc: 'The "Enter email address" field of a NewsletterForm. "focused" is the field clicked into — nothing is typed, the form is never submitted.',
    sel: 'input[type="email"]', find: (p) => p.locator('input[type="email"]').filter({ visible: true }).first(), states: ['default', 'focused', 'light'] },
  { key: 'newsletter-button', group: 'Home', title: 'Newsletter submit button',
    desc: 'The form\'s arrow submit — measured, never pressed.',
    sel: 'form button', find: (p) => p.locator('form button').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'early-access-badge', group: 'Home', title: '"Public beta" badge',
    desc: 'The β Public beta pill on the hero (EarlyAccessBadge).',
    sel: '[class*="EarlyAccessBadge"]', find: (p) => p.locator('[class*="EarlyAccessBadge_badge"], [class*="EarlyAccessBadge_pill"]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'section-heading', group: 'Home', title: 'Section heading',
    desc: 'A home section heading (the testimonial wall\'s h2).',
    sel: 'main h2', find: (p) => p.locator('h2').filter({ visible: true }).first(), states: ['default'] },
];

const CLI = [
  { key: 'cli-install-select', group: 'Terminal page', title: 'Install tool selector',
    desc: 'A package-manager pill in the CLI install picker (InstallationSelect_tool: apt / brew / choco…).',
    sel: '[class*="InstallationSelect_tool"]', find: (p) => p.locator('[class*="InstallationSelect_tool"]').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'cli-code-block', group: 'Terminal page', title: 'Terminal/code block',
    desc: 'A dark code panel with an install command and its copy button.',
    sel: 'pre, [class*="code" i]', find: async (p) => await pick(p, 'pre, [class*="Terminal_"], [class*="CodeBlock"]', (el, r) => r.width > 200 && r.height > 30 ? el.querySelectorAll('*').length : Infinity, 'cb'), states: ['default', 'light'] },
  { key: 'copy-button', group: 'Terminal page', title: 'Copy button',
    desc: 'The CopyButton beside an install command — pressed only with forcePseudoState.',
    sel: '[class*="CopyButton_button"], button[aria-label*="copy" i]', find: (p) => p.locator('[class*="CopyButton_button"], button[aria-label*="copy" i]').filter({ visible: true }).first(), states: ['default', 'hover', 'pressed'] },
];

const BLOG = [
  { key: 'post-card', group: 'Blog', title: 'Post preview card',
    desc: 'A changelog post row on the blog index (PostPreview_post): title, excerpt, meta.',
    sel: '[class*="PostPreview_post"], article, li', find: async (p) => await pick(p, '[class*="PostPreview"], main article, main li', (el, r) => r.height > 40 ? -r.width : Infinity, 'pc'), states: ['default', 'light'] },
  { key: 'post-title-link', group: 'Blog', title: 'Post title link',
    desc: 'The post\'s title inside an index card.',
    sel: '[class*="PostPreview"] a, main a', find: (p) => p.locator('main a, [class*="PostPreview"] a').filter({ visible: true }).filter({ hasText: /\w{6}/ }).first(), states: ['default', 'hover'] },
];

const PROSE = [
  { key: 'prose-h1', group: 'Prose', title: 'Article title (h1)',
    desc: 'The changelog post title.', sel: 'main h1', find: (p) => p.locator('h1').first(), states: ['default', 'light'] },
  { key: 'prose-p', group: 'Prose', title: 'Body paragraph',
    desc: 'A paragraph of article prose.', sel: 'main p (sentence)', find: (p) => p.locator('main p, p').filter({ visible: true }).filter({ hasText: /\S+(\s+\S+){7,}/ }).first(), states: ['default'] },
  { key: 'prose-link', group: 'Prose', title: 'Prose link',
    desc: 'A body-text link inside the article.', sel: 'main p a', find: (p) => p.locator('main :is(p,li) a, p a').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'prose-code', group: 'Prose', title: 'Inline code',
    desc: 'An inline code span in prose.', sel: 'main p code', find: (p) => p.locator('main p code, p code').filter({ visible: true }).first(), states: ['default'] },
  { key: 'prose-pre', group: 'Prose', title: 'Code block',
    desc: 'A fenced code block in the article (syntax-tinted).', sel: 'main pre', find: (p) => p.locator('main pre, pre').filter({ visible: true }).first(), states: ['default', 'light'] },
];

const DOCS = [
  { key: 'docs-toc', group: 'Docs', title: 'Docs table of contents',
    desc: 'The right-rail "On this page" TOC aside on a docs page.',
    sel: 'aside[class*="DocsPage_tableOfContents"]', find: (p) => p.locator('aside').filter({ visible: true }).first(), states: ['default', 'light'] },
  { key: 'docs-side-link', group: 'Docs', title: 'Docs nav section link',
    desc: 'A section link in the docs left nav ("Request method").',
    sel: 'main a, [class*="Docs"] a', find: async (p) => await domFind(p, /request method|defining requests/i, { sel: 'a', tag: 'dl', minW: 60 }), states: ['default', 'hover'] },
  { key: 'docs-code-block', group: 'Docs', title: 'Docs code block',
    desc: 'A fenced code block inside the docs article pane — the surface the code-* syntax palette paints (the captured changelog post carries no fenced block, so this is the package\'s syntax-block evidence).',
    sel: 'pre, [class*="code" i] pre', find: (p) => p.locator('pre').filter({ visible: true }).first(), states: ['default', 'light'] },
  { key: 'docs-inline-code', group: 'Docs', title: 'Docs inline code',
    desc: 'An inline code span inside the docs article pane.',
    sel: 'code', find: (p) => p.locator('main code, article code, code').filter({ visible: true }).first(), states: ['default'] },
];

// ---- /app, the signed-out HTTPie-for-Web client ----
const APP = [
  { key: 'app-sidebar', group: 'App shell', title: 'App sidebar',
    desc: 'The left rail (Layout_sidebar): space switcher, Collection/Drafts/Environments panel.',
    sel: 'aside[class*="Layout_sidebar"]', find: (p) => p.locator('aside').filter({ visible: true }).first(), states: ['default', 'light'] },
  { key: 'app-drafts-tab', group: 'App shell', title: '"Drafts" shelf header',
    desc: 'The Drafts collection header in the sidebar panel — the unsaved-requests shelf.',
    sel: 'button (text Drafts)', find: async (p) => await domFind(p, /^drafts$/i, { sel: 'button, [role="tab"]', tag: 'dt', minW: 40 }), states: ['default', 'hover'] },
  { key: 'app-drafts-empty', group: 'App shell', title: 'Drafts empty state',
    desc: 'The InfoBlock inside the Drafts shelf: "Drafts are your unsaved requests. Organize the ones you want to keep in a collection" — the signed-out draft list is empty.',
    sel: '[class*="InfoBlock_container"]', find: (p) => p.locator('[class*="InfoBlock"]').filter({ hasText: /unsaved requests/i }).filter({ visible: true }).first(), states: ['default'] },
  { key: 'app-request-tab', group: 'Request builder', title: 'Request tab card',
    desc: 'The "GET untitled" draft tab (TabCard_tab, Tab_isActive) in the tab strip.',
    sel: '[class*="TabCard_tab"]', find: (p) => p.locator('[class*="TabCard_tab"]').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'app-method-button', group: 'Request builder', title: 'Method select (GET)',
    desc: 'The method dropdown button on the request line. "opened" is its own press painting the GET/HEAD/POST/… menu — closed with Escape.',
    sel: 'button (text GET)', find: (p) => p.locator('button').filter({ hasText: /^GET$/ }).filter({ visible: true }).first(), states: ['default', 'hover',
      { name: 'opened', via: 'the method button\'s own press (GET/HEAD/POST/PUT/PATCH/DELETE/OPTIONS/Custom menu open; Escape restores)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(1100);
        const m = page.locator('ul, [role="menu"], [role="listbox"]').filter({ hasText: /HEAD/ }).filter({ visible: true }).last();
        return (await m.count()) ? m : null;
      } },
    ] },
  { key: 'app-url-field', group: 'Request builder', title: 'URL field',
    desc: 'The request URL editor (UrlBar, a CodeMirror single-line field) holding the prefilled httpie.io/hello.',
    sel: '[class*="UrlBar_urlTextareaContainer"]', find: (p) => p.locator('[class*="UrlBar_urlTextareaContainer"]').filter({ visible: true }).first(), states: ['default', 'focused'] },
  { key: 'app-send-button', group: 'Request builder', title: '"Send" button',
    desc: 'The request\'s primary action — measured at rest and with forcePseudoState only; a real press would issue a network request, so it is never fired.',
    sel: 'button (text Send)', find: (p) => p.locator('button').filter({ hasText: /^send$/i }).filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'app-panel-tabs', group: 'Request builder', title: 'Request panel tablist',
    desc: 'The Params / Headers / Auth / Body tablist (PanelTabs) above the request editor.',
    sel: '[class*="PanelTabs_container"]', find: (p) => p.locator('[class*="PanelTabs"]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'app-panel-tab', group: 'Request builder', title: 'Request panel tab',
    desc: 'One request panel tab ("Headers"). "selected" is its own activation — a local UI toggle.',
    sel: 'button[class*="PanelTabButton"]', find: (p) => p.locator('button[class*="PanelTabButton"]').filter({ hasText: /^headers$/i }).filter({ visible: true }).first(), states: ['default', 'hover',
      { name: 'selected', via: 'the tab\'s own activation', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(800);
      } },
    ] },
  { key: 'app-param-checkbox', group: 'Request builder', title: 'Param row checkbox',
    desc: 'The enable checkbox on a params row — the painted box is Checkbox_container; the real input is a hidden 1px control.',
    sel: '[class*="Checkbox_container"]', find: (p) => p.locator('[class*="Checkbox_container"]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'app-response-empty', group: 'Request builder', title: 'Response empty state',
    desc: 'The response panel before any send ("Not sent" — the send surface is never fired, so this resting panel is the honest evidence).',
    sel: '[class*="PanelState_container"]', find: (p) => p.locator('[class*="PanelState_container"]').filter({ hasText: /not sent/i }).filter({ visible: true }).first(), states: ['default'] },
  // These two opened states displace the request surface (the space menu
  // dismisses with Escape, which can close the draft tab; the environments
  // manager covers the editor) — they run last so nothing they disturb is
  // measured afterwards.
  { key: 'app-space-button', group: 'App shell', title: '"Incognito space" button',
    desc: 'The space switcher button. "opened" is its own press opening the current space\'s tab (variables/settings) in the strip — no dropdown menu paints for the unsigned product.',
    sel: 'button (text Incognito space)', find: async (p) => await domFind(p, /incognito space/i, { sel: 'button, [role="button"], [class*="button" i]', tag: 'is', minW: 60 }), states: ['default', 'hover',
      { name: 'opened', via: 'the "Incognito space" switcher\'s own press (the current space\'s tab — variables/settings — opens in the strip)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(1200);
        const m = page.locator('main, [class*="Layout_content"]').filter({ visible: true }).last();
        return (await m.count()) ? m : null;
      } },
    ] },
  { key: 'app-env-button', group: 'App shell', title: '"Environments" selector',
    desc: 'The Environments button in the tab bar — opens the environments manager panel.',
    sel: 'button[class*="Tabs_environmentSelector"], button (text Environments)', find: (p) => p.locator('button[class*="environmentSelector" i], button').filter({ hasText: /^environments$/i }).filter({ visible: true }).first(), states: ['default', 'hover',
      { name: 'opened', via: 'the "Environments" button\'s own press (the manager panel open; Collection pressed to restore)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(1200);
        const panel = page.locator('[class*="Environment"]').filter({ visible: true }).last();
        return (await panel.count()) ? panel : null;
      } },
    ] },
];

const APP_TABS = [
  { key: 'app-auth-tab', group: 'Request builder', title: 'Auth panel (opened)',
    desc: 'The Auth tab\'s panel: the "No authentication" select with None / Basic auth / Bearer token / API key options. The tab\'s own press opens it.',
    sel: 'button[class*="PanelTabButton"] (Auth) -> panel', find: async (p) => {
      const t = p.locator('button[class*="PanelTabButton"]').filter({ hasText: /^auth$/i }).first();
      await t.click({ timeout: 4000 }).catch(() => {});
      await p.waitForTimeout(900);
      return p.locator('main, [class*="Panel_"], [class*="panel" i]').filter({ hasText: /authentication|bearer|basic auth/i }).filter({ visible: true }).last();
    }, states: [{ name: 'opened', via: 'the Auth panel tab\'s own activation' }] },
  { key: 'app-body-tab', group: 'Request builder', title: 'Body panel (opened)',
    desc: 'The Body tab\'s panel: the body-type select (None / Text / Form / File / GraphQL).',
    sel: 'button[class*="PanelTabButton"] (Body) -> panel', find: async (p) => {
      const t = p.locator('button[class*="PanelTabButton"]').filter({ hasText: /^body$/i }).first();
      await t.click({ timeout: 4000 }).catch(() => {});
      await p.waitForTimeout(900);
      return p.locator('main, [class*="Panel_"], [class*="panel" i]').filter({ hasText: /no body|graphql/i }).filter({ visible: true }).last();
    }, states: [{ name: 'opened', via: 'the Body panel tab\'s own activation' }] },
  { key: 'app-auth-select', group: 'Request builder', title: 'Auth type select',
    desc: 'The "None" auth-type control inside the opened Auth panel — measured, its menu never opened.',
    sel: 'select or button (auth type)', find: async (p) => {
      const t = p.locator('button[class*="PanelTabButton"]').filter({ hasText: /^auth$/i }).first();
      await t.click({ timeout: 4000 }).catch(() => {});
      await p.waitForTimeout(900);
      return p.locator('select, [role="combobox"], button').filter({ hasText: /no authentication|^none$/i }).filter({ visible: true }).first();
    }, states: ['default', 'hover'] },
];

const APP_ENV = [
  { key: 'app-env-panel', group: 'Environments', title: 'Environments manager',
    desc: 'The environments manager (Variables / Settings / Defaults tabs, "Create environment"), opened by the Environments selector\'s own press.',
    sel: '[class*="SpaceTab_panel"], [class*="PanelContainer_container"]', find: async (p) => {
      const env = p.locator('button[class*="environmentSelector" i], button').filter({ hasText: /^environments$/i }).filter({ visible: true }).first();
      await env.click({ timeout: 4000 }).catch(() => {});
      await p.waitForTimeout(1200);
      // The manager paints as the tab strip's form panel (SpaceTab_panel)
      // holding the Variables table — never the whole 1440×900 layout.
      return p.locator('[class*="PanelContainer_container"]').filter({ hasText: /create environment|variables/i }).filter({ visible: true }).first();
    }, states: [{ name: 'opened', via: 'the Environments selector\'s own press' }, 'light'] },
  { key: 'app-env-create', group: 'Environments', title: '"Create environment" button',
    desc: 'The environments manager\'s primary action — measured, never pressed.',
    sel: 'button (text Create environment)', find: async (p) => await domFind(p, /create environment/i, { sel: 'button', tag: 'ce', minW: 80 }), states: ['default', 'hover'] },
];

const MOBILE = [
  { key: 'm-nav', group: 'Site chrome (mobile)', title: 'Mobile nav',
    desc: 'The nav at 390px (links wrap; no hamburger).', sel: 'nav',
    find: (p) => p.locator('nav').first(), states: ['default'] },
];

const GROUPS = {
  home: { page: 'home', specs: [...CHROME, ...BUTTONS, ...HOME] },
  cli: { page: 'cli', specs: CLI },
  blog: { page: 'blog', specs: BLOG },
  'blog-post': { page: 'blog-post', specs: PROSE },
  'docs-desktop': { page: 'docs-desktop', specs: DOCS },
  app: { page: 'app', app: true, specs: APP },
  'app-tabs': { page: 'app', app: true, specs: APP_TABS },
  'app-env': { page: 'app', app: true, specs: APP_ENV },
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
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); httpie.io boots html.dark — the painted default — and the footer\'s own LIGHT MODE / AUTO / DARK MODE radios repaint html.light (localStorage.theme), so `light` states are measured on the painted light surface; /app reads the same persisted choice';
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
  const url = urlOf(g.page);
  log('open', key, g.mobile ? '(mobile)' : '', url);
  if (g.app) {
    if (!(await openApp(page, { wait: 9000 }))) { log('  group skipped: the page never loaded'); await page.close().catch(() => {}); continue; }
    // The request surface mounts asynchronously after the shell: poll for
    // the method button so the first specs don't read a half-built app.
    for (let i = 0; i < 15; i++) {
      if (await page.locator('button').filter({ hasText: /^GET$/ }).count()) break;
      await page.waitForTimeout(1000);
    }
    await dismissAppPromo(page);
  }
  else if (!(await open(page, url, { wait: 7000 }))) { log('  group skipped: the page never loaded'); await page.close().catch(() => {}); continue; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  // the readable sheets' transition declarations, for measurements.md
  out._meta.sheets[pathOf(g.page)] = await page.evaluate(() => {
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
    comp.page = pathOf(g.page);
    comp.url = safeUrl(url);
    comp.run = new Date().toISOString();
    comp.states ??= {};
    // An Escape (menu dismiss, reset) can close the /app draft request
    // tab, and a left-open environments manager covers the request editor
    // — restore the request surface before each spec so editor components
    // find their elements.
    if (g.app) {
      const requestBack = async () => !!(await page.locator('button').filter({ hasText: /^GET$/ }).count());
      if (!(await requestBack())) {
        // The environments manager and other panels are tabs in the strip —
        // return to the request tab card. The sidebar's "+ Collection" is an
        // ADD button (it opens the Create-collection dialog), never the way back.
        const card = page.locator('[class*="TabCard_tab"]').filter({ hasText: /untitled|GET/i }).first();
        if (await card.count()) { await card.click({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(800); }
      }
      if (!(await requestBack())) {
        // The draft tab is gone: a "+" in the strip opens a fresh draft.
        const add = page.locator('[class*="Tabs_addButton"], button[aria-label*="new" i]').first();
        if (await add.count()) { await add.click({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(900); }
      }
      if (!(await requestBack())) {
        const dr = page.locator('button').filter({ hasText: /^drafts$/i }).first();
        if (await dr.count()) { await dr.click({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(800); }
      }
    }
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
      // An Escape can close the /app draft request tab; if the shell lost
      // it, reopen it before the next spec's find.
      if (g.app) {
        const alive = await page.locator('button').filter({ hasText: /^GET$/ }).count();
        if (!alive) {
          const card = page.locator('[class*="TabCard_tab"]').first();
          if (await card.count()) await card.click({ timeout: 4000 }).catch(() => {});
          await page.waitForTimeout(800);
        }
      }
      continue;
    }
    delete comp.missing;
    delete comp.rerunMiss;
    loc = loc.first();
    for (const st of spec.states) {
      const name = typeof st === 'string' ? st : (st.name || 'opened');
      // pressed/light are cleared in finally so a failed read can never leak
      // the forced state into the next measurement.
      let pressed = null;
      let lightOn = false;
      try {
        await reset();
        let viaText = 'resting state';
        let readLoc = loc;
        if (st === 'hover') { await hover(readLoc); viaText = via.hover; }
        else if (st === 'focus-visible') { const f = await kbFocus(readLoc); viaText = f && (f.held || f.ring) ? via['focus-visible'] : 'focus failed'; }
        else if (st === 'focused') { await readLoc.click({ timeout: 3000 }).catch(() => readLoc.evaluate((el) => el.focus())); await page.waitForTimeout(400); viaText = 'the field clicked into'; }
        else if (st === 'pressed') { pressed = await pressOn(readLoc); viaText = via.pressed; }
        else if (st === 'light') { if (!(await setTheme(page, 'light'))) { log(' ', spec.key, name, 'light never painted — skipped'); continue; } lightOn = true; if (g.app) await dismissAppPromo(page); viaText = via.light; }
        else if (st && typeof st === 'object' && st.fn) { const alt = await st.fn(readLoc); if (alt && typeof alt.count === 'function' && await alt.count()) readLoc = alt; viaText = st.via || 'reached by the component\'s own UI toggle'; }
        else if (typeof st === 'function') { await st(readLoc); viaText = 'reached by the component\'s own UI toggle'; }
        await centre(readLoc).catch(() => {});
        const v = await styleOf(readLoc);
        v.via = viaText;
        v.crop = await crop(page, readLoc, `${spec.key}-${name}`).catch((e) => { log('  crop failed', spec.key, name, e.message.split('\n')[0]); return undefined; });
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
        if (lightOn) {
          let back = await setTheme(page, 'dark').catch(() => false);
          if (!back) back = await setTheme(page, 'dark').catch(() => false);
          if (!back) {
            // A failed reset must never leak light paint into the next
            // default reading: reload, which restores the html.dark boot,
            // and re-find the element so later states measure the live page.
            log(' ', spec.key, 'dark reset failed — reloading to the dark boot');
            if (g.app) await openApp(page, { wait: 9000 }).catch(() => {});
            else await open(page, url, { wait: 7000 }).catch(() => {});
            await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
            const refound = await spec.find(page).catch(() => null);
            if (refound && await refound.count()) loc = refound.first();
          } else if (g.app) await dismissAppPromo(page);
        }
      }
    }
    save();
  }
  await setTheme(page, 'dark').catch(() => {});
  await page.close();
}
await b.close();
log('done ->', OUT);
