"use client";

import { useToast } from "@/components/Toast";

export function copyText(text: string): Promise<void> {
  if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
  return new Promise((resolve) => {
    const ta = Object.assign(document.createElement("textarea"), { value: text });
    document.body.append(ta);
    ta.select();
    try {
      document.execCommand("copy");
    } catch {}
    ta.remove();
    resolve();
  });
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
        await copyText(t || "");
        toast(done || `${label} copied`);
      }}
    >
      {label}
    </button>
  );
}
