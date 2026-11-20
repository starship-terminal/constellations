"use client";
import Link from "next/link";
import { usePathname, useRouter, useSearchParams } from "next/navigation";
import { Suspense, useEffect, useRef, useState, type ReactNode } from "react";
import {
  Grid2X2,
  BookOpen,
  BarChart3,
  Laptop,
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
import { createInFlightGuard } from "./recent-guard";
export function Mark() {
  return (
    <>
      <img
        className="brand-mark"
        src="/brand/flat/favicon.svg"
        width="26"
        height="26"
        alt=""
      />
      <img
        className="brand-mark-glass"
        src="/brand/glass/icon-192.png"
        width="26"
        height="26"
        alt=""
      />
    </>
  );
}
export function CatalogNavigation({ onNavigate }: { onNavigate: () => void }) {
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
        <span className="nav-label">Gallery</span>
      </Link>
      <Link
        className={`nav-link ${path === "/library" && platform === "web" ? "active" : ""}`}
        href="/library?platform=web"
      >
        <Monitor size={20} />
        <span className="nav-label">Web apps</span>
      </Link>
      <Link
        className={`nav-link ${path === "/library" && platform === "mobile" ? "active" : ""}`}
        href="/library?platform=mobile"
      >
        <Smartphone size={20} />
        <span className="nav-label">iOS apps</span>
      </Link>
      <Link
        className={`nav-link ${path === "/library" && platform === "desktop" ? "active" : ""}`}
        href="/library?platform=desktop"
      >
        <Laptop size={20} />
        <span className="nav-label">Desktop apps</span>
      </Link>
      <Link
        className={`nav-link ${path.startsWith("/styles") ? "active" : ""}`}
        href="/styles"
      >
        <Palette size={20} />
        <span className="nav-label">Styles</span>
      </Link>
      <Link
        className={`nav-link ${path.startsWith("/collections") ? "active" : ""}`}
        href="/collections"
      >
        <Bookmark size={20} />
        <span className="nav-label">Bookmarks</span>
      </Link>
      <Link
        className={`nav-link ${path.startsWith("/docs") ? "active" : ""}`}
        href="/docs"
      >
        <BookOpen size={20} />
        <span className="nav-label">Documents</span>
      </Link>
      <Link
        className={`nav-link ${path.startsWith("/scorecard") ? "active" : ""}`}
        href="/scorecard"
      >
        <BarChart3 size={20} />
        <span className="nav-label">Scorecard</span>
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
const SIDEBAR_KEY = "studio-sidebar-collapsed";
/** Runs before paint, like the theme script: a collapsed sidebar is laid out
 * collapsed from the first frame instead of opening and then closing. */
export const sidebarInitScript = `(function(){try{
if(localStorage.getItem('${SIDEBAR_KEY}')==='true')document.documentElement.dataset.sidebar='collapsed';
}catch(e){}})();`;
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
    // sidebarInitScript already collapsed the layout before paint; this only
    // syncs the toggle's label and icon.
    setCollapsed(document.documentElement.dataset.sidebar === "collapsed");
  }, []);
  const [showAllHistory, setShowAllHistory] = useState(false),
    [showArchived, setShowArchived] = useState(false);
  // null until the first reply, so "Your research will appear here." never
  // flashes for someone who has research.
  const [history, setHistory] = useState<Conversation[] | null>(null),
    [mobile, setMobile] = useState(false),
    [editing, setEditing] = useState<Conversation | null>(null),
    [title, setTitle] = useState(""),
    [error, setError] = useState(""),
    [renameError, setRenameError] = useState(""),
    [historyFailed, setHistoryFailed] = useState(false);
  // Only the newest history request may update the list or its failure state.
  const historyRequest = useRef(0);
  // A tab switch fires focus and visibilitychange together, and the first
  // focus can land while the mount fetch is still running: those join the
  // fetch already in flight. Once it settles, the next event fetches again.
  const inFlight = useRef(createInFlightGuard());
  function reloadWhenShown() {
    if (document.visibilityState === "visible") reloadIfIdle();
  }
  function reloadIfIdle() {
    if (!inFlight.current.busy()) reload();
  }
  function reload() {
    const request = ++historyRequest.current;
    const done = inFlight.current.start();
    api("/api/conversations")
      .then((d) => {
        if (request !== historyRequest.current) return;
        setHistory(d.conversations || []);
        setHistoryFailed(false);
      })
      .catch(() => {
        if (request === historyRequest.current) setHistoryFailed(true);
      })
      .finally(done);
  }
  // Pages that change research dispatch "research-history"; moving between
  // pages changes nothing, so it does not refetch. Research created or
  // renamed in another tab or window arrives when this one is shown or
  // focused again.
  useEffect(() => {
    reload();
    window.addEventListener("research-history", reload);
    document.addEventListener("visibilitychange", reloadWhenShown);
    window.addEventListener("focus", reloadIfIdle);
    return () => {
      window.removeEventListener("research-history", reload);
      document.removeEventListener("visibilitychange", reloadWhenShown);
      window.removeEventListener("focus", reloadIfIdle);
    };
  }, []);
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
      // Shown inside the dialog: a toast behind the modal is inert and unread.
      setRenameError((e as Error).message);
    }
  }
  // Close open history menus on an outside click or Escape, and the mobile
  // navigation on Escape, returning focus to what opened it.
  const menuButton = useRef<HTMLButtonElement>(null);
  useEffect(() => {
    const menus = () =>
      document.querySelectorAll<HTMLDetailsElement>(
        "details.history-menu[open]",
      );
    const down = (event: PointerEvent) => {
      for (const menu of menus())
        if (!menu.contains(event.target as Node)) menu.open = false;
    };
    const key = (event: KeyboardEvent) => {
      if (event.key !== "Escape" || event.defaultPrevented) return;
      const open = [...menus()];
      if (open.length) {
        for (const menu of open) {
          menu.open = false;
          menu.querySelector("summary")?.focus();
        }
        return;
      }
      if (mobile) {
        setMobile(false);
        menuButton.current?.focus();
      }
    };
    document.addEventListener("pointerdown", down);
    document.addEventListener("keydown", key);
    return () => {
      document.removeEventListener("pointerdown", down);
      document.removeEventListener("keydown", key);
    };
  }, [mobile]);
  const closeMenu = (target: EventTarget) =>
    (
      (target as HTMLElement).closest("details") as HTMLDetailsElement | null
    )?.removeAttribute("open");
  return (
    <div className={`app-shell ${collapsed ? "sidebar-collapsed" : ""}`}>
      <button
        className="desktop-sidebar-toggle icon-button"
        aria-label={collapsed ? "Expand navigation" : "Collapse navigation"}
        onClick={() => {
          setCollapsed(!collapsed);
          if (collapsed) delete document.documentElement.dataset.sidebar;
          else document.documentElement.dataset.sidebar = "collapsed";
          localStorage.setItem(SIDEBAR_KEY, String(!collapsed));
        }}
      >
        {collapsed ? <PanelLeftOpen size={18} /> : <PanelLeftClose size={18} />}
      </button>
      <button
        ref={menuButton}
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
          <span>Constellations</span>
        </Link>
        <Link href="/" className="new-research">
          <Plus size={22} />
          <span className="nav-label">New research</span>
        </Link>
        <Suspense fallback={null}>
          <CatalogNavigation onNavigate={() => setMobile(false)} />
        </Suspense>
        <div className="history-heading">
          <span>{showArchived ? "Archived research" : "History"}</span>
          {(showArchived || history?.some((c) => c.archived)) && (
            <button
              className="text-button"
              onClick={() => setShowArchived(!showArchived)}
            >
              {showArchived ? "Back" : "Archived"}
            </button>
          )}
        </div>
        <div className="history-list">
          {(history ?? [])
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
                      onClick={(event) => {
                        closeMenu(event.currentTarget);
                        setEditing(c);
                        setTitle(c.title);
                        setRenameError("");
                      }}
                    >
                      <Pencil size={14} />
                      Rename
                    </button>
                    <button
                      onClick={async (event) => {
                        closeMenu(event.currentTarget);
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
          {(history ?? []).filter((c) => !!c.archived === showArchived).length >
            18 && (
            <button
              className="text-button history-more"
              onClick={() => setShowAllHistory(!showAllHistory)}
            >
              {showAllHistory ? "Show fewer" : "Show all research"}
            </button>
          )}
          {historyFailed ? (
            <p className="history-empty" role="alert">
              Could not load your research.{" "}
              <button className="text-button" onClick={reload}>
                Try again
              </button>
            </p>
          ) : (
            history?.filter((c) => !!c.archived === showArchived).length ===
              0 && (
              <p className="history-empty">Your research will appear here.</p>
            )
          )}
        </div>
        <div className="sidebar-bottom">
          <Link
            className={`nav-link ${path === "/settings" ? "active" : ""}`}
            href="/settings"
          >
            <Settings size={18} />
            <span className="nav-label">Settings</span>
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
          {renameError && (
            <p className="error-text" role="alert">
              {renameError}
            </p>
          )}
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
