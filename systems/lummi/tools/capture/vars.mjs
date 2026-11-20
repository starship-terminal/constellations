// Reads every custom property Lummi's public stylesheets declare and writes raw/css-vars.json.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
//
// Lummi is a Next.js site. Styles arrive as /_next/static/css chunks plus inline style tags.
// Bodies are read from network responses and the CSSOM, then re-parsed with CSSStyleSheet.
// Names are resolved on a probe that carries those sheets, once plain and once with class "dark"
// (shadcn's usual switch). The public site does not expose a theme control, so a dark-class pass
// that matches light is recorded as such and is not treated as a live dark theme.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

const browser = await chromium.launch();
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const page = await context.newPage();
const bodies = new Map();
page.on('response', async (r) => {
  const rt = r.request().resourceType();
  if (rt !== 'stylesheet' && !/\.css(\?|$)/.test(r.url())) return;
  try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* gone */ }
});
await page.goto('https://www.lummi.ai/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(4000);
const meta = await page.evaluate(() => ({
  themeColor: [...document.querySelectorAll('meta[name="theme-color"]')].map((m) => ({ content: m.content, media: m.getAttribute('media') })),
  colorScheme: getComputedStyle(document.documentElement).colorScheme,
  htmlClass: document.documentElement.className,
}));
const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
  try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
}).filter(Boolean));
const sheets = [...bodies.entries()].concat(inline);
console.log('sheets', sheets.length, 'bytes', sheets.reduce((n, [, t]) => n + t.length, 0));

const probe = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [], fonts = [], errors = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
          : (r.cssText || '').split('{')[0].trim().slice(0, 120);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      let n = 0;
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k && k.startsWith('--')) { props[k] = noUrl(r.style.getPropertyValue(k).trim()); n++; }
      }
      if (n) rules.push({ file: String(file).slice(0, 180), selector: (r.selectorText || '').slice(0, 200), context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, (r.selectorText || '').slice(0, 80)], file);
    }
  };
  for (const [name, text] of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: String(name).slice(0, 120), error: String(e).slice(0, 200) }); continue; }
    walk(ss.cssRules, [], name);
  }
  return { rules, fonts, errors };
}, sheets);

const shell = (cls) => '<!doctype html><html class="' + cls + '"><head>'
  + sheets.map(([, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe"></div></body></html>';
const want = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))].filter((n) => !n.startsWith('--tw-')).sort();
const resolved = {};
for (const [pass, cls] of [['light', ''], ['dark', 'dark']]) {
  await probe.setContent(shell(cls), { waitUntil: 'load' });
  resolved[pass] = await probe.evaluate((names) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\([^)]*\)/gi, 'url(…)') : v);
    const p = document.createElement('div');
    document.body.appendChild(p);
    const out = {};
    for (const name of names) {
      const raw = noUrl(getComputedStyle(document.documentElement).getPropertyValue(name).trim());
      if (!raw) continue;
      const r = { raw: raw.length > 240 ? raw.slice(0, 240) + '…' : raw };
      p.removeAttribute('style');
      if (CSS.supports('color', raw)) {
        p.style.color = raw;
        r.kind = 'color';
        r.value = getComputedStyle(p).color;
      } else if (CSS.supports('width', raw) && !raw.includes('%')) {
        p.style.width = raw;
        r.kind = 'dimension';
        r.value = getComputedStyle(p).width;
      } else r.kind = 'other';
      out[name] = r;
    }
    p.remove();
    return out;
  }, want);
}
await browser.close();

const same = JSON.stringify(resolved.light) === JSON.stringify(resolved.dark);
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'stylesheet bodies from a signed-out load of https://www.lummi.ai/ (Next.js CSS chunks plus inline style). Resolved on a probe carrying those sheets, plain and with class dark, at 1440x900. The public site has no theme switch.',
  meta,
  darkClassMatchesLight: same,
  sheets: sheets.map(([n, t]) => `${String(n).slice(0, 120)} (${t.length} bytes)`),
  counts: { rules: result.rules.length, fonts: result.fonts.length, names: want.length },
  errors: result.errors,
  rules: result.rules,
  fonts: result.fonts.map((f) => ({ family: f['font-family'], weight: f['font-weight'], style: f['font-style'], file: f.file })),
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('rules', result.rules.length, 'names', want.length, 'fonts', result.fonts.length, 'darkMatchesLight', same);
console.log('theme-color', JSON.stringify(meta));
