"use client";

import { useEffect, useRef, useState } from "react";
import { useToast } from "@/components/Toast";
import { copyLabel, copyOutcome, flash, type CopyState } from "@/lib/copy-state";

/** Copy text to the clipboard; rejects when the browser refused. */
export function copyText(text: string): Promise<void> {
  if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
  // Plain-http origins (a tailnet host) have no async clipboard: copy from a
  // throwaway textarea, kept off-screen, read-only (no mobile keyboard) and
  // out of the tab order, focused without scrolling so the page stays put.
  return new Promise((resolve, reject) => {
    const ta = Object.assign(document.createElement("textarea"), { value: text, readOnly: true, tabIndex: -1 });
    ta.setAttribute("aria-hidden", "true");
    Object.assign(ta.style, { position: "fixed", top: "0", left: "-9999px", opacity: "0" });
    const before = document.activeElement as HTMLElement | null;
    document.body.append(ta);
    ta.focus({ preventScroll: true });
    ta.select();
    let ok = false;
    try {
      ok = document.execCommand("copy");
    } catch {}
    ta.remove();
    before?.focus?.({ preventScroll: true });
    if (ok) resolve();
    else reject(new Error("copy refused"));
  });
}

/** Copy, then toast `done`, or say the copy failed so nobody pastes stale text. */
export async function copyWithToast(text: string, toast: (m: string) => void, done: string): Promise<void> {
  try {
    await copyText(text);
    toast(done);
  } catch {
    toast("Could not copy: the browser blocked clipboard access");
  }
}

export function CopyButton({
  text,
  label = "Copy",
  done,
  className = "btn",
  title,
}: {
  text?: string;
  label?: string;
  done?: string;
  className?: string;
  title?: string;
}) {
  const { toast } = useToast();
  return (
    <button
      type="button"
      className={className}
      title={title}
      onClick={() => copyWithToast(text || "", toast, done || `${label} copied`)}
    >
      {label}
    </button>
  );
}

/** Compact copy control for a snippet: flips to "Copied" (or "Copy failed") for a moment, then reverts. */
export function SnippetCopyButton({ text, what }: { text: string; what: string }) {
  const [state, setState] = useState<CopyState>("idle");
  const timer = useRef<ReturnType<typeof setTimeout> | undefined>(undefined);
  useEffect(() => () => clearTimeout(timer.current), []);
  const label = copyLabel(state);
  return (
    <>
      <button
        type="button"
        className="btn snip-copy"
        data-state={state}
        aria-label={`Copy ${what}`}
        onClick={async () => {
          timer.current = flash(setState, await copyOutcome(text, copyText), timer.current);
        }}
      >
        <span key={state} className="snip-label">
          {label}
        </span>
      </button>
      <span className="sr-only" role="status">
        {state === "copied" ? `${what} copied` : state === "failed" ? `Could not copy ${what}` : ""}
      </span>
    </>
  );
}
