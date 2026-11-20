// prefer(), copied from the kit's tools/kit/capture/public/pin.mjs (the only helper this
// package's measure.mjs uses). No browser of its own: test_prefer.mjs runs it on stand-ins.

// The first of several candidate locators that matches a visible element, in the order given. A
// Playwright a.or(b) matches both, and its .first() is whichever comes first in the DOM, so a
// fallback that sits earlier on the page wins over the selector the spec prefers.
export async function prefer(...locs) {
  for (const l of locs) if (await l.filter({ visible: true }).count()) return l;
  return locs[0];
}
