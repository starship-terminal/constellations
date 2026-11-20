import { launch, patch, open } from './lib.mjs';
const { browser } = await launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await patch(page);
await open(page, 'https://www.gofundme.com/sign-in', { wait: 8000 });
for (const waitMs of [5000, 10000, 15000]) {
  await page.waitForTimeout(waitMs);
  const info = await page.evaluate(() => {
    const els = [...document.querySelectorAll('input, button, [role="button"], iframe, form')];
    return {
      t: performance.now() | 0,
      els: els.map((b) => {
        const r = b.getBoundingClientRect();
        return `${b.tagName}[${b.type || b.getAttribute('role') || ''}] "${(b.innerText || b.getAttribute('aria-label') || b.name || '').trim().slice(0, 50)}" ${Math.round(r.width)}x${Math.round(r.height)}@${Math.round(r.x)},${Math.round(r.y)} cls=${(b.className || '').toString().slice(0, 50)}`;
      }).filter((s) => !s.includes(' 0x0@')).slice(0, 25),
      title: document.title,
      bodyText: (document.body.innerText || '').trim().slice(0, 200),
    };
  });
  console.log(`--- after ${waitMs}ms more (${info.t})`);
  console.log(info.els.join('\n'));
  console.log('BODY:', JSON.stringify(info.bodyText));
}
await browser.close();
