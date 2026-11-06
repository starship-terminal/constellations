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

/** The saved model provider object ("ds-provider"), or null. */
export const readStoredProvider = (): Record<string, string> | null => {
  const p = readJSON("ds-provider");
  return p && typeof p === "object" && !Array.isArray(p) ? (p as Record<string, string>) : null;
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
