// A toggled state (the collapsed sidebar, an open FAQ row) is measured only
// after its own press really changed the control, and the page is put back
// to the state it had before that press, never flipped blindly: a press that
// failed leaves nothing to undo, and a press that threw after it landed is
// still undone (2026-11 audit, review on PR 1254, ported here; not run since).
//
// A state spec carries fn (the press), restore (the press back) and,
// optionally, stateOf(loc), which reads the control's state. Without
// stateOf, the restore runs only once the press itself succeeded.

async function readState(st, loc) {
  try { const s = await st.stateOf(loc); return s == null ? null : String(s); } catch { return null; }
}

// Called before the press. Reads the state the restore must return to.
export async function toggleBefore(st, loc) {
  const before = st.stateOf ? await readState(st, loc) : null;
  return { loc, before: before ?? undefined, pressed: false };
}

// The press. Throws, and leaves pressed false, when the press failed or did
// not change the control, so nothing is measured as the toggled state.
export async function toggleOpen(st, rec) {
  const alt = await st.fn(rec.loc);
  if (rec.before !== undefined) {
    const now = await readState(st, rec.loc);
    if (now === rec.before) throw new Error(`the press left the control ${rec.before}`);
  }
  rec.pressed = true;
  return alt;
}

// Called in finally. refind() returns a fresh locator for the control, or
// null. Resolves to what it did; throws when the page could not be put back.
export async function toggleRestore(st, rec, refind) {
  if (rec.before === undefined) {
    if (!rec.pressed) return 'nothing pressed';
    try { await st.restore(rec.loc); } catch (e) {
      const again = await refind();
      if (!again) throw e;
      await st.restore(again);
    }
    return 'pressed back';
  }
  let loc = rec.loc;
  let now = await readState(st, loc);
  if (now === null) {
    loc = await refind();
    if (!loc) throw new Error('the control is gone, so its state is unknown');
    now = await readState(st, loc);
  }
  if (now === rec.before) return 'already as before';
  try { await st.restore(loc); } catch (e) {
    const again = await refind();
    if (!again) throw e;
    loc = again;
    // the failed press may still have landed: press again only if needed
    if ((await readState(st, loc)) !== rec.before) await st.restore(loc);
  }
  const after = await readState(st, loc);
  if (after !== rec.before) throw new Error(`the restore left the control ${after}, not ${rec.before}`);
  return 'restored';
}
