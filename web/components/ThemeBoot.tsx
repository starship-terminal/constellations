"use client";

// Applies the stored theme before paint when layout.tsx's inline script did
// not run (see bootPrefs). Renders nothing.
import { useLayoutEffect } from "react";
import { bootPrefs } from "@/components/prefs";

export function ThemeBoot() {
  useLayoutEffect(bootPrefs, []);
  return null;
}
