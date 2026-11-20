// Reads every custom property klarna.com's stylesheets declare and writes raw/css-vars.json.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
//
// Klarna's marketing site injects the Klarna UI token sheet as inline <style> blocks
// (emotion / Panda). The light theme is `:root, .klarna-ui-DEFAULT-light`. The dark
// theme is `.klarna-ui-DEFAULT-dark`. Cross-origin link sheets are skipped; their
// bodies are not needed because the token sheet is inline and readable.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, UA, launch, hideConsent } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const ROUTES = ['/us/', '/us/shopping/', '/us/help/', '/international/'];

const { browser } = await launch();
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  userAgent: UA,
  locale: 'en-US',
});
const page = await context.newPage();
const blocks = new Map();
async function harvest(label) {
  const more = await page.evaluate((label) => {
    const out = [];
    for (const [i, s] of [...document.styleSheets].entries()) {
      if (s.href) continue;
      try {
        const css = [...s.cssRules].map((r) => r.cssText).join('\n');
        if (css.includes('--colors-') || css.includes('--font') || css.includes('@font-face') || css.length > 400) {
          out.push([label + '-' + i, css]);
        }
      } catch { /* unreadable */ }
    }
    return out;
  }, label);
  for (const [name, css] of more) {
    const key = css.length + ':' + css.slice(0, 80);
    if (!blocks.has(key)) blocks.set(key, [name, css]);
  }
  console.log(label, 'inline candidates', more.length, 'unique', blocks.size);
}

for (const route of ROUTES) {
  await page.goto(BASE + route, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch((e) => console.log('nav fail', route, e.message));
  await page.waitForTimeout(3000);
  await hideConsent(page);
  await harvest(route.replace(/\//g, '') || 'root');
}

const sheets = [...blocks.values()];
console.log('sheets', sheets.length, 'bytes', sheets.reduce((n, [, c]) => n + c.length, 0));

const probe = await browser.newPage();
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
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + r.name
          : (r.cssText || '').split('{')[0].trim().slice(0, 140);
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
      if (n) rules.push({ file, selector: (r.selectorText || '').slice(0, 220), context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, (r.selectorText || '').slice(0, 120)], file);
    }
  };
  for (const [name, text] of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: name, error: String(e).slice(0, 180) }); continue; }
    walk(ss.cssRules, [], name);
  }
  return { rules, fonts, errors };
}, sheets);

const shell = '<!doctype html><html><head>'
  + sheets.map(([, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root" class="klarna-ui-DEFAULT-light"></div></body></html>';
const want = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => n.startsWith('--colors-') || n.startsWith('--font') || n.startsWith('--spacing') || n.startsWith('--radii') || n.startsWith('--radius') || n.startsWith('--shadow') || n.startsWith('--sizes') || n.startsWith('--borders') || n.startsWith('--durations') || n.startsWith('--easings') || n.startsWith('--line') || n.startsWith('--letter') || n.startsWith('--z') || /^--(space|size|border|text|bg|fg)-/.test(n))
  .sort();
console.log('candidate names', want.length, 'of', new Set(result.rules.flatMap((r) => Object.keys(r.properties))).size);

const resolved = {};
for (const pass of [
  ['light', ''],
  ['dark', 'document.documentElement.className="klarna-ui-DEFAULT-dark"; document.getElementById("probe-root").className="klarna-ui-DEFAULT-dark";'],
]) {
  await probe.setContent(shell, { waitUntil: 'load' });
  resolved[pass[0]] = await probe.evaluate(([names, extra]) => {
    if (extra) (0, eval)(extra);
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const box = document.createElement('div');
    box.className = document.documentElement.className;
    box.style.cssText = 'position:absolute;left:0;top:0;width:1000px;height:1000px;visibility:hidden';
    const p = document.createElement('div');
    box.appendChild(p);
    document.body.appendChild(box);
    const host = document.documentElement;
    const out = {};
    const cs = getComputedStyle(host);
    for (const name of names) {
      const raw = noUrl(cs.getPropertyValue(name).trim());
      if (!raw) continue;
      const r = { raw: raw.length > 240 ? raw.slice(0, 240) + '…' : raw };
      p.removeAttribute('style');
      if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert|transparent)$/.test(raw)) {
        p.style.color = raw;
        r.kind = 'color';
        r.value = getComputedStyle(p).color;
      } else if (!raw.includes('%') && CSS.supports('width', raw) && /px|rem|em/.test(raw)) {
        p.style.width = raw;
        r.kind = 'dimension';
        r.value = getComputedStyle(p).width;
      } else if (/ms$|s$/.test(raw) && CSS.supports('transition-duration', raw)) {
        r.kind = 'duration';
        r.value = raw;
      } else {
        r.kind = 'other';
      }
      out[name] = r;
    }
    box.remove();
    return out;
  }, [want, pass[1]]);
  console.log('resolved', pass[0], Object.keys(resolved[pass[0]]).length);
}

await browser.close();

const binOf = (r) => {
  const sel = r.selector || '';
  if (/onetrust|ot-sdk/.test(sel)) return 'vendor';
  if (/dark/.test(sel) && /klarna-ui/.test(sel)) return 'dark';
  if (/klarna-ui|:root/.test(sel)) return 'theme';
  return 'app';
};
for (const r of result.rules) r.bin = binOf(r);
const names = (bin) => [...new Set(result.rules.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'inline stylesheets harvested from live loads of /us/, /us/shopping/, /us/help/ and /international/ on www.klarna.com; resolved on a probe document in light (:root / .klarna-ui-DEFAULT-light) and dark (.klarna-ui-DEFAULT-dark)',
  sheets: sheets.map(([n, t]) => `${n} (${t.length} bytes)`),
  counts: {
    rules: result.rules.length,
    fonts: result.fonts.length,
    names: { theme: names('theme').length, dark: names('dark').length, app: names('app').length, vendor: names('vendor').length },
  },
  errors: result.errors,
  theme: result.rules.filter((r) => r.bin === 'theme'),
  dark: result.rules.filter((r) => r.bin === 'dark'),
  app: result.rules.filter((r) => r.bin === 'app').slice(0, 80),
  vendor: result.rules.filter((r) => r.bin === 'vendor').slice(0, 20),
  fonts: result.fonts,
  resolved,
  nameIndex: {
    theme: names('theme'),
    dark: names('dark'),
  },
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('wrote', path.join(REF, 'raw', 'css-vars.json'), 'rules', result.rules.length, 'fonts', result.fonts.length);
