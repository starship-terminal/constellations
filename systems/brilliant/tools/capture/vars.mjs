import fs from 'fs';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
// SP is the capture's scratch directory; the readings go to $SP/cap/, outside the repository.
const SP = process.env.SP;
if (!SP) { console.error('set SP to a scratch directory outside the repository'); process.exit(2); }
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1440, height: 900 } });
  const p = await ctx.newPage();
  const fonts = [];
  // A font response URL can carry a signed or per-account query: keep the path only.
  const bare = (u) => u.split(/[?#]/)[0];
  p.on('response', r => { const u = r.url(); if (/\.(woff2?|ttf|otf)(\?|$)/.test(u) || r.headers()['content-type']?.includes('font')) fonts.push(bare(u)); });
  await p.goto('https://brilliant.org/', { waitUntil: 'networkidle', timeout: 60000 });
  await p.waitForTimeout(1500);
  const out = await p.evaluate(() => {
    // A custom property can hold a url() with a signed or per-account query: record it as url(…).
    // Its value keeps the authored tokens, so this matches URL( too, escapes and space inside the parens.
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const root = {}, dark = {}, other = {}, fontfaces = [], keyframes = [], media = new Set();
    const walk = (rules) => { for (const r of rules) {
      if (r.cssRules && !r.style) { if (r.conditionText) media.add(r.conditionText); walk(r.cssRules); }
      if (r.type === 5) fontfaces.push(noUrl(r.cssText));
      if (r.type === 7) keyframes.push(r.name);
      if (!r.style) continue;
      const sel = r.selectorText || '';
      for (const n of r.style) if (n.startsWith('--')) {
        const v = noUrl(r.style.getPropertyValue(n).trim());
        if (sel.startsWith(':where(:root, :host)')) root[n] = v;
        else if (sel.startsWith('[data-theme="dark"]') && sel.includes(':not(:is([data-theme="light"]')) { if (!sel.includes(' .')) dark[n] = v; }
        else (other[sel] ||= {})[n] = v;
      }
      if (r.cssRules && r.style) walk(r.cssRules);
    }};
    for (const ss of document.styleSheets) { try { walk(ss.cssRules) } catch {} }
    return { root, dark, other, fontfaces, keyframes: [...new Set(keyframes)], media: [...media] };
  });
  fs.writeFileSync(SP + '/cap/vars-home.json', JSON.stringify({ ...out, fonts: [...new Set(fonts)] }, null, 1));
  console.log(Object.keys(out.root).length, Object.keys(out.dark).length, out.fontfaces.length, fonts.length, out.media.length);
  await b.close();
})();
