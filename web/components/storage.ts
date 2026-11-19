"use client";

// Readers for the browser-saved values more than one component needs.
// Every read tolerates a missing, blocked or malformed localStorage.
const readJSON = (key: string): unknown => {
  try {
    return JSON.parse(localStorage.getItem(key) || "null");
  } catch {
    return null;
  }
};

/** The saved model provider object ("ds-provider"), or null. Only string
    fields are kept (a number or boolean becomes its text): a hand edit or an
    older schema can leave `{"model": 1}` or `null` there, and every reader
    calls string methods on the fields. */
export const readStoredProvider = (): Record<string, string> | null => {
  const p = readJSON("ds-provider");
  if (!p || typeof p !== "object" || Array.isArray(p)) return null;
  const out: Record<string, string> = {};
  for (const [k, v] of Object.entries(p)) {
    if (typeof v === "string") out[k] = v;
    else if (typeof v === "number" || typeof v === "boolean") out[k] = String(v);
  }
  return out;
};

/** Saved media paths ("ds-saved"). */
export const readSavedPaths = (): string[] => {
  const v = readJSON("ds-saved");
  return Array.isArray(v) ? v.filter((x): x is string => typeof x === "string") : [];
};

export const writeSavedPaths = (paths: Iterable<string>) => {
  try {
    localStorage.setItem("ds-saved", JSON.stringify([...paths]));
  } catch {}
};
