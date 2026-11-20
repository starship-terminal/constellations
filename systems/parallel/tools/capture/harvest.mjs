// Reads computed styles and custom properties from Parallel's public pages.
// Writes raw/css-vars.json and raw/components-computed.json.
// Does not click LinkedIn, Google, Apple, or submit any form.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, BASE, closePromo, PROPS } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const RAW = path.join(REF, 'raw');
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(3000);
await closePromo(page);

const sheets = await page.evaluate(() => [...document.styleSheets].map((s, i) => {
  try { return { name: s.href || 'inline-' + i, media: s.media.mediaText || '', css: [...s.cssRules].map((r) => r.cssText).join('\n') }; }
  catch { return { name: s.href || 'sheet-' + i, media: '', css: '', unreadable: true }; }
}));
log('sheets', sheets.length, 'unreadable', sheets.filter((s) => s.unreadable).length, 'bytes', sheets.reduce((n, s) => n + s.css.length, 0));

const rootVars = await page.evaluate(() => {
  const cs = getComputedStyle(document.documentElement);
  const out = {};
  for (let i = 0; i < cs.length; i++) {
    const k = cs[i];
    if (k.startsWith('--')) out[k] = cs.getPropertyValue(k).trim().slice(0, 240);
  }
  return out;
});
log('root custom props', Object.keys(rootVars).length);

const roles = await page.evaluate((props) => {
  function pick(sel) {
    const el = document.querySelector(sel);
    if (!el) return null;
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = { selector: sel, text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 60), rect: { w: Math.round(r.width), h: Math.round(r.height) } };
    for (const k of props) o[k] = cs[k];
    return o;
  }
  const body = getComputedStyle(document.body);
  const html = getComputedStyle(document.documentElement);
  return {
    page: { backgroundColor: body.backgroundColor, color: body.color, fontFamily: body.fontFamily, fontSize: body.fontSize, htmlBg: html.backgroundColor, colorScheme: html.colorScheme },
    h1: pick('h1'),
    h2: pick('h2'),
    button: pick('header button, nav button'),
    link: pick('footer a'),
    input: pick('input'),
  };
}, PROPS);
log('roles', JSON.stringify(roles.page));

await browser.close();

// Probe the harvested sheets the way the browser resolves them.
const probeBrowser = await chromium.launch();
const probe = await probeBrowser.newPage({ viewport: { width: 1440, height: 900 } });
const css = sheets.filter((s) => s.css).map((s) => s.css).join('\n');
await probe.setContent('<!doctype html><html><head><style>' + css.replace(/<\/style/gi, '<\\/style') + '</style></head><body><div id="probe"></div></body></html>', { waitUntil: 'load' });

const names = [...new Set([...css.matchAll(/(--[a-zA-Z0-9_-]+)\s*:/g)].map((m) => m[1]))].filter((n) => !n.startsWith('--tw-')).sort();
log('declared names', names.length);

const resolved = await probe.evaluate((names) => {
  const root = document.documentElement;
  const probeEl = document.getElementById('probe');
  const cs = getComputedStyle(root);
  const out = {};
  const norm = (c) => {
    const m = c.match(/^rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)$/);
    if (!m) return c;
    const rgb = [m[1], m[2], m[3]].map((v) => Math.round(+v));
    const a = m[4] === undefined ? 1 : +m[4];
    if (a === 1) return '#' + rgb.map((v) => v.toString(16).padStart(2, '0')).join('');
    return `rgba(${rgb.join(', ')}, ${Math.round(a * 1000) / 1000})`;
  };
  for (const name of names) {
    const raw = cs.getPropertyValue(name).trim();
    if (!raw) continue;
    const r = { raw: raw.slice(0, 300) };
    probeEl.style.cssText = '';
    if (CSS.supports('color', raw)) {
      probeEl.style.color = raw;
      r.kind = 'color';
      r.value = norm(getComputedStyle(probeEl).color);
    } else if (CSS.supports('width', raw) && !raw.includes('%')) {
      probeEl.style.width = raw;
      r.kind = 'dimension';
      r.value = getComputedStyle(probeEl).width;
    } else if (/^(ease|ease-in|ease-out|ease-in-out|linear|cubic-bezier)/.test(raw)) {
      r.kind = 'easing';
      r.value = raw;
    } else if (/font|sans|serif|mono/i.test(raw) && CSS.supports('font-family', raw)) {
      r.kind = 'fontFamily';
      r.value = raw;
    } else r.kind = 'other';
    out[name] = r;
  }
  return out;
}, names.slice(0, 800));
await probeBrowser.close();

const out = {
  readAt: new Date().toISOString().slice(0, 10),
  source: 'www.useparallel.com home page, stylesheets read through the CSSOM in headless Chromium at 1440x900, then re-parsed in a probe document. Cross-origin sheets that the CSSOM refused are listed under errors.',
  sheets: sheets.map(({ name, media, css, unreadable }) => ({ name: (name || '').slice(0, 180), media, bytes: (css || '').length, unreadable: !!unreadable })),
  rootComputed: rootVars,
  counts: { declared: names.length, resolved: Object.keys(resolved).length },
  resolved: { light: resolved },
  errors: sheets.filter((s) => s.unreadable).map((s) => ({ file: s.name, error: 'cross-origin to the CSSOM' })),
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
fs.writeFileSync(path.join(RAW, 'home-roles.json'), JSON.stringify(roles, null, 1) + '\n');
log('wrote css-vars', Object.keys(resolved).length, 'resolved');
