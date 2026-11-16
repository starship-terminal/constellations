// One-off DOM recon for measure.mjs spec fixes (designer + mobile + pricing).
import { BASE, DESIGNER_URL, launch, open, UA_MOBILE } from './lib.mjs';

const { browser, context } = await launch();

// ---- designer ----
{
  const ctx = await context.browser().newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, locale: 'en-US' });
  const page = await ctx.newPage();
  await open(page, DESIGNER_URL, { wait: 16000 });
  const dump = async (label, fn) => console.log('== ' + label + ' ==\n', JSON.stringify(await page.evaluate(fn), null, 0).slice(0, 3000));
  await dump('tool rail candidates', () => {
    const out = [];
    for (const el of document.querySelectorAll('[class*="toolbar"], [class*="tool"], aside, nav')) {
      const r = el.getBoundingClientRect();
      if (r.width > 0 && r.width < 300 && r.height > 100) out.push(el.tagName + '.' + String(el.className).slice(0, 80) + ' ' + (r.width | 0) + 'x' + (r.height | 0) + '@' + (r.x | 0) + ',' + (r.y | 0) + ' "' + (el.innerText || '').slice(0, 60).replace(/\n/g, '|') + '"');
      if (out.length > 15) break;
    }
    return out;
  });
  await dump('left rail buttons (x<120)', () => {
    const out = [];
    for (const el of document.querySelectorAll('button, [role="button"], a, div[class*="button"], [class*="icon"]')) {
      const r = el.getBoundingClientRect();
      if (r.x < 120 && r.y > 60 && r.width > 10 && r.height > 10 && r.width < 120) out.push(el.tagName + '.' + String(el.className).slice(0, 90) + ' ' + (r.width | 0) + 'x' + (r.height | 0) + '@' + (r.x | 0) + ',' + (r.y | 0) + ' "' + ((el.getAttribute('aria-label') || el.innerText || '').trim()).slice(0, 40).replace(/\n/g, '|') + '"');
      if (out.length > 25) break;
    }
    return out;
  });
  await dump('right panel candidates (x>1100)', () => {
    const out = [];
    for (const el of document.querySelectorAll('[class*="panel"], [class*="inspector"], aside, [class*="sidebar"], [class*="right"]')) {
      const r = el.getBoundingClientRect();
      if (r.x > 1000 && r.width > 100 && r.height > 100) out.push(el.tagName + '.' + String(el.className).slice(0, 90) + ' ' + (r.width | 0) + 'x' + (r.height | 0) + '@' + (r.x | 0) + ',' + (r.y | 0));
      if (out.length > 15) break;
    }
    return out;
  });
  await dump('all class*inspector/modal/dialog', () => {
    const out = [];
    for (const el of document.querySelectorAll('[class*="inspector" i], [class*="modal" i], [class*="dialog" i]')) {
      const r = el.getBoundingClientRect();
      out.push(el.tagName + '.' + String(el.className).slice(0, 90) + ' ' + (r.width | 0) + 'x' + (r.height | 0) + '@' + (r.x | 0) + ',' + (r.y | 0));
      if (out.length > 25) break;
    }
    return out;
  });
  await dump('visible inputs+textareas', () => {
    const out = [];
    for (const el of document.querySelectorAll('input, textarea')) {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      out.push(el.tagName + '.' + String(el.className).slice(0, 70) + ' type=' + el.type + ' ph=' + (el.placeholder || '').slice(0, 40) + ' ' + (r.width | 0) + 'x' + (r.height | 0) + '@' + (r.x | 0) + ',' + (r.y | 0) + ' vis=' + cs.visibility + ' op=' + cs.opacity);
      if (out.length > 20) break;
    }
    return out;
  });
  // open the craft dialog if possible then dump dialog DOM
  const ph = await page.evaluate(() => {
    const els = [...document.querySelectorAll('a,button,div,span')].filter((n) => { const r = n.getBoundingClientRect(); return r.width > 0 && /placeholder image/i.test(n.innerText || '') && ![...n.children].some((c) => /placeholder image/i.test(c.innerText || '')); });
    if (!els.length) return false;
    els[0].click();
    return true;
  });
  console.log('== clicked placeholder:', ph, '==');
  await page.waitForTimeout(12000);
  await dump('dialog-ish elements', () => {
    const out = [];
    for (const el of document.querySelectorAll('[class*="modal" i], [class*="dialog" i], [role="dialog"], [class*="popup" i], [class*="overlay" i], [class*="craft" i]')) {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      if (cs.display === 'none') continue;
      out.push(el.tagName + '.' + String(el.className).slice(0, 100) + ' ' + (r.width | 0) + 'x' + (r.height | 0) + '@' + (r.x | 0) + ',' + (r.y | 0) + ' "' + (el.innerText || '').slice(0, 50).replace(/\n/g, '|') + '"');
      if (out.length > 25) break;
    }
    return out;
  });
  await dump('close-ish buttons', () => {
    const out = [];
    for (const el of document.querySelectorAll('button[class*="close" i], [class*="close" i], button[aria-label*="close" i], svg[class*="close" i]')) {
      const r = el.getBoundingClientRect();
      out.push(el.tagName + '.' + String(el.className).slice(0, 90) + ' ' + (r.width | 0) + 'x' + (r.height | 0) + '@' + (r.x | 0) + ',' + (r.y | 0));
      if (out.length > 20) break;
    }
    return out;
  });
  await ctx.close();
}

// ---- mobile ----
{
  const ctx = await context.browser().newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
  const page = await ctx.newPage();
  await open(page, BASE + '/', { wait: 8000 });
  console.log('== mobile Menu* framer names ==');
  console.log(JSON.stringify(await page.evaluate(() => {
    const out = [];
    for (const el of document.querySelectorAll('[data-framer-name]')) {
      const n = el.getAttribute('data-framer-name');
      if (!/menu|nav|burger/i.test(n)) continue;
      const r = el.getBoundingClientRect();
      out.push(n + ' ' + (r.width | 0) + 'x' + (r.height | 0) + '@' + (r.x | 0) + ',' + (r.y | 0));
    }
    return out;
  }), null, 0).slice(0, 2000));
  console.log('== mobile h1/headings ==');
  console.log(JSON.stringify(await page.evaluate(() => {
    const out = [];
    for (const el of document.querySelectorAll('h1,h2,[data-framer-name*="Hero"],[data-framer-name*="Heading"]')) {
      const r = el.getBoundingClientRect();
      if (r.width > 0) out.push(el.tagName + ' ' + (r.width | 0) + 'x' + (r.height | 0) + ' "' + (el.innerText || '').slice(0, 50).replace(/\n/g, '|') + '"');
      if (out.length > 12) break;
    }
    return out;
  }), null, 0).slice(0, 2000));
  await ctx.close();
}

// ---- marketing "Get Started Now" + footer + pricing card ----
{
  const ctx = await context.browser().newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, locale: 'en-US' });
  const page = await ctx.newPage();
  await open(page, BASE + '/pricing', { wait: 8000 });
  console.log('== pricing framer names (nav/cta/plan) ==');
  console.log(JSON.stringify(await page.evaluate(() => {
    const out = new Set();
    for (const el of document.querySelectorAll('[data-framer-name]')) {
      const n = el.getAttribute('data-framer-name');
      if (/started|plan|card|billing|nav|button|footer/i.test(n)) { const r = el.getBoundingClientRect(); out.add(n + ' ' + (r.width | 0) + 'x' + (r.height | 0)); }
      if (out.size > 40) break;
    }
    return [...out];
  }), null, 0).slice(0, 3000));
  console.log('== pricing monthly/yearly leaves ==');
  console.log(JSON.stringify(await page.evaluate(() => {
    const out = [];
    for (const el of document.querySelectorAll('div,a,button,span,p')) {
      const t = (el.innerText || '').trim();
      if (!/^(monthly|yearly|annual|yearly.*)$/i.test(t) || t.length > 40) continue;
      const r = el.getBoundingClientRect();
      const leaf = ![...el.children].some((c) => (c.innerText || '').trim() === t);
      if (leaf && r.width > 0) out.push(t + ' ' + el.tagName + '.' + String(el.className).slice(0, 60) + ' ' + (r.width | 0) + 'x' + (r.height | 0) + '@' + (r.x | 0) + ',' + (r.y | 0));
      if (out.length > 15) break;
    }
    return out;
  }), null, 0).slice(0, 2000));
  console.log('== pricing plan-card candidates ==');
  console.log(JSON.stringify(await page.evaluate(() => {
    const out = [];
    for (const el of document.querySelectorAll('[data-framer-name*="Plan" i], [data-framer-name*="Card" i], [class*="card" i]')) {
      const t = (el.innerText || '');
      const r = el.getBoundingClientRect();
      if (r.width > 150 && r.width < 700 && r.height > 200 && /pro|basic|trial|\$/i.test(t)) out.push(el.tagName + '.' + String(el.getAttribute('data-framer-name') || el.className).slice(0, 80) + ' ' + (r.width | 0) + 'x' + (r.height | 0) + ' "' + t.slice(0, 60).replace(/\n/g, '|') + '"');
      if (out.length > 15) break;
    }
    return out;
  }), null, 0).slice(0, 3000));
  console.log('== footer selectors ==');
  console.log(JSON.stringify(await page.evaluate(() => {
    const out = [];
    for (const el of document.querySelectorAll('footer, [data-framer-name*="Footer" i], [data-framer-name*="footer" i]')) {
      const r = el.getBoundingClientRect();
      out.push(el.tagName + ' fn=' + (el.getAttribute('data-framer-name') || '-') + ' ' + (r.width | 0) + 'x' + (r.height | 0));
      if (out.length > 10) break;
    }
    return out;
  }), null, 0).slice(0, 1500));
  // does Get Started Now exist anywhere on pricing?
  console.log('== get-started leaf on pricing ==');
  console.log(JSON.stringify(await page.evaluate(() => {
    const out = [];
    for (const el of document.querySelectorAll('a,button,div,span')) {
      const t = (el.innerText || '').trim();
      if (!/^get started/i.test(t) || t.length > 30) continue;
      const leaf = ![...el.children].some((c) => (c.innerText || '').trim() === t);
      const r = el.getBoundingClientRect();
      if (leaf && r.width > 0) out.push(t + ' ' + el.tagName + ' ' + (r.width | 0) + 'x' + (r.height | 0) + '@' + (r.x | 0) + ',' + (r.y | 0));
    }
    return out;
  }), null, 0));
  await ctx.close();
}

await browser.close();
