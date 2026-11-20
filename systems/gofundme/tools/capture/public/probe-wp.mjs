import { launch, patch, open } from './lib.mjs';
const { browser } = await launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await patch(page);
await open(page, 'https://www.gofundme.com/c/pricing', { wait: 12000 });
const info = await page.evaluate(() => {
  const sel = 'a.wp-block-button__link, .wp-block-button a, a.hrt-base-button, button.hrt-base-button';
  return [...document.querySelectorAll(sel)].map((b) => {
    const r = b.getBoundingClientRect();
    const inHdr = !!(b.closest('header') || b.closest('nav'));
    return `${b.tagName} "${(b.innerText || '').trim().slice(0, 40)}" ${Math.round(r.width)}x${Math.round(r.height)} hdr=${inHdr} cls=${(b.className || '').toString().slice(0, 50)}`;
  }).slice(0, 15);
});
console.log(JSON.stringify(info, null, 1));
await browser.close();
