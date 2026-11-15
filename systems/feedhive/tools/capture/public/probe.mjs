// One-off DOM probe for selector fixes. Not part of the kit.
import { BASE, launch, open } from './lib.mjs';

const { browser, context } = await launch();
const page = await context.newPage();

const dump = async (name, fn) => {
  console.log('=== ' + name);
  const r = await page.evaluate(fn).catch((e) => 'ERR ' + e.message);
  console.log(JSON.stringify(r, null, 1));
};

await open(page, BASE + '/', { wait: 7000 });

await dump('header signup/login links', () =>
  [...document.querySelectorAll('header a[href*="signin"], header a[href*="signup"], header a[href*="app.feedhive"]')].map((a) => {
    const r = a.getBoundingClientRect();
    const cs = getComputedStyle(a);
    return { href: a.getAttribute('href'), text: (a.innerText || '').trim().slice(0, 30), rect: `${r.width | 0}x${r.height | 0}@${r.x | 0},${r.y | 0}`, vis: cs.visibility, op: cs.opacity, disp: cs.display, cls: String(a.className).slice(0, 80) };
  }));

await dump('hero badge candidates', () => {
  const els = [...document.querySelectorAll('main a, main div, main span, main p')].filter((n) => /Introducing FeedHive/i.test(n.innerText || ''));
  return els.slice(0, 12).map((n) => {
    const r = n.getBoundingClientRect();
    return { tag: n.tagName, cls: String(n.className).slice(0, 90), rect: `${r.width | 0}x${r.height | 0}`, text: (n.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 60) };
  });
});

await dump('hero check candidates', () => {
  const els = [...document.querySelectorAll('main li, main div, main p')].filter((n) => /Create with AI|Automate\.|Collaborate\./i.test(n.innerText || ''));
  return els.slice(0, 12).map((n) => {
    const r = n.getBoundingClientRect();
    return { tag: n.tagName, cls: String(n.className).slice(0, 90), rect: `${r.width | 0}x${r.height | 0}`, text: (n.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 60) };
  });
});

await dump('hero mock candidates', () => {
  const els = [...document.querySelectorAll('main div, main section, main aside')].filter((n) => /Discard|Accept|Create a post|Regenerate/i.test(n.innerText || ''));
  return els.slice(0, 14).map((n) => {
    const r = n.getBoundingClientRect();
    return { tag: n.tagName, cls: String(n.className).slice(0, 90), rect: `${r.width | 0}x${r.height | 0}@${r.x | 0},${r.y | 0}`, text: (n.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 60) };
  });
});

await page.goto(BASE + '/pricing', { waitUntil: 'domcontentloaded' }).catch(() => {});
await page.waitForTimeout(7000);

await dump('plan card structure', () => {
  const h = [...document.querySelectorAll('h2,h3,p,span,div')].filter((n) => /^(Business|Creator|Agency|Brand)$/.test((n.innerText || '').trim()));
  return h.slice(0, 8).map((n) => {
    const chain = [];
    for (let x = n, i = 0; x && i < 6; x = x.parentElement, i++) {
      const r = x.getBoundingClientRect();
      const cs = getComputedStyle(x);
      chain.push({ tag: x.tagName, cls: String(x.className).slice(0, 70), rect: `${r.width | 0}x${r.height | 0}`, bg: cs.backgroundColor !== 'rgba(0, 0, 0, 0)' ? cs.backgroundColor : '', rad: cs.borderRadius });
    }
    return { name: (n.innerText || '').trim(), tag: n.tagName, chain };
  });
});

await dump('trial badge candidates', () => {
  const els = [...document.querySelectorAll('main *')].filter((n) => /free trial/i.test(n.innerText || '') && n.children.length < 8);
  return els.slice(0, 14).map((n) => {
    const r = n.getBoundingClientRect();
    return { tag: n.tagName, cls: String(n.className).slice(0, 70), rect: `${r.width | 0}x${r.height | 0}`, kids: n.children.length, text: (n.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 60) };
  });
});

await page.goto(BASE + '/features/scheduling', { waitUntil: 'domcontentloaded' }).catch(() => {});
await page.waitForTimeout(7000);

await dump('feature masthead area', () => {
  const h1 = document.querySelector('h1');
  const out = { h1: h1 && (h1.innerText || '').trim() };
  out.eyebrow = [...document.querySelectorAll('main *')].filter((n) => {
    const t = (n.innerText || '').trim();
    return t.length < 40 && /^[A-Z\s&]+$/.test(t) && t.length > 3 && n.children.length < 4;
  }).slice(0, 10).map((n) => {
    const r = n.getBoundingClientRect();
    return { tag: n.tagName, cls: String(n.className).slice(0, 70), rect: `${r.width | 0}x${r.height | 0}`, text: (n.innerText || '').trim().slice(0, 40) };
  });
  out.ctas = [...document.querySelectorAll('main a')].filter((a) => {
    const r = a.getBoundingClientRect();
    return r.top < 900 && r.width < 400 && /get started|try|sign up|start|book/i.test(a.innerText || '');
  }).slice(0, 8).map((a) => {
    const r = a.getBoundingClientRect();
    return { text: (a.innerText || '').trim().slice(0, 40), rect: `${r.width | 0}x${r.height | 0}@${r.x | 0},${r.y | 0}`, cls: String(a.className).slice(0, 70) };
  });
  out.blocks = [...document.querySelectorAll('main section, main article, main li')].filter((n) => {
    const r = n.getBoundingClientRect();
    return r.height > 100 && r.height < 700 && r.width > 200 && r.width < 800;
  }).slice(0, 10).map((n) => {
    const r = n.getBoundingClientRect();
    return { tag: n.tagName, cls: String(n.className).slice(0, 70), rect: `${r.width | 0}x${r.height | 0}`, text: (n.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 60) };
  });
  return out;
});

await page.goto('https://app.feedhive.com/signin', { waitUntil: 'domcontentloaded' }).catch(() => {});
await page.waitForTimeout(12000);

await dump('login card structure', () => {
  const els = [...document.querySelectorAll('form, div, section')].filter((n) => /get you signed in/i.test(n.innerText || ''));
  return els.slice(0, 10).map((n) => {
    const r = n.getBoundingClientRect();
    const cs = getComputedStyle(n);
    return { tag: n.tagName, cls: String(n.className).slice(0, 70), rect: `${r.width | 0}x${r.height | 0}`, bg: cs.backgroundColor, rad: cs.borderRadius, kids: n.children.length };
  });
});

await browser.close();
console.log('done');
