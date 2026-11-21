// Choosing and holding the element a component's states are read from. No browser of its own: it
// takes Playwright's page and locators, and test_pin.mjs runs it on stand-ins.

// The first of several candidate locators that matches a visible element, in the order given. A
// Playwright a.or(b) matches both, and its .first() is whichever comes first in the DOM, so a
// fallback that sits earlier on the page wins over the selector the spec prefers.
export async function prefer(...locs) {
  for (const l of locs) if (await l.filter({ visible: true }).count()) return l;
  return locs[0];
}

export const pinName = (key) => String(key).replace(/[^\w-]/g, '_');

// Marks the element `target` finds now with data-m-pin and returns a locator for exactly that node,
// or null when nothing visible matches. A locator finds its element again on every action, so a
// finder such as `[role=tab]:not(.current)` or an auto-rotating carousel slide gives a different
// node once a state has changed the page; every state of one component is read from the pinned node.
export async function pin(page, target, key) {
  const name = pinName(key);
  await page.evaluate((n) => document.querySelectorAll(`[data-m-pin="${n}"]`).forEach((e) => e.removeAttribute('data-m-pin')), name);
  const l = target.filter({ visible: true }).first();
  if (!(await l.count())) return null;
  await l.evaluate((el, n) => el.setAttribute('data-m-pin', n), name);
  return page.locator(`[data-m-pin="${name}"]`);
}

export async function unpin(page, key) {
  const name = pinName(key);
  await page.evaluate((n) => document.querySelectorAll(`[data-m-pin="${n}"]`).forEach((e) => e.removeAttribute('data-m-pin')), name);
}
