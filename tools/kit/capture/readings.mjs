// Keeping earlier readings across a rerun. A run rewrites what it read again and drops only what a
// finished run shows is gone: a page or copy that failed partway, or never opened, keeps the
// readings it did not reach, since what it did not reach is not known to be gone. Plain functions,
// no browser, tested in test_readings.mjs.

// The components a run's finished pages no longer produce, and the states those pages' specs no
// longer list, removed from `components` in place. A component belongs to the page in its `run`;
// `done` holds the pages whose capture ran to the end, `touched` the components this run wrote,
// `listed` each component's states as this run's specs list them. Returns what was dropped.
export function pruneStale(components, { done, touched, listed }) {
  const dropped = [];
  for (const [key, c] of Object.entries(components)) {
    if (!done.has(c.run)) continue;
    if (!touched.has(key)) { delete components[key]; dropped.push(key); continue; }
    if (!listed.has(key)) continue;
    for (const st of Object.keys(c.states || {})) if (!listed.get(key).has(st)) { delete c.states[st]; dropped.push(`${key} ${st}`); }
  }
  return dropped;
}

// layout.json after a run: every copy read now replaces its earlier entry, a copy that failed to
// open keeps its earlier one, and an entry for a copy no longer on disk is dropped only when every
// copy opened (a partial run never erases a reading). `fresh` is keyed like the file, `label@width`;
// `failed` lists the labels that did not open, `labels` every label on disk.
export function mergeLayout(earlier, fresh, { failed, labels }) {
  const present = new Set(labels);
  const out = {};
  for (const [k, v] of Object.entries(earlier || {})) {
    const label = v && v.label ? v.label : k.replace(/@\d+$/, '');
    if (present.has(label) ? failed.includes(label) : failed.length) out[k] = v;
  }
  Object.assign(out, fresh);
  // in label order, as layout.mjs reads them, so a rerun keeps the file's order
  const label = (k) => (out[k] && out[k].label) || k.replace(/@\d+$/, '');
  const keys = Object.keys(out).sort((a, b) => (label(a) < label(b) ? -1 : label(a) > label(b) ? 1 : a < b ? -1 : a > b ? 1 : 0));
  return Object.fromEntries(keys.map((k) => [k, out[k]]));
}
