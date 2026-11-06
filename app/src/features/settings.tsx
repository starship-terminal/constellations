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
  Settings2,
  Sparkles,
} from "lucide-react";
import {
  api,
  Combobox,
  ErrorState,
  Select,
  Spinner,
  useResource,
} from "@/components/shared";
import { replaceSearch } from "./url-state";
interface Settings {
  provider: "openai" | "anthropic";
  model: string;
  baseURL: string | null;
  configured: boolean;
  providers: { openai: boolean; anthropic: boolean };
  keySources: {
    openai: "stored" | "environment" | null;
    anthropic: "stored" | "environment" | null;
  };
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
    [apiKey, setApiKey] = useState(""),
    [busy, setBusy] = useState(false),
    [saved, setSaved] = useState(false),
    [localError, setError] = useState("");
  useEffect(() => {
    setModels([]);
    setConnection("");
  }, [provider, baseURL, apiKey]);
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
    replaceSearch(next);
  }
  async function save() {
    setBusy(true);
    setError("");
    // A nonempty baseURL means a custom endpoint to the server: it switches
    // OpenAI to Chat Completions and drops screenshot evidence. The provider's
    // own URL is the default, so it saves as null.
    const trimmedURL = baseURL.trim();
    const key = apiKey.trim();
    try {
      const d = await api("/api/settings", {
        method: "PATCH",
        body: JSON.stringify({
          provider,
          model: model.trim(),
          baseURL:
            !trimmedURL || trimmedURL === DEFAULT_BASE_URL[provider]
              ? null
              : trimmedURL,
          ...(key ? { apiKeys: { [provider]: key } } : {}),
        }),
      });
      setData(d);
      setApiKey("");
      setSaved(true);
      setTimeout(() => setSaved(false), 2000);
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy(false);
    }
  }
  async function removeKey() {
    setBusy(true);
    setError("");
    try {
      const d = await api("/api/settings", {
        method: "PATCH",
        body: JSON.stringify({ apiKeys: { [provider]: null } }),
      });
      setData(d);
      setApiKey("");
      setModels([]);
      setConnection("");
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
                          setApiKey("");
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
                        aria-label="Base URL"
                        value={baseURL}
                        onChange={(e) => setBaseURL(e.target.value)}
                        placeholder={DEFAULT_BASE_URL[provider]}
                      />
                      <small>
                        Filled from the provider. Point it at a compatible
                        server or proxy to change it.
                      </small>
                    </div>
                    <div className="settings-field">
                      <span>API key</span>
                      <input
                        disabled={testing}
                        type="password"
                        autoComplete="off"
                        spellCheck={false}
                        aria-label="API key"
                        value={apiKey}
                        onChange={(e) => setApiKey(e.target.value)}
                        placeholder={
                          provider === "openai" ? "sk-…" : "sk-ant-…"
                        }
                      />
                      <small
                        className={`credential-note ${data.keySources?.[provider] ? "ready" : ""}`}
                      >
                        {data.keySources?.[provider] ? (
                          <CheckCircle2 size={13} />
                        ) : (
                          <KeyRound size={13} />
                        )}
                        <span>
                          {data.keySources?.[provider] === "stored"
                            ? "Key saved on this server. Paste a new one to replace it."
                            : data.keySources?.[provider] === "environment"
                              ? "Using the key from the server environment. Paste one here to override it."
                              : "Required for research. Saved on this server and never sent back to the browser."}
                        </span>
                      </small>
                      {data.keySources?.[provider] === "stored" && (
                        <button
                          type="button"
                          className="text-button"
                          disabled={busy || testing}
                          onClick={removeKey}
                        >
                          Remove saved key
                        </button>
                      )}
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
                          const key = apiKey.trim();
                          const result = await api<{ models: string[] }>(
                            "/api/models",
                            {
                              method: "POST",
                              body: JSON.stringify({
                                provider,
                                baseURL: baseURL.trim() || null,
                                ...(key ? { apiKey: key } : {}),
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
              </>
            )
          ))}
      </div>
    </div>
  );
}
