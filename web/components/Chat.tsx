"use client";

// The librarian chat, as a right-side drawer available on every page.
// Sends the wire-shaped turn list to /api/chat; renders result cards,
// media strips and copyable agent prompts from the reply's artifacts.
import { createContext, useCallback, useContext, useEffect, useRef, useState } from "react";
import Link from "next/link";
import { useLightbox } from "@/components/Lightbox";
import { useToast } from "@/components/Toast";
import { copyWithToast } from "@/components/CopyButton";
import { migrateStoredProvider, PROVIDER_NOTICE_KEY, saveReplyOf, type SaveReply } from "@/components/storage";

interface ChatResultCard {
  cover?: string;
  icon?: string;
  tint?: string;
  tagline?: string;
}
interface ChatResult {
  store: "systems" | "refero" | "prompt";
  slug: string;
  name: string;
  prompt?: string;
  card?: ChatResultCard;
}
interface ChatMedia {
  url: string;
  name: string;
}
interface Turn {
  role: "user" | "assistant";
  /** User: the typed message. Assistant: rendered HTML, for display only. */
  text?: string;
  /** Assistant: the model's markdown, the form history is sent back in. */
  raw?: string;
  pending?: boolean;
  error?: string;
  results?: ChatResult[];
  media?: ChatMedia[];
  calls?: string[];
}
interface ChatCtx {
  open: (draft?: string) => void;
  close: () => void;
  isOpen: boolean;
  draft: string;
  setDraft: (v: string) => void;
  enabled: boolean;
}
const Ctx = createContext<ChatCtx>({
  open: () => {},
  close: () => {},
  isOpen: false,
  draft: "",
  setDraft: () => {},
  enabled: false,
});

export const useChat = () => useContext(Ctx);

/** Dispatched on window after the server-held provider changes (Settings
    saves or removes it, or the one-time move of a browser-stored key ran). */
export const PROVIDER_EVENT = "ds-provider-change";

const CHANNEL = "ds-provider";

/** Tell this tab (PROVIDER_EVENT) and the app's other tabs (a
    BroadcastChannel carrying no data) that the server-held provider changed. */
export function announceProviderChange(): void {
  window.dispatchEvent(new Event(PROVIDER_EVENT));
  try {
    const ch = new BroadcastChannel(CHANNEL);
    ch.postMessage("changed");
    ch.close();
  } catch {}
}

/** POST a provider to the server's save route; the reply never holds the key. */
export async function saveProvider(body: Record<string, string | boolean>): Promise<SaveReply> {
  const r = await fetch("/api/provider", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(body),
  });
  return saveReplyOf(r.status, await r.json().catch(() => null));
}

// The history the model sees: each question with the markdown answer it got.
// An exchange whose answer failed, is still pending, or is a page placeholder
// is left out whole, so the wire never carries an empty or HTML assistant
// turn and roles keep alternating.
function wireHistory(turns: Turn[]): { role: "user" | "assistant"; content: string }[] {
  const out: { role: "user" | "assistant"; content: string }[] = [];
  turns.forEach((t, i) => {
    const answer = turns[i + 1];
    if (t.role !== "user" || !t.text || answer?.role !== "assistant") return;
    if (answer.pending || answer.error || !answer.raw) return;
    out.push({ role: "user", content: t.text }, { role: "assistant", content: answer.raw });
  });
  return out;
}

const UP_ICON = (
  <svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M8 13V3M3.5 7.5 8 3l4.5 4.5" /></svg>
);

export function ChatProvider({ children }: { children: React.ReactNode }) {
  const [isOpen, setIsOpen] = useState(false);
  const [draft, setDraft] = useState("");
  const [configured, setConfigured] = useState(false);
  const { toast } = useToast();
  useEffect(() => {
    // The server holds the key; the chat is available when it says a
    // provider is configured, and follows Settings through PROVIDER_EVENT.
    const sync = () =>
      fetch("/api/status")
        .then((r) => (r.ok ? r.json() : null))
        .then((d) => setConfigured(!!(d && (d.configured ?? d.envProvider))))
        .catch(() => {});
    sync();
    window.addEventListener(PROVIDER_EVENT, sync);
    // Another tab saved or removed the key: refresh here too, and let this
    // tab's Settings know. Coming back to the tab refreshes as well.
    let ch: BroadcastChannel | null = null;
    try {
      ch = new BroadcastChannel(CHANNEL);
      ch.onmessage = () => window.dispatchEvent(new Event(PROVIDER_EVENT));
    } catch {}
    const onVisible = () => {
      if (document.visibilityState === "visible") sync();
    };
    document.addEventListener("visibilitychange", onVisible);
    // An older version kept the key in localStorage: move it to the server
    // once and delete the browser copy, then say so.
    migrateStoredProvider(saveProvider).then((notice) => {
      if (!notice) return;
      try {
        sessionStorage.setItem(PROVIDER_NOTICE_KEY, notice);
      } catch {}
      toast(notice, 9000);
      announceProviderChange();
    });
    return () => {
      window.removeEventListener(PROVIDER_EVENT, sync);
      document.removeEventListener("visibilitychange", onVisible);
      ch?.close();
    };
  }, [toast]);
  const open = useCallback((d?: string) => {
    setIsOpen(true);
    if (d) setDraft(d);
  }, []);
  const close = useCallback(() => setIsOpen(false), []);
  return (
    <Ctx.Provider value={{ open, close, isOpen, draft, setDraft, enabled: configured }}>
      {children}
    </Ctx.Provider>
  );
}

export function ChatDrawer() {
  const { isOpen, open, close, draft, setDraft, enabled } = useChat();
  const [turns, setTurns] = useState<Turn[]>([]);
  const [busy, setBusy] = useState(false);
  const epoch = useRef(0);
  const body = useRef<HTMLDivElement>(null);
  const drawer = useRef<HTMLDivElement>(null);
  const input = useRef<HTMLInputElement>(null);
  const fab = useRef<HTMLButtonElement>(null);
  const opener = useRef<HTMLElement | null>(null);
  const lb = useLightbox();
  const { toast } = useToast();

  // Opening moves focus into the drawer (the composer, or Close when the
  // composer is disabled); closing hands it back to whatever opened it.
  useEffect(() => {
    if (isOpen) {
      const from = document.activeElement;
      if (from instanceof HTMLElement && !drawer.current?.contains(from)) opener.current = from;
      const target = input.current && !input.current.disabled ? input.current : drawer.current?.querySelector<HTMLElement>("[data-chat-close]");
      target?.focus({ preventScroll: true });
      return;
    }
    if (drawer.current?.contains(document.activeElement)) {
      const back = opener.current && document.contains(opener.current) ? opener.current : fab.current;
      back?.focus();
    }
    opener.current = null;
  }, [isOpen]);

  useEffect(() => {
    body.current?.scrollTo({ top: body.current.scrollHeight });
  }, [turns]);

  const reset = () => {
    epoch.current++;
    setTurns([]);
    setBusy(false);
    setDraft("");
  };

  const send = async () => {
    const text = draft.trim();
    if (!text || busy) return;
    const wire = wireHistory(turns);
    wire.push({ role: "user", content: text });
    const myEpoch = epoch.current;
    setDraft("");
    setBusy(true);
    setTurns((t) => [...t, { role: "user", text }, { role: "assistant", pending: true }]);
    try {
      const r = await fetch("/api/chat", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ messages: wire }),
      });
      const d = await r.json();
      if (myEpoch !== epoch.current) return;
      setTurns((t) => {
        const next = [...t];
        const pending = next[next.length - 1];
        if (!pending?.pending) return t;
        next[next.length - 1] = {
          role: "assistant",
          text: d.reply || d.message || (d.error === "no_provider" ? "No model is configured yet." : ""),
          raw: typeof d.raw === "string" ? d.raw : undefined,
          error: d.error,
          results: d.results || [],
          media: d.media || [],
          calls: d.calls || [],
        };
        return next;
      });
    } catch {
      if (myEpoch !== epoch.current) return;
      setTurns((t) => {
        const next = [...t];
        if (next[next.length - 1]?.pending)
          next[next.length - 1] = { role: "assistant", error: "No answer from the server.", results: [], media: [] };
        return next;
      });
    } finally {
      if (myEpoch === epoch.current) setBusy(false);
    }
  };

  return (
    <>
      <button ref={fab} className="chat-fab btn primary" type="button" aria-expanded={isOpen} onClick={() => (isOpen ? close() : open())}>
        Ask the librarian
      </button>
      <div
        ref={drawer}
        className={`chat-drawer${isOpen ? " open" : ""}`}
        role="dialog"
        aria-label="Librarian chat"
        aria-hidden={!isOpen}
        inert={!isOpen}
        onKeyDown={(e) => {
          // Escape that cancels an IME candidate belongs to the composition.
          if (e.key === "Escape" && !e.nativeEvent.isComposing) {
            e.stopPropagation();
            close();
          }
        }}
      >
        <div className="chat-head">
          <b>Librarian</b>
          <div className="side">
            <button className="rf-mini" type="button" onClick={reset}>
              New
            </button>
            <button className="rf-mini" type="button" onClick={close} aria-label="Close chat" data-chat-close>
              ✕
            </button>
          </div>
        </div>
        <p className="chat-note">Answers cite the library's own data; cards open the style.</p>
        <div className="chat-body" ref={body}>
          {!turns.length && !enabled && (
            <div className="chat-empty">
              <p>
                <b>No model is set up.</b> The librarian needs a model provider before it can answer.
              </p>
              <p>
                <Link href="/settings#model-provider" onClick={close}>
                  Set up a model in Settings
                </Link>
              </p>
            </div>
          )}
          {!turns.length && (
            <p className="chat-note">Ask for a style, mood or use — “a dark fintech dashboard”, “playful onboarding like Duolingo”.</p>
          )}
          {turns.map((t, i) => (
            <ChatTurn key={i} t={t} lb={lb} toast={toast} />
          ))}
        </div>
        <div className="chat-composer">
          <label className="field">
            <input
              ref={input}
              type="text"
              aria-label="Message the librarian"
              placeholder={enabled ? "Ask for a style, mood or use…" : "Set up a model in Settings to chat"}
              value={draft}
              onChange={(e) => setDraft(e.target.value)}
              onKeyDown={(e) => {
                // Enter that commits an IME composition is not a send.
                if (e.key === "Enter" && !e.nativeEvent.isComposing) send();
              }}
              disabled={!enabled}
            />
          </label>
          <button className="chat-send" type="button" onClick={send} disabled={busy || !enabled} aria-label="Send">
            {UP_ICON}
          </button>
        </div>
      </div>
    </>
  );
}

function ChatTurn({ t, lb, toast }: { t: Turn; lb: ReturnType<typeof useLightbox>; toast: (m: string) => void }) {
  if (t.role === "user")
    return (
      <div className="chat-turn user">
        <p style={{ margin: 0 }}>{t.text}</p>
      </div>
    );
  if (t.pending)
    return (
      <div className="chat-turn assistant">
        <div className="chat-dots">
          <i />
          <i />
          <i />
        </div>
      </div>
    );
  return (
    <div className="chat-turn assistant">
      {t.error === "no_provider" ? (
        <p className="chat-error">
          <Link href="/settings">Set up a model in Settings</Link> to chat.
        </p>
      ) : t.error ? (
        <p className="chat-error">{t.error}</p>
      ) : null}
      {t.text ? <div className="md chat-md" dangerouslySetInnerHTML={{ __html: t.text }} /> : null}
      {!!t.results?.length && (
        <div className="chat-results">
          {t.results.map((r, i) =>
            r.store === "prompt" ? (
              <button
                key={i}
                className="btn"
                type="button"
                onClick={() => copyWithToast(r.prompt || "", toast, "Agent prompt copied")}
              >
                Copy agent prompt · {r.slug}
              </button>
            ) : (
              <Link key={i} className="card" href={r.store === "systems" ? `/gallery/${r.slug}` : `/refero/${r.slug}`}>
                <div className="cover" style={r.card?.tint ? ({ "--tint": r.card.tint } as React.CSSProperties) : undefined}>
                  {r.card?.cover ? <img src={r.card.cover} alt="" loading="lazy" /> : null}
                </div>
                <div className="card-foot">
                  <span className="foot-icon">{r.card?.icon ? <img src={r.card.icon} alt="" /> : <i>{(r.name || "?")[0].toUpperCase()}</i>}</span>
                  <div className="foot-txt">
                    <h2>{r.name}</h2>
                  </div>
                </div>
              </Link>
            ),
          )}
        </div>
      )}
      {!!t.media?.length && (
        <div className="chat-media">
          {t.media.map((m, i) => (
            <button
              key={i}
              className="chat-shot"
              type="button"
              onClick={() => lb.open({ items: t.media!.map((x) => ({ path: x.url, name: x.name })), index: i })}
            >
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src={m.url} alt={m.name} loading="lazy" />
            </button>
          ))}
        </div>
      )}
      {!!t.calls?.length && <p className="chat-calls">tools: {t.calls.join(", ")}</p>}
    </div>
  );
}
