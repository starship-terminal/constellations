// How measure-pass2.mjs folds a run into the saved raw/readings-pass2.json.
//
// A component is { <state>: reading, ..., crop }. A state is replaced only by a reading this run
// actually took; every state this run did not read (because a selector missed or the pass threw
// before reaching it) keeps the saved reading. Each reading carries `readAt`, the run that took it:
// a new reading gets this run's date, a kept one keeps its own. Plain JavaScript with no imports,
// so the package test can load it without Playwright.

export function mergeReadings(earlier, out, runDate) {
  const saved = (earlier && earlier.components) || {};
  const components = {};
  for (const key of new Set([...Object.keys(saved), ...Object.keys(out.components || {})])) {
    const before = saved[key] || {};
    const now = (out.components || {})[key] || {};
    const merged = { ...before };
    for (const [state, reading] of Object.entries(now)) {
      if (reading == null) continue;  // a read that produced nothing never replaces a saved one
      merged[state] = reading && typeof reading === 'object' && !Array.isArray(reading)
        ? { ...reading, readAt: reading.readAt || runDate }
        : reading;  // crop file names and other plain fields
    }
    components[key] = merged;
  }
  return {
    ...(earlier || {}),
    ...out,
    components,
    motion: { ...((earlier && earlier.motion) || {}), ...(out.motion || {}) },
    notes: out.notes || [],
    readAt: runDate,
  };
}
