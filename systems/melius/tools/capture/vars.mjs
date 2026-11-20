// Harvest Maze public stylesheets into raw/css-vars.json.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
//
// maze.co declares a named palette on :root (--color-neutral-*, --color-blue-*,
// --font-phonic, --radius-*, --spacing, --nav-height). auth.maze.co and the
// public report paint Inter and a blue action, mostly as literals. One painted
// theme. Cross-origin sheets are read from the network response, not the CSSOM.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, BASE, APP, DOCS, hideConsent } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });

const pages = [BASE + '/', BASE + '/pricing', APP + '/login', APP + '/signup', DOCS + '/'];
const browser = await chromium.launch({ headless: true });
const bodies = new Map();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const page = await ctx.newPage();
page.on('response', async (r) => {
  const t = r.request().resourceType();
  const u = r.url().split('?')[0];
  if (t !== 'stylesheet' && !/\.css$/.test(u)) return;
  try {
    const text = await r.text();
    if (text && text.includes('{')) bodies.set(u, text);
  } catch { /* gone */ }
});
for (const url of pages) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 }).catch((e) => console.log('skip', url, e.message.split('\n')[0]));
  await page.waitForTimeout(1800);
  await hideConsent(page);
  const inline = await page.evaluate(() => [...document.querySelectorAll('style')].map((s, i) => ['inline-' + location.host + '-' + i, s.textContent || '']));
  for (const [name, text] of inline) if (text && text.length > 40) bodies.set(name + '-' + url, text);
}
const fontsLoaded = await page.evaluate(() => [...document.fonts].map((f) => ({ family: f.family, weight: f.weight, status: f.status }))).catch(() => []);
await ctx.close();

const sheets = [...bodies.entries()];
const probeCtx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const probe = await probeCtx.newPage();
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText : (r.cssText || '').split('{')[0].trim().slice(0, 60);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k && k.startsWith('--') && !k.startsWith('--tw-')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
      }
      if (Object.keys(props).length) rules.push({ file: String(file).slice(0, 80), selector: (r.selectorText || '').slice(0, 120), context: ctx.slice(-2), properties: props });
    }
  };
  for (const [name, text] of sheets) {
    if (!text || text.length > 3_000_000) continue;
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: String(name).slice(0, 80), error: String(e).slice(0, 120) }); continue; }
    walk(ss.cssRules, [], String(name).split('/').pop().slice(0, 40));
  }
  // Resolve every kept name on a probe that carries the sheets.
  const html = '<!doctype html><html><head>' + sheets.map(([, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('') + '</head><body><div id="probe"></div></body></html>';
  return { rules, fonts, errors, html };
}, sheets.map(([name, css]) => [name, css.slice(0, 2_500_000)]));

await probe.setContent('<!doctype html><html><head></head><body><div id="probe"></div></body></html>');
// Inject sheets one at a time so one bad sheet does not drop the rest.
for (const [name, css] of sheets) {
  if (!css || css.length > 2_500_000) continue;
  await probe.addStyleTag({ content: css }).catch((e) => console.log('sheet skip', String(name).slice(0, 60), e.message.split('\n')[0]));
}
const names = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))].sort();
const resolved = await probe.evaluate((names) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const lin = (c) => (c <= 0.0031308 ? 12.92 * c : 1.055 * Math.pow(c, 1 / 2.4) - 0.055);
  const fromOklab = (L, a, b) => {
    const l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3;
    const m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3;
    const s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3;
    return [4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s, -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s]
      .map((v) => Math.round(Math.min(1, Math.max(0, lin(v))) * 255));
  };
  const num = (x) => (String(x).endsWith('%') ? parseFloat(x) / 100 : parseFloat(x));
  const norm = (c) => {
    let m = c.match(/^rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)$/);
    if (m) {
      const rgb = [m[1], m[2], m[3]].map((v) => Math.round(+v));
      const a = m[4] === undefined ? 1 : +m[4];
      return a === 1 ? '#' + rgb.map((v) => v.toString(16).padStart(2, '0')).join('') : `rgba(${rgb.join(', ')}, ${a})`;
    }
    if ((m = c.match(/^oklch\(([-\d.e]+%?) ([-\d.e]+) ([-\d.e]+)(?: \/ ([\d.]+%?))?\)$/))) {
      const h = (+m[3] * Math.PI) / 180;
      const rgb = fromOklab(num(m[1]), +m[2] * Math.cos(h), +m[2] * Math.sin(h));
      const a = m[4] === undefined ? 1 : num(m[4]);
      return a === 1 ? '#' + rgb.map((v) => v.toString(16).padStart(2, '0')).join('') : `rgba(${rgb.join(', ')}, ${a})`;
    }
    return null;
  };
  const el = document.getElementById('probe');
  const box = document.createElement('div');
  box.style.cssText = 'position:absolute;width:100px;height:100px';
  document.body.appendChild(box);
  const out = {};
  for (const name of names) {
    const raw = noUrl(getComputedStyle(el).getPropertyValue(name).trim());
    if (!raw) continue;
    const r = { raw: raw.slice(0, 180) };
    box.style.color = '';
    if (CSS.supports('color', raw)) {
      box.style.color = raw;
      const painted = getComputedStyle(box).color;
      const hex = norm(painted) || norm(raw);
      r.kind = 'color';
      r.value = hex || painted;
    } else if (CSS.supports('width', raw) && !raw.includes('%')) {
      box.style.width = raw;
      r.kind = 'dimension';
      r.value = getComputedStyle(box).width;
    } else if (/font/i.test(name) && CSS.supports('font-family', raw)) {
      r.kind = 'fontFamily';
      r.value = raw;
    } else r.kind = 'other';
    out[name] = r;
  }
  return out;
}, names);
await browser.close();

const out = {
  source: 'www.melius.com, app.melius.com/login, app.melius.com/signup and docs.melius.com, harvested 2026-11-19. One painted theme (light). Marketing colour is the --color-* palette on :root (hex, with a lab() override for four Tailwind defaults).',
  pages,
  fontsLoaded: fontsLoaded.slice(0, 30),
  sheetCount: sheets.length,
  fontFaces: result.fonts.slice(0, 40),
  app: result.rules.slice(0, 500),
  errors: result.errors.slice(0, 12),
  resolved: { light: resolved },
};
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
const colors = Object.values(resolved).filter((v) => v.kind === 'color').length;
console.log('sheets', sheets.length, 'rules', result.rules.length, 'resolved', Object.keys(resolved).length, 'colors', colors, 'errors', result.errors.length);
