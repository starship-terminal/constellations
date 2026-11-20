// Read dates for measure.mjs's merge into raw/components-computed.json. Pure, so
// tools/capture/public/test_dates.mjs checks it without a browser.
//
// A rerun starts from the committed readings and replaces only what it reads, so the dates must
// say which readings are new:
// - _meta.read is the last date a state was actually read. It keeps the earlier date until this
//   run reads one, and _meta.lastAttempt records the run either way.
// - each component and each state carries its own `read`; ones kept from before per-component
//   dates existed take the earlier _meta.read (or _meta.captured), never this run's date.
// - a failed read keeps the earlier good reading with `recaptureError` and `recaptureRun`.

export function startRun(prev, run) {
  const meta = { ...(prev._meta || {}) };
  const prior = meta.read || meta.captured;
  const components = prev.components || {};
  for (const c of Object.values(components)) {
    if (!c || typeof c !== 'object') continue;
    if (!c.read && prior) c.read = prior;
    for (const st of Object.values(c.states || {})) {
      if (st && typeof st === 'object' && !st.read && prior) st.read = prior;
    }
  }
  meta.lastAttempt = run;
  return { _meta: meta, components };
}

// The first time this run reaches `key`: a fresh entry that remembers the earlier states, so a
// failed read can keep them. The entry keeps its earlier `read` until a state is read.
export function touch(out, earlier, key, fields) {
  const old = out.components[key];
  if (old && !earlier.has(key)) earlier.set(key, old.states || {});
  out.components[key] = { states: {}, ...fields, ...(old && old.read ? { read: old.read } : {}) };
  return out.components[key];
}

export function readOk(out, c, state, reading, run) {
  c.states[state] = { ...reading, read: run };
  c.read = run;
  out._meta.read = run;
  if (!out._meta.captured) out._meta.captured = run;
}

export function readFailed(c, earlierStates, state, fields, run) {
  const prev = (earlierStates || {})[state];
  c.states[state] = prev && !prev.error && !prev.skipped
    ? { ...prev, ...('error' in fields ? { recaptureError: fields.error } : { recaptureSkipped: fields.skipped }), recaptureRun: run }
    : { ...fields, recaptureRun: run };
}
