"use client";

// Settings: the chat's model provider (localStorage "ds-provider"), theme and
// sidebar prefs ("ds-theme" / "ds-nav"), saved media ("ds-saved"), and the
// data summary the server page passes in.

import { useEffect, useState } from "react";
import { useLightbox } from "@/components/Lightbox";
import { readSavedPaths, readStoredProvider } from "@/components/storage";
import { PROVIDER_EVENT } from "@/components/Chat";
import { setCollapsed, setTheme, usePrefs, type Theme } from "@/components/prefs";
import { baseUrlOf } from "@/lib/provider-defaults";
import { agentSnippets } from "@/lib/agent-snippets";
import { SnippetCopyButton } from "@/components/CopyButton";

export interface SettingsStats {
  /** The checkout's folder name, never its absolute path. */
  repo: string;
  systems: number | null;
  refero: number | null;
  audit: string | null;
}

interface Cfg {
  api: string;
  base_url: string;
  api_key: string;
  key_header: string;
  model: string;
  name: string;
}

const EMPTY: Cfg = { api: "anthropic", base_url: "", api_key: "", key_header: "", model: "", name: "" };

const readProvider = (): Cfg => ({ ...EMPTY, ...readStoredProvider() });

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

export function Settings({ stats }: { stats: SettingsStats }) {
  const lb = useLightbox();
  const [cfg, setCfg] = useState<Cfg>(EMPTY);
  const { theme, collapsed } = usePrefs();
  const [saved, setSaved] = useState<string[]>([]);
  const [models, setModels] = useState<ModelHit[]>([]);
  const [status, setStatus] = useState("");
  const [warn, setWarn] = useState(false);
  const [testing, setTesting] = useState(false);
  const [envNote, setEnvNote] = useState("");
  const [origin, setOrigin] = useState("");

  useEffect(() => {
    setOrigin(window.location.origin);
    setCfg(readProvider());
    setSaved(readSavedPaths());
    fetch("/api/status")
      .then((r) => (r.ok ? r.json() : null))
      .then((d) => setEnvNote(d?.envProvider ? " The server also has its own key configured." : ""))
      .catch(() => {});
  }, []);

  const onField =
    (k: keyof Cfg) => (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) =>
      setCfg((c) => ({ ...c, [k]: e.target.value }));

  const test = async () => {
    if (!cfg.api_key) {
      setWarn(true);
      setStatus("Fill the API key first; the test uses this form's key, not the server's.");
      return;
    }
    setTesting(true);
    setWarn(false);
    setStatus("Testing…");
    try {
      const r = await fetch("/api/models", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ provider: { ...cfg, base_url: baseUrlOf(cfg) } }),
      });
      const d = await r.json();
      if (d?.ok) {
        const list: ModelHit[] = Array.isArray(d.models) ? d.models : [];
        setModels(list);
        setStatus(list.length ? `Connected: ${list.length} models found.` : `Connected. ${d.note || "Type the model name."}`);
      } else {
        setWarn(true);
        setStatus(d?.error === "no_provider" ? "Fill the base URL and API key first." : d?.error || "Test failed.");
      }
    } catch {
      setWarn(true);
      setStatus("No answer from the server.");
    }
    setTesting(false);
  };

  const save = () => {
    if (!cfg.api_key || !cfg.model.trim()) {
      setWarn(true);
      setStatus("The chat needs an API key and a model; fill both before saving.");
      return;
    }
    const out: Record<string, string> = {
      api: cfg.api,
      base_url: baseUrlOf(cfg),
      api_key: cfg.api_key,
      model: cfg.model.trim(),
    };
    if (cfg.key_header.trim()) out.key_header = cfg.key_header.trim();
    if (cfg.name.trim()) out.name = cfg.name.trim();
    try {
      localStorage.setItem("ds-provider", JSON.stringify(out));
    } catch {}
    window.dispatchEvent(new Event(PROVIDER_EVENT));
    setWarn(false);
    setStatus(`Saved: ${cfg.name.trim() || cfg.api} · ${cfg.model.trim()}`);
  };

  const clearProvider = () => {
    try {
      localStorage.removeItem("ds-provider");
    } catch {}
    window.dispatchEvent(new Event(PROVIDER_EVENT));
    setCfg((c) => ({ ...c, api_key: "" }));
    setWarn(false);
    setStatus("Removed the saved provider.");
  };

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
        <p className="sub">Choices here are saved in this browser and apply to every page of the app.</p>
      </div>

      <div className="prefs">
        <fieldset className="pref" id="model-provider">
          <legend className="pref-name">Model provider</legend>
          <p className="pref-help">The chat&rsquo;s brain: which wire format, endpoint, key and model it talks to.</p>
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
              <input value={cfg.api_key} onChange={onField("api_key")} type="password" autoComplete="off" spellCheck={false} placeholder="sk-…" />
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
                  onClick={() => setCfg((c) => ({ ...c, model: m.id }))}
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
            <button className="btn" type="button" onClick={test} disabled={testing}>
              {testing ? "Testing…" : "Test"}
            </button>
            <button className="btn primary" type="button" onClick={save}>
              Save
            </button>
            <button className="btn" type="button" onClick={clearProvider}>
              Clear
            </button>
          </div>
          <p className="pref-note">
            Stored in this browser only. With no key here the server falls back to its own configured model.{envNote}
          </p>
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
