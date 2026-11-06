// Shared helpers for capturing an Electron app live over its remote-debugging port.
// Generic: nothing in this file names Cursor. Product parts live in product.mjs.
//
// The app must already be running with the switch, opened by the person capturing:
//   open -a <App> --args --remote-debugging-port=<PORT>
// Env: PLAYWRIGHT (path to playwright's index.mjs), PORT (default 9401).
import { writeFileSync, mkdirSync } from 'node:fs';
import { dirname } from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || `${process.env.HOME}/.design-systems/pw/node_modules/playwright/index.mjs`);
export const PORT = process.env.PORT || '9401';

// Connect and pick the window whose document title matches `title` (a string or RegExp).
// Electron windows of one app share a URL, so the title is what tells them apart.
export async function connect(title) {
  const browser = await pw.chromium.connectOverCDP(`http://127.0.0.1:${PORT}`);
  const pages = browser.contexts().flatMap(c => c.pages());
  let page;
  for (const p of pages) {
    const t = await p.title();
    if (title instanceof RegExp ? title.test(t) : t === title) { page = p; break; }
  }
  if (!page) throw new Error(`no window titled ${title}; open: ${(await Promise.all(pages.map(p => p.title()))).join(', ')}`);
  const cdp = await page.context().newCDPSession(page);
  await cdp.send('DOM.enable'); await cdp.send('CSS.enable');
  // SCHEME=light|dark emulates prefers-color-scheme for as long as this session is attached, for an
  // app whose theme follows it (Orca's System theme does; Cursor's does not). Nothing is saved in the app.
  if (process.env.SCHEME) {
    await cdp.send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-color-scheme', value: process.env.SCHEME }] });
    await page.waitForTimeout(800);
  }
  return { browser, page, cdp, pages };
}

// Disconnect without closing the app (connectOverCDP's close only drops the connection).
export const disconnect = b => b.close().catch(() => {});

// The window at its own device pixels. Playwright's page.screenshot assumes an integer
// pixel ratio and pads the image when the app zooms (Cursor's Agents window runs at 1.68);
// CDP's captureScreenshot returns exactly the backing store.
export async function shoot(cdp, path) {
  mkdirSync(dirname(path), { recursive: true });
  const { data } = await cdp.send('Page.captureScreenshot', { format: 'png' });
  writeFileSync(path, Buffer.from(data, 'base64'));
  return path;
}

export async function viewport(page) {
  return page.evaluate(() => ({ dpr: devicePixelRatio, css: [innerWidth, innerHeight],
    device: [Math.round(innerWidth * devicePixelRatio), Math.round(innerHeight * devicePixelRatio)],
    title: document.title, bodyClass: document.body.className, htmlClass: document.documentElement.className }));
}

// Force pseudo-classes (hover, focus, focus-visible, active) on the first element matching a
// CSS selector, through the DevTools protocol, so no pointer or keyboard moves. Returns an undo.
export async function force(cdp, selector, states) {
  const { root } = await cdp.send('DOM.getDocument', { depth: -1 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector });
  if (!nodeId) throw new Error(`no element matches ${selector}`);
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: states });
  return () => cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {});
}

// Box of an element in device pixels of the screenshot (CSS box x pixel ratio).
export async function box(locator) {
  const b = await locator.boundingBox({ timeout: 3000 }).catch(() => null);
  if (!b) return null;
  const dpr = await locator.page().evaluate(() => devicePixelRatio);
  return [b.x, b.y, b.width, b.height].map(v => Math.round(v * dpr));
}

// Mark an element so the readers can find it again without account text: sets data-cap=<name>.
export async function tag(locator, name) {
  await locator.evaluate((e, n) => e.setAttribute('data-cap', n), name);
  return `[data-cap="${name}"]`;
}
export async function untagAll(page) {
  await page.evaluate(() => document.querySelectorAll('[data-cap]').forEach(e => e.removeAttribute('data-cap')));
}

export const esc = async (page, n = 1) => { for (let i = 0; i < n; i++) { await page.keyboard.press('Escape'); await page.waitForTimeout(250); } };

export function writeJson(path, data) {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, JSON.stringify(data, null, 1) + '\n');
}

// Computed-style properties every measurement reads.
export const PROPS = ['color', 'background-color', 'background-image', 'border-top-color', 'border-top-width', 'border-top-style',
  'border-bottom-color', 'border-bottom-width', 'border-top-left-radius', 'border-bottom-right-radius', 'box-shadow', 'outline-color', 'outline-width', 'outline-style', 'outline-offset',
  'font-family', 'font-size', 'font-weight', 'line-height', 'letter-spacing', 'text-transform', 'text-decoration-line',
  'padding-top', 'padding-right', 'padding-bottom', 'padding-left', 'gap', 'width', 'height', 'opacity',
  'backdrop-filter', 'transition-duration', 'transition-timing-function', 'transition-property', 'cursor', 'z-index'];

// Read PROPS (minus browser defaults that say nothing) from an element handle's computed style.
export async function computed(locator, props = PROPS) {
  return locator.evaluate((e, props) => {
    // A url() in a computed value (a background photo, a cursor) can be a signed or per-account URL:
    // recorded as url(…), only data: and #fragment references kept (the kit's noUrl).
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
    const cs = getComputedStyle(e), r = e.getBoundingClientRect(), out = {};
    for (const p of props) out[p] = noUrl(cs.getPropertyValue(p));
    out._box = [r.x, r.y, r.width, r.height].map(v => Math.round(v * 10) / 10);
    out._tag = e.tagName.toLowerCase(); out._role = e.getAttribute('role');
    return out;
  }, props, { timeout: 3000 });
}
