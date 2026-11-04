"use client";
import { BookmarkImport } from "@/components/bookmark-import";
import { AppearanceSettings } from "@/components/appearance";
import { Suspense, useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import {
  BookmarkPlus,
  Check,
  CheckCircle2,
  KeyRound,
  Palette,
  Server,
  Settings2,
  Sparkles,
} from "lucide-react";
import {
  api,
  Combobox,
  CopyButton,
  ErrorState,
  Select,
  Spinner,
  useResource,
} from "@/components/shared";
interface Settings {
  provider: "openai" | "anthropic";
  model: string;
  baseURL: string | null;
  configured: boolean;
  providers: { openai: boolean; anthropic: boolean };
}
const DEFAULT_BASE_URL = {
  openai: "https://api.openai.com/v1",
  anthropic: "https://api.anthropic.com/v1",
} as const;
const DEFAULT_MODEL = {
  openai: "gpt-4.1-mini",
  anthropic: "claude-sonnet-4-5",
} as const;
const tabs = [
  { id: "appearance", label: "Appearance", icon: Palette },
  { id: "import", label: "Import", icon: BookmarkPlus },
  { id: "ai", label: "AI", icon: Sparkles },
] as const;
type SettingsTab = (typeof tabs)[number]["id"];
export function SettingsPage() {
  return (
    <Suspense
      fallback={
        <div className="page settings-page">
          <header className="page-heading">
            <h1>Settings</h1>
          </header>
        </div>
      }
    >
      <SettingsContent />
    </Suspense>
  );
}
function SettingsContent() {
  const params = useSearchParams();
  const requested = params.get("tab");
  const tab: SettingsTab = tabs.some((t) => t.id === requested)
    ? (requested as SettingsTab)
    : "appearance";
  const { data, setData, error, loading } =
    useResource<Settings>("/api/settings");
  const [models, setModels] = useState<string[]>([]);
  const [connection, setConnection] = useState("");
  const [testing, setTesting] = useState(false);
  const [provider, setProvider] = useState<"openai" | "anthropic">("openai"),
    [model, setModel] = useState(""),
    [baseURL, setBaseURL] = useState(""),
    [busy, setBusy] = useState(false),
    [saved, setSaved] = useState(false),
    [localError, setError] = useState("");
  useEffect(() => {
    setModels([]);
    setConnection("");
  }, [provider, baseURL]);
  useEffect(() => {
    if (data) {
      setProvider(data.provider);
      setModel(data.model);
      setBaseURL(data.baseURL || DEFAULT_BASE_URL[data.provider]);
    }
  }, [data?.provider, data?.model, data?.baseURL]);
  function selectTab(id: SettingsTab) {
    const next = new URLSearchParams(window.location.search);
    if (id === "appearance") next.delete("tab");
    else next.set("tab", id);
    const search = next.toString();
    // Native history keeps useSearchParams in sync without a server navigation.
    window.history.replaceState(
      null,
      "",
      `${window.location.pathname}${search ? `?${search}` : ""}`,
    );
  }
  async function save() {
    setBusy(true);
    setError("");
    try {
      const d = await api("/api/settings", {
        method: "PATCH",
        body: JSON.stringify({
          provider,
          model: model.trim(),
          baseURL: baseURL.trim() || null,
        }),
      });
      setData(d);
      setSaved(true);
      setTimeout(() => setSaved(false), 2000);
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy(false);
    }
  }
  return (
    <div className="page settings-page">
      <header className="page-heading">
        <h1>Settings</h1>
        <p className="muted">
          Your research, connected to the model you choose.
        </p>
      </header>
      <div
        className="settings-tabs"
        role="tablist"
        aria-label="Settings sections"
      >
        {tabs.map((choice, index) => (
          <button
            key={choice.id}
            id={`settings-tab-${choice.id}`}
            role="tab"
            type="button"
            aria-selected={tab === choice.id}
            aria-controls={`settings-panel-${choice.id}`}
            tabIndex={tab === choice.id ? 0 : -1}
            onClick={() => selectTab(choice.id)}
            onKeyDown={(event) => {
              const nextIndex =
                event.key === "ArrowRight"
                  ? (index + 1) % tabs.length
                  : event.key === "ArrowLeft"
                    ? (index - 1 + tabs.length) % tabs.length
                    : event.key === "Home"
                      ? 0
                      : event.key === "End"
                        ? tabs.length - 1
                        : -1;
              if (nextIndex >= 0) {
                event.preventDefault();
                selectTab(tabs[nextIndex].id);
                document
                  .getElementById(`settings-tab-${tabs[nextIndex].id}`)
                  ?.focus();
              }
            }}
          >
            <choice.icon size={15} />
            {choice.label}
          </button>
        ))}
      </div>
      <div
        role="tabpanel"
        id={`settings-panel-${tab}`}
        aria-labelledby={`settings-tab-${tab}`}
      >
        {tab === "appearance" && <AppearanceSettings />}
        {tab === "import" && <BookmarkImport />}
        {tab === "ai" &&
          (loading ? (
            <Spinner label="Loading settings…" />
          ) : error ? (
            <ErrorState message={error} />
          ) : (
            data && (
              <>
                <section className="settings-section">
                  <div className="settings-section-label">
                    <Settings2 size={19} />
                    <div>
                      <h2>Research model</h2>
                      <p>
                        The model searches and inspects the same library you
                        browse.
                      </p>
                    </div>
                  </div>
                  <form
                    className="settings-form"
                    onSubmit={(e) => {
                      e.preventDefault();
                      save();
                    }}
                  >
                    <div className="settings-field">
                      <span>Provider</span>
                      <Select
                        label="Provider"
                        disabled={testing}
                        value={provider}
                        onChange={(value) => {
                          const next = value as "openai" | "anthropic";
                          setProvider(next);
                          setBaseURL(DEFAULT_BASE_URL[next]);
                          setModel(DEFAULT_MODEL[next]);
                        }}
                        options={[
                          { value: "openai", label: "OpenAI" },
                          { value: "anthropic", label: "Anthropic" },
                        ]}
                      />
                    </div>
                    <div className="settings-field">
                      <span>Base URL</span>
                      <input
                        disabled={testing}
                        type="url"
                        value={baseURL}
                        onChange={(e) => setBaseURL(e.target.value)}
                        placeholder={DEFAULT_BASE_URL[provider]}
                      />
                      <small>
                        Filled from the provider. Point it at a compatible
                        server or proxy to change it.
                      </small>
                    </div>
                    <div
                      className={`configuration-status ${data.providers?.[provider] ? "ready" : ""}`}
                    >
                      {data.providers?.[provider] ? (
                        <CheckCircle2 size={16} />
                      ) : (
                        <KeyRound size={16} />
                      )}
                      <span>
                        {data.providers?.[provider]
                          ? "Server credential configured"
                          : "Server credential needed"}
                      </span>
                    </div>
                    <button
                      type="button"
                      className="pill"
                      disabled={busy || testing}
                      onClick={async () => {
                        setTesting(true);
                        setConnection("");
                        setError("");
                        try {
                          const result = await api<{ models: string[] }>(
                            "/api/models",
                            {
                              method: "POST",
                              body: JSON.stringify({
                                provider,
                                baseURL: baseURL.trim() || null,
                              }),
                            },
                          );
                          setModels(result.models);
                          setConnection(
                            `Connected. ${result.models.length} models available.`,
                          );
                        } catch (e) {
                          setError((e as Error).message);
                        } finally {
                          setTesting(false);
                        }
                      }}
                    >
                      {testing
                        ? "Testing connection…"
                        : "Test connection & load models"}
                    </button>
                    {connection && <p role="status">{connection}</p>}
                    <div className="settings-field">
                      <span>Model</span>
                      <Combobox
                        label="Model"
                        disabled={testing}
                        options={models}
                        value={model}
                        onChange={setModel}
                        placeholder={DEFAULT_MODEL[provider]}
                        required
                      />
                      <small>
                        Test the connection to browse available models, or type
                        an ID.
                      </small>
                    </div>
                    {localError && (
                      <p className="error-text" role="alert">
                        {localError}
                      </p>
                    )}
                    <button
                      type="submit"
                      className="primary"
                      disabled={busy || testing || !model.trim()}
                    >
                      {saved ? <Check size={15} /> : null}
                      {saved
                        ? "Settings saved"
                        : busy
                          ? "Saving…"
                          : "Save model settings"}
                    </button>
                  </form>
                </section>
                <section className="settings-section">
                  <div className="settings-section-label">
                    <Server size={19} />
                    <div>
                      <h2>Connect your provider</h2>
                      <p>
                        Keys stay on the server. The browser never reads or
                        stores them.
                      </p>
                    </div>
                  </div>
                  <div className="server-instructions">
                    <p>
                      Add your provider’s key to <code>app/.env.local</code>,
                      then restart the app server.
                    </p>
                    <div className="env-example">
                      <pre>
                        <code>
                          {provider === "openai"
                            ? "OPENAI_API_KEY=your-provider-key"
                            : "ANTHROPIC_API_KEY=your-provider-key"}
                        </code>
                      </pre>
                      <CopyButton
                        value={
                          provider === "openai"
                            ? "OPENAI_API_KEY="
                            : "ANTHROPIC_API_KEY="
                        }
                        label="Copy variable"
                      />
                    </div>
                    <p className="muted">
                      Return to your saved research and choose “Retry research”
                      after the server restarts.
                    </p>
                  </div>
                </section>
              </>
            )
          ))}
      </div>
    </div>
  );
}
