// Read Loom's declared custom properties from the live marketing page and the login wall.
// Writes raw/css-vars.json. Does not click consent or sign in.
import fs from 'node:fs';
import path from 'node:path';
import { launch, open, RAW, BASE } from './public/lib.mjs';

fs.mkdirSync(RAW, { recursive: true });

function collect() {
  const noUrl = (v) => String(v).replace(/url\((?!\s*['"]?(?:data:|#))[^)]*\)/gi, 'url(…)');
  const rules = [];
  const fonts = [];
  const walk = (list, ctx, file) => {
    if (!list) return;
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        fonts.push({
          file,
          family: r.style.getPropertyValue('font-family'),
          weight: r.style.getPropertyValue('font-weight'),
          style: r.style.getPropertyValue('font-style'),
          src: noUrl(r.style.getPropertyValue('src')).slice(0, 120),
        });
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + (r.name || '')
          : r.cssText.split('{')[0].trim().slice(0, 100);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k.startsWith('--') && !k.startsWith('--tw-')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
      }
      if (Object.keys(props).length) rules.push({ file, context: ctx, selector: r.selectorText || '', properties: props });
    }
  };
  let blocked = 0;
  for (const sheet of document.styleSheets) {
    const file = sheet.href ? new URL(sheet.href).pathname.slice(-60) : 'inline';
    try { walk(sheet.cssRules, [], file); } catch { blocked++; }
  }
  const htmlStyle = document.documentElement.getAttribute('style') || '';
  const inline = {};
  for (const part of htmlStyle.split(';')) {
    const i = part.indexOf(':');
    if (i < 1) continue;
    const k = part.slice(0, i).trim();
    if (k.startsWith('--')) inline[k] = part.slice(i + 1).trim();
  }
  const cs = getComputedStyle(document.documentElement);
  const resolved = {};
  const names = new Set([...Object.keys(inline), ...rules.flatMap((r) => Object.keys(r.properties))]);
  for (const k of names) {
    if (k.startsWith('--tw-')) continue;
    const v = cs.getPropertyValue(k).trim();
    if (v) resolved[k] = v.slice(0, 240);
  }
  return {
    title: document.title,
    url: location.href,
    blocked,
    inline,
    fonts,
    rules: rules.filter((r) => /lns-|thd-|focus-/.test(JSON.stringify(r.properties).slice(0, 80) + r.selector)).slice(0, 400),
    resolved,
    viewport: { innerWidth, innerHeight, dpr: devicePixelRatio },
  };
}

const { browser, context } = await launch();
const page = await context.newPage();
const pages = {};
for (const url of [BASE + '/', BASE + '/login', BASE + '/pricing']) {
  await open(page, url, { wait: 1800 });
  pages[new URL(url).pathname] = await page.evaluate(collect);
  console.log(url, 'resolved', Object.keys(pages[new URL(url).pathname].resolved).length, 'blocked', pages[new URL(url).pathname].blocked);
}
const out = {
  captured: '2026-11-18',
  product: 'Loom',
  note: 'Marketing html style holds --lns-* literals. Login also declares Atlassian --ds-* tokens. Dark theme tokens (--lns-themeDark-*) are declared and were not painted: marketing and the share page stay light, and adding class dark did not rebind --lns-color-*.',
  pages,
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
await browser.close();
console.log('wrote raw/css-vars.json');
