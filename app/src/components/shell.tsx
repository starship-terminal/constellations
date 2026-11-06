"use client";
import Link from "next/link";
import { usePathname, useRouter, useSearchParams } from "next/navigation";
import { Suspense, useEffect, useRef, useState, type ReactNode } from "react";
import {
  Grid2X2,
  BookOpen,
  BarChart3,
  Monitor,
  Smartphone,
  Bookmark,
  Palette,
  Plus,
  Settings,
  PanelLeftClose,
  PanelLeftOpen,
  MoreHorizontal,
  Archive,
  Pencil,
  ArchiveRestore,
} from "lucide-react";
import { api, Modal } from "./shared";
export function Mark() {
  return (
    <>
      <svg
        className="brand-mark"
        width="26"
        height="26"
        aria-hidden="true"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 64 64"
      >
        <defs>
          <clipPath id="ds-mark-clip">
            <rect width="64" height="64" rx="14" />
          </clipPath>
        </defs>
        <rect width="64" height="64" rx="14" fill="#08090a" />
        <g clipPath="url(#ds-mark-clip)">
          <polygon
            points="-6.00,28.00 21.31,28.00 16.69,36.00 -6.00,36.00"
            fill="#FFFFFF"
          />
          <polygon
            className="mark-stripe"
            points="33.80,22.99 70.00,8.00 70.00,17.60 35.88,26.60"
            fill="#FF3B30"
          />
          <polygon
            className="mark-stripe"
            points="35.88,26.60 70.00,17.60 70.00,27.20 37.96,30.20"
            fill="#FF9500"
          />
          <polygon
            className="mark-stripe"
            points="37.96,30.20 70.00,27.20 70.00,36.80 40.04,33.80"
            fill="#FFD60A"
          />
          <polygon
            className="mark-stripe"
            points="40.04,33.80 70.00,36.80 70.00,46.40 42.12,37.40"
            fill="#34C759"
          />
          <polygon
            className="mark-stripe"
            points="42.12,37.40 70.00,46.40 70.00,56.00 44.20,41.01"
            fill="#0A84FF"
          />
          <polygon
            points="29.00,14.68 49.00,49.32 9.00,49.32"
            fill="#FFFFFF"
            stroke="#08090a"
            strokeWidth="3"
            strokeLinejoin="round"
          />
        </g>
      </svg>
      <img
        className="brand-mark-glass"
        src="/brand/glass/favicon-48.png"
        width="26"
        height="26"
        alt=""
        aria-hidden="true"
      />
    </>
  );
}
function CatalogNavigation({ onNavigate }: { onNavigate: () => void }) {
  const path = usePathname();
  const params = useSearchParams();
  const platform = params.get("platform");
  return (
    <nav
      aria-label="Main navigation"
      onClick={(event) => {
        if ((event.target as Element).closest("a")) onNavigate();
      }}
    >
      <Link
        className={`nav-link ${path.startsWith("/library") && !platform ? "active" : ""}`}
        href="/library"
      >
        <Grid2X2 size={20} />
        Gallery
      </Link>
      <Link
        className={`nav-link ${path === "/library" && platform === "web" ? "active" : ""}`}
        href="/library?platform=web"
      >
        <Monitor size={20} />
        Web apps
      </Link>
      <Link
        className={`nav-link ${path === "/library" && platform === "mobile" ? "active" : ""}`}
        href="/library?platform=mobile"
      >
        <Smartphone size={20} />
        iOS apps
      </Link>
      <Link
        className={`nav-link ${path.startsWith("/styles") ? "active" : ""}`}
        href="/styles"
      >
        <Palette size={20} />
        Styles
      </Link>
      <Link
        className={`nav-link ${path.startsWith("/collections") ? "active" : ""}`}
        href="/collections"
      >
        <Bookmark size={20} />
        Bookmarks
      </Link>
      <Link
        className={`nav-link ${path.startsWith("/docs") ? "active" : ""}`}
        href="/docs"
      >
        <BookOpen size={20} />
        Documents
      </Link>
      <Link
        className={`nav-link ${path.startsWith("/scorecard") ? "active" : ""}`}
        href="/scorecard"
      >
        <BarChart3 size={20} />
        Scorecard
      </Link>
    </nav>
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
  const scene = useRef<HTMLElement | null>(null);
  useEffect(() => {
    const element = scene.current;
    if (!element || matchMedia("(prefers-reduced-motion: reduce)").matches)
      return;
    const animation = element.animate(
      [
        { opacity: 0, translate: "0 8px" },
        { opacity: 1, translate: "0 0" },
      ],
      { duration: 180, easing: "cubic-bezier(0.22, 1, 0.36, 1)" },
    );
    return () => animation.cancel();
  }, [path]);
  const [collapsed, setCollapsed] = useState(false);
  useEffect(() => {
    setCollapsed(localStorage.getItem("studio-sidebar-collapsed") === "true");
  }, []);
  const [showAllHistory, setShowAllHistory] = useState(false),
    [showArchived, setShowArchived] = useState(false);
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
    <div className={`app-shell ${collapsed ? "sidebar-collapsed" : ""}`}>
      <button
        className="desktop-sidebar-toggle icon-button"
        aria-label={collapsed ? "Expand navigation" : "Collapse navigation"}
        onClick={() => {
          setCollapsed(!collapsed);
          localStorage.setItem("studio-sidebar-collapsed", String(!collapsed));
        }}
      >
        {collapsed ? <PanelLeftOpen size={18} /> : <PanelLeftClose size={18} />}
      </button>
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
          <span>Design Studio</span>
        </Link>
        <Link href="/" className="new-research">
          <Plus size={22} />
          New research
        </Link>
        <Suspense fallback={null}>
          <CatalogNavigation onNavigate={() => setMobile(false)} />
        </Suspense>
        <div className="history-heading">
          <span>{showArchived ? "Archived research" : "History"}</span>
          {(showArchived || history.some((c) => c.archived)) && (
            <button
              className="text-button"
              onClick={() => setShowArchived(!showArchived)}
            >
              {showArchived ? "Back" : "Archived"}
            </button>
          )}
        </div>
        <div className="history-list">
          {history
            .filter((x) => !!x.archived === showArchived)
            .slice(0, showAllHistory ? undefined : 18)
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
                            body: JSON.stringify({ archived: !c.archived }),
                          });
                          reload();
                          if (!c.archived && path === `/research/${c.id}`)
                            router.push("/");
                        } catch (e) {
                          setError((e as Error).message);
                        }
                      }}
                    >
                      {c.archived ? (
                        <ArchiveRestore size={14} />
                      ) : (
                        <Archive size={14} />
                      )}
                      {c.archived ? "Restore" : "Archive"}
                    </button>
                  </div>
                </details>
              </div>
            ))}
          {history.filter((c) => !!c.archived === showArchived).length > 18 && (
            <button
              className="text-button history-more"
              onClick={() => setShowAllHistory(!showAllHistory)}
            >
              {showAllHistory ? "Show fewer" : "Show all research"}
            </button>
          )}
          {history.filter((c) => !!c.archived === showArchived).length ===
            0 && (
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
        </div>
      </aside>
      <main ref={scene} className="main-content" id="main-content">
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
