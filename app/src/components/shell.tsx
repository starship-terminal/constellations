"use client";
import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { useEffect, useState, type ReactNode } from "react";
import {
  ArrowUpRight,
  BookOpen,
  Folder,
  Plus,
  Settings,
  PanelLeftClose,
  PanelLeftOpen,
  MoreHorizontal,
  Search,
  Archive,
  Pencil,
} from "lucide-react";
import { api, Modal } from "./shared";
export function Mark() {
  return (
    <span className="brand-mark" aria-hidden="true">
      <span />
      <span />
      <span />
    </span>
  );
}
export function StandaloneHeader({ crumb }: { crumb?: string }) {
  return (
    <header className="standalone-header">
      <Link href="/" className="brand">
        <Mark />
        <span>Studio</span>
      </Link>
      <span className="header-slash">/</span>
      <Link href="/styles">Styles</Link>
      {crumb && (
        <>
          <span className="header-slash">/</span>
          <span className="muted truncate">{crumb}</span>
        </>
      )}
      <Link className="pill small header-home" href="/">
        Back to research <ArrowUpRight size={14} />
      </Link>
    </header>
  );
}
interface Conversation {
  id: string;
  title: string;
  updatedAt?: string;
  archived?: boolean;
}
export function AppShell({ children }: { children: ReactNode }) {
  const path = usePathname(),
    router = useRouter();
  const [history, setHistory] = useState<Conversation[]>([]),
    [mobile, setMobile] = useState(false),
    [editing, setEditing] = useState<Conversation | null>(null),
    [title, setTitle] = useState(""),
    [error, setError] = useState("");
  function reload() {
    api("/api/conversations")
      .then((d) => setHistory(d.conversations || []))
      .catch(() => {});
  }
  useEffect(() => {
    reload();
    window.addEventListener("research-history", reload);
    return () => window.removeEventListener("research-history", reload);
  }, [path]);
  useEffect(() => {
    setMobile(false);
  }, [path]);
  if (path.startsWith("/styles")) return <>{children}</>;
  async function rename() {
    if (!editing || !title.trim()) return;
    try {
      await api(`/api/conversations/${editing.id}`, {
        method: "PATCH",
        body: JSON.stringify({ title: title.trim() }),
      });
      setEditing(null);
      reload();
    } catch (e) {
      setError((e as Error).message);
    }
  }
  return (
    <div className="app-shell">
      <button
        className="mobile-menu icon-button"
        onClick={() => setMobile((v) => !v)}
        aria-label={mobile ? "Close navigation" : "Open navigation"}
        aria-expanded={mobile}
        aria-controls="workspace-sidebar"
      >
        {mobile ? <PanelLeftClose size={21} /> : <PanelLeftOpen size={21} />}
      </button>
      {mobile && (
        <button
          className="sidebar-scrim"
          aria-label="Close navigation"
          onClick={() => setMobile(false)}
        />
      )}
      <aside
        id="workspace-sidebar"
        className={`sidebar ${mobile ? "mobile-open" : ""}`}
      >
        <Link href="/" className="brand">
          <Mark />
          <span>Studio</span>
          <span className="brand-sub">Research library</span>
        </Link>
        <Link href="/" className="new-research">
          <Plus size={17} />
          New research
        </Link>
        <nav aria-label="Main navigation">
          <Link
            className={`nav-link ${path === "/library" ? "active" : ""}`}
            href="/library"
          >
            <BookOpen size={18} />
            Library
          </Link>
          <a
            className="nav-link"
            href="/styles"
            target="_blank"
            rel="noreferrer"
          >
            <Search size={18} />
            Styles
            <ArrowUpRight className="nav-trailing" size={15} />
          </a>
          <Link
            className={`nav-link ${path.startsWith("/collections") ? "active" : ""}`}
            href="/collections"
          >
            <Folder size={18} />
            Collections
          </Link>
        </nav>
        <div className="history-heading">Recent research</div>
        <div className="history-list">
          {history
            .filter((x) => !x.archived)
            .slice(0, 18)
            .map((c) => (
              <div
                key={c.id}
                className={`history-row ${path === `/research/${c.id}` ? "current" : ""}`}
              >
                <Link href={`/research/${c.id}`} title={c.title}>
                  {c.title || "Untitled research"}
                </Link>
                <details className="history-menu">
                  <summary aria-label={`Options for ${c.title}`}>
                    <MoreHorizontal size={16} />
                  </summary>
                  <div>
                    <button
                      onClick={() => {
                        setEditing(c);
                        setTitle(c.title);
                      }}
                    >
                      <Pencil size={14} />
                      Rename
                    </button>
                    <button
                      onClick={async () => {
                        try {
                          await api(`/api/conversations/${c.id}`, {
                            method: "PATCH",
                            body: JSON.stringify({ archived: true }),
                          });
                          reload();
                          if (path === `/research/${c.id}`) router.push("/");
                        } catch (e) {
                          setError((e as Error).message);
                        }
                      }}
                    >
                      <Archive size={14} />
                      Archive
                    </button>
                  </div>
                </details>
              </div>
            ))}
          {history.length === 0 && (
            <p className="history-empty">Your research will appear here.</p>
          )}
        </div>
        <div className="sidebar-bottom">
          <Link
            className={`nav-link ${path === "/settings" ? "active" : ""}`}
            href="/settings"
          >
            <Settings size={18} />
            Settings
          </Link>
          <div className="workspace-label">
            <span className="workspace-avatar">K</span>
            <div>
              Personal workspace<small>Built for a curious eye</small>
            </div>
          </div>
        </div>
      </aside>
      <main className="main-content" id="main-content">
        {children}
      </main>
      <Modal
        open={!!editing}
        onOpenChange={(v) => {
          if (!v) setEditing(null);
        }}
        title="Rename research"
      >
        <form
          onSubmit={(e) => {
            e.preventDefault();
            rename();
          }}
          className="dialog-form"
        >
          <label>
            Research title
            <input
              autoFocus
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              required
            />
          </label>
          <button className="primary" type="submit">
            Save title
          </button>
        </form>
      </Modal>
      {error && (
        <div className="toast" role="alert">
          {error}
          <button onClick={() => setError("")}>Dismiss</button>
        </div>
      )}
    </div>
  );
}
