"use client";
import Link from "next/link";
import { useEffect, useMemo, useRef, useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { useChat } from "@ai-sdk/react";
import { DefaultChatTransport, type UIMessage } from "ai";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import {
  ArrowDown,
  ArrowRight,
  ArrowUp,
  BookOpen,
  Check,
  ChevronDown,
  Download,
  LoaderCircle,
  Pin,
  Plus,
  Search,
  SlidersHorizontal,
  Square,
  Sparkles,
  X,
} from "lucide-react";
import type { LibraryItem, LibraryDetail } from "@/contracts/library";
import {
  api,
  CopyButton,
  download,
  Empty,
  ErrorState,
  MediaPreview,
  Spinner,
  useResource,
} from "@/components/shared";
import {
  ReferenceCard,
  ReferenceInspector,
  SaveReference,
} from "@/components/reference";
const suggestions = [
  "A calm, focused workspace",
  "Onboarding that feels effortless",
  "Editorial typography with personality",
  "Thoughtful dark interfaces",
];
function Composer({
  value,
  onChange,
  onSubmit,
  busy = false,
  onStop,
  hero = false,
}: {
  value: string;
  onChange: (value: string) => void;
  onSubmit: () => void;
  busy?: boolean;
  onStop?: () => void;
  hero?: boolean;
}) {
  const ref = useRef<HTMLTextAreaElement>(null);
  useEffect(() => {
    if (ref.current) {
      ref.current.style.height = "auto";
      ref.current.style.height = Math.min(ref.current.scrollHeight, 200) + "px";
    }
  }, [value]);
  useEffect(() => {
    function focus(e: KeyboardEvent) {
      if ((e.metaKey || e.ctrlKey) && e.key === "k") {
        e.preventDefault();
        ref.current?.focus();
      }
    }
    window.addEventListener("keydown", focus);
    return () => window.removeEventListener("keydown", focus);
  }, []);
  return (
    <form
      className={`research-composer ${hero ? "hero-composer" : ""} ${busy ? "working" : ""}`}
      onSubmit={(e) => {
        e.preventDefault();
        if (!busy && value.trim()) onSubmit();
      }}
    >
      <textarea
        ref={ref}
        aria-label="Research prompt"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={
          hero
            ? "Describe what you’re designing…"
            : "Keep exploring, or refine your direction…"
        }
        rows={hero ? 3 : 1}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey && !e.nativeEvent.isComposing) {
            e.preventDefault();
            if (!busy && value.trim()) onSubmit();
          }
        }}
      />
      <div className="composer-bottom">
        <span>
          <Search size={14} />
          {hero ? "Research your design library" : "Grounded in your library"}
        </span>
        <div className="spacer" />
        {busy && onStop ? (
          <button
            type="button"
            className="composer-submit"
            onClick={onStop}
            aria-label="Stop research"
          >
            <Square size={15} fill="currentColor" />
          </button>
        ) : (
          <button
            className="composer-submit"
            type="submit"
            disabled={busy || !value.trim()}
            aria-label="Send research prompt"
          >
            {busy ? (
              <LoaderCircle size={18} className="spin" />
            ) : (
              <ArrowUp size={20} />
            )}
          </button>
        )}
      </div>
    </form>
  );
}
export function ResearchHome() {
  const router = useRouter(),
    [prompt, setPrompt] = useState(""),
    [busy, setBusy] = useState(false),
    [error, setError] = useState(""),
    [inspecting, setInspecting] = useState<LibraryItem | null>(null);
  const { data } = useResource<{ items: LibraryItem[]; total: number }>(
    "/api/library?limit=8&source=systems",
  );
  const items = data?.items || [];
  async function begin() {
    if (!prompt.trim() || busy) return;
    setBusy(true);
    setError("");
    try {
      const d = await api("/api/conversations", {
        method: "POST",
        body: JSON.stringify({
          title: prompt.trim().slice(0, 80),
          initialText: prompt.trim(),
        }),
      });
      const id = d.id || d.conversation?.id;
      if (!id) throw new Error("The server did not return a research ID.");
      window.dispatchEvent(new Event("research-history"));
      router.push(`/research/${id}?start=1`);
    } catch (e) {
      setError((e as Error).message);
      setBusy(false);
    }
  }
  return (
    <div className="research-home">
      <div className="home-topline">
        <span>Your personal design practice</span>
        <Link href="/library">
          Browse the library
          <ArrowUpRightIcon />
        </Link>
      </div>
      <section className="research-hero">
        <div className="eyebrow">A space to look closer</div>
        <h1>
          Where will your
          <br />
          next idea take you?
        </h1>
        <p>Find references. Notice the details. Make something your own.</p>
        <div className="hero-composer-wrap">
          <Composer
            value={prompt}
            onChange={setPrompt}
            onSubmit={begin}
            busy={busy}
            hero
          />
          {error && (
            <p className="error-text" role="alert">
              {error}
            </p>
          )}
        </div>
        <div className="suggestion-row">
          {suggestions.map((s) => (
            <button
              className="suggestion-pill"
              key={s}
              onClick={() => setPrompt(s)}
            >
              {s}
              <ArrowUpRightIcon />
            </button>
          ))}
        </div>
      </section>
      <section className="home-gallery">
        <div className="section-heading">
          <div>
            <div className="eyebrow">A few places to begin</div>
            <h2>Made to be looked at.</h2>
          </div>
          <Link className="text-link" href="/library">
            Explore all references
            <ArrowRight size={15} />
          </Link>
        </div>
        <div className="home-reference-grid">
          {items.map((item) => (
            <ReferenceCard key={item.id} item={item} onOpen={setInspecting} />
          ))}
        </div>
      </section>
      <ReferenceInspector
        items={items}
        current={inspecting}
        onChange={setInspecting}
        onClose={() => setInspecting(null)}
      />
    </div>
  );
}
function ArrowUpRightIcon() {
  return (
    <svg
      width="14"
      height="14"
      viewBox="0 0 16 16"
      fill="none"
      aria-hidden="true"
    >
      <path
        d="M4 12 12 4M4 4h8v8"
        stroke="currentColor"
        strokeWidth="1.3"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}
interface Conversation {
  id: string;
  title: string;
  messages: UIMessage[];
  pinnedIds: string[];
  excludedIds: string[];
}
function normalizeConversation(data: any): Conversation {
  return data.conversation || data;
}
export function ResearchPage({ id }: { id: string }) {
  const { data, error, loading } = useResource<Conversation>(
    `/api/conversations/${id}`,
  );
  return loading ? (
    <Spinner label="Opening research…" />
  ) : error ? (
    <div className="page">
      <ErrorState message={error} />
      <Link href="/" className="pill">
        Start a new research
      </Link>
    </div>
  ) : data ? (
    <ResearchConversation key={id} initial={normalizeConversation(data)} />
  ) : null;
}
function ResearchConversation({ initial }: { initial: Conversation }) {
  const [value, setValue] = useState(""),
    [pinned, setPinned] = useState(initial.pinnedIds || []),
    [excluded, setExcluded] = useState(initial.excludedIds || []),
    [inspecting, setInspecting] = useState<LibraryItem | null>(null),
    [localError, setLocalError] = useState(""),
    [allReferences, setAllReferences] = useState<Record<string, LibraryItem>>(
      {},
    );
  const end = useRef<HTMLDivElement>(null),
    started = useRef(false),
    nearBottom = useRef(true),
    steeringQueue = useRef<Promise<void>>(Promise.resolve()),
    steeringState = useRef({
      pinned: initial.pinnedIds || [],
      excluded: initial.excludedIds || [],
    });
  const { messages, sendMessage, status, error, stop, regenerate, clearError } =
    useChat({
      id: initial.id,
      messages: initial.messages || [],
      transport: new DefaultChatTransport({ api: "/api/research" }),
      onFinish() {
        window.dispatchEvent(new Event("research-history"));
      },
    });
  const busy = status === "submitted" || status === "streaming";
  useEffect(() => {
    // Persist the prompt before navigation. Deferring the request allows React's
    // development effect setup/cleanup cycle to finish before starting a stream.
    const timer = window.setTimeout(() => {
      const url = new URL(window.location.href);
      if (started.current || url.searchParams.get("start") !== "1") return;
      if (initial.messages.at(-1)?.role !== "user") return;
      started.current = true;
      url.searchParams.delete("start");
      window.history.replaceState(
        window.history.state,
        "",
        `${url.pathname}${url.search}${url.hash}`,
      );
      regenerate({
        body: {
          id: initial.id,
          pinnedIds: initial.pinnedIds || [],
          excludedIds: initial.excludedIds || [],
        },
      }).catch((e) => setLocalError(e.message));
    }, 0);
    return () => window.clearTimeout(timer);
  }, [initial.id, regenerate]);
  useEffect(() => {
    const refs: Record<string, LibraryItem> = {};
    for (const message of messages)
      for (const part of message.parts as any[]) {
        if (part.output?.items)
          for (const item of part.output.items)
            if (item.id) refs[item.id] = item;
        if (part.output?.reference?.id)
          refs[part.output.reference.id] = part.output.reference;
      }
    setAllReferences((prev) => ({ ...prev, ...refs }));
  }, [messages]);
  useEffect(() => {
    const track = () => {
      nearBottom.current =
        document.documentElement.scrollHeight -
          window.innerHeight -
          window.scrollY <
        260;
    };
    window.addEventListener("scroll", track, { passive: true });
    return () => window.removeEventListener("scroll", track);
  }, []);
  useEffect(() => {
    if (busy && nearBottom.current)
      end.current?.scrollIntoView({
        behavior: matchMedia("(prefers-reduced-motion: reduce)").matches
          ? "instant"
          : "smooth",
        block: "end",
      });
  }, [messages, status]);
  async function submit() {
    const prompt = value.trim();
    if (!prompt || busy) return;
    setValue("");
    setLocalError("");
    clearError();
    nearBottom.current = true;
    end.current?.scrollIntoView({ behavior: "smooth", block: "end" });
    try {
      await steeringQueue.current;
      await sendMessage(
        { text: prompt },
        {
          body: {
            id: initial.id,
            pinnedIds: steeringState.current.pinned,
            excludedIds: steeringState.current.excluded,
          },
        },
      );
    } catch (e) {
      setLocalError((e as Error).message);
    }
  }
  function steer(id: string, kind: "pin" | "exclude") {
    // Resolve each operation against the last saved state, not the render that
    // received the click. Two quick pins must both survive the network round trip.
    steeringQueue.current = steeringQueue.current
      .then(async () => {
        const { pinned, excluded } = steeringState.current;
        const nextPinned =
          kind === "pin"
            ? pinned.includes(id)
              ? pinned.filter((x) => x !== id)
              : [...pinned, id]
            : pinned.filter((x) => x !== id);
        const nextExcluded =
          kind === "exclude"
            ? excluded.includes(id)
              ? excluded.filter((x) => x !== id)
              : [...excluded, id]
            : excluded.filter((x) => x !== id);
        await api(`/api/conversations/${initial.id}`, {
          method: "PATCH",
          body: JSON.stringify({
            pinnedIds: nextPinned,
            excludedIds: nextExcluded,
          }),
        });
        steeringState.current = { pinned: nextPinned, excluded: nextExcluded };
        setPinned(nextPinned);
        setExcluded(nextExcluded);
      })
      .catch((e) => setLocalError((e as Error).message));
    return steeringQueue.current;
  }
  async function retryResearch() {
    setLocalError("");
    clearError();
    await steeringQueue.current;
    await regenerate({
      body: {
        id: initial.id,
        pinnedIds: steeringState.current.pinned,
        excludedIds: steeringState.current.excluded,
      },
    }).catch((e) => setLocalError(e.message));
  }
  const references = Object.values(allReferences);
  const inspected = new Map<string, LibraryDetail>();
  for (const message of messages)
    for (const part of message.parts as any[])
      if (part.output?.kind === "inspected" && part.output.reference?.id)
        inspected.set(part.output.reference.id, part.output.reference);
  const knownError = error?.message || localError;
  const missingKey = /key|configured|provider|credential/i.test(knownError);
  const lastMessage = messages[messages.length - 1];
  const pendingUser = lastMessage?.role === "user";
  function exportResearch() {
    const text =
      `# ${initial.title}\n\n` +
      messages
        .map(
          (m) =>
            `## ${m.role === "user" ? "Your direction" : "Research"}\n\n` +
            m.parts
              .map((p: any) =>
                p.type === "text"
                  ? p.text
                  : p.output?.kind === "inspected"
                    ? `Inspected: [${p.output.reference.name}](/styles/${p.output.reference.source}/${p.output.reference.slug})\nEvidence: ${p.output.reference.evidence}`
                    : "",
              )
              .filter(Boolean)
              .join("\n\n"),
        )
        .join("\n\n");
    download(text, `research-${initial.id}.md`);
  }
  return (
    <div className="research-session">
      <header className="research-session-header">
        <div className="research-title">
          <span className="research-status-dot" />
          <span>{initial.title || "Untitled research"}</span>
        </div>
        <button className="pill small" onClick={exportResearch}>
          <Download size={14} />
          Export research
        </button>
      </header>
      <div className="conversation">
        <div className="conversation-intro">
          <span className="eyebrow">Your research</span>
          <p>Follow a direction. Keep what resonates.</p>
        </div>
        {messages.length === 0 && !busy && (
          <Empty title="What are you working on?">
            <p>Describe the experience, mood, or detail you want to explore.</p>
          </Empty>
        )}
        {messages.map((message) => (
          <Message
            key={message.id}
            message={message}
            inspected={inspected}
            onInspect={setInspecting}
            pinned={pinned}
            excluded={excluded}
            onPin={(id) => steer(id, "pin")}
            onExclude={(id) => steer(id, "exclude")}
          />
        ))}
        {busy && (
          <div className="research-working" role="status">
            <span className="thinking-mark">
              <Sparkles size={15} />
            </span>
            <span>
              {status === "submitted"
                ? "Looking through your library…"
                : "Following the details…"}
            </span>
            <span className="thinking-dots">
              <i />
              <i />
              <i />
            </span>
          </div>
        )}
        {knownError && (
          <div className="notice research-error" role="alert">
            <strong>
              {missingKey
                ? "Connect a model to continue research"
                : "Research paused"}
            </strong>
            <p>
              {missingKey
                ? "Your prompt is saved. Add a provider key on the server, then return here and retry. Your library and collections are ready to explore."
                : knownError}
            </p>
            <div className="inline-actions">
              {missingKey && (
                <Link className="pill" href="/settings">
                  Open model settings
                  <ArrowRight size={14} />
                </Link>
              )}
              <button
                className="pill"
                disabled={busy}
                onClick={() => {
                  setLocalError("");
                  clearError();
                  retryResearch();
                }}
              >
                Retry research
              </button>
            </div>
            {missingKey && (
              <details>
                <summary>Server response</summary>
                <p>{knownError}</p>
              </details>
            )}
          </div>
        )}
        {!busy && !knownError && pendingUser && (
          <div className="notice pending-research">
            <strong>Your direction is saved.</strong>
            <p>Continue this research with your connected model.</p>
            <button className="pill" onClick={() => retryResearch()}>
              Continue research
              <ArrowRight size={14} />
            </button>
            <Link className="text-link" href="/settings">
              Model settings
            </Link>
          </div>
        )}
        {!busy && !knownError && lastMessage?.role === "assistant" && (
          <div className="research-retry-row">
            <button className="text-button" onClick={() => retryResearch()}>
              Regenerate response
            </button>
          </div>
        )}
        <div ref={end} />
      </div>
      <div className="session-composer">
        <div className="steering-chips">
          {pinned.map((id) => (
            <button
              className="steering-chip"
              key={id}
              onClick={() => steer(id, "pin")}
              title="Remove pinned direction"
            >
              <Pin size={12} />
              {allReferences[id]?.name || id.split(":")[1]}
              <X size={12} />
            </button>
          ))}
          {excluded.map((id) => (
            <button
              className="steering-chip excluded"
              key={id}
              onClick={() => steer(id, "exclude")}
              title="Restore excluded reference"
            >
              Excluded: {allReferences[id]?.name || id.split(":")[1]}
              <X size={12} />
            </button>
          ))}
        </div>
        <Composer
          value={value}
          onChange={setValue}
          onSubmit={submit}
          busy={busy}
          onStop={stop}
        />
        <p className="composer-hint">
          Enter to send · Shift + Enter for a new line. Pin references to guide
          the next search.
        </p>
      </div>
      <ReferenceInspector
        items={references}
        current={inspecting}
        onChange={setInspecting}
        onClose={() => setInspecting(null)}
        pinnedIds={pinned}
        excludedIds={excluded}
        onPin={(id) => steer(id, "pin")}
        onExclude={(id) => steer(id, "exclude")}
      />
    </div>
  );
}
function Message({
  message,
  inspected,
  onInspect,
  pinned,
  excluded,
  onPin,
  onExclude,
}: {
  message: UIMessage;
  inspected: Map<string, LibraryDetail>;
  onInspect: (item: LibraryItem) => void;
  pinned: string[];
  excluded: string[];
  onPin: (id: string) => void;
  onExclude: (id: string) => void;
}) {
  const user = message.role === "user";
  return (
    <article
      className={`message ${user ? "user-message" : "assistant-message"}`}
    >
      <div className="message-label">
        {user ? "You" : "Studio"}
        {!user && <Sparkles size={12} />}
      </div>
      <div className="message-body">
        {message.parts.map((part: any, index: number) => {
          if (part.type === "text")
            return (
              <div className="prose" key={index}>
                <ReactMarkdown
                  remarkPlugins={[remarkGfm]}
                  components={{
                    a: ({ href, children }) => {
                      const found = Array.from(inspected.values()).find(
                        (d) =>
                          href === `/styles/${d.source}/${d.slug}` ||
                          href === `/library/${d.id}` ||
                          href === d.sourceUrl ||
                          href === `reference:${d.id}` ||
                          href === `#${d.id}`,
                      );
                      return found ? (
                        <button
                          className="inline-citation"
                          onClick={() => onInspect(found)}
                        >
                          {children}
                          <BookOpen size={12} />
                        </button>
                      ) : (
                        <span>{children}</span>
                      );
                    },
                  }}
                >
                  {part.text}
                </ReactMarkdown>
              </div>
            );
          if (part.type.startsWith("tool-") || part.type === "dynamic-tool") {
            const output = part.output;
            if (part.state === "output-error")
              return (
                <div className="tool-progress error-text" key={index}>
                  Couldn’t inspect that source:{" "}
                  {part.errorText || "Try another reference."}
                </div>
              );
            if (!output)
              return (
                <div className="tool-progress" key={index}>
                  <LoaderCircle className="spin" size={14} />
                  {part.type.includes("inspect")
                    ? "Inspecting the reference…"
                    : "Searching the library…"}
                </div>
              );
            if (output.kind === "candidates" || output.items)
              return (
                <details className="tool-activity" key={index}>
                  <summary>
                    <Search size={13} />
                    {output.items?.length || 0} search matches
                    <span className="muted"> · candidates to explore</span>
                  </summary>
                  <section className="research-results">
                    <div className="section-heading">
                      <h3>References to explore</h3>
                      <span className="muted small-text">
                        {output.total ?? output.items.length} found
                      </span>
                    </div>
                    {output.items?.length ? (
                      <div className="research-result-grid">
                        {output.items
                          .filter(
                            (item: LibraryItem) => !excluded.includes(item.id),
                          )
                          .slice(0, 9)
                          .map((item: LibraryItem) => (
                            <div className="research-result" key={item.id}>
                              <ReferenceCard item={item} onOpen={onInspect} />
                              <div className="research-result-actions">
                                <button
                                  className={`pill small ${pinned.includes(item.id) ? "active" : ""}`}
                                  onClick={() => onPin(item.id)}
                                >
                                  <Pin size={12} />
                                  {pinned.includes(item.id) ? "Pinned" : "Pin"}
                                </button>
                                <SaveReference item={item} compact />
                                <button
                                  className="text-button"
                                  onClick={() => onExclude(item.id)}
                                >
                                  Exclude
                                </button>
                              </div>
                            </div>
                          ))}
                      </div>
                    ) : (
                      <p className="muted">
                        No references matched this search. Try another
                        description.
                      </p>
                    )}
                  </section>
                </details>
              );
            if (output.kind === "inspected" && output.reference) {
              const item = output.reference as LibraryDetail;
              return (
                <div className="inspected-reference" key={index}>
                  <button onClick={() => onInspect(item)}>
                    {item.icon ? (
                      <img src={item.icon} alt="" />
                    ) : (
                      <BookOpen size={19} />
                    )}
                    <span>
                      <strong>{item.name}</strong>
                      <small>
                        Inspected ·{" "}
                        {item.evidence === "measured"
                          ? "measured package"
                          : "interpreted reference"}
                        {output.visualEvidence === "text-only"
                          ? " · text evidence only"
                          : ""}
                      </small>
                    </span>
                    <ArrowRight size={15} />
                  </button>
                  <SaveReference item={item} compact />
                </div>
              );
            }
            return null;
          }
          return null;
        })}
      </div>
    </article>
  );
}
