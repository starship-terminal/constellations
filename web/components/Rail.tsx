"use client";

// The site's left rail: wordmark, grouped nav, and the foot actions (chat,
// settings, theme, collapse). Collapsed it pins to an icon strip that still
// opens on hover/focus (CSS-side, the old ds-nav behaviour).
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useChat } from "@/components/Chat";
import { setCollapsed, setTheme, usePrefs } from "@/components/prefs";

const I = (d: React.ReactNode) => (
  <svg className="nav-ic" width="17" height="17" viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round">
    {d}
  </svg>
);
const icons = {
  home: I(<path d="M2 6.5 8 1.5l6 5V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1z" />),
  gallery: I(<><rect x="1.5" y="1.5" width="5.6" height="5.6" rx="1.4"/><rect x="8.9" y="1.5" width="5.6" height="5.6" rx="1.4"/><rect x="1.5" y="8.9" width="5.6" height="5.6" rx="1.4"/><rect x="8.9" y="8.9" width="5.6" height="5.6" rx="1.4"/></>),
  refero: I(<path d="M8 1.8l1.5 3.9 4.2.3-3.2 2.7 1 4.1L8 10.4l-3.5 2.4 1-4.1-3.2-2.7 4.2-.3z" />),
  scorecard: I(<path d="M2 14V8.5M6 14V4.5M10 14v-6M14 14V2.5" />),
  docs: I(<><path d="M3 2.5h8a2 2 0 0 1 2 2V13a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/><path d="M5.5 5.5h5M5.5 8h5M5.5 10.5h3"/></>),
  settings: I(<><path d="M2 4.5h7M13 4.5h1M2 11.5h1M7 11.5h7"/><circle cx="11" cy="4.5" r="2"/><circle cx="5" cy="11.5" r="2"/></>),
  chat: I(<path d="M2.5 2.5h11v9h-6l-3 3v-3h-2z" />),
};

const NAV = [
  { href: "/", label: "Home", icon: icons.home, match: (p: string) => p === "/" },
  { href: "/gallery", label: "Gallery", icon: icons.gallery, match: (p: string) => p.startsWith("/gallery") },
  { href: "/refero", label: "Refero", icon: icons.refero, match: (p: string) => p.startsWith("/refero") },
  { href: "/scorecard", label: "Scorecard", icon: icons.scorecard, match: (p: string) => p.startsWith("/scorecard") },
  { href: "/docs", label: "Docs", icon: icons.docs, match: (p: string) => p.startsWith("/docs") },
];

function Mark() {
  return (
    <svg className="mark" width="18" height="18" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
      <defs><clipPath id="ds-mark-clip"><rect width="64" height="64" rx="14" /></clipPath></defs>
      <rect width="64" height="64" rx="14" fill="#08090a" />
      <g clipPath="url(#ds-mark-clip)">
        <polygon points="-6.00,28.00 21.31,28.00 16.69,36.00 -6.00,36.00" fill="#FFFFFF" />
        <polygon points="33.80,22.99 70.00,8.00 70.00,17.60 35.88,26.60" fill="#FF3B30" />
        <polygon points="35.88,26.60 70.00,17.60 70.00,27.20 37.96,30.20" fill="#FF9500" />
        <polygon points="37.96,30.20 70.00,27.20 70.00,36.80 40.04,33.80" fill="#FFD60A" />
        <polygon points="40.04,33.80 70.00,36.80 70.00,46.40 42.12,37.40" fill="#34C759" />
        <polygon points="42.12,37.40 70.00,46.40 70.00,56.00 44.20,41.01" fill="#0A84FF" />
        <polygon points="29.00,14.68 49.00,49.32 9.00,49.32" fill="#FFFFFF" stroke="#08090a" strokeWidth="3" strokeLinejoin="round" />
      </g>
    </svg>
  );
}

export function Rail() {
  const pathname = usePathname();
  const chat = useChat();

  const { resolved, collapsed } = usePrefs();

  const toggleTheme = () => setTheme(resolved === "dark" ? "light" : "dark");

  const toggleNav = (e: React.MouseEvent<HTMLButtonElement>) => {
    setCollapsed(!collapsed);
    if (e.detail) e.currentTarget.blur();
  };

  return (
    <header className="bar">
      <Link className="brand" href="/" aria-label="Design systems">
        <Mark />
        <span>Design systems</span>
      </Link>
      <div className="bar-body">
        <nav className="site-nav" aria-label="Site">
          {NAV.map((n) => (
            <Link key={n.href} href={n.href} aria-current={n.match(pathname) ? "page" : undefined}>
              {n.icon}
              <span>{n.label}</span>
            </Link>
          ))}
        </nav>
      </div>
      <span className="bar-foot">
        <button className="icon-btn" type="button" onClick={() => chat.open()} aria-label="Open the librarian chat" title="Ask the librarian">
          {icons.chat}
          <span className="lbl">Chat</span>
        </button>
        <Link className="icon-btn" href="/settings" aria-label="Settings" title="Settings" aria-current={pathname === "/settings" ? "page" : undefined}>
          {icons.settings}
          <span className="lbl">Settings</span>
        </Link>
        <button id="theme" className="icon-btn" type="button" aria-label="Toggle colour theme" title="Toggle theme" onClick={toggleTheme}>
          <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">
            <path d="M8 1.5a6.5 6.5 0 1 0 0 13z" fill="currentColor" />
            <circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" strokeWidth="1.4" />
          </svg>
          <span className="lbl">Theme</span>
        </button>
        <button id="nav-toggle" className="icon-btn" type="button" aria-pressed={collapsed} title={collapsed ? "Expand sidebar" : "Collapse sidebar"} onClick={toggleNav}>
          <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round">
            <path d="M9.5 3.5 5 8l4.5 4.5M13.5 3.5 9 8l4.5 4.5" />
          </svg>
          <span className="lbl">Collapse</span>
        </button>
      </span>
    </header>
  );
}
