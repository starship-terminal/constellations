"use client";

import { useEffect, useRef, useState } from "react";
import { useToast } from "@/components/Toast";
import { COPY_RESET_MS, copyLabel, copyOutcome, type CopyState } from "@/lib/copy-state";

/** Copy text to the clipboard; rejects when the browser refused. */
export function copyText(text: string): Promise<void> {
  if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
  return new Promise((resolve, reject) => {
    const ta = Object.assign(document.createElement("textarea"), { value: text });
    document.body.append(ta);
    ta.select();
    let ok = false;
    try {
      ok = document.execCommand("copy");
    } catch {}
    ta.remove();
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
  fetchUrl,
}: {
  text?: string;
  label?: string;
  done?: string;
  className?: string;
  title?: string;
  /** Text to fetch on click (kept inside the gesture for Safari). */
  fetchUrl?: string;
}) {
  const { toast } = useToast();
  return (
    <button
      type="button"
      className={className}
      title={title}
      onClick={async () => {
        let t = text;
        if (!t && fetchUrl) {
          try {
            const r = await fetch(fetchUrl, { cache: "no-cache" });
            if (!r.ok) throw new Error();
            t = await r.text();
          } catch {
            toast(`No export yet; run \`make build\` first`);
            return;
          }
        }
        await copyWithToast(t || "", toast, done || `${label} copied`);
      }}
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
          const next = await copyOutcome(text, copyText);
          setState(next);
          clearTimeout(timer.current);
          timer.current = setTimeout(() => setState("idle"), COPY_RESET_MS);
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
