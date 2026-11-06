"use client";

// "/" focuses a listing's search field, unless the reader is typing or an
// open dialog (lightbox, chat drawer) holds focus.
import { useEffect, type RefObject } from "react";

export function useSlashFocus(ref: RefObject<HTMLInputElement | null>) {
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key !== "/" || e.metaKey || e.ctrlKey) return;
      const t = e.target as HTMLElement;
      if (/^(input|textarea|select)$/i.test(t.tagName) || t.isContentEditable) return;
      if (document.querySelector('[aria-modal="true"], [role="dialog"]:not([aria-hidden="true"])')) return;
      e.preventDefault();
      ref.current?.focus();
    };
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, [ref]);
}
