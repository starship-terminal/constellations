"use client";

// Settings: the chat's model provider (held by the server: /api/provider),
// theme and sidebar prefs ("ds-theme" / "ds-nav"), saved media ("ds-saved"),
// and the data summary the server page passes in.

import { useCallback, useEffect, useRef, useState } from "react";
import { useLightbox } from "@/components/Lightbox";
import { PROVIDER_NOTICE_KEY, readSavedPaths } from "@/components/storage";
import { announceProviderChange, PROVIDER_EVENT } from "@/components/Chat";
import { setCollapsed, setTheme, usePrefs, type Theme } from "@/components/prefs";
import { agentSnippets } from "@/lib/agent-snippets";
import { SnippetCopyButton } from "@/components/CopyButton";
import { afterSave, EMPTY_FORM, latestOnly, withField, type ProviderForm } from "@/components/provider-form";

export interface SettingsStats {
  /** The checkout's folder name, never its absolute path. */
  repo: string;
  systems: number | null;
  refero: number | null;
  audit: string | null;
}

/** The form (see provider-form.ts). */
type Cfg = ProviderForm;

type KeySource = "saved" | "env" | "none";

interface ProviderState {
  source: KeySource;
  configured: boolean;
  provider: Partial<Record<keyof Cfg, string>> | null;
  envAvailable: boolean;
  error?: string;
}

const EMPTY: Cfg = EMPTY_FORM;

const SOURCE_LABEL: Record<KeySource, string> = {
  saved: "Saved on the server",
  env: "From the server environment",
  none: "No key",
};

const baseName = (p: string) => {
  try {
    return decodeURIComponent(p.split("/").pop() || p);
  } catch {
    return p;
  }
};

interface ModelHit {
  id: string;
  label: string;
}

const fromState = (s: ProviderState | null): Cfg => ({ ...EMPTY, ...(s?.source === "saved" ? s.provider : null), api_key: "" });

const postJson = async (url: string, method: string, body?: unknown) => {
  const r = await fetch(url, {
    method,
    headers: body === undefined ? undefined : { "content-type": "application/json" },
    body: body === undefined ? undefined : JSON.stringify(body),
  });
  return (await r.json().catch(() => null)) as Record<string, unknown> | null;
};

function ProviderPanel() {
  const [cfg, setCfgState] = useState<Cfg>(EMPTY);
  const [state, setState] = useState<ProviderState | null>(null);
  const [models, setModels] = useState<ModelHit[]>([]);
  const [status, setStatus] = useState("");
  const [warn, setWarn] = useState(false);
  const [busy, setBusy] = useState(false);
  const [notice, setNotice] = useState("");
  // Set by any edit to the form, a model chip included. A state reply that
  // lands after the reader has typed (a slow first load, another tab's
  // change) updates the badge but never overwrites the fields.
  const edited = useRef(false);
  // The form as it is now, for replies that land later than the render
  // that sent them. Every change goes through setCfg.
  const current = useRef<Cfg>(EMPTY);
  const setCfg = useCallback((next: Cfg) => {
    current.current = next;
    setCfgState(next);
  }, []);
  const edit = (next: Cfg) => {
    edited.current = true;
    setCfg(next);
  };
  // State replies: only the newest request's reply is used, and a save or
  // remove reply outranks any read still in flight.
  const reads = useRef(latestOnly()).current;

  const load = useCallback(
    async (fill: boolean) => {
      const n = reads.begin();
      try {
        const d = (await postJson("/api/provider", "GET")) as unknown as ProviderState | null;
        if (!reads.isLatest(n)) return;
        if (!d || typeof d.source !== "string") throw new Error();
        setState(d);
        if (fill && !edited.current) setCfg(fromState(d));
        if (d.error) {
          setWarn(true);
          setStatus(d.error);
        }
      } catch {
        if (!reads.isLatest(n)) return;
        setState(null);
        setWarn(true);
        setStatus("No answer from the server.");
      }
    },
    [reads, setCfg],
  );

  useEffect(() => {
    load(true);
    const readNotice = () => {
      try {
        setNotice(sessionStorage.getItem(PROVIDER_NOTICE_KEY) || "");
      } catch {}
    };
    readNotice();
    // The one-time move of a browser-stored key may finish after this page loads.
    const onChange = () => {
      readNotice();
      load(true);
    };
    window.addEventListener(PROVIDER_EVENT, onChange);
    return () => window.removeEventListener(PROVIDER_EVENT, onChange);
  }, [load]);

  const onField =
    (k: keyof Cfg) => (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) =>
      edit(withField(current.current, k, e.target.value));

  const body = () => {
    const out: Record<string, string> = { api: cfg.api, base_url: cfg.base_url.trim(), model: cfg.model.trim() };
    if (cfg.key_header.trim()) out.key_header = cfg.key_header.trim();
    if (cfg.models_url.trim()) out.models_url = cfg.models_url.trim();
    if (cfg.name.trim()) out.name = cfg.name.trim();
    if (cfg.api_key.trim()) out.api_key = cfg.api_key.trim();
    return out;
  };

  const test = async () => {
    if (!cfg.api_key.trim() && state?.source === "none") {
      setWarn(true);
      setStatus("Enter an API key first.");
      return;
    }
    setBusy(true);
    setWarn(false);
    setStatus("Testing…");
    try {
      const d = await postJson("/api/provider/test", "POST", body());
      if (d?.ok) {
        const list = Array.isArray(d.models) ? (d.models as ModelHit[]) : [];
        setModels(list);
        setStatus(list.length ? `Connected: ${list.length} models found.` : `Connected. ${d.note || "Type the model name."}`);
      } else {
        setWarn(true);
        setStatus(typeof d?.error === "string" ? d.error : "Test failed.");
      }
    } catch {
      setWarn(true);
      setStatus("No answer from the server.");
    }
    setBusy(false);
  };

  const save = async () => {
    if (!cfg.model.trim()) {
      setWarn(true);
      setStatus("Pick a model before saving.");
      return;
    }
    if (!cfg.api_key.trim() && state?.source !== "saved") {
      setWarn(true);
      setStatus("Enter an API key to save.");
      return;
    }
    setBusy(true);
    setWarn(false);
    setStatus(cfg.api_key.trim() ? "Testing the key, then saving…" : "Saving…");
    const sent = current.current;
    try {
      const d = await postJson("/api/provider", "POST", body());
      if (d?.ok) {
        if (Array.isArray(d.models) && d.models.length) setModels(d.models as ModelHit[]);
        reads.begin();
        setState(d as unknown as ProviderState);
        // The key field empties (the server has it now and never returns
        // it), unless the reader changed the form while this was in flight.
        const after = afterSave(current.current, sent);
        setCfg(after.form);
        if (after.settled) edited.current = false;
        setStatus(
          `Saved on the server: ${sent.name.trim() || sent.api} · ${sent.model.trim()}` +
            (d.verified === false ? ". This endpoint has no model list, so the key itself was not checked." : "") +
            (after.settled ? "" : ". The form has changed since; save again to use the changes."),
        );
        announceProviderChange();
      } else {
        setWarn(true);
        setStatus(`Not saved. ${typeof d?.error === "string" ? d.error : "The server refused it."}`);
      }
    } catch {
      setWarn(true);
      setStatus("No answer from the server.");
    }
    setBusy(false);
  };

  const remove = async () => {
    setBusy(true);
    try {
      const d = await postJson("/api/provider", "DELETE");
      if (d?.ok) {
        reads.begin();
        setState(d as unknown as ProviderState);
        setCfg(EMPTY);
        edited.current = false;
        setModels([]);
        setWarn(false);
        setStatus(
          (d as unknown as ProviderState).source === "env"
            ? "Removed the saved key. The chat now uses the server's environment key."
            : "Removed the saved key.",
        );
        announceProviderChange();
      } else {
        setWarn(true);
        setStatus(typeof d?.error === "string" ? d.error : "Could not remove the saved key.");
      }
    } catch {
      setWarn(true);
      setStatus("No answer from the server.");
    }
    setBusy(false);
  };

  const source = state?.source ?? "none";
  const using = state?.provider;

  return (
    <>
      <p className="pref-help">The chat&rsquo;s brain: which wire format, endpoint, key and model it talks to.</p>
      <div className="pf-source" data-source={state ? source : undefined}>
        <span className="tag pf-badge">{state ? SOURCE_LABEL[source] : "Checking…"}</span>
        <span className="pf-using">
          {state?.error
            ? "The saved provider cannot be used."
            : using
              ? `${using.name || using.api} · ${using.model}`
              : state
                ? "The chat needs a key before it can answer."
                : ""}
        </span>
      </div>
      {notice ? (
        <p className="pf-notice" role="note">
          {notice}
        </p>
      ) : null}
      <div className="pf-grid">
        <label className="pf-field">
          <span>Label</span>
          <input value={cfg.name} onChange={onField("name")} autoComplete="off" spellCheck={false} placeholder="anthropic" />
        </label>
        <label className="pf-field">
          <span>API</span>
          <select className="st-sel" value={cfg.api} onChange={onField("api")}>
            <option value="anthropic">anthropic</option>
            <option value="openai">openai (OpenAI-compatible)</option>
          </select>
        </label>
        <label className="pf-field">
          <span>Base URL</span>
          <input
            value={cfg.base_url}
            onChange={onField("base_url")}
            type="url"
            autoComplete="off"
            spellCheck={false}
            placeholder={cfg.api === "anthropic" ? "https://api.anthropic.com" : "https://api.openai.com/v1"}
          />
        </label>
        <label className="pf-field">
          <span>API key</span>
          <input
            value={cfg.api_key}
            onChange={onField("api_key")}
            type="password"
            autoComplete="off"
            spellCheck={false}
            placeholder={source === "saved" ? "Leave blank to keep the saved key" : "sk-…"}
          />
        </label>
        <label className="pf-field">
          <span>Key header</span>
          <input
            value={cfg.key_header}
            onChange={onField("key_header")}
            autoComplete="off"
            spellCheck={false}
            placeholder={cfg.api === "anthropic" ? "x-api-key" : "authorization"}
          />
        </label>
        <label className="pf-field">
          <span>Model</span>
          <input
            value={cfg.model}
            onChange={onField("model")}
            list="st-models"
            autoComplete="off"
            spellCheck={false}
            placeholder="claude-sonnet-4-5"
          />
          <datalist id="st-models">
            {models.map((m) => (
              <option key={m.id} value={m.id}>
                {m.label}
              </option>
            ))}
          </datalist>
        </label>
      </div>
      {models.length ? (
        <div className="pf-chips">
          {models.slice(0, 12).map((m) => (
            <button
              key={m.id}
              type="button"
              className="pf-chip"
              aria-pressed={cfg.model.trim() === m.id}
              onClick={() => edit(withField(current.current, "model", m.id))}
            >
              {m.label}
            </button>
          ))}
        </div>
      ) : null}
      <p className="pf-status" role="status" data-warn={warn ? "1" : undefined}>
        {status}
      </p>
      <div className="pf-actions">
        <button className="btn" type="button" onClick={test} disabled={busy}>
          Test
        </button>
        <button className="btn primary" type="button" onClick={save} disabled={busy}>
          {source === "saved" && cfg.api_key.trim() ? "Replace key" : "Save"}
        </button>
        {source === "saved" ? (
          <button className="btn" type="button" onClick={remove} disabled={busy}>
            Remove
          </button>
        ) : null}
      </div>
      <p className="pref-note">
        The key goes to this app&rsquo;s server once. The server tests it, keeps it in its own config folder and never
        sends it back; this browser does not store it. A saved key only goes to the endpoint it was saved with, so
        changing the API, base URL or key header needs the key again.
        {state?.envAvailable && source === "saved"
          ? " The server also has ANTHROPIC_API_KEY set; it applies again once the saved key is removed."
          : ""}
      </p>
    </>
  );
}

export function Settings({ stats }: { stats: SettingsStats }) {
  const lb = useLightbox();
  const { theme, collapsed } = usePrefs();
  const [saved, setSaved] = useState<string[]>([]);
  const [origin, setOrigin] = useState("");

  useEffect(() => {
    setOrigin(window.location.origin);
    setSaved(readSavedPaths());
  }, []);

  const applyTheme = (t: Theme) => setTheme(t);
  const applyNav = (c: boolean) => setCollapsed(c);

  const clearSaved = () => {
    try {
      localStorage.removeItem("ds-saved");
    } catch {}
    setSaved([]);
  };

  return (
    <div className="page">
      <div className="g-hero">
        <h1>Settings</h1>
        <p className="sub">Preferences are saved in this browser and apply to every page of the app; the model provider is saved on the server.</p>
      </div>

      <div className="prefs">
        <fieldset className="pref" id="model-provider">
          <legend className="pref-name">Model provider</legend>
          <ProviderPanel />
        </fieldset>

        <fieldset className="pref">
          <legend className="pref-name">Preferences</legend>
          <p className="pref-help">How the app looks and how much room the sidebar takes.</p>
          <div className="pf-grid">
            <div className="pf-field">
              <span>Theme</span>
              <div className="seg" role="group" aria-label="Theme">
                <button type="button" aria-pressed={theme === "system"} onClick={() => applyTheme("system")}>
                  System
                </button>
                <button type="button" aria-pressed={theme === "dark"} onClick={() => applyTheme("dark")}>
                  Dark
                </button>
                <button type="button" aria-pressed={theme === "light"} onClick={() => applyTheme("light")}>
                  Light
                </button>
              </div>
            </div>
            <div className="pf-field">
              <span>Sidebar</span>
              <div className="seg" role="group" aria-label="Sidebar">
                <button type="button" aria-pressed={!collapsed} onClick={() => applyNav(false)}>
                  Expanded
                </button>
                <button type="button" aria-pressed={collapsed} onClick={() => applyNav(true)}>
                  Collapsed
                </button>
              </div>
            </div>
          </div>
        </fieldset>

        <fieldset className="pref">
          <legend className="pref-name">For agents</legend>
          <p className="pref-help">
            Install the ds CLI or point a coding agent at the remote MCP endpoint — both read this
            library over the same /api/mcp transport, read-only.
          </p>
          <dl className="meta snippets">
            {agentSnippets(origin).map((s) => (
              <div className="snip-row" key={s.label}>
                <dt>{s.label}</dt>
                <dd>
                  <code>{s.text}</code>
                  <SnippetCopyButton text={s.text} what={`${s.label} setup`} />
                </dd>
              </div>
            ))}
          </dl>
          <p className="pref-note">
            Any harness that takes a remote (streamable-HTTP) MCP URL works. On a machine with the
            repo checkout, <code>python3 server/mcp.py</code> is the stdio variant.
          </p>
        </fieldset>

        <fieldset className="pref">
          <legend className="pref-name">Saved media</legend>
          <p className="pref-help">Screenshots saved from the lightbox, kept in this browser.</p>
          {saved.length ? (
            <>
              <div className="shots">
                {saved.map((p, i) => (
                  <button
                    key={p}
                    type="button"
                    className="shot"
                    onClick={() =>
                      lb.open({
                        items: saved.map((x) => ({ path: x, name: baseName(x) })),
                        index: i,
                        opts: { onSave: () => setSaved(readSavedPaths()) },
                      })
                    }
                  >
                    <span className="frame">
                      {/* eslint-disable-next-line @next/next/no-img-element */}
                      <img src={p} alt="" loading="lazy" />
                    </span>
                    <span>{baseName(p)}</span>
                  </button>
                ))}
              </div>
              <div className="pf-actions st-actions">
                <button className="btn" type="button" onClick={clearSaved}>
                  Clear all
                </button>
              </div>
            </>
          ) : (
            <p className="faint">Nothing saved yet. The lightbox&rsquo;s Save button puts screenshots here.</p>
          )}
        </fieldset>

        <fieldset className="pref">
          <legend className="pref-name">Data</legend>
          <p className="pref-help">What the app is reading from disk.</p>
          <dl className="meta">
            <dt>Repo</dt>
            <dd>
              <code>{stats.repo}</code>
            </dd>
            <dt>Packages</dt>
            <dd>{stats.systems?.toLocaleString() ?? "n/a"}</dd>
            <dt>Refero styles</dt>
            <dd>{stats.refero?.toLocaleString() ?? "n/a"}</dd>
            <dt>Latest audit</dt>
            <dd>{stats.audit ?? "n/a"}</dd>
          </dl>
        </fieldset>
      </div>
    </div>
  );
}
