// Putting the owner's new-thread draft back after a run. Kept apart from product.mjs (which loads Playwright)
// so `node --test` can check it; test_draft.py runs that from `make test`.
//
// The draft is never typed back: Playwright's keyboard.type sends "\n" as an Enter press, and Enter submits
// Capy's composer, so a multi-line draft would start a real thread on the owner's account mid-restore.
// Instead the saved localStorage value is written back as it was and the page reloads to pick it up.
//
// restoreDraft takes the product's own reads and writes:
//   saved      the raw localStorage value read before the run (Capy stores an empty draft as the JSON text null)
//   write(v)   writes v back to the draft key
//   reload()   reloads the page so the composer reads the key again
//   read()     the raw localStorage value now
// It resolves `false` when there was no draft (and the composer reads back empty), `true` once the draft reads
// back unchanged, and throws when either does not hold, so the capture fails instead of leaving the owner's draft lost or changed.
export const draftText = v => {
  try { return (v && JSON.parse(v)?.text) || ''; } catch { return ''; }
};

export async function restoreDraft({ saved, write, reload, read }) {
  const want = draftText(saved);
  if (want) {
    await write(saved);
    await reload();
  }
  // Read back either way: with no saved draft the composer must be empty again (the clear before this only
  // sends keys, so a failed or slow clear would otherwise go unnoticed).
  const got = draftText(await read());
  if (got !== want) throw new Error(`the draft was not restored: ${got.slice(0, 60)}`);
  return Boolean(want);
}
