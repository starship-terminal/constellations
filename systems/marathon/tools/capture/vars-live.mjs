// Read Marathon's custom properties from the live public CSSOM and write raw/css-vars.json.
// PRODUCT (adapt): onmarathon.com ships one stylesheet. :root and .light declare the light
// shadcn set; .dark and a :root inside @media (prefers-color-scheme: dark) declare the dark
// set. html.light is the live class. The dark block is recorded and resolved on a
// probe with html.dark, and labelled as declared, not painted on a public page.
//
//   PLAYWRIGHT=... node tools/capture/vars-live.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, BASE, UA, PKG, RAW } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const page = await ctx.newPage();
const resp = await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2500);
const htmlClass = await page.evaluate(() => document.documentElement.className);

const harvested = await page.evaluate(() => {
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
          : r.cssText.split('{')[0].trim().slice(0, 120);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
      }
      if (Object.keys(props).length) rules.push({ file, context: ctx, selector: r.selectorText, properties: props });
    }
  };
  for (const sheet of [...document.styleSheets]) {
    let list;
    try { list = sheet.cssRules; } catch (e) {
      errors.push({ href: sheet.href, error: String(e).slice(0, 160) });
      continue;
    }
    walk(list, [], sheet.href || 'inline');
  }
  const computed = {};
  const cs = getComputedStyle(document.documentElement);
  for (const r of rules) for (const k of Object.keys(r.properties)) {
    if (!(k in computed)) computed[k] = cs.getPropertyValue(k).trim();
  }
  return { rules, fonts, errors, computed, title: document.title };
});

// Light is the top-level :root plus .light (the live html class). Dark is .dark plus the :root
// inside @media (prefers-color-scheme: dark). The old split took "the second top-level :root",
// but the dark :root sits inside the media rule, so darkDeclared came out empty.
const rootRules = harvested.rules.filter((r) => r.selector === ':root' && !r.context.length);
const merge = (rules) => Object.assign({}, ...rules.map((r) => r.properties));
const lightDecl = merge(harvested.rules.filter((r) => (r.selector === ':root' && !r.context.length) || (r.selector === '.light' && !r.context.length)));
const darkDecl = merge(harvested.rules.filter((r) => (r.selector === '.dark' && !r.context.length)
  || (r.selector === ':root' && r.context.length === 1 && /prefers-color-scheme:\s*dark/.test(r.context[0]))));

const sheetsCss = await page.evaluate(() => {
  const out = [];
  for (const sheet of [...document.styleSheets]) {
    try {
      const css = [...sheet.cssRules].map((r) => r.cssText).join('\n');
      out.push({ href: sheet.href || 'inline', css });
    } catch (e) {
      out.push({ href: sheet.href || 'inline', error: String(e).slice(0, 80) });
    }
  }
  return out;
});
await ctx.close();

const page2 = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const css = sheetsCss.filter((s) => s.css).map((s) => s.css).join('\n');
const names = [...new Set(harvested.rules.flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !n.startsWith('--tw-')).sort();

async function resolve(mode) {
  const html = '<!doctype html><html class="' + mode + '"><head><style>' + css.replace(/<\/style/gi, '<\\/style') + '</style></head><body><div id="probe"></div></body></html>';
  await page2.setContent(html, { waitUntil: 'load' });
  return page2.evaluate((want) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const el = document.getElementById('probe');
    const box = document.createElement('div');
    box.style.cssText = 'position:absolute;visibility:hidden;width:1000px';
    const probe = document.createElement('div');
    box.appendChild(probe);
    document.body.appendChild(box);
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
      let rgb, a = 1;
      if (m) { rgb = [m[1], m[2], m[3]].map((v) => Math.round(+v)); a = m[4] === undefined ? 1 : +m[4]; }
      else if ((m = c.match(/^color\(srgb ([-\d.e]+) ([-\d.e]+) ([-\d.e]+)(?: \/ ([\d.]+%?))?\)$/))) { rgb = [m[1], m[2], m[3]].map((v) => Math.round(Math.min(1, Math.max(0, +v)) * 255)); a = m[4] === undefined ? 1 : num(m[4]); }
      else if ((m = c.match(/^oklab\(([-\d.e]+%?) ([-\d.e]+) ([-\d.e]+)(?: \/ ([\d.]+%?))?\)$/))) { rgb = fromOklab(num(m[1]), +m[2], +m[3]); a = m[4] === undefined ? 1 : num(m[4]); }
      else if ((m = c.match(/^oklch\(([-\d.e]+%?) ([-\d.e]+) ([-\d.e]+)(?: \/ ([\d.]+%?))?\)$/))) {
        const h = (+m[3] * Math.PI) / 180;
        rgb = fromOklab(num(m[1]), +m[2] * Math.cos(h), +m[2] * Math.sin(h));
        a = m[4] === undefined ? 1 : num(m[4]);
      } else return { unparsed: c };
      a = Math.round(a * 1000) / 1000;
      return a === 1 ? '#' + rgb.map((v) => v.toString(16).padStart(2, '0')).join('') : `rgba(${rgb.join(', ')}, ${a})`;
    };
    const out = {};
    const rootCs = getComputedStyle(document.documentElement);
    for (const name of want) {
      const raw = noUrl(rootCs.getPropertyValue(name).trim());
      if (!raw) continue;
      const r = { raw: raw.length > 300 ? raw.slice(0, 300) + '…' : raw };
      const asColor = raw;
      probe.removeAttribute('style');
      probe.style.cssText = 'position:absolute;left:0;top:0';
      if (CSS.supports('color', asColor) && !/^(inherit|initial|unset|revert)$/.test(raw)) {
        probe.style.color = asColor;
        r.kind = 'color';
        r.value = norm(getComputedStyle(probe).color);
        if (typeof r.value === 'object') { r.kind = 'other'; r.note = 'colour space not converted: ' + r.value.unparsed; delete r.value; }
      } else if (CSS.supports('width', raw) && !raw.includes('%')) {
        probe.style.width = raw;
        r.kind = 'dimension';
        r.value = getComputedStyle(probe).width;
      } else if (/[A-Za-z]/.test(raw) && CSS.supports('font-family', raw)) {
        r.kind = 'fontFamily';
        r.value = raw;
      } else r.kind = 'other';
      out[name] = r;
    }
    return out;
  }, names);
}

const resolved = { light: await resolve('light'), dark: await resolve('dark') };
await browser.close();

const app = harvested.rules.filter((r) => Object.keys(r.properties).some((k) => !k.startsWith('--tw-')));
const tailwind = harvested.rules.filter((r) => Object.keys(r.properties).every((k) => k.startsWith('--tw-')));
const out = {
  readAt: new Date().toISOString().slice(0, 10),
  source: 'live CSSOM of https://onmarathon.com/ in headless Chromium, html class "' + htmlClass + '", status ' + (resp ? resp.status() : '?') + '. Light tokens are :root and .light. Dark tokens are .dark and @media (prefers-color-scheme: dark) :root. The public pages paint html.light, so the dark set is declared and resolved on a probe, not painted on a captured page.',
  liveClass: htmlClass,
  lightSelector: ':root and .light',
  darkSelector: '.dark and @media (prefers-color-scheme: dark) :root; resolved on a probe with html.dark. Not painted on the public pages captured (html.light).',
  counts: { rules: harvested.rules.length, fonts: harvested.fonts.length, names: names.length },
  errors: harvested.errors,
  app,
  tailwindCount: tailwind.length,
  fonts: harvested.fonts,
  lightDeclared: lightDecl,
  darkDeclared: darkDecl,
  liveComputed: harvested.computed,
  resolved,
};
fs.mkdirSync(RAW, { recursive: true });
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('css-vars.json', names.length, 'names; light', Object.keys(resolved.light).length, 'dark', Object.keys(resolved.dark).length);
console.log('live class', htmlClass, 'root blocks', rootRules.length, 'sheet errors', harvested.errors.length);
