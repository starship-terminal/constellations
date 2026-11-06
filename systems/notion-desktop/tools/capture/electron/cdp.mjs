// Shared helpers for capturing an Electron app live over its remote-debugging port.
// Generic: nothing in this file names Cursor. Product parts live in product.mjs.
//
// The app must already be running with the switch, opened by the person capturing:
//   open -a <App> --args --remote-debugging-port=<PORT>
// Env: PLAYWRIGHT (path to playwright's index.mjs), PORT (default 9401).
import { writeFileSync, mkdirSync } from 'node:fs';
import { dirname } from 'node:path';
import { createServer } from 'node:http';
import { createRequire } from 'node:module';

const PW = process.env.PLAYWRIGHT || `${process.env.HOME}/.design-systems/pw/node_modules/playwright/index.mjs`;
const pw = await import(PW);
export const PORT = process.env.PORT || '9401';

// Playwright's connectOverCDP attaches to every page target and waits for each to answer. An app
// can hold a page target that never answers (Notion keeps an empty, unloaded WebContents), and then
// the connection times out. So every page target is pinged first; when one stays silent, Playwright
// goes through a local proxy that hides that target from it. Nothing is sent to the silent target.
const { ws: WS, wsServer: WSS } = createRequire(PW)('playwright-core/lib/utilsBundle');
function ping(url, ms = 3000) {
  return new Promise(res => {
    const s = new WS(url); const timer = setTimeout(() => { s.terminate(); res(false); }, ms);
    s.on('open', () => s.send(JSON.stringify({ id: 1, method: 'Runtime.evaluate', params: { expression: '1', returnByValue: true } })));
    s.on('message', m => { if (JSON.parse(m).id === 1) { clearTimeout(timer); s.close(); res(true); } });
    s.on('error', () => { clearTimeout(timer); res(false); });
  });
}
async function endpoint() {
  const base = `http://127.0.0.1:${PORT}`;
  const list = await (await fetch(`${base}/json/list`)).json();
  const silent = new Set();
  for (const t of list.filter(t => t.type === 'page')) if (!(await ping(t.webSocketDebuggerUrl))) silent.add(t.id);
  if (!silent.size) return { url: base };
  const { webSocketDebuggerUrl } = await (await fetch(`${base}/json/version`)).json();
  const http = createServer(), wss = new WSS({ server: http }), hidden = new Set();
  wss.on('connection', client => {
    const up = new WS(webSocketDebuggerUrl, { perMessageDeflate: false, maxPayload: 512 * 1024 * 1024 }), queue = [];
    up.on('open', () => { queue.forEach(m => up.send(m)); queue.length = 0; });
    client.on('message', m => { m = m.toString(); up.readyState === 1 ? up.send(m) : queue.push(m); });
    up.on('message', m => {
      m = m.toString();
      const d = JSON.parse(m), info = d.params && d.params.targetInfo;
      if (d.method === 'Target.attachedToTarget' && silent.has(info.targetId)) { hidden.add(d.params.sessionId); return; }
      if (d.sessionId && hidden.has(d.sessionId)) return;
      if (info && silent.has(info.targetId)) return;
      client.send(m);
    });
    const close = () => { try { up.close(); } catch {} try { client.close(); } catch {} };
    up.on('close', close); client.on('close', close);
    // A refused or broken socket closes both ends, so Playwright's call fails and the capture's own cleanup
    // runs, instead of an unhandled 'error' event ending the process.
    up.on('error', e => { console.error('cdp proxy upstream:', e.message); close(); });
    client.on('error', e => { console.error('cdp proxy client:', e.message); close(); });
  });
  wss.on('error', e => console.error('cdp proxy:', e.message));
  http.on('error', e => console.error('cdp proxy server:', e.message));
  await new Promise(r => http.listen(0, '127.0.0.1', r));
  http.unref();
  return { url: `ws://127.0.0.1:${http.address().port}/devtools/browser/proxy`, http, silent: [...silent] };
}

// Connect and pick the window whose document title matches `title` (a string or RegExp).
// Electron windows of one app usually share a URL, so the title is what tells them apart; when
// they share a title instead (Codex's windows are all "ChatGPT"), pass { url: RegExp }; a function
// (page => boolean, may be async) picks by anything else (Notion's active tab is the visible one).
export async function connect(title) {
  const ep = await endpoint();
  const browser = await pw.chromium.connectOverCDP(ep.url);
  if (ep.http) browser.on('disconnected', () => ep.http.close());
  const pages = browser.contexts().flatMap(c => c.pages());
  let page;
  for (const p of pages) {
    const t = await p.title();
    if (typeof title === 'function' ? await title(p) : title && title.url instanceof RegExp ? title.url.test(p.url()) : title instanceof RegExp ? title.test(t) : t === title) { page = p; break; }
  }
  if (!page) throw new Error(`no window titled ${title}; open: ${(await Promise.all(pages.map(p => p.title()))).join(', ')}`);
  const cdp = await page.context().newCDPSession(page);
  await cdp.send('DOM.enable'); await cdp.send('CSS.enable');
  // Playwright's connectOverCDP emulates prefers-color-scheme: light on the page for as long as it
  // stays attached (found on OpenCode, whose theme follows the media query). COLOR_SCHEME=dark|light
  // sets the scheme this connection emulates instead; unset leaves Playwright's default.
  if (process.env.COLOR_SCHEME) {
    if (!['dark', 'light'].includes(process.env.COLOR_SCHEME)) throw new Error(`COLOR_SCHEME must be dark or light, not ${process.env.COLOR_SCHEME}`);
    await page.emulateMedia({ colorScheme: process.env.COLOR_SCHEME }); await page.waitForTimeout(600);
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

// Some apps draw part of the window in a second page (Notion's tab strip is its own WebContents above
// the tab's page). `above` is { cdp } of that page: its screenshot is stacked on top of the main one
// (Pillow, through PYTHON or python3), so the image is the whole window. Returns the stack's height
// offset in device pixels, which box() adds to every box so crops still line up.
export async function shootStacked(cdp, path, above) {
  await shoot(cdp, path);
  if (!above) return 0;
  const top = path.replace(/\.png$/, '.above.png');
  await shoot(above.cdp, top);
  const { execFileSync } = await import('node:child_process');
  const dy = execFileSync(process.env.PYTHON || 'python3', ['-c', `
import sys
from PIL import Image
a, b = Image.open(sys.argv[1]), Image.open(sys.argv[2])
w = max(a.width, b.width)
out = Image.new(b.mode, (w, a.height + b.height))
out.paste(a.convert(b.mode), (0, 0)); out.paste(b, (0, a.height))
out.save(sys.argv[2]); print(a.height)`, top, path]).toString().trim();
  const { rmSync } = await import('node:fs');
  rmSync(top, { force: true });
  return +dy;
}

// Find the page a WINDOWS entry names among already connected pages (for a stacked page).
export async function find(pages, title) {
  for (const p of pages) {
    const t = await p.title().catch(() => '');
    if (typeof title === 'function' ? await title(p) : title && title.url instanceof RegExp ? title.url.test(p.url()) : title instanceof RegExp ? title.test(t) : t === title) {
      const cdp = await p.context().newCDPSession(p);
      return { page: p, cdp };
    }
  }
  return null;
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
// dy: device pixels stacked above the page in the screenshot (shootStacked), added to y.
export async function box(locator, dy = 0) {
  const b = await locator.boundingBox({ timeout: 3000 }).catch(() => null);
  if (!b) return null;
  const dpr = await locator.page().evaluate(() => devicePixelRatio);
  const r = [b.x, b.y, b.width, b.height].map(v => Math.round(v * dpr));
  r[1] += dy;
  return r;
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
    const cs = getComputedStyle(e), r = e.getBoundingClientRect(), out = {};
    for (const p of props) out[p] = cs.getPropertyValue(p);
    out._box = [r.x, r.y, r.width, r.height].map(v => Math.round(v * 10) / 10);
    out._tag = e.tagName.toLowerCase(); out._role = e.getAttribute('role');
    return out;
  }, props, { timeout: 3000 });
}
