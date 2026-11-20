"use client";
import Link from "next/link";
import homeStyles from "./research-home.module.css";
import { ResearchResults } from "./research-results";
import { HomeBrowse } from "./home-browse";
import { useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { useChat } from "@ai-sdk/react";
import { DefaultChatTransport, type UIMessage } from "ai";
import ReactMarkdown from "react-markdown";
import { prepareResearchRequest } from "./research-transport";
import { MarkdownImageAsText } from "./research-markdown";
import { scrollMotion } from "./capture-viewer-motion";
import { researchDocumentHref } from "./package-detail-data";
import remarkGfm from "remark-gfm";
import {
  ArrowRight,
  ArrowUp,
  BookOpen,
  Binoculars,
  Download,
  Laptop,
  LoaderCircle,
  Monitor,
  Smartphone,
  Sun,
  CornerDownRight,
  Pin,
  Search,
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
  Spinner,
  useResource,
} from "@/components/shared";
import {
  ReferenceCard,
  ReferenceInspector,
  SaveReference,
} from "@/components/reference";
type ResearchMode = "research" | "web" | "ios" | "desktop";
const suggestionGroups = {
  Popular: [
    "Signup with email verification",
    "Product detail pages with ratings and reviews",
    "Command palette examples",
    "Data tables with filters",
    "SaaS landing pages with product screenshots",
    "AI SaaS product landing pages",
  ],
  Inspiration: [
    "Beautiful dashboard designs",
    "Creative portfolio websites",
    "Minimal landing pages",
    "Pricing page inspiration",
    "Finance app interfaces",
    "Editorial layouts",
  ],
  Onboarding: [
    "Welcome screens",
    "Create an account",
    "Set up your workspace",
    "Invite your teammates",
    "Choose a plan",
    "Personalize your profile",
  ],
  Workflows: [
    "Create a new project",
    "Upload and manage files",
    "Filter a data table",
    "Schedule a meeting",
    "Manage your subscription",
    "Share a document",
  ],
};
type SuggestionGroup = keyof typeof suggestionGroups;
const modeChoices = [
  // `short` is the label a phone-width composer has room for.
  {
    id: "research" as const,
    label: "Research mode",
    short: "Research",
    icon: Binoculars,
  },
  { id: "web" as const, label: "Web apps", short: "Web", icon: Monitor },
  { id: "ios" as const, label: "iOS apps", short: "iOS", icon: Smartphone },
  {
    id: "desktop" as const,
    label: "Desktop apps",
    short: "Desktop",
    icon: Laptop,
  },
];
/** The library platform and label each reference mode browses. */
const referenceModes = {
  web: { platform: "web", label: "Web" },
  ios: { platform: "mobile", label: "iOS" },
  desktop: { platform: "desktop", label: "Desktop" },
} as const;
function Composer({
  value,
  onChange,
  onSubmit,
  busy = false,
  onStop,
  hero = false,
  mode = "research",
  onModeChange,
  onShowTips,
}: {
  value: string;
  onChange: (value: string) => void;
  onSubmit: () => void;
  busy?: boolean;
  onStop?: () => void;
  hero?: boolean;
  mode?: ResearchMode;
  onModeChange?: (mode: ResearchMode) => void;
  onShowTips?: () => void;
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
      className={
        hero
          ? `${homeStyles.composer} ${busy ? homeStyles.working : ""}`
          : `research-composer ${busy ? "working" : ""}`
      }
      onSubmit={(e) => {
        e.preventDefault();
        if (!busy && value.trim()) onSubmit();
      }}
    >
      {!hero && (
        <span className={homeStyles.followupIcon}>
          <Search size={16} />
        </span>
      )}
      <textarea
        ref={ref}
        aria-label="Research prompt"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={
          hero
            ? mode === "research"
              ? "Describe a task or ask a question"
              : `Search ${referenceModes[mode].label} app references`
            : "Ask follow up…"
        }
        rows={1}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey && !e.nativeEvent.isComposing) {
            e.preventDefault();
            if (!busy && value.trim()) onSubmit();
          }
        }}
      />
      <div className={hero ? homeStyles.controls : "composer-bottom"}>
        {hero ? (
          <>
            <button
              type="button"
              className={homeStyles.tipsButton}
              onClick={onShowTips}
              aria-label="Show research tips"
            >
              <Sun size={20} />
            </button>
            <div
              className={homeStyles.modes}
              role="group"
              aria-label="Search mode"
            >
              {modeChoices.map((choice) => (
                <button
                  key={choice.id}
                  type="button"
                  aria-pressed={mode === choice.id}
                  className={
                    mode === choice.id ? homeStyles.activeMode : undefined
                  }
                  onClick={() => onModeChange?.(choice.id)}
                  title={
                    choice.id === "research"
                      ? "Research with your connected model"
                      : `Browse saved ${choice.label} in the library`
                  }
                >
                  <choice.icon size={15} />
                  <span className={homeStyles.fullLabel}>{choice.label}</span>
                  <span className={homeStyles.shortLabel}>{choice.short}</span>
                </button>
              ))}
            </div>
          </>
        ) : (
          <span>
            <Search size={14} />
            Grounded in your library
          </span>
        )}
        <div className="spacer" />
        {busy && onStop ? (
          <button
            type="button"
            className={hero ? homeStyles.submit : "composer-submit"}
            onClick={onStop}
            aria-label="Stop research"
          >
            <Square size={15} fill="currentColor" />
          </button>
        ) : (
          <button
            className={hero ? homeStyles.submit : "composer-submit"}
            type="submit"
            disabled={busy || !value.trim()}
            aria-label={
              hero && mode !== "research"
                ? "Search app references"
                : "Send research prompt"
            }
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
    [inspecting, setInspecting] = useState<LibraryItem | null>(null),
    [mode, setMode] = useState<ResearchMode>("research"),
    [coachVisible, setCoachVisible] = useState(true),
    [suggestionGroup, setSuggestionGroup] =
      useState<SuggestionGroup>("Popular");
  const { data } = useResource<{ items: LibraryItem[]; total: number }>(
    mode === "research"
      ? "/api/library?limit=8&source=systems"
      : `/api/library?limit=8&platform=${referenceModes[mode].platform}`,
  );
  const items = data?.items || [];
  async function begin() {
    if (!prompt.trim() || busy) return;
    if (mode !== "research") {
      const params = new URLSearchParams({
        platform: referenceModes[mode].platform,
        q: prompt.trim(),
      });
      router.push(`/library?${params}`);
      return;
    }
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
  function chooseSuggestion(suggestion: string) {
    setPrompt(suggestion);
    document
      .querySelector<HTMLTextAreaElement>(
        'textarea[aria-label="Research prompt"]',
      )
      ?.focus();
  }
  return (
    <div className={homeStyles.home}>
      <section className={homeStyles.hero}>
        <h1>What are you designing next?</h1>
        <p className={homeStyles.description}>
          Real product screens, styles, and patterns to help you
          <br className={homeStyles.desktopBreak} /> make better design
          decisions.
        </p>
        <div className={homeStyles.research}>
          {coachVisible && (
            <aside className={homeStyles.coach} aria-label="Research tips">
              <strong>
                {mode === "research"
                  ? "Meet research mode"
                  : `Browse ${referenceModes[mode].label} app references`}
              </strong>
              <p>
                {mode === "research"
                  ? "Describe your task, get analysis, references, and reasoning back."
                  : "Search your saved library by product, screen, or design detail."}
              </p>
              <button
                className={homeStyles.dismissCoach}
                onClick={() => setCoachVisible(false)}
                aria-label="Dismiss research tips"
              >
                <X size={17} />
              </button>
            </aside>
          )}
          <Composer
            value={prompt}
            onChange={setPrompt}
            onSubmit={begin}
            busy={busy}
            hero
            mode={mode}
            onModeChange={setMode}
            onShowTips={() => setCoachVisible((v) => !v)}
          />
          {error && (
            <p className={`error-text ${homeStyles.error}`} role="alert">
              {error}
            </p>
          )}
          <div
            className={homeStyles.suggestionTabs}
            role="tablist"
            aria-label="Suggested prompts"
          >
            {(Object.keys(suggestionGroups) as SuggestionGroup[]).map(
              (group, index, groups) => (
                <button
                  key={group}
                  id={`suggestion-tab-${group}`}
                  role="tab"
                  type="button"
                  aria-selected={suggestionGroup === group}
                  aria-controls="research-suggestions"
                  tabIndex={suggestionGroup === group ? 0 : -1}
                  className={
                    suggestionGroup === group ? homeStyles.activeTab : undefined
                  }
                  onClick={() => setSuggestionGroup(group)}
                  onKeyDown={(event) => {
                    const nextIndex =
                      event.key === "ArrowRight"
                        ? (index + 1) % groups.length
                        : event.key === "ArrowLeft"
                          ? (index - 1 + groups.length) % groups.length
                          : event.key === "Home"
                            ? 0
                            : event.key === "End"
                              ? groups.length - 1
                              : -1;
                    if (nextIndex >= 0) {
                      event.preventDefault();
                      setSuggestionGroup(groups[nextIndex]);
                      document
                        .getElementById(`suggestion-tab-${groups[nextIndex]}`)
                        ?.focus();
                    }
                  }}
                >
                  {group}
                </button>
              ),
            )}
          </div>
          <div
            className={homeStyles.suggestions}
            id="research-suggestions"
            role="tabpanel"
            aria-labelledby={`suggestion-tab-${suggestionGroup}`}
          >
            {suggestionGroups[suggestionGroup].map((suggestion) => (
              <button
                type="button"
                key={suggestion}
                onClick={() => chooseSuggestion(suggestion)}
              >
                <CornerDownRight size={20} />
                <span>{suggestion}</span>
              </button>
            ))}
          </div>
        </div>
      </section>
      <HomeBrowse
        platform={
          mode === "research" ? undefined : referenceModes[mode].platform
        }
      />
      <section className={homeStyles.gallery}>
        <div className={homeStyles.galleryHeading}>
          <h2>
            {mode === "research"
              ? "Sites"
              : `${referenceModes[mode].label} app references`}
          </h2>
          <Link
            href={
              mode === "research"
                ? "/library"
                : `/library?platform=${referenceModes[mode].platform}`
            }
          >
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

interface Conversation {
  id: string;
  title: string;
  messages: UIMessage[];
  pinnedIds: string[];
  excludedIds: string[];
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
    <ResearchConversation key={id} initial={data} />
  ) : null;
}
function ResearchConversation({ initial }: { initial: Conversation }) {
  const [value, setValue] = useState(""),
    [pinned, setPinned] = useState(initial.pinnedIds || []),
    [excluded, setExcluded] = useState(initial.excludedIds || []),
    [inspecting, setInspecting] = useState<LibraryItem | null>(null),
    [localError, setLocalError] = useState(""),
    [modelConfigured, setModelConfigured] = useState<boolean | null>(null),
    [allReferences, setAllReferences] = useState<Record<string, LibraryItem>>(
      {},
    );
  const end = useRef<HTMLDivElement>(null),
    started = useRef(false),
    continued = useRef(false),
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
      transport: new DefaultChatTransport({
        api: "/api/research",
        prepareSendMessagesRequest: prepareResearchRequest,
      }),
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
    // Re-check on return visits: a key added since the last check lets the
    // saved direction continue without a manual retry.
    let alive = true;
    const check = () =>
      api<{ configured?: boolean }>("/api/settings")
        .then((d) => {
          if (alive) setModelConfigured(d?.configured === true);
        })
        .catch(() => {
          if (alive) setModelConfigured(false);
        });
    check();
    const wake = () => {
      if (!document.hidden) check();
    };
    document.addEventListener("visibilitychange", wake);
    window.addEventListener("focus", wake);
    return () => {
      alive = false;
      document.removeEventListener("visibilitychange", wake);
      window.removeEventListener("focus", wake);
    };
  }, []);
  useEffect(() => {
    if (busy && nearBottom.current)
      end.current?.scrollIntoView({ behavior: scrollMotion(), block: "end" });
  }, [messages, status]);
  async function submit() {
    const prompt = value.trim();
    if (!prompt || busy) return;
    setValue("");
    setLocalError("");
    clearError();
    nearBottom.current = true;
    end.current?.scrollIntoView({ behavior: scrollMotion(), block: "end" });
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
        // The save moved updatedAt, which orders the sidebar history.
        window.dispatchEvent(new Event("research-history"));
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
  useEffect(() => {
    if (
      continued.current ||
      started.current ||
      modelConfigured !== true ||
      busy ||
      knownError ||
      !pendingUser
    )
      return;
    continued.current = true;
    retryResearch();
  }, [modelConfigured, busy, knownError, pendingUser]);
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
    <div className={`research-session ${homeStyles.session}`}>
      <header className={`research-session-header ${homeStyles.sessionHeader}`}>
        <div className={homeStyles.sessionTopBar}>
          <div className={`research-title ${homeStyles.sessionTitle}`}>
            <span>{initial.title || "Untitled research"}</span>
          </div>
          <button
            className="icon-button"
            onClick={exportResearch}
            aria-label="Export research"
            title="Export research"
          >
            <Download size={17} />
          </button>
          <Link
            href="/"
            className="icon-button"
            aria-label="Close research"
            title="New research"
          >
            <X size={17} />
          </Link>
        </div>
        <nav
          className={homeStyles.sessionModes}
          aria-label="Research and reference views"
        >
          <span aria-current="page">
            <Binoculars size={16} />
            Research mode
          </span>
          <Link href="/library?platform=web">
            <Monitor size={16} />
            Web apps
          </Link>
          <Link href="/library?platform=mobile">
            <Smartphone size={16} />
            iOS apps
          </Link>
          <Link href="/library?platform=desktop">
            <Laptop size={16} />
            Desktop apps
          </Link>
        </nav>
      </header>
      <div className="conversation">
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
                ? "Your prompt is saved. Add a provider key in model settings, then return here and retry. Your library and collections are ready to explore."
                : knownError}
            </p>
            <div className="inline-actions">
              {missingKey && (
                <Link className="pill" href="/settings?tab=ai">
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
        {!busy && !knownError && pendingUser && modelConfigured !== null && (
          <div className="notice pending-research">
            <strong>Your direction is saved.</strong>
            <p>
              {modelConfigured
                ? "Continue this research with your connected model."
                : "Connect a model in settings to continue this research."}
            </p>
            {modelConfigured ? (
              <button className="pill" onClick={() => retryResearch()}>
                Continue research
                <ArrowRight size={14} />
              </button>
            ) : (
              <Link className="pill" href="/settings?tab=ai">
                Model settings
                <ArrowRight size={14} />
              </Link>
            )}
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
        {!busy && !knownError && lastMessage?.role === "assistant" && (
          <div
            className={homeStyles.followupSuggestions}
            aria-label="Suggested follow-up prompts"
          >
            {[
              "Compare the strongest references",
              "Find similar screens",
              "Explain which details I should borrow",
            ].map((prompt) => (
              <button
                key={prompt}
                onClick={() => {
                  setValue(prompt);
                  document
                    .querySelector<HTMLTextAreaElement>(
                      'textarea[aria-label="Research prompt"]',
                    )
                    ?.focus();
                }}
              >
                <CornerDownRight size={14} />
                {prompt}
              </button>
            ))}
          </div>
        )}
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
        {user ? "You" : "Research insights"}
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
                    img: MarkdownImageAsText,
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
            if (output.referenceId && excluded.includes(output.referenceId))
              return null;
            if (output.kind === "handoff-prompt")
              return (
                <details className="tool-activity" key={index} open>
                  <summary>
                    <BookOpen size={13} />
                    {output.title || "Coding-agent handoff"}
                  </summary>
                  <pre
                    style={{
                      whiteSpace: "pre-wrap",
                      fontSize: 12,
                      padding: 16,
                    }}
                  >
                    {output.prompt}
                  </pre>
                  <CopyButton value={output.prompt} label="Copy agent prompt" />
                </details>
              );
            if (output.kind === "package-documents")
              return (
                <details className="tool-activity" key={index}>
                  <summary>
                    <BookOpen size={13} />
                    {output.documents?.length || 0} package documents
                  </summary>
                  <div className="inline-actions">
                    {output.documents?.map(
                      (document: { path: string; url: string }) => (
                        <Link
                          key={document.path}
                          className="pill small"
                          href={researchDocumentHref(
                            output.referenceId,
                            document.path,
                            document.url,
                          )}
                        >
                          {document.path}
                        </Link>
                      ),
                    )}
                  </div>
                </details>
              );
            if (output.kind === "package-document")
              return (
                <details className="tool-activity" key={index}>
                  <summary>
                    <BookOpen size={13} />
                    Read {output.path}
                    {output.truncated ? " (excerpt)" : ""}
                  </summary>
                  <p>
                    <Link
                      href={researchDocumentHref(
                        output.referenceId,
                        output.path,
                        output.url,
                      )}
                    >
                      Open full document
                    </Link>
                  </p>
                  <pre
                    style={{
                      whiteSpace: "pre-wrap",
                      fontSize: 12,
                      padding: 16,
                      maxHeight: 360,
                      overflow: "auto",
                    }}
                  >
                    {output.text}
                  </pre>
                </details>
              );
            if (output.kind === "package-tokens")
              return (
                <details className="tool-activity" key={index}>
                  <summary>
                    <BookOpen size={13} />
                    {output.group
                      ? `Read token group: ${output.group}`
                      : "Available token groups"}
                  </summary>
                  <pre
                    style={{
                      whiteSpace: "pre-wrap",
                      fontSize: 12,
                      padding: 16,
                      maxHeight: 360,
                      overflow: "auto",
                    }}
                  >
                    {JSON.stringify(output.tokens || output.groups, null, 2)}
                  </pre>
                  {output.truncated && (
                    <p className="muted">
                      More values are available in this group.
                    </p>
                  )}
                </details>
              );
            if (
              output.kind === "reference-media" ||
              output.kind === "viewed-media"
            ) {
              const media =
                output.kind === "viewed-media"
                  ? [output.media]
                  : output.media || [];
              return (
                <details className="tool-activity" key={index}>
                  <summary>
                    <BookOpen size={13} />
                    {output.kind === "viewed-media"
                      ? output.visualEvidence === "image-supplied"
                        ? "Captured image inspected"
                        : "Media available, text evidence only"
                      : `${media.length} captured media files`}
                  </summary>
                  <div className="research-result-grid">
                    {media.map(
                      (item: {
                        id: string;
                        url: string;
                        name: string;
                        type: string;
                      }) => (
                        <a
                          key={item.id}
                          href={item.url}
                          target="_blank"
                          rel="noreferrer"
                          className="research-result"
                        >
                          {item.type === "image" ? (
                            <img
                              src={item.url}
                              alt={item.name}
                              loading="lazy"
                              decoding="async"
                              style={{
                                width: "100%",
                                maxHeight: 220,
                                objectFit: "contain",
                              }}
                            />
                          ) : (
                            <span>{item.name} · video</span>
                          )}
                          <small>{item.name}</small>
                        </a>
                      ),
                    )}
                  </div>
                </details>
              );
            }
            if (output.kind === "candidates" || output.items)
              return (
                <ResearchResults
                  key={index}
                  items={output.items || []}
                  total={output.total ?? output.items?.length ?? 0}
                  query={part.input?.query}
                  source={part.input?.source}
                  platform={part.input?.platform}
                  theme={part.input?.theme}
                  excluded={excluded}
                  pinned={pinned}
                  onInspect={onInspect}
                  onPin={onPin}
                  onExclude={onExclude}
                />
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
