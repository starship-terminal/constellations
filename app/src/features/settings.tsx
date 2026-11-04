"use client";
import Link from "next/link";
import { useEffect, useState } from "react";
import {
  ArrowRight,
  Check,
  CheckCircle2,
  KeyRound,
  Server,
  Settings2,
} from "lucide-react";
import {
  api,
  CopyButton,
  ErrorState,
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
export function SettingsPage() {
  const { data, setData, error, loading } =
    useResource<Settings>("/api/settings");
  const [provider, setProvider] = useState<"openai" | "anthropic">("openai"),
    [model, setModel] = useState(""),
    [baseURL, setBaseURL] = useState(""),
    [busy, setBusy] = useState(false),
    [saved, setSaved] = useState(false),
    [localError, setError] = useState("");
  useEffect(() => {
    if (data) {
      setProvider(data.provider);
      setModel(data.model);
      setBaseURL(data.baseURL || "");
    }
  }, [data?.provider, data?.model, data?.baseURL]);
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
        <div className="eyebrow">Make yourself at home</div>
        <h1>A few considered settings.</h1>
        <p className="muted">
          Your research, connected to the model you choose.
        </p>
      </header>
      {loading ? (
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
                    The model searches and inspects the same library you browse.
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
                <label>
                  Provider
                  <select
                    value={provider}
                    onChange={(e) => {
                      const v = e.target.value as "openai" | "anthropic";
                      setProvider(v);
                      setBaseURL("");
                      setModel(
                        v === "openai" ? "gpt-4.1-mini" : "claude-sonnet-4-5",
                      );
                    }}
                  >
                    <option value="openai">OpenAI</option>
                    <option value="anthropic">Anthropic</option>
                  </select>
                </label>
                <label>
                  Model
                  <input
                    value={model}
                    onChange={(e) => setModel(e.target.value)}
                    placeholder={
                      provider === "openai"
                        ? "gpt-4.1-mini"
                        : "claude-sonnet-4-5"
                    }
                    required
                  />
                  <small>Use a model available to your provider account.</small>
                </label>
                <label>
                  Custom base URL <span className="muted">(optional)</span>
                  <input
                    type="url"
                    value={baseURL}
                    onChange={(e) => setBaseURL(e.target.value)}
                    placeholder="Use the provider’s default endpoint"
                  />
                  <small>
                    For a compatible server or proxy. Leave blank for the
                    default.
                  </small>
                </label>
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
                {localError && (
                  <p className="error-text" role="alert">
                    {localError}
                  </p>
                )}
                <button
                  type="submit"
                  className="primary"
                  disabled={busy || !model.trim()}
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
                    Keys stay on the server. The browser never reads or stores
                    them.
                  </p>
                </div>
              </div>
              <div className="server-instructions">
                <p>
                  Add your provider’s key to <code>app/.env.local</code>, then
                  restart the app server.
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
            <section className="settings-section">
              <div className="settings-section-label">
                <BookIcon />
                <div>
                  <h2>Your library is always here</h2>
                  <p>
                    Browse, compare, save references, and write collection notes
                    with no model connected.
                  </p>
                </div>
              </div>
              <div className="inline-actions">
                <Link className="pill" href="/library">
                  Explore references
                  <ArrowRight size={14} />
                </Link>
                <Link className="pill" href="/collections">
                  Open collections
                  <ArrowRight size={14} />
                </Link>
              </div>
            </section>
          </>
        )
      )}
    </div>
  );
}
function BookIcon() {
  return (
    <svg
      width="19"
      height="19"
      viewBox="0 0 20 20"
      fill="none"
      aria-hidden="true"
    >
      <path
        d="M3 4h5a3 3 0 0 1 3 3v10a3 3 0 0 0-3-2H3V4Zm14 0h-3a3 3 0 0 0-3 3v10a3 3 0 0 1 3-2h3V4Z"
        stroke="currentColor"
        strokeWidth="1.3"
      />
    </svg>
  );
}
